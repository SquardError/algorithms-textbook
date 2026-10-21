---
short_title: Goals
---

# Module 2 · Analysis of Recursive Algorithms

A **recursive algorithm** solves a problem by calling **itself** on smaller inputs. It has no loop that
tells us directly how often the basic operation runs, so the tools of Module 1 are not enough. Instead
we describe the count with an equation that refers to itself — a **recurrence relation** — and then
solve it. This corresponds to Lecture 5 and Sections 2.4–2.5 of Levitin.

## Goals

After this module you will be able to:

1. Apply the **five-step plan** for recursive algorithms.
2. Set up a **recurrence relation** with a correct **initial condition** for the number of basic
   operations (and for the number of calls).
3. Solve simple recurrences by the method of **backward substitutions** and **verify** the answer by
   mathematical induction.
4. Solve recurrences with $n/2$ by first assuming $n = 2^k$.
5. Draw a **recursion tree** and use it to count operations.
6. Recognize **repeated subproblems** (naive Fibonacci) and fix them with **memoization** or iteration.
7. Compare recursion and iteration in terms of **time** and **memory** (stack depth).

## Expected learning outcomes

You have mastered the module if you can, without notes:

- derive $M(n) = M(n-1) + 1$, $M(0) = 0$ for the factorial and solve it: $M(n) = n$;
- derive and solve the Tower of Hanoi recurrence: $M(n) = 2M(n-1) + 1$, $M(1) = 1$, so $M(n) = 2^n - 1$;
- solve $A(n) = A(n/2) + 1$, $A(1) = 0$ for $n = 2^k$: $A(n) = \log_2 n$;
- prove a closed form by induction;
- explain why the naive recursive Fibonacci algorithm is exponential and how to make it linear;
- state the recursion depth (stack memory) of an algorithm.

## Map of the module

| # | Section | Key idea |
|---|---|---|
| 1 | [General plan](01_general_plan.md) | Five steps; step 4 is a recurrence |
| 2 | [Backward substitutions](02_backward_substitution.md) | Unroll, find the pattern, reach the initial condition, verify |
| 3 | [Worked examples](03_worked_examples.md) | Six algorithms, three of them original |
| 4 | [Fibonacci warning](04_fibonacci_warning.md) | Repeated subproblems make recursion exponential |
| 5 | [Recursion vs. iteration](05_recursion_vs_iteration.md) | Stack depth is memory; tail recursion |
| 6 | [Quiz](06_quiz.md) | 10 auto-graded questions |
| 7 | [Problems](07_problems.md) | 13 problems with hints and solutions |
| 8 | [Summary and cheat sheet](08_summary_cheatsheet.md) | All formulas on one page |

:::{tip} Before you start
You will need the sum formulas from Module 1, especially the geometric series
$1 + 2 + 4 + \dots + 2^{i-1} = 2^i - 1$. Keep the [Module 1 cheat sheet](../module1/09_summary_cheatsheet.md)
at hand.
:::
