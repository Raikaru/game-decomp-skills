# Source Modernization Port Playbook

## First Milestone

- Build with the oldest documented path or note why it is impractical.
- Build with a modern compiler on the target PC OS.
- Launch to a visible screen with original data files.
- Run one save/load cycle.

## Modernization Order

1. Dependency inventory and license check.
2. Build-system reproducibility.
3. Compiler and warning cleanup.
4. Filesystem/path portability.
5. Platform API shims.
6. Rendering/audio/input backends.
7. Sanitizers and CI.
8. Refactors after behavior is covered.

## Compatibility Traps

- `sizeof(long)`, pointer truncation, packed structs, endianness, and alignment.
- Save files with raw struct dumps.
- Timing loops tied to CPU speed or old timer resolution.
- Case-insensitive asset lookup assumptions.
- Old graphics fixed-function state leaking across draw calls.

## Non-Obvious Failure Modes

- Public source may depend on proprietary middleware or SDK headers that cannot be redistributed.
- Warning cleanup can change behavior when old code relied on signed overflow, uninitialized memory, or aliasing.
- Unicode and long-path handling can break legacy asset lookup assumptions.
- Networking protocols and demo/replay files may be part of compatibility even when not obvious.

## First Implementation Seams

- Add a compatibility shim for obsolete platform APIs before replacing call sites.
- Put asset and save paths behind one module before packaging work.
- Add sanitizer runs after the modern compiler build works.
- Introduce file-format and save tests before changing serialization code.

## Review Prompts

- Are source and asset licenses handled separately?
- Does the modern build work from a fresh clone?
- Are third-party licenses included in packages?
- Are saves/configs in OS-appropriate user directories?
- Did sanitizer findings lead to fixes rather than blanket suppression?
