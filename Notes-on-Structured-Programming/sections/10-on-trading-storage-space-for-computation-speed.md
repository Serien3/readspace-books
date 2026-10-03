# 10. On trading storage space for computation speed

In present-day sequential computers (spring 1969) we can distinguish two main components, an active one (the processor) and a passive one (the store). The active component has the specific function to be fast, the passive one has the specific function to be large. The following is written on the assumption that this functional division is here to stay for a sufficient period of time to make a study of its consequences relevant.

From the point of view of the programmer storage space and computation time are then two distinct resources and I regard it as one of the responsibilities of the programmer – rather than of the system – to allocate them, i.e. to divide the load between them. It is to the consequences of this responsibility that the present section is devoted. This section is not devoted to techniques of estimating the various loads, i.e. to give quantitative criteria by which to influence the programmer’s choice: it is devoted to the logical relation between the alternatives between which the programmer may choose.

Note. It is not inconceivable that some of the choices can be left to the system. In all but the most trivial cases, however, design and establishment of the equivalence seem to require mathematical invention from the side of the programmer. All efforts to automate this problem-solving activity fall outside the scope of this monograph.

## 10.1 Storing Function Values and Updating on Demand

In its most simple form we are faced with a computation that regularly needs the value of “FUN(arg)”, where “FUN” is a given, computable function defined on the current value of one or more stored variables, collectively called “arg”. In version A of the program, only the value of arg is stored and the value of FUN(arg) is computed whenever needed. In version B, an additional variable, “fun” say, is introduced, whose sole purpose is to record the value of “FUN(arg)” corresponding to the current value of arg.

Where version A has

```text
arg ≔ …
```

(i.e. assignment to arg) version B will have

```text
arg ≔ …; fun ≔ FUN(arg)
```

thereby maintaining the relation `fun = FUN(arg)`. As a result of the validity of this relation, wherever version A calls for the evaluation of FUN(arg), version B will call for the current value of the variable fun.

There are two possible reasons to prefer version B to version A. When the value of FUN(arg) is more frequently requested than assignments to arg take place, version B could require less computation time. If necessary the technique can be refined by the introduction of a further (boolean) variable “fun up to date”, indicating whether the relation “fun = FUN(arg)” is assumed to hold. Assignment to arg is then associated with

```text
“fun up to date” ≔ false
```

whenever the value of FUN(arg) is needed, inspection of this boolean variable will tell, whether FUN(arg) has to be computed afresh; if so, the computed value will be assigned to fun and in accordance with its meaning “fun up to date” will be set to true. Let us call the last program version C.

It is clear that these three programs, only differing where version A assigns to arg or uses the value of FUN(arg) are equivalent as far as their output is concerned; it is certainly not inconceivable that version B or C is derived from version A by mechanical means.

## 10.2 Incremental Updates Based on How Values Change

But quite often the situation is not as simple as that and now we come to the second reason for introducing such a variable “fun”. Often it is very unattractive to compute FUN(arg) from scratch for arbitrary values of arg, while it is much easier to compute how the value of FUN(arg) changes when the value of arg is changed. In that case, the adjustment of the value of “fun” is more intimitely linked with the nature of the functional dependence than is suggested by

Often this possibility is not only intimately linked to the nature of the functional dependence, but also to the “history of the variable arg” as the computation proceeds! We have seen a very striking example in the program for the prime table (see Section “A first example of step-wise program composition”) with the introduction of “ord”, which is functionally dependent on “j”, viz. “ord” is the minimum value satisfying

$$p[ord]^2>j.$$

where the adjustment of “ord” was a very attractive operation thanks to the fact that “j” was monotonically increasing in time.

In my understanding of programs I want such additional variables that store redundant information, to be clearly recognized as such, even if it is a somewhat undefined functional relationship as in the case of the table “mult” from the same example. I am strongly inclined to view such programs as, say, optimizing refinements of a more abstract program, even when the optimization effected by the additional variables is essential when we want to make a program with a realistic performance.

From the point of view of efficiency such an additional variable may be so vital that it may strike one as irresponsible daydreaming to conceive a level in which its presence has been abstracted from. The way in which such an additional variable is manipulated is often experienced as the body of the algorithm: it is often there that we harvest the fruits of our mathematical ingenuity.

The point is that, although the possibility of at least one such optimizing refinement is essential for making something with a realistic performance, on closer inspection one often discovers that such an optimizing refinement is far from unique, even on its coarsest level.

Note. I remember one program in which the additional information was so redundant that not only the value of “fun” could be derived from that of “arg” but also the other way round. Suddenly the relation between “fun” and “arg” became symmetric and I have been seriously bothered by the question what did entitle me to treat them so asymmetrically.

The program in question generated all the solutions of a combinatorial puzzle. On closer inspection it turned out that there was a second combinatorial puzzle, where it could be proved that there existed a one-to-one correspondence between the solutions of the two problems. If I had solved the second combinatorial problem I would have found the role of “fun” and “arg” interchanged! In traditional programming, where such functional dependencies are not explicitly shown, the two puzzles would probably be solved by identical programs, whereas I made two differently structured programs.

And I think rightly so, for the single program for the two puzzles needed a different proof for its correctness, depending on which puzzle it was supposed to solve and this seems somewhat unfair when we also wish that our understanding of the computations be reflected in the structure of our programs!
