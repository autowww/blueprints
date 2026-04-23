---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Requirements package — [Feature / Epic Name]

<!--
  Copy this template into docs/requirements/ (or a subdirectory per feature/epic).
  Use for features that need more structure than a single user story.
  See blueprints/ba/knowledge-areas/requirements-analysis-design.md for context.
  See docs/requirements/STRUCTURE-PROPOSAL.md for the project's ID scheme.
-->

## 1. Overview

| Field | Detail |
|-------|--------|
| **Feature / Epic** | |
| **ID** | (e.g., M1E3 — per project ID scheme) |
| **Owner** | |
| **Status** | Draft / In Review / Approved / Superseded |
| **Date created** | YYYY-MM-DD |
| **Last updated** | YYYY-MM-DD |

---

## 2. Business context

<!--
  Why does this feature exist? Link to business case, P1 discovery, or product vision.
-->

| Field | Detail |
|-------|--------|
| **Business objective** | |
| **Problem being solved** | |
| **Target stakeholders** | |
| **Success metrics** | (link to PDLC P3 success metrics if available) |
| **Assumptions** | |
| **Constraints** | |

---

## 3. Functional requirements

<!--
  List functional requirements with unique IDs.
  Use a consistent prefix (e.g., FR- or the project's M{n}E{n}S{n} scheme).
  Each requirement should be verifiable — it must be possible to test whether it is satisfied.
-->

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| | | Must / Should / Could / Won't | |
| | | Must / Should / Could / Won't | |
| | | Must / Should / Could / Won't | |

<!--
  For complex requirements, expand with detailed acceptance criteria below:

  ### [ID]: [Requirement title]

  **Given** [precondition]
  **When** [action]
  **Then** [expected result]

  **Alternate flows:**
  - ...

  **Edge cases:**
  - ...
-->

---

## 4. Non-functional requirements

<!--
  Quality attributes that constrain the solution.
-->

| ID | Category | Requirement | Measurement |
|----|----------|-------------|-------------|
| | Performance | | |
| | Security | | |
| | Scalability | | |
| | Accessibility | | |
| | Availability | | |

---

## 5. Data requirements

<!--
  Entities, attributes, and relationships relevant to this feature.
  For complex data models, reference a separate data model document.
-->

| Entity | Key Attributes | Relationships | Notes |
|--------|---------------|---------------|-------|
| | | | |
| | | | |

---

## 6. Interface requirements

<!--
  Integration points with external systems or other features.
-->

| Interface | Direction | Protocol | Data Exchanged | Notes |
|-----------|-----------|----------|----------------|-------|
| | Inbound / Outbound / Bidirectional | | | |
| | Inbound / Outbound / Bidirectional | | | |

---

## 7. Business rules

<!--
  Decision logic, validation rules, constraints that govern behavior.
-->

| # | Rule | Condition | Action | Source |
|---|------|-----------|--------|--------|
| 1 | | | | |
| 2 | | | | |

---

## 8. Transition requirements

<!--
  Temporary capabilities needed for migration, rollout, or data conversion.
  These are removed after the transition is complete.
-->

| ID | Requirement | Needed Until |
|----|-------------|--------------|
| | | |
| | | |

---

## 9. Traceability

<!--
  Link requirements to business objectives, design elements, and tests.
  See blueprints/ba/knowledge-areas/requirements-lifecycle.md §1.1.
-->

| Requirement ID | Business Objective | Design Element | Test Case |
|----------------|--------------------|----------------|-----------|
| | | | |
| | | | |

---

## 10. Open questions

| # | Question | Owner | Status | Resolution |
|---|----------|-------|--------|------------|
| 1 | | | Open / Resolved | |
| 2 | | | Open / Resolved | |

---

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Product Owner | | Approved / Rejected | |
| Tech Lead | | Approved / Rejected | |
| BA Lead | | Approved / Rejected | |

---

*Last updated: YYYY-MM-DD · Owner: [name/role]*
