# Software development lifecycle (SDLC)

This describes a **generic** delivery flow and **which documentation** to update at each step. It pairs with [`DOCUMENTATION-STRUCTURE.md`](DOCUMENTATION-STRUCTURE.md) (where files live, including the optional **milestone → epic → story → task** hierarchy in §2.1) and your project’s **own** requirements or backlog convention (where you keep epics, stories, and IDs).

**PDLC (product lifecycle):** This SDLC covers **how to build the product right** — phases A–F from requirements through release. The **Product Development Life Cycle** ([`blueprints/pdlc/`](../pdlc/README.md)) covers **building the right product** — problem discovery, solution validation, planning and commitment, go-to-market, growth, and sunset. SDLC phases A–F sit **inside** the PDLC as the Build & Release engine. See [`PDLC-SDLC-BRIDGE.md`](../pdlc/PDLC-SDLC-BRIDGE.md) for phase alignment, artifact handoffs, role mapping, and a worked example.

**Methodology depth (Scrum, Kanban, XP, phased, Lean, Spiral, V-Model, DevOps, SAFe, FDD, Crystal, DSDM, Shape Up, DA, BDD, RAD, Agile, agentic SDLC):** see [`methodologies/README.md`](methodologies/README.md) — full guides with external links and adoption notes.

**Ceremonies (foundation vs forks):** methodology-neutral **intent types** (why recurring collaboration exists) and per-methodology mappings — [`methodologies/ceremonies/README.md`](methodologies/ceremonies/README.md).

**Bridge (intents ↔ Scrum / Kanban / phased / XP names):** [`methodologies/ceremonies/methodology-bridge.md`](methodologies/ceremonies/methodology-bridge.md) — matrix, blend suggestions, calendar mapping.

**Discipline bridges:** Cross-cutting disciplines each have a bridge mapping their practices to SDLC phases A–F and PDLC P1–P6 — see [`BRIDGES.md`](../BRIDGES.md) for the full index, or jump to a specific discipline: [BA](../disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md) · [PM](../disciplines/governance/pm/PM-SDLC-PDLC-BRIDGE.md) · [Testing](../disciplines/engineering/testing/TESTING-SDLC-PDLC-BRIDGE.md) · [Architecture](../disciplines/engineering/software-architecture/ARCH-SDLC-PDLC-BRIDGE.md) · [DevOps](../disciplines/engineering/devops/DEVOPS-SDLC-PDLC-BRIDGE.md) · [Big Data](../disciplines/data/bigdata/BIGDATA-SDLC-PDLC-BRIDGE.md) · [Data Science](../disciplines/data/data-science/DS-SDLC-PDLC-BRIDGE.md).

**Path examples** below use a common `docs/` layout; adjust names if your tree differs.

---

## 1. Roles (can be one person)

| Role | Responsibility |
|------|----------------|
| **Owner** | Prioritizes **work breakdown** / backlog; accepts epic or story **done**. |
| **Implementer** | Implements work items; updates specs, backlog, and traceability as agreed below. |

**Deeper (methodology-neutral):** delivery **archetypes** (demand, build, flow, assurance, governance), how **Scrum / Kanban / phased / XP** map **titles** onto them, and how that relates to **Contributor** in engineering tracking — see [`methodologies/roles-archetypes.md`](methodologies/roles-archetypes.md).

---

## 2. Phases & documentation obligations

### Ceremony intents vs phases (C1–C6)

Recurring collaboration (**ceremonies**) should **cover** the six **intent types** over time: **C1** Align, **C2** Commit, **C3** Sync, **C4** Inspect, **C5** Improve, **C6** Assure/release — see [`methodologies/ceremonies/ceremony-foundation.md`](methodologies/ceremonies/ceremony-foundation.md). They **do not replace** the artifact tables below; they explain **why** teams hold planning, reviews, and gates.

| Phase | Intents most engaged (typical) | Illustrative ceremony pressure | Detail |
|-------|-------------------------------|--------------------------------|--------|
| **A** Discover | **C1**, **C2** | Prioritization, roadmap/backlog sessions | [Phase A](#phase-a--discover--prioritize) |
| **B** Specify | **C1**, **C6** (readiness) | Refinement, “definition of ready,” risk triage | [Phase B](#phase-b--specify) |
| **C** Design | **C1**, **C6** | Design review, NFR alignment | [Phase C](#phase-c--design-lightweight) |
| **D** Build | **C2**, **C3**, **C6** (ongoing) | Pull/commit selection, standups, CI as assurance | [Phase D](#phase-d--build) |
| **E** Verify | **C3**, **C4**, **C6** | Test progress sync, stakeholder demo, quality gates | [Phase E](#phase-e--verify) |
| **F** Release | **C4**, **C6** | Go/no-go, release approval, post-release learnings → **C5** | [Phase F](#phase-f--release) |

**Methodology mapping:** the same intents appear as **Sprint Planning**, **replenishment**, **tollgates**, **planning game**, etc. — [`methodologies/ceremonies/methodology-bridge.md`](methodologies/ceremonies/methodology-bridge.md).

---

### Phase A — Discover / prioritize

**Activities:** Ideas, rough sizing, ordering.

**Artifacts (typical)**

| Artifact | Action |
|----------|--------|
| **Planning source of truth** | One place for prioritized work (WBS/CSV, backlog, board, or optional high-level `docs/ROADMAP.md` from [`templates/ROADMAP.template.md`](templates/ROADMAP.template.md)). Record **where** it lives in `docs/PROJECT.md` or root `README.md`. |
| Work breakdown (WBS) | e.g. `docs/requirements/WBS.csv` — new epics/stories or statuses such as `draft` / `backlog`. |
| Spec files under your milestone tree | **Optional** until you commit to build. |

**Exit:** A backlog item is **ready to specify** when it has a clear outcome and a home in the WBS (or equivalent).

---

### Phase B — Specify

**Activities:** Acceptance criteria, edge cases, dependencies, risks.

**Artifacts (typical)**

| Artifact | Action |
|----------|--------|
| Story (or feature) spec | `status: ready` when acceptance criteria are agreed. |
| Risk register | e.g. `docs/requirements/risks/register.csv` — add or update rows when scope changes risk. |
| Themes / tags matrix | e.g. `docs/requirements/traceability/themes-matrix.csv` if you use themes. |

**Exit:** Story (or equivalent) is **`ready`**; implementation tasks can be split.

---

### Phase C — Design (lightweight)

**Activities:** Enough design to implement without rework; record durable decisions only when useful.

**Artifacts (typical)**

| Artifact | When |
|----------|------|
| Epic/story body | Sketches, interfaces, UX notes in the same spec. |
| ADRs | e.g. `docs/adr/` — when a choice is hard to reverse or affects multiple modules. |
| Architecture notes | e.g. `docs/architecture/` when subsystems or data flow need a shared picture. |

**Exit:** No blocking unknown for **this** scope remains undocumented.

---

### Phase D — Build

**Activities:** Implementation, tests, local verification.

**Artifacts (typical)**

| Artifact | Action |
|----------|--------|
| Task-level notes | Link requirement or task IDs in commits or PR descriptions when useful. |
| WBS / backlog | Set items to `in_progress` when work starts. |
| API / public surface | Language-appropriate doc comments (e.g. KDoc, Javadoc, Rustdoc, docstrings). |
| **CI pipeline config** | e.g. `.github/workflows/`, GitLab CI, Jenkinsfile — lives in-repo; document **what runs** and **merge/release gates** in `docs/development/` (or equivalent). See **§7**. |
| **Optional agents & automation** | When `blueprints/agents/` is adopted: container **recipes** (e.g. browser/E2E) in `agents/`; document image build and recipe steps beside other CI gates. Broader agentic practices: [`methodologies/agentic-sdlc.md`](methodologies/agentic-sdlc.md). See [`DOCUMENTATION-STRUCTURE.md`](DOCUMENTATION-STRUCTURE.md) and the [agents blueprint](../agents/README.md). |
| **Test plan (lightweight)** | For non-trivial scope: outline scope, levels (unit/integration/e2e/manual), and exit criteria — story spec, `docs/testing/`, or [`templates/TEST-PLAN.template.md`](templates/TEST-PLAN.template.md). |

**Exit:** Acceptance criteria met; tests added **or** skip justified in the story/PR.

---

### Phase E — Verify

**Activities:** Automated tests, manual checks, regression of related behavior.

**Artifacts (typical)**

| Artifact | Action |
|----------|--------|
| Tests ↔ requirements | e.g. `docs/requirements/traceability/tests-matrix.csv`, or inline references in tests. |
| **Quality gates (CI)** | Pipeline must **pass** agreed checks (build, lint/static analysis, tests) before merge or release — documented in `docs/development/` (see **§7**). |
| Story spec | `status: done` when verified. |

**Exit:** Story **`done`**; backlog row matches reality; **CI** reflects the same bar as local verification unless a temporary exception is recorded (story/PR).

---

### Phase F — Release

**Activities:** Versioning, packaging, distribution, compliance checks.

**Artifacts (typical)**

| Artifact | Action |
|----------|--------|
| `docs/release/` (or equivalent) | Checklists, privacy / compliance links, signing notes (**no secrets** in repo). |
| Root `README.md` | User-visible features if changed. |
| Planning / milestone status | Updated to reflect what shipped (wherever you track it). |
| **Release CI (optional)** | Tag/build pipelines, store upload, or signing orchestration — **secrets** in CI vault, not in Git; document **process** in `docs/release/` or `docs/development/`. |

**Exit:** Artifact published to the intended **distribution channel** (app store, registry, fleet, etc.); status docs updated.

---

## 3. Definition of Done (story or equivalent)

A story is **done** when:

1. Acceptance criteria in the spec are met (or explicitly waived with reason).  
2. The **canonical backlog** (e.g. WBS) marks the story **`done`**.  
3. **Tests:** New logic has automated coverage **or** a documented exception.  
4. **CI:** Required pipeline checks **pass** for the merged change (or a documented waiver by Owner).  
5. **Risks:** Risk register updated if mitigation shipped or risk closed.  
6. **User-facing changes:** Product README or UI copy reviewed if applicable.

---

## 4. Definition of Done (epic or equivalent)

An epic is **done** when all **in-scope** child stories are `done`, your **planning view** reflects completion, and residual risks are **accepted** or **closed**.

---

## 5. Change control

- **Requirement IDs** (if used) stay stable once referenced in code, tests, or ADRs; deprecate with a note rather than silent renumbering.  
- **Scope management:** Scope changes show up in the backlog/WBS (or equivalent)—prefer explicit new stories/tasks over hidden scope. Descoping is explicit (cancelled/deferred); epics close when **in-scope** children are done. Risks update when scope shifts materially.  
- **Time and effort:** Git activity shows *when* work touched the repo, not *duration* or billable hours. Explicit time (if needed) lives in a tracker or agreed in-repo log — see project `sdlc/TRACKING-FOUNDATION.md` when present.  
- **ADRs:** Prefer **supersede** with a new ADR over deleting history.

See the [change management process](DOCUMENTATION-STRUCTURE.md) for diagram, tables, and links to tracking docs.

---

## 6. Review cadence (suggested)

| Cadence | Activity |
|---------|----------|
| **Per change request / PR** | Touch backlog/specs when scope or status changes. |
| **Weekly / end of milestone** | Planning/backlog accuracy, open risks, README freshness. |
| **Before major release** | Release checklist, privacy/compliance docs, signing process (documented, not secret values). |

---

## 7. CI/CD, quality gates, and test plans

**CI/CD** means continuous integration (build + checks on every push/PR) and, when you adopt it, continuous delivery or deployment (automation toward release).

**Testing depth:** [`disciplines/engineering/testing/README.md`](../disciplines/engineering/testing/README.md) is the cross-cutting testing knowledge base — test levels and types, test design techniques, modern strategies (shift-left, TDD, BDD, contract testing, AI-augmented), and the test automation frameworks landscape. Reference it when choosing *what* to test and *which tools* to use; this section covers *where* testing fits in the pipeline.

| Concept | What to capture |
|---------|-----------------|
| **Pipeline** | Where it lives (e.g. `.github/workflows/`), which branches trigger it. |
| **Quality gates** | Mandatory steps: e.g. compile, **lint/static analysis**, **unit tests**, dependency/license scan — **document** the list so “green” matches team expectations. |
| **Test plan** | For meaningful scope: **what** to test (levels, environments), **who** runs manual/exploratory checks, and **done** criteria — use a story spec section or [`templates/TEST-PLAN.template.md`](templates/TEST-PLAN.template.md). |
| **Traceability** | Keep tests ↔ requirements links in your traceability matrix or in code as your project prefers. |
| **Optional automation images** | If `blueprints/agents/` is present: same recipe should pass locally (container) and in CI unless waiver is documented. |

**Merge policy (suggested):** No merge to the main branch while **required** CI checks are failing, unless Owner explicitly accepts risk and a waiver is noted in the PR or story.

**Release policy (suggested):** No release artifact from automation until the same (or stricter) gates pass on the **release** commit/tag; add release-only checks (e.g. ProGuard, signing) as the product matures.

**Where to write details:** `docs/development/` (or your dev guide) — **not** in `blueprints/sdlc/` except this generic section.

---

*Keep product-specific context in `docs/PROJECT.md` (or equivalent), not in this file.*
