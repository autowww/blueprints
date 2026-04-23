---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Blueprint policy — do not change casually

This directory **`blueprints/product/`** is the **frozen** product-functional documentation package: information architecture and templates meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal product work (feature specs under `docs/product/`, WBS updates, etc.).  
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.  
3. **Day-to-day product documentation** belongs in **`docs/product/`** (this repo’s mutable tree) and elsewhere under **`docs/`** as needed.  
4. If you change **`STRUCTURE.md`** or related blueprint files, ensure **publishable** pages are refreshed on the public handbook per [`docs/DESIGN-PRINCIPLES.md`](../docs/DESIGN-PRINCIPLES.md) and [`docs/MAINTENANCE.md`](../docs/MAINTENANCE.md): run **`python3 generator/build-handbook.py product`** from **blueprints-website** (or rely on CI). See **`blueprints/product/docs/MAINTENANCE.md`**.

## Relationship to `docs/product/`

- **`blueprints/product/`** — canonical, generic text (immutable by convention).  
- **`docs/product/`** — where this project **writes** vision, journeys, and feature behavior without touching the blueprint.

Copying this repo: you may copy **`blueprints/product/`** wholesale to another repository; use **`docs/product/`** (or equivalent) only in repos that track project-specific functional documentation.
