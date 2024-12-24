# Appendix Quick Reference

Okay, here's a breakdown of the appendix into a quick reference section, focusing on formulas, definitions, theorems, relationships, special cases, conditions, and common patterns, all using LaTeX syntax.

## Quick Reference

### Countability
- **Definition:** A set $S$ is countable if it is finite or if its elements can be written as a list: $S = \{x_1, x_2, x_3, \dots\}$. Equivalently, there exists a bijection from a subset of $\mathbb{N}$ to $S$.
- **Examples:** $\mathbb{N}$ and $\mathbb{Q}$ are countable; $\mathbb{R}$ is not countable.

### Limits
- **Definition:** A sequence $(a_1, a_2, a_3, \dots)$ of real numbers converges to a limit $L \in \mathbb{R}$ if, for all $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that $|a_n - L| < \epsilon$ whenever $n \geq N$.
- **Notation:** $L = \lim_{n \to \infty} a_n$ or $a_n \to L$ as $n \to \infty$.

### Infinite Sums
- **Finite Sum Definition:** Given a sequence $(a_1, a_2, a_3, \dots)$, define $s_n = \sum_{k=1}^n a_k = a_1 + a_2 + \dots + a_n$ for any $n \in \mathbb{N}$.
- **Infinite Sum Definition:** The infinite sum $\sum_{k=1}^{\infty} a_k$ converges to a sum $L$ if the limit $L = \lim_{n \to \infty} s_n$ exists. Otherwise, the series diverges.
- **Absolute Convergence Definition:** The series $\sum_{k=1}^{\infty} a_k$ converges absolutely if the series $\sum_{k=1}^{\infty} |a_k|$ converges.
- **Implication:** If a series converges absolutely, then it also converges.
- **Rearrangement Theorem:** If $f: \mathbb{N} \to \mathbb{N}$ is a bijection and $b_k = a_{f(k)}$, and if $\sum_{k=1}^{\infty} a_k$ converges absolutely, then $\sum_{k=1}^{\infty} b_k$ converges, and $\sum_{k=1}^{\infty} a_k = \sum_{k=1}^{\infty} b_k$.
- **Example of Convergent but not Absolutely Convergent Series:** $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$ converges to $\ln{2}$.

### Power Series
- **Form:** A power series is a function of the form $f(x) = \sum_{k=0}^{\infty} c_k x^k$, where $c_k$ are real constants.
- **Radius of Convergence:** For any power series, there exists a radius of convergence $R \in [0, \infty] \cup \{\infty\}$ such that $\sum_{k=0}^{\infty} c_k x^k$ converges absolutely for $|x| < R$ and diverges for $|x| > R$.
- **Probability Generating Function (PGF):** In the course, power series with non-negative coefficients summing to 1 will be encountered (PGFs), in which case $R \ge 1$.
- **Differentiation:** A power series $f(x) = \sum_{k=0}^{\infty} c_k x^k$ with radius of convergence $R$ is differentiable on the interval $(-R, R)$, and its derivative is given by $f'(x) = \sum_{k=0}^{\infty} (k+1)c_{k+1}x^k$, with the same radius of convergence $R$.

### Series Identities
- **Geometric Series:**
    -  For $0 \leq r < 1$:
    $$\sum_{k=0}^{n-1} ar^k = a\frac{1-r^n}{1-r}$$
    $$\sum_{k=0}^{\infty} ar^k = \frac{a}{1-r}$$
- **Exponential Function:** For $\lambda \in \mathbb{R}$:
    $$\sum_{n=0}^\infty \frac{\lambda^n}{n!} = e^\lambda$$
- **Binomial Theorem:** For $x, y \in \mathbb{R}$ and $n \geq 0$:
    $$(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$$

- **Differentiation/Integration of Geometric Series:** For $0 < r < 1$:
  $$ \sum_{k=1}^\infty k r^{k-1} = \frac{d}{dr} \left( \sum_{k=0}^\infty r^k \right) $$
  $$ \sum_{k=1}^\infty \frac{r^k}{k} = \int_0^r \left( \sum_{k=0}^\infty t^k \right) dt $$


### Increasing Sequences of Events
- **Definition:** A sequence of events $A_n, n \ge 1$ is increasing if $A_1 \subseteq A_2 \subseteq A_3 \subseteq \dots$
- **Theorem:** If $A_n, n \ge 1$ is an increasing sequence of events, then
   $$P\left(\bigcup_{n=1}^\infty A_n \right) = \lim_{n \to \infty} P(A_n)$$

### Discrete Distributions (from Table)

**Uniform:**
- $P(X=k) = \frac{1}{n}$ for $k=1, \ldots, n$
- Mean: $\frac{n+1}{2}$
- Variance: $\frac{n^2-1}{12}$
- PGF: $G_X(s) = \frac{s(1-s^n)}{n(1-s)}$

**Bernoulli (p):**
- $P(X=1) = p,  P(X=0)=1-p$
- Mean: $p$
- Variance: $p(1-p)$
- PGF: $G_X(s) = 1-p+ps$

**Binomial (n, p):**
- $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ for $k=0, \ldots, n$
- Mean: $np$
- Variance: $np(1-p)$
- PGF: $G_X(s) = (1-p+ps)^n$

**Poisson ($\lambda$):**
- $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ for $k=0,1, \ldots$
- Mean: $\lambda$
- Variance: $\lambda$
- PGF: $G_X(s) = e^{\lambda(s-1)}$

**Geometric (p):**
- $P(X=k) = (1-p)^{k-1}p$ for $k=1, 2, \ldots$
- Mean: $\frac{1}{p}$
- Variance: $\frac{1-p}{p^2}$
- PGF: $G_X(s) = \frac{ps}{1-(1-p)s}$

**Alternative Geometric (p):**
- $P(X=k) = (1-p)^k p$ for $k=0,1, \ldots$
- Mean: $\frac{1-p}{p}$
- Variance: $\frac{1-p}{p^2}$
- PGF: $G_X(s) = \frac{p}{1-(1-p)s}$

**Negative Binomial (k, p):**
- $P(X=n) = \binom{n-1}{k-1}(1-p)^{n-k}p^k$ for $n=k, k+1, \ldots$
- Mean: $\frac{k}{p}$
- Variance: $\frac{k(1-p)}{p^2}$
- PGF: $G_X(s) = \left( \frac{p}{1-(1-p)s} \right)^k$

### Continuous Distributions (from Table)

**Uniform (a, b):**
- $f(x) = \frac{1}{b-a}$ for $a\le x \le b$
- $F(x) = \frac{x-a}{b-a}$
- Mean: $\frac{a+b}{2}$
- Variance: $\frac{(b-a)^2}{12}$

**Exponential ($\lambda$):**
- $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$
- $F(x) = 1-e^{-\lambda x}$ for $x \ge 0$
- Mean: $\frac{1}{\lambda}$
- Variance: $\frac{1}{\lambda^2}$

**Gamma ($\alpha, \lambda$):**
- $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}$ for $x \ge 0$
- Mean: $\frac{\alpha}{\lambda}$
- Variance: $\frac{\alpha}{\lambda^2}$

**Normal ($\mu$, $\sigma^2$):**
- $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ for $x\in \mathbb{R}$
- Mean: $\mu$
- Variance: $\sigma^2$
- $F(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$, where $\Phi$ is the CDF of the standard normal.

**Standard Normal:**
- $f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ for $x\in\mathbb{R}$
- Mean: 0
- Variance: 1

**Beta ($\alpha, \beta$):**
- $f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$ for $x \in [0,1]$
- Mean: $\frac{\alpha}{\alpha+\beta}$
- Variance: $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$

## Common Patterns and Techniques

### Proof Techniques
- **Countable Additivity:** This is a key property of probability measures used to prove results about unions of disjoint sets (e.g. used to prove the increasing sequence of events theorem).
- **Limit Argument:** The definitions of convergence, infinite sums, and differentiation all heavily rely on using limits.

### Problem-Solving Strategies
- **Recognize Series Patterns:** Knowing the formulas for geometric series, the exponential function, etc. are helpful in solving problems.
- **Use Definitions Carefully:** When working with limits and convergence, paying close attention to the definitions, is critical.
- **Relate Concepts:**  Understanding the relationship between absolute convergence and convergence, how differentiation applies to power series, etc. is necessary for solving problems.

### Connections between Concepts
- **Convergence:** The concept of convergence (of sequences and series) is fundamental to understanding many other mathematical concepts.
- **Power Series and Calculus:**  Power series allow to use calculus techniques (differentiation, integration) on a class of functions defined by an infinite sum.
- **Countability and Set Theory:** The idea of countability is key to understanding set theory, and is used, for example, in constructing probability measures.

### Typical Applications
- **Generating Functions:** The PGFs introduced are essential for analyzing discrete probability distributions, providing a way to compute moments.
- **Analysis of Random Variables:** All the discrete and continuous distributions listed are fundamental when doing probability and statistics.
- **Probability Theory:** The increasing sequences of events theorem is one of the foundational results of basic probability theory, necessary for proving many probability laws.

This structured breakdown should provide a good reference for the concepts in the appendix. Remember that understanding how to apply these concepts is just as important as memorizing the formulas.
