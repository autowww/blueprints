---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Lean Software Development — major processes & flow maps

## 1. Value-stream overview (idea to production)

```blueprint-diagram
key: linear
alt: Value-stream overview (idea to production)
title: Idea to production stream
summary: How work moves from demand to delivery with measurable lead time across the full value stream.
node: Value-stream overview (idea to production)
detail: Frames the end-to-end path from idea through production delivery.
more: Lean teams map this stream to expose waiting, handoffs, and queues between active work.
node: Start
detail: Demand or a validated idea enters the value stream.
node: Core steps (see walkthrough below)
detail: Work progresses through shape, plan, build, verify, release, and learn phases.
more: Section 7 and the phases table define lean focus and metrics for each blueprint phase.
node: Outcome
detail: Delivered value reaches production with traceable elapsed time.
more: Lean compares total lead time to active work time; the gap surfaces systemic waste.
fallback_ascii: |
  Value-stream overview (idea to production)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: lead time
```

Lean measures **lead time** across the entire stream and **waiting time** between steps.

## 2. Waste identification loop

```blueprint-diagram
key: decision
alt: Waste identification loop
title: Waste identification loop
summary: A repeating cycle that maps current flow, finds waste, and standardizes proven countermeasures.
node: Current state
detail: The team documents how work actually moves today.
more: Value-stream mapping and the seven-waste taxonomy in section 6 guide what to observe.
node: Checkpoint / gate
detail: A review point asks whether waste is identified and actionable.
node: refine or escalate
detail: Countermeasures need rework or a higher-level decision before proceeding.
node: Continue flow
detail: Valid countermeasures advance into the live process.
more: Successful changes are standardized so the loop restarts from an improved current state.
fallback_ascii: |
  Waste identification loop

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

## 3. A3 problem-solving flow

```blueprint-diagram
key: linear
alt: A3 problem-solving flow
title: A3 problem-solving flow
summary: A structured, concise path for analyzing complex problems and validating countermeasures.
node: A3 problem-solving flow
detail: Frames the A3 format as the bounded container for the investigation.
node: Start
detail: A complex problem worth structured analysis enters the flow.
node: Core steps (see walkthrough below)
detail: Each A3 section builds on the prior with forced conciseness.
more: Background, current state, root cause, countermeasures, and follow-up sections must justify the next step.
node: Outcome
detail: A reviewed countermeasure plan ready for execution or standardization.
more: Review validates reasoning quality before changes reach the value stream.
fallback_ascii: |
  A3 problem-solving flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 4. Pull-based work selection

```blueprint-diagram
key: linear
alt: Pull-based work selection
title: Pull-based work selection
summary: Work enters execution only when capacity exists, limiting WIP and queue waste.
node: Pull-based work selection
detail: Frames selection by available capacity rather than pushed demand volume.
node: Start
detail: Ready work waits in a governed queue until a slot opens.
node: Core steps (see walkthrough below)
detail: The team pulls the highest-priority item matching current capacity.
more: WIP limits prevent overload; this operationalizes deliver-as-fast-as-possible without batching waste.
node: Outcome
detail: Bounded work in progress flows to completion at sustainable pace.
fallback_ascii: |
  Pull-based work selection

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 5. Phases A–F (Lean focus areas)

| Blueprint phase | Lean focus | Key metric |
|-----------------|-----------|------------|
| A Shape | Define value; avoid over-specification | Time from idea to "ready" |
| B Plan | Last responsible moment; pull-based commitment | Queue time before start |
| C Build | Small batches; eliminate task switching | Cycle time per item |
| D Verify | Built-in quality; catch defects at source | Defect escape rate |
| E Release | Automate deployment; reduce batch size | Deploy lead time |
| F Learn | Production feedback; close the loop | Time from deploy to insight |

## 6. Seven wastes in software (reference)

| Manufacturing waste | Software equivalent |
|--------------------|---------------------|
| Overproduction | Features nobody uses |
| Inventory | Partially done work (branches, specs not implemented) |
| Motion | Task switching between unrelated work |
| Waiting | Blocked items; waiting for review, approval, environment |
| Transportation | Unnecessary handoffs between teams or phases |
| Over-processing | Gold-plating; excessive ceremony for the risk level |
| Defects | Bugs, rework, misunderstood requirements |

## 7. Flow details (walkthrough)

**Value-stream overview** — Every piece of work flows from demand to delivery. Lean measures the total elapsed time, not just active work time. The gap between active and elapsed is waste (waiting, handoffs, queues).

**Waste identification** — Map the current state, identify waste using the seven-waste taxonomy, analyze root causes, design and test countermeasures, then standardize what works. This is a continuous cycle, not a one-time exercise.

**A3 problem-solving** — A structured approach to complex problems. The A3 paper format forces conciseness. Each section builds on the previous; the review validates reasoning quality.

**Pull-based selection** — Work is pulled when capacity exists, not pushed based on demand volume. WIP limits prevent overloading. This is the operational mechanism behind "deliver as fast as possible."

## 8. Authoritative sources & further reading

- [Wikipedia — Lean software development](https://en.wikipedia.org/wiki/Lean_software_development) — Overview of principles and history.
- [Wikipedia — Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System) — Manufacturing roots.
- [Wikipedia — Value-stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping) — The diagnostic tool for waste identification.
- [Lean Enterprise Institute](https://www.lean.org/) — Practitioner community.
- [Agile Alliance — Lean software development](https://www.agilealliance.org/glossary/lean-software-development/) — Glossary entry.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 9. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodology-lean.html)
