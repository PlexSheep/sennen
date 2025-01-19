import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set

from .common import (
    Furigana,
    Meaning,
    Reading,
)


@dataclass
class Word:
    """Represents a word entry from JMdict"""

    id: str
    writings: List[Furigana]  # Each writing with its furigana information
    readings: List[Reading]  # All possible readings
    meanings: List[Meaning]  # Word meanings/glosses
    pos: List[str]  # Parts of speech

    def is_ok(self) -> bool:
        """Check if word has sufficient data to be useful"""
        return (
            len(self.writings) > 0  # Has at least one writing
            and len(self.readings) > 0  # Has at least one reading
            and len(self.meanings) > 0  # Has at least one meaning
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "furigana": self.writings[0].to_dict_list()
            if self.writings
            else None,
            "writings": [w.literal for w in self.writings],
            "readings": [
                {"text": str(r.text), "common": r.common} for r in self.readings
            ],
            "meanings": [
                {"text": str(m.text), "common": m.common} for m in self.meanings
            ],
            "pos": self.pos,
        }

    def to_str(self) -> str:
        """Get the first writing of this word"""
        return self.writings[0].literal


class WordParser:
    """Parser for JMdict XML entries"""

    # Standard part-of-speech mappings
    POS_MAP = {
        "&n;": "noun",
        "&v1;": "verb (ichidan)",
        "&v5k;": "verb (godan)",
        "&adj-i;": "i-adjective",
        "&adj-na;": "na-adjective",
        "&adv;": "adverb",
        "&int;": "interjection",
        "&prt;": "particle",
        "&pref;": "prefix",
        "&suf;": "suffix",
        "&unc;": "unclassified",
    }

    def __init__(self, xml_path: Path):
        """Initialize parser with JMdict XML file path"""
        if not xml_path.exists():
            raise FileNotFoundError(f"JMdict file not found: {xml_path}")
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def _parse_entry(self, entry_element) -> Optional[Word]:
        """Parse a single JMdict entry element into a Word object"""
        # Get entry ID
        entry_id = entry_element.find("ent_seq").text

        # Parse writings and their readings
        readings: List[Reading] = []
        writing_reading_map: Dict[str, Set[str]] = {}

        # First collect all readings
        for r_ele in entry_element.findall("r_ele"):
            reading_text = r_ele.find("reb").text
            if reading_text is None:
                continue

            # Check if it's marked as common
            is_common = any(
                pri.text.startswith("nf") for pri in r_ele.findall("re_pri")
            )

            # Get writing restrictions
            restrictions = {r.text for r in r_ele.findall("re_restr")}

            # Add to readings list
            readings.append(Reading(text=reading_text, common=is_common))

            # Map restricted readings to writings
            if restrictions:
                for writing in restrictions:
                    writing_reading_map.setdefault(writing, set()).add(
                        reading_text
                    )

        # Then process writings
        furigana_writings: List[Furigana] = []
        for k_ele in entry_element.findall("k_ele"):
            writing = k_ele.find("keb").text
            if writing is None:
                continue

            # Find appropriate reading
            valid_readings = writing_reading_map.get(
                writing, {r.text for r in readings}
            )
            if not valid_readings:
                continue

            # Use first valid reading for furigana
            reading = next(iter(valid_readings))
            furigana_writings.append(Furigana.create(writing, reading))

        # Parse meanings and parts of speech
        meanings: List[Meaning] = []
        pos_tags: Set[str] = set()

        for sense in entry_element.findall("sense"):
            # Get part of speech tags
            for pos in sense.findall("pos"):
                pos_text = self.POS_MAP.get(pos.text, pos.text)
                pos_tags.add(pos_text)

            # Get meanings (English glosses)
            for gloss in sense.findall("gloss"):
                if "xml:lang" in gloss.attrib:
                    continue
                # No g_type attribute indicates primary/common meaning
                is_common = not bool(gloss.attrib.get("g_type"))
                meanings.append(Meaning(text=gloss.text, common=is_common))

        word = Word(
            id=entry_id,
            writings=furigana_writings,
            readings=readings,
            meanings=meanings,
            pos=sorted(pos_tags),
        )

        return word if word.is_ok() else None

    def get_all_words(self) -> List[Word]:
        """Parse all valid words from JMdict"""
        return [
            word
            for entry in self.root.findall("entry")
            if (word := self._parse_entry(entry)) is not None
        ]

    def get_words_with_kanji(self, kanji: str) -> List[Word]:
        """Get all words containing the specified kanji"""
        return [
            word
            for word in self.get_all_words()
            if any(kanji in w.literal for w in word.writings)
        ]
