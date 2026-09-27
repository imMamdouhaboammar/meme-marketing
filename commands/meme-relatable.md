---
description: Write relatable "this is me" text posts that people repost or tag a friend on (CREATE route, relatable_post)
argument-hint: "<audience or page> [count] [dialect: egyptian|saudi|levantine|english] [platform]"
---

Use the meme-marketing skill in CREATE mode with `content_type: relatable_post` for this brief:

$ARGUMENTS

1. Read `references/relatable-posts.md` and `references/humor-engine.md` from the skill root.
2. Delegate insight mining to the `meme-moment-miner` subagent, passing the skill root path and asking for private-truth insights (hidden habits, brain glitches, family moves, energy budget).
3. Run `bun scripts/meme-craft.ts spark --mode relatable --count <n>` when a shell is available, and use the sparks as forced starting points.
4. For each post, choose one of the twelve formulas, write the line in spoken dialect with the turn in the last words, and state the share mode (mirror or arrow, and who gets tagged).
5. Run the relatable gates and the creative gates C1 to C3. Drop anything a reader could predict.
6. Deliver per post: insight, formula, post text, short social caption, card style, and a render command:
   `bun scripts/meme-craft.ts render --template text-card --style dark --name "<page name>" --handle "<page handle>" --text "<post text>" --out <file>.svg`

Use the page's own identity on cards. Never add a verified badge, a real person's name or handle, or invented like and share counts.
