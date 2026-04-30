# Case Studies

Use these as pattern references, not as source material to copy blindly. Confirm current licenses and project status before reusing code.

## Matching Decompilation To Native Port

Examples: `sm64-port`/`sm64ex`, HarbourMasters `Shipwright` / Ship of Harkinian, `2ship2harkinian`, reverse-engineered Sonic mobile decomps.

Common patterns:

- Keep a buildable game codebase and add host backends around the original game loop.
- Replace platform display, controller, audio, storage, and OS services behind narrow APIs.
- Add optional enhancements such as widescreen, high frame rate, mod loading, free camera, accessibility, or debug menus as patches layered over baseline behavior.
- Require user-provided assets or a conversion step instead of distributing original copyrighted data.
- Separate extraction/build instructions from normal runtime startup.

Risks:

- Enhancements can hide regressions against original timing or logic.
- Generated asset bundles can accidentally become redistributable copyrighted content.
- Controller, save, and frame pacing behavior often need more polish than initial boot proves.

Public references:

- https://github.com/sm64-port/sm64-port
- https://github.com/sm64pc/sm64ex
- https://github.com/HarbourMasters/Shipwright
- https://github.com/HarbourMasters/2ship2harkinian

## Static Recompilation Runtime

Examples: `Zelda64Recomp`, `N64Recomp`, project-specific recomp ports.

Common patterns:

- Translate original machine code or intermediate artifacts into native code while providing a PC runtime.
- Patch graphics, input, timing, and filesystem behavior around the translated program.
- Add mod hooks or replacement assets through a runtime patch system.
- Emphasize fast port creation when full source decompilation is not required or not available.

Risks:

- Runtime patch layers can become hard to reason about unless patches are grouped by subsystem.
- Original memory layout and platform assumptions may leak everywhere.
- Debugging can be less familiar than normal source-level C/C++.

Public references:

- https://github.com/Zelda64Recomp/Zelda64Recomp
- https://github.com/N64Recomp/N64Recomp

## Engine Reimplementation

Examples: `OpenMW`, `OpenRCT2`, `OpenLara`, `CorsixTH`.

Common patterns:

- Recreate the engine and read original user-owned game data.
- Prefer modern data models, renderer architecture, UI, networking, save formats, and modding APIs when exact binary matching is not the goal.
- Use compatibility layers for original assets, scripts, maps, and saves.
- Test against many real content files because data compatibility is the product.

Risks:

- Fidelity problems cluster in edge-case scripting, physics, AI, and save conversion.
- Scope can grow from "port" into "new engine with every bug replicated."
- Community mods and expansions often matter as much as base-game content.

Public references:

- https://github.com/OpenMW/openmw
- https://github.com/OpenRCT2/OpenRCT2
- https://github.com/XProger/OpenLara
- https://github.com/CorsixTH/CorsixTH

## Source-Available Modernization

Examples: released-source engines such as id Tech family ports, Aleph One, source-available commercial games.

Common patterns:

- Start from legitimate source and replace obsolete platform, compiler, audio, graphics, and networking dependencies.
- Preserve historical data compatibility while modernizing build, packaging, and input.
- Use sanitizers and CI early; source releases often carry undefined behavior that old compilers tolerated.

Risks:

- License boundaries can be subtle when source is public but assets remain commercial.
- Old platform assumptions may be embedded in global state, fixed tick loops, or renderer globals.

Public references:

- https://github.com/id-Software/DOOM-3
- https://github.com/Aleph-One-Marathon/alephone

## Curated Discovery

Use curated lists only as discovery indexes; verify each linked project's status and license directly.

- https://github.com/Sebastrion/awesome-unofficial-pc-ports
- https://github.com/topics/decompilation
