import json
from datetime import datetime, timedelta
from os import copy_file_range
from pathlib import Path

from .parse.kanji import KanjiParser


class SiteGenerator:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.site_dir = data_dir / "site"
        self.api_dir = self.site_dir / "api" / "v1"
        self.api_dir_daily = self.api_dir / "daily"
        self.sources_dir = data_dir / "sources"
        self.pages_dir = data_dir / "pages"
        self.cleanup()
        self.make_dirs()
        self.load_sources()

    def make_dirs(self):
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        self.site_dir.mkdir(parents=True, exist_ok=True)
        self.api_dir.mkdir(parents=True, exist_ok=True)
        self.api_dir_daily.mkdir(parents=True, exist_ok=True)

    def cleanup(self):
        recursive_remove(self.site_dir)

    def load_sources(self):
        self.kanjidic = KanjiParser(self.sources_dir / "kanjidic.xml")

    def select_kanji_for_date(self, date: datetime, all_kanji: list) -> dict:
        """
        Select a kanji for a specific date.
        Uses the date as a seed to ensure consistent selection.
        """
        # Use date as seed for selection
        date_int = int(date.strftime("%Y%m%d"))
        index = date_int % len(all_kanji)
        kanji = all_kanji[index]

        return {
            "kanji": kanji.literal,
            "meanings": kanji.meanings,
            "kun_readings": kanji.kun_readings,
            "on_readings": kanji.on_readings,
            "grade": kanji.grade,
            "jlpt": kanji.jlpt,
            "stroke_count": kanji.stroke_count,
            "frequency": kanji.freq,
        }

    def generate_daily(self, start_date: datetime, num_days: int):
        print("(i) generating daily contents...")
        print("(i) Loading kanji data...")
        all_kanji = self.kanjidic.get_all_kanji()

        print(f"(i) Generating {num_days} days of content...")
        for i in range(num_days):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime("%Y-%m-%d")

            daily_data = {
                "date": date_str,
                "kanji": self.select_kanji_for_date(
                    current_date, all_kanji
                ),
            }

            output_file = self.api_dir_daily / f"{date_str}.json"
            with output_file.open("w", encoding="utf-8") as f:
                json.dump(daily_data, f, ensure_ascii=False, indent=2)

            if i % 50 == 0:  # Progress indicator
                print(f"(i) Generated {i} days...")

        print("(i) Generation of daily contents complete.")

    def copy_pages(self):
        for page in self.pages_dir.iterdir():
            page.link_to(self.site_dir / page.name)

    def generate_site(self, start_date: datetime, num_days: int):
        print("(i) Generating site...")

        self.generate_daily(start_date,num_days)
        self.copy_pages()

        print(f"Generation of the site complete. Files saved in {self.site_dir}")

def recursive_remove(dir: Path):
    """basically just `rm -r $dir`"""
    for item in dir.iterdir():
        if item.is_dir():
            recursive_remove(item)
        else:
            item.unlink()
    dir.rmdir()
