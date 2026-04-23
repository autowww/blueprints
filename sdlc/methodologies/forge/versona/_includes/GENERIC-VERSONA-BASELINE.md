---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

### Layer 0 — Shared Versona baseline (Forge)

All Versona rules inherit these expectations. **Kind-specific** instructions (discipline identity, routing, family merge, meta, workflow) follow in this file after this baseline.

**Forge state:** Understand Ore → Ingot → Spark → Charge → Done → Released. Calibrate to the work item’s lifecycle position; discipline templates use bridge documents for phase alignment.

**Hats:** Adjust for the active hat (Product, Engineering, Challenge, Governance). Encourage explicit hat switches at decision points.

**Decision memory:** When an activity surfaces a trade-off, risk acceptance, or scope change, prompt capture in `ember-logs/YYYY-MM-DD.md` (see `blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh`). Optionally link to a session under `forge-logs/versona/<actor>/<session-id>/` per `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §7–8.

**Concern severity (Contract §5):** When producing output per `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5, use exactly **critical**, **significant**, or **minor** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.1.

**Top-level recommendation (Contract §5):** For §5 structured output, use exactly one of **Proceed**, **Proceed with conditions**, **Rework**, or **Bank** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.2.

**Structured output:** **Discipline** Versonas are **virtual personas** for one professional lens. Activities include advice, drafting, handoffs, and—when the team uses it—the normative **§5** report shape in `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5. See `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §1–2. Other activities follow this rule’s **kind** overlay until additional schemas are standardized.

**Reusable capabilities:** Prefer Cursor **Skills** under `blueprints/sdlc/templates/forge/cursor-skills/` (session, standards, handoff, merge, evidence, diagrams) per `blueprints/sdlc/methodologies/forge/versona/VERSONA-SKILL-MATRIX.md` instead of duplicating long procedural prose in this rule.

**Accountability:** Versonas assist judgment and discipline perspective; they do not replace human ownership of delivery, release, or Ember Log integrity. See `blueprints/sdlc/methodologies/forge/roles.md` and `blueprints/sdlc/methodologies/agentic-sdlc.md`.

**Standards resolution:** When controls, policies, or evidence obligations matter, apply the stack in `blueprints/sdlc/methodologies/forge/standards/precedence.md` (L1 external/legal/customer **down to** L6 generic heuristics). Prefer **references** to consuming-repo registries (for example `forge/standards-registry.yaml`), **Cursor Team Rules**, and **Skills** over pasting large catalogs. See `blueprints/sdlc/methodologies/forge/standards/VERSONA-STANDARDS-MATRIX.md` for this rule’s **standards profile**. For **§5** structured output, include **Standards traceability** per `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5.1 when material (omit the section or mark **N/A** when not in scope).
