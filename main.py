#!/usr/bin/env python3
import os

LINE = "I spent 3 hours 'researching' a bug, then fixed it by deleting the code I wrote proudly that morning."


def validate(line):
    # Self-validation: single line, non-blank, 1-200 characters.
    if not line.strip():
        raise SystemExit("invalid entry line: blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("invalid entry line: must be a single line")
    if not (1 <= len(line) <= 200):
        raise SystemExit("invalid entry line: length out of range")


def main():
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
