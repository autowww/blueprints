---
name: close-versona-session
description: >
  Close a Versona session: finalize SESSION.md, optional manifest version, handoff pointers,
  and journal cross-links — short checklist for any discipline.
---

# Close Versona session (Forge)

## When to use

- **End** of a bounded session (before switching actor, archiving, or opening a follow-up session).

## Steps

1. **Outputs present** — §5 file (if used), `handoff.json` (if any), tasklet outputs merged or linked.
2. **SESSION.md** — Add **Closed** subsection: `ended_at` (ISO), **summary** line, **links** to Ember Log entries if decisions were taken.
3. **Manifest** — Set `versona_session_schema_version` if the team versions shapes ([`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §7.4).
4. **Journal** — Optional one-liner in `forge/journal/YYYY-MM-DD.md` pointing at session folder.
5. **Git** — If policy is **gitignored** sessions, ensure **Ember Log** still captures decisions ([`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §7.5).

## Checklist (paste in SESSION.md)

```markdown
## Session close

- [ ] Outputs linked
- [ ] Handoff / next steps noted
- [ ] Decisions in Ember Log (if any)
- [ ] ended_at: …
```

## Install

Copy to **`.cursor/skills/close-versona-session/`**.

## References

- [`start-versona-session`](../start-versona-session/SKILL.md)
- [`build-versona-handoff`](../build-versona-handoff/SKILL.md)
