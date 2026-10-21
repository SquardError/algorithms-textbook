---
short_title: 7 · Problems
---

# Module 2 Problems

Thirteen problems in five groups. Open the **hint** only if you are stuck, then the **answer**, then the
**full solution**. Every answer was checked by running the algorithms and evaluating the recurrences in
[`code/verify/verify_m2_problems.py`](https://github.com/SquardError/algorithms-textbook/blob/main/code/verify/verify_m2_problems.py).

| Group | Problems | What they train |
|---|---|---|
| Level A | [A1](#m2-a1) · [A2](#m2-a2) · [A3](#m2-a3) · [A4](#m2-a4) | set up and solve a simple recurrence |
| Level B | [B1](#m2-b1) · [B2](#m2-b2) · [B3](#m2-b3) · [B4](#m2-b4) | non-trivial recurrences, $n = 2^k$, $10^k$ |
| Level C | [C1](#m2-c1) · [C2](#m2-c2) | proofs by induction |
| Find the mistake | [M1](#m2-m1) · [M2](#m2-m2) | typical mistakes in recurrences |
| Empirical | [E1](#m2-e1) | call counter vs. formula |

---

## Level A (basic)

(m2-a1)=
### A1 · Naive power

Set up and solve a recurrence for the number of multiplications.

```text
ALGORITHM PowerNaive(a, n)
    //Computes a^n for an integer n ≥ 0
    if n = 0 return 1
    else return a * PowerNaive(a, n - 1)
```

:::::{dropdown} Hint
Compare with the factorial. How many multiplications are done in the call with $n = 0$?
::::{dropdown} Answer
$M(n) = M(n-1) + 1$, $M(0) = 0$; $M(n) = n \in \Theta(n)$.
:::{dropdown} Full solution
1. **Input size:** the exponent $n$.
2. **Basic operation:** multiplication.
3. **Cases:** depends only on $n$.
4. **Recurrence:** one call on $n - 1$ plus one multiplication; the stopping case $n = 0$ returns 1 with no
   multiplication: $M(n) = M(n-1) + 1$ for $n > 0$, $M(0) = 0$.
5. **Solution:** $M(n) = M(n-1) + 1 = M(n-2) + 2 = \dots = M(n-i) + i$; with $i = n$,
   $M(n) = M(0) + n = n$.

**Check:** $M(0) = 0$ ✔, $M(n-1) + 1 = n$ ✔. Compare with the [fast exponentiation](03_worked_examples.md#ex2-power)
example: $\Theta(\log n)$ instead of $\Theta(n)$.
:::
::::
:::::

(m2-a2)=
### A2 · Solve a recurrence

Solve $T(n) = T(n-1) + 5$ for $n > 1$, $T(1) = 2$, by backward substitutions and check the answer.

:::::{dropdown} Hint
The general form after $i$ steps is $T(n-i) + 5i$. Be careful: the initial condition is at $1$, not at $0$.
::::{dropdown} Answer
$T(n) = 5n - 3 \in \Theta(n)$.
:::{dropdown} Full solution
$$
\begin{aligned}
T(n) &= T(n-1) + 5 = T(n-2) + 2\cdot 5 = T(n-3) + 3 \cdot 5 \\
     &= \dots = T(n-i) + 5i .
\end{aligned}
$$

To reach $T(1)$ take $n - i = 1$, i.e. $i = n - 1$:

$$
T(n) = T(1) + 5(n-1) = 2 + 5n - 5 = 5n - 3 .
$$

**Check:** $T(1) = 5 - 3 = 2$ ✔; $T(n-1) + 5 = 5(n-1) - 3 + 5 = 5n - 3$ ✔.
:::
::::
:::::

(m2-a3)=
### A3 · Recursive search from the end

```text
ALGORITHM SearchFromEnd(A[0..n-1], K)
    //Returns the largest index i with A[i] = K, or -1
    if n = 0 return -1
    if A[n-1] = K return n - 1
    else return SearchFromEnd(A[0..n-2], K)
```

Set up a recurrence for the number of key comparisons in the worst case and solve it. What is the best
case?

:::::{dropdown} Hint
Step 3 matters: the algorithm can stop early. Which inputs make it go all the way down to $n = 0$?
::::{dropdown} Answer
$C_{worst}(n) = C_{worst}(n-1) + 1$, $C_{worst}(0) = 0$, so $C_{worst}(n) = n$. $C_{best}(n) = 1$
(when $A[n-1] = K$).
:::{dropdown} Full solution
1. **Input size:** $n$. 2. **Basic operation:** the comparison `A[n-1] = K`.
3. **Cases:** the search stops at the first (rightmost) match, so we need cases.
   - **Best case:** $A[n-1] = K$: one comparison, $C_{best}(n) = 1$.
   - **Worst case:** $K$ is absent or only in $A[0]$: every call compares once and recurses.
4. **Recurrence (worst case):** $C_{worst}(n) = C_{worst}(n-1) + 1$ for $n > 0$, and $C_{worst}(0) = 0$ (an
   empty array needs no comparison).
5. **Solution:** $C_{worst}(n) = C_{worst}(n - i) + i$; with $i = n$, $C_{worst}(n) = n \in \Theta(n)$.

The recursion depth is $n + 1$ in the worst case — the iterative loop does the same comparisons with
$\Theta(1)$ memory.
:::
::::
:::::

(m2-a4)=
### A4 · Number of ternary digits

```text
ALGORITHM TernDigits(n)
    //Number of digits of the positive integer n in base 3
    if n < 3 return 1
    else return TernDigits(⌊n/3⌋) + 1
```

Set up a recurrence for the number of additions and solve it for $n = 3^k$.

:::::{dropdown} Hint
Imitate BinRec, with 3 instead of 2. For $n = 3^k$, $\lfloor n/3 \rfloor = 3^{k-1}$. What is the stopping case
when $n = 3^k$?
::::{dropdown} Answer
$A(n) = A(\lfloor n/3 \rfloor) + 1$ for $n \ge 3$, $A(1) = A(2) = 0$. For $n = 3^k$: $A(n) = k = \log_3 n$,
so $A(n) \in \Theta(\log n)$. (In general $A(n) = \lfloor \log_3 n \rfloor$.)
:::{dropdown} Full solution
**Recurrence.** One call on $\lfloor n/3 \rfloor$ plus one addition; for $n < 3$ no addition:
$A(n) = A(\lfloor n/3 \rfloor) + 1$ for $n \ge 3$, $A(1) = A(2) = 0$.

**Solution for $n = 3^k$.** The arguments are $3^k, 3^{k-1}, \dots, 3^0 = 1$:

$$
\begin{aligned}
A(3^k) &= A(3^{k-1}) + 1 = A(3^{k-2}) + 2 = \dots \\
       &= A(3^{k-i}) + i = \dots = A(3^0) + k = k .
\end{aligned}
$$

With $k = \log_3 n$: $A(n) = \log_3 n \in \Theta(\log n)$ (the base does not matter). Example: $n = 81 = 3^4$
gives 4 additions; the result is $4 + 1 = 5$ digits ($81 = 10000_3$).
:::
::::
:::::

---

## Level B (intermediate)

(m2-b1)=
### B1 · A loop inside a recursion

```text
ALGORITHM Rec(n)
    if n = 0 return
    for i ← 1 to 2n - 1 do
        op
    Rec(n - 1)
```

Find the number of executions of `op`.

:::::{dropdown} Hint
The work in the current call is $2n - 1$, not 1. After backward substitution you get a sum; recall the
sum of the first $n$ odd numbers (or use S1).
::::{dropdown} Answer
$T(n) = T(n-1) + (2n - 1)$, $T(0) = 0$, so $T(n) = n^2 \in \Theta(n^2)$.
:::{dropdown} Full solution
**Recurrence.** The loop executes `op` $(2n - 1) - 1 + 1 = 2n - 1$ times, then one call on $n - 1$; for
$n = 0$ nothing happens:

$$
T(n) = T(n-1) + (2n - 1) \quad (n > 0), \qquad T(0) = 0 .
$$

**Backward substitutions.**

$$
\begin{aligned}
T(n) &= T(n-1) + (2n-1) \\
&= T(n-2) + (2(n-1) - 1) + (2n - 1) \\
&\;\;\vdots \\
&= T(n-i) + \sum_{j=n-i+1}^{n} (2j - 1) .
\end{aligned}
$$

With $i = n$:

$$
T(n) = T(0) + \sum_{j=1}^{n} (2j - 1) = 2 \cdot \frac{n(n+1)}{2} - n = n^2 .
$$

**Check:** $T(0) = 0$ ✔; $T(n-1) + 2n - 1 = (n-1)^2 + 2n - 1 = n^2$ ✔.
:::
::::
:::::

(m2-b2)=
### B2 · Sum of decimal digits

```text
ALGORITHM DigitSum(n)
    //Sum of the decimal digits of a nonnegative integer n
    if n < 10 return n
    else return DigitSum(⌊n/10⌋) + (n mod 10)
```

(a) Set up a recurrence for the number of additions and solve it for $n = 10^k$.
(b) What is the exact number of additions for an arbitrary $n \ge 1$? How many for $n = 40712$?
(c) Express the answer in terms of the number of digits $d$ of $n$.

:::::{dropdown} Hint
Each call removes the last digit. For $n = 10^k$, the arguments are $10^k, 10^{k-1}, \dots, 1$.
::::{dropdown} Answer
(a) $A(n) = A(\lfloor n/10 \rfloor) + 1$ for $n \ge 10$, $A(n) = 0$ for $n < 10$; $A(10^k) = k = \log_{10} n$.
(b) $A(n) = \lfloor \log_{10} n \rfloor$; for $40712$: $4$. (c) $A = d - 1$: linear in the number of digits,
logarithmic in the value.
:::{dropdown} Full solution
**(a)** One call on $\lfloor n/10 \rfloor$ plus one addition (the `+`; we do not count the `mod`); one-digit
numbers need no addition. For $n = 10^k$:

$$
\begin{aligned}
A(10^k) &= A(10^{k-1}) + 1 = \dots = A(10^{k-i}) + i \\
        &= \dots = A(10^0) + k = k = \log_{10} n .
\end{aligned}
$$

**(b)** A number with $d$ digits makes $d - 1$ calls before it becomes a one-digit number, each with one
addition, so $A(n) = d - 1 = \lfloor \log_{10} n \rfloor$. For $40712$ ($d = 5$): $4$ additions,
$4 + 0 + 7 + 1 + 2 = 14$.

**(c)** $A = d - 1 \in \Theta(d)$, linear in the size of the input written in decimal, and
$\Theta(\log n)$ in the value of $n$.
:::
::::
:::::

(m2-b3)=
### B3 · Maximum by divide and conquer

```text
ALGORITHM MaxDC(A[l..r])
    //Returns the largest element of A[l..r]
    if l = r return A[l]
    m ← ⌊(l + r)/2⌋
    a ← MaxDC(A[l..m]);  b ← MaxDC(A[m+1..r])
    if a > b return a else return b
```

Set up a recurrence for the number of comparisons `a > b` and solve it for $n = 2^k$. Compare with
MaxElement from Module 1.

:::::{dropdown} Hint
There are **two** recursive calls, each on half of the array: $2C(n/2)$. Substituting, you get a geometric
series.
::::{dropdown} Answer
$C(n) = 2C(n/2) + 1$, $C(1) = 0$; $C(n) = n - 1$ — exactly as many comparisons as MaxElement.
:::{dropdown} Full solution
**Recurrence.** For $n = 2^k$, two calls on $n/2$ elements plus one comparison; one element needs none:

$$
C(n) = 2C(n/2) + 1 \quad (n > 1), \qquad C(1) = 0 .
$$

**Substitutions** in $k$:

$$
\begin{aligned}
C(2^k) &= 2C(2^{k-1}) + 1 \\
&= 2[2C(2^{k-2}) + 1] + 1 = 2^2 C(2^{k-2}) + 2 + 1 \\
&\;\;\vdots \\
&= 2^i C(2^{k-i}) + 2^{i-1} + \dots + 2 + 1 = 2^i C(2^{k-i}) + 2^i - 1 .
\end{aligned}
$$

With $i = k$: $C(2^k) = 2^k C(1) + 2^k - 1 = n - 1$.

**Comparison.** MaxElement also makes $n - 1$ comparisons. Divide and conquer gives no gain here, and
it uses $\Theta(\log n)$ stack memory. (In fact $C(n) = n - 1$ for every $n$: every comparison eliminates
one candidate, and $n - 1$ candidates must be eliminated.)
:::
::::
:::::

(m2-b4)=
### B4 · One call or two?

```text
ALGORITHM Twice(n)                 ALGORITHM Once(n)
    if n = 1 return 1                  if n = 1 return 1
    return Twice(n-1) + Twice(n-1)     x ← Once(n - 1)
                                       return x + x
```

Both return $2^{n-1}$. Find the number of additions for each and compare them for $n = 30$.

:::::{dropdown} Hint
`Twice` makes two identical recursive calls — like the Tower of Hanoi. `Once` makes one.
::::{dropdown} Answer
Twice: $A(n) = 2A(n-1) + 1$, $A(1) = 0$, so $A(n) = 2^{n-1} - 1$. Once: $A(n) = A(n-1) + 1$, $A(1) = 0$, so
$A(n) = n - 1$. For $n = 30$: $536\,870\,911$ vs. $29$.
:::{dropdown} Full solution
**Twice.** $A(n) = 2A(n-1) + 1$ for $n > 1$, $A(1) = 0$. As for Hanoi,
$A(n) = 2^i A(n-i) + 2^i - 1$; with $i = n - 1$:

$$
A(n) = 2^{n-1} \cdot 0 + 2^{n-1} - 1 = 2^{n-1} - 1 \in \Theta(2^n).
$$

**Once.** $A(n) = A(n-1) + 1$, $A(1) = 0$, so $A(n) = n - 1 \in \Theta(n)$.

For $n = 30$: $2^{29} - 1 = 536\,870\,911$ additions versus $29$.

**Lesson.** Computing the same recursive call twice instead of storing its result turns a linear algorithm
into an exponential one — the same effect as in naive Fibonacci.
:::
::::
:::::

---

## Level C (advanced)

(m2-c1)=
### C1 · Prove by induction

```text
ALGORITHM Grow(n)
    if n = 0
        op
    else
        Grow(n - 1)
        for i ← 1 to 2^n do
            op
```

(a) Set up a recurrence for the number of executions of `op`. (b) Solve it by backward substitutions.
(c) Prove your answer by mathematical induction.

:::::{dropdown} Hint
(a) $T(n) = T(n-1) + 2^n$, $T(0) = 1$. (b) Unrolling gives $T(0) + 2^1 + 2^2 + \dots + 2^n$. (c) Base $n = 0$;
in the inductive step use the recurrence and the hypothesis for $n - 1$.
::::{dropdown} Answer
$T(n) = 2^{n+1} - 1 \in \Theta(2^n)$.
:::{dropdown} Full solution
**(a)** For $n = 0$, `op` runs once: $T(0) = 1$. For $n > 0$: the call on $n - 1$ plus the loop with $2^n$
iterations:

$$
T(n) = T(n-1) + 2^n \quad (n > 0), \qquad T(0) = 1 .
$$

**(b)**

$$
\begin{aligned}
T(n) &= T(n-1) + 2^n = T(n-2) + 2^{n-1} + 2^n \\
     &= \dots = T(n-i) + \sum_{j=n-i+1}^{n} 2^j .
\end{aligned}
$$

With $i = n$: $T(n) = 1 + \sum_{j=1}^{n} 2^j = \sum_{j=0}^{n} 2^j = 2^{n+1} - 1$ (formula S3).

**(c) Proof by induction** that $T(n) = 2^{n+1} - 1$ for all $n \ge 0$.

- *Base case* $n = 0$: $T(0) = 1$ and $2^{1} - 1 = 1$. ✔
- *Inductive step.* Let $n \ge 1$ and assume $T(n-1) = 2^{n} - 1$ (inductive hypothesis). Then by the
  recurrence
  $$T(n) = T(n-1) + 2^n = (2^n - 1) + 2^n = 2^{n+1} - 1 . \quad \checkmark$$

By induction the formula holds for all $n \ge 0$. Note that the last loop alone runs $2^n$ times, about
half of the total — typical for geometric growth.
:::
::::
:::::

(m2-c2)=
### C2 · Binomial coefficients by recursion

The binomial coefficients satisfy $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ for $0 < k < n$, with
$\binom{n}{0} = \binom{n}{n} = 1$.

```text
ALGORITHM Binom(n, k)
    //0 ≤ k ≤ n
    if k = 0 or k = n return 1
    else return Binom(n - 1, k - 1) + Binom(n - 1, k)
```

Let $A(n, k)$ be the number of additions. (a) Write the recurrence. (b) Prove by induction on $n$ that
$A(n, k) = \binom{n}{k} - 1$. (c) Estimate $A(30, 15)$ and suggest a better algorithm.

:::::{dropdown} Hint
(b) The structure is the same as for Fibonacci: try $B(n, k) = A(n, k) + 1$. In the inductive step assume
the formula for all pairs with first argument $n - 1$.
::::{dropdown} Answer
(a) $A(n,k) = A(n-1,k-1) + A(n-1,k) + 1$ for $0 < k < n$; $A(n,0) = A(n,n) = 0$.
(b) $A(n,k) = \binom{n}{k} - 1$. (c) $A(30,15) = 155\,117\,519$: exponential. Use a table (Pascal's triangle)
— $\Theta(nk)$ additions.
:::{dropdown} Full solution
**(a)** Two recursive calls plus one addition; the stopping cases add nothing:

$$
\begin{aligned}
A(n,k) &= A(n-1,k-1) + A(n-1,k) + 1 \quad (0 < k < n), \\
A(n,0) &= A(n,n) = 0 .
\end{aligned}
$$

**(b)** Claim: $A(n,k) = \binom{n}{k} - 1$ for all $0 \le k \le n$. Induction on $n$.

- *Base case* $n = 0$: only $k = 0$; $A(0,0) = 0 = \binom00 - 1$. ✔
- *Inductive step.* Assume the claim for all pairs $(n-1, j)$ with $0 \le j \le n-1$. Take $0 \le k \le n$.
  - If $k = 0$ or $k = n$: $A(n,k) = 0 = 1 - 1 = \binom{n}{k} - 1$. ✔
  - If $0 < k < n$: by the recurrence and the hypothesis,
    $$\begin{aligned} A(n,k) &= \left(\tbinom{n-1}{k-1} - 1\right) + \left(\tbinom{n-1}{k} - 1\right) + 1 \\ &= \tbinom{n-1}{k-1} + \tbinom{n-1}{k} - 1 = \tbinom{n}{k} - 1 . \quad \checkmark \end{aligned}$$

**(c)** $A(30, 15) = \binom{30}{15} - 1 = 155\,117\,519$ additions. The central coefficient $\binom{n}{n/2}$ grows
exponentially (roughly like $2^n / \sqrt{n}$), so the recursion is exponential for $k \approx n/2$. The
reason is again **overlapping subproblems**: e.g. $\binom{n-2}{k-1}$ is computed by both recursive calls.
Filling Pascal's triangle row by row (or memoizing) computes every $\binom{i}{j}$ once: $\Theta(nk)$
additions.
:::
::::
:::::

---

## Find the mistake

(m2-m1)=
### M1 · Is the string a palindrome?

```text
ALGORITHM IsPal(S[l..r])
    //Checks whether the string S[l..r] reads the same in both directions
    if l ≥ r return true
    if S[l] ≠ S[r] return false
    return IsPal(S[l+1..r-1])
```

> **Student's solution.** Size: $n = r - l + 1$. Basic operation: the character comparison `S[l] ≠ S[r]`.
> Worst case: the string is a palindrome, so the recursion goes all the way down. Each call compares once
> and recurses on $n - 2$ characters: $C(n) = C(n-2) + 1$. When $l \ge r$ the string has 0 or 1 characters,
> so $C(0) = C(1) = 1$. Solving: $C(n) = \lfloor n/2 \rfloor + 1$.

:::::{dropdown} Hint
Look at the line `if l ≥ r return true`. Does it compare any characters?
::::{dropdown} Answer
The **initial condition is wrong** — it is not consistent with the stopping case. The stopping case compares no
characters, so $C(0) = C(1) = 0$, and $C_{worst}(n) = \lfloor n/2 \rfloor$.
:::{dropdown} Full solution
**Diagnosis.** The input size, the basic operation, the worst case and the recurrence $C(n) = C(n-2) + 1$
are correct. But the stopping case `if l ≥ r return true` makes **no** character comparison (it compares
indices, which is not the basic operation). The initial condition must be $C(0) = C(1) = 0$.

**Correct solution.** $C(n) = C(n-2) + 1$ for $n \ge 2$, $C(0) = C(1) = 0$. After $i$ steps,
$C(n) = C(n - 2i) + i$.

- $n$ even: $i = n/2$ gives $C(n) = C(0) + n/2 = n/2$.
- $n$ odd: $i = (n-1)/2$ gives $C(n) = C(1) + (n-1)/2 = (n-1)/2$.

So $C_{worst}(n) = \lfloor n/2 \rfloor \in \Theta(n)$. Check: "abba" compares (a, a) and (b, b) — 2
comparisons, not 3. The best case is $1$ comparison (first and last characters differ), for $n \ge 2$.

The wrong initial condition changes the answer by exactly 1 for every $n$; an experiment with a counter
would catch it immediately.
:::
::::
:::::

(m2-m2)=
### M2 · Counting occurrences by halves

```text
ALGORITHM CountK(A[l..r], K)
    //Number of elements equal to K in A[l..r]
    if l = r
        if A[l] = K return 1 else return 0
    m ← ⌊(l + r)/2⌋
    return CountK(A[l..m], K) + CountK(A[m+1..r], K)
```

> **Student's solution.** Size $n$, assume $n = 2^k$. Basic operation: the addition in the last line.
> Both halves have the same size $n/2$, so the recursive call costs $A(n/2)$, plus one addition:
> $A(n) = A(n/2) + 1$, $A(1) = 0$. Like BinRec, $A(n) = \log_2 n$. Counting by halves is therefore
> exponentially faster than a linear scan.

:::::{dropdown} Hint
How many recursive calls does one call of CountK make? Compare with binary search, which also halves the
array.
::::{dropdown} Answer
The mistake is **counting two recursive calls as one** term. Correct: $A(n) = 2A(n/2) + 1$, $A(1) = 0$, so
$A(n) = n - 1 \in \Theta(n)$ — no faster than a linear scan.
:::{dropdown} Full solution
**Diagnosis.** CountK calls itself **twice** — on the left half **and** on the right half. Each call does its
own work, so the recurrence needs **one term per call**: $A(n/2) + A(n/2) = 2A(n/2)$. Binary search makes
only **one** of its two possible calls, which is why it is logarithmic.

**Correct solution.**

$$
A(n) = 2A(n/2) + 1 \quad (n > 1), \qquad A(1) = 0 .
$$

As in [B3](#m2-b3): $A(2^k) = 2^i A(2^{k-i}) + 2^i - 1$; with $i = k$, $A(n) = n - 1 \in \Theta(n)$.

This is to be expected: every element has to be looked at (the $n$ comparisons `A[l] = K` happen in the
leaves), so no correct counting algorithm can be sublinear.
:::
::::
:::::

---

## Empirical task

(m2-e1)=
### E1 · Counting calls in naive and memoized Fibonacci

1. Let $Calls(n)$ be the total number of calls of the naive algorithm [F(n)](04_fibonacci_warning.md). Show
   that $Calls(n) = Calls(n-1) + Calls(n-2) + 1$ with $Calls(0) = Calls(1) = 1$, and that
   $Calls(n) = 2F(n+1) - 1$.
2. Write Python code with a call counter for the naive and for the memoized version (the memo check
   happens at the beginning of each call). Print a table $n$ | naive calls | $2F(n+1) - 1$ | memo calls for
   $n = 1, \dots, 25$.
3. Plot both call counts (logarithmic $y$-axis) and state a conclusion. Guess a formula for the memoized
   calls and explain it.

:::::{dropdown} Hint
(1) Let $D(n) = Calls(n) + 1$ and check that $D$ satisfies the Fibonacci recurrence. (3) In the memoized
version, the first call $F(n-1)$ computes everything; the second call $F(n-2)$ immediately finds its value
in the table.
::::{dropdown} Answer
Naive: $Calls(n) = 2F(n+1) - 1$ (e.g. $21\,891$ calls for $n = 20$). Memoized: $2n - 1$ calls for $n \ge 1$.
The experiment confirms both formulas: exponential vs. linear growth.
:::{dropdown} Full solution
**1.** A call with $n > 1$ makes itself (1 call) plus all calls of $F(n-1)$ and $F(n-2)$; a call with
$n \le 1$ is a single call. With $D(n) = Calls(n) + 1$:
$D(n) = Calls(n-1) + Calls(n-2) + 2 = D(n-1) + D(n-2)$, $D(0) = D(1) = 2$. Since $2F(n+1)$ satisfies the same
recurrence with the same initial values ($2F(1) = 2F(2) = 2$), $D(n) = 2F(n+1)$ and
$Calls(n) = 2F(n+1) - 1$.

**2. Code.**

```python
import matplotlib.pyplot as plt

def naive_calls(n):
    calls = 0
    def f(m):
        nonlocal calls
        calls += 1
        return m if m <= 1 else f(m - 1) + f(m - 2)
    f(n)
    return calls

def memo_calls(n):
    calls, memo = 0, {}
    def f(m):
        nonlocal calls
        calls += 1
        if m in memo:
            return memo[m]
        memo[m] = m if m <= 1 else f(m - 1) + f(m - 2)
        return memo[m]
    f(n)
    return calls

F = [0, 1]
while len(F) < 30:
    F.append(F[-1] + F[-2])

ns = range(1, 26)
print(f"{'n':>3} | {'naive':>7} | {'2F(n+1)-1':>9} | {'memo':>4}")
for n in ns:
    print(f"{n:>3} | {naive_calls(n):>7} | {2*F[n+1]-1:>9} | {memo_calls(n):>4}")

plt.semilogy(ns, [naive_calls(n) for n in ns], "o-", label="naive")
plt.semilogy(ns, [memo_calls(n) for n in ns], "s-", label="memoized")
plt.xlabel("n"); plt.ylabel("calls (log scale)"); plt.legend(); plt.show()
```

**3. Result and conclusion.** The naive column equals $2F(n+1) - 1$ in every row ($n = 10$: $177$;
$n = 20$: $21\,891$; $n = 25$: $242\,785$). On the log scale the naive curve is a straight rising line —
exponential growth, $\Theta(\varphi^n)$. The memoized column is $1, 3, 5, 7, \dots$, i.e. $2n - 1$: for each
$k = n, n-1, \dots, 2$ there is one "real" call $F(k)$ and one second call $F(k-2)$ (a memo hit, except
for $F(0)$, which is a stopping case), plus the call $F(1)$ at the bottom of the chain:
$2(n-1) + 1 = 2n - 1$. The experiment confirms the theory: memoization turns exponential time into
linear time.
:::
::::
:::::
