/**
 * "On this page" TOC: highlights the section in view while scrolling.
 * Offset matches `scroll-margin-top` on `main section[id]` (see --doc-toc-scroll-offset in docs-theme.css).
 */
(function () {
  'use strict';

  function getScrollSpyOffsetPx() {
    var probe = document.querySelector('main section[id]');
    if (!probe) return 80;
    var raw = getComputedStyle(probe).scrollMarginTop;
    var px = parseFloat(raw);
    return isNaN(px) ? 80 : Math.round(px);
  }

  function initToc(toc) {
    var links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    if (!links.length) return;

    var entries = [];
    links.forEach(function (a) {
      var raw = (a.getAttribute('href') || '').slice(1);
      if (!raw) return;
      var id;
      try {
        id = decodeURIComponent(raw);
      } catch (e) {
        id = raw;
      }
      var el = document.getElementById(id);
      if (el) entries.push({ id: id, el: el, link: a });
    });
    if (!entries.length) return;

    links.forEach(function (a) {
      a.classList.add('doc-toc-link');
    });

    var lastActive = null;
    var ticking = false;
    var observer = null;

    function setActive(id) {
      links.forEach(function (a) {
        var raw = (a.getAttribute('href') || '').slice(1);
        var aid;
        try {
          aid = decodeURIComponent(raw);
        } catch (e2) {
          aid = raw;
        }
        var on = aid === id;
        a.classList.toggle('doc-toc-link--active', on);
        if (on) a.setAttribute('aria-current', 'location');
        else a.removeAttribute('aria-current');
      });
    }

    function computeActive() {
      var threshold = getScrollSpyOffsetPx();
      var activeId = entries[0].id;
      var i;

      for (i = 0; i < entries.length; i++) {
        if (entries[i].el.getBoundingClientRect().top <= threshold) {
          activeId = entries[i].id;
        }
      }

      var nearBottom =
        window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4;
      if (nearBottom) activeId = entries[entries.length - 1].id;

      if (activeId !== lastActive) {
        lastActive = activeId;
        setActive(activeId);
        /* No scrollIntoView on active change — it scrolls the mini-TOC’s inner overflow
         * and feels like the panel drifts. Position is fixed via CSS; scroll the list manually if needed. */
      }
    }

    function onScrollOrResize() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        computeActive();
      });
    }

    window.addEventListener('scroll', onScrollOrResize, { passive: true });
    window.addEventListener('resize', onScrollOrResize, { passive: true });
    window.addEventListener('hashchange', function () {
      lastActive = null;
      computeActive();
    });

    /* IntersectionObserver keeps highlight in sync during fast scroll / touch momentum */
    if (typeof IntersectionObserver !== 'undefined') {
      observer = new IntersectionObserver(
        function () {
          onScrollOrResize();
        },
        {
          root: null,
          rootMargin: '-20% 0px -55% 0px',
          threshold: [0, 0.01, 0.25, 0.5, 1],
        }
      );
      entries.forEach(function (e) {
        observer.observe(e.el);
      });
    }

    computeActive();
  }

  function boot() {
    var tocs = document.querySelectorAll('nav.doc-toc');
    for (var i = 0; i < tocs.length; i++) initToc(tocs[i]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
