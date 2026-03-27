# Product bootstrap flow — from zero to first Charge

This document describes the step-by-step process for bootstrapping a new product through dialog using the Forge Product Manager agent. Each step produces a concrete artifact seeded from blueprint templates.

## Prerequisites

- Forge SDLC is configured (`forge/forge.config.yaml` exists, or run `forge-setup` first).
- `blueprints/` is available as a submodule or copy.
- `docs/product/` directory exists (or will be created during bootstrap).

## The pipeline

```ks-diagram
key: linear
alt: Diagram
```

---

## Step 1: Problem definition

**PDLC phase:** P1 (Discover)

**Goal:** Articulate the core problem in customer language.

**Dialog questions:**
- Who is the target user or customer?
- What problem or unmet need do they have?
- How are they solving it today (alternatives, workarounds)?
- Why does this problem matter (frequency, severity, willingness to pay)?

**Output:** Populate `docs/product/vision/VISION.md` using template:
- `blueprints/product/templates/VISION.template.md` (lightweight) or
- `blueprints/pdlc/templates/PRODUCT-VISION.template.md` (comprehensive)

**Versona checkpoint:** Consider invoking BA Versona to challenge problem clarity.

---

## Step 2: Market analysis

**PDLC phase:** P1 (Discover)

**Goal:** Size the opportunity and understand market dynamics.

**Dialog questions:**
- What market or category does this product belong to?
- How large is the total addressable market (TAM)?
- What segments can you realistically serve (SAM)?
- What share can you realistically capture near-term (SOM)?
- What market trends or technology shifts are relevant?
- What regulatory or compliance constraints exist?

**Output:** Create `docs/product/discovery/market-analysis.md` using template:
- `blueprints/pdlc/templates/MARKET-ANALYSIS.template.md`

---

## Step 3: Competitive landscape

**PDLC phase:** P1 (Discover)

**Goal:** Map the competitive landscape and identify differentiation.

**Dialog questions:**
- Who are the direct competitors (same problem, same audience)?
- Who are the indirect competitors (same problem, different approach)?
- Who could enter this market (adjacent players, platforms)?
- Where do competitors excel? Where are they weak?
- What is your differentiation — the 1–2 things no competitor matches?
- What moats exist or can be built (network effects, data, switching costs)?

**Output:** Create `docs/product/discovery/competitive-analysis.md` using template:
- `blueprints/pdlc/templates/COMPETITIVE-ANALYSIS.template.md`

**Versona checkpoint:** Consider invoking Product Management Versona to challenge competitive positioning.

---

## Step 4: Business case

**PDLC phase:** P3 (Strategize) — or P1 for lightweight version

**Goal:** Justify the investment with costs, benefits, and risks.

**Dialog questions:**
- What is the estimated cost to build (time, people, infrastructure)?
- What are the expected benefits (revenue, cost savings, strategic value)?
- What are the key risks and assumptions?
- What alternatives were considered?
- What does success look like (quantified)?

**Output:** Create `docs/product/business-case.md` using template:
- `blueprints/disciplines/product/ba/templates/business-case.template.md`

---

## Step 5: Product vision and metrics

**PDLC phase:** P3 (Strategize)

**Goal:** Define the product vision, OKRs, and success metrics.

**Dialog questions:**
- What is the product vision (one sentence)?
- What are the top 2–3 objectives for the next 6–12 months?
- What key results would prove progress on each objective?
- What is the North Star metric?
- What health metrics must not degrade?

**Output:**
- Update `docs/product/vision/VISION.md` with strategy sections.
- Create `docs/product/metrics/PRODUCT-METRICS.md` using `blueprints/pdlc/templates/PRODUCT-METRICS.template.md`.

---

## Step 6: High-level roadmap

**PDLC phase:** P3 (Strategize)

**Goal:** Sequence initiatives against the strategy.

**Dialog questions:**
- What are the major themes or initiatives for the next 2–4 quarters?
- What is the delivery approach for each (PoC, MVP, Phase)?
- What are the dependencies between themes?
- What is committed (near-term) vs aspirational (far-term)?

**Output:** Create `docs/ROADMAP.md` using:
- `blueprints/sdlc/templates/ROADMAP.template.md`

Structure the roadmap as: NOW (committed, next 1–2 iterations) / NEXT (planned, next quarter) / LATER (aspirational, 2+ quarters).

Before **Step 7**, apply **Roadmap Definition of Ready** to each theme or row (**Outcome**, **Evidence**, **Horizon**, **OKR / strategy fit**, **Dependencies**, **Non-goals**, **Next gate**) — see [`forge-product-manager.mdc.template`](forge-product-manager.mdc.template).

**Versona checkpoint:** After the roadmap is drafted, run **Product Management Versona** (`versona-product-management`) or **`versona-all`** if routing is unclear; follow **Suggested next Versonas** in the challenge output before deep WBS. Optional playbook: [`../versona/catalog/workflow/versona-roadmap-gate.mdc.template`](../versona/catalog/workflow/versona-roadmap-gate.mdc.template).

---

## Step 7: WBS decomposition

**PDLC phase:** P3 / SDLC Phase A

**Goal:** Break the roadmap into a work breakdown structure.

**Dialog questions:**
- What are the major themes (high-level groupings)?
- For each theme, what are the epics (large deliverables)?
- For each epic, what are the stories (user-facing value units)?
- For each story, what tasks are needed?

**Output:** Create `docs/requirements/WBS.md` using:
- `blueprints/pdlc/templates/WBS.template.md`

Use the project's ID scheme (e.g. `M1E1S1T1`) as defined in `PLANNING-FLOW.md`.

**Versona checkpoint:** Consider **BA Versona** for requirements completeness, **Project Management Versona** (governance) for delivery constraints and schedule feasibility. **Product Management Versona** should already have challenged the roadmap at Step 6; do not substitute governance PM for that product-strategy pass.

---

## Step 8: First Product Spark

**PDLC phase:** P3 → SDLC Phase A

**Goal:** Define the first Product Spark with a clear delivery approach.

**Dialog questions:**
- What is the highest-priority initiative from the roadmap?
- What is the appropriate approach: PoC (validate hypothesis), MVP (deliver core value), or Phase (incremental capability)?
- What are the Assay Gate criteria for this Product Spark?
- How many Forge iterations will this take (estimate)?

**Output:** Create the Product Spark plan using the appropriate template:
- PoC: `blueprints/sdlc/methodologies/forge/planning/poc-plan.template.md`
- MVP: `blueprints/sdlc/methodologies/forge/planning/mvp-plan.template.md`
- Phase: `blueprints/sdlc/methodologies/forge/planning/phase-plan.template.md`

Place the plan in `forge/releases/` or `docs/requirements/` per project convention.

---

## Step 9: First Charge

**Goal:** Populate the first Forge Charge with product bootstrap Sparks.

If product artifacts from Steps 1–8 are not yet complete, use the [first charge template](first-charge.template.md) to create a Charge that completes them as Sparks.

If Steps 1–8 are complete, skip to Step 10 and create a Charge with implementation Sparks.

**Output:** Create or update `forge/charge.md` from:
- `first-charge.template.md` (this package) — if bootstrapping
- `blueprints/sdlc/methodologies/forge/daily/charge.template.md` — if ready for implementation

---

## Step 10: Plan Sparks through dialog

**Goal:** Decompose the first Product Spark into phase-tagged Sparks.

**Dialog approach:**
1. List the Ingots (Epics/Stories) from the WBS that belong to this Product Spark.
2. For each Ingot, decompose into Sparks with phase prefixes:
   - `discover:` — research, interviews, analysis
   - `specify:` — requirements, acceptance criteria, specifications
   - `design:` — architecture, UX design, data modeling
   - `build:` — implementation, integration
   - `verify:` — testing, validation, QA
   - `release:` — deployment, documentation, communication
3. Estimate each Spark (1–4 hours).
4. Assign Sparks to Forge iterations.
5. Identify which Versonas should challenge which Sparks.

**Output:** Updated backlog with phase-tagged Sparks assigned to iterations.

---

## After bootstrap

Once the first Charge is populated and Sparks are planned:

1. **Begin daily execution** using `forge-daily` — pull Sparks into Charge, switch hats, log in journal.
2. **Run Versona challenges** at refinement and review ceremonies.
3. **Update the roadmap** as you learn — new Ore from P5 discovery.
4. **Prepare for Assay Gate** — assemble evidence against the Product Spark's criteria.

---

## References

- [PLANNING-FLOW.md](../planning/PLANNING-FLOW.md) — Forge planning pipeline
- [FORGE-SDLC-PDLC-BRIDGE.md](../FORGE-SDLC-PDLC-BRIDGE.md) — Forge lifecycle bridge
- [ceremonies-prescriptive.md](../ceremonies-prescriptive.md) — ceremony details
- [PRODUCT-MANAGEMENT.md](../../../../disciplines/product/product-management/PRODUCT-MANAGEMENT.md) — body of knowledge
- [PRODMGMT-SDLC-PDLC-BRIDGE.md](../../../../disciplines/product/product-management/PRODMGMT-SDLC-PDLC-BRIDGE.md) — lifecycle bridge
