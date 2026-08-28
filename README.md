# B.Sc. (Hons) Data Science — Major

Study material for the **Model Syllabus for 4-Year UG Honours in B.Sc.
(Data Science) as Major**, effective AY 2025-26, prepared by Adikavi Nannaya
University.

This repository contains a **review** of the official syllabus and **study
material** built from it — unit notes, worked examples, practice problems with
solutions, and every lab program as runnable code.

---

## ⚠ Four topics are examined but missing from the syllabus

Read these before you start revising, because studying the unit lists alone
will leave you unprepared for all four.

### 1. Bayes' theorem — Course 4, Statistics

Unit 1 lists only "conditional probability". Bayes appears in the prescribed
activities quiz and in lab experiment 2, but in **no unit**.

→ Covered in Course 4 Unit 1

### 2. Database triggers — Course 5, DBMS

Unit 5 lists control structures, procedures and functions — **no triggers**.
Yet Course Objective 5 names them, the activities require them, and **two of the
six PL/SQL lab questions are trigger problems**.

→ Covered in Course 5 Unit 5

### 3 and 4. GridFS and transactions — Course 10, Document Oriented Database

Unit 5's topic list ends at "Replica sets, failover, consistency" — **neither
GridFS nor transactions appears in it, or in any other unit**. Yet Course
Outcome 4 names both, and **lab experiments 18 and 19 are exactly those two
problems**. The course objective that would have introduced them is itself
truncated to the fragment "4. replication, and transactions." (finding
**D13**), which is probably how they went missing.

→ Covered in Course 10 Unit 5,
[lab experiment 18](labs/course-10-mongodb/18_gridfs.js) and
[lab experiment 19](labs/course-10-mongodb/19_transactions.js)

**Twenty further findings** are in [`SYLLABUS-REVIEW.md`](SYLLABUS-REVIEW.md),
including damaged bibliographies in all five Semester III–IV courses, a
Semester V objective that stops mid-sentence, and a course with three
objectives against four outcomes against five units.

**And a pattern worth naming:** nine of the twenty-four findings are the same
defect — **text lost at a word or sentence boundary**, across all three
documents. That is a production problem, not a scattering of typos.

---

**Published site:** https://nrstatlab.github.io/Data-Science-Major-2025/

## Start here

| Document | What it is |
|---|---|
| [`SYLLABUS-MAP.md`](SYLLABUS-MAP.md) | The full Sem I–VI structure, elective tracks, and unit-level topics |
| [`SYLLABUS-REVIEW.md`](SYLLABUS-REVIEW.md) | **33 findings** from checking the four official documents |
| [`STUDY-PLAN.md`](STUDY-PLAN.md) | Week-by-week schedules for **Semesters I–VI**, the track decision, revision cycles, progress checklist |

## Course notes

| Sem | Course | Notes |
|:---:|---|---|
| I | 1 — Computer Fundamentals and Office Automation | [notes](notes/sem-1/course-1-computer-fundamentals/) |
| I | 2 — Problem Solving Using C | [notes](notes/sem-1/course-2-problem-solving-c/) |
| II | 3 — Python Programming and Data Structures | [notes](notes/sem-2/course-3-python-data-structures/) |
| II | 4 — Statistical Foundations for Data Science | [notes](notes/sem-2/course-4-statistical-foundations/) |
| III | 5 — Database Management Systems | [notes](notes/sem-3/course-5-dbms/) |
| III | 6 — Data Science with R | [notes](notes/sem-3/course-6-data-science-r/) |
| III | 7 — Web Technologies | [notes](notes/sem-3/course-7-web-technologies/) |
| IV | 8 — Data Mining | [notes](notes/sem-4/course-8-data-mining/) |
| IV | 9 — Python for Data Analysis and Visualization | [notes](notes/sem-4/course-9-python-data-analysis/) |
| IV | 10 — Document Oriented Database | [notes](notes/sem-4/course-10-document-database/) |
| V | 11 — Business Intelligence Tools *(core)* | [notes](notes/sem-5/course-11-business-intelligence/) |
| V | 12 A — Machine Learning *(Track A)* | [notes](notes/sem-5/course-12a-machine-learning/) |
| V | 13 A — Artificial Intelligence *(Track A)* | [notes](notes/sem-5/course-13a-artificial-intelligence/) |
| V | 12 B — Big Data Technologies *(Track B)* | [notes](notes/sem-5/course-12b-big-data/) |
| V | 13 B — Cloud Computing for Data Science *(Track B)* | [notes](notes/sem-5/course-13b-cloud-computing/) |
| VI | 14 A — Neural Networks and Deep Learning *(Track A)* | [notes](notes/sem-6/course-14a-deep-learning/) |
| VI | 15 A — Natural Language Processing *(Track A)* | [notes](notes/sem-6/course-15a-nlp/) |
| VI | 14 B — Time Series Analysis and Forecasting *(Track B)* | [notes](notes/sem-6/course-14b-time-series/) |
| VI | 15 B — Data Engineering and MLOps *(Track B)* | [notes](notes/sem-6/course-15b-mlops/) |

Each course folder holds a `README.md`, five unit notes, a `practice.md` with
worked solutions, and a `lab.md`. Course 4 also has a
formula sheet.

## Lab code

| Course | Contents | Status |
|---|---|---|
| [2 — C](labs/course-2-c/) | 15 programs | Compiled `-Wall -Wextra`, no warnings, run |
| [3 — Python](labs/course-3-python/) | 18 programs | 16 run; 2 Tkinter syntax-checked only |
| [4 — Statistics](labs/course-4-stats/) | 15 Excel walkthroughs + Python equivalents | Python run; `statlib` checked against tables |
| [5 — SQL](labs/course-5-dbms/) | 3 experiments + PL/SQL | SQL executed; PL/SQL desk-checked only |
| [6 — R](labs/course-6-r/) | 18 R scripts + 14 Python equivalents | R structurally checked (uninstallable here); equivalents run |
| [7 — Web](labs/course-7-web/) | 16 experiments, HTML/CSS/JS | Run under jsdom, **184 assertions** on the resulting DOM |
| [8 — Data Mining](labs/course-8-datamining/) | 15 experiments | WEKA click-paths documented; scikit-learn/mlxtend equivalents run |
| [9 — Pandas](labs/course-9-python-da/) | 18 practicals | **All run**, outputs asserted |
| [10 — MongoDB](labs/course-10-mongodb/) | 20 experiments | 16 executed through mongomock; 4 need a server and say **NOT EXECUTED** |
| [11 — BI](labs/course-11-bi/) | 15 experiments | Every DAX, Power Query and LOD figure computed; tool click-paths **NOT EXECUTED** |
| [12 A — ML](labs/course-12a-ml/) | 12 practicals | **All run** under scikit-learn. Nothing in this course is marked NOT EXECUTED |
| [13 A — AI](labs/course-13a-ai/) | 19 experiments | 16 Prolog programs **NOT EXECUTED**; 7 Python halves run, **five as real logic programs** |
| [12 B — Big Data](labs/course-12b-bigdata/) | 17 experiments | 14 run, including **real Apache Spark, Avro and Parquet**; 15 tool files **NOT EXECUTED** |
| [13 B — Cloud](labs/course-13b-cloud/) | 15 experiments | 7 run, including a **real web server, a real ETL and a real REST endpoint**; 14 console files **NOT EXECUTED** |
| [14 A — Deep Learning](labs/course-14a-deeplearning/) | 12 experiments | **10 run against real MNIST, Fashion-MNIST, IMDb and real MobileNetV2/VGG16 ImageNet weights**; 2 **NOT EXECUTED** |
| [14 B — Time Series](labs/course-14b-timeseries/) | 13 experiments | **All 13 run.** No file in this course is marked NOT EXECUTED |
| [15 A — NLP](labs/course-15a-nlp/) | 14 experiments | **11 run against real NLTK corpora and real spaCy models**, every result scored against hand-labelled truth; 3 **NOT EXECUTED** |
| [15 B — MLOps](labs/course-15b-mlops/) | 16 experiments | **11 run against real MLflow, git, DVC and Flask**; 5 **NOT EXECUTED** |

---

## Scope

**Four** source documents, all extracted verbatim and committed under
[`docs/`](docs/):

| Document | Pages | Covers |
|---|:---:|---|
| `Data-Science-Major-Sem1-2.pdf` | 37 | Programme structure for Semesters I–VI, plus full syllabi for Courses 1–5 |
| `Data-Science-Major-Sem3-4.pdf` | 25 | Full syllabi for Courses 6–10 |
| `Data-Science-Major-Sem5.pdf` | 24 | Full syllabi for Course 11 and **both** Semester V elective pairs — 12 A/B and 13 A/B |
| `Data-Science-Major-Sem6.pdf` | 17 | Full syllabi for **both** Semester VI elective pairs — 14 A/B and 15 A/B |

Together they give **all 15 major courses at unit level**, across four source
documents. Nothing in the programme is now titles-and-credits only.

**Semester V is a fork.** Course 11 is compulsory; you then take either
**12 A + 13 A** (Machine Learning → Artificial Intelligence) or **12 B + 13 B**
(Big Data → Cloud Computing), and that choice binds you for Semester VI as
well — **14 A + 15 A** (Deep Learning → NLP) or **14 B + 15 B** (Time Series →
Data Engineering & MLOps). **Both tracks are covered here in full**, because
you cannot choose well without seeing what is in each.

**Credits verified:** every course is 3 credits theory + 1 credit lab. Semester
totals are 8, 8, 12, 12, 12, 8 — a **60-credit major**.

---

## Verifying everything

Nothing here is asserted without being checked.

```bash
bash tools/verify_all.sh          # every suite
python3 tools/check_coverage.py   # every syllabus topic has notes
```

| Suite | What it proves |
|---|---|
| `run_c_labs.sh` | 15 C programs compile warning-free and produce correct output |
| `run_python_labs.sh` | 20 Python files run; 2 Tkinter files syntax-check |
| `run_stats_labs.sh` | `statlib` matches 23 published table values; 5 experiment scripts run |
| `run_sql_labs.py` | 118 SQL statements execute; 9 constraints correctly reject bad data |
| `run_r_equivalents.py` | 14 Python equivalents run; 18 R scripts structurally checked |
| `run_web_labs.js` | 184 assertions on the DOM after each Course 7 lab script, under jsdom |
| `run_data_labs.py` | 33 Course 8 and 9 programs run, each asserting the notes' own figures |
| `run_mongo_labs.py` | 16 Course 10 experiments executed through mongomock; the other 4 audited for their NOT EXECUTED marker |
| `run_ml_labs.py` | Course 12 A's 12 practicals run under scikit-learn |
| `run_ai_labs.py` | Course 13 A's search and logic programs; 5 run as real Prolog |
| `run_bigdata_labs.py` | 14 of 17 Course 12 B experiments, including real Spark, Avro and Parquet |
| `run_cloud_labs.py` | Course 13 B's runnable halves, and 15 NOT EXECUTED markers audited |
| `run_deeplearning_labs.py` | Course 14 A on **real MNIST, Fashion-MNIST, IMDb and real ImageNet weights**; 2 markers audited |
| `run_timeseries_labs.py` | **All 13** Course 14 B experiments; no NOT EXECUTED file exists |
| `run_nlp_labs.py` | Course 15 A on **real NLTK corpora and real spaCy models**, every result scored; 3 markers audited |
| `run_mlops_labs.py` | Course 15 B against **real MLflow, git, DVC and Flask**; 5 markers audited |
| `extract_syllabus.py` | All PDF pages yield text |
| `check_coverage.py` | **1,273 syllabus topics across 95 unit files** all map to a notes section |
| `audit_content.py` | The documents' own **stated counts match the files on disk**; every course has its full note set; no malformed table; every link resolves |

Statistical results are additionally self-checked: regression output via
**R² = r²** and **t² = F**, and every critical value in the formula sheet
against `statlib`. Number-system conversions are verified by round-trip.

### What is *not* verified, and why

Honest limits, stated rather than hidden:

- **Tkinter programs** — `tkinter` is not installed in the verification
  environment and a GUI needs a display. Syntax-checked only; say so.
- **PL/SQL** — Oracle-specific. SQLite cannot run it and no Oracle instance was
  available. Written to Oracle syntax and reviewed by hand; run it on your
  college's installation before relying on it.
- **Excel walkthroughs** — not executable. The Python equivalents of the same 15
  experiments were run.
- **R, WEKA and `mongod`** — none can be installed here: the Debian
  repositories that host them are blocked by this environment's egress policy.
  Courses 6, 8 and 10 therefore ship the native script *and* an executed
  equivalent, and each native file says **NOT EXECUTED** in its own first lines.
- **Replication, GridFS and transactions** (Course 10 experiments 17–19) —
  these need a running server, and mongomock is a library. **No runnable
  equivalent exists**, and `tools/run_mongo_labs.py` asserts that each of the
  three still carries its marker, so they can never quietly start looking like
  test results.

---

## Repository layout

```
docs/                    the source PDF and its extracted text
notes/sem-N/course-N-*/  README, unit-1..5, practice, lab
labs/course-N-*/         runnable programs
tools/                   extraction and verification scripts
SYLLABUS-MAP.md          structure and topics
SYLLABUS-REVIEW.md       the findings
STUDY-PLAN.md            the schedule
```

## Rebuilding the website

The site is generated from these Markdown notes into the same house style as
[nrstatlab/Statistics-Major](https://github.com/nrstatlab/Statistics-Major) —
`css/styles.css` is adopted from that repository unchanged, so the two sites
read as one family.

```bash
pip install -r tools/requirements.txt
python3 tools/build_site.py
```

Markdown stays the source of truth: edit `notes/**/*.md`, re-run the build, and
commit both. `.nojekyll` is present, so Pages serves the generated HTML verbatim
rather than running Jekyll over it.

## Regenerating the extracted syllabus

```bash
python3 tools/extract_syllabus.py docs/Data-Science-Major-Sem1-2.pdf \
    > docs/syllabus-extracted.md
```

The extractor uses only the Python standard library, since neither `pdftotext`
nor `pypdf` was available. Note that two pages reference their content as an
*indirect array* of streams rather than a stream directly; a naive extractor
returns those pages blank and silently drops DBMS Units 2–5 and the Python
textbook list. `resolve_contents()` handles both forms.

---

## A note on the source

The official PDF is published at
`apsche.ap.gov.in/Pdf/major_minor1/Data%20Science%20Major.pdf`.

It has defects — truncated sentences, broken question numbering, and the two
missing-but-examined topics above. Where the notes reconstruct something, it is
**marked as a reconstruction** so you can tell it from the official text.
Always check against your own copy and your department's guidance.
