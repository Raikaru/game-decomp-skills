#!/usr/bin/env python3
import argparse
from pathlib import Path

BLOCKED_SUFFIXES = {
    ".z64", ".n64", ".v64", ".iso", ".gcm", ".dol", ".exe", ".bin",
    ".elf", ".rom", ".wad", ".pak", ".gdi", ".cue", ".ccd", ".img",
    ".sav", ".otr",
}

ALLOWED_DIR_PARTS = {
    "userdata",
    "original-private",
    "assets-private",
    "fixtures-private",
    "generated",
    "traces-local",
    "build",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Find private artifacts in unsafe paths.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    problems: list[str] = []

    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in BLOCKED_SUFFIXES:
            continue
        rel = path.relative_to(root)
        if not any(part in ALLOWED_DIR_PARTS for part in rel.parts):
            problems.append(str(rel))

    if problems:
        for rel in problems:
            print(f"FAIL: artifact-like file outside private/generated dirs: {rel}")
        return 1
    print("OK: no artifact-like files found outside private/generated dirs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
