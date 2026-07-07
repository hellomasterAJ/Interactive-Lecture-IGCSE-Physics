---
title: Capacitance
field: Electricity & Magnetism
type: physical-quantity
si_unit: farad (F)
symbol: C
dimension: [M⁻¹·L⁻²·T⁴·I²] = [C/V]
version: 1
tags: [electricity, capacitance, si-units, history, circuits]
related_lectures: []
related_terminology: []
related_physical_quantity: [charge, voltage, energy, time-constant, frequency]
---

# 🔋 Capacitance

## 📜 ประวัติศาสตร์ของตัวเก็บประจุ

### จุดเริ่มต้น — Leyden Jar

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1745** | **Pieter van Musschenbroek** (Leiden, เนเธอร์แลนด์) | **Leyden Jar** — ขวดแก้วหุ้มด้วยฟอยล์โลหะทั้งภายในและภายนอก → เมื่อประจุ → เก็บไฟฟ้าไว้ได้นาน! — **ตัวเก็บประจุ (capacitor) เครื่องแรกของโลก** |
| **1746** | William Watson | ปรับปรุง Leyden Jar — เคลือบผิวใน-นอก → จุประจุมากขึ้น |
| **1747** | Benjamin Franklin | ใช้ Leyden Jar หลายใบต่อขนาน → เก็บประจุได้มากขึ้น → เรียกว่า **"electrical battery"** — รากศัพท์ของคำว่าแบตเตอรี่! |
| **1748** | **Able to kill** | Franklin ทำให้ไก่ตายด้วยไฟฟ้าจาก Leyden Jar (เป็นข่าวดัง) |
| **1752** | Franklin | ใช้ Leyden Jar เก็บประจุจากฟ้าผ่าในการทดลองว่าว |

### ศตวรรษที่ 19 — Capacitor เริ่มมีทฤษฎี

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1837** | Michael Faraday | ศึกษา **dielectric** — วางฉนวนระหว่างแผ่นโลหะ → ประจุมากขึ้น → เรียกว่า "เฉพาะ electric capacity" |
| **1837** | **Faraday** | เสนอว่า ε_r (relative permittivity) — วัสดุต่างชนิดกัน → เก็บประจุได้มากขึ้น ≠ เท่า |
| **1853** | William Thomson (Lord Kelvin) | ตั้งทฤษฎีการคายประจุของ capacitor → ตีพิมพ์สมการ V(t) = V₀e^(−t/RC) |
| **1862** | Maxwell | รวม capacitor ในสมการ EM → displacement current → เสร็จสมบูรณ์ของ Maxwell's equations |
| **1881** | International Electrical Congress (Paris) | ตั้งชื่อหน่วยความจุไฟฟ้า **farad (F)** ตาม Michael Faraday |

### ศตวรรษที่ 20 — เทคโนโลยี capacitor

| ปี | นวัตกรรม |
|----|----------|
| **1909** | **Electrolytic capacitor** — ใช้ oxide film บน aluminium → จุมากแต่ขนาดเล็ก |
| **1920s** | **Variable capacitor** — หมุนแผ่นโลหะ ←→ เปลี่ยน C → ใช้ในวิทยุเพื่อปรับสถานี |
| **1930s** | **Mica capacitor** — เสถียรสูง สำหรับ RF |
| **1950s** | **Ceramic capacitor** (BaTiO₃) — ε_r สูงมาก (>1,000) → เล็ก+จุมาก |
| **1958** | **Tantalum capacitor** — MnO₂ dielectric → capacitor ขนาดเล็กสำหรับวงจรพิมพ์ |
| **1970s** | **Supercapacitor** (double-layer capacitor) → จุ F–kF (!!) |
| **1990s** | **MLCC (Multi-Layer Ceramic Capacitor)** — 500+ ชั้นในชิปตัวเดียว |
| **2010s** | **Graphene supercapacitor** — กำลังไฟสูง จุมาก ชาร์จเร็ว |
| **ปัจจุบัน** | TiN (MOS capacitor) — finFET gate capacitance ระดับ attofarad (aF) |

---

## ⚛️ คำนิยามของ 1 ฟารัด

### Derived Unit
> "1 farad = **the capacitance of a capacitor between which a potential difference of 1 volt stores a charge of 1 coulomb**"

```
1 F = 1 C/V = 1 A·s/V = 1 s/Ω = 1 kg⁻¹·m⁻²·s⁴·A²
```

### ความจุของ capacitor แบบแผ่นขนาน (Parallel Plate)
```
C = ε₀·ε_r·A/d

โดยที่:
  C  = capacitance (F)
  ε₀ = permittivity of free space ≈ 8.854 × 10⁻¹² F/m
  ε_r = relative permittivity (dielectric constant) ของวัสดุ
  A  = พื้นที่ของแผ่น (m²)
  d  = ระยะห่างระหว่างแผ่น (m)
```

### ตัวอย่างขนาด
| ตัวอย่าง | r | A | d | C |
|----------|---|---|---|-|
| Chip capacitor บน PCB | — | — | — | **~pF – μF** |
| Power supply capacitor | — | — | — | **~μF – mF** |
| Supercapacitor | — | — | — | **~1 – 3,000 F** |
| โลกเทียบกับบรรยากาศ | ≈ 6,371 km | 5.1×10¹⁴ m² | ~100 km | **~0.0007 F** (~700 μF) |
| แบบ 2 แผ่น (d=1 mm, A=1 m², air) | 1 | 1 m² | 0.001 m | **≈ 8.85 nF** |

### ค่า ε_r ของวัสดุต่างๆ

| วัสดุ | ε_r (relative permittivity) |
|-------|---------------------------|
| **Air/vacuum** | 1.00059 (~1) |
| **Teflon (PTFE)** | 2.1 |
| **Paper** | ~2–4 |
| **Glass** | ~5–10 |
| **Mica** | 5–7 (เสถียรมาก → ใช้ใน RF capacitor) |
| **Silicon dioxide (SiO₂)** | 3.9 |
| **Ceramic X7R** | ~2,000 |
| **Barium titanate (BaTiO₃)** | ~5,000–10,000 |
| **Water (H₂O)** | ~80 |
| **High-k (HfO₂)** | ~20–30 — ใช้ใน transistor gate |
| **PZT (piezoelectric)** | ~500–3,000 |

---

## 🔬 เครื่องมือวัด / ประเภทของ Capacitor

### ตามชนิดของ Dielectric

| ประเภท | Dielectric | ช่วง C | ข้อดี | ข้อเสีย |
|---------|-----------|--------|-------|---------|
| 🧈 **Paper** | Paper + oil | ~1 nF–10 μF | ราคาถูก | เสถียรภาพต่ำ, ใหญ่ |
| 🟤 **Ceramic (MLCC)** | BaTiO₃, ฯลฯ | ~0.5 pF–100 μF | เล็ก, ราคาถูก, มาตรฐาน SMD | อุณหภูมิเปลี่ยนค่า (บางรุ่น) |
| 🟣 **Mica** | Mica | ~1 pF–10 nF | เสถียรมาก, Q สูง → RF | แพง |
| 🔵 **Polyester (Mylar)** | PET film | ~1 nF–1 μF | เสถียร, ราคาไม่แพง | ไม่เหมาะกับความถี่สูง |
| 🔵 **Polypropylene (PP)** | PP film | ~1 nF–100 μF | เสถียร+low loss → audio crossover | ใหญ่ |
| 🟢 **Electrolytic (Al)** | Al₂O₃ | ~1 μF–10 mF | จุมาก, ราคาถูก | มีขั้ว (+/−), อายุจำกัด, leaky |
| 🟢 **Tantalum** | Ta₂O₅ | ~0.1 μF–1 mF | จุมากต่อปริมาตร, เสถียรกว่า Al | ราคาแพง, ระเบิดได้ถ้า reverse bias |
| 🔴 **Variable (trimmer)** | Air / ceramic | ~2–100 pF | หมุนปรับ C ได้ | ใช้ปรับความถี่ RF |
| ⚡ **Supercapacitor (EDLC)** | Carbon + electrolyte | ~1–3,000 F | จุมหาศาล, ชาร์จเร็ว | แรงดันต่ำ (2.7–3 V), ราคาต่อ F ถูกลงเรื่อยๆ |
| 🔬 **MOS capacitor** | SiO₂ / HfO₂ | ~0.1 fF–pF | ใน transistor gate | ขนาด nm |

---

## 📐 หน่วยของความจุไฟฟ้า

### SI Unit
| หน่วย | สัญลักษณ์ | คำนิยาม |
|-------|-----------|---------|
| **farad** | F | 1 F = 1 C/V |

### SI Prefixes

| หน่วย | สัญลักษณ์ | ค่า | ใช้ที่ไหน |
|-------|-----------|-----|----------|
| **attofarad** | aF | 10⁻¹⁸ F | Gate capacitance (transistor: ~0.1–1 aF/nm) |
| **femtofarad** | fF | 10⁻¹⁵ F | FinFET gate, nano-devices |
| **picofarad** | pF | 10⁻¹² F | RF circuit, crystal load cap |
| **nanofarad** | nF | 10⁻⁹ F | Decoupling in digital circuits |
| **microfarad** | μF | 10⁻⁶ F | Power supply filter, audio coupling |
| **millifarad** | mF | 10⁻³ F | Power supply bulk |
| **farad** | F | 1 | Supercapacitor (F – kF) |
| **kilofarad** | kF | 10³ F | Supercapacitor bank |
| **Planck capacitance** | — | ≈ 1.2 × 10⁻⁴² F | quantum gravity scale |

---

## 🌍 การใช้งานในชีวิตจริง

| การใช้งาน | เกี่ยวข้องกับ |
|-----------|-------------|
| 🔌 **Power supply filter** | Capacitor ขนาดใหญ่ → เก็บประจุระหว่าง peak → เรียบ DC |
| 📻 **วงจรปรับความถี่วิทยุ** | Variable capacitor + coil → LC resonant circuit → เลือกสถานี |
| 🔊 **Audio crossover** | ตัวเก็บประจุผ่านความถี่สูง → แยกให้ tweeter vs woofer |
| ⏱️ **Timer (555 IC, RC delay)** | Charging/discharging R-C → หน่วงเวลา |
| 💾 **DRAM memory** | 1 bit = 1 capacitor + 1 transistor → charge = '1', discharge = '0' |
| ⚡ **Supercapacitor (UPS)** | เก็บไฟสำรองระยะสั้น (รถเข็นไฟฟ้า, แบตสำรอง) |
| 🔬 **Sensor** | Capacitive touch screen, pressure sensor, humidity sensor |
| 🖥️ **CPU** | Gate capacitance หลายๆ ชั้น → delay ในการสลับ state → limit ความเร็ว |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Capacitor เก็บประจุได้มาก → ตัวใหญ่" | จริง + ขึ้นกับ dielectric: supercapacitor จุ kF ในกระป๋องเล็ก vs ตัวใหญ่บางตัวจุแค่ μF |
| "Capacitor ไม่มี polarity" | **เฉพาะ ceramic, film, mica** — electrolytic และ tantalum มีขั้ว! สลับ → ระเบิด! |
| "Capacitor เมื่อ charged = battery" | ไม่ — battery จ่ายไฟได้นาน (chemical reaction) — capacitor คายประจุหมดในเวลา τ = RC |
| "Capacitor ตัวเดียวกัน C คงที่ที่ทุกความถี่" | **ไม่** — ที่ RF → มี parasitic inductance (ESL) → impedance เปลี่ยน |
| "Capacitance (F) = charge (C)" | **ไม่** — C = Q/V → C คงที่ Q เปลี่ยนตาม V |
| "Capacitor ต่ออนุกรม = C_total = C₁ + C₂" | **ผิด** — อนุกรม: 1/C_total = 1/C₁ + 1/C₂ (เหมือน R ขนาน) — ขนาน: C_total = C₁ + C₂ |

### 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. Displacement current ของ Maxwell — ที่ capacitor มีกระแสไหลผ่าน dielectric?**
เมื่อ capacitor charging: current ในวงจรภายนอก I = dQ/dt — แต่ระหว่างแผ่น? ไม่มีประจุไหลผ่าน dielectric โดยตรง → Maxwell บอกว่า **"displacement current"** (ε₀·∂E/∂t) ไหลแทน → นี่คือ key ที่ทำให้คลื่น EM มีอยู่จริง!

**2. ทำไม capacitor ถึง "ผ่าน AC ไม่ผ่าน DC"?**
ที่ DC (f = 0): Z_C = 1/(2πfC) = ∞ → เหมือน开路 (open)
ที่ AC (f > 0): Z_C = 1/(2πfC) → ยิ่ง f สูง Z_C ยิ่งต่ำ → กระแสยิ่งไหลง่าย
— ที่ f → ∞, Z_C → 0 → capacitor = short

**3. Quantum Capacitance — 2D materials (graphene)**
ใน 2D materials — ความจุไม่ได้มาจาก geometry (ε₀A/d) เท่านั้น — แต่มี **quantum capacitance** (C_Q) เพิ่มเติมที่เปลี่ยนตาม Fermi level (density of states) — C_Q ≈ 2 μF/cm² สำหรับ graphene → ใน 2D material capacitor total = (1/C_geo + 1/C_Q)⁻¹

**4. Supercapacitor — ทำไม C ถึงมหาศาล?**
ใช้ **electric double layer (EDL)** — เมื่อ electrode สัมผัส electrolyte → ชั้นไอออน ~0.3–1 nm ห่างจาก electrode → d เล็กมาก → C = ε₀·ε_r·A/d โดย d ~0.5 nm → C ~10 μF/cm² (เทียบกับ ceramic cap ~10–100 nF/cm²) + use activated carbon (A = 1,000–2,000 m²/g) → ได้ F–kF!

**5. Negative capacitance — เป็นไปได้ไหม?**
ใน ferroelectric materials (เช่น PZT, BaTiO₃) — มีช่วงที่ C < 0 (dV/dQ < 0) — เกิดจากการตอบสนองของ polar domains — ใช้ใน transistor gate เพื่อลด subthreshold swing → transistor ที่กินไฟน้อยลง!

## 🔗 อ้างอิง

- Faraday, M. (1837). "Experimental Researches in Electricity – On Induction"
- Maxwell, J. C. (1873). *A Treatise on Electricity and Magnetism*
- Musschenbroek, P. van (1746). จดหมายถึง Réaumur — รายงานการค้นพบ Leyden Jar
- von Klitzing, K. (1980). Quantum Hall Effect — R_K standard indirectly used
- Conway, B. E. (1999). *Electrochemical Supercapacitors*
- BIPM (2019). *The International System of Units (SI) — 9th edition*
- Luryi, S. (1988). "Quantum capacitance devices" — *Applied Physics Letters*
- Salahuddin, S. & Datta, S. (2008). "Use of Negative Capacitance to Provide Voltage Amplification" — *Nano Letters*