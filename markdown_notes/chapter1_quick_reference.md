# Chapter 1 Quick Reference

Okay, here's a quick reference section based on Chapter 1 of the provided document, formatted with LaTeX and with sections organized according to your request:

## Quick Reference

### Formulas and Results

*   Probability for finite sample space with equally likely outcomes:  $$P(A) = \frac{|A|}{|\Omega|}$$
*   Number of arrangements of $n$ distinguishable objects: $n!$
*   Stirling's formula: $$n! \sim \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n$$
*   Number of arrangements of $n$ objects with $m_i$ copies of each of $k$ types: $$\frac{n!}{m_1! m_2! ... m_k!}$$ where $m_1 + ... + m_k = n$
*   Binomial coefficient: $${n \choose m} = \frac{n!}{m!(n-m)!}$$
*   Multinomial coefficient: $${n \choose m_1, m_2, ..., m_k} = \frac{n!}{m_1!m_2!...m_k!}$$ where $m_1 + ... + m_k = n$
*   Binomial Theorem: $$(x+y)^n = \sum_{m=0}^n {n \choose m} x^m y^{n-m}$$
*   Number of non-negative integer solutions to $x_1 + x_2 + ... + x_m = n$: $${n+m-1 \choose m-1}$$
*   Vandermonde's identity: $${m+n \choose k} = \sum_{j=0}^k {m \choose j} {n \choose k-j}$$
*   Conditional Probability:  $$P(A|B) = \frac{P(A \cap B)}{P(B)}, \text{ if } P(B) > 0$$
*   Multiplication Rule: $$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$
*   Generalized Multiplication Rule:
 $$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1 \cap A_2)...P(A_n|A_1 \cap ... \cap A_{n-1})$$
*   Law of Total Probability: $$P(A) = \sum_{i} P(A|B_i)P(B_i)$$ where $\{B_i\}$ is a partition of $\Omega$
*   Bayes' Theorem: $$P(B_k|A) = \frac{P(A|B_k)P(B_k)}{\sum_i P(A|B_i)P(B_i)}$$
*   Bayes' Theorem Odds form:
    $$\frac{P(B|A)}{P(B^c|A)} = \frac{P(A|B)}{P(A|B^c)} \frac{P(B)}{P(B^c)}$$
*   Independence: $P(A \cap B) = P(A)P(B)$

### Definitions in Mathematical Notation

*   Sample space: $\Omega$ (set of all possible outcomes)
*   Event: $A \subseteq \Omega$ (a subset of the sample space)
*   Complement of A: $A^c := \Omega \setminus A$
*   Union of A and B: $A \cup B$ ("at least one of A and B occurs")
*   Intersection of A and B: $A \cap B$ ("both A and B occur")
*   Set difference: $A \setminus B$ ("A occurs but B does not")
*   Disjoint Events:  $A \cap B = \emptyset$
*   Countable set: A set $S$ for which there is a bijection between $S$ and the natural numbers $\mathbb{N}$
*   Uncountable set: A set that is not countable
*   Probability space: $(\Omega, \mathcal{F}, P)$
    *   $\Omega$ is the sample space
    *   $\mathcal{F}$ is the set of events that satisfy properties $F_1$, $F_2$, and $F_3$
    *   $P$ is the probability measure that satisfies properties $P_1$, $P_2$, and $P_3$
*   A partition of $\Omega$: a family of events $\{B_1, B_2, ...\}$ such that $\bigcup_{i \ge 1} B_i = \Omega$ and $B_i \cap B_j = \emptyset$ for $i \neq j$.
*   Pairwise Independent: $P(A_i \cap A_j) = P(A_i)P(A_j)$ whenever $i\ne j$
*   Independent: a family of events $\{A_i : i \in I\}$ where for all finite subsets J of I:  $$P\left(\bigcap_{i \in J} A_i\right) = \prod_{i \in J} P(A_i)$$

### Theorems (Concise)

*   **Theorem 1.8:** Given a probability space $(\Omega, \mathcal{F}, P)$ and $A,B \in \mathcal{F}$,
    1.  $P(A^c) = 1 - P(A)$
    2.  If $A \subseteq B$, then $P(A) \leq P(B)$
*   **Theorem 1.11:** If $(\Omega, \mathcal{F}, P)$ is a probability space and $B\in \mathcal{F}$ such that $P(B) > 0$, then $(\Omega, \mathcal{F}, Q)$ is also a probability space, where $Q(A) = P(A|B)$.
*   **Theorem 1.16** (Law of Total Probability): If $\{B_i\}_{i=1}^\infty$ is a partition of $\Omega$, and $P(B_i) > 0$ for all $i$, then $P(A) = \sum_{i} P(A|B_i)P(B_i)$ for any event $A$.
*   **Theorem 1.18** (Bayes' Theorem): If $\{B_i\}_{i=1}^\infty$ is a partition of $\Omega$, and $P(B_i) > 0$ for all $i$, then for any event $A$ with $P(A) > 0$: $$P(B_k|A) = \frac{P(A|B_k)P(B_k)}{\sum_{i} P(A|B_i)P(B_i)}$$
*   **Theorem 1.24:** If events A and B are independent, then:
    1.  A and B^c are independent
    2.  A^c and B^c are independent

### Key Relationships and Implications

*   Disjoint events imply a simple addition rule for probabilities.
*   Conditional probability formalizes the idea of updating probability assessments based on new information.
*   Independence simplifies the calculation of probabilities involving intersections of events.
*   The Law of Total Probability decomposes the calculation of an event's probability based on a partition of the sample space.
*   Bayes' Theorem provides a way to update beliefs about an event given new evidence.
*   Pairwise independence does not imply independence for a family of events.

### Important Special Cases

*   **Finite sample spaces with equally likely outcomes:**  Simplifies calculation of probabilities.
*   **Disjoint events:** Simple addition rule for their probabilities.
*   **Independent events:** Simplification of probability calculations when events are intersected.
*   **Partition of the sample space:** Essential for applying Law of Total Probability and Bayes' Theorem.

### Key Conditions and Assumptions

*   The probability of any event is a non-negative number
*   The probability of the entire sample space is 1
*   Disjoint events have the sum of their probabilities equal to the probability of their union
*   The conditional probability formula is only defined when the conditioning event has a positive probability.

## Common Patterns and Techniques

### Key Proof Techniques Used in the Chapter

*   **Counting Arguments:**  Using combinations or permutations, often in conjunction with set theoretic arguments, to prove the results
*   **Direct Proof:** Showing a result by directly manipulating definitions and previously established facts.
*   **Set Theoretic Proofs:** Using Venn Diagrams and the properties of Set Operations to prove set-based results.
*   **Decomposition of events:** Breaking events down into disjoint components (using unions and intersections).
*   **Use of axioms:** Constructing the proofs based on the axiomatic definition of probability space.
*   **Generalization from simpler cases** Applying known results in simple cases to derive more general results

### Common Problem-Solving Strategies

*   **Identifying the sample space and events:**  Clearly define what is being observed or measured and then what we want to know about it.
*   **Using Counting Arguments:** Employing permutation and combination techniques as well as other counting tricks to find sizes of sets.
*   **Applying the multiplication rule:** Calculating probabilities of intersecting events when conditional probabilities are known or easily derived
*   **Using the Law of Total Probability:** Breaking down complicated events into more manageable cases.
*   **Applying Bayes' Theorem:** Inverting conditional probabilities when necessary.
*   **Checking if events are disjoint:** Apply a simple sum for unions of disjoint events.
*   **Checking if events are independent:** Simplify the calculations when calculating probabilities of intersections of independent events.

### Important Connections Between Concepts

*   Conditional probability and independence: Independence is defined through the relationship between a conditional probability and an unconditional probability.
*   Law of Total Probability and Bayes' Theorem:  Bayes' theorem can be derived using the Law of Total Probability along with the definition of conditional probability.
*   Counting and probability: Counting techniques are fundamental to calculations in discrete probability.
*   Axioms of Probability: They lay the foundation of how probability is defined and calculated.

### Typical Applications of Theorems

*   **Law of Total Probability:** Calculating overall probabilities when an event is contingent on other (partitioned) possibilities.
*   **Bayes' Theorem:** Inverting conditional probabilities to update beliefs given new data (e.g. medical testing, spam filtering).
*   **Multiplication Rule:** Calculating probabilities of a series of events.
*   **Inclusion-Exclusion Principle:** When events are not disjoint to avoid over-counting when looking for probabilities of unions.

This reference provides a comprehensive overview of Chapter 1, covering its core concepts and methods.  Let me know if you would like any clarification or have specific areas of focus!
