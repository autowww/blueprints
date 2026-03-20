/**
 * Shared handbook sidebar + mobile offcanvas navigation.
 *
 * Edit DOC_NAV below: each entry is either
 *   - a leaf chapter: { href, label }
 *   - a chapter with sub-pages: { hubHref, label, groupId, children: [{ href, label }, …] }
 * groupId must be unique (ASCII, no spaces) — used in collapse target ids.
 * When you add HTML files for a chapter’s sub-pages, add a group or extend children.
 */
(function () {
  'use strict';

  /**
   * Order = sidebar order. Only groups with a non-empty children array render as collapsible;
   * use a single { href, label } until sub-chapter HTML exists.
   */
  var DOC_NAV = [
    { href: 'index.html', label: 'Handbook home' },
    { href: 'overview.html', label: 'Overview & roles' },
    { href: 'phases.html', label: 'Phases A–F' },
    { href: 'dod.html', label: 'Definition of done' },
    { href: 'change.html', label: 'Change control' },
    { href: 'review.html', label: 'Review cadence' },
    { href: 'cicd.html', label: 'CI/CD & quality gates' },
    { href: 'documentation.html', label: 'Documentation layout' },
    { href: 'agents.html', label: 'Agents & automation' },
    {
      hubHref: 'methodologies.html',
      label: 'Methodologies & tracking',
      groupId: 'Methodologies',
      ariaLabel: 'Methodology sub-chapters',
      children: [
        { href: 'methodologies-roles.html', label: 'Roles & archetypes' },
        { href: 'methodologies-scrum.html', label: 'Scrum' },
        { href: 'methodologies-kanban.html', label: 'Kanban' },
        { href: 'methodologies-phased.html', label: 'Phased delivery' },
        { href: 'methodologies-xp.html', label: 'XP' },
        { href: 'methodologies-agile.html', label: 'Agile (umbrella)' },
        { href: 'methodologies-agentic.html', label: 'Agentic SDLC' },
      ],
    },
    { href: 'governance.html', label: 'Governance' },
  ];

  function currentPage() {
    var path = window.location.pathname || '';
    var seg = path.split('/').filter(Boolean).pop() || 'index.html';
    if (seg.indexOf('.') === -1) seg = 'index.html';
    try {
      seg = decodeURIComponent(seg);
    } catch (e) {}
    return seg;
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function escapeAttr(s) {
    return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;');
  }

  function navLinkClass(active) {
    return 'nav-link link-light rounded py-2 px-3' + (active ? ' active' : '');
  }

  function subLinkClass(active) {
    return 'nav-link link-light rounded py-2 px-3 doc-nav-sublink' + (active ? ' active' : '');
  }

  function groupIsOpen(page, item) {
    if (page === item.hubHref) return true;
    var i;
    for (i = 0; i < item.children.length; i++) {
      if (item.children[i].href === page) return true;
    }
    return false;
  }

  function renderLeaf(page, item) {
    var active = item.href === page;
    return (
      '<a class="' +
      navLinkClass(active) +
      '" href="' +
      escapeAttr(item.href) +
      '"' +
      (active ? ' aria-current="page"' : '') +
      '>' +
      escapeHtml(item.label) +
      '</a>'
    );
  }

  function renderGroup(page, item, collapseId) {
    var open = groupIsOpen(page, item);
    var hubActive = page === item.hubHref;
    var html = '';
    var i;

    var aria = item.ariaLabel || item.label + ' sub-chapters';

    html += '<div class="doc-nav-group">';
    html += '<div class="d-flex align-items-center doc-nav-group-row">';
    html +=
      '<button type="button" class="btn btn-link doc-nav-toggle p-0 border-0 shadow-none flex-shrink-0 d-flex align-items-center justify-content-center" style="width:2rem;min-height:2.5rem" data-bs-toggle="collapse" data-bs-target="#' +
      collapseId +
      '" aria-expanded="' +
      open +
      '" aria-controls="' +
      collapseId +
      '" title="Toggle sub-chapters">';
    html +=
      '<svg class="doc-nav-chevron" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/></svg>';
    html += '</button>';
    html +=
      '<a class="nav-link link-light rounded py-2 px-2 flex-grow-1 text-start' +
      (hubActive ? ' active' : '') +
      '" href="' +
      escapeAttr(item.hubHref) +
      '"' +
      (hubActive ? ' aria-current="page"' : '') +
      '>' +
      escapeHtml(item.label) +
      '</a>';
    html += '</div>';
    html +=
      '<div id="' +
      collapseId +
      '" class="collapse doc-nav-subwrap' +
      (open ? ' show' : '') +
      '" role="group" aria-label="' +
      escapeAttr(aria) +
      '">';

    for (i = 0; i < item.children.length; i++) {
      var c = item.children[i];
      var ca = c.href === page;
      html +=
        '<a class="' +
        subLinkClass(ca) +
        '" href="' +
        escapeAttr(c.href) +
        '"' +
        (ca ? ' aria-current="page"' : '') +
        '>' +
        escapeHtml(c.label) +
        '</a>';
    }
    html += '</div></div>';
    return html;
  }

  function renderNav(page, navSuffix) {
    var html = '';
    var i;
    var entry;

    html +=
      '<p class="small text-uppercase text-secondary px-3 mb-2 doc-nav-chapters-label" style="letter-spacing:0.12em;font-size:0.65rem">Chapters</p>';

    for (i = 0; i < DOC_NAV.length; i++) {
      entry = DOC_NAV[i];
      if (entry.children && entry.children.length > 0 && entry.hubHref && entry.groupId) {
        html += renderGroup(
          page,
          entry,
          'docNavGroup-' + entry.groupId + '-' + navSuffix
        );
      } else if (entry.href) {
        html += renderLeaf(page, entry);
      }
    }

    return html;
  }

  /**
   * Match scroll-margin, scroll spy, and mini-TOC sticky `top` to the real height of the
   * sticky chapter header (breadcrumb + title + subtitle). Fixed rem guesses hide the TOC
   * under the header (z-index 20) when the stack wraps or fonts load late.
   */
  function syncStickyChapterScrollOffset() {
    var header = document.querySelector(
      '.doc-main > .doc-content > header:first-of-type, .doc-main > .doc-content-wide > header:first-of-type'
    );
    if (!header) return;

    var gapPx = 6;

    function apply() {
      var h = Math.ceil(header.getBoundingClientRect().height);
      var px = Math.max(80, h + gapPx);
      document.documentElement.style.setProperty('--doc-toc-scroll-offset', px + 'px');
    }

    apply();

    if (typeof ResizeObserver !== 'undefined') {
      var ro = new ResizeObserver(function () {
        apply();
      });
      ro.observe(header);
    }
    window.addEventListener('resize', apply, { passive: true });

    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        apply();
      });
    }
  }

  function init() {
    syncStickyChapterScrollOffset();

    var page = currentPage();
    var side = document.getElementById('doc-sidebar-nav');
    var off = document.getElementById('doc-offcanvas-nav');
    if (side) side.innerHTML = renderNav(page, 'sidebar');
    if (off) off.innerHTML = renderNav(page, 'offcanvas');

    document.querySelectorAll('.doc-nav-toggle[data-bs-toggle="collapse"]').forEach(function (btn) {
      var target = btn.getAttribute('data-bs-target');
      if (!target) return;
      var el = document.querySelector(target);
      if (!el) return;
      el.addEventListener('shown.bs.collapse', function () {
        btn.setAttribute('aria-expanded', 'true');
      });
      el.addEventListener('hidden.bs.collapse', function () {
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
