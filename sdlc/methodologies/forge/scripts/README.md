# Forge scripts

Shell scripts for git-tracked daily Forge operations. Run from the **consuming repository root** (not from inside `blueprints/`).

## Prerequisites

- `bash` (4.0+)
- `git`
- Forge workspace initialized (`forge/`, `ember-logs/` directories exist)

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| [`forge-charge.sh`](forge-charge.sh) | Manage today's Charge | `./blueprints/sdlc/methodologies/forge/scripts/forge-charge.sh [show\|new\|done SPARK_ID\|block SPARK_ID\|bank SPARK_ID]` |
| [`forge-ember.sh`](forge-ember.sh) | Append an Ember Log entry | `./blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh "Decision summary"` |
| [`forge-journal.sh`](forge-journal.sh) | Create/commit day journal | `./blueprints/sdlc/methodologies/forge/scripts/forge-journal.sh [new\|commit]` |
| [`forge-versona-session.sh`](forge-versona-session.sh) | Scaffold Versona session folder under `forge-logs/versona/` | `./blueprints/sdlc/methodologies/forge/scripts/forge-versona-session.sh <actor> [session-id] [--with-yaml-manifest]` |
| [`forge-status.sh`](forge-status.sh) | Show iteration status | `./blueprints/sdlc/methodologies/forge/scripts/forge-status.sh` |

## Convention

Scripts create files using templates from [`../daily/`](../daily/README.md). Date-stamped files use `YYYY-MM-DD` format. All output is git-trackable Markdown.
