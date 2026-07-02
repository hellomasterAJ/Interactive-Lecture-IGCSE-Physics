# 📐 InteractiveLecture

**CIE IGCSE Physics 0625** — Interactive teaching materials for Topic 1: Motion, forces and energy.

## 🔄 Pipeline

```
lecture.md (Markdown + LaTeX) → build.py → interactive.html + lecture.pdf + lecture.json
```

## 📂 Project Structure

```
├── lectures/              ← Source: Markdown + LaTeX (8 topics)
├── output/                ← Generated: HTML + PDF + JSON
│   └── dashboard.html     ← Lecture index (auto-generated)
├── graphs/                ← Interactive graph HTML files
│   ├── kinematics_graphs_v1.html       ← Horizontal Motion 🚗
│   ├── kinematics_freefall_v1.html     ← Free Fall 🍎
│   ├── kinematics_stopping_v1.html     ← Stopping Distance 🚘
│   └── kinematics_vt_graph_v1.html     ← Advanced VT Graph 📈
├── scripts/               ← Build system (Python)
│   ├── build.py           ← Main: python build.py lecture.md
│   ├── build_dashboard.py ← Dashboard generator
│   ├── parse_lecture.py   ← Markdown parser
│   ├── pdf_export.py      ← Playwright → A4 PDF
│   └── templates/         ← Jinja2 HTML templates
└── scientists/            ← Scientist Bio Library
```

## 🚀 Quick Start

```bash
# Build all lectures
cd ~/InteractiveLecture
python3 scripts/build.py lectures/topic1_motion.md

# Build with preview
python3 scripts/build.py lectures/topic1_motion.md --preview

# Generate dashboard
python3 scripts/build_dashboard.py --open
```

### Install dependencies
```bash
pip3 install markdown playwright jinja2
python3 -m playwright install chromium
```

## 📖 Lectures (Topic 1 Complete)

| # | Topic | Interactive Graph |
|---|-------|:--------:|
| 1.1 | Physical Quantities & Measurement | ❌ |
| 1.2 | Motion — Kinematics | ✅ Horizontal, Free-fall, Stopping, Advanced VT Graph |
| 1.3 | Mass and Weight | ❌ |
| 1.4 | Density | ❌ |
| 1.5 | Forces (Hooke's Law) | ❌ |
| 1.6 | Effects of Forces (Moments, Pressure) | ❌ |
| 1.7 | Energy, Work & Power | ❌ |
| 1.8 | Energy Resources | ❌ |

## 🎯 Features

- **5-part lecture structure**: 📜 History → 🌍 Nature → ⚛️ Theory → 📊 Graphs → ✍️ Examples
- **Interactive graphs**: Real-time animation with Canvas + SVG (horizontal motion 🚗, free fall 🍎)
- **Dark/Light theme**: Warm taupe light mode (not harsh white)
- **KaTeX equations**: Beautiful LaTeX rendering
- **PDF export**: A4 format via Playwright headless browser
- **Section selector**: Filter lectures by section type
- **Scientist bio library**: 8 scientists with myth-vs-fact

## 🧪 Tech Stack

| Component | Technology |
|-----------|-----------|
| Graph rendering | JavaScript (Canvas API + SVG) |
| Build system | Python 3 |
| Markdown → HTML | Python `markdown` library |
| Templating | Jinja2 |
| PDF generation | Playwright (headless Chromium) |
| Equation rendering | KaTeX (CDN) |

## 📜 License

Educational use — HAUS Academy
