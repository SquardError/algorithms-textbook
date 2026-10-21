---
short_title: Sources
---

# Sources

## Main sources

1. Levitin, A. *Introduction to the Design and Analysis of Algorithms*, 3rd ed. Pearson, 2012.
   Section 2.3 (Mathematical Analysis of Nonrecursive Algorithms), Section 2.4 (Mathematical Analysis of
   Recursive Algorithms), Section 2.5 (Example: Computing the $n$th Fibonacci Number), Appendix A (Useful
   Formulas for the Analysis of Algorithms), Appendix B (Short Tutorial on Recurrence Relations).
2. Lecture 4. *Mathematical Analysis of Nonrecursive Algorithms*. Design and Analysis of Algorithms, course
   materials, 2026.
3. Lecture 5. *Mathematical Analysis of Recursive Algorithms*. Design and Analysis of Algorithms, course
   materials, 2026.

All definitions, notation and formulas in this book follow these three sources. The five-step plans, the
classic examples (MaxElement, UniqueElements, matrix multiplication, sequential search, factorial, Tower of
Hanoi, BinRec, Fibonacci) and the method of backward substitutions are taken from them and re-explained
for bachelor's students.

## Additional sources

4. Cormen, T. H., Leiserson, C. E., Rivest, R. L., Stein, C. *Introduction to Algorithms*, 4th ed. MIT Press,
   2022. Chapter 3 (Characterizing Running Times), Chapter 4 (Divide-and-Conquer), Appendix A (Summations).
5. Sedgewick, R., Wayne, K. *Algorithms*, 4th ed. Addison-Wesley, 2011. Section 1.4 (Analysis of
   Algorithms).
6. Kleinberg, J., Tardos, É. *Algorithm Design*. Pearson, 2005. Chapter 2 (Basics of Algorithm Analysis),
   Chapter 5 (Divide and Conquer).
7. Graham, R. L., Knuth, D. E., Patashnik, O. *Concrete Mathematics*, 2nd ed. Addison-Wesley, 1994.
   Chapter 1 (Recurrent Problems), Chapter 2 (Sums), Chapter 7 (Generating Functions).

## Original material

The following were written for this book and do not appear in the lectures or in Levitin's Sections 2.3–2.5:

- **Module 1 worked examples:** selection sort (as an example of the plan; the algorithm itself is in
  Levitin, Section 3.1), search in an $m \times n$ matrix, a linear loop around a tripling loop.
- **Module 2 worked examples:** recursive array sum, fast exponentiation, recursive binary search.
- **All quiz questions and all problems** in both modules (A, B, C levels, "Find the mistake", empirical tasks).

## Software

- [Jupyter Book 2](https://jupyterbook.org) (MyST Markdown) — the platform of this book.
- [jupyterquiz](https://github.com/jmshea/jupyterquiz) — interactive quizzes.
- [Python](https://www.python.org), [SymPy](https://www.sympy.org), [Matplotlib](https://matplotlib.org) — verification
  scripts and charts. [Mermaid](https://mermaid.js.org) — diagrams and recursion trees.

## Use of AI

Parts of this book were drafted with the help of an AI assistant (Claude, Anthropic). Every formula and
answer was checked by the verification scripts in `code/verify/` and by hand by the author. The exact use
of AI is described in the project report.
