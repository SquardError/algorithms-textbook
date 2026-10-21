---
short_title: Introduction
kernelspec:
  name: python3
  display_name: Python 3
---

# Introduction: What You Need Before We Start

This short review collects the ideas from earlier lectures that both modules rely on. If they all look
familiar, jump to the [entry quiz](#entry-quiz) at the end.

## Why count operations instead of seconds?

The running time in seconds depends on the computer, the programming language and even on what else
is running. We want a measure that depends **only on the algorithm**. So we:

1. measure the size of the input with a number $n$;
2. pick the one operation that does most of the work;
3. count how many times it runs, as a function of $n$.

(input-size)=
### Input size

The **input size** is a number $n$ that says how big the input is.

- For an array, $n$ is the number of elements.
- For an $n \times n$ matrix, we usually use $n$ (the order of the matrix), even though there are $n^2$
  numbers.
- For a problem about one number (is $n$ prime?), the honest size is the **number of bits** needed to
  write $n$ in binary, $b = \lfloor \log_2 n \rfloor + 1$, and not the value $n$ itself. We return to this
  trap in [Typical mistakes](module1/05_typical_mistakes.md).

(basic-operation)=
### Basic operation

The **basic operation** is the operation that contributes most to the running time. It is usually in the
innermost loop. Typical choices:

| Problem | Basic operation |
|---|---|
| Searching, sorting | key comparison, e.g. `A[i] > A[j]` |
| Matrix and number algorithms | multiplication (sometimes addition) |
| Tower of Hanoi | moving one disk |

We write $C(n)$ for the number of times the basic operation is executed on an input of size $n$. If one
basic operation takes time $c_{op}$, then the running time is roughly

$$
T(n) \approx c_{op} \cdot C(n).
$$

This formula already answers questions like "how much slower is the program on twice as much data?".
If $C(n) = \tfrac12 n(n-1)$, then for large $n$

$$
\frac{T(2n)}{T(n)} \approx \frac{\tfrac12 (2n)^2}{\tfrac12 n^2} = 4,
$$

so doubling the input makes the program about four times slower, whatever the computer.

(order-of-growth)=
## Order of growth

For large $n$ only the **fastest-growing term** of $C(n)$ matters, and constant factors are ignored. This
is called the **order of growth**. The most common orders, from slow to fast growth:

$$
1 \;<\; \log n \;<\; n \;<\; n \log n \;<\; n^2 \;<\; n^3 \;<\; 2^n \;<\; n!
$$

| $n$ | $\log_2 n$ | $n \log_2 n$ | $n^2$ | $n^3$ | $2^n$ |
|---:|---:|---:|---:|---:|---:|
| $10$ | $3.3$ | $33$ | $10^2$ | $10^3$ | $1024$ |
| $10^2$ | $6.6$ | $660$ | $10^4$ | $10^6$ | $1.3 \cdot 10^{30}$ |
| $10^3$ | $10$ | $1.0 \cdot 10^4$ | $10^6$ | $10^9$ | $1.1 \cdot 10^{301}$ |
| $10^6$ | $20$ | $2.0 \cdot 10^7$ | $10^{12}$ | $10^{18}$ | astronomically large |

The chart below shows how quickly the curves separate even for small $n$.

```{code-cell} python
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 20, 200)
fig, ax = plt.subplots(figsize=(7, 4))
for y, label in [(np.log2(n), r"$\log_2 n$"), (n, r"$n$"), (n*np.log2(n), r"$n\log_2 n$"),
                 (n**2, r"$n^2$"), (2**n, r"$2^n$")]:
    ax.plot(n, y, label=label, linewidth=2)
ax.set_ylim(0, 400)
ax.set_xlabel("input size $n$")
ax.set_ylabel("number of operations")
ax.set_title("Growth of common functions")
ax.legend()
ax.grid(alpha=0.3)
plt.show()
```

(asymptotic-notations)=
## The notations $O$, $\Omega$, $\Theta$

These notations compare a function $t(n)$ (usually our count $C(n)$) with a simple function $g(n)$ such as
$n^2$. Informally:

| Notation | Read as | Meaning | Example |
|---|---|---|---|
| $t(n) \in O(g(n))$ | "big oh" | $t$ grows **no faster** than $g$ | $3n+5 \in O(n^2)$ |
| $t(n) \in \Omega(g(n))$ | "big omega" | $t$ grows **at least as fast** as $g$ | $n^3 \in \Omega(n^2)$ |
| $t(n) \in \Theta(g(n))$ | "big theta" | $t$ grows **at the same rate** as $g$ | $\tfrac12 n(n-1) \in \Theta(n^2)$ |

Formally, $t(n) \in O(g(n))$ if there are a positive constant $c$ and an integer $n_0$ such that

$$
t(n) \le c\, g(n) \quad \text{for all } n \ge n_0 .
$$

$\Omega$ is the same with $\ge$, and $\Theta$ means both $O$ and $\Omega$ at once:
$c_2\, g(n) \le t(n) \le c_1\, g(n)$ for all $n \ge n_0$.

A practical way to compare two functions is the **limit** of their ratio:

$$
\lim_{n\to\infty} \frac{t(n)}{g(n)} =
\begin{cases}
0 & t \text{ grows slower than } g \quad (t \in O(g),\ t \notin \Theta(g)),\\
c > 0 & t \text{ grows at the same rate} \quad (t \in \Theta(g)),\\
\infty & t \text{ grows faster than } g \quad (t \in \Omega(g),\ t \notin \Theta(g)).
\end{cases}
$$

For example, $\lim_{n\to\infty} \frac{n(n-1)/2}{n^2} = \frac12$, so $\frac{n(n-1)}{2} \in \Theta(n^2)$.

(cases)=
## Worst, best and average case

For some algorithms the count depends not only on $n$ but on **which** input of size $n$ we get.
Sequential search for a key $K$ in an array of $n$ elements stops as soon as it finds $K$:

```text
ALGORITHM SequentialSearch(A[0..n-1], K)
    //Searches for K in A; returns its index or -1
    i ← 0
    while i < n and A[i] ≠ K do
        i ← i + 1
    if i < n return i
    else return -1
```

- **Worst case** $C_{worst}(n)$: the largest count over all inputs of size $n$. Here $K$ is last or absent:
  $C_{worst}(n) = n$ comparisons.
- **Best case** $C_{best}(n)$: the smallest count. Here $K = A[0]$: $C_{best}(n) = 1$.
- **Average case** $C_{avg}(n)$: the expected count for "typical" random inputs. It needs an explicit
  assumption about how inputs are distributed. We compute it in
  [Module 1](module1/04_average_case.md).

:::{important}
The best case is **not** "the smallest $n$". It is the most convenient input **of a fixed size $n$**.
:::

(entry-quiz)=
## Entry quiz

Five questions on what you need before the modules. Click an answer to see the explanation.

```{code-cell} python
:tags: [remove-input]
from jupyterquiz import display_quiz

entry_quiz = [
    {
        "question": "What is the most natural input size for an algorithm that sorts an array?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The number of elements $n$ in the array", "correct": True,
             "feedback": "Correct. The work of sorting depends on how many elements there are."},
            {"answer": "The largest value stored in the array", "correct": False,
             "feedback": "Incorrect. Sorting [1, 1000000] is not harder than sorting [1, 2]; the values do not measure size."},
            {"answer": "The number of seconds the program runs", "correct": False,
             "feedback": "Incorrect. That is the quantity we want to predict, not the input size."},
            {"answer": "The sum of all elements", "correct": False,
             "feedback": "Incorrect. The sum says nothing about how many steps the algorithm needs."},
        ],
    },
    {
        "question": "In the loop below, which operation is the best choice of basic operation?",
        "type": "multiple_choice",
        "code": "count ← 0\nfor i ← 0 to n - 1 do\n    if A[i] = 0\n        count ← count + 1",
        "answers": [
            {"answer": "The comparison A[i] = 0", "correct": True,
             "feedback": "Correct. It runs on every iteration, exactly n times, and is the main work of the loop."},
            {"answer": "The assignment count ← count + 1", "correct": False,
             "feedback": "Incorrect. It runs only for zero elements, so it can run 0 times and does not reflect the total work."},
            {"answer": "The assignment count ← 0", "correct": False,
             "feedback": "Incorrect. It runs only once, before the loop."},
            {"answer": "Reading the value of n", "correct": False,
             "feedback": "Incorrect. This is done once and does not depend on the input size."},
        ],
    },
    {
        "question": "Which statement is true for $t(n) = 5n^2 + 3n + 7$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$t(n) \\in \\Theta(n^2)$", "correct": True,
             "feedback": "Correct. The leading term is $5n^2$; constants and lower terms are ignored, and $t(n)/n^2 \\to 5$."},
            {"answer": "$t(n) \\in \\Theta(n)$", "correct": False,
             "feedback": "Incorrect. $t(n)/n \\to \\infty$, so $t$ grows faster than $n$."},
            {"answer": "$t(n) \\in \\Theta(n^3)$", "correct": False,
             "feedback": "Incorrect. $t(n) \\in O(n^3)$ is true, but $t(n)/n^3 \\to 0$, so it is not $\\Theta(n^3)$."},
            {"answer": "$t(n) \\in \\Theta(5n^2 + 3n)$ only, not $\\Theta(n^2)$", "correct": False,
             "feedback": "Incorrect. Both are true and mean the same thing; we write the simplest form, $\\Theta(n^2)$."},
        ],
    },
    {
        "question": "Which order of growth is the slowest (the most efficient for large $n$)?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$\\log n$", "correct": True,
             "feedback": "Correct. For $n = 10^6$, $\\log_2 n$ is only about 20."},
            {"answer": "$n$", "correct": False,
             "feedback": "Incorrect. Linear growth is fast compared with $\\log n$: $10^6$ vs about 20."},
            {"answer": "$n \\log n$", "correct": False,
             "feedback": "Incorrect. $n \\log n$ grows faster than $n$, and much faster than $\\log n$."},
            {"answer": "$2^n$", "correct": False,
             "feedback": "Incorrect. Exponential growth is the fastest in this list."},
        ],
    },
    {
        "question": "Sequential search looks for $K$ in an array of $n$ elements. What is its best case?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "1 comparison: $K$ is the first element", "correct": True,
             "feedback": "Correct. The best case is the most convenient input of size $n$; the search stops at once."},
            {"answer": "$n$ comparisons: $K$ is the last element", "correct": False,
             "feedback": "Incorrect. That is the worst case."},
            {"answer": "The array has $n = 1$ element", "correct": False,
             "feedback": "Incorrect. The best case is about the input of a fixed size $n$, not about making $n$ small."},
            {"answer": "$(n+1)/2$ comparisons", "correct": False,
             "feedback": "Incorrect. This is the average case when the search is always successful."},
        ],
    },
]
display_quiz(entry_quiz)
```

If you answered at least 4 questions correctly, you are ready for [Module 1](module1/00_goals.md).
