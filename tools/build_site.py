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
{
        "slug": "data-science-r",
        "src": "notes/sem-3/course-6-data-science-r",
        "number": 6, "year": "II", "sem": "III",
        "title": "Data Science with R",
        "tagline": "The data science process, R programming, wrangling, "
                   "visualisation, modelling and time series.",
        "blurb": "5 Units + Lab \u2022 Data science lifecycle, R programming, "
                 "dplyr/ggplot2, regression, clustering, ARIMA and Shiny.",
        "units": [
            ("Introduction to the Data Science Process",
             "Definition and applications; the Data Analytics Life Cycle; the "
             "toolkit and the team; exploratory data analysis; feature "
             "engineering and data transformation."),
            ("Basics of R Programming",
             "R and RStudio; data types and structures; operators; control "
             "structures and the apply family; functions and packages; "
             "reading CSV, Excel, JSON and XML."),
            ("Data Handling and Visualization in R",
             "The pipe and the five dplyr verbs; tidyr reshaping; missing "
             "data; dates and times; ggplot2 \u2014 grammar of graphics, "
             "geometries, scales, faceting and export."),
            ("Applications and Case Studies",
             "Simple and multiple regression; confusion matrix, precision, "
             "recall, ROC and AUC; K-Means clustering; text mining and "
             "TF-IDF; recommender systems; ethics in data science."),
            ("Advanced Topics",
             "Time series \u2014 decomposition, stationarity, differencing, "
             "ACF/PACF, ARIMA and forecasting; interactive plots with plotly; "
             "building web applications with R Shiny."),
        ],
    },
    {
        "slug": "web-technologies",
        "src": "notes/sem-3/course-7-web-technologies",
        "number": 7, "year": "II", "sem": "III",
        "title": "Web Technologies",
        "tagline": "HTML, CSS, JavaScript, the DOM, JSON and jQuery \u2014 "
                   "the only course where you build something you can see.",
        "blurb": "5 Units + Lab \u2022 HTML structure and forms, CSS layout "
                 "and responsive design, JavaScript, the DOM, JSON and jQuery.",
        "units": [
            ("HTML",
             "Web versus desktop applications; the client\u2013server model; "
             "document structure, elements and attributes; headings, text, "
             "lists, images and multimedia; tables; semantic HTML5; forms and "
             "GET versus POST."),
            ("CSS",
             "Syntax and the three attachment methods; the four combinators; "
             "specificity and the cascade; the box model; colours, borders, "
             "backgrounds, text and fonts; positioning, float, Flexbox and "
             "Grid; pseudo-classes and pseudo-elements; tooltips, galleries, "
             "forms, counters and media queries."),
            ("JavaScript",
             "DHTML; variables and types; operators and coercion; statements "
             "and loops; functions, closures and hoisting; string methods; "
             "Math; arrays and objects; classes; regular expressions; "
             "exception handling."),
            ("Client-Side Scripting",
             "The DOM and the BOM; selecting and changing elements; accessing "
             "form controls; the event model \u2014 bubbling, capturing and "
             "delegation; basic and format validation; inline messages; "
             "windows, dialog boxes and the status bar; keyboard and mouse "
             "events; animation."),
            ("JSON and jQuery",
             "Why data-exchange formats exist; JSON syntax and its "
             "restrictions; JSON versus XML; parsing, stringifying and nested "
             "access; fetch and localStorage; jQuery selectors, filters, DOM "
             "manipulation, events, effects, chaining and AJAX."),
        ],
    },
    {
        "slug": "data-mining",
        "src": "notes/sem-4/course-8-data-mining",
        "number": 8, "year": "II", "sem": "IV",
        "title": "Data Mining",
        "tagline": "Warehousing and OLAP, preprocessing, association rules, "
                   "classification and clustering \u2014 the algorithmic core.",
        "blurb": "5 Units + Lab \u2022 Star schemas and OLAP, preprocessing, "
                 "Apriori and FP-Growth, ID3/C4.5/CART, K-Means and DBSCAN.",
        "units": [
            ("Data Warehousing and OLAP",
             "Inmon\u2019s four characteristics; OLTP versus OLAP; three-tier "
             "architecture and ETL; the multidimensional model; fact and "
             "dimension tables; star, snowflake and fact constellation "
             "schemas; the cube and the five OLAP operations."),
            ("Data Mining and Preprocessing",
             "Definitions and the KDD process; predictive versus descriptive "
             "tasks; cleaning, missing data and noise; the curse of "
             "dimensionality and PCA; feature subset selection; "
             "discretization and binarization; normalisation; similarity and "
             "dissimilarity measures; issues, ethics and applications."),
            ("Association Analysis",
             "Support, confidence and lift; why confidence alone misleads; "
             "the Apriori principle and algorithm; rule generation; "
             "Partition, Pincer-Search and Dynamic Itemset Counting; the "
             "FP-tree and FP-Growth; generalized rules and item constraints."),
            ("Classification",
             "Decision trees and the best split; entropy, information gain, "
             "gain ratio and Gini; ID3, C4.5 and CART; overfitting and "
             "pruning; the confusion matrix, precision, recall, F1, ROC and "
             "AUC; rule-based classifiers; k-nearest neighbour; Na\u00efve "
             "Bayes and Laplace smoothing."),
            ("Clustering Techniques",
             "Clustering paradigms and validity measures; K-Means and its "
             "five weaknesses; K-Medoids and PAM; agglomerative clustering "
             "and linkage criteria; DBSCAN; BIRCH and the CF-tree; "
             "categorical clustering with STIRR, ROCK and CACTUS."),
        ],
    },
    {
        "slug": "python-data-analysis",
        "src": "notes/sem-4/course-9-python-data-analysis",
        "number": 9, "year": "II", "sem": "IV",
        "title": "Python for Data Analysis and Visualization",
        "tagline": "NumPy and Pandas \u2014 the tools you will actually use, "
                   "every day, in any data job you take.",
        "blurb": "5 Units + Lab \u2022 NumPy arrays, Pandas Series and "
                 "DataFrames, cleaning, feature engineering, wrangling and "
                 "three plotting libraries.",
        "units": [
            ("NumPy Essentials",
             "The ndarray against the Python list; creating arrays and dtypes; "
             "arithmetic and broadcasting; basic, boolean and fancy indexing, "
             "and which return views; transposing and swapping axes; universal "
             "functions; statistical functions and the axis parameter; random "
             "number generation."),
            ("Pandas Basics and Data Structures",
             "Series and DataFrame; Index objects; the three accessors and why "
             "\u2018loc\u2019 is inclusive; filtering and boolean indexing; "
             "arithmetic and data alignment; sorting and the five ranking "
             "methods; dropping entries; duplicate indexes."),
            ("Data Input, Output and Cleaning",
             "read_csv and the parameters that matter; JSON and "
             "json_normalize; Excel; detecting, dropping and filling missing "
             "data; replacing sentinel values; renaming axes; removing "
             "duplicates; filtering outliers by z-score and IQR; transforming "
             "with map, apply and transform."),
            ("String Operations and Feature Engineering",
             "The .str accessor; regular expressions with extract, contains "
             "and replace; engineering features from dates, numbers and "
             "categories; dummy and indicator variables and the dummy variable "
             "trap; permutation, stratified sampling and the bootstrap."),
            ("Wrangling, Reshaping and Visualization",
             "Merging and the four join types; concatenation; combining with "
             "overlap; hierarchical indexing; pivot, melt, stack and unstack; "
             "split\u2013apply\u2013combine; recomputing Course 4 in Pandas; "
             "matplotlib, Seaborn and Plotly."),
        ],
    },
    {
        "slug": "document-database",
        "src": "notes/sem-4/course-10-document-database",
        "number": 10, "year": "II", "sem": "IV",
        "title": "Document Oriented Database",
        "tagline": "MongoDB, and the design question behind every document "
                   "database: embed or reference?",
        "blurb": "5 Units + Lab \u2022 NoSQL and CAP, BSON and the document "
                 "model, CRUD and MQL, embedded against normalized models, "
                 "aggregation pipelines, indexing and replication.",
        "units": [
            ("Introduction to NoSQL and the Fundamentals of MongoDB",
             "What NoSQL is and what it is not; the CAP theorem and BASE "
             "against ACID; the four families \u2014 key-value, document, "
             "column and graph; RDBMS against NoSQL, and when NOT to use "
             "NoSQL; Redis, Cassandra, CouchDB and Neo4j compared; JSON and "
             "BSON; installation, the Mongo shell and Compass."),
            ("MongoDB Architecture, Data Modeling and Basics",
             "Database, collection and document; the BSON types and where "
             "each one bites; ObjectId and what its twelve bytes hold; schema "
             "design strategies; embedded against referenced documents; "
             "creating and dropping databases and collections."),
            ("CRUD Operations and Querying",
             "insertOne and insertMany, ordered and unordered; find and the "
             "comparison, logical, element, evaluation and array operators; "
             "updateOne, updateMany and the destructive replaceOne; deleteOne "
             "and deleteMany; regular expression queries; bulk operations; "
             "array update operators and $elemMatch."),
            ("Data Modelling and Aggregation",
             "Embedded against normalized models and the trade-offs of each; "
             "when to normalize; one-to-one, one-to-many and many-to-many; "
             "the 16 MB limit and the unbounded array; the extended reference, "
             "computed and attribute patterns; the aggregation framework, "
             "and $match/$group as WHERE and HAVING."),
            ("Advanced Query Processing and Optimization",
             "Projection, sorting, limiting and skipping, and the order the "
             "server applies them; range pagination against skip; single "
             "field, compound, multikey and text indexes; the prefix rule and "
             "ESR; reading explain(\"executionStats\"); aggregation pipelines "
             "and $lookup; replica sets, failover, write concern, and why an "
             "odd number of members."),
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
GITHUB_TREE = ("https://github.com/nrstatlab/Data-Science-Major-2025/tree/main/")


def rewrite_links(body, link_map, src_dir, out_dir):
    """Retarget the Markdown's relative links for the generated page.

    Four cases:
      * a .md file that becomes a page   -> its generated .html sibling
      * any other repo FILE (lab source, -> re-relativised, because the source
        the syllabus PDF)                   .md sits deeper in notes/ than the
                                            generated page does
      * a repo DIRECTORY (labs/course-x) -> the directory on github.com.
                                            GitHub Pages serves files, not
                                            directory listings, so a relative
                                            link to one 404s on the published
                                            site even though the directory is
                                            right there in the repository.
      * a .md file with no page          -> the file on github.com
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

        if resolved.is_dir():
            return f'[{label}]({GITHUB_TREE}{rel_to_root}{frag})'

        if resolved.exists():
            import os
            new_target = os.path.relpath(resolved, out_dir).replace("\\", "/")
            return f'[{label}]({new_target}{frag})'

        if target.endswith(".md"):
            return f'[{label}]({GITHUB_BLOB}{rel_to_root}{frag})'
        return m.group(0)

    return re.sub(r'\[([^\]]*)\]\(([^)#\s]+)(#[^)\s]*)?\)', repl, body)


# --------------------------------------------------------------------------
# Composition: map the notes' recurring structure onto the house style's
# semantic boxes, the way Statistics-Major composes its pages by hand.
# --------------------------------------------------------------------------

HEADING = re.compile(r'^(#{2,6})\s')

# Trigger heading -> (css class, label). The notes use a consistent set of
# marker headings, which is what makes this reliable rather than guesswork.
SECTION_BOXES = [
    (re.compile(r'^###\s*🎯\s*(.*)$'),  "concept", "THE BIG IDEA"),
    (re.compile(r'^###\s*📖\s*(.*)$'),  "tip",     "STORY"),
    (re.compile(r'^###\s*🔢\s*(.*)$'),  "formula", "FORMULA"),
    (re.compile(r'^###\s*💡\s*(.*)$'),  "tip",     "KEY INSIGHT"),
]

PROBLEM_RE = re.compile(r'^###\s+(Problem\s+\d+|Q\d+)\b(.*)$')
WORKED_RE = re.compile(
    r'^(?:\*\*|\*)(Worked example|Worked solution|Worked examples|Example|Trace)'
    r'([^*]*)(?:\*\*|\*)[.:]?')

# "## Worked example — trace the output" style headings.
WORKED_HEADING_RE = re.compile(
    r'^#{2,4}\s+(Worked example|Example)\b\s*[—-]?\s*(.*)$', re.I)

# "A **linked list** is ..." / "The **control unit** performs ..." -- the
# notes' definition sentences, which Statistics-Major would set as .concept.
DEFINITION_RE = re.compile(
    r'^(?:A|An|The)\s+\*\*([^*]{2,60})\*\*\s+(?:is|are|means|refers to)\b')

# Bolded rhetorical lead-ins that explain rather than define.
INSIGHT_RE = re.compile(
    r'^\*\*(Why|The point|Rule|Remember|Note|Careful|Key)\b[^*]*\*\*')


def _capture(lines, start, stop_levels=(2, 3)):
    """Return (block, next_index): lines until the next qualifying heading."""
    out = []
    i = start
    while i < len(lines):
        line = lines[i]
        m = HEADING.match(line)
        if m and len(m.group(1)) in stop_levels:
            break
        if line.strip() == "---":
            break
        out.append(line)
        i += 1
    return out, i


def _box(cls, label, title, body_lines):
    """Emit a house-style box, matching Statistics-Major's markup.

    The label is a SIBLING of the content, not part of its first paragraph --
    a blank line after it is what keeps Python-Markdown from absorbing the
    following list or paragraph into the same block.

    Blockquote markers are stripped from the body: the box already provides
    the visual container, so a quoted formula inside a .formula section would
    otherwise be boxed twice.
    """
    body = [re.sub(r'^>\s?', '', ln) for ln in body_lines]
    inner = "\n".join(body).strip("\n")

    parts = [f'<div class="{cls}" markdown="1">', f'<span class="label">{label}</span>', '']
    if title:
        parts += [f'#### {title}', '']
    parts += [inner, '</div>', '']
    return parts


def _is_formula_quote(text):
    """A blockquote that states a formula rather than making a remark."""
    if len(text) > 420:
        return False
    mathy = sum(text.count(c) for c in "=Σ∫√±×÷≤≥≠∞µσ²³")
    return "=" in text and mathy >= 1


LIST_START = re.compile(r'^\s{0,3}(?:[-*+]\s+|\d{1,3}[.)]\s+)\S')


def normalise_lists(md_text):
    """Insert the blank line Python-Markdown needs before a list.

    GitHub's renderer accepts a list that starts on the line straight after a
    paragraph; Python-Markdown treats it as lazy continuation and leaves the
    dashes as literal text. The notes are written in the GitHub style, so
    normalise here rather than editing 41 source files.
    """
    lines = md_text.split("\n")
    out = []
    in_fence = False
    for idx, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if (not in_fence and LIST_START.match(line) and out
                and out[-1].strip()
                and not LIST_START.match(out[-1])
                and not out[-1].lstrip().startswith((">", "|", "#"))
                and not out[-1].rstrip().endswith(("|",))):
            out.append("")
        out.append(line)
    return "\n".join(out)


def promote_markdown_boxes(md_text):
    """Wrap recognised sections in .concept / .formula / .example / .tip."""
    md_text = normalise_lists(md_text)
    lines = md_text.split("\n")
    out = []
    i = 0
    in_fence = False

    while i < len(lines):
        line = lines[i]

        # Never rewrite anything inside a fenced code block.
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence:
            out.append(line)
            i += 1
            continue

        # --- marker headings: 🎯 big idea, 📖 story, 🔢 formula, 💡 insight ---
        matched = False
        for rx, cls, label in SECTION_BOXES:
            m = rx.match(line)
            if m:
                title = m.group(1).strip() or None
                # Drop a redundant title that just repeats the label.
                if title and title.lower().strip(' "') in {
                        "the big idea", "the story", "the formula",
                        'the "aha!" moment'}:
                    title = None
                body, i = _capture(lines, i + 1, stop_levels=(2, 3))
                out += _box(cls, label, title, body)
                matched = True
                break
        if matched:
            continue

        # --- practice problems become worked examples ---
        m = PROBLEM_RE.match(line)
        if m:
            label = m.group(1).upper()
            title = m.group(2).strip(" —-").strip() or None
            body, i = _capture(lines, i + 1, stop_levels=(2, 3))
            out += _box("example", label, title, body)
            continue

        # --- inline "**Worked example.**" paragraphs ---
        wm = WORKED_RE.match(line)
        if wm:
            qualifier = (wm.group(2) or "").strip(" ().:")
            label = "WORKED EXAMPLE"
            if wm.group(1).lower().startswith("trace"):
                label = "TRACE"
            rest = line[wm.end():].strip()
            body, i = _capture(lines, i + 1, stop_levels=(2, 3))
            if rest:
                body = [rest] + body
            out += _box("example", label, qualifier or None, body)
            continue

        # --- "## Worked example — ..." headings ---
        m = WORKED_HEADING_RE.match(line)
        if m:
            title = m.group(2).strip() or None
            body, i = _capture(lines, i + 1, stop_levels=(2, 3))
            out += _box("example", "WORKED EXAMPLE", title, body)
            continue

        # --- definition sentences become .concept, as on Statistics-Major ---
        if DEFINITION_RE.match(line):
            body = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and \
                    not HEADING.match(lines[i]) and \
                    not lines[i].lstrip().startswith(("```", ">", "|", "-", "*", "1.")):
                body.append(lines[i])
                i += 1
            out += _box("concept", "DEFINITION", None, body)
            continue

        # --- explanatory lead-ins become .tip ---
        if INSIGHT_RE.match(line):
            body = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and \
                    not HEADING.match(lines[i]) and \
                    not lines[i].lstrip().startswith(("```", ">", "|")):
                body.append(lines[i])
                i += 1
            out += _box("tip", "WHY IT MATTERS", None, body)
            continue

        # --- blockquotes ---
        if line.startswith(">"):
            block = []
            while i < len(lines) and (lines[i].startswith(">") or
                                      (lines[i].strip() == "" and
                                       i + 1 < len(lines) and
                                       lines[i + 1].startswith(">"))):
                block.append(re.sub(r'^>\s?', '', lines[i]))
                i += 1
            text = "\n".join(block).strip()
            if "⚠" in text or "examined but" in text.lower():
                cls, label = "warn", "EXAMINED BUT NOT IN THE SYLLABUS"
            elif _is_formula_quote(text):
                cls, label = "formula", "FORMULA"
            else:
                cls, label = "tip", "NOTE"
            out += _box(cls, label, None, block)
            continue

        # --- "Mistakes that cost marks" list becomes a warning ---
        if re.match(r'^##\s+Mistakes that cost marks\s*$', line):
            out.append(line)
            i += 1
            body, i = _capture(lines, i, stop_levels=(2,))
            out += _box("warn", "COMMON ERRORS", None, body)
            continue

        out.append(line)
        i += 1

    return "\n".join(out)


def promote_boxes(html_text):
    """Map Markdown constructs onto the house style's semantic boxes."""
    # Any blockquote that survived promote_markdown_boxes (e.g. nested inside
    # a list) still gets the house .tip treatment rather than browser default.
    html_text = re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        r'<div class="tip"><span class="label">NOTE</span>\n\1\n</div>',
        html_text, flags=re.S)

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
        body = promote_boxes(render_markdown(promote_markdown_boxes(body_md)))

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
        body = promote_boxes(render_markdown(promote_markdown_boxes(body_md)))

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
        intro_html = promote_boxes(render_markdown(promote_markdown_boxes(body_md)))

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
        body = promote_boxes(render_markdown(promote_markdown_boxes(body_md)))

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
