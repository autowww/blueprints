---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Product functional documentation — structure

This document defines **where product-functional prose can live**, **what kinds of documents to maintain**, and **how they relate to delivery specs**. Add files **as you go**; empty areas are intentional.

**Related:** [`blueprints/sdlc/DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md) (whole-repo `docs/` layout) · optional **requirements** area in the consuming repo (e.g. `docs/requirements/`).

**Scalability:** Keep **`blueprints/product/`** at **repository root** (frozen). Mutable content lives under **`docs/product/`** next to `docs/requirements/`, `docs/architecture/`, etc.

---

## 1. Principles

| Principle | Meaning |
|-----------|---------|
| **Audience-first** | Functional docs are readable by PM, UX, support, and engineering without the backlog tool. |
| **Just enough** | Add a document when it reduces ambiguity about **observable product behavior**. |
| **Single source of truth** | One canonical place per topic; link to requirement IDs instead of duplicating acceptance criteria. |
| **Journeys before deep specs** | Primary flows first; detailed feature specs second (easier onboarding). |
| **Traceability** | Optional stable IDs (`CAP-…`, `JRN-…`, `FEAT-…`) that **link** to backlog IDs when both exist. |

---

## 2. Recommended layout (mutable: `docs/product/`)

```text
docs/product/
  INDEX.md                    # Hub: links + last reviewed
  vision/
    VISION.md                 # Problem, goals, non-goals (or use template name)
  personas/
    README.md                 # Segments / personas (or multiple files)
  capabilities/
    README.md                 # Capability map + links to specs
  journeys/
    README.md                 # User journeys (or one file per journey)
  features/
    README.md                 # Index; subfolders or files per domain / feature
  data/
    README.md                 # Product-level data: entities, retention (not ER diagrams only)
  integrations/
    README.md                 # External systems and behavior at product level
  discovery/                  # PDLC: research synthesis, experiment logs (from blueprints/pdlc/ templates)
    README.md
    experiments/              # Experiment logs per initiative (PDLC P1–P2, P5)
    research/                 # User research, competitive analysis (PDLC P1)
  metrics/                    # PDLC: outcome metrics dashboards (from blueprints/pdlc/ templates)
    README.md
  lifecycle/                  # PDLC: lifecycle stage assessments, sunset plans (PDLC P6)
    README.md
  glossary.md
  assumptions-open-questions.md
```

Paths are **examples** — rename if your org uses `functional/` or `prd/` instead of `product/`.

---

## 3. Document types & when to create them

| Type | Typical location | When to add / update |
|------|------------------|----------------------|
| **Vision & scope** | `docs/product/vision/` | Direction, goals, in/out of scope change. |
| **Personas / segments** | `docs/product/personas/` | ICP or constraints change. |
| **Capability map** | `docs/product/capabilities/` | Major abilities appear, merge, or retire. |
| **User journeys** | `docs/product/journeys/` | Core flows change (onboarding, checkout, etc.). |
| **Feature / domain specs** | `docs/product/features/` | Behavior, rules, errors, edge cases need clarity. |
| **Data (product view)** | `docs/product/data/` | Privacy, retention, or conceptual model at product level. |
| **Integrations (product view)** | `docs/product/integrations/` | New systems or changed contracts visible to users. |
| **Glossary** | `docs/product/glossary.md` | New domain terms. |
| **Assumptions & open questions** | `docs/product/assumptions-open-questions.md` | Review cadence; explicit uncertainty. |
| **Discovery & experiments** | `docs/product/discovery/` | PDLC P1–P2: research synthesis, experiment logs, opportunity trees. Templates in [`blueprints/pdlc/templates/`](../pdlc/templates/README.md). |
| **Product metrics** | `docs/product/metrics/` | PDLC P3–P5: outcome metrics dashboards (adoption, retention, NPS, revenue). |
| **Lifecycle & sunset** | `docs/product/lifecycle/` | PDLC P6: lifecycle stage assessments, sunset plans, migration guides. |

---

## 4. Relationship to other documentation

| Layer | Role |
|-------|------|
| **`blueprints/product/`** | Frozen IA + templates (this package). |
| **`blueprints/pdlc/`** | Frozen product lifecycle blueprint — phases, approaches, templates. See [`blueprints/pdlc/README.md`](../pdlc/README.md). |
| **`docs/product/`** | Living product functional content — including PDLC artifacts in `discovery/`, `metrics/`, `lifecycle/`. |
| **`docs/requirements/`** | Backlog, milestones, story specs, WBS — **links** from functional docs by ID. |
| **`docs/architecture/`** | Technical structure; functional docs describe **behavior**, not implementation. |
| **Root `README.md`** | Setup and user-facing feature list — keep short; deep behavior in `docs/product/`. |

---

## 5. Conventions

- **Markdown** for prose; diagrams as **SVG** or diagram-as-code in-repo when useful.  
- **Filenames:** Lowercase-with-hyphens for files; folders as above unless your org standard differs.  
- **Links:** Prefer **relative** paths from `docs/`.  
- **Secrets:** Never commit credentials — document *where* to configure integrations only.

---

## 6. Evolution

- **Small product:** `docs/product/INDEX.md` + `vision/` + `features/` may suffice.  
- **Multiple domains:** Namespace under `features/` or add subfolders per domain.  
- **Monorepo:** One `blueprints/product/` at repo root; optional `docs/product/<product-name>/` if needed.

---

*Template — adapt paths and folder names to your organization.*
