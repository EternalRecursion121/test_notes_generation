# Chapter 4 Revision Notes

Okay, here are comprehensive revision notes for Chapter 4, "Probability Generating Functions", based on the provided PDF, formatted with LaTeX, markdown, and designed for clarity and rigor:

# Chapter 4: Probability Generating Functions

This chapter introduces probability generating functions (PGFs), a powerful tool for analyzing discrete random variables, and explores their properties and applications.

---

## 4.1 Definition of Probability Generating Functions

> **Definition 4.1.** Let X be a non-negative integer-valued random variable. Let
> $$ S := \left\{ s \in \mathbb{R}: \sum_{k=0}^{\infty} |s|^k P(X=k) < \infty \right\} $$
> Then, the **probability generating function** (p.g.f.) of X is $G_X: S \rightarrow \mathbb{R}$ defined by:
> $$ G_X(s) = \mathbb{E}[s^X] = \sum_{k=0}^{\infty} s^k P(X=k) $$

*   **Intuition:** The PGF transforms the probabilities of a discrete random variable into a power series, which we can then manipulate using calculus and algebra.
*   We often use the shorthand notation $p_k = p_X(k) = P(X=k)$.
*   Notice that $G_X(1) = \sum_{k=0}^{\infty} P(X=k) = 1$ because the probabilities sum to 1.
*   The argument *s* is a parameter, not a random variable. We can plug in specific values.
*   The PGF is certainly defined for $|s| \le 1$, i.e., $[-1, 1] \subseteq S$.

---

## 4.2 Uniqueness and Convergence of Probability Generating Functions

> **Theorem 4.2 (Uniqueness Theorem).** The distribution of $X$ is uniquely determined by its probability generating function, $G_X$.

*   **Important Consequence:** If two random variables have the same PGF, then they have the same distribution.
*   A PGF is an example of a power series: $f(x) = \sum_{n=0}^{\infty} c_n x^n$.
*   The **radius of convergence**, *r*, of a power series is the value such that the sum converges for $|x| < r$ and diverges for $|x| > r$.
*   For a PGF, the radius of convergence is at least 1, since it converges for $|s| \le 1$.
*   Within the radius of convergence, a power series (such as a PGF) is differentiable, and we can differentiate term-by-term:
    $$ f'(x) = \sum_{n=1}^{\infty} n c_n x^{n-1} $$

---

## 4.3 Recovering Probabilities from the PGF

*   We can extract probabilities by differentiating the PGF:

    *   $G_X(0) = p_0$

    *   $G_X'(s) = \sum_{k=1}^{\infty} k p_k s^{k-1}$

    *   $G_X'(0) = p_1$

    *   $\frac{d^k}{ds^k} G_X(s) |_{s=0} = k! p_k$

    *   Therefore, $p_k = \frac{1}{k!} \frac{d^k}{ds^k} G_X(s) |_{s=0}$

*   This confirms that knowing the PGF is sufficient to recover the full distribution.

---

## 4.4 Common PGFs

### 4.4.1 Bernoulli Distribution

*   $X \sim \text{Ber}(p)$ where $X$ takes values 0 or 1, with $P(X=1) = p$ and $P(X=0) = 1 - p = q$.

    $$G_X(s) = \sum_{k=0}^1 s^k p_k = qs^0 + ps^1 = q + ps$$

### 4.4.2 Binomial Distribution

*   $X \sim \text{Bin}(n, p)$
$$
G_X(s) = \sum_{k=0}^n s^k \binom{n}{k} p^k (1-p)^{n-k}
= \sum_{k=0}^n \binom{n}{k} (ps)^k (1-p)^{n-k}
$$
*   By the binomial theorem, we get
    $$ G_X(s) = (1 - p + ps)^n $$

### 4.4.3 Poisson Distribution

*   $X \sim \text{Po}(\lambda)$
    $$
    G_X(s) = \sum_{k=0}^{\infty} s^k \frac{\lambda^k e^{-\lambda}}{k!}
    = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda s)^k}{k!}
    $$
    *   Since $e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$, we have
        $$ G_X(s) = e^{-\lambda} e^{\lambda s} = e^{\lambda(s-1)} $$

### 4.4.4 Geometric Distribution

*   $X \sim \text{Geo}(p)$.
*  The PGF is given by
    $$
    G_X(s) = \frac{ps}{1 - (1-p)s}
    $$
    for $|s| < \frac{1}{1-p}$.

---

## 4.5 PGFs and Independence

> **Theorem 4.3.** If $X$ and $Y$ are independent random variables, then:
>$$ G_{X+Y}(s) = G_X(s) G_Y(s) $$

*   **Proof:**
    $$ G_{X+Y}(s) = \mathbb{E}[s^{X+Y}] = \mathbb{E}[s^X s^Y] $$
    Since $X$ and $Y$ are independent, $s^X$ and $s^Y$ are independent, so:
    $$ \mathbb{E}[s^X s^Y] = \mathbb{E}[s^X] \mathbb{E}[s^Y] = G_X(s) G_Y(s) $$

*   **Important:** This is a key property that allows us to easily find the PGF of a sum of independent random variables.

---

## 4.6 Applications of PGFs in Distribution Theory

> **Theorem 4.4.** Suppose that $X_1, X_2, ..., X_n$ are independent $\text{Ber}(p)$ random variables, and let $Y = X_1 + \dots + X_n$. Then $Y \sim \text{Bin}(n, p)$.

*   **Proof:**
    $$ G_Y(s) = \mathbb{E}[s^Y] = \mathbb{E}[s^{X_1 + ... + X_n}] = \mathbb{E}[s^{X_1}] ... \mathbb{E}[s^{X_n}] $$
    Since each $X_i$ is $\text{Ber}(p)$, $\mathbb{E}[s^{X_i}] = (1 - p + ps)$.  Therefore,
    $$ G_Y(s) = (1 - p + ps)^n $$
    This is the PGF of $\text{Bin}(n, p)$.  The uniqueness theorem then implies that $Y \sim \text{Bin}(n, p)$.

> **Theorem 4.5.** Suppose that $X_1, X_2, ..., X_n$ are independent random variables such that $X_i \sim \text{Po}(\lambda_i)$.  Then
$$ \sum_{i=1}^n X_i \sim \text{Po}\left(\sum_{i=1}^n \lambda_i\right) $$

*  **Proof:**
  $$
   G_{X_1 + \dots + X_n}(s) = \prod_{i=1}^{n} E[s^{X_i}] = \prod_{i=1}^n e^{\lambda_i(s-1)} = e^{\sum_{i=1}^{n}\lambda_i(s-1)}
  $$

*   **Important Implication:** The sum of independent Poisson random variables is also a Poisson random variable with parameter equal to the sum of the parameters.

---

## 4.7 Calculating Expectations Using PGFs

*   We can obtain moments (e.g., mean and variance) of a random variable using derivatives of its PGF:

    *   $\mathbb{E}[X] = G_X'(1)$

    *   $\mathbb{E}[X(X-1)] = G_X''(1)$

    *   $\text{var}(X) = G_X''(1) + G_X'(1) - (G_X'(1))^2$

*   More generally:
    $$ \frac{d^k}{ds^k} G_X(s)|_{s=1} = \mathbb{E}[X(X-1)\dots(X-k+1)] $$

---

## 4.8 Random Sums

> **Theorem 4.8.** Let $X_1, X_2,...$ be independent and identically distributed (i.i.d.) non-negative integer-valued random variables with PGF $G_X(s)$. Let $N$ be another non-negative integer-valued random variable, independent of the $X_i$, with PGF $G_N(s)$.  Then the PGF of $Y = \sum_{i=1}^N X_i$ is
$$ G_Y(s) = G_N(G_X(s)) $$
> Where we define $\sum_{i=1}^{0} X_i = 0$

*   **Proof:**
    $$ \mathbb{E}[s^Y] = \mathbb{E}\left[\mathbb{E}[s^Y|N]\right] = \sum_{n=0}^\infty \mathbb{E}\left[s^{\sum_{i=1}^n X_i}\right] P(N=n) $$
    Because $X_i$'s are independent,
    $$ \mathbb{E}\left[s^{\sum_{i=1}^n X_i}\right] = (G_X(s))^n $$
    $$ \mathbb{E}[s^Y] = \sum_{n=0}^\infty (G_X(s))^n P(N=n) = G_N(G_X(s)) $$
*   **Interpretation:** The PGF of a sum with a random number of terms is the composition of PGFs of the random number of terms ($N$) and the individual terms ($X_i$).
    * If $N = 0$, we interpret $Y = 0$.

---

## 4.9  Application of Random Sums

> **Corollary 4.9.** Suppose that $X_1, X_2, \dots$ are i.i.d. $\text{Ber}(p)$ and that $N \sim \text{Po}(\lambda)$, independently. Then $Y = \sum_{i=1}^N X_i \sim \text{Po}(\lambda p)$.

*  **Proof:** We have $G_X(s) = 1-p+ps$ and $G_N(s) = e^{\lambda(s-1)}$.
 $$ G_Y(s) = G_N(G_X(s)) = e^{\lambda(1-p+ps-1)} = e^{\lambda p(s-1)} $$

---

## 4.10 Branching Processes

*   A **branching process** is a stochastic model for the evolution of a population.

    *   Each individual lives a unit of time and gives birth to a random number of offspring before dying.

    *   Different individuals reproduce independently in the same manner.

*   Let $X_n$ be the size of the population in generation $n$. We have $X_0 = 1$.
*   Let $C^{(n)}_i$ be the number of children of the $i^{th}$ individual in generation $n$.
    $$ X_{n+1} = \sum_{i=1}^{X_n} C_i^{(n)} $$
*   Let $G(s) = \sum_{i=0}^\infty p(i)s^i$ be the PGF of the offspring distribution, where $p(i)$ is the probability of having $i$ offspring.
*   Let $G_n(s) = E[s^{X_n}]$ be the PGF of the population size in generation $n$.

> **Theorem 4.11.** For $n \geq 0$
>$$ G_{n+1}(s) = G(G_n(s)) = G(G( ... G(s) ...)) $$
> with $n+1$ compositions of the function $G$.

*   **Proof:**
    $$ G_{n+1}(s) = \mathbb{E}[s^{X_{n+1}}] = \mathbb{E}\left[\mathbb{E}\left[s^{X_{n+1}}|X_n\right]\right]  $$
    We have $$ X_{n+1} = \sum_{i=1}^{X_n} C_i^{(n)} $$

   Now use Theorem 4.8:
  $$
   G_{n+1}(s) = \mathbb{E}[s^{X_{n+1}}] = \mathbb{E}[ G_{X_n}(s) ] = G_{X_n}(G(s))
  $$
  Letting $G_{n}(s) = \mathbb{E}[s^{X_n}]$, we have:
  $$
   G_{n+1}(s) = G_n(G(s)) = G(G_n(s))
  $$

> **Corollary 4.12.** Suppose that the mean number of children of a single individual is $\mu = \sum_{i=1}^{\infty} ip(i)$.  Then $\mathbb{E}[X_n] = \mu^n$.

*   **Proof:**

    *  We have $\mathbb{E}[X_n] = G_n'(1)$.

     * Using the chain rule:
         $$ G_n'(s) = G'(G_{n-1}(s))G'_{n-1}(s) $$
     *  Letting $s=1$ we get
      $$
       G_n'(1) = G'(G_{n-1}(1))G_{n-1}'(1) = G'(1) G_{n-1}'(1)
      $$
      * Since $G'(1) = \mu$, by induction $\mathbb{E}[X_n] = G_n'(1) = \mu^n$.

*   **Interpretation:** If $\mu>1$, we have exponential growth, if $\mu<1$ we have exponential decay.

---

## 4.11 Extinction Probability

* The **extinction probability**, $q$, is the probability that the population dies out eventually:

$$
q = P \left( \bigcup_{n=1}^\infty \{X_n = 0 \} \right) = \lim_{n \rightarrow \infty} P(X_n = 0)
$$

*   This probability can be computed by finding the solution to a fixed-point equation.

> **Theorem 4.13.** The extinction probability $q$ is the smallest non-negative solution to:
> $$ q = G(q) $$
*   **Proof:** From the definition, $q = \lim_{n\to\infty} P(X_n=0) = \lim_{n\to\infty} G_n(0)$.  Also, $$G_{n+1}(0) = G(G_n(0)).$$ Now, take the limit as $n\to\infty$:
  $$
   \lim_{n\to\infty}G_{n+1}(0) = \lim_{n\to\infty} G(G_n(0)) \implies q = G(q)
  $$
* To prove that the extinction probability is the *smallest* such solution, we can use induction. We can show that $G_n(0)\leq r$ for all $n\geq 0$ where $r$ is another solution of $r = G(r)$.
* We start with $G_0(0) = 0 < r$. Now, assume $G_{n-1}(0)\leq r$. Then,
 $$ G_n(0) = G(G_{n-1}(0)) \leq G(r) = r $$
 Therefore, $q = \lim_{n\rightarrow \infty} G_n(0) \leq r$, implying $q$ is indeed the smallest solution.

> **Theorem 4.14.** Assume that $p(1) \ne 1$. Then $q = 1$ if $\mu \le 1$ and $q < 1$ if $\mu > 1$.

*   **Proof:**
    * If $\mu<1$, $\mathbb{E}[X_n]=\mu^n \rightarrow 0$ as $n \rightarrow \infty$, and $P(X_n>0) \leq \mathbb{E}[X_n]$ also tends to 0, which implies $q=1$.
    *  For $\mu=1$, we need to consider the graphs of $y=G(x)$ and $y=x$. In this case the tangent of the curve $G(x)$ at the point $x=1$ is $1$ and since $G(x)$ is convex it lies below $y=x$ for $x < 1$, and the smallest solution for $G(x)=x$ is $x=1$ so $q=1$.
     * If $\mu>1$, the tangent of $G(x)$ at $x=1$ is greater than $1$, therefore $G(x)$ must cross the line $y=x$ for some $x<1$ and that gives a solution $q$ where $q<1$.
---

These revision notes aim to provide a structured and comprehensive understanding of probability generating functions, their properties, and applications.  The material is presented with LaTeX for mathematical rigor, and includes all major theorems and proofs.  I hope they are helpful!
