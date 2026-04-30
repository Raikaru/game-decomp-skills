---
name: matching-decomp-port
description: Plan, implement, or review native PC ports from matching decompilation projects where source rebuilds the original binary or objects. Use when Codex needs to preserve matchability while adding PC platform backends, asset extraction, build targets, input/audio/render adapters, or optional enhancements.
---

# Matching Decomp Port

## Rules

- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Require user-owned inputs for extraction or comparison.
- Do not break original matching targets unless the user explicitly accepts a nonmatching fork.
- Prefer additive PC-only files, compile flags, and narrow adapters over broad edits to matched game logic.
- Treat enhancement work as optional layers that can be disabled for regression testing.

## Workflow

1. Identify match boundaries: matched source files, generated assets, linker scripts, compiler versions, build targets, and nonmatching areas.
2. Add a PC target beside original targets, not in place of them.
3. Create platform adapters for windowing, input, audio, filesystem, time, and graphics.
4. Preserve original behavior paths first: boot, title, menus, one representative gameplay path, save/load.
5. Add enhancement flags only after baseline behavior works.
6. Document user-owned asset extraction and keep generated bundles ignored by default.

## Implementation Shape

- Put host code under `src/platform_pc/`, `platform/pc/`, `port/pc/`, or the repo's equivalent.
- Isolate backend choices behind existing engine APIs where possible.
- Keep PC-specific `#ifdef`s at the platform boundary; avoid scattering them through game logic.
- Add CI for PC build and original matching build if the project supports both.

## Reference

Read [playbook.md](references/playbook.md) for milestone details, risk checks, and PR review prompts.

For broad repo triage or release readiness, also use the `pc-port` skill's `references/repo-triage.md` or `references/checklists.md`.
