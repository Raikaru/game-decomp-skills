# Game Decomp Skills

Codex skills for game decompilation, reverse-engineering project setup, and decomp-to-PC-port planning.

These skills are designed as practical agent playbooks. They include routing rules, provenance guardrails, scaffold templates, validation scripts, platform notes, tool mini-guides, and review checklists.

## Included Skills

### Decomp Creation

- `make-matching-decomp`: create, maintain, or review matching decompilation projects where exact binary, object, function, or assembly matching is an explicit goal.
- `make-functional-decomp`: create, maintain, or review functional decompilation projects where readable source aims to match behavior rather than compiler output.

### PC Port Strategy

- `pc-port`: umbrella triage skill for unknown or cross-strategy PC-port planning.
- `matching-decomp-port`: native PC ports from matching decompilation projects.
- `functional-decomp-port`: native PC ports from functional decompilation projects.
- `static-recomp-port`: PC ports based on static recompilation runtimes and patch systems.
- `engine-reimplementation-port`: clean engine reimplementation ports that use user-owned original data.
- `source-modernization-port`: modernization of legitimate source releases into maintainable PC ports.

## Safety And Provenance

These skills intentionally focus on architecture, project hygiene, and provenance process.

They instruct Codex to keep ROMs, ISOs, executables, copyrighted assets, generated copyrighted bundles, and keys out of outputs. They also require user-owned local inputs for extraction, comparison, observation, or testing when original artifacts are needed.


## Install

Copy the desired skill folders into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\* "$env:USERPROFILE\.codex\skills\"
```

If `CODEX_HOME` is set, use:

```powershell
Copy-Item -Recurse .\skills\* "$env:CODEX_HOME\skills\"
```

## Validate

If you have the Codex skill validator available, run it for each skill:

```powershell
.\scripts\validate-skills.ps1
```

Run the stronger smoke test to validate the repo-audit scripts and functional fixture generator:

```powershell
.\scripts\smoke-test.ps1
```

The decomp creation skills also include repo-audit scripts:

```powershell
python .\skills\make-matching-decomp\scripts\check_decomp_hygiene.py <repo>
python .\skills\make-matching-decomp\scripts\check_private_artifacts.py <repo>
python .\skills\make-matching-decomp\scripts\check_provenance_docs.py <repo>
python .\skills\make-functional-decomp\scripts\check_decomp_hygiene.py <repo>
python .\skills\make-functional-decomp\scripts\check_private_artifacts.py <repo>
python .\skills\make-functional-decomp\scripts\check_provenance_docs.py <repo>
```

## Repository Layout

```text
skills/
  make-matching-decomp/
  make-functional-decomp/
  pc-port/
  matching-decomp-port/
  functional-decomp-port/
  static-recomp-port/
  engine-reimplementation-port/
  source-modernization-port/
scripts/
  validate-skills.ps1
```

## License

MIT. See [LICENSE](LICENSE).
