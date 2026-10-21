---
short_title: 5 · Recursion vs. iteration
kernelspec:
  name: python3
  display_name: Python 3
---

# Recursion vs. Iteration

The time analysis of a recursive algorithm does not tell the whole story. Recursion also costs
**memory**.

## The call stack

Every time a function is called, the computer stores a **stack frame** for it: its parameters, local
variables and the place to return to. The frames of all active (unfinished) calls form the **call stack**.
A frame is removed when its call returns.

For the factorial $F(3)$ the stack grows to four frames before anything returns:

```{mermaid}
flowchart LR
    subgraph s1["1 · calls go down"]
        direction TB
        a1["F(3): waiting for F(2)"] --- a2["F(2): waiting for F(1)"] --- a3["F(1): waiting for F(0)"] --- a4["F(0): returns 1"]
    end
    subgraph s2["2 · results come back"]
        direction TB
        b4["F(0) = 1"] --> b3["F(1) = 1·1 = 1"] --> b2["F(2) = 1·2 = 2"] --> b1["F(3) = 2·3 = 6"]
    end
    s1 --> s2
```

The largest number of frames on the stack at the same time is the **recursion depth**. Since every frame
takes memory, **the space complexity of a recursive algorithm is at least proportional to its recursion
depth.**

## Depth of the algorithms in this module

| Algorithm | Time (basic operations) | Recursion depth (memory) | Iterative version |
|---|---|---|---|
| Factorial $F(n)$ | $n$ | $n + 1 \in \Theta(n)$ | loop: $n$ mult., $\Theta(1)$ memory |
| RecSum | $n - 1$ | $n \in \Theta(n)$ | loop: $\Theta(1)$ memory |
| BinRec | $\lfloor \log_2 n \rfloor$ | $\lfloor \log_2 n \rfloor + 1 \in \Theta(\log n)$ | halving loop: $\Theta(1)$ memory |
| Binary search | $\le \lfloor \log_2 n \rfloor + 1$ | $\Theta(\log n)$ | loop: $\Theta(1)$ memory |
| Tower of Hanoi | $2^n - 1$ | $n \in \Theta(n)$ | possible, but no faster |
| Naive Fibonacci | $F(n+1) - 1$ | $n \in \Theta(n)$ | loop: $n - 1$ add., $\Theta(1)$ memory |

Notice the Tower of Hanoi: **exponential time but only linear memory**. Time counts all the calls ever
made; depth counts only those active at the same moment.

The chart shows how the stack depth changes over time while the algorithms run.

```{code-cell} python
:tags: [remove-input]
import matplotlib.pyplot as plt

def trace(run):
    depth, history = [0], []
    def enter():
        depth[0] += 1; history.append(depth[0])
    def leave():
        depth[0] -= 1; history.append(depth[0])
    run(enter, leave)
    return history

def hanoi(n, enter, leave):
    enter()
    if n > 1:
        hanoi(n - 1, enter, leave); hanoi(n - 1, enter, leave)
    leave()

def fact(n, enter, leave):
    enter()
    if n > 0:
        fact(n - 1, enter, leave)
    leave()

def fib(n, enter, leave):
    enter()
    if n > 1:
        fib(n - 1, enter, leave); fib(n - 2, enter, leave)
    leave()

fig, axes = plt.subplots(1, 3, figsize=(11, 3.2), sharey=True)
for ax, (name, run) in zip(axes, [("Factorial F(5)", lambda e, l: fact(5, e, l)),
                                  ("Hanoi, n = 5", lambda e, l: hanoi(5, e, l)),
                                  ("Naive Fibonacci F(6)", lambda e, l: fib(6, e, l))]):
    h = trace(run)
    ax.step(range(len(h)), h, where="post", linewidth=1.8)
    ax.set_title(f"{name}\nmax depth = {max(h)}", fontsize=10)
    ax.set_xlabel("time (call / return events)")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("frames on the stack")
plt.tight_layout(); plt.show()
```

Hanoi makes $2^5 - 1 = 31$ calls (a long time axis), but the stack never holds more than 5 frames.

## A practical limit: stack overflow

The stack is small compared with the rest of memory. If the recursion is too deep, the program crashes
with a **stack overflow**. Python protects itself with a recursion limit (1000 by default):

```{code-cell} python
def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n

print(len(str(factorial(500))), "digits in 500!")   # depth 501: fine
try:
    factorial(5000)                                # depth 5001: too deep
except RecursionError as error:
    print("RecursionError:", error)
```

The iterative loop computes $5000!$ without any problem, because it uses a constant number of variables.

## Tail recursion

A recursive call is a **tail call** if it is the **very last** action of the function — nothing is done
with its result except returning it. The factorial above is **not** tail-recursive: after `factorial(n - 1)`
returns, we still multiply by `n`.

We can make it tail-recursive by carrying the partial product in an extra parameter, an
**accumulator**:

```text
ALGORITHM FactTail(n, acc)
    //Returns acc · n!; call as FactTail(n, 1)
    if n = 0 return acc
    else return FactTail(n - 1, acc * n)
```

The multiplication now happens **before** the call, so nothing is left to do after it. Such a function
can be converted into a loop **mechanically**: replace the call by updating the parameters and jumping
to the start.

```text
ALGORITHM FactLoop(n)
    acc ← 1
    while n > 0 do
        acc ← acc * n
        n ← n - 1
    return acc
```

Both make $n$ multiplications, but the loop needs $\Theta(1)$ memory. Some compilers (for example, for
Scheme, and many C compilers with optimization enabled) perform this conversion automatically
(**tail-call optimization**). **Python does not**, so in Python deep recursion should be rewritten as a
loop by hand.

## When to choose recursion

- **Recursion is natural** when the problem is self-similar: trees, divide-and-conquer, the Tower of Hanoi.
  The code is often shorter and closer to the mathematical definition — a good starting point for design.
- **The price is stack memory**: depth $\Theta(n)$ for the factorial, $\Theta(\log n)$ for BinRec and binary
  search, $\Theta(n)$ for Hanoi.
- **Overlapping subproblems** (Fibonacci) make plain recursion exponentially slow; use memoization or
  bottom-up iteration.
- **Tail recursion** can always be turned into a loop.

:::{important} Report both
For a recursive algorithm, state the **time** (the solution of the recurrence) **and** the **space** (at
least the recursion depth).
:::

Next: test yourself in the [Module 2 quiz](06_quiz.md).
