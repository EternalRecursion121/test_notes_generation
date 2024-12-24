# Chapter 3 Quick Reference

Okay, here's a comprehensive Quick Reference and Common Patterns/Techniques section for Chapter 3, based on the provided text.

## Quick Reference

**Formulas and Results:**

*   **Gambler's Ruin Recurrence:**
    $$u_n = pu_{n+1} + qu_{n-1}$$ for $1 \le n \le M - 1$, where $u_n$ is the probability of bankruptcy with initial fortune $n$, and $p + q = 1$. Boundary conditions: $u_0 = 1$, $u_M = 0$.
*   **General $k^{th}$-Order Linear Recurrence Relation:**
    $$\sum_{j=0}^{k} a_j u_{n+j} = f(n)$$ where $a_0 \ne 0$ and $a_k \ne 0$.
*   **General Solution of a Linear Recurrence:**
    $$u_n = v_n + w_n$$ where $v_n$ is a particular solution to the non-homogeneous equation and $w_n$ is a general solution to the associated homogeneous equation.
*   **First-Order Linear Difference Equation:**
    $$u_{n+1} = au_n + b$$
*   **Solution to First-Order Linear Difference Equation ($a \ne 1$):**
    $$u_n = Aa^n + \frac{b}{1-a}$$
*   **Solution to First-Order Linear Difference Equation ($a = 1$):**
      $$u_n = A + bn$$
*   **First-Order Linear Difference Equation with Linear RHS:**
    $$u_{n+1} = au_n + bn$$
*   **Solution to First-Order Linear Difference Equation with Linear RHS ($a \ne 1$):**
    $$u_n = Aa^n + \frac{b}{1-a}n - \frac{b}{(1-a)^2}$$
*   **Second-Order Linear Difference Equation:**
    $$u_{n+2} + au_{n+1} + bu_n = f(n)$$
*   **Auxiliary Equation:**
    $$\lambda^2 + a\lambda + b = 0$$
*   **Homogeneous Solution with Distinct Roots $\lambda_1, \lambda_2$:**
    $$w_n = A_1 \lambda_1^n + A_2 \lambda_2^n$$
*   **Homogeneous Solution with Repeated Root $\lambda$:**
    $$w_n = (A + Bn) \lambda^n$$
*   **Gambler's Ruin Solution (p!=1/2):**
    $$u_n = \frac{1 - (q/p)^n}{1-(q/p)^M}$$ where q = 1-p
* **Gambler's Ruin Solution (p=1/2):**
 $$u_n = 1 - \frac{n}{M}$$
*  **Gambler's Ruin Expected Number of Steps ($p \neq q$):**
  $$e_n = A + B(\frac{q}{p})^n-\frac{n}{p-q}$$
  where $$A=\frac{\frac{M}{p-q}(\frac{q}{p})^M}{1-(\frac{q}{p})^M}, B = \frac{-\frac{M}{p-q}}{1-(\frac{q}{p})^M}$$
  and with boundary conditions $$e_0 = e_M = 0$$
* **Gambler's Ruin Expected Number of Steps ($p=q=1/2$):**
    $$e_n = n(M-n)$$
*   **Probability of Hitting 0 in Infinite Random Walk:**
      $$u_n = \begin{cases} \left(\frac{q}{p}\right)^n & \text{if } p > q \\ 1 & \text{if } p \le q \end{cases}$$

**Definitions:**

*   **$k^{th}$-Order Linear Recurrence Relation:** A sequence $(u_n)_{n\ge 0}$ satisfying
    $$\sum_{j=0}^{k} a_j u_{n+j} = f(n)$$ where $a_0 \ne 0$, $a_k \ne 0$, and $a_0, ..., a_k$ are independent of $n$.
* **Increasing Sequence of Events:** A sequence of events $A_k$ such that $A_1 \subset A_2 \subset A_3 \subset \dots$.

**Theorems:**

*   **Theorem 3.3 (General Solution):** The general solution to a linear recurrence is the sum of a particular solution and the general solution to the associated homogeneous recurrence.
*   **Theorem 3.15 (Infinite Random Walk Hit Probability):** The probability that a random walk on $\mathbb{Z}$ starting from $n > 0$ ever hits $0$ is $(\frac{q}{p})^n$ if $p>q$ and $1$ if $p\leq q$.

**Key Relationships and Implications:**

*   **Homogeneous vs. Non-Homogeneous:** Solutions to non-homogeneous recurrences involve solving the associated homogeneous recurrence and finding a particular solution to the non-homogeneous part.
*   **Auxiliary Equation:** The roots of the auxiliary equation determine the form of the general solution to the homogeneous recurrence.
*   **Boundary Conditions:** Boundary conditions are essential for uniquely determining constants in general solutions.
* **Expected value recursion:** Recurrence relations can be derived for expected values using conditional expectations.
* **Limit of finite random walk:** The limit of the probabilities of a finite random walk hitting zero can be used to get probabilities of a random walk on an infinite line hitting zero.

**Important Special Cases:**

*   **$a = 1$ in first-order difference equation:** Requires special handling, where a constant particular solution does not work, and  $v_n = Cn$ should be used.
*   **Repeated roots in auxiliary equation:** Leads to a general homogeneous solution of the form  $w_n = (A+Bn)\lambda^n$.
*   **Gambler's Ruin with $p=1/2$:** Simplifies significantly, both for the probability of bankruptcy and for expected number of steps.
*   **Infinite Random Walk:** The behavior of an infinite random walk depends critically on the relationship between $p$ and $q$.

**Key Conditions and Assumptions:**

*   **Linearity:** Recurrences must be linear to apply the superposition principle.
*   **Constant Coefficients:** Coefficients $a_i$ in the linear recurrence are assumed to be constant.
*   **Independence:** In the gambler's ruin problem, plays are assumed to be independent.
*   **Boundary Conditions:** Solutions require specific boundary conditions to fix the constants.
*   **Random Walk Steps:** Random walk steps are assumed to be of size 1 (e.g.,  +1 or -1).

## Common Patterns and Techniques

**Key Proof Techniques:**

*   **Partition Theorem (Law of Total Probability):** Used for conditioning on the outcome of the first step to derive recurrence relations (e.g., in Gambler's ruin).
*   **Induction:** Implicitly used in showing the general solution formula for linear homogeneous recurrence relations.
*   **Superposition Principle:** The principle is used in linear systems to break down the problem into two parts, one for the homogenous case and another for the non-homogenous case.
*   **Guess and Check:**  Technique for finding particular solutions, especially by trying polynomials of the same degree as the non-homogeneous part of the equation.
*   **Limits:** Taking limits as in the case for the random walk on the infinite line.
*   **Equating coefficients:** Used to calculate values in recurrence relations containing polynomial forms.

**Common Problem-Solving Strategies:**

*   **Identify the type of equation:** Determine if the recurrence is linear, its order, whether it is homogeneous or non-homogeneous.
*   **Solve the homogeneous equation:** Find the roots of the auxiliary equation and construct the general homogeneous solution.
*   **Find a particular solution:** Use educated guesses based on the form of $f(n)$.
*   **Combine solutions:** Combine the particular solution and the homogeneous solution to get the general solution.
*   **Apply boundary conditions:** Solve for the unknown constants using the provided boundary or initial conditions.
*   **Consider special cases:**  Be mindful of conditions like $a = 1$, repeated roots, $p = q$.

**Important Connections:**

*   **Recurrence Relations and Difference Equations:** These are simply two names for the same thing.
*   **Differential Equations:** Analogies are drawn between linear recurrences and linear ordinary differential equations.
* **Random walks and the gambler's ruin:** This chapter uses the gambler's ruin problem as a motivating example for analyzing random walks.
*   **Linear Algebra:** Recurrences can be represented using matrix notation and solved using eigenvalues and eigenvectors (not covered here).

**Typical Applications of Theorems:**

*   **Gambler's Ruin:** Calculating the probability of ruin and expected duration.
*   **Random Walk Analysis:** Determining hitting probabilities and expected times.
*   **Mathematical Modeling:** Representing real-world scenarios with recursive relationships.
*   **Fibonacci Numbers:** Deriving explicit formula for the nth Fibonacci number.

This detailed breakdown should be a helpful quick reference for Chapter 3.
