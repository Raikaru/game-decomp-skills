#!/usr/bin/env python3
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening frontmatter delimiter"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, ["missing closing frontmatter delimiter"]
    raw = text[4:end]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, errors


def check_skill(skill_dir: Path) -> list[str]:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir}: missing SKILL.md"]
    fields, errors = parse_frontmatter(skill_file)
    prefix = str(skill_file)
    if "name" not in fields:
        errors.append("missing required field: name")
    elif fields["name"] != skill_dir.name:
        errors.append(f"name {fields['name']!r} does not match folder {skill_dir.name!r}")
    elif not NAME_RE.match(fields["name"]):
        errors.append(f"invalid skill name: {fields['name']!r}")
    if "description" not in fields:
        errors.append("missing required field: description")
    elif len(fields["description"]) < 40:
        errors.append("description is too short")
    extras = set(fields) - {"name", "description"}
    if extras:
        errors.append(f"unsupported frontmatter fields: {', '.join(sorted(extras))}")
    return [f"{prefix}: {error}" for error in errors]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills")
    failures: list[str] = []
    for skill_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        failures.extend(check_skill(skill_dir))
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("OK: skill frontmatter checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
