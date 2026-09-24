#!/usr/bin/env python3
"""Focused security regression scan for executable runtime scripts in the meme-marketing skill pack."""
from __future__ import annotations

import re
import sys
from pathlib import Path


TARGETS = ("scripts/meme-craft.ts", "scripts/validate.py")
RULES = {
    "network execution primitive": [
        r"\bfetch\s*\(",
        r"\baxios\b",
        r"\bnode:https\b",
        r"\bnode:http\b",
        r"\bhttps?\.request\s*\(",
        r"\brequests\.",
        r"\burllib(?:\.request)?\b",
        r"\bhttpx\b",
        r"\baiohttp\b",
        r"\bsocket\b",
        r"\bcurl\s+",
        r"\bwget\s+",
    ],
    "arbitrary process execution primitive": [
        r"\bchild_process\b",
        r"\bBun\.spawn\b",
        r"\bDeno\.Command\b",
        r"\bos\.system\s*\(",
        r"\bsubprocess\.[A-Za-z_]+\([^\n]*shell\s*=\s*True",
    ],
    "secret-bearing environment access": [
        r"process\.env\.[A-Z0-9_]*(?:TOKEN|SECRET|API_KEY|PASSWORD)",
        r"os\.environ(?:\.get)?\([^\n]*(?:TOKEN|SECRET|API_KEY|PASSWORD)",
    ],
    "destructive shell pattern": [
        r"\brm\s+-rf\b",
        r"\bshutil\.rmtree\s*\(",
    ],
}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings: list[str] = []

    for rel in TARGETS:
        path = root / rel
        if not path.is_file():
            findings.append(f"{rel}: missing runtime script")
            continue
        text = path.read_text(encoding="utf-8")
        for label, patterns in RULES.items():
            for pattern in patterns:
                if re.search(pattern, text, flags=re.I):
                    findings.append(f"{rel}: {label} matched /{pattern}/")

    if findings:
        print("SECURITY SCAN FAILED")
        for finding in findings:
            print(f"- {finding}")
        print("Runtime scripts must remain offline, non-shelling, and free of secret-bearing environment access.")
        return 1

    print("SECURITY SCAN PASSED")
    print("- runtime scripts inspected: " + ", ".join(TARGETS))
    print("- no network execution primitives detected")
    print("- no arbitrary process execution primitives detected")
    print("- no secret-bearing environment access detected")
    print("- no destructive shell patterns detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
