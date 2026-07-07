---
title: Speed and Velocity
field: Mechanics — Kinematics
type: physical-quantity
si_unit: metre per second (m/s)
symbol: v (velocity), u (initial velocity), s (speed), c (speed of light)
dimension: [L·T⁻¹]
version: 1
tags: [velocity, speed, kinematics, motion, si-units, history]
related_lectures: [topic12_motion]
related_terminology: [kinematics, inertia, momentum, newtons_laws]
related_physical_quantity: [time, length, acceleration, momentum, energy, frequency]
---

# 🏃 Speed and Velocity

> **💡 ความแตกต่างสำคัญ:**
> - **Speed** = scalar (บอกแต่ขนาด: "60 km/h")
> - **Velocity** = vector (บอกขนาด + ทิศทาง: "60 km/h ไปทางเหนือ")
>
> ในชีวิตประจำวันใช้คำว่าความเร็วปนกัน แต่ในฟิสิกส์ IGCSE–A-Level ต้องแยกให้ออก!

---

## 📜 ประวัติศาสตร์ — การวัด "ความเร็ว" ของมนุษย์

### สมัยโบราณ — การรับรู้ความเร็วโดย感官

| ยุค | การวัด | รายละเอียด |
|-----|--------|-------------|
| **~3000 BCE** | **การเดินของมนุษย์** | ~5 km/h (3 mph) — ใช้เดินทาง, วัดด้วย sundial + pacing |
| **~2000 BCE** | **ม้า** | ~15 km/h (วิ่งเหยาะ), ~40 km/h วิ่งเต็มที่ — **เร็วที่สุดในโลกก่อนศตวรรษที่ 19** |
| **~1000 CE** | **เรือใบ** | ~10–20 km/h — ขึ้นกับลม, วัดด้วย chip log |
| **ศตวรรษที่ 16** | Chip log (การเดินเรือ) | ท่อนไม้ผูกเชือกปม → โยนท้ายเรือ → นับนอต (knot = 1 nautical mile/h) |
| **ศตวรรษที่ 17** | Galileo | พยายามวัด **ความเร็วแสง** — ใช้ตะเกียงบนเนินเขาคนละลูก — แต่เร็วเกิน → ได้เพียง "เร็วมาก" |

### กำเนิดแนวคิด "Velocity" ทางฟิสิกส์

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **~1604** | **Galileo Galilei** | — การทดลอง inclined plane → **v ∝ t** (ความเร็วเพิ่มขึ้นตามเวลาในการตก) |
| | | — เป็นคนแรกที่แยก **uniform motion** (v = constant) จาก **accelerated motion** (v ≠ constant) |
| **1638** | Galileo | *Discorsi e Dimostrazioni Matematiche* — วางรากฐาน kinematics: s ∝ t² สำหรับ accelerated motion from rest |
| **1644** | **René Descartes** | กำหนดแนวคิด **momentum (mv)** — นับเป็น vector quantity (ทิศทางสำคัญ!) |
| **1687** | **Isaac Newton** | *Principia* — กฎการเคลื่อนที่ 3 ข้อ |
| | | — **Lex I:** v = constant ถ้าไม่มีแรงภายนอก |
| | | — **Lex II:** F = dp/dt = m·a (a = dv/dt) |
| | | — แนวคิดว่า velocity = derivative ของ position |
| **1730s** | **Leonhard Euler** | วางรากฐาน **calculus of motion** → v = dx/dt เป็น formal definition |
| **1847** | Hermann von Helmholtz | **Conservation of energy** — ½mv² = kinetic energy |
| **1905** | **Albert Einstein** | **Special Relativity** — ความเร็วแสง c = **constant** สำหรับทุกผู้สังเกต (ขัดกับ intuition!) |
| | | — v ไม่สามารถบวกกันแบบคลาสสิกอีกต่อไป → relativistic velocity addition |
| **1915** | Einstein | General Relativity — velocity ในสนามโน้มถ่วง → geodesic motion |

---

## ⚛️ นิยามทางฟิสิกส์ — Calculus View

### Instantaneous Velocity
> **Velocity** = **อนุพันธ์อันดับหนึ่งของ displacement เทียบกับเวลา**
>
> **v** = d**r**/dt

| ปริมาณ | นิยามทางคณิตศาสตร์ | หน่วย SI |
|--------|-------------------|----------|
| **Speed** (อัตราเร็ว) | s = \|v\| = √(v_x² + v_y² + v_z²) | m/s |
| **Average speed** | s_avg = total distance / total time | m/s |
| **Average velocity** | **v**_avg = total displacement / total time | m/s |
| **Instantaneous speed** | \|d**r**/dt\| | m/s |
| **Instantaneous velocity** | d**r**/dt | m/s |

### การแปลงหน่วยระหว่างระบบ

| m/s → km/h | km/h → m/s | mph → m/s |
|------------|------------|-----------|
| × 3.6 | ÷ 3.6 | × 0.44704 |

### ตัวอย่างการคำนวณ

| การเคลื่อนที่ | การหา velocity |
|-------------|---------------|
| v คงที่ (uniform) | v = s/t — ง่ายที่สุด |
| v เปลี่ยนแบบ uniform accel | v = u + at — SUVAT |
| v เปลี่ยนแบบ non-uniform | v = ds/dt — ต้องใช้ calculus |
| v จากพื้นที่ใต้กราฟ a-t | v(t) = v₀ + ∫₀ᵗ a(τ) dτ |
| v ที่ความเร็วสูง (relativistic) | v_actual = (v₁+v₂)/(1+v₁v₂/c²) |

---

## 🚀 ความเร็วในขีดจำกัดต่างๆ — Physical Speed Limits

### Maximum Speed in Universe

| ขีดจำกัด | ความเร็ว | รายละเอียด |
|----------|---------|-------------|
| **Speed of light in vacuum (c)** | **299,792,458 m/s** ≈ 3 × 10⁸ m/s | ขีดจำกัดสูงสุดของข้อมูลและพลังงาน — **ไม่มีอะไรเกิน c** (Einstein, 1905) |
| **Speed of light in medium** | c/n | n = refractive index — ตัวอย่าง: c/น้ำ ≈ 225,000 km/s |
| **Cherenkov radiation** | > c/n | อนุภาคใน medium เร็วกว่าแสงใน medium → ปล่อยรังสีสีน้ำเงิน (Cherenkov, 1934) |
| **Speed of gravity** | **c** | Gravitational wave = c (LIGO 2015, GW170817) |

### Speed Records ที่น่าสนใจ

| สิ่งนี้ | ความเร็ว | หมายเหตุ |
|---------|----------|----------|
| 🐆 **Cheetah** | 112 km/h (≈ 31 m/s) | สัตว์บกที่เร็วที่สุด |
| 🚗 **Thrust SSC** | 1,228 km/h (Mach 1.016) | ทำลายกำแพงเสียงบนบก — Andy Green, 1997 |
| ✈️ **SR-71 Blackbird** | ≈ 3,540 km/h (Mach 3.3) | เครื่องบินเจ็ทเร็วที่สุด |
| 🚀 **New Horizons (Pluto)** | 16.26 km/s (≈ 58,500 km/h) | ความเร็วหลุดจากโลก fastest launch |
| ☀️ **Earth orbiting Sun** | ≈ 29.78 km/s (≈ 107,000 km/h) | เฉลี่ย |
| 🌌 **Milky Way** | ≈ 600 km/s (relative to CMB) | เคลื่อนที่สัมพันธ์กับ CMB |
| ⚡ **Electron in accelerator** | 0.9999999995 c (LHC) | 6.5 TeV — ≈ 3 cm/s ช้ากว่า c |
| 🔭 **Cosmic rays** | 0.9999999999999999999 c | สูงที่สุดที่เคยวัด (~3 × 10²⁰ eV) |
| ⚛️ **Neutrino** | ~0.99999999999999 c | แทบเท่า c (แต่ไม่ถึง) |

---

## 🔬 เครื่องมือวัดความเร็ว (Timeline)

| อุปกรณ์ | ยุค | หลักการ |
|----------|-----|---------|
| 🧭 **Chip log** | ~1500s | โยนไม้ท้ายเรือ → นับ knots ใน 28 s → 1 knot = 1 NM/h |
| ⏱️ **Stopwatch + markers** | Galileo | ระยะทางที่รู้ / เวลาจาก stopwatch → v_avg = Δs/Δt |
| 🚗 **Speedometer** | 1902 (Oldsmobile) | เกียร์หมุนตามเพลา → magnetic drag → เข็มชี้ |
| 🚔 **Radar gun** | 1947 (John Barker) | Doppler shift ของคลื่นไมโครเวฟสะท้อนจากรถ → f' = f₀(1+2v/c) |
| 🛰️ **GPS speed** | 1990s | Doppler shift จาก satellite carrier + position differencing |
| 🎯 **Laser speed gun (LIDAR)** | 1990s | Time-of-flight pulse → Δt เปลี่ยนตาม v → แม่นยำกว่า radar มาก |
| 💡 **Laser Doppler Velocimetry (LDV)** | 1980s | Doppler shift ของ laser จากอนุภาคในของไหล → วัด flow velocity |
| 🧲 **Electromagnetic flowmeter** | 1950s | Faraday's law: v = V/(B·d) — ของไหลนำไฟฟ้าในท่อ |
| 🌟 **Stellar radial velocity** | 1900s | Doppler shift ของ spectral lines (redshift/blueshift): v/c ≈ Δλ/λ |

---

## 📐 หน่วยของความเร็ว (Speed / Velocity Units)

### SI Unit
| หน่วย | สัญลักษณ์ | ค่า |
|-------|-----------|-----|
| **metre per second** | m/s | 1 |
| **kilometre per hour** | km/h | 0.277777... m/s |

### หน่วยอื่นๆ

| หน่วย | ค่า (ใน m/s) | ใช้ที่ไหน |
|-------|-------------|----------|
| **Knot (kn)** | 0.514444... m/s (1 NM/h) | การเดินเรือ, การบิน |
| **Miles per hour (mph)** | 0.44704 m/s (พอดี) | US, UK (road signs) |
| **Feet per second (ft/s)** | 0.3048 m/s | US engineering |
| **Mach (M)** | 343 m/s (ที่ 20°C ระดับน้ำทะเล) | การบินความเร็วสูง (1 Mach = speed of sound) |
| **Speed of sound (c_sound)** | 343 m/s (อากาศ 20°C), 1,482 m/s (น้ำ), 5,960 m/s (เหล็ก) | ขึ้นกับตัวกลาง |
| **Speed of light (c)** | 299,792,458 m/s | **ขีดจำกัดสูงสุดของจักรวาล** |
| **Blink** | ~5 m/s | เปลือกตาปิด (~0.1 s, ระยะ ~0.5 m) |
| **Knot (โบราณ)** | ~0.514 m/s | แต่ละ "knot" = 47 ft 3 in ของเชือกใน 28 s (≈ 1 NM/h) |
| **League per fortnight** | ≈ 0.000083 m/s | หน่วยตลก — ใช้ในการสอน conversion |
| **Natural unit (c)** | 1 (ใน unit where c = 1) | ฟิสิกส์อนุภาค, relativity |
| **Planck velocity (vᴘ)** | **c** (= 1 ใน Planck units) | ความเร็วสูงสุดในธรรมชาติ |

### ตัวอย่างการแปลง

```
90 km/h  = 90 ÷ 3.6 = 25 m/s
10 m/s   = 10 × 3.6 = 36 km/h
60 mph   = 60 × 0.44704 = 26.8224 m/s ≈ 96.6 km/h
30 knots = 30 × 0.514444 = 15.4333 m/s ≈ 55.6 km/h
Mach 2   = 2 × 343 = 686 m/s ≈ 2,470 km/h
```

---

## 🌍 ความเร็วในชีวิตจริงและธรรมชาติ

| การเคลื่อนที่ | ความเร็ว | ความรู้สึก |
|-------------|----------|-----------|
| 👣 **เดินปกติ** | 1.4 m/s (5 km/h) | สบาย |
| 🏃‍♂️ **วิ่งเหยาะ** | 3 m/s (11 km/h) | ปานกลาง |
| 🚗 **รถในเมือง** | ~15 m/s (50 km/h) | ปกติ |
| 🛣️ **รถบนทางด่วน** | ~30 m/s (110 km/h) | เร็วแต่ควบคุมได้ |
| ✈️ **เครื่องบินโดยสาร** | ~250 m/s (900 km/h) | มองไม่เห็นความเร็วจากภายใน |
| 🔇 **Speed of sound (Mach 1)** | 343 m/s (1,235 km/h) | sonic boom! |
| 🚀 **จรวดขึ้น orbit** | ~8 km/s (≈ 29,000 km/h) | g-force ~3–4 g |
| 🌍 **หนีโลก (escape velocity)** | **11.2 km/s** (≈ 40,320 km/h) | ไม่ต้องใช้แรงขับอีก |
| 🌞 **หนีระบบสุริยะ** | **42.1 km/s** (≈ 151,600 km/h) | จากวงโคจรโลก |
| 🚀 **New Horizons** | 16.26 km/s (58,500 km/h) | หนีโลกเร็วที่สุดเท่าที่มนุษย์สร้าง |
| 🌌 **ดาราจักรของเรา** | ~600 km/s | เทียบกับ CMB |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Speed = Velocity" | **ไม่** — Speed = scalar (magnitude only), Velocity = vector (magnitude + direction) — เปลี่ยน direction = เปลี่ยน velocity แต่ speed อาจ不变 |
| "ความเร็วแสงเปลี่ยนได้ตามผู้สังเกต" | **ผิด** — c = constant ≈ 3×10⁸ m/s ใน vacuum — ทุกคนวัด c ได้เท่ากัน ไม่ว่าเคลื่อนที่แค่ไหน (หลักของสัมพัทธภาพ!) |
| "เวลา + ความเร็ว = ระยะทาง" | ถูกสำหรับ **uniform speed** — v=s/t → s=vt. แต่สำหรับ accelerated motion → ต้องใช้ calculus หรือ SUVAT |
| "วัตถุที่เร็วกว่าแสง → อนาคต" | **ไม่ได้** — ใน SR: ยิ่งเข้าใกล้ c → energy ต้องใช้ → ∞ — ไม่มีวัตถุ mass > 0 ถึง c ได้ |
| "0 m/s = หยุดนิ่ง" | **สัมพัทธ์** — earth หมุนรอบแกน ~460 m/s ที่ศูนย์สูตร + หมุนรอบดวงอาทิตย์ 30 km/s + หมุนรอบ galaxy 230 km/s → ไม่มี "หยุดนิ่งสัมบูรณ์" |
| "Braking distance ขึ้นกับ speed เท่านั้น" | ขึ้นกับ **v²** — ถ้า speed เป็น 2× → braking distance = 4× |
| "ความเร็วของแสงใน fiber optic ≈ c" | **ไม่** — ใน fiber core (silica, n≈1.5) → v ≈ 200,000 km/s (≈ 0.67c) |

---

## 🔄 ความเร็วในสัมพัทธภาพ — Relativistic Velocity Addition

ที่ everyday speed (v ≪ c), เราใช้ v_total = v₁ + v₂
แต่ที่ v → c, Einstein บอกว่า:

```
v_total = (v₁ + v₂) / (1 + v₁·v₂/c²)
```

| ตัวอย่าง | Classical | Relativistic |
|---------|-----------|-------------|
| รถ 100 km/h + 100 km/h | 200 km/h | ≈ 199.9999999999 km/h (ไม่ต่าง) |
| 0.6c + 0.6c | 1.2c | **0.882c** (ไม่เกิน c!) |
| 0.9c + 0.9c | 1.8c | **0.9945c** |
| c + c | 2c | **c** |
| 0.9999c + 0.9999c | 1.9998c | **0.999999995c** |

> **ข้อสรุป:** ไม่มีทางรวม velocity แล้วเกิน c — nature มีขีดจำกัด speed limit!

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. ทำไมความเร็วแสงถึงสูงสุด?**
ใน relativity — c คือ speed of causality (ความเร็วของเหตุและผล) — ถ้าอะไรไปเร็วกว่า c → จะเกิด **causal paradox** (ผลมาก่อนเหตุ) — นี่ไม่ใช่แค่ engineering limit แต่เป็นกฎของ spacetime ที่หลีกเลี่ยงไม่ได้!

**2. Escape velocity — หนีโลกต้องเร็วแค่ไหน?**
```
v_escape = √(2GM/R)
สำหรับโลก: v_escape = √(2 × 6.67×10⁻¹¹ × 5.97×10²⁴ / 6.37×10⁶) ≈ 11.2 km/s
```
สำหรับหลุมดำ: R = 2GM/c² (Schwarzschild radius) → v_escape = c → แสงยังหนีไม่ได้!

**3. ความเร็วของเสียง ขึ้นกับอะไร?**
```
c_sound = √(γ·RT/M)
γ = specific heat ratio (≈ 1.4 สำหรับอากาศ)
R = universal gas constant
T = temperature (K)
M = molar mass
```
→ ที่อุณหภูมิสูง → เสียงเดินทางเร็วขึ้น
→ ที่ความสูง (อากาศเย็น) → เสียงช้าลง: Concorde จะบิน Mach 2 ที่ ~18 km = จริงๆ ≈ 500 m/s (ไม่ใช่ 340 m/s + 2x)

**4. Four-velocity — velocity ใน spacetime**
ใน SR, velocity 3D เปลี่ยนไปตามกรอบ → Einstein ใช้ **4-velocity** (U^μ):
```
U = γ(c, v_x, v_y, v_z)
|U| = c (constant!) — ทุกคนใน spacetime มี speed = c
```
— คุณกำลังเคลื่อนที่ใน spacetime ด้วย speed = c เสมอ — เวลาผ่านไป (iy component) หรือเคลื่อนที่ใน space (xyz components) — total magnitude = c เสมอ

**5. Terminal velocity — ทำไมวัตถุตกไม่เร็วขึ้นเรื่อยๆ?**
เมื่อ drag force = weight: mg = ½ρv²C_dA → v_terminal = √(2mg/ρC_dA)
| วัตถุ | v_terminal |
|-------|-----------|
| Skydiver (spread-eagle) | ~55 m/s (200 km/h) |
| Skydiver (head-down) | ~90 m/s (320 km/h) |
| Raindrop (1 mm) | ~6.5 m/s |
| Baseball | ~42 m/s (150 km/h) |
| Cat (พลิกตัวลง) | ~27 m/s (100 km/h) → รอดตกจากสูง! |

**6. ความเร็วสัมพัทธ์ของ GPS — ต้องแก้ relativistic effects**
ดาวเทียม GPS โคจร ≈ 3.9 km/s →
- SR time dilation: นาฬิกาช้าลง (−7.2 μs/day)
- GR gravitational blueshift: นาฬิกาเร็วขึ้น (+45.9 μs/day)
- Net = +38.6 μs/day → ถ้าไม่แก้ → GPS drift ≈ 11 km/day!

---

## 🔗 อ้างอิง

- Galileo Galilei (1638). *Discorsi e Dimostrazioni Matematiche Intorno a Due Nuove Scienze* (Two New Sciences)
- Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*
- Einstein, A. (1905). "On the Electrodynamics of Moving Bodies" — *Annalen der Physik*
- Einstein, A. (1915). "The Field Equations of Gravitation"
- Lorentz, H. A. (1904). "Electromagnetic phenomena in a system moving with any velocity less than that of light"
- Feynman, R. P. (1963). *The Feynman Lectures on Physics Vol. I* — Chapter 8: Motion
- MIT Haystack Observatory — GPS and Relativity
- National Physical Laboratory (UK). *The Chip Log — History of Speed Measurement at Sea*
- Beall, J. et al. (2017). "GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral" — *Phys. Rev. Lett.*

### ทดลองด้วยตัวเอง

เปิดไฟล์กราฟใน `~/InteractiveLecture/graphs/`:
- `kinematics_1_horizontal_graphs.html` — การเคลื่อนที่แนวราบ, jerk model, stop-at-v=0
- `kinematics_3_vertical_graphs_freefall.html` — freefall 3 กราฟ (s, v, a) เปลี่ยน g ได้
- `kinematics_4_vertical_graphs_terminal_v.html` — terminal velocity 2-phase (skydive)
- `kinematics_5_advanced_velocity_time_graphs.html` — uniform + non-uniform scenarios