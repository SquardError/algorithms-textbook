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
```

## Build the book locally

```bash
jupyter-book build --execute --html   # static site in _build/html
jupyter-book start --execute          # live preview at http://localhost:3000
```

The site is deployed to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.
