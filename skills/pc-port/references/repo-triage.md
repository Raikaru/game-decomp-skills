# Repo Triage

Use these scans to turn an unfamiliar port/decomp/recomp repo into a concrete assessment. Prefer `rg` and `rg --files`.

## Project Shape

```powershell
rg --files -g "README*" -g "LICENSE*" -g "COPYING*" -g "CMakeLists.txt" -g "meson.build" -g "Makefile" -g "premake*.lua" -g "build.gradle" -g ".github/**"
rg -n "decomp|matching|nonmatching|recomp|reverse|extract|asset|ROM|ISO|WAD|PAK|data directory|original files" README* docs .github
```

## Build And Toolchain

```powershell
rg -n "gcc|clang|msvc|cmake|meson|make|ninja|python|extract|convert|tools?|compiler|linker|ldscript|linker script" .
rg --files -g "requirements*.txt" -g "pyproject.toml" -g "package.json" -g "vcpkg.json" -g "conanfile.*" -g "CMakePresets.json"
```

## Platform Dependencies

```powershell
rg -n "SDL|GLFW|OpenGL|Vulkan|Direct3D|D3D|Metal|bgfx|wgpu|miniaudio|OpenAL|XAudio|ALSA|PulseAudio|CoreAudio" .
rg -n "sce[A-Z]|nn::|GX[A-Z]|OS[A-Z]|VI[A-Z]|AI[A-Z]|SI[A-Z]|Pad|Controller|DirectInput|XInput" .
rg -n "fopen|CreateFile|SHGetFolderPath|AppData|\\.config|save|config|user directory|filesystem|path" .
```

## Asset And Legal Boundaries

```powershell
rg --files -g "*.z64" -g "*.n64" -g "*.v64" -g "*.iso" -g "*.bin" -g "*.wad" -g "*.pak" -g "*.dat" -g "*.otr" -g "*.asset" -g "*.rom"
rg -n "copyright|licensed|proprietary|do not distribute|provide your own|dump|extract|original game|assets not included|ROM not included" .
```

If copyrighted assets, ROMs, or proprietary blobs are present, do not inspect or redistribute them. Tell the user the project needs a clean boundary and continue with architecture-only guidance.

## Candidate Seams

- Renderer init and frame submission.
- Audio mixer and backend output.
- Input polling and controller mapping.
- Asset lookup and archive mounting.
- Save/config path handling.
- Timer/frame pacing source.
- Platform SDK calls or hardware register abstractions.
- Generated-code or generated-asset directories.

## Triage Output

Report project type, current build state, legal asset boundary, platform dependencies, likely first milestone, highest-risk seams, and the strategy-specific skill to use next.
