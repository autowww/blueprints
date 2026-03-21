# IDE agent instructions blueprint

Templates and bootstrap tooling for **IDE-based AI coding agents** (Cursor, Claude Code). This package projects the SDLC methodology from [`blueprints/sdlc/`](../sdlc/README.md) into the **native instruction formats** that AI agents consume: rules, skills, commands, project-level instruction files, and plan conventions.

**Governance:** read [`POLICY.md`](POLICY.md) — **do not change** this directory unless explicitly updating the baseline. Project-level instruction files live in `.cursor/`, `.claude/`, and root `AGENTS.md` / `CLAUDE.md` after bootstrap.

| Deliverable | Purpose |
|-------------|---------|
| [**POLICY.md**](POLICY.md) | Immutability rules for this blueprint. |
| [**STRUCTURE.md**](STRUCTURE.md) | Vendor feature matrix, what maps where, how templates become project files. |
| [**templates/**](templates/README.md) | All template files: vendor-neutral root instructions, Cursor rules/commands, Claude skills/agents, plan convention. |
| [**scripts/**](scripts/README.md) | `init-ide-workspace.sh` — bootstrap IDE instruction files for a project. |
| [**docs/**](docs/README.md) | Handbook chapter source; keep in sync with `blueprints/sdlc/docs/ide.html`. |

## What does *not* belong here

- API keys, tokens, `.env` with secrets — use project-level gitignored files and CI secret stores.
- Application source code — stays in your product tree.
- Frozen SDLC text — **`blueprints/sdlc/`** only.
- Docker automation — **`blueprints/agents/`** only.

## How to adopt

1. Keep this folder at **repository root** as **`blueprints/ide/`** (or via the blueprints submodule).
2. Run from the repository root:

   ```bash
   ./blueprints/ide/scripts/init-ide-workspace.sh "My Product Name"
   ```

3. This creates `.cursor/rules/`, `.cursor/commands/`, `.cursor/plans/`, `.claude/skills/`, `.claude/agents/`, root `AGENTS.md`, and root `CLAUDE.md`.
4. **Customize** the generated files for your project: fill in build/test commands, adjust rules to your stack, add project-specific instructions.
5. Optional flags: `--cursor-only` (skip Claude files), `--claude-only` (skip Cursor files), `--force` (overwrite existing).

## Relationship to other blueprints

| Package | Concern |
|---------|---------|
| [`sdlc/`](../sdlc/README.md) | Process methodology, phases, ceremonies, spec-driven, agentic governance |
| [`docs/`](../docs/README.md) | Product-functional documentation IA |
| [`agents/`](../agents/README.md) | Docker containers, recipe scaffolding, Compose patterns |
| **`ide/`** (this) | IDE agent instructions — how AI assistants follow the process |

The `sdlc/` package defines **what** teams do; `ide/` projects **how AI agents learn and follow** that process in Cursor and Claude Code.

---

*Blueprint — no project-specific content.*
