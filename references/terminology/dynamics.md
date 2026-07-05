---
title: Dynamics
field: Mechanics
type: terminology
version: 1
tags: [dynamics, forces, motion, newton's laws, acceleration, kinematics]
related_lectures: [topic15_forces]
related_terminology: [kinematics, momentum, impulse, inertia, terminal_velocity]
---

# Dynamics

## 📖 Etymology

**Dynamics** comes from the Greek word **"δύναμις"** (*dynamis*) meaning "power, force, strength, ability." From the same root we get **dynamite**, **dynamo**, **dynamic**, and **dynasty** — all carrying the idea of power and force.

The term **"dynamics"** as a branch of physics was introduced by **Gottfried Wilhelm Leibniz** (1646–1716), who distinguished between:
- **Kinematics** — the geometry of motion (description without forces)
- **Dynamics** — the study of forces and their relationship to motion

The word was popularised in **Isaac Newton**'s *Principia Mathematica* (1687), though Newton called it the study of "motions and forces" rather than using the term "dynamics" directly.

---

## 📜 Historical Timeline

### 🏛️ Aristotle (384–322 BCE)

Aristotle's dynamics was based on two principles:
- **Natural motion**: objects seek their "natural place" (earth downward, fire upward)
- **Violent motion**: motion requiring a continuous external force

He believed that the speed of a falling object is proportional to its weight and inversely proportional to the resistance of the medium. This was the dominant view for nearly 2,000 years.

### 🔭 Galileo Galilei (1564–1642)

Galileo is considered the **father of modern dynamics**. His key contributions:
- **Inclined plane experiments**: established that acceleration is constant for a falling object, independent of mass
- **Principle of inertia**: a body in motion stays in motion unless acted upon by a force
- **Parabolic projectile motion**: showed that horizontal and vertical motion are independent

Galileo's work laid the experimental foundation for Newton's laws.

### 🧠 Isaac Newton (1687) — The Foundation

In *Philosophiæ Naturalis Principia Mathematica*, Newton published his **Three Laws of Motion**, which form the complete foundation of classical dynamics:

| Law | Statement | Equation |
|-----|-----------|----------|
| **First Law** (Inertia) | An object remains at rest or in uniform motion unless acted on by a net force | $F_{\text{net}} = 0 \iff \Delta v = 0$ |
| **Second Law** | Net force equals rate of change of momentum | $F = ma$ (or $F = \Delta p / \Delta t$) |
| **Third Law** | For every action, there is an equal and opposite reaction | $F_{AB} = -F_{BA}$ |

Newton also introduced the **Law of Universal Gravitation**, unifying terrestrial and celestial dynamics:

$$ F = G\frac{m_1 m_2}{r^2} $$

### ⚡ Leonhard Euler (1750)

Euler formalised Newton's Second Law into the differential form used today:

$$ F = \frac{dp}{dt} = m\frac{dv}{dt} = ma $$

He also extended dynamics to **rotational motion** ($\tau = I\alpha$), establishing **rigid-body dynamics**.

### 🚗 Joseph-Louis Lagrange (1788)

In *Mécanique Analytique*, Lagrange reformulated dynamics using **energy** rather than forces. His Lagrangian approach:

$$ \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} = 0 $$

where $L = T - V$ (kinetic minus potential energy). This is often more powerful than Newtonian dynamics for complex systems.

### 🌌 Albert Einstein (1905, 1915)

- **Special Relativity (1905)**: Newtonian dynamics breaks down at speeds near $c$. Relativistic dynamics uses $p = \gamma mv$ and $E = mc^2$
- **General Relativity (1915)**: gravity is not a force but a curvature of spacetime — a revolutionary reinterpretation of gravitational dynamics

### ⚛️ 20th Century & Beyond

- **Quantum dynamics**: the **Schrödinger equation** ($i\hbar\frac{\partial}{\partial t}|\Psi\rangle = \hat{H}|\Psi\rangle$) governs the dynamics of quantum systems
- **Chaos theory**: deterministic dynamics can produce unpredictable behaviour (butterfly effect, Lorenz attractor)
- **Celestial dynamics**: N-body simulations of planetary systems, galaxy formation, and orbital mechanics

---

## 📐 Modern Definition

### Dynamics

> **Dynamics** is the branch of mechanics concerned with the **relationship between forces and motion**. It answers the question **"Why does motion happen?"** — as opposed to kinematics, which only describes **how** objects move.

### The Branches of Mechanics

| Branch | Studies | Key Question | Example |
|--------|---------|--------------|---------|
| **Kinematics** | Description of motion | *How* does it move? | $v = u + at$ |
| **Dynamics** | Forces causing motion | *Why* does it move? | $F = ma$ |
| **Statics** | Forces in equilibrium | *Why* doesn't it move? | $\sum F = 0$ |

### Newton's Laws of Motion (Foundation of Dynamics)

**First Law (Inertia):**
> A body remains at rest or in uniform motion in a straight line unless acted upon by a net external force.

**Second Law (Force & Acceleration):**
> The net force on a body is equal to the product of its mass and acceleration, and acts in the direction of the acceleration.

$$ \boxed{F_{\text{net}} = ma} $$

**Third Law (Action-Reaction):**
> When one body exerts a force on a second body, the second body exerts an equal and opposite force on the first.

### Dynamics in Different Regimes

| Regime | Governing Equation | Key Feature |
|--------|-------------------|-------------|
| **Newtonian** (classical) | $F = ma$ | $v \ll c$ |
| **Relativistic** | $F = \frac{d}{dt}(\gamma mv)$ | $v \approx c$ |
| **Quantum** | $i\hbar\partial_t\Psi = \hat{H}\Psi$ | Atomic scale |
| **Fluid** | Navier-Stokes equations | Continuous media |

---

## 🧪 Key Experiments

### 1. Newton's Second Law (Dynamics Trolley)
A trolley on a friction-compensated runway is pulled by a hanging mass. The acceleration is measured using light gates. Varying the force (hanging mass) and mass (adding weights to the trolley) verifies $F = ma$.

### 2. Atwood Machine (1784)
Two masses connected by a string over a pulley. The net force is $(m_1 - m_2)g$, and the total mass is $(m_1 + m_2)$. Measuring acceleration verifies Newton's Second Law for a system.

### 3. Inclined Plane — Galileo's Experiment
A ball rolls down an inclined plane. The acceleration depends on $g\sin\theta$, verifying that the component of weight along the slope causes the acceleration.

### 4. Pendulum Dynamics
The period of a simple pendulum depends only on length and $g$ (for small angles). This is a classic example of **restoring force** dynamics — the force is proportional to displacement.

---

## 🌍 Real-World Applications

| Application | How Dynamics Matters |
|------------|---------------------|
| 🚀 **Rocket launch** | $F = ma$ — thrust must exceed weight to produce upward acceleration |
| 🚗 **Car acceleration** | Engine force overcomes friction and air resistance — net force determines acceleration |
| 🛰️ **Satellite orbits** | Gravitational dynamics — $F = GMm/r^2$ provides the centripetal force for orbit |
| 🏎️ **Formula 1** | Aerodynamic forces, tyre friction, and engine power all interact dynamically |
| 🎢 **Roller coaster** | Dynamics of gravitational potential → kinetic energy conversion, loop-the-loop forces |
| 🏢 **Earthquake engineering** | Dynamic response of buildings to oscillating ground motion |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Dynamics and kinematics are the same thing" | ❌ Kinematics **describes** motion (position, velocity, acceleration). Dynamics **explains** motion (forces, causes) |
| "If an object is moving, there must be a net force on it" | ❌ Newton's First Law — an object in uniform motion has **zero net force** |
| "Dynamics only applies to Earth" | ❌ Dynamics applies everywhere — from subatomic particles to galaxies |
| "A larger mass always accelerates more slowly" | ❌ Not if the force also scales with mass (e.g. gravity: $F = mg$, so $a = g$ regardless of mass) |
| "Action-reaction forces cancel each other out" | ❌ They act on **different objects**, so they cannot cancel for the same object |

---

## 🔗 Related Terminology & Lectures

- [Terminology: Kinematics](kinematics.md) — the description of motion (complement to dynamics)
- [Terminology: Momentum](momentum.md) — $p = mv$, conservation of momentum in dynamics
- [Terminology: Impulse](impulse.md) — $F\Delta t = \Delta p$, force over time
- [Terminology: Inertia](inertia.md) — resistance to change in motion
- [Terminology: Statics](statics.md) — the equilibrium counterpart of dynamics
- [Topic 1.5 Forces](../lectures/topic15_forces.md) — Newton's Laws of Motion

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*