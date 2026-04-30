# N64 / MIPS Matching Notes

- Common tools: `splat`, `spimdisasm`, `m2c`, `asm-differ`, `objdiff`, `decomp.me`, `decomp-permuter`.
- Common compiler axis: IDO version, optimization level, ABI assumptions, include order, and old compiler quirks.
- Watch `rodata` ordering, small data, delay slots, branch-likely instructions, register lifetimes, and undefined behavior.
- Keep ROMs and extracted assets local-only. Commit split configs and handwritten source.
- Use `decomp.me` for single-function scratch work only with shareable material.
