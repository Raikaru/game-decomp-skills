# Tool Mini-Guides

## Ghidra / IDA / radare2

Use for local observation, data-format discovery, function boundary analysis, and behavior notes. Treat output as observation material, not final source. Do not commit private databases, copied implementation, or proprietary symbols.

## m2c And Decompiler Output

Use as rough scaffolding. Rewrite into maintainable source, record provenance, and avoid pasting output directly unless the project policy allows it.

## Trace And State Comparison

Use trace logs, deterministic input sequences, state snapshots, save round-trips, and script outputs as behavior oracles. Keep traces containing copyrighted content local-only.

## Fixture Generators

Prefer generated synthetic fixtures for committed tests. Use user-owned local fixtures for full-content smoke tests without committing them.

## Fuzzers / Property Tests

Use for parsers, archive readers, script bytecode, save formats, and decompression code. Fuzz synthetic or generated inputs, not copyrighted assets.

## decomp.me

Use only when the project is allowed to upload/share the material.
