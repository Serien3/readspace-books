# 5. On the validity of proofs versus the validity of implementations

In the previous section I have assumed “perfect arithmetic” and in my experience the validity of such proofs often gets questioned by people who argue that in practice one never has perfect arithmetic at ones disposal: admissible integer values usually have an absolute upper bound, real numbers are only represented to a finite accuracy etc. So what is the validity of such proofs?

The answer to this question seems to be the following. If one proves the correctness of a program assuming an idealized, perfect world, one should not be amazed if something goes wrong when this ideal program gets executed by an “imperfect” implementation. Obviously! Therefore, if we wish to prove program correctness in a more realistic world, the thing to do is to acknowledge right at the start that all operations appealed to in the program (in particular all arithmetic operations) need not be perfect, provided we state – rather axiomatically – the properties they have to satisfy for the proper execution of the program, i.e. the properties on which the correctness proof relies. (In the example of the previous section this requirement is simply exact integer arithmetic in the range [0, 2a].)

> **Translator’s note**: When a = 0 or d > 2a, the author’s stated range does not cover the initial value d. If all integer values occurring in the program must be representable, `[0, max(d, 2a)]` is a sufficient common range. The author’s statement is retained in the text to distinguish it from this editorial correction.

When writing a program operating on real numbers with rounded operations, one must be aware of the assumptions one makes, such as

```text
b > 0 implies a + b ≥ a
a * b = b * a
-(a * b) = (-a) * b
0 * x = 0
0 + x = x
1 * x = x
etc. etc.
```

Very often the validity of such relations is essential to the logic of the program. For the sake of compatibility, the programmer would be wise to be as undemanding as possible, whereas a good implementation should satisfy as many reasonable requirements as possible.

This is the place to confess one of my blunders. In implementing ALGOL 60 we decided that “x = y” would deliver the value true not only in the case of exact equality, but also when the two values differed only in the least significant digit represented, because otherwise it was so very improbable that the value true would ever be computed. We were thinking of converging iterations that could oscillate within rounding accuracy.

While we had been generous (with the best of intentions!) in regarding real numbers as equal, it quickly turned out that the chosen operation was so weak as to be hardly of any use at all. What it boiled down to was that the established truth of a = b and b = c did not allow the programmer to conclude the truth of a = c . The decision was quickly changed.

It is since that experience that I know that the programmer can only use his tool by virtue of (a number of) its properties; conversely, the programmer must be able to state which properties he requires. (Usually programmers don’t do so because, for lack of tradition as to what properties can be taken for granted, this would require more explicitness than is otherwise desirable. The proliferation of machines with lousy floating-point hardware – together with the misapprehension that the automatic computer is primarily the tool of the numerical analyst – has done much harm to the profession!)
