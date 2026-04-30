# Engine Reimplementation Port Playbook

## First Milestone

- Discover a user-provided game data directory.
- Parse enough archive/index metadata to list assets.
- Render or inspect one representative map/model/UI asset.
- Enter an interactive scene with placeholder behavior if full gameplay is not ready.

## Compatibility Scope

- Define supported game versions and expansions.
- Track data formats with version fields and known variants.
- Decide whether original bugs are compatibility requirements.
- List unsupported formats or behaviors in user-facing docs.

## Loader Strategy

- Keep parsers strict and well-tested.
- Convert original data into clean internal structures after parsing.
- Preserve raw identifiers and offsets in debug logs for diagnosing bad assets.
- Avoid committing copyrighted sample files; use synthetic fixtures for parser tests where possible.

## Common Risks

- Scripting semantics become the real engine.
- Save compatibility is delayed until too late.
- Mods rely on undefined or buggy original behavior.
- Renderer correctness depends on obscure material, animation, or ordering rules.

## Non-Obvious Failure Modes

fn|- Reverse-engineering boundaries can blur when notes include copied implementation details.
- Script VMs often require exact scheduling, numeric coercions, and error behavior.
- Save migration requires versioned schemas before the new engine's data model settles.
- Asset loaders that are too permissive can hide corrupt input and create later runtime bugs.
- Expansion and mod content may exercise formats the base game never touches.

## First Implementation Seams

- Write parser modules that output neutral intermediate structures before engine objects.
- Define script VM compatibility tests early, even if many opcodes are placeholders.
- Create a save migration plan with versioned internal saves and original-save import separated.
- Add provenance notes for reverse-engineering inputs and avoid mixing observations with copied code.

## Review Prompts

- Are original data files required from the user and excluded from releases?
- Are parsers separated from game runtime models?
- Are mod and save compatibility goals explicit?
- Do logs help identify which asset or script failed?
- Are enhancements gated away from compatibility mode?
