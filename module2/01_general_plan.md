---
short_title: 1 · General plan
---

# The General Plan for Recursive Algorithms

## Why we need a new tool

Look at the recursive factorial:

```text
ALGORITHM F(n)
    //Computes n! recursively
    //Input: A nonnegative integer n
    //Output: The value of n!
    if n = 0 return 1
    else return F(n - 1) * n
```

There is no loop to turn into a sum. But we can still say: *to compute $F(n)$, the algorithm first
computes $F(n-1)$ and then does one multiplication*. If $M(n)$ is the number of multiplications for input
$n$, this sentence becomes an equation:

$$
M(n) = M(n-1) + 1 .
$$

An equation that expresses $M(n)$ through values of $M$ at **smaller** arguments is called a
**recurrence relation** (or simply a **recurrence**).

A recurrence alone does not determine $M(n)$: $M(n) = n$, $M(n) = n + 5$ and $M(n) = n - 3$ all satisfy
$M(n) = M(n-1) + 1$. We also need the value at the point where the recursion stops — the **initial
condition**. For the factorial, $F(0)$ returns 1 without multiplying, so

$$
M(0) = 0 .
$$

The recurrence together with the initial condition determines $M(n)$ uniquely: $M(n) = n$.

## The five steps

The plan is the same as in Module 1 except for steps 4 and 5.

```{mermaid}
flowchart TD
    S1["<b>Step 1 · Input size</b><br/>What is n?"] --> S2["<b>Step 2 · Basic operation</b><br/>What do we count?"]
    S2 --> S3{"<b>Step 3 · Cases</b><br/>Can the count differ for<br/>inputs of the same size?"}
    S3 -- "no" --> S4["<b>Step 4 · Recurrence</b><br/>M(n) = ... M(smaller) ...<br/>+ initial condition"]
    S3 -- "yes" --> S3b["Worst / best / average<br/>case separately"]
    S3b --> S4
    S4 --> S5["<b>Step 5 · Solve</b><br/>backward substitutions,<br/>then verify"]
```

1. **Input size.** Decide on the parameter $n$.
2. **Basic operation.** Identify it, as before.
3. **Cases.** Check whether the count can differ for inputs of the same size. If yes, analyze the worst,
   best (and average) case separately.
4. **Recurrence.** Set up a recurrence relation **with an initial condition** for the number of times the
   basic operation is executed.
5. **Solve.** Solve the recurrence, or at least find the order of growth of its solution.

## How to write the recurrence (Step 4)

Read the algorithm and ask two questions.

**Question 1: what happens in the general case?** Count

- the basic operations done by the **recursive calls**: one term $M(\text{smaller size})$ **per call**;
- plus the basic operations done **directly** in this call (outside the recursive calls).

$$
M(n) = \underbrace{M(\ldots) + M(\ldots) + \dots}_{\text{one term per recursive call}} + \underbrace{(\text{work in this call})}_{\text{not inside the calls}} .
$$

**Question 2: what happens in the stopping case?** Look at the line that ends the recursion
(`if n = 0 return 1`) and count the basic operations it performs. That number is the **initial
condition**.

| Algorithm | Recursive calls | Work in this call | Recurrence | Initial condition |
|---|---|---|---|---|
| Factorial $F(n)$ | $F(n-1)$ | 1 multiplication | $M(n) = M(n-1) + 1$ | $M(0) = 0$ |
| Tower of Hanoi | 2 calls on $n-1$ disks | 1 move | $M(n) = 2M(n-1) + 1$ | $M(1) = 1$ |
| BinRec$(n)$ | BinRec$(\lfloor n/2 \rfloor)$ | 1 addition | $A(n) = A(\lfloor n/2 \rfloor) + 1$ | $A(1) = 0$ |

:::{warning} Typical mistakes in Step 4
1. **Forgetting the initial condition**, or taking it from the wrong stopping case. Check: *with which
   value of $n$ does the algorithm stop, and how many basic operations does it do there?*
2. **Counting the work of the recursive calls twice** — for example, adding the multiplications done
   inside $F(n-1)$ to the "work in this call". Everything done inside a call is already in its term
   $M(n-1)$.
3. **Writing one term for two calls.** Two recursive calls on size $n-1$ give $2M(n-1)$, not $M(n-1)$.
:::

## Input size vs. recursion depth

The **recursion depth** is the largest number of calls that are active at the same time (the longest
chain of calls). It is a different quantity from the input size and from the count of operations:

| Algorithm | Count | Depth |
|---|---|---|
| Factorial $F(n)$ | $n$ multiplications | $n + 1$ calls: $F(n), F(n-1), \dots, F(0)$ |
| BinRec$(n)$ | $\lfloor \log_2 n \rfloor$ additions | $\lfloor \log_2 n \rfloor + 1$ calls |
| Tower of Hanoi | $2^n - 1$ moves | $n$ calls |

Depth matters because every active call occupies memory on the **call stack**; see
[Recursion vs. iteration](05_recursion_vs_iteration.md).

Next: how to solve a recurrence — [Backward substitutions](02_backward_substitution.md).
