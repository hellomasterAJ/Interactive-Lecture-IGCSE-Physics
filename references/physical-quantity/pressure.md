---
title: Pressure
field: Mechanics — Fluids, Thermodynamics
type: physical-quantity
si_unit: pascal (Pa)
symbol: p, P
dimension: [M·L⁻¹·T⁻²]
version: 1
tags: [pressure, fluids, thermodynamics, gas-laws, si-units]
related_lectures: [topic16_effects_of_forces, topic15_forces]
related_terminology: []
related_physical_quantity: [force, area, density, temperature, volume]
---

# 🌊 Pressure

> **Pressure = แรงต่อหน่วยพื้นที่**
>
> p = F/A — SI unit: **pascal (Pa)** = N/m²

---

## 📜 ประวัติศาสตร์

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~1643** | **Evangelista Torricelli** | Barometer — หลอดแก้ว+ปรอท → ความดันอากาศ ≈ 760 mmHg |
| | | — พิสูจน์ว่าอากาศมี **น้ำหนัก** |
| **~1650** | **Blaise Pascal** 🧪 | แนวคิด pressure ในของไหล → **Pascal's Law** |
| | | — ความดันที่กระทำต่อของไหลในภาชนะปิด → ส่งผ่านเท่ากันทุกทิศ |
| **~1654** | **Otto von Guericke** | **Magdeburg hemispheres** — สูบอากาศออก → ม้าลากไม่ออก! |
| | | — แสดงให้เห็นความดันอากาศ ~10⁵ N/m² |
| **~1660** | **Robert Boyle** | **Boyle's Law:** P ∝ 1/V (T คงที่) |
| | | — กฎของแก๊สข้อแรก |
| **~1780** | **Jacques Charles** | Charles's Law: V ∝ T (P คงที่) |
| **~1802** | **Gay-Lussac** | P ∝ T (V คงที่) |
| **~1834** | **Clapeyron** | **Ideal Gas Law:** PV = nRT |
| **~1881** | SI | ตั้งหน่วย **pascal (Pa)** ตาม Blaise Pascal |

---

## ⚛️ Pressure ขึ้นอยู่กับอะไรบ้าง?

### 1. Atmospheric Pressure — ความดันบรรยากาศ

#### 🧪 การค้นพบ (Torricelli, 1643)
**การทดลองบารอมิเตอร์ปรอท:**
1. เติมปรอทเต็มหลอดแก้วยาว ~1 m
2. คว่ำลงในอ่างปรอท
3. ปรอทในหลอดลดลง เหลือสูง ~760 mm
4. ที่ว่างเหนือปรอท = **vacuum** (Torricellian vacuum)
5. น้ำหนักของปรอท = น้ำหนักของอากาศที่กดบนผิวอ่าง

```
P_atm = ρ_Hg × g × h
      = 13,546 × 9.81 × 0.76
      ≈ 101,325 Pa

∴ 1 atm = 101,325 Pa = 760 mmHg
```

> 🧠 ความรู้: Torricelli เป็นคนแรกที่พิสูจน์ว่าอากาศมีน้ำหนัก — Aristotle เคยเชื่อว่าอากาศ = "ไม่มีน้ำหนัก"

#### 💨 อากาศมีน้ำหนักเท่าไหร่?
| ปริมาณ | ค่า |
|--------|-----|
| มวลของอากาศ 1 ลิตร (ที่ STP) | ≈ 1.2 g |
| มวลของอากาศเหนือ 1 m² (ถึง outer space) | ≈ 10,000 kg (10 ตัน!) |
| แรงที่อากาศกดบนหัวคน (≈ 500 cm²) | ≈ 5,000 N (~500 kg) |
| ทำไมเราถึงไม่ทับ? | เพราะภายในร่างกายมีอากาศดันออกเท่ากัน (balanced) |

#### 🔬 การเปลี่ยนแปลงตามความสูง
```
P(h) = P₀ · e^(−Mgh/RT)   (barometric formula)

โดย:
P₀ = 101,325 Pa (ระดับน้ำทะเล)
M = molar mass ของอากาศ ≈ 0.029 kg/mol
g = 9.81 m/s²
R = 8.314 J/(mol·K)
T = temperature (K)
```

| ระดับความสูง | P (kPa) | % ของ P_atm | ตัวอย่างสถานที่ |
|-------------|---------|-------------|----------------|
| **0 m (ระดับน้ำทะเล)** | 101.3 | 100% | หาดบางแสน |
| **500 m** | 95.5 | 94% | จังหวัดเชียงใหม่ |
| **1,550 m** | 84.5 | 83% | ดอยอินทนนท์ |
| **2,500 m** | 74.7 | 74% | เมืองลาซา (ทิเบต) |
| **5,500 m** | 50.5 | 50% | Base camp Everest |
| **8,848 m** | 31.6 | 31% | **ยอด Everest** |
| **10,000 m** | 26.5 | 26% | ระดับบินเครื่องบินโดยสาร |
| **20,000 m** | 5.5 | 5% | SR-71 Blackbird |
| **100 km (Kármán line)** | ≈ 0.0003 | 0.0003% | ขอบอวกาศ |
| **400 km (ISS)** | ≈ 10⁻⁷ | ~10⁻¹⁰% | สถานีอวกาศ |

> **💡 ข้อสังเกต:** ที่ความสูง 5,500 m (base camp Everest) = ความดันลดลงครึ่งหนึ่ง!

#### 📊 ทำไมถึงเดือดยากขึ้นบนที่สูง?
| ความสูง | จุดเดือดของน้ำ |
|---------|--------------|
| ระดับน้ำทะเล | **100°C** |
| ดอยอินทนนท์ | **≈ 96.5°C** |
| Base camp Everest | **≈ 82°C** |
| ยอด Everest | **≈ 68°C** (ต้มไข่ไม่สุก!) |

##### วิธีต้มไข่ให้สุกบนยอดเขา:
ใช้ **pressure cooker** — ความดันเพิ่ม → จุดเดือดสูงขึ้น → ต้มสุก

---

### 2. Pressure Depends on Depth — ความดันในของเหลว

**Hydrostatic Pressure:**

ความดันที่ระดับความลึก h ในของเหลวที่หยุดนิ่ง:

```
P_hydrostatic = ρgh

P_total = P_atm + ρgh (absolute pressure)
```

| ตัวแปร | ความหมาย |
|--------|----------|
| ρ | ความหนาแน่นของของเหลว (kg/m³) |
| g | แรงโน้มถ่วง (9.81 m/s²) |
| h | ความลึกจากผิวของเหลวลงไป (m) |

> **สิ่งสำคัญ:**
> - P_hydrostatic **ไม่ขึ้นกับ** รูปร่างของภาชนะ — ขึ้นกับ **ρ, g, h** เท่านั้น
> - P_hydrostatic **ไม่ขึ้นกับ** พื้นที่หน้าตัดของภาชนะ
> - **P = F/A** แต่พื้นที่ไม่เข้าไปเกี่ยวข้องกับ *size* ของภาชนะ

#### 🧪 Parodox of Hydrostatics — Pascal's Vases (Pascal, 1648)
> "ไม่ว่าภาชนะจะมีรูปร่างอย่างไร ถ้าความสูงของน้ำเท่ากัน → ความดันก้นภาชนะ = ρgh เหมือนกัน"

| ภาชนะ | รูปร่าง | P ที่ก้น |
|-------|---------|----------|
| A: ตรงแคบ | ความสูง h | ρgh |
| B: ตรงกว้าง | ความสูง h | ρgh |
| C: บานออก | ความสูง h | ρgh |
| D: คอดเข้า | ความสูง h | ρgh |

> **ทั้งหมด = ρgh เท่ากัน** — แปลกใจไหม? แม้ปริมาตรน้ำต่างกัน!

**สาเหตุ:** P = F/A — แรง (F) ที่ก้นภาชนะ = น้ำหนักของน้ำที่อยู่ *เหนือก้นโดยตรง* (ไม่ใช่ของข้างๆ) + แรงจากผนังที่รับน้ำหนักน้ำส่วนเกินไว้ ถ้าภาชนะบานออก (C) → กำแพงเอียงรับน้ำหนักส่วนหนึ่ง → ก้นไม่ต้องรับทั้งก้อน

#### 📖 สูตรที่ควรจำ

| รูปแบบ | สูตร |
|--------|------|
| ความดันของเหลวที่ความลึก h | P = ρgh |
| ความดันสัมบูรณ์ที่ глубине h (ในของเหลวเปิด) | P = P_atm + ρgh |
| ความแตกต่างความดันระหว่าง 2 จุดในของเหลว | ΔP = ρg(h₂ − h₁) |
| ความลึกที่ความดันเท่า P | h = P/(ρg) |
| ระดับความสูงของปรอทใน barometer | h = P_atm/(ρ_Hg·g) |

#### 🌊 ตัวอย่างคำนวณความดันในของเหลว

**ตัวอย่าง 1 — ดำน้ำในทะเล (น้ำทะเล ρ ≈ 1,025 kg/m³)**
```
ที่ความลึก 10 m:
P_hydro = 1,025 × 9.81 × 10 = 100,500 Pa ≈ 101 kPa
P_total = 101 + 101 ≈ 202 kPa ≈ 2 atm

ที่ความลึก 30 m:
P_hydro = 1,025 × 9.81 × 30 = 301,500 Pa ≈ 302 kPa
P_total = 101 + 302 ≈ 403 kPa ≈ 4 atm
```

| ความลึก (m) | P_hydro (kPa) | P_total (kPa) | atm |
|-------------|---------------|---------------|-----|
| **0** | 0 | 101 | **1** |
| **10** | 101 | 202 | **2** |
| **20** | 202 | 303 | **3** |
| **30** | 303 | 404 | **4** |
| **40** | 404 | 505 | **5** |
| **100** | 1,010 | 1,112 | **11** |
| **11,000 (Mariana Trench)** | 111,000+ | 111,000+ | **1,100+** |

> **📌 ทุกๆ 10 m ของน้ำ ≈ ความดันเพิ่ม 1 atm**

**ตัวอย่าง 2 — ปรอท (ρ_Hg = 13,546 kg/m³)**
```
h = P_atm/(ρ_g·g) = 101,325/(13,546 × 9.81) ≈ 0.76 m = 760 mm
```
นี่คือสาเหตุที่ **บารอมิเตอร์ปรอทสูง ~760 mm** — ถ้าใช้น้ำ ต้องใช้หลอดสูง ~10.3 m (เพราะ ρ น้ำน้อยกว่า ρ ปรอท 13.6 เท่า!)

**ตัวอย่าง 3 — ใช้น้ำวัดความดันอากาศแทนปรอท**
```
h_water = P_atm/(ρ_water·g) = 101,325/(1,000 × 9.81) ≈ 10.33 m
```
→ ถ้าจะสร้างบารอมิเตอร์น้ำ ต้องใช้หลอดยาว 10.3 m! (Torricelli เลือกปรอทเพราะขวดแคบ 1 m พอ)

#### 🏗️ ประยุกต์ — Hydraulic System (Pascal's Law)
> "ความดันที่กระทำต่อของไหลในระบบปิด → **ส่งผ่านเท่ากันทุกทิศทาง**"

**ระบบไฮดรอลิก (Hydraulic Jack / Brake):**
```
P = F₁/A₁ = F₂/A₂

∴ F₂ = F₁ × (A₂/A₁)
```

**ตัวอย่าง:** 
```
A₁ = 10 cm², F₁ = 100 N → P = 100/0.001 = 100,000 Pa
A₂ = 200 cm² → F₂ = 100,000 × 0.02 = 2,000 N
```
→ **แรงเข้า 100 N → ออก 2,000 N** (20× magnification)!

> **💡 รถยกในอู่ซ่อมรถ ใช้หลักการนี้!**

---

### 3. Absolute Pressure vs Gauge Pressure

#### Absolute Pressure (P_abs)
> **ความดันที่วัดเทียบกับ absolute zero (vacuum)**

```
P_abs = 0 Pa → perfect vacuum (ไม่มีโมเลกุลอากาศเลย)
P_abs = 101,325 Pa → atmospheric pressure ที่ระดับน้ำทะเล
P_abs = P_atm + ρgh → ที่ความลึก h ในของเหลว (ผิวเปิด)
```

#### Gauge Pressure (P_gauge)
> **ความดันที่วัดเทียบกับความดันบรรยากาศ**

```
P_gauge = P_abs − P_atm

P_gauge > 0 → มากกว่าบรรยากาศ (positive pressure)
P_gauge < 0 → น้อยกว่าบรรยากาศ (negative pressure, suction, vacuum)
P_gauge = 0 → เท่ากับบรรยากาศ (no gauge reading)
```

#### 🎯 ตัวอย่างการใช้งาน

| อุปกรณ์ | P_gauge | P_abs | หมายเหตุ |
|---------|---------|-------|----------|
| **ลมยางรถยนต์** | **30 psi(g)** | 30 + 14.7 = **44.7 psi(a)** | วัดด้วย gauge เสมอ |
| **Tire pressure (SI)** | 200 kPa | 301 kPa | |
| **Blood pressure (systolic)** | **120 mmHg** | 120 + 760 = **880 mmHg** | วัดเทียบกับ atm |
| **Pressure cooker** | ≈ 1 atm (101 kPa) | ≈ 2 atm | gauge = 1 bar over atm |
| **Vacuum cleaner** | ≈ −20 kPa | ≈ 80 kPa | gauge ติดลบ |
| **SCUBA tank (full)** | ≈ 200 bar | ≈ 201 bar | gauge = 200 bar |
| **Suction (medical)** | ≈ −80 mmHg | ≈ 680 mmHg | gauge ติดลบ |
| **Pneumatic system** | 6 bar | 7 bar | gauge common |

#### 🔄 การแปลง
```
P_abs (kPa) = P_gauge (kPa) + 101.325

หน่วยทั่วไป:
1 bar = 100 kPa ≈ 0.987 atm
1 psi = 6.89476 kPa
1 atm = 14.6959 psi
```

#### 🧪 ตารางเปรียบเทียบ

| สถานการณ์ | P_abs (kPa) | P_gauge (kPa) | เทียบกับ atm |
|-----------|-------------|---------------|-------------|
| **LHC vacuum** | ≈ 10⁻¹⁰ | ≈ −101.325 | vacuum สูงมาก |
| **Interstellar space** | ≈ 10⁻¹² | ≈ −101.325 | vacuum |
| **Moon surface** | ≈ 10⁻¹⁴ | ≈ −101.325 | เกือบสมบูรณ์ |
| **Suction pump** | ≈ 50 | ≈ −50 | ดูดได้ ~50% |
| **Atmospheric pressure** | 101.325 | **0** | **reference** |
| **Car tire** | 301 | 200 | ปกติ |
| **SCUBA (10 m)** | 202 | 101 | ดำน้ำ |
| **Pressure cooker** | 200 | 100 | เร่งทำอาหาร |
| **Diving at 30 m** | 404 | 303 | ต้องมี decompression |
| **Hydraulic press** | ~20,000+ | ~20,000+ | 100–200 MPa |

---

### 4. การประยุกต์สำคัญของความดัน

#### 🫁 การหายใจของมนุษย์
- หายใจเข้า (inhale): กะบังลมลง → ปริมาตรปอด↑ → P_intrapulmonic ลดลง ~3–4 mmHg (≈ −0.5 kPa gauge)
- หายใจออก (exhale): กะบังลมขึ้น → ปริมาตรปอด↓ → ความดันเพิ่ม (positive gauge)
- กฎของ Boyle (PV = constant): เมื่อปริมาตรเพิ่ม → ความดันลด → air ไหลเข้า

#### 🏊 SCUBA Diving — ความดันกับการดำน้ำ
| ความลึก | ปัญหา | วิธีแก้ |
|---------|-------|---------|
| 10 m | หูเจ็บ (eardrum กด) | equalization (Valsalva) |
| 30 m | Nitrogen narcosis ("Rapture of the deep") | จำกัดความลึก |
| 40 m+ | Oxygen toxicity | ใช้ special gas mix |
| หลังดำน้ำ | Decompression sickness (bends) | ascent ช้า + decompression stop |
| (กลับขึ้น) | Lung overexpansion | อย่ากลั้นหายใจตอนขึ้น! |

#### 🧰 เครื่องมือวัดความดัน

| อุปกรณ์ | วัดแบบ | หลักการ |
|---------|--------|---------|
| **Barometer** | Absolute | หลอดปรอท/aneroid — P_atm |
| **Manometer** | Gauge / Differential | U-tube + ของเหลว → h ต่าง → ΔP |
| **Bourdon gauge** | Gauge | หลอดโค้ง → ยืดตาม P → เข็ม |
| **Strain gauge pressure sensor** | Abs/Gauge | diaphragm → strain gauge → R change |
| **Piezoelectric sensor** | Dynamic | crystal → ประจุตาม P (ใช้ใน engine) |
| **Capacitive manometer** | Absolute/Gauge | diaphragm → capacitance เปลี่ยน |
| **Barometric altimeter** | Absolute | P ↓ → altitude ↑ (ใช้ในเครื่องบิน) |
| **McLeod gauge** | Absolute (vacuum) | บีบอัด gas sample → P จาก Boyle's law |
| **Pirani gauge** | Gauge (vacuum) | thermal conductivity ∝ P |
| **Ionization gauge** | Absolute (UHV) | ionization current ∝ P (ใช้ < 10⁻³ Pa) |

#### 💉 ตัวอย่าง Manometer (U-tube)
```
U-tube ใส่น้ำ/ปรอท → ต่อด้านหนึ่งกับ P_unknown, อีกด้านเปิดโล่ง (P_atm)

ΔP = ρgΔh

ตัวอย่าง:
- U-tube ต่อกับท่อแก๊ส → Δh = 15 cmH₂O
  ΔP = 1,000 × 9.81 × 0.15 = 1,471 Pa
  P_gauge = 1,471 Pa (≈ 11 mmHg)
  P_abs = 101,325 + 1,471 = 102,796 Pa

- U-tube วัด suction → Δh = −8 cmH₂O
  P_gauge = −785 Pa (vacuum)
  P_abs = 101,325 − 785 = 100,540 Pa
```

---

## 📐 หน่วยของความดัน

### SI Unit
| หน่วย | สัญลักษณ์ | คำนิยาม |
|-------|-----------|---------|
| **pascal** | Pa | 1 Pa = 1 N/m² |

### หน่วยอื่นๆ

| หน่วย | ค่าใน Pa | ใช้ที่ไหน |
|-------|----------|----------|
| **bar** | 100,000 | อุตุนิยมวิทยา, อุตสาหกรรม |
| **millibar (mbar)** | 100 | 天气预报 (1,013 mbar) |
| **atmosphere (atm)** | 101,325 | ฟิสิกส์, เคมี |
| **mmHg / Torr** | 133.322 | การแพทย์, barometer |
| **psi** | 6,894.76 | US, ลมยาง |
| **inHg** | 3,386.39 | บารอมิเตอร์ US |
| **mmH₂O** | 9.80665 | ชลศาสตร์, การแพทย์ |
| **cmH₂O** | 98.0665 | การแพทย์ (CVP) |
| **Planck pressure** | c⁷/(ℏG²) ≈ 4.6×10¹¹³ Pa | quantum gravity |

---

## 🌍 ความดันในชีวิตจริง

| สิ่งนี้ | ความดัน |
|--------|---------|
| 🌬️ อากาศระดับน้ำทะเล | 101.3 kPa |
| 🫁 ที่ความสูง 5,500 m (base camp Everest) | ≈ 50 kPa |
| 🏔️ Mount Everest summit (~8,848 m) | ≈ 31.6 kPa |
| 🌊 Underwater 10 m | ≈ 200 kPa (≈2 atm) |
| Underwater 100 m | ≈ 1,010 kPa (≈10 atm) |
| 🚗 ลมยางรถยนต์ | ≈ 200–250 kPa (≈ 2–2.5 bar) |
| 🚲 ลมยางจักรยาน | ≈ 600–800 kPa (≈ 6–8 bar) |
| 🛢️ ไฮดรอลิกใช้งาน | ≈ 10–35 MPa |
| 🏋️ Hydraulic press | ≈ 100–200 MPa |
| 🕳️ Center of Earth | ≈ 360 GPa |
| 🌞 Center of Sun | ≈ 2.5×10¹⁶ Pa |
| 🧪 Ultra-high vacuum (lab) | ≈ 10⁻¹¹ Pa |
| 🌌 Interstellar medium | ≈ 10⁻¹⁴ Pa |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Pressure = force" | **ไม่** — Pressure = force/area — 1 N บน 1 m² = 1 Pa, 1 N บน 1 mm² = 1 MPa |
| "ความดันอากาศน้อยบนดอย = ไม่มีอากาศ" | แค่บาง — ที่ Everest summit, P ≈ 31 kPa = 30% ของระดับน้ำทะเล |
| "Pascal's law = pressure ในของไหลเท่ากันทุกที่" | **ในภาชนะปิด** — แต่ hydrostatic pressure = ρgh (เพิ่มตามความลึก) |
| "ความดันของน้ำในลำธาร = 1 atm ตลอด" | **ไม่** — ความดันในแนวนอน = atm (ที่ผิว), แนวตั้งเพิ่ม ρgh |

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. แรงดันในหลอดเลือดแดง — systolic/diastolic**
120/80 mmHg =
- Systolic: 120 × 133.3 = 16,000 Pa = 16 kPa
- Diastolic: 80 × 133.3 = 10,700 Pa = 10.7 kPa

**2. Deep Sea pressure — ถ้าดำ 11,000 m (Mariana Trench)**
P ≈ P_atm + ρgh ≈ 1,000 × 9.81 × 11,000 ≈ **108 MPa** = 1,080 atm
— ต้องใช้หุ้มเหล็กหนา ~12 cm (DSV Limiting Factor)

**3. Pressure cooker — ทำไมอาหารสุกเร็ว?**
ที่ P ≈ 2 atm → T_boil ≈ 120°C (แทน 100°C) → ปฏิกิริยาเคมีของอาหารเร็วขึ้น ~2× ทุก +10°C

---

## 🔗 อ้างอิง

- Torricelli, E. (1643). *Opera Geometrica*
- Pascal, B. (1653). *Traité de l'Équilibre des Liqueurs*
- Boyle, R. (1662). *A Defence of the Doctrine Touching the Spring and Weight of the Air*
- von Guericke, O. (1672). *Experimenta Nova Magdeburgica de Vacuo Spatio*