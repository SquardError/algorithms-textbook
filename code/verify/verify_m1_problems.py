"""Module 1 problems (A1-A4, B1-B4, C1-C2, M1-M2, E1) and quiz facts."""
import itertools
import random
from fractions import Fraction

import sympy as sp

from common import Checker

ck = Checker("Module 1 problems")
N = list(range(1, 21))


# ---------------------------------------------------------------- Level A
def a1_dot_product(n):
    x = [random.randint(-9, 9) for _ in range(n)]
    y = [random.randint(-9, 9) for _ in range(n)]
    s, c = 0, 0
    for i in range(n):
        s = s + x[i] * y[i]
        c += 1
    return c


ck.table("A1 DotProduct multiplications = n", N, a1_dot_product, lambda n: n)

i, n = sp.symbols("i n", integer=True, positive=True)
ck.equal("A2 sum_{i=1}^n (3i+2) = (3n^2+7n)/2",
         sp.simplify(sp.summation(3 * i + 2, (i, 1, n)) - (3 * n**2 + 7 * n) / 2), 0)
ck.table("A2 numeric", N, lambda n: sum(3 * i + 2 for i in range(1, n + 1)),
         lambda n: (3 * n * n + 7 * n) // 2)


def a3_loop(n):
    c = 0
    for i in range(3, 2 * n + 1):
        for j in range(1, 6):
            c += 1
    return c


ck.table("A3 loop count = 10n - 10", N, a3_loop, lambda n: 10 * n - 10)


def a4_min_max(A):
    c = 0
    mn = mx = A[0]
    for i in range(1, len(A)):
        c += 1
        if A[i] < mn:
            mn = A[i]
        c += 1
        if A[i] > mx:
            mx = A[i]
    assert (mn, mx) == (min(A), max(A))
    return c


ck.table("A4 MinMax comparisons = 2(n-1)", N,
         lambda n: a4_min_max(random.sample(range(1000), n)), lambda n: 2 * (n - 1))


# ---------------------------------------------------------------- Level B
def b1(n):
    c = 0
    for i in range(0, n):
        for j in range(0, 2 * i + 1):
            c += 1
    return c


ck.table("B1 sum (2i+1) = n^2", N, b1, lambda n: n * n)


def b2_has_zero_row(M):
    n, c = len(M), 0
    for i in range(n):
        j = 0
        while j < n:
            c += 1
            if M[i][j] != 0:
                break
            j += 1
        if j == n:
            return True, c
    return False, c


def b2_worst_input(n):  # every row has its only nonzero entry in the last column
    return [[0] * (n - 1) + [1] for _ in range(n)]


ck.table("B2 HasZeroRow worst = n^2", N, lambda n: b2_has_zero_row(b2_worst_input(n))[1], lambda n: n * n)
ck.table("B2 worst (zero row is the last row) = n^2", N,
         lambda n: b2_has_zero_row(b2_worst_input(n)[:-1] + [[0] * n])[1], lambda n: n * n)
ck.table("B2 best (first row zero) = n", N, lambda n: b2_has_zero_row([[0] * n] * n)[1], lambda n: n)
ck.table("B2 best (every row starts with nonzero) = n", N,
         lambda n: b2_has_zero_row([[1] * n for _ in range(n)])[1], lambda n: n)
for nn in range(1, 4):  # exhaustive over all 0/1 matrices
    counts = [b2_has_zero_row([list(bits[r * nn:(r + 1) * nn]) for r in range(nn)])[1]
              for bits in itertools.product([0, 1], repeat=nn * nn)]
    ck.equal(f"B2 exhaustive min n={nn}", min(counts), nn)
    ck.equal(f"B2 exhaustive max n={nn}", max(counts), nn * nn)


def b3(n):
    c = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                c += 1
    return c


ck.table("B3 triple loop = n(n+1)(n+2)/6", N, b3, lambda n: n * (n + 1) * (n + 2) // 6)
j = sp.symbols("j", integer=True, positive=True)
ck.equal("B3 symbolic", sp.factor(sp.summation(sp.summation(j, (j, 1, i)), (i, 1, n))
                                  - n * (n + 1) * (n + 2) / 6), 0)


def b4_prefix_naive(A):
    n, c = len(A), 0
    P = [0] * n
    for i in range(n):
        s = 0
        for j in range(i + 1):
            s = s + A[j]
            c += 1
        P[i] = s
    assert P == list(itertools.accumulate(A))
    return c


def b4_prefix_fast(A):
    n, c = len(A), 0
    P = [0] * n
    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i - 1] + A[i]
        c += 1
    assert P == list(itertools.accumulate(A))
    return c


ck.table("B4 naive prefix sums additions = n(n+1)/2", N,
         lambda n: b4_prefix_naive(random.sample(range(100), n)), lambda n: n * (n + 1) // 2)
ck.table("B4 one-pass prefix sums additions = n-1", N,
         lambda n: b4_prefix_fast(random.sample(range(100), n)), lambda n: n - 1)
ck.equal("B4 n=1000 naive", 1000 * 1001 // 2, 500500)


# ---------------------------------------------------------------- Level C
def c1_first_even(A):
    c = 0
    for x in A:
        c += 1
        if x % 2 == 0:
            return c
    return c


def c1_exact_average(n):
    """Each element even with probability 1/2, independently: average over all 2^n patterns."""
    total = sum(c1_first_even(bits) for bits in itertools.product([0, 1], repeat=n))
    return Fraction(total, 2**n)


ck.table("C1 FirstEven average = 2 - 2^(1-n)", list(range(1, 15)), c1_exact_average,
         lambda n: 2 - Fraction(2, 2**n))
ck.table("C1 via tail sum: sum_{i=1}^n (1/2)^(i-1)", list(range(1, 15)),
         lambda n: sum(Fraction(1, 2 ** (i - 1)) for i in range(1, n + 1)),
         lambda n: 2 - Fraction(2, 2**n))
ck.equal("C1 n=3 value 7/4", c1_exact_average(3), Fraction(7, 4))


def c2_halving_outer(n):
    c, i = 0, n
    while i >= 1:
        for j in range(1, i + 1):
            c += 1
        i = i // 2
    return c


ck.table("C2 n = 2^k: 2n - 1", [2**k for k in range(0, 15)], c2_halving_outer, lambda n: 2 * n - 1)
ok = all(n <= c2_halving_outer(n) < 2 * n for n in range(1, 2001))
ck.equal("C2 n <= C(n) < 2n for n = 1..2000", ok, True)
print(f"[{'OK' if ok else 'FAIL'}] C2 bounds n <= C(n) < 2n: n = 1..2000")
ck.equal("C2 n=100 example", c2_halving_outer(100), 197)


# ---------------------------------------------------------------- Find the mistake
def m1_is_sorted(A):
    c = 0
    for i in range(len(A) - 1):
        c += 1
        if A[i] > A[i + 1]:
            return False, c
    return True, c


ck.table("M1 IsSorted worst (sorted) = n-1", N, lambda n: m1_is_sorted(list(range(n)))[1], lambda n: n - 1)
ck.table("M1 IsSorted best (A[0]>A[1]) = 1", list(range(2, 21)),
         lambda n: m1_is_sorted([5, 1] + list(range(n - 2)))[1], lambda n: 1)


def m2_sum_divisors(n):
    s, c = 0, 0
    for d in range(1, n + 1):
        c += 1
        if n % d == 0:
            s += d
    return c


ck.table("M2 SumDivisors divisions = n", N, m2_sum_divisors, lambda n: n)
# n with b bits satisfies 2^(b-1) <= n < 2^b
ck.equal("M2 bits bound", all(2 ** (n.bit_length() - 1) <= n < 2 ** n.bit_length() for n in range(1, 5000)), True)
ck.equal("M2 example: 30-bit number has >= 2^29 iterations", 2**29, 536870912)


# ---------------------------------------------------------------- Empirical task E1
def e1_zero_triples(A):
    n, c, count = len(A), 0, 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                c += 1
                if A[i] + A[j] + A[k] == 0:
                    count += 1
    return c


ck.table("E1 ZeroTriples = n(n-1)(n-2)/6", N,
         lambda n: e1_zero_triples([random.randint(-9, 9) for _ in range(n)]),
         lambda n: n * (n - 1) * (n - 2) // 6)

ck.finish()
