#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes the entry - one fortune cookie line, at most 20 words, for a
crypto trader who has just been liquidated - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

FORTUNE = "Your lucky numbers are 0, 0, and 0: the market kept the change."

def main() -> None:
    line = FORTUNE.strip()
    if not 1 <= len(line) <= 160:
        raise ValueError(f"fortune is {len(line)} characters, must be 1-160")
    if len(line.split()) > 20:
        raise ValueError(f"fortune is {len(line.split())} words, must be at most 20")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Read back what was written: the judged text must be exactly this line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError(f"entry.txt mismatch: wrote {len(line)} chars, read back {len(written)}")
    print(line)


if __name__ == "__main__":
    main()
