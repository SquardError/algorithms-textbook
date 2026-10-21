---
short_title: 6 · Quiz
kernelspec:
  name: python3
  display_name: Python 3
---

# Module 2 Quiz

Ten questions on recurrences, initial conditions, orders of growth and recursion depth. Click an answer
to see the explanation.

```{code-cell} python
:tags: [remove-input]
from jupyterquiz import display_quiz

quiz_m2 = [
    {
        "question": "1. Which pair describes the number of basic operations of a recursive algorithm completely?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "A recurrence relation together with an initial condition", "correct": True,
             "feedback": "Correct. The recurrence alone has infinitely many solutions (e.g. $M(n) = n + c$ for $M(n) = M(n-1) + 1$); the initial condition picks the right one."},
            {"answer": "A recurrence relation alone", "correct": False,
             "feedback": "Incorrect. Without the initial condition the solution is not unique: $n$, $n+5$ and $n-3$ all satisfy $M(n) = M(n-1) + 1$."},
            {"answer": "A sum over the loop indices", "correct": False,
             "feedback": "Incorrect. Sums are the tool for loops (Module 1); a recursive algorithm usually has no loop that gives the count directly."},
            {"answer": "The initial condition alone", "correct": False,
             "feedback": "Incorrect. The initial condition only says what happens in the stopping case, not how the count grows."},
        ],
    },
    {
        "question": "2. Which recurrence gives the number of multiplications $M(n)$ of this algorithm?",
        "type": "multiple_choice",
        "code": "ALGORITHM G(n)\n    if n ≤ 1 return 1\n    else return G(n - 2) * 3",
        "answers": [
            {"answer": "$M(n) = M(n-2) + 1$ for $n > 1$, $M(0) = M(1) = 0$", "correct": True,
             "feedback": "Correct. One recursive call on $n-2$ plus one multiplication; the stopping cases $n = 0, 1$ multiply nothing. (Solution: $M(n) = \\lfloor n/2 \\rfloor$.)"},
            {"answer": "$M(n) = M(n-1) + 1$, $M(0) = 0$", "correct": False,
             "feedback": "Incorrect. The recursive call is on $n - 2$, not $n - 1$."},
            {"answer": "$M(n) = 3M(n-2)$, $M(1) = 1$", "correct": False,
             "feedback": "Incorrect. The factor 3 is part of the computed value, not of the number of multiplications; each call makes one multiplication."},
            {"answer": "$M(n) = 2M(n-2) + 1$, $M(0) = M(1) = 0$", "correct": False,
             "feedback": "Incorrect. There is only one recursive call per invocation, so the coefficient is 1."},
        ],
    },
    {
        "question": "3. RecMin(A[0..n-1]) returns A[0] if n = 1; otherwise it calls RecMin on A[0..n-2] and makes one comparison. What is the initial condition for the number of comparisons $C(n)$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$C(1) = 0$", "correct": True,
             "feedback": "Correct. The recursion stops at $n = 1$ and returns $A[0]$ without comparing anything."},
            {"answer": "$C(0) = 0$", "correct": False,
             "feedback": "Incorrect. The algorithm never reaches $n = 0$; the initial condition must match the actual stopping case."},
            {"answer": "$C(1) = 1$", "correct": False,
             "feedback": "Incorrect. Returning $A[0]$ involves no comparison. Taking $C(1) = 1$ would give $n$ instead of the correct $n - 1$."},
            {"answer": "No initial condition is needed", "correct": False,
             "feedback": "Incorrect. Without it the recurrence $C(n) = C(n-1) + 1$ does not determine $C(n)$."},
        ],
    },
    {
        "question": "4. What is the solution of $M(n) = 2M(n-1) + 1$, $M(1) = 1$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$M(n) = 2^n - 1$", "correct": True,
             "feedback": "Correct. After $i$ substitutions $M(n) = 2^i M(n-i) + 2^i - 1$; with $i = n - 1$ we get $2^{n-1} + 2^{n-1} - 1 = 2^n - 1$."},
            {"answer": "$M(n) = 2n - 1$", "correct": False,
             "feedback": "Incorrect. Check $n = 3$: $M(3) = 2 \\cdot 3 + 1 = 7$, while $2 \\cdot 3 - 1 = 5$. The coefficient 2 in front of $M(n-1)$ doubles the count at each level."},
            {"answer": "$M(n) = 2^{n-1}$", "correct": False,
             "feedback": "Incorrect. Check $n = 2$: $M(2) = 2 \\cdot 1 + 1 = 3$, but $2^{1} = 2$."},
            {"answer": "$M(n) = n^2$", "correct": False,
             "feedback": "Incorrect. Check $n = 4$: $M(4) = 15$, not 16, and for larger $n$ the gap grows exponentially."},
        ],
    },
    {
        "question": "5. What is the order of growth of the solution of $A(n) = A(\\lfloor n/2 \\rfloor) + 1$, $A(1) = 0$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$\\Theta(\\log n)$", "correct": True,
             "feedback": "Correct. For $n = 2^k$: $A(2^k) = A(2^{k-1}) + 1 = \\dots = k = \\log_2 n$."},
            {"answer": "$\\Theta(n)$", "correct": False,
             "feedback": "Incorrect. That would be $A(n) = A(n-1) + 1$. Halving the argument reaches 1 after only about $\\log_2 n$ steps."},
            {"answer": "$\\Theta(n/2)$, which is smaller than $\\Theta(n)$", "correct": False,
             "feedback": "Incorrect. First, $\\Theta(n/2) = \\Theta(n)$. Second, the argument is halved, not decreased by 2."},
            {"answer": "$\\Theta(n \\log n)$", "correct": False,
             "feedback": "Incorrect. Each call does a constant amount of work (one addition), so there is no factor $n$."},
        ],
    },
    {
        "question": "6. Why does the naive recursive Fibonacci algorithm take exponential time?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "It solves the same subproblems many times (overlapping subproblems)", "correct": True,
             "feedback": "Correct. There are only $n+1$ different subproblems, but e.g. $F(n-2)$ is computed twice, $F(n-3)$ three times, $F(n-4)$ five times, and so on."},
            {"answer": "Because adding large numbers is slow", "correct": False,
             "feedback": "Incorrect. Even if every addition took constant time, the number of additions, $F(n+1) - 1$, is exponential."},
            {"answer": "Because every recursive algorithm is slower than an iterative one", "correct": False,
             "feedback": "Incorrect. Recursive factorial makes exactly as many multiplications as the loop; recursion itself is not the problem."},
            {"answer": "Because the recursion depth is exponential", "correct": False,
             "feedback": "Incorrect. The depth is only about $n$; it is the total number of calls that is exponential."},
        ],
    },
    {
        "question": "7. The Tower of Hanoi algorithm makes $2^n - 1$ moves. What is its recursion depth (the maximum number of frames on the call stack)?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$n$", "correct": True,
             "feedback": "Correct. Each active call waits for a call with one disk fewer, so the longest chain is $H(n), H(n-1), \\dots, H(1)$."},
            {"answer": "$2^n - 1$", "correct": False,
             "feedback": "Incorrect. That is the total number of calls over the whole run; most of them are finished before others start."},
            {"answer": "$2^{n-1}$", "correct": False,
             "feedback": "Incorrect. That is the number of calls on the last level of the recursion tree, not the length of the longest chain."},
            {"answer": "$\\log_2 n$", "correct": False,
             "feedback": "Incorrect. The argument decreases by 1, not by half, so the chain has length $n$."},
        ],
    },
    {
        "question": "8. Which function is tail-recursive?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "SumTo(n, acc): if n = 0 return acc, else return SumTo(n - 1, acc + n)", "correct": True,
             "feedback": "Correct. The recursive call is the very last action; its result is returned unchanged. It can be turned into a loop mechanically."},
            {"answer": "SumTo(n): if n = 0 return 0, else return SumTo(n - 1) + n", "correct": False,
             "feedback": "Incorrect. After the call returns, its result is still added to $n$, so the call is not the last action."},
            {"answer": "Fib(n): if n ≤ 1 return n, else return Fib(n - 1) + Fib(n - 2)", "correct": False,
             "feedback": "Incorrect. There are two calls and an addition after them."},
            {"answer": "Hanoi(n, …): Hanoi(n - 1, …); move a disk; Hanoi(n - 1, …)", "correct": False,
             "feedback": "Incorrect. The first call is followed by more work. (The second call is a tail call, but the function as a whole is not tail-recursive.)"},
        ],
    },
    {
        "question": "9. Backward substitution for $T(n) = T(n-1) + 2$, $T(0) = 5$. Which general form after $i$ substitutions, and which final answer, are correct?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$T(n) = T(n-i) + 2i$, so $T(n) = 2n + 5$", "correct": True,
             "feedback": "Correct. With $i = n$: $T(n) = T(0) + 2n = 2n + 5$. Check: $T(1) = 7 = T(0) + 2$."},
            {"answer": "$T(n) = T(n-i) + 2i$, so $T(n) = 2n$", "correct": False,
             "feedback": "Incorrect. You forgot the value of the initial condition: $T(0) = 5$, not $0$."},
            {"answer": "$T(n) = 2^i T(n-i)$, so $T(n) = 5 \\cdot 2^n$", "correct": False,
             "feedback": "Incorrect. The 2 is added, not multiplied; multiplication would require $T(n) = 2T(n-1)$."},
            {"answer": "$T(n) = T(n-i) + 2$, so $T(n) = 7$", "correct": False,
             "feedback": "Incorrect. Each substitution adds another 2, so after $i$ steps the constant is $2i$."},
        ],
    },
    {
        "question": "10. Why do we solve $A(n) = A(\\lfloor n/2 \\rfloor) + 1$ first for $n = 2^k$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "For $n = 2^k$ every $n/2$ is an integer, so the floors disappear; the smoothness rule then extends the order of growth to all $n$", "correct": True,
             "feedback": "Correct. This is the standard trick of Levitin's textbook (Appendix B)."},
            {"answer": "Because the algorithm only works for powers of two", "correct": False,
             "feedback": "Incorrect. BinRec works for every positive integer; powers of two only make the algebra simple."},
            {"answer": "Because for other $n$ the order of growth is different", "correct": False,
             "feedback": "Incorrect. For this kind of recurrence the order of growth is the same for all $n$ (here $\\Theta(\\log n)$); only the exact formula gets floors."},
            {"answer": "Because computers store numbers in binary", "correct": False,
             "feedback": "Incorrect. The reason is mathematical convenience, not hardware."},
        ],
    },
]
display_quiz(quiz_m2)
```

Scored 8 or more? Go on to the [problems](07_problems.md).
