---
short_title: 2 · Summation tools
kernelspec:
  name: python3
  display_name: Python 3
---

# Summation Tools

Steps 4 and 5 of the plan need a small toolkit: **two rules**, **one way to count terms**, and **three
formulas**. Learn them by heart — almost every analysis in this book uses them.

## Reading the $\Sigma$ notation

$$
\sum_{i=l}^{u} a_i = a_l + a_{l+1} + \dots + a_u
$$

reads "the sum of $a_i$ for $i$ from $l$ to $u$". The letter $i$ is the **index**; $l$ and $u$ are the
**lower** and **upper bounds**. A `for i ← l to u` loop corresponds exactly to $\sum_{i=l}^{u}$.

## Counting the terms

$$
\sum_{i=l}^{u} 1 = u - l + 1 \qquad (u \ge l - 1)
$$

This is just the number of integers from $l$ to $u$ **inclusive**. Two special cases appear all the time:

$$
\sum_{i=0}^{n-1} 1 = n, \qquad \sum_{i=1}^{n} 1 = n .
$$

If $u = l - 1$ the sum is **empty** and equals $0$ (the loop body never runs).

:::{warning} Off-by-one trap
Count the terms of $\sum_{i=5}^{n} 1$. It is **not** $n - 5$. The integers $5, 6, \dots, n$ are
$n - 5 + 1 = n - 4$ numbers. Always use the "$+1$".
:::

## Two manipulation rules

**Rule R1 — constants come out:**

$$
\sum_{i=l}^{u} c\, a_i = c \sum_{i=l}^{u} a_i .
$$

**Rule R2 — sums split over addition:**

$$
\sum_{i=l}^{u} (a_i \pm b_i) = \sum_{i=l}^{u} a_i \pm \sum_{i=l}^{u} b_i .
$$

**Example.** Using R2, then R1, then formula S1 below:

$$
\sum_{i=1}^{n} (2i + 3) = 2\sum_{i=1}^{n} i + 3\sum_{i=1}^{n} 1 = 2 \cdot \frac{n(n+1)}{2} + 3n = n^2 + 4n .
$$

:::{warning} There is no rule for products
$\sum a_i b_i \ne \left(\sum a_i\right)\left(\sum b_i\right)$ in general. Only **constants** (things that do
not depend on $i$) can be taken out.
:::

## Three standard formulas

| | Sum | Closed form | Order of growth |
|---|---|---|---|
| **S1** | $\displaystyle\sum_{i=1}^{n} i = 1 + 2 + \dots + n$ | $\dfrac{n(n+1)}{2}$ | $\Theta(n^2)$ |
| **S2** | $\displaystyle\sum_{i=1}^{n} i^2 = 1 + 4 + \dots + n^2$ | $\dfrac{n(n+1)(2n+1)}{6}$ | $\Theta(n^3)$ |
| **S3** | $\displaystyle\sum_{i=0}^{n} 2^i = 1 + 2 + 4 + \dots + 2^n$ | $2^{n+1} - 1$ | $\Theta(2^n)$ |

S3 is a special case of the **geometric series**: for any $a \ne 1$,

$$
\sum_{i=0}^{n} a^i = \frac{a^{n+1} - 1}{a - 1} .
$$

### Why S1 is true (Gauss's trick)

Write the sum twice, once forwards and once backwards, and add the columns:

$$
\begin{array}{rcccccc}
 & 1 & + & 2 & + \dots + & n \\
+ & n & + & (n-1) & + \dots + & 1 \\ \hline
 & (n+1) & + & (n+1) & + \dots + & (n+1)
\end{array}
$$

There are $n$ columns, each equal to $n+1$, so twice the sum is $n(n+1)$. The picture shows the same idea:
the blue dots form $1 + 2 + \dots + n$, and together with the orange copy they fill an $n \times (n+1)$
rectangle.

```{code-cell} python
:tags: [remove-input]
import matplotlib.pyplot as plt

n = 6
fig, ax = plt.subplots(figsize=(5, 4.3))
for row in range(1, n + 1):
    for col in range(1, n + 2):
        blue = col <= row
        ax.scatter(col, n + 1 - row, s=260, color="#1f77b4" if blue else "#ff7f0e",
                   edgecolor="black", linewidth=0.6)
ax.set_title(r"$2\,(1+2+\dots+6) = 6 \cdot 7$, so $1+\dots+6 = 21$")
ax.set_xticks(range(1, n + 2)); ax.set_yticks([])
ax.set_xlabel("blue: row $i$ has $i$ dots      orange: the mirrored copy")
ax.set_aspect("equal"); ax.set_xlim(0.3, n + 1.7); ax.set_ylim(0.3, n + 0.7)
for s in ax.spines.values():
    s.set_visible(False)
plt.show()
```

### A useful general fact

For any fixed $k \ge 0$,

$$
\sum_{i=1}^{n} i^k = 1^k + 2^k + \dots + n^k \in \Theta(n^{k+1}) .
$$

More precisely the sum is approximately $\frac{n^{k+1}}{k+1}$ for large $n$. This tells you the order of
growth **without** computing exact constants. For example, $\sum_{i=1}^{n} 4i^3 \in \Theta(n^4)$.

The chart compares the exact sums with $\frac{n^{k+1}}{k+1}$: the curves practically coincide.

```{code-cell} python
:tags: [remove-input]
import numpy as np

ns = np.arange(1, 41)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
for ax, k in zip(axes, [1, 2]):
    exact = [sum(i**k for i in range(1, n + 1)) for n in ns]
    ax.plot(ns, exact, "o", markersize=4, label=rf"exact $\sum_{{i=1}}^n i^{k}$")
    ax.plot(ns, ns ** (k + 1) / (k + 1), linewidth=2, label=rf"$n^{k+1}/{k+1}$")
    ax.set_xlabel("$n$"); ax.legend(); ax.grid(alpha=0.3)
    ax.set_title(rf"$k = {k}$: $\Theta(n^{k+1})$")
plt.tight_layout(); plt.show()
```

## Evaluating nested sums: inside out

Nested loops give nested sums. Evaluate the **innermost** sum first, treating the outer index as a
constant.

**Example.**

$$
\sum_{i=0}^{n-2} \;\sum_{j=i+1}^{n-1} 1 .
$$

*Inner sum.* For a fixed $i$, the inner sum counts the integers from $i+1$ to $n-1$:
$(n-1) - (i+1) + 1 = n - 1 - i$.

*Outer sum.*

$$
\sum_{i=0}^{n-2} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 = \frac{(n-1)n}{2} .
$$

The middle step is a **change of index**: as $i$ goes $0, 1, \dots, n-2$, the term $n-1-i$ takes the
values $n-1, n-2, \dots, 1$ — the same numbers as in S1, in reverse order, with $n-1$ in place of $n$.

## Logarithms: a reminder

Multiplicative loops (the counter doubles or halves) produce logarithms. You need three facts:

1. $\log_2 n$ is the power to which you raise 2 to get $n$: $2^{\log_2 n} = n$. For example
   $\log_2 1024 = 10$.
2. The number of times you can halve $n$ before reaching 1 is about $\log_2 n$; exactly,
   $\lfloor \log_2 n \rfloor$.
3. **The base does not matter for the order of growth**:
   $\log_a n = \dfrac{\log_b n}{\log_b a}$, so logarithms with different bases differ only by a constant
   factor. That is why we simply write $\Theta(\log n)$.

## Summary of the toolkit

| Tool | Formula |
|---|---|
| Number of terms | $\sum_{i=l}^{u} 1 = u - l + 1$ |
| R1 | $\sum c\,a_i = c \sum a_i$ |
| R2 | $\sum (a_i \pm b_i) = \sum a_i \pm \sum b_i$ |
| S1 | $\sum_{i=1}^{n} i = \frac{n(n+1)}{2} \in \Theta(n^2)$ |
| S2 | $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} \in \Theta(n^3)$ |
| S3 | $\sum_{i=0}^{n} 2^i = 2^{n+1} - 1 \in \Theta(2^n)$ |
| Powers | $\sum_{i=1}^{n} i^k \in \Theta(n^{k+1})$ |

Next: these tools in action in the [Worked examples](03_worked_examples.md).
