#!/usr/bin/env python3
"""Rejected Olympic Sports - one-line entry writer.

Writes a single made-up Olympic sport the Olympics rejected to
/output/entry.txt. Fully deterministic: the same line on every run,
no network, no randomness, no clock, no input files. The joke lands
in one read: a dead-serious broadcast event, then the deductions.
"""
import os

LINE = "Competitive Queue Standing: athletes hold a perfectly straight line for four hours while judges deduct points for sighing, shifting weight, or checking the time."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
