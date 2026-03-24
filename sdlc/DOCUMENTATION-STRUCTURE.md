# Documentation structure — proposal

This document defines **where documentation can live** in a repository, **what kinds of docs to maintain**, and **how documentation ties to the SDLC**. Add files **as you go**; empty areas are intentional until there is something worth writing down.

**Related:** [`SDLC.md`](SDLC.md) (phases, gates, doc obligations) · optional **requirements convention** in the consuming repo (e.g. `docs/requirements/STRUCTURE-PROPOSAL.md` if you adopt one).

**Scalability:** The layout below scales from a single deliverable to multiple milestones and teams by **namespacing delivery specs** (often under `docs/requirements/`) and keeping frozen blueprints under **`blueprints/`** at repository root — **`blueprints/sdlc/`** (this SDLC package), optional **`blueprints/product/`** (product-functional IA; mutable prose under **`docs/product/`**), and optional **`blueprints/agents/`** (containerized automation). **Agentic** delivery (IDE/LLM/CI) is covered in **`methodologies/agentic-sdlc.md`**. Mutable jobs live in **`agents/`** at repository root—see **`blueprints/agents/STRUCTURE.md`** and **`blueprints/agents/README.md`**. Swap folder names if you use another tool (e.g. `work-items/` instead of `requirements/`)—keep the *separation* between process docs, product-functional docs, delivery specs, and (when used) automation blueprints.

---

## 1. Principles

| Principle | Meaning |
|-----------|---------|
| **Docs as code** | Documentation lives in the repository; changes use the same review practices as code. |
| **Just enough** | Add a doc when it reduces ambiguity, onboarding cost, or operational risk. |
| **Single source of truth** | One canonical place per topic; elsewhere **link** instead of duplicating (short summaries at repo root are fine). |
| **SDLC-bound** | Major phases have **expected artifacts** (see [`SDLC.md`](SDLC.md)); skipping them is a conscious exception. |
| **Traceability** | When you use requirement IDs, risks, and tests, link by **stable IDs** so planning ↔ specs ↔ implementation stay aligned. |

---

## 2. Recommended layout (repository root + `docs/`)

This blueprint assumes **`blueprints/sdlc/`** (this folder) lives **under `blueprints/`** at repository root, next to **`docs/`** and **`sdlc/`**. A sibling **`sdlc/`** (or similar) holds **project-specific** SDLC notes and links—do not put that material inside `blueprints/sdlc/`. Optional **`blueprints/product/`** holds frozen product-functional IA; project prose belongs under **`docs/product/`**.

```text
repository root/
  README.md
  blueprints/website/           # Generated handbook HTML (CI) — python3 generator/build-handbook.py from blueprints/
  blueprints/generator/         # build-handbook.py — Markdown under each area → flat website/*.html
  blueprints/docs/              # MAINTENANCE.md — handbook build, CI, wiki sync
  blueprints/sdlc/               # Frozen SDLC template — see POLICY.md
    README.md
    POLICY.md
    SDLC.md
    DOCUMENTATION-STRUCTURE.md
    methodologies/              # Deep methodology guides (Markdown) — Scrum, Kanban, XP, …
    templates/                  # Optional copy-paste (ROADMAP, TEST-PLAN, templates/sdlc/ …)
    scripts/                    # init-sdlc-workspace.sh — see scripts/README.md, SDLc-WORKSPACE.md
    SDLc-WORKSPACE.md           # How to bootstrap sibling sdlc/

  blueprints/product/               # Frozen product-functional IA — see blueprints/product/POLICY.md
    README.md
    POLICY.md
    STRUCTURE.md
    docs/                       # Maintainer notes (MAINTENANCE.md); HTML → blueprints/website/ via build-handbook.py
    templates/

  blueprints/pdlc/               # Frozen product lifecycle blueprint — see blueprints/pdlc/POLICY.md
    README.md
    POLICY.md
    PDLC.md                     # Phases P1–P6, artifacts, exit criteria
    PDLC-SDLC-BRIDGE.md         # How PDLC and SDLC relate — diagrams, role mapping, worked example
    approaches/                 # PDLC approach guides (Dual-Track, Stage-Gate, Design Thinking, …)
    templates/                  # Product vision, experiment log, metrics, GTM, sunset plan
    docs/                       # Maintainer notes (MAINTENANCE.md); HTML → blueprints/website/ via build-handbook.py

  blueprints/disciplines/         # Cross-cutting professional disciplines — see blueprints/disciplines/README.md
    README.md                   # Hub: BA, PM, Testing, Software Architecture, DevOps, Big Data, Data Science
    ba/                         # Business analysis (BABOK, knowledge areas, techniques, perspectives)
    pm/                         # Project management (process groups, governance, approaches)
    testing/                    # Testing & QA (ISTQB approaches, automation landscape)
    software-architecture/      # Software architecture (quality attributes, patterns, ADRs)
    devops/                     # DevOps (CALMS, DORA, SRE, CI/CD, observability)
    bigdata/                    # Big data & data engineering (governance, pipeline patterns, DataOps)
    data-science/               # Data science & ML (CRISP-DM, MLOps, responsible AI)

  blueprints/agents/             # Optional frozen Docker automation blueprint — see blueprints/agents/POLICY.md
    README.md
    POLICY.md
    STRUCTURE.md
    docker/                     # Dockerfile.base, compose.yaml — build context is blueprints/agents/
    templates/                  # recipe/ + project-agents/ seeds
    scripts/
    docs/                       # Maintainer notes (README.md, MAINTENANCE.md); HTML → blueprints/website/agents--*.html via build-handbook.py

  agents/                       # Optional mutable automation workspace (NOT inside blueprints/agents) — recipes, workspaces/, compose.override.yaml

  sdlc/                         # Project SDLC workspace (mutable); bootstrap from blueprints/sdlc/templates/sdlc — see SDLc-WORKSPACE.md
    README.md
    TRACKING-FOUNDATION.md      # Optional: engineering tracking (copy from templates/sdlc; not frozen blueprint text)
    TRACKING-METHODOLOGIES.md
    TRACKING-CHALLENGES.md

  forge/                         # Optional Forge SDLC workspace (mutable); bootstrap from blueprints/sdlc/templates/forge
    forge.config.yaml            # Team, Versonas, Assay Gate, paths — from forge.config.template.yaml
    charge.md                    # Current daily Charge
    charge-archive/              # Archived daily Charge files
    journal/                     # Day journals (YYYY-MM-DD.md)
    releases/                    # Product Spark release plans
  ember-logs/                    # Ember Log entries (YYYY-MM-DD.md) — decision memory

  docs/
    INDEX.md
    PROJECT.md                  # Optional: stack, compliance context (product-specific)
    product/                    # Mutable product functional docs (from blueprints/docs templates)
      INDEX.md
      vision/
      personas/
      capabilities/
      journeys/
      features/
      data/
      integrations/
    ROADMAP.md                  # Optional: copy from blueprints/sdlc/templates/ if you want a milestone/epic table

    requirements/               # What to build & why (spec-driven); name may vary by org
      INDEX.md
      STRUCTURE-PROPOSAL.md
      WBS.csv / WBS.md
      traceability/
      risks/
      milestones/

    architecture/
    adr/
    development/              # Build, CI/CD, quality gates — see CI-CD.md when adopted
    testing/                    # Optional: test plans, scope-level strategy (see SDLC §7)
    release/
    security/
    operations/
```

**Repository root** (outside `docs/`): `README.md` (product + setup), optional `CONTRIBUTING.md`. **CI config** (e.g. `.github/workflows/`, `.gitlab-ci.yml`) lives at repo root or paths your tool expects — describe **pipelines and quality gates** in `docs/development/` (see [`SDLC.md`](SDLC.md) §7). **Where planning lives** (WBS, board, optional `docs/ROADMAP.md`)—document the canonical pointer in `docs/PROJECT.md`. A roadmap **file** is optional; the SDLC does not require it if backlog/WBS is sufficient.

### 2.1 Work breakdown hierarchy (milestones → tasks)

When you adopt **spec-driven** planning, the blueprint assumes a **nested hierarchy** so IDs, folders, WBS rows, and traceability matrices line up.

#### Levels (outside → inside)

| Level | Purpose | Typical “done” meaning |
|-------|---------|-------------------------|
| **Milestone** | Time-bound or theme-bound slice of delivery (e.g. release train, quarter, major capability). | Milestone **accepted** when agreed scope is met or explicitly descoped; planning views updated. |
| **Epic** | Large outcome that groups related stories (often maps to a user- or business-visible capability). | Epic **done** when all **in-scope** child stories are done and residual risks are accepted or closed. |
| **Story** | Sized unit with **acceptance criteria** (user story, feature slice, or equivalent). | Story **done** per [`SDLC.md`](SDLC.md) §3 (DoD). |
| **Task** | Implementation slice (PR-sized); optional file per task when you need explicit checklists or ownership. | Task **done** when merged / verified per team rule; story remains the acceptance gate. |

**Rules of thumb**

- **Acceptance criteria** live at **story** (or above for thin teams); **tasks** decompose implementation, not user value.
- **WBS** usually lists at least through **story**; tasks may live only in the tracker or in nested `tasks/` files.
- **Epics** are optional for tiny efforts; you can use milestones → stories → tasks if epics add no clarity.

#### ID scheme (example — adapt in `STRUCTURE-PROPOSAL` or equivalent)

A common **concatenated** pattern (no leading zeros on numeric segments; letters `E`, `S`, `T` are literal):

| Level | Pattern | Example |
|-------|---------|---------|
| Milestone | `M{n}` | `M1`, `M2` |
| Epic | `M{n}E{n}` | `M1E3` |
| Story | `M{n}E{n}S{n}` | `M1E3S2` |
| Task | `M{n}E{n}S{n}T{n}` | `M1E3S2T4` |

Counters restart **per parent** (each epic’s stories start at `S1`, etc.). **Risks** use a separate namespace (e.g. `R1`, `R2`) in `risks/register.csv`, not the same tree.

**Sorting caveat:** plain string sort may order `M1E10` before `M1E2`; use natural sort in tools or curated order in `INDEX.md` / WBS.

#### Artifacts at each layer

| Layer | Planning / status | Spec prose |
|-------|-------------------|------------|
| Milestone | `docs/ROADMAP.md` (optional roll-up), `WBS.csv` rows for `M{n}` | `milestones/M{n}/milestone.md` (goals, scope boundaries) |
| Epic | WBS; optional % complete in roadmap | `…/epics/M{n}E{n}/epic.md` |
| Story | WBS; board / backlog | `…/stories/M{n}E{n}S{n}/story.md` |
| Task | Tracker or WBS extension | `…/tasks/M{n}E{n}S{n}T{n}-task.md` (optional) |

**Frontmatter (typical):** `id`, `parent`, `milestone`, `type` (`milestone` \| `epic` \| `story` \| `task`), `status` (`draft` \| `ready` \| `backlog` \| `in_progress` \| `done` \| `cancelled`), optional `themes`.

#### Nested folder layout (example)

Many teams mirror IDs under `docs/requirements/milestones/`:

```text
docs/requirements/
  INDEX.md                    # Human TOC: milestones → epics → stories
  WBS.csv
  milestones/
    M1/
      milestone.md
      epics/
        M1E1/
          epic.md
          stories/
            M1E1S1/
              story.md
              tasks/
                M1E1S1T1-task.md
            M1E1S2/
              story.md
              tasks/
                ...
        M1E2/
          ...
    M2/
      ...
```

**Traceability** (`traceability/*.csv`) references the same IDs at any level (`M1`, `M1E3`, `M1E3S2`, `M1E3S2T4`). **Risks** usually stay in a **single register** with `scope_id` pointing into this tree rather than duplicating the full folder hierarchy—see your `risks/README.md` convention.

### 2.2 Agents blueprint (optional, automation)

**Software agents** in this repo’s sense include **LLM assistants**, **IDE tooling**, **CI bots**, and **containerized** jobs — see [`methodologies/agentic-sdlc.md`](methodologies/agentic-sdlc.md). **`blueprints/agents/`** is the **optional execution layer** for **repeatable, isolated** work (Docker images, Compose, `agents/recipes/`). When you adopt it, treat it like **`blueprints/product/`**: **frozen** generic package at repository root; **mutable** content in **`agents/`** (recipes, workspaces, optional `compose.override.yaml`). Full sub-layer model:

| Layer | Contents |
|-------|----------|
| **Policy** | [`blueprints/agents/POLICY.md`](../agents/POLICY.md) — immutability vs `agents/`. |
| **Layout** | `blueprints/agents/docker/` (base `Dockerfile`, `compose.yaml`) · `templates/recipe/` · `templates/project-agents/`. |
| **Execution** | `agents/recipes/<name>/` — shell, Node, Python, or Playwright-specific images per recipe README. |
| **Optional LLM runner** | Only if you need a tool-calling loop *inside* the container; most repos stop at scripted recipes. |

**Handbook (generated):** run `python3 generator/build-handbook.py` from `blueprints/`; agents pages are under `website/agents--*.html`. **Canonical Markdown:** [`blueprints/agents/STRUCTURE.md`](../agents/STRUCTURE.md).

---

## 3. Document types & when to create them

| Type | Typical location | When to add / update |
|------|------------------|----------------------|
| **Product / setup** | Root `README.md` | New setup steps, features users care about. |
| **Product functional** | `docs/product/` (mutable); IA in `blueprints/product/` | Vision, journeys, capabilities, feature behavior—when observable product behavior needs a canonical description. |
| **Project profile** | `docs/PROJECT.md` | Stack, regulatory context, **where planning/backlog lives**—keeps [`SDLC.md`](SDLC.md) generic. |
| **Planning / WBS** | `docs/requirements/WBS.*` (typical); optional `docs/ROADMAP.md` from [`templates/ROADMAP.template.md`](templates/ROADMAP.template.md) | New scope; status changes; planning cycles. |
| **Risks** | `docs/requirements/risks/register.csv` (or your RBS) | New risk, mitigation, closure. |
| **Milestone / epic / story / task specs** | `docs/requirements/milestones/...` | When an item is specified or changes. |
| **Themes / tests traceability** | `docs/requirements/traceability/*.csv` | When mapping themes or tests to requirements. |
| **Architecture** | `docs/architecture/` | Non-trivial structure or onboarding need. |
| **ADRs** | `docs/adr/` | Significant, somewhat stable technical choices. |
| **Development** | `docs/development/` | Build scripts, **CI/CD**, **quality gates**, tasks, style—when root README is too large. |
| **Agents & automation (optional)** | **`blueprints/agents/`** (frozen) + **`agents/`** (mutable) | Container images, Compose, and **recipes** for repeatable automation (incl. browser/E2E); complements IDE/LLM workflows under review policy. Handbook HTML: generated to `blueprints/website/` (see `generator/build-handbook.py`); canonical Markdown: [`blueprints/agents/STRUCTURE.md`](../agents/STRUCTURE.md). |
| **Testing / test plans** | `docs/testing/` (optional); or story spec + [`templates/TEST-PLAN.template.md`](templates/TEST-PLAN.template.md) | Scope-level test strategy; per-milestone or release plan when useful. |
| **Release & compliance** | `docs/release/` | Distribution, privacy disclosures, signing *process* (not keys). |

---

## 4. SDLC mapping (summary)

Full detail: [`SDLC.md`](SDLC.md). **PDLC context:** [`blueprints/pdlc/PDLC-SDLC-BRIDGE.md`](../pdlc/PDLC-SDLC-BRIDGE.md) shows how these SDLC phases sit inside the broader product lifecycle (P1–P6). **BA context:** [`blueprints/disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md`](../disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md) maps business analysis knowledge areas and techniques to both lifecycles.

| Phase | Typical documentation | PDLC context |
|-------|------------------------|--------------|
| **Discover / ideate** | WBS/backlog (and optional high-level planning doc); optional notes in `architecture/` or ADR draft. | Receives validated problem + solution from PDLC P3 Strategize. |
| **Specify** | Story acceptance criteria; risks; themes row if used. | Acceptance criteria reflect PDLC P3 success metrics. |
| **Design** | Story/epic detail or ADR if cross-cutting. | Informed by PDLC P2 feasibility assessment. |
| **Build** | Task notes; API comments; backlog status; CI config; optional test plan; optional **agents** recipes under `agents/` when `blueprints/agents/` is adopted. | — |
| **Verify** | Tests matrix or inline requirement references; **CI quality gates** green; optional containerized checks from **`agents/`** documented next to other gates. | Tests validate against outcome criteria (PDLC P3 metrics) alongside technical correctness. |
| **Release** | Release checklist; README; planning status update; optional release pipeline docs. | Shippable increment hands to PDLC P4 Launch. |
| **Operate / learn** | Risks, ADR supersession, planning adjustments. | PDLC P5 Grow: adoption analytics, experiment logs, iteration backlog feed back into Discover. PDLC P6: lifecycle assessment, sunset planning. See `docs/product/metrics/`, `docs/product/lifecycle/`. |

---

## 5. Conventions

- **Markdown** for prose; **CSV** for matrices when you want diffs and spreadsheet round-trip.
- **Filenames:** Lowercase-with-hyphens for general guides; requirement filenames follow your **STRUCTURE-PROPOSAL** (or equivalent).
- **Links:** Prefer **relative** paths from `docs/` so links work in Git hosting and editors.
- **Secrets:** Never commit credentials, private keys, or signing passwords—document *where* to configure them only.

---

## 6. Evolution

- **Small team / single deliverable:** `blueprints/sdlc/` + `sdlc/` + slim `docs/requirements/` + root `README` may be enough; add `blueprints/product/` + `docs/product/` when you want a structured functional spec.  
- **Multiple products or long horizons:** Add milestone namespaces (`M1`, `M2`), stricter WBS, more ADRs; keep **`blueprints/sdlc/`** unchanged per [`POLICY.md`](POLICY.md).  
- **Monorepo:** One `blueprints/` folder (with `sdlc/` inside it, etc.) at repo root; per-package `docs/` or `requirements/` as needed.  
- **Containerized automation:** Add **`blueprints/agents/`** once; keep **`agents/`** recipes scoped per package or document mount paths in `docs/development/`.

---

*Template — adapt paths and folder names to your organization.*
