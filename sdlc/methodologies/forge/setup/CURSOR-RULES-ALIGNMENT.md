# Forge `forge.config.yaml` ↔ `.cursor/rules/` alignment

`forge/forge.config.yaml` declares which **Versona families** and **sub-disciplines** are active, but Cursor does **not** read that file automatically. After you change YAML, ensure matching **`.mdc` rules** exist (copied from `blueprints/sdlc/methodologies/forge/versona/*.mdc.template` — drop the `.template` suffix).

## Quick check

From repository root (with `forge/forge.config.yaml` present):

```bash
bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh
```

Requires **Python 3** and **PyYAML** (`pip install pyyaml`). If PyYAML is missing, use the tables below manually.

## Family → template sources

| `versona.families.*` | When `true`, install from `versona/` |
|----------------------|----------------------------------------|
| `engineering` | Each `engineering_disciplines.*` that is `true` → matching `versona-*.mdc` (see sub-table). Optional: `versona-family-engineering.mdc.template` for aggregator. |
| `data` | `versona-bigdata.mdc.template`, `versona-datascience.mdc.template` (or `versona-family-data.mdc.template`). |
| `product` | Each `product_disciplines.*` that is `true` → matching `versona-*.mdc`. Optional: `versona-family-product.mdc.template`. |
| `governance` | `versona-pm.mdc.template` |

| `versona.cross_cutting.*` | Template |
|---------------------------|----------|
| `security` | `versona-security.mdc.template` |
| `compliance` | `versona-compliance.mdc.template` |

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

| Template | Installed rule (example) | Purpose |
|----------|--------------------------|---------|
| `versona-sampling.mdc.template` | `versona-sampling.mdc` | Demo meta-Versona + tasklets (often installed via `install-tasklets.sh`) |
| `versona-project-setup.mdc.template` | `versona-project-setup.mdc` | Repo bootstrap checklist and gap analysis; trigger **`setup`** or `@versona-project-setup` |
