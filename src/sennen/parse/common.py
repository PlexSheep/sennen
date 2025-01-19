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
        base = {"text": self.text, "type": self.type.name.lower()}
        if self.reading is not None:
            base["reading"] = self.reading
        return base


@dataclass
class Furigana:
    literal: str
    elements: List[FuriganaElement]

    def __init__(self, raw: str, elements: List[FuriganaElement]) -> None:
        self.elements = elements
        self.literal = raw

    @staticmethod
    def create(writing: str, reading: str):
        return Furigana._create_furigana(writing, reading)

    def to_dict_list(self) -> List[dict]:
        return [e.to_dict() for e in self.elements]

    @staticmethod
    def _create_furigana(text: str, reading: str):
        """Create furigana elements for a writing and its reading"""
        elements: List[FuriganaElement] = []
        text_pos = 0
        reading_pos = 0
        current = []
        current_type = None

        while text_pos < len(text):
            char = text[text_pos]
            is_kana = any(0x3040 <= ord(c) <= 0x30FF for c in char)
            char_type = (
                FuriganaElementType.Kana
                if is_kana
                else FuriganaElementType.Kanji
            )

            # Handle type transitions
            if current_type != char_type and current:
                if current_type is None:
                    raise Exception(
                        "current_type is None although that isn't supposed to happen here"
                    )
                element_text = "".join(current)
                if current_type == FuriganaElementType.Kana:
                    elements.append(
                        FuriganaElement(text=element_text, type=current_type)
                    )
                    reading_pos += len(element_text)
                else:  # Kanji
                    # Find next kana position in text
                    next_kana_pos = text_pos
                    while next_kana_pos < len(text):
                        if any(
                            0x3040 <= ord(c) <= 0x30FF
                            for c in text[next_kana_pos]
                        ):
                            break
                        next_kana_pos += 1

                    # Extract reading for this kanji group
                    kanji_reading = reading[reading_pos:next_kana_pos]
                    elements.append(
                        FuriganaElement(
                            text=element_text,
                            type=current_type,
                            reading=kanji_reading,
                        )
                    )
                    reading_pos = next_kana_pos
                current = []

            current.append(char)
            current_type = char_type
            text_pos += 1

        # Handle the final element
        if current:
            if current_type is None:
                raise Exception(
                    "current_type is None although that isn't supposed to happen here"
                )
            element_text = "".join(current)
            if current_type == FuriganaElementType.Kana:
                elements.append(
                    FuriganaElement(text=element_text, type=current_type)
                )
            else:
                elements.append(
                    FuriganaElement(
                        text=element_text,
                        type=current_type,
                        reading=reading[reading_pos:],
                    )
                )

        return Furigana(text, elements)


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
