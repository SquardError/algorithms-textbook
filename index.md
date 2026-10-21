---
short_title: Home
---

# Analysis of Algorithms — A Friendly Textbook

How long will my program run if the input is ten times larger? This book teaches you how to answer
that question **with mathematics instead of guessing**.

You will learn to take a piece of pseudocode and turn it into a formula such as

$$
C(n) = \frac{n(n-1)}{2} \in \Theta(n^2),
$$

which says exactly how many times the most important operation runs on an input of size $n$, and how
fast that number grows.

The book follows Sections 2.3–2.5 of A. Levitin, *Introduction to the Design and Analysis of
Algorithms* (3rd ed.), and Lectures 4 and 5 of the course. It is written for bachelor's students: short
sections, plain language, and every new term is explained the first time it appears.

## What is inside

| Part | Topic | What you will be able to do |
|---|---|---|
| [Introduction](intro.md) | Review of the basics | Recall input size, basic operation, $O$, $\Omega$, $\Theta$, cases; take the entry quiz |
| [Module 1](module1/00_goals.md) | Nonrecursive algorithms (loops) | Turn loops into sums and evaluate them |
| [Module 2](module2/00_goals.md) | Recursive algorithms | Turn recursion into a recurrence relation and solve it |
| [Glossary](glossary.md) | Key terms | Look up any term quickly |
| [Sources](sources.md) | Literature | Find where each fact comes from |

## How to use this book

1. **Start with the [Introduction](intro.md)** and take the 5-question entry quiz. If you miss more than
   one question, reread the review before going on.
2. **Read each module in order.** Every module starts with goals and ends with a summary and a formula
   cheat sheet you can keep next to you while solving problems.
3. **Work through the examples with a pencil.** Every worked example uses the same five steps, so after a
   few examples the structure becomes automatic.
4. **Take the quiz** at the end of each module. Click an answer to see why it is right or wrong.
5. **Solve the problems.** Each problem has three collapsible blocks. Open them one at a time:

   :::{dropdown} 1 · Hint
   A small push in the right direction. It does not give the answer away.
   :::{dropdown} 2 · Answer
   The final result, so you can check yourself.
   :::{dropdown} 3 · Full solution
   Every step written out.
   :::
   :::
   :::

   Try the problem first. Open the hint only if you are stuck, and the solution only after you have an
   answer of your own.

## Levels of problems

| Level | Meaning |
|---|---|
| **A** (basic) | Apply one formula or the plan directly |
| **B** (intermediate) | Nested sums, dependent bounds, case analysis, solving recurrences |
| **C** (advanced) | Average case, logarithmic loops, proofs by induction |
| **Find the mistake** | A plausible but wrong solution: find the single error and fix it |
| **Empirical** | Write code with an operation counter and compare it with your formula |

## Every answer is checked by a program

All formulas, sums, recurrences and answers in this book were checked by Python scripts that count
operations for many values of $n$ and compare the count with the closed-form answer. The scripts are in
the [`code/verify/`](https://github.com/SquardError/algorithms-textbook/tree/main/code/verify) folder of the
repository. See the README there for how to run them.

:::{note} Notation used throughout the book
- $n$ — input size.
- $C(n)$ — number of times the basic operation is executed (a "count"). We also write $M(n)$ for
  multiplications, $A(n)$ for additions.
- $\log n$ means $\log_2 n$ unless another base is written.
- $\lfloor x \rfloor$ ("floor of $x$") is $x$ rounded down to an integer, for example $\lfloor 3.7 \rfloor = 3$.
- Pseudocode uses Levitin's notation: `←` is assignment, `//` starts a comment, arrays are indexed from 0.
:::
