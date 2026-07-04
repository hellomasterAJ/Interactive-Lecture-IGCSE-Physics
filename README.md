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
- **Interactive graphs**: Real-time animation with Canvas + SVG (horizontal motion 🚗, free fall 🍎, stopping distance 🚘, advanced VT graph 📈)
- **SUVAT proofs**: 5 visual area proofs (v=u+at, s=ut+½at², s=vt-½at², s=½(u+v)t, v²=u²+2as)
- **Non-uniform scenarios**: Terminal Velocity 🪂, Rocket Launch 🚀, Harmonic Motion 〰️ with gradient & trapezoidal analysis
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

## 📋 Changelog

### 4 July 2026 — 10-Theme System (All Graphs)

| # | การเปลี่ยนแปลง | ไฟล์ที่เกี่ยวข้อง | รายละเอียด |
|---|---------------|------------------|-----------|
| 1 | **เพิ่ม 3 ธีมใหม่** | ทั้ง 4 ไฟล์ | 💎 One Dark (Atom), ☀️ Classic White, 🌃 Cyberpunk Neon |
| 2 | **ลบ Warm Sand** | ทั้ง 4 ไฟล์ | เปลี่ยนเป็น Classic White แทน |
| 3 | **เปลี่ยนชื่อ** | ทั้ง 4 ไฟล์ | Classic Light → Classic White |
| 4 | **Reorder dropdown** | ทั้ง 4 ไฟล์ | Dark→Vintage→Neon→Cosmic→OneDark→White→Clay→Warm→Sage→Mist |

### 3 July 2026 — Layout Refinements (`kinematics_vt_graph_v1.html`)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **Animate → ใต้ slider** | ย้ายปุ่ม ▶ Animate ใน Analysis Tool (Non-uniform) ไปอยู่ด้านล่างของ time slider |
| 2 | **Uniform Parameters → Left column** | ย้าย 🎛️ Uniform Acceleration Parameters เข้าไปใน left column ใต้ graph-card (กว้างเท่ากับกราฟ) อยู่เหนือ Key Concept |
| 3 | **📖 Define → Equation card** | ย้ายปุ่ม Define + panel จาก Uniform Parameters ไปไว้ด้านล่างสุดของ Equation card (ฝั่งขวา) |
| 4 | **Fix layout break** | ลบ `</div>` เกินที่เหลือจาก definePanel — แก้ HTML structure ให้ถูกต้อง |
