---
title: Acceleration
field: Mechanics — Kinematics
type: physical-quantity
si_unit: metre per second squared (m/s²)
symbol: a
dimension: [L·T⁻²]
version: 1
tags: [acceleration, kinematics, motion, force, si-units]
related_lectures: [topic12_motion]
related_terminology: [kinematics, velocity, inertia]
related_physical_quantity: [velocity, force, mass, time, distance]
---

# 🚀 Acceleration

> **Acceleration = อัตราการเปลี่ยนแปลงของ velocity** (vector)
>
> a = dv/dt — หน่วย m/s²

---

## 📜 ประวัติศาสตร์ — จาก Galileo สู่ Einstein

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~350 BCE** | **Aristotle** | เชื่อว่า "วัตถุหนักตกเร็วกว่าเบา" และ "ความเร็ว ∝ แรงที่กระทำ" |
| **~400 CE** | John Philoponus (Alexandria) | โต้แย้ง Aristotle — เสนอว่า acceleration ของวัตถุตก = constant ถ้าไม่มีตัวกลางต้าน — แต่ถูกมองข้าม |
| **~1500s** | Leonardo da Vinci | ทดลองปล่อยวัตถุจากสะพานที่วัดได้ → สังเกตว่าวัตถุ accelerate แต่ยังไม่สรุปเป็นคณิตศาสตร์ |
| **~1604** | **Galileo Galilei** 🔬 | **การทดลอง inclined plane** — ลูกกลิ้งลงทางลาดเอียง → ระยะทาง ∝ t² |
| | | → **พิสูจน์: v ∝ t สำหรับ uniform acceleration** (v = at) |
| | | → สรุปว่าวัตถุตกอิสระทุกชนิด accelerate เท่ากัน |
| | | ↳ *หักล้าง Aristotle ที่ถูกเชื่อมา 2,000 ปี!* |
| **1638** | **Galileo** | *Discorsi* — ตีพิมพ์ผลงาน + myth "Leaning Tower of Pisa" (ไม่จริง!) |
| **1687** | **Isaac Newton** | **F = ma** — a = F/m เชื่อมต่อแรงกับความเร่ง |
| | | ความเร่งเกิดจากแรง — ไม่ใช่สมบัติของวัตถุ |
| **1905** | **Albert Einstein** | SR: acceleration ไม่จำกัดแต่ velocity จำกัดที่ c |
| **1915** | **Einstein** | GR: **Equivalence Principle** — gravity = acceleration! |
| | | (คนในลิฟต์ไม่สามารถแยกได้ว่าอยู่ในสนามโน้มถ่วงหรือกำลังถูกเร่ง) |
| **2015** | **LIGO** | วัด gravitational wave = การเปลี่ยนแปลง acceleration ของ mirror ที่ 4 km → 10⁻¹⁸ m |

---

## ⚛️ นิยามทางฟิสิกส์

### Instantaneous Acceleration
```
a = dv/dt = d²r/dt²

ใน 3D:
a = a_x î + a_y ĵ + a_z k̂
  = (dv_x/dt) î + (dv_y/dt) ĵ + (dv_z/dt) k̂
  = (d²x/dt²) î + (d²y/dt²) ĵ + (d²z/dt²) k̂
```

### Average Acceleration
```
a_avg = (v₂ − v₁) / (t₂ − t₁) = Δv/Δt
```

### Uniform Acceleration (SUVAT)
| สูตร | หาได้ |
|------|-------|
| v = u + at | v เมื่อรู้ u, a, t |
| s = ut + ½at² | Displacement |
| s = vt − ½at² | อีกรูปแบบ |
| v² = u² + 2as | ไม่ต้องใช้ t |
| s = ½(u+v)t | ไม่ต้องใช้ a |

### Non-uniform Acceleration
```
เมื่อ a = a(t):
v(t) = u + ∫₀ᵗ a(τ) dτ
s(t) = ut + ∫₀ᵗ ∫₀ᵗ' a(τ) dτ dt'
```

---

## 🔬 ตัวอย่างความเร่งในชีวิตจริง

| สิ่งนี้ | ความเร่ง | หมายเหตุ |
|--------|---------|----------|
| 🍏 **วัตถุตก (gravity on Earth)** | **9.81 m/s²** (g) | มีทิศลง |
| 🚗 **รถยนต์ 0–100 km/h ใน 5 s** | ≈ **5.56 m/s²** | ≈ 0.57 g |
| 🏎️ **Formula 1 (0–300 km/h)** | ≈ **13.9 m/s²** | ≈ 1.4 g |
| ✈️ **Jet fighter takeoff (catapult)** | ≈ **30 m/s²** | ≈ 3 g |
| 🚀 **Space Shuttle launch** | ≈ **29–39 m/s²** | ≈ 3–4 g |
| 🪂 **Skydiver terminal velocity** | **0 m/s²** | a=0, v=55 m/s |
| 🎢 **Roller coaster loop** | ≈ 2–5 g | ความรู้สึกที่จุดต่ำสุด = mg + mv²/r |
| 🏓 **Tennis racket hit ball** | ≈ **10,000 m/s²** | ในช่วง ~5 ms |
| 💥 **Bullet in barrel** | ≈ **10⁶ m/s²** | ~0.5 ms, 500 m/s |
| ⚛️ **Particle in LHC** | ≈ **10¹⁰ m/s²** | centripetal in 27 km ring |
| 🌍 **Centripetal a ที่ศูนย์สูตร** | **0.034 m/s²** | จากการหมุนของโลก |
| 💫 **ดาวเทียมในวงโคจร** | **g ที่ระดับนั้น** | free fall → weightless |
| 🌞 **Gravity ที่ผิวดวงอาทิตย์** | **274 m/s²** | ≈ 28 g |
| 🕳️ **ที่ขอบฟ้าเหตุการณ์หลุมดำ** | → ∞ | spacetime gradient หัก |
| ⚛️ **Electron ใน hydrogen atom** | ≈ **10²² m/s²** | centripetal ใน Bohr model |

---

## 📐 หน่วยของความเร่ง

### SI Unit
| หน่วย | สัญลักษณ์ | ค่า |
|-------|-----------|-----|
| **m/s²** | — | 1 |
| **g** (gravity) | g | 9.80665 m/s² |

### หน่วยอื่นๆ
| หน่วย | ค่า (ใน m/s²) | ใช้ที่ไหน |
|-------|---------------|----------|
| **ft/s²** | 0.3048 | US |
| **Gal (galileo)** | 0.01 | Geodesy, seismology |
| **cm/s²** | 0.01 | CGS |
| **mGal** | 10⁻⁵ | Gravity surveys |
| **g** | 9.80665 | ความรู้สึก g-force |
| **Jerk (m/s³)** | — | อัตราเปลี่ยนของ a |
| **Planck acceleration** | c²/lᴘ ≈ 5.56×10⁵¹ m/s² | ขีดจำกัดสูงสุด |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Acceleration = เร็วขึ้น" | **ไม่** — Acceleration = velocity เปลี่ยน *ไม่ว่าเร็วขึ้นหรือช้าลง* — deceleration = acceleration ที่มีทิศตรงข้าม velocity |
| "a=0 = หยุดนิ่ง" | ไม่ — a=0 = velocity **คงที่** — อาจวิ่ง 100 km/h นิ่ง (a=0) ก็ได้ |
| "g-force = หน่วยของแรง" | g-force = **multiples of gravity** (1g = 9.81 m/s²) — วัดความเร่ง ไม่ใช่แรง |
| "Gravitational acceleration = constant เสมอ" | g เปลี่ยนตามตำแหน่ง: ขั้วโลก 9.832 m/s², ศูนย์สูตร 9.780 m/s², บน Mont Blanc 9.795 m/s² |
| "Centripetal acceleration ≠ จริง" | **มีจริง** — a_c = v²/r — รู้สึกเป็น "แรงหนีศูนย์กลาง" (centrifugal force = fictitious) |

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. ทำไมทุกวัตถุดกด้วยความเร่งเท่ากัน? (Equivalence Principle)**
F = ma (inertial mass) และ F = GMm/r² (gravitational mass) → a = (GM/r²) · m_g/m_i
ถ้า m_g = m_i (ซึ่ง Einstein ยกเป็นหลัก) → a = GM/r² — เท่ากันทุกวัตถุ!
— **Eötvös experiment (1889)** ยืนยัน m_g/m_i = 1 ด้วยความแม่นยำ 10⁻⁹

**2. Jerk — ทำไมถึงสำคัญ?**
Jerk = da/dt = d³r/dt³ → หน่วย m/s³
— ในรถไฟฟ้า: jerk = acceleration ที่เปลี่ยน **เร็วเกินไป** → ผู้โดยสารรู้สึกไม่สบาย
— สายการบิน: ควบคุม jerk ในการเร่งเครื่อง → ผู้โดยสารไม่รู้สึกกระตุก
— Roller coaster: ออกแบบความสนุกด้วย "jerk profile"

**3. Twin Paradox — เรื่องฝาแฝดกับการเดินทาง**
ฝาแฝดคนนึงอยู่โลก → อีกคนเดินทางด้วยจรวด v→c → กลับมา
- ฝาแฝดที่เดินทาง = อายุน้อยกว่า (time dilation)
- **คนที่ "accelerate" (ออกเดินทาง+กลับ) = คนที่แก่ช้ากว่า**
- นี่คือวิธีแก้ twin paradox: acceleration ทำให้กรอบทั้ง 2 **ไม่สมมาตร**

**4. Gravitational redshift — ความเร่งเปลี่ยนความถี่แสง**
ใน GR: แสงที่ออกจากสนามโน้มถ่วงสูง → ถูกดึงด้วย gravity → **สูญเสียพลังงาน → redshift**
— Pound–Rebka experiment (1959): ปล่อย γ-ray จากหอคอย 22.5 m → วัด redshift ได้ = v/c = gh/c² = 2.5×10⁻¹⁵ (สอดคล้อง GR!)

**5. คุณจะ "รู้สึก" acceleration ได้ตอนไหน?**
- ที่ a > 0.001 g → คนเริ่มรู้สึกได้
- ที่ a > 0.01 g → โต๊ะเอียง ถ้วยขยับ
- ที่ a ≈ 1 g → น้ำหนักตัวปรกติ
- ที่ a ≈ 3 g → หายใจลำบาก (fighter pilot)
- ที่ a > 5 g → G-LOC (หมดสติ ถ้าไม่ฝึก)
- ที่ a ≈ 9 g → ถึงขีดจำกัดมนุษย์
- ที่ a ≈ 100 g → รถชน → อันตรายถึงชีวิต
- ที่ a ≈ 1,000 g → ทนได้แค่ ms
- ที่ a → ∞ → หลุมดำ!

---

## 🔗 อ้างอิง

- Galileo (1638). *Discorsi e Dimostrazioni Matematiche Intorno a Due Nuove Scienze*
- Newton (1687). *Philosophiæ Naturalis Principia Mathematica*
- Einstein (1905). Special Relativity — *Annalen der Physik*
- Einstein (1907). Equivalence Principle
- Eötvös, R. v. (1889). "Über die Anziehung der Erde auf verschiedene Substanzen"
- Pound, R. V. & Rebka, G. A. (1959). "Gravitational Red-Shift in Nuclear Resonance"
- BIPM (2019). *The International System of Units*