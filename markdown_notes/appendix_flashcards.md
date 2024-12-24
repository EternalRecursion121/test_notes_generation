# Appendix Flashcards

Okay, here are the flashcards based on the provided Appendix, following your rules for formatting, concept organization, and inclusion of both basic and cloze deletion cards.

## Flashcards

### Basic Cards
START
Basic
What does it mean for a set to be countable?
Back: A set is countable if it is either finite or if its elements can be listed as a sequence (e.g., x1, x2, x3,...).
Tags: appendix, set_theory, countability
END

START
Basic
If a set is countable, is there a bijection between the set and a subset of the natural numbers?
Back: Yes, if a set $S$ is countable, there exists a bijection from a subset of $\mathbb{N}$ to $S$.
Tags: appendix, set_theory, countability
END

START
Basic
Is the set of rational numbers ($\mathbb{Q}$) countable?
Back: Yes, the set of rational numbers ($\mathbb{Q}$) is countable.
Tags: appendix, set_theory, countability
END

START
Basic
Is the set of real numbers ($\mathbb{R}$) countable?
Back: No, the set of real numbers ($\mathbb{R}$) is not countable.
Tags: appendix, set_theory, countability
END

START
Basic
What is the formal definition of the limit of a sequence of real numbers $(a_1, a_2, a_3, ...)$?
Back:  A sequence of real numbers $(a_1, a_2, a_3, ...)$ converges to a limit $L \in \mathbb{R}$ if for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that $|a_n - L| < \epsilon$ whenever $n \geq N$.
Tags: appendix, analysis, limits
END

START
Basic
What does it mean for a series $\sum_{k=1}^\infty a_k$ to converge?
Back: A series $\sum_{k=1}^\infty a_k$ converges if the limit of its partial sums $s_n = \sum_{k=1}^n a_k$ exists, i.e., $\lim_{n \to \infty} s_n = L$ for some $L \in \mathbb{R}$.
Tags: appendix, analysis, series
END

START
Basic
What does it mean for a series $\sum_{k=1}^\infty a_k$ to converge absolutely?
Back:  A series $\sum_{k=1}^\infty a_k$ converges absolutely if the series $\sum_{k=1}^\infty |a_k|$ converges.
Tags: appendix, analysis, series, absolute_convergence
END

START
Basic
If a series converges absolutely, does it also converge?
Back: Yes, if a series converges absolutely, it also converges.
Tags: appendix, analysis, series, absolute_convergence
END

START
Basic
Why is absolute convergence important?
Back: Absolute convergence guarantees that the value of a sum does not depend on the order of the terms.
Tags: appendix, analysis, series, absolute_convergence
END

START
Basic
What is the formula for the sum of a geometric series $\sum_{k=0}^{n-1} ar^k$?
Back:  If $0 \leq r < 1$, $\sum_{k=0}^{n-1} ar^k = a\frac{1 - r^n}{1 - r}$.
Tags: appendix, series, geometric_series
END

START
Basic
What is the formula for the sum of an infinite geometric series $\sum_{k=0}^{\infty} ar^k$?
Back: If $0 \leq r < 1$, $\sum_{k=0}^{\infty} ar^k = \frac{a}{1 - r}$.
Tags: appendix, series, geometric_series
END

START
Basic
What is the power series for the exponential function, $e^\lambda$?
Back: $e^\lambda = \sum_{n=0}^\infty \frac{\lambda^n}{n!}$
Tags: appendix, series, exponential_function
END

START
Basic
State the binomial theorem
Back: $(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$
Tags: appendix, series, binomial_theorem
END

START
Basic
What does it mean for a sequence of events $A_n, n\geq 1$ to be increasing?
Back: A sequence of events $A_n, n\geq 1$ is increasing if $A_1 \subseteq A_2 \subseteq A_3 \subseteq ...$
Tags: appendix, probability, sequences
END

START
Basic
If $A_n, n \geq 1$ is an increasing sequence of events, how can we express $\bigcup_{n=1}^\infty A_n$ as a disjoint union?
Back: We can write $\bigcup_{n=1}^\infty A_n = A_1 \cup \bigcup_{k=2}^\infty (A_k \setminus A_{k-1})$.
Tags: appendix, probability, sequences
END

START
Basic
If $A_n, n\geq 1$ is an increasing sequence of events, what is $\mathbb{P}(\bigcup_{n=1}^\infty A_n)$?
Back: If $A_n, n\geq 1$ is an increasing sequence of events, then $\mathbb{P}(\bigcup_{n=1}^\infty A_n) = \lim_{n \to \infty} \mathbb{P}(A_n)$.
Tags: appendix, probability, sequences
END

### Cloze Cards
START
Cloze
The set of {{c1::rational numbers}}, denoted by $\mathbb{Q}$, is countable.
Tags: appendix, set_theory, countability
END

START
Cloze
The set of {{c1::real numbers}}, denoted by $\mathbb{R}$, is not countable.
Tags: appendix, set_theory, countability
END

START
Cloze
A sequence of real numbers $(a_1, a_2, a_3, ...)$ converges to a limit $L$ if for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that $|a_n - L| < \epsilon$ whenever $n \geq {{c1::N}}$.
Tags: appendix, analysis, limits
END

START
Cloze
A series $\sum_{k=1}^\infty a_k$ converges if the limit of its partial sums exists, that is, if $\lim_{n \to \infty} \sum_{k=1}^n a_k = {{c1::L}}$ for some $L \in \mathbb{R}$.
Tags: appendix, analysis, series
END

START
Cloze
A series $\sum_{k=1}^\infty a_k$ converges {{c1::absolutely}} if the series $\sum_{k=1}^\infty |a_k|$ converges.
Tags: appendix, analysis, series, absolute_convergence
END

START
Cloze
If a series converges absolutely, then it {{c1::converges}}.
Tags: appendix, analysis, series, absolute_convergence
END

START
Cloze
Absolute convergence is important because it guarantees that the value of a sum doesn't depend on the {{c1::order of the terms}}.
Tags: appendix, analysis, series, absolute_convergence
END

START
Cloze
The sum of an infinite geometric series $\sum_{k=0}^\infty ar^k$ is $\frac{a}{1-r}$ when $0 \leq r < {{c1::1}}$.
Tags: appendix, series, geometric_series
END

START
Cloze
The power series expansion for the exponential function is given by $e^\lambda = \sum_{n=0}^\infty \frac{{\lambda}^{{c1::n}}}{{{c2::n!}}}$.
Tags: appendix, series, exponential_function
END

START
Cloze
The Binomial Theorem states that $(x+y)^n = \sum_{k=0}^n {{c1::\binom{n}{k}}} {{c2::x^k}} y^{n-k}$.
Tags: appendix, series, binomial_theorem
END

START
Cloze
A sequence of events $A_n, n \geq 1$ is called increasing if $A_1 \subseteq A_2 \subseteq {{c1::A_3}} \subseteq ...$
Tags: appendix, probability, sequences
END

START
Cloze
For an increasing sequence of events $A_n$, we can write $\bigcup_{n=1}^\infty A_n$ as a disjoint union $A_1 \cup \bigcup_{k=2}^\infty ({{c1::A_k}} \setminus {{c2::A_{k-1}}})$.
Tags: appendix, probability, sequences
END

START
Cloze
For an increasing sequence of events $A_n, n\geq 1$, the probability of the union of all the events is given by: $\mathbb{P}(\bigcup_{n=1}^\infty A_n) = \lim_{n \to \infty} {{c1::\mathbb{P}(A_n)}}$.
Tags: appendix, probability, sequences
END
