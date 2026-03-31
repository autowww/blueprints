# Adopting Blueprints

**Hands-on first hour (commands and checks):** use [Quickstarts — First hour](../sdlc/quickstarts/first-hour.md). This page is for **which adopter story** you match — not step-by-step setup.

Blueprints is a **reusable documentation framework** (SDLC, PDLC, disciplines, Forge/Versona patterns). This page is the **shortest path** from interest to a working layout in *your* repository.

## Before you start

1. Add Blueprints as a **git submodule** at `blueprints/` (or copy the tree if you do not use submodules). See the root [README](../README.md) § *Adopt in your repo*.
2. Decide your **ICP path** below — the same codebase serves different jobs.

## ICP paths

### A — Solo developer or small team

**Job to be done:** “I want a sane default SDLC/PDLC text baseline without writing it from scratch.”

1. Submodule Blueprints under `blueprints/`.
2. Add a **project** `sdlc/` folder (interpretations, principles) — do **not** edit `blueprints/sdlc/` (frozen baseline); see [`sdlc/POLICY.md`](../sdlc/POLICY.md).
3. Add `docs/product/` when you are ready for capabilities/journeys (seed from [`product/templates/`](../product/templates/README.md)).

### B — Team lead / EM

**Job to be done:** “I need a shared vocabulary for phases, ceremonies, and discipline bridges across repos.”

1. Complete path **A**.
2. Point the team at [`sdlc/README.md`](../sdlc/README.md) and the methodology slice you follow (e.g. Scrum, Kanban, Forge) under `blueprints/sdlc/methodologies/`.
3. Optionally wire **Forge** artifacts (`forge/`, `forge-logs/`) using templates under `blueprints/sdlc/templates/forge/` in a **consumer** repo.

### C — Organization method / platform group

**Job to be done:** “We want a single upstream corpus we can submodule into many products and keep in sync.”

1. Treat `autowww/blueprints` as **upstream**; fork only if you must diverge on policy.
2. Maintain a **consumer** playbook (submodule bump cadence, POLICY exceptions if any).
3. Read [`product/discovery/framework-positioning-and-mvp.md`](product/discovery/framework-positioning-and-mvp.md) for category positioning when briefing leadership.

## Maintainer cross-links

- [Roadmap](ROADMAP.md) — what we ship next for the framework *product*.
- [Positioning & MVP](product/discovery/framework-positioning-and-mvp.md) — why **Adoption spine v1** is the first Product Spark.

## Sites

- **Handbook (HTML):** [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com) — generated from this repo; see [`MAINTENANCE.md`](MAINTENANCE.md).
- **Wiki mirror:** [GitHub Wiki](https://github.com/autowww/blueprints/wiki) — [`wiki-source/sync-wiki.sh`](../wiki-source/sync-wiki.sh).
