---
short_title: 3 · Worked examples
kernelspec:
  name: python3
  display_name: Python 3
---

# Worked Examples

Every example follows the same five steps: **input size → basic operation → cases → recurrence →
solution**. Examples 1–3 are the classic examples of Lecture 5; examples 4–6 are **original examples**.

| # | Algorithm | Recurrence | Solution |
|---|---|---|---|
| 1 | [Factorial](#ex2-factorial) | $M(n) = M(n-1) + 1$, $M(0) = 0$ | $n$ |
| 2 | [Tower of Hanoi](#ex2-hanoi) | $M(n) = 2M(n-1) + 1$, $M(1) = 1$ | $2^n - 1$ |
| 3 | [Binary digits (BinRec)](#ex2-binrec) | $A(n) = A(\lfloor n/2 \rfloor) + 1$, $A(1) = 0$ | $\lfloor \log_2 n \rfloor$ |
| 4 | [Recursive array sum](#ex2-sum) *(original)* | $S(n) = S(n-1) + 1$, $S(1) = 0$ | $n - 1$ |
| 5 | [Fast exponentiation](#ex2-power) *(original)* | $M(n) = M(n/2) + 1$, $M(1) = 0$ ($n = 2^k$) | $\log_2 n$ |
| 6 | [Recursive binary search](#ex2-bsearch) *(original)* | $C(n) = C(\lfloor n/2 \rfloor) + 1$, $C(0) = 0$ | $\lfloor \log_2 n \rfloor + 1$ |

---

(ex2-factorial)=
## Example 1 · Factorial

$n! = 1 \cdot 2 \cdot \ldots \cdot n$ for $n \ge 1$ and $0! = 1$, so $n! = (n-1)! \cdot n$.

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM F(n)
    //Computes n! recursively
    //Input: A nonnegative integer n
    //Output: The value of n!
    if n = 0 return 1
    else return F(n - 1) * n
```
:::
:::{tab-item} Python
```python
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
```
:::
::::

**Step 1 · Input size.** The number $n$ itself. (Here we measure in the value of $n$, as Levitin does
for this example.)

**Step 2 · Basic operation.** The multiplication.

**Step 3 · Cases.** The count depends only on $n$.

**Step 4 · Recurrence.** Computing $F(n)$ takes $M(n-1)$ multiplications for $F(n-1)$ plus one more
multiplication by $n$:

$$
M(n) = M(n-1) + 1 \quad \text{for } n > 0, \qquad M(0) = 0,
$$

because $F(0)$ returns $1$ without multiplying.

**Step 5 · Solution.** Backward substitutions:

$$
\begin{aligned}
M(n) &= M(n-1) + 1 \\
     &= [M(n-2) + 1] + 1 = M(n-2) + 2 \\
     &= [M(n-3) + 1] + 2 = M(n-3) + 3 \\
     &\;\;\vdots \\
     &= M(n-i) + i .
\end{aligned}
$$

With $i = n$: $M(n) = M(0) + n = n \in \Theta(n)$.

**Verification.** $M(0) = 0$ ✔ and $M(n-1) + 1 = (n-1) + 1 = n$ ✔.

The iterative loop `for i ← 1 to n: p ← p * i` also makes $n$ multiplications. The recursive version is
not faster — and it uses $n+1$ stack frames of memory (see
[Recursion vs. iteration](05_recursion_vs_iteration.md)).

---

(ex2-hanoi)=
## Example 2 · Tower of Hanoi

$n$ disks of different sizes sit on peg 1, largest at the bottom. Move them all to peg 3, one disk at a
time, never putting a larger disk on a smaller one; peg 2 may be used as auxiliary.

**The recursive idea.** To move $n > 1$ disks from peg 1 to peg 3:

1. move the top $n-1$ disks from peg 1 to peg 2 (recursively, peg 3 auxiliary);
2. move the largest disk from peg 1 to peg 3;
3. move the $n-1$ disks from peg 2 to peg 3 (recursively, peg 1 auxiliary).

For $n = 1$, simply move the disk.

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM Hanoi(n, from, to, aux)
    //Moves n disks from peg "from" to peg "to" using peg "aux"
    if n = 1
        move disk from "from" to "to"
    else
        Hanoi(n - 1, from, aux, to)
        move disk from "from" to "to"
        Hanoi(n - 1, aux, to, from)
```
:::
:::{tab-item} Python
```python
def hanoi(n, src, dst, aux, moves):
    if n == 1:
        moves.append((src, dst))
    else:
        hanoi(n - 1, src, aux, dst, moves)
        moves.append((src, dst))
        hanoi(n - 1, aux, dst, src, moves)

moves = []
hanoi(3, 1, 3, 2, moves)
print(len(moves), moves)   # 7 moves
```
:::
::::

**Step 1 · Input size.** The number of disks $n$.

**Step 2 · Basic operation.** Moving one disk.

**Step 3 · Cases.** The number of moves depends only on $n$.

**Step 4 · Recurrence.** Two recursive calls on $n-1$ disks, plus one direct move:

$$
M(n) = 2M(n-1) + 1 \quad \text{for } n > 1, \qquad M(1) = 1 .
$$

**Step 5 · Solution.** Backward substitutions — keep the structure visible:

$$
\begin{aligned}
M(n) &= 2M(n-1) + 1 \\
     &= 2[2M(n-2) + 1] + 1 = 2^2 M(n-2) + 2 + 1 \\
     &= 2^2[2M(n-3) + 1] + 2 + 1 = 2^3 M(n-3) + 2^2 + 2 + 1 \\
     &\;\;\vdots \\
     &= 2^i M(n-i) + 2^{i-1} + 2^{i-2} + \dots + 2 + 1 = 2^i M(n-i) + 2^i - 1 ,
\end{aligned}
$$

using the geometric series $1 + 2 + \dots + 2^{i-1} = 2^i - 1$. The initial condition is at $n = 1$, so
take $n - i = 1$, i.e. $i = n - 1$:

$$
M(n) = 2^{n-1} M(1) + 2^{n-1} - 1 = 2^{n-1} + 2^{n-1} - 1 = 2^n - 1 \in \Theta(2^n).
$$

**Verification by induction.** Base $n = 1$: $2^1 - 1 = 1 = M(1)$ ✔. Step: if $M(n-1) = 2^{n-1} - 1$, then
$M(n) = 2(2^{n-1} - 1) + 1 = 2^n - 1$ ✔.

### The recursion tree

Draw every call as a node; a call on $n$ disks has two children, calls on $n-1$ disks. For $n = 3$:

```{mermaid}
flowchart TD
    A["H(3)<br/>1 move"] --> B["H(2)<br/>1 move"]
    A --> C["H(2)<br/>1 move"]
    B --> D["H(1)<br/>1 move"]
    B --> E["H(1)<br/>1 move"]
    C --> F["H(1)<br/>1 move"]
    C --> G["H(1)<br/>1 move"]
```

| Level | Calls | Moves at this level |
|---|---|---|
| 0: $H(3)$ | $1$ | $1$ |
| 1: $H(2)$ | $2$ | $2$ |
| 2: $H(1)$ | $4$ | $4$ |
| **total** | | $1 + 2 + 4 = 7 = 2^3 - 1$ |

In general level $j$ has $2^j$ calls ($j = 0, \dots, n-1$), each makes exactly one move, so the total is
$\sum_{j=0}^{n-1} 2^j = 2^n - 1$ — the same answer, obtained without algebra. The tree is a good
cross-check.

### How big is $2^n - 1$?

| disks $n$ | moves $2^n - 1$ |
|---|---|
| 3 | 7 |
| 10 | 1 023 |
| 20 | 1 048 575 |
| 64 | about $1.8 \cdot 10^{19}$ |

At one move per second, 64 disks would take about 585 billion years. **This is not the algorithm's
fault**: one can prove that every solution needs at least $2^n - 1$ moves (to move the largest disk, the
other $n-1$ disks must first be moved off it and then back on top of it). The exponential growth is a
property of the **problem**.

---

(ex2-binrec)=
## Example 3 · Counting binary digits (BinRec)

The binary representation of $n$ has one more digit than that of $\lfloor n/2 \rfloor$ (dividing by 2
removes the last bit).

```text
ALGORITHM BinRec(n)
    //Input: A positive decimal integer n
    //Output: The number of binary digits in n's binary representation
    if n = 1 return 1
    else return BinRec(⌊n/2⌋) + 1
```

**Step 1 · Input size.** $n$.

**Step 2 · Basic operation.** The addition `+ 1`.

**Step 3 · Cases.** The count depends only on $n$.

**Step 4 · Recurrence.**

$$
A(n) = A(\lfloor n/2 \rfloor) + 1 \quad \text{for } n > 1, \qquad A(1) = 0 .
$$

**Step 5 · Solution.** Use $n = 2^k$ (see [the $2^k$ trick](02_backward_substitution.md)):

$$
\begin{aligned}
A(2^k) &= A(2^{k-1}) + 1 = A(2^{k-2}) + 2 = \dots = A(2^{k-i}) + i \\
       &= \dots = A(2^0) + k = k ,
\end{aligned}
$$

because $A(2^0) = A(1) = 0$. With $k = \log_2 n$: $A(n) = \log_2 n \in \Theta(\log n)$. For an arbitrary
$n$ the exact answer is $A(n) = \lfloor \log_2 n \rfloor$.

:::{note} Size again
BinRec is logarithmic in the **value** of $n$, which is the same as **linear** in the number of bits $b$ of
$n$: it makes $b - 1$ additions. A careful statement says which measure is used.
:::

---

(ex2-sum)=
## Example 4 · Recursive sum of an array *(original example)*

```text
ALGORITHM RecSum(A[0..n-1])
    //Returns A[0] + ... + A[n-1], n ≥ 1
    if n = 1 return A[0]
    else return RecSum(A[0..n-2]) + A[n-1]
```

**Step 1 · Input size.** $n$, the number of elements.

**Step 2 · Basic operation.** The addition.

**Step 3 · Cases.** The count depends only on $n$.

**Step 4 · Recurrence.** One recursive call on $n-1$ elements, plus one addition. The recursion stops at
$n = 1$ and returns $A[0]$ **without any addition**:

$$
S(n) = S(n-1) + 1 \quad \text{for } n > 1, \qquad S(1) = 0 .
$$

**Step 5 · Solution.**

$$
S(n) = S(n-1) + 1 = S(n-2) + 2 = \dots = S(n-i) + i .
$$

The initial condition is at $1$: take $i = n - 1$, so $S(n) = S(1) + n - 1 = n - 1 \in \Theta(n)$.

**Verification.** $S(1) = 1 - 1 = 0$ ✔; $S(n-1) + 1 = (n-2) + 1 = n - 1$ ✔. This is exactly the number of
"$+$" signs in $A[0] + A[1] + \dots + A[n-1]$.

:::{warning} The initial condition matters
Compare with the factorial: same recurrence $X(n) = X(n-1) + 1$, but a different initial condition
($M(0) = 0$ there, $S(1) = 0$ here), and therefore a different answer ($n$ vs. $n - 1$).
:::

:::{note} A hidden cost in real code
In Python, `rec_sum(A[:-1])` would **copy** the slice, which costs $n - 1$ element copies per call — a
hidden cost that makes the total running time $\Theta(n^2)$. Pass the length (or an index) instead:

```python
def rec_sum(A, n):          # sum of A[0..n-1]
    if n == 1:
        return A[0]
    return rec_sum(A, n - 1) + A[n - 1]
```
:::

---

(ex2-power)=
## Example 5 · Fast exponentiation *(original example)*

Computing $a^n$ with the loop $a \cdot a \cdot \ldots \cdot a$ takes $n - 1$ multiplications. Using
$a^n = (a^{n/2})^2$ we can do much better:

$$
a^n =
\begin{cases}
a, & n = 1,\\
\left(a^{\lfloor n/2 \rfloor}\right)^2, & n \text{ even},\\
\left(a^{\lfloor n/2 \rfloor}\right)^2 \cdot a, & n \text{ odd}.
\end{cases}
$$

::::{tab-set}
:::{tab-item} Pseudocode
```text
ALGORITHM Power(a, n)
    //Computes a^n for an integer n ≥ 1
    if n = 1 return a
    p ← Power(a, ⌊n/2⌋)
    if n is even return p * p
    else return p * p * a
```
:::
:::{tab-item} Python
```python
def power(a, n):
    if n == 1:
        return a
    p = power(a, n // 2)
    if n % 2 == 0:
        return p * p
    return p * p * a
```
:::
::::

**Step 1 · Input size.** The exponent $n$.

**Step 2 · Basic operation.** Multiplication.

**Step 3 · Cases.** For even $n$ a call makes 1 multiplication, for odd $n$ it makes 2. So the count depends
on the binary digits of $n$, not only on its magnitude. We first solve for $n = 2^k$ (all even until 1),
then find bounds for all $n$.

**Step 4 · Recurrence.** One recursive call on $\lfloor n/2 \rfloor$:

$$
M(n) = M(\lfloor n/2 \rfloor) + \begin{cases} 1, & n \text{ even} \\ 2, & n \text{ odd} \end{cases}
\quad (n > 1), \qquad M(1) = 0 .
$$

**Step 5 · Solution.** For $n = 2^k$, every argument on the way down is even:

$$
M(2^k) = M(2^{k-1}) + 1 = M(2^{k-2}) + 2 = \dots = M(2^0) + k = k = \log_2 n .
$$

For general $n$ the number of calls that do work is $\lfloor \log_2 n \rfloor$, each doing 1 or 2
multiplications, so

$$
\lfloor \log_2 n \rfloor \;\le\; M(n) \;\le\; 2\lfloor \log_2 n \rfloor, \qquad M(n) \in \Theta(\log n).
$$

(Exactly: $M(n) = \lfloor \log_2 n \rfloor + (\text{number of 1-bits of } n) - 1$.)

**Example.** $n = 13 = 1101_2$: $13 \to 6 \to 3 \to 1$. Calls with 13 (odd, 2), 6 (even, 1), 3 (odd, 2):
$M(13) = 5$, and the formula gives $3 + 3 - 1 = 5$ ✔. For $n = 1000$: 14 multiplications instead of 999.

---

(ex2-bsearch)=
## Example 6 · Recursive binary search *(original example)*

Search for $K$ in a **sorted** array $A[l..r]$ by comparing with the middle element.

```text
ALGORITHM BinarySearch(A[l..r], K)
    //A is sorted in nondecreasing order; returns an index of K or -1
    if l > r return -1
    m ← ⌊(l + r)/2⌋
    if K = A[m] return m
    else if K < A[m] return BinarySearch(A[l..m-1], K)
    else return BinarySearch(A[m+1..r], K)
```

**Step 1 · Input size.** $n = r - l + 1$, the number of elements in the current subarray.

**Step 2 · Basic operation.** The comparison of $K$ with $A[m]$. As is customary, we count one
**three-way comparison** ($<$, $=$ or $>$) per call.

**Step 3 · Cases.** The search can stop early (if $K = A[m]$), so we analyze the **worst case**: the key
is absent, or found only at the very end. The best case is $1$ comparison ($K$ is the middle element).

**Step 4 · Recurrence (worst case).** With $n$ elements, the left part has $\lfloor (n-1)/2 \rfloor$ and
the right part $\lfloor n/2 \rfloor$ elements. The worst case continues in the larger part, of size
$\lfloor n/2 \rfloor$. An empty subarray needs no comparison:

$$
C_{worst}(n) = C_{worst}(\lfloor n/2 \rfloor) + 1 \quad \text{for } n \ge 1, \qquad C_{worst}(0) = 0 .
$$

**Step 5 · Solution.** For $n = 2^k$:

$$
C(2^k) = C(2^{k-1}) + 1 = \dots = C(2^0) + k = C(1) + k ,
$$

and $C(1) = C(0) + 1 = 1$. So $C_{worst}(2^k) = k + 1 = \log_2 n + 1$. For every $n \ge 1$ the exact
answer is

$$
C_{worst}(n) = \lfloor \log_2 n \rfloor + 1 \in \Theta(\log n),
$$

which is exactly the number of bits of $n$ (one more than the answer of BinRec).

| $n$ | $10$ | $1000$ | $10^6$ |
|---|---|---|---|
| sequential search, worst case | $10$ | $1000$ | $10^6$ |
| binary search, worst case | $4$ | $10$ | $20$ |

---

## Experiment: all six formulas at once

The cell below counts the basic operations for $n = 1, \dots, 16$ and compares them with the formulas.

```{code-cell} python
:tags: [hide-input]
import math

def count_factorial(n):
    return 0 if n == 0 else count_factorial(n - 1) + 1          # one multiplication per call

def hanoi_moves(n):
    return 1 if n == 1 else 2 * hanoi_moves(n - 1) + 1

def binrec_adds(n):
    return 0 if n == 1 else binrec_adds(n // 2) + 1

def recsum_adds(n):
    return 0 if n == 1 else recsum_adds(n - 1) + 1

def power_mults(n):
    if n == 1:
        return 0
    return power_mults(n // 2) + (1 if n % 2 == 0 else 2)

def bsearch_worst(n):
    return 0 if n == 0 else bsearch_worst(n // 2) + 1

print(f"{'n':>3} | {'F: n':>5} | {'Hanoi':>6} {'2^n-1':>6} | {'BinRec':>6} | {'RecSum':>6} | {'Power':>5} | {'BS':>3}")
for n in range(1, 17):
    lg = int(math.log2(n))
    assert count_factorial(n) == n and hanoi_moves(n) == 2**n - 1
    assert binrec_adds(n) == lg and recsum_adds(n) == n - 1
    assert lg <= power_mults(n) <= 2 * lg and bsearch_worst(n) == lg + 1
    print(f"{n:>3} | {count_factorial(n):>5} | {hanoi_moves(n):>6} {2**n-1:>6} | {binrec_adds(n):>6} | "
          f"{recsum_adds(n):>6} | {power_mults(n):>5} | {bsearch_worst(n):>3}")
print("All formulas confirmed for n = 1..16")
```

The full check (instrumented algorithms, larger $n$, legality of every Hanoi move, brute-force worst case
of binary search) is in
[`code/verify/verify_m2_theory.py`](https://github.com/SquardError/algorithms-textbook/blob/main/code/verify/verify_m2_theory.py).

Next: a recursive algorithm that is correct but hopelessly slow — the
[Fibonacci warning](04_fibonacci_warning.md).
