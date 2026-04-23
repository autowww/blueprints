---
name: start-versona-session
description: >
  Open a canonical Versona session folder under forge-logs/versona (or alias): SESSION.md,
  optional manifest, inputs/outputs/diagrams layout per blueprint contracts.
---

# Start Versona session (Forge)

## When to use

- User wants **auditability**, **handoffs**, or **artifact manifests** for a Versona run.
- Starting any **multi-step** or **enriched** pass (not a one-line chat reply).

## Steps

1. **Choose actor and session id** — Opaque `<actor>` label; `<session-id>` = ISO-ish timestamp + slug or UUID (no spaces). See [`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §7.2–7.3.
2. **Create tree** — Prefer `forge-logs/versona/<actor>/<session-id>/` with `inputs/`, `outputs/`, optional `diagrams/`. Alias: `forge/versona-sessions/...` with the **same inner layout** (document in repo README).
3. **SESSION.md** — From [`versona-session.template.md`](../../versona-session.template.md); set frontmatter: `session_id`, `started_at`, `work_item_refs` (recommended), `work_item_kind` (recommended).
4. **Optional manifest** — `session.manifest.yaml` or `.json` per [`session-manifest.schema.json`](../../../../methodologies/forge/schemas/session-manifest.schema.json).
5. **Optional shell** — `blueprints/sdlc/methodologies/forge/scripts/forge-versona-session.sh` from repo root.

## Rules

- Do **not** store secrets in `inputs/` committed paths; use gitignore policy per framework §7.5.
- Link **intake** to `forge-logs/versona-track/` if the team uses a request ledger ([`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) §3.1).

## Install

Copy to **`.cursor/skills/start-versona-session/`**.

## References

- [`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) §3.2
- Tasklet: **`@forge-tasklet-bootstrap-session`** (after install)
