import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .common import (
    Furigana,
    FuriganaElement,
    FuriganaElementType,
    Meaning,
    Reading,
)


@dataclass
class Word:
    id: str  # ent_seq
    writings: List[Furigana]  # keb elements
    readings: List[Reading]  # reb elements with restrictions
    meanings: List[Meaning]  # sense/gloss elements
    pos: List[str]  # part of speech tags

    def is_ok(self) -> bool:
        """
        Check if this word has enough data to be useful for learning.
        Returns True if the word has at least one writing (or reading if no writing)
        and at least one meaning.
        """
        has_writing = len(self.writings) > 0
        has_reading = len(self.readings) > 0
        has_meaning = len(self.meanings) > 0
        return has_writing and has_reading and has_meaning

    def furigana(self) -> Furigana:
        pass

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "furigana": self.furigana().to_dict_list(),
            "writings": self.writings,
            "readings": [
                {"text": str(r.text), "common": r.common}
                for r in self.readings
            ],
            "meanings": [
                {"text": str(m), "common": m.common} for m in self.meanings
            ],
            "pos": self.pos,
        }


class WordParser:
    def __init__(self, xml_path: Path):
        if not xml_path.exists():
            raise FileNotFoundError
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def get_all_words(self) -> List[Word]:
        pass

    def get_words_with_kanji(self, kanji: str) -> List[Word]:
        pass
