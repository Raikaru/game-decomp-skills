#!/usr/bin/env python3
"""
Score non-matching functions by estimated decompilation difficulty.

Trains a logistic regression model on already-decompiled vs. undecompiled
functions using three assembly-level features:
  - instruction count
  - branch count
  - label count

Outputs a ranked list of undecompiled functions from easiest to hardest.
"""

import argparse
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Assembly metrics (per platform)
# ---------------------------------------------------------------------------

@dataclass
class AsmMetrics:
    instruction_count: int = 0
    branch_count: int = 0
    label_count: int = 0


ARM_BRANCHES = frozenset({
    "beq", "bne", "bgt", "bge", "blt", "ble",
    "bhi", "bhs", "blo", "bls", "bcc", "bcs",
    "bmi", "bpl",
})

# ARM/Thumb comment prefix, labels, directives
ARM_COMMENT_RE = re.compile(r"\s*@.*$")
ARM_LABEL_RE = re.compile(r"^\s*(\.L\w+:|_[0-9A-Fa-f]+:|[\w]+\s*:\s*@\s*0x)")
ARM_DIRECTIVE_RE = re.compile(r"^\s*\.")
ARM_FUNC_MARKER_RE = re.compile(r"(thumb_func_start|arm_func_start)")


def count_arm_metrics(asm_code: str) -> AsmMetrics:
    m = AsmMetrics()
    for raw_line in asm_code.splitlines():
        line = ARM_COMMENT_RE.sub("", raw_line).strip()
        if not line:
            continue
        if ARM_FUNC_MARKER_RE.search(line):
            continue
        if ARM_LABEL_RE.match(line):
            m.label_count += 1
            continue
        if ARM_DIRECTIVE_RE.match(line):
            continue
        mnemonic = line.split()[0].lower()
        # bl is a call, not a branch for scoring purposes
        if mnemonic in ("bl", "bx", "bic", "bics"):
            m.instruction_count += 1
            continue
        if mnemonic in ARM_BRANCHES or mnemonic == "b":
            m.branch_count += 1
            m.instruction_count += 1
            continue
        m.instruction_count += 1
    return m


MIPS_INSTRUCTION_MARKER = re.compile(r"/\*\s*[0-9A-Fa-f]+\s+[0-9A-Fa-f]+\s+[0-9A-Fa-f]+\s*\*/")
MIPS_BRANCH_RE = re.compile(
    r"\b(beq|bne|bnez|beqz|blez|bgtz|bltz|bgez|blt|bgt|ble|bge|bltzal|bgezal)\b"
)
MIPS_LABEL_RE = re.compile(r"^\s*\.L[\w]+:")


def count_mips_metrics(asm_code: str) -> AsmMetrics:
    m = AsmMetrics()
    for line in asm_code.splitlines():
        if MIPS_LABEL_RE.match(line):
            m.label_count += 1
        if not MIPS_INSTRUCTION_MARKER.search(line):
            continue
        m.instruction_count += 1
        if MIPS_BRANCH_RE.search(line):
            m.branch_count += 1
    return m


def count_asm_metrics(asm_code: str, target: str) -> AsmMetrics:
    """Dispatch to the correct metric counter based on platform target."""
    arm_targets = {"gba", "nds", "n3ds"}
    mips_targets = {"n64", "ps1", "ps2", "psp", "irix"}
    ppc_targets = {"gc", "wii"}
    if target in arm_targets:
        return count_arm_metrics(asm_code)
    if target in mips_targets:
        return count_mips_metrics(asm_code)
    if target in ppc_targets:
        # PowerPC uses a similar format to ARM; basic counting works
        return count_arm_metrics(asm_code)
    # Fallback generic: count lines that look like instructions
    instrs = [l for l in asm_code.splitlines() if l.strip() and not l.strip().startswith(".")]
    return AsmMetrics(instruction_count=len(instrs))


# ---------------------------------------------------------------------------
# Function discovery
# ---------------------------------------------------------------------------

# Match INCLUDE_ASM / GLOBAL_ASM stubs (undecompiled markers)
STUB_RE = re.compile(r'(INCLUDE_ASM|GLOBAL_ASM|pragma\s+GLOBAL_ASM)')
# Rough function definition matcher: "type name(...) {"
FUNC_DEF_RE = re.compile(
    r'^\s*(?:static\s+|extern\s+)?(?:\w+\s+)+(\w+)\s*\([^)]*\)\s*\{'
)


@dataclass
class FuncInfo:
    name: str
    asm_code: str
    is_matched: bool = False
    source_file: str = ""
    metrics: AsmMetrics = field(default_factory=AsmMetrics)


def discover_functions(
    project_root: Path,
    asm_dirs: list[str],
    src_dirs: list[str],
    target: str,
) -> list[FuncInfo]:
    """Scan asm files for functions and cross-reference with C source."""

    # Collect matched function names from C source
    matched_names: set[str] = set()
    stub_names: set[str] = set()
    c_files: list[Path] = []
    for sd in src_dirs:
        c_files.extend((project_root / sd).rglob("*.c"))
    for c_path in c_files:
        text = c_path.read_text(encoding="utf-8", errors="replace")
        # Collect stubs
        for m in STUB_RE.finditer(text):
            # Try to extract function name from the stub line
            line = text[: m.start()].rsplit("\n", 1)[-1] + text[m.start():].split("\n", 1)[0]
            for tok in re.findall(r'"([^"]+)"', line):
                stub_names.add(tok)
                break
        # Collect actual function definitions
        for m in FUNC_DEF_RE.finditer(text):
            matched_names.add(m.group(1))

    # Functions that appear in both matched_names and stub_names are stubs
    truly_matched = matched_names - stub_names
    truly_stubs = stub_names

    # Scan asm files
    functions: list[FuncInfo] = []
    asm_files: list[Path] = []
    for ad in asm_dirs:
        asm_dir = project_root / ad
        if asm_dir.is_dir():
            asm_files.extend(asm_dir.rglob("*.s"))
            asm_files.extend(asm_dir.rglob("*.S"))

    for asm_path in asm_files:
        text = asm_path.read_text(encoding="utf-8", errors="replace")
        # Try to extract function name from file
        name = asm_path.stem
        metrics = count_asm_metrics(text, target)
        is_matched = name in truly_matched
        if name in truly_stubs:
            is_matched = False
        functions.append(
            FuncInfo(
                name=name,
                asm_code=text,
                is_matched=is_matched,
                source_file=str(asm_path.relative_to(project_root)),
                metrics=metrics,
            )
        )

    return functions


# ---------------------------------------------------------------------------
# Logistic regression
# ---------------------------------------------------------------------------

# Fallback coefficients from Chris Lewis's Snowboard Kids 2 analysis
FALLBACK_MEANS = (34.27, 1.67, 1.98)
FALLBACK_STDS = (24.76, 2.05, 2.38)
FALLBACK_COEFFS = (2.50, -0.47, 0.49)
FALLBACK_INTERCEPT = -0.52


def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    return math.exp(x) / (1.0 + math.exp(x))


def train_model(
    features: list[tuple[float, float, float]],
    labels: list[int],
) -> tuple[list[float], list[float], list[float], float]:
    """
    Train logistic regression via gradient descent.
    Returns (means, stds, coefficients, intercept).
    """
    n = len(features)
    if n < 3:
        # Fall back to pre-computed coefficients
        return (
            list(FALLBACK_MEANS),
            list(FALLBACK_STDS),
            list(FALLBACK_COEFFS),
            FALLBACK_INTERCEPT,
        )

    # Feature means and stds
    means = [sum(f[j] for f in features) / n for j in range(3)]
    stds = [
        math.sqrt(sum((f[j] - means[j]) ** 2 for f in features) / n)
        for j in range(3)
    ]

    # Z-score normalize
    X = [
        (
            (f[0] - means[0]) / stds[0] if stds[0] > 0 else 0,
            (f[1] - means[1]) / stds[1] if stds[1] > 0 else 0,
            (f[2] - means[2]) / stds[2] if stds[2] > 0 else 0,
        )
        for f in features
    ]

    # Gradient descent
    w = [0.0, 0.0, 0.0]
    b = 0.0
    lr = 0.1
    iterations = 1000

    for _ in range(iterations):
        grad_w = [0.0, 0.0, 0.0]
        grad_b = 0.0
        for i in range(n):
            logit = b + sum(X[i][j] * w[j] for j in range(3))
            pred = sigmoid(logit)
            error = pred - labels[i]
            for j in range(3):
                grad_w[j] += error * X[i][j]
            grad_b += error
        for j in range(3):
            w[j] -= (lr * grad_w[j]) / n
        b -= (lr * grad_b) / n

    return means, stds, w, b


def apply_model(
    metrics: AsmMetrics,
    means: list[float],
    stds: list[float],
    coeffs: list[float],
    intercept: float,
) -> float:
    """Compute difficulty score (0=easy, 1=hard)."""
    feats = [metrics.instruction_count, metrics.branch_count, metrics.label_count]
    logit = intercept
    for j in range(3):
        scaled = (feats[j] - means[j]) / stds[j] if stds[j] > 0 else 0
        logit += scaled * coeffs[j]
    return sigmoid(logit)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Score decompilation functions by estimated difficulty."
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=Path("."),
        help="Project root directory (default: current dir)",
    )
    parser.add_argument(
        "--target",
        default="gba",
        choices=["gba", "nds", "n3ds", "n64", "ps1", "ps2", "psp", "irix", "gc", "wii"],
        help="Target platform (default: gba)",
    )
    parser.add_argument(
        "--asm-dirs",
        nargs="*",
        default=["asm/nonmatchings", "asm"],
        help="Directories containing non-matching assembly files",
    )
    parser.add_argument(
        "--src-dirs",
        nargs="*",
        default=["src", "include"],
        help="Directories to scan for C source files",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=30,
        help="Show top N easiest undecompiled functions (default: 30)",
    )
    parser.add_argument(
        "--list-hard",
        action="store_true",
        help="Show hardest functions instead of easiest",
    )
    args = parser.parse_args()

    root: Path = args.project

    print(f"Scanning project: {root.resolve()}")
    print(f"Target platform: {args.target}")
    print(f"ASM dirs: {args.asm_dirs}")
    print(f"Source dirs: {args.src_dirs}")
    print()

    functions = discover_functions(root, args.asm_dirs, args.src_dirs, args.target)

    if not functions:
        print("No assembly functions found. Check --asm-dirs.")
        return 1

    matched = [f for f in functions if f.is_matched]
    unmatched = [f for f in functions if not f.is_matched]

    print(f"  Functions found: {len(functions)}")
    print(f"    Already matched: {len(matched)}")
    print(f"    Undecompiled:    {len(unmatched)}")
    print()

    if not matched:
        print(
            "No already-matched functions found. "
            "Using fallback coefficients from known decomp project data."
        )
        means, stds, coeffs, intercept = (
            list(FALLBACK_MEANS),
            list(FALLBACK_STDS),
            list(FALLBACK_COEFFS),
            FALLBACK_INTERCEPT,
        )
        using_fallback = True
    else:
        features = [
            (f.metrics.instruction_count, f.metrics.branch_count, f.metrics.label_count)
            for f in matched
        ]
        labels = [0] * len(matched) + [1] * len(unmatched)
        features += [
            (f.metrics.instruction_count, f.metrics.branch_count, f.metrics.label_count)
            for f in unmatched
        ]
        means, stds, coeffs, intercept = train_model(features, labels)
        using_fallback = False

    # Score all undecompiled functions
    scored: list[tuple[float, FuncInfo]] = []
    for f in unmatched:
        score = apply_model(f.metrics, means, stds, coeffs, intercept)
        scored.append((score, f))

    scored.sort(key=lambda x: x[0])

    if using_fallback:
        print("Model: fallback (no matched functions for training)")
    else:
        print(
            f"Model: trained on {len(matched)} matched + {len(unmatched)} undecompiled functions"
        )
    print(f"Coefficients: instr={coeffs[0]:.4f}  branch={coeffs[1]:.4f}  label={coeffs[2]:.4f}")
    print(f"Intercept:    {intercept:.4f}")
    print()

    display = scored if not args.list_hard else scored[::-1]
    display = display[: args.top]

    header = f"{'Rank':>4}  {'Score':>6}  {'Instructions':>13}  {'Branches':>8}  {'Labels':>6}  {'Function':<35}  {'Source'}"
    print(header)
    print("-" * len(header))
    for rank, (score, fi) in enumerate(display, 1):
        tier = "easy" if score < 0.33 else "hard" if score > 0.66 else "medium"
        print(
            f"{rank:>4}  {score:.4f}  {fi.metrics.instruction_count:>13}  "
            f"{fi.metrics.branch_count:>8}  {fi.metrics.label_count:>6}  "
            f"{fi.name:<35}  [{tier}]  {fi.source_file}"
        )

    print()
    if not args.list_hard:
        print("Lower score = easier. Target functions at the top of this list first.")
    else:
        print("Hardest functions shown. These may need more context or tooling help.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
