---
short_title: 2 · Backward substitutions
---

# The Method of Backward Substitutions

**Solving** a recurrence means finding a **closed form**: a formula for $M(n)$ that contains no $M$ on the
right-hand side, such as $M(n) = 3n + 1$. The simplest general method is **backward substitutions**: we
replace $M(\text{smaller})$ by its own recurrence again and again until a pattern appears.

## The procedure (checklist)

1. **Write** the recurrence and the initial condition. Check that the initial condition matches the
   stopping case of the algorithm.
2. **Substitute** the recurrence into itself two or three times. **Do not simplify** the structure away:
   keep $2^2 M(n-2) + 2 + 1$ instead of $4M(n-2) + 3$, so the pattern stays visible.
3. **Guess the general form** after $i$ substitutions.
4. **Choose $i$** so that the argument reaches the initial condition (e.g. $n - i = 0$, i.e. $i = n$).
5. **Simplify** using the sum formulas of Module 1.
6. **Verify**: plug the answer back into the recurrence and the initial condition, or prove it by
   induction.

## A first example, step by step

Solve

$$
T(n) = T(n-1) + 3 \quad \text{for } n > 0, \qquad T(0) = 1 .
$$

**Step 2 · Substitute.** The recurrence holds for every $n > 0$, so also $T(n-1) = T(n-2) + 3$,
$T(n-2) = T(n-3) + 3$, and so on:

$$
\begin{aligned}
T(n) &= T(n-1) + 3 \\
     &= [T(n-2) + 3] + 3 = T(n-2) + 2 \cdot 3 \\
     &= [T(n-3) + 3] + 2 \cdot 3 = T(n-3) + 3 \cdot 3 .
\end{aligned}
$$

**Step 3 · General form.** After $i$ substitutions:

$$
T(n) = T(n - i) + 3i .
$$

**Step 4 · Reach the initial condition.** The initial condition is at argument $0$, so take $n - i = 0$,
i.e. $i = n$:

$$
T(n) = T(0) + 3n = 1 + 3n .
$$

**Step 5 · Simplify.** Already simple: $T(n) = 3n + 1 \in \Theta(n)$.

**Step 6 · Verify by plugging in.**

- Initial condition: $T(0) = 3 \cdot 0 + 1 = 1$. ✔
- Recurrence: $T(n-1) + 3 = (3(n-1) + 1) + 3 = 3n + 1 = T(n)$. ✔

Both hold, so $T(n) = 3n + 1$ is the solution.

## Why verify? Proof by induction

In Step 3 we **guessed** the general form from a few lines. A guess can be wrong, so it must be checked.
Plugging in (as above) is one way. The standard way is **mathematical induction**:

:::{note} Mathematical induction in two steps
To prove that a statement $P(n)$ is true for all $n \ge n_0$:

1. **Base case:** prove $P(n_0)$.
2. **Inductive step:** assume $P(n-1)$ is true (the **inductive hypothesis**) and prove $P(n)$.

Then $P(n_0)$ is true, so $P(n_0 + 1)$ is true, so $P(n_0 + 2)$ is true, and so on — like a chain of
falling dominoes.
:::

**Example.** Prove that $T(n) = 3n + 1$ for the recurrence above.

- **Base case** $n = 0$: $T(0) = 1$ by the initial condition, and $3 \cdot 0 + 1 = 1$. ✔
- **Inductive step.** Assume $T(n-1) = 3(n-1) + 1$ for some $n \ge 1$. Then, by the recurrence,
  $$T(n) = T(n-1) + 3 = 3(n-1) + 1 + 3 = 3n + 1 . \quad \checkmark$$

So $T(n) = 3n + 1$ for all $n \ge 0$.

## Recurrences with $n/2$: the "$n = 2^k$" trick

Recurrences like

$$
A(n) = A(\lfloor n/2 \rfloor) + 1, \qquad A(1) = 0
$$

are awkward because of the floor. The standard trick is to solve the recurrence **first for powers of
two**, $n = 2^k$, where $n/2$ is always an integer:

$$
A(2^k) = A(2^{k-1}) + 1, \qquad A(2^0) = A(1) = 0 .
$$

Now substitute backwards in $k$:

$$
\begin{aligned}
A(2^k) &= A(2^{k-1}) + 1 = A(2^{k-2}) + 2 = \dots = A(2^{k-i}) + i \\
       &= \dots = A(2^0) + k = k .
\end{aligned}
$$

Since $n = 2^k$ means $k = \log_2 n$, we get $A(n) = \log_2 n \in \Theta(\log n)$ for powers of two.

Why may we then claim $\Theta(\log n)$ for **all** $n$? Levitin's textbook (Appendix B) states the
**smoothness rule**: if the solution is eventually nondecreasing and the growth function (like $\log n$,
$n$, $n^2$, $n\log n$) is "smooth", then the order of growth found for $n = 2^k$ holds for all $n$. All
recurrences in this book satisfy these conditions; we use the rule without proof. (For BinRec the exact
answer for every $n$ is in fact $A(n) = \lfloor \log_2 n \rfloor$.)

## Checklist of common errors

:::{warning} Watch out for
- **Simplifying too early.** $2^2 M(n-2) + 2 + 1$ shows the pattern; $4M(n-2) + 3$ hides it.
- **Choosing the wrong $i$.** The argument must reach exactly the initial condition: if the initial
  condition is $M(1)$, take $n - i = 1$, i.e. $i = n - 1$, not $i = n$.
- **Forgetting the initial value** when substituting: $M(n) = M(1) + (n-1)$, and $M(1)$ need not be
  $0$.
- **Skipping the verification.** Always plug the answer back in, at least for $n = 1, 2, 3$.
:::

Next: the method applied to six algorithms in the [Worked examples](03_worked_examples.md).
