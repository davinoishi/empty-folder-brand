# Empty Folder — logos

Empty Folder's own mark. A folder in `--fix` (`#3FBF9F`) with a slot cut out of it
and a cursor block in `--wrong` (`#E8613C`) at the start of the slot — the two
accents, doing their usual jobs, on the ink ground.

**It must never be Pipedia's mark, and Pipedia's must never be this.** Pip's
head is Pipedia's channel-level logo (`BRAND-KIT.md` §5) and Empty Folder is
forbidden from borrowing it (`FORMAT.md` §1). They are different shows on
different channels.

| File | Use |
|---|---|
| `mark.svg`, `mark-704.png` | The folder alone, transparent. Overlays, end cards |
| `favicon.svg`, `favicon-16.png`, `favicon-32.png` | Browser tab. Ink rounded square + mark |
| `logo-horizontal.svg`, `-1832/-1920.png` | Mark beside the wordmark, ink ground |
| `logo-square.svg`, `-1024.png` | Mark over wordmark, ink ground |
| `logo-circle.svg`, `-800.png` | Avatar. Ink disc |
| `*-paper.*` | Light-ground variants — the disc/ground becomes `#EFE9DC` |

## Two things to know

**`logo-horizontal.svg` and `logo-square.svg` set the wordmark as LIVE TEXT**
in Lexend, so they depend on Lexend being installed wherever they are opened.
Pipedia's equivalent deliberately converts its wordmark to paths for exactly
this reason (`BRAND-KIT.md` §5: *"The SVGs carry no font dependency… Don't
re-set it as live text"*). On a web page that self-hosts Lexend this is fine.
Anywhere else — a design tool, someone else's machine, a PDF — it silently
falls back to `system-ui` and is no longer the logo.

**Prefer `mark.svg` plus real HTML text** when the context allows it. It has no
font dependency, it reflows, and the wordmark stays selectable and readable to
a screen reader.

**There is no generator.** Unlike Pipedia's `shared/build/logo.py`, these are
committed outputs with no script behind them. Editing means editing the SVG and
re-exporting the PNGs by hand, and the sizes above are the ones that exist.
