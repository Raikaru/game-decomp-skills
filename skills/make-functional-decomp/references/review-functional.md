# Functional Decomp Review

Prioritize findings in this order.

## P0/P1

- Original binaries, assets, SDK files, or private fixtures are committed.
- Behavior acceptance criteria are missing for changed subsystems.
- A readable rewrite changes known compatibility behavior without documenting the deviation.
- Notes mix copied implementation details with observations.
- Matching requirements appear in the task, meaning `make-matching-decomp` should be used instead.

## P2

- Tests rely on copyrighted fixtures instead of synthetic or private local fixtures.
- Stubs fail silently or hide missing behavior.
- Save/script/data-format compatibility is undocumented.
- Platform dependencies are scattered through game logic.
- Symbol/type confidence is not tracked.

## P3

- Docs lack first-run instructions for user-owned data.
- Behavior oracles are prose-only where tests are feasible.
- Deviations are documented but not linked to tests.

## Review Output

Lead with concrete findings and file references. Include the affected behavior oracle, missing test, or provenance issue.
