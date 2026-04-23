---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Standards precedence — which controls win

Normative **stack** for resolving conflicts between policies, methodologies, and informal guidance. **Higher rows beat lower rows** when two sources disagree on the same decision or evidence obligation.

| Rank | Layer | Typical sources | Examples |
|------|--------|-----------------|----------|
| **1** | **External compliance / legal / customer contractual controls** | Statute, regulator guidance, DPA, BAA, customer security addendum, court order | GDPR lawful basis; HIPAA BA requirements; customer mandate “no production data in dev” |
| **2** | **Org-wide mandated controls** | Enterprise security baselines, GRC tool profiles, company-wide policies, mandatory training rules | Org SSO only; approved regions; mandatory DLP |
| **3** | **Repository / product / architecture local controls** | Root `AGENTS.md`, repo ADRs, threat models, `.cursor/rules` **Team Rules**, product-specific non-functional standards | “This service must be zero-trust”; repo lint/CI policy |
| **4** | **Forge SDLC methodology** (this blueprint) | `blueprints/sdlc/methodologies/forge/`, ceremonies, Assay Gate pattern, Versona contract | Spark sizing; Ember Log at decisions; §5 severity labels |
| **5** | **Discipline best practices** | `blueprints/disciplines/<domain>/`, OWASP, WCAG as *practice* (until L1–L3 elevate them) | Secure design patterns; testing pyramids |
| **6** | **Generic assistant heuristics** | Model defaults, undocumented team habit, ad-hoc prompt style | “Usually we use feature flags” without a written standard |

## Resolution rules

1. **Same layer tie-break** — If two sources at **the same rank** conflict, **stop** and escalate to the **lowest hat** that owns that layer (often Governance for L1–L2, Engineering + Architecture for L3, Product for product NFRs). Document the decision in the **Ember Log** and, when using enriched sessions, optional **waivers** (see [`examples/waiver.example.yaml`](examples/waiver.example.yaml)).
2. **Higher layer silent** — If a higher layer does not mention a topic, lower layers **may** fill the gap (e.g. L5 discipline guidance applies until L1–L3 explicitly override).
3. **Evidence follows winners** — **Evidence obligations** attach to the **winning** control. If L1 requires a retention proof, that obligation survives even when L4 Forge text is silent.
4. **Methodology does not claim legal authority** — Forge and Versonas **interpret** and **trace** standards; they do **not** replace counsel or your GRC function for L1.

## Enforcement surfaces (consuming repo)

| Surface | Role |
|---------|------|
| **Cursor Team Rules** (org or enterprise) | Ideal for **L1–L2** “always on” constraints and links to canonical policy URLs |
| **`forge/standards-registry.yaml`** (or path in [`schemas/standards-registry.schema.json`](schemas/standards-registry.schema.json)) | Machine-readable **profiles** and **control IDs** the repo actually adopts |
| **`AGENTS.md`** | **L3** defaults and pointers to registry + Team Rules |
| **Skills** | Short **workflows** (e.g. “how we run a DPIA-lite”) without duplicating ISO clauses |
| **Versona §5 Standards traceability** | Per [`../versona/VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) §5.1 — auditable record of what was considered and what won |

## Related

- [`README.md`](README.md) — adoption overview
- [`VERSONA-STANDARDS-MATRIX.md`](VERSONA-STANDARDS-MATRIX.md) — per-Versona profiles
- [`examples/CONFLICT-SCENARIOS.md`](examples/CONFLICT-SCENARIOS.md) — worked examples
