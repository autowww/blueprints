# Ceremony intents — SDD I/O (C1–C6)

**Purpose:** Full **Spec-driven development (SDD)** specifications for each **foundation ceremony intent** from [`ceremony-foundation.md`](../ceremonies/ceremony-foundation.md). Use for **calibration** with your rituals or as **copy-paste** starters (see [`../../templates/sdd/CEREMONY-INTENT.template.md`](../../templates/sdd/CEREMONY-INTENT.template.md)).

**Handbook:** [Ceremonies (SDD I/O)](../../docs/spec-driven-sdd-ceremonies.html)

---

## C1 — Align on intent

### SDD metadata

| Field | Value |
|-------|-------|
| `sdd_id` | `SDD-C1-ALIGN` |
| `kind` | `ceremony_intent` |
| `maps_to.ceremony_intents` | `C1` |
| `maps_to.sdlc_phases` | Strong: A, B |

### Summary

Produce **shared understanding** of goals, scope, and constraints for a **horizon** (release train, increment, phase, or next pull of work) **before** commitment (C2).

### Preconditions

| ID | Artifact | Format | Owner | Ready when |
|----|----------|--------|-------|------------|
| PRE-C1-1 | Stakeholder themes / problems | Doc or backlog labels | Demand | At least 3 prioritized themes or one ranked backlog |
| PRE-C1-2 | Constraints register (time, compliance, tech) | Doc / wiki / ADR list | Steer / Tech | Known “must not” and “must” stated |
| PRE-C1-3 | Horizon label | Calendar or version | Demand | Named (e.g. “2026-Q2”, “M2”, “Sprint 12”) |

### Inputs

| ID | Name | Type | Source | Format | Example (snippet) |
|----|------|------|--------|--------|-------------------|
| IN-C1-1 | Current product goal | Narrative | Demand | 1 paragraph | “Become default mobile capture for field notes in EU SMB.” |
| IN-C1-2 | Candidate scope list | Backlog / epic list | Demand + Build | Tracker IDs | `M2E1`, `M2E3`, `M2E5` |
| IN-C1-3 | Dependency assumptions | Table | Build | Markdown | “OCR service GA depends on vendor API v3 by March 1.” |

### Outputs

| ID | Name | Type | Consumer | Storage | Example (snippet) |
|----|------|------|----------|---------|-------------------|
| OUT-C1-1 | Aligned goal statement | Decision text | C2, C4 | `docs/product/` or milestone `milestone.md` | “M2 delivers offline capture + sync conflict UI; no new integrations.” |
| OUT-C1-2 | Explicit non-goals | List | All delivery | Same doc | “No desktop editor; no SSO beyond Google.” |
| OUT-C1-3 | Open questions / spikes | List with owner | Build | Issues or `story.md` drafts | “SPIKE-1: quota behavior under airplane mode — @alex, due before planning.” |

### Postconditions

- [ ] Stakeholders can **repeat the goal** in one sentence without slides.
- [ ] **Non-goals** are written, not only implied.
- [ ] Every **open question** has an owner and deadline before C2.

### Participants (typical)

| Archetype | R / A / C / I |
|-----------|---------------|
| Demand & value | **A** (outcome), **R** (message) |
| Build & integrate | **C** (feasibility), **R** (dependencies) |
| Steer | **C** (constraints) |

### Filled example — “Horizon M2 kickoff”

| Step | Instance |
|------|----------|
| PRE satisfied | `M2/milestone.md` draft exists; compliance: GDPR retention unchanged. |
| IN | Themes: offline, sync conflicts, share sheet. |
| OUT goal | “M2 ships offline read/write and conflict resolution UX; exports unchanged.” |
| OUT non-goals | “No team workspaces; no billing changes.” |
| OUT questions | “Conflict merge policy for binary attachments — PO + tech spike by Jan 15.” |

---

## C2 — Commit / select work

### SDD metadata

| Field | Value |
|-------|-------|
| `sdd_id` | `SDD-C2-COMMIT` |
| `kind` | `ceremony_intent` |
| `maps_to.ceremony_intents` | `C2` |
| `maps_to.methodology_events` | Sprint Planning (Part 2), replenishment, iteration planning |

### Summary

**Explicit choice** of work entering the next **execution slice** (sprint backlog, WIP slots, phase entry) with **capacity** visible.

### Preconditions

| ID | Artifact | Owner | Ready when |
|----|----------|-------|------------|
| PRE-C2-1 | C1 outputs (goal, non-goals) | Demand | Goal statement merged to canonical doc |
| PRE-C2-2 | Refined backlog items | Team | Top N items meet Definition of Ready |
| PRE-C2-3 | Capacity signal | Build | People-days or points available for horizon |

### Inputs

| ID | Name | Example (snippet) |
|----|------|-------------------|
| IN-C2-1 | Ordered candidate items | `M2E1S1`, `M2E1S2`, `M2E3S1` |
| IN-C2-2 | Historical throughput | “Team completes ~8 stories/sprint (median).” |
| IN-C2-3 | Dependency status | “API v3 dependency green as of Jan 10.” |

### Outputs

| ID | Name | Consumer | Storage | Example |
|----|------|----------|---------|---------|
| OUT-C2-1 | Committed item set | Build | Sprint backlog / board column | `M2E1S1`, `M2E1S2` only |
| OUT-C2-2 | Forecast narrative | Demand, Steer | Sprint goal field or `sprint-note.md` | “Finish offline MVP + conflict modal; defer share sheet to M3.” |
| OUT-C2-3 | Deferred items with reason | Flow | Backlog comments | “M2E3S1 deferred: waiting on SPIKE-1.” |

### Postconditions

- [ ] **WIP/sprint boundary** visible on board or tracker.
- [ ] **Deferred** work has a **reason** visible to the team.
- [ ] Each committed item has a **work-unit ID** for commits.

### Filled example

Committed: `M2E1S1`, `M2E1S2`. Sprint goal: “Offline MVP + conflict modal.” Deferred: `M2E3S1` (spike incomplete). Recorded in GitHub Sprint field + `docs/requirements/WBS.md` status.

---

## C3 — Sync progress

### SDD metadata

| `sdd_id` | `SDD-C3-SYNC` |
| `maps_to` | C3; phases C–E strong |

### Summary

**Coordinate** execution, **surface blockers**, adjust plan within the committed slice without losing transparency.

### Preconditions

| ID | Artifact | Ready when |
|----|----------|------------|
| PRE-C3-1 | Committed slice (C2) | Items in progress or ready column |
| PRE-C3-2 | Board / tracker truth | Updated EOD prior or start of sync |

### Inputs

| ID | Name | Example |
|----|------|---------|
| IN-C3-1 | Per-item state | “S1: in review; S2: blocked on API mock.” |
| IN-C3-2 | Impediments list | “CI flaky on module X — 2 days.” |

### Outputs

| ID | Name | Example |
|----|------|---------|
| OUT-C3-1 | Updated plan for next interval | “S2 parking lot; S1 merge today; pair on mock.” |
| OUT-C3-2 | Escalations | “Steer informed: vendor SLA miss — decision by Thu.” |
| OUT-C3-3 | Board update | Columns reflect agreed WIP |

### Postconditions

- [ ] **Blocker** has owner and **time-bound** next step.
- [ ] No **silent** carry of impossible WIP.

### Filled example

Daily: `M2E1S2` blocked on OAuth scope — SM escalates to Steer; `M2E1S1` merged; board updated; today focus: unblock S2 or swap scope per PO decision documented in issue #204.

---

## C4 — Inspect outcome

### SDD metadata

| `sdd_id` | `SDD-C4-INSPECT` |
| `maps_to` | C4; Review, demo, UAT slice |

### Summary

**Compare** delivered work to **acceptance**; capture **stakeholder feedback** as input to backlog (C1/C2 next cycle).

### Preconditions

| ID | Artifact | Ready when |
|----|----------|------------|
| PRE-C4-1 | Done increment per DoD | CI green; demo env available |
| PRE-C4-2 | Acceptance criteria visible | Linked from story specs |

### Inputs

| ID | Name | Example |
|----|------|---------|
| IN-C4-1 | Demo script / walkthrough | “1) airplane mode 2) edit 3) conflict” |
| IN-C4-2 | Story AC checklist | From `M2E1S1/story.md` |

### Outputs

| ID | Name | Consumer | Example |
|----|------|----------|---------|
| OUT-C4-1 | Accept / defer / change list | Demand | “AC3 deferred: export format — new story `M2E5S1`.” |
| OUT-C4-2 | Backlog updates | Flow / Demand | Priorities and new items filed |
| OUT-C4-3 | Recording / notes | Audit | `notes/2026-01-20-review.md` |

### Postconditions

- [ ] Stakeholders **saw working software** (when product is software).
- [ ] Feedback **traceable** to backlog items or explicit “won’t do.”

### Filled example

Review notes: AC1–2 accepted; AC3 split to `M2E5S1`; PO reordered backlog; notes committed under `docs/requirements/milestones/M2/notes/2026-01-20-review.md`.

---

## C5 — Improve the system

### SDD metadata

| `sdd_id` | `SDD-C5-IMPROVE` |
| `maps_to` | C5; retrospective |

### Summary

**Inspect and adapt** how the team works (process, tools, collaboration)—**not** product backlog ordering.

### Preconditions

| ID | Artifact | Ready when |
|----|----------|------------|
| PRE-C5-1 | Safe context | Facilitator agreed; Chatham House if needed |
| PRE-C5-2 | Data from horizon | Incidents, retro themes, CI stats optional |

### Inputs

| ID | Name | Example |
|----|------|---------|
| IN-C5-1 | Timeline of pain points | “Reviews >24h; agent PRs noisy.” |
| IN-C5-2 | Previous retro experiments | “Smaller PRs — partial success.” |

### Outputs

| ID | Name | Example |
|----|------|---------|
| OUT-C5-1 | 1–3 experiments with owners | “Cap agent PRs at 200 LOC — tech lead.” |
| OUT-C5-2 | Retro log | `sdlc/retro-log.md` or wiki page dated |

### Postconditions

- [ ] **Experiments** are **measurable** and **time-boxed**.
- [ ] **Product decisions** are parked for C1/C2, not buried in retro.

### Filled example

Experiments: (1) Review SLA 24h for `main` with calendar block; (2) Link every agent PR to `sdd_id` in description. Logged in `sdlc/retro/2026-01-21.md`.

---

## C6 — Assure / release

### SDD metadata

| `sdd_id` | `SDD-C6-ASSURE` |
| `maps_to` | C6; release train, go/no-go, DoD gate |

### Summary

**Evidence** and **decisions** that work is fit to **ship** or **pass gate** (DoD, compliance, ops readiness).

### Preconditions

| ID | Artifact | Ready when |
|----|----------|------------|
| PRE-C6-1 | Release candidate build | Versioned artifact in registry |
| PRE-C6-2 | Test evidence | Test plan / CI report linked |
| PRE-C6-3 | Checklist template | Release checklist exists |

### Inputs

| ID | Name | Example |
|----|------|---------|
| IN-C6-1 | DoD checklist per story | All `M2E1S*` marked done in WBS |
| IN-C6-2 | Security / privacy sign-off | “OWASP deps scan clean; DPIA unchanged.” |
| IN-C6-3 | Rollback plan | “Feature flag `offline_mode` default off.” |

### Outputs

| ID | Name | Example |
|----|------|---------|
| OUT-C6-1 | Go / no-go / conditional go | “Go with flag; marketing holds blog.” |
| OUT-C6-2 | Release notes | `CHANGELOG.md` + Play Store text |
| OUT-C6-3 | Deployment record | Tag `v1.4.0`, pipeline run id |

### Postconditions

- [ ] **Decision** recorded with **approver identity** and **timestamp**.
- [ ] **Version** immutable and traceable to commits.

### Filled example

Go: `v1.4.0`; notes reference `M2E1S1`, `M2E1S2`; Steer sign-off in `docs/release/M2-go.md`; CI run `4829103`.

---

## Traceability to methodology handbooks

Map your **calendar** using [`methodology-bridge.md`](../ceremonies/methodology-bridge.md) and methodology forks; this SDD layer defines **I/O contracts** independent of ritual names.
