---
title: Density
field: Mechanics — Matter
type: physical-quantity
si_unit: kilogram per cubic metre (kg/m³)
symbol: ρ (rho)
dimension: [M·L⁻³]
version: 1
tags: [density, matter, buoyancy, fluids, si-units]
related_lectures: [topic14_density]
related_terminology: []
related_physical_quantity: [mass, volume, pressure, buoyancy]
---

# 🪨 Density

> **Density = มวลต่อหน่วยปริมาตร**
>
> ρ = m/V — SI unit: kg/m³

---

## 📜 ประวัติศาสตร์

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~250 BCE** | **Archimedes** 💡 | **Eureka!** — อาบน้ำ → น้ำล้น → คำนวณปริมาตรของมงกุฎ |
| | | → เปรียบเทียบ density ของทองกับมงกุฎ → พิสูจน์ช่างทองโกง! |
| | | → ตั้ง **Archimedes' Principle** (แรงลอยตัว = น้ำหนักของน้ำที่ displaced) |
| **~200 BCE** | ชาวโรมัน | ใช้ density เพื่อตรวจสอบ纯度ของทองคำและโลหะมีค่า |
| **~1000** | Al-Biruni | วัด density ของสารต่างๆ อย่างเป็นระบบ 18 ชนิด |
| **~1600** | Galileo | ศึกษาว่าทำไมวัตถุบางอย่างลอย บางชนิดจม |
| **~1800** | **Davy, Dalton** | Atomic theory → density สัมพันธ์กับ atomic mass |
| **~1900** | **Archimedes principle** | ใช้ density ในการแยกแร่ (mineral processing) |

---

## ⚛️ นิยามทางฟิสิกส์

### Density
```
ρ = m/V

สำหรับวัสดุผสม:
ρ_avg = m_total / V_total
```

### Relative Density (Specific Gravity)
```
relative density = ρ_substance / ρ_reference

โดย ρ_reference = ρ_water ที่ 4°C = 1,000 kg/m³
ρ_water = 1 g/cm³ = 1,000 kg/m³

ตัวอย่าง:
ทอง (Au): ρ = 19,300 kg/m³ → relative density = 19.3
ไม้: ρ = 500 kg/m³ → relative density = 0.5
```

### Archimedes' Principle
```
F_buoyancy = ρ_fluid · V_displaced · g

ถ้า ρ_object > ρ_fluid → จม
ถ้า ρ_object = ρ_fluid → ลอย (neutral buoyancy)
ถ้า ρ_object < ρ_fluid → ลอย (บางส่วนเหนือน้ำ)
```

---

## 📐 Density ของสารต่างๆ

| วัสดุ | ρ (kg/m³) | เทียบกับน้ำ |
|------|-----------|-------------|
| **Plasma (core of Sun)** | ~1.5×10⁵ | 150× |
| **Osmium (Os) — หนาแน่นสุด** | **22,590** | 22.6× |
| **Iridium (Ir)** | 22,560 | 22.6× |
| **Platinum (Pt)** | 21,450 | 21.5× |
| **Gold (Au)** | 19,320 | 19.3× |
| **Mercury (Hg)** | 13,546 | 13.5× |
| **Lead (Pb)** | 11,340 | 11.3× |
| **Silver (Ag)** | 10,490 | 10.5× |
| **Copper (Cu)** | 8,960 | 9.0× |
| **Iron (Fe)** | 7,874 | 7.9× |
| **Earth (average)** | 5,514 | 5.5× |
| **Aluminium (Al)** | 2,700 | 2.7× |
| **Water (4°C)** | **1,000** | **1** |
| **Ice (0°C)** | 917 | 0.92 — ลอยน้ำ! |
| **Wood (oak)** | ~750 | 0.75 |
| **Oil (vegetable)** | ~920 | 0.92 |
| **Air (20°C, 1 atm)** | **1.204** | 0.0012 |
| **Helium (at STP)** | 0.1786 | 0.000179 |
| **Neutron star** | **~10¹⁷** | 10¹³× |
| **Black hole (event horizon)** | จนถึง ∞ | — |

### หน่วย

| หน่วย | ค่า (kg/m³) |
|-------|-------------|
| **SI: kg/m³** | 1 |
| **g/cm³** | 1,000 (1 g/cm³ = 1,000 kg/m³) |
| **g/L** | 1 (1 g/L = 1 kg/m³) |
| **oz/ft³** | 1.0012 |

---

## 🌍 การใช้งานในชีวิตจริง

| การใช้งาน | เกี่ยวข้องกับ |
|-----------|-------------|
| 🛳️ **เรือลอยน้ำ** | เหล็ก density 7,800 แต่เรือมีช่องว่าง → ρ_avg < 1,000 → ลอย |
| 🔥 **พายุหมุน** | อากาศร้อน (ρ↓) ลอย → พื้นที่ความกดอากาศต่ำ |
| 🧂 **ทะเลเดดซี** | ความเค็มสูง → ρ > 1,200 kg/m³ → ลอยตัวง่าย |
| 🪨 **แยกแร่** | Heavy liquid separation — ใช้ density ต่างกันแยก ore vs gangue |
| 🚰 **ท่อน้ำ** | น้ำเย็น ρ > น้ำร้อน → การพาความร้อน (convection) |
| 🎈 **บอลลูน** | He: ρ=0.178 < ρ_air=1.204 → ลอย |
| 🌡️ **Thermohaline circulation** | ความแตกต่างของ ρ (เค็ม+เย็น = จม) ขับเคลื่อนกระแสน้ำโลก |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "เหล็กหนักกว่าไม้" | **ไม่ใช่คำถามที่ถูก** — ต้องเทียบ **มวลเท่ากัน**: เหล็ก 1 kg vs ไม้ 1 kg = มวลเท่ากัน แต่ density ต่างกัน → ปริมาตรต่างกัน |
| "ของแข็ง density > ของเหลว" | **ไม่เสมอ** — น้ำแข็ง (917) < น้ำ (1,000) → ลอย — มีสารไม่กี่ชนิดที่ density ลดลงเมื่อแข็งตัว |
| "น้ำทะเลมี density = น้ำจืด" | น้ำทะเล ≈ 1,025 kg/m³ — เค็ม = เพิ่ม ρ — ทะเลเดดซี ≈ 1,240 |
| "วัตถุที่มี ρ มากกว่าจะจมเสมอ" | ในของไหล? ใช่ — แต่ถ้ามีแรงอื่น (surface tension, drag) → ขนาดเล็กมากอาจลอย |
| "Density = constant เสมอ" | **ไม่** — เปลี่ยนตาม T และ P — น้ำที่ 4°C = 1,000 → 100°C ≈ 958 |

### 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. Neutron star density — สสารที่หนาแน่นที่สุดในจักรวาล**
ρ_ns ≈ 2 × 10¹⁷ kg/m³ (200,000,000,000,000 เท่าของน้ำ)
— น้ำตาล 1 ก้อน (5 cm³) จาก neutron star = มวล ≈ **1 พันล้านตัน**
— ถ้าโลหะมี density ≈ 10⁴ → neutron star หนาแน่นกว่า 10¹³ เท่า!

**2. Convection current — density gradient ขับเคลื่อนกระแส**
ของไหล: ρ ↓ (ร้อน) → ลอย, ρ ↑ (เย็น) → จม
→ เกิด convection = การถ่ายเทความร้อนจากล่างขึ้นบน
— ในหม้อต้มน้ำ, ในบรรยากาศ, ในแก่นโลก, ในดวงอาทิตย์

**3. Black hole density**
หลุมดำไม่ใช่ "วัตถุ" — แต่มี "average density" ตามขอบฟ้าเหตุการณ์:
```
ρ_avg = M / (4/3 π R³)
โดย R = 2GM/c² (Schwarzschild radius)

→ ρ_avg ∝ 1/M²
— หลุมดำมวลน้อย: ρ_avg สูงมาก
— หลุมดำมวลดาราจักร: ρ_avg ≈ ρ_air (1.2 kg/m³)!
```
สรุป: หลุมดำยิ่งใหญ่มาก → ความหนาแน่นเฉลี่ยของมันยิ่งต่ำ!

---

## 🔗 อ้างอิง

- Archimedes (~250 BCE). *On Floating Bodies*
- Al-Biruni (~1000). *Determination of the Specific Gravities*
- Galileo (1638). *Discorsi e Dimostrazioni Matematiche*
- BIPM (2019). *SI Brochure*

### เชื่อมโยงกับ InteractiveLecture
เปิด simulation ใน `~/InteractiveLecture/simulations/`:
- `Measurement_1_vernier_caliper.html`
- `Measurement_2_micrometer_screw_gauge.html`