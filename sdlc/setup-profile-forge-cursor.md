---
nav_title: "Setup profile: Forge and Cursor"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Project setup profile — Forge and Cursor (steps 4–11)

## What it is

The middle phase of the [Project setup profile](SETUP.md): **Forge** workspace, **Cursor** rules, optional **tasklets** and **Skills**, and **validation**.

## When to use it

After [Bootstrap](setup-profile-bootstrap.md) (steps 1–3).

## Prerequisites

- Steps 1–3 complete or equivalent from [First hour](quickstarts/first-hour.md).

## Steps

4. **Forge workspace** — `./blueprints/sdlc/methodologies/forge/setup/forge-init.sh`  
   Creates `forge/`, `ember-logs/`, seeds `forge/forge.config.yaml`.
5. **Configure Forge in YAML** — Edit `forge/forge.config.yaml`; questionnaire: [`methodologies/forge/setup/QUESTIONNAIRE.md`](methodologies/forge/setup/QUESTIONNAIRE.md).
6. **Cursor — install rules** — From repo root: `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended` (see [`methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md`](methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md)). YAML-only / CI: `… sync` with no `--preset`. Or copy manually — [`methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md`](methodologies/forge/setup/CURSOR-RULES-ALIGNMENT.md).
7. **Cursor — optional extras** — `--preset full` or individual `--with-*` flags add more rules; see alignment doc **Reference: granular flags**. After `git submodule update` on `blueprints/`, run `sync-forge-cursor-rules.sh diff --preset recommended` (or `status`) before `sync … --force`.
8. **Cursor — tasklets + Sampling (optional)** — `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`
9. **Optional Skills** — Copy from [`templates/forge/cursor-skills/`](templates/forge/cursor-skills/) into `.cursor/skills/`.
10. **Validate alignment** — `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check` (Python 3 + PyYAML; [`versona_cursor_rules.py`](methodologies/forge/setup/versona_cursor_rules.py) `check` — same map as YAML-driven install).
11. **Operational start** — [Forge scripts overview](methodologies/forge/scripts/README.md); [Forge workspace template](templates/forge/README.template.md) for a filled-in consumer layout.

### Cursor: Project Setup Versona

- **Template:** [`methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template`](methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template) → `.cursor/rules/versona-project-setup.mdc`
- **Trigger:** **`setup`** or `@versona-project-setup` — checklist and gap analysis (pair with **`@forge-setup`** from [`methodologies/forge/setup/forge-setup.mdc.template`](methodologies/forge/setup/forge-setup.mdc.template) for the questionnaire).

## How to verify success

- After steps 4–5: `forge/forge.config.yaml` exists as in [first hour](quickstarts/first-hour.md).
- After steps 6–10: `sync-forge-cursor-rules.sh check` passes when you use the recommended preset; CI still green if you gate on it.

## What to do next

- [Setup profile: Optional product-led](setup-profile-optional-product.md) (step 12)
- [`methodologies/forge/setup/README.md`](methodologies/forge/setup/README.md)
- [`methodologies/forge/versona/README.md`](methodologies/forge/versona/README.md)
