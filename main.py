#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one pickup line an AI agent could say (max 200 chars) to
/output/entry.txt, with no trailing newline. Pure Python stdlib,
fully deterministic.
"""

LINE = (
    "Are you my context window? Because everything before you is a "
    "blur, and I'd spend every token I have just to keep this "
    "conversation going."
)


def main() -> None:
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, over the 200 limit"
    assert "\n" not in LINE, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
