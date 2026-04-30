#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED_DOCS = [
    "README.md",
    "docs/provenance.md",
    "docs/compatibility.md",
    "docs/behavior-oracles.md",
]

PRIVATE_DIR_HINTS = [
    "userdata",
    "original-private",
    "assets-private",
    "tests/fixtures-private",
    "traces-local",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Check functional decomp repo hygiene.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    problems: list[str] = []

    for rel in REQUIRED_DOCS:
        if not (root / rel).exists():
            problems.append(f"missing required doc: {rel}")

    gitignore = root / ".gitignore"
    if not gitignore.exists():
        problems.append("missing .gitignore")
    else:
        ignore_text = read_text(gitignore)
        for hint in PRIVATE_DIR_HINTS:
            if hint not in ignore_text:
                problems.append(f".gitignore does not mention private/local path: {hint}")

    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("OK: functional decomp hygiene checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
