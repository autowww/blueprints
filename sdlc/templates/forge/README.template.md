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
| `forge-versona-*.mdc` | Discipline-specific Versonas (per active disciplines) |
| `forge-tasklet-*.mdc` | Example tasklets (install via `blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh`) |
| `versona-sampling.mdc` | Demo meta-Versona (optional; same installer) |
