# Matching Decomp Port Playbook

## First Milestone

- Build the original matching target unchanged.
- Add a PC build preset that compiles host-only files.
- Open a window, clear a frame, and run the game loop until the first visible screen.
- Load assets from a user-generated local bundle or original data directory.

## Preserve Matchability

- Keep original compiler flags and object layouts isolated from PC flags.
- Avoid changing headers used by matched files unless required; prefer wrapper headers for PC-only code.
- If shared headers must change, confirm original target still rebuilds and matching reports do not regress.
- Keep enhancements behind `PORT_FEATURE_*` or existing config flags.

## Common Backend Pattern

- Window/input/controller: SDL2 or SDL3.
- Audio: original mixer plus SDL audio/miniaudio output.
- Graphics: renderer translation layer, OpenGL/bgfx/wgpu/Vulkan according to existing display-list or renderer shape.
- Filesystem: user config directory, save directory, asset directory override.
- Time: original tick mode plus optional uncapped/interpolated mode.

## Non-Obvious Failure Modes

- Shared headers can alter original object layout even when PC-only code looks isolated.
- Asset extraction tools may create redistributable bundles unless ignored and documented carefully.
- High-FPS or widescreen patches can invalidate physics, cutscene, animation, and UI assumptions.
- Original compiler bugs or undefined behavior can become behavioral requirements for matching targets.

## First Implementation Seams

- Add `platform_pc` window/input/time stubs before renderer translation.
- Route save/config paths through one function early.
- Add backend init logs before debugging game-loop problems.
- Keep original build verification in CI while PC work is active.

## Review Prompts

- Does the PC target compile without modifying generated or extracted copyrighted files?
- Can original matching targets still be built and checked?
- Are save/config paths OS-appropriate?
- Can enhancements be disabled to compare baseline behavior?
- Does first-run failure explain which user-provided asset is missing?
