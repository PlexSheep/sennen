# src/sennen/main.py
import argparse
from datetime import date, timedelta
from os import system
from pathlib import Path

from .download_dicts import DictionaryDownloader
from .generate import SiteGenerator, recursive_remove
from .conf import VERSION


data_dir = Path("data")
ressources_dir = Path("ressources")


def version():
    print(f"sennen v{VERSION}")


def download(args):
    downloader = DictionaryDownloader()
    downloader.download_all_unless_exists()


def generate(args):
    generator = SiteGenerator(data_dir, ressources_dir)
    start_date = date.today() - timedelta(
        days=args.days
    )  # make some before today too!
    generator.generate_site(start_date, args.days * 2, args.skip_daily)


def clean(args):
    recursive_remove(data_dir / "site")
    recursive_remove(data_dir / "sources")


def serve(args):
    site_path = data_dir / "site"
    cmd = f"python -m http.server --directory {site_path}"
    print(f"$ {cmd}")
    system(cmd)


def main():
    parser = argparse.ArgumentParser(
        description="sennen 「千年」- Daily Japanese Kanji and Words"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="show version and quit",
    )

    subparsers = parser.add_subparsers(
        title="Commands", dest="command", required=False
    )

    # Download command
    download_parser = subparsers.add_parser(
        "download", help="Download dictionary source files (JMdict, KANJIDIC)"
    )
    download_parser.set_defaults(func=download)

    # Serve command
    serve_parser = subparsers.add_parser(
        "serve", help="serve a local webserver"
    )
    serve_parser.set_defaults(func=serve)

    # Clean command
    serve_parser = subparsers.add_parser(
        "clean", help="clean up generated files"
    )
    serve_parser.set_defaults(func=clean)

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
    generate_parser.add_argument(
        "-s",
        "--skip-daily",
        action="store_true",
        help="Skip generation of daily files",
    )
    generate_parser.set_defaults(func=generate)

    args = parser.parse_args()
    if args.version:
        version()
    else:
        try:
            args.func(args)
        except AttributeError:
            parser.print_usage()
            exit(1)


if __name__ == "__main__":
    main()
