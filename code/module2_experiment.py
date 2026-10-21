"""Module 2 empirical verification.

1. Tower of Hanoi: counts disk moves and compares with M(n) = 2^n - 1.
2. Fibonacci: counts calls of the naive and the memoized algorithm and
   compares with 2F(n+1) - 1 and 2n - 1 (problem E1 of Module 2).

Run:  python code/module2_experiment.py          (prints tables, saves a plot)
"""
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def hanoi_moves(n):
    moves = 0

    def hanoi(k, src, dst, aux):
        nonlocal moves
        if k == 1:
            moves += 1
        else:
            hanoi(k - 1, src, aux, dst)
            moves += 1
            hanoi(k - 1, aux, dst, src)

    hanoi(n, 1, 3, 2)
    return moves


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


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    print("Tower of Hanoi")
    print(f"{'n':>3} | {'counted':>8} | {'2^n - 1':>8} | match")
    for n in range(1, 21):
        c = hanoi_moves(n)
        print(f"{n:>3} | {c:>8} | {2**n - 1:>8} | {c == 2**n - 1}")

    print("\nFibonacci: number of calls")
    print(f"{'n':>3} | {'naive':>7} | {'2F(n+1)-1':>9} | {'memo':>4} | {'2n-1':>4}")
    ns = list(range(1, 26))
    naive, memo = [], []
    for n in ns:
        a, b = naive_calls(n), memo_calls(n)
        naive.append(a)
        memo.append(b)
        print(f"{n:>3} | {a:>7} | {2 * fib(n + 1) - 1:>9} | {b:>4} | {2 * n - 1:>4}")

    out = pathlib.Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.semilogy(ns, naive, "o-", label="naive recursion (counted)")
    ax.semilogy(ns, memo, "s-", label="memoized (counted)")
    ax.set_xlabel("n")
    ax.set_ylabel("calls (log scale)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    fig.savefig(out / "module2_experiment.png", dpi=120, bbox_inches="tight")
    print(f"\nPlot saved to {out / 'module2_experiment.png'}")


if __name__ == "__main__":
    main()
