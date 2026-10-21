---
short_title: 9 · Summary & cheat sheet
---

# Module 1 · Summary and Cheat Sheet

## Summary

- A nonrecursive algorithm is analyzed with **five steps**: input size → basic operation → cases → sum →
  solution.
- The **basic operation** is the one executed most often, usually in the innermost loop.
- If the algorithm can stop early, the count depends on the input: analyze the **worst**, **best** and, if
  needed, **average** case separately, and say which case a bound describes.
- **Loops become sums**, nested loops become nested sums evaluated **from the inside out**.
- Loops whose counter is **multiplied or divided** by a constant run $\Theta(\log n)$ times; the base of
  the logarithm does not matter.
- The **average case** requires an explicit probability model of the inputs.
- Check every formula **experimentally** by counting the basic operation in code.

## Cheat sheet

### The five steps

| Step | Question |
|---|---|
| 1 | What is the input size $n$ (or $m$, $n$; or the number of bits $b$)? |
| 2 | Which operation runs most often? |
| 3 | Can the loops stop early? → worst / best / average case |
| 4 | Write $C(n)$ as a (nested) sum with the **exact** loop bounds |
| 5 | Evaluate inside out; give the order of growth and the case |

### Sums

| Formula | |
|---|---|
| $\displaystyle\sum_{i=l}^{u} 1 = u - l + 1$ | number of terms |
| $\displaystyle\sum_{i=l}^{u} c\,a_i = c\sum_{i=l}^{u} a_i$ | R1: constants out |
| $\displaystyle\sum_{i=l}^{u} (a_i \pm b_i) = \sum a_i \pm \sum b_i$ | R2: split |
| $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2} \in \Theta(n^2)$ | S1 |
| $\displaystyle\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} \in \Theta(n^3)$ | S2 |
| $\displaystyle\sum_{i=0}^{n} 2^i = 2^{n+1} - 1 \in \Theta(2^n)$ | S3 |
| $\displaystyle\sum_{i=0}^{n} a^i = \frac{a^{n+1} - 1}{a - 1}\ (a \ne 1)$ | geometric series |
| $\displaystyle\sum_{i=1}^{n} i^k \in \Theta(n^{k+1})$ | powers |

### Loop patterns

| Loop | Count |
|---|---|
| `for i ← 1 to n` | $n$ |
| `for i ← 0 to n-2`, `for j ← i+1 to n-1` | $\frac{n(n-1)}{2}$ |
| `for i ← 1 to n`, `for j ← 1 to i` | $\frac{n(n+1)}{2}$ |
| three full loops `0..n-1` | $n^3$ |
| `i ← 1; while i ≤ n: i ← 2i` | $\lfloor \log_2 n \rfloor + 1$ |
| `i ← n; while i ≥ 1: i ← ⌊i/2⌋` | $\lfloor \log_2 n \rfloor + 1$ |
| `for i ← 1 to n` around a doubling/tripling loop up to $n$ | $\Theta(n \log n)$ |
| `i ← n; while i ≥ 1: (for j ← 1 to i); i ← ⌊i/2⌋` | $< 2n$, $\Theta(n)$ |

### Results to remember

| Algorithm | Count |
|---|---|
| MaxElement | $C(n) = n - 1$ |
| UniqueElements | $C_{worst} = \frac{n(n-1)}{2}$, $C_{best} = 1$ |
| Matrix multiplication | $M(n) = n^3$ |
| Selection sort | $C(n) = \frac{n(n-1)}{2}$ (all inputs), $n - 1$ swaps |
| Sequential search | $C_{worst} = n$, $C_{best} = 1$, $C_{avg} = \frac{p(n+1)}{2} + n(1-p)$ |

### Six typical mistakes

1. Wrong basic operation. 2. Size vs. value. 3. Mixing up cases. 4. Off-by-one. 5. Ignoring early exit.
6. Hidden cost.

### Orders of growth

$$
1 < \log n < n < n \log n < n^2 < n^3 < 2^n < n!
$$

---

Continue with [Module 2 · Recursive algorithms](../module2/00_goals.md).
