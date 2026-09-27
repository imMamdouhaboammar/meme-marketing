# Collision Engine: how the skill generates ideas that feel human

This file is the creative core of the skill. Read it on every CREATE, BATCH and TUNE run, and whenever an AUDIT finds that a meme is "correct but flat".

Language models write the most probable joke first. The most probable joke is the one the audience has already seen, so it gets a polite scroll and no share. Jentzsch and Kersting (2023) asked ChatGPT for 1,008 jokes and found that over 90% of them were the same 25 jokes. Zhong et al. (CVPR 2024, "Let's Think Outside the Box") showed that models get measurably funnier on the Japanese Oogiri game when they are trained to make remote associations and then filter them, instead of answering directly. The Collision Engine turns those findings into a procedure an agent can run in plain prompting.

The engine has five stages. Run them in order, privately, before writing any caption.

```
Insight dig  ->  Far-domain collision  ->  Mechanism & register pick  ->  Sharpen  ->  Kill the obvious
   (truth)          (surprise)                 (shape)                 (receipts)      (originality)
```

---

## Theory the engine is built on (short version)

| Theory | What it predicts | How the engine uses it |
|---|---|---|
| Incongruity-resolution (Suls 1972) | Laughter comes when the reader spots a mismatch and then resolves it in one step | Every idea must contain a mismatch **and** a fast resolution. Unresolved = confusing; no mismatch = a statement |
| Bisociation (Koestler 1964, *The Act of Creation*) | Creative jokes connect two self-consistent frames that never touch | Stage 2 forces a second frame from a distant domain |
| Script opposition, GTVH (Raskin 1985; Attardo & Raskin 1991) | A joke is six knobs: script opposition, logical mechanism, situation, target, narrative strategy, language | Stage 3 turns these knobs one at a time to create real variants |
| Benign violation (McGraw & Warren 2010) | Something must feel "wrong" and "okay" at the same time | Every idea gets a violation score and a safety score; both must be present |
| Debugging theory (Hurley, Dennett & Adams 2011, *Inside Jokes*) | We laugh when we catch a false assumption we had quietly committed to | Relatable posts work because the reader catches themselves in the act |
| Remote associates (Mednick 1962) | Creative people reach distant associations that others skip | Stage 2 bans the first three associations and asks for distance |
| Relief & pluralistic ignorance | Saying out loud the thing each person thought they did alone releases tension | Core engine of the "اه دا انا" post type, see [relatable-posts.md](relatable-posts.md) |

---

## Stage 1: Insight dig (find the private truth)

A meme without an insight is a template with words on it. The insight is a small true thing about the person that they recognize instantly and rarely say.

Dig with these ten lenses. Pick at least three per brief and write one line per lens.

| Lens | Question to ask | Deck example |
|---|---|---|
| Hidden habit | What do they do that they would never put in a CV? | "أي جملة بتبدأ بكلمة طاجن بتستحوذ على 95% من تركيزي" |
| Self-lie | What do they tell themselves that the calendar disproves? | "المهم انها اخر أيام الصيفية، كل حاجة بعد كده هتلاقيها متيسرة" |
| Brain math glitch | Where does their intuition fail in a funny way? | "هو انا ليه عندي قناعة ان الربع مليون جنيه أكتر من الـ 300 ألف" |
| Unwritten rule | What rule does everyone follow and nobody wrote down? | "الكل بيخاف يتنفس قدام بابا" / "اختي الصغيرة لما تطلب من بابا حاجة" |
| Betrayal moment | When does a tool, boss or relative flip on them? | "مش انت قولتلي هنبدأ بالساليري الصغير دا وهتزودني بعد تلات شهور" |
| Predictable relative | Which family member always does the same move? | "امي مع اخويا الصغير اللي بيطلع كل أسرارنا عشان يحلّي القاعدة" |
| Time freeze | Who still treats them like an older version of themselves? | "بابا دخل عليا الأوضة... قالي مافيش كلية بكرا؟ (انا متخرج أصلا)" |
| Tiny miracle | What small normal event feels like a miracle? | "لما أقول لأخويا يجيبلي حاجة من السوبر ماركت ويجيبها فعلا" |
| Energy budget | Where do they ration social or emotional energy? | "ما احنا لسه متكلمين من ٩ أيام هي شغلانة" |
| Status gap | Where does the gap between effort and reward show? | "20 ريل ولوجو وايدنتتي بـ 2700 جنيه" |

Write the insight as a plain sentence, in the audience's own words, before any joke. If you cannot write it in one sentence, the moment is too vague. Go back to [humor-mechanics.md](humor-mechanics.md) receipts.

**Insight quality check**

- **Recognition**: would 6 out of 10 people in this audience say "حصل معايا"?
- **Privacy**: is it slightly embarrassing or unspoken? Fully public facts ("الزحمة وحشة") give no relief.
- **Specificity**: is there one object, number, phrase, tool, time or person in it?

---

## Stage 2: Far-domain collision (where surprise comes from)

Take the insight and express it through a frame that belongs to a **distant** domain. The distance is what makes the reader's brain do the small jump that feels like a laugh.

### Procedure

1. Write the first three domains that come to mind for the insight. These are the obvious ones. **Discard all three.**
2. Pick two domains from the bank below that feel far from the insight. If the `meme-craft spark` command is available, run it and use the seeded suggestions; LLMs are poor at choosing randomly and a seed breaks the habit.
3. For each chosen domain, write one "bridge": the one shared property that lets the insight live inside that domain. The bridge must be something the audience already knows about that domain.
4. Keep the collision whose bridge is the most obvious **once you see it** and the least obvious **before** you see it.

### Far-domain bank

Group A, official voices: news bulletin, weather forecast, traffic report, government office form, school principal announcement, airline cabin announcement, court verdict, telecom offer, bank SMS, pharmacy leaflet dosage, customer-service IVR, terms and conditions, election result.

Group B, cultural scripts: Egyptian cinema line, football commentary, wedding invitation, proverb or حكمة, cooking recipe, horoscope, school exam question, mother's standard phrases, dad's standard phrases, neighbour gossip, taxi driver talk, real-estate listing.

Group C, tech and platform: software patch notes, error message, app permission dialog, sign-out button, loading bar, refresh, storage full, low battery, CAPTCHA, LinkedIn announcement, recommendation algorithm, read receipts, "seen" status.

Group D, nature and body: nature documentary narration, medical report, vitamin deficiency, sleep study, fitness tracker, zoo sign, animal behaviour.

### Collision examples from the deck, decoded

| Insight | Far domain | Bridge | Result |
|---|---|---|---|
| Too many responsibilities, want to quit life for a bit | Tech (account logout) | Both are sessions you entered and cannot leave | "أنا دخلت في مسؤوليات أكبر مني بالغلط، ازاي اعمل sign out" |
| Relatives who visit without warning | Classical wisdom list (فصحى) | Both are "things that arrive uninvited" | "هناك ثلاثة أشياء يأتون بلا موعد: الصحة، الرزق، أختي وعيالها" |
| Transport fares went up again | News anchor sign-off | Both deliver bad news politely | "مساء الخير: المواصلات عملالكوا سربرايز تحفة بكره، تصبحوا على خير" |
| Lonely and needs therapy, but broke | Telecom promo | Both are about packages and discounts | "طب ايه مافيش دكتور نفسي عامل عرض الصحاب أو عرض الشلة وكده؟!!" |
| Egyptian mornings are rough | Translation across three countries | Same concept, three registers | "🇺🇸 Bad news / 🇸🇦 أخبار سيئة ومشكلة كبيرة / 🇪🇬 صاحية" |
| Mum stopped praying for me personally | Social media habits | Reels replaced effort | "ماما بقت بتكسل تدعيلي فبتبعتلي ريلز لأمهات بتدعي لعيالها" |
| Wanting a fresh start while in debt | Instalment contract | Old life still has payments | "نفسي ابدأ حياة جديدة.. بس القديمة لسه عليها أقساط" |
| Need to throw the laptop away | Religious-style proverb about toxic people | "اعتزل ما يؤذيك" applied to an object | Laptop flying out of a window with the proverb as caption |

Notice how each result keeps the insight intact and changes only the **frame**. The frame supplies the surprise; the insight supplies the recognition.

---

## Stage 3: Mechanism and register pick (shape the joke)

Choose one mechanism from [humor-mechanics.md](humor-mechanics.md) (classic ten plus the deck-derived twelve) and one **register**. Register is the voice the line is written in. Many of the best deck posts come from a register that belongs somewhere else.

| Register | Where it comes from | When it works |
|---|---|---|
| فصحى / classical | Proverbs, textbooks, announcements | Trivial pain delivered with ceremony |
| News anchor | TV bulletin | Bad news the audience already expected |
| Self-help coach | Motivational posts | Tiny achievements treated as life lessons |
| Customer-service polite | Call centres, apps | Rejection or bad news sweetened |
| Mother's voice | Home | Guilt, food, marriage, calls |
| Father's voice | Home | Money, grades, sarcasm about work from home |
| HR / corporate | LinkedIn, offer letters | Low pay dressed as opportunity |
| Commentator | Football | Ordinary events narrated as live drama |
| Street Egyptian / Gulf casual | Friends | Honest confession |

Use GTVH knobs to build batch variety. For a batch of three, change **at least two** of these per variant: script opposition, mechanism, situation, target, narrative strategy (one-liner, list, dialogue, label, announcement), language/register. Changing only the words produces a rewrite of the same joke.

---

## Stage 4: Sharpen (make it land at feed speed)

1. **Receipt**: add one concrete detail. Numbers work best when they sound lived-in: "2700 جنيه", "9 أيام", "95%", "15 ساعة", "سبعين سنة". A precise but absurd number signals exaggeration faster than any adjective.
2. **Rhythm**: put the turn at the end. The last two to four words carry the surprise ("أختي وعيالها", "لسه عليها أقساط", "صاحية").
3. **Cut**: remove every word that does not change meaning. Most deck captions are under 20 words.
4. **Texture**: keep natural spoken spelling ("دا", "فـ", "عشان", "..", "!!") when the dialect is Egyptian. Keep Gulf texture ("الحين", "مره", "وش") when the dialect is Saudi. Never mix them.
5. **Line break as timing**: in text cards, a line break before the turn works like a comedian's pause.

---

## Stage 5: Kill the obvious (originality gate)

Before release, run three quick checks on every idea:

- **Predictability test**: cover the last line. Could a regular person in the audience guess it? If yes, the turn is too predictable. Return to Stage 2 and pick a more distant domain.
- **First-idea graveyard**: compare the idea against the three obvious ideas you discarded in Stage 2. If it overlaps with any of them, discard it.
- **Template echo test**: if the idea only works because of a famous format (Drake, distracted boyfriend) and has no insight underneath, it fails. The format should carry an insight, and never replace one.

Also reject lines that fall into AI rhetoric: denial-then-reveal contrasts, "when X meets Y" slogans, rhetorical questions that answer themselves, and forced puns that need explanation.

---

## Output of the engine (internal, before captions)

For each idea, the agent should hold:

```
insight:      one plain sentence in the audience's words
lens:         which Stage 1 lens produced it
far_domain:   the frame used, and the bridge
mechanism:    id from humor-mechanics.md
register:     voice of the line
turn_words:   the last words that carry the surprise
share_mode:   mirror (this is me) | arrow (this is you) | both
violation/safety: 1-5 each; both must be at least 3 and safety must be at least 4
```

Only after this block exists should the agent write the caption, on-image text and visual brief.

---

## Sources

- Jentzsch, S. & Kersting, K. (2023). *ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models.* WASSA @ ACL.
- Zhong, S. et al. (2024). *Let's Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Creative Humor Generation.* CVPR.
- Koestler, A. (1964). *The Act of Creation.*
- Suls, J. (1972). A two-stage model for the appreciation of jokes and cartoons.
- Raskin, V. (1985). *Semantic Mechanisms of Humor*; Attardo, S. & Raskin, V. (1991). Script theory revis(it)ed: joke similarity and joke representation model.
- McGraw, A. P. & Warren, C. (2010). Benign violations: making immoral behavior funny. *Psychological Science.*
- Hurley, M., Dennett, D. & Adams, R. (2011). *Inside Jokes: Using Humor to Reverse-Engineer the Mind.*
- Mednick, S. (1962). The associative basis of the creative process. *Psychological Review.*
- Canonical examples: the Meme Marketing master deck linked in [deck-patterns.md](deck-patterns.md).
