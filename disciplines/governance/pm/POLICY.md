---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Blueprint policy — do not change casually

This directory **`blueprints/disciplines/governance/pm/`** is the **frozen** PM package: project management conventions meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal project work (status reports, risk registers, resource plans, etc.).
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.
3. **Day-to-day project governance** belongs in project-specific folders (e.g. `docs/development/`, project tracker, ALM tool), not in this blueprint.

## Relationship to project-specific docs

- **`blueprints/disciplines/governance/pm/`** — canonical, generic text (immutable by convention).
- **Project-specific docs** — where a team **creates, interprets, and extends** PM artifacts without touching the blueprint.

Copying this repo: you may copy **`blueprints/disciplines/governance/pm/`** wholesale to another repository; use project-specific folders only in repos that track project-specific governance artifacts.
