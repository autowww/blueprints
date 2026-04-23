---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Blueprint policy — do not change casually

This directory **`blueprints/disciplines/product/ba/`** is the **frozen** BA package: business analysis knowledge areas, techniques, and templates meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal project work (stakeholder registers, business cases, requirements packages, etc.).
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.
3. **Day-to-day BA work** belongs in **`docs/product/`** (discovery, research), **`docs/requirements/`** (specs, traceability), and project-specific folders, not in this blueprint.

## Relationship to project folders

- **`blueprints/disciplines/product/ba/`** — canonical, generic text (immutable by convention).
- **`docs/product/`** and **`docs/requirements/`** — where this project **creates, interprets, and extends** BA artifacts without touching the blueprint.

Copying this repo: you may copy **`blueprints/disciplines/product/ba/`** wholesale to another repository; use project-specific folders only in repos that track living BA artifacts.
