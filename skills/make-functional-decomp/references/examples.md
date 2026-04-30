# Functional Decomp Examples

## Scaffold

User asks: "Create a functional decomp scaffold for a user-owned game executable."

Use `assets/functional-decomp-template/`, then fill in compatibility scope, behavior oracles, provenance rules, private fixture paths, and one synthetic fixture test.

## Behavior Oracle

User asks: "How should we test this script VM?"

Define synthetic opcode fixtures, scheduling tests, state snapshots after fixed inputs, and private local smoke tests against user-owned content.

## Review

User asks: "Review this readable rewrite of a parser."

Read `references/review-functional.md`. Check provenance, synthetic fixtures, private fixture boundaries, format variant handling, and documented deviations.

## Port Prep

User asks: "Make this ready for a PC port later."

Keep the task in this skill only for architecture boundaries. For runtime backends, packaging, or user-facing PC release work, route to `functional-decomp-port`.
