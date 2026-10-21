"""Small helpers shared by all verification scripts.

Each verification script compares a value obtained by *counting* (running an
instrumented algorithm, or evaluating a recurrence directly) with the closed
form printed in the book.
"""
import sys


class Checker:
    def __init__(self, title: str):
        self.title = title
        self.passed = 0
        self.failed = 0

    def equal(self, label, counted, formula):
        """Record one comparison counted == formula."""
        if counted == formula:
            self.passed += 1
        else:
            self.failed += 1
            print(f"  MISMATCH {label}: counted={counted!r} formula={formula!r}")

    def table(self, label, ns, count_fn, formula_fn, show=True):
        """Compare count_fn(n) with formula_fn(n) for every n in ns."""
        rows = []
        ok = True
        for n in ns:
            c, f = count_fn(n), formula_fn(n)
            self.equal(f"{label} (n={n})", c, f)
            ok &= c == f
            rows.append((n, c, f))
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {label}: n = {ns[0]}..{ns[-1]}")
        if show and not ok:
            for n, c, f in rows:
                print(f"     n={n:>4}  counted={c}  formula={f}")
        return ok

    def finish(self):
        total = self.passed + self.failed
        print(f"--> {self.title}: {self.passed}/{total} comparisons match")
        if self.failed:
            sys.exit(1)


def floor_log(n: int, base: int) -> int:
    """Exact floor(log_base n) for n >= 1, computed with integers only."""
    k = 0
    while n >= base:
        n //= base
        k += 1
    return k


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
