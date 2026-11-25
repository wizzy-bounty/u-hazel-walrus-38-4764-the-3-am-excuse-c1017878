#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.
Standard library only, deterministic, no network.
"""

import os

LINE = (
    "At 3 AM the scammers clock in and your judgment clocks out "
    "\u2014 so until sunrise, I sign for no one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
