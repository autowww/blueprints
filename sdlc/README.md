# SDLC blueprint

This folder is a **reusable, product-agnostic** package: **process** (phases, Definition of Done) and **documentation conventions**. Copy or submodule it into any repository.

**Governance:** read [`POLICY.md`](POLICY.md) — **do not change** this directory unless explicitly updating the baseline. Project work lives in **`sdlc/`** (or equivalent) and **`docs/`**.

| Deliverable | Purpose |
|-------------|---------|
| [**POLICY.md**](POLICY.md) | Immutability rules for this blueprint. |
| [**SDLC.md**](SDLC.md) | Phases A–F, documentation obligations, Definition of Done, change control. |
| [**DOCUMENTATION-STRUCTURE.md**](DOCUMENTATION-STRUCTURE.md) | Suggested `docs/` layout, document types, conventions, evolution notes. |
| [**docs/**](docs/README.md) | **Human handbook** ([`index.html`](docs/index.html) + chapter pages, incl. optional [`methodologies.html`](docs/methodologies.html)) — HTML + diagrams; keep in sync per [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) when Markdown sources change. |
| [**templates/**](templates/README.md) | Optional copy-paste starters: `docs/` (`ROADMAP`, `TEST-PLAN`) and **`sdlc/`** workspace (`README` + `TRACKING-*`) — not required to run the SDLC. |
| [**Agents blueprint (optional)**](../agents/README.md) | Frozen **`blueprints/agents/`** — Docker base image, Compose, recipe templates for repeatable automation (alongside IDE/LLM workflows); mutable **`agents/`** at repo root. **Handbook:** [`docs/agents.html`](docs/agents.html); canonical: [`blueprints/agents/STRUCTURE.md`](../agents/STRUCTURE.md). |
| [**SDLc-WORKSPACE.md**](SDLc-WORKSPACE.md) | How to **initialize** `sdlc/` from [`templates/sdlc/`](templates/sdlc). |
| [**scripts/**](scripts/README.md) | **`init-sdlc-workspace.sh`** — bootstrap `sdlc/` + `TRACKING-*.md` (requires `bash`, `python3`). |
| [**methodologies/**](methodologies/README.md) | **Deep guides** — **roles & archetypes**, **ceremonies** (foundation + Scrum/Kanban/phased/XP forks), Scrum, Kanban, phased delivery, XP, Agile umbrella, **spec-driven development**, agentic SDLC; external links + blueprint mapping; handbook [hub](docs/methodologies.html) + `methodologies-*.html` + [spec-driven](docs/spec-driven.html). |

**Optional (consuming repo only, not in this folder):** some projects add **`sdlc/TRACKING-FOUNDATION.md`**, **`TRACKING-METHODOLOGIES.md`**, **`TRACKING-CHALLENGES.md`** next to **`sdlc/README.md`** — a single engineering-tracking model, methodology-specific lenses, and caveats. The [handbook `index.html`](docs/index.html) landing page links to those files when present (relative paths); they are **not** part of the frozen blueprint text.

## What does *not* belong here

- Product name, stack, **living** planning data, compliance targets, or requirement IDs — use a **project profile** (e.g. `docs/PROJECT.md`) and a **requirements** / backlog area (e.g. `docs/requirements/`) in the consuming repo.
- Filled-in roadmap or WBS — those live under `docs/` (or your tool), not in `blueprints/sdlc/`.

## How to adopt

1. Keep this folder at **repository root** as **`blueprints/sdlc/`** (or copy the subtree into a new repo).  
2. Add a **`sdlc/`** folder for **project-specific** SDLC links and notes—never put that in the blueprint. **Bootstrap it** from [`templates/sdlc/`](templates/sdlc) using [`SDLc-WORKSPACE.md`](SDLc-WORKSPACE.md) (includes `README.md` + optional `TRACKING-*.md` + handbook links).  
3. From your root `README.md` or `docs/INDEX.md`, link to **`blueprints/sdlc/README.md`** and **`sdlc/README.md`** (and to tracking docs if you use them).  
4. Add `docs/PROJECT.md` (or equivalent) for context; keep **`blueprints/sdlc/`** free of those details.  
5. **Roadmap:** You do **not** need a separate roadmap doc for the SDLC to apply—**`SDLC.md` + `DOCUMENTATION-STRUCTURE.md` + your backlog/WBS** are enough. If you want a milestone/epic table, copy [`templates/ROADMAP.template.md`](templates/ROADMAP.template.md) to `docs/ROADMAP.md`.  
6. **Optional — agents & automation:** Copy or submodule **[`blueprints/agents/`](../agents/README.md)** next to this folder; run **`./blueprints/agents/scripts/init-agents-workspace.sh`** (or seed **`agents/`** manually from [`blueprints/agents/templates/project-agents/`](../agents/templates/project-agents/README.md)). Link to **`blueprints/sdlc/docs/agents.html`** from `docs/INDEX.md` when adopted. Methodology for agentic delivery: [`methodologies/agentic-sdlc.md`](methodologies/agentic-sdlc.md).

## GitHub Wiki (Markdown mirror)

The **[autowww/blueprints Wiki](https://github.com/autowww/blueprints/wiki)** mirrors most blueprint `*.md` (including [`methodologies/ceremonies/`](methodologies/ceremonies/README.md)) for browser reading. **Canonical** text stays in this repo; refresh the wiki from a clone of **`autowww/blueprints`** with [`../wiki-source/sync-wiki.sh`](../wiki-source/sync-wiki.sh) — see [`../wiki-source/README.md`](../wiki-source/README.md).

---

*Blueprint — no project-specific content.*
