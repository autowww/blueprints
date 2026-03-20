# Tracking foundation (single spine)

<!-- Copy to repo `sdlc/`: handbook link uses `../blueprints/sdlc/docs/…` from that location. -->

## Document map

| Chapter | File | Contents |
|---------|------|----------|
| **Foundation** (this file) | `TRACKING-FOUNDATION.md` | Stable model: identity, work units, events, aggregates. |
| **Methodologies** | [`TRACKING-METHODOLOGIES.md`](TRACKING-METHODOLOGIES.md) | How Scrum, Kanban, phased delivery, and XP **use** the same foundation (lenses, ceremonies, add-ons). |
| **Challenges** | [`TRACKING-CHALLENGES.md`](TRACKING-CHALLENGES.md) | Limits, risks, and misleading signals — kept separate so the foundation stays honest. |

---

## Purpose

The **foundation** is one minimal, methodology-neutral model for answering:

- **Who** contributed (stable identity, usually derived from git `user.email`).
- **What** changed (events, primarily commits).
- **Which work** it relates to (issues, REQs, tickets — **work units**).
- **Where** it applies (repo, product line, or **scope**).

Scrum, Kanban, phased (Waterfall-style) delivery, and Extreme Programming (XP) all **reuse this spine**. They differ in **cadence, rules, and ceremonies**, not in redefining “contributor” or “event” in parallel systems.

---

## Principles

1. **One pipeline** — Normalize identity once; ingest events once; link to work units once. Methodology-specific views are **filters and configuration**, not duplicate stores.
2. **Git-friendly, not git-only** — Commits are the usual first signal. Blockers, reviews, or manual time may appear as **additional event types** in the same stream when ceremonies need them.
3. **Ceremony outputs are derived** — Standups, sprint reviews, replenishment, and phase reviews consume **generated reports**. Reports do not become the source of truth for identity or work units.
4. **Reproducibility** — Where possible, aggregates should be **rebuildable** from `git log` plus declared conventions and optional sidecar inputs (so numbers are explainable).

---

## Core concepts

| Concept | Definition |
|--------|------------|
| **Contributor** | Stable id for a person (or bot policy). Primary input: **normalized** git author email (`trim`, lower-case); optional **alias map** merges multiple addresses (e.g. personal vs work) into one `contributor_id`. |
| **Work unit** | The smallest item you trace and roll up to: issue key, REQ id, ticket reference. Identifiers come from **commit message conventions** (`Fixes #12`, `Refs REQ-004`) and/or enrichment from a tracker API. |
| **Event** | A timestamped fact. **Primary type:** commit (hash, author email, author date, subject, body). **Optional types:** e.g. manual time entry, blocker note, review completion — same spine, explicit `event_kind`. |
| **Linkage** | Association **event → work unit** (and optionally **event → contributor** beyond git author, e.g. co-author). Unlinked events may exist; reports should treat them as **unclassified** work, not hide them. |
| **Scope** | Boundary for aggregation: repository, monorepo path prefix, or product id. Keeps unrelated workstreams from merging in one dashboard. |

---

## Lifecycle (conceptual)

```text
ingest (git log ± optional feeds)
    → normalize contributor (email + aliases)
    → parse linkage to work units (conventions / API)
    → store or project an event log
    → apply configuration windows (sprint, phase, release) — see Methodologies
    → emit aggregates and ceremony-facing artifacts
```

Nothing in this pipeline is Scrum- or Kanban-specific until **configuration** (windows, board metadata, WIP policy) is applied. That configuration is described under [Methodologies](TRACKING-METHODOLOGIES.md).

---

## What the foundation includes

- **Identity rules** — How email becomes `contributor_id`; where aliases live; how service accounts are labeled.
- **Work-unit conventions** — Documented patterns for referencing issues/REQs in commits (single source of truth in-repo).
- **Event log** — Ordered events with enough fields to recompute aggregates (commit hash, timestamps, message, optional trailers such as `Co-authored-by:`).
- **Generic aggregates** — Definitions that do not assume a methodology: e.g. commits per contributor per day, touches per work unit, first/last activity timestamps — **slices** are parameterized by date range and scope.
- **Optional extension points** — Additional `event_kind` values and joins to external systems, without forking contributor/work-unit definitions.

---

## What the foundation does not include

These belong to **process**, **tooling**, or the [Methodologies](TRACKING-METHODOLOGIES.md) chapter — not to the core schema:

- Sprint goals, backlog order, or Scrum roles.
- Column definitions, WIP limits, or replenishment policy (Kanban).
- Phase sign-off matrices, formal baselines, or compliance artifacts (phased delivery).
- Pairing rotation rules or coding-standard enforcement (XP) — though **signals** (e.g. co-author trailers) may appear as data.

The foundation also does **not**, by itself, prove **billable hours** or **performance ratings**; see [Challenges](TRACKING-CHALLENGES.md).

---

## Add-ons (configuration, not duplicate foundations)

These sit **on top** of the same data:

| Add-on | Role |
|--------|------|
| **Cadence** | Date boundaries: sprints, release trains, review milestones. |
| **Work-unit metadata** | Phase, priority, column — from tracker or from tags; joins to the work unit id. |
| **Reporting** | Human- or machine-readable outputs per ceremony (daily standup digest, sprint summary, flow snapshot, phase touch list). |

---

## Where work units meet WBS / milestones (consuming repo)

The **foundation** is generic: a **work unit** is any issue, REQ, or ticket id you link from commits. In repos that use this blueprint’s **requirements** layout, those ids usually come from **`docs/requirements/`** (or your equivalent): milestone / epic / story / task specs, **WBS**, and roadmap — **not** from `sdlc/` itself. **`sdlc/`** holds process + tracking *conventions*; **`docs/requirements/`** holds the *backlog tree*.

| What (typical) | Where (typical) |
|----------------|-----------------|
| ID scheme | `docs/requirements/STRUCTURE-PROPOSAL.md` (or your naming doc) |
| Specs & milestones | `docs/requirements/INDEX.md`, `docs/requirements/milestones/` |
| WBS rollup | `docs/requirements/WBS.md` / `WBS.csv` when used |
| Roadmap | `docs/ROADMAP.md` when used |

**Tracking** docs describe *how* to attribute commits to work units; **requirements** docs define *what* is planned and how ids are named. Link commits to ids with message conventions your team adopts.

---

## Where duration (“time”) can live — two layers

| Layer | What it is | Storage |
|-------|------------|---------|
| **Activity / touch** | Commits, PRs — **timestamps**, not duration | **Git** (+ optional generated aggregates, e.g. under `metrics/`). |
| **Explicit duration** | Logged minutes/hours per person per work item | **Not** from git alone; use an **external tool** (tracker, time product) and/or an **in-repo log** (see below). |

**External:** time entries in Jira / Linear / Harvest / etc., keyed by the same **work unit** ids as your requirements tree.

**In-repo (optional):** e.g. `metrics/time/` or `docs/metrics/time/` — CSV or **JSON Lines** with columns like `date`, `contributor_id`, `work_unit_id`, `minutes`, optional `category`, `source`. **`sdlc/`** can hold **conventions** only; raw daily files may live elsewhere to avoid noise. **Aggregates** should be generated, not hand-edited. Sensitive data: **`.gitignore`** or keep duration off-repo.

---

## Related reading

- **How each methodology uses this model:** [`TRACKING-METHODOLOGIES.md`](TRACKING-METHODOLOGIES.md)
- **What is hard or easy to get wrong:** [`TRACKING-CHALLENGES.md`](TRACKING-CHALLENGES.md)
- **HTML handbook (condensed hierarchy + lenses):** [`../blueprints/sdlc/docs/methodologies.html`](../blueprints/sdlc/docs/methodologies.html)
