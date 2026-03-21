# Blueprints

Reusable **documentation and process packages** for software projects: SDLC conventions, product-functional doc structure, and optional agents/automation layout.

| Package | Purpose |
|--------|---------|
| [**sdlc/**](sdlc/README.md) | Phases, Definition of Done, methodologies, ceremonies, HTML handbook |
| [**docs/**](docs/README.md) | Documentation blueprint — templates for the full `docs/` tree (product, requirements, ADR, engineering) |
| [**agents/**](agents/README.md) | Optional Docker/recipe templates for repeatable automation |
| [**ide/**](ide/README.md) | IDE agent instruction templates (Cursor rules, Claude skills, commands, plan convention) |
| [**wiki-source/**](wiki-source/README.md) | Scripts to sync a [GitHub Wiki](https://github.com/autowww/blueprints/wiki) mirror of the Markdown |

**Canonical source** is this repository on `main`. The wiki is a convenience mirror—refresh it with [`wiki-source/sync-wiki.sh`](wiki-source/sync-wiki.sh) when you have push access to the wiki remote.

## Adopt in your repo

Copy or add as a **git submodule** under `blueprints/`, then bootstrap project-specific folders using the init scripts:

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name"   # → sdlc/
./blueprints/docs/scripts/init-docs-workspace.sh "Project Name"    # → docs/
./blueprints/ide/scripts/init-ide-workspace.sh  "Project Name"     # → .cursor/, .claude/, AGENTS.md, CLAUDE.md
```

See each package README for details and options.

## Community

- [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md) · [License](LICENSE)
