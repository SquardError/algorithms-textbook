---
short_title: 8 · Problems
---

# Module 1 Problems

Thirteen problems in five groups. Each problem has three nested blocks: open the **hint** only if you are
stuck, then the **answer** to check yourself, then the **full solution**. Every answer was checked by
counting operations in
[`code/verify/verify_m1_problems.py`](https://github.com/SquardError/algorithms-textbook/blob/main/code/verify/verify_m1_problems.py).

| Group | Problems | What they train |
|---|---|---|
| Level A | [A1](#m1-a1) · [A2](#m1-a2) · [A3](#m1-a3) · [A4](#m1-a4) | the plan and one formula |
| Level B | [B1](#m1-b1) · [B2](#m1-b2) · [B3](#m1-b3) · [B4](#m1-b4) | nested sums, dependent bounds, cases |
| Level C | [C1](#m1-c1) · [C2](#m1-c2) | average case, logarithmic loops |
| Find the mistake | [M1](#m1-m1) · [M2](#m1-m2) | typical mistakes |
| Empirical | [E1](#m1-e1) | operation counter vs. formula |

---

## Level A (basic)

(m1-a1)=
### A1 · Dot product

Analyze the number of multiplications.

```text
ALGORITHM DotProduct(x[0..n-1], y[0..n-1])
    //Computes the dot product of two vectors of length n
    s ← 0
    for i ← 0 to n - 1 do
        s ← s + x[i] * y[i]
    return s
```

:::::{dropdown} Hint
Follow the five steps. Is there any way for the loop to stop early?
::::{dropdown} Answer
$M(n) = n \in \Theta(n)$ for every input.
:::{dropdown} Full solution
1. **Input size:** $n$, the length of the vectors.
2. **Basic operation:** the multiplication `x[i] * y[i]` (one per iteration; the addition runs equally
   often, so either choice gives the same count).
3. **Cases:** no early exit; the count depends only on $n$.
4. **Sum:** $M(n) = \sum_{i=0}^{n-1} 1$.
5. **Solution:** $M(n) = (n-1) - 0 + 1 = n \in \Theta(n)$.
:::
::::
:::::

(m1-a2)=
### A2 · Evaluate a sum

Find a closed form and the order of growth of $\displaystyle S(n) = \sum_{i=1}^{n} (3i + 2)$.

:::::{dropdown} Hint
Split the sum into two sums (rule R2) and take the constant 3 out (rule R1).
::::{dropdown} Answer
$S(n) = \dfrac{3n^2 + 7n}{2} \in \Theta(n^2)$.
:::{dropdown} Full solution
$$
\begin{aligned}
S(n) &= 3\sum_{i=1}^{n} i + 2\sum_{i=1}^{n} 1 = 3 \cdot \frac{n(n+1)}{2} + 2n \\
     &= \frac{3n^2 + 3n + 4n}{2} = \frac{3n^2 + 7n}{2}.
\end{aligned}
$$

Check with $n = 2$: $(3 + 2) + (6 + 2) = 13$ and $\frac{12 + 14}{2} = 13$. ✔

The leading term is $\frac32 n^2$, so $S(n) \in \Theta(n^2)$.
:::
::::
:::::

(m1-a3)=
### A3 · Counting iterations

How many times is `op` executed? Give an exact formula for $n \ge 1$.

```text
for i ← 3 to 2n do
    for j ← 1 to 5 do
        op
```

:::::{dropdown} Hint
The inner loop always runs the same number of times. How many values does $i$ take?
::::{dropdown} Answer
$C(n) = 10n - 10 = 10(n-1) \in \Theta(n)$.
:::{dropdown} Full solution
$$
\begin{aligned}
C(n) &= \sum_{i=3}^{2n} \sum_{j=1}^{5} 1 = \sum_{i=3}^{2n} 5 \\
     &= 5\,(2n - 3 + 1) = 5(2n - 2) = 10n - 10.
\end{aligned}
$$

Check with $n = 2$: $i = 3, 4$ (2 values) × 5 = 10, and $10 \cdot 2 - 10 = 10$. ✔
For $n = 1$ the loop `for i ← 3 to 2` does not run at all, and the formula gives $0$. ✔
:::
::::
:::::

(m1-a4)=
### A4 · Minimum and maximum in one pass

Analyze the number of key comparisons.

```text
ALGORITHM MinMax(A[0..n-1])
    //Finds both the smallest and the largest element of A
    min ← A[0];  max ← A[0]
    for i ← 1 to n - 1 do
        if A[i] < min  min ← A[i]
        if A[i] > max  max ← A[i]
    return (min, max)
```

:::::{dropdown} Hint
How many comparisons are made in one iteration? Do they always both run?
::::{dropdown} Answer
$C(n) = 2(n - 1) \in \Theta(n)$ for every input.
:::{dropdown} Full solution
1. **Input size:** $n$.
2. **Basic operation:** key comparison. Each iteration performs **two** comparisons, `A[i] < min` and
   `A[i] > max`; both are always executed (they are two separate `if` statements).
3. **Cases:** no early exit, so the count depends only on $n$.
4. **Sum:** $C(n) = \sum_{i=1}^{n-1} 2$.
5. **Solution:** $C(n) = 2\,\big((n-1) - 1 + 1\big) = 2(n-1) \in \Theta(n)$.
:::
::::
:::::

---

## Level B (intermediate)

(m1-b1)=
### B1 · An odd-shaped loop

Find the exact number of executions of `op` and its order of growth.

```text
for i ← 0 to n - 1 do
    for j ← 0 to 2i do
        op
```

:::::{dropdown} Hint
How many values does $j$ take for a fixed $i$? Then sum over $i$. The sum of the first $n$ odd numbers
has a very nice closed form.
::::{dropdown} Answer
$C(n) = n^2 \in \Theta(n^2)$.
:::{dropdown} Full solution
The inner loop runs for $j = 0, 1, \dots, 2i$: that is $2i - 0 + 1 = 2i + 1$ times. So

$$
\begin{aligned}
C(n) &= \sum_{i=0}^{n-1} (2i + 1) = 2\sum_{i=0}^{n-1} i + \sum_{i=0}^{n-1} 1 \\
     &= 2 \cdot \frac{(n-1)n}{2} + n = n^2 - n + n = n^2.
\end{aligned}
$$

(We used $\sum_{i=0}^{n-1} i = \sum_{i=1}^{n-1} i = \frac{(n-1)n}{2}$, because the term $i = 0$ adds nothing.)

Check with $n = 3$: $1 + 3 + 5 = 9 = 3^2$. ✔ This is the classic fact that the sum of the first $n$ odd
numbers is $n^2$.
:::
::::
:::::

(m1-b2)=
### B2 · Does the matrix have a zero row?

Analyze the number of comparisons `M[i, j] = 0` in the **worst** and **best** cases.

```text
ALGORITHM HasZeroRow(M[0..n-1, 0..n-1])
    //Returns true if some row of M consists only of zeros
    for i ← 0 to n - 1 do
        j ← 0
        while j < n and M[i, j] = 0 do
            j ← j + 1
        if j = n return true
    return false
```

Assume that the `while` condition is evaluated left to right and stops as soon as `j < n` is false (so no
comparison `M[i, j] = 0` is made for $j = n$).

:::::{dropdown} Hint
How many comparisons does one row cost? It depends on where the first nonzero element of the row is.
Which inputs make every row as expensive as possible, and can the algorithm still not stop early? For
the best case: is it possible to make **fewer than $n$** comparisons?
::::{dropdown} Answer
$C_{worst}(n) = n^2 \in \Theta(n^2)$; $C_{best}(n) = n \in \Theta(n)$.
:::{dropdown} Full solution
1. **Input size:** $n$, the order of the matrix.
2. **Basic operation:** the comparison `M[i, j] = 0`.
3. **Cases:** the `while` loop stops at the first nonzero element of a row, and the algorithm stops at
   the first zero row. So the count depends on the input.

**Cost of one row.** If the first nonzero element of row $i$ is in column $t$ ($0 \le t \le n-1$), the
row costs $t + 1$ comparisons. If the row is all zeros, it costs $n$ comparisons (columns $0, \dots, n-1$)
and the algorithm returns `true`.

**Worst case.** Each row costs at most $n$, and there are at most $n$ rows, so $C(n) \le n^2$. The bound is
reached, e.g., when every row has its only nonzero element in the **last** column: each row costs $n$
comparisons, no row is zero, all $n$ rows are inspected:

$$
C_{worst}(n) = \sum_{i=0}^{n-1} n = n^2 \in \Theta(n^2).
$$

(A matrix whose last row is the only zero row also needs $n^2$.)

**Best case.** Every row that is inspected costs at least 1 comparison. Two kinds of inputs are cheap:

- the first row is all zeros → $n$ comparisons, then `return true`;
- every row starts with a nonzero element → each row costs 1, all $n$ rows inspected → $n$ comparisons.

Can it be fewer than $n$? To stop after row $i$, row $i$ must be a zero row, which costs $n$ comparisons by
itself. If no row is zero, all $n$ rows are inspected, at least 1 comparison each. Either way the count is
at least $n$. So

$$
C_{best}(n) = n \in \Theta(n).
$$

**Note.** Unlike sequential search, the best case here is **not** constant. Always derive it — never
assume it is 1.
:::
::::
:::::

(m1-b3)=
### B3 · Three nested loops with dependent bounds

Find the exact number of executions of `op`.

```text
for i ← 1 to n do
    for j ← 1 to i do
        for k ← 1 to j do
            op
```

:::::{dropdown} Hint
Inside out: the $k$-loop gives $j$; the $j$-loop then gives $\sum_{j=1}^{i} j$. Finally you need both S1 and
S2.
::::{dropdown} Answer
$C(n) = \dfrac{n(n+1)(n+2)}{6} \in \Theta(n^3)$.
:::{dropdown} Full solution
$$
\begin{aligned}
C(n) &= \sum_{i=1}^{n} \sum_{j=1}^{i} \sum_{k=1}^{j} 1 = \sum_{i=1}^{n} \sum_{j=1}^{i} j \\
     &= \sum_{i=1}^{n} \frac{i(i+1)}{2} = \frac12 \left( \sum_{i=1}^{n} i^2 + \sum_{i=1}^{n} i \right).
\end{aligned}
$$

By S2 and S1:

$$
\begin{aligned}
C(n) &= \frac12 \left( \frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2} \right) \\
     &= \frac{n(n+1)}{12} \big( (2n + 1) + 3 \big) \\
     &= \frac{n(n+1)(2n+4)}{12} = \frac{n(n+1)(n+2)}{6}.
\end{aligned}
$$

Check with $n = 2$: $(i, j, k) \in \{(1,1,1), (2,1,1), (2,2,1), (2,2,2)\}$ — 4 executions; formula
$\frac{2 \cdot 3 \cdot 4}{6} = 4$. ✔ The leading term is $\frac{n^3}{6}$, so $C(n) \in \Theta(n^3)$.
:::
::::
:::::

(m1-b4)=
### B4 · Prefix sums, the slow way and the fast way

The prefix sums of an array are $P[i] = A[0] + A[1] + \dots + A[i]$.

```text
ALGORITHM PrefixSumsNaive(A[0..n-1])
    for i ← 0 to n - 1 do
        s ← 0
        for j ← 0 to i do
            s ← s + A[j]
        P[i] ← s
    return P
```

(a) Find the number of additions `s + A[j]`.
(b) Write an algorithm that computes the same array with $n - 1$ additions, and compare the counts for
$n = 1000$.

:::::{dropdown} Hint
(a) How many times does the inner loop run for a given $i$? (b) $P[i]$ can be obtained from $P[i-1]$.
::::{dropdown} Answer
(a) $A(n) = \dfrac{n(n+1)}{2} \in \Theta(n^2)$. (b) $P[0] \leftarrow A[0]$, then
$P[i] \leftarrow P[i-1] + A[i]$: $n - 1$ additions. For $n = 1000$: $500\,500$ vs. $999$.
:::{dropdown} Full solution
**(a)** Basic operation: the addition in the inner loop. No early exit. For a fixed $i$ the inner loop runs
for $j = 0, \dots, i$, i.e. $i + 1$ times:

$$
A(n) = \sum_{i=0}^{n-1} (i + 1) = \sum_{m=1}^{n} m = \frac{n(n+1)}{2} \in \Theta(n^2)
$$

(substituting $m = i + 1$).

**(b)**

```text
ALGORITHM PrefixSumsFast(A[0..n-1])
    P[0] ← A[0]
    for i ← 1 to n - 1 do
        P[i] ← P[i - 1] + A[i]
    return P
```

Additions: $\sum_{i=1}^{n-1} 1 = n - 1 \in \Theta(n)$.

For $n = 1000$: $\frac{1000 \cdot 1001}{2} = 500\,500$ additions versus $999$ — about 500 times fewer.
The naive algorithm recomputes the same partial sums again and again; reusing $P[i-1]$ removes the
inner loop.
:::
::::
:::::

---

## Level C (advanced)

(m1-c1)=
### C1 · Average case: find the first even number

```text
ALGORITHM FirstEven(A[0..n-1])
    //Returns the index of the first even element, or -1
    for i ← 0 to n - 1 do
        if A[i] mod 2 = 0 return i
    return -1
```

Assume that each element is even with probability $\frac12$, independently of the others. Find the
**average** number of parity checks `A[i] mod 2 = 0` and compare it with the worst case.

:::::{dropdown} Hint
The algorithm performs **at least $i$** checks exactly when the first $i - 1$ elements are all odd. The
probability of that is $(1/2)^{i-1}$. The expected number of checks equals
$\sum_{i=1}^{n} P(\text{at least } i \text{ checks})$ — a geometric series. (Alternatively, list the
outcomes "first even at position $i$" and "no even element" as in the sequential-search example.)
::::{dropdown} Answer
$C_{avg}(n) = 2 - \dfrac{1}{2^{n-1}} = 2 - 2^{1-n} < 2$, so $C_{avg}(n) \in \Theta(1)$, while
$C_{worst}(n) = n$.
:::{dropdown} Full solution
**Steps 1–3.** Input size $n$; basic operation: the parity check; early exit exists, so the count depends
on the input: $C_{best}(n) = 1$, $C_{worst}(n) = n$ (all elements odd, or only the last even).

**Step 4 · Model.** The algorithm makes at least $i$ checks ($1 \le i \le n$) exactly when elements
$1, \dots, i - 1$ (counting from 1) are all odd. By independence this has probability
$\left(\frac12\right)^{i-1}$.

For a count $C$ that takes values $1, \dots, n$, the expected value can be written as
$E[C] = \sum_{i=1}^{n} P(C \ge i)$, because each value $c$ is counted once for every $i \le c$. Hence

$$
C_{avg}(n) = \sum_{i=1}^{n} \left(\tfrac12\right)^{i-1}.
$$

**Step 5 · Evaluate.** This is a geometric series with ratio $a = \frac12$ and $n$ terms:

$$
C_{avg}(n) = \frac{1 - (1/2)^n}{1 - 1/2} = 2\left(1 - \frac{1}{2^n}\right) = 2 - \frac{1}{2^{n-1}}.
$$

**Check by listing outcomes** for $n = 3$. First even at position 1: probability $\frac12$, 1 check;
position 2: $\frac14$, 2 checks; position 3: $\frac18$, 3 checks; no even element: $\frac18$, 3 checks.

$$
\tfrac12 \cdot 1 + \tfrac14 \cdot 2 + \tfrac18 \cdot 3 + \tfrac18 \cdot 3 = \tfrac{4 + 4 + 3 + 3}{8} = \tfrac74,
\qquad 2 - \tfrac{1}{2^{2}} = \tfrac74 \quad \checkmark
$$

**Conclusion.** The worst case is $\Theta(n)$, but on average fewer than **2** checks are needed, for any
$n$: $C_{avg}(n) \in \Theta(1)$. The average case can be dramatically better than the worst case — and it
depends entirely on the model (if even numbers were rare, the answer would change).
:::
::::
:::::

(m1-c2)=
### C2 · A halving outer loop with a linear inner loop

```text
i ← n
while i ≥ 1 do
    for j ← 1 to i do
        op
    i ← ⌊i / 2⌋
```

(a) Find the exact count for $n = 2^k$. (b) Show that $n \le C(n) < 2n$ for every $n \ge 1$ and give the
order of growth. (c) A student says: "the outer loop runs $\log n$ times and the inner loop up to $n$
times, so the answer is $\Theta(n \log n)$". Explain what is wrong.

:::::{dropdown} Hint
Write down the values of $i$: $n, n/2, n/4, \dots, 1$. The inner loop runs $i$ times, so the count is the sum
of these values. Recognize a geometric series.
::::{dropdown} Answer
(a) $C(2^k) = 2^{k+1} - 1 = 2n - 1$. (b) $C(n) \in \Theta(n)$. (c) $n \log n$ is only an **upper bound**:
the inner loop runs $n$ times only in the first iteration and then gets shorter and shorter.
:::{dropdown} Full solution
**(a)** For $n = 2^k$ the variable $i$ takes the values $2^k, 2^{k-1}, \dots, 2, 1$ (the loop stops when
$i$ becomes $0$). The inner loop runs $i$ times, so

$$
C(2^k) = 2^k + 2^{k-1} + \dots + 2 + 1 = \sum_{t=0}^{k} 2^t = 2^{k+1} - 1 = 2n - 1
$$

by formula S3.

**(b)** For general $n$ the values of $i$ are $n, \lfloor n/2 \rfloor, \lfloor n/4 \rfloor, \dots, 1$. The first
term alone gives $C(n) \ge n$. Since $\lfloor n / 2^t \rfloor \le n / 2^t$,

$$
C(n) \le n\left(1 + \tfrac12 + \tfrac14 + \dots\right) < n \cdot 2 = 2n .
$$

So $n \le C(n) < 2n$, and therefore $C(n) \in \Theta(n)$. (Example: $n = 100$ gives
$100 + 50 + 25 + 12 + 6 + 3 + 1 = 197$.)

**(c)** Multiplying "number of outer iterations" by "the **largest** inner count" gives only an upper bound,
$O(n \log n)$. It is not tight, because the inner counts decrease geometrically. Always write the sum of
the actual inner counts.
:::
::::
:::::

---

## Find the mistake

Each solution below contains **exactly one** typical mistake from
[Typical mistakes](05_typical_mistakes.md). Find it before opening the blocks.

(m1-m1)=
### M1 · Is the array sorted?

```text
ALGORITHM IsSorted(A[0..n-1])
    for i ← 0 to n - 2 do
        if A[i] > A[i + 1] return false
    return true
```

> **Student's solution.** Input size $n$; basic operation: the comparison `A[i] > A[i + 1]`. The loop runs
> for $i = 0, \dots, n - 2$, so $C(n) = \sum_{i=0}^{n-2} 1 = n - 1$. Therefore IsSorted makes $n - 1$
> comparisons on every input of size $n$, and its running time is $\Theta(n)$ for all inputs.

:::::{dropdown} Hint
Read the loop body once more. Can the loop end before $i$ reaches $n - 2$?
::::{dropdown} Answer
The mistake is **ignoring early termination** (Step 3 skipped). Correct:
$C_{worst}(n) = n - 1 \in \Theta(n)$, $C_{best}(n) = 1 \in \Theta(1)$, the algorithm is in $O(n)$.
:::{dropdown} Full solution
**Diagnosis.** The input size, the basic operation and the sum are all correct — but the sum describes
only the inputs on which the loop runs to the end. The `return false` inside the loop makes the count
depend on the input; the student never did Step 3.

**Correct solution.**

- **Worst case:** the loop runs to the end when no pair is out of order (a sorted array), or when the only
  out-of-order pair is the last one. $C_{worst}(n) = \sum_{i=0}^{n-2} 1 = n - 1 \in \Theta(n)$.
- **Best case:** $A[0] > A[1]$; the first comparison returns `false`. $C_{best}(n) = 1 \in \Theta(1)$.

So the correct statement is: *IsSorted makes at most $n - 1$ comparisons; its worst case is $\Theta(n)$,
its best case $\Theta(1)$; it is in $O(n)$.*
:::
::::
:::::

(m1-m2)=
### M2 · Sum of divisors

```text
ALGORITHM SumDivisors(n)
    //Input: a positive integer n
    s ← 0
    for d ← 1 to n do
        if n mod d = 0  s ← s + d
    return s
```

> **Student's solution.** Input size: $n$. Basic operation: the division `n mod d`. No early exit, so
> $C(n) = \sum_{d=1}^{n} 1 = n \in \Theta(n)$. The algorithm is linear in the input size, so it is
> efficient even for inputs written with hundreds of digits.

:::::{dropdown} Hint
The count $C(n) = n$ is right. What exactly is the "size" of an input that consists of one number?
::::{dropdown} Answer
The mistake is **confusing the input size with the value**. With $b = \lfloor \log_2 n \rfloor + 1$ bits,
$C = n \ge 2^{b-1}$, so the algorithm is $\Theta(2^b)$ — exponential in the input size, and hopeless for
numbers with hundreds of digits.
:::{dropdown} Full solution
**Diagnosis.** Steps 2–5 are correct: there are exactly $n$ divisions. The error is in Step 1: the input is
a single number, and its size is the number of bits needed to write it, not its value.

**Correct solution.** Let $b = \lfloor \log_2 n \rfloor + 1$ be the number of bits of $n$. Then
$2^{b-1} \le n < 2^b$, so

$$
C = n \in \Theta(2^b).
$$

The algorithm is **linear in the value** of $n$ but **exponential in the size** of the input. For a
30-bit number it already needs at least $2^{29} \approx 5.4 \cdot 10^8$ divisions; for a number with
hundreds of digits the count is astronomically large.
:::
::::
:::::

---

## Empirical task

(m1-e1)=
### E1 · Counting zero-sum triples

```text
ALGORITHM ZeroTriples(A[0..n-1])
    //Counts triples i < j < k with A[i] + A[j] + A[k] = 0
    count ← 0
    for i ← 0 to n - 3 do
        for j ← i + 1 to n - 2 do
            for k ← j + 1 to n - 1 do
                if A[i] + A[j] + A[k] = 0  count ← count + 1
    return count
```

1. Derive the number of comparisons `A[i] + A[j] + A[k] = 0` as a formula $C(n)$.
2. Write a Python function with an operation counter, run it for $n = 3, \dots, 20$ and for
   $n = 50, 100, 200$ on random arrays, and print a table $n$ | counted | formula.
3. Plot counted values and the formula. Does the experiment confirm the formula? By what factor does the
   count grow when $n$ doubles?

:::::{dropdown} Hint
The algorithm looks at every set of three different positions exactly once. How many 3-element subsets
does a set of $n$ elements have? Alternatively, evaluate the triple sum inside out (the inner sum gives
$n - 1 - j$).
::::{dropdown} Answer
$C(n) = \binom{n}{3} = \dfrac{n(n-1)(n-2)}{6} \in \Theta(n^3)$ for every input. Doubling $n$ multiplies the
count by about 8.
:::{dropdown} Full solution
**Derivation.** No early exit, so the count depends only on $n$. Each triple of positions $i < j < k$ is
examined once, and the number of such triples is the number of 3-element subsets:

$$
C(n) = \binom{n}{3} = \frac{n(n-1)(n-2)}{6} \in \Theta(n^3).
$$

**Code.**

```python
import random
import matplotlib.pyplot as plt

def zero_triples_count(A):
    n, comparisons, count = len(A), 0, 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                comparisons += 1
                if A[i] + A[j] + A[k] == 0:
                    count += 1
    return count, comparisons

formula = lambda n: n * (n - 1) * (n - 2) // 6
sizes = list(range(3, 21)) + [50, 100, 200]
counted = []
print(f"{'n':>4} | {'counted':>8} | {'formula':>8}")
for n in sizes:
    A = [random.randint(-50, 50) for _ in range(n)]
    c = zero_triples_count(A)[1]
    counted.append(c)
    print(f"{n:>4} | {c:>8} | {formula(n):>8}")

plt.plot(sizes, counted, "o", label="counted")
plt.plot(range(3, 201), [formula(n) for n in range(3, 201)], label="n(n-1)(n-2)/6")
plt.xlabel("n"); plt.ylabel("comparisons"); plt.legend(); plt.show()
```

**Expected result.** Every row matches, e.g. $n = 10$: $120$; $n = 20$: $1140$; $n = 100$: $161\,700$;
$n = 200$: $1\,313\,400$. The points lie on the cubic curve.

**Conclusion.** The experiment confirms $C(n) = \frac{n(n-1)(n-2)}{6}$. From $n = 100$ to $n = 200$ the
count grows by a factor of $1\,313\,400 / 161\,700 \approx 8.1$, close to $2^3 = 8$, as expected for
$\Theta(n^3)$.
:::
::::
:::::
