# 7. On comparing programs

It is a programmer’s everyday experience that for a given problem to be solved by a given algorithm, the program for a given machine is far from uniquely determined. In the course of the design process he has to select between alternatives; once he has a correct program, he will often be called to modify it, for instance because it is felt that an alternative program would be more attractive as far as the demands that the computations make upon the available equipment resources are concerned.

These circumstances have raised the question of the equivalence of programs: given two programs, do they evoke computations establishing the same net effect? After suitable formalization (of the way in which the programs are given, of the machine that performs the computations evoked by them and of the “net effect” of the computations) this can presumably be made into a well-posed problem appealing to certain mathematical minds. But I do not intend to tackle it in this general form.

On the contrary: instead of starting with two arbitrarily given programs (say: independently conceived by two different authors) I am concerned with alternative programs that can be considered as products of the same mind and then the question becomes: how can we conceive (and structure) those two alternative programs so as to ease the job of comparing the two?

I have done many experiments and my basic experience gained by them can be summed up as follows. Two programs evoking computations that establish the same net effect are equivalent in that sense and a priori not in any other. When we wish to compare programs in order to compare their corresponding computations, the basic experience is that it is impossible (or fruitless, unattractive, or terribly hard or what you wish) to do so when on the level of comparison the sequencing through the two programs differs.

To be a little bit more explicit: it is only attractive to compare two programs and the computations they may possibly evoke, when paired computations can be parsed into a time-succession of actions that can be mapped on each other and the corresponding program texts can be equally parsed into instructions, each corresponding to such an action.

This is a very strong condition. Let me give a first example.

## 7.1 The Levels of Selection and Repetition Cannot Be Freely Interchanged

Excluding side-effects of the boolean inspections and assuming the value “B2” constant (i.e. unaffected by the execution of either “S1” or “S2”), we can establish the equivalence of the following two programs:

Program (1):

```text
if B2 then
    begin while B1 do S1 end
else
    begin while B1 do S2 end
```

Program (2):

```text
while B1 do
    begin if B2 then S1 else S2 end
```

The first construction is primarily one in which sequencing is controlled by a selective clause, the second construction is primarily one in which sequencing is controlled by a repetitive clause. I can establish the equivalence of the output of the computations, but I cannot regard them as equivalent in any other useful sense. I had to force myself to the conclusion that (1) and (2) are “hard to compare”. Originally this conclusion annoyed my very much. In the meantime I have grown to regard this incomparability as one of the facts of life and, therefore, as one of the major reasons why I regard the choice between (1) and (2) as a relevant design decision, that should not be taken without careful consideration.

It is precisely its apparent triviality that has made me sensitive to the considerations that should influence such a choice. They fall outside the scope of the present section but I hope to return to them later.

## 7.2 Two Programs for Array Equality

Let me give a second example of incomparability that is slightly more subtle.

Given two arrays X[1:N] and Y[1:N] and a boolean variable “equal”, make a program that assigns to the boolean variable “equal” the value: “the two arrays are equal element-wise”. Empty arrays (i.e. N = 0) are regarded as being equal.

Introducing a variable j and giving to “equal” the meaning “among the first j pairs no difference has been detected”, we can write the following two programs.

Program (3):

```text
j ≔ 0; equal ≔ true;
while j ≠ N do
    begin j ≔ j + 1; equal ≔ equal and (X[j] = Y[j]) end
```

Program (4):

```text
j ≔ 0; equal ≔ true;
while j ≠ N and equal do
    begin j ≔ j + 1; equal ≔ (X[j] = Y[j]) end
```

(4) differs from program (3) in that repetition is terminated as soon as a pair-wise difference has been detected. For the same input the number of repetitions may differ in the two programs and therefore the programs are only comparable in our sense as long as the last two lines of the programs are regarded as describing a single action, not subdivided into subactions. But what is their relation when we do wish to take into account that they both end with a repetition? To find this out, we shall prove the correctness of the programs.

On the arrays X and Y we can define of 0 ≤ j ≤ N the N + 1 functions EQUAL<sub>j</sub>  as follows:

$$\operatorname{EQUAL}_0=\mathrm{true},$$

$$\operatorname{EQUAL}_j=\operatorname{EQUAL}_{j-1}\ \mathrm{and}\ (X[j]=Y[j]),\quad j>0. \tag{5}$$

In terms of these functions it is required to establish the net effect `equal = EQUAL_N`. Both programs maintain the relation for increasing values of j, starting with j = 0:

$$equal=\operatorname{EQUAL}_j. \tag{6}$$

It is tempting to regard both programs (3) and (4) as alternative refinements of the same (abstract) program (7):

```text
j ≔ 0; equal ≔ EQUAL₀;
while “perhaps still: equal ≠ EQUAL_N” do
    begin j ≔ j + 1; “equal ≔ EQUAL_j” end
```

in which “perhaps still: equal ≠ EQUAL<sub>N</sub>” stands for some sort of still open primitive. When this is evaluated `equal = EQUAL_j` will hold and the programs (3) and (4) differ in that they guarantee on different criteria that “equal” will have its final value EQUAL<sub>N</sub>.

(3) The criterion is very naive, viz. `j = N`. At the beginning of the repeated statement `equal = EQUAL_j` still holds. After the execution of “j ≔ j + 1” therefore `equal = EQUAL_{j-1}` holds and the assignment statement:

```text
equal ≔ equal and (X[j] = Y[j])
```

is now a straightforward transcription of the recurrence relation (5).

To come to program (4) some analysis has to be applied to the recurrence relation (5), from which can be derived (by mathematical induction again) that EQUAL<sub>j</sub> = false implies EQUAL<sub>N</sub> = false, and therefore EQUAL<sub>j</sub> = false implies EQUAL<sub>j</sub> = EQUAL<sub>N</sub>. If this situation arises, the equality “equal = EQUAL<sub>N</sub>” can also be guaranteed and this leads to program (4).

(4) The set of (sub)computations the repeated statement has to cope with is restricted to those with the initial state “equal = true” end therefore in program (4) the assignment “equal ≔ EQUAL<sub>j</sub>” can be abbreviated to

```text
equal ≔ (X[j] = Y[j])
```

And now it is clear why the introduction of (7) as an abstraction of (3) and (4) was misleading. With “perhaps still: equal ≠ EQUAL<sub>N</sub>” we have stated the meaning of truth and falsity of a boolean expression without stating the expression itself and that was very tricky. We have tried to interpret (7) as a program in which part of the sequencing at its own level was undefined and varying over its refinements. As a result we have tried to view the last lines of (7) as a model for the last lines of both (3) and (4), but this was misleading because the computations to be evoked by them cannot be brought into a one-to-one correspondence.

So much about programs that we consider as incomparable. Examples of comparable programs will be encountered in the following sections. A final remark: we have stated that “paired computations can be parsed into a time-succession of actions that can be mapped on each other”. We have not required that actions so paired should have the same net effect! We may compare alternative programs for the same job but also different programs for similar jobs.
