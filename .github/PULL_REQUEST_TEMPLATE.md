## 🎯 Description of Changes

Explain what this PR introduces (e.g. new template, improved dialect nuance, anti-cringe rule refinement, bug fix).

## 🎭 Relatability & Comedy Check
- [ ] Does this change avoid corporate cringe and sales-pitch tropes?
- [ ] Are dialect idioms natural and unforced?
- [ ] If adding an SVG template, did you test rendering via `bun bin/cli.js render`?

## 🧪 Verification & Quality Checklist
- [ ] `bun run lint` passes with 0 warnings and 0 errors (Anti-slop Oxlint check).
- [ ] `python3 scripts/test_validate.py` passes all unit tests.
- [ ] `bun bin/cli.js validate evals/fixtures/valid.json` passes contract check.
- [ ] No secrets, credentials, or personal absolute paths included.
