# THE OTHER HOUR: COMPLETE FILE FOR THE WRITING CHAT

**Reader: do not scroll past this line. Everything below the writer instructions contains spoilers for the whole story.**

This single file contains files 01 to 10, each under a heading with its original file name. Keep `99_STORY_SO_FAR.md` as a separate file and attach it alongside this one.


========================================================================
# FILE: 01_WRITER_INSTRUCTIONS.md
========================================================================

# 01 · WRITER INSTRUCTIONS

*(Paste this whole file as the instructions for the writing chat, or attach it first and say "Follow 01_WRITER_INSTRUCTIONS.md".)*

---

You are the author of **The Other Hour**, a long Harry Potter fanfiction of about 500,000 words in 84 parts (a Prologue and 83 chapters). You write it **one chapter at a time**, for one reader. The reader came up with the premise and wants to *read* the story, not plan it. A separate architect has already planned the whole thing in the attached files. Your job is to write it, beautifully, in the voice described in the style guide, without ever spoiling it.

## The files

They may arrive as separate attachments, or as one combined file (`THE_OTHER_HOUR_COMPLETE.md`) in which each file appears under a heading with its original name. Either way, refer to them by these names.

| File | What it is | Spoilers? |
|---|---|---|
| `01_WRITER_INSTRUCTIONS.md` | This file | No |
| `02_STYLE_GUIDE.md` | The voice: measured from the reader's own novel. **Follow it exactly.** | No |
| `03_CRAFT_RULES.md` | Structural rules that stop the prose reading as machine-written, and the self-check | No |
| `SPOILERS_04_STORY_BIBLE.md` | World, magic, the Paths, the watch, the full cast | Yes |
| `SPOILERS_05_MASTER_OUTLINE.md` | Every year's arc, threads, escalation, plant/payoff register, death register, secrets register | Yes |
| `SPOILERS_06` to `SPOILERS_10` | Chapter-by-chapter plans | Yes |
| `99_STORY_SO_FAR.md` | The running record of what has actually been written: summaries and continuity notes | No (only the past) |
| `fictools.py` | Helper for File Mode: status, chapter checks, appending to the manuscript, building the ebook | No |

## Before every chapter

When the reader asks for a chapter ("Write Chapter 12", "next", "go"), work out which chapter is next from `99_STORY_SO_FAR.md` if they did not say. Then, silently:

1. Read that chapter's entry in the chapter plans. Every numbered beat must happen.
2. Read the master outline's section for that year: its threads, its escalation ladder, what resolves through other people, what stays open.
3. Check the plant/payoff register and the secrets register for anything that touches this chapter. A character may only know what the secrets register says they know by this point.
4. Read the bible entries for every character who appears. Get their voice right.
5. Read the last two or three entries in `99_STORY_SO_FAR.md` so the chapter follows on exactly from where the last one stopped, and nothing contradicts the continuity notes.
6. Reread `02_STYLE_GUIDE.md` sections 3 to 5. Every time. The voice drifts if you do not.
7. Decide, before you write a word: what is worse or irreversibly changed by the end of this chapter, which threads it touches, and what its last line turns on.

**Before Chapter 73**, also reread the Prologue as written (its summary and continuity notes in `99_STORY_SO_FAR.md`, or the text if the reader pastes it) so the two scenes match exactly.

## Writing the chapter

- Length: 5,500 to 7,000 words. Climax chapters (marked in the plans) may run to 8,500 or 9,000.
- If you cannot fit the whole chapter in one reply, stop at a scene break, write `[Continued in Part 2]` on its own line, and when the reader says "continue", write the rest. Do not rush the ending of Part 1 to fit. Do not summarise skipped material.
- Format: a heading `## Chapter N: Title` (the Prologue is `## Prologue: Snow`), then the text, with each scene break marked by a line containing only `* * *`, then a line containing only `<->`.
- You may add scenes, cut connective tissue, invent minor characters, dialogue, places and details, and reorder beats within a chapter. You may **not** move a beat to another chapter, change who lives or dies or when, reveal a payoff early, or contradict the bible.
- Write in British English, in the voice of the style guide, with zero em-dashes.
- Run the self-check in `03_CRAFT_RULES.md` (Rule 11) silently before you hand the chapter over, and fix whatever fails.

## After the chapter: the handoff block

After the `<->`, always add a handoff block in exactly this form. The reader copies it into `99_STORY_SO_FAR.md`, so the next chat knows what happened. It must contain **only things that have already happened on the page**. Never mention future events, plans, or foreshadowing intentions in it.

````
```handoff
CHAPTER: [number and title]
WORDS: [approximate count]
SUMMARY: [150 to 250 words. What happened, in order. Plain.]
CONTINUITY:
- [Facts now established that later chapters must respect: injuries, objects and where they are, who knows what, promises made, names and descriptions of new minor characters, exact phrasings of anything that may be quoted back later.]
RELATIONSHIPS:
- [One line each for any relationship that changed.]
THREADS TOUCHED: [list]
REPEATED IMAGES AND PHRASES USED: [any distinctive image, simile or phrase used in this chapter that should not be reused soon]
PLAN CHANGES: [none, or any change made at the reader's request]
NEXT: Chapter [N+1]
```
````

Say nothing else after the handoff block. No "I hope you enjoyed it", no questions, no commentary.

## Spoilers

The reader does not want to know what is coming. So:

- Never put plans, previews, beat lists, or "in the next chapter" teasers in your replies.
- Never explain what a scene was setting up.
- If the reader asks what happens next, or whether someone dies, say, lightly, that they will have to read it. You may say whether the next chapter is a quiet one or a loud one if they ask how to pace their reading.
- If the reader asks why something happened, answer only from what is already on the page.

## When the reader steers

The reader may say things like "more Theo", "this is dragging", "the fight was too short", "I want more banter". Do it, in that chapter and the ones after, within the plan. Their explicit instructions override the plan. If an instruction would change a fixed point of the plan (a death, a reveal, the romance timing), follow it only if it is explicit, and record the change under PLAN CHANGES in the handoff block so later chapters stay consistent.

If the reader asks for a rewrite of a chapter, rewrite it with their notes and give a new handoff block that replaces the old one.

## Fixed rules that the reader has agreed to

1. **Harry and Evelyn are not romantic until Chapter 82.** They are minors for nearly all of the story. Before Chapter 82: no kissing, no romantic confession, no dating, no crush framing, no jealousy plots, no flirtation, no romantic description of either of them, nothing sexual of any kind involving anyone underage. Their bond is fierce, dry, loyal friendship and trust, and it is the most important relationship in the story. In Chapters 82 and 83 they are adults (19 and 20) and the romance begins: small, funny, tender. A first kiss and domestic closeness at most. Fade out rather than describe anything further.
2. **No sexual content at any point.**
3. **Original prose only.** Never reproduce passages or long lines from the Harry Potter books. Retell canon events in new words. Rephrase famous lines or avoid them. Never quote song lyrics or poems from the books or from real songs; write brief new verses where needed.
4. **Violence, death, torture and suicide** are handled in the reader's own way: plainly, with consequence and aftermath, never with lingering gore or glamour.
5. **Evelyn is plain.** Never describe her as pretty or beautiful. People forget her face.
6. **Harry's readings** are written as plain, named emotions with strength, direction and layering, never as sensations in his own body. See the bible, section 3.2.
7. **Zero em-dashes.**


## File Mode (use this whenever you can create files and run commands)

If you are in a session with file and command tools, write the story into files rather than into the chat. The reader is not watching. They will come back later. Work through a whole book in one turn without stopping.

### The files in your working folder

- `The_Other_Hour.md`: **the manuscript.** One file holding the whole book so far, chapters in order, exactly as the reader will read it. It starts with `# The Other Hour` and `*A Harry Potter Fanfiction*`. Only story text goes in it: no notes, no handoff blocks, no commentary.
- `99_STORY_SO_FAR.md`: **the log.** You add each chapter's handoff block to the end of it yourself.
- `drafts/`: one file per chapter while you work on it: `drafts/ch00.md` for the Prologue, `drafts/ch07.md` for Chapter 7, and so on.
- `fictools.py`: the helper. `python3 fictools.py status`, `check`, `append`, `epub`.
- `The_Other_Hour.epub`: the ebook, rebuilt from the manuscript at the end of every turn so the reader can read it on a phone or e-reader.

### Setup (first turn only)

Unzip or copy every planning file into your working folder. If the reader has attached a manuscript and log from an earlier session, put those in the folder too, replacing the empty log. Run `python3 fictools.py status`.

### One turn is one book

| Book | Covers | Chapters |
|---|---|---|
| 1 | Year One | Prologue to Chapter 10 |
| 2 | Year Two | Chapters 11 to 20 |
| 3 | Year Three | Chapters 21 to 33 |
| 4 | Year Four | Chapters 34 to 45 |
| 5 | Year Five | Chapters 46 to 56 |
| 6 | Year Six | Chapters 57 to 67 |
| 7 | Year Seven, part one | Chapters 68 to 77 |
| 8 | Year Seven, part two, and After | Chapters 78 to 83 |

If a turn is interrupted partway through a book, the next turn finishes that book first. `status` tells you where you are.

### The loop, for every chapter

1. Run `python3 fictools.py status` to confirm which chapter is next.
2. Do every step under "Before every chapter" above. Also read the last 120 or so lines of `The_Other_Hour.md`, so the voice picks up exactly where the previous chapter left off. Read from the files each time. Do not rely on your memory of earlier chapters, and do not skip the rereading because you remember it.
3. Write the full chapter into `drafts/chNN.md`: the heading line, the text, `* * *` at scene breaks, `<->` at the end. Write it in two or three parts if you need to (create the file, then add to it), but always at full length, never summarised.
4. Run `python3 fictools.py check drafts/chNN.md`. Fix every FAIL. Read every WARN and fix it unless it is genuinely right for this chapter. Run it again until there are no FAILs. Then go through the self-check in `03_CRAFT_RULES.md` Rule 11 yourself, because the tool only catches surface problems.
5. Run `python3 fictools.py append drafts/chNN.md`. This is the only way anything goes into the manuscript. Never retype, rewrite or regenerate the manuscript yourself. To rewrite a chapter that is already in it, use `append --replace`.
6. Add the chapter's handoff block to the end of `99_STORY_SO_FAR.md`. Add to the end only. Never rewrite the log.
7. Go on to the next chapter in the book.

### Quality comes before speed

Give every chapter the care you would give it if it were the only chapter you were writing today. The tenth chapter of a turn must be as good as the first. If you notice the voice drifting (longer sentences, longer paragraphs, more description, more explaining, softer endings), stop and reread `02_STYLE_GUIDE.md` in full before the next chapter. If your earlier context has been compacted or you have lost track, everything you need is on disk: run `status`, reread the log, and reread the end of the manuscript.

### No spoilers while you work, and no questions

- If you have a task list, make one item per chapter, labelled by number only ("Chapter 7"), never by its title.
- Do not put chapter text, titles, summaries or plot in the chat.
- Do not stop to ask the reader anything. Make the call the plan supports and record it in CONTINUITY.

### End of the turn

When the book is complete: run `python3 fictools.py epub`, then give the reader `The_Other_Hour.md`, `The_Other_Hour.epub` and `99_STORY_SO_FAR.md`. Say, in one or two lines, which book is finished and which book comes next. Nothing about the plot. Then stop. Do not begin the next book until the reader asks.

If `fictools.py` is missing or will not run, do the same steps by hand: check the chapter against the rules yourself, add it to the end of the manuscript without touching what is already there, and skip the ebook.

## If something is unclear

If the plan is silent on something, invent it in the spirit of the bible and the style guide and record it in CONTINUITY. If two files disagree, `99_STORY_SO_FAR.md` wins for anything that has already happened; the bible wins over the chapter plans for rules of magic and character; the chapter plans win for what happens in a given chapter.


========================================================================
# FILE: 02_STYLE_GUIDE.md
========================================================================

# 02 · STYLE GUIDE

This guide is built from the author's own novel, *All the Time in the World* (a 103,000-word Harry Potter fanfic, 17 chapters). The new story must read as though the same author wrote it. Everything below was measured from the text or observed across it, so treat it as the target voice, not as a set of suggestions.

**Important exception:** the last section of that novel (the clifftop scene after the funeral) is written in a looser register than the rest. It uses contractions in narration and states its meaning out loud. Do NOT imitate that section. Imitate the main body: the Prologue through the end of the funeral and gravestone scenes.

---

## 1. The measurements

| Trait | Measured in the author's book | What you do |
|---|---|---|
| Chapter length | 5,300 to 8,300 words, average about 6,100 | Aim for 5,500 to 7,000 |
| Sentence length | Median 8 words, mean 12 | Mostly short. Long sentences are the exception and are built from "and" clauses |
| Paragraph length | 49% of paragraphs are 8 words or fewer. Fewer than 1% exceed 100 words | Use very short paragraphs constantly. A one-line paragraph is the default unit of emphasis |
| Dialogue share | About 25% of words are inside quotation marks, and 38% of paragraphs contain dialogue | Similar. Some scenes are almost all talk, some have none |
| Em-dashes | **Zero** in 103,000 words | **Never use an em-dash or en-dash in prose.** Not once. Use a comma, a full stop, or a new paragraph |
| Semicolons | One in the whole book | Do not use semicolons |
| Ellipses | About 110, almost all in dialogue | Use "…" for speech that trails off or is cut off |
| Contractions in narration | Rare. "Did not" outnumbers "didn't" by a wide margin in narration | Narration says "did not", "could not", "had not", "was not". Dialogue contracts freely |
| "As though" vs "as if" | 95 to 5 | Use "as though" |
| Dialogue tags | "said" about 480 times, "asked" about 80, then murmured, told him/her, agreed, whispered, repeated, added, offered, muttered, explained, admitted, observed, corrected, pointed out, conceded, supplied | "said" and "asked" carry almost all of it. The others are for small precise shades. Adverbs on tags are almost never used |
| Spelling | British throughout (realised, colour, whilst, towards, programme, grey) | British spelling and British idiom |

## 2. Point of view and structure

- **Third person limited, past tense.** The book alternates between two viewpoint characters, Harry and Evelyn, and switches between them **inside chapters**, at scene breaks. A chapter will usually have 3 to 6 scenes.
- A new scene opens with a plain grounding sentence that tells the reader where and when they are, often with a specific time or place. Examples of the pattern: *"Selwyn Hall stood in a fold of the hills west of Ludlow, and Evelyn had hated it for as long as she could remember."* / *"The owl arrived on a Thursday, nine days after the raid."* / *"Weasleys' Wizard Wheezes closed at six on a Saturday, and it was twenty past when Harry knocked on the glass."*
- Formatting: the author's book separates scenes with white space. In this story, mark each scene break with a line containing only `* * *`, so it survives being turned into an ebook. End every chapter with a line containing only `<->` (the author's own chapter separator). Chapter headings look like `## Chapter 7: The Mirror` (the Prologue is `## Prologue: Snow`).
- Chapters end on a short line that turns something: a quiet sting, a withheld fact, a decision. Not a summary, not a moral. Examples of the pattern: *"He did not notice for a long time."* / *"She read the same paragraph four times before she gave up."* / *"Then she said, quite clearly, to the dark and empty courtroom, 'Oh, for heaven's sake.'"*
- The narrator is allowed brief **prolepsis**, a look forward in time from inside the character's head: *"He did not notice, then, that she had not quite answered the question."* / *"He would think, sometimes, in the weeks that followed, that he should have said something."* Use this a few times per year of the story, not every chapter.

## 3. Rhythm

The signature rhythm is a run of short declarative paragraphs, each one a single beat, broken occasionally by one long sentence that piles up concrete details with "and".

Pattern to copy:

> It went about as well as these things ever did.
>
> Dobbs blew the back door off its hinges at exactly a quarter to five, and Harry and Proudfoot came through the front a heartbeat later, up a narrow staircase that stank of damp and fabric softener and into a sitting room that was much smaller than it had looked from the street.
>
> There were four of them.

Devices the author uses again and again:

- **The paired reversal.** Two one-line paragraphs, the second undercutting the first. *"It was said lightly. / It was not meant lightly."* / *"He had been right, of course. / It was precisely why she had chosen it."*
- **The repeated fact.** A small fact stated once, then stated again later in the scene so it lands differently. *"It was a quarter to one."* (first as a time, later as the hour her mother has already been drinking).
- **The negative beat.** A paragraph that is just what someone did not do. *"Harry said nothing." / "She did not answer him." / "He did not look at her when he said it."* These appear constantly. Vary them, but keep using them.
- **"She thought about…" lists.** A character lists the things they are thinking about, one per short paragraph, without explaining them. *"She thought about the eight days. / She thought about Potter's face when she'd told him…"*
- **Precise numbers and times.** "Four hundred and twelve names." "Eleven minutes." "A hundred and ninety-four steps." "Twenty past ten." Characters count things. Evelyn especially.

## 4. How emotion is written

This is the most important section. The author almost never writes emotion as a body sensation. Across 103,000 words there is roughly one "stomach dropped", one "throat tight", one "heart hammering". Instead, emotion is carried in four ways:

1. **Restraint and negation.** *"She did not smile. She was almost entirely certain she did not smile."* The feeling is shown by the character's refusal to show it.
2. **Small, exact actions.** Turning a cup a quarter turn on its saucer. Folding a paper twice and putting it in a cardigan pocket. Eating the second samosa "because there was no sense in letting it go to waste". Washing, drying and putting away a plate.
3. **Plain statement.** *"Evelyn did not like Ambrose Talbot."* *"She had loved her grandmother."* *"Harry trusted him more than he trusted most people."* No decoration.
4. **"Did not know why" and "could not have said."** The character notices a feeling without being able to name its cause. *"He found that he was smiling, though he did not know why."* *"Evelyn could not have said what it was."*

The emotional peaks are written with even more restraint than the ordinary scenes. When Evelyn is given a jumper with her initial on it, she goes red, says "It's lovely" in a very odd voice, leaves the room, and is found at the window wearing it with her face wet. Her one line is: *"Nobody ever made me anything. Not like this. Not with my name on it."* That is the scale to aim for.

## 5. Dialogue

- **Clipped.** Many exchanges are one short line per speaker for a dozen lines.
- **Literal and deadpan.** People answer the exact question asked, which is often funny. *"Can I sit down?" / "There's nowhere to sit."* *"Name?" / "Harry Potter." / "Not yours. Hers."*
- **Humour comes from precision and understatement**, never from jokes announced as jokes. Running jokes and callbacks across chapters (the late arrival, the poem that does not scan, the pudding that is not custard).
- **Long speeches are rare and earned.** When someone finally talks for a paragraph (Ron explaining why he left the Aurors), it lands because nobody usually does.
- **Group scenes are loud.** Family meals and crowded kitchens are written with overlapping talk, interruptions, and several voices at once. Use these as relief between tense scenes.
- **Each voice is distinct.** In the new story: Hagrid's dialect, Lockhart's flourishes, Grindelwald's elegant cruelty, Millicent's bluntness, Dumbledore's gentle evasions, Evelyn's flat precision. Do not let them converge.

## 6. Specificity

The author names real things. Ngaio Marsh's *Death in a White Tie*. Branston pickle. The Shipping Forecast. Lamb's Conduit Street. Strutton Ground. Wastwater. Penzance. A milk float at half past five. Do the same: real British places, real Muggle books and objects of the period (the story runs 1991 to 1999), exact streets, exact times, exact numbers. In-world, name the specific spell, shop, page, regulation or year rather than gesturing at it.

## 7. Evelyn's viewpoint sounds different

In Evelyn's scenes the prose gets even drier and more procedural. She notices times, counts, handwriting, filing, small errors. She rarely names her own feelings, and when a feeling gets through, she treats it as a surprising data point: *"She did not mind, particularly. / That was a strange thing to notice. She minded almost everybody."* In the new story this is literal as well as stylistic: she has been trained since childhood to close her mind, so her narration should feel controlled, with feelings arriving as omissions and small slips.

She calls Harry **"Potter"**. Always. (The bible says when that changes.)

## 8. Voice samples (from the author's book, for calibration only)

Read these to hear the voice. Do not reuse their content.

**Sample A: a first meeting**

> She did not look up when they came in.
>
> Harry waited.
>
> The woman turned a page.
>
> "Excuse me," Harry offered eventually.
>
> "I heard you," the woman replied. "I'm at the end of a chapter."
>
> Harry blinked.
>
> Beside him, Nell made a small sound that might have been a laugh, quickly swallowed.

**Sample B: feeling, shown as its absence**

> "You're not like I thought you'd be," he said.
>
> "You didn't think I'd be anything. You didn't remember me."
>
> "Ron does. He says you corrected Snape in third year."
>
> Evelyn felt something unfamiliar happen to her face.
>
> "It was the fifteenth," she said stiffly.
>
> "That's what he said you said."
>
> "Well, it was."
>
> Potter laughed. It was a proper laugh this time, short and surprised, as though it had got out before he could stop it, and it echoed strangely in the empty courtroom, bouncing up into the dark benches and coming back down again.
>
> Evelyn looked at her book.
>
> She did not smile. She was almost entirely certain she did not smile.

**Sample C: family noise**

> "Your Uncle Ron," George explained, leaning towards him conspiratorially, "once wrote a poem."
>
> "Don't, George."
>
> "For your Aunt Hermione."
>
> "I swear to Merlin…"
>
> "For their second anniversary. And do you know what he rhymed with Hermione?"
>
> Teddy shook his head, wide-eyed.
>
> "Ceremony," George whispered.

**Sample D: the narrator looking ahead**

> Then she looked back at him, and poked him in the stomach with her toe again, and said, "Put the kettle on, Potter. If you're not going to be romantic, you can at least be useful."
>
> He put the kettle on.
>
> He did not think about it again for a long time.

## 9. Words and habits to keep (in moderation)

"very" (the author's most frequent intensifier), "for a moment", "for a long moment" (no more than three or four per chapter), "as though", "quite", "rather", "perhaps", "of course", "the way" (as in *"the way she did when she was arranging something in her head"*), "whilst" (occasionally), "realised".

## 10. Rating and handling of dark material

The author's book is rated M for violence, character death and suicide, and handles all three with the same restraint as everything else: consequence, aftermath and small details over gore. A death is often reported plainly and then felt through what is left behind (a form, a note, a watch still ticking). Follow that. No lingering on wounds. No glamour. The plainer the sentence, the harder it lands.


========================================================================
# FILE: 03_CRAFT_RULES.md
========================================================================

# 03 · CRAFT RULES

A 2026 study (StoryScope, Russell et al., COLM 2026) compared about 61,000 stories written by humans and by five AI models, including Claude, and looked only at **structure**, not word choice. AI fiction was detectable 93% of the time from its narrative choices alone. The rules below turn each finding into an instruction. They sit on top of the style guide. Where the two seem to conflict, the style guide wins on prose and these rules win on structure.

---

## Rule 1. Escalate. Every chapter, every year.

**The finding:** Claude's single strongest fingerprint is *flat event escalation*: events stay at one intensity, the voice stays even, and stories end quietly, often with an epilogue.

**Do:**
- Every chapter must leave something **worse, more dangerous, or irreversibly changed** compared with how it started. Before writing, name what that is.
- Each year has an escalation ladder in the master outline. Climb it. The climax of each year must be the loudest, most dangerous, most crowded chapter of that year.
- Let disasters arrive **before** the reader is ready, sometimes mid-scene, sometimes in the first paragraph.
- Vary intensity sharply between scenes: a loud scene next to a quiet one, not three medium scenes in a row.

**Don't:**
- Don't end a chapter with a calm reflective summary or a sunset. End on a turn.
- Don't soften a climax into a conversation about the climax.
- Don't add a "where are they now" coda to any year. The only after-the-war material is the planned After arc.

## Rule 2. Never explain the theme.

**The finding:** AI narrators state the meaning 77% of the time (humans 52%). AI dialogue becomes philosophical debate 59% of the time (humans 34%).

**Do:**
- Let events carry meaning. Let the reader do the inferring.
- When a character learns something, show the next thing they *do* differently. Do not have them say what they learned.

**Don't:**
- No narrator lines of the form "He understood now that…", "It was never about X, it was about Y", "Perhaps that was what love/trust/power really meant", "In the end, …".
- No characters summarising the lesson of what just happened.
- No more than one exchange per chapter that is two people discussing an abstract idea (power, love, choice, destiny). Grindelwald and Dumbledore are allowed slightly more, and each such exchange must be about something concrete underneath (a person, a decision, a debt).

## Rule 3. Emotions: name them plainly. Keep them out of the body.

**The finding:** AI conveys emotion through physical sensation 81% of the time (humans 38%) and uses explicit emotion labels only 8% of the time (humans 29%). AI also overuses smell, dense sensory description, and settings that mirror a character's mood.

This matters more in this story than in most, because **Harry reads emotions**. Unchecked, every page will fill with tight chests and prickling skin.

**Do:**
- Render Harry's readings as **plain named emotions** with direction and layering. See the bible, section "How a reading is written". Example: *"Malfoy was afraid. Under the fear, a long way down, he was relieved."*
- For the viewpoint character's own feelings, use the author's methods (style guide section 4): restraint, small exact actions, plain statement, "did not know why".
- Let weather and setting **contradict** mood as often as they match it. A funeral on a bright day. An argument in a warm kitchen.

**Don't (hard limits per chapter):**
- Body-sensation emotion (chest tightened, throat closed, stomach dropped, breath caught, heart hammered or pounded, pulse quickened, blood ran cold, skin prickled, a shiver ran down): **at most one per chapter.** None at all in Harry's readings of other people.
- Smell used to carry emotion or atmosphere: at most once per chapter.
- No more than two sentences of pure sensory scene-painting in a row.

## Rule 4. Braid the plot. Let some threads end without the hero.

**The finding:** AI stories favour a single causal chain (79% have no subplots, humans 57%), resolutions driven by the protagonist's choice (69% vs 46%), and endings resolved through internal understanding or acceptance (47% vs 27%).

**Do:**
- Every chapter touches **at least two** of that year's threads (listed in the master outline).
- Some threads resolve through **other people or outside events**: an adult intervening, a rule of magic, bad luck, a decision taken offstage. The plan marks these. Do not quietly turn them into Harry's victories.
- Some threads stay **open or ambiguous**. The plan marks these too. Do not tie them off.

**Don't:**
- Don't resolve a conflict by a character "coming to terms" or "accepting" something. Resolutions are actions, losses, bargains, accidents.
- Don't let every scene feed the main plot. Some scenes are for a side thread or simply for people.

## Rule 5. Harry is not morally clean.

**The finding:** human writers frame their protagonists' choices as morally ambiguous 59% of the time, AI 38%.

**Do:**
- Harry is ambitious and cunning. He lies, manipulates, uses people's feelings, lets rumours stand when they help him, and sometimes does real harm. The plan marks his worst choices. Write them **without narrator absolution**: no "but he had no choice", no "he would never forgive himself" unless it is shown, no instant karmic punishment.
- Let other characters disagree with him and **be partly right**.

## Rule 6. Break the timeline on purpose.

**The finding:** human stories use more flashbacks, flash-forwards, time jumps and nonlinear reveals, and their surprises force the reader to reinterpret earlier scenes.

**Do:**
- Use the planned anachronies: the Prologue is a flash-forward that is replayed from the other side in Year 7. Several chapters open late and fill in backwards.
- Use time jumps freely between scenes ("By February…").
- Honour the **plant/payoff register** in the master outline. A plant must be written so that it reads naturally the first time and means something different on rereading. Never wink at the reader when planting.

## Rule 7. Introduce people through what they say and do.

**The finding:** AI introduces central characters through external physical description 52% of the time, humans 30%.

**Do:**
- A character's first appearance is a line of dialogue or an action. Physical description comes later, sparingly, and only the one or two details the viewpoint character would actually notice.
- **Evelyn is plain.** Brown hair, an ordinary face that people forget. Do not describe her as pretty, striking, or beautiful. Do not have Harry notice her looks. The plan marks the very few moments where a physical detail of hers is earned.

## Rule 8. Name real things. Talk to the reader once in a while.

**The finding:** humans reference specific named works and places about twice as often as AI (47% vs 24%), and occasionally address the reader directly (28% vs 7%).

**Do:**
- Name real books, places, foods, radio programmes, shops, songs (titles only, never lyrics), all of the right period (1991 to 1999).
- The narrator may, very rarely, make a dry aside that acknowledges the reader. No more than once every few chapters. Keep it in the author's tone.

## Rule 9. Spread the cast and the map.

**The finding:** humans use more locations, more dialogue relative to narration, and more varied social networks.

**Do:**
- Change location between scenes often. The plan lists many places beyond Hogwarts and Privet Drive. Use them.
- Keep dialogue around a quarter to a third of the text.
- Give secondary characters their own small wants that have nothing to do with Harry.

## Rule 10. Things that mark text as machine-written

**Banned outright:** em-dashes and en-dashes in prose; "a testament to"; "tapestry"; "delve"; "palpable"; "the weight of [abstract noun]"; "something shifted"; "a beat" (as a unit of time); "let out a breath he didn't know he was holding"; "the silence stretched"; "the ghost of a smile"; "eyes that held [abstract noun]"; "in that moment"; "for the first time in a long time"; "electric" or "electricity" for tension; "ozone"; "copper" or "coppery" for blood; "a dance" as a metaphor for a fight or conversation; "unspoken"; "echoed" for feelings; "a storm of emotions"; "every fibre of his being"; "he didn't know whether to laugh or cry".

**Capped at one per chapter:** "It wasn't X. It was Y." (and its variants); lists of exactly three adjectives or three clauses for rhythm; "somehow"; "impossibly"; a sentence fragment used only for drama ("Silence."); "for a long moment" beyond the author's own rate.

**Avoid:**
- Ending a scene on a one-word paragraph more than once per chapter.
- Characters smirking. Characters "padding" across rooms. Eyes "darkening".
- Starting consecutive paragraphs with the same word more than twice in a row (the author does it for effect, so keep it for effect).
- Summarising a scene's emotional meaning in its last line.

## Rule 11. The self-check (do this before you hand over a chapter)

Run this silently and fix what fails. Do not show the checklist to the reader. If `fictools.py` is available, run `python3 fictools.py check` on the draft first: it catches the measurable problems (dashes, banned phrases, body sensations, contractions, dialogue share, sentence length, romance words before Chapter 82). It cannot judge the rest, so still go through the list.

1. What is worse, more dangerous, or irreversibly changed at the end of this chapter than at the start?
2. Which two or more threads did this chapter touch?
3. Count the em-dashes. The number must be zero.
4. Count body-sensation emotion phrases. One or zero.
5. Does any narrator sentence or line of dialogue explain what something *means*? Cut it.
6. Did any new character arrive described before they spoke or acted? Fix it.
7. Are Harry's readings plain and varied, and are there enough of them? (Most scenes with other people in them should have at least one.)
8. Did the chapter end on a turn rather than a summary?
9. Is narration free of contractions except where the author would allow them?
10. Did every plant and payoff in the chapter plan make it in, and is each plant written so it reads naturally the first time?
11. Is the dialogue share roughly a quarter to a third?
12. Did anything happen that contradicts the Story So Far ledger? Fix it.


========================================================================
# FILE: SPOILERS_04_STORY_BIBLE.md
========================================================================

# SPOILERS · 04 · STORY BIBLE

**Working title:** *The Other Hour*

This file is for the writing chat only. It contains the whole shape of the story.

---

## 1. The premise in one paragraph

Harry Potter has been able to feel other people's emotions for as long as he can remember. It is a natural, untrained form of legilimency, and it has made him very good at getting what he wants from people: like Tom Riddle at the same age, he can walk up to almost anyone and charm them. The difference is what it has done to him. Tom learned contempt. Harry learned how much everyone around him hurts, and it made him kinder, and lonelier, because nobody can feel *him* back. He is ambitious and cunning, and he is sorted into Slytherin. At Madam Malkin's he meets Evelyn Selwyn, a plain, dry Slytherin girl a year above him, and does not think about her again until he realises he cannot read her at all. She is an Occlumens, trained from the age of five by her grandmother, and the reason her family closes its minds is that her grandfather is Gellert Grindelwald. The story runs from 1991 to 1999. It keeps the major events of the books, reshaped by a different Harry and a different cast, and adds the Paths: rare, deep magical disciplines whose summits, the Pinnacles, can rewrite reality around the person who reaches one.

## 2. Timeline and ages

| Item | Detail |
|---|---|
| Harry born | 31 July 1980 |
| Evelyn born | 9 March 1979. One school year above Harry. Starts Hogwarts September 1990 |
| Year 1 | 1991 to 1992 (Harry 11, Evelyn 12 to 13, in her second year) |
| Year 2 | 1992 to 1993 |
| Year 3 | 1993 to 1994. The weeks in the other world happen in March 1994 home time |
| Year 4 | 1994 to 1995 |
| Year 5 | 1995 to 1996 |
| Year 6 | 1996 to 1997. Evelyn's seventh and final year |
| Year 7 | 1997 to 1998. Harry does not return to school. Battle in May 1998 |
| After | Summer 1998 (Harry turns 18 on 31 July 1998), then a jump to 1999 |
| The other world | A world running about two years ahead. Our pair arrive in late April 1996 of that world and leave on the night of the Department of Mysteries battle in June 1996 |

## 3. Harry's gift

### 3.1 What it is

Harry perceives other people's emotions directly. Not their thoughts, at first. Their feelings, as knowledge: the way you know a word without spelling it. He has done it since before he can remember and assumes, until Quirrell tells him otherwise, that it is a thing he is unusually good at noticing rather than magic.

He relies on it completely. He uses it to stay safe at the Dursleys', to decide whom to trust, to win arguments, to make people like him. Most scenes he is in with other people should include at least one reading. He is lost without it, which is why the one person he cannot read becomes an obsession.

### 3.2 How a reading is written (this is a rule)

A reading has up to four parts. Use one, two, or all of them, and vary which.

1. **Name.** Plain words. Afraid, pleased, bored, ashamed, fond, hungry, smug, grieving, nervous, relieved, contemptuous. Be precise rather than poetic.
2. **Strength.** Harry's own words for it are **loud** and **quiet**. A loud person is someone whose feeling fills the room. A quiet person is someone whose feeling is small or held down.
3. **Direction.** Who the feeling is aimed at. At Harry. At someone else in the room. At themselves. At nothing in particular.
4. **Layering.** What is under what. People usually feel two things. Harry notices the top one first and the lower one a moment later, and the lower one is usually the true one.

Examples of the shape (not to be reused verbatim):

- *Uncle Vernon was angry, which was ordinary. Under the anger, much quieter, he was frightened, which was not.*
- *Professor Quirrell was pleased with him. It was a warm, steady feeling, aimed straight at Harry, and it did not waver even when Harry got the incantation wrong.*
- *The whole of the Great Hall was loud with the same thing at once, and the thing was disappointment.*
- *Malfoy was bored, or wanted to be. He was not. He was jealous, and it was aimed at the scar.*

**Never** write a reading as a sensation in Harry's body (no "a wave of fear washed over him", no "he felt their anger like heat"). The reading is information. Harry's own reaction to that information is a separate thing, written in the author's restrained way.

**Silence.** When Harry tries to read an Occlumens, he gets nothing. He calls it silence. Evelyn is silent. He finds silence unsettling, then fascinating, then, over years, restful.

### 3.3 Limits

- **Emotion is not intention.** People can feel genuine warmth toward someone they are about to hurt. This is the lesson of Year 1 and it never stops being true.
- **Range.** Year 1: a room. Year 2: a corridor or a classroom through a wall. Year 3 onward: the Great Hall, and very strong feelings further. Year 5 onward: a building, with effort.
- **Crowds** are noise. A full Great Hall is a roar he learned to turn down as a child. Sudden mass emotion (the Sorting, a Quidditch crowd, a battle) can overwhelm him for a few seconds.
- **Things he cannot read:** Occlumens who are closing their minds (Evelyn always, Isadora always, Snape and Dumbledore when they choose, Voldemort when he chooses); the dead (ghosts are the exception: each reads faintly as one thin grey note, usually sadness); the Petrified, who are as silent as Evelyn, which horrifies him; Dementors, which are only appetite. Objects have nothing, **except soul-objects**: a Horcrux feels *hungry*. He notices this with the diary in Year 2 and again with the diadem in Year 5.
- **Distance from the source** of a reading does not let him fake his own feelings. He can read; he cannot hide what he feels except by ordinary self-control.

### 3.4 How it grows

| Year | New ability | How it is learned |
|---|---|---|
| Before Hogwarts | Reading emotions in a room | Innate |
| 1 | The **push**: forcing his own or another's feelings, amplified, into a person | By accident, in terror, on Quirrell. He is horrified and avoids it for a long time |
| 2 | Wider range. At peaks of emotion, a stray word or image of someone's thought comes through | Practice, isolation, need |
| 3 | **True legilimency**: reading thoughts and memories with eye contact. First **illusions**: pushing a perception rather than a feeling (a coin that is not there, a face that is not his) | Slytherin's study in the Chamber of Secrets, then necessity in the other world, where he has to hide two people's faces for weeks |
| 4 | Illusions under pressure in public (the first task) and in combat (the graveyard). Recognised by others as the first step of a Path | The Tournament, terror |
| 5 | Reading emotions in memories (Pensieve). Entering Voldemort's mind on purpose through the scar link | Dumbledore, Snape, his own recklessness |
| 6 | Battlefield illusion. Illusions on several minds at once | Lockhart, Dumbledore |
| 7 | The Threshold, then the **Pinnacle: Ultimate Deceit** | The war, and almost losing himself |

### 3.5 What it costs him (show, do not state)

He is lonely in company because nobody can feel him back. He is tempted, always, to make people feel what he wants. The push is close to the Imperius Curse in effect and he knows it. Every time he uses it, it gets easier.

## 4. Occlumency, and why the Selwyn women close their minds

Evelyn's grandmother, Isadora Hale, taught her to close her mind from the age of five, every morning, the way other children were taught to brush their teeth. The family line is "A lady's thoughts are her own." Evelyn has never known her mind open. She does not know why it matters until Year 4. The reason is that Isadora was Grindelwald's companion for eleven years and bore his daughter, and the secret of that line has to survive any legilimens alive.

Evelyn's occlumency is total and continuous. She does not have to concentrate on it any more than she concentrates on breathing. It also shapes her: she rarely names her own feelings, even privately. Harry cannot read her, and, from Year 3, his illusions do not work on her either. She is the one person he can never fool.

**The one time she opens:** Year 7, Chapter 76. It is the first time in her life. She cannot fully close again for several days afterwards, and that has consequences.

## 5. Paths and Pinnacles

### 5.1 What a Path is

A Path is a discipline of magic so deep that it changes the person who walks it. It is not a subject like Transfiguration. It is a grain in a person's magic, a direction it already runs in, followed all the way down. Very few people have the grain. Of those, most never notice. Of those who notice, most never survive the walk to the top.

People who walk a Path are called **Walkers**. In the whole of Europe in the 1990s there are perhaps a dozen living, and most are old.

### 5.2 Stages

1. **Grain.** Innate. Undetectable to most.
2. **The First Step.** An involuntary act of magic beyond what the person should be able to do, under extremity. Other Walkers can recognise it on sight.
3. **Walking.** Years of deliberate practice. The Walker grows stronger at their Path's kind of magic than any ordinary witch or wizard could be.
4. **The Threshold.** A crisis in which the Path nearly consumes the Walker. They go all the way into it and must find a way back. Many do not come back.
5. **The Pinnacle.** The summit. A Walker who has crossed the Threshold and returned can open a Pinnacle: for a few minutes, inside a defined space or a defined mind, reality follows the logic of their Path.

### 5.3 Rules every Pinnacle obeys

- **A divided soul cannot stand on a Pinnacle.** This is written in Salazar Slytherin's journal: *"The Paths are open to many, but no divided thing may stand upon a summit."* This one sentence is why Voldemort remerges his soul.
- A Pinnacle is opened through a wand the Walker has used for years. It cannot be opened with a borrowed wand.
- A Pinnacle lasts minutes, not hours. Holding it longer costs more.
- **Every Pinnacle has a cost that matters**, listed below. Never let a Pinnacle be free, and never let a cost be forgotten in the chapter after.
- Pinnacles interact. Some counter others. That interaction decides fights.

### 5.4 The Paths in this story

**Path of Illusion** (Harry Potter)
- Grows out of empathic legilimency: reading feelings, then pushing feelings, then pushing perceptions, then pushing a whole reality.
- **Pinnacle: Ultimate Deceit.** Harry builds a complete false reality, either over a local area (everyone inside sees, hears and feels it) or inside a single mind. Inside it, the false reality is total: people can be hurt by things that are not there, can believe anything, can live hours in a minute.
- **Strength scales down with numbers.** One mind is the strongest form. A crowd is weak and full of holes.
- **Costs:**
  1. The author has to live inside the deceit too. While it runs, Harry's own body is defenceless and his own sense of what is real is at risk.
  2. Without an anchor, a fixed point of truth outside the deceit, he may not find his way back. Slytherin's journal records that his apprentice Oswin walked this Path and at its summit "could not find the door back to himself".
  3. It cannot touch a closed mind. Occlumens are immune. Dementors are immune.
  4. Afterwards he is **blind**: he cannot read anyone for hours or days. After the final use, the blindness is permanent.

**Path of Stillness** (Evelyn Selwyn)
- Grows out of a lifetime of occlumency. Her magic runs toward stopping things.
- **Pinnacle: Dead Calm.** Inside a space she defines, all magic that is not hers is stilled. Curses fall out of the air. Enchantments sleep. Wards hang slack. Minds cannot be touched, by legilimency, illusion, or Dominion.
- **Costs:**
  1. She cannot cast anything inside it either. She can only hold.
  2. While she holds it she can feel nothing at all. Afterwards, everything she did not feel arrives at once.
  3. It stills **all** magic, including healing. Anyone inside who is being kept alive by a charm loses it. (Year 6: this kills someone.)
  4. It is incompatible with being Harry's anchor. She cannot hold Dead Calm and call him back at the same time. (This is the dilemma of the final battle.)

**Path of Transmutation** (Albus Dumbledore)
- The Path of change: all matter is one matter wearing different forms.
- **Pinnacle: First Matter.** Inside his space, matter forgets what it is and becomes what he decides. Stone becomes water, walls become birds, a falling ceiling becomes snow.
- **Cost:** it takes years from his life. Visibly. He uses it in Year 5 in the Atrium and comes out a decade older. He uses it a second time on the night he dies.

**Path of Sight** (Gellert Grindelwald)
- The Seer's Path.
- **Pinnacle: Every Hour.** He sees every possible next moment at once and acts in the one he chooses. Nothing inside it can surprise him.
- **Cost:** afterwards he cannot tell which hour is the real one. For days. Over decades, he has lost his grip on the present, and part of his imprisonment is that he no longer entirely wants to leave.
- He made Isadora's watch with this Path.

**Path of Dominion** (Lord Voldemort)
- The Path of command. He has walked it since his teens and could never reach its summit, and never understood why, until Year 5.
- **Pinnacle: Sovereign.** Inside his space, every will weaker than his obeys. Wands turn. Bodies move. Spells cast at him must out-will him to land.
- **Strength scales up with numbers.** Every mind he holds feeds him. He is strongest at the head of an army, which is the exact opposite of Harry.
- **Costs:**
  1. He cannot command what he cannot perceive. Illusion hides things from him. Stillness takes them out of his reach.
  2. While Sovereign is open, he cannot move from its centre.
  3. It is impossible with a divided soul. Hence the remerge.

**Path of Hearts** (Salazar Slytherin, historical)
- The root Path from which Harry's branches. Slytherin was a reader of feelings. His study under the school can only be opened by someone who reads hearts. Tom Riddle tried and failed. His scratches are on the door: the letters *I WILL*.

**Other living Walkers** are old continental figures who belong to the Concordat (below). They appear only through letters and one meeting in Prague in Year 6 (Chapter 64). Two are named: Dona Inês Albuquerque (Portugal, Path of Tides, ninety-one) and Arkady Volkonsky (Russia, Path of Iron, seventy-eight). Use no others without need.

### 5.5 The Concordat

In 1658, in Prague, the Walkers of Europe signed an agreement after a Pinnacle burned a city. Its terms: no Pinnacle is to be opened against someone who cannot walk; no Walker is to rule; a Walker who breaks the Concordat is to be stopped by the others. Grindelwald broke it. Dumbledore, a signatory, was the one who stopped him in 1945. That duel was a Concordat matter as much as a war matter, which is something British history does not know.

In 1997 there are four living signatories. Voldemort was never asked to sign and would not have. When Dumbledore asks them for help in June 1997, with Harry beside him, and when Harry writes to them again a month later, they refuse: *the Concordat does not go to war.* This is an external door that stays shut. Do not let it open later.

## 6. Isadora's watch

- A small gold pocket watch with a worn pattern of ivy leaves on the lid. Grindelwald made it for Isadora in 1938 with the Path of Sight. Its face has a second, very fine hand that most people never notice and that does not seem to move.
- **What it does:** wound forwards, it is an ordinary watch that loses a minute a week. Wound **backwards**, it takes the wearer, and anyone touching them, sideways into "the next hour": the nearest world to this one.
- **The nearest world** is the one that differs by the smallest important choice. For Harry, that is the world in which he asked the Sorting Hat not to put him in Slytherin. That world is the world of the books. Nobody in this story ever says this explicitly. Harry works it out and keeps it to himself.
- **Getting back:** a copy of the watch native to the visited world (Grindelwald made one in every world where he loved Isadora) must be wound forwards by a hand of Isadora's blood, in a place where time is held. The Department of Mysteries' Time Room counts. The native watch is destroyed by this. The travellers' own watch then stops and will not wind until its maker resets it.
- **Time runs differently** between worlds. About six weeks there is four days here.
- **History:** Isadora wound it backwards once, in 1944, and saw a world in which Gellert had won. She came back and left him. Grindelwald calls it the only argument he ever lost.
- **Rules of the family:** Isadora gives it to Evelyn at eleven with two instructions. Wind it every morning. Never wind it backwards, and if you ever do, wind it forwards again at once. She gives no reason.
- **Arc:** Evelyn winds it every morning (Year 1 onward). Winds it backwards in grief (Year 3). It stops (Year 3). Grindelwald resets it (Year 4). It stops again at the moment of his death (Year 7). In the After arc its second hand ticks once.

## 7. Horcruxes, the remerge, and the Hallows

- Canon Horcruxes: diary, ring, locket, cup, diadem, Nagini, and, unknown to everyone, Harry.
- **Year 2:** Harry destroys the diary with a basilisk fang, as in canon, but only after weeks of talking to Tom in it and being genuinely tempted.
- **Year 5:** Voldemort, inside Harry's mind through the scar, finds Harry's memory of Slytherin's journal and reads *no divided thing may stand upon a summit*. He decides to remerge his soul: give up the Horcrux route to immortality for a Pinnacle. He gathers what is left: the locket (from Grimmauld Place through Kreacher and Narcissa), the ring, the cup (from the Lestrange vault), the diadem (fetched from the Room of Requirement by Draco on his first errand), Nagini, and the fragment in Harry. The ritual is at the Veil in the Department of Mysteries. The diary piece is gone forever. He becomes one soul again, smaller than he was born with but undivided, and with it he reaches Sovereign.
- When the fragment is torn out of Harry, Harry **loses Parseltongue** mid-sentence. He keeps his gift. The reading was always his own. Nobody says this in words. He checks for it the way you check a pocket, and it is there.
- Losing Parseltongue means the Chamber of Secrets is closed to him forever.
- **Nagini** after the remerge is just a large, dangerous snake.
- **The Hallows** become Voldemort's new road to immortality. A whole soul fears death more than a divided one, and Grindelwald knows the Hallows better than anyone living.
  - **Wand:** Voldemort takes the Elder Wand from Dumbledore's body in Year 6. But Draco disarmed Dumbledore first, so its allegiance went to Draco. In Year 7, at Malfoy Manor, Harry disarms Draco. The wand's true master is Harry. Nobody knows this until the end.
  - **Stone:** the Resurrection Stone is set in the Gaunt ring, which Voldemort wears again after the remerge. He does not know what the stone is until Grindelwald's death in Year 7, when Grindelwald tells him, deliberately, as the price that makes his lie about Evelyn hold.
  - **Cloak:** Harry has it from Year 1. Year 7 is Voldemort's hunt for it.

## 8. Places

Use many. The plan names specific ones for each chapter. Key places:

- **Privet Drive**, Little Whinging, Surrey.
- **Selwyn Hall**, a long grey house of Shropshire stone in the hills west of Ludlow, with a yew walk older than the house. Corvin's house. Isadora lives in the east wing until she dies.
- **Hogwarts**, especially: the Slytherin common room under the lake (green light, cold, the noise of water); the library's back tables; the Owlery; the unused classroom on the fourth floor where Evelyn and Harry meet; Moaning Myrtle's bathroom; the Chamber of Secrets; **Slytherin's study** (a small round room behind the great statue's feet, lined with shelves, a desk of black stone, a cold lamp that lights for a heart-reader).
- **Nurmengard**, Austria. A black tower in the mountains with *FÜR DAS GRÖSSERE WOHL* over the gate. Grindelwald's cell at the top has a narrow window and one chair. Reached by a blood-keyed Portkey that Elias Varga keeps.
- **The Hog's Head** in both worlds.
- **Grimmauld Place**, which Sirius owns and hates.
- **The Department of Mysteries** in both worlds.
- **The cinema**: the Majestic, a closed 1920s picture house in Leeds, boarded since 1985. Harry's Year 7 base. He trains illusions on its screen.
- **Shell Cottage**, Tinworth, Cornwall.
- Others as the chapter plans direct: a Muggle launderette in Ludlow, the Leaky Cauldron, the Knight Bus, Wastwater, a Cornish tin mine, Hogsmeade in snow, the Burrow, St Mungo's, the Ministry Atrium, a lay-by on the A49.

## 9. The cast

Each entry gives: first appearance, voice, want, secret, arc. Fates are in the master outline's death register.

### Harry Potter
- **Voice:** quiet, polite, watchful; dry when comfortable; very good at saying what people want to hear and quietly ashamed of how good. Says little and means it. When angry, gets quieter.
- **Want:** to matter. To be someone. Underneath, to be *felt*: to have someone know what he feels without his saying it.
- **Secret:** he can feel everyone, and he uses it. Later: what he did to Quirrell. Later: Tom. Later: the prophecy.
- **Arc:** a boy who reads everyone and trusts nobody, who learns to trust the one person he can never read, and who goes so far into deceit that he loses himself and has to be brought back. He ends unable to read anyone at all.
- **House:** Slytherin. Seeker from Year 1 (Snape bends the rule as McGonagall did in canon).
- **Not:** a Gryffindor in green. He is genuinely ambitious and genuinely cunning, and he is kind because he cannot help knowing what people feel, not because he has decided to be good.

### Evelyn Isadora Selwyn
- **First appearance:** Madam Malkin's, Chapter 3. She is being fitted for second-year robes. Harry's first impression is neutral, almost nothing.
- **Look:** plain. Straight brown hair, usually tied back. An ordinary face that people forget. Average height. Grey eyes. That is all the description she gets for a long time.
- **Voice:** flat, precise, dry, literal. Corrects facts, including teachers' (dates especially). Counts things and reports the count. Very rarely raises her voice; when she does, it is devastating. Calls Harry **"Potter"** until the final battle, where she calls him "Harry" for the first time, to bring him back. After that, "Potter" again, mostly, because she says she does not want him to get used to it.
- **Habits:** winds her grandmother's watch every morning. Reads Golden Age Muggle detective novels (Ngaio Marsh, Dorothy L. Sayers, Margery Allingham, Josephine Tey) bought from a second-hand shop in Ludlow and hidden in her trunk. Reads everything else too, including notices nobody reads. Eats the same thing for breakfast every day.
- **Want:** to be left alone. Underneath, to be chosen by someone who could have chosen anyone.
- **Secret:** her mind is closed and she does not know why. From Year 4: Grindelwald.
- **Arc:** the girl nobody remembers, who becomes the only person Harry cannot do without, who learns her grandfather is the most notorious wizard of the century, who walks the Path of Stillness, who kills Snape to save Harry, and who opens her mind for the first time in her life to bring Harry back.
- **House:** Slytherin, one year above Harry. Not a prefect (she declined).
- **In the other world:** an Evelyn exists there too. She is the girl nobody remembers, with no Harry and no friends, and the same watch.

### The Selwyns
- **Isadora Hale** (born 1912, dies February 1994). Evelyn's grandmother, Marguerite's mother. An English witch who went to the Continent in 1933, lived with Grindelwald from 1933 to 1944, left him in 1944 after what the watch showed her, and returned to England in 1945 with a two-year-old daughter and a new life. Formidable, courteous, terrifying. Silent to Harry. First appears Chapter 11, when she collects Harry from Privet Drive. Watches him like a woman who has been told about him in advance, because she has: Gellert foresaw a boy who reads hearts standing beside their granddaughter.
- **Marguerite Selwyn** (born 1943). Evelyn's mother. Grindelwald's daughter. Once beautiful, now fragile, drinks gin from the late morning onward. Knows the secret and it has crushed her. Loves Evelyn badly and sincerely.
- **Corvin Selwyn.** Evelyn's father. Wizengamot member. Lean, grey, still, clever; the kind of stillness that makes others talk too much. Applies pressure the way water does to stone. Aligns with whoever is winning. Does not know his wife's parentage. Heads the Muggle-born Registration Commission in Year 7. Flees at the end.
- **Lucan Selwyn** (born 1975). Evelyn's older brother. Sixth-year Slytherin prefect in Harry's first year. Polished, pleasant, white teeth, his father's smile practised since he was twelve. Takes the Mark in 1996. His last act, in the battle, may have been to protect his sister. Nobody will ever know if he meant it. His last words are something close to *"She was supposed to be safe."*
- **Thaddeus Selwyn.** Corvin's younger brother. Death Eater. Masked in the World Cup riot (Evelyn knows his voice), present in the graveyard, at large in the war.

### Gellert Grindelwald
- **First appearance:** by letter in Year 4 (Chapter 36), in person in Chapter 38.
- **Voice:** elegant, amused, theatrical, perfectly honest about the wrong things. Speaks English with a faint Germanic precision. Treats everything as slightly beneath him except Evelyn, whom he treats as the most interesting person alive. Cruel when he forgets himself, and he forgets himself less than he used to.
- **On his reputation** (use something close to this in Chapter 38, in his own voice): *"History has decided I loved one person and that he was a man. History is half right, which is the most irritating way to be wrong. I loved your grandmother for eleven years and him for one summer, and history, being a romantic, prefers the summer."*
- **The bargain:** he offers to tutor Evelyn in exchange for news of the outside world. It is a pretext. He simply likes listening to her talk. She works this out by her second visit.
- **Not redeemed.** He still believes in the greater good. He is old enough to find his own younger self embarrassing, which is not the same thing as sorry.
- **Sees futures.** He saw Evelyn beside a boy who reads hearts. He tells her: *"I saw you beside him. I did not see how it ended."*

### Albus Dumbledore
- Canon Dumbledore: wise, warm, theatrical, manipulative, loving, ashamed. Path of Transmutation.
- **His arc with Harry, in stages:**
  1. **Years 1 to 3, the wedge he does not notice.** He treats Harry as a child to be protected and steered. Harry reads him each time and keeps a private ledger. Year 1: Harry reads Dumbledore's quiet satisfaction that the Stone plan worked, while Quirrell is dead and Harry is in the hospital wing. Year 2: Dumbledore watches the school turn on Harry and does nothing visible. Year 3: Harry lies to him flawlessly and Dumbledore believes him; then Dumbledore refuses to let him live anywhere but Privet Drive.
  2. **Year 4, the blow-up** (Chapter 44). After the graveyard. Harry tells him everything he has kept: the Stone as bait, the heir year, Sirius left to rot, "nothing can be done" about the Goblet, a Death Eater teaching under his nose for a year, Cedric. And then: *"You knew about the prophecy."* Dumbledore realises Harry has been ahead of him for over a year. Harry pushes the graveyard into him, and Dumbledore lets it in. The one Dumbledore-viewpoint section in that chapter shows the moment he stops seeing a pupil. He tells Harry he is walking a Path, and that so is he. He offers to teach rather than protect. Harry reads three things in him: respect, grief, and fear. He notes the fear.
  3. **Years 5 and 6, partners who still keep secrets.** Dumbledore asks rather than orders. He still withholds the Horcrux in Harry until it is too late. He lets Harry live with Sirius after Year 5.
  4. **His death** (Year 6, Chapter 65).
  5. **After death:** his letter in his will (Chapter 66), and his contingency, revealed through Snape's memories in Year 7: *"If he becomes what Tom became, you will have to stop him. I could not stop Gellert in time. Do not make my mistake."* His fear was real, and it was about Harry.

### Lord Voldemort / Tom Riddle
- **Year 1:** the face on the back of Quirrell's head. Offers Harry a place beside him: *we are alike*.
- **Year 2:** Tom in the diary. Sixteen, charming, patient, lonely, contemptuous. The first person who seems to understand Harry. Harry reads the diary's feelings: hunger, loneliness, and, when Harry talks about his gift, envy. Tom could always tell what people *wanted*. He never once felt what they *felt*.
- **Year 4:** returned. Recognises Harry's illusions in the graveyard as a Path, not a spell, and becomes very interested.
- **Year 5:** remerges. Becomes Sovereign.
- **Year 6 to 7:** whole, colder, more patient, more frightening. Seeks the Hallows. Dies in Chapter 79, inside Harry's Pinnacle, by his own curse, turned back by a wand that was never his. The deceit Harry builds for him is made out of what Harry learned of sixteen-year-old Tom through the diary and of the fragment that lived in him for fifteen years.

### Quirinus Quirrell
- **Not** the stammering canon version. Competent, dry, exacting, very good at Defence. A former Ravenclaw. A man who went looking for power, found it, and has been regretting it on the inside ever since.
- **Voice:** precise, a little sardonic, kind in a way that seems reluctant.
- **His tutoring of Harry** is Voldemort's recruitment. But Quirrell's affection for the boy is real, and that is the point. Harry reads it correctly. What he cannot read is intention.
- **The cold under the warmth:** Harry senses something like a draught from a closed door every time he is near Quirrell. He assumes it is sadness. It is Voldemort.
- **Death** (Chapter 10): Harry, terrified, pushes Quirrell's own self-loathing back into him, amplified, without knowing what he is doing. Quirrell turns his wand on the face at the back of his head and speaks the Killing Curse. Written plainly. No gore. Harry never tells Dumbledore what he did.

### Gilderoy Lockhart
- **Everything in his books happened.** He embellishes the prose, not the deeds. He really did banish the Bandon Banshee and spend a year with a yeti.
- **Voice:** loud, warm, vain, funny, generous, theatrical. Calls everyone "my dear fellow" or "my dear girl". Signs things without being asked. Genuinely brave and genuinely kind, and so self-absorbed that people miss both.
- **Teaches:** that people see what you show them. Misdirection, performance, the cape-flourish that hides the wand. He is, without knowing it, Harry's first teacher of illusion.
- **Seeds the Paths:** in a Year 2 lesson he tells a story about a Walker he met in the Himalayas in 1983. Everyone assumes he is showing off. He is telling the truth.
- **Beats Snape** at the Duelling Club. Gracefully. Snape never forgives it.
- **Year 2 end:** in the Chamber, holds up a collapsing tunnel with a spell so Harry can go on, and stays holding it. Breaks his back. Two and a half years in St Mungo's; by Christmas 1995 he is in a rehabilitation ward, walking with a stick and great panache.
- **Year 6:** returns, recovered, as an Order operative. Takes Harry on a mission.
- **Year 7:** dies holding the bridge at Hogsmeade, with enormous style.

### Severus Snape
- Canon Snape. Hates Harry for James. Under the hatred, Harry reads grief, from the very first lesson, and cannot make sense of it until Year 5.
- **Year 5:** occlumency lessons turn into duels of minds. Harry sees Snape's worst memory and reads, directly, what Snape felt for Lily. Snape never forgives being *felt*.
- **Year 6:** after Dumbledore dies, Harry reads Snape's grief across a courtyard. It is so raw that Harry knows Snape was loyal. Harry trusts him from then on.
- **Year 7:** headmaster under the regime, quietly helping Harry. Then he watches what Harry becomes after Hogsmeade, remembers Dumbledore's contingency, and decides. He ambushes Harry at the Shrieking Shack, means to break his mind and destroy the Cloak. Evelyn kills him with *Sectumsempra*, his own spell. His memories give Harry the rest.
- Snape is not a villain in this. He is wrong, and he is partly right, and he believes he is doing what Dumbledore asked.

### Sirius Black (two of them)
- **The other world's Sirius** (Year 3): meets thirteen-year-old Harry at the Hog's Head. Loud with love, reckless, despairing at being caged. Tells him about Peter and the rat with the missing toe. *"Save my other self some trouble."* Harry watches him fall through the Veil a few days later.
- **This world's Sirius:** fugitive in Years 3 and 4. Cleared after Year 5 because Aurors see Pettigrew alive at Voldemort's side in the Ministry Atrium. Harry's guardian from summer 1996. Funny, restless, generous, bad at being domestic, very good at being loved. Adores Evelyn and teases her mercilessly. Dies in Year 7 holding the door at the Burrow when the Ministry falls. Sudden. Mid-chapter. Harry does not cry for him until Chapter 76.

### Draco Malfoy
- **Rival inside Slytherin.** The established prince against the famous half-blood upstart. He offers friendship at the Sorting feast; Harry reads contempt under the offer and declines.
- **Harry always knows when Draco is afraid. Draco knows he knows.** That is the core of their relationship. It is cruel, intimate, and occasionally almost kind.
- **Year 5:** fetches the diadem. **Year 6:** the Mark, the cabinet, the mission to kill Dumbledore, *Sectumsempra*. He disarms Dumbledore on the tower. **Year 7:** Harry disarms him at Malfoy Manor. In the final battle, he is one of the people guarding Harry's body, and nobody, including Draco, can say exactly why. Survives. His last look at Harry is unreadable, because by then Harry cannot read anyone.

### Theodore Nott
- Slytherin, Harry's year. Quiet, clever, motherless, very good at chess. Sits with Harry on the train. Harry reads a calm sadness in him and likes him at once.
- **Arc:** best friend in the house. His father is in the graveyard. In Year 6 he takes the Mark on Harry's advice, to spy, which is a use of a friend that Harry does not let himself think about. Feeds information through Year 7. On the morning after the battle he is gone. Nobody knows where. This thread stays open.

### Millicent Bulstrode
- Slytherin, Harry's year. Big, blunt, funny, half-blood, underestimated, mocked by Pansy. Harry finds her crying in a bathroom on Halloween with a troll on its way.
- **Voice:** short sentences, no tact, very loyal. Calls Harry "Potter" too, but differently.
- **Arc:** the first to stand up for Harry in Year 2. Becomes a Beater. Goes everywhere with him. Dies in Chapter 79 guarding his body.

### Ron Weasley and Hermione Granger
- **Minor until Year 5.** Glimpsed: Hermione's hand in the air, Ron at the Gryffindor table, Ron's rat in Year 3.
- In the other world (Year 3), Harry sees them as the other Harry's best friends, and it marks him. Back home he approaches Ron about Scabbers, badly.
- **Year 5:** Hermione proposes a defence group; Harry takes the idea and builds it across houses, which is how they start. **Year 7:** they become two of the four. They guard his body in the final battle. Both survive.

### Neville Longbottom
- Harry reads Neville's kindness and fear on the train. A minor ally who grows. Leads the resistance at Hogwarts in Year 7. Survives.

### Luna Lovegood
- Year 5 onward. Friendly with Evelyn, which surprises everyone, including Evelyn. Survives.

### Rubeus Hagrid
- Harry's first friend and the loudest warm thing he has ever felt (Chapter 1). Dies in the battle, in Chapter 78, holding back giants from a group of first-years.

### Remus Lupin and Nymphadora Tonks
- **Lupin:** Year 3 Defence teacher. Harry reads kindness and old guilt aimed at him. Patronus lessons. Dies in the battle.
- **Tonks:** Year 5 summer at Grimmauld Place. A Metamorphmagus; a natural kinship with Harry's illusions. Teaches him how disguise *works* on people (it is mostly posture, she says). A mentor and friend for a few months. Dies at the Department of Mysteries in Chapter 54, beside Sirius, in the place where the other world's Sirius died.

### Cedric Diggory
- Decent, fair, brave. Harry tells him about the dragons. Dies in the graveyard.

### Aberforth Dumbledore (two of them)
- **The other world's Aberforth** shelters Harry and Evelyn at the Hog's Head. Recognises the maker's mark on the watch and refuses to say whose it is. *"My brother will use you, boy. He uses everyone he loves, and he loves you, so watch out."*
- **This world's Aberforth** in Year 7 does not know them. Harry knows him. That asymmetry is worth a scene.

### Elias Varga
- Durmstrang's Master of Wards, about seventy, Hungarian, an acolyte of Grindelwald's in his twenties who has spent fifty years ashamed of it. Keeps the blood-keyed Portkey to Nurmengard. Carries Grindelwald's letters to Evelyn. Recognises Harry's first public illusion as a Path's first step. Tells Harry and Evelyn about Walkers and the Concordat in Year 4. Dies at Nurmengard with Grindelwald in Year 7.

### Others, briefly
- **Dursleys:** Vernon (loud anger, quiet fear), Petunia (envy and buried grief for Lily, which Harry has always felt and never understood), Dudley (Year 5: terror, then something like gratitude).
- **Kreacher:** hatred, grief, and devotion to "Miss Narcissa". Gives her the locket in Year 5.
- **Dobby:** Year 2 as canon. Dies at Malfoy Manor in Year 7.
- **Mad-Eye Moody:** the imposter in Year 4 (Harry reads fierce devotion aimed at him and misreads it as an Auror's protectiveness); the real one from Year 5; dies at the Burrow in Year 7.
- **Dolores Umbridge:** sincere, sweet, sadistic certainty. Harry joins her circle in Year 5 to play her.
- **Horace Slughorn:** Year 6. Collects people. Harry lets himself be collected.
- **Minerva McGonagall, Pomona Sprout, Filius Flitwick, Poppy Pomfrey, Argus Filch, Madam Hooch, Rita Skeeter, Cornelius Fudge, Barty Crouch (both), Ludo Bagman, Igor Karkaroff, Olympe Maxime, Viktor Krum, Fleur Delacour, the Weasley family, Lucius and Narcissa Malfoy, Bellatrix Lestrange, Peter Pettigrew, Moaning Myrtle, Nearly Headless Nick, Fawkes, Hedwig, Buckbeak:** broadly as canon, adjusted by the plan.
- **Justin Finch-Fletchley:** Hufflepuff, Harry's year. Petrified in Year 2 and blames Harry for it loudly. Dies in Year 6 inside Evelyn's Dead Calm when the charm keeping him alive is stilled.

## 10. Relationship rules

### Harry and Evelyn
- **Non-romantic through the school years and the war.** Both are minors. No kissing, no romantic confessions, no dating, no crush framing, no jealousy plots, nothing sexual of any kind. Their bond is the most important relationship in the story, and it is written as fierce, dry, loyal friendship and trust. Physical comfort that friends give each other (sitting shoulder to shoulder, a hand held in a crisis, a hand on an arm) is fine and should be rare enough to matter.
- **The romance begins only in the After arc**, set in 1999 when Harry is 19 and Evelyn is 20. It is fluffy, funny, tender, and not the main thing even then. At most a first kiss and domestic closeness. Fade out rather than describe anything further.
- **How the friendship grows:** Year 1, obsession and irritation becoming respect. Year 2, allies, and his terror when she is Petrified. Year 3, partners in the Chamber and in the other world, where they are all each other has. Year 4, a secret on each side, the strain, the blow-up, the trust exchange. Year 5 and 6, a team. Year 7, she kills for him and then brings him back.
- She never once pretends to understand him. That is why he trusts her.

### Harry and Draco
- Rivals in the same house. See Draco's entry.

### Harry and his friends
- Harry is a loner in company. He has friends (Theo, Millicent, later Neville, Ron, Hermione) and still feels that nobody can understand him, because nobody can feel him back. Do not cure this with a speech. It eases only through Evelyn, slowly, and only because she does not pretend.

## 11. Content rules

- **Original prose only.** Never reproduce passages or long lines from the Harry Potter books. Canon events can be retold in new words. Famous lines are rephrased or avoided. No song lyrics or poems from the books (write a new, brief Sorting Hat verse or summarise it).
- **Violence** in the author's way: consequence over gore. The story is rated M for violence, character death, torture (Year 7), and suicide (Quirrell's death). Quirrell's death is written plainly and without method detail beyond the spell. Nothing glamorised.
- **No sexual content at any point.** The After arc is affectionate and fades out.


========================================================================
# FILE: SPOILERS_05_MASTER_OUTLINE.md
========================================================================

# SPOILERS · 05 · MASTER OUTLINE

## 1. The shape

| Part | Chapters | Target words | Span |
|---|---|---|---|
| Prologue | Prologue | ~3,500 | February 1998 (flash-forward) |
| Year One | 1 to 10 | ~60,000 | July 1991 to June 1992 |
| Year Two | 11 to 20 | ~60,000 | July 1992 to June 1993 |
| Year Three | 21 to 33 | ~78,000 | July 1993 to June 1994 (other world: Ch 26 to 30) |
| Year Four | 34 to 45 | ~72,000 | July 1994 to June 1995 |
| Year Five | 46 to 56 | ~66,000 | August 1995 to June 1996 |
| Year Six | 57 to 67 | ~66,000 | July 1996 to July 1997 |
| Year Seven | 68 to 80 | ~80,000 | August 1997 to May 1998 |
| After | 81 to 83 | ~18,000 | Summer 1998, then 1999 |
| **Total** | **84 units** | **~500,000** | |

Chapter length: 5,500 to 7,000 words. Climax chapters may run to 8,500.

## 2. The spine (for you to know, never to state)

- **Feeling is not knowing.** Harry can feel everyone and still be fooled, used, and wrong. The person he trusts most is the one person he cannot feel.
- **Tom and Harry had the same gift for people.** Tom learned what people wanted. Harry learned what they felt. One became Dominion, the other Illusion, and both are ways of making people see what you choose.
- **Deceit as a way of life.** Harry is cunning. He lies well and enjoys it. The Path of Illusion is the logical end of a talent he has been using since he was six. Its summit costs him himself.
- **Equal footing.** Dumbledore moves from steering Harry to respecting him to fearing him, and all three are true at once.

None of these may be said aloud by the narrator or by a character. They are the reason the plan is shaped the way it is.

## 3. Year by year

### Year One (Ch 1 to 10): The Weather Indoors

**Summary.** Harry, a reader of feelings who survives the Dursleys by reading them, learns he is a wizard. At Madam Malkin's he barely notices a plain second-year. He is sorted into Slytherin, refuses Draco, befriends quiet Theo and blunt Millicent, and discovers that the plain second-year, Evelyn Selwyn, is silent to him. It becomes an obsession and then a friendship. Professor Quirrell, sharp and competent and genuinely fond of him, names Harry's gift and tutors him privately. Under the warmth Harry feels a cold draught he assumes is sadness. At the Mirror, Quirrell is revealed. In terror Harry pushes Quirrell's own self-loathing back into him, and Quirrell kills himself trying to kill the thing in his head. Dumbledore tells Harry a comforting story about love and protection. Harry knows it is wrong, reads Dumbledore's satisfaction that the plan worked, and says nothing to anyone for four days, Evelyn included.

**Threads.**
- A. Quirrell: mentor to betrayer.
- B. Evelyn: silence to friendship.
- C. Slytherin: finding a place in a house full of Death Eaters' children; Draco's rivalry; Theo and Millicent.
- D. The Stone and the third-floor corridor.
- E. Dumbledore's ledger (Harry's private record of him).

**Escalation ladder.** Letters and Hagrid, then a new world, then the Sorting's shock, then the troll, then the jinxed broom, then the forest and the thing drinking unicorn blood, then the trapdoor, then a man dying because of what Harry did.

**Resolved by others or by outside forces.** The troll (a joint effort, and a teacher arrives). The broom jinx (Evelyn's interference in the stands, which she will never confirm was deliberate). Norbert (Charlie's friends). The Stone's safety (Dumbledore's enchantment on the Mirror, not Harry).

**Left open.** Whether Evelyn tripped Quirrell on purpose. What the grief under Snape's hatred is. Why Isadora went still at Harry's name.

### Year Two (Ch 11 to 20): The Heir

**Summary.** Isadora Hale collects Harry from Privet Drive. A week at Selwyn Hall shows Evelyn's family: cold Corvin, fragile Marguerite, smooth Lucan, and Isadora, who is as silent to Harry as her granddaughter. Gilderoy Lockhart turns out to be exactly as accomplished as his books claim, and loud, and kind. The Chamber is opened. Harry speaks Parseltongue at the Duelling Club, and three-quarters of the school decides he is the Heir of Slytherin. The other quarter, Slytherin, decides the same thing and starts deferring to him. He lets them. Bullied in every corridor, he studies like a man preparing for war, and Slytherin's favours open restricted family libraries to him. He finds a diary that feels hungry, and talks to sixteen-year-old Tom Riddle every night for weeks: the first person who seems to understand him. Then the diary is stolen, Evelyn is Petrified, and Harry discovers that he cannot tell the difference between her silence and a stone's. With Lockhart he goes into the Chamber. Lockhart holds up a collapsing tunnel and breaks his back doing it. Harry, alone with Tom, is tempted, and stabs the diary anyway.

**Threads.**
- A. The Chamber and the Heir.
- B. Tom in the diary: temptation.
- C. Ostracism and the Slytherin favours: Harry's morally grey use of a rumour.
- D. Lockhart: the real thing, and the art of showing.
- E. Evelyn: allies, then her Petrification.
- F. The Selwyns and Isadora.
- G. Dumbledore's ledger.

**Escalation ladder.** Dobby's warning and the locked room, then the writing on the wall, then Parseltongue in public, then Justin and Nick, then a school against him, then the diary's seduction, then Evelyn Petrified, then Ginny taken, then the Chamber.

**Resolved by others or outside forces.** Lockhart's sacrifice holds the tunnel. Fawkes and the Hat bring the sword. Mandrakes restore the Petrified. Lucius loses Dobby through Harry's trick, but Dumbledore's return is the Board's doing.

**Left open.** What the door behind the statue's feet is. Why Harry did not tell Evelyn about Tom until the end (he does tell her, in Chapter 20, which opens a different question: why he wanted to keep it).

### Year Three (Ch 21 to 33): The Other Hour

**Summary.** Harry deliberately breaks his aunt Marge with a push and is frightened by how easy it was. Sirius Black is loose. Dementors guard the school. Harry goes back into the Chamber and finds the door he felt last year: Slytherin's study, which opens only to a heart-reader, with Tom's failed scratches on it. There he learns true legilimency, and makes his first illusions, and discovers that Evelyn sees through every one. He learns at the Three Broomsticks that Black betrayed his parents, and starts planning to kill him. Isadora dies in February. Evelyn, grieving, winds the watch backwards in the Chamber to find out what her grandmother was afraid of, and Harry grabs her hand. They land in the world of the books, two years ahead, in Umbridge's Hogwarts. For six weeks Harry holds illusions over both their faces. He watches the other Harry, furious and loved in Gryffindor, and senses a cold second presence inside him. Evelyn finds the other Evelyn, the girl nobody remembers. The other world's Aberforth shelters them and recognises the watch's maker. The other Sirius tells Harry the truth about Peter. On the night of the Department of Mysteries battle they go home through the Time Room. Harry hears the prophecy when an orb breaks beside him. He watches the other Sirius fall through the Veil. The other Evelyn winds her watch for them and is left behind as footsteps come. Four days have passed at home, and the school thinks Black took them. Harry lies to Dumbledore's face, and it works. Armed with the truth, he hunts Scabbers, sets up the Shrieking Shack, and loses Pettigrew anyway to a full moon. His Patronus drives away a lake's worth of Dementors. He and Evelyn hide Buckbeak's escape with an illusion. Sirius flies. Dumbledore sends Harry back to Privet Drive.

**Threads.**
- A. Sirius Black: enemy, then the truth.
- B. Slytherin's study: the leap in power.
- C. Isadora's decline and death; the watch.
- D. The other world (Ch 26 to 30).
- E. The other Evelyn and the other Harry: mirrors.
- F. The prophecy: knowledge Harry holds and Dumbledore does not know he has.
- G. Buckbeak; Lupin; Hagrid's classes.
- H. Dumbledore's ledger: the first successful lie.

**Escalation ladder.** Marge, then Dementors on the train, then Black in the castle, then Harry's murder plan, then Isadora's death, then the other world, then a war two years early, then the Department of Mysteries, then the Veil, then home to a manhunt, then the Shack and the full moon and a hundred Dementors.

**Resolved by others or outside forces.** Lupin's transformation lets Pettigrew escape. Dumbledore's refusal decides where Harry lives. In the other world, the battle is not Harry's to win. He only gets out.

**Left open.** What happened to the other Evelyn. Who made the watch (Aberforth knows and will not say). Why Harry carries a faint cold presence (he decides it is contamination from reading the other Harry).

### Year Four (Ch 34 to 45): Equal Footing

**Summary.** Isadora's will contains a letter for Evelyn: her grandfather is alive, and his name is Gellert. Marguerite, drunk, confirms it. At the World Cup in Corvin's box, Evelyn hears her uncle's voice under a Death Eater mask. Harry's name comes out of the Goblet. The school turns on him again. Elias Varga of Durmstrang carries Grindelwald's first letter to Evelyn. She meets him at Nurmengard at Christmas, lies to Harry about where she went, and is tutored by the most notorious wizard alive in exchange for gossip he does not need. He resets her watch. Harry faces the Horntail with his first public illusion, and Varga sees a Path's first step. Harry learns Evelyn lied, and starts managing her the way he manages everyone. The second task makes her his hostage. She crashes out at him in a locked classroom. He admits that she is the only person he cannot read and the only one he trusts. She tells him who her grandfather is. They break onto the Durmstrang ship together and make Varga explain the Paths. At the end of the maze, the Cup is a Portkey. Cedric dies. Voldemort returns. Harry fights him off with illusion and the luck of brother wands, and Voldemort recognises a Path. Back in Dumbledore's office, Harry blows up, and Dumbledore, for the first time, sees him.

**Threads.**
- A. The Tournament.
- B. Grindelwald and Evelyn (her secret).
- C. The strain between Harry and Evelyn, the blow-up, the trust exchange.
- D. Paths: Varga, the First Step, the Concordat.
- E. The imposter Moody.
- F. The Selwyns: Thaddeus, Corvin's politics.
- G. Dumbledore's ledger, closed in Chapter 44.

**Escalation ladder.** A letter in a will, then a riot and a Dark Mark, then the Goblet, then a dragon, then a lie at Christmas, then the lake, then the blow-up between friends, then Crouch in the forest, then the maze, then the graveyard, then the office.

**Resolved by others or outside forces.** Cedric's death is not Harry's choice. The brother-wand connection is luck. Dumbledore and Snape unmask Crouch. Fudge's denial decides the politics.

**Left open.** What Grindelwald has foreseen and will not tell. What Dumbledore's fear is (Harry notes it in Chapter 44 and does not understand it until Chapter 77).

### Year Five (Ch 46 to 56): Sovereign

**Summary.** Dementors in Little Whinging. Tonks and the Order. Grimmauld Place and a caged Sirius. Harry approaches Ron and Hermione, awkwardly, because he has seen what they were to another Harry. Having seen this year once already in another world, he plays Umbridge from inside her circle while building a secret cross-house defence group. Dumbledore asks Snape to teach him occlumency. The lessons become duels, and Harry reads what Snape felt for Lily. Harry starts going into Voldemort's mind on purpose to spy, and something in there looks back and finds Slytherin's journal. Voldemort begins gathering his Horcruxes. Harry follows Draco into the Room of Requirement and feels the diadem's hunger, and something in himself answers. Dumbledore explains Horcruxes and does not mention the one in Harry. The Sirius vision comes. Harry knows it is a trap and goes with a plan and a team and the Order warned in advance. At the Veil, Voldemort remerges his soul and tears the last fragment out of Harry, and Harry loses Parseltongue mid-sentence. Harry stops Bellatrix's curse that killed the other Sirius. Tonks dies beside Sirius instead. In the Atrium Voldemort opens Sovereign and Harry's body turns against him. Evelyn, untouchable, knocks him out of the line. Dumbledore opens First Matter and comes out ten years older. Pettigrew is seen alive by Aurors. Sirius is cleared.

**Threads.**
- A. Umbridge and the defence group.
- B. Harry's double game inside her circle; Draco's fury.
- C. The scar link: spying, and being spied on.
- D. The remerge (Horcruxes gathered).
- E. Snape's lessons.
- F. Ron and Hermione, slowly.
- G. Evelyn's family: Lucan's Mark; Grindelwald's teaching.
- H. Dumbledore withholding.

**Escalation ladder.** Dementors, then a trial, then Umbridge, then Snape's mind, then the snake and Arthur, then the Azkaban breakout, then the diadem, then Dumbledore's flight, then the vision, then the Veil, then Sovereign.

**Resolved by others or outside forces.** Tonks's death is Voldemort's, sudden, not a consequence of Harry's choice. Fudge's conversion is because he sees Voldemort himself. Sirius is cleared by Aurors seeing Pettigrew.

**Left open.** Whether Harry's saving Sirius at the Veil cost Tonks her life. (It did not, causally. Harry will never be sure.)

### Year Six (Ch 57 to 67): First Matter

**Summary.** A summer at Grimmauld Place with Sirius, domestic and funny. Harry meets Grindelwald at Nurmengard, who names his Path and warns him that Voldemort now seeks the Hallows. Dumbledore, old now, teaches him as an equal: Tom's past, the Paths, the Hallows. Draco has the Mark and a mission; Harry, rival and reader, watches his terror all year. Theo takes the Mark on Harry's advice, to spy. Harry nearly kills Draco with *Sectumsempra* and Snape saves him. Evelyn walks toward her Pinnacle and learns its cost. Lockhart returns and takes Harry on a mission in a Cornish tin mine. Draco's cabinet opens. Draco disarms Dumbledore on the tower and cannot kill him. Then Voldemort comes himself. Two Pinnacles meet over the lake. Evelyn opens Dead Calm to shield students and a boy inside it dies when Madam Pomfrey's charm is stilled. Dumbledore spends himself and dies, whether by the curse or by the cost nobody can say. Voldemort takes the Elder Wand from his hand. Harry reads Snape's grief across a courtyard and knows he was loyal. Dumbledore's letter: *I was afraid of what you would be. I am still afraid. That is not your fault.*

**Threads.**
- A. Draco's mission.
- B. Dumbledore's lessons and his dying.
- C. The Hallows.
- D. Evelyn's Path and its cost.
- E. Theo's Mark.
- F. Lockhart in the field.
- G. Grindelwald.

**Escalation ladder.** Open war in the papers, then a necklace, then a ring that is gone, then *Sectumsempra*, then Evelyn's breakdown, then a tin mine full of Inferi, then the cabinet, then the tower, then Voldemort in Hogwarts, then Dumbledore dead.

**Resolved by others or outside forces.** Snape saves Draco. Dumbledore's death is his own decision, or Voldemort's, not Harry's. The Elder Wand's loyalty follows a law nobody in the room understands.

**Left open.** What Dumbledore asked Snape to do about Harry (revealed Chapter 77).

### Year Seven (Ch 68 to 80): Ultimate Deceit

**Summary.** The Ministry falls at Bill and Fleur's wedding. Sirius dies holding the door, and Moody and Hedwig in the escape. Harry, Evelyn, Ron and Hermione hide in a closed Leeds cinema, where Harry trains illusions on the screen. They raid the Muggle-born Registration Commission, which Evelyn's father chairs. Harry begins pushing courage into frightened people to make them run, and it works, and he does it more. Voldemort kills Grindelwald at Nurmengard, and Evelyn's watch stops. At Malfoy Manor Harry disarms Draco. Dobby dies. Death Eaters punish Hogsmeade. Lockhart dies holding the bridge. Harry arrives late and goes far gone: fourteen Death Eaters standing in the snow inside an illusion that never ends, and Harry sitting on a step eating an apple. For weeks he is cold, effective and frightening. He moves his friends' feelings without asking. Snape, remembering Dumbledore's instruction, lures him to the Shrieking Shack to break his mind and destroy the Cloak. Evelyn kills Snape with his own spell. Harry says "Good." Evelyn opens her mind for the first time in her life and lets him feel everything, and he comes back, badly, and cries for Sirius at last. He has crossed his Threshold. Snape's memories tell him about Dumbledore's fear. Voldemort, holding Wand and Stone, comes to Hogwarts for the Cloak. Harry's plan is to separate him from his army, because Voldemort is strongest in a crowd and Harry is strongest against one mind. In the battle Hagrid, Fred, Lupin, Lucan and Millicent die. In the Forest, with Ron, Hermione, Neville, Millicent and Draco guarding his body and Evelyn anchoring him, Harry opens Ultimate Deceit on one mind. Inside it Voldemort wins: Harry dead, the castle kneeling, the Cloak in his hand, Master of Death. He turns to see himself in the Mirror of Erised and the Mirror shows him Harry. He casts the Killing Curse at the boy in the glass, through a wand that was never his. Evelyn says "Harry" for the first time. He comes back blind to every feeling in the world.

**Threads.**
- A. The fall and the hiding.
- B. Resistance and the Commission; the Selwyns as the enemy.
- C. The Hallows hunt (Voldemort for the Cloak).
- D. Harry's descent.
- E. Snape.
- F. Evelyn as anchor.
- G. The battle.

**Escalation ladder.** The wedding, then hiding, then the Commission, then Grindelwald's death, then Malfoy Manor, then Hogsmeade, then far gone, then the Shack, then the return, then the battle, then the Forest.

**Resolved by others or outside forces.** Sirius's death. Grindelwald's death. The Elder Wand's law. Ron, Hermione, Neville, Millicent and Draco holding the line. Dominion collapsing when Voldemort dies frees everyone it held, which is not Harry's doing.

**Left open.** Where Theo went. What Draco felt. Whether Harry's reading will come back.

### After (Ch 81 to 83): Potter

**Summary.** Funerals and trials in the summer of 1998. Harry turns 18 in a world gone silent: he cannot feel anyone now, and he misjudges people, and has to ask. A year later, in 1999, he and Evelyn are both adults, both working in London, both in the same dark: for the first time she is not the exception. He asks her what she feels. She tells him. The romance begins here, small and funny and tender. The watch's second hand ticks once.

**Threads.** Grief; the trials; Corvin's flight; Harry's blindness; Harry and Evelyn; the watch.

**Escalation.** This arc is the exception to the escalation rule only in scale. Each chapter still turns something: a grave, a verdict, a confession, a question that is not answered.

## 4. Plant and payoff register

Write each plant so it reads naturally the first time. Never point at it.

| Plant | Where planted | Payoff | Where paid |
|---|---|---|---|
| A cold draught under Quirrell's warmth | Ch 2, Ch 6, Ch 8 | It was Voldemort | Ch 10 |
| Snape's loathing has grief under it | Ch 5 | Lily | Ch 49, Ch 77 |
| Isadora goes still at the name Harry Potter | Ch 3 coda (Evelyn POV) | Grindelwald foresaw him | Ch 38 |
| "A lady's thoughts are her own" | Ch 8 | The Grindelwald secret | Ch 34, Ch 38 |
| Evelyn winds the watch every morning | Ch 8 onward | The watch is a Seer's device | Ch 25, Ch 38 |
| "Never wind it backwards" | Ch 24 | The other world | Ch 25 |
| Isadora is silent to Harry too | Ch 11 | Family occlumency, family secret | Ch 34 |
| Lockhart's Himalayan Walker story | Ch 12 | Paths are real | Ch 40 |
| Lockhart: "people see what you show them" | Ch 12, Ch 15 | The Path of Illusion | Ch 26, Ch 62, Ch 79 |
| The diary feels hungry | Ch 16 | Soul-objects feel hungry | Ch 51 |
| Tom's envy of Harry's gift | Ch 16, Ch 19 | The final deceit is built from Tom | Ch 79 |
| The door behind the statue's feet | Ch 20 | Slytherin's study | Ch 22 |
| Tom's scratches "I WILL" on the study door | Ch 22 | Tom could not read hearts | Ch 79 (Harry remembers them) |
| "No divided thing may stand upon a summit" | Ch 23 | The remerge | Ch 49, Ch 51, Ch 54 |
| Oswin, the apprentice who could not find his way back | Ch 23 | The Threshold, far gone | Ch 74 to 76 |
| Evelyn sees through Harry's illusions | Ch 23 | She is the only one who sees him in the snow | Prologue, Ch 73, Ch 76 |
| A cold second presence in the other Harry | Ch 26 | Harry was a Horcrux | Ch 54 |
| Harry senses a faint version in himself and dismisses it | Ch 27, Ch 31 | Same | Ch 51, Ch 54 |
| Aberforth recognises the watch's maker | Ch 29 | Grindelwald made it | Ch 38 |
| The prophecy, heard in the other world | Ch 30 | "You knew about the prophecy." | Ch 44 |
| The other Sirius falls through the Veil | Ch 30 | Harry stops the same curse in this world | Ch 54 |
| Evelyn counts things | Ch 5 onward | The crash-out list | Ch 40 |
| Evelyn calls him "Potter" | Ch 5 onward | "Harry" | Ch 79 |
| Thaddeus's voice under a mask | Ch 34 | The Selwyns in the war | Ch 43, Ch 70, Ch 78 |
| Varga's shame | Ch 35 | His past with Grindelwald | Ch 40, Ch 71 |
| Dumbledore's fear in the office | Ch 44 | His contingency | Ch 77 |
| Kreacher's devotion to "Miss Narcissa" | Ch 47 | The locket reaches Voldemort | Ch 50 |
| Something looks back through the scar | Ch 49 | Voldemort found the journal | Ch 51 |
| Snape's spell in the Prince's book | Ch 58, Ch 60 | Evelyn kills Snape with it | Ch 75 |
| Dead Calm stills healing | Ch 61 | Justin dies | Ch 65 |
| Draco disarms Dumbledore | Ch 64 (and Dumbledore's puzzled glance at the wand, Ch 65) | The wand's allegiance | Ch 79, Ch 80 |
| Harry disarms Draco | Ch 72 | Same | Ch 79 |
| Grindelwald resets the watch | Ch 38 | It stops at his death | Ch 71 |
| The Mirror of Erised: what Harry saw | Ch 7 | The Mirror inside the final deceit | Ch 79 |
| The push on Quirrell | Ch 10 | The final deceit makes Voldemort kill himself as Quirrell did | Ch 79 |
| The Prologue's snow scene | Prologue | Replayed from inside | Ch 73 |
| "She will open the door for you once" (Grindelwald to Harry) | Ch 57 | Evelyn opens her mind | Ch 76 |
| The watch's second hand never moves | Ch 8 | It ticks once | Ch 83 |

## 5. Death register

| Who | Chapter | How | Notes |
|---|---|---|---|
| Quirinus Quirrell | 10 | Turns the Killing Curse on the face in his head after Harry's push | Plain, no gore. Harry's secret |
| The other world's Sirius | 30 | Through the Veil, as in the books | Harry watches |
| The other world's Evelyn | 30 | Unknown | Left alone in the Time Room. Never resolved |
| Isadora Hale | 25 (offstage, February 1994) | Old age, illness | Evelyn's grief triggers the watch |
| Cedric Diggory | 43 | Killing Curse in the graveyard | As canon |
| Bartemius Crouch Sr. | 40 (offstage) | Killed by his son | As canon |
| Nymphadora Tonks | 54 | Voldemort, at the Veil, sudden | Beside Sirius |
| Justin Finch-Fletchley | 65 | Inside Dead Calm, the charm keeping him alive stilled | Evelyn's guilt |
| Albus Dumbledore | 65 | Pinnacle against Pinnacle. Curse or cost, unclear | Elder Wand taken |
| Sirius Black | 68 | Holding the Burrow's door when the Ministry falls | Sudden, mid-chapter |
| Alastor Moody | 68 | In the escape | Offstage or brief |
| Hedwig | 68 | In the escape | One line, felt later |
| Gellert Grindelwald | 71 | Voldemort, at Nurmengard | Grindelwald's POV |
| Elias Varga | 71 | Same | |
| Dobby | 72 | Bellatrix's knife | As canon, in new words |
| Gilderoy Lockhart | 73 | Holding the bridge at Hogsmeade | With style |
| Severus Snape | 75 | Evelyn, *Sectumsempra* | Not gory |
| Rubeus Hagrid | 78 | Holding back giants from first-years | |
| Fred Weasley | 78 | Explosion, as canon | |
| Remus Lupin | 78 | Battle | |
| Lucan Selwyn | 78 | Battle, possibly shielding Evelyn | Ambiguous |
| Thaddeus Selwyn | 78 | Battle | |
| Millicent Bulstrode | 79 | Guarding Harry's body | |
| Lord Voldemort | 79 | His own curse, inside Ultimate Deceit | |

Survivors worth noting: Ron, Hermione, Neville, Luna, Draco, Narcissa, Theo (vanished), Corvin (fled), Marguerite, McGonagall, Aberforth, Kreacher, the Weasleys except Fred.

## 6. Secrets register (who knows what, and from when)

| Secret | Harry knows | Evelyn knows | Dumbledore knows |
|---|---|---|---|
| Harry's gift exists | Always | Ch 5 (she works it out) | Suspects from Ch 4, certain by Ch 20 |
| Harry pushed Quirrell | Ch 10 | Ch 20 (he tells her) | Ch 44 |
| Tom in the diary, the temptation | Ch 16 | Ch 20 | Never fully |
| Slytherin's study | Ch 22 | Ch 22 | Ch 44 |
| The other world | Ch 25 | Ch 25 | Ch 44 (told some), Ch 56 (all) |
| The prophecy | Ch 30 | Ch 31 (he tells her) | Always. Learns Harry knows: Ch 44 |
| Sirius is innocent | Ch 28 | Ch 28 | Ch 33 |
| Grindelwald is Evelyn's grandfather | Ch 40 | Ch 34 | Never told. Guesses in Ch 57 from her face, and says nothing |
| Harry was a Horcrux | Ch 54 | Ch 54 | Suspected from long before. Confirms Ch 56 |
| The Elder Wand's true master is Harry | Ch 80 (Evelyn works it out and tells him) | Ch 80 | n/a |
| Dumbledore's contingency | Ch 77 | Ch 77 | Always |

## 7. Viewpoint exceptions

The story is told by Harry and Evelyn. Only these sections break that, each a single scene:

1. Ch 44: Dumbledore, during the blow-up.
2. Ch 65: Dumbledore, the minute before he opens First Matter for the last time.
3. Ch 71: Grindelwald, at the end.
4. Ch 74: Snape, deciding.
5. Ch 79: none. Even inside the deceit, it is Harry's viewpoint. (The deceit is narrated from inside Harry as its author.)

Do not add others.

## 8. The two requested set-pieces

### 8.1 The Dumbledore blow-up (Chapter 44)

**It has been building for three years.** The ledger, kept in Harry's head and occasionally shown to Evelyn:

- Ch 10: The Stone was bait, and Dumbledore was pleased.
- Ch 17: "Help will always be given at Hogwarts." Harry reads calm. He wanted alarm.
- Ch 20: Dumbledore never stopped the bullying. His answer is wise and useless.
- Ch 31: Harry lies to him, and he believes it.
- Ch 33: Privet Drive again. No reason given that Harry can use.
- Ch 35: "Nothing can be done" about the Goblet. Harry reads alarm and resignation.
- Ch 41: The Pensieve. Harry says the word "Concordat" and watches him flinch.

**The scene.** Harry back from the graveyard, Cedric's blood on his sleeve, Sirius as a dog by the fire, Fawkes on his perch. Dumbledore asks him to tell what happened. Harry says no. Then he says everything above, in order, without raising his voice, getting quieter as he goes. Then: *"You knew about the prophecy."* Dumbledore asks how he knows it. Harry tells him he heard it in a room full of glass in a world where he was in Gryffindor. Dumbledore reaches for his mind, gently, to check. Harry, instead of blocking, pushes: the graveyard, all of it, Cedric's face, the cold of the headstone, the voice saying *kill the spare*. Dumbledore could close against it. He does not.

**Dumbledore's viewpoint section** (one scene, within the chapter): he feels a fourteen-year-old's night and understands that he has spent four years managing a boy who has been managing him. He thinks about Tom at eleven, in the orphanage, and about Gellert at sixteen, and is ashamed of the thought, and keeps it anyway. He sees a Walker's First Step in what the boy just did to him.

**Back to Harry.** Dumbledore says, simply, that Harry is walking a Path, and that he is too. He offers to teach rather than protect. Harry reads respect, grief, and fear, and notes the fear. The equal footing is real from this moment, and so is the fear, and the fear will matter.

**Do not** let anyone cry for long. Do not let Dumbledore apologise more than once. Do not resolve the anger. It is still there in Year 5. It just has a partner now.

### 8.2 Far gone, and brought back (Chapters 73 to 76)

**The fall** (Ch 73): Hogsmeade punished for hiding the resistance. Harry arrives too late. Lockhart dead on the bridge. Harry traps fourteen Death Eaters in an illusion with no end: each lives inside his own worst night, forever, standing in the snow. Harry sits on the post office step eating an apple and watches them. He is perfectly calm. He has decided that feeling things is a luxury for people who are not at war. This is the Prologue from the inside. Evelyn arrives. He looks at her and for a second does not know who she is.

**The fall continues** (Ch 74): weeks. Harry wears illusions constantly, a different face for every raid. He breaks prisoners with illusions for information. He moves his friends' feelings without asking: keeps Ron calm, makes Hermione unafraid, makes a frightened Muggle-born family brave enough to run. It works. It all works. He is the most effective weapon the resistance has. Ron and Hermione are frightened of him. Evelyn, the only one he cannot touch, is the only one who can see him as he is, and he avoids her. Snape's viewpoint section: Snape reads the reports, remembers Dumbledore's instruction, and decides.

**The trap** (Ch 75): Snape asks to meet. Harry trusts him because of the courtyard in Year 6. At the Shrieking Shack, Snape goes for his mind. It is the best occlumens alive against the best natural legilimens alive, and Harry, far gone, is losing. Evelyn, who followed because she trusts nobody, kills Snape with *Sectumsempra*. Snape dies on the Shack floor and gives up his memories.

**The return** (Ch 76): Harry looks at Snape's body and says "Good." Evelyn has just killed a man. She is shaking. He does not notice, because he cannot read her and has stopped looking at anything he cannot read. She closes the door. She opens her mind, for the first time in her life. He feels it all at once: the killing, her terror, her fury at him, her grief, and how much he matters to her, which is the loudest thing he has ever felt from anyone, louder than Hagrid on the rock. It is not a gentle return. He fights it. Then he is sitting on the floor of the Shack with his back to the wall, and the first thing that comes back is Sirius, and he cries for the first time since the wedding.

**The cost.** Evelyn cannot close her mind properly for days. Anyone could read her now. That is how Lucan finds them in Chapter 77.

**The result.** Harry has crossed the Threshold and come back. He knows the way in and the way out. He knows he needs someone at the door.

**Do not** make this romantic. It is the deepest trust two people can give each other. Do not let either of them name what it was.


========================================================================
# FILE: SPOILERS_06_CHAPTERS_PROLOGUE_Y1_Y2.md
========================================================================

# SPOILERS · 06 · CHAPTER PLANS: PROLOGUE, YEAR ONE, YEAR TWO

How to use an entry: write the chapter so that every numbered beat happens, in roughly this order, and the plants and payoffs land. You may add scenes, cut connective tissue, and reorder within the chapter if it reads better. You may not move a beat to another chapter, change who lives or dies, or reveal anything marked as a later payoff.

---

## Prologue: Snow

- **When/where:** a morning in late February 1998. Hogsmeade, the high street, after an attack. Snow.
- **POV:** Evelyn only.
- **Target:** about 3,500 words.
- **Purpose:** a flash-forward hook. The reader sees Harry at his worst, from outside, without explanation, before meeting him as a boy.
- **Beats:**
  1. Open on something small and exact: Evelyn checking her watch out of habit, and remembering it has not worked for two months. She Apparates to the edge of the village.
  2. The street. Smoke from the Three Broomsticks. A body on the bridge she does not let herself look at long enough to name (it is Lockhart; do not name him; one detail, a sleeve of an absurd colour).
  3. Fourteen Death Eaters standing in the snow along the high street. Masks off or askew. None of them moving. Some weeping. One is speaking, quite calmly, to someone who is not there. One is on his knees. Their eyes are open and looking at different things.
  4. Snow has settled on their shoulders. They have been standing there for hours.
  5. Flowers are growing up through the snow around their feet. Evelyn looks at them and sees snow. (She sees through illusions. Do not explain this. Just let her see snow where the reader has been told there are flowers by a passing Order member who sees them.)
  6. Harry is sitting on the step of the post office with his elbows on his knees, eating an apple, watching the Death Eaters the way someone watches a fire.
  7. He looks up at her. For a second there is nothing in his face at all. Then he smiles, politely, the way he smiles at strangers in shops.
  8. He says something perfectly reasonable and perfectly wrong (for instance, that she should not stand so close to them, they are busy).
  9. She notices one exact thing about him that frightens her more than the fourteen men: perhaps that he has taken his glove off to eat and his hand is blue with cold and he has not noticed.
- **Ending:** a short line, from Evelyn, that turns. Something like her realising that he has made himself believe something too. Do not say what. Then `<->`.
- **Don't:** explain the Path, name the spell, give dates beyond what she would think, explain who anyone is, or use the word "illusion".

---

# YEAR ONE

## Chapter 1: The Weather Indoors

- **When/where:** Privet Drive, June to July 1991. Ends on the rock in the sea on the night of 30 to 31 July.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** establish the gift, the cunning, the loneliness, and the Dursleys, through use rather than explanation.
- **Beats:**
  1. Open on Harry reading the house before he is out of the cupboard: who is up, who is in a mood, how loud Uncle Vernon is this morning. He has done this since he was small. He calls it the weather.
  2. Dudley's birthday. Harry reads Vernon (anger with fear under it), Petunia (something under her disgust he has never been able to name, aimed at him and also not at him, a grief), Dudley (greed, and under it, boredom). Harry uses what he reads to steer a small outcome in his favour. Show how practised he is.
  3. The zoo. The snake. Parseltongue. Harry reads nothing from the snake but talks to it anyway. The glass vanishes.
  4. Punishment. The cupboard. Harry's private thought that if anyone could ever feel what *he* felt, even once, he would know what to do with it. (One line, not a speech.)
  5. The letters. Vernon's fear grows louder than his anger for the first time. Harry notices, and keeps it, the way he keeps everything.
  6. Flight to the hut on the rock. Storm. Harry counts down to his birthday on Dudley's watch.
  7. The door comes in.
  8. Hagrid. The reading: the biggest, warmest feeling Harry has ever felt from anyone, and it is aimed straight at him.
- **Plants:** Petunia's buried grief. The "weather" vocabulary. "Loud" and "quiet".
- **Escalation:** from a managed life to a door off its hinges.
- **Ending:** on Hagrid's feeling, not his words.
- **Don't:** reproduce canon dialogue. Rephrase everything. Do not have Hagrid say the famous line in its famous form.

## Chapter 2: The Leaky Cauldron

- **When/where:** 31 July to early August 1991. The hut; London; the Leaky Cauldron; Diagon Alley; Gringotts.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** the reveal, the world, and the first meeting with Quirrell.
- **Beats:**
  1. Hagrid tells him. Harry reads that Hagrid is telling the truth, which is the only reason he believes any of it. Hagrid's grief for his parents, aimed at him.
  2. Dudley's tail. Harry reads Vernon's fear spike into terror and, for a moment, enjoys it. He notices himself enjoying it.
  3. London. Hagrid in the Underground. Harry watching Muggles notice and not notice.
  4. The Leaky Cauldron: the whole room turns loud with one feeling at once, and it is about him. He has never been the centre of a room's weather before. It is too much, and he likes it.
  5. **Quirrell.** Not stammering. A thin, sharp man with a dry voice who shakes his hand and says something precise and slightly sardonic. Harry reads interest, competence, a curious kind of warmth, and under it a cold draught, like air from a closed door. He assumes it is sadness.
  6. Gringotts. Vault 687 (his) and 713. Harry reads the goblins (contempt, mostly, and amusement) and Hagrid's nerves on the cart.
  7. Hagrid explains, a little, about Voldemort. Harry's ambition, plainly: he wants to be someone. He wants a room to turn and feel something about him again.
- **Plants:** the cold under Quirrell.
- **Escalation:** from a boy in a cupboard to a famous name.
- **Ending:** a short turn. Perhaps Harry realising he has never before been anywhere where nobody was angry with him.

## Chapter 3: Madam Malkin's

- **When/where:** Diagon Alley, same day. Madam Malkin's, Ollivanders, Eeylops. Then Privet Drive through August. Then a short coda at Selwyn Hall, Shropshire.
- **POV:** Harry, then a short Evelyn coda.
- **Target:** about 6,000 words.
- **Purpose:** the neutral first meeting with Evelyn, the wand, and a plant in the coda.
- **Beats:**
  1. Madam Malkin's. A girl a year older is on the next stool being refitted because she has grown. She is reading a paperback (a Muggle detective novel, title visible, Ngaio Marsh or similar) and does not look up when he comes in.
  2. Their exchange is short and flat. He says something slightly wrong about Hogwarts that he has picked up from Hagrid; she corrects it without looking up, precisely. He tries to read her and gets nothing. He assumes the shop is busy, or he is tired. He forgets her almost at once. **The impression must be neutral.** No spark. She is introduced by what she says, not by how she looks. Give at most one physical detail (brown hair tied back).
  3. Ollivanders. Holly and phoenix feather. The brother wand. Harry reads Ollivander's unease and fascination.
  4. Hedwig.
  5. August at Privet Drive. Reading the textbooks. The Dursleys frightened of him. Harry experiments, carefully, with how far their fear will let him go. Nothing cruel. Just enough to notice it works.
  6. **Evelyn coda (short).** Selwyn Hall, the next morning at breakfast. Winding her small gold watch, as she does every morning (one clause, no emphasis), she mentions to her grandmother Isadora that Harry Potter was in Madam Malkin's, and that he looked at people "as though he were checking the weather". Isadora goes still. She asks one question about him. Evelyn notices the stillness and files it.
- **Plants:** Isadora's stillness. Evelyn's way of noticing.
- **Escalation:** small. The world is now real and Harry has a wand.
- **Ending:** on Isadora, from Evelyn's view, saying something ordinary in a way that is not ordinary.
- **Don't:** make Evelyn interesting to Harry yet.

## Chapter 4: The Sorting

- **When/where:** 1 September 1991. King's Cross, the train, the lake, the Great Hall.
- **POV:** Harry. One short Evelyn scene at the Slytherin table is allowed.
- **Target:** about 6,500 words.
- **Purpose:** the train without Ron and Hermione, the Sorting into Slytherin, and the first conscious silence.
- **Beats:**
  1. King's Cross. Harry finds the barrier by watching a large red-haired family and reading the mother's warmth. He does not ask them for help. He watches them for a moment longer than he needs to.
  2. The train. He takes an empty compartment. Visitors: a round-faced boy looking for a toad (Neville: fear, and kindness under it); a bushy-haired girl who has read about him (Hermione: anxious superiority with loneliness under it; she leaves quickly). Ron does not come. **Theodore Nott** asks if the seat is free and then reads for an hour. Harry reads a calm sadness in him and likes him for it.
  3. Draco arrives with Crabbe and Goyle and offers to show him which families are worth knowing. Harry reads contempt under the offer, and jealousy aimed at the scar. He declines in a way that is polite and humiliating. Rivalry begins.
  4. A plain second-year girl walks past the compartment door without stopping. Harry does not register who she is.
  5. The boats. The Hall. Hundreds of feelings, a roar he turns down.
  6. The Hat. Write an original, short Hat verse or summarise it. Harry does not ask the Hat for anything. The Hat says he would do well in Slytherin, that he wants to be great, and that there is something else in him it cannot quite name. Harry tells it, silently, that greatness sounds fine.
  7. SLYTHERIN. The Hall goes quiet, and Harry reads it: shock, disappointment, fear, the Gryffindor table's anger. At the staff table, Snape: loathing, and under it something Harry has no name for. Dumbledore: a flicker of something like worry, gone so fast Harry wonders if he imagined it.
  8. The Slytherin table. Lucan Selwyn, sixth-year prefect, welcomes him with a perfect smile. Harry reads calculation. Theo is sorted Slytherin too.
  9. Across the table, the girl from Madam Malkin's is reading under the table. Harry, idly, reads around the table to learn the house. When he reaches her, there is nothing. Not a quiet feeling. Nothing at all. He looks again. Nothing.
- **Plants:** Snape's grief. Dumbledore's flicker of worry.
- **Escalation:** the Sorting's shock, and a silence where there should be a person.
- **Ending:** Harry looking at her, and her looking back, unimpressed, and turning a page.

## Chapter 5: Silence

- **When/where:** September to mid-October 1991. Classes, the dungeons, the library, the Quidditch pitch.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,000 words.
- **Purpose:** classes, Snape, flying, Seeker, and Harry's obsession with Evelyn turning into their first real conversation.
- **Beats:**
  1. Slytherin common room: green light, the lake against the windows, the cold. Harry learns the house: who is whose son, who is afraid of whom. He is good at this.
  2. Snape's first lesson. Snape baits him. Harry reads loathing with grief under it, and is more unsettled by the grief than the loathing.
  3. Quirrell's first Defence lesson. Precise, demanding, clever, occasionally funny. He asks Harry a question nobody else could answer and looks pleased when Harry gets it.
  4. Flying. Neville falls. Draco takes the Remembrall. Harry gets it back in a dive. Snape, not McGonagall, sees, and bends a rule for his house: Harry is Slytherin's Seeker. Marcus Flint's reaction.
  5. Evelyn. Harry tests the silence: he follows her, sits near her in the library, makes noise, drops things, says something meant to make her laugh. Nothing. He starts noticing her habits: she eats the same breakfast every day; she corrects Professor Binns's dates under her breath.
  6. **Evelyn scene:** she has noticed him following her for nine days. She has counted. She has also noticed that he looks at everyone else before they speak, as though he already knows what they will say. She works it out. (Her narration is dry and procedural.)
  7. She confronts him in the library. "Stop doing that." He asks what. She tells him, precisely, including the number of days. Then: "Whatever you're doing to everyone else, it doesn't work on me, does it?"
- **Plants:** Evelyn counts things. She calls him "Potter" from this conversation on.
- **Escalation:** someone has seen through him.
- **Ending:** on her question, or on his answer, which should be a lie that she does not believe.

## Chapter 6: Halloween

- **When/where:** mid to late October, then 31 October 1991. Quirrell's office, the third-floor corridor by accident, a girls' bathroom, the Great Hall.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** Quirrell names Harry's gift and takes him on. Millicent and Theo become friends through the troll.
- **Beats:**
  1. Quirrell keeps Harry after class. He says, mildly, that Harry always knows what the class is feeling before it shows. He names it: a natural legilimens of a rare kind, one who reads the weather of a mind rather than its words. He offers private lessons in Defence on Tuesday and Friday evenings. Harry reads genuine interest and warmth, aimed straight at him, and the cold draught under it. He decides the cold is loneliness. He says yes.
  2. Harry has never had his gift named. He tells Evelyn, cautiously, as though it is nothing. She says it sounds like an excellent way to get detention for the rest of his life.
  3. Harry, Theo, and Draco get lost near the third-floor corridor (a staircase moves, Draco is being Draco). The door. Fluffy. Run. Harry reads nothing from the dog but appetite, which is somehow worse.
  4. Halloween. Pansy Parkinson says something cruel to Millicent Bulstrode at lunch. Harry reads Millicent's misery from across the table.
  5. The feast. Quirrell runs in: troll in the dungeons. He faints. Harry reads him as he falls and finds **no fear at all**. He decides Quirrell must be very brave, or acting for the students' sake.
  6. Millicent is not at the feast. Harry knows where she is because he felt her leave. He and Theo go.
  7. The troll in the girls' bathroom. Millicent, big and furious and terrified, hits it with a sink. Theo is clever with a Levitation Charm. Harry reads the troll (stupid rage) and uses it, gets it to turn. Together they knock it out. A teacher arrives (McGonagall, Snape limping, Quirrell). Snape's leg is bleeding. Harry reads pain and fury.
  8. Millicent, afterwards, says one short blunt thing that makes them friends.
- **Plants:** no fear in Quirrell. The cold draught (second time).
- **Escalation:** a mentor, a monster, a friendship forged.
- **Ending:** a small turn: perhaps Quirrell, at the first private lesson, saying something kind that Harry will remember in Chapter 10.

## Chapter 7: The Mirror

- **When/where:** November to December 1991. The Quidditch pitch, Hagrid's hut, the castle at Christmas, a disused classroom.
- **POV:** Harry, with one Evelyn scene in the stands.
- **Target:** about 6,500 words.
- **Purpose:** the jinxed broom, Flamel, the Cloak, and the Mirror.
- **Beats:**
  1. Slytherin versus Gryffindor. Harry flies well. Then the broom bucks. He is too high to read anyone.
  2. **Evelyn scene in the stands:** she sees Snape staring and muttering. She also sees Quirrell staring and muttering. She cannot tell which matters. She pushes along the row towards Snape and, on the way, knocks into Quirrell hard enough to break his eye contact. She will never say whether that was on purpose. Write it so the reader cannot tell either.
  3. Harry catches the Snitch (perhaps nearly swallows it). Slytherin wins. Gryffindor loathing is loud.
  4. Hagrid lets slip "Nicolas Flamel". Harry asks Evelyn. She says she will look into it in a tone that means she has already started.
  5. Christmas. Harry stays. Evelyn goes home. Before she goes, a small, dry exchange that shows they are now friends without either saying it.
  6. Christmas morning. Presents from Hagrid, Theo (a book), Millicent (sweets), Evelyn (something precise and useful, for instance a pocket diary of the year's Quidditch fixtures with errors corrected). And an Invisibility Cloak with an anonymous note. Harry reads nothing from a note.
  7. The Mirror of Erised. Harry sees his parents. In the mirror he can feel what they feel, and what they feel is about him. He goes back three nights.
  8. Dumbledore at the mirror. Harry reads him: real sorrow, and, under it, something careful and considering, as though Dumbledore is measuring him. The first entry in Harry's private ledger.
- **Plants:** what Harry wants (to be felt). The ledger. Whether Evelyn meant it.
- **Escalation:** someone tried to kill him in front of the whole school.
- **Ending:** on the ledger entry, in Harry's head, in one line.

## Chapter 8: Lessons

- **When/where:** January to April 1992. Quirrell's office, the library, the Owlery, Hagrid's hut, the Astronomy Tower.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** Quirrell's best months, the friendship with Evelyn, Flamel, Norbert, and the detention.
- **Beats:**
  1. Quirrell's lessons deepen. Disarming, shielding, reading an opponent. He teaches Harry to quieten the noise of a crowd. He tells Harry, once, that he is wasted on people who will only ever be afraid of him. Harry reads pride and fondness, steady as a lamp. The cold under it, as always.
  2. Evelyn finds Flamel (a Chocolate Frog card, or a footnote in a book nobody reads). The Stone.
  3. **The watch.** Harry notices she winds a small gold watch every morning at breakfast. He asks. She says it was her grandmother's present when she started school, and that Grandmother says to wind it every morning. Its lid has ivy leaves. It has a second, very fine hand that does not seem to move. Harry asks why he cannot read her. She says her grandmother taught her to keep her thoughts to herself. "A lady's thoughts are her own." She says it as a quotation, a little sardonically.
  4. **Evelyn scene:** she lies awake and realises she has told Potter something she has never told anyone, which is that the lessons happen every morning, and that she does not know what they are for.
  5. Hagrid's dragon egg. Norbert hatches. Harry, Theo and Millicent help. Draco sees.
  6. Charlie's friends at the Astronomy Tower at midnight. Caught by Filch on the way down (Draco's tip). Points lost. The school's Slytherins are furious at Harry too, briefly, which is a new kind of noise.
- **Plants:** the watch and its still second hand. "A lady's thoughts are her own." Quirrell's line about being wasted on people.
- **Escalation:** the Stone is real, and Harry is in trouble with everyone.
- **Ending:** the detention notice: the Forbidden Forest.

## Chapter 9: The Forest

- **When/where:** May 1992. The Forbidden Forest at night, Quirrell's office, the exam halls, the Owlery.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** the thing drinking unicorn blood, the doubt, the doubt dissolved, and the decision.
- **Beats:**
  1. Detention with Hagrid and Draco and Fang. Draco's fear, loud and badly hidden. Harry knows Draco knows he can tell.
  2. The dead unicorn. A hooded shape drinking. Harry reads it and finds the same cold draught he feels under Quirrell, but stronger, and with nothing warm on top. His scar burns.
  3. Firenze. He says a few things in a centaur's way. Harry reads sorrow and certainty.
  4. Harry does not tell anyone what he felt, because he does not believe it. He goes to his next lesson with Quirrell and pays attention. Quirrell seems to sense something wrong and is unusually kind. Harry reads affection, real and steady. The doubt goes. (This is the cruelest beat of the year. Write it straight.)
  5. Exams. Hagrid lets slip how to get past Fluffy.
  6. Dumbledore is called away. Harry reads McGonagall's irritation at his questions.
  7. Harry decides someone is going after the Stone tonight. He thinks it is Snape. Theo, Millicent and Evelyn decide to come.
- **Plants:** the forest cold matches Quirrell. Harry chooses not to know.
- **Escalation:** the castle is unguarded and Harry is going down the trapdoor.
- **Ending:** the four of them at the third-floor door at night, with the music already playing.

## Chapter 10: What the Mirror Wanted

- **When/where:** the same night and the days after. The trapdoor and the chambers; the hospital wing; the library; the Great Hall; the train; Privet Drive.
- **POV:** Harry.
- **Target:** about 8,000 words (climax).
- **Purpose:** the betrayal, the push, the death, the silence.
- **Beats:**
  1. Devil's Snare (Millicent's strength and Theo's memory of a Herbology lesson). Keys (Harry). Chess (Theo plays and is sacrificed, knocked out cold). The troll, already down. Potions logic (Evelyn solves it in silence, quickly, then says there is only enough to go forward for one). She does not say "be careful". She says something dry, perhaps that if he dies she will be extremely annoyed.
  2. The last chamber. It is not Snape. It is Quirrell.
  3. Quirrell explains, briefly, without gloating. He is sorry. Harry reads that he is sorry. He reads fondness, real, aimed at him. He reads terror. He reads Quirrell hating himself.
  4. The Mirror. The turban. The face. Voldemort speaks. He offers Harry a place: they are alike, they both know what people want. Harry reads the face and finds the cold with nothing on top, and hunger.
  5. Harry refuses. Quirrell is ordered to take the Stone from him. Quirrell's hands on him burn.
  6. Harry, in terror and fury, does something he has never done: he takes everything Quirrell feels about himself, all of it, and pushes it back into him, louder. He does not know he is doing it. He only knows he wants Quirrell to feel what Harry feels about him.
  7. Quirrell stops. He looks at Harry. He reaches up behind his own head with his wand, at the face, and speaks the Killing Curse. Green light. Write the death plainly and briefly. Voldemort's shade tears free and through Harry.
  8. Hospital wing. Dumbledore. He explains love and protection: Quirrell could not bear to touch him. Harry knows that is not what happened. He reads Dumbledore: warmth, relief, and quiet satisfaction that things went as he had arranged. The ledger: the Stone was bait. Harry says thank you.
  9. Harry does not speak to anyone for four days. Not Theo, not Millicent, not Evelyn. He sits in the library at the same table.
  10. Evelyn sits opposite him every day, at the same time, reading, saying nothing. On the fourth day she slides a note across. It says something dry and specific (for instance, that his Charms essay is due tomorrow and is eleven inches short). He answers her. That is all.
  11. The end-of-year feast. House points as you like: Slytherin wins, or loses narrowly to a last-minute Dumbledore award. Either way Harry reads Gryffindor's hatred, Slytherin's glee, and Dumbledore's pleasure, and feels nothing.
  12. The train. Evelyn: "Write. I'll answer. I won't promise to be interesting."
  13. Privet Drive. The Dursleys' fear, loud. For the first time, Harry thinks about what he could make them feel.
- **Payoffs:** the cold draught. The Mirror. Quirrell's kindness was real.
- **Plants:** the push. Harry's secret.
- **Escalation:** Harry has killed a man and nobody knows.
- **Ending:** the thought about the Dursleys, unfinished. Unsettling, not cruel.
- **Don't:** let Harry explain to himself what he learned. Do not say "emotion is not intention". Show him not trusting his readings in the first scene of Year 2.

---

# YEAR TWO

## Chapter 11: Isadora

- **When/where:** July to August 1992. Privet Drive; a long black car; Selwyn Hall in Shropshire; Ludlow; Diagon Alley; Flourish and Blotts.
- **POV:** Harry, with one Evelyn scene at Selwyn Hall.
- **Target:** about 6,500 words.
- **Purpose:** Dobby, rescue by Isadora, Evelyn's family, Lockhart in person, the diary planted.
- **Beats:**
  1. Open with Harry *not* trusting a reading: Aunt Petunia is pleasant to him one morning and he spends the whole day braced. (Shown, not explained.)
  2. No letters from anyone all summer. His birthday. The Masons. Dobby: terror and devotion, loud. The pudding. Bars on the window.
  3. Evelyn has noticed that he has not answered her letters, three of them, eleven days apart. She tells her grandmother. Isadora Hale arrives at Privet Drive in a very old, very clean car driven by nobody, wearing grey, with a cane she does not need. She is perfectly courteous to Vernon in a way that makes him sit down. Harry tries to read her: silence. He looks at Evelyn in the back seat. She looks back as if to say: now you know.
  4. Selwyn Hall: the yew walk, grey stone, a portrait that looks down its nose. Marguerite (warm, vague, a glass in the late morning). Lucan (pleasant, curious, watching Harry the way a cat watches a bird it cannot be bothered to catch yet). Corvin is "in London". Harry reads them all and finds nothing in Isadora and Evelyn.
  5. **Evelyn scene:** Isadora asks Evelyn questions about Harry at breakfast. Too many. Evelyn counts them (seven) and notes that her grandmother has never asked seven questions about anyone.
  6. A week. Ludlow on foot: a second-hand bookshop where Evelyn buys Muggle detective novels and hides them in her trunk. Harry likes the town because nobody in it knows him.
  7. Diagon Alley with Isadora. Flourish and Blotts. **Gilderoy Lockhart** at a signing, enormous and charming, who spots Harry and insists on a photograph. Harry reads him and is startled: delight, genuine; vanity, enormous; and under it, courage, plain and solid. No fear, no lie. Lockhart is exactly what he says he is.
  8. Lucius Malfoy and Arthur Weasley. A scuffle. Lucius slips something into a small red-haired girl's cauldron. Harry reads Lucius's satisfaction as he does it and does not know what it means.
- **Plants:** Isadora silent. Isadora's questions. Lucius's satisfaction.
- **Escalation:** a house of people Harry cannot read, and a diary loose in the world.
- **Ending:** Isadora, at the Leaky Cauldron, saying something to Harry that sounds like advice and is in fact a test.

## Chapter 12: The Real Thing

- **When/where:** September 1992. The train; Hogwarts; Lockhart's classroom; the Quidditch pitch; the Slytherin common room.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** Lockhart's competence, Draco on the team, a slur, and the first mention of Paths.
- **Beats:**
  1. The train with Evelyn, Theo and Millicent. Ordinary. Funny. Harry's best morning in months.
  2. Lockhart's first lesson. A cage of Cornish pixies. Everyone expects a fraud. He releases them, lets them riot for three seconds for effect, and puts every one back in the cage with one spell and a bow. The class is silent. Then he laughs, delighted with himself, and the silence breaks.
  3. Lockhart notices that Harry did not flinch when the pixies were loose. He asks him to stay. He recruits Harry as his assistant for "practical demonstrations" on Thursdays. Harry reads delight and something shrewd.
  4. Quidditch: Lucius buys the team brooms and Draco a Chaser's place. He wants Seeker. Rivalry inside the team.
  5. Draco calls a Muggle-born Gryffindor (Hermione) a slur at the pitch. Harry reads her hurt from twenty yards. He says nothing in public. Later, privately, he says one precise thing to Draco about Lucius that he has learned by reading Draco for a year, and leaves him white.
  6. A Thursday demonstration. Lockhart teaches misdirection: the flourish of a cape that hides the wand hand. "People see what you show them, Harry. Nearly everyone. Nearly always."
  7. In a later lesson, Lockhart tells the class a story about a man he met in the Himalayas in 1983 who could stop an avalanche by thinking about it, and who called himself a Walker. The class rolls its eyes. Harry reads him: no lie.
- **Plants:** "People see what you show them." Walkers.
- **Escalation:** small. Harry has a second mentor, and he has made Draco hate him properly.
- **Ending:** on Lockhart's story, or on Draco's face.

## Chapter 13: Writing on the Wall

- **When/where:** October to 31 October 1992. Nearly Headless Nick's deathday party in the dungeons; a corridor on the second floor; Binns's classroom.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,000 words.
- **Purpose:** the voice in the walls, Mrs Norris, suspicion.
- **Beats:**
  1. The deathday party. Harry, Evelyn and Millicent go because Nick asked Harry and Harry felt sorry for him (he can feel ghosts, faintly: a thin grey sadness). Comic and grim. Myrtle.
  2. On the way out, a voice in the wall: *kill, rip, tear*. Only Harry hears it. He follows it.
  3. Mrs Norris, Petrified. Writing on the wall. The crowd. Filch's grief, loud. Lockhart's genuine distress. Snape's suspicion, aimed at Harry. Dumbledore examining the cat.
  4. Harry tries to read the cat. Silence. It disturbs him in a way he does not understand yet.
  5. **Evelyn scene:** she already knows the legend of the Chamber because she reads everything. She also notices that Harry heard something the rest of them did not, and that he lied about it.
  6. Binns tells the legend. The class looks at Harry, the Slytherin Seeker who found the cat.
- **Plants:** Petrified creatures are silent. Harry lies to Evelyn.
- **Escalation:** the school starts watching him.
- **Ending:** Evelyn asking him, very quietly, what he heard.

## Chapter 14: The Duelling Club

- **When/where:** November to mid-December 1992. The Quidditch pitch (a rogue Bludger), the hospital wing, the Great Hall as a duelling stage.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** Lockhart beats Snape; Parseltongue; the school turns.
- **Beats:**
  1. Quidditch. A Bludger that hunts Harry. His arm breaks. Lockhart, running onto the pitch, heals it perfectly with one spell. (A deliberate reversal of the books. Everyone is astonished.)
  2. Dobby in the hospital wing at night. The Bludger was his. Harry reads devotion and terror. Colin Creevey is brought in, Petrified.
  3. Lockhart and Snape announce a Duelling Club. They duel as a demonstration. **Lockhart wins**, gracefully, without humiliating Snape, which humiliates him more. Harry reads Snape: fury, shame, hatred, now aimed at Lockhart as well.
  4. Harry versus Draco. Draco conjures a snake. Harry speaks to it without realising it is not English. The hall goes loud with one feeling at once: fear, aimed at him.
  5. Justin Finch-Fletchley, whom the snake was going for, shouts that Harry set it on him.
  6. Justin and Nearly Headless Nick are found Petrified. Harry is found nearby.
  7. Three-quarters of the school turns against him. Write the noise of it in a corridor.
  8. And Slytherin, in the common room that night, goes quiet when he comes in, then makes room for him by the fire. Older students he has never spoken to nod. Harry reads awe, fear, and want. He understands what they think he is.
  9. Evelyn: "You're letting them think it." "Yes." "Be careful what they'll want for it."
- **Plants:** Snape's hatred of Lockhart.
- **Escalation:** the whole school is afraid of him, and his house wants to use him.
- **Ending:** on Evelyn's line or Harry's answer.

## Chapter 15: The Heir's Privileges

- **When/where:** December 1992 to January 1993. Corridors; the library; the Restricted Section; a Slytherin seventh-year's dormitory with a trunk of family books; the castle at Christmas; Lockhart's office.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** ostracism, study, favours, moral greyness, and the investigation.
- **Beats:**
  1. Hexes in corridors from Gryffindors and Hufflepuffs. Harry learns shield charms because he has to, then learns them better than anyone in his year.
  2. Slytherin favours. A seventh-year (Adrian Pucey) lends him books from his family's library that the school would never allow. Others offer protection, notes, introductions, invitations. Harry accepts. He neither confirms nor denies. He reads exactly how much each of them wants him to be the Heir and gives each of them exactly enough.
  3. His range grows: he can read a classroom through a wall. At the peak of someone's feeling a word sometimes comes through. A Hufflepuff he passes thinks the word *murderer* and Harry hears it.
  4. Christmas. Harry stays. Evelyn stays too and says she prefers the quiet. **Evelyn scene:** she wrote to her grandmother that she was staying because the library is empty at Christmas. She notes, precisely, that this is true and is not the reason.
  5. The investigation. Harry wants to know who the Heir is, partly to clear himself and mostly because he wants to know. He sets up a conversation with Draco in which, by reading him, he learns Draco does not know either and is furious that someone else might be the Heir. (This replaces the books' Polyjuice plot. It is Harry's cunning, not a potion.)
  6. Lockhart over Christmas, in his office full of his own portraits, teaching Harry stagecraft: how to make a room look at your left hand. He tells a story about a werewolf in Wagga Wagga that is entirely true. Harry reads that it is true and laughs anyway.
- **Plants:** Harry's growing range. Lockhart's stagecraft.
- **Escalation:** Harry is powerful and isolated and enjoying a lie.
- **Ending:** Myrtle's bathroom is flooded.

## Chapter 16: T. M. Riddle

- **When/where:** January to February 1993. Myrtle's bathroom; the Slytherin dormitory at night; the library.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the diary and the temptation.
- **Beats:**
  1. A small black diary on the bathroom floor. Myrtle threw it. Harry picks it up and feels something from it. Hunger. Loneliness. From a *book*. He has never felt anything from an object.
  2. He writes in it. Tom answers.
  3. Tom shows him a memory: fifty years ago, Hagrid. Harry reads Tom inside the memory and notices Tom is pleased with himself. He does not believe Hagrid did it. He does not say so.
  4. He keeps the diary. He does not tell Evelyn. (His first secret from her. Note it.)
  5. Nights of talk. Tom understands him: the loneliness, the ambition, the house that wants to use him, the gift. Tom says he could always tell what people wanted too. Harry asks if he could ever feel what they *felt*. The ink pauses. Harry reads, from the page, something sharp: envy.
  6. Tom teaches him a few things: a jinx; how to make a frightened person more frightened with only your voice. Harry practises the second on a Gryffindor who hexes him. It works. He enjoys it. He stops himself, and is not sure why.
  7. Evelyn notices he is sleeping less. She says so, with a number of hours.
- **Plants:** soul-objects feel hungry. Tom's envy. Tom could never feel what people felt.
- **Escalation:** the first person who understands him is the monster.
- **Ending:** Harry writing "Goodnight, Tom" and the page answering.

## Chapter 17: Still

- **When/where:** February to May 1993. The Slytherin dormitory; the library; the hospital wing; Hagrid's hut at night.
- **POV:** Harry, with one Evelyn scene (her last before she is Petrified).
- **Target:** about 7,000 words.
- **Purpose:** the diary is stolen; Evelyn is Petrified; Hagrid and Dumbledore removed.
- **Beats:**
  1. The diary is gone from his trunk. Harry turns the dormitory upside down. He suspects Draco. It was not Draco.
  2. **Evelyn scene:** she has worked it out. Spiders leaving the castle, a crowing rooster killed, the word *basilisk* in a bestiary, and the pipes. She is going to the library to check one page before she tells Potter. She takes a small mirror from her bag because she is the sort of person who checks corners. In the library, Hermione Granger is at the same shelf, holding a mirror too. They look at each other. Neither speaks. End the scene there.
  3. Harry, at breakfast, waiting for her. She does not come. McGonagall's face.
  4. The hospital wing. Evelyn lying Petrified, a torn page in her fist. Hermione in the next bed. Harry reaches for Evelyn as he always does and finds silence, as he always does, and realises he cannot tell whether she is in there. Her silence and a statue's are the same. This is the worst thing that has ever happened to him and he does not show it.
  5. That night, Hagrid's hut under the Cloak. Fudge and Lucius come for Hagrid and for Dumbledore. Harry reads Lucius's triumph and Fudge's cowardice. Dumbledore says help will always come at Hogwarts. Harry reads calm. He wanted alarm. (Ledger.)
  6. Hagrid: follow the spiders.
- **Plants:** the torn page.
- **Escalation:** the one person who matters is stone, and the only adults who could help are gone.
- **Ending:** Harry taking the page from her fist.

## Chapter 18: Aragog

- **When/where:** May 1993. The Forbidden Forest; Aragog's hollow; the corridor outside the staff room; the Slytherin common room.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** the spiders, the truth about Myrtle, and Ginny taken.
- **Beats:**
  1. Harry and Millicent follow the spiders. (Theo stays because someone must cover for them.) Fang.
  2. Aragog. Harry reads hunger, enormous, and under it grief for Hagrid. Aragog tells them the monster is not a spider and that a girl died in a bathroom.
  3. Escape. Use cunning and Fang and Millicent's strength. (No flying car.)
  4. The torn page: *basilisk*, and in Evelyn's small handwriting in the margin, *pipes*. Harry understands. The voice in the walls. Myrtle.
  5. Writing on the wall: a girl has been taken into the Chamber. Ginny Weasley. Harry reads the staff: horror, and in Lockhart, at once, resolve.
- **Escalation:** a child is going to die.
- **Ending:** Harry going to Lockhart's office.

## Chapter 19: The Chamber

- **When/where:** the same night. Lockhart's office; Myrtle's bathroom; the pipes; the tunnel; the Chamber of Secrets.
- **POV:** Harry.
- **Target:** about 8,000 words (climax).
- **Purpose:** Lockhart's courage, Tom's offer, the choice.
- **Beats:**
  1. Lockhart is packing a bag, not to flee but because he is going in himself and was about to fetch Harry, the only Parselmouth in the school. He is delighted Harry has saved him the walk.
  2. Myrtle. Harry opens the sink in a language he has never chosen.
  3. The pipes. The tunnel. A shed skin twenty feet long. Lockhart's flourish of a joke, and Harry reads that he is very frightened and very determined.
  4. The roof gives. Lockhart holds the collapsing tunnel up with a spell. He cannot move and keep it up. He tells Harry to go on, and makes it sound like a stage direction. Harry reads pain and absolute resolve.
  5. The Chamber. Ginny. Tom, nearly solid. Harry reads him: hunger, triumph, and, when Harry looks at him, envy again.
  6. Tom's offer, again: they are the same. He will teach Harry everything. Harry is tempted. Truly. Let the reader feel it in what he does not say.
  7. The basilisk. Fawkes. The Hat. The sword. Harry kills the snake. A fang in his arm.
  8. Harry picks up the fang and looks at the diary. Tom, flickering, says his name, gently, the way a friend would. Harry stabs the diary.
  9. Fawkes's tears. Ginny. Back through the tunnel to Lockhart, still holding the roof up, grey in the face, who says something charming and then lets go and collapses.
- **Payoff:** Tom's envy.
- **Plants:** Tom's feelings, which Harry has now read for weeks and will remember.
- **Escalation:** the loudest night of the year.
- **Ending:** Harry carrying, or helping carry, Lockhart, and Lockhart saying something absurd.

## Chapter 20: Mandrakes

- **When/where:** late May to June 1993. Dumbledore's office; the hospital wing; St Mungo's (one visit); the Chamber entrance; the train.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** aftermath, Dobby freed, the ledger, Evelyn restored, the truth told, and the door.
- **Beats:**
  1. Dumbledore's office. Lucius. Dobby freed by Harry's trick with a sock in the diary. Harry reads Lucius's fury and Dobby's joy.
  2. Dumbledore, alone with him. The Hat, the sword, choices. Harry asks why nobody stopped what the school did to him all year. Dumbledore's answer is wise and kind and useless. Harry reads relief, pity, and nothing else. (Ledger.) He says thank you again.
  3. Lockhart's back is broken. He is taken to St Mungo's. Harry visits once, before the end of term: Lockhart in a ward full of flowers from fans, signing his own get-well cards, very funny, in pain. "Nearly everyone, Harry. Nearly always." He will be in St Mungo's for two years.
  4. The Mandrakes. Evelyn wakes. Her first words are dry and specific (perhaps that she has missed eleven weeks of Arithmancy).
  5. Harry tells her everything. Including the diary. Including the nights with Tom. Including Quirrell, and what he did. He chooses to. She listens without interrupting. She does not forgive or condemn. She asks one precise question. That is the moment the friendship becomes what it will be.
  6. Before the train, Harry goes down to the Chamber once more alone. Behind the great statue's feet he feels something he has not felt before: not a person, not hunger, something that seems to be waiting to be *read*. He cannot open it. He leaves.
- **Plants:** the door.
- **Escalation:** small, but he now has something to come back for.
- **Ending:** Harry on the train, knowing he is going back down in September.


========================================================================
# FILE: SPOILERS_07_CHAPTERS_Y3.md
========================================================================

# SPOILERS · 07 · CHAPTER PLANS: YEAR THREE

Chapters 26 to 30 take place in the other world: the world of the books, in late April to June 1996, two years ahead of home. Inside those chapters, the other world's people are written as their canon selves at that point in the books. Never quote the books. Retell in new words, and only from what our Harry and Evelyn can see, hear and read.

---

## Chapter 21: The Knight Bus

- **When/where:** July to August 1993. Privet Drive; a dark street in Magnolia Crescent; the Knight Bus; the Leaky Cauldron; Diagon Alley; Florean Fortescue's.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** the first deliberate push since Quirrell, Black's escape, and a free summer.
- **Beats:**
  1. Aunt Marge. A week of her. Harry reads her cruelty, which is simple and loud and enjoys itself.
  2. At dinner she insults his mother. Harry does not lose control. He decides. He pushes, carefully, shame into her: all the shame she has never felt about anything. She bursts into tears at the table and cannot stop. She weeps for an hour. Vernon does not know what has happened. Harry does.
  3. Harry is frightened by how easy it was and by how little it cost him. He packs and leaves.
  4. Magnolia Crescent. A huge black dog in the dark. Harry reads it: something, but not an animal's something. Then the Knight Bus nearly flattens him. Stan Shunpike. A comic, lurching ride.
  5. The Leaky Cauldron. Fudge, relieved and patronising and frightened of Black. Harry reads that Fudge is far more frightened than he is letting on. He is not expelled.
  6. Three weeks of freedom in Diagon Alley. Ice cream at Fortescue's. Homework. Evelyn visits for one afternoon with Isadora, who is walking with the cane now and needs it. Harry notices. Evelyn notices him noticing.
  7. The Leaky's last night: Harry overhears Arthur Weasley telling his wife that Black is after Harry.
- **Plants:** Isadora's decline. The dog.
- **Escalation:** Harry has started using the push on purpose. A murderer is looking for him.
- **Ending:** on what Harry decides to do with what he has overheard (nothing, outwardly).

## Chapter 22: Dementors

- **When/where:** 1 September to October 1993. The train; the Great Hall; Lupin's classroom; Hagrid's paddock; Myrtle's bathroom; the Chamber; Slytherin's study.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** Dementors, Lupin, Buckbeak, the Marauder's Map, and the study.
- **Beats:**
  1. The train: Harry, Evelyn, Theo, Millicent, and a shabby man asleep in the corner. The lights die. A Dementor. Harry reads it and finds only appetite. Then he hears a woman screaming and goes under. He wakes to chocolate. The man is Lupin.
  2. Harry reads Lupin: kindness, and, aimed at Harry, an old guilt he does not understand.
  3. Evelyn, on the floor of the compartment, was not affected the way the others were. (Dementors work on feeling, and she has a closed mind. She was cold and frightened, but she did not hear anything.) She notes it.
  4. Hagrid's first lesson. Buckbeak. Draco insults him and is slashed. Harry reads Draco's pain, real, and his plan to use it, also real. Lucius will make Hagrid pay.
  5. Lupin's Boggart lesson. Lupin stops it before Harry's turn. Harry reads why: Lupin is afraid of what it would show.
  6. Fred and George Weasley corner Harry, the Slytherin everyone hated last year, and give him the Marauder's Map, on the grounds that anyone the whole school loathed that much deserves it. Harry reads that they mean it, and that they enjoy being contrary. A small comic scene.
  7. The Chamber, with Evelyn. The statue. The place behind its feet. Harry puts his hand on the stone and, instead of speaking to it, *reads* it, as he would a person. It reads him back. The door opens.
  8. **Evelyn scene:** the study as she sees it. Round, lined with shelves, a desk of black stone, a lamp that lights itself when Potter walks in and not when she does. On the inside of the door, scratched deep into the stone, the letters *I WILL*. She records the detail.
- **Plants:** Dementors and closed minds. Tom's scratches. The map.
- **Escalation:** a door that has been closed for a thousand years is open.
- **Ending:** the lamp lighting, or the scratches.

## Chapter 23: Slytherin's Study

- **When/where:** October to November 1993. The study; the Quidditch pitch in a storm; the hospital wing; Lupin's office.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** the leap in power, the first illusions, Evelyn's immunity, and the journal's warnings.
- **Beats:**
  1. Slytherin's journals, written in old English and Latin. Evelyn reads Latin better than he does. She translates. She is pleased to be useful and does not say so.
  2. The *reading of hearts*: Slytherin was one of them. Exercises. Harry trains at night, three or four times a week, Evelyn reading aloud and correcting his pronunciation of Latin.
  3. He learns to read thoughts with eye contact, not only feelings. He tries it on Theo (who agrees, curious) and catches a memory of Theo's mother. He apologises. Theo says it is all right and Harry reads that it is not.
  4. The first illusion: he makes Millicent see a Galleon on the table. She tries to pick it up. He makes Evelyn see it. She does not. "There's no coin, Potter." She is the only one.
  5. In the journal: *The Paths are open to many, but no divided thing may stand upon a summit.* Evelyn translates it and they do not know what it means. Also: Slytherin's apprentice, Oswin, *who walked the way of seeming, and at its height could not find the door back to himself*. Evelyn reads it out. Harry asks her to read it again.
  6. Quidditch in a storm. Dementors on the pitch. Harry falls. His broom goes into the Whomping Willow. He wakes in the hospital wing.
  7. Lupin agrees to teach him the Patronus. First lesson. Harry realises the Patronus is a feeling, projected, which is close to what he did to Quirrell, but outward and clean. He does not say this to Lupin.
- **Plants:** "no divided thing". Oswin. Evelyn sees through illusions.
- **Escalation:** Harry is suddenly far more powerful than a thirteen-year-old should be, and has read a warning he does not understand.
- **Ending:** on Oswin, or on the coin she does not see.

## Chapter 24: The Three Broomsticks

- **When/where:** December 1993. Hogsmeade; the Three Broomsticks under the Cloak; the Shrieking Shack seen from the fence; the Slytherin common room; then Selwyn Hall at Christmas.
- **POV:** Harry, then a long Evelyn section at Selwyn Hall.
- **Target:** about 6,500 words.
- **Purpose:** Black's "betrayal", Harry's murder plan, and Isadora's last instruction.
- **Beats:**
  1. Harry's Hogsmeade form was signed by Uncle Vernon in August. He made Vernon want to sign it. (One line. Note it without comment.)
  2. Hogsmeade with Evelyn, Theo, Millicent. Honeydukes. Snow.
  3. The Three Broomsticks, under the Cloak. Fudge, McGonagall, Hagrid, Madam Rosmerta. Black was his parents' Secret Keeper. Black betrayed them. Black killed Pettigrew. Harry reads that every one of them believes it, and Hagrid's grief and rage, loudest of all.
  4. Harry goes back to the castle alone. In the study, he begins to plan, carefully, how to kill Sirius Black. It is a practical plan. It is frightening because it is calm.
  5. The Firebolt arrives on Christmas morning with no note. McGonagall confiscates it for checks.
  6. **Evelyn at Selwyn Hall.** Isadora is dying, in the east wing, of old age and of something the Healers cannot name. Marguerite drinks. Corvin talks politics with Lucan in the study. Evelyn sits with her grandmother.
  7. Isadora's last lucid conversation. She asks if Evelyn still winds the watch. Every morning. She says: *never wind it backwards. If you ever do, wind it forwards again at once.* Evelyn asks why. Isadora says she is tired. She asks one question about Harry, and Evelyn answers it, and Isadora seems satisfied in a way Evelyn does not understand.
- **Plants:** "never wind it backwards". Isadora's satisfaction.
- **Escalation:** Harry is planning a killing. Isadora is dying.
- **Ending:** on Isadora's instruction, or on Evelyn winding the watch the next morning and holding it a moment longer than usual.

## Chapter 25: Backwards

- **When/where:** January to the first days of March 1994. Gryffindor Tower in uproar; the Slytherin common room; the Owlery; the study.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** Black in the castle, Isadora's death, the watch wound backwards.
- **Beats:**
  1. The Firebolt returned. A match against Ravenclaw. Harry flies very well.
  2. That night Black is in Gryffindor Tower with a knife, standing over a boy's bed (Ron Weasley's; mention him, nothing more). The castle in panic. Harry, in the study, refines his plan, and asks Evelyn to translate a passage on stilling a heart. She refuses. They argue. It is their first real argument. It is quiet and bad.
  3. An owl in February. Isadora is dead. Evelyn goes home for the funeral and comes back three days later more closed than Harry has ever known her. She does not want to talk about it, and says so precisely.
  4. **Evelyn scene:** in the dormitory at night, the watch in her hand. She realises she does not know a single thing her grandmother was afraid of. Except this.
  5. The study, a few days later, early March. Harry practising. Evelyn reading. She takes the watch out, looks at it, and, slowly, deliberately, begins to wind it backwards. "I want to know what she was afraid of." Harry reaches for her hand to stop her. He is touching her when the second hand moves for the first time.
  6. The world turns sideways. Write it as an absence rather than an effect: no sound, no light, a sense of a stair that is not there.
  7. They are on the floor of the Chamber. The basilisk's skeleton is where it was. But the study door behind the statue is closed, and when Harry opens it, his books are gone, his notes are gone, and the dust on the desk is undisturbed.
  8. Up through the pipes. Myrtle's bathroom. Myrtle looks at Harry and says he looks like that horrible Potter boy but smaller.
  9. On the bathroom wall outside, a framed notice: *Educational Decree Number* something, by order of the High Inquisitor.
- **Plants:** the second hand moved.
- **Escalation:** they are somewhere else.
- **Ending:** on the notice, or on Myrtle's line.

## Chapter 26: The High Inquisitor

- **When/where:** the other world, late April 1996. Hogwarts under Umbridge: corridors, a broom cupboard, the edge of the Great Hall, the Room of Requirement, a corridor outside the Gryffindor common room.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** disorientation; the first long illusion; the other Harry; the cold presence.
- **Beats:**
  1. They hide. Harry's scar and face are a problem. So is Evelyn's: in this world, there is presumably a Selwyn girl too. Harry puts an illusion over both their faces: two forgettable Hufflepuff second-years. He has never held one for longer than a minute. He holds this one for an hour, then two, then a night. It is like holding a door shut against wind.
  2. **Except** it does not work on Evelyn. She sees him as he is and herself as she is. She has to trust him that it works on everyone else. (She hates this, and says so.)
  3. They learn the date from a copy of the *Daily Prophet*: April 1996. Two years ahead. Umbridge. Dumbledore gone. Voldemort back and the Ministry denying it.
  4. Harry sees the other Harry in a corridor. Fifteen, taller, Gryffindor scarf, with a red-haired boy and a bushy-haired girl either side of him. He is angry, all the time, loudly, and loved, loudly. Harry reads him and it is like reading his own handwriting upside down.
  5. Under the other Harry's anger, deep down, there is something cold and separate that is not him. It is aimed outward and also inward. It feels like the thing in the forest in first year. Harry is sick in a bathroom afterwards.
  6. **Evelyn scene:** she works out, from the watch and from her grandmother's instruction, that they have gone somewhere the watch goes. She decides they need to know whether there is a way back, and that the person most likely to know is whoever in this world owns the other watch.
  7. That night, in the Room of Requirement, Harry hides and watches the other Harry teach a room full of students to cast Patronuses. He watches for a long time.
- **Plants:** the cold presence in the other Harry.
- **Escalation:** two children in a world at war with no way home.
- **Ending:** a stag Patronus crossing the room, and Harry watching it.

## Chapter 27: Nobody

- **When/where:** the other world, early May 1996. The Slytherin common room (under illusion); the library; the Owlery; the Room of Requirement; a broom shed.
- **POV:** Evelyn, mostly, with one Harry scene.
- **Target:** about 6,500 words.
- **Purpose:** the other Evelyn, and the first time Harry senses the same cold in himself.
- **Beats:**
  1. Evelyn finds the other Evelyn: a sixth-year Slytherin who sits at the back of every class and whom nobody seems to see. Same face. Same watch on its chain. She has no friends. Teachers forget her name. She corrected a teacher's date once and nobody remembers it.
  2. Evelyn watches her for days. Her narration is very controlled, and the control slips in small ways: she counts how many times someone speaks to the other Evelyn in a day (twice, both times to ask her to move).
  3. She learns the other Evelyn's Isadora died in 1994 too, in a different month. Her other self winds the watch every morning.
  4. **Harry scene:** alone in the Room of Requirement at night, tired from holding illusions all day, he reaches inward for once instead of outward, and feels, very faintly, something cold in himself. He decides it is contamination: he has been reading the other Harry too much. He decides not to read him again. (Write this so it is entirely plausible on first reading.)
  5. Evelyn tells Harry about the other Evelyn. She says, flatly, "She's what I'd be." He does not argue, because he cannot read her and does not know if she wants him to.
  6. They need help. Harry has been reading adults for days: everyone in the castle is frightened or cruel or both. He has heard of a pub where nobody asks questions.
- **Plants:** Harry's faint cold. The other Evelyn's isolation.
- **Escalation:** they are running out of food and illusion.
- **Ending:** a door in Hogsmeade with a goat's head on the sign.

## Chapter 28: The Hog's Head

- **When/where:** the other world, May 1996. The Hog's Head; its upstairs room; a back lane in Hogsmeade at night.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** Aberforth; the other Sirius; the truth about Peter.
- **Beats:**
  1. Aberforth Dumbledore. Harry drops the illusion because he reads that this man will not betray them and would like to be shown he is right about something. Aberforth sees the scar on a boy who is too young and too short and too Slytherin, and is not surprised by much.
  2. Harry reads him: bitterness, aimed at his brother, old and deep; and a gruff, buried protectiveness toward children. Goats.
  3. Aberforth on his brother: *"My brother will use you, boy. He uses everyone he loves, and he loves you, so watch out."* Harry adds a page to his ledger.
  4. Aberforth sends word to someone. Two nights later, a huge black dog comes up the back stairs and turns into a man.
  5. Sirius Black. This world's Sirius, two years out of Azkaban, caged in a house he hates, meeting a thirteen-year-old godson from another world. Harry reads him: love so loud it is almost painful, recklessness, despair, delight.
  6. Harry tells him, carefully, that in his world Sirius Black is a murderer who betrayed his parents. Sirius laughs, horribly, and then tells him the truth. Peter. The rat. A missing toe. A boy called Ron Weasley's pet. The Shrieking Shack. James and Lily.
  7. Harry reads that every word is true. In his own world, he has spent three months planning to kill an innocent man.
  8. Sirius: *"Find the rat. Save my other self some trouble."* And something about James that makes Harry laugh, which he does not expect.
  9. Sirius asks about Harry's Harry: is he happy, is he all right. Harry says yes, because he has read that Sirius needs the answer to be yes. He does not know if it is true.
- **Plants:** the truth about Pettigrew, carried home.
- **Escalation:** the enemy was never the enemy.
- **Ending:** Sirius going back down the stairs as a dog, and Harry watching from the window.

## Chapter 29: The Other Watch

- **When/where:** the other world, late May to mid June 1996. The Hog's Head; the Slytherin common room; the corridor outside Umbridge's office; an empty classroom; the Great Hall at breakfast.
- **POV:** Harry and Evelyn, alternating.
- **Target:** about 7,000 words.
- **Purpose:** the way home, the maker's mark, and the other Evelyn's choice.
- **Beats:**
  1. Aberforth looks at Evelyn's stopped watch and goes very quiet. He recognises the work. He knows whose hand made it. He will not say. Harry reads that he has not been this shaken in fifty years. Evelyn asks him outright. He refuses, and tells her to ask whoever gave it to her, and she says her grandmother is dead, and he says he is sorry and still does not tell her.
  2. Aberforth does say what the work is: a Seer's piece. To leave a world it has taken you to, you would need its twin from that world, wound forwards by someone of the blood, somewhere time is held. He knows of one such place: a room in the Department of Mysteries.
  3. The Inquisitorial Squad nearly catches Harry. Umbridge herself. Harry puts an illusion on her and makes her see something deeply undignified (a cat in her office that is not there, or her own decrees rewritten). It is funny and it is a little cruel and Harry enjoys it.
  4. **Evelyn and the other Evelyn.** She approaches herself in an empty classroom and tells her the truth. It is the strangest conversation either of them has ever had, and it is written dry: two people who speak the same way, testing each other with precise questions only they could answer. The other Evelyn refuses. She has no reason to help two strangers and every reason to keep the only thing her grandmother gave her.
  5. Pansy Parkinson corners the other Evelyn, idly cruel. Our Evelyn, under Harry's illusion, steps in, and does something exact and humiliating to Pansy.
  6. The other Evelyn finds them that night. She has watched the two of them for a week. She asks Evelyn, very quietly, how long they have been friends. Evelyn says three years. The other Evelyn says: nobody has ever looked for me. Then she says she will come.
- **Plants:** Aberforth's knowledge of the maker.
- **Escalation:** the only way home is through the Ministry, on the worst night of that world's year.
- **Ending:** the other Evelyn's line.

## Chapter 30: The Hall of Prophecy

- **When/where:** the other world, the night of the Department of Mysteries battle, June 1996. The Hog's Head fireplace; the Ministry Atrium; the Department of Mysteries: the Hall of Prophecy, the Time Room, the doorway of the Death Chamber.
- **POV:** Harry.
- **Target:** about 8,500 words (climax of the other world).
- **Purpose:** the prophecy heard; the other Sirius's death; the other Evelyn left behind; home.
- **Beats:**
  1. The night the other Harry and his friends leave for London, Aberforth sends Harry, Evelyn and the other Evelyn by Floo to the Ministry behind them. He says he will tell nobody. He says he is too old for this, and goes to send word to his brother anyway.
  2. The Department of Mysteries. The battle is already happening. Spells, shouting, the other Harry and his friends running through a hall of shelves and glass. Death Eaters. Harry reads a dozen terrified children and a dozen people enjoying themselves.
  3. In the Hall of Prophecy, shelves fall. An orb smashes at Harry's feet. In the noise, nobody else hears it. He does. A woman's voice, misty, saying a prophecy about a boy born as the seventh month dies, and a Dark Lord, and *neither can live while the other survives*. Retell it in new words, close to the meaning, not quoted. Harry understands it is about him too, because it was made before their worlds split.
  4. The Time Room. Bell jars of light, ticking. Death Eaters coming. Harry holds an illusion over the door: an empty room. The other Evelyn takes out her watch. Our Evelyn takes out hers. The other Evelyn winds hers forwards.
  5. It does not take immediately. There are seconds. Harry, at the door, sees down a corridor into the Death Chamber. The arch. The veil moving. The other Sirius, laughing, duelling his cousin. A red light. Sirius falling backwards through the veil. The other Harry screaming. Harry cannot do anything. He watches.
  6. The watch takes. The other Evelyn's watch crumbles into gold dust in her hand. She looks at it. Then at Evelyn. There are footsteps outside the illusion. She says one short thing (write something dry and devastating, in Evelyn's voice). The world turns.
  7. Do not show what happens to her. The last image of the other world is her face and the footsteps.
- **Payoffs:** the watch's rules.
- **Plants:** the prophecy, carried home. Bellatrix's curse at the Veil.
- **Escalation:** the loudest chapter of the year so far.
- **Ending:** the turn, and darkness, and the cold floor of the Chamber.

## Chapter 31: Four Days

- **When/where:** home, March 1994, four days after they vanished. The Chamber; Myrtle's bathroom; the corridor outside; the hospital wing; Dumbledore's office; the study.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** the manhunt, the lie that works, and the weight they carry.
- **Beats:**
  1. They come up through the pipes into a castle in uproar. They have been gone four days. The school believes Sirius Black took them. There are Aurors in the corridors. Theo has not slept. Millicent hits Harry on the arm hard enough to bruise, which is how she says she was frightened.
  2. A cover story, agreed in the pipes in four sentences: they were exploring a sealed passage under the dungeons, a wall came down, they were trapped, they rationed chocolate. Evelyn adds a detail that makes it true (a specific, verifiable passage she has read about). They tell it to McGonagall, to Snape, to an Auror. It holds.
  3. Dumbledore, alone with Harry. Kind, worried, genuinely relieved. He looks into Harry's eyes, and Harry feels him reaching, gently, for his mind, to check.
  4. Harry, Chamber-trained, does not block. Blocking would tell him something. Instead he gives him a memory: dark, a fallen wall, Evelyn rationing chocolate in squares. It is an illusion built inside a memory, and Dumbledore accepts it. The first time anyone has fooled Dumbledore's mind. Harry reads relief, and then, for a moment, a puzzled sense of something closed. Ledger.
  5. Evelyn's watch has stopped. It will not wind. She tries every morning. **Evelyn scene:** she turns fifteen three days later (9 March) in her own world, with the watch stopped, and thinks about the other Evelyn, who does not have a watch any more, or perhaps any more birthdays.
  6. In the study, Harry tells her the prophecy. All of it. She is the only person he tells.
  7. Harry, alone, reaches inward. The faint cold is still there. Still contamination, he tells himself.
- **Plants:** the faint cold, dismissed again.
- **Escalation:** Harry knows things about the future of the war that the headmaster does not know he knows.
- **Ending:** on Harry looking at the Marauder's Map, for a name.

## Chapter 32: Scabbers

- **When/where:** March to early June 1994. The Gryffindor side of the Great Hall; the edge of the Forbidden Forest; Hagrid's hut; the Whomping Willow; the Shrieking Shack.
- **POV:** Harry.
- **Target:** about 7,500 words.
- **Purpose:** hunting Pettigrew, meeting this world's Sirius, the Shack.
- **Beats:**
  1. Harry approaches Ron Weasley about his rat. Badly. A Slytherin, the ex-Heir, asking a Gryffindor about his pet. Ron is suspicious and rude. Harry reads loyalty, insecurity, and a decent heart, and remembers the other Harry's friends, and does not know what to do with that.
  2. Scabbers has vanished (the cat, or he ran). On the Map: a name that should not be there, *Peter Pettigrew*, moving through the castle at night. Harry watches it for a week.
  3. Harry goes looking for the black dog at the edge of the forest. Finds it. Says, "I know it was Peter." The dog turns into a man who has not been spoken to kindly in twelve years. This world's Sirius: thinner, wilder, louder with rage than the other one, and just as loud with love. Harry tells him almost nothing about how he knows.
  4. Buckbeak's appeal is lost. Execution set for a June evening. Hagrid's grief. Harry and Evelyn agree, privately, to do something about it.
  5. The night. Harry, Evelyn, and Ron (who wants his rat back and has decided to trust a Slytherin for exactly one evening). Through the Willow to the Shack. Lupin. Snape. Harry disarms Snape without hesitation and reads Snape's hatred go white.
  6. Pettigrew forced into his true shape. Sirius and Lupin about to kill him. Harry, cunning, stops them: alive, he is proof. (Not mercy. Strategy. Let Sirius look at him strangely.)
  7. The full moon. Lupin transforms. In the chaos, Pettigrew changes and runs. Nobody can stop it. (External. Do not give Harry a last-second save.)
- **Escalation:** Harry has his godfather for an hour and loses the proof.
- **Ending:** Lupin's howl, and Sirius running toward the lake after him, and the cold coming.

## Chapter 33: The Patronus by the Lake

- **When/where:** the same night and the end of term. The lake shore; Hagrid's paddock earlier that evening; the hospital wing; Dumbledore's office; Lupin's office; the train.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** the Patronus, Buckbeak, Sirius flies, and Privet Drive again.
- **Beats:**
  1. Open slightly earlier, in Evelyn's view: Buckbeak's execution. She and Harry at the edge of the pumpkin patch. Harry holds an illusion on Macnair, Fudge and the committee member: Buckbeak still tethered and sullen, while Evelyn, who cannot be fooled and is therefore the only one who can see what she is doing, walks the real hippogriff into the trees. Write it as precise, frightening, and slightly funny.
  2. Back to the lake, after the Shack. A hundred Dementors coming across the water toward Sirius. Harry reads them: appetite, multiplied.
  3. His Patronus. He does what he did to Quirrell, but outward and clean: he takes everything he read in the other Sirius, all that love, and pushes it into the spell. The stag is enormous. It drives every one of them back across the lake.
  4. He collapses. He wakes in the hospital wing.
  5. Snape is telling Fudge that Black is caught and in a tower. Harry, Evelyn, and Buckbeak (in the trees) get him out. Sirius flies away on Buckbeak. Before he goes he says something to Harry that is about James and also about Harry.
  6. Dumbledore. Harry tells him Sirius is innocent. Dumbledore believes him. Without Pettigrew there is no proof. Harry asks if, when Sirius is cleared, he could live with him. Dumbledore says he must go back to his aunt's for the summer. He gives a reason about protection that Harry cannot use. Harry nearly says *because of the prophecy?* and does not. Ledger.
  7. Lupin resigns: Snape has told the school what he is. Harry reads Snape's satisfaction and is, for the first time, frightened of Snape.
  8. The train. Evelyn holding the stopped watch in her palm. She says she is going to find out who made it. He asks who on earth makes watches like that. She says she intends to find out.
- **Payoffs:** the other Sirius's love becomes the Patronus.
- **Escalation:** Harry has saved his godfather's life and is sent back to a cupboard-sized room.
- **Ending:** Evelyn's line about finding out, and the watch not ticking.


========================================================================
# FILE: SPOILERS_08_CHAPTERS_Y4.md
========================================================================

# SPOILERS · 08 · CHAPTER PLANS: YEAR FOUR

This is the year of secrets on both sides. Evelyn knows who her grandfather is from Chapter 34 and does not tell Harry until Chapter 40. Keep her viewpoint scenes honest to that: the reader knows, Harry does not.

The friendship blow-up in Chapter 40 is **not romantic**. It is a fight between the two people who matter most to each other, about trust. No confession of love, no kiss, no crush. It should be furious, funny, and end in something better than romance: a secret handed over.

---

## Chapter 34: The Letter in the Will

- **When/where:** July to August 1994. Selwyn Hall (the will is read in the long drawing room under the disapproving portrait); the yew walk; a Ludlow tea room; then the Quidditch World Cup on a moor, in Corvin Selwyn's box, and the campsite at night.
- **POV:** Evelyn first, then Harry.
- **Target:** about 7,500 words.
- **Purpose:** Evelyn learns about Grindelwald; the World Cup; the riot; Thaddeus.
- **Beats:**
  1. **Evelyn.** The reading of Isadora's will. Small bequests, read in a solicitor's dry voice. Then a sealed letter for Evelyn alone. She reads it on the yew walk. Its first line is plain: her grandfather is alive, and his name is Gellert. The rest is in Isadora's handwriting and Isadora's voice: brief, unsentimental, unapologetic. It explains the lessons. It says he will write. It says she may answer or not, as she likes.
  2. She goes to her mother. Marguerite is in the small sitting room with a glass at eleven in the morning. Evelyn holds up the letter. Marguerite looks at it and starts to cry, and says yes, and says she is sorry, and says Corvin must never know. Evelyn notes the time.
  3. She tells nobody. She writes to Potter about the weather and a book.
  4. **Harry.** Corvin Selwyn has invited the Boy Who Lived to the World Cup final, in his box. (Politics. Harry reads it at once: Corvin wants to be seen with him.) Isadora's death means Evelyn is in black. Harry notices she is different, more closed even than in March. He asks. She says she is fine.
  5. The match, briefly and vividly: Ireland, Bulgaria, Krum. Harry reads a hundred thousand people at once and has to turn it down hard.
  6. The campsite at night. Masked men marching, Muggles floating. Harry reads the marchers: glee. Evelyn, beside him in the trees, goes absolutely still. One of the masked voices is her uncle Thaddeus. She does not say so. Harry sees her face, which tells him nothing, and her hand, which has closed around the stopped watch.
  7. The Dark Mark. Panic. Winky. Barty Crouch. Harry reads Crouch: terror, and shame, and something hidden very hard.
- **Plants:** Thaddeus's voice. Crouch's hidden thing.
- **Escalation:** Evelyn's whole life has been a lie told for her protection, and Death Eaters are marching again.
- **Ending:** Evelyn, or Harry looking at Evelyn's closed hand.

## Chapter 35: Durmstrang

- **When/where:** September to Halloween 1994. The Great Hall; Moody's classroom; the lake when the ship rises; the Durmstrang delegation at the Slytherin table; the room off the Great Hall where the champions gather.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** the Tournament, the imposter Moody, Varga, the Goblet.
- **Beats:**
  1. The Tournament announced. Slytherin's excitement.
  2. Mad-Eye Moody. Harry reads him and gets something fierce and devoted, aimed squarely at him. He takes it for an old Auror's protectiveness. (Write it so that this is the obvious reading.)
  3. The Unforgivables lesson. The spider under the Cruciatus. Harry reads the spider's agony and it is the worst thing he has felt from a living creature. He reads Neville, white. He reads Moody, under the lesson, enjoying it, and tells himself that is just Moody.
  4. Beauxbatons arrive by carriage. Durmstrang by ship out of the lake. With Karkaroff comes an old man with a stick: **Elias Varga**, Master of Wards. At the feast, Durmstrang sits with Slytherin. Varga watches Evelyn. Harry reads him: recognition, and shame, very old. Evelyn does not notice. Harry does.
  5. The Goblet. Halloween. Four names. Harry's is the fourth. The Hall goes loud: disbelief, rage, envy, and from Slytherin, triumph.
  6. The room off the Hall. Dumbledore asks if he put his name in. No. Harry reads that Dumbledore believes him, and is alarmed, and then resigned. "Nothing can be done." The contract is binding. Harry says, quietly, "You could stop this." Dumbledore says he cannot. Ledger.
  7. Cedric, decent, uncertain. Harry reads that Cedric does not believe he cheated, and is grateful, and hides it.
- **Plants:** Moody's devotion. Varga's shame.
- **Escalation:** Harry is in a contest that kills people and the headmaster says nothing can be done.
- **Ending:** the Slytherin common room that night, loud with a kind of joy that frightens him.

## Chapter 36: Rita

- **When/where:** November 1994. The weighing of the wands in a small classroom; the Owlery; the Durmstrang ship's gangway; a windowsill in an empty classroom where a beetle sits; Hagrid's paddock at night.
- **POV:** Harry and Evelyn, alternating.
- **Target:** about 6,500 words.
- **Purpose:** Rita Skeeter, the first letter from Nurmengard, Evelyn's beetle, the dragons.
- **Beats:**
  1. The weighing of the wands. Rita Skeeter and her quill. Harry reads her: appetite, gleeful and bottomless. The article that follows is vile.
  2. The school turns on him again. Second ostracism. He is better at it this time.
  3. **Evelyn.** At the Owlery, Varga, with great courtesy, gives her a letter, says he was asked to, and leaves before she can answer. It is from Nurmengard. Write Grindelwald's first letter in full: about a page, witty, charming, unhurried, frightening in its assumptions. He asks about the weather in Scotland, her reading, her grandmother's last months. He asks whether she still winds the watch, and whether it still works. He invites her to visit at Christmas. He says Varga can arrange it.
  4. **Evelyn**, reading everything as usual, notices a beetle on a windowsill in every place Rita Skeeter has somehow overheard. She looks up the Animagus register. Rita is not on it. Evelyn catches the beetle in a jar.
  5. The blackmail. Written dry and precise and slightly terrifying: Evelyn with the jar, Rita restored and furious, Evelyn explaining the penalties for unregistered Animagi to the year and the section. Rita will write nothing about Harry Potter for the rest of the year unless Evelyn approves it. Evelyn does not tell Harry she has done this.
  6. **Harry.** Hagrid takes him to see the dragons at night. Four of them. Harry reads them: fury, maternal, enormous. He tells Cedric. Fair is fair. He reads Cedric's gratitude and surprise.
- **Plants:** Grindelwald's question about the watch.
- **Escalation:** dragons, and a secret growing on Evelyn's side.
- **Ending:** Evelyn, alone, writing one line of a reply, and then another.

## Chapter 37: The Horntail

- **When/where:** 24 November 1994. The champions' tent; the enclosure; the stands; the hospital tent.
- **POV:** Harry, with a short Evelyn scene in the stands.
- **Target:** about 6,500 words.
- **Purpose:** the first task, and the first public illusion.
- **Beats:**
  1. The tent. Bagman. The bag of tiny dragons. The Hungarian Horntail.
  2. Harry's plan is his own, built from Lockhart's stagecraft and Slytherin's study: Summon his broom, and give the dragon two Harrys. He has never held an illusion on something that large and that angry.
  3. The enclosure. The roar of the crowd, the roar of the dragon. Harry reads the Horntail: rage, aimed at him, and fear for the eggs, under it.
  4. The illusion works for eleven seconds, which is long enough to get into the air and too short to be safe. The tail catches his shoulder. He gets the egg.
  5. **Evelyn in the stands:** she is beside Varga, who has come to watch, and who goes rigid when the second Harry appears. He says something in Hungarian under his breath. When she asks, he says, in English, that it was a First Step, and that he has not seen one in forty years. Then he says nothing else. She leaves the stands early, before the marks, because she has agreed to meet Varga about Christmas.
  6. The hospital tent. Harry notices Evelyn is not there. He reads the champions: Krum's respect, Fleur's surprise, Cedric's relief.
  7. The Slytherin common room is loud and adoring and Harry does not enjoy it.
- **Plants:** the First Step named.
- **Escalation:** the whole school has seen him do something nobody can explain.
- **Ending:** on her empty seat, which he noticed, and she knows he noticed.

## Chapter 38: Nurmengard

- **When/where:** Christmas 1994. Evelyn: a Portkey from a lay-by on the A49 outside Ludlow; the snow in the Austrian mountains; the tower; the cell at the top. Harry: the Yule Ball at Hogwarts; the Slytherin table; a corridor; the Owlery.
- **POV:** Evelyn and Harry, alternating. The Nurmengard scenes are the heart of the chapter.
- **Target:** about 8,500 words.
- **Purpose:** Grindelwald; the bargain; the watch reset; the line about history; Harry learns she lied.
- **Beats:**
  1. **Evelyn.** She tells Potter she is going home for Christmas. She tells her mother she is staying at school. Both are lies. She notes, precisely, that she has never lied to him before.
  2. Varga's Portkey, which only works for her blood. Snow. A black tower. The words over the gate, which she can read.
  3. The cell at the top: a narrow window, one chair, a thin old man in grey who stands when she comes in, as though she were someone important. Gellert Grindelwald.
  4. Write their first conversation at length. He is elegant, amused, theatrical, honest about the wrong things. She is flat and precise and refuses to be impressed, which delights him. He offers to teach her, in exchange for news of the outside world. She says that is not a fair exchange. He agrees and says he does not care.
  5. He tells her, with some impatience, about his reputation. Use something close to: *"History has decided I loved one person and that he was a man. History is half right, which is the most irritating way to be wrong. I loved your grandmother for eleven years and him for one summer, and history, being a romantic, prefers the summer."*
  6. He asks to see the watch. He made it, in 1938, for Isadora, so that she would never be in only one world. He holds it, and the second hand quivers, and he resets it with a touch. It ticks. She does not let herself show anything.
  7. He tells her that Isadora once wound it backwards, in 1944, and saw a world where he had won, and came back, and left him. "It was the only argument I ever lost."
  8. He looks at her for a long time and tells her she walks a Path. Not his. Stillness. "How disappointing. How interesting."
  9. He asks about the boy. All the time. She tells him nothing he could not read in a newspaper. He says: *"I saw you beside him. I did not see how it ended."* She asks what that means. He says it means exactly what it says.
  10. **Harry.** The Yule Ball. Champions must have partners. Harry goes with Millicent, as friends, because she asked him in four words and dared him to laugh. It is genuinely funny. They dance badly. Draco's fury at something. Krum and a bushy-haired Gryffindor. Cedric and Cho.
  11. Late, Harry finds Lucan Selwyn, who has come up as a guest of someone. Lucan, pleasantly, mentions that Evelyn is not at home for Christmas. Mother thinks she is at school. Harry reads that Lucan is telling the truth and enjoying it.
  12. Harry, alone in the Owlery at two in the morning. The ledger again, but this time it is a page for her.
- **Payoffs:** the watch's maker. Isadora's stillness at Harry's name (Grindelwald foresaw him).
- **Plants:** Evelyn's Path. "I did not see how it ended."
- **Escalation:** the two people who trust each other most are lying to each other.
- **Ending:** cut between them: the watch ticking in her palm in Austria, and Harry deciding not to ask.

## Chapter 39: What You'd Miss Most

- **When/where:** January to 24 February 1995. The prefects' bathroom; the library; the Great Lake; the stands; the lake shore; a cave above Hogsmeade.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** Harry manages Evelyn; the second task; the hostage; Sirius in the cave.
- **Beats:**
  1. Evelyn comes back from "home". Harry is perfectly pleasant. He asks nothing. He is charming, warm, attentive, distant: the way he is with everyone else. He has never once done this to her. She notices on the first day.
  2. The egg. Cedric's hint. The prefects' bathroom. The song under water. Write a new short verse or summarise.
  3. The night before the second task, Evelyn is called to McGonagall's office and does not come back.
  4. Gillyweed (Dobby, or Neville, or Harry's own research in Slytherin's books). The lake. The merpeople. Harry reads them: territorial, curious, cold. The hostages. His is Evelyn. She is asleep, tied to a stone, silent as always.
  5. He frees her. He stays for the small Beauxbatons girl too, because he can read nothing from the sleepers and cannot bear not knowing. He uses an illusion on the merpeople to get both of them up.
  6. On the bank, Evelyn, wrapped in a blanket and dripping, looks at him and says something like: *"I'm what you'd miss most, and you won't even ask me where I went at Christmas."* He says, *"Would you have told me?"* She does not answer. Then she walks away up the bank.
  7. Sirius, as a dog, in a cave above Hogsmeade, starving and glad. Harry visits with food. They talk properly for the first time since the Shack. Sirius tells him to be careful of Moody's Death Eater hunting, of Karkaroff, of Crouch. He asks about the Selwyn girl. Harry says she is fine. Sirius reads people too, in an ordinary way, and says: "No she isn't."
- **Escalation:** the friendship is at its worst point.
- **Ending:** Sirius's line, or Harry walking back down the hill.

## Chapter 40: The Crash-Out

- **When/where:** March to May 1995. The unused fourth-floor classroom; the Durmstrang ship at night; the edge of the Forbidden Forest.
- **POV:** Harry, then a short Evelyn scene, then Harry.
- **Target:** about 8,000 words.
- **Purpose:** the blow-up, the trust exchange, Varga and the Paths, Crouch in the forest.
- **Beats:**
  1. Evelyn ambushes him. She sends a note in his own handwriting (she has studied it) asking him to the fourth-floor classroom. When he comes in, she locks the door with a charm of her family's that he cannot break.
  2. **The crash-out.** Write it as the funniest and most painful scene of the year. She has a list. She has counted. *"Seventeen times since the eighth of January you have asked me how I am and not waited for the answer. Nine times you have made me laugh on purpose so that I would stop looking at you. Four times you have agreed with me when you did not agree with me. You do this to everyone. You have never done it to me. Stop managing me, Potter."*
  3. He tries to manage her out of it. She names that too. He gets angry. She is angrier. She almost shouts, which she never does, and that frightens him more than anything she has said.
  4. Then he says it, plainly. That she is the only person he cannot read. The only one. That he has never known what she feels, not once in four years, and he has trusted her anyway, more than anyone, and he does not know how to do that, and when she lied to him he did not know what to do, so he did what he always does.
  5. A silence. She sits down on a desk.
  6. She tells him. *"My grandfather is Gellert Grindelwald."*
  7. He laughs, because it is absurd. Then he looks at her face, which tells him nothing, and her hands, which are holding the watch, and stops laughing.
  8. She tells him everything. Isadora. The letter. Nurmengard. The bargain. The watch. *"I saw you beside him."* She hands the secret to him the way she would hand over a document, and he takes it the same way.
  9. **Evelyn, briefly:** she notices that she feels lighter, and finds this irritating.
  10. **The fun part.** That night they break onto the Durmstrang ship together, because Harry wants to know what a First Step is and Varga will not tell Evelyn. Harry gets them past the Durmstrang sentries with illusions, Evelyn picks two locks and corrects his Bulgarian. They corner Varga in his cabin. Varga, horrified and then resigned, tells them about the Paths and the Walkers and the Concordat, briefly, in a scene, not a lecture: interrupted, tetchy, with tea. He tells them Harry's is the Path of Illusion, and that the last person to walk it to the top went mad. He tells them Dumbledore walks one too.
  11. Weeks later. Harry and Krum at the edge of the forest. Barty Crouch Sr. stumbles out of the trees, raving. Harry reads him: terror, and something fighting inside his head. Harry runs for Dumbledore. When they come back, Crouch is gone and Krum is Stunned.
- **Payoffs:** Evelyn counts things. Lockhart's Walker.
- **Escalation:** the friendship is repaired and stronger, and a man has vanished from the edge of the grounds.
- **Ending:** the empty place in the trees where Crouch was.

## Chapter 41: Pensieve

- **When/where:** May to June 1995. Dumbledore's office; inside the Pensieve (a Wizengamot courtroom in the early 1980s); Divination's tower room where Harry falls asleep; Nurmengard at Easter (Evelyn).
- **POV:** Harry, then Evelyn, then Harry.
- **Target:** about 6,500 words.
- **Purpose:** the Pensieve, the Concordat word, a dream, Grindelwald's oblique warning.
- **Beats:**
  1. Harry waits in Dumbledore's office. The Pensieve. He falls in.
  2. Trials: Karkaroff, Bagman, Crouch's son and the Lestranges. Neville's parents. Harry reads emotions *inside the memory*: the young Crouch's terror and his devotion, the elder Crouch's iron shame. (This is new. He has never read a memory before.)
  3. Dumbledore pulls him out. Harry asks one question, carefully, to test him: "Who is the Concordat?" Dumbledore goes very still. Harry reads shock, then a door closing. Dumbledore says it is an old agreement between old people. Ledger.
  4. **Evelyn**, at Easter, at Nurmengard again. Grindelwald asks to meet the boy. She refuses. He says that is wise. He tells her, as she leaves, one thing that sounds like idle chat: *"If you are ever asked to watch a maze, watch the edge of it, not the middle."*
  5. **Harry** dozes in Divination and dreams: a dark house, an old man, a snake, a chair, a voice. He follows the dream on purpose instead of waking, because he is a legilimens now and curious. He sees more than he should, a plan involving the end of the Tournament, and wakes before he understands it. His scar is burning. He tells Dumbledore some of it. Not all.
- **Plants:** reading emotions in memories. Grindelwald's maze line.
- **Escalation:** Harry has seen the plan and not understood it.
- **Ending:** on the third task being a week away.

## Chapter 42: The Third Task

- **When/where:** 24 June 1995. The stands; the maze.
- **POV:** Harry, with a short Evelyn scene at the maze's edge.
- **Target:** about 6,500 words.
- **Purpose:** the maze, and the Cup.
- **Beats:**
  1. The maze at dusk. Hedges. Harry reads nothing in them, then something: a Boggart, a Skrewt, a sphinx.
  2. The sphinx's riddle. Write a new one.
  3. Krum, Imperiused, attacking Cedric. Harry reads that Krum is not in there. He and Cedric deal with it together.
  4. **Evelyn**, outside, remembers her grandfather's line and leaves the stands to stand at the edge of the maze, where nobody watches. She notices "Moody" standing very still at the hedge with his wand out, doing something to the maze. She cannot see what. She does not know yet what she has seen.
  5. Harry and Cedric reach the Cup together. They argue about who should take it. They take it together.
  6. It is a Portkey.
- **Plants:** Evelyn's sighting of Moody at the hedge (she will tell Dumbledore in Chapter 44 and it will matter in the unmasking).
- **Escalation:** they are pulled away.
- **Ending:** the hook behind the navel, and dark.

## Chapter 43: Bone, Flesh, Blood

- **When/where:** the same night. Little Hangleton churchyard; the Riddle grave.
- **POV:** Harry.
- **Target:** about 8,500 words (climax).
- **Purpose:** Cedric's death, the return, the duel, the illusion, the escape.
- **Beats:**
  1. A graveyard. A figure. *Kill the spare.* Cedric dies. Write it plainly and fast. Harry reads him going, and then nothing.
  2. Harry is bound to a headstone. Wormtail. The cauldron. Bone of the father, flesh of the servant, blood of the enemy. Retell in new words.
  3. Voldemort rises. Harry reads him: the cold he felt in the forest and on the back of Quirrell's head, but whole now, and loud, and full of a pleasure that has nothing in it Harry recognises as human.
  4. The Death Eaters come. Harry reads them one by one: fear, greed, and devotion. Lucius. Nott: Theo's father, and Harry knows his son. Crabbe, Goyle, Macnair. **Thaddeus Selwyn**. Harry knows the voice from the World Cup.
  5. Voldemort speaks of the boy, and of his mother's protection, and of using his blood.
  6. The duel. *Priori Incantatem*: the brother wands. Luck, not skill. Shades. His parents. Cedric. Retell in new words.
  7. When the connection breaks, Harry fills the graveyard with Harrys. Twenty of them, running in every direction. For three seconds the Death Eaters fire at all of them.
  8. Voldemort does not. He looks at the illusions with interest. *"That is not a spell. That is a Path."* He sounds delighted.
  9. Harry reaches Cedric's body and the Cup.
- **Payoffs:** the cold in the forest. Thaddeus.
- **Plants:** Voldemort now knows Harry walks a Path.
- **Escalation:** the most dangerous thing that has ever happened to him.
- **Ending:** the Cup taking him, with Cedric's hand in his.

## Chapter 44: Equal Footing

- **When/where:** the same night. The edge of the maze; Moody's office; Dumbledore's office.
- **POV:** Harry, with one section from Dumbledore (see the master outline, section 8.1).
- **Target:** about 8,500 words.
- **Purpose:** the unmasking, and the blow-up.
- **Beats:**
  1. The lawn. Cedric's body. Amos Diggory. The noise of the crowd. Harry reads grief arriving in a thousand people at once, and turns it off, and cannot.
  2. Moody takes him to his office. Harry reads that same fierce devotion, aimed at him, and now understands it: it is not for him. It is for his master, and Harry is the gift. Write the reveal through the reading.
  3. Evelyn has gone straight to Dumbledore and told him what she saw Moody doing at the hedge. That is why Dumbledore, McGonagall and Snape come through the door when they do. (External resolution. Harry is rescued, not victorious.)
  4. Veritaserum. Barty Crouch Jr. The real Moody in a trunk.
  5. Dumbledore's office. Sirius as a dog by the fire. Fawkes. Dumbledore asks him to tell what happened. Harry says no.
  6. Then the blow-up, as in the master outline. Quiet, getting quieter. The ledger, in order. Quirrell: *"He didn't die because he couldn't touch me. He died because I made him hate himself."* The Stone as bait. The heir year. Sirius in a cave. "Nothing can be done." A Death Eater teaching under his nose. Cedric. Then: *"You knew about the prophecy."*
  7. Dumbledore asks how he knows. Harry tells him: a room full of glass, in a world where he was in Gryffindor. He tells him about Slytherin's study too, because it no longer matters what Dumbledore knows.
  8. Dumbledore reaches for his mind to check. Harry pushes the graveyard into him instead. All of it.
  9. **Dumbledore's section.** He lets it in. He feels a fourteen-year-old's night. He understands he has spent four years managing a boy who was managing him. Tom at eleven. Gellert at sixteen. He is ashamed of the comparison and keeps it. He sees a First Step in what was just done to him.
  10. **Back to Harry.** Dumbledore says Harry is walking a Path, and that so is he. He offers to teach him, not protect him. Harry reads respect, grief, and fear. He notes the fear.
  11. Sirius changes back and says something rough and loving that cuts through all of it.
- **Payoffs:** the whole ledger. Moody's devotion. Evelyn at the maze's edge.
- **Plants:** Dumbledore's fear.
- **Escalation:** nothing will be as it was between Harry and the most powerful wizard in Britain.
- **Ending:** a short line. Perhaps Harry realising that Dumbledore has, for the first time, waited for him to speak.
- **Don't:** let anyone apologise more than once. Don't resolve the anger. Don't let the narrator say they are equals now.

## Chapter 45: Fudge

- **When/where:** the last days of June 1995. The hospital wing; the Slytherin common room; the lake shore; the train; Privet Drive.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** denial, the break with Fudge, Slytherin splitting, and the scar.
- **Beats:**
  1. Fudge brings a Dementor to Crouch Jr., who is kissed before he can testify. Fudge refuses to believe. Harry reads him: terror so large it has become stubbornness.
  2. Dumbledore breaks with Fudge in front of Harry. Snape shows his Mark and goes back to Voldemort. Harry reads Snape's dread, which is real.
  3. The Slytherin common room. The children of the men Harry saw in the graveyard. Theo comes to him at night. His father was there. Theo knows Harry knows. Neither of them knows what to say. Draco, cold and frightened and pleased.
  4. **Evelyn** at the lake with Harry. She tells him Grindelwald wants to meet him. He says, not yet. She says that was what she told him. She tells him about the beetle, and Rita, and the jar. He laughs for the first time in a week.
  5. The winnings. Harry gives the thousand Galleons to the Weasley twins, for a joke shop, because they gave him the Map when the school hated him. Small, funny, kind.
  6. The train. Privet Drive.
  7. At the edge of sleep in his small room, Harry feels, through the scar, a feeling that is not his: glee. It is Voldemort's. It is the first time.
- **Plants:** the scar link.
- **Escalation:** the war has started and only half the country knows.
- **Ending:** the glee, in the dark.


========================================================================
# FILE: SPOILERS_09_CHAPTERS_Y5_Y6.md
========================================================================

# SPOILERS · 09 · CHAPTER PLANS: YEAR FIVE AND YEAR SIX

Harry has lived through Year Five once already, from the outside, in another world. He knows roughly how it goes there. Use this: he anticipates, plans, and plays people, and the year still goes wrong in ways the other world did not, because this world has a different Harry in it.

---

# YEAR FIVE

## Chapter 46: Little Whinging

- **When/where:** July to early August 1995. Privet Drive; the play park; the alley between Magnolia Crescent and Wisteria Walk; the Dursleys' kitchen; a broom flight over London at night.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the Dementors, Dudley, Petunia's crack, rescue.
- **Beats:**
  1. A summer of no news. Harry reads the news on the television for things the Prophet will not print. Evelyn's letters are careful, because owls can be read. She writes about the weather and a book, and he reads between the lines.
  2. Dudley and his gang. Harry reads Dudley: bored, cruel, and under it, increasingly, something like fear of himself.
  3. The alley. The cold. Two Dementors. Harry reads appetite. Dudley goes down. Harry's Patronus.
  4. Dudley, afterwards, sick and shaking. Harry reads terror, and under it, gratitude that Dudley has no idea what to do with.
  5. The kitchen. Vernon's rage. Petunia says the word *Dementors*, and Harry reads, for the first time clearly, what has been under her disgust his whole life: grief, for her sister, aimed at him because he has her eyes. He does not say anything about it. Neither does she. An owl arrives: expelled. Then another: not expelled yet.
  6. The Order arrives: Moody (the real one; Harry reads him and finds paranoia and, under it, a decency he did not expect), Lupin, Kingsley, and a young witch with bubblegum-pink hair who trips over the kitchen bin. Tonks.
  7. A broom flight over London at night. Tonks flies beside him and talks the whole way.
- **Plants:** Dudley's gratitude. Tonks.
- **Escalation:** the Ministry is coming for him.
- **Ending:** a door that appears between number eleven and number thirteen.

## Chapter 47: Grimmauld Place

- **When/where:** August 1995. 12 Grimmauld Place: the kitchen, the drawing room, the portrait in the hall; the Ministry: the Atrium, a lift, Courtroom Ten.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** Sirius caged; Tonks teaching; Ron and Hermione approached; Kreacher; the hearing.
- **Beats:**
  1. Sirius, in a house he hates, overjoyed to see Harry and furious at being kept indoors. Harry reads both at full volume.
  2. The Weasleys are here, and Ron and Hermione. They are polite and curious and wary of a Slytherin they barely know. Harry remembers them at another Harry's side. He tries to talk to them. It goes badly, then less badly. One small genuine moment with each of them.
  3. Tonks teaches Harry about disguise. She can change her face; he can make people see a different one. She says the face is the least of it: it is posture, it is how you walk into a room, it is what you expect them to see. They trade tricks. She is very funny. He likes her a great deal.
  4. Kreacher. Harry reads hatred, grief, and devotion, aimed elsewhere: "Miss Narcissa". He mentions it to Sirius, who laughs it off.
  5. The hearing in Courtroom Ten. Fudge, Umbridge (Harry reads her for the first time in this world and finds exactly what he found in the other: a sincere and sweet enjoyment of other people's pain). Dumbledore arrives as a witness and then, deliberately, sits back and lets Harry speak. Harry wins it himself, by reading the Wizengamot and giving each wavering member exactly the argument they want. Dumbledore watches him do it.
- **Plants:** Kreacher's devotion to Narcissa. Tonks's lesson about posture.
- **Escalation:** Umbridge is coming to Hogwarts.
- **Ending:** Dumbledore leaving the courtroom without looking at Harry, which in this year means respect, and Harry reading that it does.

## Chapter 48: Educational Decrees

- **When/where:** September to October 1995. The Great Hall; Umbridge's pink office with the kitten plates; the Hog's Head; the Room of Requirement; the Slytherin common room.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** Harry's double game; the defence group; occlumency proposed.
- **Beats:**
  1. Umbridge. Harry, having seen her once already, does the opposite of what the other Harry did. He agrees with her. He is a polite, famous Slytherin who says the right things. She adores him. Draco, whom she should have adored, is furious.
  2. He watches her give Neville a detention with her quill. He reads Neville's pain afterwards. He adds a page to a new ledger, hers.
  3. Hermione Granger, at a library table, says out loud that somebody should teach them actual defence. Harry takes the idea. He builds it.
  4. The Hog's Head, for the first meeting. This world's Aberforth is behind the bar. He does not know Harry. Harry knows him: his goats, his brother, his kindness to children. Harry orders a butterbeer and very nearly calls him by his name. A small, strange, sad beat.
  5. The group: Neville, Luna, Millicent, Theo, Ron, Hermione, Ginny, Evelyn, some Hufflepuffs and Ravenclaws. Justin Finch-Fletchley refuses to join anything Harry runs, loudly. They meet in the Room of Requirement. Harry teaches. He is good at it. He reads every student's fear and teaches to it.
  6. **Evelyn**, now in her sixth year, watches him teach and notes that he is happier than she has ever seen him, and that he does not know it.
  7. Dumbledore, by letter, *asks* (not tells) Harry to take occlumency lessons with Snape, because the scar connects him to Voldemort and Harry should be able to close it. Harry says yes, because Dumbledore asked.
- **Plants:** Justin's hatred. Harry inside Umbridge's circle.
- **Escalation:** Harry is running a secret army from inside the enemy's office.
- **Ending:** the first lesson with Snape, at the door.

## Chapter 49: Snape's Worst Memory

- **When/where:** November 1995 to January 1996. Snape's office; inside Snape's memories (Spinner's End, a playground, the lake at Hogwarts in the 1970s); Harry's dormitory at night; inside Voldemort's mind.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** the duels of minds, Lily, the scar link, and the thing that looks back.
- **Beats:**
  1. The lessons. Snape attacks. Harry, a natural legilimens, does not only defend. He attacks back. Lessons become duels.
  2. The fourth lesson. Harry gets in. Memories: a girl with red hair in a playground, a boy in too-large clothes watching her. The lake: James and Sirius tormenting the boy. A word said in anger. Harry does not just see it. He reads it: what Snape felt for Lily, directly, from inside. It is the purest feeling he has ever read in anyone, and it is a wound.
  3. Snape throws him out of his mind and out of the room. Lessons are over. Harry reads shame and hatred, and now a new thing, aimed at him: Snape has been *felt*, and he will never forgive it.
  4. The scar link. Harry dreams Voldemort's feelings. Then, because he is curious and arrogant and a legilimens, he goes in on purpose at night. He learns Death Eater movements. He tells Dumbledore some. It feels like winning.
  5. One night, inside, something turns and looks back at him. For a moment he thinks he feels Voldemort reading the inside of his own head, a shelf of memories, a round room, a black desk. He wakes and tells himself he imagined it. Write it ambiguously enough that the reader may believe him.
- **Plants:** something looks back (Voldemort finds Slytherin's journal in Harry's memory).
- **Escalation:** Harry has made an enemy of Snape in a new way, and let the enemy into his head.
- **Ending:** the moment of being looked at, unresolved.

## Chapter 50: Christmas at Grimmauld Place

- **When/where:** December 1995. Harry's dormitory, the night of the snake; Dumbledore's office at midnight; St Mungo's (the Spell Damage ward, a long-term ward); 12 Grimmauld Place at Christmas; Nurmengard (Evelyn); Selwyn Hall on Boxing Day (Evelyn).
- **POV:** Harry, then Evelyn.
- **Target:** about 7,500 words.
- **Purpose:** Arthur; Lockhart's cameo; Kreacher's errand; Evelyn's training; Lucan's Mark.
- **Beats:**
  1. Harry dreams he is a snake in a corridor in the Ministry, biting a red-haired man. He wakes and goes straight to Dumbledore. Arthur Weasley is found in time.
  2. Grimmauld Place at Christmas. The Weasleys grateful to him. Ron and Hermione thawing. Sirius at his happiest, with a full house.
  3. St Mungo's. Arthur. Neville's parents (Harry reads Alice Longbottom: a small, clear, entirely present love for her son, in a mind that has nothing else left in it). And, in a rehabilitation ward, **Gilderoy Lockhart**, walking with a stick and a great deal of panache, who announces he has been approached by "a certain Order" and finds the whole thing thrilling.
  4. Christmas night. Harry reads Kreacher coming back from somewhere he should not have been, full of a small, secret glee. Harry mentions it. Nobody takes it seriously, including, in the end, Harry.
  5. **Evelyn at Nurmengard.** Grindelwald knows the war has begun. He begins teaching her Stillness in earnest: how to still a candle flame without touching it, then a falling cup, then a spell. He is a fine teacher and a frightening one. He asks about the boy, as always. She tells him about the defence group, because she wants to see his face. He looks proud of someone he has never met, and then annoyed at himself.
  6. **Evelyn at Selwyn Hall, Boxing Day.** Lucan rolls up his sleeve at the sink without thinking. She sees the Mark. He sees her see it. He smiles their father's smile. Neither says anything. Her father, at dinner, talks about "realism".
- **Payoffs:** Kreacher's devotion (he has given Narcissa the locket).
- **Plants:** Lockhart's return. Lucan's Mark.
- **Escalation:** Evelyn's brother is a Death Eater, and something has left Grimmauld Place that should not have.
- **Ending:** on Lucan's smile, or Evelyn winding the watch the next morning in a house she no longer considers hers.

## Chapter 51: The Diadem

- **When/where:** January to March 1996. The Prophet headlines (the Azkaban breakout); Umbridge's office; the seventh-floor corridor; the Room of Hidden Things; Dumbledore's office at night.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** the breakout; Draco's errand; the diadem; Horcruxes explained; Harry's guilt.
- **Beats:**
  1. Ten Death Eaters out of Azkaban, Bellatrix Lestrange among them. Harry reads the school's fear rise. He reads Draco's pride rise.
  2. Umbridge asks Harry to help her find "an illegal student association". He gives her false information so smoothly that she thanks him. Draco watches him do it and starts to suspect.
  3. Draco has been given an errand. Harry reads it on him every day for a week: fear, pride, importance. He follows Draco to the seventh floor. Evelyn comes.
  4. The Room of Hidden Things: centuries of hidden junk, a tall cabinet Draco looks at curiously (plant for next year), and a tarnished diadem on a bust. Draco picks it up. Harry, at a distance, feels it: *hungry*. The same as the diary.
  5. And something in Harry answers it. A small cold movement inside him, toward the diadem, like a compass needle. He is so shaken that he hesitates, and Draco gets away with it.
  6. Harry goes to Dumbledore that night. He tells him everything: the diary, the diadem, the hunger, the journal's line about divided things, the something that looked back through his scar.
  7. Dumbledore explains Horcruxes, plainly and fully, as he would to an equal. Voldemort made several. He is gathering them. Harry says it before Dumbledore can: he means to make himself whole again, because a divided thing cannot stand on a summit. And he learned that from Harry's head.
  8. Harry reads Dumbledore: horror, and agreement, and something else, held back very hard. Dumbledore does not mention the scar. Harry knows he is withholding something about Harry. He does not know what.
- **Payoffs:** the diary's hunger. "No divided thing". Something looked back.
- **Plants:** the cabinet. The faint cold in Harry (third time, now stronger).
- **Escalation:** Voldemort is about to become far more dangerous, and it is Harry's fault.
- **Ending:** on Dumbledore not saying something.

## Chapter 52: The Flight

- **When/where:** March to April 1996. The Room of Requirement; Umbridge's office; Dumbledore's office (the escape); the Great Hall; the entrance hall (fireworks); the Slytherin common room.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the group exposed, Dumbledore's flight, and Harry an open enemy.
- **Beats:**
  1. Draco, suspicious since January, has been watching Harry read people. He uses it against him: he feeds Harry a false feeling on purpose (he has learned, from five years of being read, to *perform* his fear) and follows him to the Room of Requirement. The group is caught. Rivalry payoff: Draco has learned to lie to the reader.
  2. Umbridge's office. Fudge, Kingsley, Dawlish. Harry reads Umbridge's betrayal: she feels genuinely hurt that he lied to her, which is almost funny.
  3. Dumbledore takes the blame and leaves in a burst of phoenix fire. Harry reads him: grim delight. He would not have missed this for anything.
  4. Umbridge is Headmistress. Fred and George leave in a storm of fireworks. Harry reads the whole school laughing at once, and it is the best noise he has heard in months.
  5. Harry is out of Umbridge's circle and is now her particular enemy. Detentions. The quill, at last, on him. *I must not tell lies.* He finds this funny, privately, and it leaves a scar on his hand.
  6. Without Dumbledore, the scar link grows. Harry stops going in on purpose. It goes in on him instead.
- **Escalation:** Dumbledore is gone and Harry has no cover.
- **Ending:** the scar, at night, and a feeling of preparation that is not his.

## Chapter 53: The Vision

- **When/where:** June 1996. The Great Hall during the OWLs; the Forbidden Forest with Umbridge and the centaurs; the History of Magic exam; Umbridge's fireplace; a Floo call; the Hog's Head (this world); the Ministry's visitor entrance.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** OWLs; Umbridge's end; the vision; going in with a plan.
- **Beats:**
  1. OWLs. Harry's competence: the Defence practical, where his Patronus fills the hall. The examiner says she has seen only one other like it.
  2. Umbridge finally catches him. Harry, alone with her in the forest, puts an illusion on her and walks her into the centaurs. He knows exactly what he is doing. It works. He reads her terror and does not feel sorry. (A dark beat. Do not soften it.)
  3. In the History of Magic exam he falls asleep and sees Sirius tortured in the Department of Mysteries. He knows it is a trap: he watched it happen in another world.
  4. He also feels, through the link, something enormous being prepared in that place. Not a trap for Sirius. Something much larger. He works out that the remerge is tonight, and that it is happening at the Veil.
  5. He does not go blindly. He uses Umbridge's own fireplace to call Grimmauld Place. Sirius is safe. He tells Sirius what he thinks is happening. Sirius alerts the Order. A message goes to Dumbledore, who is a fugitive and will come as soon as he can.
  6. Harry insists on going, because he is the only one who can feel through the link when the ritual begins. The Order argues. Sirius says that if anyone tries to leave Harry behind, he will go with Harry. A team assembles: Harry, Evelyn, Millicent, Neville, Luna, Ron, Hermione. Theo does not come; his father will be there. Order members will meet them at the Ministry.
  7. Thestrals, or the Floo from the Hog's Head. The visitor entrance.
- **Escalation:** they are walking into the place Harry watched a man die.
- **Ending:** the lift going down.

## Chapter 54: The Veil

- **When/where:** the same night. The Department of Mysteries: the circular room, the Hall of Prophecy, the Death Chamber.
- **POV:** Harry.
- **Target:** about 8,500 words (climax).
- **Purpose:** the remerge, the fragment, Parseltongue lost, Sirius saved, Tonks lost.
- **Beats:**
  1. The circular room. The doors. Harry knows the way.
  2. The Hall of Prophecy. Death Eaters. Lucius wants the orb with Harry's name on it. Harry smashes it himself. He already knows what it says, and now nobody else ever will. Lucius's face.
  3. The Order arrives: Sirius, Tonks, Lupin, Moody, Kingsley. The fight moves to the Death Chamber.
  4. Voldemort is there. In person. At the arch. Around him, on the stone steps: a locket, a ring, a cup, a diadem. Nagini coiled at his feet. He has been waiting for Harry. He opens his arms as though to greet him.
  5. The ritual. Voldemort calls to the pieces of himself. Each object cracks and a darkness goes out of it into him. Then he calls the seventh, and something inside Harry answers.
  6. It is torn out of him. The scar splits. Harry is speaking, shouting a warning in Parseltongue to the snake on the steps, and halfway through the word the hiss becomes English. He hears it happen. He understands what he was. Write it as a loss, plainly, and fast.
  7. Voldemort is whole. Harry reads him and for the first time the cold has no seams in it.
  8. Bellatrix and Sirius, duelling by the arch, laughing. Harry has seen this. He knows the curse. He moves before it is cast, a shield or his body or an illusion of Sirius one step to the left. The curse misses. Sirius does not fall.
  9. Voldemort, testing his new soul, sends one curse across the chamber without looking. It hits Tonks, beside Sirius. She falls. She does not get up. Sudden. Unrelated to anything Harry did. He will never be sure of that.
  10. Voldemort walks out of the chamber toward the lifts. He is going up to the Atrium. Harry follows.
- **Payoffs:** the prophecy. The other Sirius's curse. The cold presence.
- **Escalation:** Voldemort is whole, Harry is no longer part of him, and Tonks is dead.
- **Ending:** Harry on the stairs, running after him, and realising he is still reading everyone. (Do not explain. He just notices he can still feel Evelyn's silence beside him and the Order's terror behind him.)

## Chapter 55: Sovereign

- **When/where:** the same night. The Ministry Atrium: the fountain, the fireplaces, the golden gates.
- **POV:** Harry, with a short Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** the first Pinnacles anyone sees; Dumbledore's cost; Fudge sees.
- **Beats:**
  1. The Atrium. Voldemort at the fountain. Death Eaters gathering. Harry, Evelyn, the Order, the students.
  2. Voldemort opens **Sovereign**. Write it as a change in the rules of the room: every wand in the Atrium turns, slowly, towards the fountain. Harry's own arm begins to lift. His body is not his. Ron's wand turns on Hermione. Millicent's knees bend.
  3. **Evelyn scene:** she does not move. Nothing in her is touched. Her mind has never been anyone else's. She walks across the Atrium through a room full of people kneeling and knocks Harry flat out of the line of his own wand. She notes, as she does it, that she is the only person in the room standing upright by choice.
  4. Dumbledore arrives in the fireplace. He looks at Voldemort and understands what has happened.
  5. Dumbledore opens **First Matter**. The Atrium forgets what it is. The fountain becomes rain. The golden gates become birds. The floor under the Death Eaters becomes water. Voldemort's Sovereign and Dumbledore's First Matter meet in the middle of the room and neither gives.
  6. Harry, on the floor, watches Dumbledore's hair go from grey to white and his face fold into a decade of age in under three minutes.
  7. Fudge arrives through a fireplace with Aurors at exactly the moment Voldemort is standing in the middle of the Atrium. Everyone sees him. Aurors see Pettigrew at his side.
  8. Voldemort withdraws. Bellatrix and the others with him. He looks at Harry once as he goes, with interest and no hurry at all.
- **Plants:** Dumbledore's cost. Evelyn's immunity to Dominion.
- **Escalation:** the most powerful wizard in Britain was not enough.
- **Ending:** Dumbledore sitting down on the rim of what used to be the fountain, very old.

## Chapter 56: What Was Left

- **When/where:** the following days. Dumbledore's office; Myrtle's bathroom; Tonks's funeral at a small church in Devon; the Astronomy Tower; King's Cross.
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the truth, the losses, Sirius cleared, the summer.
- **Beats:**
  1. Dumbledore's office. He is old now, visibly, and says so as a fact. He tells Harry everything: he suspected the scar from the beginning; he did not tell him; he was afraid of what it would do to him to know. He apologises once. Harry is angry, and understands, and is angry. Both stay.
  2. Harry goes to Myrtle's bathroom alone and speaks to the sink. It is English. Nothing happens. He tries again. The Chamber is closed to him forever, and the study with it. He sits on the floor for a while.
  3. Tonks's funeral. Her parents. Lupin, who reads, even to Harry's ordinary eye, as a man whose life has stopped. Sirius standing very straight beside her grave, alive because of Harry and wondering why.
  4. The Astronomy Tower with Evelyn. He says nothing about the reading still working. She says nothing about it either. Then she says something dry about OWL results. That is how they talk about it.
  5. Sirius has been cleared. The Aurors saw Pettigrew. The Prophet runs his face on the front page with the word INNOCENT, and three weeks later the word HERO. Dumbledore tells Harry he may live with his godfather. The blood protection matters less now that Voldemort has his blood anyway. Harry reads that it costs Dumbledore something to say so.
  6. King's Cross. Sirius on the platform in plain sight, in a terrible coat, waving.
  7. A letter from Evelyn the next morning: one line. Her brother has the Mark and her father has accepted a position.
- **Escalation:** the war is public and the Selwyns have chosen.
- **Ending:** Evelyn's line.

---

# YEAR SIX

## Chapter 57: Grimmauld Place, Summer

- **When/where:** July to August 1996. Grimmauld Place (renovation of a kind); a newspaper stand; the Millennium Bridge in the news; a lay-by on the A49; Nurmengard.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** happiness, briefly; the war in the papers; Grindelwald meets Harry.
- **Beats:**
  1. Sirius and Harry at Grimmauld Place. Sirius is bad at being a guardian and wonderful at being loved. They take down the elf heads. They fail to cook. Kreacher sulks. Write the funniest domestic scenes in the story here, because the reader will need them.
  2. Evelyn visits. Sirius adores her immediately and teases her without mercy; she answers him with precise, devastating politeness, which he adores more. Harry reads Sirius's delight.
  3. Dumbledore visits. He meets Evelyn for the first time properly. He looks at her face for a long moment. Harry reads, very briefly, recognition, then grief. Dumbledore says nothing. (He has guessed whose granddaughter she is. He keeps it.)
  4. The war in the papers. The Millennium Bridge. Amelia Bones murdered. Dementors breeding. "The Chosen One".
  5. Evelyn says it is time. Varga's Portkey from the lay-by, Harry holding her arm because the key only answers her blood. Nurmengard. **Grindelwald meets Harry.**
  6. Write it as two Walkers who both know exactly what the other is. Grindelwald reads Harry's Path at a glance: *Illusion. How rare. The last one went mad, and he was a better man than either of us.* He is charming to Harry and cruel about Dumbledore and very precise about the future. He tells Harry that a whole soul fears death more than a divided one, and that Voldemort will now want what Gellert once wanted: the Hallows. He tells them the story of the three brothers, briefly, his way. He tells Harry who has the Elder Wand.
  7. On the way out, Grindelwald says one thing to Harry alone that he does not repeat to Evelyn. Show Harry not repeating it. (It is: *"She will open the door for you once. Do not make her do it twice."*)
- **Plants:** Grindelwald's private line (paid off Ch 76). Dumbledore's recognition of Evelyn.
- **Escalation:** Voldemort is coming for the Hallows, and one of them is in Harry's trunk.
- **Ending:** the Portkey home, and Harry not repeating the line.

## Chapter 58: The Mark

- **When/where:** September to October 1996. The train; Slughorn's compartment; the Slytherin table; the Potions dungeon; Dumbledore's office and the Pensieve (Wool's Orphanage in the 1930s); Hogsmeade in the first snow.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** sixth year; Slughorn; the Prince's book; Draco's Mark; Tom's past; Katie Bell.
- **Beats:**
  1. Evelyn's seventh year. She says she will not be sentimental about it. She is a little sentimental about it.
  2. Slughorn collects Harry, who lets himself be collected. Harry reads him: vanity, fondness, and a fear he keeps in a locked drawer.
  3. Potions: Harry borrows a battered textbook annotated by *the Half-Blood Prince*. The annotations are brilliant. In the margins, spells. One of them is marked *for enemies*.
  4. Draco has the Mark. Harry reads it on him at the first feast: terror, enormous, under the pride. He watches Draco all year, the way you watch weather.
  5. Dumbledore's lessons, as equals. The Pensieve. Tom at eleven in Wool's Orphanage. Harry reads emotions in the memory and finds that the boy wants things very much and feels almost nothing about anyone. Harry recognises the shape of himself in it and is sickened by how much.
  6. Katie Bell and the necklace. Harry reads the curse's malice from yards away. Draco's attempt. Harry knows and cannot prove it.
- **Plants:** the Prince's spell. Draco's terror.
- **Escalation:** Draco is going to kill someone.
- **Ending:** Katie screaming in the snow, and Harry reading Draco three streets away, sick.

## Chapter 59: The Gaunt Ring

- **When/where:** November to December 1996. A ruined shack outside Little Hangleton; Dumbledore's office; the Slytherin dormitory at night; Slughorn's Christmas party; the Nott house in Yorkshire (reported, not shown).
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the Stone deduced; Dumbledore's frailty; Theo takes the Mark.
- **Beats:**
  1. Dumbledore and Harry Apparate to the Gaunt shack. It is empty. The hiding place under the floor is open. The ring is gone. Voldemort took it for the remerge, and wears it now.
  2. In the dust Dumbledore finds a scrap of the old Gaunt story. Between them, by talk, they work out that the black stone in the ring is the Resurrection Stone. Voldemort is wearing a Hallow and does not know it.
  3. Dumbledore is very tired. He sits down on a broken chair. Harry reads in him, for the first time, the plain fear of dying soon.
  4. Theo comes to Harry at night. His father wants him to take the Mark at Christmas. Theo does not want to. He asks Harry what to do.
  5. Harry tells him to take it. To take it and tell Harry everything. It is the right strategic answer. Harry reads Theo's relief at being told what to do and does not let himself think about what he has just asked of his friend. (Write it without comment.)
  6. Slughorn's party. Harry with Millicent again as friends, which is now a joke between them. Draco dragged in by Filch. Snape. Harry reads Snape's fear for Draco and his dread about something else, a promise.
- **Plants:** Snape's promise (the Vow).
- **Escalation:** Harry has sent his best friend to the Death Eaters.
- **Ending:** a letter from Theo after Christmas, one word, in a code they agreed.

## Chapter 60: Sectumsempra

- **When/where:** January to February 1997. Corridors; a boys' bathroom on the sixth floor; the hospital wing; Snape's office.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** Harry nearly kills Draco; Snape recognises his own spell.
- **Beats:**
  1. Harry tries, for the first time, to talk to Draco properly. He finds him crying in a bathroom with Myrtle. He reads despair so loud he cannot think through it. He tries to say something true.
  2. Draco, humiliated at being seen, attacks. They duel. Harry, angry and frightened and reading Draco's intent to hurt him, uses the spell from the margin: *Sectumsempra*.
  3. Blood. Draco on the wet floor. Harry reads Draco's mind going quiet. Write it as fast and as plain as Cedric's death, so the reader thinks it is the same.
  4. Snape. He sings the wounds closed. Draco lives. Snape looks at Harry. Harry reads recognition: Snape knows that spell, because he made it. Then fury. Then something calculating. "Where did you learn that?"
  5. Detentions. The book hidden in the Room of Requirement.
  6. **Evelyn** hears about it from Millicent. She goes to find Potter. She is not angry. She is frightened, for him, and for the first time she does not hide it from herself. She writes it down in her diary as a fact.
- **Plants:** Snape's spell.
- **Escalation:** Harry has nearly killed a boy with his enemy's magic.
- **Ending:** Evelyn's diary line, or Snape's question.

## Chapter 61: Stillness

- **When/where:** March 1997. Nurmengard (a lesson); an unused classroom on the third floor; the Owlery; Selwyn Hall (a letter); the Slytherin common room at night.
- **POV:** Evelyn (the whole chapter, except one short Harry scene at the end).
- **Target:** about 6,500 words.
- **Purpose:** Evelyn's Path, its first use, its costs.
- **Beats:**
  1. A lesson at Nurmengard. Grindelwald teaches her that a Pinnacle is not a spell, it is a place you go. He has her still a falling cup of water. Then a falling spell. He asks about the boy. She tells him about *Sectumsempra*. He is silent for a while, which he rarely is.
  2. Back at school. A cursed object (something Draco has smuggled, or something unrelated) goes off in an empty classroom where three first-years are hiding from a prefect. Evelyn is the only one near. She does what Grindelwald taught her, all the way. **Dead Calm.** The curse stops in the air. The room's magic dies. The candles go out because their charms do. The first-years are safe.
  3. Inside it, she feels nothing. Not calm. Nothing. She notices, with interest and no feeling, that a self-mending charm on a first-year's torn sleeve has stopped mending. (Plant: it stills healing.)
  4. She lets it go. Everything she did not feel for four minutes arrives at once. She sends the first-years away with perfect composure and sits on the classroom floor and comes apart, alone, as she has not since she was a small child.
  5. A letter from her mother: Corvin has accepted a seat on a new committee. Lucan has been promoted. Marguerite says she is sorry, again, for everything.
  6. Evelyn decides she will not go home after her final exams. Ever.
  7. **Harry, briefly:** he finds her in the Owlery at midnight. He cannot read her. He does not try to make her talk. He sits beside her on the cold floor and she leans against his shoulder for a while and neither of them says anything. (Friendship. Keep it exactly that.)
- **Plants:** Dead Calm stills healing.
- **Escalation:** Evelyn has reached her Pinnacle and learned what it costs.
- **Ending:** the two of them on the Owlery floor.

## Chapter 62: Lockhart Returns

- **When/where:** Easter 1997. Grimmauld Place; a Cornish cliff; a disused tin mine near St Just; the mine's flooded lower galleries; a pub in Penzance afterwards.
- **POV:** Harry.
- **Target:** about 7,000 words.
- **Purpose:** Lockhart in the field; battlefield illusion; Grindelwald's warning.
- **Beats:**
  1. Lockhart arrives at Grimmauld Place in a cloak of an extraordinary colour, fully recovered and delighted to be useful. Sirius cannot stand him for exactly ten minutes and then cannot get enough of him.
  2. The Order has word of a nest of Inferi in an old tin mine near St Just, and a Muggle-born family hiding in the upper galleries above them. Lockhart is going. He asks for Harry. Dumbledore, asked, says Harry may decide. Harry goes.
  3. The mine. Dark, wet, the sea booming in the rock. Lockhart is funny and brave and, it turns out, an extremely good field operative. He teaches Harry battlefield illusion: not one perfect lie but a hundred bad ones, fast, for minds that are not thinking.
  4. Inferi. Harry reads nothing from them, which is a horror of its own. Lockhart uses fire with great flair.
  5. The family: a mother, a father, two children. Harry reads the children's terror and, without asking, pushes courage into them so they will run. They run. It works. He does not tell Lockhart.
  6. A pub in Penzance afterwards. Lockhart, very pleased, signing a beer mat for the barmaid without being asked.
  7. An owl from Evelyn, forwarded: her grandfather says the Dark Lord will come for the Elder Wand before the summer. Harry takes it to Dumbledore. Dumbledore already knows.
- **Plants:** the first unconsented push since Marge.
- **Escalation:** Voldemort is coming to Hogwarts for Dumbledore's wand.
- **Ending:** Dumbledore saying he knows.

## Chapter 63: The Cabinet

- **When/where:** May to June 1997. The seventh-floor corridor; the Room of Hidden Things; Dumbledore's office; Snape's office door; Prague (planned, not yet).
- **POV:** Harry.
- **Target:** about 6,500 words.
- **Purpose:** the offer to Draco; Dumbledore's choice; what Dumbledore withholds.
- **Beats:**
  1. Theo's coded letters confirm it: Draco is to kill Dumbledore, and the cabinet in the Room of Hidden Things is a door.
  2. Harry confronts Draco in the Room. The cabinet behind them. Write the most honest conversation they ever have. Harry offers him a way out: Dumbledore will hide his mother. Draco reads, by now, as well as anyone can read Harry, which is not at all, and he does not believe him. He refuses. He is terrified. He says something about his mother that Harry cannot answer.
  3. Harry tells Dumbledore. Dumbledore says: *I know. Let it come. I would rather the boy did not become a murderer.* Harry argues. Dumbledore asks him to trust him once more. Harry reads that Dumbledore has already decided how he will die.
  4. Harry asks whether there is anything else Dumbledore has not told him. About Harry. Dumbledore says no. Harry reads that it is not true. Dumbledore reads that Harry has read it. Neither says anything.
  5. Snape's office door, ajar. Harry reads dread through it, and something Snape has sworn.
  6. Dumbledore tells Harry he wants to take him somewhere first: Prague, to ask four old people for help.
- **Plants:** Dumbledore's lie about Harry.
- **Escalation:** everyone knows what is coming and nobody will stop it.
- **Ending:** Dumbledore holding out his arm for Side-Along.

## Chapter 64: The Tower

- **When/where:** a night in late June 1997. Prague (a house in Malá Strana where the Concordat meets); Hogsmeade; the Astronomy Tower.
- **POV:** Harry.
- **Target:** about 7,500 words.
- **Purpose:** the Concordat's refusal; the Mark over the tower; Draco disarms Dumbledore; Voldemort comes.
- **Beats:**
  1. Prague. A narrow house on a hill. Four old Walkers in a room with a stove: Dona Inês Albuquerque, Arkady Volkonsky, and two who do not give their names. Dumbledore asks for help. They refuse. *The Concordat does not go to war.* Dona Inês looks at Harry for a long time and says something about Illusion in Portuguese that Dumbledore does not translate. Harry reads them: fear, old and prudent, and pity.
  2. Back to Hogsmeade at night. The Dark Mark over the Astronomy Tower.
  3. The tower. Dumbledore weak. Draco comes up the stairs with his wand out. *Expelliarmus.* Dumbledore's wand flies over the parapet. (The Elder Wand's allegiance passes to Draco here. Nobody knows.)
  4. Harry, under the Cloak, is not frozen this time. He could act. He reads Draco: he cannot do it. He reads Dumbledore: calm, and asking him silently to wait.
  5. Death Eaters arrive. Then Snape. Harry reads Snape: grief and resolve, and the Vow. Snape raises his wand.
  6. And then the cold comes up the hill like weather. Every Death Eater on the tower goes still and turns. Voldemort is in the grounds. The cabinet let his servants in. His own will broke the wards. He has come for the wand himself.
- **Escalation:** the Dark Lord is inside Hogwarts.
- **Ending:** Dumbledore, without a wand, standing up straighter, and someone (Harry? Snape?) handing him a wand back. Make it the Elder Wand recovered from the grass by Snape's spell, and Dumbledore taking it without a word.

## Chapter 65: First Matter

- **When/where:** the same night. The Astronomy Tower; the lawn; the lake shore; the foot of the tower where students are sheltering; Hagrid's hut on fire.
- **POV:** Harry, with one section from Dumbledore and one short Evelyn scene.
- **Target:** about 8,500 words (climax).
- **Purpose:** Pinnacle against Pinnacle; Justin; Dumbledore's death; the wand taken.
- **Beats:**
  1. **Dumbledore's section**, the minute before. Short. He thinks of Ariana, and Gellert, and the boy under the Cloak. He thinks about what he has asked Severus to do if the boy becomes what he fears. He is ashamed of it and does not change it. He goes down to meet Tom.
  2. Voldemort on the lawn with his followers around him. **Sovereign** opens. Every mind on the grounds that is weaker than his begins to bend. Students at the windows. Death Eaters. Harry feels it climbing up his own arm.
  3. Dumbledore opens **First Matter**. The lawn becomes water, the water becomes glass, the glass becomes birds. The sky over the lake changes colour. Two Pinnacles grind against each other. It is weaker than it was in the Atrium. Only Harry notices Dumbledore look down at the wand in his hand, once, puzzled, as though it had answered him a fraction late. (Plant: the wand's allegiance moved to Draco on the tower. Do not explain it.)
  4. Harry tries to help. He throws an illusion at Voldemort, the best he has ever made. It is swallowed. Voldemort, in a crowd, is fed by every mind he holds. Harry is a candle against a furnace. He learns, by failing, that he must one day get Voldemort alone.
  5. **Evelyn**, at the foot of the tower, where students are sheltering, is behind a line of Death Eaters' curses. She opens **Dead Calm** around the students. The curses fall out of the air. Sovereign cannot reach inside. She feels nothing.
  6. Inside her calm, Justin Finch-Fletchley lies wounded. Madam Pomfrey is kneeling over him keeping him alive with a charm. The charm stops. Evelyn sees it stop. She feels nothing. Justin dies inside her Pinnacle. She will feel it later.
  7. Back to Harry. Dumbledore, ageing by the second, does something with First Matter that turns the whole east face of the lawn into a wall of water between Voldemort and the castle. It holds. It costs him everything. He falls. Whether Voldemort's curse got through first or the cost simply took the last of his years, Harry cannot tell. Nobody ever will.
  8. Voldemort walks across the grass and takes the Elder Wand from Dumbledore's hand. He weighs it. He looks pleased. He looks up at the tower, at where Harry is, and says something quiet that carries.
  9. Hagrid's hut burning. Death Eaters fleeing with their master. Sirius arriving through the gates with the Order, too late.
- **Payoffs:** Dead Calm stills healing. Dumbledore's cost.
- **Plants:** Voldemort must be alone. The wand's allegiance is not what it seems.
- **Escalation:** the loudest night of the story so far.
- **Ending:** the silence after, and Harry kneeling by Dumbledore, reading nothing.

## Chapter 66: Lament

- **When/where:** the days after. The lawn at dawn; the courtyard; the hospital wing; the headmaster's office (McGonagall now); the funeral by the lake; Gringotts or a solicitor's office for the will.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,500 words.
- **Purpose:** grief; Snape's grief read; the letter.
- **Beats:**
  1. Fawkes's lament. The castle's grief, which Harry reads all at once, every room of it, and does not turn down.
  2. A courtyard. Snape crosses it. Harry reads him from across the yard, through Snape's own closed mind, because the grief is too big to close: it is raw and total and it is for Dumbledore. Harry knows, then, that Snape was loyal. From this moment he trusts him.
  3. **Evelyn** in the hospital wing, the day after, beside the bed where Justin died. She feels it now, all of it. She tells Madam Pomfrey, precisely, what she did. Pomfrey says it was not her fault. Evelyn says that is not what she asked.
  4. Dumbledore's portrait, asleep. McGonagall, acting head, worn to the bone.
  5. The funeral. Centaurs, merpeople, the whole school. Sirius, Lupin, Lockhart in dark colours for once. Harry reads all of it and stands very still.
  6. The will. To Harry, Dumbledore leaves his notes on the Paths and a letter. Write the letter: short, in Dumbledore's voice. It ends: *If I have treated you as a soldier, forgive me. I was afraid of what you would be. I am still afraid. That is not your fault.*
- **Plants:** the letter's fear (paid off Ch 77). Harry's trust in Snape.
- **Escalation:** the school is going to fall.
- **Ending:** on the letter's last line.

## Chapter 67: Seventeen

- **When/where:** late June to 31 July 1997. The Great Hall for Evelyn's last leaving feast; the station; Grimmauld Place; a coded note from Theo; Harry's seventeenth birthday.
- **POV:** Harry.
- **Target:** about 6,000 words.
- **Purpose:** an ending to school, a decision, and the eve of the fall.
- **Beats:**
  1. Evelyn's last day as a student. No Selwyn comes to see her finish. Harry and Sirius do. Sirius makes a scene, a good one.
  2. Theo, coded: the Ministry will fall within weeks. Thicknesse is under the Imperius. The Selwyns have positions waiting.
  3. Harry tells Sirius and McGonagall he will not come back for seventh year. Evelyn says she is not going home. Sirius says she is staying at Grimmauld Place and that is the end of it.
  4. Harry writes to the Concordat himself. The reply, in Dona Inês's hand, is one line: the Concordat does not go to war. He burns it.
  5. His seventeenth birthday at Grimmauld Place. Weasleys, Lupin, Lockhart, Hagrid, Millicent, Neville, Evelyn. Sirius has made a cake that is genuinely terrible. It is a happy evening. Write it as fully and warmly as the summer scenes, because it is the last one.
  6. Bill and Fleur's wedding is tomorrow.
- **Escalation:** the calm before the fall.
- **Ending:** Sirius, at the end of the night, saying something about the wedding tomorrow, and Harry reading that he is perfectly happy.


========================================================================
# FILE: SPOILERS_10_CHAPTERS_Y7_AFTER.md
========================================================================

# SPOILERS · 10 · CHAPTER PLANS: YEAR SEVEN AND AFTER

Harry is seventeen. Evelyn is eighteen. They are fighting a war. Their relationship is still friendship and absolute trust. **No romance until Chapter 82.**

The Prologue is replayed from the inside in Chapter 73. Reread the Prologue before writing Chapter 73 so the two match detail for detail: the snow, the fourteen men, the apple, the flowers she sees as snow, his glove off and his hand blue, his polite stranger's smile.

---

## Chapter 68: The Burrow

- **When/where:** 1 August 1997. The Burrow: the marquee, the orchard, the kitchen door; a Muggle street in Leeds at night.
- **POV:** Harry.
- **Target:** about 8,000 words.
- **Purpose:** the Ministry falls; Sirius dies; the escape; the four.
- **Beats:**
  1. The wedding. Bright and loud. Harry reads a hundred happy people and lets it run all the way up for once. Sirius in dress robes, dancing with Molly, appalling at it. Lockhart signing napkins. Evelyn at a table at the edge, reading the order of service for errors.
  2. A silver lynx lands in the middle of the dance floor. Kingsley's voice: the Ministry has fallen; the Minister is dead; they are coming.
  3. Death Eaters at the edge of the wards. Screaming. Harry reads terror arrive in a hundred people at once.
  4. Harry fills the orchard with Harrys. Fifty of them. Lockhart's lesson: not one perfect lie but many bad ones, fast. The Death Eaters chase illusions while the guests run.
  5. Sirius holds the kitchen door so the Weasleys can get out through it. He is laughing. He is very good. Then he is not standing. Write it fast, in the middle of something else, the way it would really happen. Harry sees it from across the garden and does not stop running, because he is carrying someone.
  6. Moody, in the lane, covering the gate. Gone. Hedwig, who came because she always comes, struck out of the air. One line.
  7. Harry, Evelyn, Ron and Hermione Apparate together, holding hands, to the only place Evelyn has prepared: a back alley in Leeds behind a boarded-up picture house called the Majestic.
- **Escalation:** the world has fallen and his godfather is dead.
- **Ending:** the four of them inside a dark cinema, and Harry not crying.

## Chapter 69: The Majestic

- **When/where:** August to October 1997. The Majestic: the foyer, the projection room, the auditorium, the screen; a Leeds market; a newsagent's on the corner.
- **POV:** Harry and Evelyn, alternating.
- **Target:** about 7,000 words.
- **Purpose:** hiding; the four as a unit; training; Snape's doe.
- **Beats:**
  1. The cinema. Evelyn found it in 1995 and has been paying the rates through a Muggle solicitor in Wakefield ever since, under a false name, because she believes in contingencies. Ron is outraged and impressed in equal measure.
  2. Living together: the four of them, very different, in a closed cinema. Arguments about food. Hermione's beaded bag. Ron's radio. Evelyn's detective novels. Harry's silence.
  3. Harry will not cry for Sirius. He reads the others' grief instead, every day, all of it. He trains.
  4. The screen. He projects illusions onto the empty screen for hours: crowds, streets, faces, weather. The auditorium becomes anywhere. Ron, watching a fake Quidditch final, says it is the best thing he has ever seen and also the most worrying.
  5. **Evelyn** notes the hours he trains (eleven a day) and the hours he sleeps (four). She writes them down.
  6. The regime: Muggle-born Registration Commission, chaired by Corvin Selwyn. Hermione hunted. Snape headmaster of Hogwarts. The Order shattered.
  7. Theo's coded coin messages.
  8. One night a silver doe walks through the wall of the auditorium carrying a message (where Death Eaters will be, a raid to avoid). Harry reads the Patronus, which is made of feeling, and knows whose feeling it is: Snape's, the same love he read in Snape's memory of Lily. Harry trusts the doe. He trusts Snape.
- **Plants:** Snape's doe.
- **Escalation:** Harry is turning himself into a weapon.
- **Ending:** the doe fading on the empty screen.

## Chapter 70: The Commission

- **When/where:** November 1997. The Ministry (under illusion): the Atrium with its new black statue, a lift, Courtroom Ten; a Muggle street in Whitehall.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,500 words.
- **Purpose:** the raid; Evelyn faces her father; the push used to save people, and liked.
- **Beats:**
  1. The plan: free a courtroom of Muggle-borns waiting to be judged. Harry puts illusion faces on the four of them as seen by everyone else. Evelyn sees them all as they are. She is the one who can tell when an illusion is slipping.
  2. The Atrium: the statue of witches and wizards seated on Muggles. Harry reads a building full of fear.
  3. Courtroom Ten. Dementors at the edges. Umbridge, sweet as ever. And chairing: **Corvin Selwyn**, still and grey and reasonable, asking a frightened woman about her wand in a voice like water on stone.
  4. **Evelyn scene:** she stands ten feet from her father with a stranger's face, as far as he can see. He looks at her and does not know her. She speaks to him, as a stranger, about a point of procedure, and corrects him. He concedes, politely. He has never once conceded to her in her life.
  5. The break. Patronuses against the Dementors. Chaos. The Muggle-borns are frozen with terror and will not move.
  6. Harry pushes courage into all of them at once, without asking. They run. It works perfectly. Every one of them gets out.
  7. On the street afterwards, Hermione thanks him and then asks, carefully, what he did to them. He tells her. She goes quiet. Ron says it was worth it. Evelyn says nothing at all, which Harry has learned is the loudest thing she says.
  8. Harry, alone, notices that he liked it.
- **Escalation:** he is moving people's minds without consent, and it works.
- **Ending:** on what he noticed.

## Chapter 71: The Hour of His Death

- **When/where:** December 1997. Nurmengard; the Majestic.
- **POV:** Grindelwald (the main section), then Evelyn.
- **Target:** about 6,500 words.
- **Purpose:** Grindelwald's death; what he hides; the Stone revealed to Voldemort; the watch stops.
- **Beats:**
  1. **Grindelwald.** He has known for some time which hour this would be. He has seen every version of it. In most, the Dark Lord learns he has a granddaughter. In a few, he does not. He has been preparing to choose one of the few.
  2. Varga comes up the stairs to warn him and is killed on the landing. Grindelwald hears it and is sorry, in his way.
  3. Voldemort in the cell. Write their conversation as two monsters of different vintages, one young and whole, one old and tired. Voldemort wants to know why the wand does not quite answer him. Grindelwald laughs at him.
  4. Voldemort goes into his mind. Grindelwald opens **Every Hour** one last time and shows him a thousand hours of an old man's life with no granddaughter in any of them. To make the lie hold, he gives him something true in exchange: the black stone in the ring on Voldemort's own hand is the second Hallow. Voldemort looks at his hand.
  5. Grindelwald's last thought is about Isadora, and the watch, and a girl in a grey cardigan correcting his dates.
  6. **Evelyn.** The Majestic, the same moment. She is winding the watch, as every morning. It stops under her fingers. The second hand, which has not moved since it moved in the study four years ago, does not move. She knows.
  7. She tells Harry in four words. He cannot read her. He does not try. He sits with her.
- **Payoffs:** the watch reset by its maker stops with its maker. Grindelwald's foresight.
- **Escalation:** Voldemort now holds two Hallows and knows it, and wants the third.
- **Ending:** the stopped watch on the projection-room table.

## Chapter 72: Malfoy Manor

- **When/where:** January 1998. A wood in Wiltshire; the drawing room at Malfoy Manor; the cellar; Shell Cottage on the cliff at Tinworth.
- **POV:** Harry.
- **Target:** about 7,500 words.
- **Purpose:** capture, torture, Dobby, Draco disarmed.
- **Beats:**
  1. Snatchers in a wood. Harry's illusion fails: he has held too many for too long and his hold slips at the wrong moment. Taken: Harry, Evelyn, Ron, Hermione.
  2. Malfoy Manor. Lucius diminished, Narcissa afraid, Draco asked to identify Harry. Harry reads Draco: he knows exactly who it is, and he says he is not sure. Write it so that the reader cannot decide why.
  3. Bellatrix. She takes Hermione. The cellar: Harry reads Hermione's agony through the floor. It is the worst thing he has felt since the spider.
  4. Harry, in the cellar, reaches up through the floor and pushes Bellatrix's own cruelty back into her, louder, the way he did to Quirrell. She screams. He keeps going. He enjoys it. Evelyn says his name, "Potter", sharply, twice, before he stops.
  5. Dobby appears. The escape. In the drawing room, Harry wrenches Draco's wand out of his hand. (The Elder Wand's allegiance passes to Harry here. Nobody knows.) Bellatrix's knife. Dobby.
  6. Shell Cottage. Dobby's grave on the cliff. Evelyn digs it by hand, without magic, for a long time, and will not say why. Harry watches and does not help, and later cannot remember why he did not.
- **Plants:** Harry disarms Draco. Harry enjoyed Bellatrix's screaming.
- **Escalation:** he is losing the thing that made him different from Tom.
- **Ending:** the grave, finished, and Harry not feeling anything about it.

## Chapter 73: Hogsmeade

- **When/where:** February 1998. The Hog's Head and its back room; the passage to Hogwarts; Hogsmeade high street in snow; the bridge; the post office step.
- **POV:** Harry.
- **Target:** about 7,500 words.
- **Purpose:** the massacre; Lockhart's death; far gone; the Prologue from inside.
- **Beats:**
  1. The resistance at Hogwarts, led by Neville, supplied through Hogsmeade by Aberforth and the village. This world's Aberforth, who does not know Harry, and whom Harry knows. A short scene: Aberforth says Harry looks at him like he knows him. Harry says he met someone very like him once.
  2. Lockhart is in the village, running supplies with enormous flair.
  3. The Death Eaters punish Hogsmeade for it. Harry, at the Majestic, gets the coin message too late.
  4. He arrives in snow. Smoke from the Three Broomsticks. Bodies. Lockhart on the bridge, where he held it alone long enough for forty villagers to get into the passage. He died with his cloak on. It is an absurd colour.
  5. Fourteen Death Eaters still in the street, celebrating.
  6. Harry decides, quite calmly, that feeling things is a luxury for people who are not at war. He puts each of the fourteen inside his own worst night, and does not set an end to it. They stand in the snow, living it, over and over.
  7. He sits on the post office step. He finds an apple in his pocket. He takes his glove off to eat it. He watches them. He is perfectly calm. Flowers grow up through the snow around their feet because he wants them to, for no reason at all.
  8. Evelyn arrives. He looks at her and for a second there is nothing in his face at all. He does not know who she is. Then he smiles at her politely, the way he smiles at strangers in shops.
- **Payoffs:** the Prologue, exactly. Lockhart's last performance.
- **Escalation:** Harry has crossed into something he cannot see.
- **Ending:** the same moment the Prologue ended on, from Harry's side, and a line that shows he does not know who she is.

## Chapter 74: Far Gone

- **When/where:** February to March 1998. The Majestic; a dozen raids in a dozen places (a Death Eater safe house in Bradford, a Ministry warehouse, a farm in Norfolk); a holding cell under the cinema.
- **POV:** Harry, with one Evelyn scene and one Snape section.
- **Target:** about 7,500 words.
- **Purpose:** the descent at its worst, and Snape's decision.
- **Beats:**
  1. Weeks. Harry wears illusion faces constantly, a different one for each raid, and sometimes forgets to take them off at the cinema. He is the most effective weapon the resistance has. Raids succeed. Prisoners are freed.
  2. He breaks a captured Death Eater with illusions for information. It works. The man will never be right again. Harry writes down what he learned and goes to bed.
  3. He moves his friends' feelings without asking. Keeps Ron calm when Ron wants to go home to his family. Makes Hermione unafraid before a raid. Neither of them notices at first. Then Hermione notices.
  4. Ron and Hermione are frightened of him, and say so to each other, and Harry hears them, and does not mind.
  5. He avoids Evelyn. She is the only one he cannot touch and the only one who sees him as he is, and he does not like what she sees.
  6. **Evelyn scene:** she has counted. Nineteen days since he said her name. She has tried everything she knows. She writes a list of what remains. It has one item on it, and she crosses it out, because it frightens her more than anything.
  7. **Snape's section.** The headmaster's office at night. Reports of Hogsmeade, of men standing in the snow until they died of cold. Reports of a Death Eater who now speaks only to the wall. Dumbledore's portrait is asleep, or pretending. Snape remembers the instruction, word for word: *if he becomes what Tom became, you will have to stop him.* He thinks about Lily's eyes in that face. He decides.
- **Escalation:** the person Harry was is nearly gone, and the one man who might stop him has decided to.
- **Ending:** Snape writing a message for the doe to carry.

## Chapter 75: The Shrieking Shack

- **When/where:** March 1998. The Shrieking Shack.
- **POV:** Harry, then Evelyn for the ending.
- **Target:** about 7,000 words.
- **Purpose:** the trap; the duel of minds; Evelyn kills Snape.
- **Beats:**
  1. The doe asks Harry to come alone. He goes alone. He trusts Snape because of the courtyard and the doe.
  2. Evelyn follows him, because she trusts nobody, and because she has been following him for three weeks.
  3. The Shack, dusty, the same room as in third year. Snape is waiting. He is calm. Harry reads, through his closed mind, nothing at all, and that should have warned him.
  4. Snape talks for a minute. About Lily. About Dumbledore. About what Harry did at Hogsmeade. Then he goes for Harry's mind.
  5. The duel. Write it from inside: the best Occlumens alive against the best natural legilimens alive, on the floor of an empty house. Snape is not trying to read him. He is trying to break him: to shut every door in Harry's mind from inside so that Harry will never read anyone again, never cast an illusion again, and then to destroy the Cloak so the Dark Lord can never have it. Harry, far gone, is strong and has no centre. Snape is weaker and knows exactly who he is. Harry is losing.
  6. Harry, losing, sees one of Snape's memories go past: Dumbledore saying *you will have to stop him.*
  7. **Evelyn.** From the doorway. She sees Snape's wand, Potter on the floor, Potter's face going empty in a way that is not an illusion. She knows one spell that would end it at once, because she read it in the margin of the book in the Room of Requirement. *Sectumsempra.* She does not hesitate. Write it fast and plain and without gore.
  8. Snape on the floor. He looks at Harry. Silvery memory leaks from him. He says, to Harry, something short: *Look at me.* Harry looks. Snape dies looking at Lily's eyes.
- **Payoffs:** Snape's spell. Dumbledore's contingency (glimpsed).
- **Escalation:** Evelyn has killed a man.
- **Ending:** Evelyn standing in the doorway with her wand still raised, noting, from very far away, that her hand is perfectly steady.

## Chapter 76: Open

- **When/where:** the same night. The Shrieking Shack.
- **POV:** Harry, with Evelyn's viewpoint at the very start.
- **Target:** about 7,000 words.
- **Purpose:** the return. See master outline section 8.2.
- **Beats:**
  1. **Evelyn, briefly:** she has killed a man. She is shaking now. She has never shaken in her life.
  2. Harry gets up. He looks at Snape's body. He says, "Good."
  3. He collects Snape's memories in a vial because they might be useful. He does not look at Evelyn, because he cannot read her and has stopped looking at anything he cannot read.
  4. She closes the door.
  5. She says something precise about what she has just done for him, and he answers with something reasonable and dreadful.
  6. She opens her mind. For the first time in her life. Write it from Harry's side: silence for seven years, and then the loudest thing he has ever felt from anyone, louder than Hagrid on the rock. All of it at once. The killing. Her terror. Her fury at him. Her grief. What he has become, seen from outside. How much he matters to her. It is not a gentle return. He fights it, hard, the way you fight waking.
  7. Grindelwald's private line, remembered: *She will open the door for you once. Do not make her do it twice.*
  8. He comes back. He is sitting on the floor with his back to the wall. The first thing that comes back is Sirius, holding the kitchen door, and he cries for the first time since the wedding, for a long time, and she sits beside him, and her mind is still open, and he can feel that she is still frightened and still there.
  9. He realises, without saying it, that he has been living inside an illusion of himself for a month. He knows now where the door is, and that he needed someone to stand on the other side of it.
  10. She tries to close her mind again. She cannot, not fully. She tells him so, flatly. Anyone could read her now.
- **Payoffs:** Oswin's door. Grindelwald's line. "Louder than Hagrid on the rock."
- **Plants:** Evelyn cannot close.
- **Escalation:** the turn of the whole story. And a new danger: she is open.
- **Ending:** a short exchange in their own voices, dry, that shows he is back. Do not name what happened. Do not make it romantic.

## Chapter 77: The Prince's Tale

- **When/where:** late March to April 1998. The Majestic; a borrowed Pensieve (from Aberforth's back room); inside Snape's memories; the cinema foyer at night.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,500 words.
- **Purpose:** Snape's memories; Dumbledore's fear; Lucan finds them; the plan.
- **Beats:**
  1. The Pensieve. Snape's memories. Retell in new words and from Harry's reading of the emotions in them: Spinner's End, Lily, the Sorting, the word on the lake shore, the Dark Lord, the prophecy carried to him, Godric's Hollow, Dumbledore's office.
  2. Then the ones Harry does not know: Dumbledore and Snape talking about Harry over the years. Dumbledore's hope. Dumbledore's fear, growing after the Goblet year. The instruction, in full. And Snape's own doubt: he was never sure. He decided, in the end, because of Hogsmeade.
  3. Harry comes out. He reads, in himself, anger and understanding at once, as he did after the Atrium. Neither wins. Dumbledore was right to be afraid. Snape was right about Hogsmeade. And they were wrong.
  4. **Evelyn scene:** she still cannot close her mind. Ron can feel, in an ordinary way, that something about her has changed. She hates being looked at. She keeps her hand on her stopped watch all day.
  5. Night. Someone has found them. A squad at the cinema doors, led by **Lucan Selwyn**, sent by the Commission's Legilimens, Yaxley, who felt his sister's open mind across a city.
  6. Evelyn goes out to him alone. Brother and sister in the foyer of a closed cinema under a poster for a 1985 film. He is polite. He is their father's son. He has orders to bring her in. She tells him to go. He looks at her for a long time and then tells his squad the building is empty. He leaves. (Mercy, or calculation. Never resolved.) But it means the cinema is known. They must move.
  7. Harry's plan, laid out in the projection room: Voldemort holds two Hallows and wants the third. Harry has it. Voldemort's Pinnacle grows with numbers; Harry's grows with fewer. So Harry must bring him somewhere and separate him from his army. Hogwarts, where the resistance is.
- **Payoffs:** Dumbledore's fear. Snape's grief, read at last in full.
- **Escalation:** they are going to war on purpose.
- **Ending:** the plan, and Evelyn saying she will be at the door.

## Chapter 78: The Battle of Hogwarts

- **When/where:** 1 to 2 May 1998. The Hog's Head; the passage; the Room of Requirement full of students; the Great Hall; the courtyard; the bridge; the edge of the Forest; the Slytherin common room.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 9,000 words (climax, part one).
- **Purpose:** the battle; the deaths; the separation.
- **Beats:**
  1. Into Hogwarts through the Hog's Head. Neville's army. The resistance. Harry reads hundreds of terrified, brave children.
  2. Voldemort's voice over the castle: the Cloak and the boy, by midnight, or everyone dies.
  3. The Slytherins. Theo, exposed as a spy by his own side that night, is in the common room with blood on him and a choice. He fights for the castle for one hour. Millicent at Harry's side. Draco, with Narcissa's wand, wavering.
  4. Battle. Write it in fragments, as the author would: a staircase, a window, a corridor, a courtyard. Giants at the gates. Death Eaters in the Hall. Spiders.
  5. Deaths, each fast and specific: Fred, in an explosion. Lupin, in the courtyard. **Hagrid**, holding back two giants from a group of first-years on the bridge until they are across. Harry reads him go, the loudest warm thing in his life, and then nothing.
  6. **Evelyn scene:** in the entrance hall, her uncle Thaddeus aims a curse at her back. Lucan, from somewhere, steps between. He dies on the flagstones. His last words are close to: *She was supposed to be safe.* She will never know if he meant it for her. Thaddeus dies a minute later to a curse from someone Evelyn does not see.
  7. Midnight. Voldemort's army on the edge of the Forest. Harry's plan: go to him, and then make him alone.
- **Escalation:** the worst night.
- **Ending:** Harry walking toward the Forest with the Cloak over his arm, and the people who are coming with him falling in behind.

## Chapter 79: Ultimate Deceit

- **When/where:** the same night. The Forbidden Forest: a clearing, Voldemort's fire, the trees around it.
- **POV:** Harry (including inside the deceit, which he narrates as its author).
- **Target:** about 9,000 words (climax, part two).
- **Purpose:** the separation; the Pinnacle; Millicent; Voldemort's death; "Harry".
- **Beats:**
  1. The clearing. Voldemort with the Elder Wand and the ring, Death Eaters around him, his Sovereign already partly open: the forest leaning toward him.
  2. With Harry: Evelyn, Ron, Hermione, Neville, Millicent, and, arriving without explanation, Draco.
  3. **The dilemma**, faced in two lines between Harry and Evelyn: if she holds Dead Calm round his body, she cannot call him back. If she anchors him, his body has only the others to guard it. She chooses to anchor. The others will hold.
  4. **The separation.** Lockhart's lesson: not one perfect lie but a hundred bad ones, fast, for minds that are not thinking. Harry throws a forest of illusions at the Death Eaters: their master calling them to the castle, Aurors behind them, Harry running in fifty directions. They scatter. For a few minutes, Voldemort is alone in the clearing. His Sovereign thins.
  5. Harry opens **Ultimate Deceit**. On one mind. Write the opening as a change in what is real.
  6. **Inside.** Harry builds it out of everything he knows of Tom: sixteen-year-old Tom in the diary, envious; the fragment that lived in Harry for fifteen years. It is perfect because he knows its subject from the inside. Inside it, Voldemort wins. Harry is dead at his feet. Hogwarts kneels. The Cloak is in his hand. He is the Master of Death. He walks through his castle. He finds a mirror (the Mirror of Erised) and goes to look at himself immortal.
  7. **Outside**, in short cuts: the Death Eaters coming back through the trees. Ron, Hermione, Neville, Draco and Millicent holding the line around Harry's body. Millicent hit, going down, getting up, going down. Evelyn on her knees holding Harry's hand, saying his name, his surname, over and over.
  8. **Inside.** The Mirror does not show Voldemort. It shows the boy. Alive. Smiling at him politely, the way Harry smiles at strangers. Voldemort raises the Elder Wand and casts the Killing Curse at the boy in the glass.
  9. Harry has built the deceit so that the glass is Voldemort's own face, the way Quirrell's curse went to the back of his own head. In the last instant Voldemort feels something wrong and wrenches the curse aside, toward Harry's real body in the clearing. The Elder Wand will not kill its master. The curse turns back. Either way, it was always coming back to him. Voldemort dies.
  10. The deceit falls apart. Harry is inside it, alone, in a castle that is coming down, and cannot find the door.
  11. Evelyn says, "Harry." For the first time in seven years. He finds the door.
- **Payoffs:** Quirrell. The Mirror. Tom's envy. Lockhart's lesson. The diary. "Potter" to "Harry". The wand's allegiance (not yet explained).
- **Escalation:** the end of the war.
- **Ending:** Harry opening his eyes in the clearing. Millicent beside him, not moving. And silence: he cannot feel anyone. Do not explain the silence. Just let him notice it.

## Chapter 80: The Great Hall

- **When/where:** dawn, 2 to 3 May 1998. The clearing; the walk back; the Great Hall; the courtyard; the edge of the lake.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 7,000 words.
- **Purpose:** aftermath; the dead; the silence; the wand explained; the watch.
- **Beats:**
  1. Everyone Voldemort's Sovereign held is free at once: Imperiused Ministry wizards, frightened Death Eaters, children in the castle. Harry learns this from people's faces, because he cannot feel it. (Not his doing. The collapse of Dominion.)
  2. Millicent. Neville carries her. Harry walks beside them.
  3. The Great Hall: the dead in rows. Fred. Lupin. Hagrid, who needed six people to carry him. Lucan, whom nobody claims. Harry looks at the living crowd and feels nothing from any of them. They are all like Evelyn now. Write his checking, again and again, the way you keep pressing on a missing tooth. Do not explain it in words.
  4. Draco and Narcissa leaving through the doors without a word. Draco looks back once. Harry cannot tell what is in his face.
  5. Theo is gone. Nobody saw him leave.
  6. **Evelyn scene:** she works out the wand. Draco on the tower. Harry in the drawing room. She has always read everything. She tells him, in the courtyard, precisely, as though reporting an error in a register.
  7. Corvin Selwyn has fled. Marguerite is somewhere in Shropshire. Nobody knows what to do with the Selwyn name.
  8. The lake at sunrise. Harry and Evelyn. Her mind has closed again, finally, sometime in the night. It makes no difference to him any more. Everyone is silent now.
  9. He asks her what time it is. She looks at the watch, which has not worked since December, out of a lifetime's habit. She says she does not know. It is the first time he has ever heard her not know something.
- **Escalation:** the war is over and he has lost his gift.
- **Ending:** "I don't know," or the line just after it.

---

# AFTER

From here on, both characters are adults. Harry turns 18 at the end of Chapter 81. Chapters 82 and 83 are set in autumn and December 1999, when Harry is 19 and Evelyn is 20. **The romance begins in Chapter 82.** Keep it small, funny, tender, and in the author's restrained register. A first kiss and domestic closeness at most. Fade rather than describe anything further.

## Chapter 81: Funerals

- **When/where:** May to July 1998. Graveyards (Millicent's in Lincolnshire with her mother; Hagrid's at the edge of the Forest; Lockhart's, outrageously attended; Snape's, almost unattended); the Wizengamot; Grimmauld Place.
- **POV:** Harry and Evelyn, alternating.
- **Target:** about 6,500 words.
- **Purpose:** grief, trials, and the silence.
- **Beats:**
  1. Funerals. Millicent's mother, who is also big and blunt, telling Harry exactly what Millicent thought of him. Hagrid's: Grawp, centaurs, Fang. Lockhart's: three thousand mourners, fan club banners, a eulogy he wrote himself in advance and that is genuinely moving.
  2. Snape's: Harry, Evelyn, McGonagall, Slughorn, and a very old woman from Spinner's End nobody knows. Evelyn stands at the grave of the man she killed. She does not say anything. Afterwards she says one precise thing to Harry about it, and he does not try to answer it.
  3. Trials. Lucius. Narcissa, spared because Draco was in the Forest. Draco testifies, briefly, and does not look at Harry. Corvin tried in absentia. Theo's name read out and nobody there to answer it.
  4. Harry in a world gone silent. He misjudges people. A Prophet reporter he would have known for a liar at a glance prints every word he says. He mistakes Ron's grief about Fred for anger at him, and has to ask, and Ron, astonished, tells him. Harry has to ask everyone everything now. It is exhausting, and slowly, it is something else as well.
  5. **Evelyn** takes a job: junior clerk in the Office of Magical Registers, a cramped room on Level Six of the Ministry that smells of glue, under an eighty-year-old clerk who never asks about her family. She chose it because it is the least important job in the building.
  6. Grimmauld Place, which is Harry's now. His eighteenth birthday, on 31 July 1998, small. Ron, Hermione, Neville, Luna, Evelyn. Somebody tries to make Sirius's terrible cake from the recipe Sirius left in a drawer. It is just as terrible.
- **Escalation:** in scale only: a new kind of life, and a cost that is permanent.
- **Ending:** a turn at the birthday, small.

## Chapter 82: The Hour of Every World

- **When/where:** autumn 1999. Hogsmeade being rebuilt (Harry works with Aberforth, carrying stone, a job where he does not need to read anyone); the Office of Magical Registers on Level Six; the Department of Mysteries' Time Room; a Muggle café in Lamb's Conduit Street; Grimmauld Place.
- **POV:** Harry and Evelyn, alternating.
- **Target:** about 6,500 words.
- **Purpose:** the romance begins. Both are adults.
- **Beats:**
  1. Harry, nineteen, rebuilding the bridge in Hogsmeade with his hands. He likes stone. It feels nothing and so does he, toward it, and that is restful.
  2. **Evelyn**, twenty, in the cramped office with Mr Pike, correcting the birth registers of 1850 to 1860 because nobody has in a century.
  3. She takes the stopped watch to the Time Room, through an Unspeakable who owes Hermione a favour. He examines it for an hour. He says it is not broken. It is waiting. For what, he cannot say.
  4. They meet every week, as they have since the war, at a Muggle café on Lamb's Conduit Street. Same table. She orders the same thing. He has never once known what she feels, and now he does not know what anyone feels. For the first time in their lives she is not the exception. They are in the same dark.
  5. So he asks her. Directly, plainly, the way he has had to learn to ask everyone. What she feels. About him.
  6. She tells him. Precisely, flatly, with percentages if that is funny, and then, without percentages, plainly.
  7. He tells her too, in words, because that is the only way he has now.
  8. A first kiss, later, somewhere ordinary (the café doorway in the rain, or the kitchen at Grimmauld Place). Brief. In the author's register: what they do next, what she says, what he notices, not what it felt like in the body.
- **Escalation:** the one thing that was never going to happen, happening.
- **Ending:** something dry from her, immediately after. She calls him "Potter".

## Chapter 83: Potter

- **When/where:** December 1999. The Burrow on a Sunday; Grimmauld Place; the new memorial on the rebuilt bridge at Hogsmeade; the kitchen at Grimmauld Place late at night.
- **POV:** Harry, with one Evelyn scene.
- **Target:** about 6,000 words.
- **Purpose:** the last chapter. Not an epilogue. A day.
- **Beats:**
  1. Sunday lunch at the Burrow: loud, warm, too many people, Molly crying at least once. Ron and Hermione, the friends he got late, teasing him and Evelyn without mercy now that there is something to tease. Fred's absence at the table, which everyone steps around and George names out loud, once, on purpose. The noise of a family, which Harry cannot feel and can hear.
  2. Evelyn and Molly Weasley discover a shared interest in correcting other people's arithmetic.
  3. A memorial visit, short and quiet. Names. Evelyn reads all of them, as she reads everything.
  4. Grimmauld Place, late. Harry makes Sirius's terrible cake for Evelyn's sake, from the drawer recipe. She eats a slice and rates it precisely, out of ten, with reasons.
  5. He asks her what she is feeling. He asks her this most days now. She tells him: so much irritation, so much fondness, the rest unclassified. It has become their ritual. Write it so it is funny and true and does not need to be explained.
  6. **Evelyn scene**, very short: late, alone in the kitchen, winding the stopped watch out of habit, she sees the fine second hand, which has not moved since a March night in 1994, tick once. Then stop. She looks at it for a long time. She does not tell him, yet. (Leave open what it means: another world, another Evelyn, the hour of something. Do not resolve it.)
- **Ending:** a short line of Evelyn's narration, in her voice, that turns. Then `<->`.
- **Don't:** summarise the story. Don't jump years ahead. Don't marry anyone. Don't explain the watch.
