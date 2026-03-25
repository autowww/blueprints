# Forge `forge.config.yaml` ↔ `.cursor/rules/` alignment

`forge/forge.config.yaml` declares which **Versona families** and **sub-disciplines** are active, but Cursor does **not** read that file automatically. After you change YAML, ensure matching **`.mdc` rules** exist (copied from `blueprints/sdlc/methodologies/forge/versona/` — **`versona-generic.mdc.template`** at the `versona/` root; all other templates under `catalog/` in `discipline/<domain>/`, `discipline/<domain>/family/` for aggregators, plus `catalog/routing/`, `catalog/meta/`, `catalog/workflow/`; drop the `.template` suffix). **Optional:** root `versona-generic.mdc.template` (Layer 0 baseline only) is not driven by YAML—install if you want an explicit `@` companion to discipline rules. See `versona/catalog/ANCESTRY.md` and `versona/catalog/TEMPLATE-INDEX.md` for paths and the kind/domain map.

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
