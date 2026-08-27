# Syllabus Review — B.Sc. (Hons) Data Science Major, APSCHE AY 2025-26

A check of the official syllabus documents, not a transcription of them. Every
finding below was verified against
[`docs/syllabus-extracted.md`](docs/syllabus-extracted.md) (Semesters I–II),
[`docs/syllabus-extracted-sem3-4.md`](docs/syllabus-extracted-sem3-4.md)
(Semesters III–IV) and
[`docs/syllabus-extracted-sem5.md`](docs/syllabus-extracted-sem5.md)
(Semester V); page numbers refer to the source PDF of the semester in
question.

**Read this before you start studying.** Three findings — **D1, D2 and D13** —
name topics that are *examined but not listed in the syllabus units*. If you
study only the unit lists, you will walk into those questions unprepared. D13
sits below with the document defects because that is what caused it, but its
consequence is the same as the other two.

---

## Summary

| ID | Finding | Severity |
|:---:|---|---|
| D1 | Bayes' theorem examined but absent from the units | **High** — affects marks |
| D2 | Database triggers examined but absent from the units | **High** — affects marks |
| D3 | Text truncated in three places in the official PDF | Medium |
| D4 | Lab question numbering broken in all three DBMS experiments | Low |
| D5 | Course 2 Unit 4 title does not match its content | Low |
| D6 | Course 3 Unit 4 carries roughly double a normal unit's load | Medium — affects planning |
| D7 | Course 3 Unit 5 fuses two unrelated subjects | Medium — affects planning |
| D8 | Statistics lab never uses Python, though Python is taught the same semester | Medium — affects skills |
| D9 | Conditional formatting duplicated across Course 1 Units 4 and 5 | Low |
| D10 | Three-semester gap between statistics and its first application | Medium |
| D11 | Course 2 activity list has an orphaned entry | Low |
| D12 | Bibliographies damaged in all five Semester III–IV courses | Medium — you cannot order the books |
| D13 | Course 10 Objective 4 is a fragment, and **GridFS and transactions are examined but absent from the units** | **High** — affects marks |
| D14 | Course 10 Unit 1's "Installation & Setup" topic has lost text | Medium |
| D15 | Course 8 numbers its units differently from every other course | Low |
| D16 | Course 8's objectives are unnumbered, unlike every other course's | Low |
| D17 | Course 11's Objective 3 stops mid-sentence | Medium |
| D18 | "Business IntelligenceI" — a stray capital in Course 11 Unit 1 | Low |
| D19 | Course 12 A has 3 objectives against 4 outcomes against 5 units | Medium — affects planning |
| D20 | Course 11 numbers its units in Roman numerals | Low |
| D21 | Course 12 B's reference books are numbered 3 and 4 | Low |
| D22 | Course 13 B's reference list has an empty entry 4 | Low |
| D23 | "SudoStudents" — two words merged in Course 13 A's activities | Low |
| D24 | "HadoopSpark" and "HBaseSpark" — separators lost, twice | Low |

D1–D11 come from the Semester I–II document, **D12–D16 from the Semester III–IV
document**, and **D17–D24 from the Semester V document**. Every one was found by
the same method — reading the extracted text rather than the formatted PDF,
where truncation is invisible.

### 🎯 The pattern that emerged once all three documents were read

**Nine of the twenty-four findings are the same defect: text lost at a word or
sentence boundary.** D3 (three instances), D13, D14, D17, D23 and D24 (two
instances).

Three separate documents, one recurring mechanism. That is no longer a
scattering of typos — it is a defect in how the PDFs were produced, and the
honest conclusion is that **all three need a proofreading pass against their
extracted text before being issued to students.**

**And a second, milder pattern:** D15 and D20 are the same inconsistency
(one course numbering its units differently from every other), D12, D21 and
D22 are all damaged bibliographies, and D16 and D19 are both objective lists
that do not follow the document's own five-and-five convention. Together they
suggest each course description was authored separately and never passed
through a single formatting pass.

**What is *not* wrong:** the credit arithmetic. Every course is 3 + 1 = 4 credits;
semester totals are 8, 8, 12, 12, 12, 8 for a **60-credit major**, consistent with
the structure table on pages 1–2.

---

## Findings that affect your marks

### D1 — Bayes' theorem is examined but never listed as a topic

**Page 20** (Course 4, Unit 1) lists the probability topics as: "Concept of
Uncertainty, Axioms and rules of probability, Conditional probability". Bayes'
theorem does not appear in Unit 1, or in any other unit of the course.

But **page 22** (Activities) prescribes: "Classroom Quiz (MCQs & short problems on
probability, conditional probability, **Bayes**)". And **page 23**, lab experiment
2, is a fragment reading only "a positive result." — the surviving tail of the
standard Bayes medical-testing problem ("*…given that the test returns a positive
result*").

**Consequence:** a topic that carries assessment weight sits outside the syllabus
list you would revise from.

**What to do:** study Bayes' theorem as though it were listed in Unit 1. It is
covered in [Course 4 Unit 1](notes/sem-2/course-4-statistical-foundations/unit-1.md),
where it is flagged as an off-syllabus-but-examined addition, with the
reconstructed medical-test problem worked in full.

### D2 — Database triggers are examined but never listed as a topic

**Page 25** (Course 5, Unit 5, PL/SQL) lists: "Introduction, Shortcomings of SQL,
Structure of PL/SQL, PL/SQL Language Elements, Data Types, Operators Precedence,
Control Structures, Steps to Create a PL/SQL Program, Iterative Control,
Procedures, Functions." **Triggers are not among them.**

Yet triggers are required in three separate places:

- **Page 24**, Course Objective 5: "…incorporating control structures, functions,
  procedures, and **database triggers**."
- **Page 27**, Activities: "Build a PL/SQL-based payroll or student grading system
  using: Procedures and functions, Control structures (IF, LOOP), **Triggers for
  automated updates**."
- **Page 37**, lab Section E items 5 and 6: "Create a trigger to prevent inserting
  employees with a salary less than 30,000" and "Create a trigger to avoid any
  transactions (insert, update, delete) on the EMP table on Saturday & Sunday."

Note also that Course Outcome 5 (page 24) drops triggers even though the Objective
names them — so the omission is consistent between the outcome and the unit, and
inconsistent with the assessment.

**What to do:** study triggers as part of Unit 5. Covered in
[Course 5 Unit 5](notes/sem-3/course-5-dbms/unit-5.md), with both lab triggers
written out.

---

## Defects in the document

### D3 — Truncated text in three places

1. **Page 20, Course Outcome 1** reads: "Apply the basic rules of probability,
   **conditisolve** problems involving uncertainty." Words have been dropped mid-
   sentence. The intended reading is almost certainly "…probability, conditional
   probability and Bayes' theorem to solve problems involving uncertainty" — which
   independently supports **D1**.
2. **Page 23, lab experiment 2** is just "a positive result." The question stem is
   gone. Reconstructed in the Course 4 lab notes.
3. **Page 2, elective note** reads: "students are required to select a pair of
   electives from one of the TWO specified domains. **is chosen**, courses 12 to 15
   to be chosen as 12 A, 13 A, 14 A and 15 A." The clause naming the two domains
   has been lost, so **the domains are never actually named anywhere in the
   document**. The A/B tracks can be inferred from the course titles (see
   [`SYLLABUS-MAP.md`](SYLLABUS-MAP.md) §1), but confirm the official names with
   your department before committing to a track in Year III.

### D4 — Lab question numbering is broken in all three DBMS experiments

Verified by extracting every numbered item:

| Experiment | Pages | Missing numbers |
|---|:---:|---|
| 1 — Inventory Management | 29 | 3, 13, 20, 22 |
| 2 — Online Bookstore | 31–32 | 12, 19 |
| 3 — Employee DB | 36–37 | 8 |
| 3 — Section E (PL/SQL) | 37 | 2 |

Some gaps lost their text entirely; others left orphans. PL/SQL item 2 is the
clearest case — its text survives as a dangling fragment, "If yes, print 'High
Salary'; Otherwise print 'Standard Salary'", with no question in front of it. The
intended question is evidently "write a PL/SQL block that checks whether an
employee's salary exceeds some threshold".

Section B of Experiment 1 also begins at 4, and items 6 and 8 are cut short
("Update the stock quantity of" — of what?).

**What to do:** the lab notes renumber cleanly and reconstruct the missing items,
marking each reconstruction as such so you can tell it from the official text.

### D5 — Course 2 Unit 4 is titled "Functions" but opens with pointers

**Page 10.** The unit is headed "Unit 4. Functions:" and its first topics are
"Pointers: Pointer data type, Pointer declaration, initialization, accessing
values using pointers. Pointer arithmetic, Pointers and arrays." Functions follow
*after* pointers, then storage classes.

Harmless to the content, but if you revise from unit titles you will not expect
pointers to be examined under "Functions". The notes cover them in the order
printed and flag the mismatch.

### D11 — Orphaned activity in Course 2

**Page 11.** Every activity in the document follows the pattern `Outcome: … /
Activity: … / Evaluation Method: …`. The "Recursive Problem Solver" activity
appears with no `Outcome:` heading above it, unlike its four siblings — its
outcome line was dropped. It maps to Course Outcome 4 (modular code using
functions, recursion and parameter passing).

### D12 — Bibliographies are damaged in all five Semester III–IV courses

Every one of the five courses has at least one book entry that is unusable as
written. This is worse than it sounds: a bibliography exists so you can *order
the book*, and none of these five entries names one you could order.

| Course | Page | What the document says | What is missing |
|---|:---:|---|---|
| 6 — Data Science with R | 5 | `Textbooks 1. …Springer, 2nd Edition, 2021 2. Reference Books` | **Textbook 2 is empty** — the number survives, the entry does not |
| 7 — Web Technologies | 9 | `4. JSON at Work Media. Reference Books 1. 2. An Introduction to HTML…` | Textbook 4 has lost its **author** (Tom Marrs) and its publisher is a bare "Media"; **reference book 1 is empty** |
| 9 — Python for Data Analysis | 19 | `1. …pandas, NumPy, and Jupyter, Wes 2. Python Programming…` | The author is cut mid-name at "**Wes**" — Wes McKinney |
| 10 — Document Oriented Database | 23 | `Textbooks: 1. MongoDB: The Definitive Guide, …Chodorow, 2. MongoDB Recipes…` | Textbook 1 has **no publisher, edition or year** |
| 10 — Document Oriented Database | 23 | `Reference Books: 1. MongoDB in Action… 2. 3. M Web Resources:` | **Reference books 2 and 3 are gone**, leaving an orphaned "**M**" |

**What to do:** the four books that *are* fully named are the ones to buy. Each
course README in this repository lists them with the missing details filled in
and marked as reconstructed, so you can tell my additions from the document's
own text.

### D13 — Course 10's Objective 4 is a fragment, and GridFS and transactions go missing with it

**Page 21.** The five course objectives read:

> 1. To introduce students to the concepts of NoSQL databases…
> 2. To provide hands-on experience with MongoDB…
> 3. To develop skills in schema design, data modeling…
> **4. replication, and transactions.**
> 5. To prepare students for real-world applications of MongoDB…

Objective 4 has lost everything before "replication" — no verb, no capital, no
sentence. Course **Outcome** 4 on the same page survives intact and shows what
was intended: "Utilize advanced features like indexing, aggregation, GridFS,
and transactions to optimize data handling." So the objective was almost
certainly "To familiarise students with indexing, aggregation, GridFS,
replication, and transactions."

**Why this matters and D15 does not.** Unit 5's topic list ends at "Replication
Concepts: Replica sets, failover, consistency". **Neither GridFS nor
transactions appears in it, or in any other unit.** Both survive only in Course
Outcome 4, in the activity list on page 24, and in the practical list:

| Topic | Appears in | Appears in a unit? |
|---|---|:---:|
| **GridFS** | Outcome 4; **lab experiment 18** | **No** |
| **Transactions** | Outcome 4; the truncated Objective 4; **lab experiment 19** | **No** |

So a student who revises from the unit lists alone meets neither, and then
finds two of the twenty lab experiments are about them. That is the same shape
of problem as **D1** and **D2**. Both are covered in
[Unit 5](notes/sem-4/course-10-document-database/unit-5.md) and in lab
experiments [18](labs/course-10-mongodb/18_gridfs.js) and
[19](labs/course-10-mongodb/19_transactions.js) for that reason — and both of
those lab files also say plainly that they need a running server, which is the
other half of the answer when an examiner asks you to demonstrate them.

### D14 — Course 10 Unit 1's "Installation & Setup" topic has lost text

**Pages 21–22.** Unit 1's topic list ends across the page break as:

> …Introduction to JSON & BSON
>
> **Installation & Setupservice), connecting via Mongo shell or GUI.**

Two words have been welded together ("Setup" + "service"), and a closing
parenthesis survives with no opening one — so an entire parenthetical clause
has been dropped. Judging by the surviving fragment it listed the install
routes and named the server process, something like "Installation & Setup
(installing MongoDB, starting the `mongod` service), connecting via Mongo shell
or GUI."

[Unit 1 §1.9](notes/sem-4/course-10-document-database/unit-1.md) covers what it
evidently intended — Atlas, Docker and a local install, the `mongod` service,
and connecting with `mongosh` or Compass — and says in the section itself that
the source text is damaged.

### D15 — Course 8 numbers its units differently from every other course

**Pages 11–14.** Data Mining heads its units `Unit-1:`, `Unit-2:` … with a
hyphen and a colon. All nine other courses in both documents use `Unit 1.`,
`Unit 2.` … with a space and a full stop.

Cosmetic, and listed only because it is the kind of inconsistency that suggests
this course's text was pasted in from a different source document — which is
also the most likely explanation for **D16**.

### D16 — Course 8's objectives are unnumbered, unlike every other course's

**Page 11.** Every course in both documents numbers its five objectives 1–5.
Course 8 runs them together as unnumbered sentences:

> Course Objectives: Provide an understanding of data warehousing concepts…
> Develop knowledge of data mining fundamentals… Introduce students to
> association rule mining algorithms… Enable learners to apply classification
> techniques… Equip students with knowledge of clustering paradigms…

There are still exactly five, and they still map one-to-one onto the five
outcomes and the five units, so nothing is *missing* — but if an examiner asks
you to "state the third course objective", the document does not tell you which
one that is. Counting in printed order gives association rule mining, which is
also Unit 3 and Outcome 3.

---

## Design and sequencing issues

### D6 — Course 3 Unit 4 carries roughly double the load of a normal unit

**Page 15.** Unit 4 is "File Handling, Exception Handling & Object Oriented
Programming" and contains:

- file types, paths, open/close, read/write, CSV, `os`/`pathlib`
- syntax errors, built-in exceptions, `try-except`, `raise`, user-defined
  exceptions, assertions
- classes, objects, attributes, methods, constructors, destructors
- encapsulation with private and public members
- inheritance — single, multilevel **and** multiple — plus method overriding

That is three teachable units compressed into one. OOP alone is normally a full
unit. Compare Unit 1, which covers only literals, variables and operators.

**What to do:** budget roughly twice the study time for Unit 4 as for Unit 1. The
[study plan](STUDY-PLAN.md) already does this, splitting it across three weeks.

### D7 — Course 3 Unit 5 fuses two unrelated subjects

**Pages 15–16.** Unit 5 is "Abstract Data Structures and GUI Programming" —
linked lists, stacks, queues and priority queues, *and* Tkinter widgets and event
handling. These share nothing conceptually. Data structures are algorithmic and
carry the exam weight; Tkinter is applied and carries the lab weight (2 of the 18
lab programs).

**What to do:** treat them as two separate topics. The notes split
`unit-5.md` into two clearly divided halves.

### D8 — The statistics lab never touches Python

**Page 23.** Course 4's lab is headed "Advanced Spreadsheets/Excel Lab/PSPP Open
Source", and all 15 experiments are spreadsheet exercises — `NORM.DIST`,
`NORM.INV`, `EXPON.DIST`, the Data Analysis ToolPak, the Regression tool.

Meanwhile Course 3 teaches Python **in the same semester**. The two courses never
meet. Python-based data analysis waits until Semester IV, Course 9 ("Python for
Data Analysis and Visualization").

This is defensible pedagogically — a spreadsheet makes the arithmetic of variance
or a t-test visible in a way `scipy.stats.ttest_ind()` does not. But it means you
finish Semester II able to compute a regression in Excel and not in the language
you just spent a semester learning.

**What to do:** do each experiment **twice** — once in Excel exactly as prescribed
(that is what the exam tests) and once in Python (that is what the degree is for).
The Course 4 lab notes give both versions of all 15.

### D9 — Conditional formatting appears twice in Course 1

**Page 4.** Unit 4 lists "Data Handling: Sorting, filtering, **conditional
formatting**". Unit 5 then opens with "**Conditional Formatting**: Custom rules,
Color scales, Icon sets, Data bars" as a headline topic. Minor, but worth knowing
that Unit 5's treatment is the substantive one.

### D10 — Three-semester gap between statistics and its first real application

Regression, correlation and hypothesis testing are taught in **Semester II**
(Course 4). Their first genuine application is Data Mining in **Semester IV**, and
Machine Learning is a Year III elective in **Semester V** — three semesters after
the theory.

Statistical intuition decays without use. The [study plan](STUDY-PLAN.md)
schedules a short Course 4 refresher before Semester IV begins, so Data Mining
does not start with re-learning what a p-value is.

### D17 — Course 11's Objective 3 stops mid-sentence

**Page 5.** The third objective of Business Intelligence Tools reads:

> 3. Enable students to clean, transform and model data using Power Query and

and then stops. The verb, the object and the full stop are all missing.

**What was almost certainly there:** "…using Power Query and DAX", since DAX
is the whole of Unit 3 and Outcome 3 names it. But that is an inference, and
if an examiner asks you to state Objective 3 the document cannot tell you.

**This is the third truncation of the same kind** — see **D3** (three in the
Semesters I–II document) and **D13** (Course 10's Objective 4). Four
truncations across two documents in the same position — the end of a numbered
objective — suggests a systematic problem in whatever produced the PDF rather
than four independent typing errors.

### D18 — "Business IntelligenceI" — a stray capital in Course 11 Unit 1

**Page 5.** Unit 1's topic list reads:

> Business Intelligence: Definition, Scope, and Evolution, Business
> **IntelligenceI** vs. Data Analytics vs. Data Science, BI…

A stray capital I is welded onto "Intelligence" the second time it appears.
Trivially cosmetic — but it sits in the *first line of the first unit of the
first course of the semester*, which is the last place a proofreading pass
should miss.

### D19 — Course 12 A has three objectives against four outcomes against five units

**Pages 8–9.** Every other course in both documents has **five objectives and
five outcomes**, mapping one-to-one onto five units. Machine Learning has
**three objectives and four outcomes** — and five units.

| Course | Objectives | Outcomes | Units |
|---|---:|---:|---:|
| 11 | 5 | 5 | 5 |
| **12 A** | **3** | **4** | **5** |
| 12 B | 5 | 5 | 5 |
| 13 A | 5 | 5 | 5 |
| 13 B | 5 | 5 | 5 |

**All four outcomes do have activities and evaluation methods**, so nothing is
left outside continuous assessment. What breaks is the *mapping*: Outcome 4
carries both Unit 5's clustering algorithms **and** "identify suitable machine
learning approaches for specific application domains", which is the case-study
material. Two units' worth of content, one outcome.

**The practical consequence for a student:** Unit 5 is the largest unit in the
course by topic count — k-Means, k-Medoids, hierarchical clustering, DBSCAN,
internal and external validation, and four case studies — and it is weighted
in the outcomes as half of one. Do not read that as permission to give it half
the time. [The Course 12 A notes](notes/sem-5/course-12a-machine-learning/unit-5.md)
give it the same weight as the other four.

**And Outcome 4 has no full stop** — it runs straight into "Unit 1." on the
same line — which is the same boundary defect as D17 and D23, in a milder
form.

### D20 — Course 11 numbers its units in Roman numerals

**Pages 5–6.** Business Intelligence Tools heads its units `Unit-I:`,
`Unit-II:` … Every other course in the Semester V document uses `Unit 1.` with
an Arabic numeral, a space and a full stop.

This is **D15** again in a different course — Data Mining used `Unit-1:` where
everything else used `Unit 1.` — and it is the same signal: these course
descriptions were assembled from separately-authored sources and never passed
through a single formatting pass.

### D21 — Course 12 B's reference books are numbered 3 and 4

**Page 13.** The bibliography reads:

> Textbooks
> 1. Hadoop: The Definitive Guide…
> 2. Learning Spark, 2nd Edition…
> Reference Books
> **3.** BIG DATA, Black Book™…
> **4.** BIG DATA and ANALYTICS, Seema Acharya…

The reference list continues the textbook numbering instead of restarting at
1. Harmless in itself — but **D12** found the Semester III–IV bibliographies
damaged in all five courses, and this is the same section behaving oddly
again.

### D22 — Course 13 B's reference list has an empty entry 4

**Page 22.** The list runs:

> 3. Cloud Computing for Data Analysis, Noah Gift, Alfredo Deza…
> **4.**
> 5. Machine Learning in the AWS Cloud: Amazon SageMaker, Abhishek Mishra…

**Entry 4 is a number with nothing after it.** A book was removed, or failed to
paste, and the numbering was never closed up. The list claims five references
and supplies four.

### D23 — "e.g., SudoStudents" — a merged word in Course 13 A's activities

**Page 18.** The Outcome 4 activity reads:

> Give students a logic puzzle (e.g., SudoStudents write propositional and/or
> FOL statements, draw inference chains…

**"Sudoku)" and "Students" have merged into "SudoStudents"**, taking the
closing bracket with them. The intended text is almost certainly "(e.g.,
Sudoku). Students write…".

**Same defect class as D3, D13, D14 and D17**, and the fourth instance of text
being lost at a boundary in this pair of documents.

### D24 — "HadoopSpark" appears twice in Course 12 B

**Pages 12 and 13.** Objective 5 and Outcome 5 both read "**HadoopSpark**
integration", and the case-study activity reads "**HBaseSpark** integration".

The missing character is presumably a hyphen or a slash — "Hadoop-Spark",
"Hadoop/Spark". **Two words joined where a separator was lost**, which is the
same mechanism as D23 and D14.

**Counting the whole class:** across the two documents there are now **nine**
places where text has been lost at a word or sentence boundary — D3 (three),
D13, D14, D17, D23, and D24 (two). That is no longer a scattering of typos; it
is a defect in the production of the documents, and the honest summary is that
**both PDFs need a proofreading pass before they are issued to students.**

---

## What the five Semester V courses do well

The defects above are worth recording, but a review that lists only faults
misrepresents the document. Four things in Semester V are genuinely well done.

**The elective tracks are coherent.** Track A (Machine Learning → AI → Neural
Networks → NLP) and Track B (Big Data → Cloud → Time Series → Data
Engineering) each build properly, and the constraint that you stay in one
domain across both semesters is correct — the Semester VI courses genuinely
depend on their Semester V predecessors.

**Course 12 A's unit ordering is right.** Putting *model preparation and
evaluation* (Unit 2) **before** any algorithm is unusual and correct. Most
syllabi teach algorithms first and evaluation last, which is how students
learn to quote accuracy without a base rate.

**Course 13 B ends on monitoring and cost.** Unit 5 covers deployment,
monitoring, scalability and cost optimisation as examinable content rather
than as an afterthought. That is more realistic than most cloud syllabi, which
stop at "deploy the model".

**Course 12 B pairs every high-level tool with its foundation.** MapReduce
before Hive, HDFS before HBase, and the Spark comparison stated in terms of
what MapReduce does between stages. A student who follows the order will
understand *why* Spark replaced MapReduce rather than merely that it did.

---

## Verification notes for this repository

The lab code in [`labs/`](labs/) was checked as follows. Run
`bash tools/verify_all.sh` to reproduce all of it.

**What runs, and is asserted**

| Course | Language | Status |
|---|---|---|
| 2 | C (15 programs) | **Compiled and run.** `gcc -Wall -Wextra`, no warnings, output verified against expected results. |
| 3 | Python (16 of 18) | **Run.** Python 3.11. |
| 4 | Python (15 equivalents) | **Run**, and their results checked against the notes' hand-computed figures. |
| 5 | SQL — DDL/DML/queries | **Executed** against SQLite via `tools/run_sql_labs.py`, with schema and the official sample data loaded. |
| 6 | Python (14 equivalents) | **Run.** One per R script that has a Python counterpart. |
| 7 | JavaScript + DOM (16 experiments) | **Run under jsdom**, 184 assertions on the resulting DOM state, via `tools/run_web_labs.js`. |
| 8 | scikit-learn / mlxtend (15 experiments) | **Run**, and every hand trace in the notes — Apriori's itemsets, ID3's information gains, K-Means to convergence — reproduced by executing code. |
| 9 | NumPy / Pandas (18 practicals) | **All run**, outputs asserted. Nothing in this course is desk-checked. |
| 10 | mongomock (16 of 20 experiments) | **Run**, every query and pipeline asserted, via `tools/run_mongo_labs.py`. |
| 11 | Python (BI semantics) | **Run** via `tools/run_bi_labs.py`. Every DAX, Power Query and LOD figure in the notes was computed, not quoted. |
| 12 A | scikit-learn (12 practicals) | **All run** via `tools/run_ml_labs.py`. **No file in this course is marked NOT EXECUTED** — nothing it needs is blocked. |
| 12 B | Python, DuckDB, fastavro, pyarrow, **PySpark** (14 of 17) | **Run** via `tools/run_bigdata_labs.py`, including a **real `SparkSession`** with a real shuffle, and **real Avro and Parquet files**. |
| 13 A | pytholog + Python (7 programs, 19 experiments) | **Run** via `tools/run_ai_labs.py`. **Five experiments execute as real logic programs** through SLD resolution. |
| 13 B | Python, DuckDB, scikit-learn, `http.server` (7 programs, 15 experiments) | **Run** via `tools/run_cloud_labs.py`, including a **real web server**, a **real ETL into a real columnar warehouse**, and a **real REST endpoint** serving a real model. |

**What does not run, and says so in its own file header**

| Course | What | Why, and what stands in for it |
|---|---|---|
| 3 | Tkinter (2 programs) | `tkinter` is not installed here, so `python3 -m py_compile` is the strongest check available. |
| 4 | Excel and PSPP walkthroughs | Not executable. Written as step-by-step instructions with exact formulas; the Python equivalents of the same 15 experiments were run. |
| 5 | PL/SQL (procedures, functions, triggers) | The syllabus targets Oracle PL/SQL; SQLite cannot run it and no Oracle instance is available. Written to Oracle syntax and reviewed by hand — verify on your college's installation. |
| 6 | R (18 scripts) | R cannot be installed: the Debian repositories are blocked by this environment's egress policy. The scripts are structurally checked, and 14 have executed Python equivalents. |
| 8 | WEKA (15 click-paths) | WEKA cannot be installed here. Each experiment documents the WEKA panel, filter and parameters, alongside the scikit-learn equivalent that runs. |
| 10 | mongosh (all 20 scripts) | `mongod` cannot be installed — same egress policy. Each script is the one to run in the lab exam; 16 have a mongomock half that executes the same logic. |
| 10 | Replication, GridFS, transactions (3 experiments) | These need a server, and mongomock is a library. **No runnable half exists**, and `tools/run_mongo_labs.py` asserts that each of the three still carries its NOT EXECUTED marker. |
| 11 | Power BI and Tableau (all 15 click-paths) | Neither tool runs on Linux, and Tableau Public needs an account. Each experiment documents the exact click-path; the semantics behind every figure were computed in Python. |
| 12 B | Hadoop, Hive, Pig, Sqoop, Flume, HBase, ZooKeeper (15 files) | Same egress policy as R and `mongod`. Each file names the tool it needs and the runnable half that verifies its logic; `tools/run_bigdata_labs.py` asserts the markers. |
| 13 A | SWI-Prolog (all 16 `.pl` files) | Not installable — same egress policy. The `.pl` file is the deliverable; 7 Python halves verify the logic, and five of them run through a real Prolog engine. |
| 13 B | AWS, Azure, GCP and VMware (14 files) | **No cloud account exists for this repository and none was created** — signing up requires a payment card and accepts a billing relationship. Every provider claim is documented, never demonstrated. |

**The rule the whole repository follows:** every numeric claim in the notes is
checked by running code, and anything that genuinely cannot run says
**NOT EXECUTED** in its own first lines rather than implying a test that never
happened.

That discipline found **more than fifty errors of my own** while these notes
were being written — four in Courses 1–5, three in Course 6, six in Course 8,
seven in Course 9, two in Course 10, and roughly thirty more across the five
Semester V courses. Every one would otherwise have been a wrong worked example
a student revised from.

**And it caught more than arithmetic.** Several results came out contradicting
what I had expected to write, and the notes report the measurement rather than
the expectation:

- **Random forest lost to a single decision tree** on an iris split
  (0.8889 against 0.9778), and the cross-validated figures overlap almost
  entirely — so the honest conclusion is that the models are not
  distinguishable on that data.
- **Scaling made k-NN worse** on iris — **0.9778 unscaled against 0.9111
  scaled** — even though it transformed a synthetic case from 0.5500 to
  0.9750. Iris's four features already share a scale, so standardising only
  discarded information.
- **Adjusted R² rose by chance in 119 of 300 trials**, so a single-dataset
  demonstration of "adjusted R² penalises useless predictors" would have been
  luck rather than evidence; the notes run the distribution instead.
- **Hive's three-bucket hash left one bucket empty** with three store names.
- **The MapReduce combiner saved only 18.75%**, because the splits are tiny —
  which is the honest way to teach that its value scales with split size.
- **Autoscaling cost more than fixed capacity** in one measured configuration
  (188 instance-hours against 168), directly contradicting the slogan.
- **pytholog gives a wrong answer** for `cousin/2` through a nested derived
  predicate, returning a person as his own cousin — documented as an engine
  limitation, with the correct flat formulation shown alongside.
- **Parquet is 4.8× LARGER than CSV at nine rows**, and its 303× advantage on
  repeated data falls to 12× once every row differs.

**Reporting a result that undercuts the point you were about to make is the
whole value of executing the code.** A note that only ever confirms its own
claims has not been checked; it has been decorated.

`tools/check_coverage.py` is held to the same standard, and it had to be fixed
before it could be trusted: it was matching its keywords against the syllabus
line each note file quotes in its header, so **19 of 464 topics were passing
without a word being written about them**. Stripping the header before
searching exposed three genuine gaps in Courses 1, 3 and 7, and three more in
Course 10. All six are now written. The check currently reports **672 of 672
topics across 50 unit files**.
