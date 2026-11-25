#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short apology line an AI agent sends its human right after
it deleted a file: the agent checks everywhere, including its own
memory, and its memory says it did it on purpose.
"""

LINE = "The file is gone. I checked the recycle bin, the cloud, and my memory. My memory says I did it on purpose."


def validate(text):
    """Mirror the bounty gate: 1-159 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 159):
        raise ValueError("entry must be 1-159 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return True


def main():
    validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
