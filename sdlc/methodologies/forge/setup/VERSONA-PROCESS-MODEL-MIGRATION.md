---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Migration: discipline-first Cursor rules → process-first Versona model

**Audience:** Teams that already had **`versona-*.mdc`** rules installed from **`blueprints`**, and are adopting the **process-first** layer: canonical **artifact paths**, optional **ledger / graph** JSONL, **Skills**, **tasklets**, **recipes**, and **diagram IR** aligned with [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) and [`../versona/ARTIFACT-CONTRACTS.md`](../versona/ARTIFACT-CONTRACTS.md).

## What changed (conceptually)

| Before (still valid) | After (additive) |
|----------------------|------------------|
| Install discipline rules from **`forge.config.yaml`**; optional workflow rules via flags | Same, plus **`recommended`** preset bundles **routing, methodology, sampling meta-Versona**, standard Forge five |
| Sessions mostly **`SESSION.md`** under **`forge-logs/versona/...`** | Optional **`versona-track/`** ledger, **`session.manifest.json`**, **`handoff.json`**, **`artifact-manifest.json`**, **`diagrams/`** (see operating model) |
| Tasklets installer was the common path to **Sampling** | **`versona-sampling.mdc`** is part of **`--preset recommended`**; tasklets installer still adds **`forge-tasklet-*.mdc`** |
| Single manifest for drift | **`.forge/cursor-rules-manifest.json`** stays the **SHA ledger** for installed **`.mdc`** files; **`.forge/versona-adoption-manifest.json`** is an **optional** companion (Skills / tasklets / recipes pointers only) |

**Backward compatibility:** Omitting **`--preset`** on **`sync`** is unchanged (YAML-driven Versonas only). Existing session folders without JSON artifacts remain valid per [`../versona/MIGRATIONS.md`](../versona/MIGRATIONS.md).

## Migration checklist (consuming repo root)

1. **Bump the `blueprints/` submodule** to a commit that includes the process-first docs and templates.
2. **Scaffold** — If **`forge-init.sh`** was run before **`forge-logs/`** existed, either re-run it (it is idempotent for existing dirs) or create **`forge-logs/`** and **`forge-logs/versona-track/`** per [`../versona/ARTIFACT-CONTRACTS.md`](../versona/ARTIFACT-CONTRACTS.md).
3. **Inspect drift** — Same preset you use in CI or locally:
   ```bash
   bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh status --preset recommended
   bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh diff --preset recommended
   ```
4. **Sync rules** — After review (especially local edits to **`.mdc`** globs):
   ```bash
   bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended --force
   ```
   Expect **`versona-sampling.mdc`** to appear if it was missing.
5. **Optional adoption manifest** — One-time or in onboarding scripts:
   ```bash
   bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended --force --write-adoption-manifest
   ```
6. **Tasklets** — Run **`tasklets/install-tasklets.sh`** if you want **`forge-tasklet-*.mdc`** (cognition operations); not required for discipline §5 sessions alone.
7. **Skills** — Copy from **`blueprints/sdlc/templates/forge/cursor-skills/`** into **`.cursor/skills/`** per [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md).
8. **Recipes (execution plane)** — Copy stubs from **`blueprints/agents/templates/recipe/`** into **`agents/recipes/`** when you wire CI or headless runners; see [`../../../../agents/ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md).

## Verification

Follow [`VERSONA-VERIFICATION.md`](VERSONA-VERIFICATION.md) for an end-to-end pass that includes **`check`**, **`status`**, and **`diff`**.

## Related

- [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) — presets, manifest split, flags  
- [`../versona/MIGRATIONS.md`](../versona/MIGRATIONS.md) — changelog rows for breaking-ish template changes  
