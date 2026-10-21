---
short_title: 8 · Summary & cheat sheet
---

# Module 2 · Summary and Cheat Sheet

## Summary

- A recursive algorithm is analyzed with five steps: input size → basic operation → cases →
  **recurrence with an initial condition** → solution.
- The recurrence has **one term per recursive call** plus the work done directly in the call. The initial
  condition is the count in the **stopping case** of the algorithm.
- **Backward substitutions:** substitute 2–3 times without simplifying, guess the form after $i$ steps,
  choose $i$ to reach the initial condition, simplify, **verify** (plug in or induction).
- Recurrences with $n/2$ are solved for $n = 2^k$; the **smoothness rule** extends the order of growth to
  all $n$.
- A **recursion tree** gives a quick cross-check: sum the work over all nodes, level by level.
- **Overlapping subproblems** (naive Fibonacci) make recursion exponential; **memoization** or
  **iteration** makes it linear.
- **Recursion depth is memory.** Report time and space. **Tail recursion** can be turned into a loop.

## Cheat sheet

### Setting up the recurrence

$$
\begin{aligned}
M(n) &= \underbrace{M(n_1) + M(n_2) + \dots}_{\text{one term per call}} + \underbrace{w(n)}_{\text{work in this call}}, \\
M(\text{stop}) &= \text{work in the stopping case}.
\end{aligned}
$$

### Standard recurrences and their solutions

| Recurrence | Initial condition | Solution | Example |
|---|---|---|---|
| $M(n) = M(n-1) + 1$ | $M(0) = 0$ | $n$ | factorial |
| $S(n) = S(n-1) + 1$ | $S(1) = 0$ | $n - 1$ | recursive sum |
| $T(n) = T(n-1) + c$ | $T(0) = t_0$ | $cn + t_0$ | |
| $T(n) = T(n-1) + (2n-1)$ | $T(0) = 0$ | $n^2$ | loop inside recursion |
| $M(n) = 2M(n-1) + 1$ | $M(1) = 1$ | $2^n - 1$ | Tower of Hanoi |
| $A(n) = 2A(n-1) + 1$ | $A(1) = 0$ | $2^{n-1} - 1$ | two identical calls |
| $T(n) = T(n-1) + 2^n$ | $T(0) = 1$ | $2^{n+1} - 1$ | |
| $A(n) = A(\lfloor n/2 \rfloor) + 1$ | $A(1) = 0$ | $\lfloor \log_2 n \rfloor$ | BinRec |
| $C(n) = C(\lfloor n/2 \rfloor) + 1$ | $C(0) = 0$ | $\lfloor \log_2 n \rfloor + 1$ | binary search (worst) |
| $C(n) = 2C(n/2) + 1$ | $C(1) = 0$ | $n - 1$ | max by halves |
| $A(n) = A(n-1) + A(n-2) + 1$ | $A(0) = A(1) = 0$ | $F(n+1) - 1 \in \Theta(\varphi^n)$ | naive Fibonacci |

### Backward substitutions — general forms after $i$ steps

| Recurrence | After $i$ steps |
|---|---|
| $M(n) = M(n-1) + c$ | $M(n-i) + ci$ |
| $M(n) = 2M(n-1) + 1$ | $2^i M(n-i) + 2^i - 1$ |
| $A(2^k) = A(2^{k-1}) + 1$ | $A(2^{k-i}) + i$ |
| $C(2^k) = 2C(2^{k-1}) + 1$ | $2^i C(2^{k-i}) + 2^i - 1$ |

### Induction template

1. **Base case:** check the formula at the initial condition.
2. **Inductive step:** assume the formula for $n - 1$; substitute it into the recurrence; simplify to the
   formula for $n$.

### Useful facts

$$
1 + 2 + 4 + \dots + 2^{i-1} = 2^i - 1, \qquad \varphi = \frac{1 + \sqrt5}{2} \approx 1.618, \qquad
F(n) \approx \frac{\varphi^n}{\sqrt5}.
$$

### Recursion depth (space)

| Algorithm | Depth |
|---|---|
| factorial, recursive sum, Hanoi, naive Fibonacci | $\Theta(n)$ |
| BinRec, binary search, fast exponentiation | $\Theta(\log n)$ |

### Typical mistakes

1. Missing or wrong **initial condition** (check the stopping case!).
2. **One term for two calls** ($M(n/2)$ instead of $2M(n/2)$).
3. Counting the work of the recursive calls **twice**.
4. Choosing the wrong $i$ (initial condition at $1$ → $i = n - 1$).
5. Forgetting the value of the initial condition in the final answer.
6. Reporting time but not **stack depth**.

---

Back to the [start of the book](../index.md) · [Glossary](../glossary.md) · [Sources](../sources.md)
