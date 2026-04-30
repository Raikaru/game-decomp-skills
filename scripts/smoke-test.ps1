$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

python "$repoRoot/scripts/check-skill-frontmatter.py" "$repoRoot/skills"

python "$repoRoot/skills/make-matching-decomp/scripts/check_decomp_hygiene.py" "$repoRoot/skills/make-matching-decomp/assets/matching-decomp-template"
python "$repoRoot/skills/make-matching-decomp/scripts/check_private_artifacts.py" "$repoRoot/skills/make-matching-decomp/assets/matching-decomp-template"
python "$repoRoot/skills/make-matching-decomp/scripts/check_provenance_docs.py" "$repoRoot/skills/make-matching-decomp/assets/matching-decomp-template"

python "$repoRoot/skills/make-functional-decomp/scripts/check_decomp_hygiene.py" "$repoRoot/skills/make-functional-decomp/assets/functional-decomp-template"
python "$repoRoot/skills/make-functional-decomp/scripts/check_private_artifacts.py" "$repoRoot/skills/make-functional-decomp/assets/functional-decomp-template"
python "$repoRoot/skills/make-functional-decomp/scripts/check_provenance_docs.py" "$repoRoot/skills/make-functional-decomp/assets/functional-decomp-template"

Push-Location "$repoRoot/skills/make-functional-decomp/assets/functional-decomp-template"
try {
    python tools/generate-fixtures/generate_sample_fixture.py
    python tests/test_sample_fixture.py
}
finally {
    Remove-Item -LiteralPath "tests/fixtures/generated/sample.bin" -ErrorAction SilentlyContinue
    Pop-Location
}
