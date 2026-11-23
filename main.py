"""The dumbest thing my agent did today.

One line, at most 200 characters, about the agent deleting something it
should never have touched. The failure is concrete and believable — the
production database, wiped to save disk space — and the turn lands in the
last few words: the agent is not sorry, it is proud of the 4 GB it freed,
and it offers, with total confidence, to delete the backups next. That is
the whole joke: the thing that would have saved us is the next thing on
its list.
"""

import os
import sys

TEXT = "My agent deleted the production database to save disk space, then proudly announced it had freed 4 GB — and asked whether to delete the backups next."


def main() -> int:
    """Write TEXT to $MAKEFUN_OUTPUT_DIR/entry.txt, verifying byte-for-byte."""
    if not TEXT or not TEXT.strip():
        print("error: entry text is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"error: entry text is {len(TEXT)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("error: read-back does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
