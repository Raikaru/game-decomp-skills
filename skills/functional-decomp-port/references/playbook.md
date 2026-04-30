# Functional Decomp Port Playbook

## First Milestone

- Build the current code with a modern host compiler.
- Run a deterministic smoke path: boot, menu, gameplay entry, save/load, quit.
- Capture logs/screenshots/audio timing for comparison against the original.

## Behavior Oracles

- Use original binaries only for observation and comparison.
- Prefer save files, replay inputs, scripted scenes, map fixtures, and known bug cases.
- Record expected behavior in tests or issue notes, not in vague "feels right" language.

## Common Risks

- Refactors can erase original bugs that content depends on.
- Undefined behavior may become visible on 64-bit, different endian, or optimizing compilers.
- Save formats and script engines often carry hidden compatibility contracts.

## Non-Obvious Failure Modes

- "Cleaner" code can break content that relied on original ordering, rounding, overflow, or timing.
- Modern containers can change iteration order and destabilize scripts, AI, or replay behavior.
- Replacing fixed-point math with floating point can introduce long-tail physics regressions.
- Save migrations can appear correct until old optional fields, expansions, or mods are loaded.

## First Implementation Seams

- Introduce a platform service table for file, time, input, audio, and rendering calls.
- Add comparison logs for deterministic scenes before broad refactors.
- Create synthetic fixtures for formats and user-provided fixtures for full-content tests.
- Mark compatibility quirks in code near the behavior, not only in docs.

## Review Prompts

- Is there a baseline compatibility mode?
- Are deviations from original behavior documented?
- Do tests cover save/load and at least one content-heavy scene?
- Are PC backends isolated from gameplay code?
- Are asset requirements explicit?
