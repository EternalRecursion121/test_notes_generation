# Chapter 3 Revision Notes

Okay, here are the comprehensive revision notes for Chapter 3, as requested, with rigorous mathematical content, proper formatting, and explanatory comments:

# Chapter 3: Difference Equations and Random Walks

## 3.1 Difference Equations

### Introduction

*   Difference equations (also known as recurrence relations) are crucial tools in many areas of mathematics, including probability theory.
*   They describe the relationships between the terms of a sequence, rather than functions, like in differential equations.

---

### Example 3.1 (Gambler's Ruin)

> This example provides the motivation for introducing difference equations.

*   A gambler plays a game repeatedly, winning $\pounds 1$ with probability $p$ and losing $\pounds 1$ with probability $q = 1-p$ independently at each play.
*   The gambler stops when their fortune reaches $\pounds 0$ (bankruptcy) or $\pounds M$.
*   We want to find the probability $u_n$ that the gambler leaves with nothing given an initial fortune of $\pounds n$.
*   Conditioning on the outcome of the first play, we have:

$$ u_n = P(\text{bankruptcy} \mid \text{win 1st game}) P(\text{win 1st game}) + P(\text{bankruptcy} \mid \text{lose 1st game}) P(\text{lose 1st game})$$

*   Due to independence, if the gambler wins the first game, it's like starting over from $\pounds(n+1)$, and if they lose, from $\pounds(n-1)$. Therefore:

$$ u_n = p u_{n+1} + q u_{n-1}$$
This holds for $1 \le n \le M -1$.

*   We also have the boundary conditions:
    * $u_0 = 1$ (bankruptcy when starting with nothing is certain).
    * $u_M = 0$ (certainty of not being bankrupt when reaching M).

*   This is a second-order recurrence relation, which leads us to our formal definition of difference equations:

---

> ### Definition 3.2:  k-th Order Linear Recurrence Relation
> A k-th order linear recurrence relation (or difference equation) has the form
> $$ \sum_{j=0}^{k} a_j u_{n+j} = f(n) $$
> where $a_0 \ne 0$ and $a_k \ne 0$, and $a_0, \dots, a_k$ are known constants independent of $n$.  A solution to such a difference equation is a sequence $(u_n)_{n\geq0}$ that satisfies this equation for all $n\geq0$.

---
### Theorem 3.3: General Solution of Linear Recurrence Relation

*   The general solution $(u_n)_{n \ge 0}$ of
$$ \sum_{j=0}^{k} a_j u_{n+j} = f(n) $$
can be written as
$$ u_n = v_n + w_n $$
where $(v_n)_{n \ge 0}$ is a particular solution to the equation and $(w_n)_{n \ge 0}$ is any solution of the associated homogeneous equation:
$$ \sum_{j=0}^{k} a_j w_{n+j} = 0 $$

*   **Proof**:
    *   Since $a_k \ne 0$, we can write the equation as:

$$u_{n+k} = \frac{1}{a_k} \left[f(n) - \sum_{j=0}^{k-1} a_j u_{n+j} \right]$$
   *   We can always construct a solution by choosing $u_0 = u_1 = ... = u_{k-1} = 0$, which then defines $u_{n+k}$ inductively.
    *   Let $(v_n)_{n \ge 0}$ be a particular solution. Then consider any solution $(u_n)_{n \ge 0}$. We have:
$$ \sum_{j=0}^{k} a_j (u_{n+j} - v_{n+j}) = \sum_{j=0}^{k} a_j u_{n+j} - \sum_{j=0}^{k} a_j v_{n+j} = f(n) - f(n) = 0 $$
     * Therefore, $(u_n - v_n)_{n \ge 0}$ is a solution to the homogeneous equation. Letting $w_n = u_n - v_n$ implies that  $u_n = v_n + w_n$ as claimed.
     * The converse is true as well: If $(v_n)$ is a particular solution and $(w_n)$ is a solution to the homogenous equation then $u_n = v_n + w_n$ is a solution to the original equation.

---

## 3.2 First Order Linear Difference Equations

*   We will develop methods for solving linear difference equations through examples

### Example 3.4

*   Solve:
   $$u_{n+1} = au_n + b$$
    with $u_0 = 3$ and constants $a \neq 0$, $b$.

*   **Solution**:
    1.  **Homogeneous solution**: The associated homogeneous equation is $w_{n+1} = aw_n$. Putting into itself repeatedly, we get $w_n = a w_{n-1} = \dots = a^n w_0 = A a^n$ for some constant $A$ (where $A = w_0$).
    2.  **Particular solution**: Guess a constant solution $v_n = C$.  Substituting into the original equation, we get $C = aC + b$, which implies $C = \frac{b}{1-a}$, provided $a \ne 1$.
    3.  **General solution**: $u_n = A a^n + \frac{b}{1-a}$
    4.  **Applying initial condition**: $u_0 = 3 = A + \frac{b}{1-a}$. Thus, $A = 3 - \frac{b}{1-a}$.
    5.  **Final solution:**

       $$u_n = \left(3-\frac{b}{1-a}\right) a^n + \frac{b}{1-a} = 3a^n + \frac{b(1-a^n)}{1-a}$$

*   **Case when a=1**: If a=1, the particular solution attempt $v_n = C$ fails because $\frac{b}{1-a}$ is undefined. In this case, we should try a different particular solution $v_n = Cn$. Substituting, we have:
$$ C(n+1) = Cn + b  \implies C = b$$
*    The homogeneous solution is $w_n = A$. Then, the general solution is:
$$u_n = A + bn$$
    The initial condition $u_0 = 3$ implies that $A = 3$, so the final solution for $a=1$ is $u_n = 3 + bn$.

---

### Example 3.5

*   Solve:
$$u_{n+1} = au_n + bn$$

*   **Solution**:
    1.  **Homogeneous solution**: $w_n = Aa^n$.
    2.  **Particular solution**: Try $v_n = Cn + D$. Substituting this into the equation:
$$C(n+1) + D = a(Cn+D)+bn$$
    3. Equating coefficients, we have:
       *   Coefficients of n: $C = aC + b \implies C = \frac{b}{1-a}$ (provided $a \ne 1$).
       *   Constant terms: $C + D = aD \implies D = \frac{C}{a-1} = \frac{b}{(1-a)(a-1)}$.
    4.  **General solution**:
$$u_n = Aa^n + \frac{bn}{1-a} + \frac{b}{(1-a)^2}$$

    5.  To find A, we need a boundary condition (e.g., the value of $u_0$)

---

### Exercise 3.6

*   Solve the equation for $u_{n+1} = a u_n + b n^2$. (Hint: try $v_n = C n^2 + D n + E$)

### Solution:
*   The homogeneous solution is as before $w_n = A a^n$.
*   We try a particular solution of the form $v_n = Cn^2 + Dn + E$.
*   Substituting into the difference equation we get:
$$
C(n+1)^2 + D(n+1) + E = a(Cn^2+Dn+E) + bn^2
$$
*   Equating coefficients of $n^2$:
$$
C = aC + b \implies C = \frac{b}{1-a}, \quad a\neq 1
$$
*   Equating coefficients of $n$:
$$
2C+D=aD \implies D = \frac{2C}{a-1} = \frac{2b}{(1-a)(a-1)}, \quad a\neq 1
$$
*   Equating constants:
$$
C+D+E = aE \implies E=\frac{C+D}{1-a} = \frac{b(1-a+2)}{(1-a)^2(a-1)} = \frac{b(3-a)}{(1-a)^2(a-1)}
$$
*   Thus, the general solution is:
$$
u_n = A a^n + \frac{b n^2}{1-a} + \frac{2b n}{(1-a)(a-1)} +  \frac{b(3-a)}{(1-a)^2(a-1)}
$$

---

## 3.3 Second Order Linear Difference Equations

*   Consider:

$$ u_{n+1} + a u_n + b u_{n-1} = f(n) $$

* The general solution will depend on two constants.  The homogeneous equation is

$$  w_{n+1} + a w_n + b w_{n-1} = 0$$

*   Substitute $w_n = A \lambda^n$ :

$$  A \lambda^{n+1} + a A \lambda^n + b A \lambda^{n-1} = 0$$

Dividing by $A\lambda^{n-1}$ we obtain the auxiliary equation:

$$\lambda^2 + a\lambda + b = 0$$

*  If the roots, $\lambda_1$ and $\lambda_2$, are distinct, then the general solution to the homogeneous equation is

    $$w_n = A_1 \lambda_1^n + A_2 \lambda_2^n$$

*  If $\lambda_1 = \lambda_2 = \lambda$, then the general solution is
$$ w_n = (A + Bn) \lambda^n $$

### Exercise 3.7

*   Check that $w_n = (A + Bn) \lambda^n$ is indeed a solution to the homogeneous equation when $\lambda$ is a double root

### Proof:
*   If $\lambda$ is a repeated root, then $\lambda^2 + a \lambda + b = (\lambda-r)^2 = \lambda^2 -2r\lambda + r^2$ such that $a=-2r$ and $b=r^2$.
*   Let $w_n = (A+Bn)r^n$. Substitute into the homogenous equation we get:
$$
(A+B(n+1))r^{n+1} + a(A+Bn)r^n+b(A+B(n-1))r^{n-1} = 0
$$
*   Dividing by $r^{n-1}$:
$$
(A+Bn+B)r^2 + a(A+Bn)r+b(A+Bn-B) = 0
$$
*   Since $a=-2r$ and $b=r^2$
$$
(A+Bn+B)r^2 -2r(A+Bn)r+r^2(A+Bn-B) = 0
$$
$$
r^2[A+Bn+B-2A-2Bn+A+Bn-B] = 0
$$
$$
0 = 0
$$

Thus, $w_n = (A+Bn)r^n$ is indeed a solution.
---

### Example 3.8

*   Solve:

$$u_{n+1} + 2u_n - 3u_{n-1} = 1$$

*   **Solution**:
    1.  **Auxiliary equation:** $\lambda^2 + 2\lambda - 3 = 0$, which has roots $\lambda_1 = -3$, $\lambda_2 = 1$.
    2.  **Homogeneous solution**: $w_n = A(-3)^n + B$.
    3.  **Particular solution**: We cannot use a constant as a trial particular solution as we already know it's part of the homogeneous equation solution, therefore we try $v_n = Cn$. Substituting:
$$ C(n+1) + 2Cn - 3C(n-1) = 1$$
    4.  Simplifying: $Cn + C + 2Cn - 3Cn + 3C = 1 \implies 4C=1$. Therefore, $C = \frac{1}{4}$.
    5.  **General solution**: $u_n = A(-3)^n + B + \frac{1}{4}n$

---

### Example 3.9

*   Solve:
$$u_{n+1} - 2u_n + u_{n-1} = 1$$

*   **Solution**:
    1.  **Auxiliary equation**: $\lambda^2 - 2\lambda + 1 = 0$, which has a repeated root $\lambda = 1$.
    2.  **Homogeneous solution**: $w_n = A + Bn$.
    3.  **Particular solution**: We cannot use  $Cn$ as this is part of the homogeneous solution so we try $v_n=Cn^2$. Substituting:
$$ C(n+1)^2 - 2Cn^2 + C(n-1)^2 = 1 $$
    4.  Simplifying: $Cn^2 + 2Cn + C - 2Cn^2 + Cn^2 - 2Cn + C = 1 \implies 2C=1$, thus $C=1/2$.
    5.  **General solution**: $u_n = A + Bn + \frac{1}{2}n^2$

---

### Example 3.10 (Fibonacci Numbers)

*   The Fibonacci numbers, defined by $f_{n+2} = f_{n+1} + f_n$, with $f_0 = f_1 = 1$.

*   **Solution**:
    1.  **Auxiliary equation**: $\lambda^2 - \lambda - 1 = 0$, with roots $\lambda = \frac{1 \pm \sqrt{5}}{2}$.
    2.  **Homogeneous solution**: $f_n = A \left(\frac{1+\sqrt{5}}{2}\right)^n + B \left(\frac{1-\sqrt{5}}{2}\right)^n$
    3.  **Apply initial conditions**:

      $$ 1 = A + B$$
    $$  1 = A\frac{1+\sqrt{5}}{2} + B\frac{1-\sqrt{5}}{2} $$

    4. Solving for $A$ and $B$ we get: $A = \frac{1+\sqrt{5}}{2\sqrt{5}}$, $B = -\frac{1-\sqrt{5}}{2\sqrt{5}}$.
     5.   **Final Solution**:

      $$f_n = \frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^{n+1} -\frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^{n+1}$$

>Note that despite the fact that $\sqrt{5}$ is an irrational number this gives integer solutions

---

### Example 3.11

*   Solve:
$$u_{n+2} - 2u_{n+1} + 4u_n = 0,$$
with $u_0=u_1=1$

*   **Solution**:
    1.  **Auxiliary equation**: $\lambda^2 - 2\lambda + 4 = 0$, with roots $\lambda = 1 \pm i \sqrt{3}$.
    2.  **Homogeneous solution**: $u_n = A (1+i\sqrt{3})^n + B(1-i\sqrt{3})^n$
    3.  **Apply initial conditions**:

    $$ 1 = A + B $$
    $$ 1 = A(1 + i\sqrt{3}) + B(1 - i\sqrt{3})$$

    4. Solving for A and B, we find that $A = B = 1/2$.
    5.  **Final Solution**:

$$
u_n = \frac{1}{2}(1 + i\sqrt{3})^n + \frac{1}{2}(1 - i\sqrt{3})^n
$$

*   Note that $1+i\sqrt{3} = 2e^{i\pi/3}$ and $1 - i\sqrt{3} = 2e^{-i\pi/3}$ we can write:

$$u_n = \frac{1}{2}2^n\left(e^{in\pi/3} + e^{-in\pi/3} \right) = 2^n\cos(\frac{n\pi}{3})$$

---

## 3.4 Random Walks

### Introduction

* Random walks provide a general framework for analyzing stochastic processes such as the gambler's wealth. They are characterized by a sequence of steps that depend only on the current position, not on prior states.
*   They are used in modelling many real world phenomena

---

*   Returning to the Gambler's ruin problem we now consider a different approach
*   Recall that $u_n$ is the probability of bankruptcy with initial fortune $\pounds n$ and, rearranging equation (3.1) we have:
 $$pu_{n+1}-u_n+qu_{n-1}=0$$
   where $1 \leq n \leq M-1$, $u_0 = 1$ and $u_M = 0$
*    The auxiliary equation is then:
 $$ p\lambda^2 - \lambda + q = 0 $$
  This can be factorized as:
  $$(p\lambda - q)(\lambda - 1) = 0$$
  Therefore the roots are $\lambda_1 = q/p$ and $\lambda_2 = 1$

  * If $p \neq \frac{1}{2}$ then $\lambda_1 \neq \lambda_2$ and the general solution is
  $$ u_n = A + B \left( \frac{q}{p} \right)^n $$
   Using the boundary conditions we get:

     $$1 = u_0 = A+B$$
   $$0=u_M=A+B\left(\frac{q}{p}\right)^M$$
  Solving this we get:
  $$A = \frac{-\left(\frac{q}{p}\right)^M}{1-\left(\frac{q}{p}\right)^M}, \qquad B = \frac{1}{1-\left(\frac{q}{p}\right)^M}$$
  and so:

$$ u_n = \frac{1-\left(\frac{q}{p}\right)^n}{1-\left(\frac{q}{p}\right)^M} $$
---

### Exercise 3.12

*   Check that in the case $p = 1/2$, we get
    $$u_n = 1 - \frac{n}{M}, \quad 0 \le n \le M$$

   When $p=q=1/2$, the solution above is indeterminate because $\frac{q}{p} =1$
   In this case, we have repeated roots in the auxiliary equation and therefore the solution to the homogenous equation is:
   $$u_n = A + Bn$$
    Using the boundary conditions:
    $$1=u_0 = A \qquad 0=u_M = A+BM$$
    Thus we get $A=1$ and $B=-1/M$. Therefore $u_n = 1-\frac{n}{M}$

---

### Example 3.13

*   What is the expected number of plays in the gambler's ruin model before the gambler's fortune hits either 0 or M?
*   **Solution**:
*   Let $e_n$ be the expected number of steps given an initial fortune of $n$.  Conditioning on the first step, we get:
   $$e_n = pE[\text{steps} | \text{first step to } n+1] + qE[\text{steps} | \text{first step to } n-1]$$

   $$e_n = p(1+e_{n+1}) + q(1+e_{n-1})$$
   $$e_n = p+pe_{n+1} + q + qe_{n-1}$$
   Which rearranges to:
    $$p e_{n+1} - e_n + q e_{n-1} = -1$$

   with boundary conditions $e_0 = e_M = 0$.

*   The associated homogenous equation is
 $$p w_{n+1} - w_n + q w_{n-1} = 0 $$
which we solved earlier, the general solution is

    $$w_n = A + B \left( \frac{q}{p} \right)^n $$

* For a particular solution, try $v_n = Cn$. Substituting, we obtain
 $$ pC(n+1) - Cn + qC(n-1) = -1$$
$$ C(pn+p-n+qn-q) = -1$$
$$C(p-1+q) = -1$$
$$C(p-1+1-p) = -1$$
Then, $C = \frac{-1}{p-q}$. Therefore the general solution is:
   $$e_n = A + B \left( \frac{q}{p} \right)^n - \frac{n}{p-q} $$
  
*Using the boundary conditions we get
 $$e_0=0=A+B$$
$$e_M = 0 = A+B\left(\frac{q}{p}\right)^M - \frac{M}{p-q}$$
Solving for $A$ and $B$ we obtain
$$
e_n = \frac{M}{p-q} \frac{1-(q/p)^n}{1-(q/p)^M} - \frac{n}{p-q}
$$

---

### Exercise 3.14

* Find $e_n$ when $p=q=\frac{1}{2}$

### Solution

*   When $p=q=1/2$, the general solution to the homogenous equation is $A + Bn$. Try a particular solution of the form $Cn^2$ (as $Cn$ would be a part of the homogenous solution).
    Substituting this into:
 $$ \frac{1}{2}e_{n+1} - e_n + \frac{1}{2} e_{n-1} = -1$$
We get:
$$ \frac{1}{2} C(n+1)^2 - Cn^2 + \frac{1}{2} C(n-1)^2 = -1$$
which simplifies to:
$$ \frac{1}{2}C(n^2+2n+1)-Cn^2+\frac{1}{2}C(n^2-2n+1) = -1$$
$$ Cn^2+nC + \frac{C}{2} - Cn^2 +\frac{1}{2} Cn^2 -Cn+\frac{C}{2} = -1$$
Therefore, $C = -2$.
The general solution is:
$$
e_n = A + Bn - 2n^2
$$
Using the boundary conditions $e_0 = e_M = 0$:

$$ 0 = A $$
$$ 0 = B M - 2 M^2$$
Thus, $B = 2M$. Therefore,
$$e_n = 2Mn - 2n^2 = 2n(M-n)$$

---

*   Now, consider a random walk on the infinite set $\{0, 1, 2, ...\}$, starting at $n > 0$.
*   We are interested in the probability of hitting 0, that is, does the walk ever reach the site 0?
*   We can look at the probability of hitting 0 before $M$ and then send $M \rightarrow \infty$.
*   We have that $u_n^{(M)}$ represents the probability of the random walk hitting 0 before $M$ starting from $n$. We calculated this above:
$$ u_n^{(M)} = \frac{1-(\frac{q}{p})^n}{1-(\frac{q}{p})^M} $$
Taking the limit as $M \rightarrow \infty$:
$$ \lim_{M \rightarrow \infty} u_n^{(M)} = \begin{cases} \left( \frac{q}{p} \right)^n & \text{if } p > q \\ 1 & \text{if } p \leq q\end{cases} $$

---
### Theorem 3.15

>Consider a random walk on the integers $\mathbb{Z}$ started from some $n > 0$, which at each step increases by 1 with probability $p$ and decreases by 1 with probability $q=1-p$. Then, the probability $u_n$ that the walk ever hits 0 is given by
>$$u_n = \begin{cases} \left( \frac{q}{p} \right)^n & \text{if } p > q \\ 1 & \text{if } p \leq q\end{cases}$$

**Proof**:
*  Let $A_k$ be the event that the random walk starting at $n$ reaches 0 before reaching $k$.
*   We want the probability that the walk ever reaches 0, i.e., the probability of event $H = \bigcup_{k=1}^\infty A_k$.
*   Note that $A_k$ is an increasing sequence of events, i.e., $A_1 \subset A_2 \subset \dots$
*   Using **Proposition A.8**:
   $$P(\cup_{k=1}^\infty A_k) = \lim_{k\rightarrow \infty} P(A_k)$$
* We also know from the finite version that if the random walk started from $n$ and had barriers at $0$ and $M$, the probability of hitting $0$ before reaching $M$ is $u_n^{(M)}$. The event $A_M$ is exactly that, therefore $P(A_M) = u_n^{(M)}$.
* Thus, using the result for finite $M$:

$$
u_n = P(H) = \lim_{M\rightarrow \infty} u_n^{(M)} = \begin{cases} \left( \frac{q}{p} \right)^n & \text{if } p > q \\ 1 & \text{if } p \leq q\end{cases}
$$

---

These comprehensive notes should provide a good foundation for revising the material of Chapter 3.  Let me know if you have any questions or need further clarification.
