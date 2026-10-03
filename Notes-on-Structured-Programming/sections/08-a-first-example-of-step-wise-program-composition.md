# 8. A first example of step-wise program composition

In the section “On understanding programs.” I have stressed the need for systematic sequencing so that the structure of the computations could be reflected in the structure of our program: in this way we can speak of the joint structuring of program and computations. In the current section I shall now try to give a little bit more content to the still rather vague notion of structuring computations. It will be a first effort to exploit our powers of abstraction to reduce the appeal made to enumerative reasoning; it will be a consequent application of the decompositions mentioned in the section “On understanding programs.”.

Instead of presenting (as a ready-made product) what I would call a well-structured program I am going to describe in very great detail the composition process of such a program. I do this because programs are not there: on the contrary, they have to be made, and the kind of programs I am particularly interested in are those which I feel to be reasonably well suited to our powers of construction and conception.

The task is to instruct a computer to print a table of the first thousand prime numbers, 2 being considered as the first prime number.

Note 1. This example has been chosen because on the one hand it is sufficiently difficult to serve as a model for some of the problems encountered in programming, and on the other hand its mathematical background is so simple and familiar that our attention is not usurped by the problem.

Note 2. I do not claim that my final program will be “the best one”, measured by whatever yardstick any of my readers might care to choose. At least two readers of a previous version of this presentation – in which remainders were computed via a divide operation – reacted quite vehemently to it: “But everyone knows that the most efficient way to generate prime numbers is by using the Sieve of Eratosthenes.” thereby blocking their ability to read any further!

The basic pattern of my approach will be to compose the program in minute steps, deciding each time as little as possible. As the problem analysis proceeds, so does the further refinement of my program.

## 8.1 From the Overall Action to Two Subactions

When an algorithm has to be made, the desired computation has to be composed from actions corresponding to a well-understood instruction repertoire. The simplest form of the program is

**Description 0:**

```text
begin “print first thousand prime numbers” end
```

and when “print first thousand prime numbers” refers to an instruction from the well-understood repertoire, then description 0 solves the problem. For the sake of argument we assume that this instruction does not occur in the well-understood repertoire. Therefore we have to conceive a computation composed from “more primitive” actions that establishes the desired net effect. Our first proposal is to separate the generation of the prime numbers and their printing, and we propose

**Description 1:**

```text
begin variable “table p”;
    “fill table p with first thousand prime numbers”;
    “print table p”
end
```

describing that our computation consists of a time-succession of two actions and takes place in a state space containing a single variable, called “table p”. The first action assigns a value to this variable, the second action is controlled by the (then current) value of this variable.

Again, when “fill table p with first thousand prime numbers” and “print table p” occur in the well-understood repertoire (and “table p” occurs among the implicitly available resources) then our problem is solved. Again, for the sake of argument, we assume this not to be the case. This means that in our next refinement we have to express how the effect of these two actions can be established by two further (sub)computations. Apart from that we have to decide, how the information to be contained in the intermediate value of the still rather undefined object “table p” is to be represented.

Before going on, I would like to stress how little we have decided upon when writing down description 1, and how little of our original problem statement has been taken into account. We have assumed that the availability of a resource “table p” (in some form or other) would permit us to compute the first thousand prime numbers before printing starts, and under this assumption we have exploited that the computation of the primes can be conceived independently of the printing.

Of our original problem statement we have not taken into account very much more than that at least a thousand different prime numbers do exist (we had to assume this for the problem statement to make sense). At this stage it is still fairly immaterial what the concept “prime number” really means. Also: we have not committed ourselves in the least as regards the specific layout requirements of the print-out to be produced. Apparently it is the strength of our approach that the consequences of these two rather independent aspects of our original problem statement seem to have been allocated in the respective refinements of our two constituent actions. It suggests that we have been more or less successful in our effort to apply the golden principle “divide and rule”.

Resuming our discussion, however, we have to ask ourselves, to what extent the two subcomputations can now be conceived independently of each other. To be more precise “Have we now reached the stage that the design of the two subalgorithms (that have to evoke the two subcomputations) can be conceived by two programmers, working independently of each other?”.

When the two actions can no longer be regarded as invoked by instructions from the well-understood repertoire, neither can the variable “table p” any longer be regarded as an implicitly available resource. And in a way similar to the one in which we have to decompose the actions into subcomputations, we have to choose how the variable “table p” will be composed, viz., what data structure we select to represent the information to be handed over via “table p” from the first action to the second. At some point this has to be decided and the questions are “when?” and “how?”.

In principle, there seem to be two ways out of this.

The first one is to try to postpone the decision on how to structure “table p” into (more neutral, less problem-bound) components. If we postpone the decision on how to structure “table p”, the next thing to do is to refine one of the actions or both. We can do so, assuming a proper set of operations on the still mysterious object “table p”; finally we collect these operations and in view of their demands we design the most attractive structure of “table p”.

Alternatively, we can try to decide, here and now, upon the structure of “table p”. Once it has been decided how the table of the first thousand primes will be represented, the refinements of both actions can be done fairly independently of each other.

Both ways are equally tricky, for what will be an attractive algorithm for, say, the first subcomputation will greatly depend on the ease and elegance with which the assumed operations on “table p” can be realized, and if one or more turn out to be prohibitively clumsy, the whole edifice falls to pieces. Alternatively, if we decide prematurely upon a structure for “table p” we may well discover that then the subcomputations turn out to be awkward. There is no way around it: in an elegant program the structure of “table p” and the computations referring to it must be well-matched.

I think that the behaviour of the efficient programmer can be described as trying to take the easiest decision first, that is the decision that requires the minimum amount of investigation (trial and error, iterative mutual adjustment etc.) for the maximum justification of the hope that he will not regret it.

## 8.2 Choosing the Data Representation and Interface

In order not to make this treatment unduly lengthy we assume that the programmer finds the courage to decide that now the structure of “table p” is the first thing to be decided upon. Once this position has been taken, two alternatives immediately present themselves.

On the one hand we can try to exploit that “a table of the first 1000 primes” is not just a table of a thousand numbers – as would be a table of the monthly wages of 1000 employees in a factory – but that all these numbers are different from each other. Using this we can arrange the information with a linear boolean array (with consecutive elements associated with consecutive natural numbers) indicating whether the natural number in question is a prime number or not. Number theory gives us an estimation of the order of magnitude of the thousand-st prime number and thereby a boundary of the length of the array that will suffice. If we arrange our material in that way we have prepared an easy mechanism to answer the question “is n (less than the maximum) prime or not?”.

Alternatively, we can choose an integer array in which the successive prime numbers will be listed. (Here the same estimate, obtained by means of number theory, will be used, viz. when a maximum value of the integer array elements needs to be given a priori.) In the latter form we create a mechanism suited to answer the question “what is the value of the k-th prime number, for k ≤ 1000 ?”.

We grant the programmer the courage to choose the latter representation. It seems attractive in the printing operation in which it is requested to print the prime numbers and not to print natural numbers with an indication whether they are prime or not. It also seems attractive for the computing stage, if we grant the programmer the clairvoyance that the analysis of whether a given natural number is a prime number or not, will have something to do with the question of whether prime factors of the number to be investigated can be found.

The next stage of our program refinement then becomes the careful statement of a convention regarding the representation of the still mysterious object “table p” and a redefinition of the two operations in terms of this convention.

The convention is that the information to be contained in “table p” will be represented by the values of the elements of the “integer array p[1:1000]”, such that for 1 ≤ k ≤ 1000 p[k] will be equal to the k-th prime number, when the prime numbers are arranged in order of increasing magnitude. (If a maximum value of the integers is implicitly understood, we assume that number theory allows us to state that this is large enough.)

When we now want to describe this new refinement we are faced with a new difficulty. Our description 1 had the form of a single program, thanks to the fact that it was a refinement of the single action named “print the first thousand prime numbers”, refered *(sic)* to in description 0. (In more conventional terms: description 1 could have the form of a procedure body.) This no longer holds for our next level, in which we have to refine (simultaneously, in a sense) three named entities, viz. “table p” and the two actions, and we should invent some sort of identifying terminology indicating what refines what.

For the continuation of our discussion we make a very tentative proposal. We say: description 0 is a valid text expressed in terms of a single named action “print first thousand prime numbers”; let this be identified by the code 0a. Description 1 is called “1” because it is the next refinement of description 0; it contains a refinement of 0a – the only term in which description 0 is expressed – and is itself expressed in terms of three named entities to which we attach the codes:

| Code | Entity |
| --- | --- |
| 1a | table p |
| 1b | fill table p with first thousand prime numbers |
| 1c | print table p |

code numbers, starting with 1, because description 1 is expressed in terms of them, and “a”, “b” and “c” being attached for the purpose of distinction.

Now we have to describe our convention chosen for the representation of the information to be contained in “table p”, but this convention pertains to all three elements 1a, 1b and 1c. Therefore we call this description 2; it should contain the descriptions of the three separate elements (I use the equality sign as separator)

```text
1a = integer array p[1:1000]
1b = “make for k from 1 through 1000 p[k] equal to the k-th prime number”
1c = “print p[k] for k from 1 through 1000”
```

Description 2 is expressed in terms of three named entities to which we give (in the obvious order) the codes 2a, 2b and 2c. (In code numbers, description 2 is very meagre: it just states that for 1a, 1b and 1c, we have chosen the refinements 2a, 2b and 2c respectively.)

Remark. In the representation of the information to be contained in “table p”, we have chosen not to exploit the fact that each of the values to be printed occurs only once, nor that they occur in the order of increasing magnitude. Conversely, this implies that the action that has to take place under the name of 2c is regarded as a specific instance of printing any set of thousand integer values (it could be a table of monthly wages of thousand numbered employees!). The net effect of the printing action in this example is as uniquely defined as the first thousand prime numbers are: we conceive it, however, as a specific instance of a larger class of occurrences.

In the further refinement of 2c we deal with this whole class, the specific instance in this class being defined by the values of the elements of the array p. When people talk about “defining an interface” I often get the feeling that they overlook the presupposed generalization, the conception of the class of “possible” actions.

When 2b and 2c occur among the well-understood repertoire of instructions (and therefore 2a among the resources implicitly available) our whole problem is solved. For the sake of argument we again assume this not to be the case, and so we find ourselves faced with the task of conceiving subcomputations for the actions 2b and 2c. But now, thanks to the introduction of level 2, the respective refinements of 2b and 2c can be designed independently.

## 8.3 Generating Primes in Increasing Subscript Order

We now refine 2b: “make for k from 1 through 1000 p[k] equal to the k-th prime number”. We are looking for description 2b1, i.e. the first refinement of 2b. We introduce a fresh numbering after 2b (rather than calling our next description “3 something”) in order to indicate the mutual independence of the refinements of 2b and 2c respectively.

In description 2b1 we have to give an algorithm describing how the elements of the array p will get their values. This implies that we have to describe, for instance, in what order this will happen. In our first refinement we shall describe just that and preferably nothing more. An obvious, but ridiculous version starts as follows (with “version number” enclosed within parentheses):

**2b1(1):**

```text
begin p[1] ≔ 2; p[2] ≔ 3; p[3] ≔ 5; p[4] ≔ 7; p[5] ≔ 11; … end
```

implying that the programmer’s knowledge includes that of a table of the first thousand primes. We shall not pursue this version as it would imply that the programmer hardly needed the machine at all.

The first prime number being given (= 2), the thousand-st being assumed unknown to the programmer, the most natural order in which to fill the elements of the array p seems to be in the order of increasing subscript value, and if we express just that we arrive (for instance) at

**2b1(2):**

```text
begin integer k, j; k ≔ 0; j ≔ 1;
    while k < 1000 do
        begin “increase j until next prime number”;
            k ≔ k + 1; p[k] ≔ j
        end
end
```

By identifying k as the number of primes found and by verifying that our first prime number (= 2) is indeed the smallest prime number larger than 1 (= the initial value of j), the correctness of 2b1(2) is easily proved by mathematical induction (assuming the existence of a sufficient number of primes).

Description 2b1(2) is a perfect program when the operation described by “increase j until next prime number” – call it 2b1(2)a – occurs among the repertoire, but let us suppose that it does not. In that case we have to express in a next refinement how j is increased (and, again, preferably nothing more). We arrive at a description of level 2b2(2)

**Level 2b2(2):**

```text
2b1(2)a =
    begin boolean jprime;
        repeat j ≔ j + 1;
            “give to jprime the meaning: j is a prime number”
        until jprime
    end
```

Remark. Here we use the repeat-until clause in order to indicate that j has always to be increased at least once.

Again its correctness can hardly be subject to doubt. If, however, we assume that the programmer knows that, apart from 2, all further prime numbers are odd, then we may expect him to be dissatisfied with the above version because of its inefficiency. The price to be paid for this “lack of clairvoyance” is a revision of version 2b1(2). The prime number 2 will be dealt with separately, after which the cycle can deal with odd primes only. Instead of 2b1(2) we come to

**2b1(3):**

```text
begin integer k, j; p[1] ≔ 2; k ≔ 1; j ≔ 1;
    while k < 1000 do
        begin “increase odd j until next odd prime number”;
            k ≔ k + 1; p[k] ≔ j
        end
end
```

where the analogous refinement of the operation between quotes – “2b1(3)a” say – leads to the description on level 2b2(3):

**Level 2b2(3):**

```text
2b1(3)a =
    begin boolean jprime;
        repeat j ≔ j + 2;
            “give for odd j to jprime the meaning: j is a prime number”
        until jprime
    end
```

The above oscillation between two levels of description is in fact nothing else but adjusting to our convenience the interface between the overall structure and the primitive operation that has to fit into this structure. This oscillation, this form of trial and error, is definitely not attractive, but with a sufficient lack of clairvoyance and being forced to take our decisions in sequence, I see no other way: we can regard our efforts as experiments to explore (at a rather low cost!) where the interface can probably be most conveniently chosen.

Remark. Both 2b1(2) and 2b1(3) can be loosely described as

```text
begin “set table p and j at initial value”;
    while “table p not full” do
        begin “increase j until next prime number to be added”;
            “add j to table p”
        end
end
```

but we shall not do this as the sequencing in the two versions differs and – see “On comparing programs” – we regard them as “incomparable”. By choosing 2b1(3) we decide that our trial 2b1(2) – as 2b1(1) – is no longer applicable and therefore rejected.

The change from 2b1(2) to 2b1(3) is justified by the efficiency gain at the levels of higher refinement. This efficiency gain is earned at level 2b2, because now j can be increased by 2 at a time. It will also manifest itself in the still open primitive at level 2b2(3) where the algorithm for “give for odd j to jprime the meaning: j is a prime number” has only to cater for the analysis of odd values of j.

## 8.4 Trial Division by Known Primes

Again: in 2b2(3) we have refined 2b1(3) with an algorithm which solves our problem when “give for odd j to jprime the meaning: j is a prime number” – call it “2b2(3)a” – occurs among the well-understood repertoire. We now assume that it does not, in other words we have to evoke a computation deciding whether a given odd value of j has a factor. It is only at this stage that the algebra really enters the picture.

Here we make use of our knowledge that we only need to try prime factors: furthermore we shall use the fact that the prime numbers to be tried can already be found in the filled portion of the array p.

We use the facts that:

1. j being an odd value, the smallest potential factor to be tried is p[2], i.e. the smallest prime number larger than 2 
2. the largest prime number to be tried is p[ord-1] when p[ord] is the smallest prime number whose square exceeds j

Here I have also used the fact that the smallest prime number whose square exceeds j can already be found in the table p. In all humility I quote Don Knuth’s comment on an earlier version of this program, where I took this fact for granted:

> “Here you are guilty of a serious omission! Your program makes use of a deep result of number theory, namely that if pₙ denotes the n-th prime number we **always** have pₙ₊₁ < pₙ².”

Peccavi.

If this set is not empty, we have a chance of finding a factor, and as soon as a factor has been found, the investigation of this particular j value can be stopped. We have to decide in which order the prime numbers from the set will be tried, and we shall do so in order of increasing magnitude, because the smaller a prime number the larger the probability of its being a factor of j.

When the value of ord is known we can give for “give for odd j to jprime the meaning: j is a prime number” the following description on level 2b3(3):

```text
2b2(3)a =
    begin integer n; n ≔ 2; jprime ≔ true;
        while n < ord and jprime do
            begin “give to jprime the meaning: p[n] is not a factor of j”;
                n ≔ n + 1
            end
    end
```

But the above version is written on the assumption that the value of ord, a function of j, is known. We could have started this refinement with

```text
begin integer n, ord;
    ord ≔ 1; while p[ord] ↑ 2 ≤ j do ord ≔ ord + 1;
    …
```

i.e. recomputing the value of “ord” afresh, whenever it is needed. Here some trading of storage space for computation time seems indicated: instead of recomputing this function whenever we need it, we introduce an additional variable ord for its current value: it has to be set when j is set, it has to be adjusted when j is changed.

This, alas, forces upon us some reprogramming. One approach would be to introduce, together with j, an integer variable ord and to scan the programs in order to insert the proper operations on ord, whenever j is operated upon. I do not like this because at the level at which j is introduced and has a meaning, the function “ord” is immaterial, We shall therefore try to introduce ord only at its appropriate level and we shall be very careful.

## 8.5 Introducing ord at the Appropriate Level

For 2b: “make for k from 1 through 1000 p[k] equal to the k-th prime number” we write (analogous to level 2b1(3))

**Level 2b1(4):**

```text
begin integer k, j; p[1] ≔ 2; k ≔ 1;
    “set j to one”;
    while k < 1000 do
        begin “increase odd j until next odd prime number”;
            k ≔ k + 1; p[k] ≔ j
        end
end
```

Expressed in terms of:

| Code | Meaning |
| --- | --- |
| 2b1(4)a | increase odd j until next odd prime number |
| 2b1(4)b | set j to one |

In our next level we only introduce the subcomputation for 2b1(4)a, the other is handed down.

**Level 2b2(4):**

```text
2b1(4)a =
    begin boolean jprime;
        repeat “increase j with two”;
            “give for odd j to jprime the meaning: j is a prime number”
        until jprime
    end;
2b1(4)b = 2b2(4)b
```

Expressed in terms of:

| Code | Meaning |
| --- | --- |
| 2b2(4)b | still meaning “set j to one” |
| 2b2(4)c | increase j with two |
| 2b2(4)d | give for odd j to jprime the meaning: j is a prime number |

It is only at the next level that we need to talk about ord. Therefore we now write

**Level 2b3(4):**

```text
integer ord;
2b2(4)b =
    begin j ≔ 1; “set ord initial” end;
2b2(4)c =
    begin j ≔ j + 2; “adjust ord” end;
2b2(4)d =
    begin integer n; n ≔ 2; jprime ≔ true;
        while n < ord and jprime do
            begin “give to jprime the meaning: p[n] is not a factor of j”;
                n ≔ n + 1
            end
    end
```

Expressed in terms of:

| Code | Meaning |
| --- | --- |
| 2b3(4)a | set ord initial |
| 2b3(4)b | adjust ord |
| 2b3(4)c | give to jprime the meaning: p[n] is not a factor of j |

In our next level we give two independent refinements. (Note. We could have given them in successive levels, but then we should have to introduce an arbitrary ordering to these two levels. We could also try to treat the refinements separately – i.e. as separately as 2b and 2c –, but we feel that it is a little premature for this drastic decision.)

We are going to express  1) that, ord being a non-decreasing function of j and j only increasing in value, adjustment of ord implies a conditional increase;  2) that, whether p[n] is a factor of j is given by the question whether the remainder equal zero.

**Level 2b4(4):**

```text
2b3(4)a = 2b4(4)a;
2b3(4)b =
    begin while “ord too small” do “increase ord by one” end;
2b3(4)c =
    begin integer r;
        “make r equal to remainder of j over p[n]”;
        jprime ≔ (r ≠ 0)
    end
```

Expressed in terms of:

| Code | Meaning |
| --- | --- |
| 2b4(4)a | still meaning “set ord initial” |
| 2b4(4)b | ord too small |
| 2b4(4)c | increase ord by one |
| 2b4(4)d | make r equal to remainder of j over p[n] |

## 8.6 Reducing Computation with a Table of Multiples

If we have a built-in division, the implementation of “make r equal to the remainder of j over p[n]” can be assumed to be an easy matter. The case that the refinement of 2b4(4)d can be treated independently is now left to the interested reader. To give the algorithm an unexpected turn we shall assume the absence of a convenient remainder computation. In that case the algorithm

```text
r ≔ j; while r > 0 do r ≔ r - p[n]
```

would lead to the (non-positive) remainder but it would be most unattractive from the point of view of computation time. Again this asks for the introduction of some additional tabulated material (similar to the way in which “ord” has been introduced).

We want to know whether a given value of j is a multiple of p[n] for n < ord. In order to assist us in this analysis we introduce a second array in the elements of which we can store multiples of the successive prime numbers, as close to j as is convenient. In order to be able to give the size of the array we should like to know an upper bound for the value of ord; of course, 1000 would be safe, but number theory gives us 30 as a safe upper bound. We therefore introduce

```text
integer array mult[1:30]
```

and introduce the convention that for n < ord, mult[n] will be a multiple of p[n] and will satisfy the relation

$$mult[n]<j+p[n].$$

a relation that remains invariantly true under increase of j. Whenever we wish to investigate, whether p[n] is a factor of j, we increase mult[n] by p[n] as long as `mult[n] < j`. After this increase mult[n] = j is the necessary and sufficient condition for j to be a multiple of p[n].

The low maximum value of ord has another consequence: the inspection “ord too small” can be expressed by `p[ord] ↑ 2 ≤ j`, but this inspection has to be performed many times for the same value of ord. We may assume that we can speed up matters by introducing a variable (called “square”) whose value equals p[ord] ↑ 2 .

So we come to our final

**Level 2b5(4):**

```text
integer square; integer array mult[1:30];
2b4(4)a =
    begin ord ≔ 1; square ≔ 4 end;
2b4(4)b =
    (square ≤ j);
2b4(4)c =
    begin mult[ord] ≔ square;
        ord ≔ ord + 1; square ≔ p[ord] ↑ 2
    end;
2b4(4)d =
    begin while mult[n] < j do mult[n] ≔ mult[n] + p[n];
        r ≔ j - mult[n]
    end
```

which has made our computation close to an implementation of the Sieve of Eratosthenes!

Note. In the refinement of 2b4(4)d, when mult[n] is compared with the current value of j, mult[n] is increased as much as possible; this could have been done in steps of 2 * p[n], because we only submit odd values of j and therefore are only interested in odd multiples of p[n]. (The value of mult[1] remains, once set, equal to 4.)

The refinement of 2c “print p[k] for k from 1 through 1000” is left to the reader. I suggest that the table should be printed on five pages, each page containing four columns with fifty consecutive prime numbers.

## 8.7 Reviewing the Composition Process

Here I have completed what I announced at the beginning of this section, viz. “to describe in very great detail the composition process of such a [well-structured] program”. I would like to end this section with some comments.

The most striking observation is that our treatment of a very simple program has become very long, too long indeed to my taste and wishes, even if I take into account that essentially we did two things: we made a program and we discussed extensively the kind of considerations leading to it. It is not so much the length of the latter part that bothers me (writers fill whole novels with the description of human behaviour); what bothers me is the length of the texts at the various levels. Therefore we may expect that notational technique will be one of our main concerns.

But we have also had encouraging experiences. Giving full recognition to the fact that the poor programmer cannot decide all at once, we succeeded to a large extent in building up this program one decision at a time, and in our example quite a lot of programming was already done in its definite form while major decisions were still left open: irrespective of whether the final decisions are taken this way or that way, the coding of the earlier levels remains valid. In view of the requirement of program manageability, this is very encouraging.
