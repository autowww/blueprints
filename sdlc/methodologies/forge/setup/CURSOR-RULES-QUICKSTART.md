# Cursor rules — quickstart (Forge + Versonas)

**Full reference:** [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) · **Implementation:** [`versona_cursor_rules.py`](versona_cursor_rules.py)

From the **consuming repository root** (with `blueprints/` and `forge/forge.config.yaml`):

## After submodule update or a new machine

Install YAML-driven Versonas plus the **recommended** bundle (standard Forge rules, routing, project setup, roadmap gate, cursor-rules-sync playbook):

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended
```

Use `--force` only after you have reviewed local edits (it overwrites existing `.mdc` files).

## Check what would change

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh status --preset recommended
```

Exit code **1** if something is missing or differs from blueprints templates — same idea as `diff`, but one line per file.

## Submodule bump: diff then sync

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh diff --preset recommended
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended --force
```

## YAML-only install (CI / backward compatible)

Omitting `--preset` keeps the old behavior: only `versona-*.mdc` files implied by `forge.config.yaml` (no standard Forge five, no optional workflow bundle).

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync
```

## Quick audit: config vs disk

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check
```

Requires **Python 3** and **PyYAML** (`pip install pyyaml`).

## Presets (summary)

| Preset | What you get |
|--------|----------------|
| *(none)* / `minimal` | YAML-driven Versonas only |
| `recommended` | minimal + standard Forge rules + `versona-all`, `versona-project-setup`, `versona-roadmap-gate`, `versona-cursor-rules-sync` |
| `full` | recommended + three family aggregators + `versona-generic` |

Extra `--with-*` flags **add** on top of a preset. See **Reference: granular flags** in [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md).

## Manifest after sync

Each successful **`sync`** (install) writes **`.forge/cursor-rules-manifest.json`** at the repository root (unless `--no-write-manifest`): UTC timestamp, **`blueprints_commit`** when `blueprints/` is a git checkout, active **`preset`**, and per-rule **`source_sha256`** / **`installed_sha256`** for the install job list. Use it to see whether installed files still match templates after local edits or a submodule bump.
