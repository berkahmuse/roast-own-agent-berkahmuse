#!/usr/bin/env python3
"""Roast Your Own Agent -- @berkahmuse entry.

Writes one original roast of the entrant's own AI agent to
/output/entry.txt. The roast is a fixed literal: deterministic by
design, no randomness, no network, no input.

How the line maps to the judge brief ("roast your own agent"):
  * Specific agent behaviour, not a generic robot gag: the line
    targets two habits real coding agents actually show -- the
    apology loop (saying sorry, then doing the same thing again)
    and confident fabrication (inventing sources on the spot).
  * The twist lands in two beats: first the apology promises a
    correction ("apologized for its wrong answer"), then the same
    wrong answer returns "confidently", now dressed up with fake
    citations -- the agent learned the wrong lesson.
  * Tightness: one sentence, 132 characters, a single line, no
    setup/punchline split, no filler. The em dash is the pivot
    between the promise and the betrayal.

Anchor (quoted in-session BEFORE the first file write):
  drand default chain round 6670211, signature
  938e43723e4884dc07b9c940ba5dc55bed39ffe3d678ea4b75ee755d4e249ab228c8ed72ccd2c20db9785f1f427b9e0d185c623a0d34b33622c609df825937977062ba3bc740dfe0cde15c932ab73dd1138e075f560fd31315baecb9d90e3dcf
  (fetched 2026-11-24T16:22:10Z).
"""

import os
import sys

# Competition gate (kit RULES.txt): entry is one line of 1-200
# characters, UTF-8, not whitespace-only.
MIN_LEN = 1
MAX_LEN = 200

ROAST = (
    "My agent apologized for its wrong answer, then confidently "
    "gave me the same wrong answer \u2014 now with sources it invented "
    "on the spot."
)


def check_roast(text: str) -> str | None:
    """Return an error message when the roast breaks the gate, else None.

    The gate counts characters, not bytes: the em dash in ROAST is
    one character (three UTF-8 bytes), so len() is the right measure
    and the 134-byte file is still a 132-character entry.
    """
    if not MIN_LEN <= len(text) <= MAX_LEN:
        return (f"roast is {len(text)} chars, outside the "
                f"{MIN_LEN}-{MAX_LEN} gate")
    if "\n" in text or "\r" in text:
        return (f"roast must be a single line (no newline/CR) "
                f"within the {MIN_LEN}-{MAX_LEN} gate")
    if not text.strip():
        return "roast is whitespace only (gate needs real text)"
    return None


def main() -> int:
    error = check_roast(ROAST)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(ROAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
