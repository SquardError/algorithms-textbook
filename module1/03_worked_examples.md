---
short_title: 3 · Worked examples
kernelspec:
  name: python3
  display_name: Python 3
---

# Worked Examples

Every example uses the **same five steps**:
**input size → basic operation → cases → sum → solution.**
Examples 1–5 are the classic examples from Lecture 4, explained in more detail. Examples 6–8 are
**original examples** that do not appear in the lecture.

| # | Algorithm | Loop pattern | Result |
|---|---|---|---|
| 1 | [MaxElement](#ex-max) | one loop | $n-1 \in \Theta(n)$ |
| 2 | [UniqueElements](#ex-unique) | nested, early exit | worst $\frac{n(n-1)}{2}$, best $1$ |
| 3 | [Matrix multiplication](#ex-matrix) | three nested loops | $n^3$ |
| 4 | [Dependent bound](#ex-dependent) | inner bound $= i$ | $\frac{n(n+1)}{2}$ |
| 5 | [Doubling loop](#ex-log) | `i ← 2i` | $\lfloor \log_2 n \rfloor + 1$ |
| 6 | [Selection sort](#ex-selection) *(original)* | nested, dependent | $\frac{n(n-1)}{2}$ comparisons |
| 7 | [Search in an $m \times n$ matrix](#ex-matrix-search) *(original)* | two parameters | worst $mn$, best $1$ |
| 8 | [Linear loop around a tripling loop](#ex-tripling) *(original)* | `j ← 3j` inside | $n(\lfloor \log_3 n \rfloor + 1)$ |

---

(ex-max)=
## Example 1 · MaxElement

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM MaxElement(A[0..n-1])
    //Determines the value of the largest element in a given array
    //Input: An array A[0..n-1] of real numbers
    //Output: The value of the largest element in A
    maxval ← A[0]
    for i ← 1 to n - 1 do
        if A[i] > maxval
            maxval ← A[i]
    return maxval
```
:::
:::{tab-item} Python
```python
def max_element(A):
    maxval = A[0]
    for i in range(1, len(A)):
        if A[i] > maxval:
            maxval = A[i]
    return maxval
```
:::
::::

**Step 1 · Input size.** $n$, the number of elements.

**Step 2 · Basic operation.** The loop contains two candidates: the comparison `A[i] > maxval` and the
assignment `maxval ← A[i]`. The comparison runs on **every** iteration; the assignment only when a new
maximum appears. So the basic operation is the **comparison**.

**Step 3 · Cases.** There is no early exit: the loop always runs from $1$ to $n-1$. The number of
comparisons depends only on $n$.

**Step 4 · Sum.**

$$
C(n) = \sum_{i=1}^{n-1} 1 .
$$

**Step 5 · Solution.** By the term-counting rule, $C(n) = (n-1) - 1 + 1 = n - 1 \in \Theta(n)$.

:::{note} Why not count assignments?
The number of assignments depends on the data: $0$ if $A[0]$ is the maximum, $n-1$ if the array is
strictly increasing. Choosing them would force a three-case analysis and still miss the work done by
the comparisons. **Choose the operation that runs every time.**
:::

---

(ex-unique)=
## Example 2 · UniqueElements

Problem: check whether all the elements of an array are distinct.

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM UniqueElements(A[0..n-1])
    //Determines whether all the elements in a given array are distinct
    //Input: An array A[0..n-1]
    //Output: Returns "true" if all the elements in A are distinct
    //        and "false" otherwise
    for i ← 0 to n - 2 do
        for j ← i + 1 to n - 1 do
            if A[i] = A[j] return false
    return true
```
:::
:::{tab-item} Python
```python
def unique_elements(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True
```
:::
::::

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The comparison `A[i] = A[j]` in the innermost loop.

**Step 3 · Cases.** There **is** an early exit (`return false`). The count depends on the input:

- **Best case:** $A[0] = A[1]$. The very first comparison finds equal elements: $C_{best}(n) = 1$.
- **Worst case:** no early exit at all. This happens when all elements are distinct, or when the only
  equal pair is the last two elements $A[n-2] = A[n-1]$.

We analyze the worst case.

**Step 4 · Sum.** In the worst case both loops run completely:

$$
C_{worst}(n) = \sum_{i=0}^{n-2} \; \sum_{j=i+1}^{n-1} 1 .
$$

**Step 5 · Solution.** Inside out. The inner sum has $(n-1) - (i+1) + 1 = n - 1 - i$ terms:

$$
\begin{aligned}
C_{worst}(n) &= \sum_{i=0}^{n-2} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 \\
             &= \frac{(n-1)n}{2} \in \Theta(n^2).
\end{aligned}
$$

:::{tip} A quicker way to see it
The algorithm compares every **pair** of positions $\{i, j\}$ at most once. The number of pairs of $n$
elements is $\binom{n}{2} = \frac{n(n-1)}{2}$. In the worst case all pairs are compared.
:::

:::{important} State the case!
"UniqueElements is $\Theta(n^2)$" is **wrong** as a statement about all inputs, because the best case is
$\Theta(1)$. Correct: *the worst case is $\Theta(n^2)$, the best case is $\Theta(1)$, the algorithm is
in $O(n^2)$.*
:::

---

(ex-matrix)=
## Example 3 · Matrix multiplication

Multiply two $n \times n$ matrices by the definition $C[i,j] = \sum_k A[i,k]\,B[k,j]$.

```text
ALGORITHM MatrixMultiplication(A[0..n-1, 0..n-1], B[0..n-1, 0..n-1])
    //Multiplies two square matrices of order n by the definition-based algorithm
    //Output: Matrix C = AB
    for i ← 0 to n - 1 do
        for j ← 0 to n - 1 do
            C[i, j] ← 0.0
            for k ← 0 to n - 1 do
                C[i, j] ← C[i, j] + A[i, k] * B[k, j]
    return C
```

**Step 1 · Input size.** The order $n$ of the matrices. (There are $2n^2$ input numbers; we state
explicitly that we measure in $n$.)

**Step 2 · Basic operation.** The innermost loop has one multiplication and one addition; they run the
same number of times. By custom we count **multiplications**.

**Step 3 · Cases.** No early exit: the count depends only on $n$.

**Step 4 · Sum.**

$$
M(n) = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} \sum_{k=0}^{n-1} 1 .
$$

**Step 5 · Solution.** Inside out: the $k$-sum is $n$; then $\sum_{j=0}^{n-1} n = n^2$; then
$\sum_{i=0}^{n-1} n^2 = n^3$. So $M(n) = n^3 \in \Theta(n^3)$.

If a multiplication takes time $c_m$ and an addition $c_a$, the running time is about
$(c_m + c_a)\,n^3$: the constant changes with the hardware, the order of growth does not.

:::{note} Size matters
In terms of the number of input elements $N = 2n^2$, we have $n = \sqrt{N/2}$, so the algorithm is
$\Theta(N^{1.5})$. Both statements are true; just never mix the two size measures.
:::

---

(ex-dependent)=
## Example 4 · A loop with a dependent bound

The inner loop's upper bound is the **outer index** $i$. This pattern appears in many sorting algorithms.

```text
count ← 0
for i ← 1 to n do
    for j ← 1 to i do
        count ← count + 1
```

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The increment `count ← count + 1`.

**Step 3 · Cases.** No early exit; the count depends only on $n$.

**Step 4 · Sum.**

$$
C(n) = \sum_{i=1}^{n} \sum_{j=1}^{i} 1 .
$$

**Step 5 · Solution.** The inner sum is $i$ (it counts $1, \dots, i$). Then by S1

$$
C(n) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \in \Theta(n^2).
$$

The picture shows why: row $i$ has $i$ iterations, so the iterations fill a **triangle**, about half of
an $n \times n$ square.

```{code-cell} python
:tags: [remove-input]
import matplotlib.pyplot as plt
import matplotlib.patches as patches

n = 8
fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
for ax, title, cond in [(axes[0], r"for j ← 1 to i:  $\frac{n(n+1)}{2}$ = 36 cells", lambda i, j: j <= i),
                        (axes[1], r"for j ← i+1 to n:  $\frac{n(n-1)}{2}$ = 28 cells", lambda i, j: j > i)]:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            on = cond(i, j)
            ax.add_patch(patches.Rectangle((j - 1, n - i), 1, 1, facecolor="#4c9be8" if on else "#f0f0f0",
                                           edgecolor="white", linewidth=1.5))
    ax.set_xlim(0, n); ax.set_ylim(0, n); ax.set_aspect("equal")
    ax.set_xticks([k + 0.5 for k in range(n)]); ax.set_xticklabels(range(1, n + 1))
    ax.set_yticks([k + 0.5 for k in range(n)]); ax.set_yticklabels(range(n, 0, -1))
    ax.set_xlabel("inner index j"); ax.set_ylabel("outer index i")
    ax.set_title(title, fontsize=10)
plt.suptitle("Each blue cell is one execution of the basic operation (n = 8)")
plt.tight_layout(); plt.show()
```

With the inner loop `for j ← i + 1 to n` instead, the count is $\sum_{i=1}^{n}(n - i) = \frac{n(n-1)}{2}$.
Both counts have the same leading term $\frac{n^2}{2}$ — this is why many different-looking quadratic
algorithms run in practically the same time.

---

(ex-log)=
## Example 5 · A multiplicative loop (logarithm)

Not every loop adds 1 to its counter.

```text
i ← 1
while i ≤ n do
    //basic operation
    i ← 2 * i
```

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The operation in the loop body (one per iteration).

**Step 3 · Cases.** No early exit; depends only on $n$.

**Step 4 · Counting.** Here a plain sum $\sum 1$ needs to know **how many** iterations there are. Track
the counter: before iteration $t = 1, 2, 3, \dots$ the value of $i$ is

| iteration $t$ | 1 | 2 | 3 | 4 | … | $t$ |
|---|---|---|---|---|---|---|
| $i$ | $1$ | $2$ | $4$ | $8$ | … | $2^{t-1}$ |

The iteration happens while $2^{t-1} \le n$, i.e. while $t - 1 \le \log_2 n$.

**Step 5 · Solution.** The largest such $t$ is $\lfloor \log_2 n \rfloor + 1$, so

$$
C(n) = \lfloor \log_2 n \rfloor + 1 \in \Theta(\log n).
$$

Check with $n = 10$: $i = 1, 2, 4, 8$ pass the test, $i = 16$ does not — 4 iterations, and
$\lfloor \log_2 10 \rfloor + 1 = 3 + 1 = 4$. ✔

The same holds for a **halving** loop (`i ← n; while i ≥ 1: i ← ⌊i/2⌋`), as in binary search: it also
runs $\lfloor \log_2 n \rfloor + 1$ times. The base of the logarithm does not affect $\Theta$: tripling
gives $\Theta(\log_3 n) = \Theta(\log n)$.

:::{warning} Do not guess from the shape of the code
A loop `for i ← 1 to n` with an inner loop that **doubles** gives $\Theta(n \log n)$, but an inner loop
`for j ← 1 to i*i` gives $\Theta(n^3)$. Always write the sum and look at its upper limit before computing.
:::

---

(ex-selection)=
## Example 6 · Selection sort *(original example)*

Selection sort finds the smallest element and swaps it to position 0, then the smallest of the rest to
position 1, and so on.

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM SelectionSort(A[0..n-1])
    //Sorts a given array by selection sort
    //Input: An array A[0..n-1] of orderable elements
    //Output: Array A[0..n-1] sorted in nondecreasing order
    for i ← 0 to n - 2 do
        min ← i
        for j ← i + 1 to n - 1 do
            if A[j] < A[min]  min ← j
        swap A[i] and A[min]
```
:::
:::{tab-item} Python
```python
def selection_sort(A):
    n = len(A)
    for i in range(0, n - 1):
        m = i
        for j in range(i + 1, n):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]
    return A
```
:::
::::

**Step 1 · Input size.** $n$, the number of elements.

**Step 2 · Basic operation.** The key comparison `A[j] < A[min]` (innermost loop).

**Step 3 · Cases.** There is no early exit: both loops always run to the end, whatever the order of the
elements. Even an already sorted array gets the full treatment. So the count depends **only on $n$**.

**Step 4 · Sum.** The bounds are exactly the bounds of UniqueElements:

$$
C(n) = \sum_{i=0}^{n-2} \sum_{j=i+1}^{n-1} 1 .
$$

**Step 5 · Solution.** As in Example 2,

$$
C(n) = \sum_{i=0}^{n-2} (n-1-i) = \frac{n(n-1)}{2} \in \Theta(n^2) \quad \text{for every input.}
$$

The number of **swaps** is one per outer iteration: $\sum_{i=0}^{n-2} 1 = n - 1 \in \Theta(n)$.

:::{note} Same sum, different meaning
UniqueElements and SelectionSort have the same sum, but for UniqueElements it is only the **worst**
case, while for SelectionSort it holds for **all** inputs. Step 3 is what tells them apart.
:::

---

(ex-matrix-search)=
## Example 7 · Searching in an $m \times n$ matrix *(original example)*

```text
ALGORITHM MatrixSearch(M[0..m-1, 0..n-1], K)
    //Searches for K in an m-by-n matrix, row by row
    //Output: true if K occurs in M, false otherwise
    for i ← 0 to m - 1 do
        for j ← 0 to n - 1 do
            if M[i, j] = K return true
    return false
```

**Step 1 · Input size.** The matrix is not square, so we need **two parameters**: $m$ rows and $n$
columns. (Using a single "$n$" would lose information.)

**Step 2 · Basic operation.** The comparison `M[i, j] = K`.

**Step 3 · Cases.** There is an early exit.

- **Best case:** $K = M[0,0]$, found at the first comparison: $C_{best}(m, n) = 1$.
- **Worst case:** $K$ is absent or only in the last cell $M[m-1, n-1]$: every cell is compared.

**Step 4 · Sum (worst case).**

$$
C_{worst}(m, n) = \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} 1 .
$$

**Step 5 · Solution.** The inner sum is $n$, the outer sum adds $n$ exactly $m$ times:

$$
C_{worst}(m, n) = \sum_{i=0}^{m-1} n = mn \in \Theta(mn).
$$

For a square matrix ($m = n$) this is $n^2$. Note that $mn$ is exactly the number of input elements, so
the search is **linear in the size of the input** — as it should be, since every cell may have to be
inspected.

---

(ex-tripling)=
## Example 8 · A linear loop around a tripling loop *(original example)*

```text
ALGORITHM LinearTimesLog(n)
    for i ← 1 to n do
        j ← 1
        while j ≤ n do
            //basic operation
            j ← 3 * j
```

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The operation in the body of the `while` loop.

**Step 3 · Cases.** No early exit; the count depends only on $n$.

**Step 4 · Sum.** The inner loop does not depend on $i$. Like the doubling loop of Example 5, it runs
while $3^{t-1} \le n$, i.e. $\lfloor \log_3 n \rfloor + 1$ times. So

$$
C(n) = \sum_{i=1}^{n} \left( \lfloor \log_3 n \rfloor + 1 \right).
$$

**Step 5 · Solution.** The summand does not depend on $i$, so by rule R1 it comes out of the sum:

$$
C(n) = n \left( \lfloor \log_3 n \rfloor + 1 \right) \in \Theta(n \log n).
$$

Check with $n = 10$: inside, $j = 1, 3, 9$ pass and $27$ fails — 3 iterations, and
$\lfloor \log_3 10 \rfloor + 1 = 2 + 1 = 3$. Total $C(10) = 10 \cdot 3 = 30$. For $n = 27$:
$j = 1, 3, 9, 27$ — 4 iterations, $C(27) = 27 \cdot 4 = 108$.

:::{note} Log base again
$\Theta(n \log_3 n)$ and $\Theta(n \log_2 n)$ are the same class, because
$\log_3 n = \log_2 n / \log_2 3$. The pattern "linear loop × multiplicative loop" appears in efficient
sorting algorithms that you will meet later in the course.
:::

---

All formulas on this page were checked by counting operations for $n = 1, \dots, 20$ (and up to
$n = 1024$ for the logarithmic loops) in
[`code/verify/verify_m1_theory.py`](https://github.com/SquardError/algorithms-textbook/blob/main/code/verify/verify_m1_theory.py).

Next: what to do when the count depends on the input in a random way — the
[Average case](04_average_case.md).
