---
title: Energy
field: General Physics — Thermodynamics, Mechanics
type: physical-quantity
si_unit: joule (J)
symbol: E, U, K, V
dimension: [M·L²·T⁻²]
version: 1
tags: [energy, conservation, thermodynamics, work, si-units]
related_lectures: [topic17_energy, topic18_energy_resources]
related_terminology: [work, momentum, newtons_laws]
related_physical_quantity: [work, power, force, temperature, mass]
---

# ⚡ Energy

> **Energy = ความสามารถในการทำงาน (capacity to do work)**
>
> — อนุรักษ์เสมอ (Conservation of Energy)
>
> SI unit: **joule (J)** = N·m = kg·m²·s⁻²

---

## 📜 ประวัติศาสตร์ — แนวคิด "พลังงาน"

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~1644** | **René Descartes** | "Quantity of motion" (mv) — save ในจักรวาล (แต่คิดผิดว่า scalar) |
| **~1669** | **Christiaan Huygens** | ศึกษาการชนของ pendulum → ค้นพบว่า **mv²** อนุรักษ์ด้วย |
| **~1695** | **Gottfried Leibniz** | เรียก mv² ว่า **"vis viva"** (living force) — โต้แย้ง Cartesian school |
| **~1740s** | Dortous de Mairan, Émilie du Châtelet | เผยแพร่ vis viva ในฝรั่งเศส — du Châtelet ตั้งสมการ: mv² = 2mgh |
| **1807** | **Thomas Young** (อังกฤษ) | ใช้คำว่า **"energy"** เป็นครั้งแรกในความหมายปัจจุบัน |
| **1829** | **Gustave Coriolis** | ใช้คำว่า **"travail" (work)** — F·s — และ **kinetic energy = ½mv²** |
| **1843** | **James Prescott Joule** 🔬 | ทดลอง water stirring → น้ำร้อน → **mechanical → heat** |
| | | — วัด **mechanical equivalent of heat**: 4184 J = 1 kcal |
| **1847** | **Hermann von Helmholtz** | *Über die Erhaltung der Kraft* — **Conservation of Energy** ครั้งแรก! |
| | | — รวม kinetic, potential, heat, electrical, magnetic |
| **1850s** | **Rudolf Clausius** | First Law of Thermodynamics: ΔU = Q − W |
| **1905** | **Albert Einstein** | **E = mc²** — มวล = รูปแบบหนึ่งของพลังงาน! |
| | | 1 g = 9 × 10¹³ J ≈ พลังงานของระเบิดนิวเคลียร์ Hiroshima |
| **1927** | **Heisenberg** | Uncertainty Principle: ΔE·Δt ≥ ℏ/2 |
| **2019** | **SI Redefinition** | J = kg·m²·s⁻² → traceable ถึง h, c, ΔνCs |

---

## ⚛️ รูปแบบของพลังงาน (Forms of Energy)

| รูปแบบ | สมการ | หน่วย | หมายเหตุ |
|--------|-------|-------|----------|
| **Kinetic (K)** | ½mv² | J | พลังงานจากการเคลื่อนที่ |
| **Potential (Gravitational)** | mgh | J | พลังงานจากตำแหน่งในสนามโน้มถ่วง |
| **Elastic Potential** | ½kx² | J | สปริงอัด/ยืด (Hooke's law) |
| **Thermal (Heat)** | mcΔT | J | พลังงานจาก溫度ของสสาร |
| **Chemical** | ขึ้นกับพันธะ | J | พลังงานในพันธะเคมี |
| **Electrical** | V·I·t | J | พลังงานจากสนามไฟฟ้า |
| **Nuclear** | mc² | J | E = mc² (fission, fusion) |
| **Radiant (EM)** | hf | J | โฟตอน |
| **Sound** | ขึ้นกับความดัน | J | พลังงานคลื่นกล |
| **Rest mass energy** | **mc²** | J | ทุกวัตถุมี energy = mc² แม้หยุดนิ่ง |

### Conservation of Energy
> **พลังงานไม่สามารถสร้างหรือทำลาย — เปลี่ยนรูปเท่านั้น**
>
> E_total (ระบบปิด) = constant

---

## 📐 หน่วยของพลังงาน

### SI Unit
| หน่วย | สัญลักษณ์ | ค่า |
|-------|-----------|-----|
| **joule** | J | 1 N·m = 1 kg·m²·s⁻² |

### หน่วยอื่นๆ

| หน่วย | ค่าใน J | ใช้ที่ไหน |
|-------|---------|----------|
| **electronvolt (eV)** | 1.602×10⁻¹⁹ | ฟิสิกส์อนุภาค |
| **MeV** | 1.602×10⁻¹³ | ฟิสิกส์นิวเคลียร์ |
| **GeV** | 1.602×10⁻¹⁰ | LHC, Standard Model |
| **calorie (cal)** | 4.184 | อาหาร, ความร้อน |
| **Calorie (kcal)** | 4,184 | อาหาร (Calorie กับ C ใหญ่) |
| **kWh** | 3.6×10⁶ | ค่าไฟบ้าน (1 kWh = 3.6 MJ) |
| **BTU** | 1,055.06 | HVAC, US |
| **therm** | 1.055×10⁸ | US gas bill |
| **tonne of TNT** | 4.184×10⁹ | ระเบิด (1 ton TNT ≈ 4.2 GJ) |
| **Hiroshima bomb** | ≈ 6.3×10¹³ | 15 kT |
| **Tsar Bomba** | ≈ 2.1×10¹⁷ | 50 MT — ใหญ่ที่สุดเท่าที่มนุษย์สร้าง |
| **Sun's energy per second** | ≈ 3.8×10²⁶ | fusion |
| **Planck energy** | ≈ 1.96×10⁹ | quantum gravity scale |

---

## 🌍 พลังงานในชีวิตจริง

| สิ่งนี้ | พลังงาน (J) | เทียบ |
|---------|-------------|-------|
| 🥜 ถั่วลิสง 1 เม็ด | ≈ 10 | วิ่ง 3 วินาที |
| 🍳 ไข่ต้ม 1 ฟอง | ≈ 300,000 | วิ่ง 1 ชม. |
| 💡 หลอดไฟ LED 10W 1 ชม. | 36,000 | 36,000 J = 0.01 kWh |
| 🔋 iPhone battery (~3,000 mAh @ 3.7V) | ≈ 40,000 | 40 kJ |
| 🚗 เติมน้ำมัน 1 ลิตร | ≈ 34,000,000 | 34 MJ |
| ⚡ ฟ้าผ่า 1 ครั้ง | ≈ 5×10⁹ | เทียบเท่า 5 GJ |
| 🚀 Saturn V rocket (total) | ≈ 1.1×10¹² | — |
| ☀️ พลังงานจากดวงอาทิตย์ต่อ m²/วัน | ≈ 25×10⁶ | 25 MJ/m² |
| 💣 Hiroshima | ≈ 6×10¹³ | 15 kT |
| 🌍 World energy consumption/ปี | ≈ 5.8×10²⁰ | 2019 |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Energy = force" | **ไม่** — Force = N, Energy = J (= N·m) — energy = force × distance |
| "Conservation of energy = energy ไม่สูญ" | **อนุรักษ์** — แต่เปลี่ยนรูป — friction → heat — "สูญ" = เปลี่ยนเป็นที่ไม่ได้ใช้ |
| "Kinetic energy = mv (momentum)" | **ไม่** — K = ½mv², p = mv — ต่างกันที่ ½และ v² vs v |
| "Mass กับ energy ต่างกัน" | **E=mc²** — mass = concentrated form ของ energy — 1 g = 9×10¹³ J |
| "Temperature = energy" | **ไม่** — Temperature ≠ total energy — T ∝ average KE ต่อโมเลกุล |

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. E=mc² — 1 kg = พลังงานเท่าไหร่?**
E = 1 × (3×10⁸)² = 9×10¹⁶ J ≈ **21 megaton TNT**
— เพียง 1 kg = ระเบิดนิวเคลียร์ที่ใหญ่ที่สุดที่มนุษย์สร้าง (Tsar Bomba = 50 MT ≈ 2.4 kg)
— แต่ conversion 100% mass→energy = ต้องใช้ matter–antimatter annihilation

**2. Zero-point energy — มีใน quantum mechanics**
ที่ T=0 K (absolute zero) — quantum oscillator ยังมี E₀ = ½hf
— นักฟิสิกส์เชื่อว่าจักรวาลเต็มไปด้วย ZPE → มี energy ≠ 0 แม้ไม่มีอะไร
— Casimir effect = experimental proof ของ vacuum energy

**3. Dark energy — 68% ของจักรวาล**
— เป็นพลังงานที่ทำให้จักรวาลขยายตัวเร็วขึ้น
— เราไม่รู้ว่าคืออะไร — เรียก "dark" เพราะ unseen
— เป็นหนึ่งในปัญหาที่ใหญ่ที่สุดของฟิสิกส์

---

## 🔗 อ้างอิง

- Young, T. (1807). *A Course of Lectures on Natural Philosophy and the Mechanical Arts*
- Joule, J. P. (1843). "On the Calorific Effects of Magneto-Electricity"
- Helmholtz, H. (1847). *Über die Erhaltung der Kraft*
- Einstein, A. (1905). "Does the Inertia of a Body Depend Upon Its Energy Content?"
- Feynman R. P. (1963). *Feynman Lectures Vol. I* — Ch. 4: Conservation of Energy