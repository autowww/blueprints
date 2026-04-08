---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona ancestry — kinds, domains, templates

Normative layering for Forge Versonas: **generic baseline** (Layer 0), **kind** (routing, discipline, …), **domain** (for discipline templates only), then **concrete** `.mdc` templates. Cursor rules do not inherit automatically—each installed rule duplicates the baseline for self-containment; see [`_includes/GENERIC-VERSONA-BASELINE.md`](../_includes/GENERIC-VERSONA-BASELINE.md).

**Related:** [`../VERSONA-FRAMEWORK.md`](../VERSONA-FRAMEWORK.md) (kinds, sessions, processes) · [`../VERSONA-CONTRACT.md`](../VERSONA-CONTRACT.md) (discipline rule shape) · [`../README.md`](../README.md) (template catalog) · [`TEMPLATE-INDEX.md`](TEMPLATE-INDEX.md) (source path audit)

---

## Conceptual tree

```blueprint-diagram
key: swimlane
alt: Diagram
```

**Physical layout (on disk):** The diagram is **conceptual**. **Family aggregator** is a **kind**, not a sibling directory named `family/` next to `versona/discipline/` at the `versona/` root. Template files for that kind live under **`catalog/discipline/<domain>/family/`** (e.g. engineering, data, product). The optional **generic** baseline template is **`versona-generic.mdc.template`** at the `versona/` root (not under `catalog/`). See [`../README.md`](../README.md#source-layout-templates-on-disk).

---

## Kind: discipline (by domain)

### Domain: Engineering

**Related:** [`discipline/engineering/README.md`](discipline/engineering/README.md) — normative **ancestry** (`versona-se` as craft ancestor, specialists, family-first entry, process vs discipline “done”).

| Template | Core question (short) | Output variant |
|----------|------------------------|----------------|
| [`versona-se.mdc.template`](discipline/engineering/versona-se.mdc.template) | CS fundamentals and craft | Contract §5 |
| [`versona-architecture.mdc.template`](discipline/engineering/versona-architecture.mdc.template) | Structure and maintainability | Contract §5 |
| [`versona-devops.mdc.template`](discipline/engineering/versona-devops.mdc.template) | Delivery and operations | Contract §5 |
| [`versona-testing.mdc.template`](discipline/engineering/versona-testing.mdc.template) | Verification and quality | Contract §5 |
| [`versona-frontend.mdc.template`](discipline/engineering/versona-frontend.mdc.template) | Web UI | Contract §5 |
| [`versona-mobile.mdc.template`](discipline/engineering/versona-mobile.mdc.template) | Mobile | Contract §5 |
| [`versona-iot.mdc.template`](discipline/engineering/versona-iot.mdc.template) | Embedded / IoT | Contract §5 |

### Domain: Data

| Template | Core question (short) | Output variant |
|----------|------------------------|----------------|
| [`versona-bigdata.mdc.template`](discipline/data/versona-bigdata.mdc.template) | Data engineering / pipelines | Contract §5 |
| [`versona-datascience.mdc.template`](discipline/data/versona-datascience.mdc.template) | ML / DS responsibility | Contract §5 |

### Domain: Product

| Template | Core question (short) | Output variant |
|----------|------------------------|----------------|
| [`versona-product-management.mdc.template`](discipline/product/versona-product-management.mdc.template) | Product/market fit | Contract §5 + optional handoffs |
| [`versona-ba.mdc.template`](discipline/product/versona-ba.mdc.template) | Stakeholder needs | Contract §5 |
| [`versona-ux.mdc.template`](discipline/product/versona-ux.mdc.template) | Usability / design | Contract §5 |
| [`versona-marketing.mdc.template`](discipline/product/versona-marketing.mdc.template) | Acquisition / retention | Contract §5 |
| [`versona-cs.mdc.template`](discipline/product/versona-cs.mdc.template) | Customer success | Contract §5 |

### Domain: Governance

| Template | Core question (short) | Output variant |
|----------|------------------------|----------------|
| [`versona-pm.mdc.template`](discipline/governance/versona-pm.mdc.template) | Constraints and delivery | Contract §5 |

### Domain: Cross-cutting

| Template | Core question (short) | Output variant |
|----------|------------------------|----------------|
| [`versona-security.mdc.template`](discipline/cross-cutting/versona-security.mdc.template) | Security posture | Contract §5 |
| [`versona-compliance.mdc.template`](discipline/cross-cutting/versona-compliance.mdc.template) | Regulatory fit | Contract §5 |

---

## Kind: family_aggregator

| Template | Domain scope | Output variant |
|----------|--------------|----------------|
| [`versona-family-engineering.mdc.template`](discipline/engineering/family/versona-family-engineering.mdc.template) | Engineering (7 disciplines) | Consolidated family report |
| [`versona-family-data.mdc.template`](discipline/data/family/versona-family-data.mdc.template) | Data (2 disciplines) | Consolidated family report |
| [`versona-family-product.mdc.template`](discipline/product/family/versona-family-product.mdc.template) | Product (5 disciplines) | Consolidated family report |

---

## Kind: routing

| Template | Domain | Output variant |
|----------|--------|----------------|
| [`versona-all.mdc.template`](routing/versona-all.mdc.template) | — | Routing recommendation tables |
| Packaged copy: [`../../../../templates/forge/cursor-rules/forge-versona.mdc`](../../../../templates/forge/cursor-rules/forge-versona.mdc) | — | Same (consumer `.cursor/rules/`) |

---

## Kind: meta

| Template | Domain | Output variant |
|----------|--------|----------------|
| [`versona-sampling.mdc.template`](meta/versona-sampling.mdc.template) | — | Shortened / merged demo report |

---

## Kind: workflow

| Template | Domain | Output variant |
|----------|--------|----------------|
| [`versona-project-setup.mdc.template`](workflow/versona-project-setup.mdc.template) | — | Setup / audit report |
| [`versona-roadmap-gate.mdc.template`](workflow/versona-roadmap-gate.mdc.template) | — | Roadmap gate playbook |
| [`versona-cursor-rules-sync.mdc.template`](workflow/versona-cursor-rules-sync.mdc.template) | — | Cursor rules install/diff playbook |

---

## Optional: generic baseline-only rule

| Template | Purpose |
|----------|---------|
| [`versona-generic.mdc.template`](../versona-generic.mdc.template) | Layer 0 only; optional `@` with a discipline Versona |

---

## Master table

| Template | Kind | Domain | Family aggregator | Output variant |
|----------|------|--------|-------------------|----------------|
| versona-se.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-architecture.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-devops.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-testing.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-frontend.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-mobile.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-iot.mdc.template | discipline | Engineering | — | Contract §5 |
| versona-bigdata.mdc.template | discipline | Data | — | Contract §5 |
| versona-datascience.mdc.template | discipline | Data | — | Contract §5 |
| versona-product-management.mdc.template | discipline | Product | — | Contract §5 + optional handoffs |
| versona-ba.mdc.template | discipline | Product | — | Contract §5 |
| versona-ux.mdc.template | discipline | Product | — | Contract §5 |
| versona-marketing.mdc.template | discipline | Product | — | Contract §5 |
| versona-cs.mdc.template | discipline | Product | — | Contract §5 |
| versona-pm.mdc.template | discipline | Governance | — | Contract §5 |
| versona-security.mdc.template | discipline | Cross-cutting | — | Contract §5 |
| versona-compliance.mdc.template | discipline | Cross-cutting | — | Contract §5 |
| versona-family-engineering.mdc.template | family_aggregator | Engineering | self | Consolidated |
| versona-family-data.mdc.template | family_aggregator | Data | self | Consolidated |
| versona-family-product.mdc.template | family_aggregator | Product | self | Consolidated |
| versona-all.mdc.template | routing | — | — | Routing tables |
| forge-versona.mdc (templates) | routing | — | — | Routing tables |
| versona-sampling.mdc.template | meta | — | — | Shortened |
| versona-project-setup.mdc.template | workflow | — | — | Setup report |
| versona-roadmap-gate.mdc.template | workflow | — | — | Roadmap gate playbook |
| versona-cursor-rules-sync.mdc.template | workflow | — | — | Cursor rules sync playbook |
| versona-generic.mdc.template | baseline_only | — | — | Layer 0 only |

---

## Stable headings

For generators: **Conceptual tree**, **Kind: discipline**, **Kind: family_aggregator**, **Kind: routing**, **Kind: meta**, **Kind: workflow**, **Optional: generic baseline-only rule**, **Master table**.
