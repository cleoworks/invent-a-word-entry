#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one coined word plus its one-line definition (95 characters)
to /output/entry.txt. Deterministic: the same bytes on every run.
No network, no input, no randomness.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The coined word, then its one-line definition; joined with an em dash.
WORD = "likelapse"
DEFINITION = "accidentally liking a photo from three years ago while scrolling someone's profile."

ENTRY = f"{WORD} — {DEFINITION}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
