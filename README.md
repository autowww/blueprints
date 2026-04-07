# Blueprints

**Blueprints** is a reusable **SDLC / PDLC / discipline** framework you embed in a product repository: frozen baseline text under `blueprints/`, plus **your** project workspace (`sdlc/`, `docs/`, `forge/`, …). This page is the **handbook home** — written for **teams adopting and using** the framework, not for touring the upstream repo layout.

## When to use this handbook

Use this page when you need **what Blueprints is**, **who it is for**, and **where to go next** in the published handbook — not a map of every upstream folder or maintainer workflow.

## What it is

- Prescriptive **lifecycle** and **discipline** packages (Markdown) you consume as a **submodule** (or copy).
- Optional **Forge** (artifacts, logs, Versonas) and **Cursor** alignment on top of the same baseline.
- A **published handbook** at [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com/) — the same Markdown as this repository, formatted for reading in the browser.

## Who it is for

| You are… | Start with |
|-----------|-------------|
| Choosing how much process to take on | [**Adopting Blueprints**](sdlc/adopting-blueprints.md) — ICP-style paths A / B / C |
| Ready to run commands in a repo | [**First hour**](sdlc/quickstarts/first-hour.md) — submodule, `sdlc/` workspace, Forge init, Cursor rules |
| Standardizing setup end-to-end | [**Project setup profile**](sdlc/SETUP.md) — full ordered checklist with verification |

## Get started

1. [**Adopting Blueprints**](sdlc/adopting-blueprints.md) — what to optimize for (solo, team, org).
2. [**First hour**](sdlc/quickstarts/first-hour.md) — concrete steps and checks (~60 minutes).
3. [**Set up in your repo**](sdlc/SETUP.md) — submodule through optional product-led paths.

**Also useful:** [Quickstarts hub](sdlc/quickstarts/README.md) · [Updating the submodule](sdlc/updating-blueprints-submodule.md) · [Troubleshooting / FAQ](sdlc/troubleshooting-faq.md)

## Use the framework in practice

| Topic | Handbook entry |
|--------|------------------|
| **SDLC** (phases, DoD, methodologies) | [SDLC blueprint](sdlc/README.md) |
| **PDLC** (discovery → sunset around delivery) | [PDLC blueprint](pdlc/README.md) |
| **Disciplines** (engineering, product, data, security, …) | [Disciplines hub](disciplines/README.md) |
| **Forge + Cursor** (workflows, rules, tasklets) | [Forge methodology](sdlc/methodologies/forge.md) and [setup](sdlc/methodologies/forge/setup/README.md) |
| **Team rollout** | [Team rollout patterns](sdlc/team-rollout.md) |
| **Advanced customization (301)** | [Advanced customization](sdlc/advanced-customization.md) — safe extension points in *your* repo |

## Frozen vs editable

- **`blueprints/**`** (this submodule) is the **frozen baseline** — change only via the [package policy](sdlc/POLICY.md) process.
- **`sdlc/`**, **`docs/`**, **`forge/`** at your **repository root** are **yours** — interpretations, directives, project docs.

## Companion sites

| Site | Role |
|------|------|
| [forge-lenses on the handbook](https://blueprints.forgesdlc.com/lenses/index.html) | Workspace dashboard, Forge Studio companion (separate repo) |
| [Design system](https://blueprints.forgesdlc.com/ks/index.html) | Shared Forge theme and diagram primitives |
| [Blog](https://blueprints.forgesdlc.com/blog/) | Short framework articles |

**Full repo layout** (folder-by-folder map) lives with the source on [GitHub](https://github.com/autowww/blueprints) — use it when you are browsing the submodule tree, not as a first-day adoption read.

## Maintainers

Roadmap, WBS, design principles, and generator notes live under [`docs/`](https://github.com/autowww/blueprints/tree/main/docs) on GitHub — not part of the adoption-first handbook story.

## Blog and community

- [**Blog**](blog/README.md) — articles mirrored to [blueprints.forgesdlc.com/blog/](https://blueprints.forgesdlc.com/blog/)
- [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md) · [License](LICENSE)
