# Daily operations

Templates and Cursor rule for the daily Forge workflow: Charge management, Ember Log maintenance, and day journaling.

## How the three artifacts work together

| Artifact | Purpose | Cadence | Location (consuming repo) |
|----------|---------|---------|---------------------------|
| **Charge** | Today's selected Sparks — the daily working set | Updated each morning at daily sync | `forge/charge.md` |
| **Ember Log** | Decision memory — why, not what | Updated at decision points throughout the day | `ember-logs/YYYY-MM-DD.md` |
| **Day journal** | Activity record — what hat was worn, what was done, what was learned | End of day | `forge/journal/YYYY-MM-DD.md` |

## Templates

| Template | Purpose |
|----------|---------|
| [`charge.template.md`](charge.template.md) | Daily Charge file structure |
| [`ember-log-entry.template.md`](ember-log-entry.template.md) | Single Ember Log entry structure |
| [`day-journal.template.md`](day-journal.template.md) | Day journal entry structure |

## Cursor rule

[`forge-daily.mdc.template`](forge-daily.mdc.template) — conversational task delivery agent. When activated:

- Shows the current Charge (today's Sparks).
- Suggests the next Spark based on priority, dependencies, and current hat.
- Helps transition between hats with explicit declaration.
- Prompts for Ember Log entries at decision points.
- At end of day, summarizes what was done and helps commit the journal.

## Scripts

Shell scripts for git-tracked daily operations live in [`../scripts/`](../scripts/README.md):

| Script | Purpose |
|--------|---------|
| `forge-charge.sh` | Create/update today's Charge; show status; mark Sparks done |
| `forge-ember.sh` | Append an Ember Log entry with optional YAML frontmatter |
| `forge-journal.sh` | Create today's journal entry; commit and push daily activity |
| `forge-status.sh` | Show current Forge iteration status |
