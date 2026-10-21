---
short_title: Goals
---

# Module 1 · Analysis of Nonrecursive Algorithms

A **nonrecursive algorithm** is an algorithm that does not call itself. It is built from loops,
conditions (`if`) and assignments. In this module you learn to turn its loops into **sums** and to
evaluate them. This corresponds to Lecture 4 and Section 2.3 of Levitin.

## Goals

After this module you will be able to:

1. Apply the **five-step plan** to analyze any nonrecursive algorithm.
2. Choose a suitable **basic operation** and explain why counting it is enough.
3. Decide whether the count depends **only on $n$**, or also on the particular input, and if so analyze the
   **worst, best and average** cases separately.
4. Translate loops into **sums** and evaluate them with the standard formulas.
5. State the **order of growth** with the correct notation $O$, $\Omega$ or $\Theta$.
6. Handle loops with **dependent bounds** (the inner loop depends on the outer index) and **multiplicative
   loops** (the counter doubles, triples or halves), which give logarithms.
7. Check a derived formula **experimentally** by counting operations in a program.

## Expected learning outcomes

You have mastered the module if you can, without notes:

- write $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ and
  $\sum_{i=0}^{n} 2^i = 2^{n+1}-1$;
- count the terms of $\sum_{i=l}^{u} 1 = u - l + 1$ without an off-by-one error;
- derive $C_{worst}(n) = \frac{n(n-1)}{2}$ for the element-uniqueness algorithm;
- explain why a loop with `i ← 2·i` runs $\lfloor \log_2 n \rfloor + 1$ times;
- spot the six typical mistakes from [Typical mistakes](05_typical_mistakes.md) in someone else's solution.

## Map of the module

| # | Section | Key idea |
|---|---|---|
| 1 | [General plan](01_general_plan.md) | Five steps, always in the same order |
| 2 | [Summation tools](02_summation_tools.md) | Rules and formulas for sums |
| 3 | [Worked examples](03_worked_examples.md) | Eight algorithms analyzed step by step |
| 4 | [Average case](04_average_case.md) | Sequential search with success probability $p$ |
| 5 | [Typical mistakes](05_typical_mistakes.md) | Six traps and how to avoid them |
| 6 | [Empirical verification](06_empirical_verification.md) | Checking a formula with an operation counter |
| 7 | [Quiz](07_quiz.md) | 10 auto-graded questions |
| 8 | [Problems](08_problems.md) | 13 problems with hints and solutions |
| 9 | [Summary and cheat sheet](09_summary_cheatsheet.md) | All formulas on one page |

:::{tip} Before you start
Make sure you remember the meaning of **input size**, **basic operation** and $\Theta$ from the
[Introduction](../intro.md).
:::
