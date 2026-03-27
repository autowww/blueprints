# Forge `forge.config.yaml` ↔ `.cursor/rules/` alignment

`forge/forge.config.yaml` declares which **Versona families** and **sub-disciplines** are active, but Cursor does **not** read that file automatically. After you change YAML, ensure matching **`.mdc` rules** exist (copied from `blueprints/sdlc/methodologies/forge/versona/` — **`versona-generic.mdc.template`** at the `versona/` root; all other templates under `catalog/` in `discipline/<domain>/`, `discipline/<domain>/family/` for aggregators, plus `catalog/routing/`, `catalog/meta/`, `catalog/workflow/`; drop the `.template` suffix). **Optional:** root `versona-generic.mdc.template` (Layer 0 baseline only) is not driven by YAML—install if you want an explicit `@` companion to discipline rules. See `versona/catalog/ANCESTRY.md` and `versona/catalog/TEMPLATE-INDEX.md` for paths and the kind/domain map.

## Install (copy rules from blueprints)

**Single source of truth:** [`versona_cursor_rules.py`](versona_cursor_rules.py) maps `forge.config.yaml` → template paths (kept in sync with the check script).

From **repository root** (with `blueprints/` submodule and `forge/forge.config.yaml`):

```bash
bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh
```

| Flag | Effect |
|------|--------|
| *(default)* | Copy **missing** `versona-*.mdc` only (does not overwrite local edits) |
| `--force` | Overwrite existing files |
| `--dry-run` | Print source → dest |
| `--with-project-setup` | Also `versona-project-setup.mdc` |
| `--with-roadmap-gate` | Also `versona-roadmap-gate.mdc` |
| `--with-all-routing` | Also `versona-all.mdc` |
| `--with-family-product` / `--with-family-engineering` / `--with-family-data` | Family aggregators |
| `--with-sampling` | Also `versona-sampling.mdc` (often redundant with `tasklets/install-tasklets.sh`) |
| `--with-generic` | Also `versona-generic.mdc` |
| `--with-standard-forge-rules` | Also `forge-daily`, `forge-planning`, `forge-versona`, `forge-setup`, `forge-product-manager` from `sdlc/templates/forge/cursor-rules/` |

After **`git submodule update`** on `blueprints/`, re-run install (use **`--force`** only after reviewing local globs/edits).

**Compare installed files to current templates** (SHA256):

```bash
bash blueprints/sdlc/methodologies/forge/setup/diff-versona-cursor-rules.sh
```

Pass the same optional `--with-*` flags as install so diff includes those rules. Exit code **1** if a file is missing or differs.

## Quick check

From repository root (with `forge/forge.config.yaml` present):

```bash
bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh
```

Requires **Python 3** and **PyYAML** (`pip install pyyaml`). If PyYAML is missing, use the tables below manually.

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

Usually copied from `blueprints/sdlc/templates/forge/cursor-rules/`:

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

These templates are **not** mapped from `versona.*` YAML flags today. Install manually if you want them in `.cursor/rules/`:

| Template (source) | Installed rule (example) | Purpose |
|----------|--------------------------|---------|
| `catalog/meta/versona-sampling.mdc.template` | `versona-sampling.mdc` | Demo meta-Versona + tasklets (often installed via `install-tasklets.sh`) |
| `catalog/workflow/versona-project-setup.mdc.template` | `versona-project-setup.mdc` | Repo bootstrap checklist and gap analysis; trigger **`setup`** or `@versona-project-setup` |
| `catalog/workflow/versona-roadmap-gate.mdc.template` | `versona-roadmap-gate.mdc` | Roadmap quality gate playbook |
| `catalog/workflow/versona-cursor-rules-sync.mdc.template` | `versona-cursor-rules-sync.mdc` | Chat playbook: commands to install/diff Cursor Versona rules |
