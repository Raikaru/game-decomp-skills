# GameCube / Wii / PowerPC Matching Notes

- Common tools: `decomp-toolkit`, `objdiff`, CodeWarrior/Metrowerks-compatible workflows, project-local linker scripts.
- Split DOL/REL objects and compare relocatable objects where possible.
- Watch constructors, exception setup, small data sections, TOC/sda references, floating point, inlining, and C++ ABI details.
- Record provenance for any function signatures or SDK-like names.
- Do not commit DOL/REL files, disc images, or generated copyrighted bundles.
