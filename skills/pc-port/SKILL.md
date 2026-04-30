---
name: pc-port
description: Triage, compare, and plan PC-port strategy for decompiled, reverse-engineered, statically recompiled, or source-available game projects when the port approach is unknown or cross-strategy. Use for initial repo assessment, strategy selection, cross-strategy architecture, release-readiness checklists, or comparing PC-port approaches. If the strategy is already known, prefer the matching strategy-specific skill.
---

# PC Port

## Operating Rules


- Keep ROMs, binaries, copyrighted assets, generated asset bundles, and keys out of outputs.
- Require users to provide their own game assets when a port needs original content.
- Prefer public open-source repos, public documentation, and project-authored build instructions.
- Avoid copying code from example ports unless its license permits reuse and the target project can accept that license.

## Workflow

1. Classify the project.
   - Matching decompilation: source rebuilds original binaries or objects.
   - Functional decompilation: readable source recreates behavior without exact matching.
   - Static recompilation: translated executable or IR plus runtime patches.
   - Engine reimplementation: new engine reads original data files.
   - Commercial/open-source release: original source is available but needs modernization.

2. Inventory host services.
   - Graphics: display init, render API, shaders/microcode, framebuffer effects, aspect ratio, frame pacing.
   - Audio: mixer, sequence player, streaming, latency, sample rate, platform codecs.
   - Input: keyboard/mouse, controllers, rumble, rebinding, hotplug, text entry.
   - Filesystem: asset loading, save paths, config paths, endian/layout assumptions.
   - Time/threading: frame tick source, sleeps, jobs, determinism, platform timers.
   - OS shell: windowing, fullscreen, DPI, crash logs, paths, clipboard, localization.

3. Pick the port strategy.
   - Thin portability layer when game logic already compiles cleanly.
   - Backend swap when original platform APIs are isolated.
   - Runtime patch/recomp framework when source is unavailable or intentionally avoided.
   - Engine reimplementation when data formats are stable and gameplay code is better recreated.

4. Choose PC backends that fit the repo.
   - Use SDL2/SDL3 for windowing, input, controllers, audio, and cross-platform packaging unless the repo already standardizes elsewhere.
   - Use OpenGL, Vulkan, Direct3D, bgfx, or wgpu according to existing renderer shape and target platforms.
   - Use miniaudio, SDL audio, OpenAL, or project-native audio only after checking latency and mixer needs.
   - Use CMake, Meson, or the repo's existing build system; avoid adding a second build universe without strong reason.

5. Build the port layer.
   - Create a narrow `platform/`, `src/platform_pc/`, `port/`, or existing-equivalent boundary.
   - Keep game logic call sites stable; route OS, graphics, audio, input, paths, and time through adapters.
   - Put asset extraction/conversion in a separate tool path from runtime code.
   - Add feature flags for enhancements so original behavior can still be tested.

6. Verify behavior.
   - Compare boot, title flow, saves, loading, menus, representative levels, cutscenes, audio sync, and frame pacing.
   - Keep deterministic or original-timing modes available for regression checks.
   - Test keyboard-only, controller-only, unplug/replug, fullscreen/windowed, non-ASCII paths, and clean first-run setup.

7. Prepare release hygiene.
   - Document required user-provided assets and extraction steps.
   - Keep generated copyrighted assets out of source releases and CI artifacts.
   - Package per platform with save/config directories appropriate to the OS.
   - Include license notices for every backend and borrowed component.

## Strategy Routing

After classifying the project, use the strategy-specific skill when the user needs implementation, detailed review, or a concrete port plan.

- Matching decompilation: use the `matching-decomp-port` skill.
- Functional decompilation: use the `functional-decomp-port` skill.
- Static recompilation: use the `static-recomp-port` skill.
- Engine reimplementation: use the `engine-reimplementation-port` skill.
- Source modernization: use the `source-modernization-port` skill.

## References

Read [case-studies.md](references/case-studies.md) when comparing approaches from known public PC ports or choosing a port family.

Read [checklists.md](references/checklists.md) when producing a triage report, implementation plan, PR review, or release-readiness assessment.

Read [repo-triage.md](references/repo-triage.md) when inspecting an actual repository.
