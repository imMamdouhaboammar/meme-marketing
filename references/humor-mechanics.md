# Humor and image-text grammar

A good concept starts with a small observable tension. The humor mechanism, voice, visual form and image-text relationship are separate choices. Pick each independently.

## Mechanics

| Mechanism | Trigger | Typical payoff | Trap |
| --- | --- | --- | --- |
| Incongruous reaction | Small event, enormous expression | Familiar overreaction | Famous face chosen before the situation |
| Understatement | Disaster spoken about calmly | Audience fills the gap | Corporate "we remain committed" jargon |
| Exaggeration | Repeating real friction to absurd scale | Recognizable emotional truth | Fake statistics presented as evidence |
| Reversal | Routine event gets an unlikely outcome | Surprise through expectation | Forced binary "not X, Y" wording |
| Literalization | Mental or technical pain appears as a physical scene | Immediate visual recognition | Explaining the metaphor afterward |
| Role collision | People with incompatible everyday vocabularies meet | Two cultures clash in one frame | Generic "marketing vs design" without a concrete trigger |
| False confidence | A character sounds certain while the scene undermines them | Gentle self-own or institutional irony | Misrepresenting a real person |
| Escalation | Small request grows panel by panel | Accumulated absurdity | Panels without new information |
| Affectionate recognition | A surprisingly dependable friend or sibling | Delight at ordinary behavior | Assuming all memes require suffering |
| Visual misdirection | Caption suggests one image, composition reveals another | Fast surprise | Ambiguity that needs a long explanation |

The engine that decides which mechanism to use for an insight lives in [humor-engine.md](humor-engine.md). Read it first; this file is the catalogue.

## Deck-derived mechanics (v3.2)

These twelve mechanisms were extracted from the meme and relatable-post examples in the master deck (see [deck-patterns.md](deck-patterns.md)). They often produce stronger Arabic memes than the classic ten because they use cultural registers the audience already carries in memory. Use the ids in the `humor_mechanism` field.

| id | Mechanism | Trigger | Deck example | Trap |
| --- | --- | --- | --- | --- |
| `quote_transplant` | Film line re-homed | An iconic cinema or series line is moved into a new situation that fits it literally | Cheap competitor quote, image line: "الراجل دا كريم اوي يا بابا" | Line only works for people who know the scene; pick widely known lines |
| `register_hijack` | Wrong voice for the topic | فصحى, news anchor, دعاء formula or HR tone applied to a trivial pain | "مساء الخير: المواصلات عملالكوا سربرايز تحفة بكره" | Religious texts; keep to everyday phrases |
| `rule_of_three_break` | Third item derails | Two serious list items then one personal one | "الصحة، الرزق، أختي وعيالها" | Third item too random to resolve |
| `tech_vocab_life` | Software verb for life | sign out, refresh, update, storage full, loading used for a human state | "ازاي اعمل sign out" من المسؤوليات | Using jargon the audience does not use daily |
| `brain_glitch_confession` | Admitting faulty intuition | A belief the reader also holds, stated as a question | "الربع مليون أكتر من الـ 300 ألف" | Real ignorance about a sensitive topic |
| `absurd_precision` | Oddly exact number | Emotional truth measured with a fake exact figure | "95% من تركيزي", "بقالي سبعين سنة", "15 ساعة" | Number read as a real statistic |
| `cliche_literalized` | Cliché meets a real constraint | Self-help phrase gets a practical obstacle | "نفسي ابدأ حياة جديدة.. بس القديمة لسه عليها أقساط" | Cliché too rare to recognise |
| `mock_authority` | Tiny behaviour judged officially | Writer speaks like a principal, judge or manager | "لو جبتلي ولي أمرك ماهقبله" | Reads as genuinely aggressive |
| `time_freeze` | Someone stuck in your past | A parent or relative treats you like your younger self | "مافيش كلية بكرا ولا ايه (انا متخرج أصلا)" | Mocking the elder instead of the situation |
| `cross_market_translation` | Same concept in three voices | Flags or dialects, most honest one last | "🇺🇸 Bad news / 🇸🇦 أخبار سيئة / 🇪🇬 صاحية" | Punching at a nationality |
| `proverb_vs_visual` | Wise saying, literal picture | A proverb or advice line is illustrated literally by the image | "اعتزل ما يؤذيك" + laptop thrown out of a window | Explaining the literal link in text |
| `inner_monologue_reveal` | Polite outside, honest inside | Caption shows the public behaviour; image line is what the character actually thinks | Toxic manager: "متقلقش الـ Vibes هنا حلوة والـ Environment لذيذة" | Inner line that repeats the caption |

### Reaction-still anatomy from the deck

Almost every image meme in the deck follows one reliable structure. Use it as the default for reaction stills:

1. **Caption (above the image, in the post text)** sets the situation with "لما ..." or a quoted person, and ends with a colon.
2. **Image** is a recognisable face from Egyptian cinema, series, cartoons or a strong animal photo, with a clear emotion.
3. **On-image line (bottom, yellow or white bold text)** is spoken **by the character in the image** and adds new information: their excuse, their inner thought, their literal answer, or a labelled role ("انا مع الـ Layers").
4. **Small brand badge** in the top-left corner; no other branding.

The caption gives the cause, the face gives the emotion, the on-image line gives the twist. If any one of the three repeats another, cut it.

## Voices

Deadpan, weary, flustered, self-aware, smug, excited and mock-formal are delivery choices. An "angry designer" voice can use more than one comedic mechanism. Keep the chosen voice plausible for the person depicted, including dialect and seniority.

## Image-text relationships

- Reaction: caption supplies cause; a face supplies the emotion. On-image text optional
- Dialogue: caption names a speaker or trigger; in-image text is another actual speaker
- Labeling: short labels recast objects or participants; captions often unnecessary
- Understatement: picture shows high stakes; short text plays them down
- Literalization: visual embodies an abstract feeling or technical operation
- Delayed reveal: top panel sets one expectation; lower panel changes its meaning
- Intentional echo: the same phrase repeats because the second speaker or new context changes its meaning
- Text-free: a photo, screenshot, gesture or sequence can carry the full joke; optional accessibility alt text is external to the image

The two-mouth test applies to dialogue. For labeling, repeated words can be the joke. Text-free concepts do not need a fictional line inside the frame. The relation should add a second piece of meaning unless repetition is intentionally doing the work.

## Format selection

Reaction still, original actor scene, safe original illustration, staged screenshot, fake chat clearly marked as a constructed scene, accurately drawn UI, object labels, split panel, short video or pure-text joke are valid. A named template is a search cue unless usage rights are documented. Provide an original fallback that keeps the same mechanism without copying a recognizable character.

## Batch planning

For three concepts, prefer three different moments and at least two different mechanisms. Do not force numeric receipts, pain, a colon, a pun or a famous face into every concept. If the user explicitly requests variations of one concept, keep the same caption across alternate visual options so the comparison is meaningful.

## Quick counterexamples

Weak: "لما الشغل يبقى صعب" with an unrelated crying celebrity

Stronger illustrative setup: "لما الـ QA يرجعلك نفس الـ bug بعد ما قفلت التذكرة الساعة 11:57" with an original weary character staring at the green "resolved" label

Different direction: a staged chat of two colleagues who both think the other owns the same approval, with no reaction face

These are fictional examples of form, not claims about actual workplace events.
