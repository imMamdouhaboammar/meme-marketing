# Workflow recipes

Use this reference after routing. It contains route-specific procedures and explicit recovery paths.

## Contents

- CREATE
- AUDIT
- LOCALIZE
- TUNE
- BATCH
- RENDER
- Cross-route fallback matrix

## CREATE

### Inputs

Audience person, context, market/dialect, platform, topic/product, count, brand role, visual constraints.

### Procedure

1. Translate any broad demographic into one concrete audience person.
2. Mine 12-20 plausible micro-moments. Favor recurring actions, exact interface states, recognizable phrases, timestamps, tool names, or physical gestures.
3. Mark each receipt as brief-supplied, observed, researched, or illustrative.
4. Shortlist 3-5 moments by recognizability and send-to specificity.
5. Assign a different primary humor mechanic to each shortlisted concept.
6. Choose a visual form that naturally carries that mechanic.
7. Write caption and on-image text from two different informational roles.
8. Choose brand role. Default to none/prop unless the user's goal requires stronger product presence.
9. Run all applicable quality gates.
10. Deliver the requested count, not every private candidate.

### Recovery

- Generic premise -> replace audience category with a concrete moment.
- Same joke three times -> change mechanic before changing wording.
- Caption explains image -> remove explanation or change image role.
- Product becomes hero -> demote to prop/character.
- Unclear rights -> switch to original scene.

## AUDIT

1. Preserve the supplied meme before rewriting.
2. If JSON exists, run `python3 scripts/validate.py <file>`.
3. Evaluate the human gates one by one.
4. For every failure, provide evidence from the artifact and one targeted repair.
5. Repair only after the diagnosis is explicit.
6. Re-run affected gates.
7. If the premise itself fails the Send Test, replace the premise rather than line-editing it.

Return a concise pass/fail matrix only when the user asks for an audit; otherwise return the repaired artifact plus material caveats.

## LOCALIZE

Localization is reconstruction, not translation.

1. Identify the source meme's emotional mechanism.
2. Remove source-culture objects, idioms, celebrities, platform habits, and cadence that do not travel.
3. Identify an equivalent local micro-moment.
4. Rebuild spoken copy using `references/caption-craft.md`.
5. Replace receipts with local ones only when credible.
6. Keep protected names/brands only when the user supplied them or the reference is necessary.
7. Run dialect-integrity and dignity gates.

Recovery: if a cultural equivalent is uncertain, use a universal workplace/home/consumer moment in the target dialect instead of inventing a local fact.

## TUNE

1. Separate accepted, rejected, revised, and merely commented examples.
2. Extract the smallest preference supported by the feedback.
3. Scope it to creator/brand/audience/platform/locale where possible.
4. Mark weak inferences tentative.
5. Persist only through the documented taste-profile structure.
6. Apply the new preference to the current revision.
7. Never claim the profile proves what an audience generally likes.

## BATCH

1. Set batch objective and date/platform constraints.
2. Build a moment matrix before writing final copy.
3. Enforce diversity across mechanic, form, emotional state, and brand role.
4. Avoid repeating the same character/situation with synonym changes.
5. Reserve trend-dependent slots only when freshness can be checked.
6. Validate every machine-readable item.
7. Perform a batch-level repetition check.

A healthy batch should contain at least three distinct mechanics when three or more posts are requested.

## RENDER

1. Confirm copy is approved enough to render.
2. Choose a bundled original template or an original visual direction.
3. Check safe areas and text length with `references/design-spec.md`.
4. For bundled SVG output run:

```bash
bun scripts/meme-craft.ts render --template <name> [template options] --out <path.svg>
```

5. Verify the output file exists and is non-empty.
6. If rendering fails, do not fabricate success. Return the command error plus a complete designer brief.

## Cross-route fallback matrix

| Failure | Preferred fallback |
|---|---|
| Current trend cannot be verified | evergreen original micro-moment |
| Template rights unclear | original doodle or staged UI |
| Dialect feels translated | rewrite from target-culture moment |
| Too much copy | visual-only, object label, or one-line reaction |
| Product pitch overwhelms joke | brand role none/prop |
| Vulnerable subject becomes punchline | administrative/contextual friction or no joke |
| Renderer unavailable | production-ready visual brief |
| JSON validation fails repeatedly | fix contract first; do not render invalid data |
