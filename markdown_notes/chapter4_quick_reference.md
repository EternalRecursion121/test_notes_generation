# Chapter 4 Quick Reference

Okay, here's a detailed Quick Reference section based on Chapter 4 of the provided text, along with a breakdown of common patterns and techniques:

## Quick Reference

**Definitions**

*   **Probability Generating Function (p.g.f.):** For a non-negative integer-valued random variable $X$, the p.g.f. is given by
    $$G_X(s) = E[s^X] = \sum_{k=0}^{\infty} s^k P(X=k)$$
    where $S = \{s \in \mathbb{R} : \sum_{k=0}^{\infty} |s|^kP(X=k) < \infty \}$.
*   **Extinction Probability (q):** In a branching process, $q$ is the probability that the population eventually dies out, $q = P(\bigcup_{n=1}^\infty \{X_n = 0\})$.

**Theorems**

*   **Uniqueness Theorem (Theorem 4.2):** The distribution of $X$ is uniquely determined by its probability generating function, $G_X$.
*   **Independence Theorem (Theorem 4.3):** If $X$ and $Y$ are independent, then $G_{X+Y}(s) = G_X(s)G_Y(s)$.
*   **Sum of Bernoulli (Theorem 4.4):** If $X_1, X_2, \dots, X_n$ are independent $Ber(p)$ random variables, then $Y = X_1 + \dots + X_n \sim Bin(n,p)$.
*   **Sum of Poissons (Theorem 4.5):** If $X_1, X_2, \dots, X_n$ are independent random variables with $X_i \sim Po(\lambda_i)$, then $\sum_{i=1}^{n} X_i \sim Po(\sum_{i=1}^{n} \lambda_i)$.
*   **Random Sum (Theorem 4.8):** Let $X_1, X_2, ...$ be i.i.d. non-negative integer-valued random variables with p.g.f. $G_X(s)$ and $N$ be another non-negative integer-valued random variable, independent of $X_1, X_2, ...$ with p.g.f. $G_N(s)$. Then the p.g.f. of $\sum_{i=1}^N X_i$ is $G_N(G_X(s))$.
*   **Extinction Probability Characterization (Theorem 4.14):** The extinction probability $q$ is the smallest non-negative solution to $x = G(x)$, where $G(s)$ is the p.g.f. of the offspring distribution.
*   **Extinction Theorem (Theorem 4.15):** Let $\mu$ be the mean number of offspring of a single individual, then if $\mu \leq 1$ the extinction probability $q = 1$ and if $\mu > 1$, then the extinction probability is $q < 1$.

**Key Formulas and Results**

*   **Derivatives of p.g.f.:**
    $$ G'_X(s) = \sum_{k=1}^\infty k s^{k-1} P(X=k) = E[Xs^{X-1}]$$
    $$ G'_X(1) = E[X]$$
    $$ G''_X(1) = E[X(X-1)] = E[X^2] - E[X]$$
    $$ var(X) = G''_X(1) + G'_X(1) - (G'_X(1))^2 $$
*   **p.g.f. of Common Distributions:**
    *   Bernoulli: $G_X(s) = q + ps$
    *   Binomial: $G_X(s) = (1-p+ps)^n$
    *   Poisson: $G_X(s) = e^{\lambda(s-1)}$
    *   Geometric: $G_X(s) = \frac{ps}{1-(1-p)s}$
*   **p.g.f. of Branching Process (Theorem 4.11):**
    $$G_{n+1}(s) = G_n(G(s)) = G(G(...G(s)...)) = G(G_n(s))$$ where the composition has $(n+1)$ terms
*   **Mean of Branching Process (Corollary 4.12):**  If the mean number of offspring is $\mu$, then the mean population in the $n^{th}$ generation is $E[X_n] = \mu^n$.
*   **Extinction Probability Equation:**
    $$q = \sum_{k=0}^{\infty} q^k p(k) = G(q)$$

**Key Relationships and Implications**

*   **P.g.f. uniquely identifies the distribution:** If two random variables have the same p.g.f., they must have the same distribution.
*   **Independent random variables:** The p.g.f. of the sum of independent random variables is the product of their individual p.g.f.'s.
*   **Branching processes and offspring distribution:** The mean number of offspring in a single generation determines whether extinction is certain or possible.
*   **Connection between Random Sums and p.g.f.'s:** Random sums can be easily analyzed using the p.g.f. of the random variables that are being summed and the p.g.f. of the number of summands.

**Important Special Cases**

*   **$G_X(1) = 1$**
*   **Random sums with $N \sim Po(\lambda)$ and $X_i \sim Ber(p)$ :** Results in a $Po(\lambda p)$ distribution.

**Key Conditions and Assumptions**

*   The random variables considered are non-negative integer-valued.
*   Independence is a key assumption in theorems 4.3, 4.4, 4.5, and 4.8, and in the branching process.
*   In branching processes, the offspring distribution is identical and independent for all individuals.

## Common Patterns and Techniques

**Key Proof Techniques**

*   **Induction:** Used to show the recursive relationship for branching process generation size p.g.f. (Theorem 4.11) and the mean (Corollary 4.12).
*   **Law of Total Probability:** Used to find the p.g.f of random sums (Theorem 4.8), calculate expectation of the number of red balls chosen before a blue ball is chosen (Example 4.7) and to demonstrate the extinction probability (Theorem 4.14).
*   **Differentiating p.g.f.s:** Used to calculate moments such as $E[X]$, $E[X(X-1)]$ and hence the variance of $X$.
*   **Term-by-term differentiation of power series:** Used to derive moments from p.g.f.s, requiring the radius of convergence to be strictly greater than the value of $x$ where the derivatives are being evaluated.
*   **Properties of power series:** Used in the proof of the uniqueness theorem.
*   **Convexity:** Used to determine whether the extinction probability is 1 (for the case $\mu \leq 1$) and less than 1 (when $\mu > 1$)

**Common Problem-Solving Strategies**

*   **Identify the underlying random variables:** Determine what kind of random variables are involved in a problem and their distributions.
*   **Apply the independence properties:** If applicable, the p.g.f. of a sum of independent random variables is the product of the individual p.g.f.'s.
*   **Use p.g.f.'s to calculate expectations and variances:** Find the first and second derivatives of the p.g.f., then evaluate at s=1 to get expectations and variances.
*   **Find a relationship with one of the common distributions:** If the resulting p.g.f. matches a well-known distribution then you are done.
*   **Work with generating function:** Use the chain rule to find p.g.f.'s of complex random variables based on p.g.f.'s of simpler ones.
*   **Find a relationship via conditioning:**  Use conditional arguments to define relationships between variables.

**Important Connections between Concepts**

*   **P.g.f.'s as a convenient way to encode probabilities:** A p.g.f. encodes all information about a distribution in a single function.
*   **Calculus and p.g.f.s:** Derivatives are used to extract moments, so knowledge of calculus is used to analyze these.
*   **Branching Processes and their extinction:** The mean offspring number determines if extinction is inevitable.
*   **Random sums and p.g.f.s:** P.g.f.s are powerful tools to work with random sums.

**Typical Applications of Theorems**

*   **Verifying distribution identities:** Sums of random variables, often involving Bernoulli or Poisson variables, can have their resulting distributions calculated efficiently using Theorem 4.3 and 4.5.
*   **Calculating moments of distributions:** P.g.f.'s are frequently used to calculate the mean and variance of a random variable.
*   **Analyzing branching processes:** P.g.f.s allow determination of extinction probability and expected size of population in branching processes.
*   **Modeling random sums:** The p.g.f. of a random sum can be derived from the p.g.f.'s of the summands and the random number of summands, which can help with modelling complex systems.

This comprehensive overview should serve as a good Quick Reference for Chapter 4, providing definitions, theorems, formulas, key concepts, common techniques, and applications.  Let me know if you have any other questions or if I can clarify any of the above!
