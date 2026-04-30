# PC / x86 Matching Notes

- Common tools: `objdiff`, Ghidra/IDA/radare2 for observation, compiler-specific disassemblers, project-local diff scripts.
- Matching depends heavily on compiler version, calling convention, struct packing, floating-point mode, CRT/library boundaries, and optimization flags.
- Watch import libraries, debug symbols, PDB provenance, SEH, inline assembly, and platform SDK boundaries.
- Do not commit original executables, PDBs, or unclear symbol databases.
