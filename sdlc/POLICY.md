---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Blueprint policy — do not change casually

This directory **`blueprints/sdlc/`** is the **frozen** SDLC package: process and documentation conventions meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal product work (features, docs under `docs/`, WBS updates, etc.).  
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, fixing an upstream template bug, or a deliberate policy decision to revise the baseline.  
3. **Day-to-day project work** belongs in **`sdlc/`** (this repo’s SDLC workspace) and **`docs/`** (requirements, roadmap, profile, etc.).  
4. If you change **`SDLC.md`**, **`DOCUMENTATION-STRUCTURE.md`**, **`methodologies/*.md`**, or related blueprint files, ensure **publishable** Markdown is refreshed on **blueprints.forgesdlc.com** per [`docs/DESIGN-PRINCIPLES.md`](../docs/DESIGN-PRINCIPLES.md) and [`docs/MAINTENANCE.md`](../docs/MAINTENANCE.md) — update the **human handbook** in **`blueprints/sdlc/docs/`** (chapter `*.html`, SVGs as needed) when applicable, per **`blueprints/sdlc/docs/MAINTENANCE.md`**. When **`blueprints/agents/`** in the same repository changes, align **`blueprints/sdlc/docs/agents.html`** with **`blueprints/agents/STRUCTURE.md`**.

## Relationship to `sdlc/`

- **`blueprints/sdlc/`** — canonical, generic text (immutable by convention).  
- **`sdlc/`** — where this project **links, interprets, and extends** the SDLC without touching the blueprint.

Copying this repo: you may copy **`blueprints/sdlc/`** wholesale to another repository; use **`sdlc/`** (or equivalent) only in repos that track project-specific SDLC notes.
