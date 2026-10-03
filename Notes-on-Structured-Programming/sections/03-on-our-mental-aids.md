# 3. On our mental aids

In the previous section we have stated that the programmer’s duty is to make his product “usefully structured” and we mentioned the program structure in connection with a convincing demonstration of the correctness of the program.

But how do we convince? And how do we convince ourselves? What are the typical patterns of thought enabling ourselves to understand? It is to a broad survey of such questions that the current section is devoted. It is written with my sincerest apologies to the professional psychologist, because it will be amateurishly superficial. Yet I hope (and trust) that it will be sufficient to give us a yardstick by which to measure the usefulness of a proposed structuring.

Among the mental aids available to understand a program (or a proof of its correctness) there are three that I should like to mention explicitly:

1. Enumeration
2. Mathematical induction
3. Abstraction.

## 3.1 Enumeration

I regard as an appeal to enumeration the effort to verify a property of the computations that can be evoked by an enumerated set of statements performed in sequence, including conditional clauses distinguishing between two or more cases. Let me give a simple example of what I call “enumerative reasoning”.

It is asked to establish that the successive execution of the following two statements, operating on the variables “r” and “dd”, leaves relations (1) invariant.

```text
dd ≔ dd / 2;
if dd ≤ r do r ≔ r - dd
```

$$0 \le r < dd. \tag{1}$$

One just “follows” the little piece of program assuming that (1) is satisfied to start with. After the execution of the first statement, which halves the value of dd, but leaves r unchanged, the relations

$$0 \le r < 2 \times dd. \tag{2}$$

Now we distinguish two mutually exclusive cases.

**Case 1: `dd ≤ r`.** Together with (2) this leads to the relations

$$dd \le r < 2 \times dd. \tag{3}$$

In this case the statement following do will be executed, ordering a decrease of r by dd, so that from (3) it follows that eventually `0 ≤ r < dd`, i.e. (1) will be satisfied.

**Case 2: `non dd ≤ r` (i.e. `dd > r`).** In this case the statement following do will be skipped and therefore also r has its final value. In this case “dd > r” together with (2), which is valid after the execution of the first statement leads immediately to `0 ≤ r < dd`, so that also in the second case (1) will be satisfied.

Thus we have completed our proof of the invariance of relations (1), we have also completed our example of enumerative reasoning, conditional clauses included.

## 3.2 Mathematical Induction

I have mentioned mathematical induction explicitly because it is the only pattern of reasoning that I am aware of that eventually enables us to cope with loops (such as can be expressed by repetition clauses) and recursive procedures. I should like to give an example.

Let us consider the sequence of values

$$d_0,d_1,d_2,d_3,\ldots \tag{1}$$

given by

$$d_0=D, \tag{2a}$$

$$d_i=f(d_{i-1}),\quad i>0. \tag{2b}$$

> **Translator’s note**: In (2b), the source transcription has `i > 1`, leaving `d₁` undefined. Following the subsequent argument, this is corrected to `i > 0`.

where D is a given value and f a given (computable) function. It is asked to make the value of the variable “d” equal to the first value d<sub>k</sub>, in the sequence that satisfies a given (computable) condition “prop”. It is given that such a value exists for finite k. A more formal definition of the requirement is to establish the relation

$$d=d_k, \tag{3}$$

where k is given by the (truth of the) expressions

$$\operatorname{prop}(d_k), \tag{4}$$

$$\neg\operatorname{prop}(d_i),\quad 0\le i<k. \tag{5}$$

We now consider the following program part:

```text
d ≔ D;
while non prop(d) do d ≔ f(d)
```

Program (6): the first line represents the initialization and the second one the loop, controlled by the (hopefully self-explanatory) repetition clause while...do. In terms of the conditional clause if...do, used in our previous example, a more formal definition of the semantics of the repetition clause is by stating that

```text
while B do S
```

is semantically equivalent with

```text
if B do
    begin S; while B do S end
```

Expressing that “non B” is the necessary and sufficient condition for the repetition to terminate.

Calling in the construction “while B do S” the statement S “the repeated statement” we shall prove that in program (6): after the n-th execution of the repeated statement will hold (for n ≥ 0)

$$d=d_n, \tag{7a}$$

$$\neg\operatorname{prop}(d_i),\quad 0\le i<n. \tag{7b}$$

The above statement holds for n = 0 (by enumerative reasoning); we have to prove (by enumerative reasoning) that when it holds for n = N (N ≥ 0), it will also hold for n = N + 1.

After the N-th execution of the repeated statement relations (7a) and (7b) are satisfied for n = N. For the N+1st execution to take place, the necessary and sufficient condition is the truth of `non prop(d)`, which, thanks to (7a) for n = N (i.e. d = d<sub>N</sub>) means `non prop(d_N)`, leading to condition (7b) being satisfied for n = N + 1. Furthermore, d = d<sub>N</sub> and (2b) leads to `f(d) = d_{N+1}`, so that the net effect of the N+1st execution of the repeated statement `d ≔ f(d)` established the relation `d = d_{N+1}`, i.e. relation (7a) for n = N + 1 and thus the induction step (7) has been proved.

Now we shall show that the repetition terminates after the k-th execution of the repeated statement. The n-th execution cannot take place for n > k for (on account of 7b) this would imply `non prop(d_k)`, thereby violating (4). When the repetition terminates after the n-th execution of the repeated statement, the necessary and sufficient condition for termination, viz. `non (non prop(d))` becomes, thanks to (7a)

$$\operatorname{prop}(d_n). \tag{8}$$

This excludes termination for n < k, as this would violate (5). As a result the repetition will terminate with n = k, so that (3) follows from (7a), (4) follows from (8) and (5) follows from (7b). Which terminates our proof.

Before turning our attention away from this example illustrating the use of mathematical induction as a pattern of reasoning, I should like to add some remarks, because I have the uneasy feeling that by now some of my readers – in particular experienced and competent programmers – will be terribly irritated, viz. those readers for whom program (6) is so obviously correct that they wonder what all the fuss is about: “Why his pompous restatement of the problem as in (3), (4) and (5), because anyone knows what is meant by the first value in the sequence, satisfying a condition? Certainly he does not expect us, who have work to do, to supply such lengthy proofs, with all the mathematical dressing, whenever we use such a simple loop as that?” Etc.

To tell the honest truth: the pomp and length of the above proof infuriate me as well! But at present I cannot do much better if I really try to prove the correctness of this program. But it sometimes fills me with the same kind of anger as years ago the crazy proofs of the first simple theorems in plane geometry did, proving things of the same degree of “obviousness” as Euclid’s axioms themselves.

Of course I would not dare to suggest (at least at present!) that it is the programmer’s duty to supply such a proof whenever he writes a simple loop in his program. If so, he could never write a program of any size at all! It would be as impractical as reducing each proof in plane geometry explicitly and in extension to Euclid’s axioms. (Cf. Section “On our inability to do much.”)

My moral is threefold.

Firstly, when a programmer considers a construction like (6) as obviously correct, he can do so because he is familiar with the construction. I prefer to regard his behaviour as an unconscious appeal to a theorem he knows, although perhaps he has never bothered to formulate it; and once in his life he has convinced himself of its truth, although he has probably forgotten in which way he did it and although the way was (probably) unfit for print. But we could call our assertions about program (6), say, “The Linear Search Theorem” and knowing such a name it is much easier (and more natural) to appeal to it consciously.

Secondly, to the best of my knowledge, there is no set of theorems of the type illustrated above, whose usefulness has been generally accepted. But we should not be amazed about that, for the absence of such a set of theorems is a direct consequence of the fact that the type of object – i.e. programs – has not settled down. The kind of object the programmer is dealing with, viz, programs, is much less well-established than the kind of object that is dealt with in plane geometry. In the mean time the intuitively competent programmer is probably the one who confines himself, whenever acceptable, to program structures with which he is very familiar, while becoming very alert and careful whenever he constructs something unusual (for him). For an established style of programming, however, it might be a useful activity to look for a body of theorems pertinent to such programs.

Thirdly, the length of the proof we needed in our last example is a warning that should not be ignored. There is of course the possibility that a better mathematician will do a much shorter and more **elegant** job than I have done. Personally I am inclined to conclude from this length that programming is more difficult than is commonly assumed: let us be honestly humble and interpret the length of the proof as an urgent advice to restrict ourselves to simple structures whenever possible and to avoid in all intellectual modesty “clever constructions” like the plague.

## 3.3 Abstraction

At this stage I find it hard to be very explicit about the role of abstraction, partly because it permeates the whole subject. Consider an algorithm and all possible computations it can evoke: starting from the computations the algorithm is what remains when one abstracts from the specific values manipulated this time. The concept of “a variable” represents an abstraction from its current value.

It has been remarked to me (to my great regret I cannot remember by whom and so I am unable to give credit where it seems due) that once a person has understood the way in which variables are used in programming, he has understood the quintessence of programming. We can find a confirmation for this remark when we return to our use of mathematical induction with regard to the repetition: on the one hand it is by abstraction that the concepts are introduced in terms of which the induction step can be formulated; on the other hand it is the repetition that really calls for the concept of “a variable”. (Without repetition one can restrict oneself to “quantities” the value of which has to be defined at most once but never has to be redefined as in the case of a variable.)

There is also an abstraction involved in naming an operation and using it on account of “what it does” while completely disregarding “how it works”. (In the same way one should state that a programming manual describes an abstract machine: the specific piece of hardware delivered by the manufacturer is nothing but a – usually imperfect! – mechanical model of this abstract machine.) There is a strong analogy between using a named operation in a program regardless of “how it works” and using a theorem regardless of how it has been proved. Even if its proof is highly intricate, it may be a very convenient theorem to use!

Here, again, I refer to our inability to do much. Enumerative reasoning is all right as far as it goes, but as we are rather slow-witted it does not go very far. Enumerative reasoning is only an adequate mental tool under the severe boundary condition that we use it only very moderately. We should appreciate abstraction as our main mental technique to reduce the demands made upon enumerative reasoning.

(Here Mike Woodger, National Physical Laboratory, Teddington, England, made the following remark, which I insert in gratitude: “There is a parallel analogy between the unanalyzed terms in which an axiom or theorem is expressed and the unanalyzed operands upon which a named operation is expected to act.”)
