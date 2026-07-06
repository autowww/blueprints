---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# V-Model — major processes & flow maps

## 1. V-Model structure (classic)

```blueprint-diagram
key: linear
alt: V-Model structure (classic)
title: Classic V-Model structure
summary: How left-side decomposition pairs with right-side integration and verification across levels.
node: Start
detail: Entry point for applying the classic V lifecycle discipline.
node: Core steps (see walkthrough below)
detail: Descend through specification levels; ascend through matching verification levels.
more: Each left-side level produces specifications the corresponding right-side level verifies; test planning pairs with design rather than following implementation.
node: Outcome
detail: Integrated system validated with traceability across every V-level.
more: Dotted arrows link each specification level to its verification counterpart on the ascent.
fallback_ascii: |
  V-Model structure (classic)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

Left side descends (decomposition); right side ascends (integration and verification). Dotted arrows show traceability pairing.

## 2. Traceability flow

```blueprint-diagram
key: linear
alt: Traceability flow
title: Requirement-to-evidence traceability
summary: How requirements link to tests and recorded results as the V-Model core deliverable.
node: Start
detail: A stakeholder need or requirement enters the traceability chain.
node: Core steps (see walkthrough below)
detail: Map each requirement to tests and capture results as reviewable evidence.
more: Every requirement must be testable, every test traces to a requirement, and every result is recorded; gaps indicate missing tests or unnecessary requirements.
node: Outcome
detail: A complete requirement-to-evidence chain with no traceability gaps.
fallback_ascii: |
  Traceability flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 3. Test-level gate decision

```blueprint-diagram
key: linear
alt: Test-level gate decision
title: V-level test gate checks
summary: How entry and exit gates at each V-level govern test readiness and recorded results.
node: Start
detail: A verification activity at a given V-level begins.
node: Core steps (see walkthrough below)
detail: Pass entry readiness, execute tests, then evaluate exit results.
more: Entry checks confirm test readiness; exit checks record results; failures feed back to the matching development level, not a generic fix phase.
node: Outcome
detail: Level exit with documented results or bounded rework at the source level.
fallback_ascii: |
  Test-level gate decision

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 4. Change impact (V-Model perspective)

```blueprint-diagram
key: linear
alt: Change impact (V-Model perspective)
title: V-Model change ripple analysis
summary: How a requirement change propagates across design, implementation, and tests at multiple levels.
node: Start
detail: A change request targets a requirement or specification artifact.
node: Core steps (see walkthrough below)
detail: Analyze impact across all affected V-levels before committing rework.
more: A requirement change may require design updates, code changes, and retesting at unit, integration, system, and acceptance levels.
node: Outcome
detail: Bounded rework plan covering every impacted specification and test level.
fallback_ascii: |
  Change impact (V-Model perspective)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

A change to a requirement potentially impacts design, implementation, and tests at multiple V-levels.

## 5. Phases A–F (V-Model mapping)

| Blueprint phase | V-Model locus |
|-----------------|---------------|
| A Shape | Stakeholder needs; concept of operations |
| B Plan | Requirements analysis + acceptance test planning (paired) |
| C Build | System design → detailed design → implementation (left side descent) |
| D Verify | Unit → integration → system testing (right side ascent) |
| E Release | Acceptance testing; deployment readiness |
| F Learn | Operational validation; field feedback; lessons for next cycle |

## 6. Flow details (walkthrough)

**V-Model structure** — The V is not just a picture; it encodes a discipline. Each left-side level produces specifications that the corresponding right-side level will verify. Test planning happens during design, not after coding. This early pairing catches specification issues before they become implementation defects.

**Traceability** — The requirement-to-evidence chain is the V-Model's core deliverable. Every requirement must be testable, every test must trace to a requirement, and every test result must be recorded. Gaps in traceability indicate either missing tests or unnecessary requirements.

**Test-level gates** — Each V-level has an entry check (test readiness) and exit check (test results). Failures feed back to the corresponding development level for resolution, not to a generic "fix bugs" phase.

**Change impact** — Changes in the V-Model are expensive because they ripple across levels. Impact analysis must consider all affected V-levels: a requirement change may require design updates, code changes, and retesting at unit, integration, system, and acceptance levels.

## 7. Authoritative sources & further reading

- [Wikipedia — V-model (software development)](https://en.wikipedia.org/wiki/V-model_(software_development)) — Stable overview.
- [Wikipedia — Verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation) — V&V concepts.
- [ISO 26262 (catalogue)](https://www.iso.org/standard/68383.html) — Automotive functional safety (V-Model-aligned).
- [IEC 62304 (catalogue)](https://www.iso.org/standard/71604.html) — Medical device software lifecycle.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodologies-v-model.html)
