# Blueprint policy — do not change casually

This directory **`blueprints/docs/`** is the **frozen** product-functional documentation package: information architecture and templates meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal product work (feature specs under `docs/product/`, WBS updates, etc.).  
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.  
3. **Day-to-day product documentation** belongs in **`docs/product/`** (this repo’s mutable tree) and elsewhere under **`docs/`** as needed.  
4. If you change **`STRUCTURE.md`** or related blueprint files, **update the human handbook** in **`blueprints/docs/docs/`** (`index.html` as needed) per **`blueprints/docs/docs/MAINTENANCE.md`**.

## Relationship to `docs/product/`

- **`blueprints/docs/`** — canonical, generic text (immutable by convention).  
- **`docs/product/`** — where this project **writes** vision, journeys, and feature behavior without touching the blueprint.

Copying this repo: you may copy **`blueprints/docs/`** wholesale to another repository; use **`docs/product/`** (or equivalent) only in repos that track project-specific functional documentation.
