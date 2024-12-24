# Chapter 2 Flashcards

Okay, here are the flashcards for Chapter 2, formatted as requested:

## Flashcards

### Basic Cards
START
Basic
What is a discrete random variable?
Back: A function from a probability space to the real numbers that takes a finite or countable set of values.
Tags: chapter2, random_variable, definition
END
START
Basic
What is the probability mass function (p.m.f.) of a discrete random variable X?
Back: The function $p_X(x) = P(X = x)$.
Tags: chapter2, probability_mass_function, definition
END
START
Basic
What must be true of the p.m.f., $p_X(x)$, for it to be valid?
Back: $p_X(x) \geq 0$ for all x, and $\sum_{x} p_X(x) = 1$.
Tags: chapter2, probability_mass_function, properties
END
START
Basic
What is the Bernoulli distribution?
Back: A distribution with parameter $p$ where $P(X = 1) = p$ and $P(X=0)=1-p$.
Tags: chapter2, bernoulli_distribution, definition
END
START
Basic
What does a Bernoulli random variable model?
Back: It models the outcome of a single trial with two outcomes, success or failure, such as a coin flip.
Tags: chapter2, bernoulli_distribution, model
END
START
Basic
What is the Binomial distribution?
Back: A distribution with parameters n and $p$ describing the number of successes in $n$ independent Bernoulli trials, with success probability $p$.
Tags: chapter2, binomial_distribution, definition
END
START
Basic
What is the Geometric distribution?
Back: A distribution with parameter $p$ describing the number of independent trials until the first success in a sequence of Bernoulli trials with success probability $p$.
Tags: chapter2, geometric_distribution, definition
END
START
Basic
What is the Poisson distribution?
Back: A distribution with parameter $\lambda$ that describes the number of events that occur in some interval, with $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$
Tags: chapter2, poisson_distribution, definition
END
START
Basic
What is the expectation (or expected value) of a discrete random variable X?
Back: $E[X] = \sum_{x \in ImX} xP(X=x)$.
Tags: chapter2, expectation, definition
END
START
Basic
What is the variance of a discrete random variable X?
Back:  $var(X) = E[(X - E[X])^2]$ or $var(X) = E[X^2] - (E[X])^2$.
Tags: chapter2, variance, definition
END
START
Basic
What does the variance measure?
Back: The spread of a distribution around its mean.
Tags: chapter2, variance, interpretation
END
START
Basic
What is the relationship between variance and standard deviation?
Back: Standard deviation is the square root of the variance.
Tags: chapter2, variance, standard_deviation
END
START
Basic
What is conditional probability mass function of X given event B?
Back: $P(X = x | B) = \frac{P(X=x \cap B)}{P(B)}$.
Tags: chapter2, conditional_distribution, definition
END
START
Basic
What is the conditional expectation of X given event B?
Back: $E[X|B] = \sum_x x P(X=x|B)$
Tags: chapter2, conditional_expectation, definition
END
START
Basic
If {B₁, B₂, ...} is a partition of the sample space, what is the total expectation formula?
Back:  $E[X] = \sum_{i} E[X|B_i]P(B_i)$
Tags: chapter2, partition_theorem, expectation
END
START
Basic
What is the joint probability mass function of two discrete random variables X and Y?
Back: $p_{X,Y}(x, y) = P(X=x, Y=y)$.
Tags: chapter2, joint_distribution, definition
END
START
Basic
How can you obtain the marginal probability mass function of X from the joint p.m.f. of X and Y?
Back: $p_X(x) = \sum_y p_{X,Y}(x,y)$
Tags: chapter2, marginal_distribution, definition
END
START
Basic
What does it mean for two discrete random variables X and Y to be independent?
Back: $P(X=x, Y=y) = P(X=x)P(Y=y)$ for all $x$ and $y$.
Tags: chapter2, independence, definition
END
START
Basic
What is the definition of $E[h(X,Y)]$ where h is a function of two discrete variables?
Back: $E[h(X,Y)] = \sum_x \sum_y h(x,y) P(X=x, Y=y)$
Tags: chapter2, expectation_function, definition
END
START
Basic
When can you use the linear property of expectation?
Back: Always! $E[aX+bY] = aE[X] + bE[Y]$, whether X and Y are independent or not.
Tags: chapter2, expectation, linearity
END
START
Basic
For two independent random variables X and Y, what is true of $E[XY]$?
Back: $E[XY] = E[X]E[Y]$
Tags: chapter2, expectation, independence
END
START
Basic
What is the covariance between two random variables X and Y?
Back: $cov(X,Y) = E[(X-E[X])(Y-E[Y])]$ or equivalently, $cov(X,Y) = E[XY] - E[X]E[Y]$
Tags: chapter2, covariance, definition
END
START
Basic
If X and Y are independent, what is their covariance?
Back: If X and Y are independent, $cov(X,Y) = 0$
Tags: chapter2, covariance, independence
END
START
Basic
Is covariance of 0 a sufficient condition for independence?
Back: No! Zero covariance doesn't imply independence.
Tags: chapter2, covariance, independence
END

### Cloze Cards
START
Cloze
A discrete random variable X is a function $X: \Omega \rightarrow \mathbb{R}$ where its image, Im(X) is a {{c1::finite or countable}} subset of the reals.
Tags: chapter2, random_variable, definition
END
START
Cloze
The probability mass function of a random variable X, denoted $p_X(x)$, is defined as $p_X(x) = {{c1::P(X=x)}}$.
Tags: chapter2, probability_mass_function, definition
END
START
Cloze
For a discrete random variable X, its probability mass function must satisfy $p_X(x) \geq 0$ and $\sum_x p_X(x) = {{c1::1}}$.
Tags: chapter2, probability_mass_function, properties
END
START
Cloze
If $X \sim \text{Bern}(p)$, then $P(X=0) = {{c1::1-p}}$ and $P(X=1)={{c2::p}}$.
Tags: chapter2, bernoulli_distribution, definition
END
START
Cloze
A random variable $X$ following a {{c1::binomial}} distribution describes the number of successes in a fixed number of independent Bernoulli trials.
Tags: chapter2, binomial_distribution, definition
END
START
Cloze
A random variable $X$ following a {{c1::geometric}} distribution describes the number of independent Bernoulli trials needed until the first success.
Tags: chapter2, geometric_distribution, definition
END
START
Cloze
A random variable $X$ follows a Poisson distribution if $P(X=k) = {{c1:: \frac{\lambda^k e^{-\lambda}}{k!}}}$ for k = 0, 1, 2, ....
Tags: chapter2, poisson_distribution, definition
END
START
Cloze
The expectation of a random variable $X$ is calculated as $E[X] = \sum_{x \in ImX} {{c1::xP(X=x)}}$.
Tags: chapter2, expectation, definition
END
START
Cloze
The variance of $X$ is defined as $var(X) = {{c1:: E[(X-E[X])^2]}} = E[X^2]-(E[X])^2$.
Tags: chapter2, variance, definition
END
START
Cloze
The conditional p.m.f. of X given event B is $P(X=x|B) = {{c1::\frac{P(X=x \cap B)}{P(B)}}}$.
Tags: chapter2, conditional_distribution, definition
END
START
Cloze
The conditional expectation of X given event B is $E[X|B] = \sum_x {{c1:: xP(X=x|B)}}$.
Tags: chapter2, conditional_expectation, definition
END
START
Cloze
If {B₁, B₂, ...} is a partition of the sample space, the law of total expectation says $E[X] = {{c1::\sum_{i} E[X|B_i]P(B_i)}}$
Tags: chapter2, partition_theorem, expectation
END
START
Cloze
The joint probability mass function of two discrete random variables X and Y is defined as $p_{X,Y}(x, y) = {{c1::P(X=x, Y=y)}}$
Tags: chapter2, joint_distribution, definition
END
START
Cloze
The marginal probability mass function of X can be found as $p_X(x) = {{c1:: \sum_y p_{X,Y}(x,y)}}$.
Tags: chapter2, marginal_distribution, definition
END
START
Cloze
Discrete random variables X and Y are independent if and only if $P(X=x, Y=y) = {{c1::P(X=x)P(Y=y)}}$ for all x and y.
Tags: chapter2, independence, definition
END
START
Cloze
If $h$ is a function of two discrete random variables, $E[h(X, Y)] = \sum_x \sum_y {{c1::h(x,y) P(X=x, Y=y)}}$.
Tags: chapter2, expectation_function, definition
END
START
Cloze
Expectation is linear: $E[aX + bY] = {{c1::aE[X] + bE[Y]}}$
Tags: chapter2, expectation, linearity
END
START
Cloze
If X and Y are independent, $E[XY] = {{c1::E[X]E[Y]}}$.
Tags: chapter2, expectation, independence
END
START
Cloze
The covariance of two random variables X and Y is $cov(X,Y) = {{c1::E[(X-E[X])(Y-E[Y])]}} = E[XY] - E[X]E[Y]$.
Tags: chapter2, covariance, definition
END
START
Cloze
Independent random variables have a covariance of {{c1::0}}, but a covariance of 0 does not guarantee {{c2::independence}}.
Tags: chapter2, covariance, independence
END

I believe that covers the major concepts and fits the rules you provided. Let me know if you would like any revisions!
