# Versona template index (source paths)

**Purpose:** Authoritative **audit table** for every `versona-*.mdc.template` source path, kind, domain, and link-depth checks. Prefer this file over duplicating paths elsewhere; the Versona hub explains how docs fit together (see **Documentation map** in [`../README.md`](../README.md)).

**Layout contract:** `versona-generic.mdc.template` at the `versona/` root; all other templates under `versona/catalog/` (see [Source layout in README](../README.md#source-layout-templates-on-disk)).

**Related:** [`ANCESTRY.md`](ANCESTRY.md) (kinds, domains) · [`../README.md`](../README.md) · [`../../setup/CURSOR-RULES-ALIGNMENT.md`](../../setup/CURSOR-RULES-ALIGNMENT.md)

| Basename | Source path (under `versona/`) | Kind | Domain | Checks |
|----------|-------------------------------|------|--------|--------|
| `versona-se.mdc.template` | `catalog/discipline/engineering/versona-se.mdc.template` | discipline | Engineering | Baseline; `<!-- Ancestry:`; `../../../VERSONA-CONTRACT` |
| `versona-architecture.mdc.template` | `catalog/discipline/engineering/versona-architecture.mdc.template` | discipline | Engineering | same |
| `versona-devops.mdc.template` | `catalog/discipline/engineering/versona-devops.mdc.template` | discipline | Engineering | same |
| `versona-testing.mdc.template` | `catalog/discipline/engineering/versona-testing.mdc.template` | discipline | Engineering | same |
| `versona-frontend.mdc.template` | `catalog/discipline/engineering/versona-frontend.mdc.template` | discipline | Engineering | same |
| `versona-mobile.mdc.template` | `catalog/discipline/engineering/versona-mobile.mdc.template` | discipline | Engineering | same |
| `versona-iot.mdc.template` | `catalog/discipline/engineering/versona-iot.mdc.template` | discipline | Engineering | same |
| `versona-bigdata.mdc.template` | `catalog/discipline/data/versona-bigdata.mdc.template` | discipline | Data | same |
| `versona-datascience.mdc.template` | `catalog/discipline/data/versona-datascience.mdc.template` | discipline | Data | same |
| `versona-product-management.mdc.template` | `catalog/discipline/product/versona-product-management.mdc.template` | discipline | Product | same |
| `versona-ba.mdc.template` | `catalog/discipline/product/versona-ba.mdc.template` | discipline | Product | same |
| `versona-ux.mdc.template` | `catalog/discipline/product/versona-ux.mdc.template` | discipline | Product | same |
| `versona-marketing.mdc.template` | `catalog/discipline/product/versona-marketing.mdc.template` | discipline | Product | same |
| `versona-cs.mdc.template` | `catalog/discipline/product/versona-cs.mdc.template` | discipline | Product | same |
| `versona-pm.mdc.template` | `catalog/discipline/governance/versona-pm.mdc.template` | discipline | Governance | same |
| `versona-security.mdc.template` | `catalog/discipline/cross-cutting/versona-security.mdc.template` | discipline | Cross-cutting | same |
| `versona-compliance.mdc.template` | `catalog/discipline/cross-cutting/versona-compliance.mdc.template` | discipline | Cross-cutting | same |
| `versona-family-engineering.mdc.template` | `catalog/discipline/engineering/family/versona-family-engineering.mdc.template` | family_aggregator | Engineering | `../../../../VERSONA-CONTRACT`; `../../../../../../../../disciplines/` README links |
| `versona-family-data.mdc.template` | `catalog/discipline/data/family/versona-family-data.mdc.template` | family_aggregator | Data | same |
| `versona-family-product.mdc.template` | `catalog/discipline/product/family/versona-family-product.mdc.template` | family_aggregator | Product | same |
| `versona-all.mdc.template` | `catalog/routing/versona-all.mdc.template` | routing | — | Baseline; ancestry; `blueprints/…` refs |
| `versona-sampling.mdc.template` | `catalog/meta/versona-sampling.mdc.template` | meta | — | `../../VERSONA-CONTRACT`; `../../../tasklets/` |
| `versona-project-setup.mdc.template` | `catalog/workflow/versona-project-setup.mdc.template` | workflow | — | `../../../VERSONA-CONTRACT`; `../../../setup/` |
| `versona-generic.mdc.template` | `versona-generic.mdc.template` (root) | baseline_only | — | `catalog/ANCESTRY`; `VERSONA-*` (siblings) |

## Verification commands

- From the blueprints repo root: search for stale path segments such as `versona/baseline/`, top-level `versona/discipline/` (without `catalog/`), or `versona/family/` (family templates now live under `catalog/discipline/<domain>/family/`).
- `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh --dry-run` — resolves `catalog/meta/versona-sampling.mdc.template`.
