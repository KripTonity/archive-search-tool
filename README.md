````markdown
# 🗂️ archive-search-tool

The goal of **archive-search-tool** is to let users enter **one single search query** and get results back from **multiple online archive platforms** (such as Gallica, Internet Archive, etc.) in a clean, unified interface.

---

## ✨ Features

- 🔍 Unified search across multiple archive sources
- 📋 Results are displayed in a scrollable, interactive UI
- 🌐 Clickable links to open the documents in your browser
- 💾 (Coming soon) Export results as CSV
- ⚙️ Easy packaging into `.exe` or standalone applications

---

## 🖼️ Preview of the Interface

> Built with [Dear PyGui](https://github.com/hoffstadt/DearPyGui)  
> Lightweight, modern UI with search input, result table, and action buttons

---

## 🚀 Quick Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/archive-search-tool.git
cd archive-search-tool
````

### 2. Set up virtual environment and install dependencies

Just run:

```bash
python3 setup_env.py
```

This script will:

* Create a Python virtual environment in `./venv`
* Install all required packages from `requirements.txt`

### 3. Activate the virtual environment

#### On Linux/macOS:

```bash
source venv/bin/activate
```

#### On Windows:

```cmd
venv\Scripts\activate
```

### 4. Run the application

```bash
python run.py
```

---

## 📦 Build a `.exe` file (Windows)

First, install PyInstaller:

```bash
pip install pyinstaller
```

Then generate the executable:

```bash
pyinstaller --onefile --noconsole --icon=assets/icon.ico run.py
```

The `.exe` will be located in the `dist/` directory.

---

## 📁 Project Structure

```
archive-search-tool/
├── app/
│   ├── main.py               # UI launcher
│   ├── search_manager.py     # Coordinates all site scrapers
│   ├── exporter.py           # (Planned) CSV export
│   └── scrapers/
│       ├── gallica.py
│       └── internet_archive.py
├── assets/
│   └── icon.ico              # Optional icon
├── build/
├── dist/
├── venv/
├── run.py                    # Main entry point
├── requirements.txt
├── setup_env.py              # Virtualenv + install automation
└── README.md
```

---

## 🧰 Technologies Used

| Component          | Library                 |
| ------------------ | ----------------------- |
| GUI                | `Dear PyGui`            |
| HTTP Requests      | `requests`              |
| HTML/XML Parsing   | `beautifulsoup4`        |
| Web Browser Launch | `webbrowser` (built-in) |
| CSV Export         | `csv` (built-in)        |
| Binary Packaging   | `pyinstaller`           |

---

## 🛠 Planned Features

* [ ] Add more sources (Internet Archive, INA, RetroNews, etc.)
* [ ] CSV export of search results
* [ ] Integrated web preview (`pywebview`)
* [ ] Search filters and history
* [ ] Offline mode (optional result caching)

---

## 🤝 Contributing

Pull requests and contributions are welcome!
You can fork the repository and open an issue or PR.
[github.com/your-username/archive-search-tool](https://github.com/your-username/archive-search-tool)

---

## 📄 License
This project is released under the **MIT License** — feel free to use, modify, and distribute.

---

## 👤 Author

**Your Name Here**
GitHub: [@KripTonity](https://github.com/KripTonity)

