# Versona catalog

**Purpose:** Entry point for **`versona/catalog/`** — all `versona-*.mdc.template` files except [`versona-generic.mdc.template`](../versona-generic.mdc.template) at the `versona/` root.

| Document | Role |
|----------|------|
| [`ANCESTRY.md`](ANCESTRY.md) | Kind/domain taxonomy and links to each template |
| [`TEMPLATE-INDEX.md`](TEMPLATE-INDEX.md) | Authoritative source path and checks per template |

**Hub:** [Versonas README](../README.md) — documentation map (Diátaxis-style), ASCII source tree, adoption steps.

**Install into Cursor:** from the consuming repo, [`../../setup/sync-forge-cursor-rules.sh`](../../setup/sync-forge-cursor-rules.sh) `sync --preset recommended` (driven by `forge.config.yaml`); drift / status: same script `diff` / `status`. Quick ref: [`../../setup/CURSOR-RULES-QUICKSTART.md`](../../setup/CURSOR-RULES-QUICKSTART.md). Logic: [`../../setup/versona_cursor_rules.py`](../../setup/versona_cursor_rules.py).
