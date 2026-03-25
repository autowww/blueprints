# Forge workspace

Project-specific Forge SDLC workspace. This directory contains mutable Forge artifacts — Charge files, Ember Logs, journals, release plans, and configuration.

**Methodology:** [`blueprints/sdlc/methodologies/forge.md`](../blueprints/sdlc/methodologies/forge.md)

## Structure

| Path | Purpose |
|------|---------|
| `forge/forge.config.yaml` | Project Forge configuration |
| `forge/charge.md` | Current daily Charge |
| `forge/charge-archive/` | Archived Charge files |
| `forge/journal/` | Day journals (`YYYY-MM-DD.md`) |
| `forge/releases/` | Product Spark release plans |
| `forge-logs/` | Spark journals, DoD notes; **Versona sessions** under `forge-logs/versona/<actor>/<session-id>/` (see `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §7) |
| `ember-logs/` | Ember Log entries (`YYYY-MM-DD.md`) |

## Scripts

Run from repository root:

```bash
# Daily Charge
./blueprints/sdlc/methodologies/forge/scripts/forge-charge.sh [show|new|done ID|block ID|bank ID]

# Ember Log
./blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh "Decision summary"

# Day journal
./blueprints/sdlc/methodologies/forge/scripts/forge-journal.sh [new|commit]

# Versona session folder (optional)
./blueprints/sdlc/methodologies/forge/scripts/forge-versona-session.sh <actor> [session-id] [--with-yaml-manifest]

# Status
./blueprints/sdlc/methodologies/forge/scripts/forge-status.sh
```

## Cursor rules

Active Forge rules in `.cursor/rules/`:

| Rule | Purpose |
|------|---------|
| `forge-daily.mdc` | Daily operations: Charge, hats, Ember Log, journal |
| `forge-planning.mdc` | Product planning: Ore, Product Sparks, iterations |
| `forge-setup.mdc` | Setup wizard (can be removed after initial setup) |
| `forge-versona.mdc` | Master Versona routing |
| `versona-generic.mdc` | Optional Layer-0 baseline only; pair with discipline Versonas (`blueprints/.../versona/versona-generic.mdc.template` at repo root of `versona/`) |
| `forge-product-manager.mdc` | Product strategy orchestration (optional; product-led teams) |
| `versona-*.mdc` | Discipline / family / routing Versonas (copy from `blueprints/.../versona/catalog/…` per `versona/catalog/TEMPLATE-INDEX.md`) |
| `forge-tasklet-*.mdc` | Example tasklets (install via `blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`) |
| `versona-sampling.mdc` | Demo meta-Versona (optional; same installer) |
| `versona-project-setup.mdc` | Project bootstrap checklist (`setup` / `@versona-project-setup`; copy from `blueprints/sdlc/methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template`) |

Copy optional **Skills** from `blueprints/sdlc/templates/forge/cursor-skills/` into `.cursor/skills/`. Align `forge/forge.config.yaml` with installed Versonas: `bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh`.
