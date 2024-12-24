# Chapter 5 Flashcards

## Flashcards

### Basic Cards
START
Basic
What is a continuous random variable?
Back: A continuous random variable is a random variable whose cumulative distribution function (c.d.f.) can be expressed as an integral of a probability density function (p.d.f.).
Tags: chapter5, continuous_random_variable, definition
END

START
Basic
What is the cumulative distribution function (c.d.f.) of a random variable X?
Back: The c.d.f. of a random variable X is a function $F_X(x) = P(X \leq x)$.
Tags: chapter5, cdf, definition
END

START
Basic
What does it mean for a c.d.f. to be non-decreasing?
Back: A c.d.f. is non-decreasing, which means that if $a < b$, then $F_X(a) \leq F_X(b)$.
Tags: chapter5, cdf, property
END

START
Basic
What is the probability $P(a < X \le b)$ in terms of the c.d.f. $F_X$?
Back: $P(a < X \leq b) = F_X(b) - F_X(a)$
Tags: chapter5, cdf, probability
END

START
Basic
What is the limiting value of $F_X(x)$ as $x$ approaches $-\infty$?
Back: $\lim_{x\to-\infty} F_X(x) = 0$
Tags: chapter5, cdf, property
END

START
Basic
What is the limiting value of $F_X(x)$ as $x$ approaches $\infty$?
Back: $\lim_{x\to\infty} F_X(x) = 1$
Tags: chapter5, cdf, property
END

START
Basic
What is the probability density function (p.d.f.) of a continuous random variable X?
Back: The p.d.f. $f_X(x)$ is a function such that $F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(u) \, du$.
Tags: chapter5, pdf, definition
END

START
Basic
What is the value of $\int_{-\infty}^{\infty} f_X(u) \, du$?
Back: $\int_{-\infty}^{\infty} f_X(u) \, du = 1$
Tags: chapter5, pdf, property
END

START
Basic
When is the derivative of the c.d.f equal to the p.d.f?
Back:  The derivative of the c.d.f. $F_X'(x) = f_X(x)$ at any point where $f_X$ is continuous.
Tags: chapter5, pdf, cdf, relationship
END

START
Basic
If X is a continuous random variable, what is P(X=x) for any real number x?
Back: If X is a continuous random variable, P(X=x) = 0 for any real number x
Tags: chapter5, continuous_random_variable, property
END

START
Basic
What is the expectation $E[X]$ of a continuous random variable X with p.d.f. $f_X(x)$?
Back: $E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$
Tags: chapter5, expectation, definition
END

START
Basic
What is the expectation $E[h(X)]$ of a function of a continuous random variable X with p.d.f. $f_X(x)$?
Back: $E[h(X)] = \int_{-\infty}^{\infty} h(x) f_X(x) \, dx$
Tags: chapter5, expectation, definition
END

START
Basic
What is the variance of a continuous random variable $X$?
Back: $var(X) = E[(X-E[X])^2] = E[X^2] - (E[X])^2$
Tags: chapter5, variance, definition
END

START
Basic
What is the variance of $aX+b$ given a random variable X and constants a,b?
Back: $var(aX+b) = a^2 var(X)$
Tags: chapter5, variance, property
END

START
Basic
What is $E[aX + b]$ given a random variable $X$ and constants $a$, $b$?
Back: $E[aX+b] = aE[X] + b$
Tags: chapter5, expectation, property
END

START
Basic
What is the uniform distribution on an interval [a,b]?
Back: A random variable X has uniform distribution on [a,b] if its pdf is $f_X(x) = \frac{1}{b-a}$ for $a\leq x \leq b$ and $0$ otherwise.
Tags: chapter5, uniform_distribution, definition
END

START
Basic
What is the exponential distribution with parameter $\lambda$?
Back:  A random variable X has exponential distribution with parameter $\lambda$ if its pdf is $f_X(x) = \lambda e^{-\lambda x}$ for $x\geq 0$ and $0$ otherwise.
Tags: chapter5, exponential_distribution, definition
END

START
Basic
What is the gamma distribution with parameters $\alpha, \lambda$?
Back: A random variable X has gamma distribution with parameters $\alpha, \lambda$ if its pdf is $f_X(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-\lambda x}$ for $x \geq 0$ and 0 otherwise.
Tags: chapter5, gamma_distribution, definition
END

START
Basic
What is the normal distribution with mean $\mu$ and variance $\sigma^2$?
Back: A random variable X has normal distribution with mean $\mu$ and variance $\sigma^2$ if its pdf is $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(x-\mu)^2}{2\sigma^2})$ for $x\in \mathbb{R}$.
Tags: chapter5, normal_distribution, definition
END

START
Basic
What is the standard normal distribution?
Back: The standard normal distribution is the normal distribution with $\mu=0$ and $\sigma^2=1$, denoted as N(0,1).
Tags: chapter5, normal_distribution, standard
END

START
Basic
What is a joint cumulative distribution function (joint c.d.f.) $F_{X,Y}(x,y)$?
Back: The joint c.d.f. $F_{X,Y}(x,y)$ is given by $P(X \le x, Y \le y)$.
Tags: chapter5, joint_distributions, cdf, definition
END

START
Basic
What is a joint density function (joint p.d.f.) $f_{X,Y}(x,y)$?
Back:  The joint p.d.f. $f_{X,Y}(x,y)$ is a function such that $F_{X,Y}(x,y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u,v) \, dv \, du$.
Tags: chapter5, joint_distributions, pdf, definition
END

START
Basic
How do you find the marginal density $f_X(x)$ from the joint density $f_{X,Y}(x,y)$?
Back: $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dy$
Tags: chapter5, joint_distributions, marginal_density
END

START
Basic
How do you find the marginal density $f_Y(y)$ from the joint density $f_{X,Y}(x,y)$?
Back: $f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dx$
Tags: chapter5, joint_distributions, marginal_density
END

START
Basic
When are two random variables $X$ and $Y$ independent?
Back: Random variables $X$ and $Y$ are independent if their joint density factorizes as $f_{X,Y}(x,y) = f_X(x) f_Y(y)$.
Tags: chapter5, joint_distributions, independence
END

### Cloze Cards
START
Cloze
A continuous random variable X is a random variable whose c.d.f. $F_X(x)$ can be expressed as ${{c1::$\int_{-\infty}^{x} f_X(u) \, du$}} $ for some probability density function $f_X(x)$.
Tags: chapter5, continuous_random_variable, definition
END

START
Cloze
The cumulative distribution function $F_X(x)$ is defined as ${{c1::$P(X \leq x)$}}$.
Tags: chapter5, cdf, definition
END

START
Cloze
If $a < b$, then the c.d.f. $F_X$ satisfies ${{c1::F_X(a) \leq F_X(b)}}$.
Tags: chapter5, cdf, property
END

START
Cloze
The probability $P(a < X \leq b)$ is equal to ${{c1::F_X(b) - F_X(a)}}$.
Tags: chapter5, cdf, probability
END

START
Cloze
The limiting value of the c.d.f. as x approaches $-\infty$ is ${{c1::0}}$.
Tags: chapter5, cdf, property
END

START
Cloze
The limiting value of the c.d.f. as x approaches $\infty$ is ${{c1::1}}$.
Tags: chapter5, cdf, property
END

START
Cloze
The c.d.f. $F_X(x)$ of a continuous random variable can be expressed in terms of the p.d.f. $f_X(x)$ as ${{c1::$\int_{-\infty}^{x} f_X(u) \, du$}}.
Tags: chapter5, pdf, definition
END

START
Cloze
The integral of a p.d.f. over the entire real line is equal to ${{c1::1}}$, i.e. $\int_{-\infty}^{\infty} f_X(u) \, du = 1$.
Tags: chapter5, pdf, property
END

START
Cloze
At any point x where the p.d.f. $f_X$ is continuous, we have ${{c1::$F_X'(x) = f_X(x)$}}.
Tags: chapter5, pdf, cdf, relationship
END

START
Cloze
If X is a continuous random variable, then the probability that X takes any particular value is always ${{c1::0}}$ , i.e $P(X=x) = 0$.
Tags: chapter5, continuous_random_variable, property
END

START
Cloze
The expectation $E[X]$ of a continuous random variable X with p.d.f. $f_X(x)$ is defined as ${{c1::$\int_{-\infty}^{\infty} x f_X(x) \, dx$}}.
Tags: chapter5, expectation, definition
END

START
Cloze
The expectation of a function of a continuous random variable, $E[h(X)]$, is given by ${{c1::$\int_{-\infty}^{\infty} h(x) f_X(x) \, dx$}}.
Tags: chapter5, expectation, definition
END

START
Cloze
The variance of a continuous random variable $X$ is defined as ${{c1::$E[(X-E[X])^2]$}} which is also equal to $E[X^2] - (E[X])^2$.
Tags: chapter5, variance, definition
END

START
Cloze
If $a$ and $b$ are constants, then the variance of $aX+b$ is ${{c1::$a^2 var(X)$}}.
Tags: chapter5, variance, property
END

START
Cloze
If $a$ and $b$ are constants, then $E[aX+b]$ is equal to ${{c1::$aE[X]+b$}}.
Tags: chapter5, expectation, property
END

START
Cloze
If a random variable X is uniformly distributed on [a,b], then its pdf is given by $f_X(x) = {{c1::$\frac{1}{b-a}$}}$ for $a\leq x \leq b$ and $0$ otherwise.
Tags: chapter5, uniform_distribution, definition
END

START
Cloze
If a random variable X has an exponential distribution with parameter $\lambda$, then its pdf is given by $f_X(x) = ${{c1::$\lambda e^{-\lambda x}$}}$ for $x\geq 0$ and 0 otherwise.
Tags: chapter5, exponential_distribution, definition
END

START
Cloze
If a random variable X has a gamma distribution with parameters $\alpha, \lambda$, then its pdf is given by $f_X(x) = ${{c1::$\frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-\lambda x}$}}$ for $x \geq 0$ and 0 otherwise.
Tags: chapter5, gamma_distribution, definition
END

START
Cloze
If a random variable X has a normal distribution with mean $\mu$ and variance $\sigma^2$, then its pdf is given by $f_X(x) = {{c1::$\frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(x-\mu)^2}{2\sigma^2})$}}$ for $x\in \mathbb{R}$.
Tags: chapter5, normal_distribution, definition
END

START
Cloze
The standard normal distribution is the normal distribution with mean ${{c1::0}}$ and variance ${{c2::1}}$.
Tags: chapter5, normal_distribution, standard
END

START
Cloze
The joint c.d.f. $F_{X,Y}(x,y)$ is defined as ${{c1::$P(X \le x, Y \le y)$}}.
Tags: chapter5, joint_distributions, cdf, definition
END

START
Cloze
The joint p.d.f. $f_{X,Y}(x,y)$ can be used to compute the joint c.d.f as $F_{X,Y}(x,y) = {{c1::$\int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u,v) \, dv \, du$}}.
Tags: chapter5, joint_distributions, pdf, definition
END

START
Cloze
Given a joint density $f_{X,Y}(x,y)$, the marginal density $f_X(x)$ can be computed as ${{c1::$\int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dy$}}.
Tags: chapter5, joint_distributions, marginal_density
END

START
Cloze
Given a joint density $f_{X,Y}(x,y)$, the marginal density $f_Y(y)$ can be computed as ${{c1::$\int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dx$}}.
Tags: chapter5, joint_distributions, marginal_density
END

START
Cloze
Two random variables $X$ and $Y$ are independent if their joint density function factorizes into the product of their marginal densities, ${{c1::$f_{X,Y}(x,y) = f_X(x) f_Y(y)$}}.
Tags: chapter5, joint_distributions, independence
END
