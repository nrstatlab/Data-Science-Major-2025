#!/usr/bin/env python3
"""Audit the repository's own claims and markup against what is on disk.

The other tools in this directory check that the LAB CODE is correct. This one
checks that the PROSE is correct -- that the counts the documents state match
the files that exist, that every course has its full set of notes, that no
table is malformed, and that every link resolves.

It exists because those claims drift. A repository that says "24 findings from
three documents" while holding 33 findings from four is wrong in the way that
is hardest to notice: nothing fails, nothing renders badly, and the reader has
no reason to doubt it.

Two markup checks earn their place specifically:

  * UNESCAPED PIPES IN TABLE CELLS. Writing `O(n^3 . |G|)` in a markdown table
    silently splits the cell, and the rendered page shows a truncated value
    with the bold markers left as literal asterisks. Three of those were found
    and fixed the first time this ran.
  * RAGGED ROWS. A row with fewer cells than its header renders short without
    any warning.

Run: python3 tools/audit_content.py
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
problems = []


def check(label, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'} {label}"
          f"{'' if ok else '  -- ' + detail}")
    if not ok:
        problems.append(label)


def cells(line):
    """Count table cells, ignoring pipes inside `code` and escaped pipes."""
    line = re.sub(r"`[^`]*`", "X", line)
    line = line.replace("\\|", "")
    return line.strip().strip("|").count("|") + 1


def markdown_files():
    return sorted(
        list(ROOT.glob("*.md"))
        + list(ROOT.glob("notes/**/*.md"))
        + list(ROOT.glob("labs/**/*.md")))


def main():
    pdfs = sorted(ROOT.glob("docs/*.pdf"))
    # Source files only. Counting __pycache__ made this number depend on
    # whether the suites had been run since the last clean, so the hub
    # figure it is checked against drifted every time.
    lab_files = [p for p in (ROOT / "labs").rglob("*")
                 if p.is_file() and "__pycache__" not in p.parts
                 and p.suffix != ".pyc"]
    note_dirs = sorted(p for p in ROOT.glob("notes/sem-*/*") if p.is_dir())
    unit_files = sorted(ROOT.glob("notes/sem-*/*/unit-*.md"))
    pages = sorted(list(ROOT.glob("*.html")) + list(ROOT.glob("*/*.html")))
    review = (ROOT / "SYLLABUS-REVIEW.md").read_text()
    findings = re.findall(r"^### (D\d+)", review, re.M)
    mds = markdown_files()

    print("\nGROUND TRUTH")
    for label, n in (("source PDFs", len(pdfs)),
                     ("course note directories", len(note_dirs)),
                     ("unit files", len(unit_files)),
                     ("lab files", len(lab_files)),
                     ("generated pages", len(pages)),
                     ("markdown files", len(mds)),
                     ("review findings", len(findings))):
        print(f"  {label:<26}{n}")

    # -- 1 -----------------------------------------------------------------
    print("\n1. EVERY COURSE HAS ITS FULL SET OF NOTES")
    required = (["README.md", "practice.md", "lab.md"]
                + [f"unit-{i}.md" for i in range(1, 6)])
    incomplete = []
    for d in note_dirs:
        missing = [f for f in required if not (d / f).exists()]
        if missing:
            incomplete.append(f"{d.name} missing {missing}")
    check(f"{len(note_dirs)} course directories complete", not incomplete,
          "; ".join(incomplete))

    # -- 2 -----------------------------------------------------------------
    print("\n2. REVIEW FINDINGS ARE NUMBERED CLEANLY")
    nums = [int(f[1:]) for f in findings]
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    gaps = [n for n in range(1, max(nums) + 1) if n not in nums]
    check("numbers unique", not dupes, str(dupes))
    check("numbers contiguous", not gaps, str(gaps))

    # -- 3 -----------------------------------------------------------------
    print("\n3. STATED COUNTS MATCH THE FILES")
    readme = (ROOT / "README.md").read_text()
    index = (ROOT / "index.html").read_text()
    check(f"README states {len(findings)} findings",
          f"**{len(findings)} findings**" in readme)
    check("README states four source documents",
          "four official documents" in readme)
    check(f"hub states {len(lab_files)} lab files",
          f"{len(lab_files)} lab source files" in index,
          "the hub's file count has drifted")

    # -- 4 -----------------------------------------------------------------
    print("\n4. NO ISSUING-BODY BRANDING")
    hits = subprocess.run(
        ["grep", "-rl", "APSCHE", "--include=*.md", "--include=*.py",
         "--include=*.html", "--include=*.txt", "--include=*.sh", "."],
        cwd=ROOT, capture_output=True, text=True).stdout.split()
    # this file names the string it searches for, so it always matches itself
    hits = [h for h in hits
            if "node_modules" not in h and "audit_content.py" not in h]
    check("no APSCHE reference anywhere", not hits, str(hits))

    # -- 5 -----------------------------------------------------------------
    print("\n5. EVERY DECLARED 'NOT EXECUTED' FILE SAYS SO")
    marker = "*** NOT EXECUTED ***"
    declared = []
    for runner in ROOT.glob("tools/run_*.py"):
        declared += re.findall(r'"([\w./-]+\.(?:md|sql|js|pl|R))":\s*"',
                               runner.read_text())
    silent = [str(h.relative_to(ROOT))
              for name in set(declared)
              for h in ROOT.glob(f"labs/*/{name}")
              if marker not in h.read_text()]
    check(f"{len(set(declared))} declared files carry the marker",
          not silent, str(silent))

    # -- 6 -----------------------------------------------------------------
    print("\n6. MARKDOWN TABLES ARE WELL FORMED")
    ragged = []
    for m in mds:
        lines = m.read_text().splitlines()
        for i in range(len(lines) - 1):
            head, sep = lines[i].strip(), lines[i + 1].strip()
            if not (head.startswith("|") and sep.startswith("|")):
                continue
            if not set(sep) <= set("|-: "):
                continue
            width, j = cells(head), i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                if cells(lines[j]) != width:
                    ragged.append(f"{m.relative_to(ROOT)}:{j + 1}")
                j += 1
    check(f"no ragged rows across {len(mds)} files", not ragged,
          str(ragged[:6]))

    # -- 7 -----------------------------------------------------------------
    print("\n7. LINKS RESOLVE")
    broken = []
    for p in pages:
        text = p.read_text(errors="replace")
        # href inside a code sample is documentation, not a link
        text = re.sub(r"<code>.*?</code>", "", text, flags=re.S)
        text = re.sub(r"<pre.*?</pre>", "", text, flags=re.S)
        for mo in re.finditer(r'href="([^"#?][^"]*)"', text):
            href = mo.group(1)
            if href.startswith(("http", "mailto:", "#")):
                continue
            if not (p.parent / href.split("#")[0]).resolve().exists():
                broken.append(f"{p.relative_to(ROOT)} -> {href}")
    check(f"{len(pages)} pages, every internal link resolves", not broken,
          str(broken[:5]))

    # a link to a .md file is useless on the published site: the server hands
    # the visitor raw markdown, or the browser downloads it. Every such link
    # was unlinked; this keeps them from creeping back.
    md_links = []
    for p in pages:
        text = p.read_text(errors="replace")
        text = re.sub(r"<code>.*?</code>", "", text, flags=re.S)
        text = re.sub(r"<pre.*?</pre>", "", text, flags=re.S)
        for mo in re.finditer(r'href="([^"]*\.md[^"]*)"', text):
            md_links.append(f"{p.relative_to(ROOT)} -> {mo.group(1)}")
    check("no page links to a .md file", not md_links, str(md_links[:5]))

    # a contents entry pointing at a heading that is not on the page is worse
    # than no contents at all -- the click does nothing and the reader assumes
    # the section is missing
    toc_bad, toc_n = [], 0
    for p in pages:
        h = p.read_text(errors="replace")
        if 'class="toc"' not in h:
            continue
        ids = set(re.findall(r'<h[23][^>]*id="([^"]+)"', h))
        for a in re.findall(r'<li><a href="#([^"]+)"', h):
            toc_n += 1
            if a not in ids:
                toc_bad.append(f"{p.relative_to(ROOT)} #{a}")
    check(f"{toc_n} on-page contents anchors resolve", not toc_bad,
          str(toc_bad[:5]))

    md_broken = []
    for name in ("README.md", "SYLLABUS-MAP.md", "SYLLABUS-REVIEW.md",
                 "STUDY-PLAN.md"):
        md = ROOT / name
        body = re.sub(r"```.*?```", "", md.read_text(), flags=re.S)
        for mo in re.finditer(r"\]\(([^)#][^)]*)\)", body):
            href = mo.group(1)
            if href.startswith(("http", "mailto:", "#")):
                continue
            if not (md.parent / href.split("#")[0]).resolve().exists():
                md_broken.append(f"{name} -> {href}")
    check("top-level markdown links resolve", not md_broken,
          str(md_broken[:5]))

    # the notes point at lab files constantly; a renamed lab silently breaks
    # every reference to it, and nothing else in this repository would notice
    note_broken, n_links = [], 0
    for md in ROOT.glob("notes/**/*.md"):
        body = re.sub(r"```.*?```", "", md.read_text(), flags=re.S)
        for mo in re.finditer(r"\]\((\.\./[^)#]*)\)", body):
            href = mo.group(1)
            n_links += 1
            if not (md.parent / href.split("#")[0]).resolve().exists():
                note_broken.append(f"{md.relative_to(ROOT)} -> {href}")
    check(f"{n_links} note-to-lab cross-references resolve", not note_broken,
          str(note_broken[:5]))

    # -- 8 -----------------------------------------------------------------
    print("\n8. WHITESPACE HYGIENE")
    tabs = [str(m.relative_to(ROOT)) for m in mds if "\t" in m.read_text()]
    check("no tabs in markdown", not tabs, str(tabs[:4]))
    trailing = [str(m.relative_to(ROOT)) for m in mds
                if any(ln.rstrip() != ln and ln.strip() and not ln.endswith("  ")
                       for ln in m.read_text().splitlines())]
    check("no stray trailing whitespace", not trailing, str(trailing[:4]))

    print("\n" + "=" * 62)
    print(f"{len(problems)} PROBLEM(S)" if problems else "AUDIT CLEAN")
    print("=" * 62)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
