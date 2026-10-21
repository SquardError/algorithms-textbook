---
short_title: 4 · Fibonacci warning
kernelspec:
  name: python3
  display_name: Python 3
---

# A Warning Example: Naive Fibonacci

A recursive algorithm can be **correct** and still **hopelessly slow**. The classic example is the
direct recursive computation of the Fibonacci numbers.

## The Fibonacci numbers

$$
F(n) = F(n-1) + F(n-2) \quad \text{for } n > 1, \qquad F(0) = 0, \quad F(1) = 1 .
$$

The sequence starts $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$

## The naive algorithm

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM F(n)
    //Computes the nth Fibonacci number recursively by using its definition
    //Input: A nonnegative integer n
    //Output: The nth Fibonacci number
    if n ≤ 1 return n
    else return F(n - 1) + F(n - 2)
```
:::
:::{tab-item} Python
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
:::
::::

It looks harmless: it is just the definition. Let us analyze it.

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The addition.

**Step 3 · Cases.** The count depends only on $n$.

**Step 4 · Recurrence.** Two recursive calls, on $n-1$ and $n-2$, plus one addition. For $n \le 1$ there
is no addition:

$$
A(n) = A(n-1) + A(n-2) + 1 \quad \text{for } n > 1, \qquad A(0) = 0, \quad A(1) = 0 .
$$

**Step 5 · Solution.** Backward substitution is awkward here (two different smaller arguments). Instead,
look at a table:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $A(n)$ | 0 | 0 | 1 | 2 | 4 | 7 | 12 | 20 | 33 |
| $A(n) + 1$ | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 |
| $F(n+1)$ | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 |

The pattern suggests $A(n) + 1 = F(n+1)$. Indeed, put $B(n) = A(n) + 1$. Adding 1 to both sides of the
recurrence gives

$$
\begin{aligned}
B(n) &= A(n-1) + A(n-2) + 2 = B(n-1) + B(n-2), \\
B(0) &= B(1) = 1,
\end{aligned}
$$

which is the Fibonacci recurrence, shifted by one. Therefore

$$
A(n) = F(n+1) - 1 .
$$

It is known that $F(n) \approx \frac{\varphi^n}{\sqrt5}$, where $\varphi = \frac{1 + \sqrt5}{2} \approx 1.618$
is the **golden ratio**. So

$$
A(n) \in \Theta(\varphi^n) \qquad \text{(exponential!)}
$$

Computing $F(50)$ this way needs $F(51) - 1 = 20\,365\,011\,073$ — more than $2 \cdot 10^{10}$ — additions.

## Why so slow? The recursion tree

The recursion tree for $F(5)$ shows the problem: **the same subproblems are solved again and again**.

```{mermaid}
flowchart TD
    F5["F(5)"] --> F4["F(4)"]
    F5 --> F3a["F(3)"]
    F4 --> F3b["F(3)"]
    F4 --> F2a["F(2)"]
    F3a --> F2b["F(2)"]
    F3a --> F1a["F(1)"]
    F3b --> F2c["F(2)"]
    F3b --> F1b["F(1)"]
    F2a --> F1c["F(1)"]
    F2a --> F0a["F(0)"]
    F2b --> F1d["F(1)"]
    F2b --> F0b["F(0)"]
    F2c --> F1e["F(1)"]
    F2c --> F0c["F(0)"]
    classDef rep3 fill:#ffd6a5,stroke:#c77700
    classDef rep2 fill:#ffadad,stroke:#b00020
    class F3a,F3b rep2
    class F2a,F2b,F2c rep3
```

$F(3)$ (red) is computed **twice** and $F(2)$ (orange) **three times**; $F(1)$ appears 5 times and $F(0)$
3 times. In general, while computing $F(n)$, the value $F(n - j)$ is computed $F(j+1)$ times — the
repetition itself grows like the Fibonacci numbers.

| Subproblem in the tree of $F(n)$ | $F(n)$ | $F(n-1)$ | $F(n-2)$ | $F(n-3)$ | $F(n-4)$ | $F(n-5)$ |
|---|---|---|---|---|---|---|
| times computed | 1 | 1 | 2 | 3 | 5 | 8 |

There are only $n + 1$ **different** subproblems, $F(0), \dots, F(n)$, but the naive algorithm solves
exponentially many copies of them.

## Two cures

### Cure 1 · Memoization

**Memoization** means storing each computed value in a table and looking it up before recomputing.

```text
ALGORITHM MemoF(n)
    //memo[0..n] is a global table initialized with "empty"
    if memo[n] is not empty return memo[n]
    if n ≤ 1 result ← n
    else result ← MemoF(n - 1) + MemoF(n - 2)
    memo[n] ← result
    return result
```

Each $F(k)$ is now computed **once**, with one addition for $k \ge 2$: $n - 1$ additions,
$\Theta(n)$ time, and $\Theta(n)$ memory for the table (plus a recursion depth of about $n$). This idea is
the starting point of **dynamic programming**, which you will study later in the course.

### Cure 2 · Iteration (bottom-up)

Compute the sequence from the beginning, keeping only the last two values:

```text
ALGORITHM IterF(n)
    if n ≤ 1 return n
    prev ← 0;  curr ← 1
    for i ← 2 to n do
        next ← prev + curr
        prev ← curr;  curr ← next
    return curr
```

Additions: $\sum_{i=2}^{n} 1 = n - 1$. Time $\Theta(n)$, memory $\Theta(1)$.

## Seeing the difference

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

def fib_numbers(m):
    F = [0, 1]
    while len(F) <= m:
        F.append(F[-1] + F[-2])
    return F

ns = np.arange(2, 41)
F = fib_numbers(42)
naive = [F[n + 1] - 1 for n in ns]       # A(n) = F(n+1) - 1
linear = [n - 1 for n in ns]             # memoized or iterative

fig, ax = plt.subplots(figsize=(7.5, 4))
ax.semilogy(ns, naive, "o-", markersize=3, label=r"naive recursion: $F(n+1)-1 \in \Theta(\varphi^n)$")
ax.semilogy(ns, linear, "s-", markersize=3, label=r"memoization / iteration: $n-1$")
ax.set_xlabel("$n$"); ax.set_ylabel("additions (log scale)")
ax.set_title("Additions needed to compute $F(n)$")
ax.legend(); ax.grid(alpha=0.3, which="both")
plt.show()

for n in [10, 20, 30, 40]:
    print(f"n = {n:>2}: naive {F[n+1]-1:>12,} additions   vs   memo/iterative {n-1:>2}")
```

On a logarithmic scale an exponential function is a straight line going up; a linear function is
almost flat. For $n = 40$ the naive algorithm needs over 165 million additions, the others 39.

:::{important} The lesson
A recursive formulation that is **correct** may still be hopelessly **inefficient** if its subproblems
**overlap**. Writing the recurrence for the running time makes this visible before you run the program.
:::

Next: the memory side of recursion — [Recursion vs. iteration](05_recursion_vs_iteration.md).
