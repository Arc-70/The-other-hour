#!/usr/bin/env python3
"""fictools.py: helper for writing The Other Hour in File Mode.

Commands (run from the folder that holds the manuscript):
  python3 fictools.py status                 where the story is up to, and the next book
  python3 fictools.py check drafts/ch07.md   check a draft chapter against the style rules
  python3 fictools.py append drafts/ch07.md  add a checked draft to the manuscript (in order)
  python3 fictools.py append drafts/ch07.md --replace   replace a chapter already in it
  python3 fictools.py epub                   rebuild The_Other_Hour.epub from the manuscript

No third-party packages needed.
"""
import argparse, datetime, html, os, re, sys, uuid, zipfile
from collections import Counter

MANUSCRIPT = "The_Other_Hour.md"
EPUB = "The_Other_Hour.epub"
TITLE = "The Other Hour"
SUBTITLE = "A Harry Potter Fanfiction"
LAST_CHAPTER = 83

# Eight books, one per turn of File Mode. 0 is the Prologue.
BOOKS = [
    (1, "Year One", [0] + list(range(1, 11))),
    (2, "Year Two", list(range(11, 21))),
    (3, "Year Three", list(range(21, 34))),
    (4, "Year Four", list(range(34, 46))),
    (5, "Year Five", list(range(46, 57))),
    (6, "Year Six", list(range(57, 68))),
    (7, "Year Seven, part one", list(range(68, 78))),
    (8, "Year Seven, part two, and After", list(range(78, 84))),
]

HEAD_RE = re.compile(r"^##\s+(Prologue|Chapter\s+(\d+))\s*:\s*(.+?)\s*$", re.M)

BANNED = [
    r"a testament to", r"tapestry", r"\bdelve", r"palpable",
    r"the weight of (it all|everything|the world|what|his words|her words|the silence|the moment|the news|his gaze|her gaze)",
    r"something shifted", r"\ba beat\b", r"breath (he|she|they) didn'?t know", r"the silence stretched",
    r"ghost of a smile", r"eyes that held", r"\bin that moment\b", r"for the first time in a long time",
    r"electric(ity)? (in the air|between them)", r"crackled with (electricity|tension)", r"\bozone\b",
    r"(taste|smell|tang) of copper", r"\bcoppery\b", r"\bunspoken\b", r"storm of emotions",
    r"every fib(re|er) of", r"whether to laugh or cry",
]
BODY = [
    r"chest (tightened|tight|constricted|ached|squeezed)", r"throat (tightened|closed|tight|ached|thickened)",
    r"stomach (dropped|lurched|twisted|knotted|turned|churned|clenched|flipped|sank)",
    r"breath (caught|hitched|stuttered)", r"heart (hammered|pounded|raced|skipped|lurched|clenched|ached|thudded|stuttered|leapt|sank)",
    r"pulse (quickened|raced|jumped|spiked)", r"blood ran cold", r"(skin|scalp|neck|spine) (prickled|tingled)",
    r"shiver (ran|went|crawled) (down|up)", r"a (wave|surge|rush) of \w+ (washed|swept|crashed|flooded)",
    r"knot in (his|her|their) (stomach|chest)", r"lump in (his|her|their) throat",
]
CAPPED = [
    (r"\b(it|this|that) (wasn'?t|was not) [^.!?]{1,60}[.!?]\s+(it|this|that) was\b", "'It wasn't X. It was Y.'"),
    (r"\bsomehow\b", "'somehow'"), (r"\bimpossibly\b", "'impossibly'"),
]
AVOID = [(r"\bsmirk", "smirking (avoid)"), (r"\bpadded\b", "'padded' (avoid)"), (r"eyes darken", "eyes darkening (avoid)"),
         (r"\bas if\b", "'as if' (the author writes 'as though')")]
ROMANCE = [r"\bkiss(ed|es|ing)?\b", r"\bcrush\b", r"\bin love\b", r"\bromantic", r"\bflirt", r"\bdate\b with"]


def ch_id(match):
    return 0 if match.group(1).startswith("Prologue") else int(match.group(2))


def ch_label(n):
    return "Prologue" if n == 0 else f"Chapter {n}"


def book_of(n):
    for b, name, chs in BOOKS:
        if n in chs:
            return b, name, chs
    return None


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def split_chapters(text):
    heads = list(HEAD_RE.finditer(text))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.append((ch_id(m), m.group(3), m.start(), end))
    return out


# ---------- check ----------
def check(path):
    text = read(path)
    fails, warns = [], []
    heads = list(HEAD_RE.finditer(text))
    if len(heads) != 1:
        fails.append(f"draft must contain exactly one chapter heading (found {len(heads)}). Format: '## Chapter 7: Title' or '## Prologue: Title'")
        n = None
    else:
        n = ch_id(heads[0])
    body = HEAD_RE.sub("", text).strip()
    if not body.rstrip().endswith("<->"):
        fails.append("chapter must end with a line containing only <->")
    body = body.replace("<->", "")
    words = len(body.split())
    lo, hi, hard = (2500, 5000, 1500) if n == 0 else (5000, 9500, 3000)
    if words < hard:
        fails.append(f"only {words} words: far too short")
    elif words < lo or words > hi:
        warns.append(f"{words} words (target {'3,000 to 4,500' if n == 0 else '5,500 to 7,000, climaxes up to 9,000'})")

    d = body.count("—") + body.count("–")
    if d:
        fails.append(f"{d} em/en dashes. Must be zero")
    if re.search(r"\w--\w|\s--\s", body):
        fails.append("double-hyphen dash found. Must be zero")
    semi = body.count(";")
    if semi > 1:
        warns.append(f"{semi} semicolons (the author uses almost none)")

    low = body.lower()
    for pat in BANNED:
        hits = re.findall(pat, low)
        if hits:
            fails.append(f"banned phrase /{pat}/ x{len(hits)}")
    body_hits = []
    for pat in BODY:
        body_hits += [m.group(0) for m in re.finditer(pat, low)]
    if len(body_hits) > 1:
        fails.append(f"{len(body_hits)} body-sensation emotion phrases (max 1): {', '.join(body_hits[:8])}")
    for pat, label in CAPPED:
        c = len(re.findall(pat, low))
        if c > 1:
            warns.append(f"{label} used {c} times (max 1)")
    for pat, label in AVOID:
        c = len(re.findall(pat, low))
        if c:
            warns.append(f"{label} x{c}")
    c = low.count("for a long moment")
    if c > 4:
        warns.append(f"'for a long moment' x{c} (max 4)")
    c = len(re.findall(r"\bfor a moment\b", low))
    if c > 8:
        warns.append(f"'for a moment' x{c} (max 8)")

    # dialogue share and narration contractions
    quotes = re.findall(r"[\"“]([^\"”]*)[\"”]", body)
    dw = sum(len(q.split()) for q in quotes)
    share = 100 * dw / max(words, 1)
    if n != 0 and (share < 10 or share > 45):
        warns.append(f"dialogue share {share:.0f}% (the author's chapters run 8 to 41%, usually 20 to 35%)")
    narr = re.sub(r"[\"“][^\"”]*[\"”]", " ", body)
    nw = max(len(narr.split()), 1)
    nt = len(re.findall(r"\b\w+n['’]t\b", narr, re.I))
    rate = 1000 * nt / nw
    if rate > 5:
        fails.append(f"{nt} n't contractions in narration ({rate:.1f} per 1,000 words). Narration says 'did not', 'could not'")
    elif rate > 2:
        warns.append(f"{nt} n't contractions in narration ({rate:.1f} per 1,000). The author's rate is under 1")

    paras = [p.strip() for p in body.split("\n\n") if p.strip() and p.strip() != "* * *"]
    if paras:
        short = 100 * sum(1 for p in paras if len(p.split()) <= 8) / len(paras)
        if short < 35:
            warns.append(f"only {short:.0f}% of paragraphs are 8 words or fewer (the author's run 42 to 54%)")
        sents = [len(s.split()) for s in re.split(r"(?<=[.!?…])\s+", " ".join(paras)) if s.split()]
        med = sorted(sents)[len(sents) // 2]
        if med > 11:
            warns.append(f"median sentence {med} words (the author's is 6 to 10)")

    # Evelyn is plain
    for s in re.split(r"(?<=[.!?])\s+", body):
        if "Evelyn" in s and re.search(r"\b(pretty|beautiful|gorgeous|lovely face|striking)\b", s, re.I):
            warns.append(f"Evelyn described as attractive? -> {s[:120]}")
    # romance boundary
    if n is not None and n < 82:
        for pat in ROMANCE:
            for m in re.finditer(pat, low):
                ctx = low[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")
                warns.append(f"romance word before Chapter 82, check it is not about Harry and Evelyn: ...{ctx}...")

    # repeated phrases inside the chapter
    toks = re.findall(r"[a-z']+", low)
    grams = Counter(" ".join(toks[i:i + 4]) for i in range(len(toks) - 3))
    stop = {"he did not know", "she did not know", "did not know what", "for a long moment", "at the same time"}
    reps = [(g, c) for g, c in grams.most_common(40) if c >= 4 and g not in stop]
    if reps:
        warns.append("repeated 4-word phrases: " + "; ".join(f"'{g}' x{c}" for g, c in reps[:6]))

    label = ch_label(n) if n is not None else "draft"
    print(f"CHECK {label}: {words} words, dialogue {share:.0f}%")
    for f in fails:
        print("  FAIL ", f)
    for w in warns:
        print("  WARN ", w)
    if not fails and not warns:
        print("  PASS  no problems found")
    elif not fails:
        print("  PASS  with warnings: fix any that are real problems")
    return 1 if fails else 0


# ---------- append ----------
def append(path, replace=False, force=False, manuscript=MANUSCRIPT):
    draft = read(path).strip() + "\n"
    heads = list(HEAD_RE.finditer(draft))
    if len(heads) != 1:
        print("FAIL: draft must contain exactly one chapter heading.")
        return 1
    n = ch_id(heads[0])
    if not os.path.exists(manuscript):
        with open(manuscript, "w", encoding="utf-8") as f:
            f.write(f"# {TITLE}\n\n*{SUBTITLE}*\n")
    text = read(manuscript)
    chs = split_chapters(text)
    present = [c[0] for c in chs]
    if n in present:
        if not replace:
            print(f"REFUSED: {ch_label(n)} is already in the manuscript. Use --replace to rewrite it.")
            return 1
        _, _, s, e = chs[present.index(n)]
        text = text[:s] + draft + "\n" + text[e:].lstrip("\n")
        with open(manuscript, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Replaced {ch_label(n)}.")
        return 0
    expected = (max(present) + 1) if present else 0
    if n != expected and not force:
        print(f"REFUSED: next chapter in order is {ch_label(expected)}, draft is {ch_label(n)}. Use --force only if you mean it.")
        return 1
    with open(manuscript, "a", encoding="utf-8") as f:
        f.write("\n" + draft)
    print(f"Appended {ch_label(n)}. Manuscript now {len(read(manuscript).split()):,} words.")
    return 0


# ---------- status ----------
def status(manuscript=MANUSCRIPT):
    if not os.path.exists(manuscript):
        print("No manuscript yet. Next: Prologue (Book 1: Year One, Prologue to Chapter 10).")
        return 0
    text = read(manuscript)
    chs = split_chapters(text)
    present = [c[0] for c in chs]
    words = len(text.split())
    print(f"Manuscript: {len(present)} of 84 parts, {words:,} words.")
    gaps = [ch_label(i) for i in range(0, max(present) + 1) if i not in present] if present else []
    if gaps:
        print("Missing (gaps): " + ", ".join(gaps))
    nxt = (max(present) + 1) if present else 0
    if nxt > LAST_CHAPTER:
        print("The story is complete.")
        return 0
    b, name, rng = book_of(nxt)
    done = [c for c in rng if c in present]
    print(f"Next: {ch_label(nxt)}. It belongs to Book {b} ({name}): {ch_label(rng[0])} to {ch_label(rng[-1])}. "
          f"{len(done)} of {len(rng)} of that book already written.")
    return 0


# ---------- epub ----------
def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"<em>\1</em>", s)
    return s


def xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en-GB" xml:lang="en-GB">\n'
            f'<head><meta charset="utf-8"/><title>{html.escape(title)}</title>'
            '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
            f'<body>\n{body}\n</body>\n</html>\n')


def epub(manuscript=MANUSCRIPT, out=EPUB):
    if not os.path.exists(manuscript):
        print("No manuscript to build from.")
        return 1
    text = read(manuscript)
    chs = split_chapters(text)
    if not chs:
        print("No chapters found.")
        return 1
    items = []
    for i, (n, title, s, e) in enumerate(chs):
        section = text[s:e]
        lines = section.split("\n", 1)
        heading = HEAD_RE.match(lines[0]).group(0).lstrip("#").strip()
        rest = lines[1] if len(lines) > 1 else ""
        paras = []
        for p in re.split(r"\n\s*\n", rest):
            p = p.strip()
            if not p or p == "<->":
                continue
            if p in ("* * *", "***", "*  *  *"):
                paras.append('<p class="break">* * *</p>')
                continue
            p = p.replace("<->", "").strip()
            paras.append("<p>" + md_inline(" ".join(p.split("\n"))) + "</p>")
        body = f'<section epub:type="chapter"><h2>{html.escape(heading)}</h2>\n' + "\n".join(paras) + "</section>"
        items.append((f"ch{i:03d}.xhtml", heading, xhtml(heading, body)))

    uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "the-other-hour"))
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    title_page = xhtml(TITLE, f'<section class="title"><h1>{TITLE}</h1><p class="sub">{SUBTITLE}</p></section>')
    nav = xhtml("Contents", '<nav epub:type="toc" id="toc"><h2>Contents</h2><ol>\n' +
                "\n".join(f'<li><a href="{f}">{html.escape(h)}</a></li>' for f, h, _ in items) + "\n</ol></nav>")
    manifest = ['<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>',
                '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="style.css" media-type="text/css"/>']
    manifest += [f'<item id="c{i}" href="{f}" media-type="application/xhtml+xml"/>' for i, (f, _, _) in enumerate(items)]
    spine = ['<itemref idref="title"/>', '<itemref idref="nav"/>'] + [f'<itemref idref="c{i}"/>' for i in range(len(items))]
    opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en-GB">\n'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
           f'<dc:identifier id="bookid">{uid}</dc:identifier>\n<dc:title>{TITLE}</dc:title>\n'
           f'<dc:language>en-GB</dc:language>\n<meta property="dcterms:modified">{now}</meta>\n</metadata>\n'
           '<manifest>\n' + "\n".join(manifest) + '\n</manifest>\n<spine toc="ncx">\n' + "\n".join(spine) + '\n</spine>\n</package>\n')
    ncx = ('<?xml version="1.0" encoding="utf-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
           f'<head><meta name="dtb:uid" content="{uid}"/></head><docTitle><text>{TITLE}</text></docTitle><navMap>\n' +
           "\n".join(f'<navPoint id="n{i}" playOrder="{i + 1}"><navLabel><text>{html.escape(h)}</text></navLabel><content src="{f}"/></navPoint>'
                     for i, (f, h, _) in enumerate(items)) + '\n</navMap></ncx>\n')
    css = ("body{font-family:Georgia,serif;line-height:1.5;margin:0 5%;}h1{text-align:center;margin-top:30%;}"
           "h2{text-align:center;margin:2em 0 1.5em;font-weight:normal;}p{margin:0 0 .8em;}"
           "p.break{text-align:center;margin:1.5em 0;}p.sub{text-align:center;font-style:italic;}")
    container = ('<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>\n')
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/title.xhtml", title_page, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", css, compress_type=zipfile.ZIP_DEFLATED)
        for f, _, x in items:
            z.writestr("OEBPS/" + f, x, compress_type=zipfile.ZIP_DEFLATED)
    print(f"Built {out}: {len(items)} chapters, {len(text.split()):,} words.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    c = sub.add_parser("check"); c.add_argument("draft")
    a = sub.add_parser("append"); a.add_argument("draft"); a.add_argument("--replace", action="store_true"); a.add_argument("--force", action="store_true")
    sub.add_parser("epub")
    args = ap.parse_args()
    if args.cmd == "status":
        sys.exit(status())
    if args.cmd == "check":
        sys.exit(check(args.draft))
    if args.cmd == "append":
        sys.exit(append(args.draft, args.replace, args.force))
    if args.cmd == "epub":
        sys.exit(epub())


if __name__ == "__main__":
    main()
