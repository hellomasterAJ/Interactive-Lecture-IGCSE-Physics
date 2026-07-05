---
title: Momentum
field: Mechanics
type: terminology
version: 1
tags: [momentum, impulse, conservation, collision, force]
related_lectures: [topic15_forces]
---

# Momentum

## 📖 Etymology

**Momentum** comes from the Latin word **"mōmentum"** meaning "movement" or "moving power". It is derived from **"movēre"** (to move).

The term was first used in a physical sense by **John Philoponus** (6th century CE), a Byzantine philosopher who challenged Aristotle's view of motion. He proposed that a moving object carries an inherent "impetus" — an early precursor to the concept of momentum.

The modern mathematical definition **$p = mv$** was formalised by **René Descartes** (1596–1650) and later refined by **Isaac Newton** and **Gottfried Wilhelm Leibniz**.

---

## 📜 Historical Timeline

### 🏛️ Aristotle (384–322 BCE)

Aristotle believed that a moving object requires a continuous force to keep it moving — once the force stops, the object stops. He had no concept of momentum or inertia.

### 💡 John Philoponus (6th Century CE)

Proposed the **theory of impetus** — an object is given an internal force ("impetus") when set in motion, which keeps it moving until it is exhausted. This was the first step away from Aristotelian physics.

### 🎯 Jean Buridan (14th Century)

The French philosopher **Jean Buridan** (c. 1300–1358) refined the impetus theory. He stated:
- Impetus is proportional to speed and quantity of matter (an early intuition of $p = mv$)
- In the absence of resistance, impetus would keep an object moving forever

This directly foreshadowed Newton's first law of motion.

### 📐 René Descartes (1644)

In *Principia Philosophiae*, Descartes formally defined momentum as the **"quantity of motion"**:
$$ \text{Quantity of motion} = \text{mass} \times \text{speed} $$

He also proposed the **conservation of quantity of motion** in the universe — though he treated it as a scalar (not a vector), which was later corrected.

### 🧠 Isaac Newton (1687)

In *Principia Mathematica*, Newton gave momentum its modern definition as a **vector quantity**:

> **Newton's Second Law** (original form): The rate of change of momentum is proportional to the impressed force, and takes place in the direction of the force.
> $$ F = \frac{dp}{dt} $$

Newton also used momentum to analyse collisions, establishing the **principle of conservation of momentum** for closed systems.

### ⚙️ Gottfried Wilhelm Leibniz (1686)

Leibniz distinguished between **momentum** ($mv$) and **kinetic energy** ($mv^2$), sparking the famous **vis viva** ("living force") debate. He argued that $mv^2$ (not $mv$) was the true measure of "force" in a moving body. This debate lasted over 50 years and ultimately led to the clear distinction between momentum and energy that we use today.

### 🔬 20th Century

- **Quantum mechanics**: Momentum is quantised and obeys the **uncertainty principle** ($\Delta x \Delta p \geq \frac{\hbar}{2}$)
- **Relativity**: Einstein showed that momentum at high speeds follows $p = \gamma mv$ where $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$

---

## 📐 Modern Definition

### Momentum

> **Momentum** ($p$) is the product of an object's mass and its velocity. It is a **vector quantity** — its direction is the same as the velocity.

$$ \boxed{p = mv} $$

| Symbol | Meaning | Unit | Nature |
|--------|---------|------|--------|
| $p$ | Momentum | $\text{kg} \cdot \text{m/s}$ | ✅ Vector |
| $m$ | Mass | $\text{kg}$ | ❌ Scalar |
| $v$ | Velocity | $\text{m/s}$ | ✅ Vector |

### Newton's Second Law in Terms of Momentum

$$ F = \frac{\Delta p}{\Delta t} = \frac{mv - mu}{\Delta t} $$

For constant mass, this simplifies to the familiar $F = ma$.

### Impulse

**Impulse** ($J$) is the change in momentum caused by a force acting over a time interval:

$$ J = F \cdot \Delta t = \Delta p = mv - mu $$

**Unit**: $\text{N} \cdot \text{s}$ (equivalent to $\text{kg} \cdot \text{m/s}$)

### Conservation of Momentum

> In a **closed system** (no external forces), total momentum before an interaction equals total momentum after.

$$ m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 $$

#### Types of Collisions

| Type | Momentum | Kinetic Energy | Example |
|------|----------|---------------|---------|
| **Elastic** | ✅ Conserved | ✅ Conserved | Billiard balls, gas molecules |
| **Inelastic** | ✅ Conserved | ❌ Not conserved | Car crash, two objects sticking together |
| **Explosive** | ✅ Conserved | ❌ Increases | Recoil of a gun, rocket propulsion |

---

## 🧪 Key Experiments

### 1. Newton's Cradle (Cradle of Newton)
Demonstrates **conservation of momentum** and **energy** in elastic collisions. When one ball swings and hits the row, the same number of balls swings out on the opposite side.

### 2. Air Track Collisions
A frictionless air track allows near-perfect elastic and inelastic collisions between gliders. Using photogates, velocities before and after can be measured to verify conservation of momentum.

### 3. Ballistic Pendulum
A bullet is fired into a block of wood suspended as a pendulum. By measuring the swing height, the initial velocity of the bullet can be determined using conservation of momentum.

### 4. Rocket Propulsion (Action-Reaction)
A rocket expels gas downward at high velocity. By conservation of momentum, the rocket gains an equal and opposite momentum upward. The **Tsiolkovsky rocket equation** derives from this principle.

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Momentum and kinetic energy are the same thing" | ❌ Different quantities — momentum is a vector ($mv$), kinetic energy is a scalar ($\frac{1}{2}mv^2$). One can be conserved without the other |
| "A stationary object has no momentum" | ✅ Correct — if $v = 0$, then $p = 0$ |
| "Momentum is always conserved in any collision" | ❌ Only in **closed systems** with no external forces. Friction, air resistance, etc. can change total momentum |
| "A heavier object always has more momentum" | ❌ Depends on velocity too — a fast lightweight object can have more momentum than a slow heavy one |
| "In an inelastic collision, momentum is lost" | ❌ Momentum is still conserved — only kinetic energy is lost (to heat, sound, deformation) |

---

## 🔗 Related Lectures

- [Topic 1.5 Forces](../lectures/topic15_forces.md) — IGCSE Physics lecture covering momentum and $F = \Delta p / \Delta t$

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*