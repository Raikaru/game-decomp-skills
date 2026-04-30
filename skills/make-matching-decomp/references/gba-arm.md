# GBA / ARM Matching Notes

- Common tools: `objdiff`, `agbcc`-style workflows, `arm-none-eabi` tools, project-local disassembly/diff scripts.
- Watch THUMB vs ARM mode, literal pools, alignment, data/code boundaries, interrupt handlers, and fixed memory addresses.
- Matching may depend on exact compiler behavior and file ordering.
- Keep ROMs and extracted assets local-only.
- Use synthetic fixtures for tools and committed tests.
