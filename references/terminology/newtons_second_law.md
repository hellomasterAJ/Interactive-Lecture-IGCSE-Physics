---
title: Newton's Second Law of Motion
field: Mechanics
type: terminology
version: 1
tags: [newton's second law, force, acceleration, mass, momentum, f=ma]
related_lectures: [topic15_forces]
related_terminology: [newtons_laws, momentum, impulse, dynamics]
aliases: [Law of Acceleration, Lex II, F=ma]
---

# Newton's Second Law of Motion (Law of Acceleration)

## 📖 Etymology

The **Second Law** is Newton's most famous and practically useful law. In the original *Principia*, the Latin reads:

> *"Mutationem motus proportionalem esse vi motrici impressae, et fieri secundum lineam rectam qua vis illa imprimitur."*

— "The change in motion is proportional to the motive force impressed and is made in the direction of the straight line in which that force is impressed."

Note that Newton used **"motus"** (motion) meaning **momentum** ($mv$), not velocity. The modern form $F = ma$ was introduced by **Leonhard Euler** in 1750.

---

## 📜 The Two Forms of the Second Law

### Newton's Original Form (1687)

$$ \boxed{F \propto \frac{\Delta(mv)}{\Delta t}} $$

Or in modern calculus notation:

$$ \boxed{F = \frac{dp}{dt}} $$

This form is **more general** — it works even when mass changes (rockets, relativistic speeds).

### Euler's Reformulation (1750)

For a body with **constant mass**:

$$ \boxed{F = m \frac{dv}{dt} = ma} $$

This is the form taught at IGCSE and A-Level.

### Why Both Forms Matter

| Form | When to Use | Advantage |
|------|------------|-----------|
| $F = ma$ | Constant mass (most everyday situations) | Simple, intuitive |
| $F = dp/dt$ | Changing mass (rockets, conveyer belts), original Newtonian form, relativistic dynamics | More universal |

---

## 📐 The Law

### Modern Statement

> **The net force acting on an object is equal to the rate of change of its momentum, and acts in the direction of that change.**

For constant mass, this simplifies to:

> **The acceleration of an object is directly proportional to the net force acting on it, and inversely proportional to its mass.**

$$ \boxed{\sum \vec{F} = m\vec{a}} $$

### Key Insights

| Relationship | Meaning |
|-------------|---------|
| $F \propto a$ | Double the force → double the acceleration (same mass) |
| $a \propto 1/m$ | Double the mass → half the acceleration (same force) |
| $\vec{F} \parallel \vec{a}$ | Force and acceleration are **always in the same direction** |
| Vector nature | Forces in perpendicular directions are independent — resolve into $x$ and $y$ components |

### The Equation in Components

$$ \sum F_x = ma_x \qquad \sum F_y = ma_y \qquad \sum F_z = ma_z $$

This is why we can analyse horizontal and vertical motion independently (e.g., projectile motion).

---

## 🧪 Key Experiment — The Dynamics Trolley

A trolley on a friction-compensated runway is pulled by a hanging mass via a string over a pulley:

| Hanging Mass ($m_h$) | Force ($F = m_h g$) | Trolley Mass ($M$) | Acceleration ($a$) | $F/m$ Check |
|:---:|:---:|:---:|:---:|:---:|
| 50 g | 0.49 N | 1.0 kg | 0.49 m/s² | 0.49 |
| 100 g | 0.98 N | 1.0 kg | 0.98 m/s² | 0.98 |
| 100 g | 0.98 N | 2.0 kg | 0.49 m/s² | 0.49 |
| 150 g | 1.47 N | 1.5 kg | 0.98 m/s² | 0.98 |

**Conclusion**: The data confirm $a = F/m$ within experimental error.

---

## 🌍 Everyday Examples

| Situation | Second Law in Action |
|-----------|---------------------|
| 🏎️ **Car acceleration** | More engine force → greater acceleration ($a = F/m$). A lighter car accelerates faster for the same engine |
| 🛑 **Braking** | Brake force produces deceleration ($a = -F_{\text{brake}}/m$). More mass → longer stopping distance |
| 🏋️ **Pushing a heavy box** | Same force on a heavier box → smaller acceleration — you have to push harder or longer |
| 🚀 **Rocket launch** | Thrust must exceed weight: $F_{\text{net}} = F_{\text{thrust}} - mg = ma$. The rocket accelerates upward |
| ⚽ **Kicking a ball** | The force of your foot on the ball determines its acceleration. A harder kick = larger $F$ = larger $a$ |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "$F = ma$ means force is caused by acceleration" | ❌ **Force causes acceleration**, not the other way around |
| "A large force always produces a large acceleration" | ❌ If the mass is also large, $a = F/m$ may still be small (e.g., pushing a truck) |
| "$F = ma$ only works for horizontal motion" | ❌ It works for **any direction** — vertical, horizontal, or at an angle |
| "If $a = 0$, then $F = 0$ too" | ❌ If $a = 0$, the **net** force is zero, but individual forces can still be large (they just cancel) |
| "The Second Law is always $F = ma$" | ❌ Newton's original form was $F = dp/dt$. $F = ma$ is a special case for constant mass |

---

## 🔗 Related Terminology & Lectures

- [Newton's Laws of Motion (Complete)](newtons_laws.md) — all three laws together with summary table
- [Terminology: Momentum](momentum.md) — $p = mv$, the quantity in Newton's original Second Law
- [Terminology: Impulse](impulse.md) — $F\Delta t = \Delta p$, directly derived from the Second Law
- [Terminology: Dynamics](dynamics.md) — the study of forces causing motion
- [Topic 1.5 Forces](../lectures/topic15_forces.md) — IGCSE lecture on forces and Newton's Laws

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*