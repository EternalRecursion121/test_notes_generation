# Appendix Revision Notes

Okay, let's break down the appendix and create detailed revision notes.

# Appendix: Essential Concepts from Analysis

This appendix covers key ideas from analysis needed for the main course. We'll focus on sets, sequences, series, and a few common distributions.

---

## A.1 Useful Ideas from Analysis

### Countability

> **Definition (Countable Set):**
> A set $S$ is considered *countable* if it is either finite, or its elements can be arranged into a list: $S = \{x_1, x_2, x_3, ...\}$. Equivalently, there exists a bijection from a subset of the natural numbers $\mathbb{N}$ to $S$.

*   **Examples:**
    *   The set of natural numbers $\mathbb{N}$ is countable.
    *   The set of rational numbers $\mathbb{Q}$ is countable.
*   **Non-Example:** The set of real numbers $\mathbb{R}$ is *not* countable.

---

### Limits

> **Definition (Limit of a Sequence):**
> A sequence of real numbers $(a_1, a_2, a_3, ...)$ is said to *converge* to a limit $L \in \mathbb{R}$ if, for every $\epsilon > 0$, there exists an $N \in \mathbb{N}$ such that $|a_n - L| < \epsilon$ whenever $n \geq N$.
> We write this as: $L = \lim_{n \to \infty} a_n$ or $a_n \to L$ as $n \to \infty$.

This definition formalizes the idea that the terms of a sequence get arbitrarily close to some number $L$ as $n$ gets large.

---

### Infinite Sums (Series)

*   **Finite Sums:** For a sequence $(a_1, a_2, a_3, ...)$, the finite sum up to $n$ is denoted by:
    $$ s_n = \sum_{k=1}^n a_k = a_1 + a_2 + ... + a_n $$

> **Definition (Convergent Series):**
> For a sequence $(a_1, a_2, a_3, ...)$, the infinite sum or series $\sum_{k=1}^{\infty} a_k$ *converges* to a sum $L$ if the limit of the partial sums, $L = \lim_{n\rightarrow \infty} s_n$, exists. If the limit does not exist, the series *diverges*.

*   **Partial Sums:** The sequence of partial sums $(s_1, s_2, s_3, ...)$ is defined as $s_n = \sum_{k=1}^{n} a_k$.
    *   A series converges if this sequence of partial sums converges.

> **Definition (Absolute Convergence):**
> A series $\sum_{k=1}^{\infty} a_k$ *converges absolutely* if the series $\sum_{k=1}^{\infty} |a_k|$ converges.

*   **Theorem:** If a series converges absolutely, then it also converges. This is a crucial property.

*   **Rearrangement of Terms:**  Suppose $f$ is a bijection from $\mathbb{N}$ to $\mathbb{N}$, and let $b_k = a_{f(k)}$. If $\sum_{k=1}^{\infty} a_k$ converges absolutely, then $\sum_{k=1}^{\infty} b_k$ also converges, and both sums are equal:
    $$\sum_{k=1}^{\infty} a_k = \sum_{k=1}^{\infty} b_k$$
*   **Example:** The alternating harmonic series $\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$ converges to $\ln(2)$, but not absolutely.

    If rearranged: $1+\frac{1}{3}+\frac{1}{5}-\frac{1}{2}+\frac{1}{7}+\frac{1}{9}+\frac{1}{11}-\frac{1}{4} \dots = \frac{3}{2} ln(2)$. So, order matters for conditionally convergent series.

---

### Power Series

> **Definition (Power Series):**
> A power series is a function of the form:
>  $$ f(x) = \sum_{k=0}^{\infty} c_k x^k $$
> where $c_k$ are real coefficients.

*   **Radius of Convergence:** For every power series, there exists a radius of convergence $R \in [0, \infty] \cup \{\infty\}$ such that:
    *   The series converges absolutely for all $|x| < R$.
    *   The series diverges for all $|x| > R$.

*   **Probability Generating Functions:** In this course, we focus on power series where the coefficients are non-negative and sum to 1. In this case, $R \geq 1$.

*   **Differentiation:** Power series behave well when differentiated.
    *   A power series $f(x) = \sum_{k=0}^{\infty} c_k x^k$ with radius of convergence $R$ is differentiable on $(-R, R)$.
    *   The derivative, given by $f'(x) = \sum_{k=0}^{\infty} (k+1) c_{k+1} x^k$ also has radius of convergence $R$.

---

### Series Identities

*   **Geometric Series:** If $0 \leq r < 1$, then:
    *  $$\sum_{k=0}^{n-1} ar^k = a\frac{(1-r^n)}{1-r}$$
    *  $$\sum_{k=0}^{\infty} ar^k = \frac{a}{1-r}$$

*   **Exponential Function:** For $\lambda \in \mathbb{R}$:
     $$\sum_{n=0}^{\infty} \frac{\lambda^n}{n!} = e^{\lambda}$$

*   **Binomial Theorem:** For $x, y \in \mathbb{R}$ and $n \geq 0$:
     $$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$$

*   **Differentiation and Integration:** These operations can be applied term by term within the radius of convergence.
    *  $$\sum_{k=1}^{\infty} kr^{k-1} = \frac{d}{dr}\left( \sum_{k=0}^{\infty} r^k \right)$$
    *  $$\sum_{k=1}^{\infty} \frac{r^k}{k} = \int_{0}^{r} \left(\sum_{k=0}^{\infty} t^k \right) dt$$

---

## A.2 Increasing Sequences of Events

> **Definition (Increasing Sequence of Events):**
> A sequence of events $A_n$, $n \geq 1$ is called an *increasing sequence* if $A_1 \subseteq A_2 \subseteq A_3 \subseteq ...$.

> **Proposition:**
> If $A_n$, $n \geq 1$, is an increasing sequence of events, then:
> $$P\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} P(A_n)$$

* **Proof:**
    *  We can rewrite $A_n$ as a disjoint union due to increasing nature of the sequence:
       $$A_n = A_1 \cup (A_2 \setminus A_1) \cup (A_3 \setminus A_2) \cup \dots \cup (A_n \setminus A_{n-1})$$
       Similarly, $\bigcup_{k=1}^\infty A_k = A_1 \cup \bigcup_{k=2}^\infty(A_k \setminus A_{k-1})$
    *  Applying the countable additivity axiom twice:
       $$P\left(\bigcup_{k=1}^{\infty} A_k\right) = P(A_1) + \sum_{k=2}^\infty P(A_k \setminus A_{k-1})$$
    *   Since the limit of a sum is the sum of the limits:
        $$P\left(\bigcup_{k=1}^{\infty} A_k\right) = \lim_{n\rightarrow \infty}\left[ P(A_1) + \sum_{k=2}^n P(A_k \setminus A_{k-1}) \right]$$
     *   Recognizing this as a telescoping sum, we get:
        $$P\left(\bigcup_{k=1}^{\infty} A_k\right) = \lim_{n\rightarrow \infty} P\left(A_n\right)$$
    

---

## Common Discrete Distributions

Here's a summary of common discrete probability distributions, including:

* **Uniform** ($U\{1,2,...,n\}$): Each outcome has equal probability.
* **Bernoulli** ($Ber(p)$): Represents a single trial with two outcomes: success or failure.
* **Binomial** ($Bin(n,p)$): Counts the number of successes in $n$ independent Bernoulli trials.
* **Poisson** ($P(\lambda)$): Models the number of events occurring in a fixed interval of time/space.
* **Geometric** ($Geom(p)$): Counts the number of trials until the first success.
* **Alternative Geometric**: $P(X = k) = (1 - p)^k p, k=0,1,...$. Counts the number of failures before the first success.
* **Negative Binomial** ($NegBin(k,p)$): Counts the number of trials until the $k^{th}$ success.

(Table from document is reproduced here)

| Distribution | Probability mass function  | Mean | Variance   | Generating function                 |
|--------------------|--------------------------------------------------------------------------|--------------------|---------------------|----------------------------------------------------|
| Uniform $U\{1,2,...,n\}$ | $P(X = k) = \frac{1}{n}, 1 \le k \le n$ | $\frac{n+1}{2}$| $\frac{n^2 - 1}{12}$ |$ G_X(s)=\frac{s(1-s^n)}{n(1-s)}$ |
| Bernoulli $Ber(p)$| $P(X = 1) = p, P(X = 0) = 1 - p$ | $p$ | $p(1-p)$ | $G_X(s)=1-p+ps$        |
| Binomial $Bin(n, p)$| $P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, k=0,1,..,n$ | $np$ | $np(1-p)$ | $G_X(s)=(1 - p + ps)^n$         |
| Poisson $P(\lambda)$ | $P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, k = 0, 1, 2, ...$ | $\lambda$ | $\lambda$ | $G_X(s)=e^{\lambda(s-1)}$ |
| Geometric $Geom(p)$ | $P(X = k) = (1 - p)^{k-1}p, k = 1, 2, ...$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$| $ G_X(s)=\frac{ps}{1-(1-p)s} $ |
| Alternative Geometric | $P(X = k) = (1 - p)^{k}p, k = 0, 1, ...$  | $\frac{1-p}{p}$ | $\frac{1-p}{p^2}$  | $ G_X(s)=\frac{p}{1-(1-p)s} $|
| Negative Binomial $NegBin(k,p)$ | $P(X = n) = \binom{n-1}{k-1} (1-p)^{n-k}p^k, n=k,k+1,...$| $\frac{k}{p}$  | $\frac{k(1-p)}{p^2}$| $G_X(s) = (\frac{p}{1-(1-p)s})^k$ |

---
## Common Continuous Distributions

Here are some common continuous probability distributions:
* **Uniform** ($U[a, b]$): Probability is uniform in the range $[a,b]$.
* **Exponential** ($Exp(\lambda)$): Models time between events in Poisson process.
* **Gamma** ($\Gamma(\alpha, \lambda)$):  Represents waiting time for $\alpha$ events in a Poisson process.
* **Normal** ($N(\mu, \sigma^2)$): The most common continuous distribution, often arises from the sum of independent random variables.
* **Standard Normal** ($N(0, 1)$): The normal distribution with zero mean and unit variance.
* **Beta** ($Beta(\alpha, \beta)$): Defined over the interval $[0, 1]$, often used as prior distributions.

(Table from document is reproduced here)

| Distribution   | Probability density function       | Cumulative distribution function | Mean              | Variance            |
|----------------|--------------------------------------|----------------------------------|-------------------|----------------------|
| Uniform $U[a,b]$ | $f_X(x)=\frac{1}{b-a}, a \le x \le b$ | $F_X(x) = \frac{x-a}{b-a}, a \le x \le b$    |$\frac{a+b}{2}$    | $\frac{(b-a)^2}{12}$   |
| Exponential $Exp(\lambda)$    |   $f_X(x) = \lambda e^{-\lambda x}, x \geq 0$ | $F_X(x) = 1-e^{-\lambda x}, x >0$| $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$|
| Gamma $Gamma(\alpha,\lambda)$ |   $f_X(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1}e^{-\lambda x}, x \ge 0$  |  -      |$\frac{\alpha}{\lambda}$|$\frac{\alpha}{\lambda^2}$   |
| Normal $N(\mu,\sigma^2)$    |  $f_X(x) = \frac{1}{\sqrt{2\pi \sigma^2}}e^{\frac{-(x-\mu)^2}{2\sigma^2}}, x \in \mathbb{R}$| $F_X(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$   | $\mu$   |  $\sigma^2$   |
| Standard Normal $N(0,1)$    |   $f_X(x) = \frac{1}{\sqrt{2\pi}}e^{\frac{-x^2}{2}}, x \in \mathbb{R}$|  $F_X(x) = \Phi(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{\frac{-u^2}{2}}du$   | $0$     |  $1$     |
| Beta $Beta(\alpha,\beta)$    | $f_X(x)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}, x \in [0,1]$ |  -   | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

---
This concludes the revision notes for the appendix. This summary combines the mathematical details with some intuitive explanations, aiming to give a complete and structured overview of the content. Let me know if there are any parts you would like me to expand or clarify.
