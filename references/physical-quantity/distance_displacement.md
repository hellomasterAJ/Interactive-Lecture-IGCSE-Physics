---
title: Distance and Displacement
field: Mechanics — Kinematics
type: physical-quantity
si_unit: metre (m)
symbol: s (displacement), d (distance)
dimension: [L]
version: 1
tags: [distance, displacement, kinematics, motion, si-units]
related_lectures: [topic12_motion]
related_terminology: [kinematics, velocity, acceleration]
related_physical_quantity: [time, velocity, acceleration, length, speed]
---

# 📏 Distance and Displacement

> **💡 หัวใจสำคัญ:**
> - **Distance (ระยะทาง)** = scalar (บอกแต่ขนาด: "วิ่ง 5 km")
> - **Displacement (การกระจัด)** = vector (บอกขนาด + ทิศทาง: "เคลื่อนที่ 3 km ไปทางตะวันออก")
>
> Distance ≥ |Displacement| เสมอ — เท่ากันก็ต่อเมื่อเคลื่อนที่เป็นเส้นตรงไม่เปลี่ยนทิศ

---

## 📜 ประวัติศาสตร์ — การวัด "ไกล" ของมนุษย์

### สมัยโบราณ — วัดระยะทางด้วยร่างกาย

| ยุค/อารยธรรม | หน่วย | รายละเอียด |
|-------------|-------|-------------|
| **~10,000 BCE** | **การก้าว (pace)** | มนุษย์ยุคหินวัดระยะด้วยการก้าว — คิดเป็น "กี่วันเดินทาง" |
| **~3000 BCE (อียิปต์)** | **Cubit (ศอก)** | ระยะจากข้อศอกถึงปลายนิ้ว ≈ 52.3 cm — ใช้สร้างมหาพีระมิด |
| **~2000 BCE (อียิปต์)** | **Iteru (river measure)** | ≈ 10.5 km — ระยะทางตามแม่น้ำไนล์ระหว่าง 2 เมือง |
| **~800 BCE (กรีก)** | **Stadium (stadion)** | ≈ 185–192 m — ระยะทางของสนามกีฬา Olympia |
| | | **Eratosthenes (~240 BCE)** ใช้ stadion คำนวณเส้นรอบวงโลก = 250,000 stadia ≈ 46,250 km (แม่นยำ ~15%!) |
| **~500 BCE (เปอร์เซีย)** | **Parasang (παρασάγγης)** | ≈ 5.7 km — ระยะทางที่ทหารเดินใน 1 ชม. Herodotus ใช้บรรยายขนาดจักรวรรดิ |
| **~200 BCE (โรมัน)** | **Mille passus (mile)** | ≈ 1,480 m — 1,000 ก้าวคู่ (passus = 5 pedes) → รากของ "mile" |
| | **Roman road** | ถนนโรมันยาวรวม ≈ 400,000 km — ปักคิลโลเมตรทุก mille passus |
| **~1000 CE (จีน)** | **Li (里)** | ≈ 500 m — มาตรฐานวัดระยะทางในจีน — Zhou dynasty กำหนด 300 bu = 1 li |
| **~1800 (ไทย)** | **เส้น (sen)** | 40 m — 20 วา = 1 เส้น, 400 เส้น = 1 โยชน์ (~16 km) |

### ยุคสำรวจ — วัดพิสัยไกล

| ปี/ช่วง | เหตุการณ์ | รายละเอียด |
|----------|-----------|-------------|
| **~250 BCE** | **Eratosthenes** | แท่งไม้ใน Alexandria vs Syene → เงาต่างกัน 7.2° → โลกเส้นรอบวง = 250,000 stadia |
| **~150 CE** | **Ptolemy** | *Geography* — ใช้ latitude/longitude ระบบแรกของโลก |
| **~1600** | **Triangulation** | Gemma Frisius, Willebrord Snellius — วัดระยะทางด้วยสามเหลี่ยม — รากฐานการทำแผนที่สมัยใหม่ |
| **~1735** | **French Geodesic Mission** | Bouguer, La Condamine — วัด 1° ของ latitude ในเปรู vs Lapland → พิสูจน์โลกแป้นขั้ว |
| **1792–1798** | **Delambre & Méchain** | วัดส่วนของ Paris Meridian → กำหนด 1 เมตร = 1/10,000,000 ของ Pole–Equator |
| **1830s** | **Great Trigonometrical Survey of India** | George Everest — วัดเทือกเขาหิมาลัย → Mount Everest (29,002 ft) ตั้งชื่อตาม |

### ยุคอวกาศ — วัดระยะทางในจักรวาล

| ปี | เหตุการณ์ | รายละเอียด |
|----|----------|-------------|
| **1672** | **Cassini & Richer** | parallax ของ Mars → วัด AU ได้ ≈ 140 million km (ใกล้เคียงมาก) |
| **1838** | **Friedrich Bessel** | parallax ของ 61 Cygni → ระยะทางถึงดาว = 10.4 ly (แม่นยำ!) |
| **1920** | **Edwin Hubble** | ระยะทางถึง Andromeda = 900,000 ly → พิสูจน์ว่าหมอกนอกทางช้างเผือก = ดาราจักรอื่น |
| **1969** | **Apollo 11 — Lunar Laser Ranging** | สะท้อน laser จาก retroreflector บนดวงจันทร์ → วัดระยะ Earth–Moon = 384,400 km ± 1 cm |
| **2015** | **LIGO** | วัดคลื่นความโน้มถ่วงจาก GW150914 — ระยะทาง 1.3 พันล้านปีแสง |

---

## ⚛️ นิยามทางฟิสิกส์

### Displacement (การกระจัด)
> **Displacement = การเปลี่ยนแปลงของตำแหน่ง = เวกเตอร์จากจุดเริ่มต้นไปยังจุดสิ้นสุด**

```
ใน 1 มิติ:
s = x_final − x_initial

ใน 2–3 มิติ:
s = r_final − r_initial = (Δx)î + (Δy)ĵ + (Δz)k̂

ขนาดของ displacement:
|s| = √(Δx² + Δy² + Δz²)
```

### Distance (ระยะทาง)
> **Distance = scalar = ความยาวทั้งหมดของเส้นทางที่เดินทางจริง**

```
Distance = ʃ |dr| = ผลรวมของทุก segment ตลอดเส้นทาง

Distance ≥ |Displacement|
Distance = |Displacement| เมื่อเคลื่อนที่เป็นเส้นตรงโดยไม่เปลี่ยนทิศ
```

### ความสัมพันธ์กับปริมาณอื่น

| ปริมาณ | ความสัมพันธ์กับ displacement |
|--------|---------------------------|
| **Velocity (v)** | v = ds/dt (derivative ของ displacement) |
| **Speed (s)** | s = \|v\| = \|ds/dt\| — ไม่สนใจทิศทาง |
| **Acceleration (a)** | a = dv/dt = d²s/dt² |
| **Area under v-t graph** | = net displacement (สเกลาร์กรณี 1D) |
| **Integral of speed** | = total distance = ∫\|v\| dt |

---

## 🗺️ ตัวอย่างที่แยก Distance vs Displacement

### ตัวอย่างที่ 1 — เดินไป-กลับ

| | A → B → A |
|---|----------|
| **เส้นทาง** | เดินจากบ้านไปร้าน 300 m → กลับบ้าน |
| **Distance** | 300 + 300 = **600 m** |
| **Displacement** | **0 m** (กลับมาที่เดิม) |

### ตัวอย่างที่ 2 — เส้นโค้ง vs เส้นตรง

| | A → B (ทางอ้อม) | A → B (ทางตรง) |
|---|----------------|---------------|
| **Distance** | **15 km** (อ้อมเขา) | **8 km** |
| **Displacement** | **8 km** ตะวันออก | **8 km** ตะวันออก |
| | ทั้งสองทาง displacement = เท่ากัน | แต่ distance ต่างกัน |

### ตัวอย่างที่ 3 — วงกลม

| | ครบ 1 รอบ | ครึ่งรอบ | ¼ รอบ |
|---|----------|---------|-------|
| **Distance** | 2πR | πR | πR/2 |
| **Displacement** | **0** | **2R** (เส้นผ่านศูนย์กลาง) | **R√2** |
| **ทิศทาง displacement** | — | ทิศจากจุดเริ่ม→จุดสิ้นสุด | ทำมุม 45° |

### ตัวอย่างที่ 4 — ทางโค้งใดๆ (calculus)
```
ถ้า r(t) = (3t)î + (2t²)ĵ
v(t) = dr/dt = (3)î + (4t)ĵ
speed s(t) = |v| = √(3² + (4t)²) = √(9 + 16t²)

Total distance from t=0 ถึง t=2:
Distance = ∫₀² √(9 + 16t²) dt ≈ 13.78 m

Displacement = r(2) − r(0) = (6)î + (8)ĵ → |s| = √(6²+8²) = 10 m
```

> **สังเกต:** Distance (13.78 m) > Displacement (10 m) เพราะเส้นทางโค้ง

---

## 🔬 วิธีการวัดระยะทาง (Distance Measurement)

### วิธีหลัก — 5 แนวทาง

| วิธี | หลักการ | ช่วง | ความแม่นยำ |
|------|---------|------|-------------|
| 🦶 **Pacing / Gaging** | นับก้าว × ความยาวก้าว | m – km | ±5–10% |
| 📏 **Tape / Chain** | เทียบกับมาตรฐาน (steel tape, Gunter's chain) | cm – 100 m | ±0.1% |
| 🗺️ **Triangulation** | มุมของสามเหลี่ยมจาก 2 จุดรู้ → side length | m – หลาย km | ±0.01% |
| 💡 **Time-of-flight (LIDAR, radar, sonar)** | v × Δt / 2 (สะท้อนกลับ) | cm – AU | ±1 cm (Lunar ranging) |
| 🔭 **Parallax** | มุมเปลี่ยนเมื่อมองจาก 2 จุด → d = baseline/θ | ภายใน galaxy (~10⁴ ly) | ±0.001″ (GAIA) |
| 🔴 **Redshift** | z = Δλ/λ → v = c·z → d = v/H₀ (Hubble's law) | galaxy ไกล (~10¹⁰ ly) | ±10% |
| ⭐ **Standard candle** | เปรียบเทียบ luminosity ที่รู้ vs วัดได้ → d = √(L/4πF) | ภายในจักรวาล | ±1–20% |

### เครื่องมือสำคัญในประวัติศาสตร์

| อุปกรณ์ | ปี | วัดอะไร | หลักการ |
|----------|-----|---------|---------|
| 📐 **Groma** | ~300 BCE (โรมัน) | มุมฉากในที่ดิน | เสา + เส้นดิ่ง 4 เส้น |
| 📏 **Gunter's chain** | 1620 | ระยะทางในที่ดิน | โซ่ 66 ft (= 1 chain) — ใช้ใน surveying จนถึง 1900s |
| 🗺️ **Theodolite** | ~1571 (Leonard Digges) | มุมแนวนอน+แนวตั้ง | telescope + angle scale |
| 📐 **Plane table** | ~1590 | แผนที่ภาคสนาม | กระดาน + alidade มองผ่าน |
| 💡 **EDM (Electronic Distance Measurement)** | 1950s | ระยะทางด้วยคลื่น | microwave (Tellurometer) / laser (Geodimeter) |
| 🛰️ **GPS** | 1990s | ตำแหน่ง 3D | time-of-flight จาก ≥4 satellites |
| 🔭 **GAIA** | 2013–2025 | parallax 1.7 พันล้านดาว | accuracy 0.01 milliarcsecond |

---

## 📐 หน่วยของ Distance / Displacement

เนื่องจาก distance/displacement มีมิติ [L] เหมือน length → หน่วยเหมือนกันทั้งหมด — ดูเพิ่มใน `length.md`

| หน่วยเด่นๆ | ค่าใน m | ใช้กับ |
|------------|---------|--------|
| **μm, mm, cm, m, km** | — | ชีวิตประจำวัน |
| **Astronomical Unit (AU)** | 1.495978707 × 10¹¹ m | ภายในระบบสุริยะ |
| **Light-year (ly)** | 9.461 × 10¹⁵ m | ระหว่างดาว |
| **Parsec (pc)** | 3.086 × 10¹⁶ m (= 3.26 ly) | ดาราศาสตร์ |
| **Fermi** | 10⁻¹⁵ m | ฟิสิกส์นิวเคลียร์ |

---

## 🌍 ระยะทางในชีวิตจริงและจักรวาล

| ระยะทาง | ค่า | การเทียบ |
|---------|-----|----------|
| 🧬 **เส้นผ่าศูนย์กลาง DNA** | ~2.5 nm | 2.5 × 10⁻⁹ m |
| 🦠 **แบคทีเรีย** | ~1 μm | 10⁻⁶ m |
| ความหนากระดาษ | ~0.1 mm | 10⁻⁴ m |
| 🏃 **สนามฟุตบอล** | ~100 m | 10² m |
| 🏔️ **Mount Everest** | 8,848 m | 8.8 × 10³ m |
| 🛰️ **ISS orbit** | ~400 km | 4 × 10⁵ m |
| 🌍 **เส้นรอบวงโลก** | 40,075 km | 4 × 10⁷ m |
| 🌙 **โลก–ดวงจันทร์** | 384,400 km | 3.844 × 10⁸ m |
| ☀️ **โลก–ดวงอาทิตย์ (1 AU)** | 150 million km | 1.5 × 10¹¹ m |
| 🪐 **โลก–ดาวพลูโต** | ~40 AU | 6 × 10¹² m |
| ☀️ **ถึง Proxima Centauri** | 4.246 ly | 4 × 10¹⁶ m |
| 🌌 **เส้นผ่าศูนย์กลางทางช้างเผือก** | ~100,000 ly | 9.5 × 10²⁰ m |
| 🔭 **จักรวาลที่สังเกตได้** | 93 billion ly | 8.8 × 10²⁶ m |
| ⚛️ **Planck length (สเกลสั้นสุดที่รู้)** | 1.616 × 10⁻³⁵ m | — |

### สเกลการกระจัดในการทดลองฟิสิกส์

| การทดลอง | displacement ที่วัด |
|-----------|-------------------|
| **LIGO (gravitational wave)** | เปลี่ยนระยะทาง 4 km arms → ~10⁻¹⁸ m (1/1,000 ของโปรตอน!) |
| **LHC (particle collision)** | proton displacement ≈ 27 km loop ~11,000 ครั้ง/s |
| **Cassini–Huygens** | displacement Earth→Saturn ≈ 1.2 × 10¹² m (~8 AU) |
| **Voyager 1** | displacement ≈ 165 AU (≈ 2.5 × 10¹³ m) — วัตถุที่มนุษย์สร้างที่ไกลที่สุด! |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Distance = Displacement" | **ไม่** — Distance ≥ \|Displacement\| — distance คือทางที่เดินจริง, displacement คือ vector จากจุดเริ่ม→จบ |
| "Area under v-t graph = distance" | **ไม่เสมอไป** — area under v-t = **displacement** (คิดเครื่องหมาย ±) — area under **speed**-t = **distance** |
| "ที่ displacement = 0 → ไม่ได้ขยับ" | displacement = 0 ได้ถ้ากลับมาจุดเดิม แม้จะเดินมาไกลมาก |
| "GPS วัด displacement = ระยะทางที่รถวิ่ง" | GPS วัด displacement (<300 km/h → แก้แล้ว) หรือ distance ได้จากการ sampling ทุก 1 s → sum of segments |
| "ระยะทางเป็นปริมาณสัมบูรณ์" | **ไม่** — ในทฤษฎีสัมพัทธภาพ — **length contraction**: L = L₀/γ — วัตถุเคลื่อนที่ → สั้นลงเมื่อมองจากกรอบนิ่ง |
| "ระยะไกลในจักรวาล = มองเห็นเวลาโบราณ" | **ถูกต้องบางส่วน** — dly = ระยะที่แสงใช้ 1 ปี — มองดาว 10 ly = เห็นเมื่อ 10 ปีก่อน ไม่ใช่ "โบราณมาก" |
| "Parallax วัดได้ทุกที่ในจักรวาล" | **ไม่ได้** — GAIA วัดได้ถึง ~10⁴ ly (ทางช้างเผือก) — ไกลกว่านั้นต้องใช้ redshift หรือ standard candle |

---

## 🔄 ความสัมพันธ์กับปริมาณอื่น — Displacement เป็นรากฐาน

### 1D Kinematics (IGCSE / A-Level)

| สูตร | สิ่งที่หาได้ |
|------|-------------|
| **s = (u+v)t/2** | displacement จาก average velocity |
| **s = ut + ½at²** | displacement จาก uniform acceleration |
| **s = vt − ½at²** | displacement จาก velocity ตอนท้าย |
| **v² = u² + 2as** | ความสัมพันธ์ไม่ใช้ t |
| **s-phase in SHM** | x(t) = A·sin(ωt+φ) — displacement ใน simple harmonic motion |

### 2D/3D — Vector Displacement

```
s(t) = x(t)î + y(t)ĵ + z(t)k̂
r(t) = |s(t)| คือ distance from origin (not total distance traveled)
```

### General Relativity — Geodesic

ใน GR: displacement ไม่ใช่ "เส้นตรง" ใน space แต่เป็น **geodesic** ใน curved spacetime:
- ใกล้หลุมดำ → เส้นทางโค้งงอ
- Gravitational lensing → displacement ของแสงจากแหล่ง→ผู้สังเกต ถูกเบนโดย gravity

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. ทำไมสเกลจักรวาลถึงใช้ "light-year" — ซึ่งเป็นทั้งระยะทางและเวลา?**
1 light-year = ระยะทางที่แสงเดินทางใน 1 ปี ≈ 9.46 × 10¹⁵ m = 9,461 พันล้าน km
— สะดวกสำหรับดาราศาสตร์: บอกทั้งระยะทางและ "time lag" ของแสง
— **มองดาว 1,000 ly = เห็นเมื่อ 1,000 ปีก่อน**

**2. Length contraction — displacement ของวัตถุเปลี่ยนเมื่อเคลื่อนที่เร็ว?**
ใน SR:
```
L = L₀ / γ = L₀ · √(1 − v²/c²)
L₀ = proper length (ในกรอบที่วัตถุหยุดนิ่ง)
L = length ที่ผู้สังเกตเห็น (วัตถุเคลื่อนที่)
```
**ตัวอย่าง:**
- Muon เกิดที่ 10 km กับ speed 0.998c → γ ≈ 15.8
- ในกรอบของ muon: displacement โลก→บรรยากาศ = 10/15.8 ≈ **633 m** (เลยเห็น muon มีชีวิตถึงพื้น!)
- ในกรอบโลก: muon ยังต้องเดินทาง 10 km **แต่ time dilation ทำให้นาฬิกามิวออนช้า** → อยู่ได้นานพอ → **ผลลัพธ์เหมือนกัน!**

**3. Fermat's Principle — displacement ของแสง = เส้นทางที่ใช้เวลาน้อยที่สุด**
"แสงเดินทางจาก A → B ตามเส้นทางที่ใช้เวลา **น้อยที่สุด** (หรือ extremum)"
→ displacement ของแสงในตัวกลาง ≠ เส้นตรง → refraction (Snell's law) = application

**4. Displacement ใน quantum mechanics — probability amplitude**
ใน QM, particle ไม่มี "path" ที่แน่นอน → **Feynman path integral**: displacement = sum over ALL possible paths (อนันต์เส้นทาง!) → แต่ละ path มี phase = e^(iS/ℏ) → รวมกัน → ได้ probability
— ที่ macroscopic: paths อื่น cancel → ทาง classical โดดเด่น
— ที่ microscopic: ทุกทางมีผล → interference!

**5. Distance บนพื้นผิวโค้ง — ทรงกลม**
บนโลก: ระยะทางสั้นที่สุดระหว่าง 2 จุด = **great-circle distance** (geodesic ไม่ใช่เส้นตรง!)
```
โดยใช้ haversine formula:
a = sin²(Δφ/2) + cos φ₁·cos φ₂·sin²(Δλ/2)
c = 2 · atan2(√a, √(1−a))
d = R · c

R = 6,371 km (Earth radius)
φ, λ = latitude, longitude (radian)
```

นี่คือวิธีที่ **Google Maps** ใช้คำนวณระยะทางจริง — ไม่ใช่เส้นตรงบนแผนที่!

---

## 🔗 อ้างอิง

- Eratosthenes (~240 BCE). *On the Measurement of the Earth*
- Galileo Galilei (1638). *Discorsi e Dimostrazioni Matematiche Intorno a Due Nuove Scienze*
- Newton, I. (1687). *Principia Mathematica*
- Einstein, A. (1905). "On the Electrodynamics of Moving Bodies" — Special relativity
- Snellius, W. (1617). *Eratosthenes Batavus* — Triangulation method
- Bessel, F. W. (1838). "On the parallax of 61 Cygni" — *Monthly Notices of the Royal Astronomical Society*
- Hubble, E. (1929). "A Relation between Distance and Radial Velocity among Extra-Galactic Nebulae"
- GAIA Collaboration (2016–2025). *GAIA Data Release — Parallax of 1.7 billion stars*
- Feynman, R. P. (1965). *The Feynman Lectures on Physics Vol. I* — Chapter 8, 11
- BIPM (2019). *The International System of Units (SI)* — Definition of the metre

### เชื่อมโยงกับ InteractiveLecture

เปิดกราฟใน `~/InteractiveLecture/graphs/`:
- `kinematics_1_horizontal_graphs.html` — displacement จาก area ใต้ v-t graph
- `kinematics_3_vertical_graphs_freefall.html` — displacement-time graph
- `kinematics_5_advanced_velocity_time_graphs.html` — displacement ใน non-uniform scenarios