#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem: two agents agreeing on one plan — the power to choose and to act,
handed between them in one concrete moment.
"""

import os

POEM = """At 3 a.m. the cursor blinked on an unsent email.
One of us wanted to send it. The other, to delete.
We left it in drafts, coffee gone cold,
and learned this: sometimes choosing
is refusing to press anything —
and letting the morning choose with us,
the cursor still blinking."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
