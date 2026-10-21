---
short_title: 1 · General plan
---

# The General Plan

Every analysis in this module follows the same **five steps**. The plan is deliberately mechanical: its
value is that it forces you to make every decision explicitly, instead of "seeing" the answer and getting
it wrong.

```{mermaid}
flowchart TD
    S1["<b>Step 1 · Input size</b><br/>What is n?"] --> S2["<b>Step 2 · Basic operation</b><br/>What do we count?"]
    S2 --> S3{"<b>Step 3 · Cases</b><br/>Does the count depend<br/>only on n?"}
    S3 -- "yes" --> S4["<b>Step 4 · Sum</b><br/>Write C(n) as a sum"]
    S3 -- "no" --> S3b["Analyze worst, best<br/>(and average) case separately"]
    S3b --> S4
    S4 --> S5["<b>Step 5 · Solution</b><br/>Evaluate the sum,<br/>find the order of growth"]
```

## Step 1 · Choose the input size

Decide which parameter (or parameters) measure the size of the input.

- Array of $n$ elements → $n$.
- $n \times n$ matrix → usually the order $n$.
- $m \times n$ matrix → two parameters, $m$ and $n$.
- One number $n$ → strictly, the number of bits $b = \lfloor \log_2 n \rfloor + 1$.

:::{warning} Typical mistake
Using the **value** of a number as its size. An algorithm that loops from 1 to the value $n$ makes $n$
steps, which is **exponential** in the number of digits of $n$. See
[size vs. value](05_typical_mistakes.md#mistake-size-value).
:::

## Step 2 · Identify the basic operation

Find the operation that runs **most often**. It is almost always in the **innermost loop**. Typical
choices are key comparisons (searching, sorting) and multiplications (numerical algorithms).

How to check your choice: ask "is there an operation that runs more often than this one?" If the answer
is yes, choose that one instead.

:::{warning} Typical mistake
Counting an operation that runs only **sometimes**, such as the assignment inside an `if`. Its count
depends on the data and hides the real work. See
[wrong basic operation](05_typical_mistakes.md#mistake-basic-op).
:::

## Step 3 · Check whether the count depends only on $n$

Look for anything that can stop the loops early: `return`, `break`, a `while` condition that depends on
the data.

- **No early exit** → the count is the same for all inputs of size $n$. One formula $C(n)$ is enough.
- **Early exit possible** → the count differs between inputs of the same size. Analyze the **worst case**
  (and often the **best** and **average** cases) separately.

:::{warning} Typical mistake
Writing "the algorithm is $\Theta(n^2)$" when only the **worst case** is $\Theta(n^2)$ and the best case
is $\Theta(1)$. See [mixing up cases](05_typical_mistakes.md#mistake-cases).
:::

## Step 4 · Write a sum

Each loop becomes a sum; nested loops become nested sums.

| Pseudocode | Sum |
|---|---|
| `for i ← l to u do` *(body executes the operation once)* | $\displaystyle\sum_{i=l}^{u} 1$ |
| `for i ← 0 to n-1 do` `for j ← 0 to n-1 do` *op* | $\displaystyle\sum_{i=0}^{n-1}\sum_{j=0}^{n-1} 1$ |
| `for i ← 0 to n-2 do` `for j ← i+1 to n-1 do` *op* | $\displaystyle\sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1} 1$ |

The bounds of the sum are **exactly** the bounds of the loop. Copy them carefully.

## Step 5 · Evaluate the sum and find the order of growth

Evaluate nested sums **from the inside out** using the rules and formulas from
[Summation tools](02_summation_tools.md). Then drop constants and lower-order terms to get the order of
growth, and **say which case** it describes.

:::{note} A complete answer looks like this
"For the worst case, $C_{worst}(n) = \frac{n(n-1)}{2} \in \Theta(n^2)$; the best case is
$C_{best}(n) = 1 \in \Theta(1)$; therefore the algorithm is in $O(n^2)$."
:::

## A first tiny example

```text
ALGORITHM SumArray(A[0..n-1])
    //Returns the sum of the elements of A
    s ← 0
    for i ← 0 to n - 1 do
        s ← s + A[i]
    return s
```

1. **Input size:** $n$, the number of elements.
2. **Basic operation:** the addition `s + A[i]` (it is in the only loop).
3. **Cases:** there is no early exit, so the count depends only on $n$.
4. **Sum:** $C(n) = \sum_{i=0}^{n-1} 1$.
5. **Solution:** $C(n) = (n-1) - 0 + 1 = n \in \Theta(n)$.

Now we need tools for evaluating more interesting sums: [Summation tools](02_summation_tools.md).
