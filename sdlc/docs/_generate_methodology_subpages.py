#!/usr/bin/env python3
"""Legacy stub generator. Full methodology subchapters use build_methodology_chapters.py instead.

Run from docs/: python3 _generate_methodology_subpages.py — skips paths owned by the builder + hand-maintained Scrum Roles."""
from __future__ import annotations

SHELL_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SDLC blueprint — {title}</title>
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
        <div class="mx-auto doc-content">
"""

SHELL_TAIL = """
          <nav class="d-flex flex-wrap justify-content-between gap-2 mt-4 pt-3 border-top" aria-label="Chapter navigation">
            <a href="{hub_html}" class="btn btn-outline-secondary btn-sm">← {hub_label}</a>
            <a href="methodologies.html" class="btn btn-outline-success btn-sm">Methodologies hub</a>
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
{extra_scripts}
</body>
</html>
"""

def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


METHODS = [
    {
        "slug": "scrum",
        "label": "Scrum",
        "hub_html": "methodologies-scrum.html",
        "overview_md": "scrum.md",
        "folder": "scrum",
        "pages": [
            (
                "foundation",
                "Foundation &amp; fit",
                "foundation-connection.md",
                "How Scrum maps to <strong class=\"text-body\">Phases A–F</strong>, the <strong class=\"text-body\">tracking spine</strong>, ceremony intents <strong class=\"text-body\">C1–C6</strong>, and role archetypes.",
            ),
            (
                "roles",
                "Roles",
                "roles.md",
                "<strong class=\"text-body\">Product Owner</strong>, <strong class=\"text-body\">Scrum Master</strong>, <strong class=\"text-body\">Developers</strong> — accountabilities, event participation matrix, RACI-style outcomes.",
            ),
            (
                "ceremonies",
                "Ceremonies",
                "ceremonies-prescriptive.md",
                "Prescriptive <strong class=\"text-body\">inputs / outputs / participants / agendas</strong> for refinement, Sprint Planning, Daily Scrum, Review, Retrospective, and the Sprint container.",
            ),
            (
                "process",
                "Process &amp; flows",
                "process-and-flows.md",
                "Sprint lifecycle, planning flow, daily loop, DoD gate, stakeholder feedback — see <strong class=\"text-body\">KS diagram</strong> templates in the Markdown source; interactive handbook at blueprints.forgesdlc.com.",
            ),
        ],
    },
    {
        "slug": "kanban",
        "label": "Kanban",
        "hub_html": "methodologies-kanban.html",
        "overview_md": "kanban.md",
        "folder": "kanban",
        "pages": [
            (
                "foundation",
                "Foundation &amp; fit",
                "foundation-connection.md",
                "Flow, WIP, and policies mapped to <strong class=\"text-body\">A–F</strong>, tracking, and <strong class=\"text-body\">C1–C6</strong>.",
            ),
            (
                "roles",
                "Roles",
                "roles.md",
                "<strong class=\"text-body\">Service request manager</strong> / PM, <strong class=\"text-body\">delivery team</strong>, <strong class=\"text-body\">coach</strong> — participation by ceremony.",
            ),
            (
                "ceremonies",
                "Ceremonies",
                "ceremonies-prescriptive.md",
                "<strong class=\"text-body\">Replenishment</strong>, stand-up, delivery review, retrospective, <strong class=\"text-body\">service delivery review</strong> — I/O and cadence.",
            ),
            (
                "process",
                "Process &amp; flows",
                "process-and-flows.md",
                "Pull, replenishment, blocked-work escalation, optional release train.",
            ),
        ],
    },
    {
        "slug": "phased",
        "label": "Phased delivery",
        "hub_html": "methodologies-phased.html",
        "overview_md": "phased-delivery.md",
        "folder": "phased",
        "pages": [
            (
                "foundation",
                "Foundation &amp; fit",
                "foundation-connection.md",
                "Stages, gates, and baselines aligned with <strong class=\"text-body\">A–F</strong> and the tracking spine.",
            ),
            (
                "roles",
                "Roles",
                "roles.md",
                "<strong class=\"text-body\">Sponsor</strong>, <strong class=\"text-body\">PM</strong>, <strong class=\"text-body\">BA</strong>, <strong class=\"text-body\">tech lead</strong>, team — gate participation.",
            ),
            (
                "ceremonies",
                "Ceremonies",
                "ceremonies-prescriptive.md",
                "Charter, planning baseline, design review, TRR, UAT, release readiness, PIR — prescriptive I/O.",
            ),
            (
                "process",
                "Process &amp; flows",
                "process-and-flows.md",
                "Stage sequence, gate decision, change control, traceability thread.",
            ),
        ],
    },
    {
        "slug": "xp",
        "label": "XP",
        "hub_html": "methodologies-xp.html",
        "overview_md": "xp.md",
        "folder": "xp",
        "pages": [
            (
                "foundation",
                "Foundation &amp; fit",
                "foundation-connection.md",
                "Stories, technical practices, and iterations mapped to <strong class=\"text-body\">A–F</strong> and ceremony intents.",
            ),
            (
                "roles",
                "Roles",
                "roles.md",
                "<strong class=\"text-body\">Customer</strong>, <strong class=\"text-body\">coach</strong>, <strong class=\"text-body\">developers</strong> — who accepts work.",
            ),
            (
                "ceremonies",
                "Ceremonies",
                "ceremonies-prescriptive.md",
                "Release planning, iteration planning, stand-up (optional), acceptance, demo, retrospective.",
            ),
            (
                "process",
                "Process &amp; flows",
                "process-and-flows.md",
                "Iteration loop, TDD micro-loop, story lifecycle, planning game.",
            ),
        ],
    },
]


def page_html(
    m: dict,
    _page_id: str,
    page_title_html: str,
    md_file: str,
    blurb_html: str,
) -> str:
    title_plain = f"{m['label']} — {page_title_html.replace('&amp;', '&')}"
    breadcrumb = f"""<nav aria-label="breadcrumb"><ol class="breadcrumb small mb-3">
              <li class="breadcrumb-item"><a href="index.html">Handbook</a></li>
              <li class="breadcrumb-item"><a href="methodologies.html">Methodologies</a></li>
              <li class="breadcrumb-item"><a href="{m['hub_html']}">{m['label']}</a></li>
              <li class="breadcrumb-item active" aria-current="page">{page_title_html}</li>
            </ol></nav>"""
    md_path = f"../methodologies/{m['folder']}/{md_file}"
    readme = f"../methodologies/{m['folder']}/README.md"
    body = f"""
          <header class="mb-3 pb-3 border-bottom">
            {breadcrumb}
            <h1 class="font-display h2 fw-bold text-body mb-0">{page_title_html}</h1>
            <p class="text-body-secondary small mt-2 mb-0">{blurb_html} Full prescriptive text: <a href="{md_path}" class="link-success"><code>{md_path.replace('../', '')}</code></a> · package index <a href="{readme}" class="link-success">README.md</a> · overview <a href="../methodologies/{m['overview_md']}" class="link-success">{m['overview_md']}</a>.</p>
          </header>
          <div class="alert alert-light border shadow-sm py-3" role="note">
            <p class="fw-semibold text-body mb-2">Canonical source</p>
            <p class="small text-body-secondary mb-0">This handbook page is a <strong class="text-body">navigational stub</strong>. Tables, agendas, RACI matrices, and anti-patterns live in the Markdown file — keep them in sync when you change process.</p>
          </div>
"""
    return (
        SHELL_HEAD.format(title=esc(title_plain))
        + body
        + SHELL_TAIL.format(
            hub_html=m["hub_html"],
            hub_label=m["label"],
            extra_scripts="",
        )
    )


# Full methodology subchapters are generated by build_methodology_chapters.py (tables + diagrams).
# This script only overwrites paths not listed there (none today). Hand-maintained: Scrum Roles.
try:
    from build_methodology_chapters import BUILDERS as _FULL_METHODOLOGY_PAGES
except ImportError:
    _FULL_METHODOLOGY_PAGES = {}

SKIP_STUB_GENERATOR = frozenset(_FULL_METHODOLOGY_PAGES.keys()) | frozenset(
    {"methodologies-scrum-roles.html"}
)


def main() -> None:
    for m in METHODS:
        for page_id, title_html, md_file, blurb in m["pages"]:
            fn = f"methodologies-{m['slug']}-{page_id}.html"
            if fn in SKIP_STUB_GENERATOR:
                print("Skip (use build_methodology_chapters.py or hand-maintained):", fn)
                continue
            html = page_html(m, page_id, title_html, md_file, blurb)
            with open(fn, "w", encoding="utf-8") as f:
                f.write(html)
            print("Wrote", fn)


if __name__ == "__main__":
    main()
