---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Spiral Model — major processes & flow maps

## 1. Spiral quadrant cycle

```blueprint-diagram
key: linear
alt: Spiral quadrant cycle
title: Spiral quadrant cycle
summary: How each spiral pass cycles four quadrants from objectives through risk-gated build to evaluation.
node: Start
detail: A new spiral begins with the current product and risk posture.
more: Each pass through all four quadrants counts as one spiral; numbering tracks maturity, not calendar time alone.
node: Core steps (see walkthrough below)
detail: Q1 sets direction, Q2 manages risk, Q3 produces work, Q4 evaluates and plans.
more: Q2 gates commitment to expensive Q3 build; no significant construction proceeds without acceptable risk resolution.
node: Outcome
detail: The spiral closes with stakeholder evaluation and the next spiral's entry criteria.
fallback_ascii: |
  Spiral quadrant cycle

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

Each pass through the four quadrants is one **spiral**. Risk analysis (Q2) gates commitment to build (Q3).

## 2. Risk-driven decision (Q2 detail)

```blueprint-diagram
key: decision
alt: Risk-driven decision (Q2 detail)
title: Risk-driven Q2 gate
summary: How Q2 risk analysis decides whether the spiral continues build work or refines approach.
node: Current state
detail: The spiral's scope, known threats, and unresolved uncertainties are visible.
node: Checkpoint / gate
detail: Risk analysis evaluates whether threats are acceptable for current commitment.
more: Q2 produces actionable resolution: prototype feasibility tests, safeguards, monitored acceptance, or approach change.
node: refine or escalate
detail: Unacceptable risk triggers refinement, scope change, or escalation.
more: The cycle repeats until risk fits the current spiral scope before Q3 build commitment.
node: Continue flow
detail: Acceptable risk authorizes Q3 development within the bounded spiral scope.
fallback_ascii: |
  Risk-driven decision (Q2 detail)

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 3. Anchor-point milestone sequence

```blueprint-diagram
key: linear
alt: Anchor-point milestone sequence
title: Anchor-point milestone gates
summary: How LCO, LCA, and IOC commitment gates pace spiral investment across the program.
node: Start
detail: The program begins toward the first anchor-point commitment gate.
node: Core steps (see walkthrough below)
detail: LCO, LCA, and IOC gates confirm worth, architecture fitness, and operational readiness.
more: These are stakeholder commitment gates—each decides whether to invest in the next phase of spirals.
node: Outcome
detail: Passed gates authorize deeper spirals; failed gates halt or redirect investment.
fallback_ascii: |
  Anchor-point milestone sequence

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

Milestone count and spiral numbering are illustrative; actual projects adjust based on risk and scope.

## 4. Spiral scope evolution

```blueprint-diagram
key: linear
alt: Spiral scope evolution
title: Spiral scope evolution
summary: How spiral scope and engineering intensity grow as confidence and risk acceptance increase.
node: Start
detail: Early spirals explore objectives with minimal committed scope.
node: Core steps (see walkthrough below)
detail: Each spiral expands scope and verification depth as confidence grows.
more: Early spirals stay cheap and exploratory; throwaway prototypes are valid. Later spirals become more engineering-intensive.
node: Outcome
detail: Progressive commitment yields a mature product without premature large-scale investment.
more: This graduated commitment is the model's core risk management strategy.
fallback_ascii: |
  Spiral scope evolution

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 5. Phases A–F (Spiral mapping per spiral)

| Blueprint phase | Typical Spiral locus | Notes |
|-----------------|----------------------|-------|
| A Shape | Q1: Objectives, constraints | Revisited each spiral with increasing detail |
| B Plan | Q1 + Q4: Spiral planning, risk approach | Plan adapts to current risk profile |
| C Build | Q3: Development, prototyping | Scope matches spiral maturity |
| D Verify | Q3: Testing against spiral objectives | Verification depth grows with product maturity |
| E Release | Q4: Milestone review, stakeholder commit | Early releases are internal (demos); later are operational |
| F Learn | Q4 → next Q1: Feedback loop | Systematic learning drives next spiral |

## 6. Flow details (walkthrough)

**Quadrant cycle** — The four quadrants are not sequential phases but a repeated cycle. Q1 sets direction, Q2 manages risk, Q3 produces work, Q4 evaluates and plans. The model's power is in the Q2 gate: no commitment to expensive build work without understanding risks.

**Risk-driven decision** — Q2 produces actionable risk resolution: build a prototype to test feasibility, add safeguards for known threats, accept monitored risks, or change approach to avoid them entirely. The cycle repeats until risk is acceptable for the current spiral's scope.

**Anchor-point milestones** — LCO confirms the project is worth doing. LCA confirms the architecture can support it. IOC confirms the system is ready for users. These are **commitment gates** — stakeholders decide whether to invest in the next phase of spirals.

**Scope evolution** — Early spirals are cheap, exploratory, and may produce throwaway prototypes. As confidence grows, spirals become more engineering-intensive. This progressive commitment is the model's core risk management strategy.

## 7. Authoritative sources & further reading

- [Wikipedia — Spiral model](https://en.wikipedia.org/wiki/Spiral_model) — Stable overview of quadrants and history.
- [Wikipedia — Barry Boehm](https://en.wikipedia.org/wiki/Barry_Boehm) — Author context.
- [IEEE — Boehm 1988 paper](https://doi.org/10.1109/2.59) — Original publication (may require IEEE access).
- [SEI/CMU](https://resources.sei.cmu.edu/) — Software Engineering Institute resources.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodologies-spiral.html)
