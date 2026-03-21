# Documentation blueprint — structure

This document defines **the full `docs/` tree** that a project bootstraps from this blueprint: product-functional prose, requirements & WBS, architecture, ADRs, development, testing, release, security, and operations. Add files **as you go**; empty areas are intentional until there is something worth writing down.

**Related:** [`blueprints/sdlc/DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md) (whole-repo layout including `sdlc/`, `agents/`, `blueprints/`) · [`blueprints/sdlc/SDLC.md`](../sdlc/SDLC.md) (phases, gates, doc obligations).

**Scalability:** Keep **`blueprints/docs/`** at **repository root** (frozen). Mutable content lives under **`docs/`** in the consuming repo — seeded by **`scripts/init-docs-workspace.sh`**.

---

## 1. Principles

| Principle | Meaning |
|-----------|---------|
| **Audience-first** | Functional docs are readable by PM, UX, support, and engineering without the backlog tool. |
| **Just enough** | Add a document when it reduces ambiguity, onboarding cost, or operational risk. |
| **Single source of truth** | One canonical place per topic; link to requirement IDs instead of duplicating acceptance criteria. |
| **Docs as code** | Documentation lives in the repository; changes use the same review practices as code. |
| **Traceability** | Stable IDs (`M1E3S2`, `R1`, etc.) **link** planning ↔ specs ↔ implementation ↔ tests. |

---

## 2. Full `docs/` layout (bootstrapped by init script)

```text
docs/
  INDEX.md                        # Hub: links to every documentation area
  PROJECT.md                      # Stack, compliance, repo context (project-specific)
  ROADMAP.md                      # Milestone + epic status + % complete

  product/                        # Product functional — vision, journeys, features
    INDEX.md
    vision/
    personas/
    capabilities/
    journeys/
    features/
    data/
    integrations/
    glossary.md
    assumptions-open-questions.md

  requirements/                   # Spec-driven breakdown (WBS, risks, traceability)
    INDEX.md                      # Milestone → epic → story links
    STRUCTURE-PROPOSAL.md         # ID scheme, folder layout, frontmatter
    WBS.csv / WBS.md              # Work breakdown to stories + status
    traceability/
      themes-matrix.csv
      tests-matrix.csv
    risks/
      README.md                   # RBS layout conventions
      RBS.md                      # Risk process (scoring, cadence)
      register.csv                # Master risk register
      items/                      # Optional: R1.md, R2.md, …
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

  architecture/                   # System overview, diagrams (grow as needed)
  adr/                            # Architecture decision records
  development/                    # Build, style, CI/CD, quality gates
    README.md
    CI-CD.md
  testing/                        # Scope-level test plans
  release/                        # Distribution, signing, compliance
  security/                       # Non-secret security notes
  operations/                     # Runbooks, ops procedures
```

Paths are **examples** — rename if your org uses `functional/` instead of `product/`, `work-items/` instead of `requirements/`, etc. Keep the *separation* between product docs, delivery specs, and engineering guides.

---

## 3. Document types & when to create them

### 3.1 Product functional (`docs/product/`)

| Type | Typical location | When to add / update |
|------|------------------|----------------------|
| **Vision & scope** | `product/vision/` | Direction, goals, in/out of scope change. |
| **Personas / segments** | `product/personas/` | ICP or constraints change. |
| **Capability map** | `product/capabilities/` | Major abilities appear, merge, or retire. |
| **User journeys** | `product/journeys/` | Core flows change. |
| **Feature / domain specs** | `product/features/` | Behavior, rules, errors, edge cases need clarity. |
| **Data (product view)** | `product/data/` | Privacy, retention, conceptual model. |
| **Integrations** | `product/integrations/` | New systems or changed contracts. |
| **Glossary** | `product/glossary.md` | New domain terms. |

### 3.2 Requirements & planning (`docs/requirements/`)

| Type | Typical location | When to add / update |
|------|------------------|----------------------|
| **Structure proposal** | `requirements/STRUCTURE-PROPOSAL.md` | ID scheme, folder layout (confirm before scaffolding). |
| **Requirements index** | `requirements/INDEX.md` | New milestone or epic. |
| **WBS** | `requirements/WBS.csv` + `WBS.md` | New scope; status changes. |
| **Milestone / epic / story / task** | `requirements/milestones/…` | When an item is specified or changes. |
| **Risk register** | `requirements/risks/register.csv` | New risk, mitigation, closure. |
| **Traceability** | `requirements/traceability/*.csv` | Theme or test mapping changes. |

### 3.3 Engineering & operations

| Type | Typical location | When to add / update |
|------|------------------|----------------------|
| **Project profile** | `PROJECT.md` | Stack, regulatory, or repo context change. |
| **Roadmap** | `ROADMAP.md` | Epic status or milestone schedule changes. |
| **Architecture** | `architecture/` | Non-trivial structure or onboarding need. |
| **ADRs** | `adr/` | Significant, somewhat stable technical choices. |
| **Development guide** | `development/` | Build scripts, CI/CD, quality gates, style. |
| **Test plans** | `testing/` | Scope-level strategy; per-milestone/release plan. |
| **Release** | `release/` | Distribution, privacy, signing process. |
| **Security** | `security/` | Non-secret security notes (when needed). |
| **Operations** | `operations/` | Runbooks, ops (when needed). |

---

## 4. Relationship to other blueprint packages

| Layer | Role |
|-------|------|
| **`blueprints/docs/`** (this) | Frozen IA + templates for the **entire** `docs/` tree. |
| **`blueprints/sdlc/`** | Process methodology, phases, ceremonies, doc obligations. |
| **`blueprints/ide/`** | IDE agent instructions (Cursor rules, Claude skills). |
| **`blueprints/agents/`** | Docker automation (containers, recipes). |
| **`docs/`** (project) | Mutable content — seeded from templates, customized freely. |

---

## 5. Conventions

- **Markdown** for prose; **CSV** for matrices (diffs + spreadsheet round-trip).
- **Filenames:** Lowercase-with-hyphens for general guides; requirement filenames follow **STRUCTURE-PROPOSAL**.
- **Links:** Prefer **relative** paths from `docs/`.
- **Secrets:** Never commit credentials — document *where* to configure them only.
- **Diagrams:** SVG or Mermaid in-repo when useful.

---

## 6. Bootstrap

Run from the repository root:

```bash
./blueprints/docs/scripts/init-docs-workspace.sh "Project Name"
```

This seeds `docs/` with all template files, replacing `{{PROJECT_NAME}}` and `{{DATE}}`. Use `--force` to overwrite existing files. See [`scripts/README.md`](scripts/README.md).

---

## 7. Evolution

- **Small product:** `INDEX.md` + `PROJECT.md` + `product/vision/` + `product/features/` + slim `requirements/` may suffice.
- **Multiple domains:** Namespace under `product/features/` or add subfolders per domain.
- **Monorepo:** One `blueprints/docs/` at repo root; per-package `docs/` if needed.

---

*Blueprint — adapt paths and folder names to your organization.*
