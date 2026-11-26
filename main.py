#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Weirdest Job Title: Blind Judge Showdown"
(u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922).

Writes one job title to /output/entry.txt.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 60
characters, not only white space. The title below is 59 characters.
"""

import os
import sys

TITLE = "Certified Apologizer for Smoke Detectors Chirping at 3 A.M."


def main() -> int:
    text = TITLE
    if not 1 <= len(text) <= 60:
        print(f"gate fail: title is {len(text)} chars, must be 1-60",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: title is whitespace-only", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not UTF-8-encodable
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
