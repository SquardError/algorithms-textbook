---
short_title: Glossary
---

# Glossary

Key terms in alphabetical order. The section in brackets is where the term is introduced.

:::{glossary}
Accumulator
: An extra parameter that carries a partial result through recursive calls, e.g. `FactTail(n, acc)`. Used to
  make a function tail-recursive. [Module 2 · Recursion vs. iteration]

Average case
: The expected number of basic operations over random inputs of size $n$, $C_{avg}(n)$. Requires an explicit
  probability model of the inputs. [Module 1 · Average case]

Backward substitutions
: A method of solving a recurrence: substitute the recurrence into itself repeatedly, find the general form
  after $i$ steps, choose $i$ to reach the initial condition. [Module 2 · Backward substitutions]

Basic operation
: The operation that contributes most to the running time, usually in the innermost loop; the algorithm's
  efficiency is measured by counting it. [Introduction]

Best case
: The smallest number of basic operations over all inputs of a fixed size $n$, $C_{best}(n)$. [Introduction]

Big-Omega, $\Omega$
: $t(n) \in \Omega(g(n))$ if $t(n) \ge c\,g(n)$ for some $c > 0$ and all $n \ge n_0$: $t$ grows at least as fast
  as $g$. [Introduction]

Big-Oh, $O$
: $t(n) \in O(g(n))$ if $t(n) \le c\,g(n)$ for some $c > 0$ and all $n \ge n_0$: $t$ grows no faster than $g$.
  [Introduction]

Big-Theta, $\Theta$
: $t(n) \in \Theta(g(n))$ if $t(n)$ is both in $O(g(n))$ and in $\Omega(g(n))$: $t$ and $g$ grow at the same rate.
  [Introduction]

Call stack
: The memory area that holds a stack frame for every active (unfinished) function call.
  [Module 2 · Recursion vs. iteration]

Closed form
: A formula for $C(n)$ or $M(n)$ without sums or references to $M$ at smaller arguments, e.g. $\frac{n(n-1)}{2}$.
  [Module 1 · Summation tools]

Dependent bound
: A loop bound that depends on the index of an outer loop, e.g. `for j ← 1 to i`. [Module 1 · Worked examples]

Early exit (early termination)
: A `return` or `break` that can stop a loop before it ends; it makes the count depend on the input.
  [Module 1 · General plan]

Empirical analysis
: Checking an analysis by running the algorithm and counting operations (or measuring time) for many input
  sizes. [Module 1 · Empirical verification]

Geometric series
: A sum $\sum_{i=0}^{n} a^i = \frac{a^{n+1}-1}{a-1}$ ($a \ne 1$); for $a = 2$ it equals $2^{n+1} - 1$.
  [Module 1 · Summation tools]

Golden ratio, $\varphi$
: $\varphi = \frac{1+\sqrt5}{2} \approx 1.618$; the Fibonacci numbers grow like $\varphi^n$.
  [Module 2 · Fibonacci warning]

Initial condition
: The value of the count in the stopping case of a recursive algorithm, e.g. $M(0) = 0$. Together with the
  recurrence it determines the solution uniquely. [Module 2 · General plan]

Input size
: A parameter $n$ measuring the size of the input: number of elements, order of a matrix, or number of bits of
  a number. [Introduction]

Mathematical induction
: A proof method: prove the base case, then prove that the statement for $n - 1$ implies the statement for $n$.
  [Module 2 · Backward substitutions]

Memoization
: Storing the results of solved subproblems in a table so that each one is computed only once.
  [Module 2 · Fibonacci warning]

Multiplicative loop
: A loop whose counter is multiplied or divided by a constant (`i ← 2i`, `i ← ⌊i/2⌋`); it runs $\Theta(\log n)$
  times. [Module 1 · Worked examples]

Nonrecursive algorithm
: An algorithm that does not call itself; it consists of loops, conditions and assignments. [Module 1]

Order of growth
: The behavior of a count for large $n$, ignoring constant factors and lower-order terms, e.g. $\Theta(n^2)$.
  [Introduction]

Overlapping subproblems
: The situation where a recursive algorithm solves the same subproblem many times, e.g. naive Fibonacci.
  [Module 2 · Fibonacci warning]

Recurrence relation
: An equation that expresses $M(n)$ through values of $M$ at smaller arguments, e.g. $M(n) = 2M(n-1) + 1$.
  [Module 2 · General plan]

Recursion depth
: The largest number of simultaneously active calls of a recursive algorithm; it determines the stack memory.
  [Module 2 · General plan]

Recursion tree
: A tree whose nodes are the calls of a recursive algorithm; summing the work of all nodes gives the count.
  [Module 2 · Worked examples]

Recursive algorithm
: An algorithm that solves a problem by calling itself on smaller inputs. [Module 2]

Smoothness rule
: A theorem (Levitin, Appendix B) that allows extending an order of growth found for $n = 2^k$ to all $n$, for
  eventually nondecreasing solutions and smooth growth functions. [Module 2 · Backward substitutions]

Stack frame
: The memory record of one active function call: parameters, local variables, return address.
  [Module 2 · Recursion vs. iteration]

Summation ($\Sigma$) notation
: $\sum_{i=l}^{u} a_i = a_l + a_{l+1} + \dots + a_u$; $i$ is the index, $l$ and $u$ are the bounds.
  [Module 1 · Summation tools]

Tail recursion
: Recursion in which the recursive call is the last action of the function; it can be replaced by a loop.
  [Module 2 · Recursion vs. iteration]

Worst case
: The largest number of basic operations over all inputs of a fixed size $n$, $C_{worst}(n)$. [Introduction]
:::
