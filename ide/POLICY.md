# Blueprint policy — IDE agent instructions

This directory **`blueprints/ide/`** is the **frozen** IDE agent instruction package: templates for `.cursor/rules/`, `CLAUDE.md`, `AGENTS.md`, commands, skills, and plan conventions meant to be **reused and compared** across projects.

## Rules

1. **Do not edit** files here as part of normal product work.
2. **Change only when explicitly requested** — e.g. adopting a new blueprint version, adding a vendor feature, or a deliberate policy decision to revise the baseline.
3. **Day-to-day customization** belongs in the project's own `.cursor/rules/`, `CLAUDE.md`, `AGENTS.md`, etc. — the mutable copies produced by `init-ide-workspace.sh`.
4. If you change templates here, **update the handbook chapter** in `blueprints/sdlc/docs/ide.html` per `blueprints/sdlc/docs/MAINTENANCE.md`.

## Relationship to project files

- **`blueprints/ide/`** — canonical, generic templates (immutable by convention).
- **`.cursor/`**, **`.claude/`**, **`AGENTS.md`**, **`CLAUDE.md`** (project root) — where this project **copies, interprets, and extends** the templates without touching the blueprint.

Copying this repo: you may copy **`blueprints/ide/`** wholesale to another repository; use the init script to seed project-level files, then customize freely.
