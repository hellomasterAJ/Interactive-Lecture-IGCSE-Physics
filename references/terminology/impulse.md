---
title: Impulse
field: Mechanics
type: terminology
version: 1
tags: [impulse, momentum, force, collision, impact]
related_lectures: [topic15_forces]
---

# Impulse

## 📖 Etymology

**Impulse** derives from the Latin word **"impulsus"**, the past participle of **"impellere"** — meaning "to push against, strike upon, drive forward" (from *in-* "against" + *pellere* "to push, drive").

The term entered physics through the study of **collisions and impacts**. The mathematical relationship between impulse and momentum change ($F\Delta t = \Delta p$) was implicitly understood by **Newton** in *Principia* (1687), though the formal name "impulse" was popularised later in the 18th–19th century as mechanics was systematised by Euler, Lagrange, and others.

---

## 📜 Historical Timeline

### 🏛️ Ancient Foundations — Aristotle (384–322 BCE)

Aristotle's analysis of motion lacked a clear concept of impulse. He saw motion as requiring continuous force — no distinction between force applied momentarily (impulse) and force applied continuously.

### 🧠 René Descartes (1644)

Descartes' "quantity of motion" ($mv$) was an early form of momentum, but he treated interactions as instantaneous exchanges — an implicit impulse framework.

### ⚡ Isaac Newton (1687) — The Core Insight

In *Principia Mathematica*, Newton's **Second Law** originally stated:

> *"The change in motion [momentum] is proportional to the motive force impressed and is made in the direction of the straight line in which that force is impressed."*

This is fundamentally an **impulse-momentum** statement: the "motive force impressed" acting over a short time changes the body's momentum. Newton understood that for a collision, what matters is not just the force, but the **force multiplied by the time it acts**.

### 🔧 Leonhard Euler (1750)

Euler formalised Newton's second law into the continuous differential form $F = \frac{dp}{dt}$, which directly leads to the impulse-momentum theorem when integrated over time:

$$ \int_{t_1}^{t_2} F \, dt = \Delta p $$

### 🚀 Jean le Rond d'Alembert (1743)

D'Alembert extended the concept to **constrained motion**, using impulse-based reasoning in his *Traité de Dynamique*. His principle ($\sum(F_i - m_i a_i) \cdot \delta r_i = 0$) can be derived from impulse-momentum considerations.

### 🏭 19th–20th Century Engineering

Impulse became a practical engineering tool:
- **Impact mechanics**: analysing collisions, car crashes, hammer blows
- **Rocket propulsion**: the **specific impulse** ($I_{sp}$) measures rocket efficiency
- **Sports science**: analysing bat/ball, club/ball, foot/ball impacts

---

## 📐 Modern Definition

### Impulse

> **Impulse** ($J$) is the product of a force and the time interval over which it acts. It equals the **change in momentum** of the object.

$$ \boxed{J = F \cdot \Delta t = \Delta p = mv - mu} $$

| Symbol | Meaning | Unit | Nature |
|--------|---------|------|--------|
| $J$ | Impulse | $\text{N} \cdot \text{s}$ | ✅ Vector |
| $F$ | Average force | $\text{N}$ | ✅ Vector |
| $\Delta t$ | Time interval | $\text{s}$ | ❌ Scalar |
| $\Delta p$ | Change in momentum | $\text{kg} \cdot \text{m/s}$ | ✅ Vector |

### Impulse from a Varying Force

When the force is not constant, impulse is the **area under a force–time graph**:

$$ J = \int_{t_1}^{t_2} F(t) \, dt $$

This is the **area under the F–t curve**.

### Impulse-Momentum Theorem

$$ F_{\text{avg}} \cdot \Delta t = m \Delta v $$

This theorem is useful when the force varies rapidly and is difficult to measure directly — measure velocities before and after instead.

### Specific Impulse (Rocketry)

$$ I_{sp} = \frac{F_{\text{thrust}}}{g_0 \cdot \dot{m}} $$

where $g_0 = 9.81 \, \text{m/s}^2$ and $\dot{m}$ is the mass flow rate of propellant. **Unit**: seconds. Higher $I_{sp}$ means more efficient propulsion.

---

## 🧪 Key Experiments

### 1. Egg Drop Experiment
An egg dropped onto a hard surface breaks ($\Delta t$ small → large $F$). The same egg dropped onto a cushion survives ($\Delta t$ large → small $F$). Demonstrates $F\Delta t = \Delta p$ in action.

### 2. Force–Time Sensor (F–t Graph)
A collision sensor (e.g. Vernier force plate) records force as a function of impact time. The area under the F–t curve gives the impulse. Students verify that the area equals $m\Delta v$.

### 3. Air Track with Force Probe
A glider on an air track collides with a force probe attached to a spring. The force–time curve is recorded, velocities are measured with photogates, and impulse is verified to equal momentum change.

### 4. Ballistic Pendulum (Revisited)
The impulse imparted by a bullet to a block is $J = \Delta p = m_{\text{bullet}} v_{\text{bullet}}$. Measuring the swing height gives $v_{\text{bullet}}$ indirectly.

---

## 📈 Real-World Applications

| Application | How Impulse Matters |
|------------|-------------------|
| 🚗 **Airbags** | Increase $\Delta t$ → decrease $F$ for same $\Delta p$ — prevents injury |
| 🏏 **Catching a cricket ball** | Pull hands back on impact: increases $\Delta t$ → reduces $F$ on hands |
| 🥊 **Boxing gloves** | Padding increases impact time → reduces peak force |
| 🚀 **Rocket engines** | High $I_{sp}$ means more thrust per unit of fuel |
| 🔨 **Hammer and nail** | Small $\Delta t$ → large $F$ — the force concentrates to drive the nail |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Impulse and force are the same thing" | ❌ Impulse is **force × time**. A small force over a long time can produce the same impulse as a large force over a short time |
| "Impulse is zero if force is zero" | ✅ Correct — no force means no impulse |
| "Impulse is only for collisions" | ❌ Any force acting over time produces an impulse — including gravity, friction, and thrust |
| "A larger impulse always means more damage" | ❌ A large impulse delivered over a **long** time (airbag) causes less damage than the same impulse delivered instantly |
| "Impulse is a scalar" | ❌ Impulse is a **vector** — same direction as the force that produces it |

---

## 🔗 Related Lectures

- [Topic 1.5 Forces](../lectures/topic15_forces.md) — IGCSE Physics covering $F = \Delta p / \Delta t$
- [Terminology: Momentum](momentum.md) — companion term

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*