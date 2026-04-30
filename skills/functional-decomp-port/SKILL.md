---
name: functional-decomp-port
description: Plan, implement, or review PC ports from functional decompilation projects where readable source recreates behavior without exact binary matching. Use when Codex needs to stabilize behavior, isolate platform dependencies, choose PC backends, build regression tests, or turn a readable reverse-engineered codebase into a maintainable native port.
---

# Functional Decomp Port

## Rules

- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Require user-owned inputs for extraction, observation, or comparison.
- Prioritize behavioral tests because binary matching is not available as the main oracle.
- Make fidelity decisions explicit: original-accurate, compatibility-focused, or enhanced.

## Workflow

1. Establish the behavior oracle: original executable observations, documented test cases, community bug lists, saves, videos, or scripted repros.
2. Inventory platform assumptions in rendering, audio, input, filesystem, timing, memory layout, and serialization.
3. Stabilize the build with modern compilers, warnings, sanitizers, and deterministic asset paths.
4. Introduce PC backends through narrow service interfaces.
5. Build regression fixtures for core gameplay, saves, scripts, physics, menus, and audio timing.
6. Add enhancements only after a baseline compatibility mode exists.

## Implementation Shape

- Favor tests and instrumentation over match reports.
- Encapsulate "known original quirks" so future cleanup does not erase compatibility.
- Keep data-format loaders strict by default, with compatibility paths for real-world assets.

## Reference

Read [playbook.md](references/playbook.md) for test strategy, compatibility triage, and modernization boundaries.

For broad repo triage or release readiness, also use the `pc-port` skill's `references/repo-triage.md` or `references/checklists.md`.
