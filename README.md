# Empty Folder — brand

The single source of truth for the design tokens, the fonts and the canonical
strings shared by everything under the **Empty Folder Projects** umbrella.

**This repo is public on purpose.** Two of the three repos that consume it are
private, and a private source cannot be fetched by a static-site build. It is
also consistent with [`making-of`](https://github.com/davinoishi/making-of):
the reasoning behind this work is already published, so the palette it produced
is not the secret.

> All you need is an idea and an empty folder.

## What's in here

```
tokens/pipedia.css        Pipedia's kit — warm paper, Fredoka, series accents
tokens/empty-folder.css   Empty Folder's kit — ink ground, Lexend + mono, two accents
fonts/                    the .woff2 that ship, the .ttf they came from, and the licences
strings/strings.json      taglines, the about line, the compliance line, the synthesis
                          disclosure, the sign-off
strings/copy-rules.json   British English, the conversion table, and what is exempt from it
MANIFEST.sha256           every file above, hashed
```

## Who consumes it

| Repo | Consumes | How |
|---|---|---|
| `Pipedia` (private) | tokens, fonts, strings | vendored at `brand/`, verified against `MANIFEST.sha256` |
| `empty-folder-website` (private) | tokens, fonts, strings | same |

## The contract — vendor and verify, not fetch

Consumers keep a **committed copy** at `brand/` and verify it against
`MANIFEST.sha256`. They do not fetch this repo at build time.

That is deliberate, and it is the same rule the video pipeline already lives
under: **a build must not need the network.** Pipedia's own kit forbids a Google
Fonts URL for exactly this reason — it fails offline and in CI. A brand repo
fetched at render time would reintroduce the failure mode the font rule exists
to prevent, and it would make a video render depend on GitHub being up.

**Why not a submodule.** It would give the same pinning for free. It was
rejected because the consuming repos are worked in `git worktree` checkouts,
and `git worktree add` does not initialise submodules — so the common case
would be a fresh worktree that builds against an empty `brand/` directory. A
vendored copy is present the moment the worktree exists.

**The verification is the point, not the copy.** A copy nothing checks is
`MAKING-OF.md` Act 9 with a new filename: a stylesheet documented as the source
of consistency that nothing imported, agreeing with reality by luck. The hash
check is what makes the copy legitimate. Consumers should run it as a build
gate rather than as a habit.

## Changing a token

1. Change it here. Commit.
2. Regenerate the manifest: `python3 tools/manifest.py`
3. In each consumer: re-run its sync, which rewrites `brand/` and its lock.
4. Run that consumer's checks. For Pipedia that includes `colour_check.py`,
   which recomputes every contrast ratio the token comments claim.

The tokens carry their own reasoning in comments, including the measured
contrast ratios. Changing a value without re-running the check is how the
comments start lying.

## Changing a string is not the same as changing a token

A token is only ever read by a build. **A string may already be sitting in
public** — pasted into a YouTube description, a playlist, an app listing — where
nothing here can reach it. Editing one in this repo changes what the consumers
render and does not change what is already published, so the surfaces this repo
exists to keep identical quietly stop matching.

**So before editing a string, ask where it has already been said.** If the
answer is "twenty-odd published video descriptions", the edit is not a string
change, it is a string change plus a re-paste of every one of them — and the
honest move is usually to add a string rather than rewrite one.

Worked example, 2026-08-28. Pipedia's website panel showed the compliance line
alone, which reads as money-only on a channel that is no longer only about
money. Rewriting `compliance` looked like the fix. It was not: `BRAND-KIT.md`
§13 is LOCKED and that wording covers all ten series deliberately, and the line
was already live on every published description. The actual gap was that the
*about* line — shipped above the compliance line on every video since the money
series — had never been made canonical, so the one surface that could not read
it went without. `shows.pipedia.about` was added; nothing was rewritten;
nothing published had to change.

**`_note` keys are part of the file, not clutter.** `_compliance_note` is what
made that call obvious. A string whose reasoning lives only in a commit message
gets rewritten by the next person who finds it inconvenient.

## Licence

- **Fonts** — SIL Open Font License 1.1, each with its own `OFL-*.txt` in
  `fonts/`. Lexend and Fredoka's copyright lines were read out of the TTF name
  tables rather than typed from memory.
- **Everything else** — MIT, see `LICENSE`.
