#!/usr/bin/env python3
"""
Generate full handbook HTML for methodology subchapters (Foundation / Ceremonies / Process
for Scrum, Kanban, Phased, XP). Same layout pattern as methodologies-scrum-roles.html.

Run from this directory:
  python3 build_methodology_chapters.py

Does not overwrite methodologies-scrum-roles.html (hand-maintained).
"""
from __future__ import annotations

import html
from pathlib import Path

OUT = Path(__file__).resolve().parent

MERMAID_SCRIPT = """
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
  </script>
"""

SKIP = frozenset({"methodologies-scrum-roles.html"})


def e(s: str) -> str:
    return html.escape(s, quote=False)


def b(s: str) -> str:
    return f'<strong class="text-body">{e(s)}</strong>'


def table(headers: list[str], rows: list[list[str]], striped: bool = True) -> str:
    cls = "table table-sm table-bordered mb-0"
    if striped:
        cls += " table-striped"
    th = "".join(f"<th scope='col'>{h}</th>" for h in headers)
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return (
        f'<div class="doc-table-wrap mt-2"><table class="{cls}">'
        f'<thead class="table-light"><tr>{th}</tr></thead>'
        f'<tbody class="small text-body-secondary">{body}</tbody></table></div>'
    )


def section(sid: str, title: str, inner: str, *, first: bool = False) -> str:
    top = "mb-4" if first else "mb-4 pt-3 border-top"
    return f'<section class="{top}" id="{e(sid)}"><h2 class="font-display h5 fw-semibold">{e(title)}</h2>{inner}</section>'


def mermaid_block(diagram: str) -> str:
    # diagram: raw mermaid source (no HTML in nodes)
    esc_d = (
        diagram.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    return (
        '<div class="border rounded-3 bg-white p-3 shadow-sm my-3">'
        f'<div class="mermaid small">{esc_d}</div></div>'
    )


def diagrams_section(title: str, sid: str, diagrams: list[str]) -> str:
    inner = "".join(mermaid_block(d) for d in diagrams)
    inner = f'<p class="text-body-secondary small mb-2">Rendered when JavaScript runs. Same diagrams in canonical Markdown.</p>{inner}'
    return section(sid, title, inner, first=False)


def flow_details_section(sid: str, items: list[tuple[str, str]]) -> str:
    """(subsection title, plain-text paragraph) — narrative for each process diagram."""
    chunks: list[str] = []
    for idx, (title, para) in enumerate(items):
        mt = "mt-1" if idx == 0 else "mt-3"
        chunks.append(
            f'<h3 class="font-display h6 fw-semibold text-body {mt} mb-2">{e(title)}</h3>'
            f'<p class="text-body-secondary small mb-0">{e(para)}</p>'
        )
    inner = "".join(chunks)
    return section(
        sid,
        "Flow details (walkthrough)",
        inner,
        first=False,
    )


def external_sources_section(sid: str, items: list[tuple[str, str, str]]) -> str:
    """(url, link label, executive summary plain text)."""
    lis: list[str] = []
    for i, (url, label, summary) in enumerate(items):
        mb = "mb-2" if i < len(items) - 1 else "mb-0"
        lis.append(
            f'<li class="{mb}"><a href="{e(url)}" class="link-success" rel="noopener">{e(label)}</a>'
            f'<span class="doc-external-summary">{e(summary)}</span></li>'
        )
    ref_note = (
        '<p class="small text-body-secondary mb-0 mt-3">'
        'Full curated list with matching blurbs: '
        f'<a href="{e("../methodologies/REFERENCE-LINKS.md")}" class="link-success">'
        f'<code>{e("REFERENCE-LINKS.md")}</code></a> (repository path).</p>'
    )
    inner = (
        '<ul class="list-unstyled small text-body-secondary mb-0">' + "".join(lis) + "</ul>"
        + ref_note
    )
    return section(sid, "Authoritative sources & further reading", inner, first=False)


def page_shell(
    *,
    browser_title: str,
    h1: str,
    intro: str,
    crumbs: list[tuple[str | None, str]],
    main_sections: str,
    toc: list[tuple[str, str]],
    prev_href: str,
    prev_label: str,
    next_href: str,
    next_label: str,
    canonical_md: str,
    mermaid: bool,
) -> str:
    trail = []
    for href, label in crumbs:
        if href is None:
            trail.append(
                f'<li class="breadcrumb-item active" aria-current="page">{e(label)}</li>'
            )
        else:
            trail.append(
                f'<li class="breadcrumb-item"><a href="{e(href)}">{e(label)}</a></li>'
            )
    breadcrumb = '<ol class="breadcrumb small mb-3">' + "".join(trail) + "</ol>"

    toc_links = "".join(
        f'<a class="nav-link fw-semibold py-1" href="#{e(sid)}">{e(lab)}</a>'
        for sid, lab in toc
    )

    extra = MERMAID_SCRIPT if mermaid else ""

    note = (
        f'<div class="alert alert-light border shadow-sm mt-4 py-3" role="note">'
        f'<p class="fw-semibold text-body mb-2">Canonical source</p>'
        f'<p class="small text-body-secondary mb-0">Edit <a href="{e(canonical_md)}" class="link-success"><code>{e(canonical_md.replace("../", ""))}</code></a> first; regenerate this page with <code>build_methodology_chapters.py</code>.</p></div>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SDLC blueprint — {browser_title}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@900&display=swap" rel="stylesheet" />
  <link href="https://fonts.cdnfonts.com/css/proxima-nova-2" rel="stylesheet" />
  <link rel="stylesheet" href="assets/docs-theme.css" />
</head>
<body class="bg-body-tertiary">
  <a href="#main" class="skip-link">Skip to content</a>
  <button type="button" class="btn btn-primary position-fixed top-0 start-0 m-3 d-lg-none shadow" style="z-index: 1040" data-bs-toggle="offcanvas" data-bs-target="#docNavOffcanvas" aria-controls="docNavOffcanvas" aria-label="Open navigation">
    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/></svg>
  </button>
  <div class="container-fluid px-0">
    <div class="row g-0 flex-lg-nowrap min-vh-100">
      <aside class="col-lg-3 col-xl-2 d-none d-lg-flex flex-column bg-dark text-white border-end p-0" style="min-height: 100vh">
        <div class="p-3 border-bottom border-secondary">
          <p class="fs-6 fw-semibold text-white mb-0">SDLC blueprint</p>
          <p class="small text-secondary mt-2 mb-0">Human handbook · Product-agnostic</p>
        </div>
        <nav class="nav-scroll flex-grow-1 px-2 py-3" id="doc-sidebar-nav" aria-label="Handbook chapters"></nav>
      </aside>
      <div class="offcanvas offcanvas-start text-bg-dark" tabindex="-1" id="docNavOffcanvas" aria-labelledby="docNavLabel">
        <div class="offcanvas-header border-bottom border-secondary">
          <h5 class="offcanvas-title fs-6 fw-semibold" id="docNavLabel">SDLC blueprint</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body p-0">
          <nav class="nav flex-column px-2 py-2 nav-scroll" id="doc-offcanvas-nav" aria-label="Handbook chapters mobile"></nav>
        </div>
      </div>
      <main id="main" class="doc-main col-lg-9 col-xl-10 px-3 px-md-4 pt-4 pt-lg-3 pb-4">
        <div class="mx-auto doc-content-wide px-lg-1">
          <header class="mb-3 pb-3 border-bottom">
            <nav aria-label="breadcrumb">{breadcrumb}</nav>
            <h1 class="font-display h2 fw-bold text-body mb-0">{h1}</h1>
            <p class="text-body-secondary small mt-2 mb-0">{intro}</p>
          </header>
          <div class="row g-3 g-lg-4">
            <div class="col-lg-8 col-xl-9 order-2 order-lg-1">
{main_sections}
            </div>
            <div class="col-lg-4 col-xl-3 order-1 order-lg-2">
              <nav class="doc-toc doc-toc-sticky border rounded bg-body shadow-sm" aria-label="On this page">
                <p class="doc-toc-title px-3 pt-3 mb-0">On this page</p>
                <div class="nav flex-column px-3 pb-3 small">
{toc_links}
                </div>
              </nav>
            </div>
          </div>
{note}
          <nav class="d-flex flex-wrap justify-content-between gap-2 mt-4 pt-3 border-top" aria-label="Chapter navigation">
            <a href="{e(prev_href)}" class="btn btn-outline-secondary btn-sm">{e(prev_label)}</a>
            <a href="{e(next_href)}" class="btn btn-outline-success btn-sm">{e(next_label)}</a>
          </nav>
          <footer class="mt-4 pt-3 border-top text-muted small">
            <p class="mb-1">Handbook last aligned with blueprint Markdown: <strong class="text-body">2026-03-20</strong>.</p>
            <p class="mb-0 text-secondary" style="font-size: 0.8rem">Styled with <a href="https://getbootstrap.com/docs/5.3/" class="link-success" rel="noopener">Bootstrap 5.3</a> (CDN).</p>
          </footer>
        </div>
      </main>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
  <script src="assets/docs-nav.js"></script>
  <script src="assets/docs-toc-scrollspy.js"></script>
{extra}
</body>
</html>
"""


# --- Scrum (foundation, ceremonies, process) ---


def scrum_foundation() -> str:
    s = []
    s.append(
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Scrum plugs into the shared <strong class="text-body">tracking spine</strong> and <strong class="text-body">ceremony intents C1–C6</strong>. It adds timeboxes, the three accountabilities, and Scrum commitments—not a replacement for traceability.</p>',
            first=True,
        )
    )
    s.append(
        section(
            "phases",
            "Phases A–F in Scrum",
            table(
                ["Phase", "Scrum expression", "Notes"],
                [
                    [
                        b("A — Shape"),
                        "Backlog ordering, stakeholder input",
                        "PO leads; Developers may join discovery",
                    ],
                    [
                        b("B — Plan"),
                        "Sprint Planning (what)",
                        "Select PBIs for Sprint Goal",
                    ],
                    [
                        b("C — Build"),
                        "Sprint execution, Daily Scrum",
                        "Scope changes only with PO if goal at risk",
                    ],
                    [
                        b("D — Verify"),
                        "Review + DoD",
                        "Integrated increment",
                    ],
                    [
                        b("E — Release"),
                        "Potentially shippable increment",
                        "Release cadence may differ from sprint",
                    ],
                    [
                        b("F — Operate & learn"),
                        "Retro; ops handoff if applicable",
                        "Improve process; feed backlog",
                    ],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0"><strong class="text-body">Rule:</strong> Each sprint touches <strong class="text-body">B–E</strong> at minimum. <strong class="text-body">A</strong> is continuous (refinement). <strong class="text-body">F</strong> every sprint.</p>',
        )
    )
    s.append(
        section(
            "tracking",
            "Tracking spine",
            table(
                ["Artifact", "Scrum mapping"],
                [
                    ["Intent / request", "PBI or epic"],
                    ["Spec", "Acceptance on item; ADR/spec link"],
                    ["Plan", "Sprint Backlog + Sprint Goal"],
                    ["Tasks", "Subtasks on PBIs"],
                    ["PRs", "Slices toward Done"],
                    ["Reviews", "Code review + DoD"],
                    ["Release", "Ship decision vs sprint end"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0">Do not let the board replace traceability—each shipped PBI links to spec and PRs.</p>',
        )
    )
    s.append(
        section(
            "intents",
            "Ceremony intents ↔ events",
            table(
                ["Intent", "Primary events", "Secondary"],
                [
                    [b("C1"), "Planning, refinement", "Stakeholder sessions"],
                    [b("C2"), "Planning part 2, refinement", "In-sprint breakdown"],
                    [b("C3"), "Daily Scrum", "Pairing, swarming"],
                    [b("C4"), "Review, DoD", "Code review, tests"],
                    [b("C5"), "Retrospective", "Improvement backlog"],
                    [b("C6"), "Review demo, refinement", "Docs, tech talks"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0">See <a href="methodologies-ceremonies.html" class="link-success">Ceremonies</a> · <a href="../methodologies/ceremonies/methodology-bridge.md" class="text-secondary">methodology-bridge.md</a></p>',
        )
    )
    s.append(
        section(
            "archetypes",
            "Role archetypes",
            table(
                ["Scrum role", "Archetype emphasis"],
                [
                    ["Product Owner", "Sponsor proxy, Orchestrator"],
                    ["Scrum Master", "Orchestrator, Quality advocate"],
                    ["Developers", "Implementer, Quality advocate (shared)"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0"><a href="methodologies-scrum-roles.html" class="link-success">Scrum — Roles</a> · <a href="../methodologies/roles-archetypes.md" class="text-secondary">roles-archetypes.md</a></p>',
        )
    )
    s.append(
        section(
            "adds",
            "What Scrum adds",
            '<ul class="text-body-secondary small mb-0"><li>Fixed-length Sprints</li><li>PO / SM / Developers</li><li>Commitments: Product Goal, Sprint Goal, DoD</li><li>Official events</li></ul>',
        )
    )
    s.append(
        section(
            "antipatterns",
            "Anti-patterns",
            table(
                ["Anti-pattern", "Fix"],
                [
                    ["SM as admin only", "SM protects Scrum theory; facilitates"],
                    ["PO sole story writer", "Developers in refinement"],
                    ["Skip retro when busy", "Retro is non-negotiable"],
                    ["No increment end of sprint", "Inspect DoD / slicing"],
                ],
            ),
        )
    )
    dm = """flowchart LR
  subgraph sp[Sprint]
    P[Planning] --> D[Daily loop]
    D --> V[Review]
    V --> RT[Retro]
  end
  R[Refinement] --> P
  RT --> R"""
    s.append(diagrams_section("Lifecycle diagram", "diagram", [dm]))
    main = "\n".join(s)
    return page_shell(
        browser_title="Scrum — Foundation &amp; fit",
        h1="Scrum — Foundation &amp; fit",
        intro='How Scrum maps to <strong class="text-body">phases A–F</strong>, the <strong class="text-body">tracking spine</strong>, and <strong class="text-body">C1–C6</strong>. Canonical: <a href="../methodologies/scrum/foundation-connection.md" class="link-success">foundation-connection.md</a> · <a href="../methodologies/scrum.md" class="link-success">scrum.md</a>.',
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-scrum.html", "Scrum"),
            (None, "Foundation"),
        ],
        main_sections=main,
        toc=[
            ("overview", "Overview"),
            ("phases", "Phases A–F"),
            ("tracking", "Tracking spine"),
            ("intents", "Intents ↔ events"),
            ("archetypes", "Archetypes"),
            ("adds", "What Scrum adds"),
            ("antipatterns", "Anti-patterns"),
            ("diagram", "Diagram"),
        ],
        prev_href="methodologies-scrum.html",
        prev_label="← Scrum",
        next_href="methodologies-scrum-roles.html",
        next_label="Roles →",
        canonical_md="../methodologies/scrum/foundation-connection.md",
        mermaid=True,
    )


def io_table(rows: list[tuple[str, str, str, str, str]]) -> str:
    """Intent, Inputs, Outputs, People, Timebox"""
    h = ["Intent", "Inputs", "Outputs", "Participants", "Timebox / cadence"]
    body_rows = [[e(a), e(b), e(c), e(d), e(t)] for a, b, c, d, t in rows]
    return table(h, body_rows)


def scrum_ceremonies() -> str:
    s = []
    s.append(
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Official Scrum events plus <strong class="text-body">refinement</strong> (essential in practice). Each block: intent, I/O, participants, timebox, agenda. Scale timeboxes down for shorter sprints (Scrum Guide). Canonical: <a href="../methodologies/scrum/ceremonies-prescriptive.md" class="link-success">ceremonies-prescriptive.md</a>.</p>',
            first=True,
        )
    )
    dm = """flowchart LR
  Ref[Refinement] --> SP[Sprint Planning]
  SP --> DS[Daily Scrum]
  DS --> SR[Sprint Review]
  SR --> Ret[Sprint Retrospective]
  Ret --> Ref"""
    s.append(diagrams_section("Event chain", "diagram-chain", [dm]))
    s.append(
        section(
            "refinement",
            "Product Backlog refinement",
            io_table(
                [
                    (
                        "C2 + C1",
                        "Product Goal, themes, estimates, risks",
                        "Ready ordered PBIs",
                        "PO R, Devs R, SM O",
                        "~10% capacity; 1–2×/wk slots",
                    )
                ]
            )
            + '<ol class="small text-body-secondary mb-2"><li>PO presents top (5–10 min)</li><li>Clarify acceptance (20–30 min)</li><li>Split/spike (15–20 min)</li><li>Re-order (5–10 min)</li></ol>'
            + '<p class="text-body-secondary small mb-0"><strong class="text-body">DoR example:</strong> value clear, AC testable, deps known, fits sprint horizon.</p>',
        )
    )
    s.append(
        section(
            "planning",
            "Sprint Planning",
            io_table(
                [
                    (
                        "C1 + C2",
                        "Backlog, increment, capacity, DoD",
                        "Sprint Goal, Sprint Backlog",
                        "PO, SM, Devs (all R)",
                        "≤8h / month sprint",
                    )
                ]
            )
            + '<p class="text-body-secondary small mb-0"><strong class="text-body">Part 1:</strong> why/what (PO). <strong class="text-body">Part 2:</strong> how (Devs)—tasks, risks, confidence.</p>',
        )
    )
    s.append(
        section(
            "daily",
            "Daily Scrum",
            io_table(
                [
                    (
                        "C3",
                        "Sprint Backlog, goal, blockers",
                        "24h plan, impediments visible",
                        "Devs R; SM O; PO —",
                        "15 min daily",
                    )
                ]
            )
            + '<p class="text-body-secondary small mb-0">Walk board right-to-left or classic three questions. Problem-solving after, not inside 15 min.</p>',
        )
    )
    s.append(
        section(
            "review",
            "Sprint Review",
            io_table(
                [
                    (
                        "C4 + C6",
                        "Done increment, backlog, metrics",
                        "Feedback, backlog updates",
                        "PO, SM, Devs, stakeholders",
                        "≤4h / month sprint",
                    )
                ]
            )
            + '<p class="text-body-secondary small mb-0">Demo working software; PO frames forecast vs done; discuss next.</p>',
        )
    )
    s.append(
        section(
            "retro",
            "Sprint Retrospective",
            io_table(
                [
                    (
                        "C5",
                        "Sprint data, mood, prior actions",
                        "1–3 improvement experiments",
                        "Whole team (PO default R)",
                        "≤3h / month sprint",
                    )
                ]
            )
            + '<p class="text-body-secondary small mb-0">Stages: set stage → data → insights → experiments → close.</p>',
        )
    )
    s.append(
        section(
            "sprint",
            "Sprint container",
            io_table(
                [
                    (
                        "B–E",
                        "Goal, backlog, DoD, environments",
                        "≤1 Done increment",
                        "Whole Scrum Team",
                        "Fixed length; no extension",
                    )
                ]
            )
            + '<p class="text-body-secondary small mb-0">Optional: mid-sprint risk check; pre-Review DoD walkthrough.</p>',
        )
    )
    s.append(
        section(
            "summary",
            "Quick I/O summary",
            table(
                ["Event", "Primary inputs", "Primary outputs"],
                [
                    ["Refinement", "Themes, PBIs", "Ready backlog"],
                    ["Planning", "Backlog, capacity", "Goal + Sprint Backlog"],
                    ["Daily", "Board", "Plan, impediments"],
                    ["Review", "Increment", "Feedback"],
                    ["Retro", "Experience", "Experiments"],
                ],
            ),
        )
    )
    main = "\n".join(s)
    return page_shell(
        browser_title="Scrum — Ceremonies",
        h1="Scrum — Ceremonies",
        intro='Prescriptive <strong class="text-body">inputs, outputs, participants, agendas</strong> for Scrum events.',
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-scrum.html", "Scrum"),
            (None, "Ceremonies"),
        ],
        main_sections=main,
        toc=[
            ("overview", "Overview"),
            ("diagram-chain", "Event chain"),
            ("refinement", "Refinement"),
            ("planning", "Planning"),
            ("daily", "Daily Scrum"),
            ("review", "Review"),
            ("retro", "Retro"),
            ("sprint", "Sprint"),
            ("summary", "I/O summary"),
        ],
        prev_href="methodologies-scrum-roles.html",
        prev_label="← Roles",
        next_href="methodologies-scrum-process.html",
        next_label="Process →",
        canonical_md="../methodologies/scrum/ceremonies-prescriptive.md",
        mermaid=True,
    )


def scrum_process() -> str:
    diagrams = [
        """flowchart LR
  subgraph refine[Ongoing refinement]
    R[Refinement]
  end
  subgraph sprint[Sprint]
    P[Sprint Planning]
    D[Daily Scrum loop]
    V[Sprint Review]
    RT[Sprint Retrospective]
  end
  R --> P
  P --> D
  D --> D
  D --> V
  V --> RT
  RT --> R""",
        """flowchart TD
  A[Product Backlog top items] --> B{Value clear and ordered?}
  B -->|No| C[Refinement / spike]
  C --> A
  B -->|Yes| D[Select PBIs for capacity]
  D --> E[Draft Sprint Goal]
  E --> F{Team confident?}
  F -->|No| G[Remove or swap items]
  G --> D
  F -->|Yes| H[Part 2: Sprint Backlog]
  H --> I[Sprint starts]""",
        """flowchart TD
  S[Start of day] --> M[Daily Scrum 15m]
  M --> W[Work toward Sprint Goal]
  W --> I{Impediment?}
  I -->|Yes| X[SM / team remove blocker]
  X --> W
  I -->|No| W
  W --> E[End of day: board updated]
  E --> S""",
        """flowchart TD
  C[Code complete] --> T[Tests pass]
  T --> R[Review / PR merged]
  R --> Doc[Docs / release notes]
  Doc --> Rel{DoD met?}
  Rel -->|Yes| Done[Done increment]
  Rel -->|No| Fix[Fix or descope]
  Fix --> C""",
        """flowchart LR
  Demo[Increment demo] --> FB[Feedback]
  FB --> PO[PO synthesizes]
  PO --> BL[Backlog updates]
  BL --> NS[Next Planning]""",
    ]
    flow_items = [
        (
            "Sprint lifecycle (refinement → events → retro)",
            "Refinement is not a single meeting: it keeps the top of the Product Backlog transparent enough that Sprint Planning can commit. "
            "Inside the Sprint, the Daily Scrum is a daily inspect-and-adapt loop toward the Sprint Goal. "
            "Sprint Review inspects the increment with stakeholders; Sprint Retrospective improves how the team works. "
            "Outputs from Review and Retro inform the next refinement and planning cycle—closing the empirical process loop.",
        ),
        (
            "Sprint Planning (Part 1 → Part 2)",
            "Part 1 establishes why this Sprint matters: the Product Owner presents ordered Product Backlog items; if value or ordering is unclear, the team returns to refinement or a timeboxed spike rather than guessing. "
            "The Developers select what fits capacity and craft one Sprint Goal. If the team lacks confidence, they remove or swap work until the forecast is credible. "
            "Part 2 decomposes selected items into a plan (often a Sprint Backlog); the Sprint starts once the team agrees how it will meet the goal.",
        ),
        (
            "Daily execution loop",
            "The Daily Scrum is a maximum 15-minute event for Developers to inspect progress toward the Sprint Goal and adapt the plan for the next day. "
            "Detailed problem-solving happens outside the timebox. Impediments are surfaced here but cleared by the Scrum Master and team through the day. "
            "The board or backlog should reflect reality by end of day so transparency holds for the next Daily Scrum.",
        ),
        (
            "Definition of Done (increment quality gate)",
            "An increment must meet the shared Definition of Done before work is called Done—otherwise transparency about releasable product is false. "
            "Typical checks include automated tests, review/merge policy, documentation, and release readiness where applicable. "
            "If DoD is not met, the team fixes quality issues or negotiates scope with the Product Owner rather than labeling incomplete work as Done.",
        ),
        (
            "Stakeholder feedback → backlog",
            "Sprint Review grounds discussion in a working increment; feedback is explicit input to the Product Backlog. "
            "The Product Owner synthesizes competing stakeholder views into ordering and clarity for the next Sprint. "
            "That backlog state is the primary input to the next Sprint Planning—so delivery stays empirically steered by real use and conversation.",
        ),
    ]
    ext = [
        (
            "https://scrumguides.org/scrum-guide.html",
            "The Scrum Guide",
            "Official Scrum definition—events, accountabilities, artifacts—normative reference for these flows.",
        ),
        (
            "https://www.scrum.org/resources/what-is-scrum",
            "Scrum.org — What is Scrum?",
            "Learning-oriented intro; complements the Guide with context and training paths.",
        ),
        (
            "https://www.agilealliance.org/glossary/scrum/",
            "Agile Alliance — Scrum (glossary)",
            "Short community glossary entry—shared vocabulary alongside the Guide.",
        ),
        (
            "https://www.scrum.org/resources/kanban-guide-scrum-teams",
            "Kanban Guide for Scrum Teams",
            "When you blend flow policies with Scrum cadence—extends the lifecycle map with pull and WIP thinking.",
        ),
    ]
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Process maps for sprint lifecycle, planning, daily loop, Definition of Done, and Review feedback. '
            "They mirror the <strong class=\"text-body\">empirical process</strong> (transparency, inspection, adaptation) described in the Scrum Guide. "
            'Canonical Markdown: <a href="../methodologies/scrum/process-and-flows.md" class="link-success">process-and-flows.md</a>.</p>',
            first=True,
        ),
        diagrams_section("Flow diagrams", "diagrams", diagrams),
        flow_details_section("flow-details", flow_items),
        section(
            "phases",
            "Phases A–F in one sprint",
            table(
                ["Phase", "Where in Scrum"],
                [
                    ["A Shape", "Refinement + PO/stakeholder"],
                    ["B Plan", "Sprint Planning"],
                    ["C Build", "Execution + Daily"],
                    ["D Verify", "DoD + Review"],
                    ["E Release", "Business ships when ready"],
                    ["F Learn", "Retro + production feedback"],
                ],
            ),
        ),
        external_sources_section("sources", ext),
    ]
    main = "\n".join(s)
    return page_shell(
        browser_title="Scrum — Process &amp; flows",
        h1="Scrum — Process &amp; flows",
        intro="<strong class=\"text-body\">Mermaid</strong> maps plus a per-diagram walkthrough and framework links—kept in sync with Markdown.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-scrum.html", "Scrum"),
            (None, "Process"),
        ],
        main_sections=main,
        toc=[
            ("overview", "Overview"),
            ("diagrams", "Diagrams"),
            ("flow-details", "Flow details"),
            ("phases", "A–F map"),
            ("sources", "Sources"),
        ],
        prev_href="methodologies-scrum-ceremonies.html",
        prev_label="← Ceremonies",
        next_href="methodologies-kanban.html",
        next_label="Kanban →",
        canonical_md="../methodologies/scrum/process-and-flows.md",
        mermaid=True,
    )


# --- Kanban ---


def kanban_foundation() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Kanban optimizes <strong class="text-body">flow</strong> with visualization, policies, and WIP limits. Tracking and C1–C6 still apply. Canonical: <a href="../methodologies/kanban/foundation-connection.md" class="link-success">foundation-connection.md</a>.</p>',
            first=True,
        ),
        section(
            "phases",
            "Phases A–F",
            table(
                ["Phase", "Kanban expression"],
                [
                    [b("A"), "Options / funnel / discovery"],
                    [b("B"), "Replenishment → committed columns"],
                    [b("C"), "Pull per Definition of Workflow"],
                    [b("D"), "Column DoD / QA swimlanes"],
                    [b("E"), "Release policy (on demand, train)"],
                    [b("F"), "SDR, retros, upstream feedback"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0"><strong class="text-body">Rule:</strong> No replenishment + no review cadence = board only, not a managed system.</p>',
        ),
        section(
            "tracking",
            "Tracking spine",
            table(
                ["Artifact", "Kanban mapping"],
                [
                    ["Intent", "Card at intake; may be off-board"],
                    ["Spec", "Linked doc / AC on card"],
                    ["Plan", "Policies + commitment point"],
                    ["Tasks", "Subtasks / child cards"],
                    ["PRs", "Linked; policy may require before merge"],
                    ["Reviews", "Per transition policy"],
                    ["Release", "Train or continuous"],
                ],
            ),
        ),
        section(
            "intents",
            "Ceremony intents",
            table(
                ["Intent", "Typical ceremony"],
                [
                    [b("C1"), "Replenishment; prioritization"],
                    [b("C2"), "Refinement before pull"],
                    [b("C3"), "Stand-up / workflow meeting"],
                    [b("C4"), "QA / release checklist"],
                    [b("C5"), "Retro; systems thinking"],
                    [b("C6"), "Stakeholder review; docs"],
                ],
            ),
        ),
        section(
            "archetypes",
            "Archetypes",
            table(
                ["Role", "Archetypes"],
                [
                    ["SRM / PM", "Sponsor proxy, Orchestrator"],
                    ["Delivery team", "Implementer, Quality advocate"],
                    ["Coach", "Orchestrator, Quality advocate"],
                ],
            ),
        ),
        section(
            "commitments",
            "Conceptual commitments",
            '<ul class="text-body-secondary small mb-0"><li>Visualization</li><li>WIP limits / policies</li><li>Explicit Definition of Workflow</li><li>Manage flow (lead time, predictability)</li></ul>',
        ),
        section(
            "antipatterns",
            "Anti-patterns",
            table(
                ["Anti-pattern", "Fix"],
                [
                    ["Infinite columns, no WIP", "Minimal workflow + limits"],
                    ["Urgent bypass lane abuse", "Steer authorizes class of service"],
                    ["Dev-only board", "Extend upstream visibility"],
                ],
            ),
        ),
        diagrams_section(
            "Diagrams",
            "diagrams",
            [
                """flowchart LR
  O[Options] --> R[Ready]
  R --> D[Doing]
  D --> V[Verify]
  V --> Rel[Released]""",
                """flowchart TD
  A[Top options] --> B{Fits WIP?}
  B -->|No| C[Defer / split]
  C --> A
  B -->|Yes| D{Deps clear?}
  D -->|No| E[Spike]
  E --> A
  D -->|Yes| F[Pull]""",
            ],
        ),
    ]
    return page_shell(
        browser_title="Kanban — Foundation &amp; fit",
        h1="Kanban — Foundation &amp; fit",
        intro='Foundation fit for Kanban teams.',
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-kanban.html", "Kanban"),
            (None, "Foundation"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("phases", "Phases A–F"),
            ("tracking", "Tracking"),
            ("intents", "Intents"),
            ("archetypes", "Archetypes"),
            ("commitments", "Commitments"),
            ("antipatterns", "Anti-patterns"),
            ("diagrams", "Diagrams"),
        ],
        prev_href="methodologies-kanban.html",
        prev_label="← Kanban",
        next_href="methodologies-kanban-roles.html",
        next_label="Roles →",
        canonical_md="../methodologies/kanban/foundation-connection.md",
        mermaid=True,
    )


def kanban_roles() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Kanban does not mandate Scrum roles—these <strong class="text-body">accountabilities</strong> are typical. Canonical: <a href="../methodologies/kanban/roles.md" class="link-success">roles.md</a>.</p>',
            first=True,
        ),
        section(
            "srm",
            "Service request manager / PM",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Ordering work entering the system; stakeholder alignment"],
                    ["Archetypes", "Sponsor proxy, Orchestrator"],
                    ["Outputs", "Ordered options, AC at pull, class of service"],
                ],
            ),
        ),
        section(
            "team",
            "Delivery team",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Pull per policy; DoW / DoD; improve flow"],
                    ["Archetypes", "Implementer, Quality advocate"],
                    ["Outputs", "Shipped increments, blockers surfaced, honest metrics"],
                ],
            ),
        ),
        section(
            "coach",
            "Coach",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Evolution of system; teaching Kanban"],
                    ["Archetypes", "Orchestrator, Quality advocate"],
                    ["Outputs", "Policy drafts, retro facilitation, fitness metrics"],
                ],
            ),
        ),
        section(
            "participation",
            "Ceremony participation",
            table(
                ["Ceremony", "SRM/PM", "Team", "Coach"],
                [
                    ["Replenishment", "R", "R", "O"],
                    ["Stand-up", "O", "R", "O"],
                    ["Delivery review", "R", "R", "O"],
                    ["Retro", "O", "R", "O (facilitate)"],
                    ["Service delivery review", "R", "R", "O"],
                ],
            ),
        ),
        section(
            "raci",
            "Replenishment RACI",
            table(
                ["Outcome", "SRM", "Team"],
                [
                    ["What pulls next", b("A") + "/R", "C"],
                    ["WIP feasibility", "C", b("R")],
                    ["Policy experiments", "C", "R"],
                ],
            ),
        ),
        section(
            "scrum_titles",
            "Scrum titles on a Kanban team",
            '<p class="text-body-secondary small mb-0">PO ≈ SRM for ordering. SM ≈ coach/facilitator unless coding—document in working agreement.</p>',
        ),
        diagrams_section(
            "Flow",
            "diagrams",
            [
                """flowchart LR
  Rep[Replenishment] --> Pull[Team pulls]
  Pull --> Done[Done / release]
  Done --> Rep"""
            ],
        ),
    ]
    return page_shell(
        browser_title="Kanban — Roles",
        h1="Kanban — Roles",
        intro="Accountabilities and ceremony participation.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-kanban.html", "Kanban"),
            (None, "Roles"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("srm", "SRM / PM"),
            ("team", "Delivery team"),
            ("coach", "Coach"),
            ("participation", "Participation"),
            ("raci", "Replenishment RACI"),
            ("scrum_titles", "Scrum titles"),
            ("diagrams", "Diagram"),
        ],
        prev_href="methodologies-kanban-foundation.html",
        prev_label="← Foundation",
        next_href="methodologies-kanban-ceremonies.html",
        next_label="Ceremonies →",
        canonical_md="../methodologies/kanban/roles.md",
        mermaid=True,
    )


def kanban_ceremonies() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Policies and cadences replace fixed Scrum timeboxes. Canonical: <a href="../methodologies/kanban/ceremonies-prescriptive.md" class="link-success">ceremonies-prescriptive.md</a>.</p>',
            first=True,
        ),
        diagrams_section(
            "Cadence overview",
            "diagram",
            [
                """flowchart LR
  Rep[Replenishment] --> SU[Stand-up]
  SU --> W[Work]
  W --> DR[Delivery review]
  DR --> RT[Retro]"""
            ],
        ),
    ]
    blocks = [
        (
            "replenishment",
            "Replenishment",
            "C1 + C2",
            "Ordered options, WIP, deps",
            "Pulled cards, transparent queue",
            "SRM R, team R, stakeholders O",
            "Weekly or threshold; 30–60 min",
            "Aging review → clarify → pull → policy notes",
        ),
        (
            "standup",
            "Stand-up / workflow",
            "C3",
            "Board, blockers",
            "Unblocks, handoffs",
            "Team R; SRM O; coach O",
            "Daily or 2–3×/wk",
            "Walk board right-to-left",
        ),
        (
            "delivery",
            "Delivery review",
            "C4 + C6",
            "Shipped work, metrics, demo",
            "Feedback, options updates",
            "SRM R, team R, stakeholders R",
            "Weekly–monthly",
            "Shipped → demo → metrics → Q&A",
        ),
        (
            "retro",
            "Team retrospective",
            "C5",
            "Flow metrics, pain, prior actions",
            "1–3 experiments",
            "Team R; SRM O; coach facilitates O",
            "Bi-weekly–monthly",
            "Data → insights → experiments",
        ),
        (
            "sdr",
            "Service delivery review",
            "C1 + C5",
            "Cross-team deps, portfolio",
            "Management actions",
            "Team reps, leadership",
            "Monthly–quarterly",
            "Service metrics → systemic impediments",
        ),
    ]
    for sid, title, intent, inp, out, people, timeb, agenda in blocks:
        inner = io_table([(intent, inp, out, people, timeb)])
        inner += f'<p class="text-body-secondary small mb-0"><strong class="text-body">Agenda:</strong> {e(agenda)}</p>'
        s.append(section(sid, title, inner))
    s.append(
        section(
            "summary",
            "I/O summary",
            table(
                ["Ceremony", "Outputs"],
                [
                    ["Replenishment", "Pulled work, clarity"],
                    ["Stand-up", "Unblocks"],
                    ["Delivery review", "Feedback"],
                    ["Retro", "Experiments"],
                    ["SDR", "Escalations resolved"],
                ],
            ),
        )
    )
    return page_shell(
        browser_title="Kanban — Ceremonies",
        h1="Kanban — Ceremonies",
        intro="Prescriptive ceremonies for flow-based delivery.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-kanban.html", "Kanban"),
            (None, "Ceremonies"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("diagram", "Cadence"),
            ("replenishment", "Replenishment"),
            ("standup", "Stand-up"),
            ("delivery", "Delivery review"),
            ("retro", "Retro"),
            ("sdr", "SDR"),
            ("summary", "Summary"),
        ],
        prev_href="methodologies-kanban-roles.html",
        prev_label="← Roles",
        next_href="methodologies-kanban-process.html",
        next_label="Process →",
        canonical_md="../methodologies/kanban/ceremonies-prescriptive.md",
        mermaid=True,
    )


def kanban_process() -> str:
    diagrams = [
        """flowchart LR
  O[Options] --> R[Ready]
  R --> D[Doing]
  D --> V[Verify]
  V --> Rel[Released]""",
        """flowchart TD
  A[Top options] --> B{Fits WIP / policy?}
  B -->|No| C[Defer or split]
  C --> A
  B -->|Yes| D{Dependencies clear?}
  D -->|No| E[Spike or align]
  E --> A
  D -->|Yes| F[Pull to Ready / Doing]""",
        """flowchart TD
  X[Blocker raised] --> Y{Fix in 24h?}
  Y -->|Yes| Z[Swarm]
  Z --> W[Resume]
  Y -->|No| U[Escalate SRM / Steer]
  U --> P[Decision]
  P --> W""",
        """flowchart LR
  Done[Done] --> RC[Release candidate]
  RC --> T[Train T]
  T --> Prod[Production]""",
    ]
    flow_items = [
        (
            "Pull through the value stream",
            "Columns represent agreed states of work, not org chart silos. Movement is governed by your Definition of Workflow (policies per transition) and WIP limits. "
            "Work is pulled when downstream capacity signals readiness—pushing work into Doing without capacity creates queueing waste and hides true lead time.",
        ),
        (
            "Replenishment decision",
            "Replenishment chooses which options enter the committed part of the system. Before pull, the item must fit WIP and class-of-service rules and have clear dependencies; otherwise defer, split, or run a timeboxed alignment or spike. "
            "This loop prevents half-ready work from consuming attention in Doing.",
        ),
        (
            "Blocked work escalation",
            "Blockers are first-class: the team tries fast resolution (e.g. swarm or pair) when policy allows. "
            "If resolution exceeds a time threshold or needs a priority trade-off, escalate to service delivery management or steering so the decision is explicit. "
            "The flow resumes only after a recorded decision—avoid silent workarounds that break policy.",
        ),
        (
            "Release train (example policy)",
            "Done on the board does not automatically mean in production: many systems batch releases on a train or calendar for coordination. "
            "The handoff from Done to release candidate should be policy-driven (who approves, what evidence is required). "
            "Adjust the diagram to match continuous delivery if your Definition of Workflow says so.",
        ),
    ]
    ext = [
        (
            "https://kanban.university/kanban-guide",
            "Kanban University — The Kanban Guide",
            "Current guide text for Kanban method practices—primary framework reference for flow and evolution.",
        ),
        (
            "https://www.agilealliance.org/glossary/kanban/",
            "Agile Alliance — Kanban (glossary)",
            "Short definition and roots—quick orientation before deeper guides.",
        ),
        (
            "https://www.scrum.org/resources/kanban-guide-scrum-teams",
            "Kanban Guide for Scrum Teams",
            "Official integration narrative when Kanban policies sit inside a Scrum cadence.",
        ),
        (
            "https://prokanban.org/",
            "ProKanban.org",
            "Professional Kanban community—training paths and deeper patterns.",
        ),
    ]
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Value stream, replenishment, escalation, and release policy. Kanban is <strong class="text-body">policy- and metrics-driven</strong> flow, not a fixed ceremony set—your Definition of Workflow is the source of truth. '
            'Canonical: <a href="../methodologies/kanban/process-and-flows.md" class="link-success">process-and-flows.md</a>.</p>',
            first=True,
        ),
        diagrams_section("Diagrams", "diagrams", diagrams),
        flow_details_section("flow-details", flow_items),
        section(
            "af",
            "Phases A–F",
            table(
                ["Phase", "Locus"],
                [
                    ["A", "Options"],
                    ["B", "Replenishment"],
                    ["C", "Doing"],
                    ["D", "Verify"],
                    ["E", "Release policy"],
                    ["F", "Ops → options"],
                ],
            ),
        ),
        external_sources_section("sources", ext),
    ]
    return page_shell(
        browser_title="Kanban — Process",
        h1="Kanban — Process &amp; flows",
        intro="Mermaid maps, per-diagram narrative, and links to Kanban guide–grade sources.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-kanban.html", "Kanban"),
            (None, "Process"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("diagrams", "Diagrams"),
            ("flow-details", "Flow details"),
            ("af", "A–F"),
            ("sources", "Sources"),
        ],
        prev_href="methodologies-kanban-ceremonies.html",
        prev_label="← Ceremonies",
        next_href="methodologies-phased.html",
        next_label="Phased →",
        canonical_md="../methodologies/kanban/process-and-flows.md",
        mermaid=True,
    )


# --- Phased ---


def phased_foundation() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Stages, gates, baselines—mapped to blueprint A–F and tracking. Canonical: <a href="../methodologies/phased/foundation-connection.md" class="link-success">foundation-connection.md</a>.</p>',
            first=True,
        ),
        section(
            "stages",
            "A–F vs stage artifacts",
            table(
                ["Phase", "Typical artifacts"],
                [
                    [b("A"), "Charter, business case, HL requirements"],
                    [b("B"), "Schedule, WBS, design baseline"],
                    [b("C"), "Implementation per baseline"],
                    [b("D"), "Test phases, audits"],
                    [b("E"), "Deploy plan, go-live, handover"],
                    [b("F"), "Warranty, hypercare, benefits"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0">Map stage names to A–F in RAID/handbook for one language with agents and audits.</p>',
        ),
        section(
            "tracking",
            "Tracking spine",
            table(
                ["Artifact", "Phased expression"],
                [
                    ["Intent", "CR / requirement ID"],
                    ["Spec", "SRS, design baseline"],
                    ["Plan", "WBS activities"],
                    ["Tasks", "Work packages"],
                    ["PRs", "Linked to requirement IDs"],
                    ["Reviews", "Inspections, signatures"],
                    ["Release", "CM tag, release record"],
                ],
            ),
        ),
        section(
            "intents",
            "Ceremony intents",
            table(
                ["Intent", "Examples"],
                [
                    [b("C1"), "Steering; gate go/no-go"],
                    [b("C2"), "Planning workshop; design review"],
                    [b("C3"), "War room; weekly status"],
                    [b("C4"), "TRR; UAT sign-off"],
                    [b("C5"), "PIR; lessons learned"],
                    [b("C6"), "Knowledge transfer; training"],
                ],
            ),
        ),
        section(
            "archetypes",
            "Archetypes",
            table(
                ["Role", "Archetypes"],
                [
                    ["Sponsor / SRO", "Sponsor proxy, Steer"],
                    ["PM", "Orchestrator"],
                    ["BA", "Orchestrator, Implementer"],
                    ["Tech lead", "Quality advocate, Implementer"],
                    ["Team", "Implementer"],
                ],
            ),
        ),
        section(
            "antipatterns",
            "Anti-patterns",
            table(
                ["Anti-pattern", "Fix"],
                [
                    ["Gate = paperwork", "Objective exit criteria"],
                    ["Scope via email", "Change control"],
                    ["UAT = first test", "Shift C4 left"],
                ],
            ),
        ),
        diagrams_section(
            "Diagrams",
            "diagrams",
            [
                """flowchart LR
  A[Shape] --> B[Plan]
  B --> C[Build]
  C --> D[Verify]
  D --> E[Release]
  E --> F[Operate]"""
            ],
        ),
    ]
    return page_shell(
        browser_title="Phased — Foundation",
        h1="Phased delivery — Foundation &amp; fit",
        intro="Stage-gate fit to the blueprint.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-phased.html", "Phased delivery"),
            (None, "Foundation"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("stages", "Stages"),
            ("tracking", "Tracking"),
            ("intents", "Intents"),
            ("archetypes", "Archetypes"),
            ("antipatterns", "Anti-patterns"),
            ("diagrams", "Diagrams"),
        ],
        prev_href="methodologies-phased.html",
        prev_label="← Phased delivery",
        next_href="methodologies-phased-roles.html",
        next_label="Roles →",
        canonical_md="../methodologies/phased/foundation-connection.md",
        mermaid=True,
    )


def phased_roles() -> str:
    roles = [
        (
            "sponsor",
            "Sponsor / SRO",
            [
                ["Accountable for", "Outcomes, funding, escalations; gate acceptance"],
                ["Archetypes", "Sponsor proxy, Steer"],
                ["Outputs", "Charter go, stage go, change exceptions"],
            ],
        ),
        (
            "pm",
            "Project / program manager",
            [
                ["Accountable for", "Schedule, budget, RAID, comms—not technical truth"],
                ["Archetypes", "Orchestrator"],
                ["Outputs", "Status, gate packs, dependencies"],
            ],
        ),
        (
            "ba",
            "Business analyst",
            [
                ["Accountable for", "Requirements traceability, elicitation, UAT often"],
                ["Archetypes", "Orchestrator, Implementer"],
                ["Outputs", "SRS, use cases, AC packs"],
            ],
        ),
        (
            "tech",
            "Tech lead / architect",
            [
                ["Accountable for", "Technical integrity, NFRs, build approach"],
                ["Archetypes", "Quality advocate, Implementer"],
                ["Outputs", "Design baselines, ADRs, test strategy"],
            ],
        ),
        (
            "team",
            "Delivery team",
            [
                ["Accountable for", "Work packages per baseline; escalate variances"],
                ["Archetypes", "Implementer, Quality advocate"],
                ["Outputs", "Build, test execution"],
            ],
        ),
    ]
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Prescriptive roles for gated delivery. Canonical: <a href="../methodologies/phased/roles.md" class="link-success">roles.md</a>.</p>',
            first=True,
        ),
    ]
    for sid, title, rows in roles:
        s.append(section(sid, title, table(["Aspect", "Guidance"], rows)))
    s.append(
        section(
            "participation",
            "Ceremony participation",
            table(
                ["Ceremony", "Sponsor", "PM", "BA", "Tech", "Team"],
                [
                    ["Gate review", "R", "R", "R", "R", "O"],
                    ["Weekly status", "O", "R", "O", "O", "O"],
                    ["Design review", "O", "R", "R", "R", "R"],
                    ["Test readiness", "O", "R", "O", "R", "R"],
                    ["UAT", "O", "R", "R", "O", "O"],
                    ["PIR", "O", "R", "R", "R", "R"],
                ],
            ),
        )
    )
    s.append(
        diagrams_section(
            "RACI at gate (concept)",
            "diagram",
            [
                """flowchart TD
  GP[Gate pack] --> TL[Tech lead review]
  TL --> PM[PM integrates]
  PM --> SP[Sponsor decision]
  SP -->|Go| NX[Next stage]
  SP -->|Hold| AC[Actions]"""
            ],
        )
    )
    return page_shell(
        browser_title="Phased — Roles",
        h1="Phased delivery — Roles",
        intro="Sponsor, PM, BA, tech lead, team.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-phased.html", "Phased delivery"),
            (None, "Roles"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("sponsor", "Sponsor"),
            ("pm", "PM"),
            ("ba", "BA"),
            ("tech", "Tech lead"),
            ("team", "Team"),
            ("participation", "Participation"),
            ("diagram", "Diagram"),
        ],
        prev_href="methodologies-phased-foundation.html",
        prev_label="← Foundation",
        next_href="methodologies-phased-ceremonies.html",
        next_label="Ceremonies →",
        canonical_md="../methodologies/phased/roles.md",
        mermaid=True,
    )


def phased_ceremonies() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Stage-gate ceremonies (names vary by PMO). Canonical: <a href="../methodologies/phased/ceremonies-prescriptive.md" class="link-success">ceremonies-prescriptive.md</a>.</p>',
            first=True,
        ),
        diagrams_section(
            "Stage flow",
            "diagram",
            [
                """flowchart LR
  CH[Charter] --> PL[Plan baseline]
  PL --> DR[Design review]
  DR --> BL[Build]
  BL --> TR[TRR]
  TR --> UA[UAT]
  UA --> RL[Release readiness]
  RL --> PI[PIR]"""
            ],
        ),
    ]
    items = [
        ("charter", "Initiation / charter", "C1", "Business case, scope", "Charter, PM appointed", "Sponsor R, PM R", "Days–weeks"),
        ("plan", "Planning baseline", "C1+C2", "Req outline, estimates", "Baseline schedule/WBS", "PM, BA, tech R", "Workshops"),
        ("design", "Design review", "C2+C4", "Design, NFR, security", "Approved baseline / actions", "Tech R", "Gate"),
        ("status", "Weekly status", "C3+C1", "Variance, RAID", "Decisions, comms", "PM R, leads R", "30–60 min"),
        ("trr", "Test readiness (TRR)", "C4", "Plans, env, traceability", "Go/hold to test", "QA, tech, PM R", "Gate"),
        ("uat", "UAT / acceptance", "C4", "Scripts, stable build", "Sign-off or defects", "Business A, BA, PM R", "Formal"),
        ("go", "Release readiness", "C1+E", "Checklist, rollback", "Go / no-go", "PM, ops R; sponsor A", "Gate"),
        ("pir", "PIR / lessons", "C5+C6", "Benefits, incidents", "Lessons register", "PM, leads R", "Post-release"),
    ]
    for sid, title, intent, inp, out, people, timeb in items:
        inner = io_table([(intent, inp, out, people, timeb)])
        s.append(section(sid, title, inner))
    s.append(
        section(
            "summary",
            "Summary",
            table(
                ["Ceremony", "Output"],
                [
                    ["Charter gate", "Authorized project"],
                    ["Plan gate", "Baselines"],
                    ["Design review", "Technical approval"],
                    ["TRR", "Test entry"],
                    ["UAT", "Acceptance"],
                    ["Release readiness", "Production go"],
                    ["PIR", "Organizational learning"],
                ],
            ),
        )
    )
    return page_shell(
        browser_title="Phased — Ceremonies",
        h1="Phased delivery — Ceremonies",
        intro="Gates and reviews with I/O.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-phased.html", "Phased delivery"),
            (None, "Ceremonies"),
        ],
        main_sections="\n".join(s),
        toc=[("overview", "Overview"), ("diagram", "Stage flow")]
        + [(x[0], x[1]) for x in items]
        + [("summary", "Summary")],
        prev_href="methodologies-phased-roles.html",
        prev_label="← Roles",
        next_href="methodologies-phased-process.html",
        next_label="Process →",
        canonical_md="../methodologies/phased/ceremonies-prescriptive.md",
        mermaid=True,
    )


def phased_process() -> str:
    diagrams = [
        """flowchart LR
  I[Initiate] --> P[Plan]
  P --> D[Design]
  D --> B[Build]
  B --> T[Test]
  T --> U[UAT]
  U --> R[Release]
  R --> O[Operate]""",
        """flowchart TD
  G[Gate pack] --> C{Exit criteria met?}
  C -->|No| H[Hold + actions]
  H --> G
  C -->|Yes| N{Sponsor approves?}
  N -->|No| X[Defer / kill]
  N -->|Yes| Y[Next stage]""",
        """flowchart LR
  CR[Change request] --> IA[Impact analysis]
  IA --> B{Steer decision}
  B -->|Approve| BL[Re-baseline]
  B -->|Reject| Q[Queue / drop]""",
        """flowchart LR
  Req[Requirement ID] --> DS[Design ref]
  DS --> TC[Test case]
  TC --> RN[Release note]""",
    ]
    flow_items = [
        (
            "Stage sequence",
            "This linear chain is a teaching simplification: real programs often overlap design and build or run rolling UAT, subject to governance. "
            "Governance gates usually sit on transitions: each stage produces a baseline (scope, design, test strategy) that the next stage consumes. "
            "Map your organization’s named stages onto blueprint phases A–F in RAID and the handbook so audits and agents share one vocabulary.",
        ),
        (
            "Gate decision",
            "A gate pack proves exit criteria for the stage—evidence of quality, risk treatment, and readiness. If criteria fail, the stage is held with corrective actions rather than rubber-stamping. "
            "Sponsor or steering approval is an explicit decision to spend and commit to the next baseline; defer, kill, or replan are valid outcomes.",
        ),
        (
            "Change control (scope)",
            "Change requests capture proposed deviation from the approved baseline. Impact analysis covers schedule, cost, risk, and traceability. "
            "Steering approves (re-baseline, often with versioned artifacts) or rejects (queue for a later release or drop). "
            "Ad-hoc scope without this path erodes traceability and auditability.",
        ),
        (
            "Traceability thread",
            "Regulated and large-scale delivery depends on forward and backward trace: requirement IDs link to design references, test cases, and release notes. "
            "This supports impact analysis when a defect or CR arrives and demonstrates coverage to auditors—not optional when gates are meaningful.",
        ),
    ]
    ext = [
        (
            "https://www.iso.org/standard/63712.html",
            "ISO/IEC/IEEE 12207 (catalogue)",
            "International software life-cycle process standard—formal anchor for phased / regulated lifecycles (full text is licensed).",
        ),
        (
            "https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge",
            "Wikipedia — Project Management Body of Knowledge (PMBOK)",
            "Encyclopedia overview of PMI’s knowledge areas and process groups—frames phased governance when full PMBOK text is licensed; see also PMI.org in REFERENCE-LINKS.md.",
        ),
        (
            "https://en.wikipedia.org/wiki/Waterfall_model",
            "Wikipedia — Waterfall model",
            "Informal history and diagrams of sequential delivery—context, not a normative substitute for your SDLC policy.",
        ),
        (
            "https://en.wikipedia.org/wiki/Agile_software_development",
            "Wikipedia — Agile software development",
            "Contrast with iterative methods—useful when blending phase gates with iterative build inside stages.",
        ),
    ]
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Stages, gate decisions, change control, and traceability—typical of <strong class="text-body">plan-driven</strong> and regulated contexts. '
            "Adapt names to your org; keep the intent: explicit baselines, decisions, and evidence. "
            'Canonical: <a href="../methodologies/phased/process-and-flows.md" class="link-success">process-and-flows.md</a>.</p>',
            first=True,
        ),
        diagrams_section("Diagrams", "diagrams", diagrams),
        flow_details_section("flow-details", flow_items),
        section(
            "af",
            "Phases A–F (typical mapping)",
            table(
                ["Blueprint phase", "Typical phased locus"],
                [
                    ["A Shape", "Initiate; charter; high-level requirements"],
                    ["B Plan", "Planning; WBS; schedule baseline"],
                    ["C Build", "Design and implementation per baseline"],
                    ["D Verify", "Test phases; inspections; exit evidence"],
                    ["E Release", "UAT; deployment; handover"],
                    ["F Learn", "Operate; warranty; benefits realization"],
                ],
            ),
        ),
        external_sources_section("sources", ext),
    ]
    return page_shell(
        browser_title="Phased — Process",
        h1="Phased delivery — Process &amp; flows",
        intro="Mermaid maps, gate/CR/traceability narrative, and standards-oriented links.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-phased.html", "Phased delivery"),
            (None, "Process"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("diagrams", "Diagrams"),
            ("flow-details", "Flow details"),
            ("af", "A–F map"),
            ("sources", "Sources"),
        ],
        prev_href="methodologies-phased-ceremonies.html",
        prev_label="← Ceremonies",
        next_href="methodologies-xp.html",
        next_label="XP →",
        canonical_md="../methodologies/phased/process-and-flows.md",
        mermaid=True,
    )


# --- XP ---


def xp_foundation() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Technical excellence + tight customer feedback. Canonical: <a href="../methodologies/xp/foundation-connection.md" class="link-success">foundation-connection.md</a>.</p>',
            first=True,
        ),
        section(
            "phases",
            "Phases A–F",
            table(
                ["Phase", "XP expression"],
                [
                    [b("A"), "Stories with customer; release planning themes"],
                    [b("B"), "Iteration planning; tasks"],
                    [b("C"), "Pairing, TDD, CI"],
                    [b("D"), "Acceptance tests; collective ownership"],
                    [b("E"), "Small / frequent releases"],
                    [b("F"), "Production feedback; retro"],
                ],
            ),
        ),
        section(
            "tracking",
            "Tracking spine",
            table(
                ["Artifact", "XP mapping"],
                [
                    ["Intent", "Story"],
                    ["Spec", "Story + acceptance tests"],
                    ["Plan", "Iteration plan, board"],
                    ["Tasks", "Engineering tasks"],
                    ["PRs", "Git; pair may co-author"],
                    ["Reviews", "Pair + standards"],
                    ["Release", "Small batch / CD"],
                ],
            ),
        ),
        section(
            "intents",
            "Ceremony intents",
            table(
                ["Intent", "XP"],
                [
                    [b("C1"), "Release planning"],
                    [b("C2"), "Iteration planning"],
                    [b("C3"), "Stand-up or pairing"],
                    [b("C4"), "Acceptance; demo"],
                    [b("C5"), "Retro"],
                    [b("C6"), "Coding standards; metaphor"],
                ],
            ),
        ),
        section(
            "archetypes",
            "Archetypes",
            table(
                ["Role", "Archetypes"],
                [
                    ["Customer", "Sponsor proxy"],
                    ["Coach", "Orchestrator, Quality advocate"],
                    ["Developers", "Implementer, Quality advocate"],
                ],
            ),
        ),
        section(
            "antipatterns",
            "Anti-patterns",
            table(
                ["Anti-pattern", "Fix"],
                [
                    ["XP without tests", "TDD / ATDD"],
                    ["Absent customer", "Empowered proxy + office hours"],
                    ["Pairing as watching", "Rotate driver/nav; ping-pong TDD"],
                ],
            ),
        ),
        diagrams_section(
            "Iteration loop",
            "diagrams",
            [
                """flowchart LR
  RP[Release plan] --> IP[Iteration plan]
  IP --> B[Build TDD/CI]
  B --> A[Accept]
  A --> D[Demo]
  D --> RT[Retro]
  RT --> IP"""
            ],
        ),
    ]
    return page_shell(
        browser_title="XP — Foundation",
        h1="XP — Foundation &amp; fit",
        intro="Foundation mapping for Extreme Programming.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-xp.html", "XP"),
            (None, "Foundation"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("phases", "Phases"),
            ("tracking", "Tracking"),
            ("intents", "Intents"),
            ("archetypes", "Archetypes"),
            ("antipatterns", "Anti-patterns"),
            ("diagrams", "Diagram"),
        ],
        prev_href="methodologies-xp.html",
        prev_label="← XP",
        next_href="methodologies-xp-roles.html",
        next_label="Roles →",
        canonical_md="../methodologies/xp/foundation-connection.md",
        mermaid=True,
    )


def xp_roles() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Customer, coach, developers—often maps to PO + team + coach today. Canonical: <a href="../methodologies/xp/roles.md" class="link-success">roles.md</a>.</p>',
            first=True,
        ),
        section(
            "customer",
            "Customer",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Stories, priorities, acceptance"],
                    ["Archetypes", "Sponsor proxy"],
                    ["Outputs", "Ordered stories, AT approval, iteration done calls"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0">If not onsite: single empowered proxy + fixed availability windows.</p>',
        ),
        section(
            "coach",
            "Coach",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Practice adherence; facilitation"],
                    ["Archetypes", "Orchestrator, Quality advocate"],
                    ["Outputs", "Improvements; shield from thrash"],
                ],
            )
            + '<p class="text-body-secondary small mt-2 mb-0">Not people manager assigning tasks unless org merges roles—document if so.</p>',
        ),
        section(
            "devs",
            "Developers",
            table(
                ["Aspect", "Guidance"],
                [
                    ["Accountable for", "Collective ownership; pairing; tests; CI"],
                    ["Archetypes", "Implementer, Quality advocate"],
                    ["Outputs", "Running tested features / iteration"],
                ],
            ),
        ),
        section(
            "participation",
            "Ceremony participation",
            table(
                ["Ceremony", "Customer", "Coach", "Developers"],
                [
                    ["Release planning", "R", "R", "R"],
                    ["Iteration planning", "R", "O", "R"],
                    ["Daily stand-up", "O", "O", "R"],
                    ["Mid-iteration check-in", "O", "O", "R"],
                    ["Acceptance / demo", "R", "O", "R"],
                    ["Retro", "O", "R", "R"],
                ],
            ),
        ),
        diagrams_section(
          "Practice loop",
          "diagrams",
          [
              """flowchart LR
  C[Customer priority] --> T[Team builds with tests]
  T --> A[Acceptance]
  A --> C"""
          ],
        ),
    ]
    return page_shell(
        browser_title="XP — Roles",
        h1="XP — Roles",
        intro="XP accountabilities.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-xp.html", "XP"),
            (None, "Roles"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("customer", "Customer"),
            ("coach", "Coach"),
            ("devs", "Developers"),
            ("participation", "Participation"),
            ("diagrams", "Diagram"),
        ],
        prev_href="methodologies-xp-foundation.html",
        prev_label="← Foundation",
        next_href="methodologies-xp-ceremonies.html",
        next_label="Ceremonies →",
        canonical_md="../methodologies/xp/roles.md",
        mermaid=True,
    )


def xp_ceremonies() -> str:
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Iteration rhythm + engineering practices. Canonical: <a href="../methodologies/xp/ceremonies-prescriptive.md" class="link-success">ceremonies-prescriptive.md</a>.</p>',
            first=True,
        ),
        diagrams_section(
            "Rhythm",
            "diagram",
            [
                """flowchart LR
  RP[Release planning] --> IP[Iteration planning]
  IP --> B[Build]
  B --> AC[Acceptance]
  AC --> DM[Demo]
  DM --> RT[Retro]
  RT --> IP"""
            ],
        ),
    ]
    items = [
        (
            "rp",
            "Release planning",
            "C1",
            "Backlog, velocity, goals",
            "Release plan / themes",
            "Customer R, devs R, coach R",
            "Hours–2 days",
            "Priorities → estimates → cut line",
        ),
        (
            "ip",
            "Iteration planning",
            "C2",
            "Ordered stories, capacity",
            "Iteration backlog, tasks, AT outline",
            "Customer R, devs R, coach O",
            "~½ day / week iteration",
            "Select stories → tasks → pairs → AT outline",
        ),
        (
            "su",
            "Daily stand-up (optional)",
            "C3",
            "Board",
            "Coordination, blocks",
            "Devs R; customer/coach O",
            "15 min",
            "Optional if pairing gives continuous sync",
        ),
        (
            "acc",
            "Acceptance (ongoing)",
            "C4",
            "Story done, tests green",
            "Customer accepts / changes",
            "Customer R, pair R",
            "Continuous",
            "DoD includes agreed tests",
        ),
        (
            "demo",
            "Iteration demo",
            "C4+C6",
            "Accepted stories, environment",
            "Feedback, backlog updates",
            "Customer R, team R",
            "30–60 min",
            "Show accepted work → feedback → backlog tweaks",
        ),
        (
            "retro",
            "Retrospective",
            "C5",
            "Practice adherence, incidents",
            "1–3 practice experiments",
            "Team R; coach R; customer O",
            "1–2 h",
            "Data → insights → practice experiments",
        ),
    ]
    for sid, title, intent, inp, out, people, timeb, agenda in items:
        inner = io_table([(intent, inp, out, people, timeb)])
        inner += f'<p class="text-body-secondary small mb-0"><strong class="text-body">Agenda:</strong> {e(agenda)}</p>'
        s.append(section(sid, title, inner))
    s.append(
        section(
            "practices",
            "Engineering practices (discipline)",
            table(
                ["Practice", "Cadence / rule"],
                [
                    ["Pair programming", "Default for prod code"],
                    ["TDD", "Red–green–refactor"],
                    ["Continuous integration", "Main green; integrate often"],
                    ["Refactoring", "Budget each iteration"],
                    ["Collective ownership", "Anyone improves any module"],
                ],
            ),
        )
    )
    return page_shell(
        browser_title="XP — Ceremonies",
        h1="XP — Ceremonies &amp; rhythm",
        intro="Events and technical discipline.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-xp.html", "XP"),
            (None, "Ceremonies"),
        ],
        main_sections="\n".join(s),
        toc=[("overview", "Overview"), ("diagram", "Rhythm")]
        + [(x[0], x[1]) for x in items]
        + [("practices", "Engineering practices")],
        prev_href="methodologies-xp-roles.html",
        prev_label="← Roles",
        next_href="methodologies-xp-process.html",
        next_label="Process →",
        canonical_md="../methodologies/xp/ceremonies-prescriptive.md",
        mermaid=True,
    )


def xp_process() -> str:
    diagrams = [
        """flowchart LR
  IP[Iteration planning] --> DEV[Build: pair + TDD + CI]
  DEV --> ACC[Acceptance]
  ACC --> DEMO[Demo]
  DEMO --> RT[Retro]
  RT --> IP""",
        """flowchart TD
  R[Red: failing test] --> G[Green: minimal code]
  G --> RF[Refactor]
  RF --> R""",
        """flowchart LR
  S[Story] --> AT[Acceptance tests agreed]
  AT --> IMPL[Implement + unit tests]
  IMPL --> CI[CI green]
  CI --> ACP[Customer accepts]""",
        """flowchart TD
  C[Customer: top story?] --> T[Team: estimate]
  T --> D{Fits iteration?}
  D -->|Yes| P[Pull to iteration]
  D -->|No| C""",
    ]
    flow_items = [
        (
            "Iteration loop",
            "XP compresses feedback: iteration planning commits a small batch of stories; the team builds with pairing, TDD, and continuous integration; acceptance proves value; demo closes the loop with the customer; retrospective improves engineering and collaboration. "
            "The next iteration replanning uses that learning—short cycles reduce the cost of wrong assumptions.",
        ),
        (
            "TDD micro-loop (Red → Green → Refactor)",
            "Write a failing test that expresses desired behavior (Red), implement the smallest change that passes (Green), then refactor with tests green (Refactor). "
            "The loop repeats within a story so design stays test-guided and regressions are caught immediately by CI.",
        ),
        (
            "Story lifecycle",
            "A story is not ready for implementation until acceptance tests are agreed—they define done from the customer’s perspective. "
            "Implementation adds unit tests and keeps CI green; customer acceptance is the final gate before the story counts as delivered.",
        ),
        (
            "Planning game (priorities vs estimates)",
            "The customer orders by business value; the team estimates cost. Stories are pulled into the iteration until capacity is respected. "
            "If the highest-value story does not fit, the conversation returns to splitting, deferring, or adjusting scope—explicit trade-offs instead of silent overload.",
        ),
    ]
    ext = [
        (
            "https://en.wikipedia.org/wiki/Extreme_programming",
            "Wikipedia — Extreme programming",
            "Stable encyclopedia overview of practices and history—entry point before books or blogs.",
        ),
        (
            "https://www.agilealliance.org/agile101/agile-glossary/",
            "Agile Alliance — Agile glossary",
            "Searchable terms for XP-related Agile vocabulary.",
        ),
        (
            "https://ronjeffries.com/xprog/",
            "Ron Jeffries — XP",
            "Practitioner perspective from a central XP voice.",
        ),
        (
            "https://martinfowler.com/bliki/ExtremeProgramming.html",
            "Martin Fowler — XP (Bliki)",
            "Short expert summary on a widely cited site.",
        ),
        (
            "https://wiki.c2.com/?ExtremeProgrammingRoadmap",
            "Wiki.c2 — Extreme Programming Roadmap",
            "Classic wiki index of XP topics—historically influential knowledge base.",
        ),
    ]
    s = [
        section(
            "overview",
            "Overview",
            '<p class="text-body-secondary small mb-0">Iteration cadence, test-driven development, story flow, and the planning game. XP couples <strong class="text-body">technical discipline</strong> (TDD, CI, pairing) with <strong class="text-body">business feedback</strong> (customer, acceptance tests). '
            'Canonical: <a href="../methodologies/xp/process-and-flows.md" class="link-success">process-and-flows.md</a>.</p>',
            first=True,
        ),
        diagrams_section("Diagrams", "diagrams", diagrams),
        flow_details_section("flow-details", flow_items),
        section(
            "af",
            "Phases A–F (XP locus)",
            table(
                ["Phase", "Typical XP locus"],
                [
                    ["A Shape", "Stories with customer; release themes"],
                    ["B Plan", "Iteration planning; tasks"],
                    ["C Build", "Pairing, TDD, CI"],
                    ["D Verify", "Acceptance tests; collective ownership"],
                    ["E Release", "Small / frequent releases"],
                    ["F Learn", "Production feedback; retrospective"],
                ],
            ),
        ),
        external_sources_section("sources", ext),
    ]
    return page_shell(
        browser_title="XP — Process",
        h1="XP — Process &amp; flows",
        intro="Mermaid maps, narrative per flow, and practitioner/wiki references.",
        crumbs=[
            ("index.html", "Handbook"),
            ("methodologies.html", "Methodologies"),
            ("methodologies-xp.html", "XP"),
            (None, "Process"),
        ],
        main_sections="\n".join(s),
        toc=[
            ("overview", "Overview"),
            ("diagrams", "Diagrams"),
            ("flow-details", "Flow details"),
            ("af", "A–F map"),
            ("sources", "Sources"),
        ],
        prev_href="methodologies-xp-ceremonies.html",
        prev_label="← Ceremonies",
        next_href="methodologies-agile.html",
        next_label="Agile →",
        canonical_md="../methodologies/xp/process-and-flows.md",
        mermaid=True,
    )


BUILDERS = {
    "methodologies-scrum-foundation.html": scrum_foundation,
    "methodologies-scrum-ceremonies.html": scrum_ceremonies,
    "methodologies-scrum-process.html": scrum_process,
    "methodologies-kanban-foundation.html": kanban_foundation,
    "methodologies-kanban-roles.html": kanban_roles,
    "methodologies-kanban-ceremonies.html": kanban_ceremonies,
    "methodologies-kanban-process.html": kanban_process,
    "methodologies-phased-foundation.html": phased_foundation,
    "methodologies-phased-roles.html": phased_roles,
    "methodologies-phased-ceremonies.html": phased_ceremonies,
    "methodologies-phased-process.html": phased_process,
    "methodologies-xp-foundation.html": xp_foundation,
    "methodologies-xp-roles.html": xp_roles,
    "methodologies-xp-ceremonies.html": xp_ceremonies,
    "methodologies-xp-process.html": xp_process,
}


def main() -> None:
    for fn, builder in BUILDERS.items():
        if fn in SKIP:
            print("Skip:", fn)
            continue
        path = OUT / fn
        path.write_text(builder(), encoding="utf-8")
        print("Wrote", fn)


if __name__ == "__main__":
    main()
