#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

ENTRY = (
    "My smart speaker heard me say I was lonely, so now it keeps "
    "offering me a support line for my feelings."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
