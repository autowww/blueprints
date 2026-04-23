---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Daily operations

Templates and Cursor rule for the daily Forge workflow: Charge management, Ember Log maintenance, and day journaling.

The **daily sync** ceremony (**C3** — sync progress) confirms the Charge and surfaces blockers; see [§3 Daily sync (Charge confirmation)](../ceremonies-prescriptive.md#3-daily-sync-charge-confirmation) in the prescriptive ceremonies package.

## How the three artifacts work together

| Artifact | Purpose | Cadence | Location (consuming repo) |
|----------|---------|---------|---------------------------|
| **Charge** | Today's selected Sparks — the daily working set | Updated each morning at daily sync | `forge/charge.md` |
| **Ember Log** | Decision memory — why, not what | Updated at decision points throughout the day | `ember-logs/YYYY-MM-DD.md` |
| **Day journal** | Activity record — what hat was worn, what was done, what was learned | End of day | `forge/journal/YYYY-MM-DD.md` |

Full **artifact** layout (specs, ADRs, evidence packs, Versona sessions): [`../versona/ARTIFACT-CONTRACTS.md`](../versona/ARTIFACT-CONTRACTS.md).

Optional **enriched** Versona tracking (request ledger, JSON manifests, graph append-only logs) **extends** this trio; it does not replace Ember Log or the journal. See [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md).

## Templates

| Template | Purpose |
|----------|---------|
| [`charge.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/daily/charge.template.md) | Daily Charge file structure |
| [`ember-log-entry.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/daily/ember-log-entry.template.md) | Single Ember Log entry structure |
| [`day-journal.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/daily/day-journal.template.md) | Day journal entry structure |

## Request classification (intake)

Before opening a **Versona** session or editing **Charge**, teams can run a single **classifier + router** prompt: [`../../templates/forge/forge-request-classifier-intake.prompt.md`](../../templates/forge/forge-request-classifier-intake.prompt.md) — classifies work as Ore / Product Spark / Ingot / Forge Spark / defect / spike; proposes Markdown file updates, IDs, Versona order, and a **canonicalization** action (markdown-canonical profile). For **meta-requests**, follow with [`../../templates/forge/forge-meta-request-decomposition.prompt.md`](../../templates/forge/forge-meta-request-decomposition.prompt.md) to refresh **ROADMAP**, **WBS**, and **TRACEABILITY**. For **direct execution**, follow with [`../../templates/forge/forge-direct-execution-sparks-charge.prompt.md`](../../templates/forge/forge-direct-execution-sparks-charge.prompt.md) to align **Forge Sparks** and **`forge/charge.md`**.

## Cursor rule

[`forge-daily.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/daily/forge-daily.mdc.template) — conversational task delivery agent. When activated:

- Shows the current Charge (today's Sparks).
- Suggests the next Spark based on priority, dependencies, and current hat.
- Helps transition between hats with explicit declaration.
- Prompts for Ember Log entries at decision points.
- At end of day, summarizes what was done and helps commit the journal.

## Scripts

Shell scripts for git-tracked daily operations live in [`../scripts/`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/scripts/README.md):

| Script | Purpose |
|--------|---------|
| `forge-charge.sh` | Create/update today's Charge; show status; mark Sparks done |
| `forge-ember.sh` | Append an Ember Log entry with optional YAML frontmatter |
| `forge-journal.sh` | Create today's journal entry; commit and push daily activity |
| `forge-versona-session.sh` | Create `forge-logs/versona/<actor>/<session-id>/` with `SESSION.md` (see [`../versona/VERSONA-FRAMEWORK.md`](../versona/VERSONA-FRAMEWORK.md) §7) |
| `forge-status.sh` | Show current Forge iteration status |
