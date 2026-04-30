# Matching Decomp Examples

## Scaffold

User asks: "Create a matching decomp scaffold for a user-provided N64 artifact."

Use `assets/matching-decomp-template/`, then fill in `docs/match-target.md`, `config/versions.yml`, and local tool placeholders. Do not create or request copyrighted artifacts.

## Review

User asks: "Review this PR that replaces a GLOBAL_ASM function."

Read `references/review-matching.md`. Check provenance, matching command output, object/function diff, generated files, and whether the original target still builds.

## Difficult Function

User asks: "Help match this nonmatching function."

Confirm local material. Use project diff output. Try semantic/control-flow fixes first, then expression shape, type/layout, register lifetime, and only late-stage permutation.

## Tooling

User asks: "Should this use splat, dtk, or objdiff?"

Read the relevant tool and platform references. Choose based on platform, object format, and whether the repo compares full objects or function assembly.
