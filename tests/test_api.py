import json
from pathlib import Path

import pytest  # noqa: F401 do not remove this import. This is needed for pytest fixtures to work
import requests

import sennen  # noqa: F401


def test_api_word_kanji_order(generated_site):
    """Test that word and kanji order is consistent"""
    api_dir = generated_site / "api" / "v1" / "daily"

    for json_file in api_dir.glob("*.json"):
        with json_file.open() as f:
            data = json.load(f)

        # Check that each file has both word and kanji
        assert "word" in data, f"Missing word in {json_file}"
        assert "kanji" in data, f"Missing kanji in {json_file}"

        # Verify the date matches the filename
        expected_date = json_file.stem
        assert data["date"] == expected_date


def test_source_parsing(data_sources):
    """Test that dictionary sources can be parsed"""
    from sennen.parse.kanji import KanjiParser
    from sennen.parse.word import WordParser

    # Test KANJIDIC parsing
    kanji_parser = KanjiParser(data_sources / "kanjidic.xml")
    all_kanji = kanji_parser.get_all_kanji()
    assert len(all_kanji) > 0, "No kanji parsed"

    # Test JMdict parsing
    word_parser = WordParser(data_sources / "jmdict.xml")
    all_words = word_parser.get_all_words()
    assert len(all_words) > 0, "No words parsed"


def test_site_generation(generated_site):
    """Test that the site was generated with all required files and none of the unwanted files"""
    required_files = [
        "index.html",
        "kanji.html",
        "word.html",
        "img/logo.svg",
        "js/common.js",
        "api/v1/daily/2025-01-01.json",
        "api/v1/daily/2025-12-31.json",
        "api/v1/daily/2025-09-01.json",
        "api/v1/daily/2025-09-30.json",
    ]
    unwanted_files = [
        "base.html",
        "api/v1/daily/1970-01-01.json",
        "api/v1/daily/2970-01-01.json",
        "api/v1/daily/2026-02-30.json",
        "api/v1/daily/2025-09-31.json",
    ]

    for file in required_files:
        assert (generated_site / file).exists(), f"Missing: {file}"
    for file in unwanted_files:
        assert not (generated_site / file).exists(), f"Should not exist: {file}"


def test_site_responses(http_server):
    """Test that key pages return HTTP 200 and that unwanted pages return HTTP 4XX"""
    wanted_pages = [
        "",  # Root/index
        "index.html",
        "kanji.html",
        "word.html",
        "img/logo.svg",
        "js/common.js",
        "api/v1/daily/2025-01-01.json",
        "api/v1/daily/2025-12-31.json",
        "api/v1/daily/2025-09-01.json",
        "api/v1/daily/2025-09-30.json",
    ]
    unwanted_pages = [
        "base.html",
        "api/v1/daily/1970-01-01.json",
        "api/v1/daily/2970-01-01.json",
        "api/v1/daily/2026-02-30.json",
        "api/v1/daily/2025-09-31.json",
    ]

    for page in wanted_pages:
        url = f"{http_server}/{page}"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to load {url}"
    for page in unwanted_pages:
        url = f"{http_server}/{page}"
        response = requests.get(url)
        assert 400 <= response.status_code < 500, (
            f"Unwanted Page did not fail to load {url}"
        )


@pytest.mark.skip(
    reason="Let's not put too much load on the dictionary servers and also save us some time :)"  # and also save us some time
)
def test_download_data_sources(
    actively_download_sources: Path, temp_data_dir: Path
):
    sources = ["jmdict.xml", "kanjidic.xml"]

    for source in sources:
        assert (actively_download_sources / source).exists(), (
            f"data source {source} does not exist after download"
        )
