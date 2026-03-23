# Maintaining agents blueprint docs

## Source of truth

| Canonical (edit first) | Published handbook |
|------------------------|--------------------|
| [`../STRUCTURE.md`](../STRUCTURE.md), [`../ORCHESTRATION.md`](../ORCHESTRATION.md), [`../README.md`](../README.md), [`../docker/README.md`](../docker/README.md) | Generated HTML under **`blueprints/website/`** (e.g. `agents--*.html`) via **`python3 generator/build-handbook.py agents`** run from **`blueprints/`**, or CI |

Do **not** hand-edit HTML under `website/`; change Markdown in **`blueprints/agents/`** and rebuild.

## Relationship to `blueprints/docs/MAINTENANCE.md`

Cross-area handbook build steps, `website/` layout, and CI deployment are documented in **[`../../docs/MAINTENANCE.md`](../../docs/MAINTENANCE.md)**.

---

*Maintainers only — not frozen blueprint process text.*
