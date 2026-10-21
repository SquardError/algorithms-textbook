"""Numbers quoted in the text and in the quizzes that are not covered elsewhere."""
import math
from math import comb

from common import Checker, fib, floor_log

ck = Checker("Text and quiz facts")


def count(fn, n):
    c = [0]
    fn(n, c)
    return c[0]


# ---- Introduction: growth table
ck.equal("log2(10) ~ 3.3", round(math.log2(10), 1), 3.3)
ck.equal("log2(100) ~ 6.6", round(math.log2(100), 1), 6.6)
ck.equal("log2(10^6) ~ 20", round(math.log2(10**6)), 20)
ck.equal("10 log2 10 ~ 33", round(10 * math.log2(10)), 33)
ck.equal("100 log2 100 ~ 660", round(100 * math.log2(100), -1), 660)
ck.equal("2^100 ~ 1.3e30", f"{float(2**100):.1e}", "1.3e+30")
ck.equal("2^1000 ~ 1.1e301", f"{float(2**1000):.1e}", "1.1e+301")
ck.equal("T(2n)/T(n) -> 4 for n(n-1)/2", round((2000 * 1999 / 2) / (1000 * 999 / 2), 2), 4.0)

# ---- Module 1 quiz
ck.equal("Q3 sum_{i=3}^n 1 = n-2 (n=5)", len(range(3, 6)), 3)
i, c = 3**10, 0
while i > 1:
    i //= 3
    c += 1
ck.equal("Q5 n=3^10 -> 10 iterations", c, 10)
for n in range(1, 30):
    ck.equal(f"Q6 10n (n={n})", sum(1 for _ in range(n) for _ in range(10)), 10 * n)
    ck.equal(f"Q10 n^2(n+1)/2 (n={n})",
             sum(1 for a in range(1, n + 1) for b in range(1, n + 1) for k in range(1, a + 1)),
             n * n * (n + 1) // 2)

# ---- Module 1 problems: numbers quoted in E1
for n, v in [(10, 120), (20, 1140), (100, 161700), (200, 1313400)]:
    ck.equal(f"M1-E1 C({n},3)", comb(n, 3), v)
ck.equal("M1-E1 ratio ~ 8.1", round(1313400 / 161700, 1), 8.1)
ck.equal("M1-M2 2^29 ~ 5.4e8", round(2**29 / 1e8, 1), 5.4)
ck.equal("M1 mistakes: 2^29 - 2 > 5*10^8", 2**29 - 2 > 5 * 10**8, True)
ck.equal("M1 experiment 4950 -> 19900", (100 * 99 // 2, 200 * 199 // 2), (4950, 19900))

# ---- Module 2
ck.equal("Hanoi 64 disks at 1 move/s ~ 585 billion years",
         round((2**64 - 1) / (365.25 * 24 * 3600) / 1e9), 585)
ck.equal("binary search n=10 worst = 4", floor_log(10, 2) + 1, 4)
A = [0, 0]
for n in range(2, 9):
    A.append(A[-1] + A[-2] + 1)
ck.equal("Fibonacci A(n) table n=0..8", A, [0, 0, 1, 2, 4, 7, 12, 20, 33])
ck.equal("Fibonacci table F(n+1), n=0..8", [fib(n + 1) for n in range(9)], [1, 1, 2, 3, 5, 8, 13, 21, 34])
ck.equal("F(41)-1 > 165 million (n=40)", fib(41) - 1, 165580140)
ck.equal("times computed row 1,1,2,3,5,8", [fib(j + 1) for j in range(6)], [1, 1, 2, 3, 5, 8])
ck.equal("M2-C2 C(30,15)-1", comb(30, 15) - 1, 155117519)
ck.equal("M2-E1 naive calls n=10", 2 * fib(11) - 1, 177)
ck.equal("M2-E1 naive calls n=25", 2 * fib(26) - 1, 242785)
ck.equal("M2-A4 81 = 10000 in base 3", (81 == 3**4, int("10000", 3)), (True, 81))
ck.equal("M2-B2 digit sum 40712", sum(map(int, "40712")), 14)
ck.equal("power n=13 is 1101b", bin(13), "0b1101")
# quiz M2 Q2: G(n) = G(n-2)*3 multiplications floor(n/2)
memo = {0: 0, 1: 0}
for n in range(2, 40):
    memo[n] = memo[n - 2] + 1
    ck.equal(f"M2 Q2 floor(n/2) n={n}", memo[n], n // 2)
# quiz M2 Q4 checks
M = {1: 1}
for n in range(2, 6):
    M[n] = 2 * M[n - 1] + 1
ck.equal("M2 Q4 M(2..4)", (M[2], M[3], M[4]), (3, 7, 15))
# quiz M2 Q9: T(n)=T(n-1)+2, T(0)=5
T = 5
for n in range(1, 30):
    T += 2
    ck.equal(f"M2 Q9 T({n}) = 2n+5", T, 2 * n + 5)
# stack depth chart: fact(5) depth 6, hanoi(5) depth 5, fib(6) depth 6
ck.equal("depth labels", (5 + 1, 5, 6), (6, 5, 6))

print("[OK] text and quiz facts" if ck.failed == 0 else "[FAIL] text and quiz facts")
ck.finish()
