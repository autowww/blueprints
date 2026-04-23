---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Decision analysis — [Decision Title]

<!--
  Copy this template into docs/product/, docs/requirements/, or docs/adr/ as appropriate.
  Use for structured evaluation of alternatives using weighted criteria.
  See blueprints/ba/techniques/README.md (Decision analysis) for context.
  For architectural decisions, consider the ADR format in docs/adr/ instead.
-->

## 1. Decision context

| Field | Detail |
|-------|--------|
| **Decision** | (What is being decided?) |
| **Trigger** | (What prompted this decision?) |
| **Owner** | (Who makes the final call?) |
| **Participants** | (Who contributed to the analysis?) |
| **Date** | YYYY-MM-DD |
| **Deadline** | YYYY-MM-DD |
| **Status** | Open / Decided / Deferred |

---

## 2. Options

<!--
  Describe each option being evaluated.
  Include "do nothing" as an explicit option when applicable.
-->

### Option A: [Name]

**Description:** ...

**Pros:**
- ...

**Cons:**
- ...

**Estimated cost / effort:** ...

### Option B: [Name]

**Description:** ...

**Pros:**
- ...

**Cons:**
- ...

**Estimated cost / effort:** ...

### Option C: Do nothing

**Description:** Maintain current state; accept existing limitations.

**Pros:**
- No investment required

**Cons:**
- ...

---

## 3. Evaluation criteria

<!--
  Define the criteria used to evaluate options.
  Assign weights that reflect relative importance (weights should sum to 100 or 1.0).
-->

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| | **Total** | 100 | |

---

## 4. Scoring matrix

<!--
  Score each option against each criterion (e.g., 1–5 scale).
  Weighted score = score × weight.
-->

| Criterion | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted | Option C Score | Option C Weighted |
|-----------|--------|---------------|-------------------|---------------|-------------------|---------------|-------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| **Total** | | | **0** | | **0** | | **0** |

---

## 5. Risk assessment

<!--
  Key risks for each option, beyond what the scoring matrix captures.
-->

| Option | Key Risks | Mitigation |
|--------|-----------|------------|
| A | | |
| B | | |
| C | | |

---

## 6. Recommendation

| Field | Detail |
|-------|--------|
| **Recommended option** | |
| **Rationale** | (Why this option? Reference scoring, risks, and qualitative factors.) |
| **Conditions / assumptions** | |
| **Next steps** | |

---

## 7. Decision record

| Field | Detail |
|-------|--------|
| **Decision made** | |
| **Decided by** | |
| **Date** | YYYY-MM-DD |
| **Rationale** | (If different from recommendation, explain why.) |

---

*Last updated: YYYY-MM-DD · Owner: [name/role]*
