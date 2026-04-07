---
nav_title: Project setup profile
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Project setup profile (consuming repository)

## What it is

The **full ordered checklist** for a product repository that hosts **`blueprints/` at the repository root** (typically a git submodule): submodule through optional Forge and product-led flows, with the same assumptions as the [first-hour quickstart](quickstarts/first-hour.md), but in one place.

You may copy this file to your project root as `SETUP.md` if you want a local checklist.

| Field | Value |
|-------|--------|
| **Profile version** | 1.0 |
| **Last reviewed** | 2025-03-24 |
| **Blueprints submodule** | Record `git rev-parse HEAD` inside `blueprints/` after `git submodule update` |

**Layout reference:** full consuming-repo doc tree (optional detail) — [`DOCUMENTATION-STRUCTURE.md` on GitHub](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md).

### Setup phases (map of the numbered steps)

| Phase | Steps (see below) | Required? | Outcome |
|-------|-------------------|-----------|---------|
| **Bootstrap** | 1–3 | Required | `blueprints/` on disk, `docs/` as needed, project **`sdlc/`** workspace |
| **Forge** | 4–5 | Required for Forge adoption | `forge/forge.config.yaml` and related paths |
| **Cursor + automation** | 6–11 | Required if you use Cursor rules / tasklets | Rules aligned; optional tasklets and Skills installed |
| **Product-led (optional)** | 12 | Optional | Product bootstrap artifacts per methodology |

**Depth profiles:** **Minimum** = phases Bootstrap + Forge through a working `forge.config.yaml`. **Recommended** = through step 10 (`sync-forge-cursor-rules.sh check` clean). **Full** = all rows including optional product-led flows.

## When to use it

Use this page when you are **standardizing setup end-to-end** after you already know you will use Blueprints at the repo root.

**Before you start:** if you have not chosen an adoption story yet, skim [**Adopting Blueprints**](adopting-blueprints.md). For a faster guided pass with verification after each step, use [Quickstarts — First hour](quickstarts/first-hour.md) first, then return here for anything you skipped.

## Prerequisites

- **`blueprints/`** must sit at the **repository root** next to `forge/`, `sdlc/`, `docs/`, etc. Scripts such as [`methodologies/forge/setup/forge-init.sh`](methodologies/forge/setup/forge-init.sh) and [`methodologies/forge/tasklets/install-tasklets.sh`](methodologies/forge/tasklets/install-tasklets.sh) use paths like `blueprints/sdlc/...` from the current working directory (repo root).
- If your org cannot use that layout, you need **wrapper scripts** or forks that adjust paths — the stock blueprints tooling does **not** support a configurable `BLUEPRINTS_ROOT`.

## Steps

1. **Submodule** — Ensure `blueprints/` is present; `git submodule update --init` so `blueprints/sdlc` exists.
2. **Documentation tree (as needed)** — Create `docs/` per the [layout template on GitHub](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md).
3. **Project `sdlc/` workspace** — From repo root:  
   `./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name"`  
   Context and layout: [`SDLc-WORKSPACE.md`](SDLc-WORKSPACE.md).
4. **Forge workspace** — `./blueprints/sdlc/methodologies/forge/setup/forge-init.sh`  
   Creates `forge/`, `ember-logs/`, seeds `forge/forge.config.yaml`.
5. **Configure Forge in YAML** — Edit `forge/forge.config.yaml`; questionnaire: [`methodologies/forge/setup/QUESTIONNAIRE.md`](methodologies/forge/setup/QUESTIONNAIRE.md).
6. **Cursor — install rules** — From repo root: `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended` (see [`methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md`](methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md)). YAML-only / CI: `… sync` with no `--preset`. Or copy manually — [`methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md`](methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md).
7. **Cursor — optional extras** — `--preset full` or individual `--with-*` flags add more rules; see alignment doc **Reference: granular flags**. After `git submodule update` on `blueprints/`, run `sync-forge-cursor-rules.sh diff --preset recommended` (or `status`) before `sync … --force`.
8. **Cursor — tasklets + Sampling (optional)** — `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`
9. **Optional Skills** — Copy from [`templates/forge/cursor-skills/`](templates/forge/cursor-skills/) into `.cursor/skills/`.
10. **Validate alignment** — `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check` (Python 3 + PyYAML; [`versona_cursor_rules.py`](methodologies/forge/setup/versona_cursor_rules.py) `check` — same map as YAML-driven install).
11. **Operational start** — [Forge scripts overview](methodologies/forge/scripts/README.md); [Forge workspace template](templates/forge/README.template.md) for a filled-in consumer layout.
12. **Optional product-led path** — [`methodologies/forge/product-manager/README.md`](methodologies/forge/product-manager/README.md), [`methodologies/forge/product-manager/product-bootstrap-flow.md`](methodologies/forge/product-manager/product-bootstrap-flow.md).

### Cursor: Project Setup Versona

- **Template:** [`methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template`](methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template) → `.cursor/rules/versona-project-setup.mdc`
- **Trigger:** **`setup`** or `@versona-project-setup` — checklist and gap analysis (pair with **`@forge-setup`** from [`methodologies/forge/setup/forge-setup.mdc.template`](methodologies/forge/setup/forge-setup.mdc.template) for the questionnaire).

## How to verify success

- After step 1: `test -f blueprints/sdlc/README.md` from repo root.
- After steps 3–4: project `sdlc/README.md` and `forge/forge.config.yaml` exist as in [first hour](quickstarts/first-hour.md).
- After steps 6–10: `sync-forge-cursor-rules.sh check` passes when you use the recommended preset; CI still green if you gate on it.
- After step 12 (if used): product bootstrap artifacts exist per the linked methodology docs.

## What to do next

- [`methodologies/forge/setup/README.md`](methodologies/forge/setup/README.md) — adoption entry point  
- [`methodologies/forge/versona/README.md`](methodologies/forge/versona/README.md) — Versona catalog