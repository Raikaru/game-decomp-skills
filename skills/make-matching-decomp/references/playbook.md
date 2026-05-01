# Matching Decomp Playbook

## Repo Skeleton

- `.gitignore`: ignore user-owned artifacts, generated splits, build outputs, local scratch spaces, and generated copyrighted bundles.
- `README.md`: quickstart, legal artifact requirements, build/check commands, and contribution expectations.
- `docs/match-target.md`: target versions, hashes, match granularity, compiler/toolchain assumptions, and acceptance criteria.
- `docs/provenance.md`: allowed sources, symbol/type confidence, and note policy.
- `docs/artifacts.md`: where users place local artifacts and which generated outputs must not be committed.
- `config/versions.yml`: accepted artifact hashes, tool versions, compiler identifiers, and platform metadata.
- `config/` or `splat/`: split configuration and version manifests.
- `asm/`: generated or hand-maintained assembly baselines when policy allows.
- `src/`: handwritten source intended to match.
- `include/`: project headers and reconstructed types.
- `tools/verify_hash.*`: verify user-provided artifact hashes before splitting.
- `tools/split.*`: run `splat`, `decomp-toolkit`, or project-specific split tooling.
- `tools/diff.*` and `tools/check_match.*`: repeatable object/function/binary diff commands.
- `tools/`: extraction, split, diff, asset, or build helper scripts.
- `build/`: generated objects and linked outputs; ignored.
- `artifacts-local/`, `original-private/`, or `baserom-local/`: user-provided and generated local artifacts; ignored unless redistribution rights are explicit.

Minimum `.gitignore` patterns:

```gitignore
artifacts-local/
original-private/
baserom-local/
build/
expected/
*.z64
*.n64
*.v64
*.iso
*.gcm
*.dol
*.exe
*.bin
*.elf
*.o
*.map
```

## First Milestone

1. Verify the user-provided artifact hash.
2. Split one small code/data unit.
3. Compile one handwritten function with the target toolchain.
4. Produce an assembly or object diff.
5. Document the exact command for repeating the match check.

Expected deliverables:

- `README.md` quickstart.
- `.gitignore` with local artifact/build-output exclusions.
- `docs/match-target.md`.
- `docs/provenance.md`.
- `docs/artifacts.md`.
- `config/versions.yml`.
- One split config.
- One minimal source unit.
- One repeatable `check-match` or diff command.

## Tool Selection

- Use `splat` for N64, PSX, PS2, or PSP-style binary splitting when it fits the platform.
- Use `decomp-toolkit` for GameCube/Wii DOL/REL-oriented projects and object relinking workflows.
- Use `objdiff` when comparing relocatable objects, functions, and data with rebuild-on-change ergonomics.
- Use `asm-differ` or project-local diff scripts for fast function-level assembly comparisons.
dy|- Use `decomp.me` as collaborative scratch space for individual functions, compiler experiments, and shareable matching attempts only with material the project is allowed to upload or share; do not upload copyrighted binaries.
- Use `m2c` as a starting point for MIPS/PowerPC/ARM source approximations; manually refine before accepting code.
tr|- Use `decomp-permuter` late, after control flow and semantics are already close; only keep changes that make source-level sense.

## Automated Pipeline

For function-by-function matching without manual iteration, orchestrate the
tools into a retry pipeline with three phases:

### 1. Setup
- Run `m2ctx.py` or equivalent to extract context (types, macros,
  signatures) from the project for the target function.

### 2. Programmatic Phase
- Run `m2c` on the function's assembly to produce a first C attempt.
- Compile and objdiff the result against the target object.
- If no match, run `decomp-permuter` to brute-force code mutations
  for better scores.
- Pass the best attempt as seed code to the next phase.

### 3. AI-Powered Phase (optional)
- Send a prompt to an LLM with platform context, similar-function
  examples, caller/callee signatures, and type definitions (see
  `references/prompt-construction.md`).
- **Loop**: LLM submits C → compile → objdiff → diff report back to LLM.
- Run permuter in the background on each LLM attempt; if it finds a
  perfect match, short-circuit.
- Retry on compile errors, timeouts, or partial matches up to a
  configurable limit.

Benchmarks on 60 functions across N64 and GBA decomp projects show
a ~74% match rate with 12 attempts per function using this architecture
(programmatic + Claude Sonnet). The programmatic phase alone matches
near-zero on GBA (no m2c ARM result matched) and ~7/30 on N64 (m2c +
permuter). The AI phase does the remaining work.

Known tools implementing this pipeline:
- **[Mizuchi](https://github.com/macabeus/mizuchi)** (MIT) — full
  pipeline runner with plugin system, Decomp Atlas UI, and benchmark
  reporting. Supports ARM, MIPS, PowerPC targets.
- **[Kappa](https://github.com/macabeus/kappa)** — VS Code extension
  by the same author; LLM-assisted single-function workflow.
- **[SK2 Agent](https://github.com/cdlewis/snowboardkids2-decomp)** —
  Chris Lewis's agentic decomp pipeline (Python, project-specific).

## Diff Triage

- Register allocation mismatch: check variable lifetimes, declaration order, signedness, volatile, and expression shape.
- Stack mismatch: check local variable size/order, struct layout, inlining, saved registers, and ABI rules.
- Instruction mismatch: check casts, integer promotion, constants, macros, and compiler flags.
- Section/layout mismatch: check alignment, rodata ordering, file order, linker script, and object boundaries.
- Branch mismatch: check control-flow shape before changing semantics.

## Provenance Notes

- Label notes as observation, hypothesis, public documentation, generated output, or implemented source.
ve|- Keep proprietary materials out of issue text, comments, commits, and generated docs.
- Avoid importing names from unclear symbol maps; use descriptive temporary names instead.
- Keep a local-only path for user-owned artifacts and generated comparisons.
- Record source, URL, license, and confidence for public symbols, signatures, headers, or documentation.
- Do not scrape decomp.me or similar collaborative services; use documented APIs where permitted or user-provided scratch links/content.

## Useful Scans

```powershell
rg --files -g "README*" -g "LICENSE*" -g "*.ld" -g "*.lcf" -g "*.splat*" -g "*.yaml" -g "Makefile" -g "CMakeLists.txt"
rg -n "match|nonmatch|baserom|splat|split|diff|objdump|asm|linker|compiler|sha1|md5|expected" .
rg -n "TODO|NON_MATCHING|GLOBAL_ASM|INCLUDE_ASM|stub|fake|hack" src include asm tools
```

## Non-Obvious Failure Modes

- Matching can depend on compiler bugs, undefined behavior, or exact include order.
- A type that makes one function match can break object layout elsewhere.
- Data and rodata ordering may be the blocker, not the function body.
- Generated local artifacts can become redistribution risks if ignored paths are incomplete.
- "Clean" names can overstate certainty and make future correction harder.

## Review Prompts

- Are original artifacts and generated outputs excluded from version control and CI artifacts?
- Is the match target explicit and repeatable?
- Are toolchain versions pinned or discoverable?
- Are nonmatching units clearly tracked?
- Did source changes improve the diff without changing intended behavior or provenance boundaries?
