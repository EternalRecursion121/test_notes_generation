# Chapter 4 Flashcards

## Flashcards

### Basic Cards
START
Basic
What is a probability generating function (p.g.f.) of a discrete random variable $X$?
Back: $G_X(s) = E[s^X] = \sum_{k=0}^{\infty} s^k P(X=k)$. Source: Definition 4.1
Tags: chapter4, probability, generating_functions, definition
END

START
Basic
For what values of $s$ is the probability generating function, $G_X(s)$, always defined?
Back:  $|s| \leq 1$. Source: Chapter 4, page 36
Tags: chapter4, probability, generating_functions, convergence
END

START
Basic
What is the value of the probability generating function at $s=1$?
Back: $G_X(1) = 1$. Source: Chapter 4, page 36
Tags: chapter4, probability, generating_functions, property
END

START
Basic
What does the uniqueness theorem say about the relationship between a discrete random variable $X$ and its probability generating function, $G_X(s)$?
Back: The distribution of X is uniquely determined by its probability generating function, $G_X(s)$. Source: Theorem 4.2
Tags: chapter4, probability, generating_functions, uniqueness_theorem
END

START
Basic
What is the radius of convergence for a probability generating function?
Back: The radius of convergence must be at least 1. Source: Chapter 4, page 36
Tags: chapter4, probability, generating_functions, convergence
END

START
Basic
If $X \sim Ber(p)$, what is the probability generating function, $G_X(s)$?
Back: $G_X(s) = q + ps$ where $q = 1-p$. Source: Chapter 4, page 37
Tags: chapter4, probability, generating_functions, Bernoulli
END

START
Basic
If $X \sim Bin(n,p)$, what is the probability generating function, $G_X(s)$?
Back: $G_X(s) = (1-p+ps)^n$. Source: Chapter 4, page 37
Tags: chapter4, probability, generating_functions, Binomial
END

START
Basic
If $X \sim Po(\lambda)$, what is the probability generating function, $G_X(s)$?
Back: $G_X(s) = e^{\lambda(s-1)}$. Source: Chapter 4, page 37
Tags: chapter4, probability, generating_functions, Poisson
END

START
Basic
If X and Y are independent random variables, how is the p.g.f. of their sum, $G_{X+Y}(s)$, related to their individual p.g.f.'s, $G_X(s)$ and $G_Y(s)$?
Back: $G_{X+Y}(s) = G_X(s)G_Y(s)$. Source: Theorem 4.3
Tags: chapter4, probability, generating_functions, independence
END

START
Basic
If $X_1, X_2, ..., X_n$ are independent Bernoulli random variables with parameter $p$, what is the distribution of $Y = X_1 + ... + X_n$?
Back: $Y \sim Bin(n,p)$. Source: Theorem 4.4
Tags: chapter4, probability, generating_functions, Binomial, sum
END

START
Basic
If $X_1, X_2, ..., X_n$ are independent Poisson random variables such that $X_i \sim Po(\lambda_i)$, what is the distribution of $Y = X_1 + ... + X_n$?
Back: $Y \sim Po(\sum_{i=1}^n \lambda_i)$. Source: Theorem 4.5
Tags: chapter4, probability, generating_functions, Poisson, sum
END

START
Basic
How can you use the probability generating function $G_X(s)$ to find $E[X]$?
Back: $E[X] = G_X'(1)$. Source: Chapter 4, page 38
Tags: chapter4, probability, generating_functions, expected_value
END

START
Basic
How can you use the probability generating function $G_X(s)$ to find $E[X(X-1)]$?
Back: $E[X(X-1)] = G_X''(1)$. Source: Chapter 4, page 38
Tags: chapter4, probability, generating_functions, expected_value
END

START
Basic
How can you use the probability generating function $G_X(s)$ to find $var(X)$?
Back: $var(X) = G_X''(1) + G_X'(1) - (G_X'(1))^2$. Source: Chapter 4, page 38
Tags: chapter4, probability, generating_functions, variance
END

START
Basic
If $X_1, X_2, ...$ are i.i.d. random variables with p.g.f. $G_X(s)$ and $N$ is a random variable with p.g.f. $G_N(s)$ independent of the $X_i$, what is the p.g.f. of $\sum_{i=1}^{N} X_i$?
Back: $G_{\sum_{i=1}^{N} X_i}(s) = G_N(G_X(s))$. Source: Theorem 4.8
Tags: chapter4, probability, generating_functions, random_sum
END

START
Basic
What is a branching process?
Back: A process where individuals in a population reproduce randomly and independently. Source: Chapter 4, page 41
Tags: chapter4, probability, branching_process
END

START
Basic
If $G(s)$ is the p.g.f. of the number of children of a single individual in a branching process, what is $G_n(s)$, the p.g.f. of the number of individuals in generation $n$?
Back:  $G_{n+1}(s) = G(G_n(s))$, with $G_0(s) = s$. Source: Theorem 4.11
Tags: chapter4, probability, branching_process, generating_functions
END

START
Basic
In a branching process, what is the expected size of generation $n$, $E[X_n]$, in terms of the mean number of children of a single individual, $\mu$?
Back: $E[X_n] = \mu^n$. Source: Corollary 4.12
Tags: chapter4, probability, branching_process, expected_value
END

START
Basic
What is the extinction probability, $q$, in a branching process?
Back:  $q$ is the probability that the population will eventually die out. Source: Chapter 4, page 43
Tags: chapter4, probability, branching_process, extinction_probability
END

START
Basic
How do you find the extinction probability, $q$, in a branching process?
Back:  $q$ is the smallest non-negative solution of $x = G(x)$, where $G(x)$ is the p.g.f. of the offspring distribution. Source: Theorem 4.14
Tags: chapter4, probability, branching_process, extinction_probability
END

START
Basic
In a branching process, if the mean number of children of a single individual, $\mu$, is less than or equal to 1, what is the extinction probability, $q$?
Back: $q = 1$. Source: Theorem 4.15
Tags: chapter4, probability, branching_process, extinction_probability
END

START
Basic
In a branching process, if the mean number of children of a single individual, $\mu$, is greater than 1, what is the extinction probability, $q$?
Back: $q < 1$. Source: Theorem 4.15
Tags: chapter4, probability, branching_process, extinction_probability
END

### Cloze Cards
START
Cloze
The probability generating function of a discrete random variable $X$ is defined as $G_X(s) = {{c1::E[s^X]}} = \sum_{k=0}^{\infty} {{c2::s^k P(X=k)}}$
Tags: chapter4, probability, generating_functions, definition
END

START
Cloze
The radius of convergence of a probability generating function must be at least {{c1::1}}.
Tags: chapter4, probability, generating_functions, convergence
END

START
Cloze
The value of a probability generating function at $s=1$ is always $G_X(1) = {{c1::1}}$.
Tags: chapter4, probability, generating_functions, property
END

START
Cloze
The distribution of a discrete random variable $X$ is uniquely determined by its {{c1::probability generating function}}, $G_X(s)$.
Tags: chapter4, probability, generating_functions, uniqueness_theorem
END

START
Cloze
If $X \sim Ber(p)$, then the probability generating function is given by $G_X(s) = {{c1::q + ps}}$, where $q=1-p$.
Tags: chapter4, probability, generating_functions, Bernoulli
END

START
Cloze
If $X \sim Bin(n,p)$, then the probability generating function is given by $G_X(s) = {{c1::(1-p+ps)^n}}$.
Tags: chapter4, probability, generating_functions, Binomial
END

START
Cloze
If $X \sim Po(\lambda)$, then the probability generating function is given by $G_X(s) = {{c1::e^{\lambda(s-1)}}}$.
Tags: chapter4, probability, generating_functions, Poisson
END

START
Cloze
If X and Y are independent random variables, the probability generating function of their sum is $G_{X+Y}(s) = {{c1::G_X(s)G_Y(s)}}$.
Tags: chapter4, probability, generating_functions, independence
END

START
Cloze
If $X_1, X_2, ..., X_n$ are independent Bernoulli random variables with parameter $p$, then $Y = X_1 + ... + X_n$ has distribution ${{c1::Bin(n,p)}}$.
Tags: chapter4, probability, generating_functions, Binomial, sum
END

START
Cloze
If $X_1, X_2, ..., X_n$ are independent Poisson random variables such that $X_i \sim Po(\lambda_i)$, then $Y = X_1 + ... + X_n$ has distribution ${{c1::Po(\sum_{i=1}^n \lambda_i)}}$.
Tags: chapter4, probability, generating_functions, Poisson, sum
END

START
Cloze
The expected value of a discrete random variable, $X$, can be found from its p.g.f. as $E[X] = {{c1::G_X'(1)}}$.
Tags: chapter4, probability, generating_functions, expected_value
END

START
Cloze
The expected value of $X(X-1)$ can be found from the p.g.f. as $E[X(X-1)] = {{c1::G_X''(1)}}$.
Tags: chapter4, probability, generating_functions, expected_value
END

START
Cloze
The variance of a discrete random variable, $X$, can be found from its p.g.f. as $var(X) = {{c1::G_X''(1) + G_X'(1) - (G_X'(1))^2}}$.
Tags: chapter4, probability, generating_functions, variance
END

START
Cloze
If $X_1, X_2, ...$ are i.i.d. random variables with p.g.f. $G_X(s)$ and $N$ is a random variable with p.g.f. $G_N(s)$ independent of the $X_i$, then the p.g.f. of $\sum_{i=1}^{N} X_i$ is given by $G_{\sum_{i=1}^{N} X_i}(s) = {{c1::G_N(G_X(s))}}$.
Tags: chapter4, probability, generating_functions, random_sum
END

START
Cloze
In a branching process, the p.g.f. of the number of individuals in generation $n+1$ is related to the p.g.f. of the number in generation $n$ by $G_{n+1}(s) = {{c1::G(G_n(s))}}$.
Tags: chapter4, probability, branching_process, generating_functions
END

START
Cloze
In a branching process, the expected size of generation $n$ is given by $E[X_n] = {{c1::\mu^n}}$, where $\mu$ is the mean number of children of a single individual.
Tags: chapter4, probability, branching_process, expected_value
END

START
Cloze
In a branching process, the extinction probability, $q$, is the smallest non-negative solution of $x = {{c1::G(x)}}$, where $G(x)$ is the p.g.f. of the offspring distribution.
Tags: chapter4, probability, branching_process, extinction_probability
END

START
Cloze
In a branching process, if the mean number of children of a single individual, $\mu$, is less than or equal to 1, the extinction probability is ${{c1::1}}$.
Tags: chapter4, probability, branching_process, extinction_probability
END

START
Cloze
In a branching process, if the mean number of children of a single individual, $\mu$, is greater than 1, the extinction probability is ${{c1::<1}}$.
Tags: chapter4, probability, branching_process, extinction_probability
END
