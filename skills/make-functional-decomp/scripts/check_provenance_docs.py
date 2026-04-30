#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED_TERMS = [
    "allowed",
    "confidence",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check provenance documentation.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    doc = root / "docs" / "provenance.md"
    if not doc.exists():
        print("FAIL: missing docs/provenance.md")
        return 1

    text = doc.read_text(encoding="utf-8", errors="ignore").lower()
    missing = [term for term in REQUIRED_TERMS if term not in text]
    if missing:
        for term in missing:
            print(f"FAIL: provenance doc missing concept: {term}")
        return 1
    print("OK: provenance doc includes required concepts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
