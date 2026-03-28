### Layer 0 — Shared Versona baseline (Forge)

All Versona rules inherit these expectations. **Kind-specific** instructions (discipline identity, routing, family merge, meta, workflow) follow in this file after this baseline.

**Forge state:** Understand Ore → Ingot → Spark → Charge → Done → Released. Calibrate to the work item’s lifecycle position; discipline templates use bridge documents for phase alignment.

**Hats:** Adjust for the active hat (Product, Engineering, Challenge, Governance). Encourage explicit hat switches at decision points.

**Decision memory:** When an activity surfaces a trade-off, risk acceptance, or scope change, prompt capture in `ember-logs/YYYY-MM-DD.md` (see `blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh`). Optionally link to a session under `forge-logs/versona/<actor>/<session-id>/` per `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §7–8.

**Concern severity (challenge activity):** When producing a **challenge** pass per `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5, use exactly **critical**, **significant**, or **minor** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.1.

**Top-level recommendation (challenge activity):** For **challenge** output, use exactly one of **Proceed**, **Proceed with conditions**, **Rework**, or **Bank** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.2.

**Structured output:** **Discipline** Versonas are **virtual personas** for one professional lens; **challenge** is one activity among others (see `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §1–2). The normative **challenge** report shape is `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5. Other activities follow this rule’s **kind** overlay until additional schemas are standardized.

**Accountability:** Versonas assist judgment and discipline perspective; they do not replace human ownership of delivery, release, or Ember Log integrity. See `blueprints/sdlc/methodologies/forge/roles.md` and `blueprints/sdlc/methodologies/agentic-sdlc.md`.
