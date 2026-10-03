# 14. On grouping and sequencing

While we are considering a programming tool in which explicit recognition has been given to the hierarchy of levels of abstraction, the present section is also applicable to programming in programming languages as they are understood today, viz. on a constant semantic level. (And there is a fair chance that the current section has its morals outside the restricted field of programming, for it seems to be concerned with problem solving in general.)

I shall illustrate my point with two examples, both of which, again, I have used in viva voce examinations. I owe the first example to Niklaus Wirth.

## 14.1 Sequences Without Equal Adjoining Subsequences

The problem is to construct a program generating non-empty sequences of 0’s, 1’s and 2’s without non-empty, element-wise equal, adjoining subsequences, generating these sequences in alphabetical order until a sequence of length 100 (i.e. of 100 digits) has been generated. The programmer may make use of the knowledge that a sequence of length 100 and satisfying the conditions actually exists. The start of the list of sequences to be generated is:

```text
0
01
010
0102
01020
010201
0102010
0102012
…
```

Each solution (apart from the first one) is an extension (by one digit) of an earlier solution and the algorithm is therefore a straightforward backtracking one.

We are looking for the “good” sequences, we assume a primitive available for the investigation of whether a trial sequence is good. If it is good, the trial sequence is printed and extended with a zero to give the next trial sequence; if the trial sequence is no good, we perform on it the operation “increase” to get the next trial sequence, i.e. final digits = 2 are removed and then the last remaining digit is increased by 1.

(The operations “extend with zero” and “increase” guarantee that trial sequences are generated in alphabetical order, the solutions, being a selection from them, will then be printed in alphabetical order as well.) The algorithm will start investigating the following trial sequences, those marked by an asterisk will be rejected as “no good”:

```text
  0
* 00
  01
  010
* 0100
* 0101
  0102
  01020
* 010200
  010201
  0102010
* 01020100
* 01020101
* 01020102
* 0102011
  0102012
  …
```

I found the majority of my students inclined to make a program with the following structure:

```text
set trial sequence to single zero;
repeat
    if good then
        begin print trial sequence; extend trial sequence with zero end
    else
        increase trial sequence
until length = 101
```

Although a program along these lines produces the correct output, objections can – and to my taste: should – be made against it.

The first objections regards the stopping criterion: when a solution of length 100 has been printed, we (knowing the algorithm) can deduce that after that for the first time the trial sequence will have length = 101 and this is now the criterion to stop, but this is a rather indirect and tortuous way to establish the stopping criterion. (How tortuous it is was clearly demonstrated by those students who did not see that an unnecessary trial sequence was generated and declared for the trial sequence an array of 100 elements instead of 101.)

The second objection is that the operation “increase trial sequence” never increases its length: after rejection of a trial sequence a superfluous test on the length is performed.

(When I used this example for student examinations I had not stressed very explicitly in my lectures any problem solving principles, so my disappointment was not too severe. In a sense I am glad to have observed these examinations, for it was for me an incentive to stress problem solving principles as far as I could find, formulate and teach them.)

The program to which the above objections do not apply treats the empty sequence as a virtual solution, not to be printed. It has – to the same level of detail – the following structure:

```text
set trial sequence empty;
repeat
    extend trial sequence with zero;
    while no good do increase trial sequence;
    print trial sequence
until length = 100
```

Here length is the length of the solution printed (if any), thus avoiding the tortuous reasoning for the stopping criterion. Also no superfluous last trial sequence (never to be investigated) will be generated, thanks to the fact that we have two loops inside each other, superfluous length testing no longer occurs.

Those for whom efficiency is the main criterion will probably be most convinced by the last observation. I myself, who attach considerable importance to understandability, am attracted to the latter program because I can interpret it as a further refinement of the program structure

```text
set sequence empty;
repeat
    transform sequence to next solution;
    print sequence
until length = 100
```

This (more abstract) program is only concerned with sequences that are solutions: on this level of description one can ignore that the transition from one solution to the next takes place via a sequence of trial solutions that turn out to be failures.

## 14.2 The Smallest Number with at Least Two Decompositions into Sums of Powers

I owe to Joe Weizenbaum the second example. Make a program that, for given positive integer n, determines the smallest number s that can be decomposed into the sum of two n-th powers in at least two non-trivially different ways.

For example:

$$n=1:\quad s=2=0^1+2^1=1^1+1^1.$$

$$n=2:\quad s=25=0+5^2=3^2+4^2.$$

$$n=3:\quad s=1729=1^3+12^3=9^3+10^3.$$

$$n=4:\quad s=635318657=59^4+158^4=133^4+134^4.$$

> **Translator’s note**: As the examples indicate, the bases are non-negative integers. “Non-trivially different” excludes differences consisting only of interchanging the two summands.

When I first used this example in an oral examination, it took the student twenty minutes to get somewhat familiar with the problem and he then sketched a searching algorithm which – when patched up – could indeed find a number that allowed multiple decompositions into sums of two n-th powers, but he could not prove that when his algorithm produced a value s that it would be the minimum value. (As a matter of fact he had, up till then, ignored that part of the problem statement.)

He then regrouped his forces and made a program of the following form:

```text
integer s, k;
s ≔ 1;
repeat
    s ≔ s + 1;
    k ≔ “the number of ways in which s can be decomposed as the sum of two n-th powers”
until k > 1
```

thus arriving at a hopelessly inefficient algorithm. The error he made was the decision at too early a stage to investigate the natural numbers in succession, the overwhelming majority of which are not decomposable at all.

Reasoning that the value we are looking for is the smallest decomposable number satisfying an additional property, one comes to an algorithm whose first sketch could be

```text
integer k, s, t;
t ≔ 1; (and further initialization);
repeat
    s ≔ “smallest decomposable value larger than t”;
    k ≔ “the number of ways the above minimum is obtained”;
    t ≔ s
until k > 1
```

By storing a collection of triples (number pairs with their corresponding s-value), among which each time the pair(s) with minimum s-value exceeding t will occur and adjusting this collection each time t is increased, a program emerges that is orders of magnitude more efficient, t jumping from decomposable value to the next decomposable value.

Programming (or problem solving in general?) as the judicious postponement of decisions and commitments!

---

transcribed by Jonathan David Arndt  revised  06-Aug-2022
