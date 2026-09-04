"""Regenerate MANIFEST.sha256 — every shipped file, hashed.

    python3 tools/manifest.py            # write
    python3 tools/manifest.py --check    # verify, exit 1 on drift
    python3 tools/manifest.py --force    # write anyway from a dirty tree

Consumers vendor this repo and verify their copy against this manifest. The
manifest is what makes a vendored copy legitimate rather than trusted; see
README, "The contract".
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("tokens", "fonts", "strings", "logos", "characters")
OUT = os.path.join(ROOT, "MANIFEST.sha256")


def entries():
    for d in DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            rel = f"{d}/{name}"
            with open(os.path.join(ROOT, rel), "rb") as fh:
                yield f"{hashlib.sha256(fh.read()).hexdigest()}  {rel}"


def dirty():
    """Tracked files that differ from HEAD.

    THE MANIFEST MUST DESCRIBE WHAT IS COMMITTED, not what happens to be on
    disk. Written from a dirty tree it records a file nobody else can obtain,
    and every consumer's verification then fails against a hash that looks
    authoritative — which is exactly what happened on 2026-09-03: a regenerate
    run picked up an uncommitted logos/README.md, the manifest shipped its
    hash, and Pipedia's check-brand failed on a file it had synced correctly."""
    out = subprocess.run(["git", "diff", "--name-only", "HEAD", "--"] + list(DIRS),
                         cwd=ROOT, capture_output=True, text=True)
    return [f for f in out.stdout.split() if f]


def main():
    d = dirty()
    if d and "--force" not in sys.argv:
        print("refusing to write a manifest from a dirty tree — these differ "
              "from HEAD:")
        for f in d:
            print("   ", f)
        print("Commit them, stash them, or pass --force if you know why.")
        return 1
    body = "\n".join(entries()) + "\n"
    if "--check" in sys.argv:
        have = open(OUT).read() if os.path.exists(OUT) else ""
        if have != body:
            print("MANIFEST.sha256 is stale — run: python3 tools/manifest.py")
            return 1
        print(f"manifest OK — {body.count(chr(10))} files")
        return 0
    with open(OUT, "w") as fh:
        fh.write(body)
    print(f"wrote {OUT} — {body.count(chr(10))} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
