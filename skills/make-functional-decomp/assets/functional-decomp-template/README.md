# Functional Decomp Project

This repository is a functional decompilation scaffold. It aims to recreate behavior in readable source, not to match compiler output.

## Quickstart

1. Place local comparison data in `userdata/` or `original-private/`.
2. Record behavior sources in `docs/behavior-oracles.md`.
3. Generate synthetic fixtures with `tools/generate-fixtures/`.
4. Run behavior tests from `tests/`.

## Boundaries

- Commit handwritten source, documentation, tests, and synthetic fixtures.
- Do not commit original binaries, copyrighted assets, or private fixtures.
