---
short_title: 5 · Typical mistakes
---

# Typical Mistakes

Most wrong answers in algorithm analysis come from one of six mistakes. Learn to recognize them — the
"Find the mistake" problems in this book each contain exactly one of them.

| # | Mistake | Which step of the plan |
|---|---|---|
| 1 | [Wrong basic operation](#mistake-basic-op) | Step 2 |
| 2 | [Size vs. value](#mistake-size-value) | Step 1 |
| 3 | [Mixing up cases](#mistake-cases) | Steps 3 and 5 |
| 4 | [Off-by-one in sums](#mistake-off-by-one) | Steps 4 and 5 |
| 5 | [Ignoring early exit](#mistake-early-exit) | Step 3 |
| 6 | [Hidden cost](#mistake-hidden-cost) | Step 2 |

(mistake-basic-op)=
## 1 · Wrong basic operation

:::{warning} The mistake
Counting an operation that is **not** executed most often, for example an assignment that runs only
when a condition is true, or an operation outside the innermost loop.
:::

```text
ALGORITHM CountPositive(A[0..n-1])
    count ← 0
    for i ← 0 to n - 1 do
        if A[i] > 0
            count ← count + 1
    return count
```

*Wrong:* "The basic operation is `count ← count + 1`. For an array without positive numbers it never
runs, so the algorithm takes $\Theta(1)$ time."

*Right:* The comparison `A[i] > 0` runs on **every** iteration, $n$ times. That is the basic operation:
$C(n) = n \in \Theta(n)$ for every input.

**How to avoid it:** look at the innermost loop and ask "does anything here run more often than my
choice?"

(mistake-size-value)=
## 2 · Confusing input size with the value of the input

:::{warning} The mistake
Taking the **value** of a number as the input size, when the input is a single number.
:::

```text
ALGORITHM IsPrime(n)
    //n ≥ 2
    for d ← 2 to n - 1 do
        if n mod d = 0 return false
    return true
```

*Wrong:* "At most $n - 2$ divisions, so the algorithm is linear, i.e. efficient."

*Right:* A number $n$ is written with $b = \lfloor \log_2 n \rfloor + 1$ bits, so $n \ge 2^{b-1}$. In the
worst case ($n$ prime) the loop makes $n - 2 \ge 2^{b-1} - 2$ divisions, which is $\Theta(2^b)$:
**exponential in the input size $b$**. For a 30-bit prime that is more than half a billion divisions
($2^{29} \approx 5.4 \cdot 10^8$).

**How to avoid it:** if the input is one number, write the answer both in terms of the value $n$ and in
terms of the number of bits $b$, and say which is which.

(mistake-cases)=
## 3 · Mixing up the cases

:::{warning} The mistake
Stating one $\Theta$ class for an algorithm whose best and worst cases grow differently.
:::

*Wrong:* "UniqueElements runs in $\Theta(n^2)$ time."

*Right:* "The **worst-case** count is $\Theta(n^2)$; the **best-case** count is $\Theta(1)$. Hence the
algorithm is in $O(n^2)$." Remember: $O$ is an **upper** bound and is true for all inputs; $\Theta$
must be attached to a specific case.

**How to avoid it:** whenever Step 3 found that the count depends on the input, write a subscript:
$C_{worst}$, $C_{best}$, $C_{avg}$.

(mistake-off-by-one)=
## 4 · Off-by-one errors in sums

:::{warning} The mistake
Getting the number of terms wrong: writing $n$ instead of $n-1$, or $u - l$ instead of $u - l + 1$.
:::

```text
for i ← 1 to n - 1 do
    //basic operation
```

*Wrong:* "$\sum_{i=1}^{n-1} 1 = n$." *Right:* $(n-1) - 1 + 1 = n - 1$.

Off-by-one errors do **not** change the order of growth, but they **do** change the exact formula — and an
experiment with an operation counter will immediately show the difference (see
[Empirical verification](06_empirical_verification.md)).

**How to avoid it:** use $u - l + 1$ every time, and test the formula on a small $n$ by hand
(for $n = 3$ the loop above runs for $i = 1, 2$: 2 times, not 3).

(mistake-early-exit)=
## 5 · Ignoring early termination

:::{warning} The mistake
Writing the sum for "all iterations" when the loop contains `return` or `break`, and presenting it as
the count for every input.
:::

```text
ALGORITHM HasNegative(A[0..n-1])
    for i ← 0 to n - 1 do
        if A[i] < 0 return true
    return false
```

*Wrong:* "$C(n) = \sum_{i=0}^{n-1} 1 = n$ for every input."

*Right:* If $A[0] < 0$ the algorithm stops after 1 comparison. $C_{best}(n) = 1$,
$C_{worst}(n) = n$ (no negative numbers, or only the last one).

**How to avoid it:** at Step 3, scan the code for `return`, `break` and data-dependent `while`
conditions.

(mistake-hidden-cost)=
## 6 · Forgetting hidden costs

:::{warning} The mistake
Treating a line of pseudocode as one operation when it actually hides a loop: a library call, a string
comparison, a list slice, arithmetic on huge numbers.
:::

```text
ALGORITHM CountWord(W[0..n-1], s)
    //W is an array of n strings, each of length m; s is a string of length m
    count ← 0
    for i ← 0 to n - 1 do
        if W[i] = s  count ← count + 1
    return count
```

*Wrong:* "$n$ comparisons, so $\Theta(n)$."

*Right:* Comparing two strings of length $m$ compares up to $m$ **characters**. If we count character
comparisons, the worst case is $nm \in \Theta(nm)$. It is fine to count string comparisons, but then
you must say so, and remember that each one is not constant time.

Similar hidden costs in Python: `x in list` (a loop), `A[i:j]` (copies $j - i$ elements), `sorted(A)`,
`max(A)`, `A.index(x)`.

**How to avoid it:** for every line in the loop, ask "is this really a constant amount of work?"

---

You will meet each of these mistakes again in the "Find the mistake" problems in
[Module 1 problems](08_problems.md) and [Module 2 problems](../module2/07_problems.md).

Next: [Empirical verification](06_empirical_verification.md).
