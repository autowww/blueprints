# Bellows — discipline challenge agents

**Bellows** are AI challenge agents that pressure-test work from discipline-specific perspectives. They are **not** team roles — they are challenge functions that strengthen thinking before costly commitments.

## How Bellows work

1. A **decision point** is reached (refinement, pre-build, pre-release, architecture choice).
2. The team identifies which **discipline perspectives** are relevant.
3. The appropriate Bellows are **invoked** (via Cursor rule or manual prompt).
4. Each Bellows **challenges** the work from its discipline's perspective, producing structured output.
5. The team **acts** on concerns or accepts the risk, capturing the decision in the Ember Log.

## Bridge-awareness

Each Bellows template references its discipline's **bridge document** (`*-SDLC-PDLC-BRIDGE.md`). The bridge contains a **phase alignment table** that tells the Bellows agent *when* its discipline is most relevant:

- **Architecture** Bellows is strongest at phases A–C (discover, specify, design), lighter at D–F.
- **Testing** Bellows activates at phases D–E (build, verify) and during Assay Gate.
- **BA** Bellows is strongest at phases A–B (discover, specify) and at Review.

This phase-awareness lets Bellows calibrate challenge intensity based on the current Spark's phase prefix (`discover:`, `build:`, `verify:`, etc.).

## Template catalog

### Engineering family (7 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`bellows-se.mdc.template`](bellows-se.mdc.template) | Software Engineering | Are CS fundamentals and craft practices sound? |
| [`bellows-architecture.mdc.template`](bellows-architecture.mdc.template) | Software Architecture | Is this structurally sound and maintainable? |
| [`bellows-devops.mdc.template`](bellows-devops.mdc.template) | DevOps | Can we deliver and operate this reliably? |
| [`bellows-testing.mdc.template`](bellows-testing.mdc.template) | Testing & QA | Can we prove this works correctly? |
| [`bellows-frontend.mdc.template`](bellows-frontend.mdc.template) | Frontend | Is the web UI fast, accessible, and maintainable? |
| [`bellows-mobile.mdc.template`](bellows-mobile.mdc.template) | Mobile | Is the mobile experience performant and reliable? |
| [`bellows-iot.mdc.template`](bellows-iot.mdc.template) | Embedded / IoT | Is this reliable and safe for constrained environments? |

### Data family (2 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`bellows-bigdata.mdc.template`](bellows-bigdata.mdc.template) | Big Data & Data Engineering | Is data engineered, governed, and processed correctly? |
| [`bellows-datascience.mdc.template`](bellows-datascience.mdc.template) | Data Science & ML | Are models valid, reproducible, and responsible? |

### Product family (5 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`bellows-product-management.mdc.template`](bellows-product-management.mdc.template) | Product Management | Are we building the right product for the right market? |
| [`bellows-ba.mdc.template`](bellows-ba.mdc.template) | Business Analysis | Do we understand what stakeholders need? |
| [`bellows-ux.mdc.template`](bellows-ux.mdc.template) | UX / UI Design | Is this usable, desirable, and accessible? |
| [`bellows-marketing.mdc.template`](bellows-marketing.mdc.template) | Marketing | Can we acquire, engage, and retain users? |
| [`bellows-cs.mdc.template`](bellows-cs.mdc.template) | Customer Success | Will users achieve their goals? |

### Governance family (1 discipline)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`bellows-pm.mdc.template`](bellows-pm.mdc.template) | Project Management | Are we delivering within constraints? |

### Cross-cutting (2 disciplines)

| Template | Discipline | Core challenge |
|----------|-----------|----------------|
| [`bellows-security.mdc.template`](bellows-security.mdc.template) | Security | Is this safe from attacks and breaches? |
| [`bellows-compliance.mdc.template`](bellows-compliance.mdc.template) | Compliance | Does this meet regulatory obligations? |

### Family aggregators

| Template | Activates |
|----------|-----------|
| [`bellows-family-engineering.mdc.template`](bellows-family-engineering.mdc.template) | All 7 engineering Bellows |
| [`bellows-family-data.mdc.template`](bellows-family-data.mdc.template) | Both data Bellows |
| [`bellows-family-product.mdc.template`](bellows-family-product.mdc.template) | All 5 product Bellows |
| [`bellows-all.mdc.template`](bellows-all.mdc.template) | Master routing — suggests which Bellows based on context |

## Adopting Bellows in a consuming repo

1. Copy the templates you need to `.cursor/rules/` in your repo (remove `.template` suffix).
2. Update `globs:` in each rule to match your project's file structure.
3. Configure which Bellows are active in `forge.config.yaml` (via the setup wizard).
4. Use family aggregators to activate discipline groups without configuring each individually.

See [`BELLOWS-CONTRACT.md`](BELLOWS-CONTRACT.md) for the standard structure every Bellows rule must follow.
