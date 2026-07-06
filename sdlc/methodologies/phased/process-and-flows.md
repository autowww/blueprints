---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Phased delivery — major processes & flow maps

## 1. Classic stage sequence (simplified)

```blueprint-diagram
key: linear
alt: Classic stage sequence (simplified)
title: Classic phased stage sequence
summary: How phased delivery advances through governed stages, producing baselines consumed by the next stage.
node: Start
detail: The program enters the phased lifecycle with an approved charter or mandate.
more: Initiation establishes scope boundaries and sponsors before any stage baseline is committed.
node: Core steps (see walkthrough below)
detail: Each stage executes work and proves exit criteria at transition gates.
more: Stages may overlap where policy allows; gates sit on arrows and each stage produces baselines the next consumes.
node: Outcome
detail: The sequence closes with released capability and recorded learnings.
more: Map org stage names to blueprint phases A–F so RAID, audits, and agents share one language.
fallback_ascii: |
  Classic stage sequence (simplified)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

Overlap stages where policy allows; **gates** sit on arrows.

## 2. Gate decision

```blueprint-diagram
key: decision
alt: Gate decision
title: Phase gate decision
summary: How a checkpoint decides whether the program continues, refines, or escalates based on exit criteria.
node: Current state
detail: The phase under review with its artifacts and open risks visible.
node: Checkpoint / gate
detail: Sponsors evaluate exit criteria packs for quality, risk, and readiness.
more: Gate packs prove exit criteria; failed criteria mean hold and corrective actions, not silent waivers.
node: refine or escalate
detail: Criteria not met triggers rework, deferral, or steering escalation.
more: Hold and corrective actions replace silent waivers; replan and kill remain valid outcomes.
node: Continue flow
detail: Approved criteria commit spend and authorize the next baseline.
more: Sponsor or steering approval advances the program to the next stage baseline.
fallback_ascii: |
  Gate decision

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

## 3. Change control path (scope)

```blueprint-diagram
key: linear
alt: Change control path (scope)
title: Scope change control path
summary: How governed change requests protect schedule, cost, risk, and traceability baselines.
node: Start
detail: A proposed scope change enters the formal control path.
node: Core steps (see walkthrough below)
detail: Impact analysis feeds steering with schedule, cost, risk, and traceability effects.
more: Change requests and impact analysis feed steering decisions: re-baseline with versioned artifacts, or reject and queue.
node: Outcome
detail: Steering approves a re-baselined artifact set or rejects the request.
more: Ad-hoc scope without this path breaks audit trails and baseline integrity.
fallback_ascii: |
  Change control path (scope)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 4. Traceability thread

```blueprint-diagram
key: linear
alt: Traceability thread
title: Requirements traceability thread
summary: How requirement identifiers thread through design, test, and release for auditable coverage.
node: Start
detail: A governed requirement ID anchors the traceability chain.
node: Core steps (see walkthrough below)
detail: Links propagate from design through test cases to release notes.
more: Requirement ID → design → test case → release note supports impact analysis and demonstrates coverage to auditors.
node: Outcome
detail: The thread yields reviewable evidence of end-to-end coverage.
fallback_ascii: |
  Traceability thread

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 5. Phases A–F (typical mapping)

| Blueprint phase | Typical phased locus |
|-----------------|----------------------|
| A Shape | Initiate; charter; high-level requirements |
| B Plan | Planning; WBS; schedule baseline |
| C Build | Design and implementation per baseline |
| D Verify | Test phases; inspections; exit evidence |
| E Release | UAT; deployment; handover |
| F Learn | Operate; warranty; benefits realization |

## 6. Flow details (walkthrough)

**Stage sequence** — The linear diagram is pedagogical; real programs may overlap stages where policy allows. Gates sit on transitions; each stage produces baselines the next consumes. Map org stage names to blueprint A–F for one language across RAID, audits, and agents.

**Gate decision** — Gate packs prove exit criteria (quality, risk, readiness). Failed criteria mean hold and corrective actions, not silent waivers. Sponsor or steering approval commits spend and the next baseline; defer, kill, or replan are valid.

**Change control** — Change requests and impact analysis (schedule, cost, risk, traceability) feed steering decisions: re-baseline with versioned artifacts, or reject/queue. Ad-hoc scope without this path breaks audit trails.

**Traceability** — Requirement ID → design → test case → release note supports impact analysis and demonstrates coverage to auditors.

## 7. Authoritative sources & further reading

- [ISO/IEC/IEEE 12207 (catalogue)](https://www.iso.org/standard/63712.html) — International software life-cycle processes (full text licensed).
- [Wikipedia — Project Management Body of Knowledge (PMBOK)](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) — Overview of knowledge areas and process groups.
- [Wikipedia — Waterfall model](https://en.wikipedia.org/wiki/Waterfall_model) — Informal sequential-lifecycle context (not normative for your SDLC).
- [Wikipedia — Agile software development](https://en.wikipedia.org/wiki/Agile_software_development) — Contrast with iterative approaches when blending gates and iterations.

[PMI — Standards & guides](https://www.pmi.org/standards) is listed in [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md) for practitioner depth (some networks block automated fetches to `pmi.org`).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodologies-phased-delivery.html)
