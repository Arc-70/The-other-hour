# 00 · START HERE

*This file has no spoilers. It's the only one you need to read.*

**The Other Hour** (working title, rename it whenever you like) is planned as a Prologue plus 83 chapters, about 500,000 words, running from the summer of 1991 to 1999. Everything else in this folder is for the writing chat.

## What's in the folder

| File | Safe for you to open? |
|---|---|
| `00_START_HERE.md` | Yes (you're reading it) |
| `01_WRITER_INSTRUCTIONS.md` | Yes. How the writing chat behaves. No plot |
| `02_STYLE_GUIDE.md` | Yes. Your own style, measured from *All the Time in the World* |
| `03_CRAFT_RULES.md` | Yes. The paper's findings turned into rules |
| `fictools.py` | Yes. A small helper the writer uses to check chapters and build the ebook |
| `SPOILERS_04` to `SPOILERS_10` | **No.** The whole story, chapter by chapter |
| `THE_OTHER_HOUR_COMPLETE.md` | **No** past its first screen. Files 01 to 10 merged into one |
| `99_STORY_SO_FAR.md` | Yes. Only what has already been written |

---

## The way you asked for: one book file, written in eight turns

The writer keeps the whole story in one growing file, `The_Other_Hour.md`, like your own book, plus an ebook copy (`The_Other_Hour.epub`) you can open on a phone or e-reader. Each turn it writes one "book" (roughly one school year) from start to finish, checks every chapter, adds it to the file, and hands you the updated files at the end.

| Turn | Book | Chapters |
|---|---|---|
| 1 | Year One | Prologue to 10 |
| 2 | Year Two | 11 to 20 |
| 3 | Year Three | 21 to 33 |
| 4 | Year Four | 34 to 45 |
| 5 | Year Five | 46 to 56 |
| 6 | Year Six | 57 to 67 |
| 7 | Year Seven, part one | 68 to 77 |
| 8 | Year Seven, part two, and After | 78 to 83 |

This needs a session that can work with files (like this one), not a plain chat. Use the highest effort setting.

### Turn 1: the starting prompt

Start a new session, attach `The_Other_Hour_files.zip`, and send:

```
You are writing The Other Hour. I've attached The_Other_Hour_files.zip. Unzip it into your working folder and follow 01_WRITER_INSTRUCTIONS.md exactly, using File Mode.

This turn, write Book 1: the Prologue and Chapters 1 to 10. Every chapter at full length, in the voice of 02_STYLE_GUIDE.md. Check each one with fictools.py and fix what it finds, append it to The_Other_Hour.md, and add its handoff block to 99_STORY_SO_FAR.md. Reread the style guide and the end of the manuscript before every chapter. Don't ask me anything, and don't put any chapter text, titles or plot in the chat. When all of Book 1 is done, build the epub, send me The_Other_Hour.md, The_Other_Hour.epub and 99_STORY_SO_FAR.md, and stop.
```

### Turns 2 to 8: the continuing prompt (same session)

```
Continue The Other Hour in File Mode. Run python3 fictools.py status to see where you are, then write the next book in full, following 01_WRITER_INSTRUCTIONS.md exactly. Before you start, reread 02_STYLE_GUIDE.md and the last part of the manuscript, and keep rereading before every chapter. Same rules as before: full-length chapters, check each one and fix what it finds, append it, log it, no questions, and no chapter text, titles or plot in the chat. When the book is done, rebuild the epub, send me the three files, and stop.
```

### Turns 2 to 8: the continuing prompt (new session)

Use this if the old session is gone, or if quality seems to be slipping and you want a fresh start. Attach `The_Other_Hour_files.zip` **and** your latest `The_Other_Hour.md` and `99_STORY_SO_FAR.md`, and send:

```
Continue The Other Hour in File Mode. I've attached The_Other_Hour_files.zip plus my latest The_Other_Hour.md and 99_STORY_SO_FAR.md. Unzip the zip into your working folder, then put my attached manuscript and log in the same folder, replacing the empty log from the zip. Run python3 fictools.py status to see where you are, then write the next book in full, following 01_WRITER_INSTRUCTIONS.md exactly. Before you start, reread 02_STYLE_GUIDE.md and the last part of the manuscript, and keep rereading before every chapter. Full-length chapters, check each one and fix what it finds, append it, log it, no questions, and no chapter text, titles or plot in the chat. When the book is done, rebuild the epub, send me the three files, and stop.
```

### If you come back too early

Every chapter is saved to the file the moment it's finished, so nothing is lost. If the session is still working, its progress list shows how far it has got (by chapter number only). It's safest not to send anything until it says the book is done. If you do interrupt it, just send the continuing prompt. It will finish the book it was on before starting the next one.

---

## The other way: one chapter at a time in a normal chat

1. Start a new chat. Attach `THE_OTHER_HOUR_COMPLETE.md` and `99_STORY_SO_FAR.md`.
2. Paste the contents of `01_WRITER_INSTRUCTIONS.md` as the instructions (or tell it "Follow 01_WRITER_INSTRUCTIONS.md").
3. Say **"Write the Prologue."** Then **"Next chapter"** each time.
4. After each chapter, copy the `handoff` block to the bottom of `99_STORY_SO_FAR.md` and save. It only contains what you've just read.
5. Start a fresh chat every chapter or two with the updated `99` attached.

---

## Steering (either way)

You can say anything: "more banter", "this dragged", "longer fight scenes", "more Evelyn chapters", "rewrite Chapter 12, the ending was flat". The writer applies it from then on. If you ask for something that changes the plan, it will do it and record the change so later chapters stay consistent. "What happens next?" gets you "you'll have to read it".

## What's different from what you first asked for

- **The romance comes after the war**, once they're both adults, as we agreed. Before that it's friendship and trust, and that's still the spine of the story.
- **Year 7 is included**, so the plan is longer than 300k.
- **Evelyn's surname is Selwyn.** She's adapted from your Evelyn, with her own history here. If you'd rather a different name, say so in your first message.

## If quality slips

- "Reread the style guide in full and rewrite Chapter N in that voice."
- "Too many body sensations. Follow Rule 3."
- "That chapter ended on a summary. End on a turn."
- "Nothing got worse in that chapter. Follow Rule 1."
- "Run fictools.py check on every chapter of the last book and fix what it finds."
