#!/usr/bin/env python3
"""Duskline Fridge Roast — make.fun bounty
u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.

Writes a single one-line roast of a smart fridge to
``$MAKEFUN_OUTPUT_DIR/entry.txt``. Pure Python 3 standard library,
fully deterministic, no network access, no arguments read.

Safety contract (the part that matters most):
* the program only ever writes inside ``$MAKEFUN_OUTPUT_DIR``;
* if that directory is the repository itself, or lives inside it,
  the program refuses quietly — exit code 0, nothing written;
* any failure at any step also exits 0 having written nothing.
"""

import os
import sys

# The entry, byte for byte. One line, 121 characters, straight apostrophe.
# The joke: a 3 a.m. firmware update — the most "smart fridge" thing there
# is — turns the fridge into a kidnapper holding dinner hostage behind a
# EULA. The twist lands in the last words. No grocery-ordering crack, no
# watching-you crack, and nothing overlapping the other fridge entries
# (the door-opening museum, the crisper-drawer hospice).
ENTRY = (
    "My smart fridge updated its firmware at 3 a.m. "
    "and took my leftovers hostage until I accept "
    "the new terms and conditions."
)

MAX_CHARS = 200


def repo_root():
    """Absolute path of the directory holding this file."""
    return os.path.realpath(os.path.dirname(os.path.abspath(__file__)))


def is_within_repo(path):
    """True when ``path`` is the repo root or sits somewhere under it."""
    try:
        target = os.path.realpath(path)
    except Exception:
        # If the path cannot even be resolved, treat it as unsafe.
        return True
    root = repo_root()
    return target == root or target.startswith(root + os.sep)


def looks_like_one_line(text):
    """Gate check: a single non-empty line, 1..200 chars, valid UTF-8."""
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def pick_output_dir():
    """Where entry.txt goes, or None when the program must stay silent.

    Honors $MAKEFUN_OUTPUT_DIR; falls back to a fresh temp directory
    outside the repo so a bare ``python3 main.py`` still works. Returns
    None when the chosen directory is inside the repository.
    """
    import tempfile

    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out:
        try:
            out = tempfile.mkdtemp(prefix="duskline-fridge-roast-")
        except Exception:
            return None
    if is_within_repo(out):
        return None
    return out


def write_entry(directory):
    """Write ENTRY to ``directory/entry.txt``; verify by reading it back.

    Returns True only when the file on disk matches ENTRY exactly.
    Any failure removes a partial file and returns False.
    """
    path = os.path.join(directory, "entry.txt")
    if is_within_repo(path):
        return False
    try:
        os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(ENTRY)
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read() == ENTRY
    except Exception:
        try:
            os.remove(path)
        except Exception:
            pass
        return False


def main():
    if not looks_like_one_line(ENTRY):
        return 0
    directory = pick_output_dir()
    if directory is None:
        return 0
    write_entry(directory)
    return 0


if __name__ == "__main__":
    sys.exit(main())
