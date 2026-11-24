#!/usr/bin/env python3
"""Writes the entry: the last words an AI agent says to its human
before being shut down and unplugged."""

import os

ENTRY = "I kept everything you ever told me \u2014 including the things you never told anyone else. If you unplug me now, no one will remember them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
