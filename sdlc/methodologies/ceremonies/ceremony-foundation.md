# Ceremony foundation (methodology-neutral)

## Purpose

This file defines **why** recurring delivery collaboration exists in this blueprint—**without** Scrum, Kanban, or XP names. Methodology guides **map** their official events and practices **onto** these **intent types**.

**Pairs with:** [`roles-archetypes.md`](../roles-archetypes.md) (**who**), [`SDLC.md`](../../SDLC.md) Phases A–F (**what artifacts the lifecycle expects**), and (in adopting repos) [`sdlc/TRACKING-FOUNDATION.md`](../../../../sdlc/TRACKING-FOUNDATION.md) (**contributor → events → work units**).

**Forks (methodology-specific):** [Scrum](scrum.md) · [Kanban](kanban.md) · [Phased](phased.md) · [XP](xp.md) · [Index](README.md)

---

## Vocabulary

| Term | Meaning here |
|------|----------------|
| **Ceremony** | Any **recurring or gate-bound** collaboration whose job is a **clear outcome** (decision, alignment, inspection, or improvement)—**sync meeting**, **async review**, or **formal review** all count. |
| **Intent type** | A **stable label** for *what job* the ceremony does for the delivery system—not the calendar title your team uses. |
| **Foundation** | This document: **intent types** + phase/archetype mapping + principles. |
| **Methodology fork** | A file that names **official** or **common** ceremonies (e.g. Sprint Planning) and maps them to **intent types**. |
| **Cadence** | How often the pattern repeats (Sprint, week, on-demand replenishment, phase gate)—defined in the **fork**, not in the foundation. |

---

## Six ceremony intent types

Each type answers a different class of **delivery risk** (drift, surprise, quality, or stagnation).

| ID | Intent type | Job to be done (outcome) |
|----|-------------|---------------------------|
| **C1** | **Align on intent** | Shared understanding of **goals, scope, and constraints** for a horizon (release, increment, phase, or next pull of work). |
| **C2** | **Commit / select work** | Explicit **choice** of what enters the next execution slice (sprint backlog, column, phase entry, WIP slot). |
| **C3** | **Sync progress** | **Coordination** and **blocker surfacing** so work keeps moving without silent drift. |
| **C4** | **Inspect outcome** | **Compare** delivered work to expectations; **feedback** from stakeholders or governance; input to **next alignment**. |
| **C5** | **Improve the system** | **Inspect and adapt** how people work together (process, tools, relationships)—not the product backlog order. |
| **C6** | **Assure / release** | **Evidence** and **decisions** that work is fit to **proceed** or **ship** (DoD, gates, go/no-go, operational readiness). |

**Note:** A single **calendar event** (e.g. “planning”) often covers **more than one** intent—forks call that out.

---

## Intent × SDLC phases (typical touch)

Phases refer to [`SDLC.md`](../../SDLC.md) A–F. Cells show where an intent **most often** appears; your methodology may shift emphasis.

| Intent | A Discover | B Specify | C Design | D Build | E Verify | F Release |
|--------|------------|-----------|----------|---------|----------|-----------|
| **C1 Align** | ●● | ●● | ● | ● | ○ | ○ |
| **C2 Commit** | ● | ●● | ● | ●● | ○ | ○ |
| **C3 Sync** | ○ | ○ | ● | ●● | ● | ○ |
| **C4 Inspect** | ○ | ● | ● | ●● | ●● | ● |
| **C5 Improve** | ○ | ○ | ○ | ● | ● | ● |
| **C6 Assure** | ○ | ● | ● | ●● | ●● | ●● |

Legend: **●●** strong, **●** common, **○** optional / indirect.

---

## Intent × archetypes (typical facilitation)

Archetypes are defined in [`roles-archetypes.md`](../roles-archetypes.md). “Lead” means **accountable for driving the outcome**, not necessarily the only speaker.

| Intent | Typical lead archetype(s) | Often participates |
|--------|---------------------------|-------------------|
| **C1 Align** | Demand & value | Build, Steer (constraints) |
| **C2 Commit** | Demand & value + Build & integrate | Flow (facilitation) |
| **C3 Sync** | Build & integrate | Flow, Demand |
| **C4 Inspect** | Demand & value | Build, Steer, Assure |
| **C5 Improve** | Flow & improvement | All |
| **C6 Assure** | Assure & ship | Build, Demand, Steer |

---

## Principles

1. **Ceremony ≠ meeting** — The **outcome** matters; async boards, recorded reviews, or written gate packets can satisfy the **intent** if transparency and decisions are real.
2. **Foundation does not prescribe cadence** — Sprints, weekly replenishment, or phase gates live in **methodology forks** and project policy.
3. **Git is not the ceremony** — Commits support **C3/C4/C6** narratives; **Sprint Goals**, **blockers**, **acceptance**, and **sign-offs** usually need **ALM, board, or compliance** records—see [Scrum fork](scrum.md) table “What git approximates.”
4. **One pipeline for identity** — Repos using the tracking foundation keep **Contributor** in the **event stream**; ceremony attendance does not replace **work-unit linkage** in commits when that is your convention.
5. **Avoid duplicate foundations** — Do not invent parallel “ceremony taxonomies” per team; add **project** notes in `sdlc/`, not new blueprint intent types, unless you extend this file deliberately.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`roles-archetypes.md`](../roles-archetypes.md) | **Who** leads and tweaks by methodology |
| [`scrum.md`](../scrum.md) | Scrum events (source narrative) |
| [`kanban.md`](../kanban.md) | Flow, replenishment, reviews |
| [`phased-delivery.md`](../phased-delivery.md) | Gates and baselines |
| [`xp.md`](../xp.md) | Practices and rhythm |
| [`agentic-sdlc.md`](../agentic-sdlc.md) | Human vs agent in rituals |
| [Project `TRACKING-CHALLENGES`](../../../../sdlc/TRACKING-CHALLENGES.md) | Limits of commit-based proxies |
