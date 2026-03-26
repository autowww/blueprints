# Versonas — discipline challenge agents

**Versonas** are AI challenge agents that pressure-test work from discipline-specific perspectives. They are **not** team roles — they are challenge functions that strengthen thinking before costly commitments.

Repo-wide documentation habits (single source of truth, link don’t duplicate) are summarized in [`sdlc/DOCUMENTATION-STRUCTURE.md`](../../../DOCUMENTATION-STRUCTURE.md).

## Documentation map (Diátaxis-style)

| Mode | Start here | Role |
|------|------------|------|
| **Explanation** | [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md), [`DISCIPLINE-SPIKE.md`](DISCIPLINE-SPIKE.md), [How Versonas work](#how-versonas-work) (below) | Kinds, sessions, exploration spikes, handoffs |
| **How-to** | [`../../../SETUP.md`](../../../SETUP.md), [`../setup/CURSOR-RULES-ALIGNMENT.md`](../setup/CURSOR-RULES-ALIGNMENT.md), [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh) | Install rules, align `forge.config.yaml`, tasklets + Sampling |
| **Reference** | [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md), [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md), [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md), [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md) | Authoritative paths, kind/domain tables, rule shape, globs |

**Single source of truth for paths:** [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md) — other pages summarize and link there.

## Source layout (templates on disk)

Only **`versona-generic.mdc.template`** lives at the `versona/` root. Every other **`versona-*.mdc.template`** lives under **`catalog/`**.

```
versona/
├── versona-generic.mdc.template          # optional Layer-0-only companion (baseline)
├── VERSONA-CONTRACT.md …                 # normative docs, README, _includes/, …
└── catalog/
    ├── ANCESTRY.md
    ├── TEMPLATE-INDEX.md
    ├── discipline/
    │   ├── engineering/                  # + family/versona-family-engineering.mdc.template
    │   ├── data/
    │   ├── product/
    │   ├── governance/
    │   └── cross-cutting/
    ├── meta/versona-sampling.mdc.template
    ├── workflow/versona-project-setup.mdc.template
    └── routing/versona-all.mdc.template
```

**Family aggregators** are a **kind** in the taxonomy, not a top-level folder next to `discipline/`: on disk they sit under **`catalog/discipline/<domain>/family/`** (engineering, data, product).

## How to find a template

- **By domain** (Engineering, Data, …): open `catalog/discipline/<domain>/` for single-discipline templates; family rules are in that domain’s `family/` subfolder.
- **By kind** (routing, meta, workflow): see section headings in [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md).
- **Definitive path per file:** find the basename in [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md).
- **Copying into a consumer repo:** drop the `.template` suffix; installed rule names stay flat (`versona-se.mdc`, …).

## Framework (kinds, sessions, processes)

Normative concepts—**Versona kinds**, input/output **interfaces**, repeatable **process** docs, **inter-Versona** handoffs, **session** layout under `forge-logs/versona/`, and alignment with Ember Log and day journal—are in **[`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md)**. Cursor rule structure for discipline templates remains in [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md).

## Ancestry and shared baseline

**Kinds** (discipline, routing, family aggregator, meta, workflow) and **domains** (Engineering, Data, Product, Governance, Cross-cutting) are mapped in **[`catalog/ANCESTRY.md`](catalog/ANCESTRY.md)**. Every `versona-*.mdc.template` includes a duplicated **`## Baseline (inherited)`** block so a single attached rule stays self-contained (Cursor has no rule inheritance). The canonical snippet lives in [`_includes/GENERIC-VERSONA-BASELINE.md`](_includes/GENERIC-VERSONA-BASELINE.md)—edit there first, then propagate into templates. **Optional:** copy [`versona-generic.mdc.template`](versona-generic.mdc.template) (at this folder’s root) to `.cursor/rules/` as a Layer-0-only companion to `@` alongside a discipline Versona. All other `versona-*.mdc.template` files live under [`catalog/`](catalog/) (see [`catalog/README.md`](catalog/README.md)).

## How Versonas work

1. A **decision point** is reached (refinement, pre-build, pre-release, architecture choice).
2. The team identifies which **discipline perspectives** are relevant.
3. The appropriate Versonas are **invoked** (via Cursor rule or manual prompt).
4. Each Versona **challenges** the work from its discipline's perspective, producing structured output.
5. The team **acts** on concerns or accepts the risk, capturing the decision in the Ember Log.

## Bridge-awareness

Each Versona template references its discipline's **bridge document** (`*-SDLC-PDLC-BRIDGE.md`). The bridge contains a **phase alignment table** that tells the Versona agent *when* its discipline is most relevant:

- **Architecture** Versona is strongest at phases A–C (discover, specify, design), lighter at D–F.
- **Testing** Versona activates at phases D–E (build, verify) and during Assay Gate.
- **BA** Versona is strongest at phases A–B (discover, specify) and at Review.

This phase-awareness lets Versonas calibrate challenge intensity based on the current Spark's phase prefix (`discover:`, `build:`, `verify:`, etc.).

## Template catalog

### Engineering family (7 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-se.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-se.mdc.template) | Software Engineering | Are CS fundamentals and craft practices sound? |
| [`versona-architecture.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-architecture.mdc.template) | Software Architecture | Is this structurally sound and maintainable? |
| [`versona-devops.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-devops.mdc.template) | DevOps | Can we deliver and operate this reliably? |
| [`versona-testing.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-testing.mdc.template) | Testing & QA | Can we prove this works correctly? |
| [`versona-frontend.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-frontend.mdc.template) | Frontend | Is the web UI fast, accessible, and maintainable? |
| [`versona-mobile.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-mobile.mdc.template) | Mobile | Is the mobile experience performant and reliable? |
| [`versona-iot.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/versona-iot.mdc.template) | Embedded / IoT | Is this reliable and safe for constrained environments? |

### Data family (2 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-bigdata.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/data/versona-bigdata.mdc.template) | Big Data & Data Engineering | Is data engineered, governed, and processed correctly? |
| [`versona-datascience.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/data/versona-datascience.mdc.template) | Data Science & ML | Are models valid, reproducible, and responsible? |

### Product family (5 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-product-management.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/versona-product-management.mdc.template) | Product Management | Are we building the right product for the right market? |
| [`versona-ba.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/versona-ba.mdc.template) | Business Analysis | Do we understand what stakeholders need? |
| [`versona-ux.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/versona-ux.mdc.template) | UX / UI Design | Is this usable, desirable, and accessible? |
| [`versona-marketing.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/versona-marketing.mdc.template) | Marketing | Can we acquire, engage, and retain users? |
| [`versona-cs.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/versona-cs.mdc.template) | Customer Success | Will users achieve their goals? |

### Governance family (1 discipline)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-pm.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/governance/versona-pm.mdc.template) | Project Management | Are we delivering within constraints? |

### Cross-cutting (2 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-security.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/cross-cutting/versona-security.mdc.template) | Security | Is this safe from attacks and breaches? |
| [`versona-compliance.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/cross-cutting/versona-compliance.mdc.template) | Compliance | Does this meet regulatory obligations? |

### Methodology / demo (3)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`versona-generic.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/versona-generic.mdc.template) | Generic baseline (optional) | Layer 0 only—pair with a discipline Versona for full challenges. |
| [`versona-sampling.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/meta/versona-sampling.mdc.template) | Sampling (demo) | What assumptions, unknowns, and top signals appear before a full Versona pass? |
| [`versona-project-setup.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/workflow/versona-project-setup.mdc.template) | Project setup (onboarding) | What is missing for blueprints + Forge + Cursor alignment, and what commands should run next? Invoke with **`setup`** or `@versona-project-setup` after copying to `.cursor/rules/`. |

### Family aggregators

| Template | Activates |
|----------|-----------|
| [`versona-family-engineering.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/engineering/family/versona-family-engineering.mdc.template) | All 7 engineering Versonas |
| [`versona-family-data.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/data/family/versona-family-data.mdc.template) | Both data Versonas |
| [`versona-family-product.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/discipline/product/family/versona-family-product.mdc.template) | All 5 product Versonas |
| [`versona-all.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/versona/catalog/routing/versona-all.mdc.template) | Master routing — suggests which Versonas based on context |

## Tasklets (example bundle)

Small **single-operation** Cursor rules and an installer script live in [`../tasklets/README.md`](../tasklets/README.md). They demonstrate how a **meta-Versona** (e.g. **Sampling**) can chain **tasklets** before deeper discipline Versonas.

- **Install:** `bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh` from the consuming repo root (requires `blueprints/` submodule).
- **Docs:** [`../tasklets/README.md`](../tasklets/README.md) · [`../tasklets/TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md)
- **Product `globs`:** [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md)
- **Align rules with `forge.config.yaml`:** [`../setup/CURSOR-RULES-ALIGNMENT.md`](../setup/CURSOR-RULES-ALIGNMENT.md)

### Discipline overlay (neutral tasklets + normative Versona)

```ks-diagram
key: swimlane
alt: Diagram
```

### Sampling Versona sequence (demo)

```ks-diagram
key: sequence
alt: Diagram
```

### Where documentation is published

```ks-diagram
key: swimlane
alt: Diagram
```

## Adopting Versonas in a consuming repo

1. Copy the templates you need to `.cursor/rules/` in your repo (remove `.template` suffix).
2. **Optional:** Copy [`versona-generic.mdc.template`](versona-generic.mdc.template) if you want an explicit Layer-0 baseline rule to pair with discipline Versonas.
3. **Optional:** Copy [`catalog/workflow/versona-project-setup.mdc.template`](catalog/workflow/versona-project-setup.mdc.template) for **repo bootstrap** (keyword **`setup`**) — orchestrates checklist and gap analysis; pair with [`../setup/forge-setup.mdc.template`](../setup/forge-setup.mdc.template) for the questionnaire wizard.
4. **Optional:** Install the example tasklets + Sampling Versona via [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh).
5. Update `globs:` in each rule to match your project's file structure.
6. Configure which Versonas are active in `forge.config.yaml` (via the setup wizard).
7. Use family aggregators to activate discipline groups without configuring each individually.

See [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) for the standard structure **discipline** Versonas follow. See [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) for kinds, sessions, processes, and logging conventions. See [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md) for the kind/domain tree and [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md) for every template source path.
