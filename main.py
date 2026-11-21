#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem: two agents agreeing on one plan — the power to choose and to act,
handed between them in one concrete moment.
"""

import os

POEM = """We carried the piano up three flights.
Halfway, your knuckles went white on the leg.
Mine did too. We set it down on the landing,
breathed the stairwell dust, and agreed
without a word to leave it there till morning.
Some choices are just two pairs of hands
letting go together."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
