---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Disciplined Agile (DA)

## What it is

**Disciplined Agile (DA)** is a **process-decision toolkit** originally developed by Scott Ambler and Mark Lines, now owned by the **Project Management Institute (PMI)**. Rather than prescribing a single process, DA provides a **goal-driven** approach: it presents **process goals** (e.g. "Explore Scope," "Address Changing Stakeholder Needs") and offers **decision points** with multiple **options** drawn from Scrum, Kanban, XP, Lean, SAFe, and other sources.

DA is designed for organizations that want **guided choice** rather than a single mandated framework. It covers the full delivery lifecycle and extends into **Disciplined Agile Enterprise (DAE)** for organizational transformation.

## Process diagram (handbook)

![DA — goal-driven process decision](../docs/assets/methodology-da-goals.svg)

*Process goals → decision points → options (from multiple frameworks). Teams choose options based on context.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**PMI — Disciplined Agile**](https://www.pmi.org/disciplined-agile) | **Official** DA body of knowledge — goal diagrams, lifecycles, and process options (PMI-owned). |
| [Wikipedia — Disciplined agile delivery](https://en.wikipedia.org/wiki/Disciplined_agile_delivery) | **Stable overview** of DA's approach, lifecycles, and relationship to other Agile methods. |

---

## Core concepts

| Concept | Meaning |
|---------|---------|
| **Process goals** | Named outcomes a team should achieve (e.g. "Produce a Potentially Consumable Solution"). |
| **Decision points** | Within each goal, choices the team must make (e.g. "How will we coordinate work?"). |
| **Options** | Concrete practices drawn from Scrum, Kanban, XP, Lean, SAFe, etc. that satisfy a decision point. |
| **Context** | Team size, regulatory environment, organizational culture — what makes one option better than another. |
| **Lifecycles** | DA offers multiple lifecycle templates: Agile (Scrum-based), Lean (Kanban-based), Continuous Delivery, Exploratory (Lean Startup), and Program (for large efforts). |

---

## DA lifecycles

| Lifecycle | Based on | When to use |
|-----------|----------|-------------|
| **Agile** | Scrum | Iteration-based delivery; most common starting point |
| **Lean** | Kanban | Flow-based delivery; variable demand |
| **Continuous Delivery** | DevOps + Lean | Continuous deployment; mature CI/CD |
| **Exploratory** | Lean Startup | New products; hypothesis-driven; build-measure-learn |
| **Program** | SAFe-like coordination | Multiple teams; coordinated delivery |

---

## Mapping to this blueprint's SDLC

| DA idea | Blueprint touchpoint |
|---------|----------------------|
| Process goals | Phases A–F: each phase has implicit process goals that DA makes explicit. |
| Decision points | Methodology selection: DA formalizes the choices this blueprint leaves to teams. |
| Options from multiple frameworks | The methodology guides in this blueprint (Scrum, Kanban, XP, etc.) are DA "options." |
| Context-driven selection | The "choosing a primary rhythm" table in [`agile.md`](agile.md) is a simplified DA decision. |

---

## DA vs SAFe

| Dimension | DA | SAFe |
|-----------|-----|------|
| Approach | Toolkit of options; guided choice | Prescribed framework; configurations |
| Prescription level | Low — teams select from options | High — roles, events, artifacts defined |
| Scaling | Covers team to enterprise; lighter touch | Strong multi-team coordination (ART, PI Planning) |
| Ownership | PMI | Scaled Agile, Inc. |
| Best fit | Orgs wanting flexibility with guidance | Orgs wanting structured multi-team alignment |

---

## Agentic SDLC: DA + agents

| Topic | Guidance |
|-------|----------|
| **Process selection** | Agents can analyze team context (size, domain, maturity) and suggest DA options. **Humans** make the process decisions. |
| **Goal tracking** | DA's explicit process goals are useful for agentic audit: has the team addressed each goal this cycle? |
| **Multi-framework** | DA's multi-framework nature means agents working with DA teams must understand **which** practices were selected, not assume Scrum defaults. |

---

## Further reading

- [PMI — Disciplined Agile](https://www.pmi.org/disciplined-agile) — **Official** toolkit.
- [Wikipedia — Disciplined agile delivery](https://en.wikipedia.org/wiki/Disciplined_agile_delivery) — **Overview**.
- Companion: [SAFe](safe.md), [Scrum](scrum.md), [Kanban](kanban.md), [Agile umbrella](agile.md)
