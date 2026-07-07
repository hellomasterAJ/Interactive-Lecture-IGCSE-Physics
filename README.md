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
│   ├── kinematics_1_horizontal_graphs.html      ← Horizontal Motion 🚗
│   ├── kinematics_2_horizontal_graph_stopping_d.html ← Stopping Distance 🚘
│   ├── kinematics_3_vertical_graphs_freefall.html    ← Free Fall 🍎
│   ├── kinematics_4_vertical_graphs_terminal_v.html  ← Terminal Velocity Skydive 🪂
│   └── kinematics_5_advanced_velocity_time_graphs.html ← Advanced VT Graph 📈
├── simulations/           ← Interactive physics simulations (ไม่ใช่กราฟ)
│   ├── Measurement_1_vernier_caliper.html            ← Vernier Caliper 📏
│   ├── Measurement_2_micrometer_screw_gauge.html     ← Micrometer Screw Gauge 🔧
│   └── Measurement_3_balance_newtonmeter.html        ← Mass vs Weight (Balance & Newtonmeter) ⚖️
├── scripts/               ← Build system (Python)
│   ├── build.py           ← Main: python build.py lecture.md
│   ├── build_dashboard.py ← Dashboard generator
│   ├── parse_lecture.py   ← Markdown parser
│   ├── pdf_export.py      ← Playwright → A4 PDF
│   └── templates/         ← Jinja2 HTML templates
├── Equipments/            ← ⏳ Legacy (กำลังย้ายไป simulations/)
├── references/
│   ├── scientists/        ← Scientist Bio Library
│   ├── terminology/       ← Physics terminology
│   ├── historical-milestones/ ← Newton's apple, Tower of Pisa, ...
│   └── physical-quantity/ ← In-depth reference per physical quantity (time, length, mass, ...)
└── Junkyard/              ← Retired prototypes (old micrometer sim)
```

## 🚀 Quick Start

```bash
# Build all lectures
cd ~/InteractiveLecture
python3 scripts/build.py lectures/topic12_motion.md

# Build with preview
python3 scripts/build.py lectures/topic12_motion.md --preview

# Generate dashboard
python3 scripts/build_dashboard.py --open
```

### Install dependencies
```bash
pip3 install markdown playwright jinja2
python3 -m playwright install chromium
```

## 📖 Lectures (Topic 1 Complete)

| # | Topic | Interactive Graph | Simulation |
|---|-------|:--------:|:--------:|
|| 1.1 | Physical Quantities & Measurement | ❌ | ✅ Vernier Caliper, Micrometer |
|| 1.2 | Motion — Kinematics | ✅ Horizontal, Free-fall, Stopping, Advanced VT, Terminal Velocity 🪂 | ❌ |
|| 1.3 | Mass and Weight | ❌ | ✅ Balance & Newtonmeter ⚖️ |
|| 1.4 | Density | ❌ | ❌ |
|| 1.5 | Forces (Hooke's Law) | ❌ | ❌ |
|| 1.6 | Effects of Forces (Moments, Pressure) | ❌ | ❌ |
|| 1.7 | Energy, Work & Power | ❌ | ❌ |
|| 1.8 | Energy Resources | ❌ | ❌ |

> 💡 **Simulations** = virtual lab instruments / interactive phenomena (ไม่ใช่กราฟ). ปัจจุบันมี: 📏 Vernier Caliper (Topic 1.1), 🔧 Micrometer Screw Gauge (Topic 1.1), ⚖️ Balance & Newtonmeter (Topic 1.3)

## 🎯 Features

- **5-part lecture structure**: 📜 History → 🌍 Nature → ⚛️ Theory → 📊 Graphs → ✍️ Examples
- **Interactive graphs**: Real-time animation with Canvas 2D (horizontal motion 🚗, free fall 🍎, stopping distance 🚘, advanced VT graph 📈, terminal velocity skydive 🪂)
- **Interactive physics simulations**: Virtual lab instruments และ interactive phenomena ที่ไม่ต้องใช้กราฟ
  - 📏 **Vernier Caliper** — 3 modes (Simulate/Practice/Quiz), 3 difficulty levels, zoom double-click, zero error ±5 div, workpiece clamping
  - 🔧 **Micrometer Screw Gauge** — 0–25 mm, LC 0.01 mm, drag-to-rotate thimble, sleeve + thimble scale, magnifier overlay, tutorial animation, practice/exam mode, 3 themes
  - ⚖️ **Balance & Newtonmeter (Mass vs Weight)** — ลาก masses (100 g–2 kg, ซ้อนได้ 5 ชิ้น) ขึ้นเครื่องชั่งดิจิทัล (g/kg) หรือแขวน spring balance (N), 4 ดาว (Earth/Moon/Mars/Jupiter), Simple (g=10, Earth เท่านั้น) ⇄ Location (g จริงต่อดาว), Newtonmeter range 0–5/0–10/Auto + over-range warning, force arrow W=mg, 3 modes (Simulate/Practice/Quiz)
- **SUVAT proofs**: 5 visual area proofs (v=u+at, s=ut+½at², s=vt-½at², s=½(u+v)t, v²=u²+2as)
- **Non-uniform scenarios**: Terminal Velocity 🪂, Rocket Launch 🚀, Harmonic Motion 〰️ with gradient & trapezoidal analysis
- **2-phase Skydive simulation**: Freefall (tanh model, a=g→Vt₁) + Parachute deployment (drag multiplier→Vt₂) with force arrows (Weight ↓ / Drag ↑), animated skydiver, moving clouds, airplane background
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

### 7 July 2026 — Mass vs Weight Simulator (`simulations/Measurement_3_balance_newtonmeter.html`)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **สร้าง Balance & Newtonmeter Simulator** | Canvas ล้วน — masses ทองเหลือง 5 ขนาด (100 g–2 kg) ลากวางบนจานชั่งดิจิทัล (อ่าน g/kg) หรือแขวน newtonmeter (อ่าน N พร้อมสปริงเด้ง) |
| 2 | **4 ดาว** | Earth / Moon / Mars / Jupiter — balance อ่านเท่าเดิมทุกดวง, newtonmeter เปลี่ยนตาม g; ฉากหลังเปลี่ยนตามดาว (เห็นโลกจากดวงจันทร์ 🌍, ดาวเสาร์จากดาวพฤหัส 🪐) |
| 3 | **ปุ่ม Level toggle เดียว** | Simple (ทอง, g=10, ล็อกที่โลก) ⇄ Location (เขียวมิ้นต์, g จริง 9.81/1.62/3.72/24.79 เลือกดาวได้) |
| 4 | **Newtonmeter range** | 0–5 N / 0–10 N / **Auto** (ปรับ scale อัตโนมัติตั้งแต่ตอนหยิบก้อน ก่อนแขวน ให้ max ≥ น้ำหนักเสมอ) + เตือน OVER RANGE เมื่อเกิน scale ในโหมด manual |
| 5 | **วางซ้อนได้ 5 ชิ้น** | drop zone ขยายตามความสูงกอง (แก้บั๊กปล่อยเหนือยอดกองแล้วเด้งกลับ), ก้อนชิดกันสวยงาม |
| 6 | **3 โหมด** | Simulate / Practice (โจทย์ W=mg, m=W/g, ย้ายดาว-มวลไม่เปลี่ยน พร้อมเฉลยละเอียด + คะแนน) / Quiz (5 ข้อ + ดาว + ตารางผล) |
| 7 | **UI** | Force arrow W=mg, formula panel แทนค่าสด, HAUS logo มุมขวา toolbar, Labels ย้ายขึ้นแถวบน, ปุ่ม Reset |

### 7 July 2026 — Simulations Directory + README Update

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **สร้าง `simulations/`** | directory ใหม่สำหรับ interactive simulations ที่ไม่ใช่กราฟ (virtual lab instruments, phenomena) |
| 2 | **rename → Measurement_*** | `vernier_caliper_v1.html` → `Measurement_1_vernier_caliper.html`, `micrometer_screw_gauge_v1.html` → `Measurement_2_micrometer_scraw_gauge.html` |
| 3 | **อัปเดต README structure** | แก้ชื่อไฟล์กราฟให้ตรง + เพิ่ม `simulations/` + เปลี่ยน `Equipments/` เป็น Legacy |
| 4 | **เพิ่ม Simulation column** | ใน Lecture table — แยก Graph vs Simulation ชัดเจน |
| 5 | **อัปเดต Features** | เพิ่มรายละเอียด Simulation (Vernier Caliper, Micrometer) |

### 6 July 2026 — Vernier Caliper Simulator (`Equipments/vernier_caliper.html`)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **สร้าง Vernier Caliper Simulator** | Canvas ล้วน ไม่ใช้รูปภาพ — สเกล vernier วาดใหม่ตาม LC ที่เลือก (10/20/50 ขีด) |
| 2 | **โหมดการใช้งาน** | Simulate / Practice (เฉลยละเอียด + คะแนน) / Quiz (5 ข้อ + ดาว) |
| 3 | **ระดับความยาก** | Simple (LC 0.1 mm) / Advance (LC 0.1 / 0.05 / 0.02 mm) |
| 4 | **Zoom แบบ double-click** | ขยาย 4× รอบตำแหน่ง vernier zero, ESC/pill ออกได้, ลากต่อได้ขณะซูม |
| 5 | **Zero Error ±5 div** | การ์ด Observed − ZE = Corrected รองรับ ZE ลบ (−(N−i)×LC) |
| 6 | **Workpiece + Guide toggle** | วัตถุหนีบระหว่างปากจับ, แถบทอง coincidence เปิด/ปิดได้ |
| 7 | **ความสมจริง** | ขาหนีบ chisel-point มี bevel/แสง-เงา/brushed texture, เม็ดมะยมกว้าง-แบนตามของจริง |
| 8 | **Toolbar 2 แถวคงที่** | LC pills ล็อกจาง ๆ ตอน Simple — layout ไม่ขยับข้ามโหมด |
| 9 | **ย้าย micrometer ไป Junkyard/** | เลิกใช้เวอร์ชันเก่าที่พึ่งรูปภาพ |
| 10 | **เพิ่ม historical-milestones** | Newton's apple, Tower of Pisa experiment ใน references/ |

### 4 July 2026 — 10-Theme System (All Graphs)

| # | การเปลี่ยนแปลง | ไฟล์ที่เกี่ยวข้อง | รายละเอียด |
|---|---------------|------------------|-----------|
| 1 | **เพิ่ม 3 ธีมใหม่** | ทั้ง 4 ไฟล์ | 💎 One Dark (Atom), ☀️ Classic Light, 🌃 Cyberpunk Neon |
| 2 | **ลบ Warm Sand** | ทั้ง 4 ไฟล์ | เปลี่ยนเป็น Classic Light แทน |
| 3 | **เปลี่ยนชื่อ** | ทั้ง 4 ไฟล์ | กลับไปใช้ Classic Light (แก้จาก White) |
| 4 | **Reorder dropdown** | ทั้ง 4 ไฟล์ | Dark→Vintage→Neon→Cosmic→OneDark→White→Clay→Warm→Sage→Mist |

### 3 July 2026 — Layout Refinements (`kinematics_vt_graph_v1.html`)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **Animate → ใต้ slider** | ย้ายปุ่ม ▶ Animate ใน Analysis Tool (Non-uniform) ไปอยู่ด้านล่างของ time slider |
| 2 | **Uniform Parameters → Left column** | ย้าย 🎛️ Uniform Acceleration Parameters เข้าไปใน left column ใต้ graph-card (กว้างเท่ากับกราฟ) อยู่เหนือ Key Concept |
| 3 | **📖 Define → Equation card** | ย้ายปุ่ม Define + panel จาก Uniform Parameters ไปไว้ด้านล่างสุดของ Equation card (ฝั่งขวา) |
| 4 | **Fix layout break** | ลบ `</div>` เกินที่เหลือจาก definePanel — แก้ HTML structure ให้ถูกต้อง |
