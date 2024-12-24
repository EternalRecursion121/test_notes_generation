# Chapter 6 Revision Notes

Okay, here are the comprehensive revision notes for Chapter 6, following your specifications:

# Chapter 6: Random Samples and the Weak Law of Large Numbers

This chapter explores the concept of random samples and introduces the Weak Law of Large Numbers, a cornerstone of probability and statistics. We will see how repeated samples from a distribution allow us to infer properties of the underlying distribution.

---
## 6.1 Random Samples

### Definition of a Random Sample
>
> **Definition 6.1.** Let $X_1, X_2, ..., X_n$ denote i.i.d. (independent and identically distributed) random variables. These random variables are said to constitute a *random sample* of size $n$ from the distribution.
>
---
* **Intuitive Explanation:** A random sample is essentially a set of observations taken from a single probability distribution. Each observation is independent of the others, and all observations follow the same distribution. This mimics real-world scenarios where we collect data.

### Sample Mean

>
> **Definition 6.2.** The *sample mean* is defined as:
>
> $$\begin{equation} \bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i \end{equation}$$
>
---
* **Significance:** The sample mean is an estimator of the population mean $\mu$. We are interested in properties of the sample mean itself.

### Properties of Sample Mean

#### Variance of Sum of Random Variables

Before we explore the properties of the sample mean, let's establish how the variance of the sum of random variables works:
$$
\text{var}(X + Y) = \text{var}(X) + \text{var}(Y) + 2 \text{cov}(X,Y)
$$

The variance of the sum can be extended by induction:
$$
\text{var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{var}(X_i) + \sum_{i \neq j} \text{cov}(X_i,X_j) = \sum_{i=1}^n \text{var}(X_i) + 2 \sum_{i<j} \text{cov}(X_i, X_j)
$$

#### Theorem 6.3

>
> **Theorem 6.3.** Suppose that $X_1, X_2, ..., X_n$ form a random sample from a distribution with mean $\mu$ and variance $\sigma^2$. Then the expectation and variance of the sample mean are
>
> $$
> E[\bar{X}_n] = \mu \quad \text{and} \quad \text{var}(\bar{X}_n) = \frac{\sigma^2}{n}.
> $$

* **Proof:**
    1.  **Expectation:**
        Using the linearity of expectation:
        $$
         E[\bar{X}_n] = E\left[\frac{1}{n}\sum_{i=1}^n X_i\right] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \frac{1}{n} \sum_{i=1}^n \mu = \frac{n\mu}{n} = \mu
        $$
    2.  **Variance:**
        Since $X_i$'s are independent, $cov(X_i, X_j) = 0$ for $i \neq j$. We have:
        $$
         \text{var}(\bar{X}_n) = \text{var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2} \text{var}\left(\sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n \text{var}(X_i)
        $$
         As the variance of each $X_i$ is given as $\sigma^2$
        $$
         = \frac{1}{n^2} \sum_{i=1}^n \sigma^2 = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}
        $$
        

* **Implication:**
    * The sample mean is an *unbiased* estimator for the population mean.
    * The variance of the sample mean decreases as the sample size $n$ increases.

---
## 6.2 Weak Law of Large Numbers

### Example 6.4 (Bernoulli Sample)
   * Consider a sample of $X_1, X_2,... X_n$ from a Bernoulli distribution with parameter p.
   * $E[X_i] = p$, and  $Var(X_i)=p(1-p)$
   * Thus $E[\bar{X}_n] = p$, and  $Var(\bar{X}_n) = \frac{p(1-p)}{n}$

### Indicator Random Variables

Before delving into the main theorem, it helps to explore indicator random variables. If A is an event with probability p = P(A), the *indicator random variable* is:
$$
X(\omega) =
\begin{cases}
1 \quad \text{ if } \omega \in A\\
0 \quad \text{ if } \omega \notin A
\end{cases}
$$

And $X$  ~ Ber(p) and $E[X] = p$. Consider $n$ trials of this experiment, $X_i$ are the indicators of A occurring on the ith trial. By intuition, the proportion of times A occurs should be close to p when n is large.

### Theorem 6.5 (Weak Law of Large Numbers)

>
> **Theorem 6.5 (Weak Law of Large Numbers).** Suppose that $X_1, X_2,...$ are independent and identically distributed random variables with mean $\mu$. Then for any fixed $\epsilon > 0$,
>
> $$
> P\left( \left| \frac{1}{n}\sum_{i=1}^n X_i - \mu \right| > \epsilon \right) \rightarrow 0 \quad \text{as } n \rightarrow \infty
> $$
>
>
> (Equivalently,
>
> $$
> P\left( \left| \frac{1}{n}\sum_{i=1}^n X_i - \mu \right| \leq \epsilon \right) \rightarrow 1 \quad \text{as } n \rightarrow \infty
> $$
>
> )
>
---
* **Intuitive Explanation:** The Weak Law of Large Numbers states that as the sample size grows, the sample mean converges in probability to the true mean of the distribution. In other words, for a large sample size, the sample mean is very likely to be very close to the population mean.

### Theorem 6.6 (Markov's Inequality)

>
> **Theorem 6.6 (Markov's Inequality).** Suppose that Y is a non-negative random variable whose expectation exists. Then
>
> $$
> P(Y \geq t) \leq \frac{E[Y]}{t} \quad \text{for all } t > 0
> $$
>
---

*   **Proof:**
    *   Let $A = \{ Y \geq t \}$. We can assume $P(A) \in (0,1)$ (otherwise, the result is trivial).
    *   Using the law of total expectation:
        $$
        E[Y] = E[Y|A]P(A) + E[Y|A^c]P(A^c)
        $$
    *   Since $Y$ is non-negative, and $P(A^c) \geq 0$, we have
        $$
        E[Y] \geq E[Y|A] P(A)
        $$
    *   Also, when $Y \geq t$, $E[Y|A] \geq t$. Substituting into the previous equation:
         $$
         E[Y] \geq t P(A)
         $$
     *  Rearranging gives the result
         $$
           P(Y \geq t) \leq \frac{E[Y]}{t}
         $$

### Theorem 6.7 (Chebyshev's Inequality)
> **Theorem 6.7 (Chebyshev's Inequality).** Suppose that Z is a random variable with a finite variance. Then for any $t > 0$,
>
> $$P(|Z - E[Z]| \geq t) \leq \frac{\text{var}(Z)}{t^2}$$
>

* **Proof:**
    *   Note that  $P(|Z - E[Z]| \geq t) = P((Z - E[Z])^2 \geq t^2)$
    *   Apply Markov's inequality with $Y = (Z - E[Z])^2$:
        $$
        P((Z-E[Z])^2 \geq t^2) \leq \frac{E[(Z-E[Z])^2]}{t^2} = \frac{var(Z)}{t^2}
        $$

### Proof of Theorem 6.5 (Under finite variance assumption)

*  **Assumption:** We assume $X_i$'s come from a distribution with finite variance $\sigma^2$.

*  **Set up:**
  *  Define  $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$
  * From theorem 6.3, we know that $E[\bar{X}_n] = \mu$ and $Var(\bar{X}_n) = \frac{\sigma^2}{n}$

* **Using Chebyshev's inequality:**
 $$
  P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu \right| \geq \epsilon\right) = P\left(|\bar{X}_n - E[\bar{X}_n]| \geq \epsilon\right)  \leq \frac{var(\bar{X}_n)}{\epsilon^2} = \frac{\sigma^2}{n \epsilon^2}
 $$
*  Since $\epsilon$ is fixed, the RHS goes to zero as $n \rightarrow \infty$.
*  Thus, we have that
$$
 P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu \right| \geq \epsilon\right) \rightarrow 0 \quad \text{ as } n \rightarrow \infty
 $$
   Which proves the weak law of large numbers under the finite variance assumption.

---

These notes cover the core concepts and proofs from the provided pages. Feel free to ask if you need clarification on any of these points.
