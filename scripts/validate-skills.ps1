$ErrorActionPreference = "Stop"

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$validator = Join-Path $codexHome "skills/.system/skill-creator/scripts/quick_validate.py"
if (-not (Test-Path $validator)) {
    throw "Could not find Codex skill validator at $validator"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $repoRoot "skills"

Get-ChildItem -Directory $skillsRoot | ForEach-Object {
    Write-Host "Validating $($_.Name)"
    python $validator $_.FullName
}
