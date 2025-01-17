import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path


@dataclass
class Kanji:
    literal: str
    meanings: List[str]  # English meanings only for now
    grade: Optional[int]
    jlpt: Optional[int]
    stroke_count: int
    freq: Optional[int]  # Frequency of use ranking
    kun_readings: List[str]
    on_readings: List[str]


class KanjiParser:
    def __init__(self, xml_path: Path):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def __parse_kanji(self, character_element) -> Kanji:
        literal = character_element.find('literal').text

        # Get misc info
        misc = character_element.find('misc')
        grade = misc.find('grade')
        grade = int(grade.text) if grade is not None else None

        jlpt = misc.find('jlpt')
        jlpt = int(jlpt.text) if jlpt is not None else None

        stroke_count = int(misc.find('stroke_count').text)

        freq = misc.find('freq')
        freq = int(freq.text) if freq is not None else None

        # Get readings and meanings
        rm = character_element.find('reading_meaning')
        if rm is not None:
            rmgroup = rm.find('rmgroup')
            if rmgroup is not None:
                # Get only English meanings (no m_lang attribute)
                meanings = [m.text for m in rmgroup.findall('meaning')
                            if 'm_lang' not in m.attrib]

                # Get readings
                kun_readings = [r.text for r in rmgroup.findall('reading')
                                if r.attrib['r_type'] == 'ja_kun']
                on_readings = [r.text for r in rmgroup.findall('reading')
                               if r.attrib['r_type'] == 'ja_on']
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
            on_readings=on_readings
        )

    def get_all_kanji(self) -> List[Kanji]:
        """Parse all kanji from the XML file."""
        return [self.__parse_kanji(char) for char in self.root.findall('character')]
