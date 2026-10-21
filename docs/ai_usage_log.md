# AI usage log

Every entry records what an AI assistant generated, where it went, and how it was checked.
Tool: Claude Code (model: Claude Opus 5.5, Anthropic).

| Date | What AI did | Where | How it was checked |
|---|---|---|---|
| 2026-10-21 | Read `docs/task.pdf` and both lecture PDFs; tested `jupyterquiz` and nested dropdowns with Jupyter Book 2.1.7 on a throw-away page | (test page, deleted) | Built locally; clicked quiz options and dropdowns in headless Chrome (Playwright) and inspected screenshots |
| 2026-10-21 | Created the project skeleton: `myst.yml`, `.github/workflows/deploy.yml` (from the official `jupyter-book init --gh-pages` template), `requirements.txt`, placeholder pages, `code/verify/run_all.py` | repository root | Local `jupyter-book build --html` succeeded; package versions checked on PyPI |
| 2026-10-21 | Wrote verification scripts `code/verify/verify_*.py` (operation counters, recurrence evaluation, sympy sums/rsolve, exhaustive best/worst-case search for small n) | `code/verify/` | Ran `python code/verify/run_all.py`: 5/5 scripts, 16 837 comparisons, 0 mismatches |
| 2026-10-21 | Drafted all book text: introduction + entry quiz, Module 1 and Module 2 (theory, worked examples incl. 3 + 3 original examples, quizzes 10 + 10, problems 13 + 13 with hints/answers/solutions), summaries, cheat sheets, glossary, sources | `index.md`, `intro.md`, `module1/`, `module2/`, `glossary.md`, `sources.md` | Every formula/answer covered by a verification script; book built locally with `--execute` without warnings; all 25 quiz questions clicked automatically (each option gives feedback, exactly one correct); pages inspected via screenshots. **Hand check by the author still pending.** |
| 2026-10-21 | Wrote experiment scripts and local build helper | `code/module1_experiment.py`, `code/module2_experiment.py`, `code/build_local.py` | Scripts run; tables match formulas |
