# CLAUDE.md — E-Textbook on Algorithm Analysis

## 1. Project in one paragraph

Build an **e-textbook for bachelor's students** on the mathematical analysis of the efficiency of **nonrecursive** (Lecture 4) and **recursive** (Lecture 5) algorithms, based on Levitin, *Introduction to the Design and Analysis of Algorithms*, 3rd ed., Sections 2.3–2.5. The textbook must explain the material **more simply** than the master's-level lecture and include a system of tasks with full solutions. The full assignment text is in `docs/task.pdf` (read it when in doubt; it is the source of truth for requirements and grading).

This is a university course assignment graded out of 30 points. **Correctness matters more than decoration.**

## 2. Working agreements

- **Language of the textbook: English.** Talk to the user in **Russian**; everything that goes into the book, code comments and commit messages is in **English**.
- The work is done **by one person** (the instructor has approved individual work, although the assignment is written for groups of 2–3). Do not invent team members and do not ask about this again. Do not ask about the deadline either: the user manages the schedule. Cross-review is replaced by (a) verifying every answer with code and (b) a test by 1–2 bachelor's students whose feedback is described in the report.
- **Never guess lecture content.** Lecture 4 and Lecture 5 materials should be in `docs/lectures/`. If they are missing, ask the user for them before writing theory. All facts, notation and formulas must agree with the lectures and Levitin.
- **AI use is allowed only if documented.** Keep `docs/ai_usage_log.md` and append a short entry whenever AI generates content (what, where, how it was checked). The report must state exactly what AI was used for.
- Every solution and answer must be **checked** (see section 7). Do not present anything as verified unless it was actually run.
- Before using any tool, package or command, **check the current official documentation** (versions and CLI change). Do not rely on memory for install commands.

## 3. Tech stack and hosting

- **Jupyter Book (MyST-based, current version)**, published through **GitHub Pages** with GitHub Actions (`jupyter book init --gh-pages`; Pages source must be set to *GitHub Actions*). Verify the current install and build commands in the official docs.
- The result must **open via a public link with no software installed**.
- **Formulas: real LaTeX math** (`$...$`, `$$...$$`, MyST `math` directive). Never images or plain text.
- **Code: Python**, pseudocode in **Levitin's notation**.
- **Quizzes: `jupyterquiz` (or a similar ready package for Jupyter Book).** Compatibility with the current MyST-based Jupyter Book must be tested **first**. If it does not work, report it to the user and propose the fallback (a small custom HTML/JS block, or H5P). Each answer option needs an explanation of why it is correct or incorrect.
- Hints, answers and solutions: three nested **collapsible (dropdown) blocks**, so the student reveals them step by step.
- Visuals: matplotlib / Plotly for charts, Mermaid or graphviz for recursion trees and diagrams. Do not use remote images that can disappear.

## 4. Repository layout

```
.
├── CLAUDE.md
├── README.md                  # how to run the code, link to the live book
├── requirements.txt
├── myst.yml                   # book config + table of contents
├── index.md                   # title page, how to use the book
├── intro.md                   # review + 5-question entry quiz
├── module1/                   # nonrecursive algorithms (Lecture 4)
│   ├── 00_goals.md
│   ├── 01_general_plan.md
│   ├── 02_summation_tools.md
│   ├── 03_worked_examples.md
│   ├── 04_average_case.md
│   ├── 05_typical_mistakes.md
│   ├── 06_empirical_verification.md
│   ├── 07_quiz.md
│   ├── 08_problems.md
│   └── 09_summary_cheatsheet.md
├── module2/                   # recursive algorithms (Lecture 5)
│   ├── 00_goals.md
│   ├── 01_general_plan.md
│   ├── 02_backward_substitution.md
│   ├── 03_worked_examples.md
│   ├── 04_fibonacci_warning.md
│   ├── 05_recursion_vs_iteration.md
│   ├── 06_quiz.md
│   ├── 07_problems.md
│   └── 08_summary_cheatsheet.md
├── glossary.md
├── sources.md
├── code/                      # Python for empirical tasks + answer verification
│   ├── module1_experiment.py
│   ├── module2_experiment.py
│   └── verify/                # scripts that check every answer in the book
├── docs/
│   ├── task.pdf
│   ├── lectures/              # Lecture 4 and 5 materials
│   ├── ai_usage_log.md
│   └── tracker.md             # task checklist
└── .github/workflows/deploy.yml
```

Do not commit `.venv/` or `_build/` (make sure `.gitignore` has both).

## 5. Required content

### Introductory part (review)
- Input size, basic operation, order of growth.
- O, Ω, Θ notations; worst, best and average cases.
- **Entry quiz: 5 questions** (what the student must know before the modules).

### Module 1 — Analysis of nonrecursive algorithms (Lecture 4)
| Section | Must cover |
|---|---|
| General plan | The five steps, the meaning of each, typical mistakes |
| Summation tools | Rules for sums, counting the number of terms, formulas for Σi, Σi², geometric series, Σiᵏ ∈ Θ(nᵏ⁺¹) |
| Worked examples | MaxElement, UniqueElements (worst and best case), matrix multiplication, loop with a dependent bound, multiplicative loop (log n) |
| Average case | Sequential search with success probability p |
| Typical mistakes | Wrong basic operation, size vs. value, mixing up cases, off-by-one, early exit, hidden cost |
| Empirical verification | How to check a derived formula by counting operations |

### Module 2 — Analysis of recursive algorithms (Lecture 5)
| Section | Must cover |
|---|---|
| General plan | The five steps, the recurrence relation and the initial condition |
| Backward substitutions | Step-by-step procedure and verifying the result by induction |
| Worked examples | Factorial, Tower of Hanoi (with a recursion tree), counting binary digits (n = 2ᵏ) |
| Warning example | Naive Fibonacci, repeated subproblems, memoization and iteration |
| Recursion vs. iteration | Stack depth as memory, tail recursion |

### Fixed elements
- Table of contents and navigation between sections.
- At the **start** of each module: goals and expected learning outcomes.
- At the **end** of each module: short summary and a **formula cheat sheet**.
- **At least 2 visual elements per module** (diagram, recursion tree, growth-of-functions chart, animation, or a video up to 5 min).
- Glossary of key terms; list of sources.
- Short sections; **new terms explained at first use** (the audience is bachelor's students).

## 6. Tasks: quotas and rules

**Minimum per module** (totals: ≥ 20 quiz questions, ≥ 26 problems for the whole book):

| Task type | Count | Checks |
|---|---|---|
| Auto-graded quiz | 10 questions | Terms, choice of basic operation, order of growth |
| Level A (basic) | 4 | Direct application of a formula or the plan |
| Level B (intermediate) | 4 | Nested sums, dependent bounds, case analysis, solving recurrences |
| Level C (advanced) | 2 | Average case, logarithmic loops, proof by induction |
| "Find the mistake" | 2 | An incorrect solution with **one** typical mistake from the list in section 5 |
| Empirical verification | 1 | Code with an operation counter, compared with the formula |

(The entry quiz in the introduction — 5 questions — is in addition to the 10 per module.)

**Rules**
1. **Originality.** Do not copy review questions or exercises from the lectures or Levitin. Change the **algorithm**, not just the numbers.
2. Every problem has a **hint** (guides without giving away the answer), an **answer**, and a **full step-by-step solution**, all hidden in collapsible blocks.
3. Quiz: every option has an explanation (why correct / why incorrect).
4. Each worked example follows the plan: **input size → basic operation → cases → sum or recurrence → solution**.
5. Each module has **at least 2 original worked examples** not found in the lectures (aim for 3–4). Candidates: selection sort, bubble sort, array sum, counting even elements, brute-force inversion count, loops with `i = i*3` / `i = i//2`, loops with `range(i, n)`; recursive array sum, recursive maximum, fast exponentiation, recursive binary search, digit sum, `T(n)=T(n/2)+1`, `T(n)=2T(n-1)+1`, `T(n)=T(n-1)+n`.
6. "Find the mistake" tasks: write a plausible wrong solution containing exactly one typical mistake, then give the diagnosis and the correct solution.

## 7. Verification (non-negotiable)

- For every formula, sum and recurrence in the book, add a script in `code/verify/` that counts operations (or evaluates the recurrence) for n = 1…20 (or similar) and compares with the closed form. Use `sympy` for symbolic sums/recurrences where useful.
- Run the scripts and report the actual output. Mismatch = fix the book, not the test.
- Empirical tasks: the book shows a table `n | counted | formula`, a growth plot, and a written conclusion about whether the experiment confirms the theory.
- Keep `docs/tracker.md` as a checklist: section / status / verified by code / verified by hand.
- Build the book locally and fix warnings (broken references, math not rendering) before every push.

## 8. Deliverables

1. **Link** to the e-textbook (public).
2. **Report (2–3 pages):** roles and contribution (single author — state it), sources, **exact description of AI use**, feedback from bachelor's students and what was corrected.
3. **Code** for the empirical tasks (`.py` or `.ipynb`) with run instructions in `README.md`.
4. **Defense:** 7–10 min presentation; questions on Lectures 4–5; the instructor picks a random problem from the book and it is solved at the board without preparation; the instructor checks navigation, quizzes and one or two solutions.

## 9. Grading (30 points) — priorities

| Criterion | Pts | What to prioritize |
|---|---|---|
| Correctness of theory | 5 | No errors in definitions, sums, recurrences, orders of growth |
| Quality of tasks and solutions | 5 | Levels A/B/C respected; full correct solutions; useful hints |
| Original examples | 5 | Not copied from lectures/Levitin; worked step by step |
| Interactivity and visuals | 3 | Auto-graded quizzes, recursion trees, tables, charts |
| Empirical part | 2 | Code works; experiment confirms the estimate; conclusions stated |
| Design and navigation | 2 | Logical structure, TOC, links between sections, formulas render |
| Report | 3 | Roles, contribution, sources, AI use |
| Defense | 5 | Presentation, answers, solving a random problem |

Order of effort: **theory correctness → tasks and solutions → original examples**, then visuals, empirical part, design, report.

## 10. Writing style

- Short paragraphs, plain language, one idea per section. Define each term at first use and add it to the glossary.
- Use the same five-step template in every worked example so the structure is recognizable.
- Typeset all math as LaTeX; keep notation consistent with the lectures (e.g. the same symbol for input size, basic-operation count `C(n)`, recurrence `T(n)`).
- Mark typical mistakes with a "Warning" admonition.

## 11. Open items (ask the user, do not assume)

- **Lecture materials:** confirm that Lectures 4 and 5 are in `docs/lectures/`.
- **Quiz package:** confirm that `jupyterquiz` works with the current Jupyter Book before writing all 25 questions.

## 12. Suggested order of work

1. Create the skeleton, `myst.yml`, GitHub Actions deploy; confirm the live link works.
2. Test the quiz package and the collapsible-block syntax on one sample page.
3. Introduction + entry quiz.
4. Module 1: theory → worked examples → verification scripts → problems and quiz.
5. Module 2: same order.
6. Glossary, sources, module summaries and cheat sheets.
7. Test on 1–2 bachelor's students; fix; write the report.
