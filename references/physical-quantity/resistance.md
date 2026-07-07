---
title: Electrical Resistance
field: Electricity & Magnetism
type: physical-quantity
si_unit: ohm (Ω)
symbol: R
dimension: [M·L²·T⁻³·I⁻²] = [V/A]
version: 1
tags: [electricity, resistance, si-units, history, materials]
related_lectures: []
related_terminology: []
related_physical_quantity: [voltage, current, power, conductance, resistivity]
---

# 🔌 Electrical Resistance

## 📜 ประวัติศาสตร์ของความต้านทานไฟฟ้า

### ก่อนจะมี Ohm — แนวคิดแรกเริ่ม

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **~1740s** | Watson, Bevis, Franklin | สังเกตว่าเส้นลวด **ยาวขึ้น → ส่งไฟฟ้าได้น้อยลง** แต่ยังไม่เข้าใจเป็นคณิตศาสตร์ |
| **1800** | Alessandro Volta | สร้าง Voltaic pile → มีกระแส แต่สังเกตว่าวัสดุต่างชนิดกัน → กระแสต่างกัน |
| **1821** | Sir Humphry Davy | พบว่าความต้านทานของโลหะ **เพิ่มขึ้นเมื่ออุณหภูมิสูงขึ้น** (positive temperature coefficient) |
| **1825** | **Georg Ohm** | ทดลองส่งกระแสผ่านลวดยาวต่างๆ → ตั้งกฎ V ∝ I — แต่ยังไม่สมบูรณ์ |

### Ohm's Struggle และการยอมรับ

| ปี | เหตุการณ์ |
|----|-----------|
| **1827** | **Ohm ตีพิมพ์ *Die galvanische Kette*** — V = IR อย่างชัดเจนครั้งแรก |
| **•** | ถูก **โจมตีอย่างหนัก** โดยนักฟิสิกส์เยอรมัน (โดยเฉพาะ Georg Friedrich Pohl) — "ไร้สาระ" "ฟิสิกส์ไม่ใช่คณิตศาสตร์" |
| **1833** | Ohm เสียตำแหน่งอาจารย์ที่ Cologne — ใช้ชีวิตอย่างยากจน |
| **1841** | ในที่สุด **Royal Society** (อังกฤษ) มอบเหรียญ Copley ให้ Ohm — งานของเขาเริ่มได้รับการยอมรับ |
| **1849** | Ohm ได้ตำแหน่ง professor ที่ Munich — **ช้าไป 20 ปี** |
| **1881** | **International Electrical Congress (Paris)** — ตั้งชื่อหน่วยความต้านทาน **Ohm (Ω)** |

> **🎖️ ข้อคิด:** Ohm ถูกปฏิเสธโดยเพื่อนร่วมชาติเยอรมัน แต่ได้รับการยอมรับจากอังกฤษ — ปัจจุบันกฎของโอห์มเป็นกฎพื้นฐานที่สุดของไฟฟ้าที่นักเรียนทุกคนต้องรู้!

### การพัฒนาเพิ่มเติม

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1843** | Charles Wheatstone | **Wheatstone bridge** — วัด R แม่นยำครั้งแรก |
| **1871** | Siemens | เสนอ "unit of resistance" = ความต้านทานของคอลัมน์ปรอท 1 m³ × 1 m (→ ohm) |
| **1873** | Maxwell | วางทฤษฎี EM → resistivity (ρ) เป็น intrinsic property ของวัสดุ |
| **1911** | Kamerlingh Onnes | **Superconductivity** — R = 0 ที่ T < T_c (ปรอท 4.2 K) |
| **1927** | Arnold Sommerfeld | แบบจำลอง quantum electron gas → อธิบาย conduction ในโลหะ |
| **1980** | Klaus von Klitzing | **Quantum Hall Effect** → R_K = h/e² = 25,812.807... Ω → **quantum resistance standard** |
| **1982** | Laughlin, Thouless, Haldane | Topological insulator → integer Quantum Hall Effect |
| **1990** | **Quantum Hall Effect** ใช้เป็น primary standard ของความต้านทานทั่วโลก |

---

## ⚛️ คำนิยามของ 1 โอห์ม

### Derived Unit
> "1 ohm = **the electrical resistance between two points when a constant potential difference of 1 volt produces a current of 1 ampere**"

```
1 Ω = 1 V/A = 1 kg·m²·s⁻³·A⁻²
```

### Quantum Standard — Von Klitzing Constant (1990–ปัจจุบัน)

```
R_K = h/e² = 25,812.807459304... Ω (fixed, post-2019)

R_K/2 = 12,906.403729652... Ω (R_H = R_K/2 สำหรับ integer QHE)
```

**หลักการ Quantum Hall Effect:**
| ขั้นตอน | รายละเอียด |
|---------|-------------|
| **2D electron gas** (GaAs/AlGaAs heterostructure) ที่ T < 1.5 K, B > 10 T | |
| กระแส I ผ่าน sample → แรงดัน Hall V_H ตั้งฉาก | |
| **Hall resistance** R_H = V_H/I = R_K/i (i = integer 1, 2, 3, ...) | |
| ค่า i = 2 → R_H = 12,906.4 Ω — ใช้เป็น standard จริง | |
| ถ้าใช้ i = 2 กับ R_H = 12,906.4 Ω → ทราบ R ใดๆ จาก potentiometric comparison | |

> **🎯 ความสำคัญ:** เช่นเดียวกับ JVS สำหรับแรงดัน — QHE ให้ quantum standard สำหรับความต้านทานที่ไม่ขึ้นกับวัสดุ อุณหภูมิ หรือเวลา → reproducible ทุกที่! แม่นยำ ~10⁻⁹

### Post-2019: e fixed → R_K เป็น fixed constant

```
เมื่อ e = 1.602176634 × 10⁻¹⁹ C (fixed)
และ h = 6.62607015 × 10⁻³⁴ J·s (fixed)

R_K = h/e² = 25,812.807459304... Ω (fixed!)
```

---

## 🔬 เครื่องมือวัดความต้านทาน (Timeline)

| อุปกรณ์ | ปี | หลักการ | ช่วงวัด |
|----------|-----|---------|---------|
| 🔄 **Wheatstone bridge** | 1843 (Wheatstone) | 4 ตัวต้านทาน — ปรับเพื่อ zero current | mΩ – MΩ |
| 🔧 **Ohmmeter (moving-coil)** | 1890s | ตัวต้านทาน + กระแสคงที่ → วัด V (I·R) | Ω – MΩ |
| 💻 **Digital multimeter (DMM)** | 1970s | กระแสคงที่ + ADC วัด V | mΩ – GΩ |
| ⚡ **Kelvin double bridge** | 1862 (Lord Kelvin) | 4-terminal measurement — ขจัด lead resistance | μΩ – mΩ |
| 🧲 **Four-point probe** | 1916 (Wenner) | 2 จ่าย I, 2 วัด V — ไม่รวม contact R | mΩ – MΩ สำหรับ thin film |
| 🔬 **Quantum Hall resistance standard** | 1980 (von Klitzing) | QHE ใน 2DEG | ~12,906 Ω (fixed) |
| 📟 **LCR meter** | ปัจจุบัน | วัด Z = √(R²+X²) ที่ความถี่ต่างๆ | mΩ – MΩ |
| ✅ **Cryogenic current comparator (CCC)** | 1990s | เปรียบเทียบกระแสใน superconducting coil | nΩ – mΩ |

---

## 📐 หน่วยของความต้านทาน

### SI Unit
| หน่วย | สัญลักษณ์ | คำนิยาม |
|-------|-----------|---------|
| **ohm** | Ω | 1 Ω = 1 V/A |
| **Conductance** | siemens (S) | 1 S = 1/Ω |
| **Resistivity** | Ω·m | ρ = R·A/l (intrinsic property) |
| **Conductivity** | S/m | σ = 1/ρ |

### SI Prefixes

| หน่วย | สัญลักษณ์ | ค่า | ใช้ที่ไหน |
|-------|-----------|-----|----------|
| **micro-ohm** | μΩ | 10⁻⁶ Ω | Superconductor, busbar resistance |
| **milli-ohm** | mΩ | 10⁻³ Ω | Battery internal resistance, PCB trace |
| **ohm** | Ω | 1 | Resistor, load |
| **kilo-ohm** | kΩ | 10³ Ω | Electronics, pull-up resistor |
| **mega-ohm** | MΩ | 10⁶ Ω | Insulation resistance |
| **giga-ohm** | GΩ | 10⁹ Ω | High-voltage insulation |
| **tera-ohm** | TΩ | 10¹² Ω | Dielectric, electrometer input |
| **peta-ohm** | PΩ | 10¹⁵ Ω | Ultra-insulator, cryogenic |
| **Planck resistance (Rᴘ)** | ≈ 2.9 × 10⁴² Ω | quantum gravity scale — huge! |

### หน่วยอื่นๆ

| หน่วย | ค่า | ที่มา |
|-------|-----|------|
| **statohm** | ≈ 8.987 × 10¹¹ Ω | CGS esu |
| **abohm** | 10⁻⁹ Ω | CGS emu |
| **von Klitzing constant (R_K)** | 25,812.80759... Ω | Quantum Hall standard |
| **Siemens (S)** | 1/Ω | Conductance (หน่วยกลับ) |

---

## 🔬 ความต้านทานของวัสดุต่างๆ

### ความต้านทานไฟฟ้าจำเพาะ (Resistivity, ρ) ที่ 20°C

| วัสดุ | ρ (Ω·m) | ประเภท |
|-------|----------|--------|
| **Silver (Ag)** | 1.59 × 10⁻⁸ | ตัวนำดีที่สุด |
| **Copper (Cu)** | 1.68 × 10⁻⁸ | ตัวนำ (นิยมใช้ในสายไฟ) |
| **Gold (Au)** | 2.44 × 10⁻⁸ | ตัวนำ (ใช้ใน contact) |
| **Aluminium (Al)** | 2.65 × 10⁻⁸ | ตัวนำ (สายส่ง) |
| **Iron (Fe)** | 9.71 × 10⁻⁸ | ตัวนำ |
| **Nichrome (Ni-Cr)** | ~1.0 × 10⁻⁶ | ตัวต้านทาน (heater) |
| **Carbon** | ~3.5 × 10⁻⁵ | ตัวต้านทาน, carbon resistor |
| **Water (pure)** | ~1.8 × 10⁵ | ฉนวน |
| **Glass** | ~10¹⁰ – 10¹⁴ | ฉนวน |
| **Rubber** | ~10¹³ – 10¹⁶ | ฉนวน |
| **Teflon (PTFE)** | ~10²² – 10²⁴ | ฉนวนยอดเยี่ยม |
| **Superconductor (Nb)** | **0** Ω (ต่ำกว่า T_c) | ตัวนำยิ่งยวด |
| **Graphene** | ~1 × 10⁻⁸ | ตัวนำ 2D ความต้านทานต่ำมาก |

---

## 🌍 การใช้งานในชีวิตจริง

| การใช้งาน | ที่เกี่ยวข้อง |
|-----------|-------------|
| 🔥 **เครื่องทำความร้อน** | Resistance wire (nichrome): P = V²/R |
| 💡 **หลอดไส้** | W filament — R เพิ่มขึ้นตาม T (≈15× hotter → R ≈15× higher) |
| 🔇 **Fuse** | ตัวนำจุดอ่อน — I เกิน → ร้อน → ขาด |
| 📏 **Strain gauge** | R เปลี่ยนตามการยืด/หด (piezoresistive) |
| 🌡️ **RTD (Resistance Temperature Detector)** | Pt-100: R ∝ T → วัดอุณหภูมิ |
| 🖥️ **PCB** | Copper trace — R เล็กน้อย (ต้องคำนวณ IR drop) |
| ⚡ **Grounding** | Earth resistance (ต้อง < 5 Ω ตามมาตรฐาน) |
| 🧠 **Neural network** | Memristor — R เปลี่ยนตาม history (device ที่ "จำ" ได้) |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Ohm's law (V=IR) ใช้ได้กับทุกอุปกรณ์" | **ไม่** — Ohm's law ใช้ได้กับ **ohmic materials** (R คงที่) เท่านั้น — diode, transistor, LED, และตัวต้านทานที่ร้อนขึ้น ไม่เป็น ohmic |
| "ความต้านทานของตัวต้านทานคงที่ตลอด" | R เปลี่ยนตามอุณหภูมิ — ส่วนใหญ่ PTC (positive temp coeff), บางชนิด NTC |
| "สายไฟทองแดงมีความต้านทาน = 0" | ไม่ใช่ — 0.017 Ω ต่อเมตร ที่ 1 mm² → 100 m = 1.7 Ω |
| "Conductor กับ Insulator ต่างกันที่ R" | **ถูก** — แต่สิ่งที่เรียกว่า insulator = R สูงมาก — ถ้า V สูงพอ อิเล็กตรอนจะกระโดดข้ามได้ (dielectric breakdown) |
| "ความต้านทาน = ไม่ดี" | ไม่เสมอไป — จำเป็นใน heater, fuse, voltage divider, current limiter |
| "Resistance กับ Resistivity ต่างกันยังไง?" | **Resistance (R)** ขึ้นกับ geometry; **Resistivity (ρ)** = intrinsic property ของวัสดุ — R = ρ·l/A |

### 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. Quantum Hall Effect เกิดได้ยังไง? (แบบง่าย)**
ใน 2D electron gas ที่อุณหภูมิต่ำมาก + สนามแม่เหล็กแรง → electron orbit กลายเป็น **Landau levels** (quantized cyclotron orbits) → เมื่อระดับ Fermi อยู่ระหว่าง Landau levels → conduction ไร้ loss ทางขอบ sample → Hall resistance = h/(ie²) เป็นทวีคูณของ R_K

**2. Superconductor มี R = 0 จริงหรือ?**
**จริง** (สำหรับ DC) — วัด limite = < 10⁻²⁴ Ω·m (เทียบกับทองแดง 10⁻⁸) — นั่นคือดีกว่า ~10¹⁶ เท่า! แต่สำหรับ AC: มี surface resistance เล็กน้อย (จาก flux motion และ thermal excitation) — นี่คือข้อจำกัดของ superconducting RF (SRF) cavities

**3. Negative resistance — มีจริงไหม?**
มี! ในอุปกรณ์บางชนิด: **tunnel diode** (Esaki diode, 1957), **Gunn diode** — เมื่อเพิ่ม V → I *ลดลง* (dV/dI < 0 ในบางช่วง) — ใช้สร้าง **oscillator** และ amplifier โดยไม่ต้องใช้ transistor

**4. What's the smallest possible resistance?**
ใน nature: 
- 1 quantum of resistance (for a single mode conductor) = h/2e² ≈ **12.9 kΩ**  
- อะไรก็ตามที่ < R_K ต้องมีหลาย conduction channel (parallel)
- ใน superconductor → 0 Ω (ไม่มี limit จริง แต่ practical limit < 10⁻²⁴ Ω·m)

**5. Memristor — "ตัวต้านทานที่จำได้"**
4th fundamental circuit element (Chua, 1971) — R เปลี่ยนตาม *history* (integral ของ current) → เมื่อปิดไฟ → R คงอยู่ → เหมือน "จำ" สถานะ → ใช้เป็น non-volatile memory (RRAM / ReRAM)

## 🔗 อ้างอิง

- Ohm, G. S. (1827). *Die galvanische Kette, mathematisch bearbeitet*
- Wheatstone, C. (1843). "An Account of Several New Instruments and Processes for Determining the Constants of a Voltaic Circuit"
- von Klitzing, K. et al. (1980). "New Method for High-Accuracy Determination of the Fine-Structure Constant"
- Chua, L. O. (1971). "Memristor—The Missing Circuit Element" — *IEEE Trans. Circuit Theory*
- BIPM (2019). *The International System of Units (SI) — 9th edition*
- Jeanneret, B. & Benz, S. P. (2009). "Application of the Quantum Hall Standard" — *Eur. Phys. J. Special Topics*