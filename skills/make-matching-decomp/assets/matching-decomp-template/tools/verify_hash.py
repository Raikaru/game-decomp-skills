#!/usr/bin/env python3
import hashlib
from pathlib import Path

TARGET = Path("artifacts-local/original.bin")
EXPECTED = "replace-with-expected-sha256"

if not TARGET.exists():
    raise SystemExit(f"Missing local artifact: {TARGET}")

digest = hashlib.sha256(TARGET.read_bytes()).hexdigest()
if EXPECTED.startswith("replace-"):
    raise SystemExit(f"Hash for {TARGET}: {digest}\nUpdate config/versions.yml and this script.")
if digest != EXPECTED:
    raise SystemExit(f"Hash mismatch for {TARGET}: {digest} != {EXPECTED}")
print(f"OK: {TARGET} sha256={digest}")
