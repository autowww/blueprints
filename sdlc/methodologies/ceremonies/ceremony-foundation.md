# Ceremony foundation (methodology-neutral)

## Purpose

This file defines **why** recurring delivery collaboration exists in this blueprint—**without** Scrum, Kanban, or XP names. Methodology guides **map** their official events and practices **onto** these **intent types**.

**Pairs with:** [`roles-archetypes.md`](../roles-archetypes.md) (**who**), [`SDLC.md`](../../SDLC.md) Phases A–F (**what artifacts the lifecycle expects**), and (in adopting repos) [`sdlc/TRACKING-FOUNDATION.md`](../../../../sdlc/TRACKING-FOUNDATION.md) (**contributor → events → work units**). **SDD I/O (inputs/outputs/examples per C1–C6):** [`spec-driven/ceremonies-sdd.md`](../spec-driven/ceremonies-sdd.md) · template [`templates/sdd/CEREMONY-INTENT.template.md`](../../templates/sdd/CEREMONY-INTENT.template.md).

**Forks (methodology-specific):** [Scrum](https://forgesdlc.com/methodology-scrum.html) · [Kanban](https://forgesdlc.com/methodology-kanban.html) · [Phased](phased.md) · [XP](https://forgesdlc.com/methodology-xp.html) · [Index](README.md)

**Bridge (intents ↔ methodology names):** [`methodology-bridge.md`](methodology-bridge.md) — crosswalk matrix, blend suggestions, how to map your calendar.

---

## Document map

| Section | Contents |
|---------|----------|
| [Vocabulary](#vocabulary) | Ceremony, intent, foundation, fork |
| [Six intent types](#six-ceremony-intent-types) | C1–C6 definitions |
| [Intent × phases](#intent--sdlc-phases-typical-touch) | A–F touch matrix |
| [Intent × archetypes](#intent--archetypes-typical-facilitation) | Who leads |
| [Practice suggestions](#practice-suggestions-by-intent) | Actionable guidance per C1–C6 |
| [Principles](#principles) | Design rules |
| [Related reading](#related-reading) | Links |

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

## Practice suggestions (by intent)

Methodology-neutral **hints** for running or replacing ceremonies. For **named** Scrum/Kanban/phased/XP rituals and per-event tips, see the [**methodology bridge**](methodology-bridge.md) and each [fork](README.md).

### C1 — Align on intent

- **Minimum viable:** Written **goal** + **out of scope** for the next horizon; one **Demand**-owned sentence stakeholders can repeat.  
- **Prefer:** Tie alignment to **measurable** outcomes or **user** stories, not only internal tasks.  
- **Avoid:** Re-aligning **only** in crisis—schedule **before** commitment (C2) breaks.  
- **Doc hook:** Update [`SDLC.md`](../../SDLC.md) Phase A–B artifacts when priorities or acceptance shift.

### C2 — Commit / select work

- **Minimum viable:** Explicit **list** of work items entering execution with **WIP** or **Sprint** boundary visible on the board/tracker.  
- **Prefer:** **Capacity** check (people, skills, dependencies)—not only PO desire.  
- **Avoid:** Silent **overflow** (everything “in progress”); forces honest **descope** or **defer**.  
- **Doc hook:** WBS/backlog **status** and **ready** criteria per Phase B.

### C3 — Sync progress

- **Minimum viable:** **Blockers** visible within 24h (board column, chat, or stand-up).  
- **Prefer:** **Dependency** ownership named (person or team), not “the org.”  
- **Avoid:** Status-only round-robin with **no** decisions or escalations—merge with **C5** if the team only vents.  
- **Doc hook:** Link **commits/PRs** to work units so sync can reference **evidence** ([`TRACKING-FOUNDATION`](../../../../sdlc/TRACKING-FOUNDATION.md)).

### C4 — Inspect outcome

- **Minimum viable:** **Demo** or **walkthrough** of **Done** work against acceptance; notes captured.  
- **Prefer:** **Stakeholders** who can say “yes / not yet / change X”—not only developers.  
- **Avoid:** **Deck-only** reviews with no running increment when software is the product.  
- **Doc hook:** Phase E exit, Phase F readiness; story **done** per [`SDLC.md`](../../SDLC.md) §3.

### C5 — Improve the system

- **Minimum viable:** **One** agreed experiment or policy tweak per cadence with **owner** and **date**.  
- **Prefer:** **Data** from board/CI/incidents—not only opinions.  
- **Avoid:** **Blame** framing; keep focus on **system** and **interfaces**.  
- **Doc hook:** Optional `sdlc/NOTES.md` or retro log in project repo.

### C6 — Assure / release

- **Minimum viable:** **Checklist** (tests, security, rollback) attached to **release** or **merge to main**.  
- **Prefer:** **Automate** repeatable checks in CI; humans for **judgment** calls.  
- **Avoid:** **Assurance** only at the end of a long branch—shift **left** per risk.  
- **Doc hook:** Phase F artifacts, `docs/release/`, CI docs per [`SDLC.md`](../../SDLC.md) §7.

---

## Principles

1. **Ceremony ≠ meeting** — The **outcome** matters; async boards, recorded reviews, or written gate packets can satisfy the **intent** if transparency and decisions are real.
2. **Foundation does not prescribe cadence** — Sprints, weekly replenishment, or phase gates live in **methodology forks** and project policy.
3. **Git is not the ceremony** — Commits support **C3/C4/C6** narratives; **Sprint Goals**, **blockers**, **acceptance**, and **sign-offs** usually need **ALM, board, or compliance** records—see [Scrum fork](https://forgesdlc.com/methodology-scrum.html) table “What git approximates.”
4. **One pipeline for identity** — Repos using the tracking foundation keep **Contributor** in the **event stream**; ceremony attendance does not replace **work-unit linkage** in commits when that is your convention.
5. **Avoid duplicate foundations** — Do not invent parallel “ceremony taxonomies” per team; add **project** notes in `sdlc/`, not new blueprint intent types, unless you extend this file deliberately.
6. **Fork cadence complements decision-triggered work** — **Methodology forks** (e.g. Forge) name **recurring** events and typical **cadence** for covering C1–C6. **Decision-triggered** sessions (e.g. discipline Versonas) address specific gates; they **complement** that cadence and are not a substitute for **core intents** such as **C3 sync** or **C5 improve** unless the team **explicitly** merges them in policy.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`methodology-bridge.md`](methodology-bridge.md) | **Crosswalk** C1–C6 ↔ Scrum/Kanban/phased/XP names |
| [`roles-archetypes.md`](../roles-archetypes.md) | **Who** leads and tweaks by methodology |
| [`scrum.md`](https://forgesdlc.com/methodology-scrum.html) | Scrum events (source narrative) |
| [`kanban.md`](https://forgesdlc.com/methodology-kanban.html) | Flow, replenishment, reviews |
| [`phased-delivery.md`](https://forgesdlc.com/methodologies-phased-delivery.html) | Gates and baselines |
| [`xp.md`](https://forgesdlc.com/methodology-xp.html) | Practices and rhythm |
| [`agentic-sdlc.md`](../agentic-sdlc.md) | Human vs agent in rituals |
| [Project `TRACKING-CHALLENGES`](../../../../sdlc/TRACKING-CHALLENGES.md) | Limits of commit-based proxies |
