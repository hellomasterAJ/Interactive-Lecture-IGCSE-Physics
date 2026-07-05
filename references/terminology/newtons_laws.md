---
title: Newton's Laws of Motion
field: Mechanics
type: terminology
version: 1
tags: [newton's laws, inertia, force, acceleration, action-reaction, classical mechanics]
related_lectures: [topic15_forces]
related_terminology: [inertia, dynamics, momentum, impulse, statics]
---

# Newton's Laws of Motion

## 📖 Etymology

The word **"law"** comes from the Old English **"lagu"** — "a rule, ordinance, statute." In science, a **law** is a concise, general statement of a consistent pattern in nature.

**Isaac Newton** (1643–1727) did not invent the term "Newton's Laws" himself. In his monumental work **Philosophiæ Naturalis Principia Mathematica** (1687), he called them the **"Axiomata sive Leges Motus"** — "Axioms, or Laws of Motion." The name **"Newton's Laws"** was applied by later generations as they became the foundation of classical mechanics.

---

## 📜 Historical Timeline

### The Road to Newton — Predecessors

Before Newton, several thinkers had pieces of the puzzle:

| Thinker | Contribution | Date |
|---------|-------------|------|
| **Aristotle** | Motion requires continuous force (wrong, but dominant for 2,000 years) | c. 350 BCE |
| **John Philoponus** | Theory of impetus — internal force keeps objects moving | 6th century CE |
| **Jean Buridan** | Impetus proportional to speed and mass; foreshadows inertia | 14th century |
| **Galileo Galilei** | Principle of inertia; inclined plane experiments; $s \propto t^2$ | 1590–1638 |
| **René Descartes** | Quantity of motion ($mv$); conservation ideas | 1644 |
| **Christiaan Huygens** | Conservation of momentum and kinetic energy in collisions | 1669 |

Newton synthesised these ideas into a single, unified framework.

### 🧠 Isaac Newton (1687) — The Principia

In July 1687, Newton published **Philosophiæ Naturalis Principia Mathematica** (Mathematical Principles of Natural Philosophy), often called simply the **Principia**. It is arguably the most important scientific book ever written.

The **Three Laws of Motion** appear in the opening pages as the "Axioms" — fundamental truths from which all of mechanics could be derived. Newton also added eight **Corollaries** (consequences), including the parallelogram of forces and the conservation of momentum.

> *"Nature is pleased with simplicity, and affects not the pomp of superfluous causes."* — Newton

### ⚡ The 18th–19th Century — Refinement

- **Leonhard Euler** (1750): reformulated the Second Law as $F = ma$ (Newton originally stated it as $F \propto \Delta p / \Delta t$)
- **Jean d'Alembert** (1743): d'Alembert's principle — $\sum(F - ma) = 0$ — extended Newton's laws to constrained systems
- **Joseph-Louis Lagrange** (1788): energy-based reformulation in *Mécanique Analytique*
- **Ernst Mach** (1883): criticised Newton's absolute space and time, paving the way for Einstein

### 🌌 20th Century — Limitations & Extensions

Newton's laws are not universally valid — they apply only in **inertial frames** and at speeds much less than $c$:

| Theory | When Newton's Laws Break Down | Replacement |
|--------|------------------------------|-------------|
| **Special Relativity** (Einstein, 1905) | $v \approx c$ (high speed) | $p = \gamma mv$, $E = mc^2$ |
| **General Relativity** (Einstein, 1915) | Strong gravitational fields | Gravity = spacetime curvature |
| **Quantum Mechanics** (1920s) | Atomic and subatomic scales | Schrödinger equation, uncertainty principle |

Despite these limitations, Newton's laws remain **excellent approximations** for everyday phenomena and are the foundation of **engineering, astronomy, and classical physics**.

---

## 📐 The Three Laws — Modern Definitions

### First Law — The Law of Inertia

> **"Every body perseveres in its state of being at rest or of moving uniformly straight forward, except insofar as it is compelled to change its state by force impressed."**
>
> — Newton's original Latin, 1687

**Modern form:**
> An object at rest stays at rest, and an object in motion stays in motion at constant velocity, **unless acted upon by a net external force**.

$$ \boxed{\sum \vec{F} = 0 \iff \vec{v} = \text{constant}} $$

| Key Concept | Meaning |
|-------------|---------|
| **Inertia** | The natural tendency of an object to resist changes in motion |
| **Mass** | The quantitative measure of inertia — more mass = more resistance |
| **Net force = 0** | The object is either at rest or moving at constant velocity |

**Everyday Example:** A book on a table stays there forever unless you push it. A hockey puck on ice slides for a long time because the net force is nearly zero (low friction).

---

### Second Law — The Law of Acceleration

> **"The change in motion [momentum] is proportional to the motive force impressed, and is made in the direction of the straight line in which that force is impressed."**
>
> — Newton's original, 1687

**Modern form (Euler's formulation, 1750):**
> The net force on an object equals the product of its mass and acceleration, and acts in the direction of the acceleration.

$$ \boxed{\sum \vec{F} = m\vec{a}} $$

**Newton's original form (momentum version):**
$$ \boxed{\sum \vec{F} = \frac{d\vec{p}}{dt}} $$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $\sum \vec{F}$ | Net (resultant) external force | $\text{N}$ |
| $m$ | Mass of the object | $\text{kg}$ |
| $\vec{a}$ | Acceleration | $\text{m/s}^2$ |
| $d\vec{p}/dt$ | Rate of change of momentum | $\text{kg·m/s}^2$ |

**Key implications:**
- Force and acceleration are **always in the same direction**
- Doubling the force **doubles the acceleration** (for constant mass)
- Doubling the mass **halves the acceleration** (for constant force)
- $F = ma$ is a **vector equation** — it applies in each direction independently

**Everyday Example:** Pushing two shopping carts — one empty ($m$ small) and one full ($m$ large). The same push produces a much smaller acceleration on the full cart.

---

### Third Law — The Law of Action-Reaction

> **"To every action there is always opposed an equal reaction; or, the mutual actions of two bodies upon each other are always equal and directed to contrary parts."**
>
> — Newton's original, 1687

**Modern form:**
> When one object exerts a force on a second object, the second object exerts an equal and opposite force on the first.

$$ \boxed{\vec{F}_{AB} = -\vec{F}_{BA}} $$

| Key Concept | Meaning |
|-------------|---------|
| **Action and reaction** | The two forces are **equal in magnitude** and **opposite in direction** |
| **Different objects** | The forces act on **different objects** — they do NOT cancel each other |
| **Same type** | Both forces are of the **same physical nature** (both gravitational, both contact, etc.) |

**Everyday Example:**
- **Walking**: Your foot pushes backward on the ground (action), the ground pushes forward on your foot (reaction) — this is what propels you forward
- **Jumping**: You push down on the ground, the ground pushes you upward
- **Rocket propulsion**: The engine pushes exhaust gases backward, the gases push the rocket forward

---

## 🧪 Key Experiments

### 1. Newton's First Law — The Inertia Experiment
A heavy book is placed on a sheet of paper on a table. If the paper is pulled **slowly**, the book moves with it. If the paper is **yanked quickly**, the book stays put due to its inertia.

### 2. Newton's Second Law — Dynamics Trolley
A trolley is placed on a friction-compensated runway. A known force (hanging mass) accelerates the trolley. Light gates measure the acceleration. Varying the **force** (change hanging mass) and **mass** (add weights to trolley) verifies $F = ma$.

| $F$ (N) | $m$ (kg) | $a$ (m/s²) | $F/m$ |
|---------|----------|------------|-------|
| 0.5 | 1.0 | 0.50 | 0.5 |
| 1.0 | 1.0 | 1.00 | 1.0 |
| 1.0 | 2.0 | 0.50 | 0.5 |

### 3. Newton's Third Law — Spring Balance Pair
Two spring balances are hooked together. When one is pulled, **both read the same value** — regardless of which one is pulled harder. This shows that the force on each balance is equal and opposite.

### 4. Newton's Cradle
A row of suspended metal balls. Lifting and releasing one ball on the left causes exactly one ball on the right to swing out. This demonstrates conservation of momentum AND energy, and the action-reaction forces between balls during collisions.

### 5. Rocket Propulsion (Action-Reaction)
A model rocket or an inflated balloon released with its nozzle open. The air rushes out backward (action), and the balloon/rocket shoots forward (reaction). This is a direct demonstration of Newton's Third Law.

---

## 🌍 Real-World Applications

| Application | Law(s) | How It Works |
|------------|--------|-------------|
| 🚗 **Seatbelts** | 1st Law | Without a seatbelt, your body continues forward (inertia) when the car stops suddenly |
| 🏎️ **Drag racing** | 2nd Law | More engine force → more acceleration. Lighter cars accelerate faster ($a = F/m$) |
| 🚀 **Rocket launch** | 2nd + 3rd | $F_{\text{thrust}} > mg$ → upward acceleration. Exhaust pushes down, rocket goes up |
| 🛑 **ABS Brakes** | 2nd Law | Anti-lock brakes maximise friction force without skidding, maximising deceleration |
| 🏊 **Swimming** | 3rd Law | You push water backward → water pushes you forward |
| 🪂 **Parachute** | 1st + 2nd | Weight = drag at terminal velocity, so net force = 0, acceleration = 0 |
| 🚲 **Cycling** | All three | Push pedals (3rd), accelerate ($F=ma$), coast at constant speed (1st) |
| 🛰️ **Orbiting satellite** | 1st + 2nd | Gravity provides centripetal force ($F=ma_c$). Satellite is in free fall — no net force in its frame |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Newton's First Law is just a special case of the Second Law (with $a=0$)" | ❌ The First Law defines **inertial reference frames**, which are a **prerequisite** for the Second Law. You need the First Law to apply the Second Law |
| "Action-reaction forces cancel out" | ❌ They act on **different objects**, so they cannot cancel for a single system |
| "A moving object has a force acting on it" | ❌ An object in constant-velocity motion has **zero net force** (First Law) |
| "$F=ma$ means a large force always produces a large acceleration" | ❌ Not if the mass is also large — $a = F/m$, so a large force on an enormous mass gives a tiny acceleration |
| "Newton's Laws are universally correct" | ❌ They break down at high speeds ($v \approx c$), strong gravity, and atomic scales |
| "The Third Law means forces always occur in balanced pairs" | ❌ They are equal and opposite, but that does **not** mean the object is in equilibrium — one force acts on one object, the other acts on a different object |

---

## 🔗 Related Terminology & Lectures

- [Terminology: Inertia](inertia.md) — the property underlying the First Law
- [Terminology: Dynamics](dynamics.md) — the broader study of forces and motion
- [Terminology: Momentum](momentum.md) — the original form of the Second Law
- [Terminology: Impulse](impulse.md) — $F\Delta t = \Delta p$, directly derived from the Second Law
- [Terminology: Statics](statics.md) — equilibrium (First Law applied to stationary objects)
- [Topic 1.5 Forces](../lectures/topic15_forces.md) — IGCSE Physics lecture covering Newton's Laws

---

### 🧠 Summary Table

| Law | Name | Core Idea | Equation | Everyday |
|-----|------|-----------|----------|----------|
| **1st** | Inertia | Object resists change in motion | $\sum F = 0 \iff v = \text{constant}$ | Book on a table, hockey puck |
| **2nd** | Acceleration | Force causes acceleration | $\sum F = ma$ | Pushing a trolley |
| **3rd** | Action-Reaction | Forces come in equal-opposite pairs | $F_{AB} = -F_{BA}$ | Walking, rocket propulsion |

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*