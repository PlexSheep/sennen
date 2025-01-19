from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class FuriganaElementType(Enum):
    Kanji = auto()
    Kana = auto()


@dataclass
class FuriganaElement:
    text: str
    type: FuriganaElementType
    reading: str | None = None  # Only populated for KANJI type

    def to_dict(self) -> dict:
        base = {
            "text": self.text,
            "type": self.type.name.lower()
        }
        if self.reading is not None:
            base["reading"] = self.reading
        return base


@dataclass
class Furigana:
    base: str
    elements: List[FuriganaElement]

    def __init__(self, raw: str, elements: List[FuriganaElement]) -> None:
        self.elements = elements
        self.base = raw

    def to_dict_list(self) -> List[dict]:
        return  [e.to_dict() for e in self.elements]

@dataclass
class Reading:
    text: str
    common: bool = False

    def __str__(self) -> str:
        return self.text


@dataclass
class Meaning:
    text: str
    common: bool = False

    def __str__(self) -> str:
        return self.text
