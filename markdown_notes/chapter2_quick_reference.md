# Chapter 2 Quick Reference

Okay, here's a quick reference and analysis of Chapter 2, "Discrete Random Variables", as described, using proper LaTeX syntax.

## Quick Reference

### Definitions

*   **Discrete Random Variable:** A function $X: \Omega \rightarrow \mathbb{R}$ such that
    (a)  $\{ \omega \in \Omega: X(\omega) = x \} \in \mathcal{F}$ for each $x \in \mathbb{R}$
    (b) $ImX := X(\Omega) = \{X(\omega) : \omega \in \Omega\}$ is a finite or countable subset of $\mathbb{R}$.

*  **Probability Mass Function (p.m.f.):**  For a discrete r.v. $X$, the function $p_X: \mathbb{R} \rightarrow [0,1]$ defined by $p_X(x) = P(X = x)$.

*   **Expectation (Expected Value or Mean):**  For a discrete r.v. $X$,
    $E[X] = \sum_{x \in ImX} xP(X=x)$, provided $\sum_{x \in ImX} |x|P(X=x) < \infty$.

*   **Variance:** For a discrete r.v. $X$,
    $var(X) = E[(X - E[X])^2]$, provided this exists.

* **Conditional Probability Mass Function:**  If $B$ is an event such that $P(B)>0$, then
$P(X=x | B) = \frac{P(\{X=x\}\cap B)}{P(B)}$ for $x\in \mathbb{R}$.

*   **Conditional Expectation:**  Given an event B such that $P(B) > 0$,
    $E[X|B] = \sum_{x} xP(X = x|B)$, provided the sum converges absolutely.

* **Joint Probability Mass Function:** For discrete r.v.s $X$ and $Y$,
$p_{X,Y}(x,y) = P(\{X=x\} \cap \{Y=y\}), \quad x,y\in \mathbb{R}$.

*   **Independent Random Variables:** Discrete random variables $X$ and $Y$ are independent if
    $P(X=x, Y=y) = P(X=x)P(Y=y)$ for all $x,y \in \mathbb{R}$.
    Equivalently, $p_{X,Y}(x,y) = p_X(x)p_Y(y)$.
    
*   **Covariance:** For random variables $X$ and $Y$,
    $$cov(X, Y) = E[(X - E[X])(Y - E[Y])]$$

* **Multivariate Probability Mass Function:** For random variables $X_1, X_2, ..., X_n$,
    $$p_{X_1, X_2, ..., X_n}(x_1, x_2, ..., x_n) = P(X_1 = x_1, X_2 = x_2, ..., X_n = x_n),$$
    for $x_1, x_2, ..., x_n \in \mathbb{R}$.

* **Independent Random Variables Family:**  A family $\{X_i: i \in I\}$ of discrete random variables is independent if for all finite sets $J \subseteq I$ and all collections $\{A_i : i \in J\}$ of subsets of $\mathbb{R}$,
 $$P\left(\bigcap_{i \in J} \{ X_i \in A_i\}\right) = \prod_{i \in J} P(X_i \in A_i).$$

* **Independent and Identically Distributed (i.i.d.) Random Variables:**  Random variables $X_1, X_2, ...$ are i.i.d. if they are independent and have the same distribution.

### Key Formulas and Results

*   **P.M.F. Summation:** $\sum_{x \in ImX} p_X(x) = 1$
*   **P.M.F. for Indicator Function:**  If $X = 1_A$, then
    $p_X(0) = P(A^c) = 1 - P(A)$ and $p_X(1) = P(A)$

*   **Bernoulli Distribution:**  $P(X=0) = 1-p$, $P(X=1) = p$, where $X \sim Ber(p)$.

*   **Binomial Distribution:**  $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$, where $X \sim Bin(n,p)$, $k=0, 1, ..., n$

*   **Geometric Distribution:** $P(X=k) = p(1-p)^{k-1}$, where $X \sim Geom(p), \ k = 1, 2, ...$

* **Alternative Geometric Distribution (number of failures):**  $P(Y=k) = p(1-p)^{k}, k=0, 1, 2, ...$ where Y = X - 1, and X is defined above.

*   **Poisson Distribution:**  $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$, where $X \sim Po(\lambda)$, $k=0, 1, 2, ...$

* **Expectation of $h(X)$:** $E[h(X)] = \sum_{x \in ImX} h(x) P(X = x)$, provided $\sum_{x \in ImX} |h(x)|P(X=x)<\infty$.

*   **Variance Formula:**  $var(X) = E[X^2] - (E[X])^2$

*   **Variance of Linear Transformation:** $var(aX + b) = a^2var(X)$

* **Conditional Expectation by Law of Total Probability:** If {B1, B2, ...} is a partition of $\Omega$ such that $P(B_i)>0$, then
$E[X] = \sum_i E[X|B_i]P(B_i)$.

* **Conditional Expectation Formula:** $$E[Y|X=x]=\sum_{y}yP(Y=y|X=x)$$

*   **Joint Probability Mass Function Summation:**
    $\sum_{x}\sum_{y} p_{X,Y}(x, y) = 1$

*   **Marginal Distributions:**
    $p_X(x) = \sum_{y} p_{X,Y}(x,y)$ and $p_Y(y) = \sum_{x} p_{X,Y}(x,y)$

*   **Conditional Probability Mass Function:**  $P(Y=y|X=x) = \frac{p_{X,Y}(x,y)}{p_X(x)}$

* **Expectation of $h(X,Y)$:**  $E[h(X,Y)] = \sum_x \sum_y h(x,y)p_{X,Y}(x,y)$, provided $\sum_{x,y}|h(x,y)|p_{X,Y}(x,y)<\infty$.

*   **Linearity of Expectation:** $E[aX+bY] = aE[X] + bE[Y]$

*  **Expectation of Independent Random Variables:** If $X$ and $Y$ are independent, then $E[XY] = E[X]E[Y]$

* **Variance of Independent Random Variables:** If $X$ and $Y$ are independent, then $var(X+Y)=var(X)+var(Y)$.

* **Covariance Formula:** $$cov(X,Y) = E[XY]-E[X]E[Y].$$

*  **Variance of the Sum:** $$var(X+Y) = var(X)+var(Y)+2cov(X,Y).$$

### Theorems

* **Theorem 2.8** If $h:\mathbb{R} \to \mathbb{R}$, then
    $$E[h(X)]=\sum_{x \in ImX}h(x)P(X=x)$$

*   **Theorem 2.10:** Let $X$ be a discrete r.v. such that $E[X]$ exists.
    (a) If $X$ is non-negative, then $E[X] \geq 0$.
    (b) If $a, b \in \mathbb{R}$, then $E[aX+b] = aE[X] + b$.

*   **Theorem 2.12:** If $X$ is a discrete r.v. with variance and $a, b \in \mathbb{R}$, then $var(aX + b) = a^2 var(X)$.

* **Theorem 2.14 (Partition Theorem for Expectations):** If $\{B_1,B_2,...\}$ is a partition of $\Omega$ such that $P(B_i)>0$, then $E[X] = \sum_i E[X|B_i]P(B_i)$.

*  **Theorem 2.21** If X and Y are discrete random variables and a,b are constants, then
$$E[aX+bY]=aE[X]+bE[Y].$$

*   **Theorem 2.23:** If $X$ and $Y$ are independent discrete r.v.s whose expectations exist, then $E[XY]=E[X]E[Y]$.

### Key Relationships and Implications

*   If $x \notin ImX$, then $p_X(x) = 0$.

*   $E[X]$ represents the "average value" of $X$.

*   $var(X)$ measures how spread out the distribution of $X$ is.

*   Independence implies zero covariance, but zero covariance doesn't necessarily imply independence.

### Important Special Cases

*   Indicator function $1_A$ is a Bernoulli random variable with $p = P(A)$.
*   If $X$ is a constant, $var(X) = 0$.
* The expectation of a Poisson random variable, $E[X]$ is its parameter, $\lambda$.

### Key Conditions and Assumptions
*   For $E[X]$ to exist, we require absolute convergence: $\sum_{x \in ImX} |x|P(X=x) < \infty$.
*   For $E[h(X)]$ to exist, we need $\sum_{x \in ImX} |h(x)|P(X=x) < \infty$.
*   For $E[XY]$ to exist, we need absolute convergence of $\sum_{x,y} |xy|P(X=x,Y=y)$

## Common Patterns and Techniques

### Key Proof Techniques Used
* **Absolute Convergence:** The requirement of absolute convergence is used when showing the sum is independent of the order of summation.
*   **Expansion and Simplification:**  Expanding terms, using the definition of $E[X]$, and using properties of summation.
*   **Law of Total Probability:** Used for conditional expectation (Theorem 2.14) and for the example involving repeated coin flips.
*   **Decomposition:**  Rewriting sums based on partitions or conditioning events.
* **Independence:** Used to separate terms in calculations involving expectations and variances when the variables are independent.
* **Linearity of Expectation:** Used to simplify expectations of sums of random variables, even when they're not independent.

### Common Problem-Solving Strategies
*   **Use Definitions:** Many proofs start directly from definitions of expectation, variance, independence, etc.
*   **Break Down Complex Random Variables** into simpler components, like sums of indicator random variables.
*   **Conditioning:** When analyzing random variables on sequential events.
*  **Linearity:** To simplify the calculation of expectation
* **Marginal Distributions:** To calculate expected values and variances by reducing joint distributions to simpler single-variable ones.

### Important Connections Between Concepts
*   **Expectation and Variance:** Variance uses expectation in its definition.
*   **Independence and Zero Covariance:** Independence implies zero covariance, but the reverse is not true. This demonstrates a subtle difference between non-correlation and independence.
*  **Independence and Expectation:** If X and Y are independent $E[XY]=E[X]E[Y]$
*  **Variance and Covariance:** Variance of the sum is equal to the sum of variances plus twice the covariance.
*   **Marginal and Joint Distributions:** Marginal distributions are derived from joint distributions by summing over the values of the other variable.
* **Indicator Functions:** Serve as a good building block to prove properties of probability mass functions.

### Typical Applications of Theorems
*   **Linearity of Expectation:** Simplifies finding the expectation of sums of random variables, such as the total number of loops in the spaghetti example.
*   **Partition Theorem:** Useful when events or outcomes have a complex structure, allowing calculations of expectation by breaking into simple cases.
*   **Independence:** Simplifies many calculations of expectation and variance when r.v.'s are independent, which is a frequent assumption in probability models.
*   **Conditional Expectation:** Used to analyze sequential processes and to simplify calculations of expected values.

I have tried to make this comprehensive. Please let me know if you have any more questions.
