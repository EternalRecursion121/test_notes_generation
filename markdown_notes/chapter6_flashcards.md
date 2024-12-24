# Chapter 6 Flashcards

Okay, here are the flashcards based on Chapter 6, following the specified rules and format:

## Flashcards

### Basic Cards
START
Basic
What is the definition of a random sample of size n?
Back: A set of n i.i.d. (independent and identically distributed) random variables.
Tags: chapter6, random_samples, definition
END

START
Basic
What is the formula for the sample mean, given random variables $X_1, X_2, ..., X_n$?
Back: $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$
Tags: chapter6, sample_mean, formula
END

START
Basic
If $X$ and $Y$ are random variables, what is the variance of their sum, var$(X+Y)$?
Back: var$(X+Y)$ = var$(X)$ + var$(Y)$ + 2cov$(X,Y)$
Tags: chapter6, variance, addition_rule
END

START
Basic
When random variables are independent, what is their covariance?
Back: The covariance between independent random variables is 0.
Tags: chapter6, covariance, independence
END

START
Basic
Given a random sample $X_1, X_2, ..., X_n$ from a distribution with mean $\mu$, what is the expected value of the sample mean $\bar{X}_n$?
Back: $E[\bar{X}_n] = \mu$
Tags: chapter6, sample_mean, expectation
END

START
Basic
Given a random sample $X_1, X_2, ..., X_n$ from a distribution with variance $\sigma^2$, what is the variance of the sample mean $\bar{X}_n$?
Back: var$(\bar{X}_n) = \frac{\sigma^2}{n}$
Tags: chapter6, sample_mean, variance
END

START
Basic
What is an indicator function of an event A?
Back: A random variable X which is 1 if the event occurs, and 0 otherwise.
Tags: chapter6, indicator_function, definition
END

START
Basic
What is the expected value of a random variable X which is the indicator of event A, where $\mathbb{P}(A) = p$?
Back: $E[X] = p$
Tags: chapter6, indicator_function, expected_value
END

START
Basic
What does the Weak Law of Large Numbers describe?
Back: It states that the sample mean converges in probability to the true mean of the distribution as the sample size increases.
Tags: chapter6, weak_law, definition
END

START
Basic
What does convergence in probability imply?
Back: For any fixed $\epsilon > 0$, the probability that the sample mean deviates from the population mean by more than $\epsilon$ goes to 0 as n approaches infinity.
Tags: chapter6, weak_law, convergence
END

START
Basic
What is Markov's inequality?
Back: For a non-negative random variable Y and any t > 0, $\mathbb{P}(Y \geq t) \leq \frac{E[Y]}{t}$.
Tags: chapter6, markov_inequality, definition
END

START
Basic
What is Chebyshev's inequality?
Back: For a random variable Z with a finite variance and any t > 0, $\mathbb{P}(|Z - E[Z]| \geq t) \leq \frac{var(Z)}{t^2}$
Tags: chapter6, chebyshev_inequality, definition
END

### Cloze Cards
START
Cloze
A set of $n$ {{c1::i.i.d. (independent and identically distributed)}} random variables is called a random sample of size $n$.
Tags: chapter6, random_samples, definition
END

START
Cloze
The sample mean $\bar{X}_n$ is defined as $\frac{1}{n} {{c1::\sum_{i=1}^n X_i}}$ where $X_1, \dots, X_n$ are the random variables in the sample.
Tags: chapter6, sample_mean, formula
END

START
Cloze
If X and Y are random variables, var$(X+Y)$ = var$(X)$ + var$(Y)$ + {{c1::2cov$(X,Y)$}}.
Tags: chapter6, variance, addition_rule
END

START
Cloze
For a random sample from a distribution with mean $\mu$ and variance $\sigma^2$, the variance of the sample mean $\bar{X}_n$ is equal to {{c1::$\frac{\sigma^2}{n}$}}.
Tags: chapter6, sample_mean, variance
END

START
Cloze
An indicator function of an event A is a random variable that is {{c1::1}} if the event occurs and {{c2::0}} otherwise.
Tags: chapter6, indicator_function, definition
END

START
Cloze
The Weak Law of Large Numbers states that for any $\epsilon > 0$, $\mathbb{P}(|\bar{X}_n - \mu| > \epsilon) \to {{c1::0}}$ as $n \to \infty$.
Tags: chapter6, weak_law, convergence
END

START
Cloze
Markov's inequality states that for a non-negative random variable Y and any t > 0,  $\mathbb{P}(Y \geq t) \leq {{c1::\frac{E[Y]}{t}}}$.
Tags: chapter6, markov_inequality, definition
END

START
Cloze
Chebyshev's inequality states that for any random variable Z with finite variance,  $\mathbb{P}(|Z - E[Z]| \geq t) \leq {{c1::\frac{var(Z)}{t^2}}}$.
Tags: chapter6, chebyshev_inequality, definition
END
