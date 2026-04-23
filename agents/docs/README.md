# Agents blueprint — handbook maintenance

- **Canonical Markdown:** [`../STRUCTURE.md`](../STRUCTURE.md), [`../README.md`](../README.md), [`../ORCHESTRATION.md`](../ORCHESTRATION.md) · **Versona + execution tasklets:** [`VERSONA-EXECUTION-TASKLETS.md`](VERSONA-EXECUTION-TASKLETS.md).  
- **Published HTML:** not stored under this `docs/` folder. CI runs **`blueprints/generator/build-handbook.py`**, which writes a flat static site under **`blueprints/website/`** (pages such as `agents--index.html`).  
- **Maintainers:** [`MAINTENANCE.md`](MAINTENANCE.md) · repo-wide handbook build: [Maintaining the documentation (repo-wide)](https://github.com/autowww/blueprints/blob/main/docs/MAINTENANCE.md).

This `docs/` folder is part of the reusable **`blueprints/agents/`** package. If you copy **only** `blueprints/agents/` without the rest of `blueprints/`, use the Markdown files above as the main entry points.
