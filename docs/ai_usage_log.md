# AI usage log

Every entry records what an AI assistant generated, where it went, and how it was checked.
Tool: Claude Code (model: Claude Opus 5.5, Anthropic).

| Date | What AI did | Where | How it was checked |
|---|---|---|---|
| 2026-10-21 | Read `docs/task.pdf` and both lecture PDFs; tested `jupyterquiz` and nested dropdowns with Jupyter Book 2.1.7 on a throw-away page | (test page, deleted) | Built locally; clicked quiz options and dropdowns in headless Chrome (Playwright) and inspected screenshots |
| 2026-10-21 | Created the project skeleton: `myst.yml`, `.github/workflows/deploy.yml` (from the official `jupyter-book init --gh-pages` template), `requirements.txt`, placeholder pages, `code/verify/run_all.py` | repository root | Local `jupyter-book build --html` succeeded; package versions checked on PyPI |
