# 12. A second example of step-wise program composition

With a picture of program structure as a layered hierarchy of machines emerging, my fingers are itching to play with it, i.e. to make another program. The notational techniques employed should not be regarded as a well-considered proposal: they have been chosen to suit my fancy and should be regarded as part of the experiment.

## 12.1 The Problem: Plotting with a Line Printer

The problem is the following one. There is given a line printer which is controlled by two commands “NLCR” (New Line Carriage Return) which defines the utmost left position of the next line as the “currently printable position”, and the command “PRSYM(n)” which prints a character identified by the value of the integer parameter n on the currently printable position and defines the position immediately to the right of the printed position as the new currently printable position. (For our discussion we can regard lines of infinite length as permissible.)

We shall only make use of two specific values of n, called “space” and “mark” respectively. “PRSYM(space)” causes the currently printable position to remain blank, “PRSYM(mark)” will print a given, visible character, some sort of asterisk say.

Furthermore two integer function of an integer argument are given, satisfying

$$0\le i<1000\quad\Longrightarrow\quad0\le fx(i)<100,\quad0\le fy(i)<50.$$

Now we have to make a program printing 50 lines, numbered from top to bottom by a y-co-ordinate running from 49 through 0, the positions on a line being numbered from left to right by an x-co-ordinate running from 0 through 99. On the thousand positions (or less in the case of coincidence) given by

$$x=fx(i),\qquad y=fy(i),$$

a mark has to be printed; all other positions on the paper have to remain blank. In other words: a curve is given in a discrete parameter representation and we wish to use the line printer as a digital plotter.

I have used this problem extensively in viva voce examinations and the majority of the students quickly discover that, due to the absence of OLCR (Old Line Carriage Return) and of a “backspace”, the order in which the printable positions have to be served is dictated by the printing commands and, secondly, that this order has nothing to do with the order of the marks if we number them, say, in the order of increasing i.

As a result they quickly conclude that the use of storage seems indicated: first the thousand i-values should be scanned, i.e. the page image should be stored in a convenient manner, while afterwards, under control of the stored image, the page should be printed. (To be more precise: we assume that the computer has sufficient store for this purpose and that the computation of the function values “fx(i)” and “fy(i)” may be so time-consuming that we wish to have them computed only once for each i-value.)

## 12.2 COMPFIRST: Build the Image, Then Print It

We now document this design decision, and I propose the following piece of text:

```text
COMPFIRST
begin
    draw: {build; print};
    var image;
    instr build(image), print(image)
end
```

The above piece of documentation, which is considered as an integral part of the final program, should be interpreted as follows.

It refers to a machine called “COMPFIRST” (we use capitals for machine names and try to express the type of decision reflected in the program made for them).

The next line gives a named algorithm: its name is “draw” (this being assumed to be the name of the total program to be made, that has to “draw” a curve), the algorithm expresses the desired time-succession of two actions, building the image in store, followed by printing paper under control of the stored value.

In the last two lines we give the declarations (or declaration headings), naming the components of the machine for which the above algorithm is intended. The first line describes that the name “image” will be used for the data structure that has to accommodate the page image; the variable “image” is the only component of the state space of this machine. Its instruction code comprises two instructions, named “build” and “print” respectively.

Before proceeding, it should be noted that we have used some abbreviations of which I don’t know yet whether they are very wise or very foolish. They have both to do with the fact that the variable “image” is a unique variable of this type.

If the state space should have contained two images, I would have written

```text
type image;
image var image1, image2
```

Expressing that the state space comprises two variables (called “image1” and “image2” respectively), with the same set of possible values, this set being characterized by their type, called “image”. In a later step the type image would enjoy further detailing and this would apply to both variables.

As the set of variables of this type contains only one element, I have ventured not to distinguish between the set (called “image”) and its only element (also called “image”). When descriptions in COMPFIRST (such as “build(image)”) refer to “image”, they refer to the variable; when later structuring detail is given, it refers to the type image.

The last line contains the code of instructions which are like the procedure heading. In general they contain the type of the parameters, where the call contains the variables as actual parameters. Again this seems foolish if the parameter is uniquely given by its type and for this reason we have mentioned the actual parameter in the declaration, and have omitted the mentioning of “image” in the code describing the algorithm “draw”. Thus we can reserve the explicitly mentioned actual parameters for the case where this combinatorial freedom is actually used.

Before proceeding, I would like to stress that our little algorithm named “draw” can and should be regarded as a program written for a machine. We should write the manual for this machine; in it we have to state

1. that the operation “build” assigns a value to the variable “image” specifying the image to be printed on paper as given by the functions fx and fy.
2. that the operation “print” prints the picture on paper as specified by the current value of the variable “image”.

The fact that it can really be regarded as an algorithm for a machine is perhaps most easily seen when we consider alternative algorithms for “draw” e.g.

```text
draw: {print; build}
```

is wrong, because now the action “print” is undefined;

```text
draw: {build; build; print}
```

is correct but unnecessarily time-consuming, because the second action “build” assigns to “image” the value it already has;

```text
draw: {build; print; print}
```

would make sense: it would print the picture twice.

We now resume our programming task. If we had machine “COMPFIRST” at our disposal, the little program named “draw” to be executed by it would do the job. For the sake of argument and in order to be realistic we now assume that we do not have at our disposal such a machine tailored to our needs, and therefore our next task (similar to the previous one!) is to make such a machine.

There are three named entities assumed, viz. “build”, “print” and “image”, where the first two refer to the latter one. As a consequence, a further detailing of the latter one will affect the two first ones; also, it is very hard to give any further detailing of the action “print” without any further commitments as to the structure of “image”. The action “build”, however, admits a further detailing all by itself. And it is for that reason that we take “build” as our first candidate for further refinement.

## 12.3 CLEARFIRST: Clear First, Then Set the Marks

We have to describe, how the variable “image” will get its value corresponding to the proper positioning of the thousand marks. As a total operation, it assigns a value to a variable, whose earlier value was undefined: anticipating that the marks will be added “one at a time”, we see, that addition of a next mark will turn out to be an action operating on an already defined value of the variable “image”. It therefore seems attractive to view the whole setting of the marks as operating on an already defined value, viz. the one corresponding to the blank page.

This decision leads to

```text
CLEARFIRST
begin
    build: {clear; setmarks};
    instr clear(image), setmarks(image)
end
```

where the action “clear” assigns to image the value corresponding to a picture of fifty blank lines, where the action “setmarks” adjusts the initial value of image to the one in which the thousand (or less) marks of the curve have been added.

Again, CLEARFIRST is a machine for which alternative programs could have been written, e.g.

```text
build: {clear}
```

would make sense, but would produce fifty blank lines as output;

```text
build: {setmarks; clear}
```

would contain an undefined operation;

```text
build: {clear; clear; setmarks}
```

would contain a superfluous operation, just as

```text
build: {clear; setmarks; setmarks}
```

would, because the second action “setmarks” would only add marks to the picture that would already be there and therefore would not change the value of “image”.

(Note on notation used. The algorithm explaining “build” in terms of “clear” and “setmarks” does so without explicitly mentioning “image”, because we do not wish to use the actual parameter notation in algorithms unless its actual combinatorial freedom is in fact used in this machine.  Furthermore, “build” being a one-parameter operation no separate identifier for its formal parameter has been introduced. Also this abbreviation on my part could turn out to be very unwise.)

## 12.4 ISCANNER and COMPPOS: Scanning Marks and Computing Coordinates

The next step in the design of the computation – because it can be made without any further commitments – is to describe how the thousand marks of the curve will be dealt with in turn. For the time being I propose the following write-up:

```text
ISCANNER
begin integer i;
    setmarks: {i ≔ 0;
        while i < 1000 do {add mark; i plus 1}};
    instr add mark(i, image)
end
```

This algorithm is to be understood in a machine whose instruction repertoire comprises “add mark(i, image)” which will change the value of “image” in accordance with the addition of the i-th mark. It describes the order in which the marks are dealt with; it shows that all marks will be dealt with exactly once.

But this is not all: a new variable (viz. “i”) has been introduced, the algorithm appeals to a set of actions refering *(sic)* to this variable (“i ≔ 0”, “i < 1000” and “i plus 1”) and if I were completely consistent, it seems that I should list them at the bottom, as possibly requiring further clarification at a later stage, just as “add mark”. I have not done so (I have treated them along the same lines as the while-do clause). From the point of view of language semantics this separate treatment of an implicitly understood type integer does not seem attractive, and it seems hard to justify, why the type integer is treated differently from the type “image”: both are implicitly understood in this machine.

Yet I have done it. All the time I design programs for non-existing machines and add: “if we now had a machine comprising the primitives here assumed, then the job is done”. This is, logically speaking, correct; in practice it is a joke, because we know very well that we cannot assume a general purpose machine to be available whose instruction code is so very well tailored to our needs.

We should not close our eyes – nor feign to do so! – to our responsibility to provide such primitives in a later stage of the design. When I now appeal to a well-understood type “integer” and the operations defined on variables of such a type in this exceptional manner, I do so with the intention of expressing that – although these facilities have to be provided in some form or another – providing these facilities falls outside the scope of the programmer’s responsibility and also that the programmer will accept any reasonable implementation of them.

Again we are left with a primitive that admits further refinement without commitments regarding the other primitives. We have to describe how dealing with mark no.i can be expressed in terms of dealing with a position on the page: we create the machine dealing with the computation of this position.

```text
COMPPOS
begin integer x, y;
    add mark: {x ≔ fx(i); y ≔ fy(i); mark pos};
    instr mark pos(x, y, image)
end
```

where “mark pos” will change the current value of the variable “image” in accordance with the addition of a mark with the co-ordinates “x” and “y” on the picture to be printed.

(Note. In the last refinement it is explicitly assumed that the functions fx(i) and fy(i) can be evaluated in any order of their argument values. If these two thousand function values were to be read from an input stream, pair wise in a prescribed order of i-values, then the last two machines would have to be merged into a single one.)

## 12.5 Why the Representation Decision Can Be Postponed

By now I see no possibility of further refinement without committing myself to the structure of the still rather vague type “image”. How do we propose that this value will be stored? We have to structure the variables of type “image”, or, what amounts to exactly the same thing, we have to choose a representation for its possible values.

While lecturing at various places I have described versions of this program to different audiences, and it may be worth-while to point out that at least twice part of my audience was deeply troubled by the time I had reached this stage. They felt for instance, that I could not claim that my program, as far as developed, was correct; they objected to my remark that `draw: {build; print; print}` would produce the same picture twice, for how did I know, that “print” did not (by means of some side-effect) change the value of “image” before I had made the primitive “print”?

The answer to this, of course, is that “print” has to do what has been stated and should not do what has not been stated. But then more objections came: I had failed to show that the representation was unique, perhaps it was such, that “print” was only a partial function, undefined for some possible values of “image”, etc.

The answer to this seems to be the following: legitimate as such concerns are, they should be dealt with at the right moment, i.e. not before we are committing ourselves to a representation. It is apparently the strength of our approach that so much of the program could be written down independently of the representation to be chosen for the values of the type “image”. What we have done so far seems indeed a judicious exploitation of our power of abstraction (here abstraction of the particular representation to be chosen for the data structure “image”).

But even if we now come to the conclusion that the time has come to decide upon the data structure for the type “image” we still don’t need to commit ourselves completely. Faced with the question how to structure our variable now, we can take our decisions step-wise, just as we have done with the algorithmic refinements encountered so far.

## 12.6 LINER: Representing the Image as an Array of Lines

We recall that the origin of the problem was to be found in the circumstance that the printing primitives “PRSYM” and “NLCR” forced the computation to produce the picture line after line going from top to bottom. Let us try to give recognition to that fact by regarding the image as composed of an array of lines. I then come to the following next level.

```text
LINER
begin integer j;
    image: {array line[0:49]};
    print: {j ≔ 49;
        while j ≥ 0 do {lineprint(line[j]); j minus 1}};
    clear: {j ≔ 49;
        while j ≥ 0 do {lineclear(line[j]); j minus 1}};
    mark pos: {linemark(line[y])};
    type line;
    instr lineprint(line), lineclear(line), linemark(x, line)
end
```

> **Translator’s note**: The source uses an opening parenthesis for the loop body in clear; it is corrected here to an opening brace matching the closing brace. `linemark(line[y])` follows the author’s experimental convention of omitting the uniquely determined parameter x.

In the last line but one we have introduced a type called “line”; a type, I recall, is regarded as a collection of distinguishable values and a variable of such a type can, at any moment, have one of this collection as its value. The first line of code expresses that the type “image” is composed of an array of 50 elements of type “line”, numbered from 0 through 49, and, being the only type composed from this type, again we abstain from introducing a new identifier (wisely or not).

Then, “print”, “clear”, and “mark pos”, being operations that were understood as operating on an “image” are translated in algorithms expressed in terms of operations on a line. In the code of these algorithms, the (true) actual parameter specifies which line; at the end of the description we give the instruction list, indicating that the actions operate on “a line”; we have given the type, but not the parameter.

This level introduces some new features. To start with (as in explaining “image”) we treat the structural refinement of a data type on a footing very similar to the algorithmic refinements (as applied to “print”, “clear” and “mark pos”). Before this level, our approach could have been regarded as an effort to establish a discipline for “subroutinization” – if the reader will excuse this horrible term! –, now we observe that that characterization of our effort covers only half of what we are trying to do, as we are trying to apply a similar technique to data structures as well.

Secondly, our previous machine explained just one entity (instruction or data type) in contrast to “LINER”, which explains a whole bunch of them. The point is that we try to associate with each level a separate design decision; the decision take here is to understand the image from now onwards in terms if lines, and therefore all operations dealing with an image as such have to be translated in terms of operations dealing with its lines.

The image has been “explained away”, the only unusual type we still have to deal with is the type “line” and that is what we are going to do now. I draw your attention to the fact that in the level to come, we have to deal with lines: that lines are used to compose images from is no longer relevant!

## 12.7 LONGREP: Representing a Line as an Array of Characters

To represent a line we have many different possibilities, e.g. a list of the x-co-ordinates of the positions where a mark should be printed (possibly sorted in order of increasing x-value), a boolean array of 100 elements, each element indicating whether the corresponding position on the line of the picture should be marked, or an integer array of 100 elements, each element having the value “mark” or “space” of the PRSYM-parameter for the corresponding printable position.

The last representation caters for extension when different curves (with different marks) have to be printed in the same picture; therefore we select the last one. This leads to

```text
LONGREP
begin integer k;
    line: {integer array sym[0:99]};
    lineprint: {k ≔ 0;
        while k < 100 do {PRSYM(sym[k]); k plus 1};
        NLCR};
    lineclear: {k ≔ 0;
        while k < 100 do {sym[k] ≔ space; k plus 1}};
    linemark: {sym[x] ≔ mark}
end
```

This however leads to an implementation filling out the line with spaces at the righthand side of the rightmost mark: it is like banging the space bar until the bell rings when we want to effect the transition to a new paragraph while writing a letter!

## 12.8 SHORTREP: Printing Only the Necessary Part

The next version suppresses superfluous PRSYM-commands and even leaves those elements of the variable of type “line” undefined that do not need to be defined. With each line a counter “f” is associated, giving the number of PRSYM-commands to be given for that line. Clearing a line now shrinks into setting “f” to zero!

```text
SHORTREP
begin integer k;
    line: {integer f; integer array sym[0:99]};
    lineprint: {k ≔ 0;
        while k < f do {PRSYM(sym[k]); k plus 1};
        NLCR};
    lineclear: {f ≔ 0};
    linemark: {sym[x] ≔ mark;
        if f ≤ x do {
            k ≔ f;
            while k < x do {sym[k] ≔ space; k plus 1};
            f ≔ x + 1}}
end
```

## 12.9 Note Added Later: Making Correctness Easier to Understand

The above program is essentially the program as I have shown it to at least five different audiences. Now, two months later, while thinking at leisure about correctness proofs, I suddenly realize that the given algorithm for “linemark” betrays my past, for it is a piece of lousy coding, compared with the following alternative:

```text
linemark: {
    while f ≤ x do {sym[f] ≔ space; f plus 1};
    sym[x] ≔ mark}
```

a version which guarantees that whenever “sym[x] ≔ mark” is executed, the relation “x < f” will always be satisfied: it is precisely the function of the first line to see to this. The reader is invited to try to understand both versions of linemark and to compare both reasonings. He will then agree with my judgement that the original version is lousy.

The second version jumped into my mind on account of the following observation. The conditional clause

```text
if B do S
```

is used in programs in two different ways. On the one hand we have the applications, in which the execution of the statement S does not invalidate the truth of B, on the other hand we have the situations in which the execution of the statement S is guaranteed to invalidate the truth of B. In the latter case, it is the function of the conditional statement to ensure that after its execution B will not hold.

It is then, essentially, a shortcut for

```text
while B do S
```

which has the property of invalidating the truth of B (provided that it stops), but the justification of the shortcut requires a separate proof that the repeated statement will be executed at most once. In “A first example of step-wise program composition” we did not bother to introduce this shortcut on level 2b4(4) where we wrote

```text
while “ord too small” do “increase ord by one”
```

here a conditional clause would have done the job!
