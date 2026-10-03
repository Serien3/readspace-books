# 13. On what we have achieved

One of the metaphors in which I find myself thinking about the program structure envisaged regards the program as a necklace, strung from individual pearls.

We have described the program in terms of levels and each level contained “refinements” of entities that were assumed available in higher levels. These refinements were either dynamic refinements (algorithms) or static refinements (data structures) to be understood by an appropriate machine. I use the term “pearl” for such a machine, refinements included.

Our previous program consists of a necklace of six pearls, in order either

```text
COMPFIRST         COMPFIRST
CLEARFIRST        CLEARFIRST
ISCANNER          ISCANNER
COMPPOS           COMPPOS
LINER             LINER
LONGREP           SHORTREP
```

LONGREP and SHORTREP are two different pearls, they explain the same concepts (from the “upper face”) into the same concept (of the “lower face”); only the particular refinements differ: they are as alternative programs for the same job and the same machine.

Changing a program will be treated as replacing one or more pearls of the original necklace by one or more other pearls. The pearl is the individual unit from which programs are composed. Making a program (as a member of a class of related programs) is now regarded as a two-stage process: making pearls (more than strictly necessary) and then stringing a fitting necklace out of (a selection of) them.

## 13.1 Why Use Pearls as Units of Modification

The reasons for this two-stage approach are many. In designing a program we have to consider many, many alternative programs and once our program is finished, we will have to change it (into one of the alternative ones). As long as programs are regarded as linear strings of basic symbols of a programming language and, accordingly, program modification is treated as text manipulation on that level, then each program modification must be understood in the universe of all programs (right or wrong!) that can be written in that programming language. No wonder that program modification is then a most risky operation!

The basic symbol is too small and meaningless a unit in terms of which to describe this. The pearl, embodying the independent design decision or, as the case may be, an isolated aspect of the original problem statement, is meant to be the natural unit for such modifications.

To rephrase the same argument: with the birth of ALGOL 60, syntax was discovered as a powerful means for expressing structure in a program text. (Syntax became so glorified that many workers in the field identified Computing Science with Syntactic Analysis!) It was slightly overlooked, however, that by expressing structure via syntax, this structure is only given very indirectly, i.e. to be derived by means of a parsing algorithm to be applied to a linear sequence of basic symbols.

This hurts if we realize that many a program modification leaves large portions of the structure unaffected, so that after painful re-parsing of the modified text the same structure re-emerges! I have a strong feeling that the adequacy of context-free methods for the representation of structure has been grossly overestimated.

In my immediate environment the following program bug in an ALGOL 60 program was brought to my attention. A program produced erroneous output with a completely checking implementation which in addition to the program text requires a final “progend” after the last “end”; this additional character is refused everywhere else so that a correct “begin – end” bracketing can be established. It turned out that

1. somewhere in the program a closing string quote was omitted;
2. somewhere further down in the program text an opening string quote was omitted;
3. the “begin – end” structure of the resulting program was syntactically correct;
4. the identifiers declared between the two omissions were only used between the two omissions, so that even context-dependent checks were unable to give alarm.

Having already my doubt as to the adequacy of context-free methods for expressing macroscopic structure, I was delighted when this bug was shown to me !

The more I think about pearls, the more I feel that something like them is the only way out of it, if we recognize our responsibility to take (for a large program) say a thousand (possible) versions into consideration. You cannot expect the programmer to make all these thousand versions from scratch, independent of each other.

The only way I see to produce such a potential variety is by a combinatorial technique, i.e. by making more pearls (say 250) than needed for a single necklace (say 200) and stringing a necklace from a particular selection. I see no other feasible way. The other mechanism to achieve great variety by combinatorial means is permutation, but this is denied to us because the final necklace must be a fitting necklace and, given the pearls, the order in which they have to be strung on the thread to produce a fitting necklace is pretty well defined. And also: if it is not, the permissible change of order is pretty irrelevant!

## 13.2 Interfaces and the Range of Validity of Concepts

Also, the pearl gives a clear status to an “incomplete” program, consisting of the top half of a necklace: it can be regarded as a complete program to be executed by a suitable machine (of which the bottom half of the necklace gives a feasible implementation). As such, the correctness of the upper half of the necklace can be established regardless of the choice of the bottom half.

Between two successive pearls we can make a “cut” which is a manual for a machine, provided by the part of the necklace below the cut and used by the program represented by the part of the necklace above the cut. This manual serves as an interface between the two parts of the necklace. We feel this form of interface more helpful than regarding data-representation as an interface between operations, in particular more helpful towards ensuring the combinatorial freedom required when a program has to be adapted.

Another remark concerns the range of validity of concepts along the necklace. For instance, the concept “image” is introduced in our top pearl “COMPFIRST” and is explained away in our bottom pearl but one, viz. “LINER”. If we now come to the conclusion that the program as envisaged is too demanding on storage space so that we cannot afford to introduce the variable “image”, we are faced with a major program revision and we have to replace the top five pearls by other ones, because that is the range of validity of the concept “image”! The bottom pearl (either “LONGREP” or “SHORTREP”), however, can be retained. (I mention this as an example of the fact that pearl exchange is by no means restricted to exchange of the bottom pearl.)

With respect to the validity range of concepts along the necklace I would like to ask your attention for an observation which thrilled me the first time I made it. (In retrospection it is pretty obvious and that is exactly why it may be worth-while to be explicit about it.) With each pearl we associate “an independent design decision” and the ordering of the pearls along the necklace therefore implies an ordering of the design decisions. Can we change this order? Yes, we can, although we then have different pearls.

By way of experiment I have followed the well-known advice: if you are faced with two primitives – in our case “build” and “print” – decide immediately upon their interface – in our example “image” – so that the two primitives can now be refined independently of each other. So I did, and I came to the following form of necklace

```text
COMPFIRST
LINER′
CLEARFIRST′
ISCANNER′
COMPPOS′
SHORTREP
```

(the four middle pearls being primed to indicate that they refer to different pearls, although they embody the same decisions as the ones in the original set.) The resulting program is much messier. Why?

Along the necklace we can indicate for each concept its range of validity: of course they overlap and we can view them as the individual threads from which the whole explanation is twined, as a kind of “logical rope”. The messy version has a logical rope twined from more and sometimes longer individual threads: its logical rope is thicker, the whole construction is more tightly interconnected.

The observation thrilled me because it gave a very convincing demonstration (at least for me!) that elegance, clarity and the 1ike have indeed marked quantitative aspects (as Mozart knew: many if his compositions that make one catch one’s breath are misleadingly simple, they seem to be made just out of practically nothing!).

## 13.3 The Benefits of Postponing Representation Decisions

We can phrase the observation in more technical terms. The primed version is messy because the image is explained away in terms of lines at too early a stage, thereby forcing us to explain “CLEARFIRST”, “ISCANNER” and “COMPPOS” in terms of lines, while they could still be explained in terms of the image, i.e. independent of the representation to be chosen for it.

Or, in other words, in the original version we have made a more judicious exploitation of our power of abstraction than in the primed one. The larger the number of pearls independent of the particular representation, the more adaptable one’s program and the more easily understandable – because that set of pearls can be understood at a higher level of abstraction.

The experience seems to indicate that the goals of adaptability and clarity have been given some substance and (what is more) go by their very nature hand in hand. This is very encouraging (although not surprising).

It also gives – me at least – a somewhat clearer picture of the scope of my present efforts. Whatever I shall develop, it will not be a General Problem Solver, not a mechanical one, not even one written for the benefit of the human problem solver. But it may give the human some appreciation for the various aspects of “elegance” of a solution when he succeeds in finding one. And as such it may give him a guide line.
