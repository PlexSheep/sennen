# sennen 「千年」

<div align="center">
    <img src="ressources/static/img/logo.svg" width="75%" alt="Sennen - Daily Japanese Learning">
    <p>
        A modern, minimal Japanese learning platform that delivers daily kanji and vocabulary,
        <br/>
        powered by JMdict and KANJIDIC with beautiful furigana rendering.
    </p>
    <br/>
    <a href="https://github.com/PlexSheep/sennen/actions">
        <img src="https://img.shields.io/github/actions/workflow/status/PlexSheep/sennen/deploy.yml?label=CI" alt="CI Status"/>
    </a>
    <a href="https://github.com/PlexSheep/sennen/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/PlexSheep/sennen" alt="License"/>
    </a>
    <a href="https://github.com/PlexSheep/sennen/releases">
        <img src="https://img.shields.io/github/v/release/PlexSheep/sennen" alt="Release"/>
    </a>
    <br/>
    <img src="https://img.shields.io/badge/python-%233776AB.svg?style=flat&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=flat&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"/>
    <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript"/>
</div>

## ✨ Features

- 📆 Daily kanji and words
- 🎯 Intelligent selection based on JLPT level and frequency
- 💫 Furigana rendering for kanji compounds
- 🌓 Dark mode support
- 📱 Responsive design for all devices
- 🚀 Fast and lightweight static site generation
- 🔄 10-year calendar with consistent daily content in both directions in time

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/PlexSheep/sennen.git
cd sennen

# Install sennen
pip install -e .

# Download dictionary files
sennen download

# Generate the site
sennen generate

# Done! The site should now be generated to the directory data/site

# You can use any webserver to serve the static files in data/site
# sennen serve uses a basic python webserver for development purposes
# With this, you can reach the website at http://localhost:8000
sennen serve
```

## 🛠️ Technology Stack

- **Backend:**

    - Python for static site generation
    - XML parsing for JMdict and KANJIDIC2
    - Custom hacky furigana generation
    - Jinja2 templates

- **Frontend:**
    - Vanilla JavaScript for interactivity and webui
    - Tailwind CSS for styling
    - Dark mode with toggle switch

## 📚 Content Generation

Sennen uses a unique algorithm to select daily content:

1. Parses JMdict and KANJIDIC2 XML files
2. Filters content based on certin quiterias (quality of data, commonness of word or kanji)
3. Uses a deterministic random selection based on date and a magic prime number
4. Generates static JSON files for each day with kanji and word of the day
5. Pre-renders HTML templates with Jinja2

## 💡 Development

### Prerequisites

- Python 3.10+
- Internet connection (for dictionary downloads)
- Basic understanding of Japanese language structure 😼

### Project Structure

```
sennen/
├── data/                       # Generated data and source files (dictionaries)
├── ressources/                 # Static assets and templates
│   ├── static/                 # CSS, JavaScript, and images
│   └── templates/              # Jinja2 templates
└── src/
    └── sennen/                 # Python source code
        ├── parse/              # XML parsing modules for the dictionaries
        ├── download_dicts.py   # downloads the source dictionaries
        ├── generate.py         # generates the website
        └── main.py             # CLI entry point
```

### Building from Source

1. Clone the repository
2. Install development dependencies
3. Generate development build
4. use sennen to download the sources and generate the site
5. Start local server

## 🤝 Contributing

All Contributions are welcome!
Please feel free to submit a Pull Request or Issue (Bug Reports and Feature Requests).
For major changes, please open an issue before making a PR to discuss what you would like to change.
You may also use the discussions tab if you have any questions.

For code contributions please make sure to:

- Follow the existing code style
- Add tests for any new functionality
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [JMdict/EDICT](http://www.edrdg.org/jmdict/edict.html) and [KANJIDIC](http://www.edrdg.org/kanjidic/kanjidic.html) projects
- [Electronic Dictionary Research and Development Group](http://www.edrdg.org/)
- The Japanese language learning community

---

<div align="center">
    Made for 日本語 learners and speakers everywhere
</div>
