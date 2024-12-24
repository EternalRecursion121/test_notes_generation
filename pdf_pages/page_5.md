## 1.2 Counting

Many of you will have seen before the basic ideas involving permutations and combinations. If you haven't, or if you find them confusing, then you can find more details in the first chapter of *Introduction to Probability* by Ross.

### Arranging distinguishable objects

Suppose that we have *n* distinguishable objects (e.g. the numbers 1, 2,..., *n*). How many ways to order them (permutations) are there? If we have three objects *a*, *b*, *c* then the answer is 6: *abc*, *acb*, *bac*, *bca*, *cab* and *cba*.

In general, there are *n* choices for the first object in our ordering. Then, whatever the first object was, we have *n* - 1 choices for the second object. Carrying on, we have *n* - *m* + 1 choices for the *m*th object and, finally, a single choice for the *n*th. So there are

*n*(*n* - 1) ... 2.1 = *n*!

different orderings.

Since *n*! increases extremely fast, it is sometimes useful to know Stirling's formula:

$$ n! \sim \sqrt{2\pi n}n^{n+\frac{1}{2}}e^{-n} $$

where *f(n)* ~ *g(n)* means *f(n)*/*g(n)* → 1 as *n* → ∞. This is astonishingly accurate even for quite small *n*. For example, the error is of the order of 1% when *n* = 10.

### Arrangements when not all objects are distinguishable

What happens if not all the objects are distinguishable? For example, how many different arrangements are there of *a*, *a*, *a*, *b*, *c*, *d*?

If we had *a*<sub>1</sub>, *a*<sub>2</sub>, *a*<sub>3</sub>, *b*, *c*, *d*, there would be 6! arrangements. Each arrangement (e.g. *b*, *a*<sub>2</sub>, *d*, *a*<sub>3</sub>, *a*<sub>1</sub>, *c*) is one of 3! which differ only in the ordering of *a*<sub>1</sub>, *a*<sub>2</sub>, *a*<sub>3</sub>. So the 6! arrangements fall into groups of size 3! which are indistinguishable when we put *a*<sub>1</sub> = *a*<sub>2</sub> = *a*<sub>3</sub>. We want the number of groups which is just 6!/3!.

We can immediately generalise this. For example, to count the arrangements of *a*, *a*, *a*, *b*, *b*, *d*, play the same game. We know how many arrangements there are if the *b*’s are distinguishable, but then all such arrangements fall into pairs which differ only in the ordering of *b*<sub>1</sub>, *b*<sub>2</sub>, and we see that the number of arrangements is 6!/3!2!.

**Lemma 1.1.** The number of arrangements of the *n* objects

$$ \underbrace{\alpha_1,\dots,\alpha_1}_{m_1 \text{ times}},\underbrace{\alpha_2,\dots,\alpha_2}_{m_2 \text{ times}}, \dots, \underbrace{\alpha_k,\dots,\alpha_k}_{m_k \text{ times}} $$

where *α*<sub>i</sub> appears *m*<sub>i</sub> times and *m*<sub>1</sub> + ... + *m*<sub>k</sub> = *n* is

$$ \frac{n!}{m_1!m_2!\dots m_k!} \qquad (1.1) $$

**Example 1.2.** The number of arrangements of the letters of *STATISTICS* is  $\frac{10!}{3!3!2!}$.

If there are just two types of object then, since *m*<sub>1</sub> + *m*<sub>2</sub> = *n*, the expression (1.1) is just a binomial coefficient, $\binom{n}{m_1} = \frac{n!}{m_1!(n-m_1)!} = \binom{n}{m_2}$.

Note: we will always use the notation

$$ \binom{n}{m} = \frac{n!}{m!(n-m)!} $$
