---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge `forge.config.yaml` ↔ `.cursor/rules/` alignment

**Quickstart (one screen):** [`CURSOR-RULES-QUICKSTART.md`](CURSOR-RULES-QUICKSTART.md)

`forge/forge.config.yaml` declares which **Versona families** and **sub-disciplines** are active, but Cursor does **not** read that file automatically. After you change YAML, ensure matching **`.mdc` rules** exist (copied from `blueprints/sdlc/methodologies/forge/versona/` — **`versona-generic.mdc.template`** at the `versona/` root; all other templates under `catalog/` in `discipline/<domain>/`, `discipline/<domain>/family/` for aggregators, plus `catalog/routing/`, `catalog/meta/`, `catalog/workflow/`; drop the `.template` suffix). **Optional:** root `versona-generic.mdc.template` (Layer 0 baseline only) is not driven by YAML—install if you want an explicit `@` companion to discipline rules. See `versona/catalog/ANCESTRY.md` and `versona/catalog/TEMPLATE-INDEX.md` for paths and the kind/domain map.

## Single entry: `sync-forge-cursor-rules.sh`

**Single source of truth:** [`versona_cursor_rules.py`](versona_cursor_rules.py) maps `forge.config.yaml` → template paths (shared with `check`).

From **repository root** (with `blueprints/` submodule and `forge/forge.config.yaml`):

| Subcommand | Maps to | Typical use |
|------------|---------|-------------|
| `sync` | `install` | Copy templates into `.cursor/rules/` |
| `diff` | `diff` | SHA256 compare installed files vs blueprints |
| `status` | `status` | Per-file missing / drift / ok (exit **1** if bad) |
| `check` | `check` | YAML-expected Versona files exist (CI / quick audit) |

**Recommended for humans:**

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended
```

**Backward compatible (YAML-driven Versonas only, no preset bundle):**

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync
```

Thin wrappers still work: [`install-versona-cursor-rules.sh`](install-versona-cursor-rules.sh) → `sync sync`, [`diff-versona-cursor-rules.sh`](diff-versona-cursor-rules.sh) → `sync diff`, [`check-forge-cursor-alignment.sh`](check-forge-cursor-alignment.sh) → `sync check`.

### Presets

| Preset | Effect |
|--------|--------|
| *(omit)* / `--preset minimal` | Copy **only** `versona-*.mdc` implied by `forge.config.yaml` (same as pre-preset behavior) |
| `--preset recommended` | Minimal + standard Forge five (`forge-daily`, `forge-planning`, `forge-versona`, `forge-setup`, `forge-product-manager`) + `versona-all`, `versona-project-setup`, `versona-roadmap-gate`, `versona-cursor-rules-sync` |
| `--preset full` | Recommended + family aggregators (`versona-family-*`) + `versona-generic` |

**Additive:** `--with-*` flags on `sync` / `diff` / `status` **add** on top of the chosen preset.

After **`git submodule update`** on `blueprints/`, re-run `sync` (use **`--force`** only after reviewing local globs/edits and `diff` / `status`).

### `status` and `diff`

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh status --preset recommended
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh diff --preset recommended
```

Pass the same `--preset` and `--with-*` flags as for `sync` so the job list matches. Exit code **1** when something is missing or differs.

### Quick check (YAML expectations only)

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check
```

Requires **Python 3** and **PyYAML** (`pip install pyyaml`). If PyYAML is missing, use the tables below manually.

### Manifest (`.forge/cursor-rules-manifest.json`)

After each successful **`sync`** (non–dry-run `install`), the tool writes **`.forge/cursor-rules-manifest.json`** at the **repository root** unless you pass **`--no-write-manifest`**. It records a UTC **`generated_at`**, optional **`blueprints_commit`** (`git rev-parse HEAD` in the resolved `blueprints/` root when it is a git work tree), the **`preset`** used (if any), and for each file in the install job list: **`name`**, **`label`**, **`source_sha256`**, **`installed_sha256`**. Compare `source` vs `installed` to spot drift; compare `blueprints_commit` across machines to confirm submodule alignment.

## Reference: granular flags (`sync` / install)

Use these with **`sync-forge-cursor-rules.sh sync`** (or `install-versona-cursor-rules.sh`, which delegates to `sync`).

| Flag | Effect |
|------|--------|
| *(default)* | Copy **missing** `versona-*.mdc` only when no preset bundle applies (does not overwrite local edits) |
| `--preset minimal`, `recommended`, or `full` | See [Presets](#presets) above |
| `--force` | Overwrite existing files |
| `--dry-run` | Print source → dest |
| `--no-write-manifest` | Skip writing `.forge/cursor-rules-manifest.json` |
| `--with-project-setup` | Also `versona-project-setup.mdc` |
| `--with-roadmap-gate` | Also `versona-roadmap-gate.mdc` |
| `--with-all-routing` | Also `versona-all.mdc` |
| `--with-cursor-rules-sync` | Also `versona-cursor-rules-sync.mdc` |
| `--with-family-product` / `--with-family-engineering` / `--with-family-data` | Family aggregators |
| `--with-sampling` | Also `versona-sampling.mdc` (often redundant with `tasklets/install-tasklets.sh`) |
| `--with-generic` | Also `versona-generic.mdc` |
| `--with-standard-forge-rules` | Also `forge-daily`, `forge-planning`, `forge-versona`, `forge-setup`, `forge-product-manager` from `sdlc/templates/forge/cursor-rules/` |

## Family → template sources

| `versona.families.*` | When `true`, install from `versona/` (see **source path** in [`TEMPLATE-INDEX.md`](../versona/catalog/TEMPLATE-INDEX.md)) |
|----------------------|----------------------------------------|
| `engineering` | Each `engineering_disciplines.*` that is `true` → matching `versona-*.mdc` under `versona/catalog/discipline/engineering/` (see sub-table). Optional: `catalog/discipline/engineering/family/versona-family-engineering.mdc.template` for aggregator. |
| `data` | `catalog/discipline/data/versona-bigdata.mdc.template`, `catalog/discipline/data/versona-datascience.mdc.template` (or `catalog/discipline/data/family/versona-family-data.mdc.template`). |
| `product` | Each `product_disciplines.*` that is `true` → matching `versona-*.mdc` under `versona/catalog/discipline/product/`. Optional: `catalog/discipline/product/family/versona-family-product.mdc.template`. |
| `governance` | `catalog/discipline/governance/versona-pm.mdc.template` |

| `versona.cross_cutting.*` | Template (source) |
|---------------------------|----------|
| `security` | `catalog/discipline/cross-cutting/versona-security.mdc.template` |
| `compliance` | `catalog/discipline/cross-cutting/versona-compliance.mdc.template` |

## Engineering sub-disciplines → filenames

| YAML key | Installed rule (example) |
|----------|---------------------------|
| `software_engineering` | `versona-se.mdc` |
| `software_architecture` | `versona-architecture.mdc` |
| `devops` | `versona-devops.mdc` |
| `testing` | `versona-testing.mdc` |
| `frontend` | `versona-frontend.mdc` |
| `mobile` | `versona-mobile.mdc` |
| `embedded_iot` | `versona-iot.mdc` |

## Product sub-disciplines → filenames

| YAML key | Installed rule (example) |
|----------|---------------------------|
| `product_management` | `versona-product-management.mdc` |
| `business_analysis` | `versona-ba.mdc` |
| `ux_design` | `versona-ux.mdc` |
| `marketing` | `versona-marketing.mdc` |
| `customer_success` | `versona-cs.mdc` |

## Standard Forge Cursor rules (not driven by `versona`)

Usually copied from `blueprints/sdlc/templates/forge/cursor-rules/` (included in **`--preset recommended`** and above, or `--with-standard-forge-rules`):

| File | Purpose |
|------|---------|
| `forge-daily.mdc` | Charge, hats, Ember Log, journal |
| `forge-planning.mdc` | Ore, Product Sparks, planning |
| `forge-versona.mdc` | Master routing |
| `forge-setup.mdc` | First-time setup (optional after onboarding) |
| `forge-product-manager.mdc` | Product orchestration (optional; product-led teams) |

## Tasklets (optional)

Run `blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh` for example **tasklets** + **Sampling Versona** — not controlled by `forge.config.yaml` today.

## Optional Versonas (not driven by `forge.config.yaml`)

These templates are **not** mapped from `versona.*` YAML flags today. Use **`--preset recommended`** / **`full`** or individual **`--with-*`** flags to install into `.cursor/rules/`:

| Template (source) | Installed rule (example) | Purpose |
|----------|--------------------------|---------|
| `catalog/meta/versona-sampling.mdc.template` | `versona-sampling.mdc` | Demo meta-Versona + tasklets (often installed via `install-tasklets.sh`) |
| `catalog/workflow/versona-project-setup.mdc.template` | `versona-project-setup.mdc` | Repo bootstrap checklist and gap analysis; trigger **`setup`** or `@versona-project-setup` |
| `catalog/workflow/versona-roadmap-gate.mdc.template` | `versona-roadmap-gate.mdc` | Roadmap quality gate playbook |
| `catalog/workflow/versona-cursor-rules-sync.mdc.template` | `versona-cursor-rules-sync.mdc` | Chat playbook: commands to install/diff Cursor Versona rules |
