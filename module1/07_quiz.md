---
short_title: 7 · Quiz
kernelspec:
  name: python3
  display_name: Python 3
---

# Module 1 Quiz

Ten questions on terms, the choice of the basic operation and orders of growth. Click an answer: it
turns green or red and an explanation appears. You can try again as many times as you like.

:::{tip}
Have a pencil ready — some questions need a quick calculation. The
[cheat sheet](09_summary_cheatsheet.md) contains every formula you need.
:::

```{code-cell} python
:tags: [remove-input]
from jupyterquiz import display_quiz

quiz_m1 = [
    {
        "question": "1. What is the basic operation of an algorithm?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The operation that contributes most to the total running time, usually in the innermost loop",
             "correct": True,
             "feedback": "Correct. Counting this one operation gives the order of growth of the whole running time."},
            {"answer": "The first operation of the algorithm", "correct": False,
             "feedback": "Incorrect. The first operation usually runs only once and says nothing about the total work."},
            {"answer": "The most expensive single operation, even if it runs only once", "correct": False,
             "feedback": "Incorrect. What matters is the total contribution: cost times number of executions. An operation that runs once is negligible for large n."},
            {"answer": "Any operation; the choice never affects the analysis", "correct": False,
             "feedback": "Incorrect. A bad choice (e.g. an assignment inside an if) can make the count depend on the data or hide the dominant term."},
        ],
    },
    {
        "question": "2. Which operation should be chosen as the basic operation in this fragment?",
        "type": "multiple_choice",
        "code": "for i ← 0 to n - 2 do\n    for j ← 0 to n - 2 - i do\n        if A[j + 1] < A[j]\n            swap A[j] and A[j + 1]",
        "answers": [
            {"answer": "The comparison A[j + 1] < A[j]", "correct": True,
             "feedback": "Correct. It runs on every iteration of the inner loop, for every input."},
            {"answer": "The swap", "correct": False,
             "feedback": "Incorrect. The swap runs only when the condition is true: never for a sorted array. Its count depends on the data."},
            {"answer": "The assignment i ← i + 1 of the outer loop", "correct": False,
             "feedback": "Incorrect. It runs only n - 1 times, far fewer than the inner-loop operations."},
            {"answer": "Computing n - 2", "correct": False,
             "feedback": "Incorrect. This is bookkeeping that does not grow with the work of the loop body."},
        ],
    },
    {
        "question": "3. What is $\\displaystyle\\sum_{i=3}^{n} 1$ (for $n \\ge 2$)?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$n - 2$", "correct": True,
             "feedback": "Correct. The number of terms is $u - l + 1 = n - 3 + 1 = n - 2$."},
            {"answer": "$n - 3$", "correct": False,
             "feedback": "Incorrect. This is the classic off-by-one error: you forgot the $+1$ in $u - l + 1$."},
            {"answer": "$n$", "correct": False,
             "feedback": "Incorrect. The sum starts at $i = 3$, not at $i = 1$, so the terms for $i = 1, 2$ are missing."},
            {"answer": "$n - 4$", "correct": False,
             "feedback": "Incorrect. Check with $n = 5$: the terms are $i = 3, 4, 5$, that is 3 terms, and $n - 2 = 3$."},
        ],
    },
    {
        "question": "4. What is the order of growth of $\\displaystyle\\sum_{i=1}^{n} i^3$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "$\\Theta(n^4)$", "correct": True,
             "feedback": "Correct. In general $\\sum_{i=1}^{n} i^k \\in \\Theta(n^{k+1})$; here $k = 3$."},
            {"answer": "$\\Theta(n^3)$", "correct": False,
             "feedback": "Incorrect. Summing $n$ terms of size up to $n^3$ adds one more power of $n$."},
            {"answer": "$\\Theta(3^n)$", "correct": False,
             "feedback": "Incorrect. The exponent is fixed ($i^3$), so the sum is polynomial, not exponential."},
            {"answer": "$\\Theta(n^2)$", "correct": False,
             "feedback": "Incorrect. That is the order of $\\sum i$ ($k = 1$), not $\\sum i^3$."},
        ],
    },
    {
        "question": "5. How many times (asymptotically) does this loop run?",
        "type": "multiple_choice",
        "code": "i ← n\nwhile i > 1 do\n    i ← ⌊i / 3⌋",
        "answers": [
            {"answer": "$\\Theta(\\log n)$", "correct": True,
             "feedback": "Correct. Dividing by 3 each time reaches 1 after about $\\log_3 n$ steps, and the base of the logarithm does not matter for $\\Theta$."},
            {"answer": "$\\Theta(n/3)$, i.e. $\\Theta(n)$", "correct": False,
             "feedback": "Incorrect. That would be the answer for i ← i - 3. Here the counter is divided, not decreased by a constant."},
            {"answer": "$\\Theta(\\log_3 n)$, which grows strictly slower than $\\Theta(\\log_2 n)$", "correct": False,
             "feedback": "Incorrect. $\\log_3 n = \\log_2 n / \\log_2 3$: the two differ only by a constant factor, so they are the same $\\Theta$ class."},
            {"answer": "$\\Theta(1)$", "correct": False,
             "feedback": "Incorrect. The number of iterations grows with $n$: for $n = 3^{10}$ there are 10 iterations."},
        ],
    },
    {
        "question": "6. What is the order of growth of the number of executions of op?",
        "type": "multiple_choice",
        "code": "for i ← 1 to n do\n    for j ← 1 to 10 do\n        op",
        "answers": [
            {"answer": "$\\Theta(n)$", "correct": True,
             "feedback": "Correct. The count is $10n$; the constant 10 does not affect the order of growth."},
            {"answer": "$\\Theta(n^2)$", "correct": False,
             "feedback": "Incorrect. Two nested loops do not automatically mean $n^2$: the inner loop runs a constant 10 times."},
            {"answer": "$\\Theta(10^n)$", "correct": False,
             "feedback": "Incorrect. The count is $10 \\cdot n$, not $10^n$."},
            {"answer": "$\\Theta(n \\log n)$", "correct": False,
             "feedback": "Incorrect. There is no multiplicative loop here."},
        ],
    },
    {
        "question": "7. An algorithm with an early exit makes $\\frac{n(n-1)}{2}$ comparisons in the worst case and 1 in the best case. Which statement is correct?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Its worst case is $\\Theta(n^2)$, and the algorithm is in $O(n^2)$", "correct": True,
             "feedback": "Correct. $\\Theta$ must be attached to a specific case, while $O(n^2)$ is an upper bound valid for all inputs."},
            {"answer": "The algorithm is $\\Theta(n^2)$ for all inputs", "correct": False,
             "feedback": "Incorrect. For inputs where it stops after 1 comparison the count is $\\Theta(1)$, not $\\Theta(n^2)$. This is the 'mixing up cases' mistake."},
            {"answer": "The algorithm is $\\Theta(1)$ because the best case is constant", "correct": False,
             "feedback": "Incorrect. The best case alone does not describe the algorithm; most inputs may need far more work."},
            {"answer": "Its average case is $\\frac{1}{2}\\left(1 + \\frac{n(n-1)}{2}\\right)$", "correct": False,
             "feedback": "Incorrect. The average case is not the mean of best and worst; it requires a probability model of the inputs."},
        ],
    },
    {
        "question": "8. An algorithm takes one positive integer $n$ and loops for $i$ from 1 to $n$. What is the correct input size?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The number of bits $b = \\lfloor \\log_2 n \\rfloor + 1$, so the loop is exponential in the input size", "correct": True,
             "feedback": "Correct. The input is written with $b$ bits; $n \\ge 2^{b-1}$ iterations is exponential in $b$."},
            {"answer": "The value $n$, so the algorithm is linear and efficient", "correct": False,
             "feedback": "Incorrect. This is the 'size vs. value' mistake: the loop is linear in the value but exponential in the length of the input."},
            {"answer": "The input size is always 1, because there is one number", "correct": False,
             "feedback": "Incorrect. The size of a number is how much space it takes to write it, which grows with $n$."},
            {"answer": "The number of loop iterations", "correct": False,
             "feedback": "Incorrect. The number of iterations is what we count; the input size is a property of the input."},
        ],
    },
    {
        "question": "9. What do you need before you can compute the average-case count $C_{avg}(n)$?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "An explicit assumption about the probability distribution of the inputs", "correct": True,
             "feedback": "Correct. For example: 'the search succeeds with probability $p$, and every position is equally likely'."},
            {"answer": "Only the best and worst cases; the average is their mean", "correct": False,
             "feedback": "Incorrect. The mean of best and worst is not an expected value; for sequential search it is right only when $p = 1$, and only by coincidence."},
            {"answer": "Nothing: the average case is a property of the algorithm alone", "correct": False,
             "feedback": "Incorrect. Different input distributions give different averages for the same algorithm."},
            {"answer": "A computer to measure the running time", "correct": False,
             "feedback": "Incorrect. The average case is computed mathematically; experiments can only check it."},
        ],
    },
    {
        "question": "10. What is the order of growth of the number of executions of op?",
        "type": "multiple_choice",
        "code": "for i ← 1 to n do\n    for j ← 1 to n do\n        for k ← 1 to i do\n            op",
        "answers": [
            {"answer": "$\\Theta(n^3)$", "correct": True,
             "feedback": "Correct. $\\sum_{i=1}^{n}\\sum_{j=1}^{n} i = n \\sum_{i=1}^{n} i = \\frac{n^2(n+1)}{2} \\in \\Theta(n^3)$."},
            {"answer": "$\\Theta(n^2)$", "correct": False,
             "feedback": "Incorrect. The innermost loop runs $i$ times, which is up to $n$; three nested loops of length up to $n$ give a cubic count."},
            {"answer": "$\\Theta(n^2 \\log n)$", "correct": False,
             "feedback": "Incorrect. There is no multiplicative loop; the innermost loop adds 1 to k."},
            {"answer": "$\\Theta(n^4)$", "correct": False,
             "feedback": "Incorrect. Write the sum: the innermost sum is $i$, the middle one multiplies by $n$, the outer one gives $n \\cdot \\frac{n(n+1)}{2}$."},
        ],
    },
]
display_quiz(quiz_m1)
```

Scored 8 or more? Go on to the [problems](08_problems.md). Otherwise reread the sections linked in the
explanations of the questions you missed.
