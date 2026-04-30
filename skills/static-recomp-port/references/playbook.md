# Static Recomp Port Playbook

## First Milestone

- Generate or load translated code from user-provided artifacts.
- Initialize host memory and runtime services.
- Reach a first visible frame with logging enabled.
- Accept input and advance to an interactive scene.

## Patch Organization

- `baseline/`: required to boot or preserve original behavior on PC.
- `platform/`: host filesystem, input, display, audio, timing.
- `compat/`: fixes for known runtime differences.
- `enhancements/`: widescreen, high FPS, QoL, accessibility, debug UI.
- `mods/`: external patch hooks or plugin APIs.

## Runtime Checks

- Validate memory map and alignment assumptions.
- Track frame pacing, audio buffer underflow, and input latency.
- Log every failed asset lookup with the search paths used.
- Add assertions for unsupported opcodes, syscalls, or platform service calls.

## Non-Obvious Failure Modes

- Generated translated code can drift from the user's input artifact unless generation is reproducible.
- Generated translated code may be a redistribution risk when derived from copyrighted inputs; prefer local generation from user-owned artifacts.
- ABI mismatches around calling convention, float state, vector registers, or stack alignment can look like gameplay bugs.
- Memory-map mistakes often pass boot and fail only in later scenes, DMA-like paths, or overlays.
- Enhancement patches can accidentally become required for baseline boot.

## First Implementation Seams

- Create a manifest that records input hashes, tool versions, generated outputs, and patch set versions.
- Add memory-map validation before rendering or input work.
- Group patches by subsystem and load baseline patches before optional enhancements.
- Build a minimal trace mode for branch targets, patch application, asset lookup, and service calls.

## Review Prompts

- Can a user reproduce generated artifacts from legally owned inputs?
- Are baseline and enhancement patches separated?
- Are crash logs actionable for translated-code faults?
- Are save/config paths native to each target OS?
- Is mod support documented without requiring copyrighted redistribution?
