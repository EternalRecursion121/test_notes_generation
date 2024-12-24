# Chapter 1 Revision Notes

Okay, here are the comprehensive revision notes for Chapter 1 of the provided PDF, adhering to all the specified requirements:

# Chapter 1: Events and Probability

## 1.1 Introduction

- We begin by considering an experiment with a set of possible outcomes.
- The set of all possible outcomes is called the **sample space**, denoted by $\Omega$.

**Examples of Sample Spaces**

1.  Tossing a coin: $\Omega = \{H, T\}$ (where H = heads, T = tails)
2.  Throwing two dice: $\Omega = \{(i, j) : 1 \le i, j \le 6\}$

> An **event** is a subset of the sample space, i.e., $A \subseteq \Omega$. An event $A$ occurs if the outcome $\omega \in \Omega$ satisfies $\omega \in A$.

**Examples of Events**

1. Coming up heads when tossing a coin: $A = \{H\}$
2. Getting a total of 4 when throwing two dice: $A = \{(1, 3), (2, 2), (3, 1)\}$

**Set Operations on Events**

- The **complement** of an event $A$ is $A^c := \Omega \setminus A$, which means "A does not occur".
- The union of two events $A$ and $B$, denoted by $A \cup B$, means "at least one of $A$ and $B$ occurs".
- The intersection of two events $A$ and $B$, denoted by $A \cap B$, means "both $A$ and $B$ occur".
- The set difference $A \setminus B$ means "$A$ occurs but $B$ does not occur."
- Two events are **disjoint** if $A \cap B = \emptyset$, i.e., they cannot both occur simultaneously.

**Probability Assignment**

- We assign a probability $P(A)$ to each event $A$.
- In the case where $\Omega$ is finite and all outcomes are equally likely, the probability of an event $A$ is given by:

$$
P(A) = \frac{|A|}{|\Omega|}
$$

where $|A|$ denotes the number of elements in $A$ and $|\Omega|$ denotes the number of elements in $\Omega$.

**Examples**
1.  For a fair coin, $P(A) = \frac{1}{2}$.
2.  For throwing two dice, let $A$ be the event that the total is $4$.  Then, $P(A) = \frac{3}{36} = \frac{1}{12}$.

---

## 1.2 Counting

> In this section, we consider the problem of counting the number of possible outcomes and events. The material covered here relates to combinatorics and permutations.

### Arranging Distinguishable Objects

- Given $n$ distinguishable objects, the number of ways to order them (permutations) is $n!$. This is because there are $n$ choices for the first object, $n-1$ for the second, and so on, which yields $n(n-1)\cdots 2 \cdot 1 = n!$.

**Stirling's Formula**

-  A useful approximation for $n!$ when $n$ is large:

$$
n! \sim \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n
$$

### Arrangements When Not All Objects Are Distinguishable

- When not all objects are distinguishable, we need to adjust our counting formula.
- Suppose we have $n$ objects, where $\alpha_1$ appears $m_1$ times, $\alpha_2$ appears $m_2$ times, ..., and $\alpha_k$ appears $m_k$ times, with $m_1 + m_2 + ... + m_k = n$. The number of distinct arrangements is given by the following:

> **Lemma 1.1**: The number of arrangements of $n$ objects with repetitions is

> $$
 \frac{n!}{m_1! m_2! ... m_k!}
 $$

**Example**
The number of arrangements of the letters in "STATISTICS" is:
$$
\frac{10!}{3! 3! 2! 1! 1!} = \frac{10!}{3!3!2!}
$$
If there are only two types of objects then, since $m_1+m_2 = n$, this is a binomial coefficient.

$$
 \binom{n}{m_1} = \binom{n}{m_2} = \frac{n!}{m_1!(n-m_1)!} = \frac{n!}{m_2!(n-m_2)!}
$$

### Multinomial Coefficients

- The expression $$ \frac{n!}{m_1! m_2! ... m_k!} $$ is called a **multinomial coefficient** and is often written as:
    
$$
\binom{n}{m_1 \ m_2 \ ... \ m_k}
$$

- This is the coefficient of $a_1^{m_1} a_2^{m_2} ... a_k^{m_k}$ in the expansion of $(a_1 + a_2 + ... + a_k)^n$

**Connection to Binomial Theorem**

- Recall the **binomial theorem**:

$$
(x+y)^n = \sum_{m=0}^n \binom{n}{m} x^m y^{n-m}
$$

- The binomial coefficient $\binom{n}{m}$ arises as the number of ways to choose $m$ "slots" for $x$ out of $n$ total slots when expanding $(x+y)^n$

**Choices as Combinations**

- A binomial coefficient can be interpreted as the number of ways to choose a committee of size $k$ from $n$ people, denoted $\binom{n}{k}$.

**Example 1.3: Team Selection**

-  Picking a team of $m$ players from a squad of $n$. Let $\Omega = \{(i_1, i_2, ..., i_n): i_k \in \{0, 1\}, \sum_{k=1}^n i_k=m\}$ where $i_k = 1$ if player $k$ is picked. Then, if $A$ is the event that player 1 is in the team:

    $$
    P(A) = \frac{\binom{n-1}{m-1}}{\binom{n}{m}} = \frac{m}{n}
    $$

**Example 1.4: Non-negative Integer Solutions**
-  The number of non-negative integer solutions to $x_1 + x_2 + ... + x_m = n$ is:
    $$
     \binom{n+m-1}{m-1}
    $$

This can be seen by considering a sequence of $n$ stars and $m-1$ bars.

---

### Lemma 1.5: Vandermonde's Identity
> For $k, m, n \geq 0$
>>  $$
\binom{m+n}{k} = \sum_{j=0}^k \binom{m}{j}\binom{n}{k-j}
$$
**Proof:** Consider choosing a committee of $k$ people from a group of $m$ men and $n$ women.

1. There are $\binom{m+n}{k}$ ways to do this directly.

2.  Alternatively, we can choose $j$ men out of $m$ in $\binom{m}{j}$ ways and then $k-j$ women out of $n$ in $\binom{n}{k-j}$ ways, where $j$ ranges from $0$ to $k$. Summing over all these possibilities yields the right-hand side, which is the same total number of committees.

---

### An Aside on Sizes of Sets
> We will differentiate between sets that are *countable* and those that are *uncountable*
- A set is called **countable** if there is a bijection between the set and the natural numbers.
- A set that is not countable is **uncountable**
- The natural numbers and rational numbers are countable.
- The real numbers are uncountable.

---

## 1.3 The Axiomatic Approach

> We now formally define a probability space and the associated axioms.

>  **Definition 1.6**: A probability space is a triple $(\Omega, \mathcal{F}, P)$ where
> 1.  $\Omega$ is a set called the **sample space.**
> 2.  $\mathcal{F}$ is a collection of subsets of $\Omega$, called **events**, satisfying axioms F1-F3.
> 3.  $P$ is a probability measure, which is a function $P: \mathcal{F} \to \mathbb{R}$ satisfying axioms P1-P3.

**Axioms for Events**

> $\mathcal{F}$ is a collection of subsets of $\Omega$, with
>
> 1.  $\Omega \in \mathcal{F}$.
> 2.  If $A \in \mathcal{F}$, then $A^c \in \mathcal{F}$.
> 3.  If $\{A_i, i \in I\}$ is a finite or countably infinite collection of members of $\mathcal{F}$, then $\bigcup_{i \in I} A_i \in \mathcal{F}$.

**Axioms of Probability**
> $P$ is a function from $\mathcal{F}$ to $\mathbb{R}$, with:
>
> 1.  For all $A \in \mathcal{F}$, $P(A) \ge 0$.
> 2.  $P(\Omega) = 1$.
> 3. If $\{A_i, i \in I\}$ is a finite or countably infinite collection of members of $\mathcal{F}$, and $A_i \cap A_j = \emptyset$ for $i \ne j$, then:
>> $$
P\left( \bigcup_{i \in I} A_i \right) = \sum_{i \in I} P(A_i)
$$

**Special Case of P3**

- If $A, B \in \mathcal{F}$ with $A \cap B = \emptyset$, then $P(A \cup B) = P(A) + P(B)$. This is the addition rule for disjoint events.

**Remark**
> If $\Omega$ is finite or countable then $\mathcal{F}$ is the set of all subsets of $\Omega$.  If $\Omega$ is uncountable, then we can't have $\mathcal{F}$ be all of the subsets of $\Omega$ because this will cause issues with assigning consistent probabilities.

**Example 1.7: Probability Function**

- Consider a countably infinite set $\Omega = \{w_1, w_2, ...\}$. Let $(p_1, p_2, ...)$ be a collection of non-negative numbers with $\sum_{i=1}^{\infty} p_i = 1$. Define $P(A) = \sum_{i: w_i \in A} p_i$. Then P satisfies axioms P1-P3, and the numbers $(p_1, p_2, ...)$ are a probability function.

**Theorem 1.8: Consequences of Axioms**

>  Suppose $(\Omega, \mathcal{F}, P)$ is a probability space and that $A, B \in \mathcal{F}$. Then,
>
> 1. $P(A^c) = 1 - P(A)$
> 2. If $A \subseteq B$, then $P(A) \le P(B)$.

**Proof**

1.  $A \cup A^c = \Omega$ and $A \cap A^c = \emptyset$. By P3, we have $P(\Omega) = P(A) + P(A^c)$. Since $P(\Omega) = 1$, we have $P(A^c) = 1 - P(A)$.

2.  If $A \subseteq B$, then $B = A \cup (B \cap A^c)$. Since $A$ and $B \cap A^c$ are disjoint, $P(B) = P(A) + P(B \cap A^c)$. By P1, $P(B \cap A^c) \ge 0$, so $P(B) \ge P(A)$.

---

## 1.4 Conditional Probability

> Conditional probability allows us to formalize the notion of probability given additional information.

> **Definition 1.10**: Let $(\Omega, \mathcal{F}, P)$ be a probability space. If $A, B \in \mathcal{F}$ and $P(B) > 0$, then the **conditional probability of $A$ given $B$** is

> $$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

**Remark**
If $P(B) = 0$ then $P(A|B)$ is undefined

> **Theorem 1.11**: Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $B \in \mathcal{F}$ satisfy $P(B) > 0$. Define a new function $Q: \mathcal{F} \to \mathbb{R}$ by $Q(A) = P(A|B)$. Then $(\Omega, \mathcal{F}, Q)$ is also a probability space.

**Proof**
We have to check axioms P1 - P3:

1.  $Q(A) = \frac{P(A \cap B)}{P(B)} \geq 0$ since probabilities are non-negative.
2.  $Q(\Omega) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$
3.  For disjoint events $A_i$, $i \in I$:
    $$
    \begin{aligned}
    Q(\bigcup_{i\in I} A_i) &= \frac{P((\bigcup_{i\in I} A_i) \cap B)}{P(B)} \\
    &= \frac{P(\bigcup_{i\in I} (A_i \cap B))}{P(B)} \\
    &= \frac{\sum_{i\in I} P(A_i \cap B)}{P(B)} \\
    &= \sum_{i\in I} \frac{P(A_i \cap B)}{P(B)} = \sum_{i\in I} Q(A_i)
    \end{aligned}
    $$
    since the $A_i \cap B$ are disjoint if the $A_i$ are disjoint.

**Multiplication Rule**

- From the definition of conditional probability, we obtain the **multiplication rule:**

$$
P(A \cap B) = P(A|B) P(B)
$$
This can be generalised to:
$$
P (A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1)P(A_2 | A_1)P(A_3 | A_1 \cap A_2) \dots P(A_n | A_1 \cap A_2 \cap \dots \cap A_{n-1})
$$
**Example 1.12: Urn Problem**
- An urn contains 8 red and 4 white balls. We draw 3 balls without replacement. The probability that all three balls are red is:
    $$
    P(R_1 \cap R_2 \cap R_3) = \frac{8}{12} \cdot \frac{7}{11} \cdot \frac{6}{10} = \frac{14}{55}
    $$

**Example 1.14: Bitstream Transmission**
- In a noisy bitstream, $P(0 \text{ sent}) = \frac{4}{7}, P(1 \text{ sent}) = \frac{3}{7}$. Owing to noise,
$$
P(1 \text{ received}| 0 \text{ sent}) = \frac{1}{8}, \quad P(0 \text{ received}| 1 \text{ sent}) = \frac{1}{6}
$$
Then,
$$
\begin{aligned}
P(0 \text{ sent } | 0 \text{ received}) &= \frac{P(0 \text{ sent and } 0 \text{ received})}{P(0 \text{ received})} \\
&= \frac{P(0 \text{ received}| 0 \text{ sent}) P(0 \text{ sent})}{P(0 \text{ received}| 0 \text{ sent}) P(0 \text{ sent}) + P(0 \text{ received}| 1 \text{ sent}) P(1 \text{ sent})} \\
&= \frac{\frac{7}{8} \cdot \frac{4}{7}}{\frac{7}{8} \cdot \frac{4}{7} + \frac{1}{6} \cdot \frac{3}{7}} \\
&= \frac{7/14}{7/14 + 1/14} = \frac{7}{8}
\end{aligned}
$$

---
## 1.5 The Law of Total Probability and Bayes' Theorem

> These tools allow us to calculate probabilities using a partitioning of the sample space.

> **Definition 1.15:** A family of events $\{B_1, B_2, ...\}$ is a **partition of $\Omega$** if:
>
> 1.  $\Omega = \bigcup_{i \ge 1} B_i$ (at least one $B_i$ must occur).
> 2.  $B_i \cap B_j = \emptyset$ whenever $i \ne j$ (no two can occur together).

> **Theorem 1.16 (Law of Total Probability):** Suppose $\{B_1, B_2,...\}$ is a partition of $\Omega$ by sets from $\mathcal{F}$, such that $P(B_i) > 0$ for all $i \ge 1$. Then for any $A \in \mathcal{F}$:
>
> $$
P(A) = \sum_{i \ge 1} P(A|B_i)P(B_i)
$$

**Proof**

$$
\begin{aligned}
P(A) &= P(A \cap \Omega) = P(A \cap (\bigcup_{i\geq 1} B_i)) = P(\bigcup_{i\geq 1} (A\cap B_i)) \\
&= \sum_{i \geq 1} P(A \cap B_i) = \sum_{i \geq 1} P(A|B_i)P(B_i)
\end{aligned}
$$

**Example 1.17: Crossword Setter**

- Setter I composes $m$ clues, and setter II composes $n$ clues.  Alice solves a clue with probability $\alpha$ if it was composed by setter I, and with probability $\beta$ if it was composed by setter II.

   The probability Alice solves a clue is
   $$
   P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) = \alpha\frac{m}{m+n} + \beta\frac{n}{m+n} = \frac{\alpha m + \beta n}{m+n}
   $$

> **Theorem 1.18 (Bayes' Theorem):** Suppose that $\{B_1, B_2, ...\}$ is a partition of $\Omega$ by sets from $\mathcal{F}$ such that $P(B_i) > 0$ for all $i \ge 1$. Then for any $A \in \mathcal{F}$ such that $P(A) > 0$:

> $$
P(B_k | A) = \frac{P(A|B_k)P(B_k)}{\sum_{i \geq 1} P(A|B_i)P(B_i)}
$$

**Proof**
    $$
    P(B_k | A) = \frac{P(B_k \cap A)}{P(A)} = \frac{P(A|B_k) P(B_k)}{P(A)}
    $$
    We then use the Law of Total Probability to express the denominator.

**Odds Form of Bayes' Theorem**
    
   We can also express Bayes' theorem in odds form by considering a partition $\{B, B^c\}$. Then, comparing the expressions of $P(B|A)$ and $P(B^c | A)$, we get:

   $$
   \frac{P(B|A)}{P(B^c | A)} = \frac{P(A|B)}{P(A|B^c)}\frac{P(B)}{P(B^c)}
   $$

   The term $P(B)/P(B^c)$ are the prior odds, $P(B|A)/P(B^c|A)$ are the posterior odds, and $\frac{P(A|B)}{P(A|B^c)}$ is the Bayes factor.

**Example 1.20: Medical Condition Test**

- A medical condition has a prevalence of 1/1000. A test has a false negative rate of 0 and a false positive rate of 0.01. If an individual tests positive, the probability they have the condition is:
    $$
    \frac{1 \times \frac{1}{1000}}{1 \times \frac{1}{1000} + 0.01 \times \frac{999}{1000}} = \frac{1}{1000 + 9.99} \approx 0.091
    $$

## Example 1.21: Simpson's Paradox
    Simpson's paradox illustrates that conditional probabilities can be counterintuitive.
    It's possible that:
    $$
    P(E|F\cap G) > P(E|F^c \cap G)
    $$
     $$
    P(E|F\cap G^c) > P(E|F^c \cap G^c)
    $$
    while at the same time:
    $$
   P(E|F) < P(E|F^c)
    $$

---
## 1.6 Independence
>  We consider the case when the knowledge of an event does not influence another event.

> **Definition 1.22:**
> 1.  Events A and B are **independent** if $P(A \cap B) = P(A)P(B)$.
> 2.  A family of events $A = \{A_i: i \in I\}$ is **independent** if for all finite subsets $J \subset I$, $$ P(\bigcap_{i \in J} A_i) = \prod_{i \in J} P(A_i) $$
> 3.  A family of events is **pairwise independent** if $P(A_i \cap A_j) = P(A_i) P(A_j)$ whenever $i \neq j$

**Warning**
> Pairwise independence does not imply independence

**Remark**
> If A and B are independent then P(A|B) = P(A) if P(B) > 0 and P(B|A) = P(B) if P(A) > 0

**Example 1.23: Two Fair Dice**

- If $A =$ {first die shows 4}, $B = $ {total score is 6}, and $C =$ {total score is 7}, then A and B are not independent, but A and C are.

> **Theorem 1.24:** Suppose $A$ and $B$ are independent. Then:
>
> 1.  $A$ and $B^c$ are independent
> 2.  $A^c$ and $B^c$ are independent

**Proof**
1. $$ P(A \cap B^c) = P(A) - P(A\cap B) = P(A) - P(A)P(B) = P(A) (1-P(B)) = P(A) P(B^c) $$
2.  Apply part (1) to the events $B^c$ and $A$

**Remark**
> If $\{A_i, i \in I\}$ is any family of independent events, then so is any family with elements replaced by their complements. This can be proven using the inclusion exclusion formula.

---

## 1.7 Some Useful Rules for Calculating Probabilities

- **AND:** Use the multiplication rule: $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$, or its generalisation: $P (A_1 \cap A_2 \cap ... \cap A_n) = P (A_1) P (A_2|A_1) ... P (A_n|A_1 \cap A_2 \cap ... \cap A_{n-1})$

- **OR:** If events are disjoint, use $P (A_1 \cup A_2 \cup ... \cup A_n) = P (A_1) + P (A_2) + ... + P (A_n)$. Otherwise, use complements: $P (A_1 \cup A_2 \cup ... \cup A_n) = 1 - P ((A_1 \cup A_2 \cup ... \cup A_n)^c) = 1 - P(A_1^c \cap A_2^c \cap ... \cap A_n^c)$. Alternatively, use the inclusion exclusion formula.
     $$ P(A_1 \cup A_2 \cup \dots \cup A_n) = \sum_{i=1}^n P(A_i) - \sum_{i<j}P(A_i \cap A_j) + \dots + (-1)^{n+1}P(A_1 \cap A_2 \cap \dots \cap A_n) $$
- **Splitting and Total Probability:** If you can't calculate the probability of your event directly, split it up according to some partition of $\Omega$ and use the law of total probability.

**Important Check:** Any probability that you calculate should be in the interval [0, 1]. If not, something has gone wrong.

This concludes the revision notes for Chapter 1.
