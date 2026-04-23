---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Standards conflict scenarios (worked examples)

Illustrative **§5 Standards traceability** outcomes. Control IDs are fictional; map to your [`registry.example.yaml`](registry.example.yaml) shape.

---

## 1. Security — customer control vs fast iteration (L1 beats L6)

**Situation:** A Spark proposes copying a **production** database snapshot to a developer laptop for debugging. **Discipline heuristic (L6)** says “developers need realistic data.” **Customer DPA (L1)** forbids production PII outside production.

| Field | Example content |
|-------|-----------------|
| **standards_considered** | L1 `CUST-ACME-DPA-7`; L5 secure engineering practice (realistic test data); L6 informal team habit |
| **standards_applied** | **L1 wins** — no production PII in non-prod |
| **conflicts_detected** | L6 habit vs L1 contractual control |
| **waivers_required** | `none` (waivers cannot waive statute/DPA without legal path; use masking/subset instead) |
| **evidence_obligations** | Synthetic data pipeline or masked export; ticket link showing data-class compliance; optional Compliance Versona pass on Ingot |

**Top-level recommendation:** **Rework** or **Proceed with conditions** (conditions: approved synthetic data only).

---

## 2. Compliance — regulation vs repo convenience (L1 beats L3)

**Situation:** Team wants **one** shared S3 bucket for all environments to cut cost ( **L3** local convenience). **Regulatory mapping (L1)** requires logical separation and access logging per environment for audit.

| Field | Example content |
|-------|-----------------|
| **standards_considered** | L1 sector retention/access rules; L3 proposed bucket consolidation ADR draft |
| **standards_applied** | **L1** — separate buckets or equivalent controls with demonstrable separation |
| **conflicts_detected** | L3 cost/convenience vs L1 separation of environments |
| **waivers_required** | If org legal accepts compensating controls: file waiver with **compensating_controls**; else `none` and change design |
| **evidence_obligations** | Architecture diagram; logging/retention config references; Assay Gate checklist |

**Handoff:** **Architecture** + **DevOps** Versonas to implement L1-compliant design.

---

## 3. Product — roadmap pressure vs Assay evidence (L4 beats L6)

**Situation:** Product wants to **ship** a Spark on Friday (**L6** urgency). **Forge Assay pattern (L4)** says verify Sparks lack open **significant** concerns without mitigation. **No L1/L2** conflict.

| Field | Example content |
|-------|-----------------|
| **standards_considered** | L4 Assay Gate / evidence; L5 PM discipline (market timing) |
| **standards_applied** | **L4** — do not bypass evidence for “just this once” without Ember Log risk acceptance |
| **conflicts_detected** | L6 schedule pressure vs L4 methodology |
| **waivers_required** | If shipping with accepted risk: Ember Log + optional `waivers_required` pointing to governance approval; else `none` and defer |
| **evidence_obligations** | Minimal agreed test/evidence for the Spark type; PM articulates trade-off in Ember Log |

**Top-level recommendation:** **Proceed with conditions** (explicit evidence + logged trade-off) or **Bank** until evidence exists.

---

## 4. Engineering — OWASP-style practice vs org crypto standard (L2 beats L5)

**Situation:** **Software Engineering Versona (L5)** suggests a common JWT-in-localStorage pattern for speed. **Org crypto baseline (L2)** mandates **httpOnly** cookies for session tokens on customer-facing apps.

| Field | Example content |
|-------|-----------------|
| **standards_considered** | L2 `ORG-SEC-014`-class transport/session rules; L5 common SPA patterns |
| **standards_applied** | **L2** — session storage mechanism must meet org standard |
| **conflicts_detected** | L5 convenience pattern vs L2 mandated control |
| **waivers_required** | `none` unless Architecture files exception via GRC |
| **evidence_obligations** | Code review note; Security Versona spot-check; link to org standard in PR |

**Top-level recommendation:** **Rework** implementation approach or **Proceed with conditions** (if prototype is throwaway and **not** customer-facing — state boundary clearly).

---

## Summary

- **L1–L2** almost always **defeat** L4–L6 when they collide on the same requirement.
- **L4** Forge beats **L6** ad-hoc urgency for **evidence and ceremony** expectations.
- **Waiver** records document **approved** deviation from a **specific** `control_id`; they do not “cancel” law.

See [`../precedence.md`](../precedence.md) for the full stack.
