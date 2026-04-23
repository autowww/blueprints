---
name: resolve-versona-standards
description: >
  Apply Forge standards precedence (L1–L6) for a Versona pass: registry, matrix row,
  and conflict surfacing before or during §5 output. Use instead of pasting long policy text in rules.
---

# Resolve Versona standards (Forge)

## When to use

- Before or during a **discipline §5** pass when controls, contracts, or org baselines may apply.
- When the user asks **which layer wins** or **what to cite** in **Standards traceability**.

## Steps

1. **Identify scope** — Data class, customer contract, regulated environment, or “local craft only”?
2. **Load precedence** — Read [`precedence.md`](../../../../methodologies/forge/standards/precedence.md) (L1 external → L6 heuristics).
3. **Registry** — If the repo has `forge/standards-registry.yaml`, treat it as the **control index**; if missing, say so and proceed with L6 + Cursor Team Rules only.
4. **Matrix row** — Open [`VERSONA-STANDARDS-MATRIX.md`](../../../../methodologies/forge/standards/VERSONA-STANDARDS-MATRIX.md) for **this** Versona’s **standards profile** (what to consider first).
5. **Resolve** — For each material topic, state **winner** and **losers**; note **waivers** / tickets if lower-layer “wins” are overridden.
6. **Emit fields** — When producing §5, fill **`### Standards traceability`** per [`VERSONA-CONTRACT.md`](../../../../methodologies/forge/versona/VERSONA-CONTRACT.md) §5.1 (or mark **N/A** when out of scope).

## Output shape (minimal)

```markdown
## Standards resolution (Versona)

- **Scope:** …
- **Layers consulted:** L? …
- **Winners by topic:** …
- **Conflicts / waivers:** …
```

## Install

Copy to **`.cursor/skills/resolve-versona-standards/`** in the consuming repo.

## References

- [`VERSONA-SKILL-MATRIX.md`](../../../../methodologies/forge/versona/VERSONA-SKILL-MATRIX.md) — which Versonas run this pack often.
- [`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) — `forge/waivers/`, evidence paths.
