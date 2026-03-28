# Framework positioning and first MVP — Blueprints

**Status:** Draft (from spike **SPIKE-BP-ROADMAP-MVP**, 2026-03-27)  
**PDLC:** P1–P3 slice (discover → strategize) for the *framework as product*  
**Related:** [`../plans/mvp-adoption-spine.md`](../plans/mvp-adoption-spine.md) · [`../../ROADMAP.md`](../../ROADMAP.md) · [`../../ADOPTION.md`](../../ADOPTION.md)

---

## 1. Problem (who and why)

| Segment | Problem | Today’s workaround |
|---------|---------|-------------------|
| **Engineering leads** | Teams lack a **shared**, versioned SDLC/PDLC baseline across repos | Confluence/Notion pages, one-off “engineering handbook” docs |
| **Methodology-minded ICs** | Want **discipline bridges** (BA, PM, architecture, security…) aligned to phases | Books, training decks, or framework silos (SAFe, PMI) not mapped to *their* delivery model |
| **Forge / autowww ecosystem** | Need a **single submodule** that powers handbook, sites, and agent rules consistently | Duplicate markdown or outdated forks |

**Core job:** “Give me a **credible, linkable, git-native** methodology spine I can submodule and extend in `sdlc/` + `docs/` without authoring thousands of pages from zero.”

---

## 2. Market category

- **Primary category:** Open **software delivery & product development** methodology corpus (Markdown, GitHub-renderable).
- **Adjacent:** Internal engineering playbooks, agile coaching kits, **AI agent** process libraries (Versona templates, agent orchestration docs under `agents/`).

Blueprints is **not** a project-management tool, requirements database, or certifying body.

---

## 3. TAM / SAM / SOM (directional)

| Level | Scope | Notes |
|-------|--------|------|
| **TAM** | Teams shipping software who document process | Very large; not a useful planning unit alone. |
| **SAM** | Teams already on **Git + Markdown** who value submodule-based reuse | Smaller; matches Blueprints’ delivery model. |
| **SOM** (near-term) | Repos in the **Forge SDLC** orbit + intentional open-source adopters | Concrete; grow with evidence (submodule consumers, handbook traffic — track in M2). |

*Numbers are intentionally omitted until measurement exists.*

---

## 4. Competitive landscape (summary)

| Type | Examples | Blueprints contrast |
|------|-----------|---------------------|
| **Wiki / doc tools** | Notion, Confluence, Google Docs | Blueprints is **versioned**, diffable, and **submodule-friendly**; weaker for WYSIWYG non-dev users. |
| **Scaled frameworks (paid / heavy)** | SAFe, formal ISO suites | Blueprints is **modular** and **free**; you bring your own ceremony weight. |
| **Minimal templates** | README-only “how we work” | Blueprints adds **PDLC**, **discipline bridges**, **Forge/Versona** depth. |
| **Academic / book SDLC** | Sommerville, textbooks | Blueprints is **operational** Markdown + templates for daily use. |

**Differentiation (1–2 pillars):** (1) **Frozen reusable baseline** + explicit **consumer** layers (`sdlc/`, `docs/product/`). (2) **Forge integration** — Ore/Ingot/Spark, Versona sessions, exploration spikes, planning flow — in the same corpus as SDLC/PDLC.

---

## 5. Recommended first MVP — “Adoption spine v1” (Product Spark F1)

**Decision:** The first MVP should **not** be “more methodology chapters” or “homepage redesign alone.” It should make **adoption and positioning legible**:

1. **Positioning** — this document + roadmap honesty about evidence gaps.  
2. **Entry path** — [`../../ADOPTION.md`](../../ADOPTION.md) with ICP A/B/C.  
3. **Execution backbone** — [`../../requirements/WBS.md`](../../requirements/WBS.md) + [`../plans/mvp-adoption-spine.md`](../plans/mvp-adoption-spine.md).  
4. **Discoverability** — root README pointers to maintainer `docs/` (handbook CTA = **NEXT** milestone).

**Why this MVP:** It converts “what we are” into **actionable next steps** for both adopters and maintainers, and it is **bounded** (mostly docs in this repo).

**Explicit non-goals for F1:** New certification program; paid tier; rewriting frozen `blueprints/sdlc/` policy; full blueprints-website redesign.

---

## 6. Evidence and follow-up (M2)

- [ ] Add **one adopter note** (anonymous OK) after a short interview or issue discussion.  
- [ ] Decide **one north-star** metric for framework success (e.g. checklist completion, time-to-first-`sdlc/` file, or submodule bump cadence).

---

## 7. References (in-repo)

- Product bootstrap flow: [`../../../sdlc/methodologies/forge/product-manager/product-bootstrap-flow.md`](../../../sdlc/methodologies/forge/product-manager/product-bootstrap-flow.md)  
- Product package policy: [`../../../product/POLICY.md`](../../../product/POLICY.md)  
- Root README: [`../../../README.md`](../../../README.md)
