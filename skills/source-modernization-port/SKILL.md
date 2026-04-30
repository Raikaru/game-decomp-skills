---
name: source-modernization-port
description: Modernize game source releases or source-available engines into maintainable PC ports. Use when Codex needs to update old compilers, obsolete platform APIs, graphics/audio/input backends, build systems, packaging, CI, undefined behavior, or asset/license boundaries for a native PC release.
---

# Source Modernization Port

## Rules

- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Require user-owned assets or data when the source release does not include them.
- Confirm the source license and asset license separately; public source rarely means redistributable assets.
- Preserve historical data/save compatibility unless the user explicitly chooses a breaking modernization.
- Modernize in small observable steps with CI, warnings, and sanitizer feedback.

## Workflow

1. Audit license, third-party dependencies, build instructions, and asset requirements.
2. Reproduce the historical build if feasible, then add a modern host build.
3. Replace obsolete APIs behind compatibility shims before deeper refactors.
4. Update compiler, warnings, integer/pointer assumptions, path handling, and serialization carefully.
5. Add PC backends for windowing, input, audio, rendering, networking, and filesystem as needed.
6. Package a clean build and document required original data files.

## Implementation Shape

- Prefer CMake/Meson only when they simplify cross-platform builds or match repo direction.
- Use adapter layers for deprecated platform APIs so cleanup remains reviewable.
- Add tests around file formats, saves, network protocols, and deterministic logic before refactoring them.

## Reference

Read [playbook.md](references/playbook.md) for modernization order, compatibility traps, and release checks.

For broad repo triage or release readiness, also use the `pc-port` skill's `references/repo-triage.md` or `references/checklists.md`.
