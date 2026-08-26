#!/usr/bin/env python3
"""Generate the study-material website from the Markdown notes.

House style is adopted from nrstatlab/Statistics-Major: the same
css/styles.css, the same .banner/.crumbs header, .chips topic row,
.unit-card grids, .page-nav footer navigation and MathJax loading, so the
two sites read as one family.

Markdown stays the source of truth. The notes remain readable on github.com
and the verification tooling (tools/verify_all.sh, tools/check_coverage.py)
keeps operating on them; this script only renders them.

Usage:
    pip install markdown
    python3 tools/build_site.py

Writes .html files next to nothing -- into per-course directories at the
repository root, mirroring the Statistics-Major layout:

    index.html                     course hub
    css/styles.css                 shared stylesheet
    <course-slug>/index_<slug>.html
    <course-slug>/unit1_<slug>.html ... unit5_<slug>.html
    <course-slug>/practice_<slug>.html, lab_<slug>.html
    syllabus-review.html, syllabus-map.html, study-plan.html
"""

import html
import pathlib
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("markdown is required:  pip install markdown")

ROOT = pathlib.Path(__file__).resolve().parent.parent

MATHJAX = ('<script id="MathJax-script" async '
           'src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">'
           '</script>')

MERMAID = """<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  document.querySelectorAll('pre > code.language-mermaid').forEach((code) => {
    const holder = document.createElement('pre');
    holder.className = 'mermaid';
    holder.textContent = code.textContent;
    code.closest('pre').replaceWith(holder);
  });
  mermaid.initialize({ startOnLoad: true, securityLevel: 'strict',
                       flowchart: { useMaxWidth: true }, er: { useMaxWidth: true } });
</script>"""

# --------------------------------------------------------------------------
# Course definitions -- order matches the syllabus, not the filesystem.
# --------------------------------------------------------------------------

COURSES = [
    {
        "slug": "computer-fundamentals",
        "src": "notes/sem-1/course-1-computer-fundamentals",
        "number": 1, "year": "I", "sem": "I",
        "title": "Computer Fundamentals and Office Automation",
        "tagline": "Number systems, computer organization, networking, "
                   "word processing, spreadsheets and dashboards.",
        "blurb": "5 Units + Lab • Number systems, memory hierarchy, networks, "
                 "Word, Excel, pivot tables and dashboards.",
        "units": [
            ("Number Systems, Evolution, Block Diagram and Generations",
             "Binary, octal, hexadecimal and conversions; evolution of computers; "
             "block diagram; five generations."),
            ("Basic Organization and Networking Fundamentals",
             "Functional components, memory hierarchy, types of computers; LAN, WAN, "
             "MAN; star, ring and bus topologies; Internet basics."),
            ("Word Processing and Presentations",
             "Formatting, styles, tables, mail merge; slide design, animations, "
             "transitions; keyboard shortcuts."),
            ("Spreadsheet Basics",
             "Cell referencing, SUM/AVERAGE/IF/COUNT, charts, text functions, "
             "VLOOKUP, HLOOKUP, XLOOKUP, INDEX and MATCH."),
            ("Data Analysis and Visualization",
             "Conditional formatting, pivot tables, data validation, Goal Seek, "
             "Scenario Manager, dashboards, slicers and sparklines."),
        ],
    },
    {
        "slug": "problem-solving-c",
        "src": "notes/sem-1/course-2-problem-solving-c",
        "number": 2, "year": "I", "sem": "I",
        "title": "Problem Solving Using C",
        "tagline": "Structured programming, control flow, arrays, pointers, "
                   "dynamic memory and file handling.",
        "blurb": "5 Units + Lab • Control flow, arrays, strings, pointers, "
                 "structures, unions and file handling. 15 runnable programs.",
        "units": [
            ("Introduction to Computer Programming",
             "Types of software, compiler vs interpreter, algorithms and flowcharts; "
             "C tokens, data types, operators and I/O."),
            ("Control Statements",
             "if, if-else, else-if ladder, switch; while, for, do-while; "
             "break, continue and goto."),
            ("Derived Data Types: Arrays and Strings",
             "One- and two-dimensional arrays, memory representation, row-major "
             "order; strings and string handling functions."),
            ("Pointers, Functions and Storage Classes",
             "Pointers and pointer arithmetic; functions, recursion, call by value "
             "and by address; auto, extern, static and register."),
            ("Dynamic Memory, Structures, Unions and Files",
             "malloc, calloc, realloc, free; structures and unions; "
             "text file operations."),
        ],
    },
    {
        "slug": "python-data-structures",
        "src": "notes/sem-2/course-3-python-data-structures",
        "number": 3, "year": "I", "sem": "II",
        "title": "Python Programming and Data Structures",
        "tagline": "Python fundamentals, collections, file handling, "
                   "object-oriented programming and abstract data structures.",
        "blurb": "5 Units + Lab • Syntax, collections, files, exceptions, OOP, "
                 "linked lists, stacks, queues and Tkinter. 18 runnable programs.",
        "units": [
            ("Basics of Python Programming",
             "Features, programming modes, identifiers, literals, built-in types, "
             "operators and precedence."),
            ("Control Flow, Functions and Modules",
             "if-elif-else, loops, for…else; functions, argument types, scope, "
             "recursion, lambda; modules and namespaces."),
            ("Sequences, Sets and Mapping Types",
             "Strings, lists, tuples, sets and dictionaries; slicing, mutability "
             "and comprehensions."),
            ("File Handling, Exception Handling and OOP",
             "Files and CSV; try-except-else-finally; classes, constructors, "
             "encapsulation, inheritance and overriding."),
            ("Abstract Data Structures and GUI Programming",
             "Linked lists, stacks, queues, priority queues; Tkinter widgets "
             "and event handling."),
        ],
    },
    {
        "slug": "statistical-foundations",
        "src": "notes/sem-2/course-4-statistical-foundations",
        "number": 4, "year": "I", "sem": "II",
        "title": "Statistical Foundations for Data Science",
        "tagline": "Probability, random variables, distributions, regression "
                   "and statistical inference.",
        "blurb": "5 Units + Lab • Probability, distributions, correlation, "
                 "regression, estimation and hypothesis testing. Formula sheet included.",
        "units": [
            ("Fundamentals of Probability and Basic Statistics",
             "Axioms and rules of probability, conditional probability and Bayes' "
             "theorem; central tendency, dispersion, correlation and covariance."),
            ("Random Variables, Expectation and Variance",
             "Discrete and continuous random variables, PMF, PDF and CDF; "
             "expectation, variance, moments and the MGF."),
            ("Probability Distributions",
             "Binomial, Poisson, geometric, negative binomial; uniform, normal, "
             "exponential, gamma; joint distributions and the Central Limit Theorem."),
            ("Correlation and Regression",
             "Bivariate data, Pearson and Spearman correlation; simple linear "
             "regression, ANOVA, residuals and goodness of fit."),
            ("Statistical Inference, Estimation and Hypothesis Testing",
             "Sampling distributions, confidence intervals; z, t, chi-square and "
             "F tests; p-values, Type I and II errors and power."),
        ],
    },
    {
        "slug": "dbms",
        "src": "notes/sem-3/course-5-dbms",
        "number": 5, "year": "II", "sem": "III",
        "title": "Database Management Systems",
        "tagline": "Database design, the relational model, normalization, "
                   "SQL and PL/SQL.",
        "blurb": "5 Units + Lab • Three-schema architecture, ER modelling, "
                 "normalization to 3NF, SQL joins and PL/SQL. Executable SQL labs.",
        "units": [
            ("Overview of Database Management Systems",
             "Data and information, file-based systems and their drawbacks; the "
             "database approach, data models and the three-schema architecture."),
            ("The Entity-Relationship Model",
             "ER building blocks, entity and attribute classification, cardinality; "
             "reducing ER diagrams to tables; the EER model."),
            ("The Relational Model and Normalization",
             "Codd's rules, keys, integrity constraints, relational algebra; "
             "functional dependencies and normal forms to 3NF and BCNF."),
            ("Structured Query Language",
             "DDL, DML and DQL; aggregates, GROUP BY and HAVING; joins, set "
             "operations, subqueries and views."),
            ("PL/SQL and Triggers",
             "Block structure, control structures, cursors and exceptions; "
             "procedures, functions and database triggers."),
        ],
    },
]

EXTRA_PAGES = {
    "practice.md": ("practice", "PRACTICE",
                    "Exam-style questions with fully worked solutions."),
    "lab.md": ("lab", "LAB",
               "Every prescribed lab experiment, with code and expected output."),
    "formula-sheet.md": ("formula-sheet", "REFERENCE",
                         "Every formula from the five units on one page for revision."),
}

TOP_PAGES = [
    ("SYLLABUS-REVIEW.md", "syllabus-review", "Syllabus Review",
     "Eleven findings from checking the official APSCHE document."),
    ("SYLLABUS-MAP.md", "syllabus-map", "Syllabus Map",
     "Programme structure for Semesters I–VI, elective tracks and unit topics."),
    ("STUDY-PLAN.md", "study-plan", "Study Plan",
     "Week-by-week schedule, revision cycles and a progress checklist."),
]


# --------------------------------------------------------------------------
# Markdown -> HTML
# --------------------------------------------------------------------------

def render_markdown(text):
    """Convert Markdown to HTML with the extensions the notes rely on."""
    md = markdown.Markdown(extensions=[
        "tables", "fenced_code", "sane_lists", "attr_list", "md_in_html",
    ])
    return md.convert(text)


def strip_first_heading(text):
    """Remove the leading '# Title' so it is not repeated under the banner."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return line[2:].strip(), "\n".join(lines[i + 1:])
    return None, text


GITHUB_BLOB = ("https://github.com/nrstatlab/Data-Science-Major-2025/blob/main/")


def rewrite_links(body, link_map, src_dir, out_dir):
    """Retarget the Markdown's relative links for the generated page.

    Three cases:
      * a .md file that becomes a page   -> its generated .html sibling
      * any other repo file (lab source, -> re-relativised, because the source
        the syllabus PDF)                   .md sits deeper in notes/ than the
                                            generated page does
      * a .md file with no page           -> the file on github.com
    """
    def repl(m):
        label, target, frag = m.group(1), m.group(2), m.group(3) or ""

        key = pathlib.PurePosixPath(target).name
        if key in link_map:
            return f'[{label}]({link_map[key]}{frag})'

        # Resolve against the SOURCE directory to get a repo-relative path,
        # then re-relativise from the OUTPUT directory. Without this a link
        # written as ../../../labs/... from notes/sem-1/course-2-x/ keeps a
        # depth that is wrong for a page living one level down.
        resolved = (src_dir / target).resolve()
        try:
            rel_to_root = resolved.relative_to(ROOT)
        except ValueError:
            return m.group(0)

        if resolved.exists():
            import os
            new_target = os.path.relpath(resolved, out_dir).replace("\\", "/")
            return f'[{label}]({new_target}{frag})'

        if target.endswith(".md"):
            return f'[{label}]({GITHUB_BLOB}{rel_to_root}{frag})'
        return m.group(0)

    return re.sub(r'\[([^\]]*)\]\(([^)#\s]+)(#[^)\s]*)?\)', repl, body)


def promote_boxes(html_text):
    """Map Markdown constructs onto the house style's semantic boxes."""
    # Blockquotes carrying the off-syllabus warnings become .warn; the rest
    # become .tip, matching how Statistics-Major uses those classes.
    def blockquote(m):
        inner = m.group(1)
        warn = ("⚠" in inner or "examined but" in inner.lower()
                or "not in the syllabus" in inner.lower())
        cls = "warn" if warn else "tip"
        label = "EXAMINED BUT NOT IN THE SYLLABUS" if warn else "NOTE"
        return (f'<div class="{cls}"><span class="label">{label}</span>\n'
                f'{inner}\n</div>')

    html_text = re.sub(r'<blockquote>\s*(.*?)\s*</blockquote>',
                       blockquote, html_text, flags=re.S)

    # Review-finding references (finding D1, finding **D2**, ...) get a chip.
    html_text = re.sub(
        r'finding\s+(?:<strong>)?\*{0,2}(D\d{1,2})\*{0,2}(?:</strong>)?',
        r'finding <span class="finding">\1</span>', html_text)

    # Left-align the first column of every table -- the house style centres
    # all cells, which suits numeric tables but not topic listings.
    html_text = html_text.replace("<table>", '<table class="main-table">')
    return html_text


def chips_from_headings(body_md, limit=12):
    """Build the .chips topic row from the page's H2 headings."""
    chips = []
    for line in body_md.splitlines():
        if line.startswith("## "):
            t = line[3:].strip()
            # drop numbering prefixes: "1.2 ", "A.1 ", "5.10 "
            t = re.sub(r'^[A-Z]?\d*(\.\d+)*\s+', '', t)
            t = re.sub(r'^(Part\s+[A-Z]\s*[—-]\s*)', '', t)
            t = re.sub(r'[*`]', '', t)
            t = t.split("—")[0].split(" - ")[0].strip()
            if t and t.lower() not in {c.lower() for c in chips}:
                chips.append(t)
    return chips[:limit]


def page(title, banner_title, banner_sub, crumbs, body, css_prefix="",
         mathjax=False, mermaid=False, chips=None, nav=None, footer=""):
    """Assemble one page in the Statistics-Major house layout."""
    head_extra = "\n".join(x for x in
                           [MATHJAX if mathjax else "",
                            ] if x)
    chip_html = ""
    if chips:
        spans = "\n    ".join(f'<span class="chip">{html.escape(c)}</span>'
                              for c in chips)
        chip_html = f'  <h2>Topics Covered</h2>\n  <div class="chips">\n    {spans}\n  </div>\n\n'

    nav_html = ""
    if nav:
        links = "\n    ".join(f'<a href="{href}">{html.escape(label)}</a>'
                              for label, href in nav)
        nav_html = f'  <div class="page-nav">\n    {links}\n  </div>\n\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css_prefix}css/styles.css">
{head_extra}
</head>
<body>
<div class="wrapper">

  <div class="banner">
    <div class="crumbs">{crumbs}</div>
    <h1>{html.escape(banner_title)}</h1>
    <p>{banner_sub}</p>
  </div>

{chip_html}{body}

{nav_html}  <footer>{footer}</footer>
</div>
{MERMAID if mermaid else ""}
</body>
</html>
"""

# --------------------------------------------------------------------------
# Builders
# --------------------------------------------------------------------------

def build_course(course, link_map):
    """Render one course: its landing page plus every unit and extra page."""
    slug = course["slug"]
    src = ROOT / course["src"]
    out_dir = ROOT / slug
    out_dir.mkdir(exist_ok=True)
    written = []

    unit_files = sorted(src.glob("unit-*.md"),
                        key=lambda p: int(re.search(r'\d+', p.stem).group()))

    # ---- unit pages ----
    for idx, md_path in enumerate(unit_files, start=1):
        raw = md_path.read_text()
        heading, body_md = strip_first_heading(raw)
        unit_title, unit_desc = course["units"][idx - 1]

        body_md = rewrite_links(body_md, link_map, src, out_dir)
        body = promote_boxes(render_markdown(body_md))

        nav = [("← Course home", f"index_{slug}.html")]
        if idx > 1:
            prev_title = course["units"][idx - 2][0]
            nav.append((f"← Unit {idx - 1}", f"unit{idx - 1}_{slug}.html"))
        if idx < len(unit_files):
            next_title = course["units"][idx][0]
            nav.append((f"Next: Unit {idx + 1} — {next_title} →",
                        f"unit{idx + 1}_{slug}.html"))

        out = out_dir / f"unit{idx}_{slug}.html"
        out.write_text(page(
            title=f"Unit {idx} — {unit_title} | {course['title']}",
            banner_title=f"Unit {idx} — {unit_title}",
            banner_sub=html.escape(unit_desc),
            crumbs=f'<a href="../index.html">Home</a> &raquo; '
                   f'<a href="index_{slug}.html">{html.escape(course["title"])}</a> '
                   f'&raquo; Unit {idx}',
            body=body,
            css_prefix="../",
            mathjax=True,
            mermaid="```mermaid" in raw,
            chips=chips_from_headings(body_md),
            nav=nav,
            footer=f"Unit {idx} — {html.escape(unit_title)} • "
                   f"Course {course['number']}, Semester {course['sem']}",
        ))
        written.append(out)

    # ---- practice / lab / formula-sheet ----
    extras = []
    for fname, (out_slug, tag, desc) in EXTRA_PAGES.items():
        md_path = src / fname
        if not md_path.exists():
            continue
        raw = md_path.read_text()
        heading, body_md = strip_first_heading(raw)
        body_md = rewrite_links(body_md, link_map, src, out_dir)
        body = promote_boxes(render_markdown(body_md))

        out = out_dir / f"{out_slug}_{slug}.html"
        out.write_text(page(
            title=f"{heading or tag} | {course['title']}",
            banner_title=heading or tag.title(),
            banner_sub=html.escape(desc),
            crumbs=f'<a href="../index.html">Home</a> &raquo; '
                   f'<a href="index_{slug}.html">{html.escape(course["title"])}</a> '
                   f'&raquo; {tag.title()}',
            body=body,
            css_prefix="../",
            mathjax=True,
            mermaid="```mermaid" in raw,
            nav=[("← Course home", f"index_{slug}.html")],
            footer=f"{tag.title()} • Course {course['number']} — "
                   f"{html.escape(course['title'])}",
        ))
        written.append(out)
        extras.append((out_slug, tag, desc, out.name))

    # ---- course landing page ----
    readme = src / "README.md"
    intro_html = ""
    if readme.exists():
        raw = readme.read_text()
        _, body_md = strip_first_heading(raw)
        # Keep the prose above the unit table; the cards below replace it.
        body_md = re.split(r'^## Units\b', body_md, flags=re.M)[0]
        body_md = rewrite_links(body_md, link_map, src, out_dir)
        intro_html = promote_boxes(render_markdown(body_md))

    cards = []
    for idx, (unit_title, unit_desc) in enumerate(course["units"], start=1):
        cards.append(
            f'    <a class="unit-card" href="unit{idx}_{slug}.html">\n'
            f'      <span class="tag">UNIT {idx}</span>\n'
            f'      <h3>{html.escape(unit_title)}</h3>\n'
            f'      <p>{html.escape(unit_desc)}</p>\n'
            f'    </a>')
    for out_slug, tag, desc, fname in extras:
        cards.append(
            f'    <a class="unit-card" href="{fname}">\n'
            f'      <span class="tag">{tag}</span>\n'
            f'      <h3>{html.escape(out_slug.replace("-", " ").title())}</h3>\n'
            f'      <p>{html.escape(desc)}</p>\n'
            f'    </a>')

    body = (intro_html
            + '\n  <h2>Units in this Course</h2>\n  <div class="unit-grid">\n\n'
            + "\n\n".join(cards)
            + '\n\n  </div>\n')

    out = out_dir / f"index_{slug}.html"
    out.write_text(page(
        title=f"{course['title']} — Complete Study Material",
        banner_title=course["title"],
        banner_sub=f"B.Sc. (Hons) Data Science — Year {course['year']}, "
                   f"Semester {course['sem']}, Course {course['number']}",
        crumbs='<a href="../index.html">Home</a> &raquo; '
               f'Course {course["number"]}',
        body=body,
        css_prefix="../",
        mathjax=True,
        nav=[("← All courses", "../index.html")],
        footer=f"Course {course['number']} — {html.escape(course['title'])} • "
               f"3 credits theory + 1 credit lab",
    ))
    written.append(out)
    return written


def build_top_pages(link_map):
    """Render the three repository-level documents."""
    written = []
    for fname, out_slug, title, desc in TOP_PAGES:
        md_path = ROOT / fname
        if not md_path.exists():
            continue
        raw = md_path.read_text()
        heading, body_md = strip_first_heading(raw)
        body_md = rewrite_links(body_md, link_map, ROOT, ROOT)
        body = promote_boxes(render_markdown(body_md))

        out = ROOT / f"{out_slug}.html"
        out.write_text(page(
            title=f"{title} | Data Science Major 2025",
            banner_title=heading or title,
            banner_sub=html.escape(desc),
            crumbs='<a href="index.html">Home</a> &raquo; ' + html.escape(title),
            body=body,
            css_prefix="",
            mathjax=True,
            nav=[("← Home", "index.html")],
            footer="APSCHE Model Syllabus for B.Sc. (Data Science) Major, "
                   "AY&nbsp;2025-26",
        ))
        written.append(out)
    return written


def build_link_map():
    """Map every source .md filename to the page it becomes."""
    link_map = {}
    for course in COURSES:
        slug = course["slug"]
        for idx in range(1, 6):
            link_map[f"unit-{idx}.md"] = f"unit{idx}_{slug}.html"
        for fname, (out_slug, _, _) in EXTRA_PAGES.items():
            link_map[fname] = f"{out_slug}_{slug}.html"
        link_map["README.md"] = f"index_{slug}.html"
    for fname, out_slug, _, _ in TOP_PAGES:
        link_map[fname] = f"{out_slug}.html"
    return link_map


def main():
    written = []

    # Course-local link maps: unit-3.md means a different page in each course,
    # so rebuild the map per course rather than sharing one.
    for course in COURSES:
        slug = course["slug"]
        lm = {}
        for idx in range(1, 6):
            lm[f"unit-{idx}.md"] = f"unit{idx}_{slug}.html"
        for fname, (out_slug, _, _) in EXTRA_PAGES.items():
            lm[fname] = f"{out_slug}_{slug}.html"
        lm["README.md"] = f"index_{slug}.html"
        for fname, out_slug, _, _ in TOP_PAGES:
            lm[fname] = f"../{out_slug}.html"
        written += build_course(course, lm)

    top_lm = {fname: f"{out_slug}.html" for fname, out_slug, _, _ in TOP_PAGES}
    written += build_top_pages(top_lm)

    print(f"{len(written)} pages generated")
    for p in sorted(written):
        print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
