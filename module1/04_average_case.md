---
short_title: 4 · Average case
kernelspec:
  name: python3
  display_name: Python 3
---

# Average Case: Sequential Search

The worst case is a guarantee ("never more than…"), the best case is an optimistic bound. Neither tells
us what happens **typically**. For that we need the **average case**.

:::{important} The key idea
The average case is **not** the average of the best and worst cases. It is the **expected value** of the
count when inputs are random. So we must first **state an assumption** about how the inputs are
random — a *probability model*.
:::

## The algorithm

```text
ALGORITHM SequentialSearch(A[0..n-1], K)
    //Searches for a given value in a given array by sequential search
    //Output: The index of the first element equal to K or -1 if there is none
    i ← 0
    while i < n and A[i] ≠ K do
        i ← i + 1
    if i < n return i
    else return -1
```

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The key comparison `A[i] ≠ K`.

**Step 3 · Cases.** Early exit exists. $C_{worst}(n) = n$ (key last or absent), $C_{best}(n) = 1$
(key first). Now the average case.

## Step 4 · The probability model

We assume:

1. The search is **successful** with probability $p$ (where $0 \le p \le 1$), and unsuccessful with
   probability $1 - p$.
2. If the key is present, it is **equally likely** to be in any of the $n$ positions. So the probability
   that the first match is at position $i$ (counting from 1) is $\frac{p}{n}$.

Now list every possible outcome, its probability, and its number of comparisons:

| Outcome | Probability | Comparisons |
|---|---|---|
| key found at position 1 | $p/n$ | $1$ |
| key found at position 2 | $p/n$ | $2$ |
| … | … | … |
| key found at position $i$ | $p/n$ | $i$ |
| … | … | … |
| key found at position $n$ | $p/n$ | $n$ |
| key absent | $1 - p$ | $n$ |

The **expected value** is the sum of "probability × comparisons" over all outcomes:

$$
C_{avg}(n) = \left[ 1 \cdot \frac{p}{n} + 2 \cdot \frac{p}{n} + \dots + n \cdot \frac{p}{n} \right] + n \cdot (1 - p).
$$

## Step 5 · Evaluate

Take $\frac{p}{n}$ out of the bracket (rule R1) and use S1:

$$
\begin{aligned}
C_{avg}(n) &= \frac{p}{n} \sum_{i=1}^{n} i + n(1-p)
            = \frac{p}{n} \cdot \frac{n(n+1)}{2} + n(1-p) \\
           &= \frac{p(n+1)}{2} + n(1 - p).
\end{aligned}
$$

## What the formula tells us

| Situation | $p$ | $C_{avg}(n)$ | Meaning |
|---|---|---|---|
| Key is always present | $1$ | $\frac{n+1}{2}$ | about half of the array is scanned |
| Key is never present | $0$ | $n$ | the whole array is scanned |
| Half of the searches succeed | $\frac12$ | $\frac{n+1}{4} + \frac{n}{2} = \frac{3n+1}{4}$ | about three quarters |

For example, with $n = 100$ and $p = \frac12$: $C_{avg} = \frac{301}{4} = 75.25$ comparisons on average.

In every case $C_{avg}(n) \in \Theta(n)$ (for any fixed $p$), but the constant in front of $n$ depends on
the model.

```{code-cell} python
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0, 1, 101)
n = 100
fig, ax = plt.subplots(figsize=(6.5, 3.6))
ax.plot(p, p * (n + 1) / 2 + n * (1 - p), linewidth=2.5, label=r"$C_{avg}(100) = \frac{p\,(n+1)}{2} + n(1-p)$")
ax.axhline(n, color="tab:red", linestyle="--", label="worst case $n = 100$")
ax.axhline(1, color="tab:green", linestyle="--", label="best case $1$")
ax.set_xlabel("probability of a successful search $p$")
ax.set_ylabel("comparisons")
ax.set_title("Average case of sequential search, $n = 100$")
ax.legend(loc="center left"); ax.grid(alpha=0.3)
plt.show()
```

## A simulation agrees

We search 20 000 times in an array of $n = 100$ elements with $p = 0.5$ and average the counted
comparisons.

```{code-cell} python
import random

def sequential_search_count(A, K):
    comparisons = 0
    for x in A:
        comparisons += 1
        if x == K:
            break
    return comparisons

random.seed(1)
n, p, trials = 100, 0.5, 20_000
A = list(range(n))
total = 0
for _ in range(trials):
    K = random.randrange(n) if random.random() < p else -1   # present with probability p
    total += sequential_search_count(A, K)
print(f"simulated average = {total / trials:.2f}")
print(f"formula           = {p * (n + 1) / 2 + n * (1 - p):.2f}")
```

The simulated value is close to the formula, and it gets closer with more trials. The exact formula
itself was checked with exact fractions for $n = 1, \dots, 20$ and several values of $p$ in
`code/verify/verify_m1_theory.py`.

:::{warning} Typical mistake
Writing $C_{avg}(n) = \frac{C_{best}(n) + C_{worst}(n)}{2} = \frac{n+1}{2}$ "because it is in the middle".
This happens to match the case $p = 1$, but it is wrong for every other $p$, and the reasoning is wrong in
all cases. The average must be computed from a probability model.
:::

Next: [Typical mistakes](05_typical_mistakes.md).
