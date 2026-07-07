---
title: Bohr's Atomic Model — The Quantum Atom
field: Physics — Atomic & Quantum
type: historical-milestone
year: 1913
scientist: Niels Bohr
related_lectures: [topic15_forces, topic17_energy]
related_terminology: []
tags: [bohr, atomic-model, quantum-mechanics, hydrogen, spectra, copenhagen, 20th-century]
version: 1.0.0
---

# ⚛️ Bohr's Atomic Model — The Quantum Atom

## 📜 Overview

In **1913**, the Danish physicist **Niels Bohr** (1885–1962) proposed a revolutionary model of the atom that solved the two critical problems of Rutherford's nuclear model:

1. **Why don't electrons spiral into the nucleus?** (Classical EM says they should — in ~10⁻¹¹ s!)
2. **Why do atoms emit only specific colours of light (line spectra)?**

Bohr's answer was radical: he **quantised** the electron orbits — only certain orbits were allowed, and electrons could "jump" between them, emitting photons of specific energies.

> *"If atomic structure is to be stable, the laws of classical electrodynamics must be modified."*
> — **Niels Bohr**, 1913

| Key fact | Detail |
|----------|--------|
| **Who** | Niels Henrik David Bohr (1885–1962) |
| **When** | July 1913 — three papers published in *Philosophical Magazine* |
| **Where** | University of Copenhagen (though he was with Rutherford at Manchester when developing the idea) |
| **What** | Quantised electron orbits; explained the **hydrogen spectrum** (Balmer series) |
| **Equation** | E_n = −13.6/n² eV (energy levels of hydrogen) |
| **Why it matters** | First application of **quantum theory** to atomic structure; foundation of modern quantum mechanics |
| **Nobel** | **1922 Nobel Prize in Physics**— "for his services in the investigation of the structure of atoms and of the radiation emanating from them" |

---

## 📅 Timeline of Understanding

| Era | Figure / Work | Contribution |
|-----|---------------|-------------|
| ~400 BCE | **Democritus** | Atomism — atoms are indivisible |
| 1803 | **John Dalton** | Modern atomic theory — solid sphere model |
| **1897** | **J.J. Thomson** | **Discovered the electron** → plum pudding model |
| **1911** | **Rutherford** | **Gold foil experiment** → nuclear model (tiny + nucleus) |
| — | — | **But:** classical physics predicts atoms should collapse in ~10⁻¹¹ s! |
| 1885 | **Johann Jakob Balmer** | Empirical formula for hydrogen spectral lines: λ = B·n²/(n² − 4) |
| 1888 | **Johannes Rydberg** | Generalised Balmer's formula: 1/λ = R(1/n² − 1/m²) |
| **1900** | **Max Planck** | **Quantum hypothesis**: E = hf — energy is quantised! |
| 1905 | **Einstein** | **Photoelectric effect**: light consists of **photons** (E = hf) |
| **1913** | **Niels Bohr** 🏆 | **Bohr model**: quantised orbits + quantum jumps → explains hydrogen spectrum! |
| 1914 | **James Franck & Gustav Hertz** | **Franck–Hertz experiment** — confirmed discrete atomic energy levels |
| 1916 | **Arnold Sommerfeld** | Extended Bohr's model with **elliptical orbits** and **fine structure** |
| 1922 | Bohr | **Nobel Prize in Physics** |
| **1925** | **Werner Heisenberg** | **Matrix mechanics** — first complete formulation of quantum mechanics |
| **1926** | **Erwin Schrödinger** | **Wave equation** — electron cloud / orbitals; replaced Bohr's planetary orbits |
| 1927 | **Heisenberg** | **Uncertainty Principle** — you can't know both position and momentum precisely → Bohr's orbits (both known!) are impossible |
| **1927** | **Bohr & Heisenberg** | **Copenhagen interpretation** of quantum mechanics |

---

## 👤 Biography — Niels Bohr (1885–1962)

| Detail | Info |
|--------|------|
| **Born** | 7 October 1885, Copenhagen, Denmark |
| **Died** | 18 November 1962, Copenhagen (age 77) |
| **Education** | University of Copenhagen (Master's 1909, PhD 1911) |
| **Postdoc** | **Cambridge** under J.J. Thomson (1911) → **Manchester** under **Rutherford** (1912) — where the atomic model was born! |
| **Position** | Professor of Theoretical Physics, University of Copenhagen (1913–1962); founded the **Institute for Theoretical Physics** (now the Niels Bohr Institute) in 1921 |
| **Nobel** | **1922 Nobel Prize in Physics** |
| **Family** | Son **Aage Bohr** also won Nobel Prize in Physics (1975, nuclear structure) |
| **Key students/collaborators** | **Heisenberg, Schrödinger, Dirac, Pauli, Gamow, Wheeler** — virtually every major quantum physicist of the 1920s–30s worked with or debated Bohr |
| **Copenhagen Interpretation** | The standard interpretation of quantum mechanics: particles don't have definite properties until measured; probability waves "collapse" upon observation |
| **WWII** | Escaped from Nazi-occupied Denmark in 1943 (via fishing boat to Sweden, then to England/USA) — involved with the **Manhattan Project** (as a consultant, advocating for international control of nuclear weapons) |
| **Personality** | Known for his **mumbling** (hard to understand), his **gentle nature**, and his habit of thinking aloud — working out ideas by talking through them with students. His favourite phrase: "I am not a physicist; I am a **philosopher about physics**" |
| **Legacy** | The **Bohr model** was superseded, but the **principles he established** (quantised states, quantum jumps, complementarity, correspondence principle) are **foundational** to all modern physics |

---

## 🔬 The Model — Core Content

### Bohr's Three Postulates

| Postulate | Statement | Significance |
|-----------|-----------|-------------|
| **1: Stationary States** | Electrons can only exist in certain **stable orbits** (stationary states) without radiating energy | **Why atoms don't collapse** — electrons in these orbits do NOT obey Maxwell's equations |
| **2: Angular Momentum Quantisation** | Only orbits where angular momentum = nℏ are allowed: mvr = nℏ, where n = 1, 2, 3, ... | **Why only specific orbits** — quantisation condition; n = **principal quantum number** |
| **3: Quantum Jumps** | Electrons "jump" between orbits by absorbing or emitting a **photon** of energy ΔE = hf | **Why line spectra** — each jump produces light of a specific colour; explains Balmer, Lyman, Paschen series |

---

### 🧮 The Mathematics of the Bohr Model

#### Quantised Orbits

From postulate 2 (angular momentum quantisation):
```
mvr = nℏ = n·h/2π
```

Coulomb force provides centripetal acceleration:
```
F = k·e²/r² = mv²/r   →   v² = k·e²/(mr)
```

Combining:
```
v = nℏ/(mr)   →   (nℏ/(mr))² = k·e²/(mr)
```

**Radius of the n-th orbit:**
```
r_n = n²·ℏ²/(mk·e²) = n²·a₀

where a₀ = Bohr radius = 0.529 × 10⁻¹⁰ m (≈ 0.53 Å)
```

| n | r_n (× a₀) | r_n (m) | State |
|---|-----------|---------|-------|
| 1 | 1 | 5.29 × 10⁻¹¹ | Ground state |
| 2 | 4 | 2.12 × 10⁻¹⁰ | First excited |
| 3 | 9 | 4.76 × 10⁻¹⁰ | Second excited |
| 4 | 16 | 8.47 × 10⁻¹⁰ | — |

#### Electron Velocity in Orbit

```
v_n = (k·e²)/(nℏ) = (c·α)/n

where α = fine-structure constant ≈ 1/137

For n = 1:
v₁ = (k·e²)/ℏ ≈ 2.19 × 10⁶ m/s ≈ c/137
```

| n | v_n (m/s) | % of c |
|---|-----------|--------|
| 1 | 2.19 × 10⁶ | **0.73%** |
| 2 | 1.09 × 10⁶ | 0.37% |
| 3 | 7.3 × 10⁵ | 0.24% |

#### Energy Levels

Total energy = Kinetic + Potential:
```
E_n = KE + PE = ½mv² − k·e²/r

E_n = −k·e²/(2r_n) = −(mk²·e⁴)/(2ℏ²) · 1/n²

E_n = −13.6 eV / n²
```

| n | E_n (eV) | E_n (J) | State |
|---|----------|---------|-------|
| ∞ | 0 | 0 | **Ionised** (free electron) |
| 4 | −0.85 | −1.36 × 10⁻¹⁹ | — |
| 3 | **−1.51** | −2.42 × 10⁻¹⁹ | Second excited |
| 2 | **−3.40** | −5.44 × 10⁻¹⁹ | First excited |
| **1** | **−13.6** | −2.18 × 10⁻¹⁸ | **Ground state** |

> 💡 **Ionisation energy of hydrogen = 13.6 eV** — exactly the energy needed to remove the electron from the ground state!

---

### 🔥 Spectrum of Hydrogen — Explaining the Balmer Series

When an electron jumps from a higher orbit (m) to a lower orbit (n):

```
ΔE = E_m − E_n = 13.6(1/n² − 1/m²) eV

The photon frequency: f = ΔE/h
The photon wavelength: 1/λ = ΔE/(hc) = R(1/n² − 1/m²)

where R = Rydberg constant ≈ 1.097 × 10⁷ m⁻¹
```

**Spectral Series of Hydrogen:**

```
                Energy
n=∞ ───────── 0 eV         ← Ionisation
n=5 ─────── −0.54 eV
n=4 ─────── −0.85 eV
n=3 ─────── −1.51 eV       ────────
n=2 ─────── −3.40 eV       ←────── Balmer series (visible)
                ↘│↙
              ────┼────
n=1 ─────── −13.6 eV       ←── Lyman series (UV)
```

| Series | n_final | n_initial | Region | First line |
|--------|---------|-----------|--------|-----------|
| **Lyman** | 1 | 2, 3, 4, ... | **Ultraviolet** (UV) | 121.6 nm |
| **Balmer** | 2 | 3, 4, 5, ... | **Visible** | 656.3 nm (Hα, red) |
| **Paschen** | 3 | 4, 5, 6, ... | **Infrared** (IR) | 1,875 nm |
| **Brackett** | 4 | 5, 6, 7, ... | Far IR | 4,052 nm |
| **Pfund** | 5 | 6, 7, 8, ... | Far IR | 7,456 nm |

**The Balmer series (visible spectrum of hydrogen):**

| Line | Transition | Wavelength (nm) | Colour |
|------|-----------|-----------------|--------|
| Hα | 3 → 2 | 656.3 | **Red** |
| Hβ | 4 → 2 | 486.1 | **Blue-green** |
| Hγ | 5 → 2 | 434.0 | **Violet** |
| Hδ | 6 → 2 | 410.2 | **Deep violet** |

> 🎯 **Bohr's triumph:** The Balmer series was known experimentally since 1885. Bohr's model **derived** the Rydberg constant from first principles: R = mk²e⁴/(4πcℏ³) — which perfectly matched the experimental value!

---

## 🔍 Detail — The Franck–Hertz Experiment (1914)

**Experimental confirmation of Bohr's quantised energy levels:**

| Step | Observation |
|------|-------------|
| 1 | Accelerate electrons through mercury vapour |
| 2 | Measure the current at the collector as voltage increases |
| 3 | At **4.9 V**, the current **drops sharply** |
| 4 | At **9.8 V** (= 2 × 4.9), another drop |
| 5 | At **14.7 V** (= 3 × 4.9), another drop |

| Conclusion | Detail |
|-----------|--------|
| Electrons can only lose energy in **discrete amounts** | The mercury atom can only absorb **4.9 eV** at a time — corresponding to a transition to the first excited state |
| **Bohr was right!** | Energy levels are quantised — they exist! |

> **James Franck and Gustav Hertz** received the **1925 Nobel Prize in Physics** for confirming Bohr's model. (Gustav Hertz was the nephew of **Heinrich Hertz**, who discovered radio waves.)

---

## 💡 Strengths & Limitations of the Bohr Model

### What It Got Right ✅

| Success | Detail |
|---------|--------|
| ✅ **Hydrogen spectrum** | Perfectly predicts the Lyman, Balmer, Paschen series |
| ✅ **Rydberg constant** | Calculated from fundamental constants (m, e, h, c, k) — matches experiment |
| ✅ **Ionisation energy** | 13.6 eV for hydrogen — matches experiment |
| ✅ **Quantised energy** | Introduced the idea of discrete energy levels in atoms |
| ✅ **Quantum jumps** | First model to explain **how** atoms emit and absorb light at specific wavelengths |
| ✅ **Bohr radius** | a₀ = 0.529 Å — correct order of magnitude for atomic size |

### What It Couldn't Explain ❌

| Failure | Detail |
|---------|--------|
| ❌ **Only hydrogen-like atoms** | Works for H, He⁺, Li²⁺ (single electron), but fails for multi-electron atoms |
| ❌ **Fine structure** | Spectral lines split in magnetic fields (Zeeman effect) — Bohr model couldn't explain this; Sommerfeld added elliptical orbits |
| ❌ **Intensity of spectral lines** | Why are some spectral lines brighter than others? Bohr said nothing about transition probabilities |
| ❌ **Chemical bonding** | The model couldn't explain why atoms form molecules |
| ❌ **Electron "orbits"** | Heisenberg (1927): you **cannot** know both position and momentum precisely enough to define an orbit → the whole concept of "planetary orbits" for electrons is wrong |

> **Final verdict:** The Bohr model was **a brilliant stepping stone** — it introduced quantisation into atomic physics and gave the right answers for hydrogen. But it was a **hybrid** (part classical, part quantum) and was **superseded** by full quantum mechanics (Schrödinger/Heisenberg, 1925–26).

---

## 💡 Myth vs Fact

| Myth | Fact |
|------|------|
| Bohr **invented** quantum theory | **Planck** (1900, E = hf) and **Einstein** (1905, photons) got there first. Bohr **applied** quantum theory to the atom |
| The Bohr model shows **how electrons really move** | **No** — electrons don't orbit like planets. The Bohr model is a useful **analogy** but is **physically wrong** for describing electron motion |
| Bohr's model was **immediately accepted** | Some physicists rejected it ("ad-hoc" quantisation). The Franck–Hertz experiment (1914) was critical for winning acceptance |
| Bohr **did all the mathematics** | Bohr was **not a strong mathematician** — he relied on physical intuition and rough calculations. The detailed mathematics was refined by **Sommerfeld** and others |
| The Bohr model is **still taught as correct** | It's taught as a **historical stepping stone** and as an introduction to quantum concepts — but every exam syllabus then says "replaced by the quantum mechanical model" |
| Bohr **discovered** the electron cloud model | **Schrödinger** (1926) developed the wave equation that replaced orbits with probability clouds |
| Hydrogen has **exactly** 13.6 eV ground state | **Yes** for the simple Bohr model. Quantum electrodynamics (QED) adds **tiny corrections** (Lamb shift ≈ 4.4 × 10⁻⁶ eV) that Bohr's model didn't predict |
| Bohr and Einstein **always agreed** | They had a **legendary 30-year debate** over quantum mechanics. Einstein said "God does not play dice" — Bohr replied "Einstein, stop telling God what to do!" |

---

## 🎯 Classroom Demonstration

### Building the Bohr Model — Physical Analogy
> A **spiral staircase** vs a **step ladder**:
> - Classical physics predicted electrons could be at **any** energy (like a ramp)
> - Bohr said electrons can only be at **specific** energy levels (like steps on a ladder)
> - Electrons "jump" between steps — no intermediate positions allowed!

### The Hydrogen Spectrum
> Use a **diffraction grating** or **spectroscope** to observe emission spectra:
> - **Hydrogen tube** → see the distinct Balmer lines (red, blue-green, violet)
> - Compare to **mercury, helium, neon** — each element has a **unique "fingerprint"** spectrum

### Energy Level Diagram
> Draw the energy levels (like a ladder with rungs getting closer together at the top):
> - Label n = 1, 2, 3, ...
> - Draw arrows for Lyman, Balmer, Paschen transitions
> - Show that longer arrows (bigger ΔE) → shorter wavelength → higher energy photons

### PhET Simulation
> PhET "Bohr Model" or "Models of the Hydrogen Atom":
> - Compare Thomson, Rutherford, Bohr models
> - See electrons "jump" between levels
> - Observe which spectral lines are produced

---

## 🌍 Applications

| Application | Connection to Bohr's model |
|-------------|----------------------------|
| 💡 **Fluorescent lights / neon signs** | Exciting atoms → electrons jump → emit specific colours |
| 🔬 **Spectroscopy (chemical analysis)** | Identifying elements by their spectral fingerprints (Bohr's model explains why they're unique!) |
| ☀️ **Stellar spectra (astronomy)** | Fraunhofer lines in sunlight — tells us what elements stars contain |
| 🩺 **X-ray machines** | X-rays produced when electrons jump in high-Z atoms |
| 💻 **Semiconductors & LEDs** | Energy band theory evolved from the idea of quantised energy levels |
| 🔭 **Redshift → expanding universe** | Spectral lines shift → Hubble's law → the Big Bang |
| 🧬 **Lasers** | Stimulated emission (Einstein, 1917) relies on controlled quantum jumps between energy levels |

---

## 📚 Curriculum Connection — IGCSE / A-Level

| Syllabus | Topic | Link |
|----------|-------|------|
| **IGCSE Physics** | 5.2 Radioactivity & Particles | Models of the atom (mention Thomson, Rutherford, Bohr) |
| **IGCSE Co-ordinated** | Atomic structure | Bohr model; energy levels; line spectra |
| **A-Level Physics** | Particles & quantum phenomena | **Energy levels; photon emission; line spectra; ionisation energy** |
| **A-Level Physics** | Quantum physics | Wave-particle duality; photoelectric effect; **the hydrogen spectrum** |
| **A-Level Chemistry** | Atomic structure | **Bohr model → sub-shells → quantum numbers → orbitals** |

### Key Calculations

**1. Energy of a photon emitted from n=3 → n=2 (Hα line):**
```
ΔE = 13.6(1/2² − 1/3²) = 13.6(1/4 − 1/9) = 13.6(5/36) = 1.89 eV
λ = hc/ΔE = (6.63×10⁻³⁴ × 3×10⁸)/(1.89 × 1.602×10⁻¹⁹) = 656 nm (red — matches!)
```

**2. Ionisation energy from n=2:**
```
E_ion(2) = E_∞ − E₂ = 0 − (−3.40) = 3.40 eV
```
(This is why only UV light can ionise excited hydrogen atoms!)

**3. Radius of the n=3 orbit:**
```
r₃ = 3² × a₀ = 9 × 5.29×10⁻¹¹ = 4.76 × 10⁻¹⁰ m ≈ 4.8 Å
```

### Questions for Students

1. **State** Bohr's three postulates.
   - *Answer: (1) Stationary states (no radiation), (2) quantised angular momentum: mvr = nℏ, (3) quantum jumps: ΔE = hf*

2. **Derive** the energy of the n-th level of hydrogen.
   - *Answer: Combine mvr = nℏ with k·e²/r² = mv²/r → solve for r and E → E_n = −13.6/n² eV*

3. **Calculate** the wavelength of light emitted when an electron falls from n=4 → n=2.
   - *Answer: ΔE = 13.6(1/4 − 1/16) = 13.6(3/16) = 2.55 eV → λ = hc/ΔE ≈ 486 nm (blue-green, Hβ line)*

4. **Explain** why Bohr's model works for hydrogen but fails for helium.
   - *Answer: Bohr's model assumes a single electron orbiting a nucleus. Helium has **two electrons** → electron-electron repulsion must be accounted for → can't solve analytically*

5. **Why** was the Franck–Hertz experiment important?
   - *Answer: It provided direct experimental evidence that **atomic energy levels are quantised**, confirming Bohr's model*

---

## 🔗 References

- Bohr, N. (1913). "On the Constitution of Atoms and Molecules" — *Philosophical Magazine*, 26(151), 1–24 — **Part I: The hydrogen atom**
- Bohr, N. (1913). "On the Constitution of Atoms and Molecules" — *Philosophical Magazine*, 26(153), 476–502 — **Part II: Multi-electron atoms**
- Bohr, N. (1913). "On the Constitution of Atoms and Molecules" — *Philosophical Magazine*, 26(155), 857–875 — **Part III: Molecules**
- Bohr, N. (1922). *Nobel Lecture* — "The Structure of the Atom"
- Balmer, J. J. (1885). "Notiz über die Spectrallinien des Wasserstoffs" — *Annalen der Physik*, 261(5), 80–87
- Rydberg, J. R. (1890). "Recherches sur la constitution des spectres d'émission des éléments chimiques" — *Kongliga Svenska Vetenskaps-Akademiens Handlingar*, 23(11)
- Franck, J. & Hertz, G. (1914). "Über Zusammenstöße zwischen Elektronen und den Molekülen des Quecksilberdampfes" — *Verhandlungen der Deutschen Physikalischen Gesellschaft*, 16, 457–467
- Sommerfeld, A. (1916). "Zur Quantentheorie der Spektrallinien" — *Annalen der Physik*, 356(17), 1–94 — **Elliptical orbits + fine structure**
- de Broglie, L. (1924). "Recherches sur la théorie des quanta" — PhD thesis — **Wave nature of electrons**
- Heisenberg, W. (1925). "Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen" — Matrix mechanics
- Schrödinger, E. (1926). "Quantisierung als Eigenwertproblem" — Wave equation
- Heisenberg, W. (1927). "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik" — **Uncertainty principle**
- Bohr, N. (1928). "The Quantum Postulate and the Recent Development of Atomic Theory" — Complementarity
- Pais, A. (1991). *Niels Bohr's Times: In Physics, Philosophy, and Polity*
- Moore, R. (1966). *Niels Bohr: The Man, His Science, and the World They Changed*
- Kragh, H. (2012). *Niels Bohr and the Quantum Atom: The Bohr Model of Atomic Structure 1913–1925*