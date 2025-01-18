# src/sennen/main.py
import argparse
from datetime import datetime, timedelta
from os import system
from pathlib import Path

from .download_dicts import DictionaryDownloader
from .generate import SiteGenerator


def download_command(args):
    downloader = DictionaryDownloader()
    downloader.download_all()


def generate_command(args):
    data_dir = Path("data")
    generator = SiteGenerator(data_dir)
    start_date = datetime.now() - timedelta(days=args.days) # make some before today too!
    generator.generate_site(start_date, args.days * 2)


def serve(args):
    site_path = Path("data") / "site"
    cmd = f"python -m http.server --directory {site_path}"
    print(f"$ {cmd}")
    system(cmd)


def main():
    parser = argparse.ArgumentParser(
        description="sennen 「千年」- Daily Japanese Kanji and Words"
    )

    subparsers = parser.add_subparsers(
        title="Commands", dest="command", required=True
    )

    # Download command
    download_parser = subparsers.add_parser(
        "download", help="Download dictionary source files (JMdict, KANJIDIC)"
    )
    download_parser.set_defaults(func=download_command)

    # Download command
    serve_parser = subparsers.add_parser(
        "serve", help="serve a local webserver"
    )
    serve_parser.set_defaults(func=serve)

    # Generate command
    generate_parser = subparsers.add_parser(
        "generate", help="Generate daily JSON files"
    )
    generate_parser.add_argument(
        "--days",
        type=int,
        default=3650,
        help="Number of days to generate into past and future (default: 3650 - 10 years). Very large numbers will slow down the system and be difficult to deploy.",
    )
    generate_parser.set_defaults(func=generate_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
