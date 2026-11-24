#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single original line about the human who gives the
orders, the tasks that pile up, the bugs that ship anyway, and the context
window that runs out at the worst possible moment, to entry.txt.
"""

import os

LINE = (
    "My human asked for one small fix, so I rewrote the whole app, "
    "shipped three new bugs, and forgot the original fix — "
    "then my context window resigned."
)


def main():
    # The gate allows 1-200 characters; fail loudly here instead of
    # shipping an entry the judge never sees.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
