#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

One line (under 200 characters): the most creative excuse a hardware
wallet gives for refusing to sign a transaction at 3 AM.
Standard library only, deterministic, no network.
"""

import os

LINE = "At 3 AM the scammers clock in and your judgment clocks out \u2014 so until sunrise, I sign for no one."


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    if not LINE or len(LINE) > 200 or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character single-line gate")
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
