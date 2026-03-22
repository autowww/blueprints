# Blueprint policy — do not change casually

This directory **`blueprints/pdlc/`** is the **frozen** PDLC package: product lifecycle conventions meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal product work (discovery notes, experiment logs, metrics dashboards, etc.).
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.
3. **Day-to-day product work** belongs in **`docs/product/`** (living product-functional content) and project-specific folders, not in this blueprint.
4. If you change **`PDLC.md`**, **`PDLC-SDLC-BRIDGE.md`**, **`approaches/*.md`**, or related blueprint files, **update the human handbook** in **`blueprints/pdlc/docs/`** per **`blueprints/pdlc/docs/MAINTENANCE.md`**.

## Relationship to `docs/product/`

- **`blueprints/pdlc/`** — canonical, generic text (immutable by convention).
- **`docs/product/`** — where this project **creates, interprets, and extends** product lifecycle artifacts without touching the blueprint.

Copying this repo: you may copy **`blueprints/pdlc/`** wholesale to another repository; use **`docs/product/`** (or equivalent) only in repos that track project-specific product artifacts.
