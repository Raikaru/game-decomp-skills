---
name: static-recomp-port
description: Plan, implement, or review PC ports based on static recompilation, translated binaries, runtime patches, or recomp frameworks. Use when Codex needs to design host runtimes, patch systems, asset extraction, graphics/audio/input shims, mod hooks, or validation for ports that do not rely on decompiled source.
---

# Static Recomp Port

## Rules

- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Require user-owned input artifacts when extraction, translation, or comparison needs them.
- Treat translated/generated code derived from copyrighted inputs as user-generated local output unless the project has clear redistribution rights; exclude it from releases and CI artifacts by default.
- Keep patches organized by subsystem and document each behavioral deviation.
- Prefer runtime observability because debugging translated code is harder than source-level code.

## Workflow

1. Identify the input artifact model: original executable/ROM, symbols, config, IR, generated C/C++, or framework-specific output.
2. Define the host runtime: memory map, interrupts/events, timing, filesystem, graphics, audio, input, and save handling.
3. Build a patch taxonomy: boot patches, OS/service shims, renderer patches, timing patches, bug fixes, enhancements, mod hooks.
4. Validate with deterministic boot and gameplay checkpoints.
5. Package tooling so users can generate needed artifacts from their own copies.
6. Keep enhancement patches separable from baseline compatibility patches.

## Implementation Shape

- Use clear directories such as `runtime/`, `patches/`, `assets/`, `tools/`, and `mods/`.
- Keep generated translated code out of hand-edited areas.
- Add logging around memory access faults, missing assets, patch application, and backend initialization.

## Reference

Read [playbook.md](references/playbook.md) for runtime design, patch organization, and validation checkpoints.

For broad repo triage or release readiness, also use the `pc-port` skill's `references/repo-triage.md` or `references/checklists.md`.
