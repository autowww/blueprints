---
product_spark: F{n}
type: poc
status: planning
hypothesis:
target_date:
---

# PoC plan — {name}

## Hypothesis

<!-- What are we trying to learn? State as a testable hypothesis. -->

**If** {we do X}, **then** {we expect Y}, **because** {assumption Z}.

## Success criteria

<!-- How will we know the PoC answered our question? -->

- [ ] {criterion 1}
- [ ] {criterion 2}

## Scope (minimal)

<!-- The least work needed to validate or invalidate the hypothesis. -->

### Build

<!-- What must be built -->

### Skip

<!-- What we intentionally skip (production quality, full UX, edge cases) -->

## Forge iterations

| Iteration | Sparks focus |
|-----------|-------------|
| F{n} | `discover:` and `build:` Sparks |

## Assay Gate criteria (PoC exit)

- [ ] Hypothesis validated or invalidated with evidence
- [ ] Key findings documented in Ember Log
- [ ] Decision captured: proceed to MVP, pivot, or stop
- [ ] Technical feasibility assessed (Architecture Bellows)

## Bellows challenges

| Discipline | Question |
|------------|----------|
| Architecture | Is this technically feasible at production scale? |
| BA | Does this address a validated user need? |

## Risks

| Risk | Mitigation |
|------|------------|
| PoC scope creep | Strict "skip" list; timebox |
| Confirmation bias | Pre-register hypothesis; Bellows challenge results |
