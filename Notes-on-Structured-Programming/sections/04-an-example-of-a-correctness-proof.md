# 4. An example of a correctness proof

Let us consider the following program section, where the integer constants a and d satisfy the relations `a ≥ 0` and `d > 0`.

```text
integer r, dd;
r ≔ a; dd ≔ d;
while dd ≤ r do dd ≔ 2 * dd;
while dd ≠ d do
    begin dd ≔ dd / 2;
        if dd ≤ r do r ≔ r - dd
    end
```

To apply the Linear Search Theorem (see Section “On our mental aids”, subsection “On mathematical induction”) we consider the sequence of values given by

$$dd_0=d,\qquad dd_i=2dd_{i-1}\quad(i>0).$$

From this, by normal mathematical techniques, we can derive:

$$dd_n=d\times2^n. \tag{1}$$

These techniques also tell us that (because d > 0) for finite r `dd_k > r` will hold for some finite k, thus ensuring that the first repetition terminates with `dd = d * 2^k`.

Solving the relation `dd_i = 2 * dd_{i-1}` for `dd_{i-1}` gives `dd_{i-1} = dd_i / 2`, and the Linear Search Theorem then tells us, that the second repetition will also terminate. (As a matter of fact the second repeated statement will be executed exactly the same number of times as the first one.)

At the termination of the first repetition, `dd = dd_k`, and therefore,

$$0\le r<dd. \tag{2}$$

As shown earlier (Section “On our mental aids.”, subsection “On enumeration”) the repeated statement of the second clause leaves this relation invariant. After termination (on account of “while dd ≠ d do”) we can conclude `dd = d`, which together with (2) gives

$$0\le r<d. \tag{3}$$

Furthermore we prove that after the initialisation

$$dd\equiv0\pmod d. \tag{4}$$

this follows, for instance, from the fact that the possible values of dd are – see (1) – `d * 2^i` for `0 ≤ i ≤ k`.

Our next step is to verify, that after the initial assignment to r the relation (5) holds:

$$a\equiv r\pmod d. \tag{5}$$

1. It holds after the initial assignments.
2. The repeated statement of the first clause (“dd ≔ 2 * dd”) maintains the invariance of (5) and therefore the whole first repetition maintains the validity of (5).
3. The second repeated statement consists of two statements. The first (“dd ≔ dd/2”) leaves (5) invariant, the second one also leaves (5) invariant for either it leaves r untouched or it decreases r by the current value of dd, an operation which on account of (4) also maintains the validity of (5). Therefore the whole second repeated statement leaves (5) invariant and therefore the whole repetition leaves (5) invariant.

Combining (3) and (5), the final value therefore satisfies:

$$0\le r<d,\qquad a\equiv r\pmod d.$$

i.e. r is the smallest non-negative remainder of the division of a by d.

## 4.1 Remark 1: Computing the Quotient as Well

The following program assigns to q the value of the corresponding quotient:

```text
integer r, dd, q;
r ≔ a; dd ≔ d; q ≔ 0;
while dd ≤ r do dd ≔ 2 * dd;
while dd ≠ d do
    begin dd ≔ dd / 2; q ≔ 2 * q;
        if dd ≤ r do begin r ≔ r - dd; q ≔ q + 1 end
    end
```

The proof can be established by observing the invariance of the relation

$$a=q\times dd+r.$$

(I owe this example to my colleague N.G.de Bruijn.)

## 4.2 Remark 2: The Loop Invariant Theorem

In the subsection “On mathematical induction.” we have proved the Linear Search Theorem. In the previous proof we have used another theorem about repetitions (a theorem that, obviously, can only be proved by mathematical induction, but the proof is so simple that we leave it as an exercise to the reader), viz. that if prior to entry of a repetition a certain relation P holds, whose truth is not destroyed by a single execution of the repeated statement, then relation P will still hold after termination of the repetition.

This is a very useful theorem, often allowing us to bypass an explicit appeal to mathematical induction. We can state the theorem a little bit sharper; in the repetition

```text
while B do S
```

one has to show that S is such that the truth of `P and B` prior to the execution of S implies the truth of `P` after its execution.

## 4.3 Remark 3: An Exercise

As an exercise (for which acknowledgement is due to James King, CMU, Pittsburgh, USA) for the reader:

Prove that with integer A, B, x, y and z, and `A > 0` and `B ≥ 0`, after the execution of the following program section finally `z = A^B` will hold.

```text
x ≔ A; y ≔ B; z ≔ 1;
while y ≠ 0 do
    begin if odd(y) do begin y ≔ y - 1; z ≔ z * x end;
        y ≔ y / 2; x ≔ x * x
    end
```

The proof has to show that (in spite of “y ≔ y / 2”) all variables keep integer values; the method shows the invariance of

$$x>0\quad\text{and}\quad y\ge0\quad\text{and}\quad A^B=z\times x^y.$$

> **Translator’s note**: The source transcription has `y > 0` and an uppercase `Y` in the exponent of `x^y`. Here the condition is corrected to `y ≥ 0` and the exponent is consistently written as y, since the initial condition allows B = 0 and the loop also terminates with y = 0. Strict positivity cannot be an invariant throughout this program.
