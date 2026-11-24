#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes a single line of an out-of-office auto-reply to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not whitespace only.
"""

import os

ENTRY = (
    "I'm out of office until Monday. I've read your email in spirit and "
    "chosen, spiritually, to ignore it until then."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-140")
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
