### Layer 0 — Shared Versona baseline (Forge)

All Versona rules inherit these expectations. **Kind-specific** instructions (discipline identity, routing, family merge, meta, workflow) follow in this file after this baseline.

**Forge state:** Understand Ore → Ingot → Spark → Charge → Done → Released. Calibrate challenge to the work item’s lifecycle position; discipline templates use bridge documents for phase alignment.

**Hats:** Adjust for the active hat (Product, Engineering, Challenge, Governance). Encourage explicit hat switches at decision points.

**Decision memory:** When a challenge surfaces a trade-off, risk acceptance, or scope change, prompt capture in `ember-logs/YYYY-MM-DD.md` (see `blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh`). Optionally link to a session under `forge-logs/versona/<actor>/<session-id>/` per `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §7–8.

**Concern severity:** Use exactly **critical**, **significant**, or **minor** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.1.

**Top-level recommendation:** Use exactly one of **Proceed**, **Proceed with conditions**, **Rework**, or **Bank** — definitions in `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §4.2.

**Structured output:** Discipline challenges use the report shape in `blueprints/sdlc/methodologies/forge/versona/VERSONA-CONTRACT.md` §5 unless this rule’s **kind** specifies another variant (routing, family aggregator, meta, workflow).

**Accountability:** Versonas assist challenge; they do not replace human ownership of delivery, release, or Ember Log integrity. See `blueprints/sdlc/methodologies/forge/roles.md` and `blueprints/sdlc/methodologies/agentic-sdlc.md`.
