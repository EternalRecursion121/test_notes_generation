# Chapter 2 Revision Notes

Okay, here are comprehensive revision notes for Chapter 2 of the provided text, adhering to your specifications:

# Chapter 2: Discrete Random Variables

## 2.1 Introduction to Random Variables

> **Intuitive Idea:** Random variables are numerical measurements associated with random phenomena.

- Discrete random variables take on a finite or countable set of values. This contrasts with continuous random variables which will be discussed later.

### Definition 2.1: Discrete Random Variable
> A discrete random variable $X$ on a probability space $(\Omega, \mathcal{F}, P)$ is a function $X: \Omega \rightarrow \mathbb{R}$ such that:
>
> (a) For each $x \in \mathbb{R}$, $\{\omega \in \Omega : X(\omega) = x \} \in \mathcal{F}$
> (b) The image of $X$,  $\text{Im}X := X(\Omega) = \{X(\omega) : \omega \in \Omega\}$, is a finite or countable subset of $\mathbb{R}$.

- **Explanation:**
   - Condition (a) ensures that the set of outcomes where the random variable $X$ takes a specific value $x$ is an event in our sample space (i.e., it is measurable). This allows us to assign probabilities to the events $\{X=x\}$.
   - Condition (b) means $X$ can only take on a discrete set of values.

-   We often abbreviate "random variable" to "r.v."
-   The event $\{\omega \in \Omega: X(\omega) = x\}$ is often abbreviated as $\{X = x\}$, and we write $P(X = x)$ for  $P(\{ \omega \in \Omega : X(\omega) = x\})$.
- If $\Omega$ is countable and $\mathcal{F}$ is the set of all subsets of $\Omega$, then (b) holds automatically and  (a) is also immediate.

---

## 2.2 Examples of Random Variables

- Example 2.2: Rolling two dice:
   - Let  $\Omega = \{(i,j): 1 \leq i, j \leq 6\}$.
   -  $X(i,j) = \max\{i,j\}$ represents the maximum of the two scores.
   -  $Y(i,j) = i + j$ represents the total score.

### Definition 2.3: Probability Mass Function (p.m.f.)

> The probability mass function (p.m.f.) of a discrete random variable $X$ is the function $p_X : \mathbb{R} \rightarrow [0, 1]$ defined by
> $$p_X(x) = P(X=x)$$

- **Key properties of a p.m.f.:**
  -  $p_X(x) = 0$ if $x \notin \text{Im}X$ (i.e. $X(\omega)$ never equals $x$)
  -  $\sum_{x \in \text{Im}X} p_X(x) = 1$ (because the sample space $\Omega$ has to map to something within $\text{Im}X$).
  -  The events $\{ X=x \}$ for each $x\in ImX$ are disjoint.

    
  $$ \sum_{x\in ImX} p_X(x) = \sum_{x \in ImX} P(\{\omega : X(\omega) = x\})  =  P \left( \bigcup_{x \in ImX} \{\omega : X(\omega) = x\}\right) = P(\Omega) = 1$$

- Example 2.4:  Indicator Function
    -   For an event $A \in \mathcal{F}$, we can define $X = 1_A$ where
    $$X(\omega) = \begin{cases}
        1 & \text{if } \omega \in A \\
        0 & \text{otherwise}
    \end{cases}$$
     - $p_X(0) = P(A^c) = 1 - P(A)$
     - $p_X(1) = P(A)$
     - $p_X(x) = 0$ for all $x \notin \{0,1\}$

---

## 2.3 Classical Discrete Distributions

### 1. Bernoulli Distribution

> A random variable $X$ has a Bernoulli distribution with parameter $p$, where $0 \leq p \leq 1$, denoted $X \sim \text{Ber}(p)$, if
> $$P(X=0) = 1-p, \quad P(X=1) = p$$

-  Often $q = 1 - p$ is used.
-  $P(X=x) = 0$ for all other values of $x$.
-  Models the outcome of a single trial with two possibilities (e.g., a coin flip).

### 2. Binomial Distribution

> A random variable $X$ has a binomial distribution with parameters $n$ and $p$, where $n$ is a positive integer and $0 \leq p \leq 1$, denoted $X \sim \text{Bin}(n, p)$, if
>$$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} \quad \text{ for } k=0,1, \ldots, n $$
-   Models the number of successes in $n$ independent Bernoulli trials.
-   $\binom{n}{k} = \frac{n!}{k!(n-k)!}$  is the binomial coefficient.

### 3. Geometric Distribution

> A random variable $X$ has a geometric distribution with parameter $p$, where $0 < p \leq 1$, denoted $X \sim \text{Geom}(p)$, if
>$$ P(X=k) = p(1-p)^{k-1} \quad \text{ for } k=1,2,\ldots $$

-   Models the number of trials needed to get the first success.
-   Alternative Definition: Some define $Y$ as the number of failures before the first success, then  $P(Y = k) = p(1-p)^k$, $k=0, 1, ...$

### 4. Poisson Distribution

> A random variable $X$ has a Poisson distribution with parameter $\lambda \geq 0$, denoted $X \sim \text{Po}(\lambda)$, if
>$$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{ for } k=0, 1, 2,\ldots$$

-   Models the number of events occurring in a fixed interval of time or space (e.g., radioactive decays).
-   It arises as a limit of Binomial distribution Bin$(n, \lambda/n)$ as $n \rightarrow \infty$.

### Exercise 2.5
- **Task:** Verify that each of the distributions above define a valid probability mass function. This requires checking:
    -  $p_X(x) \geq 0$ for all $x$
    - $\sum_x p_X(x) = 1$

-   This can be verified by referring to properties of geometric and exponential sums.

---

## 2.4 Constructing Random Variables

- Given a function $p_X$ satisfying the conditions of a p.m.f., we can always construct a probability space $(\Omega, \mathcal{F}, P)$ and a random variable $X$ with p.m.f. $p_X$
    -   We can let $\Omega = \{x \in \mathbb{R}: p_X(x) \neq 0 \}$, $\mathcal{F}$ to be all subsets of $\Omega$, $P(\{\omega\}) = p_X(\omega)$ and the random variable to be the identity function $X(\omega) = \omega$.

-   Often, there are more natural ways to construct the probability space.
  -   Example:  The Binomial(3, 1/2) distribution is often naturally constructed using three coin tosses with sample space consisting of all possible sequences of 0 and 1's.

---

## 2.5 Expectation

> **Intuitive Idea:** Expectation is the "average value" of a random variable.

### Definition 2.6: Expectation

> The expectation (or expected value or mean) of a discrete random variable $X$ is
>  $$E[X] = \sum_{x \in \text{Im}X} x P(X=x)$$
> provided the sum $\sum_{x \in \text{Im}X} |x|P(X=x)$ converges absolutely. If the sum does not converge absolutely, we say the expectation does not exist.

-   **Explanation:** The sum must converge absolutely to avoid dependence of the result on the order of the terms
-  We say $E[X] = \infty$ if $\sum_{x \in \text{Im}X} x P(X=x)$ diverges and $X$ is a non-negative random variable.

- Examples 2.7
  - Roll of a fair die: $E[X] = 3.5$
   - Indicator function $1_A$: $E[1_A] = P(A)$

### Theorem 2.8: Law of the Unconscious Statistician (LOTUS)

> If $h: \mathbb{R} \rightarrow \mathbb{R}$ is a function and $X$ is a discrete random variable, then
>$$ E[h(X)] = \sum_{x \in \text{Im}X} h(x)P(X=x)$$
> provided the sum converges absolutely.

- **Proof**: Let $A = \{y : y = h(x)$ for some $x \in \text{Im}X\}$.

$$ \begin{aligned}
    \sum_{x \in \text{Im}X} h(x) P(X=x) &= \sum_{y \in A} \sum_{x \in \text{Im}X : h(x) = y} y P(X=x) \\
                               &= \sum_{y \in A} y  \sum_{x \in \text{Im}X : h(x) = y} P(X=x) \\
                               &= \sum_{y \in A} y P(h(X) = y) \\
                               &= E[h(X)].
\end{aligned} $$

- Example 2.9: $E[X^k]$ is the $k$-th moment of $X$.

### Theorem 2.10: Properties of Expectation

> Let $X$ be a discrete random variable such that $E[X]$ exists. Then
>
>   (a) If $X$ is non-negative, then $E[X] \geq 0$
>   (b) If $a, b \in \mathbb{R}$, then $E[aX + b] = aE[X] + b$

- Proof:
    - (a) If $X$ is non-negative then the terms of the expectation sum are non-negative.
    - (b)
      $$ \begin{aligned}
           E[aX+b] &= \sum_x (ax+b)P(X=x) \\
                    &= a\sum_x xP(X=x) + b \sum_x P(X=x) \\
                    &= aE[X] + b
      \end{aligned} $$
---
## 2.6 Variance

> **Intuitive Idea:** Variance measures the "spread" of a random variable around its mean.

### Definition 2.11: Variance
> The variance of a discrete random variable $X$ is defined by
>$$ \text{var}(X) = E[(X-E[X])^2] $$
>provided the expectation exists.

-   If the distribution is concentrated around the mean, the variance will be low. If the distribution is very spread out, the variance will be high.
- A deterministic variable (where the outcome is always the same) will have a variance of 0.
- Another expression for variance:
   $$ \text{var}(X) = E[X^2] - (E[X])^2  $$
-   **Proof**: Let $\mu = E[X]$. Then
$$ \begin{aligned}
    \text{var}(X) &= E[(X-\mu)^2] \\
               &= E[X^2 -2\mu X + \mu^2] \\
               &= E[X^2] - 2\mu E[X] + \mu^2 \\
               &= E[X^2] -2\mu^2 + \mu^2 \\
               &= E[X^2] - \mu^2 \\
               &= E[X^2] - (E[X])^2
\end{aligned} $$

### Theorem 2.12
> Suppose that X is a discrete random variable whose variance exists. Then if $a, b \in \mathbb{R}$, the variance of $Y = aX + b$ is given by
> $$ \text{var}(aX+b) = a^2\text{var}(X) $$

- **Intuition**: Variance is a measure of spread around the mean. Shifting all data points by $b$ doesn't change this spread and therefore does not affect the variance, while scaling the data by $a$ will scale the variance by $a^2$
-  The standard deviation is $\sqrt{\text{var}(X)}$; it has the same units as X and often preferred to variance

---

## 2.7 Conditional Distributions

> **Intuitive Idea:**  Conditional distributions describe how random variables behave when we have partial information.

### Definition 2.13: Conditional Probability Mass Function
> Suppose that $B$ is an event such that $P(B) > 0$. The conditional probability mass function of a discrete random variable $X$ given $B$ is
> $$ P(X=x|B) = \frac{P(\{X=x\} \cap B)}{P(B)}$$
> for $x \in \mathbb{R}$.

-   We can define conditional expectation in a similar fashion:
    $$ E[X|B] = \sum_x x P(X=x|B) $$

### Theorem 2.14: Partition Theorem for Expectations

> If $\{B_1, B_2, \ldots\}$ is a partition of $\Omega$ such that $P(B_i) > 0$ for all $i \geq 1$, then
> $$ E[X] = \sum_{i \geq 1} E[X|B_i] P(B_i) $$
> provided the expectations exist.

-   **Proof**:
    $$ \begin{aligned}
      E[X] &= \sum_x x P(X=x) \\
           &= \sum_x x \sum_i P(X=x|B_i) P(B_i) \quad \text{ (law of total probability)} \\
           &= \sum_i \sum_x x P(X=x|B_i) P(B_i) \\
           &= \sum_i P(B_i) \sum_x x P(X=x|B_i) \\
           &= \sum_i P(B_i) E[X|B_i]
    \end{aligned} $$

- Example 2.15: Number of rolls needed to get a six on a die.

---

## 2.8 Joint Distributions

> **Intuitive Idea:**  Joint distributions describe the behavior of multiple random variables simultaneously.

### Definition 2.16: Joint Probability Mass Function

> Given two discrete random variables $X$ and $Y$, their joint probability mass function is
> $$ p_{X,Y}(x, y) = P(\{X=x\} \cap \{Y=y\}) = P(X=x, Y=y) $$
>  for $x, y \in \mathbb{R}$.

- Key properties:
  - $p_{X,Y}(x, y) \geq 0$
  - $\sum_x \sum_y p_{X,Y}(x, y) = 1$

-   **Marginal Distributions:** Given $p_{X,Y}(x, y)$, we can get the marginal p.m.f. of $X$ or $Y$:
    $$ p_X(x) = \sum_y p_{X,Y}(x, y) \quad \text{and} \quad p_Y(y) = \sum_x p_{X,Y}(x, y) $$

-   **Conditional Probability Mass Function:**
    $$ p_{Y|X=x}(y) = P(Y=y|X=x) = \frac{p_{X,Y}(x,y)}{p_X(x)} \quad \text{if } p_X(x)>0 $$

-   **Conditional Expectation:**
    $$ E[Y|X=x] = \sum_y y p_{Y|X=x}(y) $$

- Example 2.17:  A table is a common way to visualize the joint p.m.f. and calculating the marginals from them

### Definition 2.19: Independence
> Two discrete random variables $X$ and $Y$ are independent if
> $$P(X=x, Y=y) = P(X=x)P(Y=y)$$
> for all $x,y \in \mathbb{R}$
> Alternatively, we can say that $X$ and $Y$ are independent if
> $$p_{X,Y}(x,y) = p_X(x)p_Y(y)$$
> for all $x, y \in \mathbb{R}$

-   In other words,  events $\{X=x\}$ and $\{Y=y\}$ are independent for all choices of $x$ and $y$.

- Example 2.20:  Repeated coin flips

### Theorem 2.21: Linearity of Expectation
> Suppose X and Y are discrete random variables, and a, b are constants.  Then
> $$E[aX + bY] = aE[X] + bE[Y]$$
> provided that E[X] and E[Y] exist.

- **Proof**:
  $$
  \begin{aligned}
    E[aX+bY] &= \sum_x \sum_y (ax+by) p_{X,Y}(x,y) \\
              &= a \sum_x \sum_y x p_{X,Y}(x,y) + b \sum_x \sum_y y p_{X,Y}(x,y) \\
              &= a \sum_x x p_X(x) + b \sum_y y p_Y(y) \\
              &= aE[X] + bE[Y]
  \end{aligned}
  $$
-  This property extends to any finite set of variables:
    $$E[a_1X_1 + \ldots + a_n X_n] = a_1E[X_1] + \ldots + a_nE[X_n]$$
-   Note that independence is not required for linearity of expectation.

### Example 2.22
-   Example of linearity of expectation: Spaghetti bowl looping.

### Theorem 2.23

> If $X$ and $Y$ are independent discrete random variables whose expectations exist, then
> $$ E[XY] = E[X]E[Y] $$
- **Proof**
  $$ \begin{aligned}
      E[XY] &= \sum_x \sum_y xy P(X=x, Y=y) \\
             &= \sum_x \sum_y xy P(X=x)P(Y=y) \qquad \text{(independence)}\\
             &= \sum_x xP(X=x) \sum_y yP(Y=y) \\
             &= E[X] E[Y]
  \end{aligned} $$
### Exercise 2.24
- If $X$ and $Y$ are independent, then var$(X+Y)=$var$(X)$+var$(Y)$

### Covariance
-   The covariance of $X$ and $Y$ is given by
    $$ \text{cov}(X,Y) = E[(X-E[X])(Y-E[Y])] = E[XY] - E[X]E[Y] $$
-   var$(X+Y)$ = var$(X)$ + var$(Y)$ + 2cov$(X,Y)$
-   If $X$ and $Y$ are independent, then cov$(X,Y)=0$
-   However,  cov$(X,Y)=0$ DOES NOT IMPLY $X$ and $Y$ are independent.

### Definition 2.26: Multivariate Probability Mass Function

> We can define the joint probability mass function for multiple discrete random variables $X_1, X_2, \ldots, X_n$ as
>  $$ p_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = P(X_1=x_1, \ldots, X_n=x_n) $$

### Definition 2.27: Independence for a Family of Random Variables
>A family $\{X_i: i \in I\}$ of discrete random variables are independent if for all finite sets $J \subset I$ and all collections $\{A_i: i \in J\}$ of subsets of $\mathbb{R}$:
> $$P\left(\bigcap_{i \in J} \{X_i \in A_i\}\right) = \prod_{i\in J} P(X_i \in A_i)$$
### i.i.d.
-   If $X_1, X_2, ...$ are independent and have the same distribution, we say they are *independent and identically distributed* (i.i.d.).

---
This provides a comprehensive and well-structured revision of Chapter 2 as requested, with mathematical rigor and clarity. Let me know if you have any further questions or require modifications!
