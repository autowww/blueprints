# Spiral Model — connection to the SDLC foundation

The Spiral Model treats each development cycle as a **risk-driven** pass through planning, risk analysis, engineering, and evaluation. The blueprint's **A–F** phases still apply; the Spiral adds **explicit risk gates** and **iterative deepening** across multiple passes.

## 1. SDLC phases A–F (how Spiral maps)

Each spiral is a **partial or full** pass through A–F, with increasing fidelity:

| Phase | Spiral expression | Notes |
|-------|-------------------|-------|
| **A — Shape** | Q1: Determine objectives, alternatives, constraints | Each spiral refines scope based on prior learning |
| **B — Plan** | Q1 + Q4: Plan the approach for this cycle; select risk-reduction strategy | Early spirals may plan only a prototype; later spirals plan full build |
| **C — Build** | Q3: Develop the increment (prototype, partial, or full) | Scope matches the risk profile of this spiral |
| **D — Verify** | Q3: Test and validate against objectives | Verification depth matches the spiral's maturity |
| **E — Release** | Q4: Stakeholder review; anchor-point milestone if applicable | Release may be internal (demo) or external (IOC) |
| **F — Operate & learn** | Q4 → next Q1: Feedback from this spiral feeds objectives for the next | Learning is **systematic**, not incidental |

**Prescriptive rule:** Every spiral must pass through **Q2 (risk analysis)** before committing resources to Q3 (build). Skipping risk analysis defeats the model's purpose.

## 2. Tracking spine (mandatory link)

Spiral teams maintain the blueprint tracking spine across spirals:

| Artifact | Spiral mapping |
|----------|----------------|
| **Intent / request** | Objectives defined in Q1 of each spiral |
| **Spec** | Evolves across spirals; early specs may be high-level concepts, later specs are detailed |
| **Plan** | Spiral plan (Q1+Q4); includes risk-reduction approach |
| **Tasks** | Engineering tasks within Q3 |
| **PRs** | Implementation within Q3; link to risk items resolved |
| **Reviews** | Q4 stakeholder review; anchor-point milestones |
| **Release** | IOC or operational release in later spirals |

**Prescriptive rule:** Maintain a **risk register** as a first-class artifact alongside the tracking spine. Each spiral should reference risks addressed and residual risks carried forward.

## 3. Ceremony intents (C1–C6) ↔ Spiral quadrants

| Intent | Spiral practice | Notes |
|--------|-----------------|-------|
| **C1 — Align & decide** | Q1: Objectives workshop; stakeholder alignment on goals and constraints | Each spiral re-aligns based on prior results |
| **C2 — Plan the slice** | Q1 + Q4: Spiral planning; commitment to risk-reduction approach | Commit to the **approach**, not just the deliverable |
| **C3 — Execute & unblock** | Q3: Development coordination; risk-driven prioritization | Address highest-risk items first within the spiral |
| **C4 — Review & quality** | Q4: Stakeholder review; anchor-point milestone evaluation | Evidence-based review; prototype demos for early spirals |
| **C5 — Reflect & improve** | Q4: Lessons learned; process improvement across spirals | Compare actual vs predicted risk outcomes |
| **C6 — Knowledge share** | Q2: Risk analysis results; Q4: milestone evidence packages | Risk knowledge is critical cross-spiral context |

See [ceremony foundation](../ceremonies/ceremony-foundation.md) and [methodology bridge](../ceremonies/methodology-bridge.md).

## 4. Role archetypes (blueprint hats on a Spiral team)

| Spiral role | Typical archetype emphasis | Notes |
|-------------|----------------------------|-------|
| **Project manager** | **Orchestrator** | Plans spirals; coordinates stakeholders; manages schedule and resources |
| **Risk analyst / chief engineer** | **Quality advocate** + **Orchestrator** | Drives Q2 risk identification and resolution strategy |
| **Chief architect** | **Implementer** + **Quality advocate** | Technical decisions; architecture evolution across spirals |
| **Development team** | **Implementer** | Executes Q3 within the risk-driven plan |
| **Stakeholders / sponsors** | **Sponsor proxy** + **Steer** | Commit resources at anchor-point milestones |

Detail: [roles-archetypes.md](../roles-archetypes.md), [Spiral roles chapter](roles.md).

## 5. What Spiral adds beyond the foundation

- **Risk-driven iteration** — risk analysis gates every cycle.
- **Anchor-point milestones** — LCO, LCA, IOC structure stakeholder commitment.
- **Flexible process** — each spiral can contain any sub-process (prototype, waterfall phase, Agile iteration).
- **Cumulative progress** — the model explicitly tracks increasing investment and fidelity.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| Skipping risk analysis in Q2 | Q2 is the model's core value; without it, you have uncontrolled iteration |
| Treating every spiral identically | Early spirals are exploratory (prototypes); later spirals are engineering-grade |
| No stakeholder commitment at anchor points | Anchor-point reviews prevent runaway investment; insist on explicit go/no-go |
| Using Spiral for low-risk projects | Overhead may not be justified; consider Agile or phased delivery instead |

## 7. References in-repo

- [`https://forgesdlc.com/methodologies-spiral.html`](https://forgesdlc.com/methodologies-spiral.html) — methodology summary + diagram  
- [`../ceremonies/spiral.md`](../ceremonies/spiral.md) — fork table C1–C6  
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview  
