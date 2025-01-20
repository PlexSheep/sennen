import http.server
import os
import tempfile
import threading
import time
from datetime import date, timedelta
from pathlib import Path

from _pytest.outcomes import skip
import pytest

from sennen.download_dicts import DictionaryDownloader
from sennen.generate import SiteGenerator


@pytest.fixture(scope="session")
def temp_data_dir():
    """Create a temporary directory for test data"""
    return Path(tempfile.mkdtemp())


@pytest.fixture(scope="session")
def actively_download_sources(temp_data_dir):
    """Download dictionary sources for testing"""
    downloader = DictionaryDownloader()
    downloader.data_dir = temp_data_dir / "sources"
    downloader.download_all()
    yield downloader.data_dir


@pytest.fixture(scope="session")
def data_sources(temp_data_dir):
    """Download or copy dictionary sources for testing purposes. This does not always actually download"""
    downloader = DictionaryDownloader()
    downloader.data_dir = temp_data_dir / "sources"

    # for testing: do not always download, instead just link the already exisitng data source files if possible
    real_data_dir = Path("data/sources")
    if real_data_dir.exists():
        print(
            "real data dir exists, trying to just link the actual source files to avoid downloading"
        )
        downloader.ensure_data_directory()
        for filename in downloader.urls.keys():
            os.link(real_data_dir / filename, downloader.data_dir / filename)

    downloader.download_all_unless_exists()
    yield downloader.data_dir


@pytest.fixture(scope="session")
def generated_site(temp_data_dir, data_sources):
    """Generate a test site"""
    generator = SiteGenerator(temp_data_dir, Path("ressources"), verbose=True)
    days = 3650
    generator.generate_site(
        start_date=date(year=2025, month=1, day=1) - timedelta(days=days),
        num_days=days * 2,
        skip_daily=False,
    )
    yield generator.site_dir


@pytest.fixture(scope="session")
def http_server(generated_site):
    """Start a local HTTP server for testing"""
    port = 8999  # Use a different port than development
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(("", port), handler)

    # Change to the generated site directory
    original_dir = Path.cwd()
    os.chdir(generated_site)

    # Start server in a thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    yield f"http://localhost:{port}"

    # Cleanup
    httpd.shutdown()
    httpd.server_close()
    os.chdir(original_dir)
