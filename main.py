#!/usr/bin/env python3
"""One-line joke excusing a missed deadline.

Writes the single best excuse to /output/entry.txt, using only the
standard library. The line is fixed and deterministic: no randomness,
no network, no input.
"""

import os

EXCUSE = "I was going to submit on time, but my Wi-Fi chose that exact minute to discover itself."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1-200 characters of non-blank UTF-8 text, one line.
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 200 and "\n" not in line
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
