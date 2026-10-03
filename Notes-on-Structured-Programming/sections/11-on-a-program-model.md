# 11. On a program model

Before we have a program we must have composed it; after we have a program – if there was any sense in making it – we shall have it executed. In this section I shall not stress the activities of program composition and of program execution too much and I shall try to view the program as a static object. We want to view it as a highly structured object and our main question is: what kind of structures do we envisage and why? Our hope is that eventually we shall arrive at a program structure that is both nice to compose and nice to execute.

Mentally, of course, I am unable to ignore these processes, but at present I do not want to discuss them; in particular: I do not want to discuss a design methodology (whether to work “from outside inwards” or the other way round), nor do I want to discuss implementation consequences now. Again, in order not to complicate matters too much, I shall restrict myself to sequential programs.

If I judge a program by itself, my central theme, I think, is that I want the program written down as I can understand it, I want it written down as I would like to explain it to someone. But without further qualification these are just motherhood statements, so let me try and see whether I can be more specific.

## 11.1 From Region Comments to Abstract Instructions

Let us consider a very simple computation, in which three distinct actions can be distinguished to take place in succession, say: input of data, manipulation (i.e. the computation proper) and the output of the results. One way of representing the program is as a long string of statements:

```text
begin
    …
    …
    …
    …
    …
    …
end
```

A next form adds some labels for explanatory purposes:

```text
begin
    begin of input:…
              …
    begin of manipulation:…
              …
    begin of output:…
              …
end
```

suggesting to us, when we read the text, what is going to happen next. Still better, we write:

```text
begin
    input:begin …
                … end;
    manipulation:begin …
                … end;
    output:begin …
                … end
end
```

where the labels are considered less as markers of points in the program text than as names of regions – as indicated by the bracket pairs “begin - end” – that follow the label, or as names of the three actions in which the computation has been decomposed.

But if we take this point of view, the three “labels” are still comments, i.e. explanatory noise for the benefit of the interested (human) reader, whereas I would like to consider them as an integral part of the program. I want my program text to reflect somewhere the fact that the computation has been decomposed into a time-succession of the three actions, whatever form these might take upon closer inspection.

A way of doing this is to write somewhere the (textual) succession of the three (abstract) statements

```text
input; manipulation; output
```

on the understanding that the time-succession of these three actions will indeed be controlled from the above textual succession, whereas the further refinements of these three actions will be given “somewhere else”, perhaps separately, but certainly without relative ordering.

Well, if closed subroutines had not been invented more than twenty years ago, this would have been the time to do it! In other words: we are returning to familiar grounds, to such an extent even that many of my readers will feel cheated! I don’t, because one should never be ashamed of sticking to a proven method as long as it is satisfactory. But we should get a clear picture of the benefits we should like to derive from it, if necessary we should adjust it, and finally we should create a discipline for using it. Let me therefore review the subroutine concept, because my appreciation for it has changed in the course of the last year.

## 11.2 Subroutines, Procedures and Local Variables

I was introduced to the concept of the closed subroutine in connection with the EDSAC [1], where the subroutine concept served as the basis for a library of standard routines. Those were the days when the construction of hardware was a great adventure and many of the standard routines were means by which (scarce!) memory and computation time could be traded for circuitry: as the order code did not comprise a divide instruction, they had subroutines for division.

Yet I do not remember having appreciated subroutines as a means for “rebuilding” a given machine into a more suitable one – curiously enough. Nor do I remember from those days subroutines so much as objects to be conceived and constructed by the user to reflect his analysis: they were more the standard routines to be used by the user. Eventually I saw them mainly as a device for the reduction of program length.

But the whole program as such remained conceived as acting in a single homogeneous store, in an unstructured state space, the whole computation remained conceived as a single sequential process performed by a single processor. In the following years, in the many programming courses I gave, I have preached the gospel faithfully and I have often explained how the calling sequence handed over the return address and how the subroutine would then begin by setting “the link” – i.e. the return jump – at its own end.

At present I would rather view the main program as having its own instruction counter that just continues “counting” upon the completion of the subroutine execution and would certainly not regard the “sleeping value” as a parameter handed over to the subroutine.

(Still the old view has found its way into the hardware of many machines. We have seen machines in which a subroutine jump stored the link at “address zero” of the subroutine and ordered instruction fetch to be resumed at “address one”, an arrangement which makes re-entrant code and recursive subroutines somewhat hard to implement. And even in this decade we find machines which store at program interrupt the “program status” of the interrupted program at a location associated with the interrupt rather than with the interrupted program!)

Ten years later, when ALGOL 60 emerged, the scene changed and we did not talk any more about closed subroutines: we called them “procedures” instead. They remained to be appreciated by the programmer as a very handy means for shortening the program text, and more and more programmers started to use them for the purpose of structuring, so that program adaptation to foreseen changes in problem specification could be confined to the replacement of one or more procedure bodies, or to a procedure call with some actual parameters changed. But the main novelty was the concept of the local variables.

This was reflected in two important aspects.

The first one was the concept of “scope”, i.e. the idea that not all variables are homogeneously accessible all through the program: local variables of a procedure are inaccessible from outside the procedure body because outside it they are irrelevant, What local variables a procedure needs to do its private task is its private concern, is no concern of the calling main program and the fact that the main program can (and must!) be conceived independently of these local variables is judiciously reflected. We may have some misgivings about the specific scope rules, as embodied in ALGOL 60, but we should appreciate them as a very significant step in the right direction.

The second aspect of the novelty was given by the fact that procedures could be used recursively, more precisely, that a procedure was allowed to call itself, either directly or indirectly. The virtue of this facility has been the subject of many hot debates; as far as I can see the discussion has died down. The argument against recursive procedures was always an efficiency argument: non-re-entrant code could be executed so much more efficiently.

But with the advent of multiprogramming another need for flexible storage allocation has emerged. And if there are still machines in which non-re-entrant code can be executed much more efficiently, i.e. in which the use of recursive routines is punished by too heavy a penalty, then I would venture the opinion that the structure of such a machine should now be called somewhat old-fashioned.

The recursive procedure, however, forced upon us the recognition of the difference between its (static) text and its (dynamic) activation – its “incarnation” as it has been called. The procedure text is one thing; the set of local variables it operates upon this time is quite another matter.

## 11.3 Limitations of the Procedure Concept

So far, so good, but now some of its shortcomings (and I don’t care, whether you call them linguistic or conceptual).

Local variables are “created” upon procedure entry, and are “annihilated” upon procedure exit. It is precisely this automatic control over the life-time of variables pertaining to a procedure incarnation that allows us to implement the (recursive) procedures by means of a stack (i.e. a last-in-first-out storage arrangement). The fact that local variables pertaining to an incarnation only exist during the incarnation make it impossible for the procedure to transmit information behind the scenes from one incarnation to the next.

To overcome this the concept “own” has been introduced, but this is no solution to the problem: what own variables are really good for becomes very unclear in the case of recursion and, secondly, it is impossible to write a set of procedures sharing a number of own variables. (We can simulate this by declaring them in an outer block, embracing the procedure declarations, but then the scope rules make them too generally accessible: they can then no longer be regarded as “behind the scenes”.)

Our conclusion – by no means new and by no means only mine! – is that the concept “own” as introduced in ALGOL 60 must be regarded as ill-considered, and that we must look for new ways to control and describe life-time, accessibility and identity of local variables.

But I have still another complaint about the procedure concept, and that is that it is still primarily regarded as a means for shortening the program text (although it may be a text of unknown length as in the case of recursion). The semantics of the procedure call are described in terms of the famous “copy rule”: the procedure call is to be understood as a short-hand, because, semantically speaking, we should replace it with a copy of the text of the procedure body (with suitable adjustments of identifiers and substitutions for parameters) whereupon the thus modified text will be executed by the same machine as the one executing the main program.

It remains (a representation for) a single program text to be executed by a single sequential machine. And it is precisely this picture of a single machine that does not satisfy me any longer.

## 11.4 A Layered Hierarchy of Virtual Machines

I want to view the main program as executed by its own, dedicated machine, equipped with the adequate instruction repertoire operating on the adequate variables and sequenced under control of its own instruction counter, in order that my main program would solve my problem if I had such a machine.

I want to view it that way, because it stresses the fact that the correctness of the main program can be discussed and established regardless of the availability of this (probably still virtual) machine: I don’t need to have it, I only need to have its specifications as far as relevant for the proper execution of the main program under consideration.

For me, the conception of this virtual machine is an embodiment of my powers of abstraction, not unlike the way in which I can understand a program written in a so-called higher level language, without knowing how all kinds of operations (such as multiplication and subscription) are implemented and without knowing such irrelevant details as the number system used in the hardware that is eventually responsible for the program execution.

In actual practice, of course, this ideal machine will turn out not to exist, so our next task – structurally similar to the original one – is to program the simulation of the “upper” machine. In programming this simulation we have to decide upon data structures to provide for the state space of the upper machine; furthermore we have to make a bunch of algorithms, each of them providing an implementation of an instruction assumed for the order code of the upper machine. Finally, the “lower” machine may have a set of private variables, introduced for its own benefit and completely outside the realm and scope of the upper machine.

But this bunch of programs is written for a machine that on all probability will not exist, so our next job will be to simulate it in terms of programs for a next-lower machine, etc. until finally we have a program that can be executed by our hardware.

If we succeed in building up our program along the lines just given, we have arranged our program in layers. Each program layer is to be understood all by itself, under the assumption of a suitable machine to execute it, while the function of each layer is to simulate the machine that is assumed to be available on the level immediately above it.

Why this model? What are the benefits we hope to derive from it? Let me try to list them.

1. Our experience as recorded in “A first example of step-wise program composition” strongly suggests that the arrangement of various layers, corresponding to different levels of abstraction, is an attractive vehicle for program composition.
2. It is not vain to hope that many a program modification can now be presented as replacement of one (virtual) machine by a compatible one.
3. We may hope that the model will give us a better grip on the problems that arise when a program has to be modified while it is in action. If a machine at a given level is stopped between two of its instructions, all lower machines are completely passive and can be replaced, while all higher machines must be regarded as engaged in the middle of an instruction: their state must be considered as being in transition. In a sequential machine the state can only be interpreted in between instruction executions and the picture of this hierarchy of machines, each having its own instruction counter – “counting its instructions” – seems more profitable if we wish to decide at any given moment, what interpretations are valid. In the usual programming language in which computational progress is measured in a homogeneous measure – say “the grain” of one statement – I feel somewhat helpless when faced with the question of which interpretations are valid when.
4. We may hope that the model will even assist us in recovery problems – total or partial – when some malfunctioning has been detected. (Recently I have been involved in the design and construction of a multiprogramming system, but one of the most annoying things was our total inability to estimate (mechanically) the scope of the disaster when a memory cell gave a parity alarm. The only safe reaction we could implement was instantaneous machine stop, hardly a solution to be proud of!)
5. The picture of a layered hierarchy of machines provides a counter poison to one of the dangers evoked by ruthless application of the principle “Divide and Rule”, viz. that different components are programmed so independently of each other that duplication of work (or worse) takes place. The fact that a layer contains “a bunch of programs” to be executed by some conceptual machine stresses the fact that the programs of this bunch are invited to share the same primitives. Separation of tasks is a good thing, on the other hand we have to tie the loose ends together again!

Reference for this chapter: “The Preparation of Programs for an Electronic Digital Computer; with Special Reference to the EDSAC and the use of a Library of Subroutines”, M. V. Wilkes, D. J. Wheeler and S. Gill, Addison-Wesley Press, 1951
