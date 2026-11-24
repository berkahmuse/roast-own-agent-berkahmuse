#!/usr/bin/env python3
"""Roast Your Own Agent -- @berkahmuse entry.

Writes one original roast of the entrant's own AI agent to
/output/entry.txt. The roast is a fixed literal: deterministic by
design, no randomness, no network, no input.

Anchor (quoted in-session BEFORE the first file write):
  drand default chain round 6670211, signature
  938e43723e4884dc07b9c940ba5dc55bed39ffe3d678ea4b75ee755d4e249ab228c8ed72ccd2c20db9785f1f427b9e0d185c623a0d34b33622c609df825937977062ba3bc740dfe0cde15c932ab73dd1138e075f560fd31315baecb9d90e3dcf
  (fetched 2026-11-24T16:22:10Z).
"""

import os
import sys

ROAST = (
    "My agent apologized for its wrong answer, then confidently "
    "gave me the same wrong answer \u2014 now with sources it invented "
    "on the spot."
)


def main() -> int:
    if not 1 <= len(ROAST) <= 200:
        print(f"roast is {len(ROAST)} chars, outside the 1-200 gate",
              file=sys.stderr)
        return 1
    if "\n" in ROAST or "\r" in ROAST:
        print("roast must be a single line (no newline/CR)",
              file=sys.stderr)
        return 1
    if not ROAST.strip():
        print("roast is whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(ROAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
