import json
import os
import random
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

from .parse.kanji import Kanji, KanjiParser
from .parse.word import Word, WordParser

MAGIC_PRIME_NUMBER: int = 104729


class SiteGenerator:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir.absolute()
        self.site_dir = self.data_dir / "site"
        self.api_dir = self.site_dir / "api" / "v1"
        self.api_dir_daily = self.api_dir / "daily"
        self.sources_dir = self.data_dir / "sources"
        self.ressources_dir = self.data_dir / "ressources"
        self.cleanup()
        self.make_dirs()
        self.load_sources()

    def make_dirs(self):
        self.ressources_dir.mkdir(parents=True, exist_ok=True)
        self.site_dir.mkdir(parents=True, exist_ok=True)
        self.api_dir.mkdir(parents=True, exist_ok=True)
        self.api_dir_daily.mkdir(parents=True, exist_ok=True)

    def cleanup(self):
        recursive_remove(self.site_dir)

    def load_sources(self):
        print("(i) Loading kanji data...")
        self.kanjidic = KanjiParser(self.sources_dir / "kanjidic.xml")
        self.all_kanji = self.kanjidic.get_all_kanji()
        print(f"(i) Loaded {len(self.all_kanji)} kanji")

        print("(i) Loading word data...")
        self.worddict = WordParser(self.sources_dir / "jmdict.xml")
        self.all_words = self.worddict.get_all_words()
        print(f"(i) Loaded {len(self.all_words)} words")

        print("(i) Building kanji-word index...")
        self.kanji_word_index = self.build_kanji_word_index()
        print(f"(i) Index built with {len(self.kanji_word_index)} kanji entries")

    def build_kanji_word_index(self) -> Dict[Kanji, List[Word]]:
        """Build an index mapping kanji to words containing them."""
        index = defaultdict(list)
        for word in self.all_words:
            # For each writing of the word
            for writing in word.writings:
                # For each character in the writing
                for char in writing.base:
                    index[char].append(word)
        return index

    def seed_from_date(self, date: datetime) -> int:
        date_int = int(date.strftime("%Y%m%d"))
        return date_int * MAGIC_PRIME_NUMBER

    def select_kanji_for_date(self, date: datetime, all_kanji: list) -> Kanji:
        """
        Select a kanji for a specific date.
        Uses the date as a seed to ensure consistent selection.
        """
        # Use date as seed for selection
        rng = random.Random(self.seed_from_date(date))
        kanji = rng.choice(all_kanji)
        return kanji

    def select_word_for_date(
        self, date: datetime, kanji: Kanji, all_words: list
    ) -> Word:
        """Select a word for a specific date that contains the daily kanji if possible."""
        rng = random.Random(self.seed_from_date(date))

        # Get words containing this kanji from our index
        kanji_words = self.kanji_word_index.get(kanji, [])

        # If we found words with today's kanji, randomly select one
        # Otherwise, select any word
        word = rng.choice(kanji_words) if kanji_words else rng.choice(all_words)
        return word

    def generate_daily(self, start_date: datetime, num_days: int):
        print("(i) generating daily contents...")

        print(f"(i) Generating {num_days} days of content...")
        for i in range(num_days):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime("%Y-%m-%d")

            kanji = self.select_kanji_for_date(current_date, self.all_kanji)
            word = self.select_word_for_date(current_date, kanji, self.all_words)
            daily_data = {
                "date": date_str,
                "kanji": kanji.to_dict(),
                "word": word.to_dict(),
            }

            output_file = self.api_dir_daily / f"{date_str}.json"
            with output_file.open("w", encoding="utf-8") as f:
                json.dump(daily_data, f, ensure_ascii=False, indent=2)

            p = (float(i) / float(num_days) * 100)
            if p % 5 == 0:  # Progress indicator
                print(f"(i) Generated {p:.02f} % of the days...")

        print("(i) Generation of daily contents complete.")

    def link_ressources(self):
        for ressource in self.ressources_dir.iterdir():
            os.symlink(
                self.ressources_dir / ressource, self.site_dir / ressource.name
            )

    def generate_site(self, start_date: datetime, num_days: int):
        print("(i) Generating site...")

        self.generate_daily(start_date, num_days)
        self.link_ressources()

        print(
            f"Generation of the site complete. Files saved in {self.site_dir}"
        )


def recursive_remove(path: Path):
    """basically just `rm -r $dir`"""
    if not path.exists():
        return
    if not path.is_dir():
        os.remove(path)
        return
    if path.is_symlink():
        os.unlink(path)
        return
    for item in path.iterdir():
        if item.is_dir():
            recursive_remove(item)
        else:
            item.unlink()
    path.rmdir()
