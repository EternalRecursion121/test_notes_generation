# Chapter 5 Revision Notes

Okay, here are the comprehensive revision notes for Chapter 5, following your specifications:

# Chapter 5: Continuous Random Variables

## 5.1 Random Variables and Cumulative Distribution Functions

### Introduction
*   We extend the definition of a random variable beyond discrete values to include continuous outcomes.
*   This allows us to model quantities like lengths, weights, and speeds that naturally take uncountably many values.

### Need for More General Random Variables

*   **Continuous Outcomes:** Many physical quantities are continuous and can't be represented with discrete values, thus requiring a more general framework.
*   **Approximations:** Even for discrete quantities, continuous approximations can simplify modeling. For instance, modeling the proportion of adults contributing to charity can be approximated by a continuous variable on \[0,1].

### Concrete Example: Board Game Spinner

*   Imagine a board game spinner where every angle between 0 and $2\pi$ is equally likely.
*   We want to model the angle $X$ as a random variable.
*   We can't assign positive probability to each angle; instead, we consider probabilities for intervals.
*   The probability of $X$ lying in an interval $[a, b] \subseteq [0, 2\pi)$ is proportional to the length of the interval:
    $$ P(X \in [a, b]) = \frac{b-a}{2\pi} $$
* This is because of the symmetry of uniform distribution

---

### Formal Definition of a Random Variable

> **Definition 5.1.** A random variable $X$ defined on a probability space $(\Omega, \mathcal{F}, P)$ is a function $X : \Omega \to \mathbb{R}$ such that $\{ \omega : X(\omega) \leq x \} \in \mathcal{F}$ for each $x \in \mathbb{R}$.

*  This definition ensures that we can assign a probability to the event that the random variable is less than or equal to some value $x$.
*  This is consistent with our earlier definition of a discrete random variable. 
* If X is a discrete random variable,
    $$ \{ \omega: X(\omega) \leq x \} = \bigcup_{y \leq x : y \in ImX} \{ \omega: X(\omega) = y \} $$
* The image of discrete variable $X$, $ImX$, is countable, this is a countable union of events belonging to $\mathcal{F}$.

---

### Cumulative Distribution Function (CDF)

> **Definition 5.2.** The cumulative distribution function (c.d.f.) of a random variable $X$ is the function $F_X : \mathbb{R} \to [0, 1]$ defined by
> $$ F_X(x) = P(X \leq x) $$

*   The CDF gives the probability that the random variable $X$ takes a value less than or equal to $x$.
*   The collection of these probabilities (for each $x$) is central to understanding the distribution of a random variable.

#### Examples

1.  **Coin Tosses (Discrete)**
    *   Let $X$ be the number of heads in 3 tosses of a fair coin.
    $$P(X=0)=\frac{1}{8}, P(X=1)=\frac{3}{8}, P(X=2)=\frac{3}{8}, P(X=3)=\frac{1}{8}$$
    * The c.d.f is a step function:
        $$
        F_X(x) =
        \begin{cases}
          0 & \text{if } x < 0 \\
          \frac{1}{8} & \text{if } 0 \leq x < 1 \\
          \frac{1}{8} + \frac{3}{8} = \frac{1}{2} & \text{if } 1 \leq x < 2 \\
          \frac{1}{2} + \frac{3}{8} = \frac{7}{8} & \text{if } 2 \leq x < 3 \\
          1 & \text{if } x \geq 3
        \end{cases}
        $$
2.  **Board Game Spinner (Continuous)**
    *   Let $X$ be the angle of the board game spinner.
    $$
        F_X(x) =
        \begin{cases}
          0 & \text{if } x < 0 \\
          \frac{x}{2\pi} & \text{if } 0 \leq x < 2\pi \\
          1 & \text{if } x \geq 2\pi
        \end{cases}
        $$

---

### Properties of CDFs

> **Theorem 5.5.**  The CDF $F_X$ of a random variable $X$ has the following properties:
>
>  1.  $F_X$ is non-decreasing.
>  2.  For $a < b$, $P(a < X \leq b) = F_X(b) - F_X(a)$.
>  3.  As $x \to -\infty$, $F_X(x) \to 0$.
>  4.  As $x \to \infty$, $F_X(x) \to 1$.

#### Proof:

1.  **Non-decreasing:**
    *   If $a < b$, then the event $\{\omega : X(\omega) \leq a\}$ is a subset of $\{\omega : X(\omega) \leq b\}$.
    *   Therefore, $P(X \leq a) \leq P(X \leq b)$, so $F_X(a) \leq F_X(b)$.

2.  **Probability of Interval:**
    *   The event $\{X \leq b\}$ can be decomposed as the disjoint union of $\{X \leq a\}$ and $\{a < X \leq b\}$:
        $$ \{X \leq b\} = \{X \leq a\} \cup \{a < X \leq b\} $$
    *   Thus,  $$P(X \leq b) = P(X \leq a) + P(a < X \leq b)$$, or  $$P(a < X \leq b) = P(X \leq b) - P(X \leq a) = F_X(b) - F_X(a)$$

3.  **Limit as $x \to -\infty$**
    *   Intuitively, the event $X < -\infty$ has probability zero since X can't take values less than $-\infty$.
    *   This is proven using countable additivity in a more rigorous manner.

4.  **Limit as $x \to \infty$**
    *   Intuitively, the event $X \leq \infty$ covers the whole sample space, thus having probability one.
    *   Again, the formal proof needs countable additivity and limits.

> **Remark:** Any function $F$ satisfying conditions 1, 3 and 4 of theorem 5.5, as well as right-continuity, is the cumulative distribution function of some random variable defined on a probability space.

---

## 5.2 Some Classical Distributions

### Introduction

* We focus on the case where the CDF is differentiable almost everywhere, except possibly at a finite number of isolated points.
* In this case, we define a probability density function.

---

### Probability Density Function (PDF)

> **Definition 5.6.** A continuous random variable $X$ is a random variable whose c.d.f. satisfies
> $$ F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(u) du $$
> where $f_X: \mathbb{R} \to \mathbb{R}$ is a function (the probability density function) such that:
>
> (a) $f_X(u) \geq 0$ for all $u \in \mathbb{R}$
> (b) $\int_{-\infty}^{\infty} f_X(u) du = 1$

*   $f_X(x)$ is called the probability density function (PDF) of $X$.
*   It is not a probability! It is only a density.
*   It allows us to calculate probabilities as area under the curve.
*   We often denote it as just $f(x)$ when $X$ is clear from context.

> **Remark 5.7.** The functions $f_X$ which might serve as a PDF are not completely arbitrary, but must satisfy properties such as smoothness, and can have, at most, a countable number of jumps.

> **Remark 5.8.** The Fundamental Theorem of Calculus states that, at any point $x$ where $f_X$ is continuous:
> $$ \frac{d F_X(x)}{dx} = f_X(x) $$

---

#### Example 5.9
*   Suppose $X$ has the c.d.f:
    $$
        F_X(x) =
        \begin{cases}
          0 & \text{if } x < 0 \\
          1 - e^{-x} & \text{if } x \geq 0
        \end{cases}
    $$
*   The PDF is given by:
     $$
        f_X(x) =
        \begin{cases}
          0 & \text{if } x < 0 \\
          e^{-x} & \text{if } x \geq 0
        \end{cases}
    $$
* Notice that $f_X(0) = 1$, yet $f_X$ is not a probability.
* The c.d.f $F_X$ is smooth at 0 but not differentiable as the derivatives from the left and right are different. 
* Everywhere else we have $$F_X'(x) = f_X(x)$$
---

### Classical Continuous Distributions

1.  **Uniform Distribution:**
    *   $X \sim U[a, b]$ has PDF:
      $$
        f_X(x) =
        \begin{cases}
          \frac{1}{b-a} & \text{for } a \leq x \leq b \\
          0 & \text{otherwise}
        \end{cases}
      $$
2.  **Exponential Distribution:**
    *   $X \sim Exp(\lambda)$ has PDF:
         $$
        f_X(x) =
        \begin{cases}
          \lambda e^{-\lambda x} & \text{for } x \geq 0 \\
          0 & \text{for } x < 0
        \end{cases}
        $$
     *   Used to model lifetimes, waiting times, etc.

3.  **Gamma Distribution:**
    *  $X \sim Gamma(\alpha, \lambda)$ has PDF:
        $$
        f_X(x) =
        \begin{cases}
          \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x} & \text{for } x \geq 0 \\
          0 & \text{for } x < 0
        \end{cases}
        $$
      where the Gamma function $\Gamma(\alpha)$ is defined as:
       $$\Gamma(\alpha) = \int_{0}^\infty u^{\alpha-1} e^{-u} du$$
    * A generalisation of the exponential distribution, and the chi-squared distribution.

4.  **Normal (Gaussian) Distribution:**
    *  $X \sim N(\mu, \sigma^2)$ has PDF:
    $$ f_X(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \quad x \in \mathbb{R} $$
    * The most important distribution in all of statistics.

---

### Important Note on PDF vs. PMF
*   Analogous, but PDFs are densities, not probabilities.
    |                             | Probability Density Function (Continuous)  | Probability Mass Function (Discrete)  |
    |-----------------------------|------------------------------------------|------------------------------------|
    | Non-negativity             | $f_X(x) \ge 0 \ \forall x \in \mathbb{R}$ |  $p_X(x) \ge 0 \ \forall x \in \mathbb{R}$ |
    | Summation/Integration      | $\int_{-\infty}^{\infty} f_X(x) dx = 1$  | $\sum_{x \in ImX} p_X(x) = 1$        |
    | Cumulative Distribution   |  $F_X(x) = \int_{-\infty}^{x} f_X(u)du$  | $F_X(x) = \sum_{u \le x : u \in ImX} p_X(u)$|

> **WARNING:** $f_X(x)$ is *not* a probability. It's a probability density, meaning it has to be integrated to give the correct probability.

---

### Relating PDF to Probability
*  For a small interval $\epsilon > 0$, the probability that $X$ falls between $x$ and $x + \epsilon$ is approximately $f_X(x)\epsilon$, based on Taylor's theorem.
* The following theorem makes the link between PDF and probability explicit.

> **Theorem 5.12.**  If $X$ is a continuous random variable with PDF $f_X$, then
>
> 1. $P(X = x) = 0$ for all $x \in \mathbb{R}$.
> 2. For $a < b$, $P(a \leq X \leq b) = \int_a^b f_X(x) dx$.

#### Proof:

1. **Zero Probability for Individual Values:**
    * Suppose that for some $x$,  $P(X = x) = p > 0$, so that for all $n \ge 1$,  $P(x - \frac{1}{n} < X \leq x) \ge p$.
    * But $$P(x - \frac{1}{n} < X \leq x) = F_X(x) - F_X(x-\frac{1}{n})$$
    * Since $F_X$ is a continuous function, it follows that
    $$\lim_{n\rightarrow \infty} \left(F_X(x) - F_X(x-\frac{1}{n}) \right) = 0 $$
    which contradicts the fact that $P(x - \frac{1}{n} < X \leq x) \ge p >0$ for all $n \ge 1$.

2. **Probability of Interval:**
    * The fact that $P(a \le X \le b) = \int_a^b f_X(x) dx$ follows directly from the fact that:
    $$P(a \le X \le b) = F_X(b) - F_X(a) = \int_{-\infty}^b f_X(x) dx - \int_{-\infty}^a f_X(x) dx = \int_a^b f_X(x) dx$$

---

> **Remark 5.13:** Random variables can be neither discrete nor continuous.
> For example, flipping a coin. If it is heads, then sample uniformly from $[0,1]$; otherwise set X = 1/2.

---
## 5.3 Expectation

### Definition of Expectation

* We want to generalize the definition of expectation to continuous random variables.

> **Definition 5.16.** Let $X$ be a continuous random variable with probability density function $f_X$. The expectation (or mean) of $X$ is defined as
> $$ E[X] = \int_{-\infty}^{\infty} x f_X(x) dx $$
>
> Provided the integral exists (i.e., $\int_{-\infty}^{\infty} |x| f_X(x) dx < \infty$)

### Expectation of a Function

> **Theorem 5.17.** Let $X$ be a continuous random variable with PDF $f_X$, and let $h$ be a function from $\mathbb{R}$ to $\mathbb{R}$. Then
> $$ E[h(X)] = \int_{-\infty}^{\infty} h(x) f_X(x) dx $$
>
> Provided the integral exists (i.e., $\int_{-\infty}^{\infty} |h(x)| f_X(x) dx < \infty$)

#### Proof (Idea, Non-Examinable)

1.  If $X$ is a non-negative continuous random variable, we have:

    $$ E[X] = \int_0^\infty x f_X(x) dx = \int_0^\infty \int_0^x f_X(x) dy dx = \int_0^\infty \int_y^\infty f_X(x) dx dy $$
    $$= \int_0^\infty P(X > y) dy $$

2.  Generalize to non-negative continuous random variables $h(X)$, by substitution.

---

### Variance

*   Variance for continuous random variables is defined analogously to the discrete case.

>  **Definition.** The variance of a continuous random variable is given by:
> $$Var(X) = E[(X - E[X])^2]$$
>
> Provided that $E[X^2] < \infty$

*   The variance can be calculated by the following formula:

    $$Var(X) = E[X^2] - (E[X])^2$$

### Linearity of Expectation

> **Theorem 5.18.** Suppose $X$ is a continuous random variable with PDF $f_X$. Then, for $a, b \in \mathbb{R}$,
>  1. $E[aX + b] = a E[X] + b$.
>  2. $Var(aX + b) = a^2 Var(X)$.

#### Proof:

1.  **Linearity of Expectation:**
    $$ E[aX + b] = \int_{-\infty}^{\infty} (ax + b)f_X(x)dx = a\int_{-\infty}^{\infty} xf_X(x)dx + b\int_{-\infty}^{\infty} f_X(x)dx = aE[X]+b $$

2. **Variance of Linear Transformation:**
    $$ Var(aX + b) = E[((aX + b) - E[aX + b])^2] = E[(aX + b - aE[X] - b)^2] = E[(a(X-E[X]))^2]$$
    $$= E[a^2(X-E[X])^2] = a^2 E[(X-E[X])^2] = a^2Var(X)$$

---

#### Example 5.19
* For  $X \sim N(\mu, \sigma^2)$, we have that
  *  $X$ has same distribution as $\mu + \sigma Z$, where $Z \sim N(0,1)$.
  *  $X$ has c.d.f $F_X(x) = \Phi \left( \frac{x-\mu}{\sigma}\right)$, where $\Phi$ is the standard normal c.d.f.
  *  $E[X] = \mu$.
  *  $Var(X) = \sigma^2$.

### Examples of Expectation and Variance Calculations

> **Exercise 5.20.** Show that if $X \sim U[a, b]$ and $Y \sim Exp(\lambda)$ then
>
>  1. $E[X] = \frac{a+b}{2}$,  $Var(X) = \frac{(b-a)^2}{12}$
>  2. $E[Y] = \frac{1}{\lambda}$, $Var(Y) = \frac{1}{\lambda^2}$

#### Example 5.21
*   $X \sim Gamma(2,2)$ with density
    $$
        f_X(x) =
        \begin{cases}
          4xe^{-2x} & \text{if } x \ge 0 \\
          0 & \text{if } x < 0
        \end{cases}
    $$
   * $$E[X] = \int_0^\infty x\cdot 4xe^{-2x} dx = \int_0^\infty 4x^2 e^{-2x} dx = 1$$
    $$E\left[\frac{1}{X}\right] = \int_0^\infty \frac{1}{x} \cdot 4xe^{-2x} dx = \int_0^\infty 4e^{-2x} dx = 2$$

> **WARNING:** In general, $E[\frac{1}{X}] \neq \frac{1}{E[X]}$.

---
## 5.4 Examples of Functions of Continuous Random Variables

### Introduction
* We look into how to derive the distribution of a transformation of a continuous random variable.

#### Example 5.22
*   $R$ is the distance of a tree to its nearest neighbour, with the pdf $f_R(r) = re^{-r^2/2}$ for $r \ge 0$ and $0$ otherwise.
* Let $A = \pi R^2$ be the area of the tree-free circle.
* Let's find the distribution of the area.
*   We have that $F_R(r) = 1-e^{-r^2/2}$. For $a \ge 0$, we have:
   $$ F_A(a) = P(A \le a) = P(\pi R^2 \le a) = P(R \le \sqrt{\frac{a}{\pi}}) = F_R(\sqrt{\frac{a}{\pi}}) = 1 - e^{-\frac{a}{2\pi}}$$
  *   Differentiating the c.d.f. we get the PDF:
      $$ f_A(a) = \frac{1}{2\pi} e^{-a/(2\pi)} $$
     * Thus $A$ is distributed exponentially with rate parameter $1/(2\pi)$
### Transformation Theorem

> **Theorem 5.24.** Suppose $X$ is a continuous random variable with PDF $f_X$ and that $h: \mathbb{R} \to \mathbb{R}$ is a differentiable function with $\frac{dh(x)}{dx} > 0$ for all $x$ (i.e., strictly increasing). Let $Y = h(X)$. Then $Y$ is a continuous random variable with PDF
>
>  $$ f_Y(y) = f_X(h^{-1}(y)) \left| \frac{dh^{-1}(y)}{dy} \right| $$
>
>  where $h^{-1}$ is the inverse of $h$.

#### Proof:

*   Since $h$ is strictly increasing, $h(X) \le y$ if and only if $X \le h^{-1}(y)$.
*   So, the CDF of $Y$ is:
    $$ F_Y(y) = P(h(X) \le y) = P(X \le h^{-1}(y)) = F_X(h^{-1}(y)) $$
*   Differentiating, we get:
  $$f_Y(y) = f_X(h^{-1}(y)) \frac{dh^{-1}(y)}{dy}$$
* A similar result holds for strictly decreasing $h$.
* When h is not monotonic, the situation is more complex and you should deal with it case-by-case basis.

#### Example 5.25
* A point is chosen uniformly on the circumference of the unit circle. Let $\Theta$ be the angle, so $\Theta \sim U[0, 2\pi)$.
* Let $X=\cos{\Theta}$ be the x-coordinate.
* The c.d.f of $\Theta$ is:
    $$
        F_\Theta(\theta) =
        \begin{cases}
          0 & \text{for } \theta < 0 \\
         \frac{\theta}{2\pi} & \text{for } 0 \le \theta \le 2\pi \\
         1 & \text{for } \theta > 2\pi
        \end{cases}
    $$
* Then, for $-1\le x\le 1$, we have
    $$F_X(x) = P(\cos{\Theta} \le x) = P(\arccos{x} \le \Theta \le 2\pi-\arccos{x})$$
    $$ = F_\Theta(2\pi-\arccos{x}) - F_\Theta(\arccos{x}) =  1 - \frac{\arccos{x}}{\pi}$$
* Differentiating with respect to $x$, we obtain that, for $-1 < x < 1$,
    $$ f_X(x) = \frac{1}{\pi \sqrt{1-x^2}} $$

---
## 5.5 Joint Distributions

### Introduction
* We often need to consider several random variables at the same time. This leads to joint distributions.

### Joint Cumulative Distribution Function

> **Definition** For random variables $X$ and $Y$, the joint cumulative distribution function (CDF) is defined by:
> $$ F_{X,Y}(x, y) = P(X \leq x, Y \leq y) $$
> for $x, y \in \mathbb{R}$

*   Similar to the single-variable case, this function is non-decreasing in each of its arguments.

### Joint Density Function

> **Definition 5.26.** Let $X$ and $Y$ be random variables such that
> $$ F_{X,Y}(x, y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u, v) du dv $$
> for some function $f_{X,Y}: \mathbb{R}^2 \to \mathbb{R}$, called the joint probability density function,  satisfying:
>  (a) $f_{X,Y}(u, v) \geq 0$ for all $u, v \in \mathbb{R}$
>  (b) $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(u, v) du dv = 1$

*   The joint PDF $f_{X,Y}(x, y)$ is not a probability; it is integrated to obtain probabilities.
*  If $f_{X,Y}$ is sufficiently smooth at $(x,y)$, then
  $$\frac{\partial^2}{\partial x \partial y} F_{X,Y}(x,y) = f_{X,Y}(x,y)$$
*   For a nice region $B \subset \mathbb{R}^2$:
$$ P((X,Y) \in B) = \iint_B f_{X,Y}(x, y) dx dy $$
*   Specifically for rectangular region, where $B = \{(x,y):a < x < b, c < y < d\}$

> **Theorem 5.27.** For a pair of jointly continuous random variables $X$ and $Y$, we have:
>
> $$ P(a< X \leq b, c < Y \leq d) = \int_c^d \int_a^b f_{X,Y}(x, y) dx dy $$
>
> for $a < b$ and $c < d$

#### Proof:

$$P(a < X \leq b, c < Y \leq d) = P(X \le b, Y \le d) - P(X \le a, Y \le d) + P(X \le a, Y \le c) - P(X \le b, Y \le c)$$

  $$= F_{X,Y}(b,d) - F_{X,Y}(a,d) + F_{X,Y}(a,c) - F_{X,Y}(b,c) = \int_a^b \int_c^d f_{X,Y}(x,y) dy dx$$

### Marginal Densities

>  **Theorem 5.28.** Suppose X and Y are jointly continuous with joint density $f_{X,Y}$. Then X is a continuous random variable with density:
> $$ f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dy$$
>  Similarly, Y is a continuous random variable with density
>  $$ f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx$$
> These are the marginal densities of X and Y.

#### Proof:
If $f_X$ is defined by $f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x,y) dy$, then we have
    $$\int_{-\infty}^x f_X(u) du = \int_{-\infty}^x \int_{-\infty}^\infty f_{X,Y}(u,y) dy du = P(X \leq x)$$
    which proves that $X$ has the density $f_X$. The case for $f_Y$ is analogous.

---
#### Example 5.29
*   Suppose
     $$
       f_{X,Y}(x, y) =
        \begin{cases}
         \frac{1}{4}(x+y) & 0\leq x \leq 1, 1\leq y\leq 2 \\
         0 & \text{otherwise}
        \end{cases}
    $$
*   The marginal densities are:
     $$
        f_X(x) = \int_1^2 \frac{1}{4}(x+y) dy = \frac{1}{4} \left( xy + \frac{y^2}{2} \right)\bigg\rvert_1^2 = \frac{1}{4}(x+\frac{3}{2})
     $$
        for $0 \le x \le 1$
     $$
       f_Y(y) = \int_0^1 \frac{1}{4}(x+y) dx = \frac{1}{4} \left( \frac{x^2}{2} + xy \right)\bigg\rvert_0^1 = \frac{1}{4}(\frac{1}{2}+y)
     $$
        for $1 \le y \le 2$

### Independence of Random Variables
> **Definition 5.30.** Jointly continuous random variables X and Y with joint density $f_{X,Y}$ are independent if
> $$ f_{X,Y}(x, y) = f_X(x) f_Y(y) $$
> for all $x, y \in \mathbb{R}$. Likewise, $X_1, X_2, \ldots, X_n$ are independent if
> $$ f_{X_1, X_2, \ldots, X_n}(x_1, x_2, \ldots, x_n) = f_{X_1}(x_1) f_{X_2}(x_2) \cdots f_{X_n}(x_n) $$
> for all $x_1, x_2, \ldots, x_n \in \mathbb{R}$.

*   For independent random variables, the joint CDF is a product of marginal CDFs:
    $$ F_{X,Y}(x, y) = F_X(x) F_Y(y) $$

#### Example 5.31
*   Revisiting the setup of example 5.29, we note that
  $$\frac{1}{4} (x+y) \neq \frac{1}{4} (x + \frac{3}{2}) \frac{1}{4} (y+\frac{1}{2}) $$
 *   Therefore $X$ and $Y$ are not independent.

---
### 5.5.1 Expectation

#### Expectation of a Function of Two Variables

> **Theorem 5.32.** The expectation of a function of jointly continuous random variables $X$ and $Y$ is given by:
>  $$ E[h(X,Y)] = \int_{-\infty}^\infty \int_{-\infty}^\infty h(x,y) f_{X,Y}(x,y) dx dy $$
>
> Provided that $\int_{-\infty}^\infty \int_{-\infty}^\infty |h(x,y)| f_{X,Y}(x,y) dx dy < \infty$

#### Covariance

*   The covariance is defined as:
 $$ cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$

#### Linearity of Expectation

> **Exercise 5.33.** Check that:
>  1. $E[aX + bY] = aE[X] + bE[Y]$
>  2. $Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X,Y)$

> **Remark 5.34:** The rules for calculating expectations, variances, covariances, are exactly the same as for the discrete case.

#### Example 5.35
*   Consider the bivariate normal distribution with joint density:
 $$f_{X,Y}(x,y) = \frac{1}{2\pi\sqrt{1-\rho^2}} \exp \left( -\frac{1}{2(1-\rho^2)} (x^2-2\rho xy+y^2) \right)$$
    for $x, y \in \mathbb{R}$ and $-1 < \rho < 1$.
*   The marginal distributions are $X \sim N(0, 1)$ and $Y \sim N(0, 1)$.
* The covariance of X and Y is $Cov(X,Y)=\rho$

#### Proof:
*    $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$
 *    $E[X] = E[Y] = 0$
 *    $E[XY] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy f_{X,Y}(x,y) dy dx = \rho$

> **Remark:** For bivariate normal distributions, $X$ and $Y$ are independent if and only if their covariance is 0. This is a special property of normal distributions and is not true for general random variables.

---
Let me know if you have any other requests or adjustments.
