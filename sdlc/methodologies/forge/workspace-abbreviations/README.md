---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
nav_title: Workspace abbreviation term index
description: Per-term pages for Forge workspace abbreviations — repos, lifecycle, disciplines, and platform shorthand.
---

# Workspace abbreviations — maintainer README

| Path | Role |
|------|------|
| `catalog.yaml` | Source of truth for terms and bridges |
| `terms/*.md` | Generated per-term handbook pages |
| `bridges/*.md` | Generated collision guides |
| `../WORKSPACE-ABBREVIATIONS.md` | Generated hub index |

## Regenerate

```bash
python3 scripts/generate-workspace-abbreviations.py
./sync-workspace-abbreviations.sh
```

Then rebuild **forgesdlc** and **blueprints-website** per `auto-build-sites.mdc`.

Term count: **84** · Bridges: **8**
