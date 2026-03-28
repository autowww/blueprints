# Work breakdown structure — Blueprints framework (M1)

<!--
  Product Spark F1 — Adoption spine v1.
  See docs/product/plans/mvp-adoption-spine.md and docs/ROADMAP.md.
-->

## 1. Overview

| Field | Detail |
|-------|--------|
| **Product / initiative** | Blueprints (`autowww/blueprints`) — framework product |
| **Product Spark / Milestone** | F1 / M1 — Adoption spine v1 |
| **Delivery approach** | MVP |
| **Owner** | Maintainers |
| **Date** | 2026-03-27 |
| **Status** | Draft |

---

## 2. Themes

| Theme ID | Theme | Strategic objective |
|----------|-------|---------------------|
| T1 | **Clarity** | Adopters understand category, ICP, and first steps |
| T2 | **Execution hygiene** | Maintainers track work against roadmap + MVP exit |

---

## 3. WBS hierarchy

### Theme: T1 — Clarity

#### Epic: M1E1 — Positioning & category narrative

| Story ID | Story | Acceptance criteria (summary) | Priority | Estimate | Dependencies |
|----------|-------|------------------------------|----------|----------|----------------|
| M1E1S1 | Publish positioning + MVP rationale doc | `docs/product/discovery/framework-positioning-and-mvp.md` on `main`; linked from INDEX + ADOPTION | High | S | — |
| M1E1S2 | Validate positioning with one external signal | Add “Evidence” subsection or issue link in positioning doc | Medium | S | M1E1S1 |

#### Epic: M1E2 — Adoption path & repo entry points

| Story ID | Story | Acceptance criteria (summary) | Priority | Estimate | Dependencies |
|----------|-------|------------------------------|----------|----------|----------------|
| M1E2S1 | Adoption quickstart | `docs/ADOPTION.md` with ICP A/B/C; links to templates and POLICY | High | S | — |
| M1E2S2 | README maintainer/adopter links | Root README section points to `docs/ROADMAP.md`, `docs/ADOPTION.md`, `docs/INDEX.md` | High | S | M1E2S1 |
| M1E2S3 | Docs index | `docs/INDEX.md` lists roadmap, adoption, product docs, WBS | Medium | S | — |

### Theme: T2 — Execution hygiene

#### Epic: M1E3 — WBS execution & MVP exit

| Story ID | Story | Acceptance criteria (summary) | Priority | Estimate | Dependencies |
|----------|-------|------------------------------|----------|----------|----------------|
| M1E3S1 | Roadmap live | `docs/ROADMAP.md` with M1/M2/M3 and NOW/NEXT/LATER | High | S | — |
| M1E3S2 | MVP plan baselined | `docs/product/plans/mvp-adoption-spine.md` matches scope; Assay checklist tracked | High | S | M1E3S1 |
| M1E3S3 | Close F1 Assay Gate | Spike close + WBS statuses updated; deferrals documented | High | M | M1E1S1, M1E2S2, M1E3S2 |

**Tasks** (optional decomposition):

| Task ID | Task | Story | Phase prefix | Estimate (hrs) |
|---------|------|-------|--------------|------------------|
| M1E1S1T1 | Author positioning sections 1–5 | M1E1S1 | `specify:` | 2 |
| M1E2S2T1 | Edit README — maintainer section | M1E2S2 | `release:` | 0.5 |

---

## 4. Estimation summary

| Level | Count |
|-------|-------|
| Themes | 2 |
| Epics | 3 |
| Stories | 8 |

*(Estimates: S ≈ under half a day, M ≈ about one day for a single maintainer.)*

---

## 5. Status legend

| Status | Meaning |
|--------|---------|
| done | Merged / satisfied |
| in progress | Active |
| not started | Backlog |

Update this table as stories complete:

| Story ID | Status |
|----------|--------|
| M1E1S1 | done |
| M1E1S2 | not started |
| M1E2S1 | done |
| M1E2S2 | done |
| M1E2S3 | done |
| M1E3S1 | done |
| M1E3S2 | done |
| M1E3S3 | not started |
