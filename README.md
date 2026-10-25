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
│   ├── CH0_Fundamental_1_Vector_Addition_Lab.html    ← Vector Addition ➕
│   ├── CH0_Fundamental_2_Density.html                ← Density 📦
│   ├── CH0_Instrument_1_Vernier_Caliper.html         ← Vernier Caliper 📏
│   ├── CH0_Instrument_2_Micrometer_Screw_Gauge.html  ← Micrometer Screw Gauge 🔧
│   ├── CH0_Instrument_3_Balance_Newtonmeter.html     ← Mass vs Weight (Balance & Newtonmeter) ⚖️
│   ├── CH1_Mechanics_1_Motion_Graphs_Lab.html        ← Motion Graphs 🚗
│   ├── CH1_Mechanics_2_Newtons_Laws_Lab.html         ← Newton's Laws 🍎
│   ├── CH1_Mechanics_5_Moments_Equilibrium_Lab.html  ← Moments & Equilibrium ⚖️ (v2: 3-force scenes, choose-any-pivot, slope topple)
│   ├── CH1_Mechanics_6_Energy_Lab.html               ← Energy ⚡
│   ├── CH2_Thermal_1_Molecular_Models_Lab.html       ← Molecular Models ⚛️ (states + history + gas laws)
│   ├── CH2_Thermal_2_Thermal_Properties_Lab.html     ← Thermal Properties 🌡️ (heating/cooling curves · specific heat & latent heat · evaporation/boiling · expansion)
│   ├── CH2_Thermal_3_Heat_Transfer_Lab.html          ← Heat Transfer 🌡️ (Conduction · Convection · Radiation · Application)
│   ├── CH3_Wave_1_Introduction_to_Waves_v1.html      ← Introduction to Waves 🌊
│   ├── CH3_Wave_2_Refraction_of_Light.html           ← Refraction of Light 🔦
│   ├── CH3_Wave_3_Dispersion_of_Light.html           ← Dispersion of Light 🌈
│   ├── CH3_Wave_4_Optical_Instruments.html           ← Optical Instruments 🔭
│   ├── CH3_Wave_5_Diffraction_of_Waves.html          ← Diffraction of Waves 🌀
│   ├── CH4_Electricity_1_Electrostatics_Lab.html     ← Electrostatics ⚡
│   ├── CH4_Electricity_2_Circuit_Lab.html            ← Circuit Lab 🛠️
│   ├── CH4_Magnetism_1_Magnetic_Fields_Lab.html      ← Magnetic Fields 🧲
│   ├── CH4_Magnetism_2_Motor_Effect_Lab.html         ← Motor Effect 🔌
│   ├── CH5_Nuclear_1_Atomic_Models.html              ← Atomic Models ⚛️
│   ├── CH5_Nuclear_2_Nuclear_Symbols_Reactions.html  ← Nuclear Symbols & Reactions ☢️
│   ├── CH5_Nuclear_3_Radioactive_Lab.html            ← Radioactive Lab ☢️
│   ├── CH6_Space_1_Solar_System_Lab.html             ← Solar System 🌌
│   ├── CH6_Space_2_Star_Life_Cycle_Lab.html          ← Star Life Cycle ⭐
│   ├── CH6_Space_3_Universe_Lab.html                 ← Universe 🔭
│   └── AS/                                            ← A-Level 9702 sims
│       ├── AS_CH0_Fundamental_1_SI_Units_and_Homogeneity.html ← SI Units & Homogeneity 🧱
│       ├── AS_CH0_Fundamental_2_Uncertainty_and_Significant_Figures.html ← Uncertainty & Sig Figs ⚠️📏
│       ├── AS_CH0_Fundamental_3_Estimation.html ← Estimation & Order of Magnitude 🔢
│       ├── AS_CH3_Wave_1_Progressive_and_Stationary_Waves.html ← Progressive & Stationary Waves 〰️
│       ├── AS_CH3_Wave_2_Interference_and_Grating.html ← Interference & Diffraction Grating 🎯
│       ├── AS_CH3_Wave_3_Doppler_Effect.html         ← Doppler Effect & Redshift 🚨
│       ├── AS_CH3_Wave_4_Intensity_and_Polarisation.html ← Intensity & Polarisation 🔆
├── scripts/               ← Build system (Python)
│   ├── build.py           ← Main: python build.py lecture.md
│   ├── build_dashboard.py ← Dashboard generator
│   ├── parse_lecture.py   ← Markdown parser
│   ├── pdf_export.py      ← Playwright → A4 PDF
│   └── templates/         ← Jinja2 HTML templates
├── Junkyard/              ← Retired prototypes (vernier caliper, micrometer, old micrometer sim)
├── references/
│   ├── scientists/        ← Scientist Bio Library
│   ├── terminology/       ← Physics terminology (15 terms)
│   ├── historical-milestones/ ← 14 key experiments & discoveries (Torricelli → Atomic Bomb)
│   └── physical-quantity/ ← 18 in-depth reference files per physical quantity
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
| 1.1 | Physical Quantities & Measurement | ❌ | ✅ Vernier Caliper, Micrometer |
| 1.2 | Motion — Kinematics | ✅ Horizontal, Free-fall, Stopping, Advanced VT, Terminal Velocity 🪂 | ❌ |
| 1.3 | Mass and Weight | ❌ | ✅ Balance & Newtonmeter ⚖️ |
| 1.4 | Density | ❌ | ✅ Density 📦 |
| 1.5 | Forces (Hooke's Law) | ❌ | ❌ |
| 1.6 | Effects of Forces (Moments, Pressure) | ❌ | ✅ Moments & Equilibrium ⚖️ |
| 1.7 | Energy, Work & Power | ❌ | ❌ |
| 1.8 | Energy Resources | ❌ | ❌ |

> 💡 **Simulations** = virtual lab instruments / interactive phenomena (ไม่ใช่กราฟ). ปัจจุบันมี 27 labs: CH0 (Vernier Caliper 📏, Micrometer 🔧, Balance ⚖️, Vector Addition ➕, Density 📦), CH1 (Motion Graphs 🚗, Newton's Laws 🍎, Moments & Equilibrium ⚖️, Energy ⚡), CH2 (Molecular Models ⚛️, Thermal Properties 🌡️, Heat Transfer 🌡️), CH3 (Waves 🌊), CH4 (Electricity ⚡, Magnetism 🧲), CH5 (Nuclear ☢️), CH6 (Solar System 🌌, Star Life Cycle ⭐, Universe 🔭)

## 🎯 Features

- **5-part lecture structure**: 📜 History → 🌍 Nature → ⚛️ Theory → 📊 Graphs → ✍️ Examples
- **Interactive graphs**: Real-time animation with Canvas 2D (horizontal motion 🚗, free fall 🍎, stopping distance 🚘, advanced VT graph 📈, terminal velocity skydive 🪂)
- **Interactive physics simulations**: Virtual lab instruments และ interactive phenomena ที่ไม่ต้องใช้กราฟ
  - 📏 **Vernier Caliper** — 3 modes (Simulate/Practice/Quiz), 3 difficulty levels, zoom double-click, zero error ±5 div, workpiece clamping
  - 🔧 **Micrometer Screw Gauge** — 0–25 mm, LC 0.01 mm, drag-to-rotate thimble, sleeve + thimble scale, magnifier overlay, tutorial animation, practice/exam mode, 3 themes
  - ⚖️ **Balance & Newtonmeter (Mass vs Weight)** — ลาก masses (100 g–2 kg, ซ้อนได้ 5 ชิ้น) ขึ้นเครื่องชั่งดิจิทัล (g/kg) หรือแขวน spring balance (N), 4 ดาว (Earth/Moon/Mars/Jupiter), Simple (g=10, Earth เท่านั้น) ⇄ Location (g จริงต่อดาว), Newtonmeter range 0–5/0–10/Auto + over-range warning, force arrow W=mg, 3 modes (Simulate/Practice/Quiz)
  - ⚛️ **Kinetic Particle Model** — 3 modes (States of Matter: solid/liquid/gas particles + changes of state · Particle Motion: temp↔motion, Brownian motion, diffusion, absolute zero −273°C · Gas Pressure: pressure from wall collisions, p↔T(K), pV=constant Boyle, Kelvin↔Celsius), Layout B 70/30, zoom ×2 + hold-drag pan
  - 🌡️ **Thermal Properties** — 3 modes (Thermal Expansion: bimetallic strip, thermometer, gas, solids+applications · Specific Heat Capacity: c=ΔQ/(mΔθ), measure c of a solid & water via E=IVt, compare materials · Melting/Boiling/Evaporation: heating curve with latent-heat plateaus 0°C/100°C, evaporation cooling, boiling vs evaporation), Layout B 70/30, zoom ×2 + hold-drag pan
  - 🌡️ **Heat Transfer Lab — Thermal** — 4 modes (Conduction: molecular lattice + free electrons toggle + rods experiment with 🌡️ IR thermometer; Convection: wall-AC / floor-heater rooms · smoke box · dye beaker · sea & land breeze; Radiation: Leslie's cube + absorption/emission races + vacuum flask + Earth's balance (greenhouse) with atomic reasoning; Application: 7 real objects with colour-coded mechanism breakdown), Layout B 70/30, zoom ×2 + hold-drag pan
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

### 25 Oct 2026 — CH6 Solar System `v1.0.8` (Sun surface polish)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **ผิวดวงอาทิตย์สว่างขึ้น** | เปลี่ยนพาเลตต์ granule เป็นโทนขาว-ทองสว่าง, ทำ lanes ระหว่าง granule ให้แคบและจางลง (อ่านเป็นแก๊สสว่าง ไม่ใช่รอยแตก) |
| 2 | **เพิ่ม bloom/glare** | ใส่ชั้นเรืองแสง (`lighter` composite) ทับจานดาว เพื่อให้สายตาจับที่ชั้นบรรยากาศมากกว่าพื้นผิว |
| 3 | **เอา sunspot ออก** | จุดมืดบนดวงอาทิตย์ไม่ใช่เนื้อหาของบทนี้และดึงสายตาไปจากชั้น — ฟังก์ชัน `sunspot()` ยังเก็บไว้ให้ใช้ซ้ำ |

### 24 Oct 2026 — CH6 Space Physics 3 / Universe `v1.1.0` (`simulations/CH6_Space_3_Universe_Lab.html`) · IGCSE 0625 Topic 6

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **4 โหมดย่อย × 16 pills** | ① History (🌌 Now · 🔭 1920s Great Debate · 🌞 Copernicus→Galileo · 🏛️ Ptolemy & the fixed stars) ② Present Model (🏗️ Structure & scale · 🪜 Scale ladder · 💥 Big Bang model · ❓ What it does not say) ③ Evidence (🎵 Doppler → Redshift · 📡 CMB · 🧪 Light elements · 🌌 Distant galaxies look young · ⏳ Discovery timeline) ④ Hubble Law (📈 v–d graph · H₀ · 🕯️ Measuring d · ⏳ Age = 1/H₀) |
| 2 | **History ย้อนยุค** | era scrubber 4 จุด (Now อยู่ซ้าย → อดีตอยู่ขวา) + mythology 3 เรื่อง (Helios · Atlas · นมที่หก → ที่มาคำว่า galaxy) → ปรัชญากรีก → Ptolemy |
| 3 | **หลักฐาน** | Doppler 3 ขั้น (รถพยาบาล 700 Hz → 1171 Hz → สเปกตรัมเลื่อน → 4 galaxy เรียง z) · CMB 2.725 K ± 0.0002 K (1:100 000) ปล่อยที่ z ≈ 1100 · Steady State แพ้เพราะไม่มี CMB |
| 4 | **Hubble** | dataset `Simple: 6` / `Full: 8` · v/d = 68.0 km/s per Mpc · H₀ = 2.2 × 10⁻¹⁸ s⁻¹ · 1/H₀ = 14.4 พันล้านปี + accepted age 13.8 |
| 5 | **มาตรฐาน** | 6 themes / KaTeX offline / zoom ×2 + hold-drag pan / panel 4 tabs พับได้ / Practical 8 · Quiz 20 / badge v1.1.0 / window.S |

### 22 Oct 2026 — CH2 Thermal Properties `v1.1.9` (refinement pass)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **Ice raft** | ก้อนน้ำแข็งลอยเป็นแพ จมลงใต้น้ำ ≈ 9/10 ตามหลักการลอย + แกว่งเบา ๆ ตอนลอย (เดิมเรียงเป็นกองซ้อนขึ้นเหนือผิวน้ำ) |
| 2 | **Ring 3-D** | วงแหวนในโหมดขยายตัววาดเป็นท่อกลมมองเกือบข้าง (ellipse + gradient เงาเข้มสองข้าง) แทนวงแบน |
| 3 | **Shared liquid** | รวมตัววาดของเหลวเป็น `m2Liquid()` ตัวเดียว — หม้อต้ม / บีกเกอร์ / หลอด ใช้ผิวน้ำชุดเดียวกันให้ตรงกันทุกฉาก |

### 22 Oct 2026 — CH2 Thermal Properties รวมเป็นไฟล์เดียว `v1.1.7` · CH6 Star Life Cycle `v1.1.1`

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **Thermal Properties: v2 กลายเป็นไฟล์หลัก** | `CH2_Thermal_2_Thermal_Properties_Lab.html` = เนื้อหา `v1.1.7` (heating/cooling curves · specific heat & latent heat · evaporation/boiling · expansion) — ลบไฟล์คู่ `_v2.html` ออก และเก็บฉบับ `v1.0.3` เดิมไว้ใน Junkyard |
| 2 | **Star Life Cycle `v1.1.1`** | กราฟ star data: ป้ายแกนอ่านง่ายขึ้น (`M = million` / `B = billion`) + ตัวอักษร tick ใหญ่ขึ้น |
| 3 | **จำนวน labs** | 27 → 26 (Thermal Properties เหลือไฟล์เดียว) |

### 20 Oct 2026 — CH6 Space Physics 2 / Star Life Cycle `v1.0.9` (`simulations/CH6_Space_2_Star_Life_Cycle_Lab.html`) · IGCSE 0625 Topic 6

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **4 โหมดย่อย** | ① Radiation (🌈 Spectrum · 🎨 Colour & temperature · 💡 Fusion · ⚖ Stability · 🌟 Cepheid variable) ② Low mass (🌱 Birth · ☀ Stable star · 🔴 Red giant · 🌫 Planetary nebula + white dwarf · ⏱ Timeline) ③ Massive (🌱 Shared trunk · 🔴 Red supergiant · 💥 Supernova · ⚫ Remnant · ♻ New stars) ④ H-R Diagram (📈 The diagram · ☀ Where the Sun sits · ➡ Evolution tracks · 📊 Star data) |
| 2 | **เนื้อหาหลัก** | รังสี IR 50 % / visible 43 % / UV 7 % · fusion 4 H → He + mass defect `E = mc²` · สมดุล gravity ⇄ radiation pressure · trunk เดียวแยก 2 สาขาที่ ≈ 8 M☉ · iron problem · supernova 99 % neutrino · planetary nebula name trap (Herschel) · วัฏจักรกลับเป็นดาวใหม่ |
| 3 | **H-R diagram** | แกนอุณหภูมิกลับด้าน `hotter ← → cooler` · 4 regions · ดาวจริง ≥10 ดวง · 2 evolution tracks (1 M☉ / 15 M☉) · absolute magnitude + spectral classes |
| 4 | **มาตรฐาน** | 6 themes / KaTeX offline / zoom ×2 + hold-drag pan / side panel 4 tabs พับได้ / Practical 8 · Quiz 20 (5/โหมดย่อย) / badge v1.0.9 / window.S |

### 20 Oct 2026 — CH6 Space Physics 1 / Solar System `v1.0.7` (อัปเดตในที่)

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **Eclipse ลึกขึ้น** | มุมมองจากด้านบน (`SEEN FROM ABOVE`) + umbra/penumbra + ระยะยกของวงโคจรดวงจันทร์เหนือระนาบ (`height above the orbit plane` → อธิบายว่าทำไมคราสไม่เกิดทุกเดือน) |
| 2 | **ผิวดวงอาทิตย์** | sunspot + prominence + ผิวแบบมีเทกซ์เจอร์ (เดิมเป็นวงกลมเรียบ) |
| 3 | **Hover labels** | ชี้ที่วัตถุบน canvas แล้วขึ้นป้ายชื่อ/ค่า (เดิมต้องคลิก) |

### 19 Oct 2026 — CH6 Space Physics 1 / Solar System `v1.0.4` (`simulations/CH6_Space_1_Solar_System_Lab.html`) · IGCSE 0625 Topic 6

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **3 โหมดย่อย** | ① Our Solar System (⭐ Star · 🪐 Planets · ☄️ Asteroids · 🌠 Comet · 🛰️ Tour) ② Earth and Moons (Day & Night · Seasons · Moon Phases · Eclipses) ③ Orbits (Accretion Model · Gravity & Orbits · Elliptical Orbits · Planetary Data) |
| 2 | **ข้อมูลจริง** | 8 ดวง + Pluto/Ceres คลิกได้ → การ์ดข้อมูล Ø / ระยะ / คาบ / ดวงจันทร์ / บรรยากาศ / วงแหวน · scale 2 โหมด (`Sizes to scale` + `True ⋆ distances` / `Compact`) · หาง comet ชี้ออกห่างดวงอาทิตย์เสมอ (ion ตรง + dust โค้ง) · 2 มุมมองคู่ (อวกาศ + ผู้สังเกตบนโลก) |
| 3 | **Interaction** | zoom ×2 ด้วย double-click + กดค้างลากเลื่อนอิสระ · side panel 4 tabs + ย่อ/ขยายทุกหัวข้อ · equal-areas sweep + energy bar (KE/PE/total) · log-log `T² ∝ r³` · Practical 6 ข้อ · Quiz 15 ข้อ (5/โหมดย่อย) |
| 4 | **มาตรฐาน** | 6 themes / KaTeX offline / badge v1.0.4 / window.S |

### 11 Oct 2026 — AS/Estimation & Order of Magnitude `v1.0.1` (`simulations/AS/AS_CH0_Fundamental_3_Estimation.html`) · A-Level 9702 Chapter 0

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **3 โหมด** | ① Order of Magnitude (บันได 10ⁿ + อ่าน order จากเลข) ② Estimation Method (Fermi builder ต่อสมมติฐาน `×÷` → ปัด order) ③ Practice (P1–P6) |
| 2 | **Scenario** | มวลรถ `~10³kg` · โมเลกุลในหยดน้ำ `~10²¹` · พลังงานมนุษย์ `~10²W` · ข้าว 1 ถุง `~5×10⁴` |
| 3 | **มาตรฐาน** | 6 themes / KaTeX offline / badge v1.0.1 / window.S |

### 10 Oct 2026 — AS/Uncertainty & Significant Figures `v1.1.1` (`simulations/AS/AS_CH0_Fundamental_2_Uncertainty_and_Significant_Figures.html`) · A-Level 9702 Chapter 0

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **3 โหมดใหม่** | ① Data & Errors (systematic/random, instrument, N น้อย→มาก/SD) ② Uncertainty Math (Abs/Rel/%, operators +−×÷xⁿ, graph+error bars, least DP/SF report) ③ Problem Solving (โจทย์จริง Q1–Q10) |
| 2 | **อ้างอิงไฟล์จริง** | Mode 2 ตามวิธี lecture ลายมือ (`Lecture.pdf`); Mode 3 ทำโจทย์จริงจาก `Uncertainty.pdf` (10 ข้อ) |
| 3 | **Operator machine** | +−→รวม absolute, ×÷→รวม % , power→×n (x³/∛x เพิ่ม) + result รูป `(a±b)×10ⁿ` สำหรับค่าใหญ่/เล็ก |
| 4 | **UI** | box width ปรับ, 💬 Hints default off, s.f. box ชี้ลงถึงหลักที่รายงาน; badge v1.1.1 / KaTeX offline / 6 themes |
| 5 | **เอกสาร** | `Uncertainty_v1.0.7_Changes.xlsx` — change log + box widths + วิธีทำ Example 2 แนบในโฟลเดอร์ |

### 8 Oct 2026 — AS/SI Units & Homogeneity `v1.1.7` (`simulations/AS/AS_CH0_Fundamental_1_SI_Units_and_Homogeneity.html`) · A-Level 9702 Chapter 0

| # | การเปลี่ยนแปลง | รายละเอียด |
|---|---------------|-----------|
| 1 | **โจทย์จริงจาก PDF** | เอาโจทย์ข้อสอบ SI Units (จาก `0. SI Units.pdf`) มาเป็น exercise bank — prefix / homogeneity / derive unit ตามข้อจริง |
| 2 | **Prefix เต็มสเกล** | ตาราง prefix `tera→atto` + เครื่องแปลง (`nm→pm`, `MW→W`, `kΩ→Ω`) + ฝึกแปลงข้อสอบ |
| 3 | **Homogeneity คมขึ้น** | พิสูจน์ LHS=RHS + distractor ผิด, highlight จุดที่หน่วยไม่สมดุล |
| 4 | **UI/เครื่องมือ** | natural-display calculator + unit keypad โดยรวม 6 themes / KaTeX offline / badge v1.1.7 |

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
