import gzip
import requests
from pathlib import Path


class DictionaryDownloader:
    def __init__(self):
        self.data_dir = Path("data/sources")
        self.urls = {
            "jmdict.xml": "http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz",
            "kanjidic.xml": "http://www.edrdg.org/kanjidic/kanjidic2.xml.gz",
        }

    def ensure_data_directory(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def download_file(self, url: str, filename: str) -> Path:
        output_path = self.data_dir / filename

        print(f"(i) Downloading {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Save compressed file
        gz_path = output_path.with_suffix(".gz")
        with gz_path.open("wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Decompress
        print(f"(i) Decompressing {filename}...")
        with gzip.open(gz_path, "rb") as gz_file:
            with output_path.open("wb") as out_file:
                out_file.write(gz_file.read())

        # Clean up compressed file
        gz_path.unlink()
        return output_path

    def download_all_unless_exists(self):
        all_exist = True
        all_exist &= self.data_dir.exists()
        for fname in self.urls.keys():
            all_exist &= (self.data_dir / fname).exists()

        if not all_exist:
            self.download_all()

    def download_all(self):
        self.ensure_data_directory()

        for name, url in self.urls.items():
            try:
                path = self.download_file(url, name)
                print(
                    f"(i) Successfully downloaded and extracted {name} to {path}"
                )
            except Exception as e:
                print(f"(!) Error downloading {name}: {str(e)}")
