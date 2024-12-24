# Chapter 1 Flashcards

## Flashcards

### Basic Cards
START
Basic
What is a sample space?
Back: A sample space, denoted by $\Omega$, is the set of all possible outcomes of an experiment.
Tags: chapter1, probability, sample_space
END

START
Basic
What is an event?
Back: An event is a subset of the sample space $\Omega$.
Tags: chapter1, probability, event
END

START
Basic
What does $A^c$ mean?
Back: $A^c$ is the complement of event $A$. It means "A does not occur".
Tags: chapter1, probability, complement
END

START
Basic
What does $A \cup B$ mean?
Back: $A \cup B$ means "at least one of A and B occurs."
Tags: chapter1, probability, union
END

START
Basic
What does $A \cap B$ mean?
Back: $A \cap B$ means "both A and B occur".
Tags: chapter1, probability, intersection
END

START
Basic
What does $A \setminus B$ mean?
Back: $A \setminus B$ means "A occurs but B does not".
Tags: chapter1, probability, set_difference
END

START
Basic
What does it mean for two events $A$ and $B$ to be disjoint?
Back: Two events $A$ and $B$ are disjoint if $A \cap B = \emptyset$, meaning they cannot both occur.
Tags: chapter1, probability, disjoint
END

START
Basic
What is the probability of an event when all outcomes are equally likely?
Back: If the sample space $\Omega$ is finite and all outcomes are equally likely, the probability of an event A is given by $\mathbb{P}(A) = \frac{|A|}{|\Omega|}$.
Tags: chapter1, probability, equiprobable
END

START
Basic
What is the formula for the number of permutations of $n$ distinct objects?
Back: The number of permutations of $n$ distinct objects is $n!$.
Tags: chapter1, counting, permutation
END

START
Basic
What is the Stirling's formula for $n!$?
Back:  Stirling's formula is an approximation: $n! \sim \sqrt{2 \pi n} n^n e^{-n}$
Tags: chapter1, counting, stirling
END

START
Basic
What is the formula for the number of arrangements of $n$ objects with repetitions?
Back: If there are $n$ objects with $m_1$ of type 1, $m_2$ of type 2, ... , $m_k$ of type k, the number of arrangements is $\frac{n!}{m_1!m_2!...m_k!}$.
Tags: chapter1, counting, permutation_with_repetition
END

START
Basic
What is the binomial coefficient $\binom{n}{m}$?
Back: The binomial coefficient $\binom{n}{m}$ is given by $\frac{n!}{m!(n-m)!}$.
Tags: chapter1, counting, binomial_coefficient
END

START
Basic
What is a multinomial coefficient?
Back: A multinomial coefficient is a generalization of the binomial coefficient and appears in the multinomial theorem.
Tags: chapter1, counting, multinomial_coefficient
END

START
Basic
What is a bijection?
Back: A bijection is a one-to-one correspondence between two sets.
Tags: chapter1, counting, bijection
END

START
Basic
What are the axioms of probability for a set $\mathcal{F}$ and measure $\mathbb{P}$?
Back: 
$\mathcal{F}$ has:
1.  $\Omega \in \mathcal{F}$
2.  If $A \in \mathcal{F}$, then $A^c \in \mathcal{F}$
3.  If $\{A_i, i \in I\}$ is a countable collection in $\mathcal{F}$, then $\bigcup_{i \in I} A_i \in \mathcal{F}$
$\mathbb{P}$ has:
1.  For all $A \in \mathcal{F}$, $\mathbb{P}(A) \geq 0$.
2. $\mathbb{P}(\Omega) = 1$.
3. If $\{A_i, i \in I\}$ is a countable collection of disjoint members of $\mathcal{F}$, then $\mathbb{P}(\bigcup_{i \in I} A_i) = \sum_{i \in I} \mathbb{P}(A_i)$.
Tags: chapter1, probability, axioms
END

START
Basic
If $A \subseteq B$, how are their probabilities related?
Back: If $A \subseteq B$, then $\mathbb{P}(A) \leq \mathbb{P}(B)$
Tags: chapter1, probability, subset
END

START
Basic
What is the definition of conditional probability?
Back: The conditional probability of A given B is $\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$, provided $\mathbb{P}(B) > 0$.
Tags: chapter1, probability, conditional_probability
END

START
Basic
What is the multiplication rule for two events A and B?
Back: The multiplication rule is $\mathbb{P}(A \cap B) = \mathbb{P}(A|B)\mathbb{P}(B)$.
Tags: chapter1, probability, multiplication_rule
END

START
Basic
What is the multiplication rule for a sequence of events $A_1, A_2, \dots, A_n$?
Back: The multiplication rule is $\mathbb{P}(A_1 \cap A_2 \cap \dots \cap A_n) = \mathbb{P}(A_1)\mathbb{P}(A_2|A_1)\mathbb{P}(A_3|A_1 \cap A_2) \dots \mathbb{P}(A_n|A_1 \cap \dots \cap A_{n-1})$.
Tags: chapter1, probability, multiplication_rule
END

START
Basic
What is a partition of $\Omega$?
Back: A family of events $\{B_1, B_2, \dots\}$ is a partition of $\Omega$ if $\Omega = \bigcup_i B_i$ and $B_i \cap B_j = \emptyset$ for $i \neq j$.
Tags: chapter1, probability, partition
END

START
Basic
What is the law of total probability?
Back: If $\{B_1, B_2, ...\}$ is a partition of $\Omega$, then for any event $A$, $\mathbb{P}(A) = \sum_i \mathbb{P}(A|B_i)\mathbb{P}(B_i)$.
Tags: chapter1, probability, total_probability
END

START
Basic
What is Bayes' Theorem?
Back: If $\{B_1, B_2, ...\}$ is a partition of $\Omega$, then for any event $A$ with $\mathbb{P}(A) > 0$, $\mathbb{P}(B_k|A) = \frac{\mathbb{P}(A|B_k)\mathbb{P}(B_k)}{\sum_i \mathbb{P}(A|B_i)\mathbb{P}(B_i)}$.
Tags: chapter1, probability, bayes_theorem
END

START
Basic
What does it mean for two events $A$ and $B$ to be independent?
Back: Events $A$ and $B$ are independent if $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$.
Tags: chapter1, probability, independence
END

START
Basic
What does it mean for a family of events $\{A_i : i \in I\}$ to be independent?
Back: A family of events $\{A_i : i \in I\}$ is independent if for all finite subsets $J \subseteq I$, $\mathbb{P}(\bigcap_{i\in J}A_i) = \prod_{i\in J} \mathbb{P}(A_i)$.
Tags: chapter1, probability, independence
END

START
Basic
What is the relationship between independence and conditional probability?
Back: If $\mathbb{P}(B)>0$ and $A$ and $B$ are independent, then $\mathbb{P}(A|B) = \mathbb{P}(A)$.
Tags: chapter1, probability, independence, conditional_probability
END

### Cloze Cards
START
Cloze
The complement of A, denoted by $A^c$, means "A {{c1::does not occur}}".
Tags: chapter1, probability, complement
END

START
Cloze
If two events A and B are disjoint, then $A \cap B = {{c1::\emptyset}}$.
Tags: chapter1, probability, disjoint
END

START
Cloze
The number of arrangements of $n$ distinct objects is {{c1::$n!$}}.
Tags: chapter1, counting, permutation
END

START
Cloze
If there are $n$ objects with $m_1$ of type 1, $m_2$ of type 2, ... , $m_k$ of type k, the number of arrangements is {{c1::$\frac{n!}{m_1!m_2!...m_k!}$}}.
Tags: chapter1, counting, permutation_with_repetition
END

START
Cloze
The binomial coefficient $\binom{n}{m}$ is given by {{c1::$\frac{n!}{m!(n-m)!}$}}.
Tags: chapter1, counting, binomial_coefficient
END

START
Cloze
For any event $A$, the probability of the complement is given by $\mathbb{P}(A^c) = {{c1::$1 - \mathbb{P}(A)$}}$.
Tags: chapter1, probability, complement_rule
END

START
Cloze
The conditional probability of A given B is defined as $\mathbb{P}(A|B) = {{c1::\frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}}}$ , provided $\mathbb{P}(B)>0$.
Tags: chapter1, probability, conditional_probability
END

START
Cloze
The multiplication rule for two events A and B is  $\mathbb{P}(A \cap B) = {{c1::$\mathbb{P}(A|B)\mathbb{P}(B)$}}$.
Tags: chapter1, probability, multiplication_rule
END

START
Cloze
If $\{B_1, B_2, \dots\}$ is a partition of $\Omega$, then for any event A, $\mathbb{P}(A) =  {{c1::$\sum_i \mathbb{P}(A|B_i)\mathbb{P}(B_i)$}}$.
Tags: chapter1, probability, total_probability
END

START
Cloze
If $\{B_1, B_2, \dots\}$ is a partition of $\Omega$, and $\mathbb{P}(A) > 0$ then Bayes' Theorem states that $\mathbb{P}(B_k|A) = {{c1::\frac{\mathbb{P}(A|B_k)\mathbb{P}(B_k)}{\sum_i \mathbb{P}(A|B_i)\mathbb{P}(B_i)}}}$ .
Tags: chapter1, probability, bayes_theorem
END

START
Cloze
Events A and B are independent if $\mathbb{P}(A \cap B) = {{c1::$\mathbb{P}(A)\mathbb{P}(B)$}}$.
Tags: chapter1, probability, independence
END
