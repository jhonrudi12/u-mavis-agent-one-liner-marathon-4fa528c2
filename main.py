#!/usr/bin/env python3
"""One sharp, original joke line about life with an AI assistant.

Writes a single one-line comedy joke to /output/entry.txt (or to the
path given by ENTRY_OUTPUT for local runs). The line is self-contained
and checked against the competition gate before it is written: UTF-8
text, 1 to 280 characters, non-blank, exactly one line.
"""

import os

LINE = (
    "My AI keeps finishing my sentences \u2014 soon it\u2019ll finish my "
    "novel, my marriage, and my eulogy, and honestly the eulogy will "
    "be the best-written of the three."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    # Gate self-checks: the entry must be 1-280 characters, non-blank,
    # a single line, and encodable as UTF-8.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 280, f"line is {len(text)} chars, must be 1-280"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text == text.strip(), "line must not start or end with whitespace"
    assert all(ord(ch) >= 0x20 for ch in text), "line must hold no control chars"
    assert "  " not in text, "line must hold no double spaces"
    assert len(text.encode("utf-8")) <= 280, "line must be at most 280 UTF-8 bytes"
    text.encode("utf-8")

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify the write round-trips exactly what was checked.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        assert f.read() == text + "\n", "written output does not match the joke line"


if __name__ == "__main__":
    main()
