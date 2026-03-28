# Feature-Driven Development (FDD)

## What it is

**Feature-Driven Development (FDD)** is a model-driven, short-iteration, **feature-centric** Agile method developed by Jeff De Luca and Peter Coad in the late 1990s. It structures delivery around five sequential activities: **develop an overall model**, **build a features list**, **plan by feature**, **design by feature**, and **build by feature**. Each "feature" is a small, client-valued function expressed as `<action> the <result> <by|for|of|to> a <object>`.

FDD is designed for **larger teams** (10–250 developers) where individual ownership of features within a shared domain model reduces coordination overhead. It is **less ceremony-heavy** than Scrum but more structured than XP.

## Process diagram (handbook)

![FDD — five activities](../docs/assets/methodology-fdd-flow.svg)

*Overall model → features list → plan by feature → design by feature → build by feature. The last two activities iterate per feature set.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Feature-driven development**](https://en.wikipedia.org/wiki/Feature-driven_development) | **Stable overview** of FDD's five activities, roles, and history — entry point before books. |
| [Agile Alliance — FDD](https://www.agilealliance.org/glossary/fdd/) | **Short definition** in the Agile glossary — shared vocabulary. |

**Book:** De Luca & Coad, *Java Modeling in Color with UML* (1999); Palmer & Felsing, *A Practical Guide to Feature-Driven Development* (2002).

---

## Five activities (summary)

| Activity | Purpose | Frequency |
|----------|---------|-----------|
| **1. Develop an overall model** | Domain walkthrough; high-level object model with the team | Once at start; updated as needed |
| **2. Build a features list** | Decompose the model into subject areas → business activities → features | Once; maintained throughout |
| **3. Plan by feature** | Assign feature sets to chief programmers; set completion dates | Once; updated per iteration |
| **4. Design by feature** | Chief programmer selects features, forms feature team, designs collaboratively | Per feature set (1–2 weeks) |
| **5. Build by feature** | Implement, test, inspect, integrate the feature | Per feature set (1–2 weeks) |

---

## Mapping to this blueprint's SDLC

| FDD idea | Blueprint touchpoint |
|----------|----------------------|
| Overall model + features list | Phase A–B: discovery, requirements decomposition. |
| Plan by feature | Phase B: planning, assignment, WBS. |
| Design by feature + build by feature | Phase C–D: build and verify per feature set. |
| Class ownership + inspections | Phase D–E: code review, quality gates. |
| Regular builds | Phase E–F: CI, integration, release readiness. |

---

## Roles (FDD-specific)

| Role | Responsibility |
|------|----------------|
| **Chief programmer** | Experienced developer who leads design and build of a feature set; selects features, forms small teams. |
| **Class owner** | Developer who owns a specific class/module in the domain model; participates in feature teams as needed. |
| **Domain expert** | Business/domain knowledge; participates in modeling and feature definition. |
| **Project manager** | Administrative coordination; reporting; not a gatekeeper for technical decisions. |
| **Chief architect** | Overall model integrity; guides domain decomposition. |

---

## Agentic SDLC: FDD + agents

| Topic | Guidance |
|-------|----------|
| **Modeling** | Agents can generate domain model drafts; **human** domain experts validate and refine. |
| **Feature decomposition** | Agents can suggest feature breakdowns from requirements; **human** chief programmer validates granularity. |
| **Build by feature** | Agents can scaffold feature implementations; **class owners** review for domain model consistency. |

---

## Further reading

- [Wikipedia — Feature-driven development](https://en.wikipedia.org/wiki/Feature-driven_development) — **Overview**.
- Companion: [Scrum](scrum.md), [XP](xp.md), [Agile umbrella](agile.md)
