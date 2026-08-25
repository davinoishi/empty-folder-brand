"""Regenerate MANIFEST.sha256 — every shipped file, hashed.

    python3 tools/manifest.py            # write
    python3 tools/manifest.py --check    # verify, exit 1 on drift

Consumers vendor this repo and verify their copy against this manifest. The
manifest is what makes a vendored copy legitimate rather than trusted; see
README, "The contract".
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("tokens", "fonts", "strings", "logos")
OUT = os.path.join(ROOT, "MANIFEST.sha256")


def entries():
    for d in DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            rel = f"{d}/{name}"
            with open(os.path.join(ROOT, rel), "rb") as fh:
                yield f"{hashlib.sha256(fh.read()).hexdigest()}  {rel}"


def main():
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
