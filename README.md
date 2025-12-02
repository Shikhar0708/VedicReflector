![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Security Tool](https://img.shields.io/badge/Category-Offensive%20Security-red.svg)
![Maintainer](https://img.shields.io/badge/Maintainer-VEDIC/DEVIC-blueviolet.svg)

# VXSS — Vedic Reflector  
### A lightweight reflected XSS scanner with multi-payload detection and a clean offensive-security CLI.

VXSS (Vedic Reflector) is a modular Python tool designed to identify **reflected Cross-Site Scripting (XSS)** vulnerabilities.  
It analyzes both **query parameters** and **HTML forms**, injects multiple payload types, and highlights parameters that reflect data without proper encoding.

With clean CLI colors, rotating banners, and a structured codebase, VXSS is ideal for security research, pentesting labs, and portfolio demonstration.

---

## 🚀 Features

- **Multi-payload XSS detection**  
  Tests HTML, SVG, Attribute, and JavaScript contexts.

- **Form & parameter scanning**  
  Handles GET/POST forms + direct query parameter fuzzing.

- **Colored CLI output**  
  Clean, readable results with severity-style colors.

- **Rotating ASCII banners**  
  Random mirror-style VXSS banners for terminal aesthetics.

- **Modular structure**  
  Easy to expand with crawlers, reporting, JSON scanning, etc.

---

## 📦 Installation

```bash
git clone https://github.com/Shikhar0708/VedicReflector.git
cd VedicReflector
pip install -r requirements.txt
```

▶️ Usage
```bash
python3 main.py <target_url>
```
Example:

```bash
python3 main.py http://sudo.co.il/xss/level0.php
```
Sample output:

<img width="490" height="353" alt="test" src="https://github.com/user-attachments/assets/662aa7d3-fbef-4942-9434-6b8e994247c2" />

## 🧩 Project Structure

graphql
Copy code
vedicreflector/
│
├── main.py
└── core/
    ├── banner.py      # Random ASCII banner rotation
    ├── utils.py       # Color helpers + common utilities
    ├── payloads.py    # Multi-vector XSS payloads
    ├── extractor.py   # Form & query parameter extraction
    ├── scanner.py     # Reflection testing engine
    └── reporter.py    # Colorized result printing

## 🔧 Payload Types

VXSS tests multiple reflected XSS contexts using different payload vectors:

| Context    | Example Payload                               |
|------------|-----------------------------------------------|
| **HTML**      | `<img src=x onerror=alert(1)>VEDICXSS`       |
| **SVG**       | `<svg/onload=alert(1)>VEDICXSS`              |
| **Attribute** | `" autofocus onfocus=alert(1)" VEDICXSS`     |
| **JS**        | `');alert(1);//VEDICXSS`                     |

## 🛤 Roadmap (Upcoming)

- [ ] Crawler for multi-page scanning  
- [ ] HTML / Markdown report generation  
- [ ] CLI arguments (e.g., `--url`, `--crawl`, `--verbose`)  
- [ ] JSON / API request scanning  
- [ ] DOM-XSS detection using a headless browser  
- [ ] Packaging as `pip install vxss`  


## 📜 License

This project is licensed under the **MIT License**.  
See the [`LICENSE`](LICENSE) file for details.


## 👤 Author

**Shikhar Kant Sinha (VEDIC/DEVIC)**  
Offensive Security • Pentesting • Tool Development
