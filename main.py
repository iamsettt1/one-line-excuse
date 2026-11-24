#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Writes a single line (at most 160 characters) to /output/entry.txt.
Deterministic: every run writes byte-identical output. Stdlib only.
"""

import os

EXCUSE = (
    "Sorry \u2014 my context window evicted your deadline to fit "
    "the three \u2018quick questions\u2019 you sent right after it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
