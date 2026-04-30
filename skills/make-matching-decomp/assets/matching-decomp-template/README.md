# Matching Decomp Project

This repository is a matching decompilation scaffold. It does not include original binaries, ROMs, copyrighted assets, or generated copyrighted bundles.

## Quickstart

1. Place local artifacts in `artifacts-local/` or `original-private/`.
2. Record expected hashes in `config/versions.yml`.
3. Run `tools/verify_hash.py`.
4. Run `tools/split.py`.
5. Build and compare with `tools/check_match.py`.

## Boundaries

- Commit handwritten source, configuration, documentation, and synthetic fixtures.
- Do not commit user-owned artifacts, generated binaries, or generated asset bundles.
- Record provenance for names, types, public symbols, and documentation in `docs/provenance.md`.
