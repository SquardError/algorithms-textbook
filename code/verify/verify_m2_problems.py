"""Module 2 problems (A1-A4, B1-B4, C1-C2, M1-M2, E1)."""
import itertools
import sys
from math import comb

import sympy as sp

from common import Checker, fib, floor_log

sys.setrecursionlimit(10_000)
ck = Checker("Module 2 problems")
N = list(range(1, 21))


def recurrence(f, base, n):
    memo = dict(base)

    def T(m):
        if m not in memo:
            memo[m] = f(T, m)
        return memo[m]

    return T(n)


# ---------------------------------------------------------------- Level A
def a1_power_naive(a, n, c):
    if n == 0:
        return 1
    r = a1_power_naive(a, n - 1, c)
    c[0] += 1
    return a * r


def a1(n):
    c = [0]
    assert a1_power_naive(2, n, c) == 2**n
    return c[0]


ck.table("A1 naive power M(n) = n", list(range(0, 21)), a1, lambda n: n)
ck.table("A2 T(n)=T(n-1)+5, T(1)=2 -> 5n-3", N,
         lambda n: recurrence(lambda T, m: T(m - 1) + 5, {1: 2}, n), lambda n: 5 * n - 3)


def a3_search_from_end(A, n, K, c):
    if n == 0:
        return -1
    c[0] += 1
    if A[n - 1] == K:
        return n - 1
    return a3_search_from_end(A, n - 1, K, c)


def a3(n, K):
    c = [0]
    a3_search_from_end(list(range(n)), n, K, c)
    return c[0]


ck.table("A3 search from end, worst (absent) = n", list(range(0, 21)), lambda n: a3(n, -5), lambda n: n)
ck.table("A3 search from end, worst (K = A[0]) = n", N, lambda n: a3(n, 0), lambda n: n)
ck.table("A3 search from end, best (K = A[n-1]) = 1", N, lambda n: a3(n, n - 1), lambda n: 1)


def a4_tern_digits(n, c):
    if n < 3:
        return 1
    r = a4_tern_digits(n // 3, c)
    c[0] += 1
    return r + 1


def a4(n):
    c = [0]
    r = a4_tern_digits(n, c)
    digits, m = 0, n
    while m:
        digits, m = digits + 1, m // 3
    assert r == digits
    return c[0]


ck.table("A4 TernDigits A(3^k) = k", list(range(0, 15)), lambda k: a4(3**k), lambda k: k)
ck.table("A4 TernDigits A(n) = floor(log3 n)", list(range(1, 2001)), a4, lambda n: floor_log(n, 3))
ck.equal("A4 n=81", a4(81), 4)


# ---------------------------------------------------------------- Level B
def b1_rec(n, c):
    if n == 0:
        return
    for _ in range(1, 2 * n):
        c[0] += 1
    b1_rec(n - 1, c)


def b1(n):
    c = [0]
    b1_rec(n, c)
    return c[0]


ck.table("B1 T(n)=T(n-1)+(2n-1), T(0)=0 -> n^2", list(range(0, 21)), b1, lambda n: n * n)


def b2_digit_sum(n, c):
    if n < 10:
        return n
    r = b2_digit_sum(n // 10, c)
    c[0] += 1
    return r + n % 10


def b2(n):
    c = [0]
    assert b2_digit_sum(n, c) == sum(map(int, str(n)))
    return c[0]


ck.table("B2 DigitSum A(10^k) = k", list(range(0, 15)), lambda k: b2(10**k), lambda k: k)
ck.table("B2 DigitSum A(n) = (number of digits) - 1 = floor(log10 n)", list(range(1, 5001)), b2,
         lambda n: floor_log(n, 10))
ck.equal("B2 n=40712 additions", b2(40712), 4)


def b3_max_dc(A, l, r, c):
    if l == r:
        return A[l]
    m = (l + r) // 2
    a = b3_max_dc(A, l, m, c)
    b = b3_max_dc(A, m + 1, r, c)
    c[0] += 1
    return a if a > b else b


def b3(n):
    c = [0]
    A = [(7 * i) % 23 for i in range(n)]
    assert b3_max_dc(A, 0, n - 1, c) == max(A)
    return c[0]


ck.table("B3 MaxDC C(2^k) = 2^k - 1", list(range(0, 13)), lambda k: b3(2**k), lambda k: 2**k - 1)
ck.table("B3 MaxDC C(n) = n - 1 for all n", list(range(1, 300)), b3, lambda n: n - 1)


def b4_silly(n, c):
    if n == 1:
        return 1
    r = b4_silly(n - 1, c) + b4_silly(n - 1, c)
    c[0] += 1
    return r


def b4_fixed(n, c):
    if n == 1:
        return 1
    x = b4_fixed(n - 1, c)
    c[0] += 1
    return x + x


def b4(fn, n):
    c = [0]
    assert fn(n, c) == 2 ** (n - 1)
    return c[0]


ck.table("B4 two identical calls A(n) = 2^(n-1) - 1", N, lambda n: b4(b4_silly, n), lambda n: 2 ** (n - 1) - 1)
ck.table("B4 one call reused A(n) = n - 1", N, lambda n: b4(b4_fixed, n), lambda n: n - 1)
ck.equal("B4 n=30 silly", 2**29 - 1, 536870911)


# ---------------------------------------------------------------- Level C
def c1_rec(n, c):
    if n == 0:
        c[0] += 1
        return
    c1_rec(n - 1, c)
    for _ in range(2**n):
        c[0] += 1


def c1(n):
    c = [0]
    c1_rec(n, c)
    return c[0]


ck.table("C1 T(n)=T(n-1)+2^n, T(0)=1 -> 2^(n+1)-1", list(range(0, 18)), c1, lambda n: 2 ** (n + 1) - 1)
nn = sp.symbols("n", integer=True, nonnegative=True)
T = sp.Function("T")
ck.equal("C1 rsolve", sp.simplify(sp.rsolve(T(nn) - T(nn - 1) - 2**nn, T(nn), {T(0): 1}) - (2 ** (nn + 1) - 1)), 0)


def c2_binom(n, k, c):
    if k == 0 or k == n:
        return 1
    r = c2_binom(n - 1, k - 1, c) + c2_binom(n - 1, k, c)
    c[0] += 1
    return r


for n in range(0, 19):
    for k in range(0, n + 1):
        c = [0]
        assert c2_binom(n, k, c) == comb(n, k)
        ck.equal(f"C2 binomial additions A({n},{k}) = C(n,k) - 1", c[0], comb(n, k) - 1)
print("[OK] C2 binomial additions A(n,k) = C(n,k) - 1 for 0 <= k <= n <= 18" if ck.failed == 0 else "[FAIL] C2")
ck.equal("C2 A(20,10)", comb(20, 10) - 1, 184755)
ck.equal("C2 A(30,15) > 1.5*10^8", comb(30, 15) - 1 > 1.5 * 10**8, True)


# ---------------------------------------------------------------- Find the mistake
def m1_is_pal(S, l, r, c):
    if l >= r:
        return True
    c[0] += 1
    if S[l] != S[r]:
        return False
    return m1_is_pal(S, l + 1, r - 1, c)


def m1(S):
    c = [0]
    assert m1_is_pal(S, 0, len(S) - 1, c) == (S == S[::-1])
    return c[0]


ck.table("M1 IsPal worst (palindrome) = floor(n/2)", list(range(0, 21)), lambda n: m1("a" * n), lambda n: n // 2)
ck.table("M1 recurrence C(n)=C(n-2)+1, C(0)=C(1)=0", list(range(0, 21)),
         lambda n: recurrence(lambda T, m: T(m - 2) + 1, {0: 0, 1: 0}, n), lambda n: n // 2)
ck.table("M1 wrong initial condition C(0)=C(1)=1 gives floor(n/2)+1", list(range(0, 21)),
         lambda n: recurrence(lambda T, m: T(m - 2) + 1, {0: 1, 1: 1}, n), lambda n: n // 2 + 1)
for n in range(0, 9):  # exhaustive over binary strings: the palindrome is the worst case
    worst = max(m1("".join(s)) for s in itertools.product("ab", repeat=n))
    ck.equal(f"M1 exhaustive worst n={n}", worst, n // 2)


def m2_count(A, l, r, K, c):
    if l == r:
        return 1 if A[l] == K else 0
    m = (l + r) // 2
    x = m2_count(A, l, m, K, c)
    y = m2_count(A, m + 1, r, K, c)
    c[0] += 1
    return x + y


def m2(n):
    c = [0]
    A = [i % 3 for i in range(n)]
    assert m2_count(A, 0, n - 1, 0, c) == A.count(0)
    return c[0]


ck.table("M2 CountK additions A(2^k) = 2^k - 1", list(range(0, 13)), lambda k: m2(2**k), lambda k: 2**k - 1)
ck.table("M2 wrong recurrence A(n)=A(n/2)+1 gives log2 n", list(range(0, 13)),
         lambda k: recurrence(lambda T, m: T(m // 2) + 1, {1: 0}, 2**k), lambda k: k)


# ---------------------------------------------------------------- Empirical task E1
def e1_naive_calls(n):
    calls = [0]

    def f(m):
        calls[0] += 1
        return m if m <= 1 else f(m - 1) + f(m - 2)

    assert f(n) == fib(n)
    return calls[0]


def e1_memo_calls(n):
    calls, memo = [0], {}

    def f(m):
        calls[0] += 1
        if m in memo:
            return memo[m]
        r = m if m <= 1 else f(m - 1) + f(m - 2)
        memo[m] = r
        return r

    assert f(n) == fib(n)
    return calls[0]


ck.table("E1 naive Fibonacci calls = 2F(n+1) - 1", list(range(0, 26)), e1_naive_calls, lambda n: 2 * fib(n + 1) - 1)
ck.table("E1 memoized Fibonacci calls = 2n - 1", list(range(1, 200)), e1_memo_calls, lambda n: 2 * n - 1)
ck.equal("E1 naive calls n=20", e1_naive_calls(20), 21891)

ck.finish()
