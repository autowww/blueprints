# Blueprints

Reusable **documentation and process packages** for software projects — organized into **lifecycles** (when work happens), **disciplines** (cross-cutting professional competencies grouped into families), and **support** packages (tooling and infrastructure).

### Lifecycles

| Package | Purpose |
|---------|---------|
| [**sdlc/**](sdlc/README.md) | Software delivery lifecycle: phases A–F, Definition of Done, methodologies, ceremonies, HTML handbook |
| [**pdlc/**](pdlc/README.md) | Product development lifecycle: discovery, validation, strategy, launch, growth, sunset — wraps around SDLC |

### Disciplines

Cross-cutting professional competencies organized into **four families** and **two cross-cutting standalone disciplines**. Hub: [`disciplines/README.md`](disciplines/README.md). Each discipline has a **bridge document** mapping its practices to SDLC and PDLC — see [`BRIDGES.md`](BRIDGES.md).

#### Engineering — how we build software

| Package | Purpose |
|---------|---------|
| [**disciplines/engineering/software-engineering/**](disciplines/engineering/software-engineering/README.md) | Software engineering: paradigms, algorithms, design patterns, SOLID, clean code, concurrency, networking |
| [**disciplines/engineering/software-architecture/**](disciplines/engineering/software-architecture/README.md) | Software architecture: quality attributes, viewpoints, ADRs, patterns — structures systems |
| [**disciplines/engineering/devops/**](disciplines/engineering/devops/README.md) | DevOps: CALMS, DORA metrics, SRE, CI/CD, observability — bridges dev and ops |
| [**disciplines/engineering/testing/**](disciplines/engineering/testing/README.md) | Testing & QA: ISTQB-aligned approaches, test automation landscape — verifies correctness |
| [**disciplines/engineering/frontend/**](disciplines/engineering/frontend/README.md) | Frontend / web engineering: component architecture, rendering, performance, design systems — web UIs |
| [**disciplines/engineering/mobile/**](disciplines/engineering/mobile/README.md) | Mobile engineering: native/cross-platform, offline-first, app store lifecycle — mobile experiences |
| [**disciplines/engineering/embedded-iot/**](disciplines/engineering/embedded-iot/README.md) | Embedded / IoT: real-time systems, firmware, protocols, OTA, safety-critical — constrained devices |

#### Data — how we handle information at scale

| Package | Purpose |
|---------|---------|
| [**disciplines/data/bigdata/**](disciplines/data/bigdata/README.md) | Big data & data engineering: data governance, pipeline patterns, DataOps — data at scale |
| [**disciplines/data/data-science/**](disciplines/data/data-science/README.md) | Data science & ML: CRISP-DM, MLOps, model evaluation, responsible AI — models from data |

#### Product — how we understand users, design experiences, and grow

| Package | Purpose |
|---------|---------|
| [**disciplines/product/ba/**](disciplines/product/ba/README.md) | Business analysis: BABOK knowledge areas, techniques, perspectives — spans PDLC and SDLC |
| [**disciplines/product/ux-design/**](disciplines/product/ux-design/README.md) | UX / UI Design: design thinking, interaction design, visual design, accessibility — makes products usable |
| [**disciplines/product/marketing/**](disciplines/product/marketing/README.md) | Marketing: digital channels, growth engineering, positioning, analytics, GTM — acquires and retains users |
| [**disciplines/product/customer-success/**](disciplines/product/customer-success/README.md) | Customer success: onboarding, health scoring, support, feedback loops, churn prevention — keeps users succeeding |

#### Governance — how we manage and improve delivery

| Package | Purpose |
|---------|---------|
| [**disciplines/governance/pm/**](disciplines/governance/pm/README.md) | Project management: process groups, governance, knowledge areas, metrics — governs delivery |

#### Cross-cutting

| Package | Purpose |
|---------|---------|
| [**disciplines/security/**](disciplines/security/README.md) | Security: threat modeling, OWASP, auth patterns, incident response — protects products |
| [**disciplines/compliance/**](disciplines/compliance/README.md) | Compliance: GDPR, HIPAA, PCI-DSS, WCAG, SOC 2, AI Act, ISO 27001 — meets regulatory obligations |

### Support

| Package | Purpose |
|---------|---------|
| [**product/**](product/README.md) | Product-functional documentation blueprint (capabilities, journeys, specs) |
| [**agents/**](agents/README.md) | Optional Docker/recipe templates for repeatable automation |
| [**wiki-source/**](wiki-source/README.md) | Scripts to sync a [GitHub Wiki](https://github.com/autowww/blueprints/wiki) mirror of the Markdown |

**Canonical source** is this repository on `main`. The wiki is a convenience mirror—refresh it with [`wiki-source/sync-wiki.sh`](wiki-source/sync-wiki.sh) when you have push access to the wiki remote.

## Published handbook site (Forge)

The static handbook at [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com/) is generated from this repo’s Markdown (see the **blueprints-website** consumer). The same site also publishes companion docs from adjacent repositories:

- [forge-lenses](https://blueprints.forgesdlc.com/lenses/index.html) — workspace dashboard (`docs/` + `lenses/website/` merged for navigation)
- [Kitchensink and forge-autodoc](https://blueprints.forgesdlc.com/ks/index.html) — shared design system and Markdown→HTML handbook builder shipped inside **forgesdlc-kitchensink**

## Get started (handbook)

Use the static site at [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com/) — same content as this repo’s Markdown, built by the **blueprints-website** project.

| Goal | Start here |
|------|------------|
| **First hour in a repo** | [Quickstarts](sdlc/quickstarts/README.md) — submodule, `sdlc/` workspace, Forge, Cursor |
| **Which adopter path fits you?** | [Adopting Blueprints](docs/ADOPTION.md) — ICP paths A / B / C |
| **What ships next** | [Roadmap](docs/ROADMAP.md) — maintainers |
| **Positioning & MVP** | [Framework positioning & first MVP](docs/product/discovery/framework-positioning-and-mvp.md) |
| **Work breakdown** | [WBS](docs/requirements/WBS.md) |
| **Docs index** | [Framework docs index](docs/INDEX.md) |

## Adopt in your repo

Copy or add as a **git submodule** under `blueprints/`, then bootstrap project-specific folders (e.g. `sdlc/`, `docs/product/`) using the scripts and templates linked from each package README.

## Community

- [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md) · [License](LICENSE)
