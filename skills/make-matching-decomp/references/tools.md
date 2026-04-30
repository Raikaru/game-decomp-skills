# Tool Mini-Guides

## splat

Use for supported console binary splitting, especially MIPS-era projects. Commit split configs, not user-owned binaries or generated copyrighted outputs. Verify input hashes before splitting.

## decomp-toolkit

Use for GameCube/Wii-style DOL/REL splitting, analysis, and relinking workflows. Record tool versions and object boundaries. Keep original DOL/REL files local-only.

## objdiff

Use for object/function/data comparison and rebuild-on-change review loops. Pair with a repeatable check command so CI or local review can reproduce results.

## asm-differ

Use for fast assembly-level iteration. Treat it as a diagnostic loop, not a replacement for provenance or build reproducibility.

## m2c

Use as a rough starting point for some architectures. Manually rewrite output into project-style source and confirm provenance policy before committing.

## decomp.me

Use for collaborative single-function scratch work only with material the project is allowed to upload/share. Do not upload original binaries.

## decomp-permuter

Use late, after semantics and control flow are understood. Keep only readable changes that improve the diff and do not obscure behavior.

## Ghidra / IDA / radare2

Use for local observation, symbol discovery, and behavior understanding. Do not export or commit proprietary databases, copied implementation, private symbols, or output whose sharing rights are unclear.
