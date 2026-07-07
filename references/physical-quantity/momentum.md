---
title: Momentum
field: Mechanics — Dynamics
type: physical-quantity
si_unit: kilogram-metre per second (kg·m/s)
symbol: p
dimension: [M·L·T⁻¹]
version: 1
tags: [momentum, dynamics, collision, conservation, si-units]
related_lectures: [topic15_forces]
related_terminology: [momentum, impulse, newtons_second_law, newtons_third_law]
related_physical_quantity: [velocity, mass, force, energy, impulse]
---

# 💥 Momentum

> **Momentum = "ปริมาณการเคลื่อนที่"** — vector
>
> **p = mv** — หน่วย kg·m/s

---

## 📜 ประวัติศาสตร์ — แนวคิด "ปริมาณการเคลื่อนที่"

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~530 BCE** | **Pythagoreans** | เชื่อว่าทุกสิ่งเคลื่อนที่มี "force" ภายใน — ยังไม่ใช่ momentum |
| **~350 BCE** | **Aristotle** | พลังงานการเคลื่อนที่ต้องมี "mover" ตลอดเวลา — เมื่อหยุดออกแรง → หยุดทันที |
| **~550 CE** | John Philoponus | เสนอ **impetus** — สิ่งที่ถูกผลักจะเคลื่นที่ต่อไปโดยไม่ต้องมีแรงกระทำต่อเนื่อง → ใกล้แนวคิด momentum/inertia |
| **~1638** | **René Descartes** | *Principia Philosophiae* — กำหนด **"quantity of motion" (mv)** อย่างชัดเจนครั้งแรก |
| | | — เชื่อว่า conserve ตลอดจักรวาล (แต่ผิดที่คิดว่าเป็น scalar) |
| **~1668** | **John Wallis, Christopher Wren, Christiaan Huygens** | ศึกษา **การชน (collision)** อย่างเป็นระบบ |
| | | — Wren: pendulum collision วัดก่อน-หลัง → momentum conserved |
| | | — Huygens: **mv² อนุรักษ์ด้วย** (→ kinetic energy!) |
| **1687** | **Isaac Newton** | *Principia* — **Lex II: F = dp/dt** (form ดั้งเดิม!) |
| | | — Lex III: momentum เปลี่ยนไป = แรงกระทำ × เวลา |
| **1750** | **Leonhard Euler** | ทำให้ F = dp/dt เป็น standard form ที่ใช้ทุกวันนี้ |
| **~1900** | **Einstein** | SR: p = γmv (γ → ∞ เมื่อ v→c) → momentum ไม่จำกัดแม้ v เข้าใกล้ c |
| **2019** | **SI Redefinition** | p = kg·m/s — kg นิยามจาก h, m นิยามจาก c, s นิยามจาก ΔνCs → momentum traceable ถึง constants of nature |

---

## ⚛️ นิยามทางฟิสิกส์

### Classical Momentum
```
p = mv (vector)

magnitude: |p| = mv
ทิศทาง: ทิศเดียวกับ velocity
```

### Relativistic Momentum
```
p = γmv = mv / √(1 − v²/c²)

เมื่อ v → 0: p ≈ mv (classical)
เมื่อ v → c: p → ∞ (ต้องใช้แรงอนันต์)
```

### Newton's Second Law (form ดั้งเดิม)
```
F = dp/dt (vector)

เมื่อ m คงที่:
F = m·dv/dt = ma

เมื่อ m เปลี่ยน (จรวด, relativity):
F = m·dv/dt + v·dm/dt
```

### Conservation of Momentum
```
ในระบบปิด (ไม่มีแรงภายนอก):
P_total = Σp_i = constant

ก่อนชน = หลังชน:
m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂
```

### Impulse–Momentum Theorem
```
J = F·Δt = Δp = mv − mu

แรงกระทำในช่วงเวลาสั้น → เปลี่ยน momentum
— ถุงลมนิรภัย: ↑ Δt → ↓ F (Δp คงที่)
— รถเหล็ก vs รถบุบ: ↑ Δt → ↓ แรงกระแทก
```

---

## 🔬 การชน (Collisions)

### 3 ประเภทหลัก

| ประเภท | Energy อนุรักษ์ | รายละเอียด |
|--------|---------------|-------------|
| **Elastic (ยืดหยุ่น)** | ✅ KE คงที่ | วัตถุเด้งออกจากกัน, momentum + KE conserved |
| **Inelastic (ไม่ยืดหยุ่น)** | ❌ KE Loss | วัตถุติดกัน → KE บางส่วนกลายเป็นความร้อน/เสียง |
| **Partially elastic** | ❌ KE บางส่วน | เด้งแต่เสีย energy — ใช้ coefficient of restitution (e) |

### 1D Elastic Collision (สูตร)
```
v₁ = (m₁ − m₂)/(m₁ + m₂) · u₁ + (2m₂)/(m₁ + m₂) · u₂
v₂ = (2m₁)/(m₁ + m₂) · u₁ + (m₂ − m₁)/(m₁ + m₂) · u₂
```

| กรณีพิเศษ | ผล |
|-----------|-----|
| m₁ = m₂ | แลก velocity กัน |
| m₂ ≫ m₁, u₂ = 0 | v₁ ≈ −u₁ (เด้งกลับ), v₂ ≈ 0 |
| m₁ ≫ m₂, u₂ = 0 | v₁ ≈ u₁ (แทบไม่เปลี่ยน), v₂ ≈ 2u₁ |

### Coefficient of Restitution (e)
```
e = (v₂ − v₁) / (u₁ − u₂)

e = 1 → elastic (เด้ง perfect)
e = 0 → inelastic (ติดกัน)
0 < e < 1 → partially elastic
```

---

## 🌍 ตัวอย่างในชีวิตจริง

| สิ่งนี้ | Momentum (kg·m/s) | หมายเหตุ |
|---------|-------------------|----------|
| 🐜 **มดวิ่ง** | ≈ 10⁻⁵ | มด 10 mg, วิ่ง 1 m/s |
| 🏃 **คนวิ่ง** | ≈ 500 | 70 kg × 7 m/s |
| 🚗 **รถยนต์ที่ 100 km/h** | ≈ 18,000 | 1,000 kg × 18 m/s |
| 🚢 **เรือบรรทุกน้ำมัน** | ≈ 2×10⁸ | 200,000 ton × 1 m/s |
| 🌍 **โลกโคจร** | ≈ 1.8×10²⁹ | M🜨 × v_orbital |
| ⚛️ **อิเล็กตรอนใน LHC** | ≈ 10⁻¹⁹ | γmₑv ≈ mₑv · 7,000 |

### Impulse ตัวอย่าง
| เหตุการณ์ | แรงเฉลี่ย | เวลา | Δp |
|-----------|----------|------|-----|
| ต่อยเป้า (มวย) | 2,500 N | 0.02 s | 50 kg·m/s |
| รถชนกำแพง (60 km/h) | 100,000 N | 0.05 s | 5,000 kg·m/s |
| นักฟุตบอลยิงประตู | 2,000 N | 0.01 s | 20 kg·m/s |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "Momentum = force" | ไม่ — Momentum = mv, Force = ma = dp/dt — สัมพันธ์แต่ไม่ใช่สิ่งเดียวกัน |
| "Momentum ไม่ conserved ในโลกจริง" | ยัง conserved — friction = external force → ระบบไม่ปิด — แต่ถ้ารวม friction ในระบบ → momentum ยัง conserved |
| "มวลมาก = momentum มากกว่า เสมอ" | ขึ้นกับ **velocity** — รถบรรทุกจอด = 0 momentum — ลูกปิงปอง 100 km/h = momentum น้อย |
| "Elastic collision = ไม่มีเสียง/ความร้อน" | **ถูก** — พลังงานกลคงที่ — แต่ในโลกจริงมี loss เสมอ (ใกล้ elastic ที่ atomic scale) |
| "โมเมนตัมสัมพัทธภาพ = γmv ≈ mv" | ที่ everyday speed (v ≪ c) → γ≈1 → ถูก แต่ที่ v→c → γ→∞ → momentum → ∞ |

---

## 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. ทำไมถึงมี 2 ปริมาณอนุรักษ์ (momentum + energy)?**
**Noether's Theorem (Emmy Noether, 1918):**
- Momentum conserved ↔ homogeneity of space (สมมาตรการเลื่อนที่)
- Energy conserved ↔ homogeneity of time (สมมาตรการเลื่อนเวลา)
- Angular momentum conserved ↔ isotropy of space (สมมาตรการหมุน)
→ Conservation laws = symmetry ของ spacetime!

**2. Momentum ใน quantum mechanics — operator**
ใน QM: momentum **เป็น operator** แทนที่จะเป็นตัวเลข:
```
p̂ = −iℏ · ∂/∂x (ใน 1D เวกเตอร์)
p̂ = −iℏ · ∇ (ใน 3D)
```
นี่คือแกนหลักของ Schrödinger equation: iℏ ∂ψ/∂t = −(ℏ²/2m) ∇²ψ + Vψ

**3. Relativistic momentum — ใช้ rocket equation**
```
Tsiolkovsky rocket equation:
Δv = v_ex · ln(m₀/m_f)
```
— จรวดเร่งโดยการดีดมวลออก (dm/dt) → momentum ของจรวด + ควันไอเสีย = conserved
— ที่ v → c → ต้องใช้ relativistic momentum + relativistic rocket equation (ซับซ้อนกว่า)
— นี่คือเหตุผลที่ต้องใช้จรวด multistage!

**4. Photon momentum — "ไม่มีมวลแต่มีโมเมนตัม"**
```
p = E/c = hf/c = h/λ
```
— โฟตอนไม่มี m₀ = 0 แต่มี momentum (เพราะมี energy + velocity = c)
— นี่คือหลักการของ **solar sail** (ใบเรือพลังงานแสงอาทิตย์)

**5. Angular momentum of Earth — เท่าไหร่?**
```
L = Iω = ⅖MR² × (2π/T)
  = ⅖ × 5.97×10²⁴ × (6.37×10⁶)² × 2π/86400
  ≈ 7.1 × 10³³ kg·m²/s
```
— นี่คือ momentum การหมุนของโลก — 1 วันค่อยๆ ยาวขึ้น ~1.7 ms/ศตวรรษ (tidal friction จากดวงจันทร์)

**6. จรวดน้ำ (น้ำเป็นมวลดีดทิ้ง) — conservation of momentum**
ขวดน้ำอัดลม + น้ำ → อัดอากาศ → ปล่อย → น้ำพุ่งลง → ขวดพุ่งขึ้น
— นี่คือ **action-reaction** และ **conservation of momentum** ที่เห็นชัดที่สุด!

---

## 🔗 อ้างอิง

- Descartes, R. (1644). *Principia Philosophiae*
- Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*
- Huygens, C. (1669). "Rules of Motion in the Collision of Bodies"
- Euler, L. (1750). "Decouverte d'un nouveau principe de Mécanique"
- Planck, M. (1906). Das Prinzip der Relativität — Relativistic momentum
- Tsiolkovsky (1903). *The Exploration of Cosmic Space by Means of Reaction Devices*
- Noether, E. (1918). "Invariante Variationsprobleme" — *Göttinger Nachrichten*