---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona standards matrix

**Purpose:** Map each installed **Versona rule** (`versona-*.mdc`) to a **standards profile**—the precedence layers it is expected to **surface most often** when producing traceable output. **Authoritative machine-readable copy:** [`versona-standards-matrix.yaml`](versona-standards-matrix.yaml) · [`versona-standards-matrix.json`](versona-standards-matrix.json).

**Precedence layers** (1 = wins over 6): see [`precedence.md`](precedence.md).

## Profile definitions

| Profile ID | Role | Typical layers emphasized |
|------------|------|---------------------------|
| `discipline_cross_cutting_assurance` | Security & Compliance lenses; external/org controls vs habits | 1, 2, 5 |
| `discipline_governance` | PM/governance; delivery constraints and methodology | 2, 4, 5 |
| `discipline_product` | Product family; value and roadmap; law when claims or data in scope | 1, 3, 4, 5 |
| `discipline_engineering` | Engineering specialists; ADRs and org baselines beat informal patterns | 3, 4, 5, 6 |
| `discipline_data` | Data/ML; residency and AI governance when applicable | 1, 2, 3, 5 |
| `routing` | Master router; suggest lenses when L1/L2 likely | 3, 4, 5 |
| `family_aggregator` | Merge child passes; consolidate traceability fields | 4, 5 |
| `meta_tasklet` | Thin meta + tasklets | 4, 6 |
| `workflow_bootstrap` | Setup workflows; detect missing registry / rules | 3, 4 |
| `methodology_orchestrator` | Forge SDLC A–F execution plans; L1–L2 in graph; trace on merge | 1, 2, 3, 4 |
| `baseline_only` | Generic baseline companion only | 4, 6 |

## Per-Versona mapping

| Versona (installed basename) | Kind | Domain | Standards profile |
|------------------------------|------|--------|-------------------|
| `versona-security` | discipline | Cross-cutting | `discipline_cross_cutting_assurance` |
| `versona-compliance` | discipline | Cross-cutting | `discipline_cross_cutting_assurance` |
| `versona-pm` | discipline | Governance | `discipline_governance` |
| `versona-estimation` | discipline | Governance | `discipline_governance` |
| `versona-product-management` | discipline | Product | `discipline_product` |
| `versona-ba` | discipline | Product | `discipline_product` |
| `versona-ux` | discipline | Product | `discipline_product` |
| `versona-marketing` | discipline | Product | `discipline_product` |
| `versona-cs` | discipline | Product | `discipline_product` |
| `versona-se` | discipline | Engineering | `discipline_engineering` |
| `versona-architecture` | discipline | Engineering | `discipline_engineering` |
| `versona-devops` | discipline | Engineering | `discipline_engineering` |
| `versona-testing` | discipline | Engineering | `discipline_engineering` |
| `versona-frontend` | discipline | Engineering | `discipline_engineering` |
| `versona-mobile` | discipline | Engineering | `discipline_engineering` |
| `versona-iot` | discipline | Engineering | `discipline_engineering` |
| `versona-bigdata` | discipline | Data | `discipline_data` |
| `versona-datascience` | discipline | Data | `discipline_data` |
| `versona-family-engineering` | family_aggregator | Engineering | `family_aggregator` |
| `versona-family-data` | family_aggregator | Data | `family_aggregator` |
| `versona-family-product` | family_aggregator | Product | `family_aggregator` |
| `versona-all` | routing | — | `routing` |
| `versona-sampling` | meta | — | `meta_tasklet` |
| `versona-project-setup` | workflow | — | `workflow_bootstrap` |
| `versona-roadmap-gate` | workflow | — | `workflow_bootstrap` |
| `versona-forge-sdlc` | workflow | — | `methodology_orchestrator` |
| `versona-cursor-rules-sync` | workflow | — | `workflow_bootstrap` |
| `versona-generic` | baseline_only | — | `baseline_only` |

**Note:** [`forge-product-manager.mdc.template`](../../product-manager/forge-product-manager.mdc.template) (**product** authoring / bootstrap dialog) differs from **`versona-forge-sdlc`** (**methodology** SDLC orchestration — [`../../orchestration/README.md`](../../orchestration/README.md)). For standards profiles, treat `forge-product-manager` as **`workflow_bootstrap` + `discipline_product`** when scoping; reference this matrix and the consuming repo registry.

## §5 output hook

When using **Contract §5** structured output, add **Standards traceability** per [`../versona/VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) §5.1 when material.

## Examples

Worked conflicts: [`examples/CONFLICT-SCENARIOS.md`](examples/CONFLICT-SCENARIOS.md).
