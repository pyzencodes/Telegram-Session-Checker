[![GitHub stars](https://img.shields.io/github/stars/pyzencodes/Telegram-Session-Checker?style=flat-square)](https://github.com/pyzencodes/Telegram-Session-Checker/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/pyzencodes/Telegram-Session-Checker?style=flat-square)](https://github.com/pyzencodes/Telegram-Session-Checker/issues)
![Python version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-Private%20Use-red?style=flat-square)

````markdown
# Session Checker



Private utility script for testing Telegram `.session` files and automatically sorting them into **working** and **non-working** groups.

> ⚠️ This is a private tool. Do **NOT** share publicly or upload `.session` files / API credentials to public repositories.

---

## 🔍 Overview

This script:
- Reads `.session` files inside the `./sessions` folder
- Tries to connect using your Telegram API credentials
- Separates sessions into:
  - `./sessions_ok` → authorized / valid sessions
  - `./sessions_bad` → unauthorized / invalid / failed sessions
- Displays a result summary when finished

No logs or additional metadata are stored.

---

## ⚙️ Setup & Configuration

### Requirements
- Python **3.8+**
- Telethon library

Install dependency:
```bash
pip install telethon
````

### Edit API credentials inside the script:

```python
API_ID = XXXX          # your API ID (integer)
API_HASH = "XXXXXX"    # your API HASH (string)
```

### Folder structure (default)

```bash
./sessions       # put .session files here
./sessions_ok    # script will store valid sessions
./sessions_bad   # script will store invalid sessions
```

---

## ▶️ Usage

1. Place all session files into the `sessions` folder
2. Run the script:

```bash
python session_checker.py
```

3. When finished, check results:

```
sessions_ok    → authorized sessions
sessions_bad   → unauthorized / failed sessions
```

---

## 🛑 Important Notes

* Keep your API keys and session files private
* Do not push `.session` files or credentials to GitHub
* For internal usage only

---

## License

This repository is for personal / internal use only.  
All rights reserved. You may not copy, distribute, sublicense, or use this code for commercial purposes without explicit permission from the author.

