# Syllabus Map — B.Sc. (Hons) Data Science, Major

**Issuing body:** Andhra Pradesh State Council of Higher Education (APSCHE)
**Prepared by:** Adikavi Nannaya University, Rajahmundry
**Effective:** AY 2025-26 · 4-Year UG Honours · Course structure for Semesters I–VI

Sources, both extracted verbatim:

| Document | Covers | Extracted text |
|---|---|---|
| [`docs/Data-Science-Major-Sem1-2.pdf`](docs/Data-Science-Major-Sem1-2.pdf) | Programme structure + Courses 1–5 | [`syllabus-extracted.md`](docs/syllabus-extracted.md) |
| [`docs/Data-Science-Major-Sem3-4.pdf`](docs/Data-Science-Major-Sem3-4.pdf) | Courses 6–10 | [`syllabus-extracted-sem3-4.md`](docs/syllabus-extracted-sem3-4.md) |

---

## 1. Programme structure (Semesters I–VI)

Every course follows the same shape: **3 credits theory (3 hrs/week) + 1 credit
lab (2 hrs/week) = 4 credits**.

| Year | Sem | # | Course | Hrs/wk | Credits |
|:---:|:---:|:---:|---|:---:|:---:|
| I | I | 1 | Computer Fundamentals and Office Automation | 3 | 3 |
| | | | Computer Fundamentals and Office Automation Lab | 2 | 1 |
| I | I | 2 | Problem Solving Using C | 3 | 3 |
| | | | Problem Solving Using C Lab | 2 | 1 |
| I | II | 3 | Python Programming and Data Structures | 3 | 3 |
| | | | Python Programming and Data Structures Lab | 2 | 1 |
| I | II | 4 | Statistical Foundations for Data Science | 3 | 3 |
| | | | Statistical Foundations for Data Science Lab | 2 | 1 |
| II | III | 5 | Database Management Systems | 3 | 3 |
| | | | Database Management Systems Lab | 2 | 1 |
| II | III | 6 | Data Science with R | 3 | 3 |
| | | | Data Science with R Lab | 2 | 1 |
| II | III | 7 | Web Technologies | 3 | 3 |
| | | | Web Technologies Lab | 2 | 1 |
| II | IV | 8 | Data Mining | 3 | 3 |
| | | | Data Mining Lab | 2 | 1 |
| II | IV | 9 | Python for Data Analysis and Visualization | 3 | 3 |
| | | | Python for Data Analysis and Visualization Lab | 2 | 1 |
| II | IV | 10 | Document Oriented Database | 3 | 3 |
| | | | Document Oriented Database Lab | 2 | 1 |
| III | V | 11 | Business Intelligence Tools | 3 | 3 |
| | | | Business Intelligence Tools Lab | 2 | 1 |
| III | V | 12 A / B | **Elective** — Machine Learning **or** Big Data Technologies | 3 | 3 |
| | | | (matching lab) | 2 | 1 |
| III | V | 13 A / B | **Elective** — Artificial Intelligence **or** Cloud Computing for Data Science | 3 | 3 |
| | | | (matching lab) | 2 | 1 |
| III | VI | 14 A / B | **Elective** — Neural Networks and Deep Learning **or** Time Series Analysis and Forecasting | 3 | 3 |
| | | | (matching lab) | 2 | 1 |
| III | VI | 15 A / B | **Elective** — Natural Language Processing **or** Data Engineering & MLOps | 3 | 3 |
| | | | (matching lab) | 2 | 1 |

### Credit totals

| Semester | Courses | Credits |
|:---:|:---:|:---:|
| I | 1, 2 | 8 |
| II | 3, 4 | 8 |
| III | 5, 6, 7 | 12 |
| IV | 8, 9, 10 | 12 |
| V | 11, 12, 13 | 12 |
| VI | 14, 15 | 8 |
| **Total (Major)** | **15 courses** | **60** |

Verified against the structure table on pages 1–2; the arithmetic is internally
consistent.

### Elective rule (page 2)

In Year III you choose a **pair of electives from one of two domains**, and must
**stay in the same domain across both Semester V and VI**. Choosing the A track
means taking 12A, 13A, 14A and 15A.

| | Sem V (12) | Sem V (13) | Sem VI (14) | Sem VI (15) |
|---|---|---|---|---|
| **Track A** | Machine Learning | Artificial Intelligence | Neural Networks and Deep Learning | Natural Language Processing |
| **Track B** | Big Data Technologies | Cloud Computing for Data Science | Time Series Analysis and Forecasting | Data Engineering & MLOps |

Read Track A as the **modelling / AI** path and Track B as the **infrastructure /
engineering** path. The PDF's sentence naming the two domains is truncated — see
[`SYLLABUS-REVIEW.md`](SYLLABUS-REVIEW.md) finding **D3** — so confirm the official
domain names with your department before choosing.

---

## 2. Detailed unit map (Courses 1–13)

These **fifteen course numbers** — Courses 1–11 plus both halves of each
Semester V elective pair, 12 A/B and 13 A/B — cover the whole Major through
Semester V and have full syllabi in the three source documents. **You take
thirteen of them**: Courses 1–11 and one track's pair. **Courses 14 and
15, the Semester VI elective pairs, appear as titles and credits only**, so
they cannot be mapped until that document is published.

### Course 1 — Computer Fundamentals and Office Automation (Sem I)
Notes: [`notes/sem-1/course-1-computer-fundamentals/`](notes/sem-1/course-1-computer-fundamentals/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Number Systems, Evolution, Block Diagram and Generations | Binary/decimal/octal/hexadecimal and conversions; evolution of computers; block diagram (Input, Output, Memory, CPU = ALU + CU); generations I–V |
| 2 | Basic organization and N/W fundamentals | Functional components, I/O devices, storage types, memory hierarchy; micro/mini/mainframe/super; networks (LAN/WAN/MAN), topologies (star/ring/bus); Internet basics — IP address, domain name, browser, email, WWW |
| 3 | Word Processing and Presentations | MS Word / Google Docs — formatting, styles, tables, mail merge; PowerPoint / Slides — design, animations, transitions; resumes, reports, brochures; keyboard shortcuts |
| 4 | Spreadsheet Basics | Rows/columns/cells, cell referencing; SUM, AVERAGE, IF, COUNT; charts; sorting, filtering, conditional formatting; text functions (LEFT, RIGHT, MID, LEN, TRIM, CONCAT, TEXTJOIN); logical (IF, AND, OR, IFERROR); lookup (VLOOKUP, HLOOKUP, XLOOKUP, INDEX, MATCH) |
| 5 | Data Analysis and Visualization | Conditional formatting (custom rules, colour scales, icon sets, data bars); pivot tables and pivot charts; data validation; what-if analysis (Goal Seek, Scenario Manager, data tables); interactive dashboards, slicers, combo charts, sparklines; named ranges, freeze panes, split view |

**Textbooks:** Reema Thareja, *Fundamentals of Computers* (OUP, 2e) · V. Rajaraman, *Fundamentals of Computers* (PHI) · Peter Norton, *Introduction to Computers* (McGraw Hill) · Randy Nordell, *Microsoft Office 365 In Practice* (McGraw Hill)
**References:** Alexander & Kusleika, *Excel 2021 Bible* (Wiley) · Doug Lowe, *Networking All-in-One For Dummies* (Wiley) · learn.microsoft.com · Google Workspace Learning Center

### Course 2 — Problem Solving Using C (Sem I)
Notes: [`notes/sem-1/course-2-problem-solving-c/`](notes/sem-1/course-2-problem-solving-c/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to computer programming | Types of software; compiler vs interpreter; machine/assembly/high-level; flowcharts and algorithms; history and features of C; tokens — variables, keywords, identifiers, constants, data types; rules for variable names; operators; structure of a C program; formatted and unformatted I/O |
| 2 | Control statements | `if`, `if-else`, `else-if` ladder, `switch`; `while`, `for`, `do-while`; `break`, `continue`, `goto` |
| 3 | Derived data types in C | 1-D arrays — declaration, initialization, memory representation; 2-D arrays — same; strings — declaring and initializing, string handling functions, character handling functions |
| 4 | Functions (opens with pointers — see review **D5**) | Pointer data type, declaration, initialization, dereferencing; pointer arithmetic; pointers and arrays; function prototype, definition, calling; `return`; nesting; categories of functions; recursion (basic); parameter passing by value and by address; local vs global variables; storage classes — auto, extern, static, register |
| 5 | Dynamic Memory Management | `malloc`, `calloc`, `realloc`, `free`; structures — members, access, nested, array of structures, structures with functions and pointers; unions and how they differ from structures; text files — modes, open, read, write, close |

**Textbooks:** E. Balagurusamy, *Programming in ANSI C* (TMH, 6e) · Reema Thareja, *Computer Fundamentals and Programming in C* (OUP)
**References:** Y. Kanetkar, *Let Us C* (BPB) · Griffiths & Griffiths, *Head First C*

### Course 3 — Python Programming and Data Structures (Sem II)
Notes: [`notes/sem-2/course-3-python-data-structures/`](notes/sem-2/course-3-python-data-structures/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Basics of Python Programming | Introduction and features; interactive vs script mode; identifiers, naming conventions, keywords; built-in data types; literals (int, float, complex, boolean, string); variables, operators, expressions; assignment; I/O statements; lines, comments, indentation; operator classification — arithmetic, relational, logical, bitwise, assignment, augmented assignment, identity; precedence |
| 2 | Control Flow, Functions & Modules | `if` / `if-else` / `if-elif-else`; `while`, `for`, nested loops; `break`, `continue`, `pass`, `else` with loops; defining and invoking functions; `return`; scope — local, global, nested; arguments — required, positional, default, variable-length; `main()`; docstrings; recursion; lambda; library functions; modules — `import`, `from..import`, creating modules, namespaces |
| 3 | Sequence, Set, Mapping Types | Strings — indexing, slicing, immutability, operators, traversal, accumulation, formatting, methods; lists — indexing, slicing, methods, mutability, add/update/delete/search/copy/traverse, comprehension; tuples — operations, immutability, tuple assignment, arrays; sets — methods, mathematical operations, frozenset, comprehension; dictionaries — methods, operations, traversal, comparison |
| 4 | File Handling, Exception Handling & OOP **(overloaded — see review D6)** | File types, paths, open/close, read/write, CSV, `os`/`pathlib`; syntax errors, built-in exceptions, `try-except`, `raise`, user-defined exceptions, assertions; classes, objects, attributes, methods, constructors, destructors; encapsulation — private/public members; inheritance — single, multilevel, multiple; method overriding |
| 5 | Abstract Data Structures and GUI Programming **(two subjects fused — see review D7)** | ADT concepts; linked lists — singly, doubly, circular; node structure, insertion, deletion, traversal (singly implemented); stacks — LIFO, list implementation, applications; queues — FIFO, list implementation, priority queues; Tkinter — Label, Button, Entry, Menu, Listbox, Canvas; event handling; simple GUI apps |

**Textbooks:** Anita Goel, *Python Programming — An Object Oriented Approach* (Universities Press) · Reema Thareja, *Python Programming using Problem Solving Approach* (OUP, 2020) · Budd T. A., *Exploring Python* (McGraw-Hill, 1e, 2011)
**References:** Martin C. Brown, *Python: The Complete Reference* (McGraw-Hill, 2018) · Kenneth A. Lambert, *Fundamentals of Python: First Programs* (Cengage, 2e, 2019)

### Course 4 — Statistical Foundations for Data Science (Sem II)
Notes: [`notes/sem-2/course-4-statistical-foundations/`](notes/sem-2/course-4-statistical-foundations/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Fundamentals of Probability & Basic Statistics | Concept of uncertainty; axioms and rules of probability; conditional probability; central tendency — mean, median, mode; dispersion — range, IQR, variance, standard deviation; correlation and covariance (introduction); data representation — histograms, bar charts, scatter plots |
| 2 | Random Variables, Expectation, and Variance | Random variables — definition, discrete vs continuous, properties; PMF and PDF; CDF; mathematical expectation, variance, standard deviation; moments and moment-generating functions |
| 3 | Probability Distributions | Discrete — Binomial, Poisson, Geometric, Negative Binomial; continuous — Uniform, Normal, Exponential, Gamma; joint, marginal and conditional distributions; Central Limit Theorem (introduction) |
| 4 | Correlation and Regression | Bivariate data and scatter plots; Pearson and Spearman coefficients and interpretation; simple linear regression — model, estimation, properties, ANOVA; multiple linear regression (conceptual); residuals and goodness of fit |
| 5 | Statistical Inference, Estimation, and Hypothesis Testing | Population vs sample, parameters vs statistics; sampling distributions; point and interval estimation (confidence intervals); z-test, t-test, chi-square test, F-test; p-values; Type I and Type II errors; power of a test |

**Also examinable but missing from the units:** Bayes' theorem — see review **D1**.

**Textbooks:** Walpole, *Probability and Statistics for Engineers and Scientists* (Wiley) · Sheldon M. Ross, *Introduction to Probability and Statistics for Engineers and Scientists* · Montgomery & Runger, *Applied Statistics and Probability for Engineers*
**References:** D. C. Agarwal, *Statistics for Data Science and AI* · Larry J. Stephens, *Excel Data Analysis*

### Course 5 — Database Management Systems (Sem III)
Notes: [`notes/sem-3/course-5-dbms/`](notes/sem-3/course-5-dbms/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Overview of Database Management System | Data, information, database, DBMS; file-based systems and their drawbacks; database approach; classification of DBMS; advantages; data models; components of a DBMS; three-schema architecture; costs and risks of the database approach |
| 2 | Entity-Relationship Model | Building blocks of an ER diagram; classification of entity sets; attribute classification; relationship degree and classification; reducing ER diagrams to tables; EER model; generalization and specialization; IS-A and attribute inheritance; multiple inheritance; constraints on specialization/generalization; advantages of ER modelling |
| 3 | Relational Model | CODD rules; relational data model; concept of key; relational integrity; relational algebra and its operations, advantages and limitations; functional dependencies and normal forms |
| 4 | Structured Query Language | Commands and data types; DDL; selection and projection; aggregate functions; DML; table modification commands; joins; set operations; views; subqueries |
| 5 | PL/SQL | Shortcomings of SQL; structure of PL/SQL; language elements; data types; operator precedence; control structures; steps to create a PL/SQL program; iterative control; procedures; functions |

**Also examinable but missing from the units:** database triggers — see review **D2**.

**Textbooks:** Silberschatz, Korth & Sudarshan, *Database System Concepts* (McGraw-Hill, 7e) · Raghu Ramakrishnan, *Database Management Systems* (McGraw-Hill)
**References:** Elmasri & Navathe, *Fundamentals of Database Systems* (Pearson) · C. J. Date, *An Introduction to Database Systems* (Pearson)

---

### Course 6 — Data Science with R (Sem III)
Notes: [`notes/sem-3/course-6-data-science-r/`](notes/sem-3/course-6-data-science-r/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to the Data Science Process | Definition; data science in various fields; impact; Data Analytics Life Cycle; data science toolkit; the data scientist and the data science team; Exploratory Data Analysis; feature engineering and data transformation |
| 2 | Basics of R Programming | R and RStudio; data types, variables, operators; control structures (`if`, loops, `apply`); functions and packages; data input/output (CSV, Excel, XML, JSON) |
| 3 | Data Handling and Visualization in R | Data frames, lists, matrices; wrangling with `dplyr` and `tidyr`; missing data; date/time; `ggplot2` — grammar of graphics, aesthetics, geometries, scales, faceting, layering; customising and exporting plots |
| 4 | Applications and Case Studies | Simple and multiple linear regression; model evaluation — accuracy, confusion matrix, ROC; K-Means clustering; text mining and word clouds; recommender system basics; ethical issues |
| 5 | Advanced Topics **(overloaded — see review D12)** | Time series in R — trend, seasonality, noise, `ts`/`zoo`/`xts`, decomposition, stationarity and differencing, ACF/PACF, AR/MA/ARIMA, forecasting; interactive plots with `plotly`; R Shiny — UI and server functions, reactivity, widgets, dashboard layout |

**Textbook:** James, Witten, Hastie & Tibshirani, *An Introduction to Statistical Learning with Applications in R* (Springer, 2e, 2021)
**References:** Matloff, *The Art of R Programming* (No Starch, 2011) · Venables & Ripley, *Modern Applied Statistics with S* (Springer, 2002) · Irizarry, *Introduction to Data Science* (CRC, 2020) · Grus, *Data Science from Scratch*

### Course 7 — Web Technologies (Sem III)
Notes: [`notes/sem-3/course-7-web-technologies/`](notes/sem-3/course-7-web-technologies/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | HTML | Web design principles; web vs desktop applications; HTML structure, elements, attributes; headings, paragraphs, images, tables, lists, blocks, symbols; embedding multimedia; HTML forms |
| 2 | CSS | Syntax and combinators; colours, background, borders, margins, padding, height/width; text, fonts, tables, lists; position, overflow, float; pseudo-classes and pseudo-elements; opacity, tooltips, image gallery; CSS forms and counters |
| 3 | JavaScript | DHTML; basics, variables, operators, statements; string manipulation; mathematical functions; arrays, functions, objects; regular expressions; exception handling |
| 4 | Client-Side Scripting | Accessing form elements through the JavaScript object model; basic and format validation; responsive messages; opening windows; dialog boxes; the status bar; animation with keyboard and mouse events |
| 5 | JSON and jQuery | Need for data exchange formats; JSON syntax; JSON vs XML; parsing, creating and accessing nested JSON; reading/writing JSON in JavaScript. jQuery — selectors, filters, DOM manipulation, event handling, animations, effects, chaining |

**Textbooks:** Chris Bates, *Web Programming: Building Internet Applications* (Wiley, 2e) · Wang & Katila, *An Introduction to Web Design plus Programming* (Thomson) · Chaffer & Swedberg, *Learning jQuery* (Packt) · *JSON at Work*
**Reference:** David R. Brooks, *An Introduction to HTML and JavaScript* (Springer)

### Course 8 — Data Mining (Sem IV)
Notes: [`notes/sem-4/course-8-data-mining/`](notes/sem-4/course-8-data-mining/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Data Warehousing | Introduction; database systems vs data warehouse; characteristics; architecture and components; data modelling; schema design — star, snowflake, fact constellation; fact table; OLAP cube and OLAP operations |
| 2 | Data Mining | Definitions; KDD vs data mining; data mining tasks; preprocessing — cleaning, missing data, dimensionality reduction, feature subset selection, discretization and binarization, transformation; similarity and dissimilarity measures; issues, challenges and applications |
| 3 | Association Analysis | What an association rule is; methods to discover rules; A Priori; Partition; Pincer-Search; Dynamic Itemset Counting; FP-Tree Growth; generalized association rules; rules with item constraints |
| 4 | Classification | Decision trees — construction principle, best split, splitting indices and criteria; CART, ID3, C4.5; comparing classifiers; rule-based classifiers; nearest neighbour; Bayesian classifiers |
| 5 | Clustering Techniques | Clustering paradigms; partitioning (K-Means); k-Medoid; hierarchical — DBSCAN, BIRCH; categorical clustering — STIRR, ROCK, CACTUS |

**Textbooks:** Arun K. Pujari, *Data Mining Techniques* (Universities Press, 3e) · Han, Kamber & Pei, *Data Mining: Concepts and Techniques* (Morgan Kaufmann, 3e)
**References:** Soman, Diwakar & Ajay, *Insight into Data Mining Theory and Practice* (PHI, 2006) · Tan, Steinbach, Karpatne & Kumar, *Introduction to Data Mining* (2e)

### Course 9 — Python for Data Analysis and Visualization (Sem IV)
Notes: [`notes/sem-4/course-9-python-data-analysis/`](notes/sem-4/course-9-python-data-analysis/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | NumPy Essentials | The `ndarray`; creating arrays; data types; arithmetic; basic indexing and slicing; boolean and fancy indexing; transposing and swapping axes; universal functions; mathematical and statistical functions; random number generation |
| 2 | Pandas Basics and Data Structures | `Series`, `DataFrame`, `Index` objects; indexing and selection; filtering and boolean indexing; arithmetic and data alignment; sorting and ranking; dropping entries; duplicate indexes |
| 3 | Data Input, Output and Cleaning | Reading and writing text formats (CSV, TXT); JSON; Excel; handling missing data — dropping, filling, replacing; renaming axis indexes; removing duplicates; filtering outliers; transforming with mapping or functions |
| 4 | String Operations and Feature Engineering | Pandas string methods; basic regular expressions; vectorized string functions; dummy/indicator variables; permutation and random sampling |
| 5 | Data Wrangling, Reshaping and Visualization | Merging and joining; concatenating along an axis; combining with overlap; pivot, stack and unstack; hierarchical indexing; summary statistics by group or level; `matplotlib`; `seaborn`; `plotly` |

**Textbooks:** Wes McKinney, *Python for Data Analysis* · Anita Goel, *Python Programming — An Object Oriented Approach* (Universities Press) · Vasiliev, *Python for Data Science For Dummies* (Wiley, 2e, 2022)
**Reference:** Jake VanderPlas, *Python Data Science Handbook* (2023)

### Course 10 — Document Oriented Database (Sem IV)
Notes: [`notes/sem-4/course-10-document-database/`](notes/sem-4/course-10-document-database/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to NoSQL and MongoDB Fundamentals | What NoSQL is; history and evolution; features; CAP theorem and BASE; types (key-value, document, column, graph); RDBMS vs NoSQL; when to use NoSQL; misconceptions; benefits and use cases; comparison of Redis, Cassandra, CouchDB, Neo4j; JSON and BSON; installation and setup |
| 2 | MongoDB Architecture and Data Modeling | Database, collection and document concepts; BSON; advantages over RDBMS; datatypes; schema design strategies; embedded vs referenced documents; creating and dropping databases and collections |
| 3 | CRUD Operations and Querying | `insertOne`/`insertMany`; `find` with operators and conditions; `updateOne`/`updateMany`/`replaceOne`; `deleteOne`/`deleteMany`; query operators (`$gt`, `$lt`, `$in`, `$nin`, `$and`, `$or`, `$not`); regular expression queries; bulk operations; working with arrays |
| 4 | Data Modelling and Aggregation | Embedded vs normalized models — use cases, benefits, limitations, trade-offs; references between documents; relationships; data models using embedded documents and document references; the aggregation framework — simple pipelines and operators |
| 5 | Advanced Query Processing and Optimization | Projection; limiting and skipping; sorting; indexing (single field, compound, multikey, text); aggregation pipelines, stages and operators; replication — replica sets, failover, consistency |

---

## 3a. Semester V — the core course and both elective tracks

Semester V is **Course 11 plus one elective pair**. Course 11 is compulsory;
you then take either **12 A + 13 A** or **12 B + 13 B**, and the choice binds
you for Semester VI too. All five are mapped below, because you cannot make
that choice well without seeing what is in both.

### Course 11 — Business Intelligence Tools (Sem V) — *core, everyone takes it*
Notes: [`notes/sem-5/course-11-business-intelligence/`](notes/sem-5/course-11-business-intelligence/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to BI and Decision Support Systems | BI definition, scope and evolution; BI vs Data Analytics vs Data Science; the BI lifecycle; applications in finance, HR, marketing, retail, education, healthcare; BI maturity models and organizational readiness; DSS concepts, components and architecture; Power BI, Tableau and other tools compared; case study — a retail chain's BI strategy for inventory |
| 2 | Data Preparation and Visualization with Power BI | The Power BI ecosystem — Desktop, Service, Mobile; the interface; data sources (Excel, CSV, SQL Server, Web APIs); Power Query for preparation, cleaning and transformation; basic DAX — SUM, COUNT, AVERAGE, CALCULATE, IF; charts, tables and cards; sharing via Power BI Service; case studies — student performance, finance dataset |
| 3 | Data Preparation, Visualization and Storytelling with Tableau | Tableau characteristics; architecture and components — Public, Desktop, Reader, Online, Server; the interface — shelves, marks card, views; extensions; data connection and preparation — cleaning, pivoting, filtering; calculated fields and LOD expressions; bar, line, tree, geo map and scatter visualizations; storytelling and creating a Tableau story; case study — HR analytics |
| 4 | Data Modeling and Relationships in BI Tools | Dimensional modeling — dimension, dimension table, fact, fact table, schema; star and snowflake schemas; Power BI relationships, cardinality and cross-filtering; Tableau joins (inner, left, full) and blending; data governance — metadata, hierarchies, quality; data model design best practices; case study — retail BI for sales optimization |
| 5 | Dashboard Design and Business Insights | When to use a dashboard; dashboard components; principles of effective visualization and dashboarding; advanced visuals — parameters, slicers, filters, drilldowns, graphs and maps; layout, alignment and accessibility; publishing to Power BI Service and Tableau Public; storytelling and insight communication; case study — sales forecasting and budgeting |

### Course 12 A — Machine Learning (Sem V) — *Track A*
Notes: [`notes/sem-5/course-12a-machine-learning/`](notes/sem-5/course-12a-machine-learning/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to Machine Learning | Types of human learning; what machine learning is; supervised, unsupervised, semi-supervised and reinforcement learning; machine learning activities; applications; types of data in ML; structure of data |
| 2 | Model Preparation, Evaluation and Feature Engineering | Data pre-processing; model selection and training for supervised learning; model representation and interpretability; evaluating algorithms and enhancing performance; feature engineering; feature transformation; feature subset selection; principal component analysis |
| 3 | Supervised Learning — Regression | Introduction to regression; simple linear regression; multiple linear regression; polynomial regression; logistic regression; maximum likelihood estimation |
| 4 | Supervised Learning — Classification | Introduction to supervised learning; the classification model and its learning steps; Naïve Bayes; k-Nearest Neighbour; decision trees; support vector machines; random forest |
| 5 | Unsupervised Learning | Introduction; unsupervised vs supervised; applications; clustering and its types; partitioning methods — k-Means and k-Medoids; hierarchical clustering; density-based methods — DBSCAN; case studies — image recognition, speech recognition, email spam filtering, online fraud detection |

### Course 13 A — Artificial Intelligence (Sem V) — *Track A*
Notes: [`notes/sem-5/course-13a-artificial-intelligence/`](notes/sem-5/course-13a-artificial-intelligence/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to AI and Intelligent Agents | Definition and scope of AI; history and evolution; the Turing Test; real-world applications; Weak vs Strong AI, Narrow vs General AI; intelligent agents — structure, rationality, agent types; environments — deterministic vs stochastic, static vs dynamic, discrete vs continuous; PEAS representation |
| 2 | Problem Solving — State Space and Uninformed Search | State space representation — state, actions, goal test, path cost; problem formulation with the 8-puzzle, water jug and vacuum cleaner world; breadth first search; depth first search; uniform cost search; properties — completeness, optimality, time and space complexity |
| 3 | Informed and Advanced Search Strategies | Heuristics — concept, admissibility, consistency; greedy best first search; A\*; local search — hill climbing, simulated annealing; genetic algorithms; constraint satisfaction problems and backtracking search |
| 4 | Knowledge Representation and Reasoning | Representation issues and approaches; propositional logic — syntax, semantics, truth tables, inference rules; first order logic — syntax, semantics, quantifiers, substitution, unification; forward chaining, backward chaining, resolution; knowledge-based agents |
| 5 | Expert Systems, Probabilistic and Emerging AI | Expert system architecture — knowledge base, inference engine, explanation facility; probabilistic reasoning — Bayes' theorem, Bayesian belief networks; fuzzy logic and uncertainty handling; NLP basics; robotics; AI ethics and societal impact |

### Course 12 B — Big Data Technologies (Sem V) — *Track B*
Notes: [`notes/sem-5/course-12b-big-data/`](notes/sem-5/course-12b-big-data/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Foundations of Big Data and the Hadoop Ecosystem | Big Data characteristics — volume, variety, velocity, veracity, value; ecosystem overview — HDFS, MapReduce, YARN, Hadoop Common; Hadoop architecture and use cases |
| 2 | HDFS and YARN | HDFS architecture — blocks, NameNode, DataNodes; file operations; fault tolerance; replication; YARN architecture — ResourceManager, NodeManager, application scheduling |
| 3 | MapReduce and High-Level Tools | The MapReduce programming model — map, shuffle, reduce phases; writing MapReduce applications; high-level abstractions — Hive, Pig, Crunch; introduction to Spark integration |
| 4 | Data Ingestion and Serialization | Ingestion pipelines — Sqoop for RDBMS, Flume for streaming; data formats and serialization — Avro, Parquet, SequenceFile; batch and streaming ingestion workflows |
| 5 | NoSQL and Ecosystem Enhancements | NoSQL within the Hadoop ecosystem — HBase; configuring and using ZooKeeper for coordination; Hadoop integration with Spark for data processing |

### Course 13 B — Cloud Computing for Data Science (Sem V) — *Track B*
Notes: [`notes/sem-5/course-13b-cloud-computing/`](notes/sem-5/course-13b-cloud-computing/)

| Unit | Title | Topics |
|:---:|---|---|
| 1 | Introduction to Cloud Computing | Definition and evolution; service-oriented architecture and web services; utility and grid computing; characteristics of cloud computing; architecture — front-end, back-end, networking, delivery models; service models — SaaS, PaaS, IaaS; continuous delivery using PaaS |
| 2 | Virtualization and Deployment Models | Concept and importance of virtualization; types — application, network, desktop, storage, server, data; deployment models — public, private, community, hybrid; the role of cloud computing in data science; advantages of cloud in machine learning |
| 3 | Cloud Storage and Data Management | Cloud storage — introduction, benefits, use cases (backup, archiving, disaster recovery, content delivery); storage systems — block-based, file-based, object-based; key-value databases — features and limitations; batch vs streaming data for ML pipelines; cloud data warehouses — AWS Redshift, Google BigQuery |
| 4 | Cloud Platforms for Data Science and ML | Machine learning in the cloud — benefits and limitations; cloud-based ML services — AIaaS, GPUaaS; managed ML platforms; AWS SageMaker, Azure ML Studio, Google Cloud AutoML |
| 5 | Training and Deployment of ML on the Cloud | Factors for selecting a platform — ETL/ELT pipeline support, scale-up/scale-out training, ML frameworks, pre-tuned services; steps for training in the cloud — data source identification, feature engineering, training, validation, deployment, monitoring; improving cloud-deployed models; case studies and industry applications |

---

## 4. Courses still not detailed

Structure only — titles, hours and credits. These are the **Semester VI**
elective pairs, for which APSCHE has not yet published unit-level syllabi in
the documents supplied.

| # | Course | Sem |
|:---:|---|:---:|
| 14 A/B | Neural Networks and Deep Learning / Time Series Analysis and Forecasting | VI |
| 15 A/B | Natural Language Processing / Data Engineering & MLOps | VI |

**The Semester V document confirmed the track structure** that §1 inferred from
the Semester I–II tables: 12 A pairs with 13 A (Machine Learning →
Artificial Intelligence) and 12 B with 13 B (Big Data → Cloud Computing). The
inference was right, but confirm the Semester VI pairing with your department
rather than assuming the same, because the document that would settle it has
not been published.
