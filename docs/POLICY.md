# Blueprint policy — do not change casually

This directory **`blueprints/docs/`** is the **frozen** documentation package: information architecture, templates, and bootstrap tooling for the **entire `docs/` tree** — product-functional, requirements, architecture, ADRs, development, testing, release, security, and operations.

## Rules

1. **Do not edit** files here as part of normal product work (feature specs, WBS updates, etc.).
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.
3. **Day-to-day documentation** belongs in **`docs/`** (this repo's mutable tree) — the files produced by `init-docs-workspace.sh`.
4. If you change **`STRUCTURE.md`**, templates, or related blueprint files, **update the human handbook** in **`blueprints/docs/docs/`** (`index.html` as needed) per **`blueprints/docs/docs/MAINTENANCE.md`**.

## Relationship to `docs/`

- **`blueprints/docs/`** — canonical, generic templates and IA (immutable by convention).
- **`docs/`** — where this project **copies, interprets, and extends** the templates without touching the blueprint.

Copying this repo: you may copy **`blueprints/docs/`** wholesale to another repository; use the init script to seed project-level files, then customize freely.
