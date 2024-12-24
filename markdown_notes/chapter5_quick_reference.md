# Chapter 5 Quick Reference

Okay, let's break down Chapter 5 and create that quick reference.

## Quick Reference

**Definitions**

*   **Random Variable (General):** A function $X: \Omega \rightarrow \mathbb{R}$ such that $\{\omega: X(\omega) \leq x\} \in \mathcal{F}$ for each $x \in \mathbb{R}$, where $(\Omega, \mathcal{F}, P)$ is a probability space.
*   **Cumulative Distribution Function (c.d.f.):** The function $F_X: \mathbb{R} \rightarrow [0,1]$ defined by $F_X(x) = P(X \leq x)$.
*   **Continuous Random Variable:**  A random variable whose c.d.f. satisfies
    $$F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(u)du$$
     where $f_X: \mathbb{R} \rightarrow \mathbb{R}$ is a function such that
    (a) $f_X(u) \geq 0$ for all $u \in \mathbb{R}$, and
    (b) $\int_{-\infty}^{\infty} f_X(u)du = 1$.
    $f_X$ is called the *probability density function (p.d.f.)*.
*   **Expectation (Mean):** The expectation of a continuous random variable $X$ is
    $$E[X] = \int_{-\infty}^{\infty} xf_X(x)dx$$
    provided the integral is absolutely convergent.
*   **Expectation of a function:**  The expectation of a function $h(X)$ of a continuous random variable $X$ is
    $$E[h(X)] = \int_{-\infty}^{\infty} h(x)f_X(x)dx$$
    provided the integral is absolutely convergent.
*   **Variance:** The variance of a random variable $X$ is
    $$var(X) = E[(X - E[X])^2]$$
*   **Joint c.d.f.:** For random variables $X$ and $Y$, the joint c.d.f. is
    $$F_{X,Y}(x,y) = P(X \leq x, Y \leq y)$$
*  **Jointly Continuous Random Variables:** Random variables $X$ and $Y$ where
$$F_{X,Y}(x,y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u,v)dvdu$$
where $f_{X,Y}: \mathbb{R}^2 \rightarrow \mathbb{R}$ such that
(a) $f_{X,Y}(u,v) \geq 0$ for all $u,v \in \mathbb{R}$
(b) $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(u,v)dudv=1$.
$f_{X,Y}$ is the *joint density function*.
*   **Joint Expectation:** For a function $h(X,Y)$,
    $$E[h(X,Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} h(x,y) f_{X,Y}(x,y)dxdy$$
*   **Covariance:** The covariance of two random variables $X$ and $Y$ is
     $$cov(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
*   **Marginal Density:** The marginal density of X in a joint distribution is given by
    $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)dy$$
   Similarly, the marginal density of Y is
   $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)dx$$
*   **Independent Random Variables:**  Random variables $X$ and $Y$ are independent if their joint density factors:
    $$f_{X,Y}(x,y) = f_X(x)f_Y(y)$$
    for all $x, y \in \mathbb{R}$

**Theorems**

*   **Theorem 5.5 (Properties of c.d.f.):**  If $F_X$ is the c.d.f. of a random variable $X$, then
     1. $F_X$ is non-decreasing.
     2. $P(a < X \leq b) = F_X(b) - F_X(a)$ for $a<b$.
     3. As $x \to -\infty$, $F_X(x) \to 0$.
     4. As $x \to \infty$, $F_X(x) \to 1$.
*   **Theorem 5.12:** If $X$ is a continuous r.v. with p.d.f. $f_X$ then $P(X=x) = 0$ for all $x \in \mathbb{R}$, and $P(a \leq X \leq b) = \int_a^b f_X(x) dx$ for all $a<b$.
*   **Theorem 5.17:**  If X is a continuous r.v. with p.d.f. $f_X$ and $h: \mathbb{R} \to \mathbb{R}$, then
     $$E[h(X)] = \int_{-\infty}^{\infty} h(x) f_X(x)dx$$
     provided the integral is absolutely convergent.
*   **Theorem 5.18:** If $a, b \in \mathbb{R}$ then $E[aX+b]=aE[X]+b$ and $var(aX+b)=a^2var(X)$.
*   **Theorem 5.24:** If $X$ is continuous with density $f_X$, and $h: \mathbb{R} \to \mathbb{R}$ is differentiable with $h'(x)>0$ for all $x$, then $Y=h(X)$ is continuous with p.d.f.
    $$f_Y(y) = f_X(h^{-1}(y)) \frac{d}{dy}h^{-1}(y)$$
*  **Theorem 5.27:** If $X$ and $Y$ are jointly continuous then
    $$P(a< X <b, c < Y <d) = \int_c^d \int_a^b f_{X,Y}(x,y)dxdy$$
*   **Theorem 5.32:**
$$E[h(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} h(x,y) f_{X,Y}(x,y)dxdy$$

**Key Relationships and Implications**

*   **Derivative of c.d.f.:** If $F_X$ is differentiable at $x$, then $F'_X(x) = f_X(x)$.
*   **Variance:**  $var(X) = E[X^2] - (E[X])^2$.
*   **Linearity of Expectation:**  $E[aX + bY] = aE[X] + bE[Y]$.
*   **Variance of Sum:**  $var(X + Y) = var(X) + var(Y) + 2cov(X,Y)$.
*   **Independent RVs:** If $X$ and $Y$ are independent, then $cov(X, Y) = 0$. (However, the converse is not true for all random variables.)
* **Standard Bivariate Normal:** $X$ and $Y$ are independent in the standard bivariate normal if and only if $cov(X,Y) = 0$.
*   **Marginal Density Relationship:**  The joint density determines the marginal densities.
    $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)dy$$
   $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)dx$$

**Important Special Cases**

*   **Uniform Distribution:** $X \sim U[a,b]$ with $f_X(x) = \frac{1}{b-a}$ for $a \leq x \leq b$.
*   **Exponential Distribution:** $X \sim Exp(\lambda)$ with $f_X(x) = \lambda e^{-\lambda x}$ for $x \geq 0$.
*   **Gamma Distribution:**  $X \sim Gamma(\alpha, \lambda)$ with $f_X(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$ for $x \geq 0$.
*   **Normal Distribution:** $X \sim N(\mu,\sigma^2)$ with $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ for $x\in\mathbb{R}$.
*   **Standard Normal:** $Z\sim N(0,1)$
*  **Chi-squared:** $\chi^2_d = Gamma(d/2, 1/2)$
*   **Standard Bivariate Normal:**  $f_{X,Y}(x,y) = \frac{1}{2\pi\sqrt{1-\rho^2}} exp(-\frac{1}{2(1-\rho^2)}(x^2-2\rho xy+y^2))$

**Key Conditions and Assumptions**

*   **Absolute Convergence:**  Expectation formulas are valid if the relevant integrals or sums are absolutely convergent.
*   **Smoothness of p.d.f.:** For derivatives of c.d.f.'s to equal p.d.f.'s, the p.d.f. must be continuous.
*   **Differentiability of h:** In Theorem 5.24, the function $h$ must be differentiable with a positive (or negative) derivative everywhere.
*  **Nice Sets:** When dealing with probability, the sets need to be measurable.

## Common Patterns and Techniques

**Key Proof Techniques**

*   **Monotone Convergence Theorem:** Used when proving that as $x\to\infty$, $F_X(x) \to 1$ or as $x \to -\infty, F_X(x)\to 0$, and when changing the order of integration.
*   **Calculus of Integrals:** Using the fundamental theorem of calculus to relate c.d.f.'s and p.d.f.'s.
*   **Change of Variables:**  Used for finding distributions of functions of random variables.
*   **Integration by Parts:** Used frequently in integration and expectation calculations.
*   **Contradiction:** Used to show that a random variable cannot have $P(X=x) > 0$.
*   **Chain Rule:** Used when changing the variable in a c.d.f.

**Common Problem-Solving Strategies**

*   **Find the c.d.f. first:** For functions of a random variable, start by finding the c.d.f. of the new random variable.
*   **Use symmetry:** Often simplifying expectation calculation for even or odd functions.
*   **Utilize linearity of expectation:** To compute means of sums of RVs.
*   **Break down the region:** When finding probabilities on rectangular regions use the fact that
$$P(a< X <b, c < Y <d) = \int_c^d \int_a^b f_{X,Y}(x,y)dxdy$$
*   **Identify densities:** When evaluating complex integrals, recognize known p.d.f.'s to simplify.
*   **Express integrals in terms of expected values:**  If possible, express integrals using $E[X]$.

**Important Connections Between Concepts**

*   **General R.V. to Discrete/Continuous:** General Random Variable is a more general notion of discrete and continuous R.V.
*   **c.d.f and p.d.f:** The c.d.f. is obtained by integrating the p.d.f., and the derivative of the c.d.f. gives the p.d.f.
*   **Density and Probability:** The area under the p.d.f. curve between $a$ and $b$ represents the probability $P(a \leq X \leq b)$.
*   **Covariance and Independence:** Zero covariance does not imply independence in general, but independence does imply zero covariance. In standard bivariate normal distributions zero covariance implies independence.

**Typical Applications of Theorems**

*   **Theorem 5.5 (Properties of c.d.f.):** Helps establish the properties of any random variable.
*   **Theorem 5.12:** Justifies that one can integrate to calculate probability of continuous R.V.
*   **Theorem 5.17:** Used to compute expectations of functions of random variables.
*   **Theorem 5.18:** Used to compute expected value and variance of linear transformations of random variables
*   **Theorem 5.24:** Used to find distribution of function of a random variable
*   **Theorem 5.27:** Used to calculate the probability over rectangular regions for joint distributions.
*   **Theorem 5.32:** Used to calculate expected value of functions of jointly distributed random variables

Let me know if you'd like any of these points expanded upon!
