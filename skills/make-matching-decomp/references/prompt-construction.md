# Prompt Construction For LLM-Assisted Matching Decompilation

When asking an LLM to decompile a single function, the prompt quality
determines whether the result compiles at all — let alone matches.

This reference describes the proven prompt structure from automated
decompilation pipelines such as Mizuchi and Kappa.

## Prompt Anatomy

An effective decompilation prompt has six sections.

| Section | Purpose |
|---|---|
| **Platform context** | Architecture, calling convention, compiler |
| **Similar examples** | 3-5 decompiled functions similar to the target |
| **Caller context** | C signatures of functions that call the target |
| **Callee context** | Declarations of functions the target calls |
| **Type definitions** | Structs, enums, and typedefs used by those declarations |
| **Target assembly** | The function to decompile, with clear success criteria |

These sections accumulate into a prompt of several thousand tokens. The LLM
uses all of them to produce correct, matching C.

## Platform Context

State the target upfront so the LLM selects the right ABI, endianness, and
calling convention.

```
You are decompiling an assembly function called `cosf_table`
in ARMv4T from a Game Boy Advance game.
```

Supported platform labels:

| Platform | Architecture | Label |
|---|---|---|
| GBA | ARMv4T (Thumb/ARM) | Game Boy Advance |
| N64 | MIPS | Nintendo 64 |
| PS1 | MIPS | PlayStation |
| PS2 | MIPS | PlayStation 2 |
| GC/Wii | PowerPC | GameCube / Wii |

## Similar Examples (Embedding Search)

The most impactful section. Include 3-5 already-decompiled functions whose
assembly is similar to the target. Similarity is measured by embedding the
normalized assembly and selecting the nearest neighbors by cosine distance.

Present each example as both the C source and the original assembly.

```
## `func_800A1B34`

```c
s32 func_800A1B34(s32 arg0) {
    s32 temp = arg0 * 3;
    return temp + 1;
}
```

```asm
glabel func_800A1B34
/* 0A1B34 27BDFFE8 */  addiu   $sp, $sp, -0x18
/* 0A1B38 AFBF0014 */  sw      $ra, 0x14($sp)
/* 0A1B3C 00041080 */  sll     $v0, $a0, 2
...
```

Exclude examples that call the target function — those go in the
caller context section instead.

### Without Embeddings

If you don't have an embedding model, select examples manually by:
- Same source file or module
- Similar instruction count (within 20%)
- Similar register usage patterns
- Same type signatures (parameters, return type)

## Caller Context

Include C source of functions that call the target. The LLM uses these to
infer the target's signature and calling semantics.

```
## Functions that call the target assembly

## `Actor_UpdateAll`

```c
void Actor_UpdateAll(ActorContext* ctx) {
    for (s32 i = 0; i < ctx->count; i++) {
        Actor_Update(ctx->actors[i]);
    }
}
```
```

## Callee Declarations

Include declarations of every function the target calls. The LLM needs the
exact parameter types and return types to match register assignments.

```
## Declarations for the functions called from the target assembly

- `void* malloc(size_t size);`
- `void free(void* ptr);`
- `s32 Math_SinS(s16 angle);`
```

## Type Definitions

Include every custom type (struct, typedef, enum) referenced in the
declarations above. Skip standard types (u8, u16, u32, s8, s16, s32, s64).

```
## Types definitions used in the declarations

```c
typedef struct {
    /* 0x00 */ u16 x;
    /* 0x02 */ u16 y;
    /* 0x04 */ u8  flags;
} Vec2s;
```

```c
typedef struct Actor {
    /* 0x00 */ Vec2s pos;
    /* 0x04 */ s32   velocity;
    /* 0x08 */ u8    health;
    /* 0x0C */ void  (*update)(struct Actor*);
} Actor;
```
```

## Target Assembly

Present the assembly with the function entry point as a label and
instruction-level comments that make the hex bytes visible.

```
# Primary Objective

Decompile the following target assembly function from
`asm/nonmatchings/code_800A1B00.s` into clean, readable C code that compiles
to an assembly matching EXACTLY the original one.

```asm
glabel func_800A1B34
/* 0A1B34 27BDFFE8 */  addiu   $sp, $sp, -0x18
/* 0A1B38 AFBF0014 */  sw      $ra, 0x14($sp)
/* 0A1B3C 00041080 */  sll     $v0, $a0, 2
...
```
```

## Rules To Include

Close with minimal, enforceable rules:

```
- You may create new types as needed. Include them in the result.
- Show the ENTIRE function body without cropping or placeholders.
- Do not claim the output matches unless you have verified it produces
  byte-for-byte identical assembly.
```

## Full Example

Assembling all sections produces a prompt like:

```
You are decompiling an assembly function called `func_800A1B34`
in MIPS from a Nintendo 64 game.

## Examples

## `func_800A0F00`

\`\`\`c
...
\`\`\`

\`\`\`asm
...
\`\`\`

## Functions that call the target assembly

## `Scene_Init`

\`\`\`c
...
\`\`\`

## Declarations for the functions called from the target assembly

- `void* malloc(size_t size);`
- `s32 Math_SinS(s16 angle);`

## Types definitions used in the declarations

\`\`\`c
typedef struct { ... } Vec2s;
\`\`\`

# Primary Objective

Decompile the following target assembly function from
`asm/nonmatchings/code_800A1B00.s` into clean, readable C code that
compiles to an assembly matching EXACTLY the original one.

\`\`\`asm
glabel func_800A1B34
/* 0A1B34 27BDFFE8 */  addiu   $sp, $sp, -0x18
...
\`\`\`

# Rules

- You may create new types as needed. Include them in the result.
- Show the ENTIRE function body without cropping or placeholders.
```

## Automation Notes

This prompt structure is used by automated decompilation pipelines
(Mizuchi, Kappa) that achieve >70% match rates on benchmark datasets.
Key implementation details for automation:

- **Embedding model**: `jina-embeddings-v2-base-code` works well for
  assembly similarity. Normalize the assembly before embedding (strip
  comments, normalize whitespace, remove addresses).
- **Example limit**: 5 is a practical ceiling. More examples crowd out
  the target assembly and type definitions.
- **Type discovery**: Walk the AST of the caller/callee declarations to
  find every custom type identifier, then search the codebase for its
  definition. Skip primitive types.
- **Fallback**: Without embeddings, use the same source file's
  already-decompiled functions as examples.
