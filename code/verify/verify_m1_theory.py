"""Module 1 theory: summation tools, worked examples, average case.

Every function `count_*` runs the algorithm exactly as written in the book
(Levitin pseudocode translated line by line) and counts the basic operation.
"""
import itertools
import random
from fractions import Fraction

import sympy as sp

from common import Checker, floor_log

ck = Checker("Module 1 theory")
N = list(range(1, 21))

# ---------------------------------------------------------------- 02 summation tools
i, n, l, u, k = sp.symbols("i n l u k", integer=True, positive=True)
ck.equal("sum 1, i=l..u", sp.simplify(sp.summation(1, (i, l, u)) - (u - l + 1)), 0)
ck.equal("sum i", sp.simplify(sp.summation(i, (i, 1, n)) - n * (n + 1) / 2), 0)
ck.equal("sum i^2", sp.simplify(sp.summation(i**2, (i, 1, n)) - n * (n + 1) * (2 * n + 1) / 6), 0)
ck.equal("sum 2^i, i=0..n", sp.simplify(sp.summation(2**i, (i, 0, n)) - (2 ** (n + 1) - 1)), 0)
# general geometric series, a != 1
a = sp.symbols("a", positive=True)
ck.equal("sum a^i, i=0..n", sp.simplify(sp.summation(a**i, (i, 0, n)) - (a ** (n + 1) - 1) / (a - 1)).subs(a, 3), 0)
# sum i^k ~ n^(k+1)/(k+1): the ratio tends to 1/(k+1)
for kk in range(1, 6):
    lim = sp.limit(sp.summation(i**kk, (i, 1, n)) / n ** (kk + 1), n, sp.oo)
    ck.equal(f"lim sum i^{kk} / n^{kk+1}", lim, sp.Rational(1, kk + 1))
# small examples used in the text
ck.equal("sum_{i=1}^n (2i+3) = n^2+4n", sp.simplify(sp.summation(2 * i + 3, (i, 1, n)) - (n**2 + 4 * n)), 0)
ck.equal("sum_{i=0}^{n-2} (n-1-i) = n(n-1)/2",
         sp.simplify(sp.summation(n - 1 - i, (i, 0, n - 2)) - n * (n - 1) / 2), 0)
ck.equal("sum_{i=5}^{n} 1 = n-4", sp.simplify(sp.summation(1, (i, 5, n)) - (n - 4)), 0)
ck.equal("sum_{i=1}^{n} 4i^3 Theta(n^4) leading coeff",
         sp.limit(sp.summation(4 * i**3, (i, 1, n)) / n**4, n, sp.oo), 1)
print("[OK] symbolic summation identities checked with sympy" if ck.failed == 0 else "[FAIL] symbolic")


# ---------------------------------------------------------------- 03 worked examples
def count_max_element(n):
    A = [random.randint(0, 99) for _ in range(n)]
    c = 0
    maxval = A[0]
    for i in range(1, n):
        c += 1
        if A[i] > maxval:
            maxval = A[i]
    return c


ck.table("MaxElement C(n) = n-1", N, count_max_element, lambda n: n - 1)


def count_unique(A):
    n, c = len(A), 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            c += 1
            if A[i] == A[j]:
                return c
    return c


ck.table("UniqueElements worst (all distinct) = n(n-1)/2", N,
         lambda n: count_unique(list(range(n))), lambda n: n * (n - 1) // 2)
ck.table("UniqueElements worst (only last two equal) = n(n-1)/2", list(range(2, 21)),
         lambda n: count_unique(list(range(n - 1)) + [n - 2]), lambda n: n * (n - 1) // 2)
ck.table("UniqueElements best (A[0]=A[1]) = 1", list(range(2, 21)),
         lambda n: count_unique([7, 7] + list(range(n - 2))), lambda n: 1)
# worst case really is the maximum over all inputs (exhaustive for small n)
for nn in range(2, 7):
    best = min(count_unique(list(p)) for p in itertools.product(range(nn), repeat=nn))
    worst = max(count_unique(list(p)) for p in itertools.product(range(nn), repeat=nn))
    ck.equal(f"UniqueElements exhaustive best n={nn}", best, 1)
    ck.equal(f"UniqueElements exhaustive worst n={nn}", worst, nn * (nn - 1) // 2)


def count_matrix_mult(n):
    c = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c += 1
    return c


ck.table("MatrixMultiplication M(n) = n^3", N, count_matrix_mult, lambda n: n**3)


def count_dependent(n):
    c = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            c += 1
    return c


def count_dependent_upper(n):
    c = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            c += 1
    return c


ck.table("dependent bound j=1..i: n(n+1)/2", N, count_dependent, lambda n: n * (n + 1) // 2)
ck.table("dependent bound j=i+1..n: n(n-1)/2", N, count_dependent_upper, lambda n: n * (n - 1) // 2)


def count_doubling(n):
    c, i = 0, 1
    while i <= n:
        c += 1
        i = 2 * i
    return c


NN = list(range(1, 1025))
ck.table("doubling loop: floor(log2 n)+1", NN, count_doubling, lambda n: floor_log(n, 2) + 1)
ck.table("doubling loop = number of bits of n", NN, count_doubling, lambda n: n.bit_length())


def count_halving(n):
    c, i = 0, n
    while i >= 1:
        c += 1
        i = i // 2
    return c


ck.table("halving loop: floor(log2 n)+1", NN, count_halving, lambda n: floor_log(n, 2) + 1)


# ---- original example O1: selection sort
def selection_sort_counts(A):
    A = list(A)
    n = len(A)
    comps = swaps = 0
    for i in range(0, n - 1):
        mn = i
        for j in range(i + 1, n):
            comps += 1
            if A[j] < A[mn]:
                mn = j
        A[i], A[mn] = A[mn], A[i]
        swaps += 1
    assert A == sorted(A)
    return comps, swaps


for label, make in [("random", lambda n: random.sample(range(100), n)),
                    ("sorted", lambda n: list(range(n))),
                    ("reversed", lambda n: list(range(n, 0, -1)))]:
    ck.table(f"SelectionSort comparisons ({label}) = n(n-1)/2", N,
             lambda n: selection_sort_counts(make(n))[0], lambda n: n * (n - 1) // 2)
    ck.table(f"SelectionSort swaps ({label}) = n-1", N,
             lambda n: selection_sort_counts(make(n))[1], lambda n: n - 1)


# ---- original example O2: search in an m x n matrix
def matrix_search(M, K):
    c = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            c += 1
            if M[i][j] == K:
                return c
    return c


for m in range(1, 8):
    for nn in range(1, 8):
        M = [[i * nn + j for j in range(nn)] for i in range(m)]
        ck.equal(f"MatrixSearch worst (absent) m={m} n={nn}", matrix_search(M, -1), m * nn)
        ck.equal(f"MatrixSearch worst (last cell) m={m} n={nn}", matrix_search(M, m * nn - 1), m * nn)
        ck.equal(f"MatrixSearch best m={m} n={nn}", matrix_search(M, 0), 1)
print("[OK] MatrixSearch: worst m*n, best 1 for m,n = 1..7" if ck.failed == 0 else "[FAIL] MatrixSearch")


# ---- original example O3: linear outer loop, tripling inner loop
def count_tripling_nested(n):
    c = 0
    for i in range(1, n + 1):
        j = 1
        while j <= n:
            c += 1
            j = 3 * j
    return c


ck.table("outer linear, inner tripling: n(floor(log3 n)+1)", list(range(1, 301)),
         count_tripling_nested, lambda n: n * (floor_log(n, 3) + 1))
# values quoted in the text
ck.equal("tripling inner loop, n=10", count_tripling_nested(10) // 10, 3)
ck.equal("tripling inner loop, n=27", count_tripling_nested(27) // 27, 4)


# ---------------------------------------------------------------- 04 average case
def seq_search_count(A, K):
    c = 0
    for x in A:
        c += 1
        if x == K:
            return c
    return c


def exact_average(n, p):
    """Expected comparisons: key at position i (1..n) with prob p/n, absent with prob 1-p."""
    A = list(range(1, n + 1))
    exp = sum(Fraction(p) / n * seq_search_count(A, pos) for pos in A)
    exp += (1 - Fraction(p)) * seq_search_count(A, 0)
    return exp


for p in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(2, 3), Fraction(1)]:
    ck.table(f"SequentialSearch C_avg, p={p}", N, lambda n: exact_average(n, p),
             lambda n: p * (n + 1) / 2 + n * (1 - p))
ck.equal("p=1/2, n=100 example", exact_average(100, Fraction(1, 2)), Fraction(301, 4))

ck.finish()
