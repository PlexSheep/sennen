# src/sennen/main.py
import argparse
from pathlib import Path
from .download_dicts import DictionaryDownloader


def download_command(args):
    downloader = DictionaryDownloader()
    downloader.download_all()


def generate_command(args):
    print("Generate command not implemented yet")
    # TODO: Implement generation of daily JSON files


def main():
    parser = argparse.ArgumentParser(
        description="sennen 「千年」- Daily Japanese Kanji and Words"
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True
    )

    # Download command
    download_parser = subparsers.add_parser(
        "download",
        help="Download dictionary source files (JMdict, KANJIDIC)"
    )
    download_parser.set_defaults(func=download_command)

    # Generate command
    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate daily JSON files"
    )
    generate_parser.add_argument(
        "--days",
        type=int,
        default=365,
        help="Number of days to generate (default: 365)"
    )
    generate_parser.set_defaults(func=generate_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
