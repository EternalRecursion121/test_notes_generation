# Chapter 3 Flashcards

Okay, here are the flashcards based on Chapter 3 of the provided document, following your specified rules:

## Flashcards

### Basic Cards
START
Basic
What is a recurrence relation (or difference equation)?
Back: A recurrence relation (or difference equation) expresses a term in a sequence as a function of preceding terms.
Tags: chapter3, difference_equations, definition
END

START
Basic
What is a $k^{th}$ order linear recurrence relation?
Back: A $k^{th}$ order linear recurrence relation has the form $\sum_{j=0}^{k} a_j u_{n+j} = f(n)$, where $a_0 \neq 0$ and $a_k \neq 0$, and the $a_j$ are constants.
Tags: chapter3, difference_equations, definition
END

START
Basic
What does it mean for a sequence $(u_n)_{n \ge 0}$ to be a solution to a difference equation?
Back: A sequence $(u_n)_{n \ge 0}$ is a solution to a difference equation if it satisfies the equation for all $n \ge 0$.
Tags: chapter3, difference_equations, solution
END

START
Basic
In the context of solving difference equations, what does the term "homogeneous" mean?
Back: A homogeneous difference equation is one where $f(n) = 0$.
Tags: chapter3, difference_equations, homogeneous
END

START
Basic
When solving a linear difference equation, how is the general solution constructed?
Back: The general solution is the sum of a particular solution and the general solution of the associated homogeneous equation.
Tags: chapter3, difference_equations, general_solution
END

START
Basic
In a first order linear difference equation of the form $u_{n+1} = au_n + b$, what form does the homogeneous solution take?
Back: The homogeneous solution takes the form $w_n = A a^n$, where A is a constant.
Tags: chapter3, difference_equations, first_order_homogeneous
END

START
Basic
In the context of random walks, what does the term "random walk" refer to?
Back: A random walk is a process where a particle moves randomly through a series of locations, with the current position determining the probabilities of moving to other locations.
Tags: chapter3, random_walks, definition
END

START
Basic
In the gambler's ruin problem, what does $u_n$ represent?
Back: $u_n$ represents the probability that the gambler will eventually lose all their money given they start with £$n$ and the game stops when the gambler has either £0 or £M.
Tags: chapter3, random_walks, gambler_ruin
END

START
Basic
In the gambler's ruin problem, what does $M$ represent?
Back: $M$ represents the upper limit for the gambler's fortune at which point the gambler stops playing.
Tags: chapter3, random_walks, gambler_ruin
END

START
Basic
What is the auxiliary equation for a second order linear recurrence relation?
Back: For a recurrence relation $u_{n+1} + au_n + bu_{n-1} = 0$, the auxiliary equation is $\lambda^2 + a \lambda + b = 0$.
Tags: chapter3, difference_equations, auxiliary_equation
END

START
Basic
What is a "particular solution" in the context of solving linear difference equations?
Back: A particular solution is any solution to the non-homogeneous equation.
Tags: chapter3, difference_equations, particular_solution
END

START
Basic
In solving difference equations, when do you try a constant solution, and when do you need to try more complex solutions?
Back: Try a constant solution for the particular solution to a non-homogenous linear equation, unless a constant is a solution to the homogeneous equation (in which case try a polynomial in n).
Tags: chapter3, difference_equations, particular_solution_strategy
END

### Cloze Cards
START
Cloze
A $k^{th}$ order linear recurrence relation has the form $\sum_{j=0}^{k} {{c1::a_j}} u_{n+j} = f(n)$, where $a_0 \neq 0$ and $a_k \neq 0$.
Tags: chapter3, difference_equations, definition
END

START
Cloze
The general solution to a linear difference equation is the sum of a {{c1::particular solution}} and the general solution of the associated {{c2::homogeneous}} equation.
Tags: chapter3, difference_equations, general_solution
END

START
Cloze
In a first order linear difference equation of the form $u_{n+1} = au_n + b$, the homogeneous solution takes the form $w_n = {{c1::A a^n}}$, where A is a constant.
Tags: chapter3, difference_equations, first_order_homogeneous
END

START
Cloze
In the gambler's ruin problem, the probability of eventual bankruptcy starting with £$n$ is often denoted as ${{c1::u_n}}$.
Tags: chapter3, random_walks, gambler_ruin
END

START
Cloze
For the recurrence relation $u_{n+1} + au_n + bu_{n-1} = 0$, the auxiliary equation is ${{c1::\lambda^2 + a\lambda + b = 0}}$.
Tags: chapter3, difference_equations, auxiliary_equation
END

START
Cloze
If the auxiliary equation has distinct roots $\lambda_1$ and $\lambda_2$, the general solution to the homogeneous equation is $w_n = {{c1::A_1 \lambda_1^n + A_2 \lambda_2^n}}$.
Tags: chapter3, difference_equations, homogeneous_solution
END

START
Cloze
If the auxiliary equation has a repeated root $\lambda$, the general solution to the homogeneous equation is $w_n = {{c1::(A+Bn)\lambda^n}}$.
Tags: chapter3, difference_equations, homogeneous_solution
END

START
Cloze
In the gambler's ruin problem, if the probability of winning a single game is $p$ and the probability of losing is $q$, and $p \neq \frac{1}{2}$, then the probability of bankruptcy starting from £n is $u_n = \frac{1-(\frac{q}{p})^n}{1-(\frac{q}{p})^M}$
Tags: chapter3, random_walks, gambler_ruin
END

START
Cloze
For the random walk on integers, the probability that the walk ever hits 0 is 1 if the probability of going down, $q$, is greater than or equal to the probability of going up, $p$ and is $(\frac{q}{p})^n$ if $p>q$
Tags: chapter3, random_walks
END
