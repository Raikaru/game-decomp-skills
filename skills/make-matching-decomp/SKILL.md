---
name: make-matching-decomp
description: Plan, implement, or review matching decompilation projects where exact binary, object, function, or assembly matching is an explicit goal. Use when Codex needs to scaffold a matching decomp repo, define provenance rules, split binaries, create build/linker/diff workflows, analyze compiler/ABI behavior, name symbols, match functions, review nonmatching diffs, or design validation for reverse engineering. If exact compiler output matching is not required, prefer make-functional-decomp; if the task is PC runtime/backends/release packaging, prefer the matching-decomp-port skill.
---

# Make Matching Decomp

## Rules

- Keep ROMs, ISOs, executables, binaries, copyrighted assets, and keys out of outputs.
- Require user-owned input artifacts for extraction, comparison, or build verification.
- Do not scrape collaborative services; use documented APIs or manual user-provided snippets when allowed.
- Keep provenance clean: distinguish observation notes, generated assembly, handwritten source, public documentation, and speculation.
- Do not copy decompiler output verbatim into final source unless the project policy and license/provenance rules allow it.

## Workflow

Use this skill for creating or maintaining the decompilation project itself. For PC runtime backends, platform adapters, user-facing packaging, or port release work, switch to or combine with the `matching-decomp-port` skill.

1. Define the match target.
   - Whole binary, relocatable objects, functions, overlays, libraries, assets, or generated assembly.
   - Exact match, equivalent assembly, equivalent object layout, or staged nonmatching progress.

2. Establish inputs and repo boundaries.
   - Store user-provided binaries outside version control.
   - Put extraction/splitting outputs in ignored directories unless redistribution rights are clear.
   - Document required hashes and accepted versions.

3. Reproduce the original toolchain model.
   - Compiler, assembler, linker, ABI, endianness, object format, optimization flags, section layout, alignment, calling conventions.
   - Linker scripts, symbol maps, splat/split configuration, build graph, and diff tooling.

4. Create the matching loop.
   - Split binary into units.
   - Generate assembly or object baselines.
   - Write or refine source.
   - Build with the target compiler.
   - Diff assembly/object/binary output.
   - Iterate until the chosen match threshold passes.

5. Manage symbols and types.
   - Prefer public symbols with source/license recorded, user-owned artifact observations, debug strings, logs, public docs, behavior, and internal consistency.
   - Reject unclear symbol packs or names whose provenance cannot be documented.
   - Track confidence for speculative names and types.
   - Keep type changes localized until object layout is verified.

6. Review and validate.
   - Run match checks before behavior refactors.
   - Keep nonmatching progress visible by unit.
   - Review provenance, generated files, ignored outputs, and build reproducibility.

## Reference

Read [playbook.md](references/playbook.md) before scaffolding a repo, reviewing an existing matching project, changing build/diff tooling, making provenance decisions, or working through difficult nonmatching diffs. For short conceptual answers, keep the playbook unloaded unless details are needed.

Use `assets/matching-decomp-template/` when scaffolding a new project.

Run `scripts/check_decomp_hygiene.py`, `scripts/check_private_artifacts.py`, and `scripts/check_provenance_docs.py` when auditing or before delivery.

Read `references/review-matching.md` for PR/code review tasks. Read `references/examples.md` for realistic task shapes. Read platform/tool references only when that ecosystem or tool is relevant.
