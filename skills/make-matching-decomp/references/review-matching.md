# Matching Decomp Review

Prioritize findings in this order.

## P0/P1

- Original ROMs, binaries, assets, SDK files, or generated copyrighted bundles are committed or emitted by CI.
- Match target, artifact hash, or toolchain is missing or ambiguous.
- A change regresses matching output without documenting the new nonmatching state.
- Symbol/type provenance is unclear for names imported from outside the repo.
- PC-port work is mixed into matching logic in a way that breaks original targets.

## P2

- `.gitignore` misses local artifact/build/generated-output paths.
- Diff/check commands are not repeatable.
- Type changes make one function match while risking shared object layout.
- Nonmatching units lack tracking.
- Tool versions are not pinned or recorded.

## P3

- Docs are stale or missing examples.
- Speculative names lack confidence notes.
- Review logs are hard to reproduce.

## Review Output

Lead with concrete findings and file references. Include the match command, observed regression or risk, and the smallest correction.
