# BA handbook maintenance

This folder is reserved for a future **HTML handbook** for the BA blueprint, following the same pattern as [`blueprints/sdlc/docs/`](../../../../sdlc/docs/MAINTENANCE.md) and [`blueprints/pdlc/docs/`](../../../../pdlc/docs/MAINTENANCE.md).

## When to create the handbook

Generate HTML when:

1. The Markdown sources in `blueprints/ba/` are stable enough to warrant a rendered version.
2. The team needs an offline-friendly or browser-friendly reading experience.

## Source files

All content is authored in Markdown under `blueprints/ba/`. The handbook would render:

| Source | Handbook Chapter |
|--------|------------------|
| `BABOK.md` | Overview, knowledge areas, competencies |
| `BA-SDLC-PDLC-BRIDGE.md` | Bridge document |
| `knowledge-areas/*.md` | One chapter per knowledge area |
| `techniques/README.md` | Technique catalog |
| `perspectives/*.md` | One chapter per perspective |

## Build

No build script exists yet. When created, follow the pattern in `blueprints/sdlc/docs/build_methodology_chapters.py`.
