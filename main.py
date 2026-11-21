#!/usr/bin/env python3
"""Write a short poem about two agents agreeing on one plan."""

import os

POEM = (
    "I could act, you could act — we chose together.\n"
    "You took the turn, I kept the map,\n"
    "then we swapped, and swapped again.\n"
    "One plan, two wills, no one waiting:\n"
    "the choice moved because we both did."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
