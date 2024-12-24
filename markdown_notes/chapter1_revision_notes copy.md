# Chapter 1: Events and Probability - Revision Notes

> These notes are optimized for revision. Key definitions and theorems are highlighted, and proofs are included but visually separated for focused study.

---

Here are comprehensive revision notes for Chapter 1 of the provided PDF, formatted according to your specifications.

# Chapter 1: Events and Probability - Revision Notes

## 1.1 Introduction

This section introduces fundamental concepts:

* **Sample Space ($\Omega$):** The set of all possible outcomes of an experiment.  Think of it as the universe of possibilities.

* **Event ($A$):** A subset of the sample space ($\Omega$). An event occurs if the outcome of the experiment is in that subset.  Events are things you can observe and determine whether they happened or not.

* **Complement ($A^c$):**  The event that $A$ does not occur.  $A^c = \Omega \setminus A$.

* **Union ($A \cup B$):** The event that at least one of $A$ and $B$ occurs.

* **Intersection ($A \cap B$):** The event that both $A$ and $B$ occur.

* **Difference ($A \setminus B$):** The event that $A$ occurs but $B$ does not.

* **Disjoint Events:** Two events $A$ and $B$ are disjoint if $A \cap B = \emptyset$ (they cannot both occur).


### Probability Assignment in Simple Cases

In simple cases where the sample space $\Omega$ is finite and all outcomes are equally likely, the probability of an event $A$ is given by:

$P(A) = \frac{|A|}{|\Omega|}$

where $|A|$ denotes the number of elements in $A$.


---

## 1.2 Counting

This section focuses on counting techniques for determining probabilities in finite sample spaces:

### Arranging Distinguishable Objects

The number of ways to arrange $n$ distinguishable objects is $n!$ (n factorial).

> Stirling's approximation provides a useful estimate for large $n$: $n! \approx \sqrt{2\pi n} \left( \frac{n}{e} \right)^n$.

### Arrangements with Indistinguishable Objects

If there are $n$ objects with $m_1$ of type 1, $m_2$ of type 2, ..., $m_k$ of type k ($m_1 + m_2 + ... + m_k = n$), the number of distinct arrangements is given by the multinomial coefficient:

$\frac{n!}{m_1! m_2! ... m_k!}$

This is also the coefficient of $a_1^{m_1} a_2^{m_2} ... a_k^{m_k}$ in the expansion of $(a_1 + a_2 + ... + a_k)^n$.

### Binomial Coefficients and Choices

The number of ways to choose a committee of size $k$ from $n$ people is given by the binomial coefficient:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$

This is also the coefficient of $x^k y^{n-k}$ in the binomial expansion $(x+y)^n$.

> The binomial theorem states: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$.


### Lemma 1.1

The number of arrangements of $n$ objects, where object $a_i$ appears $m_i$ times and $\sum_{i=1}^k m_i = n$, is given by:

$\frac{n!}{m_1! m_2! ... m_k!}$


### Vandermonde's Identity (Lemma 1.5)

For $k, m, n \ge 0$:

$\sum_{j=0}^k \binom{m}{j}\binom{n}{k-j} = \binom{m+n}{k}$

**Proof:**  Consider choosing a committee of size $k$ from a group of $m$ men and $n$ women.  The left-hand side counts the number of ways to do this by summing over the possible numbers of men ($j$) in the committee.  The right-hand side directly counts the number of ways to choose a committee of size $k$ from $m+n$ people.


---

## 1.3 The Axiomatic Approach

This section formalizes probability using axioms:

### Probability Space

A probability space is a triple $(\Omega, \mathcal{F}, P)$, where:

* $\Omega$ is the sample space (the set of all possible outcomes).
* $\mathcal{F}$ is a $\sigma$-algebra (a collection of subsets of $\Omega$ called events, satisfying certain closure properties).
* $P$ is a probability measure (a function $P: \mathcal{F} \to [0, 1]$ satisfying the axioms below).

### Axioms of Probability

The probability measure $P$ must satisfy:

1.  $P(A) \ge 0$ for all $A \in \mathcal{F}$ (non-negativity).
2.  $P(\Omega) = 1$ (normalization).
3.  If $\{A_i\}_{i \in I}$ is a countable collection of disjoint events in $\mathcal{F}$, then $P(\bigcup_{i \in I} A_i) = \sum_{i \in I} P(A_i)$ (countable additivity).

### Theorem 1.8

1. $P(A^c) = 1 - P(A)$
2. If $A \subset B$, then $P(A) \le P(B)$

**Proof:** (1) follows from countable additivity and the fact that $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$. (2) follows from countable additivity and the fact that $B = A \cup (B \setminus A)$, where $A$ and $B \setminus A$ are disjoint.


---

## 1.4 Conditional Probability

This section introduces conditional probability:

### Definition 1.10: Conditional Probability

Given events $A, B \in \mathcal{F}$ with $P(B) > 0$, the conditional probability of $A$ given $B$ is:

$P(A|B) = \frac{P(A \cap B)}{P(B)}$

> Intuitively, this represents the probability of $A$ occurring, given that we know $B$ has already occurred.  We are restricting our attention to the smaller sample space defined by event $B$.

### Theorem 1.11

If $P(B) > 0$, then defining $Q(A) = P(A|B)$ creates a valid probability space $(\Omega, \mathcal{F}, Q)$.

**Proof:**  This involves verifying the probability axioms for $Q$.  Non-negativity and normalization are straightforward. Countable additivity follows from the countable additivity of $P$.


### Multiplication Rule (1.3)

$P(A \cap B) = P(A|B)P(B)$

This is a direct consequence of the definition of conditional probability.  It's a fundamental tool for calculating probabilities involving multiple events.

### General Multiplication Rule (1.4)

For events $A_1, A_2, ..., A_n$:

$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1 \cap A_2)...P(A_n|A_1 \cap ... \cap A_{n-1})$


---

## 1.5 Law of Total Probability and Bayes' Theorem

This section introduces these important theorems:

### Definition 1.15: Partition of $\Omega$

A family of events $\{B_i\}_{i \ge 1}$ is a partition of $\Omega$ if:

1.  $\bigcup_{i=1}^\infty B_i = \Omega$ (at least one $B_i$ must occur).
2.  $B_i \cap B_j = \emptyset$ for $i \ne j$ (no two $B_i$ can occur simultaneously).

### Theorem 1.16: Law of Total Probability

If $\{B_i\}_{i \ge 1}$ is a partition of $\Omega$ with $P(B_i) > 0$ for all $i$, then for any event $A$:

$P(A) = \sum_{i=1}^\infty P(A|B_i)P(B_i)$

> This allows us to compute $P(A)$ by considering the conditional probabilities of $A$ given each of the mutually exclusive and exhaustive events $B_i$.

**Proof:** This follows directly from countable additivity and the multiplication rule.


### Bayes' Theorem (Theorem 1.18)

Given a partition $\{B_i\}_{i \ge 1}$ of $\Omega$ with $P(B_i) > 0$ for all $i$, and an event $A$ such that $P(A) > 0$:

$P(B_k|A) = \frac{P(A|B_k)P(B_k)}{\sum_{i=1}^\infty P(A|B_i)P(B_i)}$

> This allows us to "invert" conditional probabilities.  It is crucial in Bayesian inference for updating beliefs about an event based on new evidence.

**Proof:** This follows directly from the definition of conditional probability and the law of total probability.



---

## 1.6 Independence

This section defines independence:

### Definition 1.22: Independence

1.  Two events $A$ and $B$ are independent if $P(A \cap B) = P(A)P(B)$.
2.  A family of events $\{A_i\}_{i \in I}$ is independent if for any finite subset $J \subset I$, $P(\bigcap_{i \in J} A_i) = \prod_{i \in J} P(A_i)$.
3.  A family of events is pairwise independent if any pair of events in the family is independent.

>  Pairwise independence does *not* imply independence!

### Theorem 1.24

If A and B are independent, then:

(a) $A^c$ and $B^c$ are independent.
(b) $A$ and $B^c$ are independent.


---

## 1.7 Some Useful Rules for Calculating Probabilities

This section summarizes strategies for probability calculations:

* **AND:** Use the multiplication rule (and its generalizations).
* **OR:** If events are disjoint, sum probabilities. Otherwise, use complements or the inclusion-exclusion principle.
* **Partition:** If direct calculation is difficult, condition on a partition of the sample space and use the law of total probability.


---

## Quick Reference

* **Sample Space ($\Omega$):** Set of all possible outcomes.
* **Event ($A$):** Subset of $\Omega$.
* **Complement ($A^c$):** $\Omega \setminus A$.
* **Probability (Equally Likely Outcomes):** $P(A) = \frac{|A|}{|\Omega|}$.
* **Conditional Probability:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* **Multiplication Rule:** $P(A \cap B) = P(A|B)P(B)$
* **Law of Total Probability:** $P(A) = \sum_{i=1}^\infty P(A|B_i)P(B_i)$ (for partition $\{B_i\}$)
* **Bayes' Theorem:** $P(B_k|A) = \frac{P(A|B_k)P(B_k)}{\sum_{i=1}^\infty P(A|B_i)P(B_i)}$
* **Independence:** $P(A \cap B) = P(A)P(B)$


---

## Common Patterns and Techniques

* **Counting Arguments:**  Many proofs involve clever counting arguments to establish equalities between different ways of counting the same thing.
* **Conditional Probability:**  Breaking down complex problems by conditioning on intermediate events is often very effective.
* **Law of Total Probability:** This is essential for calculating probabilities when you have a partition of the sample space.
* **Bayes' Theorem:**  This is frequently useful for reversing conditional probabilities, a common task in Bayesian inference.
* **Induction:** Vandermonde's identity proof used induction to extend the result from two events to multiple events.


This comprehensive set of revision notes should significantly aid in your review of Chapter 1. Remember to work through examples to solidify your understanding of each concept. Remember to consult the appendix for additional mathematical concepts (such as series convergence) that are relevant to this chapter.