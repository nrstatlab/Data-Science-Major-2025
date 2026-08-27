# Study Plan — B.Sc. (Hons) Data Science Major

A week-by-week schedule for all ten courses of the Major, weighted by the
difficulty established in [`SYLLABUS-REVIEW.md`](SYLLABUS-REVIEW.md).

**The weighting is the point.** An even split across five units is the wrong
plan when one unit holds three units' worth of material. Where a unit gets more
weeks than its neighbours below, the review explains why.

---

## Semester I — 15 weeks

Two courses, 8 credits. The lightest semester of the degree; use the slack to
build programming habits that will carry you through the next two years.

| Week | Course 1 — Computer Fundamentals | Course 2 — Problem Solving Using C |
|:---:|---|---|
| 1 | Unit 1 — number systems: binary, decimal | Unit 1 — software types, compiler vs interpreter |
| 2 | Unit 1 — octal, hex, conversions | Unit 1 — algorithms, flowcharts, C history |
| 3 | Unit 1 — binary arithmetic, complements, generations | Unit 1 — tokens, data types, operators, I/O |
| 4 | Unit 2 — memory hierarchy, storage | Unit 2 — if, if-else, else-if ladder |
| 5 | Unit 2 — types of computers, networks | Unit 2 — switch, loops |
| 6 | Unit 2 — topologies, Internet basics | Unit 2 — break, continue, goto; **patterns** |
| 7 | **Revision 1** — Units 1–2 both courses | **Revision 1** |
| 8 | Unit 3 — Word: formatting, styles, tables | Unit 3 — 1-D arrays, memory representation |
| 9 | Unit 3 — mail merge, presentations, shortcuts | Unit 3 — 2-D arrays, matrix operations |
| 10 | Unit 4 — cell referencing, basic functions | Unit 3 — strings, string functions |
| 11 | Unit 4 — logical and text functions | **Unit 4 — pointers** ⚠ |
| 12 | Unit 4 — VLOOKUP, XLOOKUP, INDEX+MATCH | **Unit 4 — functions, recursion, parameter passing** ⚠ |
| 13 | Unit 5 — pivot tables, slicers | **Unit 4 — storage classes** ⚠ |
| 14 | Unit 5 — what-if analysis, dashboards | Unit 5 — dynamic memory, structures, unions |
| 15 | **Revision 2** — full syllabus | Unit 5 — file handling; **Revision 2** |

**Course 2 Unit 4 gets three weeks** (11–13). It is the hardest material in the
first year, and the syllabus mislabels it "Functions" when it opens with
pointers — see finding **D5**. Draw memory diagrams for every pointer example.

---

## Semester II — 15 weeks

Two courses, 8 credits. **The most important semester in the degree.** Python
and statistics are the foundation of everything from Semester III onward.

| Week | Course 3 — Python | Course 4 — Statistics |
|:---:|---|---|
| 1 | Unit 1 — features, modes, identifiers, types | Unit 1 — probability rules, axioms |
| 2 | Unit 1 — operators, precedence, I/O | Unit 1 — conditional probability, **Bayes** ⚠ |
| 3 | Unit 2 — control flow, `for…else` | Unit 1 — central tendency, dispersion |
| 4 | Unit 2 — functions, arguments, scope, lambda | Unit 2 — random variables, PMF/PDF/CDF |
| 5 | Unit 3 — strings and lists | Unit 2 — expectation, variance, moments |
| 6 | Unit 3 — tuples, sets | **Unit 3 — binomial, Poisson** |
| 7 | **Revision 1** — Units 1–3 | **Revision 1**; Unit 3 — geometric, negative binomial |
| 8 | Unit 3 — dictionaries, comprehensions | **Unit 3 — normal distribution, z-scores** |
| 9 | **Unit 4 — file handling, CSV** ⚠ | **Unit 3 — exponential, gamma, CLT** |
| 10 | **Unit 4 — exception handling** ⚠ | **Unit 4 — covariance, correlation** |
| 11 | **Unit 4 — classes, objects, encapsulation** ⚠ | **Unit 4 — regression, least squares** |
| 12 | **Unit 4 — inheritance, MRO, polymorphism** ⚠ | **Unit 4 — residuals, R², ANOVA** |
| 13 | Unit 5 — linked lists, stacks, queues | **Unit 5 — estimation, confidence intervals** |
| 14 | Unit 5 — priority queues; Tkinter | **Unit 5 — z-test, t-test** |
| 15 | **Revision 2** — full syllabus | **Unit 5 — chi-square, F-test, errors, power** |

### Why the weighting

**Course 3 Unit 4 gets four weeks (9–12), not two.** It contains file handling
*and* exception handling *and* the whole of object-oriented programming — three
units compressed into one. Compare Unit 1, which covers only literals and
operators. Finding **D6**.

**Course 4 Units 3, 4 and 5 get three weeks each.** Distributions, regression
and inference are where the marks and the difficulty both are.

**Bayes' theorem is scheduled in week 2** even though it is not in the syllabus
unit list, because it is examined. Finding **D1**.

---

## Semester III — 15 weeks

**Three courses, 12 credits — a 50% jump from Semesters I and II, and it lands
all at once.** Semesters III and IV are the heaviest in the programme. Plan for
it before week 1 rather than discovering it in week 6: the two-course rhythm
that worked for a year will not survive contact with three.

| Week | Course 5 — DBMS | Course 6 — Data Science with R | Course 7 — Web Technologies |
|:---:|---|---|---|
| 1 | Unit 1 — data vs information, file-based systems | Unit 1 — the data science process, lifecycle | Unit 1 — HTML structure, elements, attributes |
| 2 | Unit 1 — three-schema architecture, data independence | Unit 1 — EDA, feature engineering | Unit 1 — headings, images, **tables**, lists |
| 3 | Unit 2 — ER building blocks, entity and attribute types | Unit 2 — R and RStudio, types, operators | Unit 1 — **forms and every input type** |
| 4 | Unit 2 — relationships, cardinality, participation | Unit 2 — control structures, `apply`, functions | Unit 2 — selectors, combinators, the box model |
| 5 | Unit 2 — **reducing ER to tables**; EER | Unit 2 — packages, I/O (CSV, Excel, JSON) | Unit 2 — **position, float, Flexbox and Grid** |
| 6 | Unit 3 — relational model, keys, constraints | Unit 3 — data frames, lists, matrices | Unit 2 — pseudo-classes, transitions, CSS forms |
| 7 | **Revision 1**; Unit 3 — relational algebra | **Revision 1**; Unit 3 — **dplyr and tidyr** | **Revision 1**; Unit 3 — JS basics, variables, operators |
| 8 | **Unit 3 — functional dependencies, 1NF, 2NF** | Unit 3 — missing data, dates and times | Unit 3 — **strings, arrays, functions** |
| 9 | **Unit 3 — 3NF, BCNF, worked normalization** | **Unit 3 — ggplot2: grammar, aesthetics, geoms** | Unit 3 — objects, regular expressions, exceptions |
| 10 | Unit 4 — DDL, constraints, DML | Unit 3 — faceting, layering, exporting | **Unit 4 — the DOM and form elements** |
| 11 | Unit 4 — SELECT, aggregates, GROUP BY, HAVING | Unit 4 — simple and multiple regression | **Unit 4 — validation, responsive messages** |
| 12 | **Unit 4 — joins** (inner, left, self, three-table) | Unit 4 — accuracy, confusion matrix, ROC | Unit 4 — dialogs, windows, keyboard and mouse events |
| 13 | Unit 4 — set operations, subqueries, views | Unit 4 — K-Means, text mining, recommenders, ethics | Unit 5 — JSON syntax, parsing, nested access |
| 14 | Unit 5 — PL/SQL blocks, cursors, exceptions | **Unit 5 — time series: `ts`, decomposition, ACF/PACF** | Unit 5 — jQuery selectors, DOM manipulation, chaining |
| 15 | **Unit 5 — procedures, functions, TRIGGERS** ⚠; **Revision 2** | **Unit 5 — ARIMA, forecasting; plotly and Shiny** | Unit 5 — events, animations; **Revision 2** |

### Why the weighting

**Triggers are scheduled in week 15** despite being absent from the Course 5
Unit 5 syllabus list. Two of the six PL/SQL lab questions are trigger problems.
Finding **D2**.

**Course 5 weeks 8–9 (normalization) and week 12 (joins)** carry the most exam
weight in that course. Nothing else in DBMS is asked as reliably.

**Course 6 Unit 5 gets two weeks (14–15) and is still tight.** It fuses three
unrelated subjects — ARIMA time series, plotly interactivity, and building
Shiny web applications — any one of which would be a unit elsewhere. If you run
short, **ARIMA is the examinable half**; Shiny is the one that gets a
descriptive question rather than a technical one.

**Course 7 is the lightest of the three to *learn* and the heaviest to
*practise*.** Nothing in it is conceptually hard, and its 16 lab experiments
still take longer than the other two courses' labs combined, because each one
has to be built and looked at. Do the lab work in the week the topic is taught,
not in a block before the exam.

### Use Course 5 and Course 7 together

They are taught in the same semester and they meet in Semester IV. Course 5's
`SELECT … WHERE … GROUP BY` becomes Course 10's aggregation pipeline; Course
7's JSON becomes Course 10's document. Every hour you spend understanding
*why* a join exists in DBMS pays out twice more before the degree ends.

---

## Before Semester IV — a statistics refresher

**Two weeks, during the break before Semester IV begins.**

Regression, correlation and hypothesis testing are taught in Semester II. Their
first real application is Data Mining in **Semester IV**, and Machine Learning
is a Year III elective in **Semester V** — three semesters after the theory.
Statistical intuition decays without use. Finding **D10**.

| Day | Revise |
|---|---|
| 1–2 | Descriptive statistics, distributions ([formula sheet](notes/sem-2/course-4-statistical-foundations/formula-sheet.md)) |
| 3–4 | Correlation and regression; re-run [`04_correlation_regression.py`](labs/course-4-stats/python/04_correlation_regression.py) |
| 5–6 | Hypothesis testing; re-run [`05_inference_hypothesis_tests.py`](labs/course-4-stats/python/05_inference_hypothesis_tests.py) |
| 7–10 | Bridge the Excel/Python gap — redo the stats labs in Python (finding **D8**) |
| 11–14 | Python revision: NumPy and Pandas basics, ready for Course 9 |

That last block matters. The Semester II stats lab is entirely Excel, so you
arrive in Semester IV able to run a regression in a spreadsheet but not in the
language you spent a semester learning.

---

## Semester IV — 15 weeks

**Three courses, 12 credits again — and this is the semester the degree has
been building towards.** Course 9 is the one you will use in every job you take;
Course 8 is where the Semester II statistics finally gets applied; Course 10 is
Course 5 seen from the other side.

| Week | Course 8 — Data Mining | Course 9 — Python for Data Analysis | Course 10 — Document Database |
|:---:|---|---|---|
| 1 | Unit 1 — warehouse vs database, characteristics | **Unit 1 — the ndarray, dtypes, creating arrays** | Unit 1 — NoSQL, its history and features |
| 2 | Unit 1 — architecture, **star and snowflake schemas** | **Unit 1 — indexing, slicing, views vs copies** | Unit 1 — **CAP and BASE against ACID**; the four types |
| 3 | Unit 1 — fact constellation, **OLAP cube operations** | Unit 1 — broadcasting, ufuncs, `axis`, random | Unit 1 — RDBMS vs NoSQL; JSON and BSON; install |
| 4 | Unit 2 — KDD vs data mining, tasks | **Unit 2 — Series, DataFrame, Index objects** | Unit 2 — database/collection/document, BSON format |
| 5 | **Unit 2 — cleaning, missing data, dimensionality reduction** | **Unit 2 — `loc` vs `iloc`, boolean filtering** | Unit 2 — data types, ObjectId, the type traps |
| 6 | **Unit 2 — discretization, transformation, similarity measures** | Unit 2 — alignment, sorting, ranking, duplicates | **Unit 2 — schema design; embed or reference** |
| 7 | **Revision 1**; Unit 3 — association rules, support and confidence | **Revision 1**; Unit 3 — `read_csv` and the parameters that matter | **Revision 1**; Unit 3 — insert, and find with comparison operators |
| 8 | **Unit 3 — Apriori, worked by hand** | Unit 3 — JSON, `json_normalize`, Excel | Unit 3 — logical, element and evaluation operators |
| 9 | Unit 3 — Partition, Pincer-Search, DIC, **FP-Growth** | **Unit 3 — missing data, outliers, `map`/`apply`** | **Unit 3 — update, `replaceOne`, delete; arrays** |
| 10 | **Unit 4 — decision trees, best split, ID3 by hand** | Unit 4 — the `.str` accessor, regex, `extract` | Unit 4 — embedded vs normalized, the trade-offs |
| 11 | **Unit 4 — C4.5, CART, comparing classifiers** | Unit 4 — feature engineering, dummies, sampling | Unit 4 — the three relationships; design patterns |
| 12 | Unit 4 — rule-based, k-NN, **Bayesian classifiers** | **Unit 5 — merge and the four join types** | **Unit 4 — the aggregation framework, `$match`/`$group`** |
| 13 | **Unit 5 — K-Means to convergence; k-Medoid** | **Unit 5 — pivot, melt, stack, unstack** | Unit 5 — projection, sort, limit, skip; pagination |
| 14 | Unit 5 — hierarchical linkage, **DBSCAN**, BIRCH | Unit 5 — group-by; recompute the Course 4 examples | **Unit 5 — indexes: compound, multikey, text; ESR** |
| 15 | Unit 5 — STIRR, ROCK, CACTUS; **Revision 2** | Unit 5 — matplotlib, Seaborn, Plotly; **Revision 2** | Unit 5 — replication and failover; GridFS ⚠; **Revision 2** |

### Why the weighting

**Course 8 is arithmetic, not reading.** Apriori, ID3 and K-Means are all
*asked as hand traces*: given this table, compute the support, the information
gain, the centroids after two iterations. Weeks 8, 10 and 13 are the ones to
protect, and the only way to prepare is to work the traces on paper until the
arithmetic is automatic. The notes give each one fully worked, and
[`labs/course-8-datamining/`](labs/course-8-datamining/) recomputes every figure
in code so you can check your own work against something that runs.

**Course 9 Units 1 and 2 get five weeks between them (1–6).** Everything after
them assumes the ndarray and the DataFrame, and a student who is still unsure
whether `loc` is inclusive will lose time in every week that follows. This is
the course that pays out longest — treat it as the priority when three courses
collide.

**Course 10 Unit 4 gets three weeks (10–12)** because embed-or-reference is the
whole subject in one question, and the aggregation pipeline is the other half
of the paper.

**GridFS is scheduled in week 15** although it appears in no unit's topic list —
it survives only in Course Outcome 4 and lab experiment 18. Same shape as
findings **D1** and **D2**; here it is finding **D13**.

### Deliberately reinforce, rather than learning three subjects in parallel

The three courses overlap far more than their titles suggest, and using that is
the difference between 12 credits and three separate 4-credit efforts:

| When you meet | In another course you already have |
|---|---|
| Course 8's preprocessing (week 5) | Course 9's cleaning (week 9) — **the same operations, in code** |
| Course 8's K-Means (week 13) | Course 9's DataFrames; the lab does it in scikit-learn |
| Course 9's `merge` and join types (week 12) | Course 5's SQL joins — identical semantics, one exception: **Pandas joins NaN to NaN and SQL never joins NULL to NULL** |
| Course 10's aggregation (week 12) | Course 5's `GROUP BY`/`HAVING`, and Course 9's `groupby` |
| Course 10's documents (week 4) | Course 7's JSON |
| Course 8's classification metrics (week 11) | Course 6's confusion matrix and ROC |

**Say the connection out loud in the viva.** "This `$group` is a `GROUP BY`,
and this second `$match` is the `HAVING`" is worth more than a memorised
pipeline, in every one of these three courses.

---

## Weekly rhythm

A schedule you can actually keep beats an ambitious one you abandon in week 3.

| Day | Focus |
|---|---|
| **Mon–Fri** | Attend, then spend **1 hour per subject** the same evening consolidating |
| **Saturday** | **3 hours** — lab programs, typed and run, not copied |
| **Sunday** | **2 hours** — revise the week; **1 hour** — revise something from three weeks ago |

**The Sunday spaced-revision hour is the highest-value hour of the week.**
Re-reading this week's material feels productive and mostly is not; retrieving
three-week-old material is what moves it into long-term memory.

---

## Revision cycles

| Cycle | When | What |
|---|---|---|
| **Daily** | Same evening | Review the day's notes — 15 minutes |
| **Weekly** | Sunday | The week's units, plus one older topic |
| **Revision 1** | Week 7 | Units 1–3 of every course |
| **Revision 2** | Week 15 | Full syllabus, past papers |
| **Pre-exam** | Final fortnight | See below |

### The final fortnight

| Days | Activity |
|---|---|
| 14–11 | One full pass of every unit's notes |
| 10–8 | Formula sheets and the "mistakes that cost marks" section of each unit |
| 7–5 | **Past papers under timed conditions** |
| 4–3 | Practice problems; re-work anything you got wrong |
| 2–1 | Formula sheets and quick self-tests only — no new material |
| Exam eve | Sleep. Cramming past midnight costs more than it gains. |

**Past papers are the highest-value revision there is.** They reveal which
topics actually recur, how questions are phrased, and how marks are distributed
— none of which the syllabus tells you.

---

## Progress checklist

Tick a unit only when you can (a) explain it without notes and (b) solve a
problem on it unaided.

### Semester I

**Course 1 — Computer Fundamentals**
- [ ] Unit 1 — Number systems, evolution, block diagram, generations
- [ ] Unit 2 — Organization and networking
- [ ] Unit 3 — Word processing and presentations
- [ ] Unit 4 — Spreadsheet basics
- [ ] Unit 5 — Data analysis and visualization
- [ ] Lab — all 14 experiments

**Course 2 — Problem Solving Using C**
- [ ] Unit 1 — Introduction to programming
- [ ] Unit 2 — Control statements
- [ ] Unit 3 — Arrays and strings
- [ ] Unit 4 — Pointers, functions, storage classes ⚠
- [ ] Unit 5 — Dynamic memory, structures, files
- [ ] Lab — all 15 programs compiled and run

### Semester II

**Course 3 — Python Programming and Data Structures**
- [ ] Unit 1 — Basics
- [ ] Unit 2 — Control flow, functions, modules
- [ ] Unit 3 — Sequences, sets, dictionaries
- [ ] Unit 4 — Files, exceptions, OOP ⚠
- [ ] Unit 5 — Data structures and GUI
- [ ] Lab — all 18 programs run

**Course 4 — Statistical Foundations**
- [ ] Unit 1 — Probability and descriptive statistics (**including Bayes** ⚠)
- [ ] Unit 2 — Random variables, expectation, variance
- [ ] Unit 3 — Distributions
- [ ] Unit 4 — Correlation and regression
- [ ] Unit 5 — Inference and hypothesis testing
- [ ] Lab — all 15 experiments, **in Excel and in Python**

### Semester III

**Course 5 — Database Management Systems**
- [ ] Unit 1 — DBMS overview and three-schema architecture
- [ ] Unit 2 — ER and EER models
- [ ] Unit 3 — Relational model and normalization
- [ ] Unit 4 — SQL
- [ ] Unit 5 — PL/SQL (**including triggers** ⚠)
- [ ] Lab — all three experiments plus PL/SQL

**Course 6 — Data Science with R**
- [ ] Unit 1 — The data science process, lifecycle and EDA
- [ ] Unit 2 — R basics, control structures, functions, I/O
- [ ] Unit 3 — Data handling with dplyr and tidyr; ggplot2
- [ ] Unit 4 — Regression, evaluation, clustering, ethics
- [ ] Unit 5 — Time series and ARIMA; plotly; Shiny ⚠
- [ ] Lab — all 18 R scripts run in RStudio

**Course 7 — Web Technologies**
- [ ] Unit 1 — HTML structure, tables, forms
- [ ] Unit 2 — CSS: the box model, layout, Flexbox and Grid
- [ ] Unit 3 — JavaScript: strings, arrays, objects, regex
- [ ] Unit 4 — The DOM, validation, events
- [ ] Unit 5 — JSON and jQuery
- [ ] Lab — all 16 experiments built and opened in a browser

### Semester IV

**Course 8 — Data Mining**
- [ ] Unit 1 — Warehousing, schemas and OLAP
- [ ] Unit 2 — Preprocessing and similarity measures
- [ ] Unit 3 — Association analysis (**Apriori traced by hand**)
- [ ] Unit 4 — Classification (**ID3 traced by hand**)
- [ ] Unit 5 — Clustering (**K-Means traced to convergence**)
- [ ] Lab — all 15 experiments run in WEKA

**Course 9 — Python for Data Analysis and Visualization**
- [ ] Unit 1 — NumPy: ndarray, indexing, broadcasting
- [ ] Unit 2 — Pandas: Series, DataFrame, selection
- [ ] Unit 3 — I/O and cleaning
- [ ] Unit 4 — Strings and feature engineering
- [ ] Unit 5 — Wrangling, reshaping and visualization
- [ ] Lab — all 18 practicals run

**Course 10 — Document Oriented Database**
- [ ] Unit 1 — NoSQL, CAP and BASE
- [ ] Unit 2 — Architecture, BSON, data modeling
- [ ] Unit 3 — CRUD and MQL
- [ ] Unit 4 — Embedded vs normalized; aggregation
- [ ] Unit 5 — Indexing, pipelines, replication (**and GridFS** ⚠)
- [ ] Lab — all 20 experiments run against a real `mongod` or Atlas

---

## The four things that matter most

If you do nothing else from this plan:

1. **Type every lab program.** Reading code teaches nothing. All 52 programs in
   [`labs/`](labs/) run — type them, break them, fix them.
2. **Give Course 3 Unit 4 and Course 4 Units 3–5 double time.** They carry the
   difficulty and the marks.
3. **Study Bayes' theorem and database triggers**, though neither appears in
   its syllabus unit list. Both are examined.
4. **Do past papers under timed conditions**, starting a week before the exam.
