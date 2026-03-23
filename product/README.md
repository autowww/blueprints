# Product functional documentation blueprint

This folder is a **reusable, product-agnostic** package: **what the product does** for users and stakeholders (capabilities, journeys, behavioral rules)—not delivery process (see **`blueprints/sdlc/`**) and not granular backlog specs (see consuming repo’s **`docs/requirements/`** when present).

**Governance:** read [`POLICY.md`](POLICY.md) — **do not change** this directory unless explicitly updating the baseline. Project content lives under **`docs/product/`** (or your chosen path) in the consuming repo.

| Deliverable | Purpose |
|-------------|---------|
| [**POLICY.md**](POLICY.md) | Immutability rules for this blueprint. |
| [**STRUCTURE.md**](STRUCTURE.md) | Canonical information architecture, document types, conventions. |
| [**docs/**](docs/README.md) | Maintainer notes ([`MAINTENANCE.md`](docs/MAINTENANCE.md)). Handbook HTML is generated into **`blueprints/website/`** by **`generator/build-handbook.py`** (CI). |
| [**templates/**](templates/README.md) | Copy-paste starters for vision, capabilities, journeys, feature specs. |

## What does *not* belong here

- Product name, filled-in journeys, or **living** feature text — use **`docs/product/`** (mutable) in the consuming repo.
- SDLC phases, CI gates, or repo-wide `docs/` layout — **`blueprints/sdlc/`**.
- Story-level acceptance criteria and WBS — **`docs/requirements/`** (or equivalent).

## How to adopt

1. Keep this folder at **repository root** as **`blueprints/product/`** (or copy the subtree).  
2. Add **`docs/product/`** (mutable) and seed it from **`templates/`** — never put project prose inside **`blueprints/product/`**.  
3. From **`docs/INDEX.md`** (or root `README.md`), link to **`blueprints/product/README.md`** and **`docs/product/`**.  
4. Optional: add **`docs/PROJECT.md`** for stack and planning pointers; keep **`blueprints/product/`** free of those details.

---

*Blueprint — no project-specific content.*
