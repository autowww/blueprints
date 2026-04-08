---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Tracking challenges (separate from the foundation)

**Purpose:** document what is *hard*, misleading, or politically sensitive about engineering tracking — without bloating [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md). The foundation stays small; this file holds the nuance.

| Doc | Role |
|-----|------|
| [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md) | Stable model (identity, events, work units). |
| [`TRACKING-METHODOLOGIES.md`](TRACKING-METHODOLOGIES.md) | Scrum, Kanban, phased, XP — how each uses the foundation. |
| **This file** | Limits and tensions — cross-cutting and per methodology. |

---

## Cross-cutting challenges

| Challenge | Why it matters |
|-----------|----------------|
| **Commit time ≠ work time** | Commits are a *touch* proxy, not duration. Capacity and “hours per role” need other data sources if decisions depend on them. |
| **One email ≠ one person** | Shared machines, multiple addresses, contractors — alias maps and policy reduce confusion; they don’t eliminate it. |
| **Metric gaming** | Any visible aggregate (commit count, LOC) can be gamed. Prefer **work-unit completion** and qualitative review over raw volume. |
| **Rebuild vs source of truth** | If aggregates are regenerated from git, history is honest but **branch strategy** and **squash merges** change narratives; document conventions. |
| **Privacy & HR** | Attribution can approach performance surveillance. Scope reporting to **team/process improvement** unless policy explicitly allows individual management use. |

---

## Scrum-oriented challenges

| Challenge | Notes |
|-----------|--------|
| **Sprint commitment vs emergent work** | Commits alone don’t show carry-over or scope change; the **board** or sprint backlog is still the source of truth for “what we promised.” |
| **Capacity** | Story points or hours in planning are not inferrable from git; foundation only supports **proxies** unless you log time or points elsewhere and join by work unit. |
| **Ceremony prep** | Review decks need **outcomes** (done items), not only activity; link events to **closed** work units, not open churn. |

---

## Kanban-oriented challenges

| Challenge | Notes |
|-----------|--------|
| **Waiting time is invisible in git** | Blocked work often produces **fewer** commits; flow metrics that ignore blockers look “healthy” when the team is stuck. |
| **WIP limits** | Git doesn’t know column WIP; you need **board state** (API or manual snapshots) or accept weak proxies. |
| **Cycle time** | “First commit to merge” is a rough proxy; **true** cycle time usually needs **created → done** from the tracker. |

---

## Phased / Waterfall-oriented challenges

| Challenge | Notes |
|-----------|--------|
| **Gates and approvals** | Sign-offs, hazard analysis, formal baselines are often **outside** git. The foundation tracks **engineering touch**; compliance lives in controlled artifacts or ALM tools. |
| **Phase attribution** | Same commit might touch “implementation” while actually fixing a **requirements** doc; **path or REQ metadata** must classify work units, not only file paths. |
| **Variance to plan** | Planned effort vs actual **hours** is not in git; phase reviews still need planned baselines from project data. |

---

## XP-oriented challenges

| Challenge | Notes |
|-----------|--------|
| **Pairing** | Invisible unless you use `Co-authored-by`, pairing tools, or explicit events. |
| **TDD / quality** | Test commits and CI results are **orthogonal** to the identity + work-unit spine; correlate in a **quality** stream, not by overloading “commit.” |
| **Sustainable pace** | Activity spikes don’t show burnout; don’t infer well-being from graphs. |

---

## When to extend the foundation (without forking it)

- Add **event types** (e.g. `blocker_recorded`, `review_completed`) when ceremonies **repeatedly** lack signal.
- Add **external joins** (tracker API) when a framework’s core metric **cannot** be approximated from git alone.

---

## Review

Revisit this file when:

- methodology changes (e.g. Scrum → Kanban),
- someone proposes a **new KPI**,
- compliance or HR asks for individual attribution.

---

*Foundation:* [`TRACKING-FOUNDATION.md`](TRACKING-FOUNDATION.md) · *Methodologies:* [`TRACKING-METHODOLOGIES.md`](TRACKING-METHODOLOGIES.md)
