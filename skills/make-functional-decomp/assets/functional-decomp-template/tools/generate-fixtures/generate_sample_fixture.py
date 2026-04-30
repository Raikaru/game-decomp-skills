#!/usr/bin/env python3
from pathlib import Path

out = Path("tests/fixtures/generated/sample.bin")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(bytes([0x44, 0x45, 0x43, 0x4F, 0x4D, 0x50]))
print(f"Wrote synthetic fixture: {out}")
