# Blueprints

Reusable **documentation and process packages** for software projects: SDLC conventions, product-functional doc structure, and optional agents/automation layout.

| Package | Purpose |
|--------|---------|
| [**sdlc/**](sdlc/README.md) | Phases, Definition of Done, methodologies, ceremonies, HTML handbook |
| [**docs/**](docs/README.md) | Product-functional documentation blueprint (capabilities, journeys, specs) |
| [**agents/**](agents/README.md) | Optional Docker/recipe templates for repeatable automation |
| [**wiki-source/**](wiki-source/README.md) | Scripts to sync a [GitHub Wiki](https://github.com/autowww/blueprints/wiki) mirror of the Markdown |

**Canonical source** is this repository on `main`. The wiki is a convenience mirror—refresh it with [`wiki-source/sync-wiki.sh`](wiki-source/sync-wiki.sh) when you have push access to the wiki remote.

## Adopt in your repo

Copy or add as a **git submodule** under `blueprints/`, then bootstrap project-specific folders (e.g. `sdlc/`, `docs/product/`) using the scripts and templates linked from each package README.

## Community

- [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md) · [License](LICENSE)
