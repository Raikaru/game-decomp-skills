---
name: engine-reimplementation-port
description: Plan, implement, or review clean engine reimplementations that run on PC using user-owned original game data. Use when Codex needs to design data loaders, compatibility layers, gameplay systems, renderer/audio/input backends, save conversion, mod support, or release packaging for projects like OpenMW/OpenRCT2-style ports.
---

# Engine Reimplementation Port

## Rules

- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Treat original data files as user-provided inputs, not bundled project content.
- Make compatibility explicit: data formats, scripting semantics, saves, mods, expansions, and known original quirks.
- Prefer tests built from synthetic or user-provided fixtures; do not commit copyrighted fixtures.

## Workflow

1. Define the compatibility target: base game, expansions, patched versions, mods, save files, scripting behavior, and bugs.
2. Inventory original data formats: archives, maps, models, animations, audio, scripts, localization, UI, and saves.
3. Build loaders and validators before recreating large gameplay systems.
4. Implement subsystems behind modern PC services: rendering, audio, input, filesystem, networking, config, logging.
5. Add compatibility tests and golden metadata for formats that can be tested without copyrighted content.
6. Create user-owned asset discovery and first-run diagnostics.
7. Add enhancements without silently changing compatibility mode.

## Implementation Shape

- Organize around `components/`, `systems/`, `formats/`, `platform/`, and `tools/` or the repo's existing equivalent.
- Keep original-format parsing separate from runtime data models.
- Make scripting and save compatibility first-class because content depends on edge cases.

## Reference

Read [playbook.md](references/playbook.md) for compatibility scope, loader strategy, and release-readiness checks.

For broad repo triage or release readiness, also use the `pc-port` skill's `references/repo-triage.md` or `references/checklists.md`.
