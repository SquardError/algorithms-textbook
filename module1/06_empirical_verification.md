---
short_title: 6 · Empirical verification
kernelspec:
  name: python3
  display_name: Python 3
---

# Empirical Verification

A derived formula can contain a mistake — a wrong bound, a forgotten case, an off-by-one. The best way to
catch it is an **experiment**: run the algorithm and **count** the basic operation.

## The method in four steps

1. **Instrument the code.** Add a counter variable and increase it by 1 exactly where the basic operation
   is executed.
2. **Choose inputs** that realize the case you analyzed (for the worst case of UniqueElements: all
   elements distinct).
3. **Run for many sizes** $n$ and print a table: $n$ | counted | formula.
4. **Compare and conclude.** If every row matches, the experiment confirms the formula. If not, there is
   an error in the code, in the derivation, or in the choice of the basic operation — find it.

:::{note} Counting vs. timing
We count operations instead of measuring seconds: a counter gives an **exact** number that does not
depend on the computer, so it can be compared with the formula exactly. Timing experiments are useful too
(they show effects such as caching), but their results are noisy.
:::

## Experiment 1 · UniqueElements in the worst case

Formula from [Example 2](03_worked_examples.md#ex-unique): $C_{worst}(n) = \frac{n(n-1)}{2}$.

```{code-cell} python
import random

def unique_elements_count(A):
    """UniqueElements with a counter of the basic operation A[i] = A[j]."""
    n, comparisons = len(A), 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            comparisons += 1              # <- the basic operation is executed here
            if A[i] == A[j]:
                return False, comparisons
    return True, comparisons

def formula(n):
    return n * (n - 1) // 2

random.seed(2026)
print(f"{'n':>4} | {'counted':>8} | {'formula':>8} | match")
print("-" * 36)
sizes = list(range(2, 21)) + [50, 100, 200]
counted_values = []
for n in sizes:
    A = random.sample(range(10 * n), n)   # n distinct numbers -> worst case
    _, counted = unique_elements_count(A)
    counted_values.append(counted)
    print(f"{n:>4} | {counted:>8} | {formula(n):>8} | {'yes' if counted == formula(n) else 'NO'}")
```

```{code-cell} python
:tags: [hide-input]
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(sizes, counted_values, "o", markersize=6, label="counted")
xs = range(2, 201)
ax.plot(xs, [formula(n) for n in xs], linewidth=2, label=r"formula $n(n-1)/2$")
ax.set_xlabel("input size $n$"); ax.set_ylabel("comparisons")
ax.set_title("UniqueElements, worst case: experiment vs. formula")
ax.legend(); ax.grid(alpha=0.3)
plt.show()
```

**Conclusion.** For every tested $n$ the counted number of comparisons equals $\frac{n(n-1)}{2}$, and the
points lie exactly on the parabola. The experiment **confirms** the worst-case formula and the
$\Theta(n^2)$ growth: from $n = 100$ to $n = 200$ the count grows from $4950$ to $19900$, about
**4 times**, as expected for a quadratic function.

## Experiment 2 · What does a wrong formula look like?

Suppose someone made off-by-one errors: they counted the inner loop as $n - i$ terms instead of
$n - 1 - i$ and let the outer index run to $n - 1$, obtaining
$\sum_{i=0}^{n-1} (n - i) = \frac{n(n+1)}{2}$. The experiment immediately reveals it:

```{code-cell} python
wrong = lambda n: n * (n + 1) // 2
for n in [2, 5, 10, 20]:
    counted = unique_elements_count(list(range(n)))[1]
    print(f"n = {n:>2}: counted = {counted:>3}, wrong formula = {wrong(n):>3}, difference = {wrong(n) - counted}")
```

The difference is exactly $n$ every time — a sign that the sum has $n$ extra terms. The order of growth is
the same, but the exact formula is wrong.

## Experiment 3 · Random inputs fall between best and worst

On random arrays with many repeated values, UniqueElements usually stops early:

```{code-cell} python
for n in [10, 100, 400]:
    runs = [unique_elements_count([random.randrange(n) for _ in range(n)])[1] for _ in range(200)]
    print(f"n = {n:>3}: average {sum(runs)/len(runs):8.1f} comparisons "
          f"(best case 1, worst case {formula(n)})")
```

The average is far below the worst case. This shows why Step 3 of the plan matters: the worst case is a
guarantee, not a prediction of the typical behavior.

## Run it yourself

The same experiment (plus SelectionSort, whose count $\frac{n(n-1)}{2}$ holds for **every** input) is in
[`code/module1_experiment.py`](https://github.com/SquardError/algorithms-textbook/blob/main/code/module1_experiment.py):

```bash
python code/module1_experiment.py
```

Next: test yourself in the [Module 1 quiz](07_quiz.md).
