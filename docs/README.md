# Documentation blueprint

Templates and bootstrap tooling for the **entire `docs/` tree**: product-functional prose, requirements & WBS, architecture, ADRs, development, CI/CD, testing, release, security, and operations. This package projects the documentation information architecture from [`blueprints/sdlc/DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md) into **ready-to-use templates** that the init script copies into a project.

**Governance:** read [`POLICY.md`](POLICY.md) — **do not change** this directory unless explicitly updating the baseline. Project content lives under **`docs/`** (mutable) in the consuming repo after bootstrap.

| Deliverable | Purpose |
|-------------|---------|
| [**POLICY.md**](POLICY.md) | Immutability rules for this blueprint. |
| [**STRUCTURE.md**](STRUCTURE.md) | Full `docs/` IA: layout, document types, conventions, bootstrap instructions. |
| [**templates/**](templates/README.md) | All template files for the complete `docs/` tree. |
| [**scripts/**](scripts/README.md) | `init-docs-workspace.sh` — bootstrap `docs/` for a project. |
| [**docs/**](docs/README.md) | **Human handbook** ([`index.html`](docs/index.html)) — HTML summary; sync per [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md). |

## What does *not* belong here

- Product name, filled-in journeys, or **living** content — use **`docs/`** (mutable) in the consuming repo.
- SDLC phases, CI gates, or process methodology — **`blueprints/sdlc/`**.
- IDE agent instructions — **`blueprints/ide/`**.
- Docker automation — **`blueprints/agents/`**.

## How to adopt

1. Keep this folder at **repository root** as **`blueprints/docs/`** (or via the blueprints submodule).
2. Run from the repository root:
   ```bash
   ./blueprints/docs/scripts/init-docs-workspace.sh "My Product Name"
   ```
3. This creates `docs/INDEX.md`, `docs/PROJECT.md`, `docs/ROADMAP.md`, product templates, requirements structure (STRUCTURE-PROPOSAL, INDEX, WBS, risks, traceability), ADR, architecture, development, CI-CD, testing, release, security, and operations placeholders.
4. **Customize** the generated files for your project: fill in stack details, confirm ID scheme, remove areas you don't need yet.
5. Use `--force` to overwrite existing files when upgrading to a newer template version.

## Relationship to other blueprints

| Package | Concern |
|---------|---------|
| [`sdlc/`](../sdlc/README.md) | Process methodology, phases, ceremonies, doc obligations |
| [`ide/`](../ide/README.md) | IDE agent instructions (Cursor rules, Claude skills) |
| [`agents/`](../agents/README.md) | Docker containers, recipe scaffolding, Compose patterns |
| **`docs/`** (this) | Documentation IA — templates for the entire `docs/` tree |

The `sdlc/` package defines **what** documentation to produce at each phase; `docs/` provides **the templates** to produce it.

---

*Blueprint — no project-specific content.*
