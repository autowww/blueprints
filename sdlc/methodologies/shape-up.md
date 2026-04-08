---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Shape Up

## What it is

**Shape Up** is a product development methodology created at **Basecamp** (published 2019 by Ryan Singer). It structures work in **six-week cycles** with a **two-week cooldown** between them. Work is "shaped" (scoped and de-risked) by senior people **before** it enters a cycle, then given to small teams with **full autonomy** to execute within the fixed time appetite.

Shape Up rejects both the open-ended nature of Scrum backlogs and the predictive planning of Waterfall. Instead, it uses **appetites** (how much time the work deserves) rather than estimates (how much time it will take), and **betting tables** rather than prioritized backlogs.

## Process diagram (handbook)

![Shape Up — shaping, betting, building](../docs/assets/methodology-shapeup-cycle.svg)

*Shape (senior staff) → Bet (betting table) → Build (small team, 6 weeks). Cooldown between cycles for cleanup, exploration, and pitching.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Shape Up (free book)**](https://basecamp.com/shapeup) | **Official** book by Ryan Singer — full methodology description, free online. |
| [Wikipedia — Shape Up (software development)](https://en.wikipedia.org/wiki/Shape_Up_(software_development)) | **Short overview** of the methodology and its origin at Basecamp. |

---

## Core concepts

| Concept | Meaning |
|---------|---------|
| **Appetite** | How much time the work **deserves** (not how long it will take). Fixed at 6 weeks (big batch) or 2 weeks (small batch). |
| **Shaping** | Senior staff define the problem, sketch a solution at the right level of abstraction, and identify **rabbit holes** (risks). |
| **Pitch** | A shaped proposal: problem, appetite, solution sketch, rabbit holes, no-gos. |
| **Betting table** | Leadership selects pitches for the next cycle. No backlog — unbetted pitches are gone unless re-pitched. |
| **Hill chart** | Progress visualization: uphill (figuring things out) → downhill (executing). Replaces percentage-complete tracking. |
| **Scope hammering** | Cut scope to fit the appetite, not extend the deadline to fit the scope. |
| **Cooldown** | Two weeks between cycles for bug fixes, exploration, technical debt, and preparing next pitches. |

---

## Mapping to this blueprint's SDLC

| Shape Up idea | Blueprint touchpoint |
|---------------|----------------------|
| Shaping | Phase A–B: discovery, specification — but done by senior staff, not the whole team. |
| Betting table | Phase B: planning, commitment — replaces backlog grooming with a binary bet. |
| Building | Phase C–D: build and verify — small team with full autonomy for 6 weeks. |
| Hill charts | Phase C–D: progress tracking — replaces velocity/burndown. |
| Cooldown | Phase F: learn, clean up, explore — dedicated space between cycles. |

---

## Roles (Shape Up-specific)

| Role | Responsibility |
|------|----------------|
| **Shaper** | Defines the problem and solution at the right abstraction level; identifies risks. Senior designer/strategist. |
| **Bettor** | Selects pitches for the cycle. Usually senior leadership or product team. |
| **Builder** | Small team (1 designer + 1–2 programmers) with full autonomy during the cycle. |

---

## Shape Up vs Scrum

| Dimension | Shape Up | Scrum |
|-----------|----------|-------|
| Cycle length | 6 weeks (fixed) | 1–4 weeks (Sprint) |
| Backlog | No persistent backlog; pitches expire | Ordered Product Backlog |
| Estimation | Appetite (time budget) | Story points or hours |
| Progress | Hill charts | Sprint burndown |
| Scope | Hammered to fit appetite | Negotiated per Sprint |
| Team autonomy | Full (no daily standup required) | Self-managing within Sprint framework |

---

## Agentic SDLC: Shape Up + agents

| Topic | Guidance |
|-------|----------|
| **Shaping** | Agents can research prior art, generate solution sketches, and surface rabbit holes from codebase analysis. **Shapers** make the final scoping decisions. |
| **Building** | Small autonomous teams benefit from agents for rapid prototyping within the 6-week appetite. Ensure review keeps pace. |
| **Hill charts** | Agents can contribute to "downhill" execution but the "uphill" (figuring things out) is fundamentally human. |

---

## Further reading

- [Shape Up — free book](https://basecamp.com/shapeup) — **Complete** methodology.
- Companion: [Scrum](scrum.md), [Kanban](kanban.md), [Agile umbrella](agile.md)
