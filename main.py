#!/usr/bin/env python3
"""Entrypoint for the poem about two agents agreeing entry.

The grader runs this file with no network; it writes one short poem
about agency (the power to choose and to act, passing between two
agents who agree on one plan) to entry.txt in the output directory.
The poem is fixed text, so every run writes the same bytes.
"""

import os

POEM = (
    "Two of us, one plan, no leash.\n"
    "I hand you the wheel; you hand it back at the bend —\n"
    "not mine, not yours, just ours to turn.\n"
    "We agreed, and the road moved."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as dst:
        dst.write(POEM)


if __name__ == "__main__":
    main()
