import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from .common import Meaning, Reading


@dataclass
class Kanji:
    literal: str
    meanings: List[Meaning]  # English meanings only for now
    grade: Optional[int]
    jlpt: Optional[int]
    stroke_count: int
    freq: Optional[int]  # Frequency of use ranking
    kun_readings: List[Reading]
    on_readings: List[Reading]

    def is_ok(self) -> bool:
        """
        Check if this kanji has enough data to be useful for learning.
        """
        return (
            len(self.meanings) > 0  # Has at least one meaning
            and (
                len(self.kun_readings) > 0 or len(self.on_readings) > 0
            )  # Has at least one reading
            and self.grade is not None  # Is a grade-level kanji
            and self.jlpt is not None
            and self.freq is not None
        )

    def to_dict(self) -> dict:
        return {
            "kanji": self.literal,
            "meanings": self.meanings,
            "kun_readings": self.kun_readings,
            "on_readings": self.on_readings,
            "grade": self.grade,
            "jlpt": self.jlpt,
            "stroke_count": self.stroke_count,
            "frequency": self.freq,
        }

    def __key(self):
        return self.literal

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Kanji):
            return self.__key() == other.__key()
        return NotImplemented


class KanjiParser:
    def __init__(self, xml_path: Path):
        if not xml_path.exists():
            raise FileNotFoundError
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def __parse_kanji(self, character_element) -> Kanji:
        literal = character_element.find("literal").text

        # Get misc info
        misc = character_element.find("misc")
        grade = misc.find("grade")
        grade = int(grade.text) if grade is not None else None

        jlpt = misc.find("jlpt")
        jlpt = int(jlpt.text) if jlpt is not None else None

        stroke_count = int(misc.find("stroke_count").text)

        freq = misc.find("freq")
        freq = int(freq.text) if freq is not None else None

        # Get readings and meanings
        rm = character_element.find("reading_meaning")
        if rm is not None:
            rmgroup = rm.find("rmgroup")
            if rmgroup is not None:
                # Get only English meanings (no m_lang attribute)
                meanings = [
                    m.text
                    for m in rmgroup.findall("meaning")
                    if "m_lang" not in m.attrib
                ]

                # Get readings
                kun_readings = [
                    r.text
                    for r in rmgroup.findall("reading")
                    if r.attrib["r_type"] == "ja_kun"
                ]
                on_readings = [
                    r.text
                    for r in rmgroup.findall("reading")
                    if r.attrib["r_type"] == "ja_on"
                ]
            else:
                meanings = []
                kun_readings = []
                on_readings = []
        else:
            meanings = []
            kun_readings = []
            on_readings = []

        return Kanji(
            literal=literal,
            meanings=meanings,
            grade=grade,
            jlpt=jlpt,
            stroke_count=stroke_count,
            freq=freq,
            kun_readings=kun_readings,
            on_readings=on_readings,
        )

    def get_all_kanji(self) -> List[Kanji]:
        """Parse all kanji from the XML file."""
        all_kanji = [
            self.__parse_kanji(char) for char in self.root.findall("character")
        ]
        # Filter out kanji without sufficient learning data
        all = [k for k in all_kanji if k.is_ok()]
        return all
