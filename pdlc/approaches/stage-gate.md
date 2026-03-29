# Stage-Gate

## What it is

**Stage-Gate** is a structured product development framework that divides the innovation process into **stages** (where work happens) separated by **gates** (where decisions happen). At each gate, a cross-functional team reviews evidence and makes an explicit **go / kill / pivot / recycle** decision before allowing the initiative to proceed.

Originally developed by Robert Cooper in the 1980s for physical product development, Stage-Gate has evolved through five generations. The **5th-generation** model (current) integrates Agile practices, AI-assisted decision-making, and adaptive gates — it is not the rigid, waterfall process of earlier versions.

Companies using modern Stage-Gate achieve **63–78% product success rates**, compared to ~24% for ad-hoc approaches (PDMA benchmarking studies).

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [Stage-Gate International](https://www.stage-gate.com/) | **Official** Stage-Gate body of knowledge — Robert Cooper's framework, 5th-generation updates, research, and case studies. The authority for gate criteria and stage definitions. |
| [5th-Generation Stage-Gate Model](https://www.stage-gate.com/about/5th-generation-stage-gate-model/) | **Current evolution** of Stage-Gate: iterative stages, Agile integration, lean gates, adaptive governance — addresses historical criticisms of rigidity. |
| [PDMA — Stage-Gate 2026](https://community.pdma.org/) | **Product Development and Management Association** — practitioner community, research, and updated Stage-Gate guidance. Hosts Cooper's latest articles. |

---

## Core structure

### Stages and gates

The classic 5-stage model, adapted for software products:

```blueprint-diagram
key: linear
alt: Diagram
```

| Stage | Activities | Key deliverable |
|-------|-----------|-----------------|
| **Scoping** | Quick assessment: market, technical, financial, strategic fit | One-page opportunity brief |
| **Build Business Case** | Detailed investigation: user research, competitive analysis, concept testing, feasibility | Business case with evidence |
| **Development** | Design and build the product (via SDLC) | Working increment |
| **Testing & Validation** | Market testing, beta, usability, operational readiness | Validated product ready for launch |
| **Launch** | Market activation, GTM execution, scaling | Product in market |

### Gate decisions

Each gate uses **explicit criteria** — not opinions:

| Decision | Meaning | Action |
|----------|---------|--------|
| **Go** | Evidence meets criteria; proceed to next stage | Fund next stage, assign resources |
| **Kill** | Evidence shows the initiative should not proceed | Stop work, reallocate resources, document learnings |
| **Pivot** | Evidence suggests a different direction is more promising | Recycle to an earlier stage with revised framing |
| **Hold** | Insufficient evidence to decide; more information needed | Time-boxed investigation, then re-gate |

### 5th-generation adaptations

| Evolution | What changed |
|-----------|-------------|
| **Agile integration** | Stages use Agile/Scrum for execution; gates remain as strategic decision points |
| **Lean gates** | Gates are lighter, data-driven, and faster — not bureaucratic review boards |
| **Spiral / iterative stages** | Stages iterate internally (build-test-learn) rather than being strictly sequential |
| **Adaptive** | Gate criteria adjust based on project risk and novelty — higher risk = more rigorous gates |
| **AI-assisted** | AI can prepare gate materials, analyze market data, and flag risks — humans make decisions |

---

## Mapping to PDLC phases

Stage-Gate maps directly to PDLC phases and gates:

| Stage-Gate | PDLC phase | PDLC gate |
|------------|-----------|-----------|
| Gate 0: Idea Screen | — | Pre-P1 screening |
| Stage 1: Scoping | **P1 Discover Problem** | — |
| Gate 1: Second Screen | — | **G1** (problem worth solving?) |
| Stage 2: Business Case | **P2 Validate Solution** + **P3 Plan & Commit** | — |
| Gate 2: Go to Development | — | **G2** (solution viable?) + **G3** (invest in building?) |
| Stage 3: Development | **SDLC A–F** | — |
| Gate 3: Go to Testing | — | (SDLC Phase E exit) |
| Stage 4: Testing & Validation | SDLC E–F + **P4 Launch** (beta) | — |
| Gate 4: Go to Launch | — | **G4** (ready to launch?) |
| Stage 5: Launch | **P4 Launch** (GA) | — |
| Post-Launch Review | **P5 Grow** | **G5** (continue investing?) |

### Using Stage-Gate within this blueprint

Use [`templates/STAGE-GATE-REVIEW.template.md`](../templates/STAGE-GATE-REVIEW.template.md) to document gate decisions. The template captures:
- Gate identifier and date
- Evidence reviewed (with links to artifacts)
- Criteria assessment (met / not met / partially met)
- Decision (go / kill / pivot / hold)
- Conditions for proceeding (if any)
- Resource allocation for next stage

---

## Anti-patterns

| Anti-pattern | Fix |
|-------------|-----|
| **Gates as bureaucratic checkpoints** | Gates should be fast, evidence-based decisions — not multi-day review boards. If gates slow you down, make them leaner, not fewer. |
| **Skipping gates for "urgent" projects** | The riskier the project, the more you need gates. "Urgency" is not evidence of viability. Adapt gate rigor, don't skip. |
| **Gates without kill authority** | If a gate never kills a project, it's theater. Empower gatekeepers to say no. Track kill rate as a health metric. |
| **Waterfall stages** | Use Agile execution within stages. Stage-Gate provides strategic decision points; stages are iterative, not sequential waterfalls. |

---

## Further reading

- [PDLC.md §4 — Stage gates](../PDLC.md) — Gate definitions G1–G5 in this blueprint
- [PDLC-SDLC Bridge §6 — Decision framework](../PDLC-SDLC-BRIDGE.md) — When to use heavy vs light gates
- [Lean Startup](lean-startup.md) — Complementary: hypothesis-driven validation within stages
- [Design Thinking](design-thinking.md) — Complementary: human-centered methods for Stages 1–2
