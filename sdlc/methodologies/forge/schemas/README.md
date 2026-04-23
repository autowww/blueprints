---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge Versona — JSON Schemas (optional contracts)

JSON Schema files for **machine-readable** Versona artifacts. **Normative prose** for **where artifacts live** and **allowed formats**: [`../versona/ARTIFACT-CONTRACTS.md`](../versona/ARTIFACT-CONTRACTS.md). Sessions and logging detail: [`../versona/VERSONA-FRAMEWORK.md`](../versona/VERSONA-FRAMEWORK.md) and [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md).

| Schema | Purpose |
|--------|---------|
| [`request-ledger-entry.schema.json`](request-ledger-entry.schema.json) | One line in `forge-logs/versona-track/request-ledger.jsonl` |
| [`session-manifest.schema.json`](session-manifest.schema.json) | `session.manifest.json` beside `SESSION.md` |
| [`routing-decision.schema.json`](routing-decision.schema.json) | `outputs/routing-decision.json` |
| [`handoff-payload.schema.json`](handoff-payload.schema.json) | `outputs/handoff.json` |
| [`artifact-manifest.schema.json`](artifact-manifest.schema.json) | `outputs/artifact-manifest.json` |
| [`graph-analytics-record.schema.json`](graph-analytics-record.schema.json) | One line in `forge-logs/versona-track/graph-analytics.jsonl` |

**Draft:** JSON Schema version **2020-12**. `$id` values use the placeholder URI `https://blueprints.forgesdlc.com/schema/forge/…` for stable referencing; validators may load files from disk instead.
