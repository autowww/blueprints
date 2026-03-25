# Phased delivery — major processes & flow maps

## 1. Classic stage sequence (simplified)

```ks-diagram
key: linear
alt: Diagram
```

Overlap stages where policy allows; **gates** sit on arrows.

## 2. Gate decision

```ks-diagram
key: decision
alt: Diagram
```

## 3. Change control path (scope)

```ks-diagram
key: linear
alt: Diagram
```

## 4. Traceability thread

```ks-diagram
key: linear
alt: Diagram
```

## 5. Phases A–F (typical mapping)

| Blueprint phase | Typical phased locus |
|-----------------|----------------------|
| A Shape | Initiate; charter; high-level requirements |
| B Plan | Planning; WBS; schedule baseline |
| C Build | Design and implementation per baseline |
| D Verify | Test phases; inspections; exit evidence |
| E Release | UAT; deployment; handover |
| F Learn | Operate; warranty; benefits realization |

## 6. Flow details (walkthrough)

**Stage sequence** — The linear diagram is pedagogical; real programs may overlap stages where policy allows. Gates sit on transitions; each stage produces baselines the next consumes. Map org stage names to blueprint A–F for one language across RAID, audits, and agents.

**Gate decision** — Gate packs prove exit criteria (quality, risk, readiness). Failed criteria mean hold and corrective actions, not silent waivers. Sponsor or steering approval commits spend and the next baseline; defer, kill, or replan are valid.

**Change control** — Change requests and impact analysis (schedule, cost, risk, traceability) feed steering decisions: re-baseline with versioned artifacts, or reject/queue. Ad-hoc scope without this path breaks audit trails.

**Traceability** — Requirement ID → design → test case → release note supports impact analysis and demonstrates coverage to auditors.

## 7. Authoritative sources & further reading

- [ISO/IEC/IEEE 12207 (catalogue)](https://www.iso.org/standard/63712.html) — International software life-cycle processes (full text licensed).
- [Wikipedia — Project Management Body of Knowledge (PMBOK)](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) — Overview of knowledge areas and process groups.
- [Wikipedia — Waterfall model](https://en.wikipedia.org/wiki/Waterfall_model) — Informal sequential-lifecycle context (not normative for your SDLC).
- [Wikipedia — Agile software development](https://en.wikipedia.org/wiki/Agile_software_development) — Contrast with iterative approaches when blending gates and iterations.

[PMI — Standards & guides](https://www.pmi.org/standards) is listed in [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md) for practitioner depth (some networks block automated fetches to `pmi.org`).

## 8. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodologies-phased-delivery.html)
