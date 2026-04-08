---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Spiral Model

## What it is

The **Spiral Model** (Barry Boehm, 1986) is a **risk-driven** software development process that combines elements of **iterative** development with **systematic** risk management. Work progresses through repeated **spirals** (cycles), each passing through four quadrants: **determine objectives**, **identify and resolve risks**, **develop and test**, and **plan the next iteration**. Each spiral produces a progressively more complete version of the product.

It is **not** a simple waterfall or a lightweight Agile cadence. It **is** a strong fit when **high-risk**, **large-scale**, or **safety-critical** systems require systematic risk analysis before committing resources to each development phase.

## Process diagram (handbook)

![Spiral Model — quadrant cycle](../docs/assets/methodology-spiral-quadrants.svg)

*Each spiral passes through four quadrants; the radius grows with cumulative cost and progress. Risk analysis gates each cycle.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Spiral model**](https://en.wikipedia.org/wiki/Spiral_model) | **Stable overview** of Boehm's model—quadrants, risk-driven cycles, history, and comparison with other lifecycles. |
| [Wikipedia — Barry Boehm](https://en.wikipedia.org/wiki/Barry_Boehm) | **Author** biography—context for the model's origins in defense/aerospace software. |
| [SEI/CMU — Spiral Model resources](https://resources.sei.cmu.edu/) | **Software Engineering Institute** — research and publications on risk-driven processes; search for "spiral model" for relevant papers. |

**Paper:** Boehm, B.W. "A Spiral Model of Software Development and Enhancement," *IEEE Computer*, 21(5), May 1988 — the canonical publication.

---

## Core structure (summary)

### Four quadrants (per spiral)

| Quadrant | Activities |
|----------|-----------|
| **1 — Determine objectives** | Define goals, alternatives, and constraints for this cycle. |
| **2 — Identify & resolve risks** | Risk analysis, prototyping, simulation, benchmarking — address top risks before committing to build. |
| **3 — Develop & test** | Design, code, integrate, and verify the increment. |
| **4 — Plan next iteration** | Review results, get stakeholder commitment, plan the next spiral. |

### Key characteristics

| Characteristic | Description |
|----------------|-------------|
| **Risk-driven** | Risk analysis determines the effort and approach for each cycle; high-risk items are addressed first. |
| **Iterative** | Multiple spirals, each producing a more complete product; not a single pass. |
| **Anchor-point milestones** | Life Cycle Objectives (LCO), Life Cycle Architecture (LCA), Initial Operational Capability (IOC) — stakeholder commitment gates. |
| **Flexible** | Subsumes other models: a spiral can contain a waterfall phase, a prototype, an Agile iteration, or a formal review. |
| **Cumulative cost** | The spiral's radius represents cumulative project cost and progress. |

---

## Mapping to this blueprint's SDLC

[`SDLC.md`](../SDLC.md) uses **Phases A–F** (discover → release). The Spiral Model maps as **multiple passes** through these phases, with risk analysis gating each pass:

| Spiral idea | Blueprint touchpoint |
|-------------|----------------------|
| Objectives + constraints (Q1) | Phase A–B: discovery, requirements, feasibility in `docs/requirements/`. |
| Risk analysis + prototyping (Q2) | Phase B–C: risk register, proof-of-concept, design alternatives. |
| Development + testing (Q3) | Phase C–E: build, verify, integrate — scope depends on the spiral. |
| Planning + review (Q4) | Phase E–F + next A: review, stakeholder commit, plan next cycle. |
| Anchor-point milestones | Phase gates: LCO ≈ end of discovery, LCA ≈ architecture approved, IOC ≈ first operational release. |

Each **spiral** may be short (weeks for a prototype) or long (months for a safety-critical build phase). The key is that **risk analysis** precedes **commitment** in every cycle.

---

## Agentic SDLC: Spiral + agents + tracking

| Topic | Guidance |
|-------|----------|
| **Risk analysis** | Agents can assist with **automated risk scanning** (dependencies, security, complexity metrics) but **human judgment** drives risk prioritization and resolution strategy. |
| **Prototyping** | Agents can rapidly generate prototypes for risk reduction; ensure prototypes are **disposable** (not accidentally promoted to production). |
| **Anchor-point reviews** | Stakeholder commitment at LCO/LCA/IOC is a **human** decision; agents can prepare evidence packages. |
| **Tracking** | Each spiral should be trackable as a **milestone** or **iteration** in the tracking spine; risk register updates are explicit artifacts. |

---

## Spiral vs other methodologies

| Comparison | Relationship |
|------------|-------------|
| **Spiral → Phased** | Phased delivery is a **single pass**; Spiral is **multiple passes** with risk gates. A phased project can use Spiral thinking by adding risk analysis before each phase gate. |
| **Spiral → Agile** | Agile iterations can be viewed as **lightweight spirals** where risk analysis is implicit in demo/retro feedback. Spiral makes risk management **explicit and systematic**. |
| **Spiral → V-Model** | V-Model pairs development with testing levels; Spiral adds **risk-driven iteration** and **prototyping** to the verification structure. |

---

## Ceremonies

**Methodology-neutral intent types** (Align, Commit, Sync, …) live in [`ceremonies/ceremony-foundation.md`](ceremonies/ceremony-foundation.md). **Spiral events mapped to those intents:** [`ceremonies/spiral.md`](ceremonies/spiral.md).

---

## Prescriptive deep dive (teams)

Package **[`spiral/README.md`](spiral/README.md)** — foundation fit, roles (risk analyst, chief architect, project manager, stakeholders), ceremonies (risk review, anchor-point review, prototype demo, spiral planning), process maps.

---

## Further reading

- [Wikipedia — Spiral model](https://en.wikipedia.org/wiki/Spiral_model) — **Overview** of quadrants and history.  
- [IEEE — Boehm's 1988 paper](https://doi.org/10.1109/2.59) — **Original** publication (may require IEEE access).  
- Companion: [Phased delivery](phased-delivery.md), [Agile umbrella](agile.md), [Agentic SDLC](agentic-sdlc.md)
