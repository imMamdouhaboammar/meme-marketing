#!/usr/bin/env python3
"""Validate that meme-marketing is a self-contained, progressively disclosed Agent Skill pack."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


REQUIRED_DIRS = ("scripts", "references", "assets", "evals")
REQUIRED_FILES = (
    "SKILL.md",
    "scripts/validate.py",
    "scripts/meme-craft.ts",
    "references/runtime-contract.md",
    "references/workflow-recipes.md",
    "references/humor-mechanics.md",
    "references/format-bank.md",
    "references/caption-craft.md",
    "references/bineval-gates.md",
    "references/design-spec.md",
    "references/output-contract.md",
    "references/post-tuning.md",
    "assets/output-template.json",
    "assets/taste-profile.json",
    "evals/evals.json",
    "evals/fixtures/valid.json",
    "evals/fixtures/invalid.json",
)
LINK_RE = re.compile(r"\[[^\]]+\]\(((?:references|scripts|assets|evals)/[^)#]+)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for dirname in REQUIRED_DIRS:
        if not (root / dirname).is_dir():
            fail(errors, f"missing directory: {dirname}/")

    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            fail(errors, f"missing file: {filename}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(skill)
        name = fm.get("name", "")
        description = fm.get("description", "")
        if name != "meme-marketing":
            fail(errors, "frontmatter.name must be meme-marketing")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            fail(errors, "frontmatter.name violates Agent Skill naming rules")
        if not description or len(description) > 1024:
            fail(errors, "frontmatter.description must be 1..1024 characters")
        body_lines = skill.splitlines()
        if len(body_lines) > 500:
            fail(errors, f"SKILL.md is {len(body_lines)} lines; keep it at or below 500")
        for rel in LINK_RE.findall(skill):
            target = (root / rel).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                fail(errors, f"reference escapes skill root: {rel}")
                continue
            if not target.exists():
                fail(errors, f"broken local link in SKILL.md: {rel}")

    evals_path = root / "evals/evals.json"
    if evals_path.is_file():
        try:
            payload = json.loads(evals_path.read_text(encoding="utf-8"))
            if payload.get("skill_name") != "meme-marketing":
                fail(errors, "evals/evals.json skill_name mismatch")
            evals = payload.get("evals")
            if not isinstance(evals, list) or len(evals) < 3:
                fail(errors, "evals/evals.json must contain at least 3 evaluations")
            elif any(not item.get("assertions") for item in evals if isinstance(item, dict)):
                fail(errors, "every eval must contain assertions")
        except (OSError, ValueError) as exc:
            fail(errors, f"cannot parse evals/evals.json: {exc}")

    template_path = root / "assets/output-template.json"
    if template_path.is_file():
        try:
            template = json.loads(template_path.read_text(encoding="utf-8"))
            if template.get("skill") != "meme-marketing":
                fail(errors, "assets/output-template.json skill mismatch")
        except (OSError, ValueError) as exc:
            fail(errors, f"cannot parse assets/output-template.json: {exc}")

    validator = root / "scripts/validate.py"
    valid = root / "evals/fixtures/valid.json"
    invalid = root / "evals/fixtures/invalid.json"
    if validator.is_file() and valid.is_file() and invalid.is_file():
        good = subprocess.run(
            [sys.executable, str(validator), str(valid)],
            capture_output=True, text=True, timeout=30
        )
        if good.returncode != 0:
            fail(errors, f"valid fixture rejected: {good.stdout.strip()} {good.stderr.strip()}")

        bad = subprocess.run(
            [sys.executable, str(validator), str(invalid)],
            capture_output=True, text=True, timeout=30
        )
        if bad.returncode == 0:
            fail(errors, "invalid fixture unexpectedly passed structural validation")

    if errors:
        print("FULL PACK VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FULL PACK VALIDATION PASSED")
    print(f"- root: {root}")
    print(f"- required directories: {', '.join(REQUIRED_DIRS)}")
    print("- frontmatter and progressive-disclosure links: valid")
    print("- behavioral eval suite: present")
    print("- valid/invalid structural fixtures: behave as expected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
