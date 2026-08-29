# Forge environment lifecycle

Methodology for governed N-environment deployment on Granite.

## Principles

1. **Environment record** — Fleet persists `{app_id}--{env_id}`; compose `.env` is rendered from templates.
2. **Fleet-only orchestration** — lmeta flows use HTTP atoms (`curl_get`, `curl_request`) against Fleet APIs; no shell/SSH atoms.
3. **Generic health envelope** — same `status` + `summary` for every product; `checks[]` is product-defined.
4. **Multi-pipeline per product** — `forge/pipelines/<id>.yaml` plus legacy `forge/delivery-pipeline.yaml` as `default`.

## Phases

| Phase | Outcome |
|-------|---------|
| Learnings | Regression tests for bootstrap lock, import gate, Postgres DDL once |
| Fleet N-env | Parameterized rollout, ports, volumes, gateways |
| Health contract | Honest `/health` with environment identity |
| lmeta | Reusable env lifecycle units + Lenses consumer hooks |
| Lenses | Pipeline discovery, health aggregation, Studio remediation |

## Verification

Soak gateway health after rollout; prove Postgres isolation between environments before promoting artifacts.
