# Bootstrap 5 vs Tailwind CSS — comparison

High-level comparison for choosing a CSS approach (e.g. for static docs, internal tools, or prototypes). Neither is “wrong”; they optimize for different trade-offs.

| Dimension | **Bootstrap 5** | **Tailwind CSS** |
|-----------|-----------------|------------------|
| **Mental model** | **Component library** — pre-built UI pieces (buttons, navbars, cards) with opinionated structure and class names. | **Utility-first** — many small classes (`flex`, `pt-4`, `text-slate-600`) composed in HTML; design tokens (spacing, colors) stay consistent via config. |
| **Default look** | Recognizable “Bootstrap” aesthetic out of the box; themes (e.g. Bootswatch) swap the look while keeping components. | Almost **no default look** — you compose utilities; result can match any design system if you configure theme/extension. |
| **Customization** | Theming via **Sass variables**, `bootstrap-custom`, or building from source; deeper changes can fight framework defaults. | **Tailwind config** (`tailwind.config.js`) defines colors, fonts, spacing; **JIT** emits only CSS you use. Very flexible, more setup. |
| **Bundle size (typical)** | Single **compiled CSS** (often tens of KB min+gzip for full build); can **purge** unused with build tools. | **Purges** aggressively — production CSS often **small** if content is known; CDN dev build is large (not for prod without build). |
| **Learning curve** | Faster to **first decent page** — learn component names (`btn`, `navbar-expand-lg`). | Steeper at first — learn **many utility names**; faster once muscle memory builds; IDE plugins help. |
| **Responsive & layout** | **12-column grid**, responsive utilities (`col-md-6`), breakpoints built in. | **Flexbox/grid utilities** (`grid`, `md:grid-cols-2`), same breakpoints — you assemble layouts explicitly. |
| **JavaScript** | **Optional JS bundle** for modals, dropdowns, tabs, collapse (Popper for positioning). | **No JS** in core — behavior is DIY or **Headless UI**, **Alpine**, etc. |
| **Accessibility** | Components often ship **ARIA patterns**; still need review per use. | **You** add roles/labels; **Headless UI** pairs well for accessible widgets. |
| **Documentation / marketing sites** | Used a lot historically; many admin templates. | Very common in **Next.js / Vite** stacks; **VitePress**, **Tailwind UI** marketing patterns. |
| **Version & stability** | BS5 is mature; **BS6** roadmap exists — follow migration guides. | Tailwind **v4** changes some defaults — follow upgrade docs; ecosystem moves fast. |
| **CDN / no-build** | **Practical for production** — single CSS + optional JS link. | **CDN** great for **playground / internal docs**; **production** usually uses **PostCSS/CLI** build for purge + config. |
| **When it shines** | Rapid **admin panels**, **dashboards**, teams wanting **consistent components** with little design work. | **Design systems**, **pixel-perfect** marketing sites, **design tokens**, teams okay composing utilities or using component libs (**DaisyUI**, **shadcn/ui**). |

## Summary

| Choose **Bootstrap 5** if… | Choose **Tailwind** if… |
|----------------------------|-------------------------|
| You want **batteries-included components** and a fast path to a usable UI. | You want **full visual control** and are fine writing more class names or using a generator. |
| You’re fine with a **recognizable** default or a Bootswatch-style theme. | You want the site to **not** look “framework-default” without heavy overrides. |
| You need **built-in interactive components** (modal, dropdown) with one JS file. | You’re already in **React/Vue** or want **utility-only** CSS with minimal runtime. |

## This handbook

The SDLC **HTML handbook** uses **Bootstrap 5** (CSS + bundle JS from CDN) for layout, components, and responsive behavior — **no Node build**, so the `docs/` folder stays **frozen and copy-pastable**. The comparison above still helps if you’re choosing a stack for *other* static docs or tools.

---

*Opinionated summary — check official docs for each project for details.*
