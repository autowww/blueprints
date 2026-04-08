---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Methodologies (lenses on the tracking foundation)

<!-- Copy to repo `sdlc/`: links use `../blueprints/sdlc/…` from that location. -->

**Purpose:** describe how **Scrum**, **Kanban**, **phased (Waterfall-style) delivery**, and **XP** use the **same** foundation defined in [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md). This file is about **process fit** and **ceremony support**, not a second data model.

**Handbook (browser):** [`../blueprints/sdlc/docs/methodologies.html`](../blueprints/sdlc/docs/methodologies.html) — hub + sub-chapters.

**Blueprint deep guides:** [`../blueprints/sdlc/methodologies/README.md`](../blueprints/sdlc/methodologies/README.md) — full methodology write-ups + external links + agentic SDLC.

**Ceremony intent model (blueprint):** [`../blueprints/sdlc/methodologies/ceremonies/README.md`](../blueprints/sdlc/methodologies/ceremonies/README.md) — neutral **C1–C6** + Scrum/Kanban/phased/XP **forks**; this file stays **how ceremonies consume aggregates** on the tracking spine.

**Foundation:** [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md) · **Challenges / limits:** [`TRACKING-CHALLENGES.md`](TRACKING-CHALLENGES.md)

---

## Shared idea

Each methodology **configures**:

- **Time windows** (sprint, cadence, phase, or continuous),
- **What “done” means** for reporting (often via the work tracker, not git alone),
- **Which ceremonies** consume which aggregates.

The foundation still answers only: **contributor → events → work units** (within **scope**). Methodology docs below say **what to layer on** for planning and rituals.

---

## Scrum

**Intent:** predictable iterations, shared commitment, inspect-and-adapt on a fixed cadence.

| Layer on foundation | Use |
|---------------------|-----|
| **Sprint window** | Date range (start/end) filters events and completed work units for burndown-style views and sprint review. |
| **Sprint backlog linkage** | Work units tagged as “in sprint” in the tracker; foundation joins commits to those ids — not inferred from git alone. |
| **Ceremonies** | **Planning:** capacity often needs **story points or hours** outside git. **Daily:** “yesterday/today” from **closed/open** work units + recent commits. **Review:** **done** items + merged work. **Retro:** throughput and themes; see [challenges](TRACKING-CHALLENGES.md#scrum-oriented-challenges). |

**Add-on configuration (non-foundation):** sprint calendar, definition of done, optionally team capacity from the ALM tool.

---

## Kanban

**Intent:** flow, WIP limits, continuous delivery; optimize cycle time over batch planning.

| Layer on foundation | Use |
|---------------------|-----|
| **Continuous or rolling window** | Less emphasis on fixed sprints; reports use trailing N days or release cadence. |
| **Board / column metadata** | **WIP and queue time** need **tracker state** (or snapshots); git shows **activity**, not waiting. |
| **Ceremonies** | **Standup:** blockers + aging work units. **Replenishment / review:** throughput and **cycle time** — best when **created → done** comes from the board; “first commit → merge” is a rough proxy. |

**Add-on configuration:** column map, WIP limits, policies for ready/done; optional service classes.

---

## Phased delivery (Waterfall-style)

**Intent:** sequential phases (e.g. requirements → design → build → verify) with **gates** and **baselines**.

| Layer on foundation | Use |
|---------------------|-----|
| **Phase labels on work units** | Commits link to REQs or phase-tagged items; **which phase** is metadata on the work unit or path, not guessed only from file folder. |
| **Milestone windows** | Date ranges for “requirements freeze,” “UAT,” etc., filter events for **phase touch** and traceability reports. |
| **Ceremonies** | **Phase exit / tollgates:** often need **sign-offs and documents outside git**; foundation supplies **engineering activity** and linkage, not the approval record itself. |

**Add-on configuration:** phase taxonomy, milestone dates, REQ ↔ phase mapping; compliance store for formal artifacts.

---

## Extreme Programming (XP)

**Intent:** technical excellence, small releases, feedback — practices more than a board shape.

| Layer on foundation | Use |
|---------------------|-----|
| **Small batch signal** | Commit size/frequency and **short-lived branches** (if measured) support “small releases” narratives — interpret with care (see [challenges](TRACKING-CHALLENGES.md#xp-oriented-challenges)). |
| **Pairing / ensemble** | **`Co-authored-by:`** trailers (or explicit events) attribute touch beyond a single email. |
| **Quality** | CI/test results are a **parallel stream** correlated by commit or PR — not redefined as “contributor” in the foundation. |
| **Ceremonies** | **Planning game, small releases, retros** benefit from **done work units** + quality trends, not raw commit counts. |

**Add-on configuration:** pairing conventions, CI dashboards, definition of “green.”

---

## Agile (umbrella)

**Agile** is values and principles (collaboration, feedback, working software), not a separate tracking stack. In practice teams combine **Scrum or Kanban** (cadence) with **XP practices** (TDD, CI, pairing). The foundation stays one; **pick the methodology rows above** that match your actual rituals.

---

## Summary

| Methodology | Foundation uses | Typical extra inputs (not duplicate foundations) |
|-------------|-----------------|-----------------------------------------------|
| **Scrum** | Same events + work units | Sprint dates, backlog membership, capacity from ALM |
| **Kanban** | Same | Board columns, blockers, created/done from tracker |
| **Phased** | Same | Phase tags, milestones, REQ map; gates in compliance/ALM |
| **XP** | Same | Co-author/CI/test correlation, team norms |

When something is **hard or misleading**, it is documented in [`TRACKING-CHALLENGES.md`](TRACKING-CHALLENGES.md), not hidden inside the foundation.
