# Checklists

## Triage Report Template

Use this shape when the user asks "can this be ported?" or gives a repo.

```markdown
## Project Type
[matching decomp / functional decomp / static recomp / engine reimplementation / source modernization]

## Current Build State
[toolchain, supported hosts, reproducibility, asset requirements]

## Platform Dependencies
[graphics, audio, input, filesystem, time, threading, OS shell]

## Recommended Port Strategy
[thin platform layer / backend replacement / recomp runtime / engine reimplementation]

## First Milestone
[smallest playable or observable PC target]

## Risks
[legal, technical, fidelity, packaging, maintainability]

## Next Tasks
[ordered implementation tasks]
```

## Architecture Checklist

- Isolate game logic from platform services.
- Make a single owner for display/window lifecycle.
- Make one canonical input event model and map controllers into it.
- Choose save/config paths that match OS conventions.
- Keep extraction/conversion tools separate from runtime.
- Avoid committing generated copyrighted data.
- Preserve original timing mode before adding high-FPS behavior.
- Gate enhancements behind flags or settings.
- Add logging for asset lookup, backend init, and save/config errors.
- Keep backend code replaceable without changing game logic.

## Backend Selection Heuristics

- SDL is the default first choice for cross-platform windowing/input/audio when no local standard exists.
- GLFW is reasonable for OpenGL/Vulkan windowing when audio/input are already solved elsewhere.
- bgfx or wgpu helps when a renderer must target several graphics APIs without maintaining each directly.
- OpenGL is often quickest for older fixed-function-style ports, but check macOS constraints.
- Vulkan or Direct3D is justified when the original renderer or target audience demands modern GPU control.
- miniaudio is useful for small portable audio layers; use project-native mixers when music sequencing is complex.

## Milestone Ladder

1. Configure and compile host tools on PC.
2. Run asset extraction/conversion with user-provided assets.
3. Open a window and clear a frame.
4. Boot game loop to first visible screen.
5. Wire keyboard/controller input through menus.
6. Play one representative scene/level with audio.
7. Save, quit, relaunch, and reload.
8. Package a clean machine build.
9. Add optional enhancements after baseline works.

## Release Readiness

- Fresh clone build works from documented dependencies.
- First-run asset setup gives actionable errors.
- Windows, Linux, and macOS paths are correct if those platforms are advertised.
- Controller hotplug and rebinding are tested.
- Fullscreen/windowed, DPI scaling, and aspect ratio are tested.
- Saves/configs survive upgrades.
- CI artifacts do not include copyrighted game assets.
- Third-party licenses are included.
- README states legal asset requirements plainly.
- Known deviations from original behavior are documented.
