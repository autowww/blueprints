---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Blueprint policy — do not change casually

This directory **`blueprints/agents/`** is the **frozen** package for **Docker-based automation and optional agent-style runners**: layout conventions, foundational images, compose patterns, and templates meant to be **reused** across repositories.

## Rules

1. **Do not edit** files here as part of normal product work (features, app code, WBS updates, etc.).  
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.  
3. **Day-to-day automation recipes, secrets, and CI wiring** belong in a **mutable** tree — typically **`agents/`** (or your chosen name) at repository root, seeded from [`templates/project-agents/`](templates/project-agents/README.md) — never put project-specific scripts or credentials inside **`blueprints/agents/`**.  
4. If you change **`STRUCTURE.md`**, **`ORCHESTRATION.md`**, **`README.md`**, or Docker templates, ensure **publishable** handbook output is refreshed per [`docs/DESIGN-PRINCIPLES.md`](../docs/DESIGN-PRINCIPLES.md): run **`python3 generator/build-handbook.py agents`** from **blueprints-website** or rely on CI (output: `website/agents--*.html`). See [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) and [Maintaining the documentation (repo-wide)](https://github.com/autowww/blueprints/blob/main/docs/MAINTENANCE.md). Keep **`.cursor/rules/new-agent-recipe.mdc`** pointing at **`ORCHESTRATION.md`** (no duplicated playbook prose in the rule).

## Relationship to `blueprints/sdlc/` and `agents/`

- **`blueprints/agents/`** — canonical, generic layout and **foundational** Docker/compose text (immutable by convention).  
- **`blueprints/sdlc/`** — SDLC process; [`DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md) references this blueprint in the repository layout; agents handbook HTML is generated into **`blueprints/website/`**.  
- **`agents/`** (mutable, optional) — where a project **writes** recipes, `compose.override.yaml`, env samples, and CI entrypoints.

Copying this repo: you may copy **`blueprints/agents/`** wholesale to another repository; use **`agents/`** (or equivalent) only in repos that track project-specific automation.
