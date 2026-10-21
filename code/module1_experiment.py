"""Module 1 empirical verification.

Counts the basic operation in UniqueElements and SelectionSort and compares the
count with the formulas derived in Module 1:

    UniqueElements, worst case:  C_worst(n) = n(n-1)/2
    SelectionSort, every input:  C(n)       = n(n-1)/2

Run:  python code/module1_experiment.py          (prints tables, saves a plot)
"""
import pathlib
import random

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def unique_elements_count(A):
    """UniqueElements with a counter of the comparisons A[i] = A[j]."""
    n, comparisons = len(A), 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            comparisons += 1
            if A[i] == A[j]:
                return False, comparisons
    return True, comparisons


def selection_sort_count(A):
    """SelectionSort with a counter of the comparisons A[j] < A[min]."""
    A = list(A)
    n, comparisons = len(A), 0
    for i in range(0, n - 1):
        m = i
        for j in range(i + 1, n):
            comparisons += 1
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]
    return A, comparisons


def formula(n):
    return n * (n - 1) // 2


def main():
    random.seed(2026)
    sizes = list(range(2, 21)) + [50, 100, 200, 400]

    print("UniqueElements, worst case (all elements distinct)")
    print(f"{'n':>5} | {'counted':>8} | {'formula':>8} | match")
    unique_counts = []
    for n in sizes:
        A = random.sample(range(10 * n), n)  # distinct elements -> worst case
        _, counted = unique_elements_count(A)
        unique_counts.append(counted)
        print(f"{n:>5} | {counted:>8} | {formula(n):>8} | {counted == formula(n)}")

    print("\nSelectionSort, random arrays")
    print(f"{'n':>5} | {'counted':>8} | {'formula':>8} | match")
    for n in sizes:
        A = [random.randint(0, 9) for _ in range(n)]
        result, counted = selection_sort_count(A)
        assert result == sorted(A)
        print(f"{n:>5} | {counted:>8} | {formula(n):>8} | {counted == formula(n)}")

    print("\nUniqueElements, random arrays with values 0..n-1 (repeats likely)")
    for n in [10, 100, 400]:
        runs = [unique_elements_count([random.randrange(n) for _ in range(n)])[1] for _ in range(200)]
        print(f"n={n:>4}: average {sum(runs) / len(runs):8.1f}  (best 1, worst {formula(n)})")

    out = pathlib.Path(__file__).resolve().parent / "output"
    out.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(sizes, unique_counts, "o", label="counted (UniqueElements, worst case)")
    xs = list(range(2, sizes[-1] + 1))
    ax.plot(xs, [formula(n) for n in xs], label="formula n(n-1)/2")
    ax.set_xlabel("n")
    ax.set_ylabel("comparisons")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.savefig(out / "module1_experiment.png", dpi=120, bbox_inches="tight")
    print(f"\nPlot saved to {out / 'module1_experiment.png'}")


if __name__ == "__main__":
    main()
