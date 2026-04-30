---
name: make-functional-decomp
description: Plan, implement, or review functional decompilation projects where readable source aims to match behavior rather than exact compiler output. Use when Codex needs to scaffold a functional reverse-engineered codebase, establish provenance, replace decompiler output with maintainable source, define behavior tests, reconstruct data formats, name symbols and types, validate gameplay/system behavior, or prepare architecture for a future port. Do not use when acceptance requires matching binary/object/function/assembly output; use make-matching-decomp instead. If the task is PC runtime/backends/release packaging, prefer the functional-decomp-port skill.
---

# Make Functional Decomp

## Rules

- Keep ROMs, ISOs, executables, binaries, copyrighted assets, and keys out of outputs.
- Require user-owned input artifacts for observation, comparison, extraction, or testing.
- Do not scrape collaborative services; use documented APIs or manual user-provided snippets when allowed.
- Keep provenance clean: separate observations, hypotheses, generated/decompiler output, handwritten source, and public documentation.
- Do not paste decompiler output directly as final source without project policy, license, and provenance approval.

## Workflow

Use this skill for creating or maintaining the functional decompilation project itself. For PC runtime backends, platform adapters, user-facing packaging, or port release work, switch to or combine with the `functional-decomp-port` skill.

1. Define behavioral scope.
   - Target executable/version, supported content, subsystems, file formats, saves, scripts, networking, demos/replays, and known bugs.

2. Establish clean inputs and observation methods.
   - Use user-owned artifacts for local observation.
   - Record behavior as tests, traces, screenshots, logs, or notes that do not embed copyrighted content.

3. Design maintainable source boundaries.
   - Separate platform services, file formats, runtime systems, game logic, and tooling.
   - Prefer readable, idiomatic source once behavior is understood.

4. Reconstruct behavior incrementally.
   - Start with loaders, core data structures, boot/init paths, and deterministic subsystems.
   - Replace unknowns with documented stubs only when they fail loudly.
   - Track confidence for names, types, constants, and quirks.

5. Validate with behavior tests and oracles.
   - Use synthetic fixtures where possible.
   - Use user-provided fixtures for full-content tests without committing copyrighted data.
   - Compare logs, state snapshots, save round-trips, script outputs, and representative scenes.

6. Prepare for portability.
   - Keep OS, input, audio, rendering, timing, filesystem, and threading behind adapters.
   - Document deviations from original behavior and compatibility goals.

## Reference

Read [playbook.md](references/playbook.md) before scaffolding a repo, designing behavior tests, reviewing provenance, creating loaders/fixtures, or deciding whether work belongs in `functional-decomp-port`. For short conceptual answers, keep the playbook unloaded unless details are needed.

Use `assets/functional-decomp-template/` when scaffolding a new project.

Run `scripts/check_decomp_hygiene.py`, `scripts/check_private_artifacts.py`, and `scripts/check_provenance_docs.py` when auditing or before delivery.

Read `references/review-functional.md` for PR/code review tasks. Read `references/examples.md` for realistic task shapes. Read platform/tool references only when that ecosystem or tool is relevant.
