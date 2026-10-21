"""Module 2 theory: backward substitutions, worked examples, Fibonacci, stack depth."""
import sys

import sympy as sp

from common import Checker, fib, floor_log

sys.setrecursionlimit(10_000)
ck = Checker("Module 2 theory")
N = list(range(1, 21))


class Counter:
    def __init__(self):
        self.ops = 0
        self.calls = 0
        self.depth = 0
        self.max_depth = 0

    def enter(self):
        self.calls += 1
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)

    def leave(self):
        self.depth -= 1


def recurrence(f, base, n):
    """Evaluate a recurrence literally: f(T, n) gives T(n) from smaller values."""
    memo = dict(base)

    def T(m):
        if m not in memo:
            memo[m] = f(T, m)
        return memo[m]

    return T(n)


# ---------------------------------------------------------------- 02 backward substitution demo
ck.table("demo T(n)=T(n-1)+3, T(0)=1 -> 3n+1", list(range(0, 21)),
         lambda n: recurrence(lambda T, m: T(m - 1) + 3, {0: 1}, n), lambda n: 3 * n + 1)
ck.table("demo T(n)=T(n-2)... general form after i steps: T(n-i)+3i (n=20)", list(range(0, 21)),
         lambda i: recurrence(lambda T, m: T(m - 1) + 3, {0: 1}, 20 - i) + 3 * i, lambda i: 61)


# ---------------------------------------------------------------- 03 worked examples
def factorial(n, ct):
    ct.enter()
    if n == 0:
        r = 1
    else:
        r = factorial(n - 1, ct)
        ct.ops += 1
        r = r * n
    ct.leave()
    return r


def fact_counts(n):
    ct = Counter()
    factorial(n, ct)
    return ct


ck.table("Factorial M(n) = n", list(range(0, 21)), lambda n: fact_counts(n).ops, lambda n: n)
ck.table("Factorial calls = n+1", list(range(0, 21)), lambda n: fact_counts(n).calls, lambda n: n + 1)
ck.table("Factorial max stack depth = n+1", list(range(0, 21)), lambda n: fact_counts(n).max_depth, lambda n: n + 1)


def hanoi(n, src, dst, aux, ct, moves):
    ct.enter()
    if n == 1:
        moves.append((src, dst))
    else:
        hanoi(n - 1, src, aux, dst, ct, moves)
        moves.append((src, dst))
        hanoi(n - 1, aux, dst, src, ct, moves)
    ct.leave()


def hanoi_run(n):
    ct, moves = Counter(), []
    hanoi(n, 1, 3, 2, ct, moves)
    # simulate the moves to be sure they are legal and finish the puzzle
    pegs = {1: list(range(n, 0, -1)), 2: [], 3: []}
    for s, d in moves:
        disk = pegs[s].pop()
        assert not pegs[d] or pegs[d][-1] > disk
        pegs[d].append(disk)
    assert pegs[3] == list(range(n, 0, -1))
    return ct, len(moves)


ck.table("Hanoi M(n) = 2^n - 1 (moves are legal)", N, lambda n: hanoi_run(n)[1], lambda n: 2**n - 1)
ck.table("Hanoi calls = 2^n - 1", N, lambda n: hanoi_run(n)[0].calls, lambda n: 2**n - 1)
ck.table("Hanoi max stack depth = n", N, lambda n: hanoi_run(n)[0].max_depth, lambda n: n)
ck.table("Hanoi recursion tree: level j has 2^j calls, sum = 2^n-1", N,
         lambda n: sum(2**j for j in range(n)), lambda n: 2**n - 1)
ck.equal("Hanoi 10 disks", 2**10 - 1, 1023)
ck.equal("Hanoi 20 disks > 10^6", 2**20 - 1 > 10**6, True)
ck.equal("Hanoi 64 disks ~ 1.8e19", round((2**64 - 1) / 1e19, 1), 1.8)
ck.equal("Hanoi 3 disks", 2**3 - 1, 7)


def binrec(n, ct):
    ct.enter()
    if n == 1:
        r = 1
    else:
        r = binrec(n // 2, ct)
        ct.ops += 1
        r = r + 1
    ct.leave()
    return r


def binrec_counts(n):
    ct = Counter()
    r = binrec(n, ct)
    assert r == n.bit_length()
    return ct


NN = list(range(1, 1025))
ck.table("BinRec A(n) = floor(log2 n)", NN, lambda n: binrec_counts(n).ops, lambda n: floor_log(n, 2))
ck.table("BinRec A(2^k) = k", list(range(0, 31)), lambda k: binrec_counts(2**k).ops, lambda k: k)
ck.table("BinRec stack depth = floor(log2 n)+1", NN, lambda n: binrec_counts(n).max_depth,
         lambda n: floor_log(n, 2) + 1)


# ---- original O1: recursive array sum
def rec_sum(A, n, ct):
    ct.enter()
    if n == 1:
        r = A[0]
    else:
        r = rec_sum(A, n - 1, ct)
        ct.ops += 1
        r = r + A[n - 1]
    ct.leave()
    return r


def rec_sum_counts(n):
    ct = Counter()
    A = list(range(3, 3 + n))
    assert rec_sum(A, n, ct) == sum(A)
    return ct


ck.table("RecSum S(n) = n-1", N, lambda n: rec_sum_counts(n).ops, lambda n: n - 1)
ck.table("RecSum depth = n", N, lambda n: rec_sum_counts(n).max_depth, lambda n: n)


# ---- original O2: fast exponentiation (base case n = 1)
MOD = 1_000_000_007  # keep numbers small; multiplications are counted, not their cost


def power(a, n, ct):
    ct.enter()
    if n == 1:
        r = a
    else:
        p = power(a, n // 2, ct)
        if n % 2 == 0:
            ct.ops += 1
            r = p * p % MOD
        else:
            ct.ops += 2
            r = p * p % MOD * a % MOD
    ct.leave()
    return r


def power_counts(n):
    ct = Counter()
    assert power(3, n, ct) == pow(3, n, MOD)
    return ct


ck.table("Power M(2^k) = k", list(range(0, 31)), lambda k: power_counts(2**k).ops, lambda k: k)
ck.table("Power M(n) = floor(log2 n) + (ones(n) - 1)", NN, lambda n: power_counts(n).ops,
         lambda n: floor_log(n, 2) + bin(n).count("1") - 1)
ck.table("Power M(2^k - 1) = 2(k-1)", list(range(1, 31)), lambda k: power_counts(2**k - 1).ops,
         lambda k: 2 * (k - 1))
ok = all(floor_log(n, 2) <= power_counts(n).ops <= 2 * floor_log(n, 2) for n in NN)
ck.equal("Power floor(log2 n) <= M(n) <= 2 floor(log2 n)", ok, True)
ck.equal("Power n=13 example", power_counts(13).ops, 5)
ck.equal("Power n=16 example", power_counts(16).ops, 4)
ck.equal("Power n=1000 (vs 999 for naive)", power_counts(1000).ops, 14)


# ---- original O3: recursive binary search, worst case
def bin_search(A, l, r, K, ct):
    ct.enter()
    if l > r:
        res = -1
    else:
        m = (l + r) // 2
        ct.ops += 1  # one three-way key comparison
        if K == A[m]:
            res = m
        elif K < A[m]:
            res = bin_search(A, l, m - 1, K, ct)
        else:
            res = bin_search(A, m + 1, r, K, ct)
    ct.leave()
    return res


def bs_worst(n):
    A = [2 * i for i in range(n)]  # even numbers; odd keys are absent
    worst = 0
    for K in list(range(-1, 2 * n + 1)):
        ct = Counter()
        res = bin_search(A, 0, n - 1, K, ct)
        assert (res == -1) == (K not in A)
        worst = max(worst, ct.ops)
    return worst


ck.table("BinarySearch C_worst(n) = floor(log2 n)+1", list(range(1, 300)), bs_worst,
         lambda n: floor_log(n, 2) + 1)
ck.table("BinarySearch C_worst(2^k) = k+1", list(range(0, 11)), lambda k: bs_worst(2**k), lambda k: k + 1)
ck.table("BinarySearch recurrence C(n)=C(floor(n/2))+1, C(0)=0", list(range(1, 300)),
         lambda n: recurrence(lambda T, m: T(m // 2) + 1, {0: 0}, n), lambda n: floor_log(n, 2) + 1)
ck.equal("BinarySearch n=1000 worst", floor_log(1000, 2) + 1, 10)
ck.equal("BinarySearch n=10^6 worst", floor_log(10**6, 2) + 1, 20)


# ---------------------------------------------------------------- 04 Fibonacci
def fib_naive(n, ct):
    ct.enter()
    if n <= 1:
        r = n
    else:
        a = fib_naive(n - 1, ct)
        b = fib_naive(n - 2, ct)
        ct.ops += 1
        r = a + b
    ct.leave()
    return r


def fib_naive_counts(n):
    ct = Counter()
    assert fib_naive(n, ct) == fib(n)
    return ct


FN = list(range(0, 26))
ck.table("Fibonacci naive additions A(n) = F(n+1) - 1", FN, lambda n: fib_naive_counts(n).ops,
         lambda n: fib(n + 1) - 1)
ck.table("Fibonacci recurrence A(n)=A(n-1)+A(n-2)+1", FN,
         lambda n: recurrence(lambda T, m: T(m - 1) + T(m - 2) + 1, {0: 0, 1: 0}, n), lambda n: fib(n + 1) - 1)
ck.table("Fibonacci naive calls = 2F(n+1) - 1", FN, lambda n: fib_naive_counts(n).calls,
         lambda n: 2 * fib(n + 1) - 1)
ck.table("Fibonacci naive depth = max(n,1)", FN, lambda n: fib_naive_counts(n).max_depth, lambda n: max(n, 1))


def times_computed(n):
    """How many times fib_naive(n) evaluates F(k), for every k."""
    cnt = {}

    def f(m):
        cnt[m] = cnt.get(m, 0) + 1
        if m > 1:
            f(m - 1)
            f(m - 2)

    f(n)
    return cnt


for nn in [5, 6, 10, 15]:
    c = times_computed(nn)
    for kk in range(1, nn + 1):
        ck.equal(f"F({nn}) computes F({nn}-{kk}+...) : F(n-j) computed F(j+1) times",
                 c[nn - (kk - 1)], fib(kk))
ck.equal("F(5) computes F(1) 5 times", times_computed(5)[1], 5)
ck.equal("F(5) computes F(0) 3 times", times_computed(5)[0], 3)
ck.equal("F(5) naive additions = 7", fib_naive_counts(5).ops, 7)
ck.equal("F(5) naive calls = 15", fib_naive_counts(5).calls, 15)
ck.equal("F(50) naive additions > 2*10^10", fib(51) - 1 > 2 * 10**10, True)
ck.equal("F(50) naive additions = 20365011073", fib(51) - 1, 20365011073)
phi = (1 + 5**0.5) / 2
ck.equal("phi rounded", round(phi, 3), 1.618)


def fib_memo_counts(n):
    memo = {}
    ct = Counter()

    def f(m):
        ct.enter()
        if m in memo:
            r = memo[m]
        elif m <= 1:
            r = m
            memo[m] = r
        else:
            a = f(m - 1)
            b = f(m - 2)
            ct.ops += 1
            r = a + b
            memo[m] = r
        ct.leave()
        return r

    assert f(n) == fib(n)
    return ct


ck.table("Fibonacci memo additions = n-1", list(range(1, 60)), lambda n: fib_memo_counts(n).ops, lambda n: n - 1)
ck.table("Fibonacci memo calls = 2n-1", list(range(1, 60)), lambda n: fib_memo_counts(n).calls, lambda n: 2 * n - 1)


def fib_iter_counts(n):
    if n <= 1:
        return 0
    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        a, b = b, a + b
        c += 1
    assert b == fib(n)
    return c


ck.table("Fibonacci iterative additions = n-1", list(range(1, 60)), fib_iter_counts, lambda n: n - 1)

# ---------------------------------------------------------------- 05 recursion vs iteration
ck.table("factorial tail-recursive: n multiplications", list(range(0, 21)),
         lambda n: (lambda f: f(f, n, 1, 0))(lambda s, m, acc, c: (acc, c) if m == 0 else s(s, m - 1, acc * m, c + 1))[1],
         lambda n: n)
ck.equal("Python default recursion limit", sys.getrecursionlimit() >= 1000, True)

# symbolic check of the backward-substitution results with sympy rsolve
T = sp.Function("T")
nn = sp.symbols("n", integer=True, nonnegative=True)
ck.equal("rsolve M(n)=M(n-1)+1, M(0)=0", sp.simplify(sp.rsolve(T(nn) - T(nn - 1) - 1, T(nn), {T(0): 0}) - nn), 0)
ck.equal("rsolve M(n)=2M(n-1)+1, M(1)=1",
         sp.simplify(sp.rsolve(T(nn) - 2 * T(nn - 1) - 1, T(nn), {T(1): 1}) - (2**nn - 1)), 0)
ck.equal("rsolve T(n)=T(n-1)+3, T(0)=1",
         sp.simplify(sp.rsolve(T(nn) - T(nn - 1) - 3, T(nn), {T(0): 1}) - (3 * nn + 1)), 0)

ck.finish()
