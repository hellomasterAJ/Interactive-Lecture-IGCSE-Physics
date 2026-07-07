---
title: Electric Charge and Electric Current
field: Electricity & Magnetism
type: physical-quantity
si_unit: coulomb (C), ampere (A)
symbol: q, Q (charge), I (current)
dimension: [I] (current is base), charge = [I·T]
version: 1
tags: [electricity, charge, current, si-units, history, instruments]
related_lectures: []
related_terminology: []
related_physical_quantity: [time, force, energy, voltage, resistance]
---

# ⚡ Electric Charge & Electric Current

> **หมายเหตุ:** กระแสไฟฟ้า (current, A) เป็น **SI base unit** — มีมิติ [I] แยกต่างหากจากปริมาณอื่น
> ส่วนประจุไฟฟ้า (charge, C) เป็น **derived unit** — 1 C = 1 A·s

---

## 📜 ประวัติศาสตร์ไฟฟ้า — จากอำพันสู่แอมแปร์

### สมัยโบราณ — สิ่งแรกที่มนุษย์รู้จักไฟฟ้า

| ปี/ช่วง | นักวิทยาศาสตร์ | การค้นพบ |
|----------|---------------|-----------|
| **~600 BCE** | Thales of Miletus | ถู **อำพัน (ἤλεκτρον — elektron)** กับขนสัตว์ → ดูดวัตถุเบา → **แรกเริ่มของไฟฟ้าสถิต** |
| **~0–400 CE** | ไม่ปรากฏ | ชาวโรมันรู้จัก **ปลาไฟฟ้า (torpedo fish)** — ใช้ปลา Torpedo รักษาโรคปวดศีรษะและ gout |
| **ศตวรรษที่ 13** | Petrus Peregrinus | ศึกษาแม่เหล็ก แต่ยังไม่แยกไฟฟ้า vs แม่เหล็ก |

### ยุคฟื้นฟู — ไฟฟ้าสถิตเริ่มมีระบบ

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1600** | **William Gilbert** (อังกฤษ) | *De Magnete* — แยก "electric" (ดึงดูดแบบอำพัน) กับ "magnetic" (ดึงดูดแบบแม่เหล็ก) — ตั้งคำศัพท์ **electricus** |
| **~1660** | Otto von Guericke | สร้าง **เครื่องกำเนิดไฟฟ้าสถิต** เครื่องแรก — ลูกกำมะถันหมุน + ถูด้วยมือ |
| **1729** | Stephen Gray | ค้นพบ **ตัวนำไฟฟ้า (conductor)** vs **ฉนวน (insulator)** — ส่งกระแสไฟฟ้าได้ไกลถึง 293 เมตร |
| **1733** | Charles-François du Fay | พบไฟฟ้ามี **2 ชนิด**: vitreous (แก้วถู = +) และ resinous (ยางถู = −) — "สองชนิดไฟฟ้า" |
| **1745** | **Leyden Jar** (Pieter van Musschenbroek) | สะสมประจุไฟฟ้าได้เป็นครั้งแรก — **ตัวเก็บประจุ (capacitor) เครื่องแรกของโลก** |
| **1747** | Benjamin Franklin | เสนอ **fluid theory of electricity** → กำหนด **+ และ −** — ไฟฟ้าไหลจาก + ไป − (แต่ความจริงอิเล็กตรอนไหลกลับทาง!) |
| **1752** | **Benjamin Franklin** | **ว่าวกับกุญแจ** — พิสูจน์ว่าฟ้าผ่า = ไฟฟ้า |

### ยุคกระแสไฟฟ้า — Volta, Galvani, Ampère

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1780** | Luigi Galvani | ขากบกระตุกเมื่อสัมผัสโลหะ 2 ชนิด → "animal electricity" (ผิด — ที่จริงเป็นปฏิกิริยาเคมี) |
| **1791** | Galvani ตีพิมพ์ | *De Viribus Electricitatis in Motu Musculari* |
| **1800** | **Alessandro Volta** | **Voltaic Pile** — แผ่นสังกะสี+ทองแดง+น้ำเกลือสลับกัน → **แบตเตอรี่เครื่องแรกของโลก** — กระแสไฟฟ้าต่อเนื่องเป็นครั้งแรก! |
| **1820** | **Hans Christian Ørsted** (เดนมาร์ก) | **ค้นพบแม่เหล็กไฟฟ้า** — กระแสไฟฟ้าในเส้นลวดทำให้เข็ม compass เบน → ไฟฟ้า ↔ แม่เหล็ก! |
| **1820** | André-Marie Ampère (ฝรั่งเศส) | ตั้งทฤษฎีทางคณิตศาสตร์ของ Ørsted → กำหนด **แรงระหว่างเส้นลวด 2 เส้นที่มีกระแส** |
| **1821** | Michael Faraday | **การหมุนของแม่เหล็กรอบเส้นลวดที่มีกระแส** → มอเตอร์ไฟฟ้าเครื่องแรก |
| **1826** | **Georg Ohm** (เยอรมนี) | **กฎของโอห์ม** — V = IR — ความสัมพันธ์ระหว่างกระแส แรงดัน และความต้านทาน |
| **1831** | Michael Faraday | **การเหนี่ยวนำแม่เหล็กไฟฟ้า** — ขดลวดเคลื่อนที่ในสนามแม่เหล็ก → เกิดกระแส → **ไดนาโม/เจนเนอเรเตอร์** |
| **1834** | Charles Wheatstone | ใช้ **Wheatstone bridge** วัดความต้านทานอย่างแม่นยำ |
| **1873** | James Clerk Maxwell | *A Treatise on Electricity and Magnetism* — **สมการของแมกซ์เวลล์** 4 สมการ — รวมไฟฟ้า แม่เหล็ก และแสงเข้าด้วยกัน |
| **1881** | **International Electrical Congress** (Paris) | ตั้งชื่อหน่วย: **ampere** (A), **coulomb** (C), **volt** (V), **ohm** (Ω), **farad** (F) |
| **1897** | **J.J. Thomson** (อังกฤษ) | ค้นพบ **อิเล็กตรอน** — อนุภาคที่ขนส่งประจุลบ — กระแสไฟฟ้า = การเคลื่อนที่ของอิเล็กตรอน |

### ยุคควอนตัม — เข้าใจไฟฟ้าอย่างลึกซึ้ง

| ปี | การค้นพบ |
|----|----------|
| **1905** | Einstein — photoemission: โฟตอนกระแทกอิเล็กตรอนหลุด → เสนอ quantized energy |
| **1911** | Millikan — **oil drop experiment**: วัดประจุของอิเล็กตรอน e = 1.602 × 10⁻¹⁹ C |
| **1911** | Kamerlingh Onnes — ค้นพบ **superconductivity** (Hg ที่ 4.2 K: R = 0) |
| **1956** | NIST-Josephson Effect → เชื่อมแรงดันกับ frequency → quantum volt |
| **1980** | Klaus von Klitzing — **Quantum Hall Effect** → R_K = h/e² = 25,812.8 Ω (fixed constant) |
| **2019** | **SI Redefinition** — e fixed: e = 1.602176634 × 10⁻¹⁹ C → แอมแปร์นิยามจาก electron charge |

---

## ⚛️ คำนิยามของ 1 แอมแปร์ — 2 ยุค

### 1. Force Between Wires Definition (1948–2019)
> "1 ampere = **the constant current which, if maintained in two straight parallel conductors of infinite length, of negligible circular cross-section, and placed 1 metre apart in vacuum, would produce between conductors a force equal to 2 × 10⁻⁷ N per metre of length**"
>
> (*9ᵗʰ CGPM, 1948*)

**🧮 ที่มา:**
```
F/l = μ₀ · I₁ · I₂ / (2πd)

เมื่อ F/l = 2 × 10⁻⁷ N/m
I₁ = I₂ = 1 A
d = 1 m
μ₀ = 4π × 10⁻⁷ H/m (permeability of free space — fixed then)
```

| ปัญหาของนิยามนี้ | รายละเอียด |
|-----------------|-------------|
| **สร้างยากมาก** | ต้องใช้เส้นลวดตรงยาวไม่จำกัดในทางปฏิบัติ — ทำไม่ได้จริง |
| **ความแม่นยำต่ำ** | ~10⁻⁶ — แย่กว่าหน่วย SI อื่นๆ |
| **ต้องพึ่งการวัดแรง** | ซึ่งเสียง่าย มีการสั่นสะเทือนเข้ามารบกวน |

### 2. Elementary Charge Definition (2019 – ปัจจุบัน) — SI Definition
> "**1 ampere = the flow of exactly 1/(1.602176634 × 10⁻¹⁹) elementary charges per second**"
>
> หรือ **1 A = 6.241509074 × 10¹⁸ e/s**

**หลักการ:**
```
e = 1.602176634 × 10⁻¹⁹ C (fixed)

1 C = 1/1.602176634 × 10⁻¹⁹ e ≈ 6.24 × 10¹⁸ e
1 A = 1 C/s

ดังนั้น:
1 A = 6.241509074... × 10¹⁸ elementary charges per second
```

> **🎯 ความสำคัญ:** 
> - e เป็น constant of nature → reproducible ทุกที่ในจักรวาล
> - เชื่อมโยงกับ quantum standards: Josephson effect (V = nf/K_J, K_J = 2e/h) + von Klitzing constant (R_K = h/e²)
> - ความแม่นยำ: ดีกว่า 10⁻⁹ โดยใช้ quantum metrology

**และการเปลี่ยนแปลงของ μ₀:**

| ค่าคงที่ | ก่อน 2019 | หลัง 2019 |
|----------|-----------|-----------|
| **μ₀ (permeability of free space)** | **4π × 10⁻⁷ H/m** (fixed) | ต้องวัด — ≈ 4π × 10⁻⁷ H/m (ยังใกล้เคียง) |
| **ε₀ (permittivity of free space)** | 1/(μ₀c²) — derived from fixed μ₀ | ต้องวัด — ยัง ≈ 8.854... × 10⁻¹² F/m |
| **e (elementary charge)** | ต้องวัด | **1.602176634 × 10⁻¹⁹ C (fixed)** |

---

## 🧪 อิเล็กตรอน — ตัวนำส่งประจุไฟฟ้า

### ประจุของอิเล็กตรอน

| ปริมาณ | ค่า |
|--------|-----|
| **e (elementary charge)** | **1.602176634 × 10⁻¹⁹ C** (fixed, 2019) — เท่ากับประจุของโปรตอน (+e) |
| **Charge of electron** | **−e** = −1.602176634 × 10⁻¹⁹ C |
| **Charge of proton** | **+e** = +1.602176634 × 10⁻¹⁹ C |

### Millikan Oil Drop Experiment (1911)

**Robert Millikan** — วัด e เป็นครั้งแรกด้วยความแม่นยำ ~0.3%

| ขั้นตอน | รายละเอียด |
|---------|-------------|
| 1 | พ่นละอองน้ำมันเล็กๆ ในห้อง |
| 2 | ละอองได้รับประจุจากรังสี X (friction หรือ ionization) |
| 3 | สนามไฟฟ้าระหว่างแผ่นโลหะ 2 แผ่น: ปรับ E จน mg = qE → ละอองลอยนิ่ง |
| 4 | เปลี่ยนประจุของละออง (โดยรังสี X) — วัด q=mg/E |
| 5 | q ทุกค่าที่วัดได้เป็น **integer multiple** ของ e → e = 1.592 × 10⁻¹⁹ C (ใกล้เคียงมาก) |

> **ข้อน่ารู้:** Millikan ได้ Nobel Prize ในปี 1923 แต่มีข้อโต้แย้งว่าเขา "เลือกข้อมูล" ที่สนับสนุนค่าที่ต้องการ — การวิเคราะห์ใหม่ในปี 1970s พบว่าค่า e จริงๆ อยู่ที่ 1.602 × 10⁻¹⁹ C (ต่าง ~0.6% จากของ Millikan)

---

## 🔬 เครื่องมือวัดประจุและกระแส (Timeline)

### วัดประจุ (Electroscope / Electrometer)

| อุปกรณ์ | ปี | หลักการ | ความไว |
|----------|-----|---------|---------|
| 🌿 **Gold leaf electroscope** | ~1787 (Bennett) | ใบทองคำ 2 แผ่น → ประจุเหมือน → ผลักกัน | ~10⁻¹⁰ C |
| ⚡ **Quadrant electrometer** | ~1850 (Lord Kelvin) | เข็มหมุนระหว่างประจุใน quadrant | ~10⁻¹² C |
| 🔬 **String electrometer** | ~1910 | เส้นใยควอตซ์เคลื่อนที่ใน E-field | ~10⁻¹⁵ C |
| ⚛️ **Keithley electrometer (modern)** | ปัจจุบัน | MOSFET input + feedback capacitor | < 1 fC (10⁻¹⁵ C) |

### วัดกระแส (Galvanometer / Ammeter)

| อุปกรณ์ | ปี | หลักการ | ช่วงวัด |
|----------|-----|---------|---------|
| 🧲 **Tangent galvanometer** | 1820 (Schweigger) | เข็มแม่เหล็กเบนตามกระแสในขดลวด | mA – A |
| 🔧 **D'Arsonval galvanometer** | 1881 | ขดลวดหมุนในสนามแม่เหล็กถาวร — กระจกสะท้อนแสงวัดมุม | μA – mA |
| 📏 **Moving-coil meter (analogue)** | ~1890 | หน้าปัด + เข็มชี้ | μA – A |
| 💻 **Digital multimeter (DMM)** | 1970s | แปลงกระแสเป็นแรงดัน → ADC | nA – A |
| ⚡ **Picoammeter** | ปัจจุบัน | Feedback ammeter (op-amp) | fA – mA |
| 🔬 **Scanning tunneling microscope (STM)** | 1981 | กระแสจาก tip → surface (~nA) | pA – nA |

### วัดประจุของอนุภาคเดี่ยว

| อุปกรณ์ | วัดอะไร | หลักการ |
|----------|---------|---------|
| **Faraday cup** | จำนวนไอออน/อิเล็กตรอน | กระแสที่สะสมใน cup → I = dq/dt |
| **Microchannel plate (MCP)** | อิเล็กตรอนเดี่ยว | 1 electron → cascade → 10⁶–10⁸ อิเล็กตรอน |
| **Single-electron transistor (SET)** | 1 e ไป-มา | Coulomb blockade — วัด tunneling ของอิเล็กตรอนเดี่ยว |

---

## 📐 หน่วยของประจุและกระแส

### SI Units

| ปริมาณ | หน่วย | สัญลักษณ์ | คำนิยาม |
|--------|-------|-----------|---------|
| **Electric current** | **ampere** | A | **SI base unit** — 1 A = 1 C/s |
| **Electric charge** | **coulomb** | C | C = A·s — 1 C = e/1.602...×10⁻¹⁹ ≈ 6.24×10¹⁸ e |
| **Current density** | ampere per m² | A/m² | — |
| **Charge density** | coulomb per m³ | C/m³ | — |

### SI Prefixes (charge)

| หน่วย | สัญลักษณ์ | ค่า | ใช้ที่ไหน |
|-------|-----------|-----|----------|
| **yoctocoulomb** | yC | 10⁻²⁴ C | — |
| **zeptocoulomb** | zC | 10⁻²¹ C | — |
| **attocoulomb** | aC | 10⁻¹⁸ C | single-electron transistor (~160 aC) |
| **femtocoulomb** | fC | 10⁻¹⁵ C | STM, electrometer |
| **picocoulomb** | pC | 10⁻¹² C | เซนเซอร์เพียโซ, ไฟฟ้าสถิต |
| **nanocoulomb** | nC | 10⁻⁹ C | ประจุจากตัวเก็บประจุขนาดเล็ก |
| **microcoulomb** | μC | 10⁻⁶ C | ไฟฟ้าสถิตในชีวิตประจำวัน |
| **millicoulomb** | mC | 10⁻³ C | flash capacitor |
| **coulomb** | C | 1 | SI derived |
| **kilocoulomb** | kC | 10³ C | ฟ้าผ่า (~15–30 kC) |
| **megacoulomb** | MC | 10⁶ C | — |
| **A·h (ampere-hour)** | Ah | 3,600 C | แบตเตอรี่ (1 Ah = 3,600 C) |

### SI Prefixes (current)

| หน่วย | สัญลักษณ์ | ค่า |
|-------|-----------|-----|
| **yoctoampere** | yA | 10⁻²⁴ A |
| **zeptoampere** | zA | 10⁻²¹ A |
| **attoampere** | aA | 10⁻¹⁸ A |
| **femtoampere** | fA | 10⁻¹⁵ A — STM tunnel current |
| **picoampere** | pA | 10⁻¹² A — leakage current |
| **nanoampere** | nA | 10⁻⁹ A — biological ion channels |
| **microampere** | μA | 10⁻⁶ A — ECG, EEG signals |
| **milliampere** | mA | 10⁻³ A — LED, sensor |
| **ampere** | A | 1 — household appliance (0.1–10 A) |
| **kiloampere** | kA | 10³ A — lightning, arc furnace |
| **megaampere** | MA | 10⁶ A — Z-pinch, plasma |

### หน่วยอื่นๆ ที่เคยใช้ / หาได้ยาก

| หน่วย | ค่า | ที่มา |
|-------|-----|------|
| **e (elementary charge)** | 1.602176634 × 10⁻¹⁹ C | fixed constant นิยามแอมแปร์ |
| **Faraday constant (F)** | 96,485.33212 C/mol | ประจุของอิเล็กตรอน 1 โมล (NA × e) — ใช้ในเคมีไฟฟ้า |
| **statcoulomb (esu)** | ≈ 3.33564 × 10⁻¹⁰ C | CGS system — electrostatic unit |
| **abampere** | 10 A | CGS system — electromagnetic unit |
| **Franklin (Fr)** | ≈ 3.33564 × 10⁻¹⁰ C | CGS esu — same as statcoulomb |
| **Biot (Bi)** | 10 A | CGS emu — same as abampere |

---

## 🌍 การใช้งานในชีวิตจริง

| การใช้งาน | เกี่ยวข้องกับ |
|-----------|-------------|
| 💡 **ไฟฟ้าในบ้าน** | กระแส ~5–15 A (220 V), วัดด้วย clamp meter |
| 🔋 **แบตเตอรี่** | ประจุเก็บได้ = capacity (Ah หรือ mAh) — 1 Ah = 3,600 C |
| ⚡ **ฟ้าผ่า** | ประจุ ~15–30 kC, กระแส ~30 kA peak |
| ⚛️ **ฟิสิกส์อนุภาค** | LHC: 1 proton bunch ≈ 1.15 × 10¹¹ p → ≈ 1.8 × 10⁻⁸ C |
| 🧬 **ชีววิทยา** | Ion channel: ~1 pA (= 6.24 × 10⁶ ions/s) |
| 🖥️ **อิเล็กทรอนิกส์** | CPU: ~50–200 A at 1 V |
| 🔬 **SEM / TEM** | Electron beam: ~0.1 pA – 1 nA |
| 📡 **ภาคพื้นดิน** | Telluric current: ~A–kA (กระแสธรรมชาติในเปลือกโลก) |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "กระแสไฟฟ้า = อิเล็กตรอนวิ่งในสายไฟ" | จริงแต่วิ่ง **ช้ามาก** — drift velocity ของอิเล็กตรอนในทองแดง ~0.02 mm/s (ไม่ใช่ความเร็วแสง!) สัญญาณไฟฟ้า (fields) วิ่ง ≈ c (~0.7c ในทองแดง) |
| "ประจุบวกไหลจาก + ไป −" | Franklin กำหนดแบบนั้น แต่อิเล็กตรอน (−) ไหลจาก − ไป + → **conventional current (บวก) vs electron flow** |
| "ไฟฟ้า 1 หน่วย = 1 kWh" | kWh คือ **พลังงาน** (kilo watt × hour) ไม่ใช่ประจุ — 1 kWh = 3.6 MJ |
| "แอมแปร์ = อัตราการไหลของประจุ" | **ถูกต้อง** — 1 A = 1 C/s |
| "ฟ้าผ่ามีแค่ 1 เส้น" | ฟ้าผ่า = stepped leader (หลายกิ่ง) → return stroke หลัก → ตามด้วย dart leaders หลายครั้ง |
| "อะตอมเป็นกลางทางไฟฟ้าเสมอ" | อะตอมปกติ = กลาง แต่ **ไอออน** (+ หรือ −) เกิดขึ้นได้ตลอดในสารละลาย ก๊าซ และพลาสมา |

---

## 🔗 อ้างอิง

- BIPM. (2019). *The International System of Units (SI) — 9th edition*
- CGPM Resolutions: 9th CGPM (1948) — definition of ampere, 26th CGPM (2018) — redefinition
- Franklin, B. (1751–1754). *Experiments and Observations on Electricity*
- Ørsted, H. C. (1820). *Experimenta circa Effectum Conflictus Electrici in Acum Magneticam*
- Ampère, A.-M. (1822). *Recueil d'Observations Électro-dynamiques*
- Ohm, G. S. (1827). *Die galvanische Kette, mathematisch bearbeitet*
- Maxwell, J. C. (1873). *A Treatise on Electricity and Magnetism*
- Millikan, R. A. (1913). "On the Elementary Electrical Charge and the Avogadro Constant" — *Physical Review*
- von Klitzing, K. (1980). "New Method for High-Accuracy Determination of the Fine-Structure Constant" — *Phys. Rev. Lett.*
- Kibble, B. P. (1976). "A Measurement of the Gyromagnetic Ratio of the Proton by the Strong Field Method"
- Halliday, D., Resnick, R., & Walker, J. — *Fundamentals of Physics*

### 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. ทำไมกระแสไฟฟ้าถึงเป็น SI base unit? — แทนที่จะใช้ประจุ**
อดีต: แอมแปร์วัดได้จากแรงระหว่างเส้นลวด (real experiment) — ประจุ (C = A·s) ก็วัดจาก ammeter + stopwatch ได้ง่ายกว่า → SI ก็เลยเลือก "กระแส" เป็น base ไว้ก่อน ประจุเป็น derived ต่อมาในปี 2019 ถึงแม้นิยามจะเปลี่ยนไปใช้ e (charge) แต่ก็ไม่เปลี่ยนสถานะ: แอมแปร์ยังคงเป็น SI base unit ตามประเพณี

**2. กระแส 1 A มีอิเล็กตรอนกี่ตัวต่อวินาที?**
```
1 C/s ÷ e = 1/(1.602176634 × 10⁻¹⁹)
= 6.24150907446 × 10¹⁸ electrons per second
```
นับได้ประมาณนี้ — ถ้าเอามาเรียงกัน 1 วินาที จะเป็นเส้นยาว ≈ 3 × 10¹⁵ m (0.3 light-year)

**3. Quantum metrology — อนาคตของแอมแปร์?**
ปัจจุบันมี **single-electron pump** (เช่น จาก NIST, PTB) — ส่งอิเล็กตรอนทีละตัวด้วยความถี่ f → I = ef → วัดกระแสแบบ counting โดยตรง (แม่นยำ 10⁻⁸) ในอนาคตอาจใช้เป็น primary standard ของแอมแปร์เลย

**4. Charge quantization — ทำไมประจุถึง quantized (เป็นทวีคูณของ e)?**
ใน Standard Model of particle physics — e เกิดจาก coupling ระหว่าง U(1) gauge field (photon) กับ matter fields — ค่า quantized = topological condition ของ gauge group สาเหตุที่ quark มี fractional charge (±⅓ e, ±⅔ e) เพราะพวกมันไม่เคยถูกสังเกตเดี่ยวๆ (color confinement) — ใน nature เศษส่วนของ e จะรวมกันเป็น hadron ที่มีประจุ integer เสมอ

**5. อนาคต: "แอมแปร์" จะถูกแทนที่ด้วยการนับอิเล็กตรอนไหม?**
ตั้งแต่ 2019 — e ถูก fixed แล้ว → 1 A = 1/(e) e/s = "ส่งอิเล็กตรอน 6.24 × 10¹⁸ ตัวต่อวินาที" — ในทางทฤษฎี นี่คือนิยามแบบ counting ที่ตรงไปตรงมาที่สุด รอแค่ technology (single-electron pump + fast enough RF) ที่เสถียรพอ → แอมแปร์จะกลายเป็น "unit of counting"!