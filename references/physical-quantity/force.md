---
title: Force
field: Mechanics — Dynamics
type: physical-quantity
si_unit: newton (N)
symbol: F
dimension: [M·L·T⁻²]
version: 1
tags: [force, dynamics, mechanics, newton, si-units]
related_lectures: [topic15_forces]
related_terminology: [newtons_laws, newtons_first_law, newtons_second_law, newtons_third_law, inertia, momentum, impulse]
related_physical_quantity: [mass, acceleration, momentum, energy, pressure, work]
---

# 💪 Force

> **Force = สิ่งที่ทำให้วัตถุเปลี่ยนความเร็ว (accelerate) หรือเปลี่ยนรูปร่าง**
>
> F = ma (หรือ F = dp/dt) — หน่วย N

---

## 📜 ประวัติศาสตร์ — แนวคิด "แรง"

### สมัยโบราณ — แรงที่มองเห็น

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~350 BCE** | **Aristotle** | แบ่ง motion เป็น natural (ตก,ลอย) และ violent (ถูกบังคับ) |
| | | เชื่อผิด: "วัตถุหนักออกแรงมากกว่า" → วัตถุหนักตกเร็วกว่า |
| | | — ความเชื่อนี้อยู่ 2,000 ปี! |
| **~260 BCE** | **Archimedes** | ศึกษา **การถ่วงดุล** (static forces) |
| | | ค้นพบ **กฎการถ่ายแรง**: F_in/F_out = d_out/d_in |
| | | **"Give me a lever long enough and a place to stand, and I will move the Earth."** |
| **~550 CE** | John Philoponus | Impetus theory — โต้ Aristotle แต่มองข้าม |
| **~1021** | **Al-Biruni** (เปอร์เซีย) | วัดแรงโน้มถ่วงแบบ quantitative — ใกล้แนวคิด Newton |

### ยุคปฏิวัติ — วิทยาศาสตร์ของแรง

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~1590** | **Simon Stevin** | ทรงกลมบนระนาบเอียง — แรงที่ต้องใช้ ∥ sin θ |
| **~1604** | **Galileo Galilei** | Inclined plane → เริ่มแนวคิด inertia |
| | | **"วัตถุจะรักษาความเร็วถ้าไม่มีแรงมากระทำ"** — โต้ Aristotle |
| **1666** | **Newton** (อายุ 23) | **ปิดมหาวิทยาลัยเพราะกาฬโรค** → ที่บ้านคิดค้น Calculus, Optics, Gravity |
| **1687** | **Isaac Newton** | *Principia Mathematica* — **3 Laws of Motion** |
| | | — **Lex I:** Inertia |
| | | — **Lex II:** F = dp/dt |
| | | — **Lex III:** Action = Reaction |
| | | — **Universal Gravitation:** F = GMm/r² |
| **1785** | **Charles-Augustin de Coulomb** | F = k·q₁q₂/r² — **แรงไฟฟ้า** (similar structure to gravity!) |
| **1807** | **Thomas Young** | ใช้คำว่า "energy" ครั้งแรก — ปูทางแนวคิด energy–force relation |
| **1864** | **James Clerk Maxwell** | Electromagnetic force — unified electricity, magnetism, light |
| **1897** | **J.J. Thomson** | ค้นพบอิเล็กตรอน → electromagnetic force อธิบาย atomic level |
| **1915** | **Einstein (General Relativity)** | **แรงโน้มถ่วงไม่ใช่ "แรง"** → curvature of spacetime |
| **1930s** | **Yukawa, Fermi** | Strong & Weak nuclear force — Fundamental forces ที่ 3 และ 4 |
| **1970s** | **Standard Model** | Unify EM + Weak → Electroweak force (\(W^±, Z⁰\) bosons) |

---

## ⚛️ 4 Fundamental Forces (แรงพื้นฐานในจักรวาล)

| แรง | ความแรง (เทียบกับ strong = 1) | พิสัย | อนุภาคตัวกลาง | ตัวอย่าง |
|-----|-----------------------------|------|--------------|---------|
| **⚡ Strong nuclear** | **1** | 10⁻¹⁵ m (femtometer) | Gluons (g) | ยึด proton+neutron ในนิวเคลียส |
| **💡 Electromagnetic** | 10⁻² | ∞ (∼ 1/r²) | Photon (γ) | ไฟฟ้า, แม่เหล็ก, แสง, พันธะเคมี |
| **🔄 Weak nuclear** | 10⁻¹³ | 10⁻¹⁸ m | W, Z bosons | Beta decay, neutrino interaction |
| **🌌 Gravitational** | 10⁻³⁸ | ∞ (∼ 1/r²) | Graviton (?) | วงโคจร, ตก, แรงระหว่างมวล |

> **💡 สิ่งที่น่าสนใจ:** Electromagnetic ≈ 10³⁶ × gravitational → แม่เหล็กเล็กๆ ตัวเดียวเอาชนะ gravity ของโลก!

---

## 📐 หน่วยของแรง

### SI Unit
| หน่วย | สัญลักษณ์ | คำนิยาม |
|-------|-----------|---------|
| **newton** | N | 1 N = 1 kg·m/s² |

### SI Prefixes
| หน่วย | สัญลักษณ์ | ค่า | ใช้ที่ไหน |
|-------|-----------|-----|----------|
| **piconewton** | pN | 10⁻¹² N | แรงระหว่างโมเลกุล, optical tweezers |
| **nanonewton** | nN | 10⁻⁹ N | แรงระหว่างอะตอม (AFM tip) |
| **micronewton** | μN | 10⁻⁶ N | ฝุ่น, แรงคาปิลลารี |
| **millinewton** | mN | 10⁻³ N | แรงของแมลง, droplet |
| **newton** | N | 1 | แรงในชีวิตประจำวัน (แอปเปิล ≈ 1 N) |
| **kilonewton** | kN | 10³ N | รถยนต์, แรงเบรก |
| **meganewton** | MN | 10⁶ N | จรวด, สะพาน |
| **giganewton** | GN | 10⁹ N | แผ่นเปลือกโลก |
| **teranewton** | TN | 10¹² N | ผลกระทบอุกกาบาต |
| **Planck force** | Fᴘ | c⁴/G ≈ 1.2×10⁴⁴ N | ขีดจำกัดสูงสุดทางฟิสิกส์ |

### หน่วยอื่นๆ
| หน่วย | ค่า (N) | ที่มา |
|-------|---------|------|
| **dyne** | 10⁻⁵ | CGS |
| **pond** | 9.80665 × 10⁻³ | แรงของ 1 g (เลิกใช้) |
| **pound-force (lbf)** | 4.4482216152605 | US customary |
| **kilogram-force (kgf)** | 9.80665 | 1 kg × g |
| **statnewton** | 10⁻⁵ | CGS esu |

---

## 🌍 แรงในชีวิตจริง

| สิ่งนี้ | แรง | หมายเหตุ |
|--------|-----|----------|
| 🍏 **แอปเปิลตก** | **≈ 1 N** | 0.1 kg × 9.81 m/s² |
| ✉️ **จดหมาย (แผ่น A4)** | **≈ 0.05 N** | 5 g |
| 💪 **ยกของ 5 kg** | **≈ 49 N** | 5 × 9.81 |
| 👣 **น้ำหนักคน 70 kg** | **≈ 690 N** | 70 × 9.81 |
| 🚗 **ลากรถเข็น** | **≈ 50–100 N** | ขึ้นกับน้ำหนัก |
| 🦷 **แรงกัด** | **≈ 700 N** | มนุษย์ |
| 🐊 **แรงกัดจระเข้** | **≈ 16,000 N** | สูงที่สุดในสัตว์ |
| 🚀 **Saturn V thrust** | **≈ 34 MN** | 34,000,000 N |
| 🌍 **โลกดึงเรา** | **≈ 690 N** | gravity |
| 🌞 **ดวงอาทิตย์ดึงโลก** | **≈ 3.5 × 10²² N** | แรงโน้มถ่วง |
| ⚡ **Electron–proton ใน H atom** | **≈ 8.2 × 10⁻⁸ N** | EM force |

---

## 🔬 เครื่องมือวัดแรง (Timeline)

| อุปกรณ์ | ปี | หลักการ |
|----------|-----|---------|
| ⚖️ **Equal-arm balance** | ~3000 BCE | มวลเทียบกับมวลอ้างอิง = แรงสมดุล |
| 🔩 **Spring balance** | 1660 (Hooke) | F = kx — ขยายสปริง ∝ แรง |
| 🔄 **Torsion balance** | 1785 (Coulomb) | แรงบิดบนเส้นลวด → วัดแรงไฟฟ้าอ่อนๆ |
| 📏 **Load cell (strain gauge)** | 1950s | ความต้านทานเปลี่ยนเมื่อยืด/หด |
| 🔬 **AFM cantilever** | 1986 | deflection ของ cantilever → แรงระหว่าง tip กับ surface → nN |
| 🔵 **Optical tweezer** | 1986 (Ashkin) | laser trap วัตถุระดับ μm → วัดแรง pN |
| ⚡ **Electrostatic force balance** | 1990s | แรงไฟฟ้าสมดุลกับ mg → calibrate |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "No motion = No force" | **ไม่** — วัตถุนิ่ง = resultant force = 0 — แต่แรงย่อยๆ (gravity, normal) ยังมีอยู่ |
| "Force = energy" | **ไม่** — Force มีหน่วย N, Energy มีหน่วย J = N·m — แรงกระทำเป็นระยะทาง = work → energy |
| "g-force = แรง" | g-force = **ความเร่ง** (multiples of g) — 1g = 9.81 m/s² — แรงที่รู้สึก = m × g-force |
| "น้ำหนัก = มวล" | **ไม่** — มวล (kg) ≠ น้ำหนัก (N) = mg — แต่มักใช้ปนในชีวิตประจำวัน |
| "Centrifugal force = จริง" | **Centrifugal = fictitious force** — รู้สึกในกรอบหมุน (rotating frame) — จริงๆ = inertia อยากออกนอก ในกรอบนิ่งมีแค่ centripetal |
| "แรงที่พื้นรองเท้าขณะเดิน > น้ำหนัก" | **ถูก** — ตอนเดิน/วิ่ง → normal force ช่วงส้น → > mg — วัดด้วย force plate |

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. แรงทั้ง 4 จะรวมเป็น 1 ทฤษฎีได้ไหม? — Theory of Everything**
| รวมแล้ว | เมื่อไหร่ | ผู้ทำให้ |
|---------|----------|---------|
| EM + Weak → **Electroweak** | 1979 (Nobel) | Glashow, Weinberg, Salam |
| + Strong → **GUT** (Grand Unified Theory) | ยังไม่เสร็จ | รอ proton decay |
| + Gravity → **Theory of Everything** (ToE) | ยังไม่เสร็จ | String theory, Loop quantum gravity... |

**2. Casimir effect — "แรงจากสุญญากาศ"**
ระหว่างแผ่นโลหะ 2 แผ่นใน vacuum (ห่าง ~μm):
- อนุภาค virtual photon ระหว่างแผ่น = modes น้อยกว่า → ความดันต่ำกว่า
- ภายนอกมีทุก mode → ความดันสูงกว่า → **แผ่นถูกกดเข้าหากัน**
- **นี่คือ macroscopic evidence ของ quantum vacuum fluctuations!**

**3. Fictitious forces — ทำไมถึงรู้สึก?**
ในกรอบอ้างอิงที่ **accelerate** (ไม่ใช่ inertial):
- **Centrifugal:** รู้สึก "ออกนอก" ในรถเลี้ยว
- **Coriolis:** รู้สึกเบน (ลม, ballistic missile)
- **Euler:** รู้สึกตอนความเร่งเชิงมุมเปลี่ยน (หมุนเร็วขึ้น)
— เหล่านี้เป็น "แรงเทียม" ที่เกิดจากการเลือกกรอบอ้างอิงที่เร่ง — ถ้าเปลี่ยนเป็น inertial frame → หายไป

**4. แรงที่มากที่สุดในจักรวาล**
Planck force: Fᴘ = c⁴/G ≈ 1.2 × 10⁴⁴ N
— แรงที่ photon มี energy = 1 Planck energy (1.2 × 10¹⁹ GeV) ผ่าน Schwarzschild radius
— ถ้าเกิน Fᴘ → เกิด microscopic black hole (ใน quantum gravity)

---

## 🔗 อ้างอิง

- Archimedes (~260 BCE). *On the Equilibrium of Planes*
- Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*
- Hooke, R. (1678). *Lectures de Potentia Restitutiva*
- Coulomb, C. A. (1785). *Premier Mémoire sur l'Électricité et le Magnétisme*
- Maxwell, J. C. (1873). *A Treatise on Electricity and Magnetism*
- Einstein, A. (1915). General Theory of Relativity
- Yukawa, H. (1935). "On the Interaction of Elementary Particles"
- Casimir, H. B. G. (1948). "On the attraction between two perfectly conducting plates"