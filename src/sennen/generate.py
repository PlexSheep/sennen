import json
from datetime import datetime, timedelta
from pathlib import Path
from .parse.kanji import KanjiParser

class DailyGenerator:
    def __init__(self, data_dir: Path):
        self.kanjidic = KanjiParser(data_dir / "sources" / "kanjidic.xml")
        self.output_dir = data_dir / "generated"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def select_kanji_for_date(self, date: datetime, all_kanji: list) -> dict:
        """
        Select a kanji for a specific date.
        Uses the date as a seed to ensure consistent selection.
        """
        # Use date as seed for selection
        date_int = int(date.strftime('%Y%m%d'))
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
            "frequency": kanji.freq
        }

    def generate_days(self, start_date: datetime, num_days: int):
        print("Loading kanji data...")
        all_kanji = self.kanjidic.get_all_kanji()

        print(f"Generating {num_days} days of content...")
        for i in range(num_days):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime('%Y-%m-%d')

            daily_data = {
                "date": date_str,
                "kanji_of_the_day": self.select_kanji_for_date(current_date, all_kanji)
            }

            output_file = self.output_dir / f"{date_str}.json"
            with output_file.open('w', encoding='utf-8') as f:
                json.dump(daily_data, f, ensure_ascii=False, indent=2)

            if i % 50 == 0:  # Progress indicator
                print(f"Generated {i} days...")

        print(f"Generation complete. Files saved in {self.output_dir}")
