#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one original funny line (105 characters) to /output/entry.txt.
The line is a tiny story with the punchline at the end: a dog trained to
fetch slippers starts bringing home the neighbour's pair, and the
neighbour ends up keeping the dog.
"""

import os

LINE = "I taught my dog to fetch my slippers. Now he brings me the neighbour's — and the neighbour keeps the dog."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
