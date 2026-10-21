# algorithms-textbook

An e-textbook for bachelor's students on the mathematical analysis of the efficiency of
**nonrecursive** and **recursive** algorithms (Levitin, *Introduction to the Design and Analysis of
Algorithms*, 3rd ed., Sections 2.3–2.5).

**Live book:** https://squarderror.github.io/algorithms-textbook/

## Run the code

Requires Python 3.11+ (and Node.js 18+ only if you want to build the book).

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

# Check every formula and answer in the book (n = 1..20 and more)
python code/verify/run_all.py

# Empirical experiments (tables + plots saved to code/output/)
python code/module1_experiment.py   # UniqueElements and SelectionSort vs n(n-1)/2
python code/module2_experiment.py   # Hanoi moves vs 2^n - 1; Fibonacci calls, naive vs memoized
```

| Script | What it checks |
|---|---|
| `code/verify/verify_m1_theory.py` | sums, Module 1 worked examples, average case |
| `code/verify/verify_m1_problems.py` | answers to all Module 1 problems |
| `code/verify/verify_m2_theory.py` | recurrences, Module 2 worked examples, Fibonacci, stack depth |
| `code/verify/verify_m2_problems.py` | answers to all Module 2 problems |
| `code/verify/verify_text_facts.py` | numbers quoted in the text and in the quizzes |

## Build the book locally

```bash
jupyter-book build --execute --html   # static site in _build/html
jupyter-book start --execute          # live preview at http://localhost:3000
```

On Windows, if the build stops with `fetch failed` while executing notebooks, use the helper that starts
the Jupyter server on 127.0.0.1 itself:

```bash
python code/build_local.py            # same as build --execute --html
python code/build_local.py start      # live preview
```

The site is deployed to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.
