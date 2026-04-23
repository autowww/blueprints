# Branching consistency audit

**Date:** 2026-04-11  
**Last pass:** 2026-04-11 (extended consumer `GIT-WORKFLOW.md` parity)  
**Scope:** Reconcile Forge-native branching documentation with the canonical lane model and with **setup-aware** Team-tier defaults (`feature/*`, `fix/*`) used across autowww repositories.

## Canonical branch model (in force)

Unless a **consuming** repo documents otherwise in `forge/branching.yml` or `docs/process/branching-profile.md`:

| Element | Rule |
|---------|------|
| **`main`** | Protected trunk; **next releasable** |
| **`product/*`** | Optional parent for multi-iteration, multi-repo, or pre-main integration |
| **`iter/*`** | Default working / integration branch per **Forge iteration** for a Product Spark effort |
| **`spark/*`** | Conditional; risky or parallel **build** / **verify** work |
| **`spike/*`** | Exploration (discipline spikes) only |
| **`release/*`** | Optional stabilization window |
| **`hotfix/*`** | Production fixes; promotion + back-merge documented per repo |
| **Charge** | `forge/charge.md` (or documented alias) — **daily view only**; **never** `charge/*` |

**Promotion ladder (default tabletop):** `spark/*` → `iter/*` → `product/*` or `main` → `release/*` or `main`, with direct `iter/*` → `main` when parent is disabled ([Charge 03](../../sdlc/methodologies/forge/setup/charge-plans/branching/charge-03-promotion-and-integration.md)).

**Blueprint methodology:** [BRANCHING-STRATEGY.md](../../sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md) (includes **Forge-native branch lanes (optional)**) · [branching charge pack](../../sdlc/methodologies/forge/setup/charge-plans/branching/README.md).

## Actual policy implied by this workspace

| Layer | Finding |
|-------|---------|
| **blueprints** (git) | **Team-tier:** `main`, short-lived `feature/*`, `wip/*`; no `iter/*` / `spark/*` in routine use |
| **Consumer sites / apps** | Same defaults; **optional lane** paragraph now mirrored in top-level `docs/GIT-WORKFLOW.md` where listed below |
| **`forge/branching.yml`**, **`forge/charge.md`**, **`docs/process/branching-profile.md`**, mapping/promotion/matrix docs | **Absent** in workspace clones audited — expected until a repo runs Charge 01+ outputs |
| **Nested `kitchensink/docs/GIT-WORKFLOW.md`** (inside consumers) | Copies **forgesdlc-kitchensink**; update via **kitchensink submodule bump**, not one-off edits per consumer |

## Files reviewed (cumulative)

**Blueprints (methodology)**

- `sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md`
- `sdlc/methodologies/forge/setup/charge-plans/branching/README.md`
- `sdlc/methodologies/forge/setup/charge-plans/branching/CURSOR-PREAMBLE.md`
- `sdlc/methodologies/forge/setup/charge-plans/branching/charge-01` … `charge-08`, `optional-spikes.md`
- `CONTRIBUTING.md`
- `docs/INDEX.md`
- `docs/process/README.md`
- `docs/process/branching-consistency-audit.md` (this file)

**Workspace + consumers**

- `Code/.cursor/rules/workspace-git-workflow.mdc`
- `forgesdlc/docs/GIT-WORKFLOW.md`
- `blueprints-website/docs/GIT-WORKFLOW.md`
- `Situ8/docs/GIT-WORKFLOW.md`
- `forgesdlc-kitchensink/docs/GIT-WORKFLOW.md`
- `forge-lenses/docs/GIT-WORKFLOW.md`

**Spot check (intentional non-Forge prescriptive text)**

- `disciplines/engineering/software-engineering/SOFTWARE-ENGINEERING.md` — GitFlow **comparison** table (literature), not project policy

## Inconsistencies found

### Pass 1 (blueprints + forgesdlc + workspace rule)

1. Charge-pack **README** omitted **`product/*`** in the Charge branch-type sentence (fixed).
2. **BRANCHING-STRATEGY** lacked a first-class **Forge-native lanes** table (fixed).
3. **CONTRIBUTING**, **workspace-git-workflow**, **forgesdlc GIT-WORKFLOW** lacked setup-aware **optional lanes** note (fixed).
4. **CURSOR-PREAMBLE** branch rules missing **`main`**, **`release/*`/`hotfix/*`** (fixed).
5. **`iter/F1-` vs `F2-` vs `F3-` in charge examples** — denotes **pack phase** (F1–F3), not three Product Sparks; easy to misread (**documented only**).

### Pass 2 (consumer parity)

6. **blueprints-website**, **Situ8**, **forgesdlc-kitchensink**, **forge-lenses** top-level `docs/GIT-WORKFLOW.md` lacked the same **Optional Forge-native lanes** subsection as **forgesdlc** (fixed).

## Fixes applied

| File | Change |
|------|--------|
| `sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md` | **Forge-native branch lanes (optional)** section; `feature/*` ↔ lane model mapping |
| `sdlc/methodologies/forge/setup/charge-plans/branching/README.md` | Charge may reference **`product/*`** |
| `sdlc/methodologies/forge/setup/charge-plans/branching/CURSOR-PREAMBLE.md` | Branch rules: **`main`**, **`product/*`**, **`iter/*`**, **`release/*`/`hotfix/*`**, no **`charge/*`** |
| `CONTRIBUTING.md` | **Forge-native lanes (optional)** + link to charge pack |
| `docs/INDEX.md` | Link to `docs/process/` |
| `docs/process/README.md` | Index for process maintainer notes |
| `Code/.cursor/rules/workspace-git-workflow.mdc` | Lane model vs `feature/*`/`fix/*` |
| `forgesdlc/docs/GIT-WORKFLOW.md` | **Optional Forge-native lanes** |
| `blueprints-website/docs/GIT-WORKFLOW.md` | Same subsection (**handbook repository**) |
| `Situ8/docs/GIT-WORKFLOW.md` | Same subsection (**app repository**) |
| `forgesdlc-kitchensink/docs/GIT-WORKFLOW.md` | Same subsection (**design-system repository**) |
| `forge-lenses/docs/GIT-WORKFLOW.md` | Same subsection |

## Open decisions

- Whether any listed repo will **adopt** `iter/*` / `spark/*` for real work (currently **no**).
- Handbook URL for charge-pack pages once navigation includes them (GitHub link stable until then).
- **WBS IDs** in charges are **illustrative**; replace per repo.

## Follow-up not changed

- **Branch Steward scripts / tasklets** (Charge 05) — consumer implementation only.
- **Repos without top-level `docs/GIT-WORKFLOW.md`** (e.g. **Situ8-web**, **forge-a11y-checker**): only nested **kitchensink** copies — parity flows from **forgesdlc-kitchensink** submodule updates.
- **aw3** and other clones: add the same subsection if they gain a top-level git workflow doc.

---

## Summary

**Changed files (by repo):**

- **blueprints:** `BRANCHING-STRATEGY.md`, charge-pack `README.md`, `CURSOR-PREAMBLE.md`, `CONTRIBUTING.md`, `docs/INDEX.md`, `docs/process/README.md`, `docs/process/branching-consistency-audit.md`
- **forgesdlc:** `docs/GIT-WORKFLOW.md`
- **blueprints-website:** `docs/GIT-WORKFLOW.md`
- **Situ8:** `docs/GIT-WORKFLOW.md`
- **forgesdlc-kitchensink:** `docs/GIT-WORKFLOW.md`
- **forge-lenses:** `docs/GIT-WORKFLOW.md`
- **workspace:** `.cursor/rules/workspace-git-workflow.mdc`

**Unresolved mismatches:** None in methodology text; **git practice** remains Team-tier `feature/*`/`fix/*` until a project authors lane policy artifacts.

**Next recommended action:** In the first product repo that runs **PS-BRANCH-01**, add `forge/branching.yml` (or `docs/process/branching-profile.md`) and the Charge-pack `docs/process/*` outputs, then bump **kitchensink** (and any other submodules embedding `docs/GIT-WORKFLOW.md`) so nested copies pick up the optional-lanes paragraph.
