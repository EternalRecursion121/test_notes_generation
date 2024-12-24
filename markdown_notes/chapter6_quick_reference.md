# Chapter 6 Quick Reference

Okay, here's a comprehensive breakdown of Chapter 6, structured into the requested "Quick Reference" and "Common Patterns and Techniques" sections.

## Quick Reference

**Definitions**

*   **Random Sample:** A sequence of i.i.d. random variables $X_1, X_2, ..., X_n$.
*   **Sample Mean:** $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$

**Formulas and Results**

*   **Variance of a Sum:**  For random variables $X$ and $Y$:
    $\text{var}(X+Y) = \text{var}(X) + \text{var}(Y) + 2 \text{cov}(X,Y)$
*   **Variance of Sum of n Variables:**
    $\text{var} (\sum_{i=1}^n X_i) = \sum_{i=1}^n \text{var}(X_i) + 2 \sum_{i<j} \text{cov}(X_i, X_j)$
*   **Expectation of Sample Mean:** $E[\bar{X}_n] = \mu$ (when $E[X_i]=\mu$ for all i)
*   **Variance of Sample Mean:** $\text{var}(\bar{X}_n) = \frac{\sigma^2}{n}$ (when $\text{var}(X_i)=\sigma^2$ for all i and $X_i$ are independent)
*   **Indicator Function:** $\mathbb{I}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$

**Theorems**

*   **Theorem 6.3:** If $X_1, X_2, ..., X_n$ is a random sample with mean $\mu$ and variance $\sigma^2$, then $E[\bar{X}_n] = \mu$ and $\text{var}(\bar{X}_n) = \frac{\sigma^2}{n}$.
*   **Theorem 6.5 (Weak Law of Large Numbers):** If $X_1, X_2, ...$ are independent and identically distributed random variables with mean $\mu$, then for any $\epsilon > 0$,
    $$\lim_{n \to \infty} P\left( \left| \frac{1}{n}\sum_{i=1}^n X_i - \mu \right| > \epsilon \right) = 0$$
    (or equivalently, $\lim_{n \to \infty} P\left( \left| \frac{1}{n}\sum_{i=1}^n X_i - \mu \right| \le \epsilon \right) = 1$)
*   **Theorem 6.6 (Markov's Inequality):** If $Y$ is a non-negative random variable with expectation, then for any $t > 0$, $P(Y \ge t) \le \frac{E[Y]}{t}$.
*   **Theorem 6.7 (Chebyshev's Inequality):** If $Z$ is a random variable with finite variance, then for any $t > 0$, $P(|Z-E[Z]| \ge t) \le \frac{\text{var}(Z)}{t^2}$.

**Key Relationships and Implications**

*   **Sample Mean as Estimator:** The sample mean $\bar{X}_n$ is an estimator for the population mean $\mu$.
*   **Weak Law of Large Numbers:**  As the sample size $n$ increases, the sample mean $\bar{X}_n$ converges in probability to the population mean $\mu$. This means that with very high probability for a large sample size, sample mean will be very close to the population mean.
*   **Variance Reduction:** The variance of the sample mean decreases as the sample size $n$ increases ($\text{var}(\bar{X}_n) = \frac{\sigma^2}{n}$). This means that larger samples give more precise estimates.
*   **Markov and Chebyshev:** Markov's inequality is a more general tool but it gives a weaker bound. Chebyshev's inequality requires a finite variance, but gives tighter bounds when the assumption is met.
*   **Proof of WLLN using Chebyshev:** The weak law of large numbers (with finite variance) can be proven using Chebyshev's inequality.

**Important Special Cases**

*   **Bernoulli Distribution:** When $X_i$ are Bernoulli variables with parameter $p$, then $E[X_i] = p$ and $\text{var}(X_i) = p(1-p)$. Thus, the sample mean's expected value and variance are $E[\bar{X}_n] = p$ and $\text{var}(\bar{X}_n) = \frac{p(1-p)}{n}$.

**Key Conditions and Assumptions**

*   **I.I.D. Assumption:** Many of these results depend on the assumption that random variables are independent and identically distributed (i.i.d.).
*   **Finite Variance:** Chebyshev's inequality and the proof of the weak law of large numbers presented in the text require the random variables to have a finite variance. Markov's Inequality works if expectation exists

## Common Patterns and Techniques

**Key Proof Techniques**

*   **Linearity of Expectation:** Used extensively to compute the expected value of sample mean.
*   **Law of Total Probability:**  Used to establish the Markov's inequality for non-negative random variables.
*   **Variance Properties:** Using $\text{var}(X+Y)$ formula and induction, and the fact that covariance is zero for independent variables, to find the variance of sample mean.
*   **Inequality Manipulation:** Rearranging inequalities and using known properties of expectation to establish Markov and Chebyshev inequalities.
*   **Replacing Absolute Value:** The absolute value in the WLLN is handled by considering the square.  
*   **Bounding Probabilities** Using Chebyshev's inequality to bound the probability of the difference between the sample mean and the true mean exceeding a given threshold, and showing the limit of the bound to be zero.

**Common Problem-Solving Strategies**

*   **Recognizing Random Samples:** Identifying whether a given scenario involves independent and identically distributed random variables.
*   **Applying Definitions:**  Using the definition of sample mean, variance, and covariance to find expected value and variance of the sample mean.
*   **Using Inequalities:** Employing Markov's and Chebyshev's inequalities when looking for upper bound on the probability of an event
*   **Choosing the Right Theorem:** Determining when to apply the WLLN and which inequality is most suitable for a given problem.

**Important Connections Between Concepts**

*   **Sample Mean and Estimation:** The sample mean serves as a fundamental tool for estimating the population mean.
*   **Large Sample Size:** WLLN explains why sample means get closer to population means as sample sizes increase.
*   **Variance and Precision:** The variance of the sample mean, inversely proportional to sample size, shows how larger samples improve the precision of the estimate.
*  **Proof by Inequalities:** Markov's inequality is used in the proof of Chebyshev's inequality, which is then used in the proof of the WLLN.

**Typical Applications of Theorems**

*   **Estimating Population Parameters:** In real-world applications, WLLN provides justification for using sample means to estimate population means.
*   **Approximations:** WLLN provides a foundation for approximation theory.
*  **Statistical Inference** Foundations for making statistical inferences about population means and distribution parameters.
* **Quality Control:** Quality control and sampling to monitor the performance of a manufacturing process.

Let me know if you'd like any of these points elaborated further or have more questions about the chapter!
