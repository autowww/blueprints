/**
 * PDLC handbook sidebar + mobile offcanvas navigation.
 *
 * Same rendering engine as the SDLC handbook (blueprints/sdlc/docs/assets/docs-nav.js).
 * Edit DOC_NAV below to change chapter order.
 */
(function () {
  'use strict';

  var DOC_NAV = [
    { href: 'index.html', label: 'Handbook home' },
    { href: 'overview.html', label: 'Overview & roles' },
    { href: 'phases.html', label: 'Phases P1\u2013P6' },
    { href: 'bridge.html', label: 'PDLC \u2194 SDLC bridge' },
    { href: 'stage-gates.html', label: 'Stage gates' },
    { href: 'metrics.html', label: 'Metrics framework' },
    {
      hubHref: 'approaches.html',
      label: 'Approaches',
      groupId: 'Approaches',
      ariaLabel: 'Approach sub-chapters',
      children: [
        { href: 'approaches.html', label: 'Overview' },
        { href: 'approach-dual-track.html', label: 'Dual-Track Agile' },
        { href: 'approach-stage-gate.html', label: 'Stage-Gate' },
        { href: 'approach-design-thinking.html', label: 'Design Thinking' },
        { href: 'approach-lean-startup.html', label: 'Lean Startup' },
        { href: 'approach-plm.html', label: 'Product Lifecycle Mgmt' },
        { href: 'approach-ost.html', label: 'Opportunity Solution Trees' },
      ],
    },
  ];

  function currentPage() {
    var path = window.location.pathname || '';
    var seg = path.split('/').filter(Boolean).pop() || 'index.html';
    if (seg.indexOf('.') === -1) seg = 'index.html';
    try { seg = decodeURIComponent(seg); } catch (e) {}
    return seg;
  }

  function escapeHtml(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function escapeAttr(s) {
    return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;');
  }

  function navLinkClass(active) {
    return 'nav-link link-light rounded py-2 px-3' + (active ? ' active' : '');
  }
  function subLinkClass(active) {
    return 'nav-link link-light rounded py-2 px-3 doc-nav-sublink' + (active ? ' active' : '');
  }

  function groupIsOpen(page, item) {
    if (page === item.hubHref) return true;
    for (var i = 0; i < item.children.length; i++) {
      if (item.children[i].href === page) return true;
    }
    return false;
  }

  function renderLeaf(page, item) {
    var active = item.href === page;
    return '<a class="' + navLinkClass(active) + '" href="' + escapeAttr(item.href) + '"' +
      (active ? ' aria-current="page"' : '') + '>' + escapeHtml(item.label) + '</a>';
  }

  function renderGroup(page, item, collapseId) {
    var open = groupIsOpen(page, item);
    var hubActive = page === item.hubHref;
    var html = '<div class="doc-nav-group">';
    html += '<div class="d-flex align-items-center doc-nav-group-row">';
    html += '<button type="button" class="btn btn-link doc-nav-toggle p-0 border-0 shadow-none flex-shrink-0 d-flex align-items-center justify-content-center" style="width:2rem;min-height:2.5rem" data-bs-toggle="collapse" data-bs-target="#' + collapseId + '" aria-expanded="' + open + '" aria-controls="' + collapseId + '" title="Toggle sub-chapters">';
    html += '<svg class="doc-nav-chevron" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/></svg>';
    html += '</button>';
    html += '<a class="nav-link link-light rounded py-2 px-2 flex-grow-1 text-start' + (hubActive ? ' active' : '') + '" href="' + escapeAttr(item.hubHref) + '"' + (hubActive ? ' aria-current="page"' : '') + '>' + escapeHtml(item.label) + '</a>';
    html += '</div>';
    html += '<div id="' + collapseId + '" class="collapse doc-nav-subwrap' + (open ? ' show' : '') + '" role="group" aria-label="' + escapeAttr(item.ariaLabel || item.label) + '">';
    for (var i = 0; i < item.children.length; i++) {
      var c = item.children[i];
      var ca = c.href === page;
      html += '<a class="' + subLinkClass(ca) + '" href="' + escapeAttr(c.href) + '"' + (ca ? ' aria-current="page"' : '') + '>' + escapeHtml(c.label) + '</a>';
    }
    html += '</div></div>';
    return html;
  }

  function renderNav(page, navSuffix) {
    var html = '<p class="small text-uppercase text-secondary px-3 mb-2 doc-nav-chapters-label" style="letter-spacing:0.12em;font-size:0.65rem">Chapters</p>';
    for (var i = 0; i < DOC_NAV.length; i++) {
      var entry = DOC_NAV[i];
      if (entry.children && entry.children.length > 0 && entry.hubHref && entry.groupId) {
        html += renderGroup(page, entry, 'docNavGroup-' + entry.groupId + '-' + navSuffix);
      } else if (entry.href) {
        html += renderLeaf(page, entry);
      }
    }
    return html;
  }

  function syncStickyChapterScrollOffset() {
    var header = document.querySelector('.doc-main > .doc-content > header:first-of-type');
    if (!header) return;
    function apply() {
      var h = Math.ceil(header.getBoundingClientRect().height);
      document.documentElement.style.setProperty('--doc-toc-scroll-offset', Math.max(80, h + 6) + 'px');
    }
    apply();
    if (typeof ResizeObserver !== 'undefined') { new ResizeObserver(apply).observe(header); }
    window.addEventListener('resize', apply, { passive: true });
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(apply); }
  }

  function init() {
    syncStickyChapterScrollOffset();
    var page = currentPage();
    var side = document.getElementById('doc-sidebar-nav');
    var off  = document.getElementById('doc-offcanvas-nav');
    if (side) side.innerHTML = renderNav(page, 'sidebar');
    if (off)  off.innerHTML  = renderNav(page, 'offcanvas');
    document.querySelectorAll('.doc-nav-toggle[data-bs-toggle="collapse"]').forEach(function (btn) {
      var target = btn.getAttribute('data-bs-target');
      if (!target) return;
      var el = document.querySelector(target);
      if (!el) return;
      el.addEventListener('shown.bs.collapse', function () { btn.setAttribute('aria-expanded','true'); });
      el.addEventListener('hidden.bs.collapse', function () { btn.setAttribute('aria-expanded','false'); });
    });
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); }
  else { init(); }
})();
