---
title: Electric Potential and Voltage
field: Electricity & Magnetism
type: physical-quantity
si_unit: volt (V)
symbol: V (potential difference / voltage), φ (electric potential)
dimension: [M·L²·T⁻³·I⁻¹] = [J/C]
version: 1
tags: [electricity, voltage, potential, si-units, history]
related_lectures: []
related_terminology: []
related_physical_quantity: [charge, current, energy, resistance, capacitance]
---

# ⚡ Voltage (Electric Potential)

## 📜 ประวัติศาสตร์ของแรงดันไฟฟ้า

### ก่อนจะมีคำว่า "Volt" — แนวคิดของแรงดัน

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **~1752** | Benjamin Franklin | เสนอแนวคิด "electrical fluid" — สสารไฟฟ้าไหลจากที่มากไปน้อย → เริ่มแนวคิดของ "ระดับ" ของไฟฟ้า |
| **1780s** | Alessandro Volta | ศึกษา **tension** (ความตึง) — ยิ่งแผ่นโลหะต่างชนิดกันมาก → แรงระหว่างแผ่นยิ่งมาก |
| **1800** | **Alessandro Volta** | **Voltaic Pile** — แผ่น Zn + Cu + เกลือ → แหล่งจ่ายแรงดันคงที่เป็นครั้งแรก → ตั้งชื่อภายหลังเป็น **Volt** |
| **1821** | **Georg Ohm** | ค้นพบความสัมพันธ์ระหว่างแรงดัน กระแส และความต้านทาน (แต่ถูกปฏิเสธในตอนแรก!) |

### กำเนิดแนวคิด "Potential" — Faraday, Maxwell

| ปี | นักวิทยาศาสตร์ | การค้นพบ |
|----|---------------|-----------|
| **1832** | Michael Faraday | พบว่าการเปลี่ยนแปลงสนามแม่เหล็ก → เกิดแรงดัน (induced EMF) → กฎการเหนี่ยวนำ |
| **1845** | Gustav Kirchhoff | **กฎของเคิร์ชฮอฟฟ์** — KVL: ผลรวมแรงดันใน loop = 0 — ปูทางแนวคิดศักย์ไฟฟ้า |
| **1861–73** | James Clerk Maxwell | รวมแนวคิดของ **scalar potential (φ)** และ **vector potential (A)** — E = −∇φ − ∂A/∂t |
| **1881** | **International Electrical Congress** (Paris) | ตั้งชื่อหน่วย **volt (V)** ตาม Alessandro Volta |

### ยุคควอนตัม

| ปี | การค้นพบ |
|----|----------|
| **1911** | Kamerlingh Onnes — แรงดันตก = 0 ใน superconducting state |
| **1956** | Brian Josephson ทำนาย **Josephson Effect** — supercurrent ระหว่าง superconductors 2 ตัว → เชื่อม V ↔ frequency |
| **1962** | Josephson effect confirmed → ใช้เป็น standard ของแรงดัน: K_J = 2e/h = 483.5979... GHz/V |
| **1980** | Klaus von Klitzing — Quantum Hall Effect → R_K = h/e² เป็น quantum resistance standard |
| **1990** | **Josephson Voltage Standard (JVS)** — ใช้งานจริงทั่วโลก |
| **2019** | SI Redefinition: e fixed, K_J = 2e/h fixed → แรงดันนิยามจาก frequency ล้วน |

---

## ⚛️ คำนิยามของ 1 โวลต์

### Derived Unit (ก่อน 2019)
> "1 volt = **the potential difference across a conductor when a current of 1 ampere dissipates 1 watt of power**"
>
> หรือ **1 V = 1 W/A = 1 J/C**

```
1 V = 1 kg·m²·s⁻³·A⁻¹

โดย: V = W/Q (energy per charge)
    W = F·d (work)
    F = m·a (force)
```

### Post-2019 — Quantum Definition

ตอนนี้แรงดันถูก **วัดเทียบกับ Josephson constant** โดยตรง:

```
K_J = 2e/h = 483.597848416... GHz/V (fixed)

เมื่อ V = f/K_J
   f = microwave frequency (จาก atomic clock)
   K_J = fixed constant
```

> **🎯 นั่นหมายความ:** 1 โวลต์วันนี้ = ความถี่ 483.597848416 GHz ที่ตกคร่อม Josephson junction array → **แรงดัน = frequency measurement**!

### Josephson Voltage Standard (JVS)

| ชิ้นส่วน | รายละเอียด |
|-----------|-------------|
| **Nb/NbOₓ/Pb junction** | Superconductor-insulator-superconductor (SIS) |
| **Microwave irradiation (70–90 GHz)** | จาก Gunn diode หรือ synthesizer |
| **1 junction → ~0.15 mV** | ต้องต่อ ~20,000  junctions แบบอนุกรมเพื่อให้ได้ 1 V |
| **NIST 10V array** | แรงดัน 10 V ด้วยความแม่นยำ ~10⁻¹⁰ |
| **Programmable JVS (PJVS)** | เปลี่ยนแรงดันแบบ digital → output ค่าใดก็ได้ |

---

## 🔬 เครื่องมือวัดแรงดัน (Timeline)

| อุปกรณ์ | ปี | หลักการ | ช่วงวัด |
|----------|-----|---------|---------|
| 🧲 **Galvanometer** (indirect) | 1820s | แรงดัน ∝ กระแสผ่าน R ที่รู้ค่า → ใช้ I × R | mV – V |
| 📏 **Voltmeter (moving-coil)** | 1880s | ขดลวดหมุนในสนามแม่เหล็ก + ตัวต้านทานอนุกรม (multiplier) | mV – several kV |
| ⚡ **Electrostatic voltmeter** | ~1900 | ประจุบนแผ่นโลหะ → แรงดูด → การกระจัด | kV – MV |
| 💻 **Digital Multimeter (DMM)** | 1970s | ADC + voltage divider | μV – 1 kV |
| 🔬 **Nanovoltmeter** | ปัจจุบัน | Lock-in amplifier / chopper-stabilized | nV – mV |
| ⚛️ **Josephson Voltage Standard (JVS)** | 1990s | f = K_J·V — เชื่อม V กับ frequency standard | ~0.1 nV – 10 V |
| ✅ **Kelvin–Varley voltage divider** | ยุคแรก→ปัจจุบัน | ตัวต้านทาน precision ladder → วัด unknown V จาก known V | μV – 1 kV |

---

## 📐 หน่วยของแรงดันไฟฟ้า

### SI Unit
| หน่วย | สัญลักษณ์ | คำนิยาม |
|-------|-----------|---------|
| **volt** | V | 1 V = 1 W/A = 1 J/C |
| **Equivalent** | — | 1 V = 1 kg·m²·s⁻³·A⁻¹ |

### SI Prefixes

| หน่วย | สัญลักษณ์ | ค่า | ใช้ที่ไหน |
|-------|-----------|-----|----------|
| **nanovolt** | nV | 10⁻⁹ V | Josephson voltage standard level |
| **microvolt** | μV | 10⁻⁶ V | EEG, ECG, thermocouple |
| **millivolt** | mV | 10⁻³ V | เซนเซอร์, battery cell (~1.2–3.7 V) |
| **volt** | V | 1 | อิเล็กทรอนิกส์ |
| **kilovolt** | kV | 10³ V | สายส่งไฟฟ้า, X-ray tube |
| **megavolt** | MV | 10⁶ V | Van de Graaff generator, lightning (~100 MV) |
| **gigavolt** | GV | 10⁹ V | ฟิสิกส์พลาสมา (Z-pinch) |
| **teravolt** | TV | 10¹² V | Pulsar magnetosphere (ไม่ใช่ในแล็บ) |

### หน่วยอื่นๆ ที่เคยใช้ / หาได้ยาก

| หน่วย | ค่า | ที่มา |
|-------|-----|------|
| **statvolt** | ≈ 299.792458 V | CGS esu |
| **abvolt** | 10⁻⁸ V | CGS emu |
| **Planck voltage (Vᴘ)** | ≈ 1.043 × 10²⁷ V | quantum gravity scale |

---

## 🌍 การใช้งานในชีวิตจริง

| การใช้งาน | ระดับแรงดัน |
|-----------|-------------|
| 🔋 **แบตเตอรี่โทรศัพท์** | 3.7–4.4 V (Li-ion) |
| 🔌 **ปลั๊กไฟบ้าน (ไทย)** | 220 V RMS (≈ 311 V peak) |
| 🏭 **สายส่งไฟฟ้าแรงสูง** | 115–500 kV |
| ⛈️ **ฟ้าผ่า** | ~100 MV peak |
| 🧠 **ศักย์ไฟฟ้าในเซลล์ประสาท** | −70 mV (resting) → +40 mV (action potential) |
| 🖥️ **CPU core voltage** | ~0.6–1.5 V |
| 🔬 **SEM / TEM** | 1–300 kV |
| ⚛️ **Van de Graaff** | 1–25 MV (terminal) |
| 🌌 **Pulsar magnetosphere** | ~10¹² V (teravolt) |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "โวลต์ = กระแส" | **ไม่ใช่** — โวลต์คือ **energe per charge** (J/C) กระแสคือ **charge per time** (C/s) — V = IR แสดงความสัมพันธ์ของสองคนนี้ |
| "แรงดันสูง = อันตรายเสมอ" | อันตรายขึ้นกับ **กระแส** ที่ผ่านร่างกาย (I = V/R) — ไฟฟ้าสถิต 10 kV อาจไม่เป็นอันตรายถ้า I ต่ำมาก (แต่ก็อาจทำให้ตกใจได้) |
| "1.5 V battery = 1.5 V ตลอดเวลา" | แรงดันลดลงเรื่อยๆ ตามการใช้งาน (discharge curve) — 1.5 V คือค่า nominal |
| "Ground (GND) = 0 V เสมอ" | GND เป็น reference point — 0 V สัมพันธ์กับจุดที่เลือก — ไม่ใช่ค่านิรันดร์ |
| "Volt drop ไม่มีใน superconductor" | **ถูกต้อง** — R=0 → V=0 ตาม Ohm's law |
| "ศักย์ไฟฟ้า = พลังงาน" | **ไม่เชิง** — ศักย์ไฟฟ้าคือ *energe per unit charge* (J/C) → พลังงานรวม = V·q |

### 🔥 คำถามขั้นสูง — สำหรับนักเรียนที่อยากรู้จริง

**1. Josephson junction ทำงานอย่างไร? (โดยสังเขป)**
Superconductor-insulator-superconductor structure → Cooper pairs (คู่อิเล็กตรอน) tunnel ผ่าน barrier → เมื่อฉาย microwave f → current-voltage characteristic มี step ที่ V = n·hf/2e → ขั้น step ห่างกัน = hf/2e → **ถ้าวัด f ได้แม่นยำ V ก็ได้ความแม่นยำตามไปด้วย**

**2. ทำไมต้องใช้ 2e?**
เพราะ carrier ใน superconductor คือ **Cooper pair** (อิเล็กตรอน 2 ตัวจับคู่กัน) → charge = **2e** → ดังนั้น Josephson constant = 2e/h (ไม่ใช่ e/h)

**3. Quantum Hall effect เกี่ยวข้องกับ voltage standard ยังไง?**
ใช้กำหนด **R_K = h/e²** (von Klitzing constant) → เมื่อรวมกับ Josephson effect (K_J = 2e/h) → **สามารถวัด watt (= V²/R) ได้โดยตรงจาก quantum standards** → สร้าง tracing chain จาก SI units ทั้งหมดกลับไปที่ e, h, และ c

**4. "EMF" vs "Potential Difference" ต่างกันไหม?**
**EMF (Electromotive Force):** แรงดันที่แหล่งจ่าย *สร้างขึ้น* (เช่น battery 1.5 V)
**Potential Difference (PD):** แรงดันที่ *ตกคร่อม* load ตอนมีกระแส (เช่น ไฟ LED มี PD ≈ 2 V)

ต่างกันตรง **internal resistance**: EMF = PD + I·r (r = internal resistance)

**5. สนามไฟฟ้า E กับศักย์ V ต่างกันยังไง?**
```
E = −∇V (ใน 3D)
V(B) − V(A) = −∫ₐᵝ E · dl (1D: V = E·d ถ้า E uniform)
```
สรุป: **E = gradient (ความชัน) ของ V** — เหมือนความสูงของภูเขา (V) กับความชันของทางลาด (E)

## 🔗 อ้างอิง

- BIPM (2019). *The International System of Units (SI) — 9th edition*
- CGPM Resolutions: 9th CGPM (1948), 26th CGPM (2018)
- Josephson, B. D. (1962). "Possible new effects in superconductive tunnelling" — *Physics Letters*
- von Klitzing, K. (1980). "New Method for High-Accuracy Determination of the Fine-Structure Constant"
- Ohm, G. S. (1827). *Die galvanische Kette, mathematisch bearbeitet*
- Volta, A. (1800). "On the Electricity Excited by the Mere Contact of Conducting Substances of Different Kinds" — *Philosophical Transactions*
- Hamilton, C. A. (2000). "Josephson voltage standards" — *Review of Scientific Instruments*