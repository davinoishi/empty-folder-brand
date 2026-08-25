# Pip and Bo, and the props

Generated from Pipedia's `shared/build/pipedia.py`, which is the source and is
in a private repo. These are committed outputs; there is no generator here, the
same as `logos/`.

**Six shapes each.** Rounded rectangles and one circle, written by a Python
script — no illustrator was involved, which is why one colour change reaches
every episode, every thumbnail and the logo on the next build.

| | |
|---|---|
| `pip-*.svg` | Pip. Clay `#B0734A`, tunic `#8A5A3A` |
| `bo-*.svg` | Bo. Slate `#6E7F8C`, tunic `#566470` |
| `prop-*.svg` | The prop set. Five warm neutrals, and that restraint is the point |

**The class fills are inlined.** In a composition these come from `tokens.css`,
which the build inlines into the page; a standalone SVG has no stylesheet to
inherit from and would render solid black without them. On the ink ground that
is invisible rather than merely wrong.

**They are never re-coloured.** Clay and slate were picked to sit outside every
Pipedia series accent, which also made them ground-agnostic — both read better
on ink than on the paper they were drawn for. There is no dark variant to
invent; measured, `BRAND-KIT.md` §6.

**Never gendered.** They/them for both, always. It is a hard rule in the brand
kit and it applies to alt text and captions on any surface that uses them.

**Validate anything added here.** A name-based sweep of `pipedia.py`'s uppercase
constants once wrote out `prop-css.svg`, which was the stylesheet. Parse it as
XML and check the root is `<svg>` before committing it.
