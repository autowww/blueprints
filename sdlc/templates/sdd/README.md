---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SDD templates (Spec-driven development)

Blank specs for **ceremony intents** and **process slots** using the [SDD I/O schema](../../methodologies/spec-driven/SDD-IO-SCHEMA.md).

| File | Use |
|------|-----|
| [`CEREMONY-INTENT.template.md`](CEREMONY-INTENT.template.md) | C1–C6 or named team ritual: preconditions, inputs, outputs, examples |
| [`PROCESS-SLOT.template.md`](PROCESS-SLOT.template.md) | Gate, phase transition, release slice, or toolchain step |

**Copy** into your repo (e.g. `docs/process/sdd/` or next to a story) and rename; fill every **Example** column before marking `status: active`.

**Handbook (generated):** CI runs `blueprints/generator/build-handbook.py`; SDD chapters are emitted under `blueprints/website/` (for example `sdlc--methodologies-spec-driven-sdd-io-schema.html`, `sdlc--methodologies-spec-driven-ceremonies-sdd.html`, `sdlc--methodologies-spec-driven-process-slots-sdd.html`). See [Maintaining the documentation (repo-wide)](https://github.com/autowww/blueprints/blob/main/docs/MAINTENANCE.md).
