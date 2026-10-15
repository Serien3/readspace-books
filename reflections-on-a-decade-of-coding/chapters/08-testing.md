# Testing

原文：<https://www.scattered-thoughts.net/writing/testing/>  
发布日期：2021-11-26

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

This will be a short entry because I agree with almost everything written [here](https://matklad.github.io/2021/05/31/how-to-test.html). Read that first.

------------------------------------------------------------------------

I think about tests in terms of [defense in depth](https://buttondown.email/hillelwayne/archive/defense-in-depth-is-actually-a-good-thing/), value-for-effort and debugging efficiency.

Debugging efficiency is not something I see discussed often and it's the only place where I disagree slightly with Aleksey's post above. The more that happens between the cause of a bug and the actual test failure, the longer it takes to track down the bug. So I tend to write unit tests for code which is:

- likely to be wrong
- hard to debug from integration tests

Eg in [dida](https://github.com/jamii/dida) I wrote a lot of unit tests for things like frontier compaction and diff coalescing. These areas are also exercised by integration tests, but when an integration test fails it's a lot of work to track that failure back to some off-by-one bug in a merge sort deep inside the dataflow graph. So testing them directly saves me a lot of debugging time.

------------------------------------------------------------------------

Aleksey's post also briefly mentions generating structured input from fuzzer-supplied bytes. For an in-depth explanation see [How hypothesis works](https://hypothesis.works/articles/how-hypothesis-works/). It's easy to implement from scratch in any language.

------------------------------------------------------------------------

It's useful to be able to mark tests as known failures. They should be reported as such in the output, but not cause the test suite to fail.

When I find a bug that I'm not going to fix immediately, I add it as a failing test with a link to the issue. If I later accidentally fix the bug, the test suite will fail and I'll know to mark the test as passing and close the issue. That prevents out-of-date issues hanging around.

------------------------------------------------------------------------

It's really hard to test non-determistic code. I'm willing to eat a lot of pain at design time to avoid doing so.

For code which generates random numbers, it often isn't sufficient to fix the seed. For example:

``` language-zig
fn foo() void {
    const a = random_int();
    const b = random_int();
    do_stuff_with(a,b);
}
```

If I change this to:

``` language-zig
fn foo() void {
    const b = random_int();
    const a = random_int();
    do_stuff_with(a,b);
}
```

A test with a fixed seed might now start failing, even though this change does not make the code more or less correct.

In this silly example it's easy to see what happened, but I've run into similar problems in real code and it often takes me a long time to figure out that the failure wasn't really caused by my changes, but by some reordering of operations resulting in different random choices.

This can also come up with any multithreaded code, code that uses timeouts, any IO that exposes race conditions etc.

------------------------------------------------------------------------

One way to get a lot more value from testing, especially fuzzing, is to write a lot of asserts over internal invariants.

These can be arbitrarily expensive and test complex global invariants. I like to write these as a function which takes some object and returns a list of errors. Then I insert calls like this:

```
if (test_mode) assert_empty(self.validate())
```

Eg [here](https://github.com/jamii/dida/blob/0f640092ac1506f71e6829778d8d5cc98373d0c9/lib/dida/debug.zig#L307-L467) is a function in dida that scans the entire state of the dataflow looking for accidentally aliased pointers. It returns errors that look like this:

```
[
    ValidationError{
        .Aliasing = [
            [
                "node_frontiers",
                "4",
                "frontier",
            ],
            [
                "node_states",
                "7",
                "Join",
                "index_input_frontiers",
                "0",
            ],
        ]
    },
]
thread 9322 panic: Found invalid shard state. See errors above.
/home/jamie/dida/lib/dida/util.zig:22:5: 0x38e831 in lib.dida.util.panic (build)
    @panic(buf.toOwnedSlice());
    ^
/home/jamie/dida/lib/dida/debug.zig:313:16: 0x37654f in lib.dida.debug.validateOrPanic (build)
        u.panic("Found invalid shard state. See errors above.", .{});
               ^
/home/jamie/dida/native-debugger/main.zig:219:31: 0x3404e0 in tryEmitDebugEvent (build)
    dida.debug.validateOrPanic(global_allocator, shard);
                              ^
/home/jamie/dida/native-debugger/main.zig:208:22: 0x2e9258 in emitDebugEvent (build)
    tryEmitDebugEvent(shard, debug_event) catch
                     ^
```

This brings the test failure much closer to the cause of the bug, and is much easier to debug than eg a dataflow that produces subtly wrong output because it mutated a frontier that was used in two different places.

------------------------------------------------------------------------

Aleksey's post also mentioned [rho problems](https://buttondown.email/hillelwayne/archive/cross-branch-testing/) - code which is hard to test because we don't know how to specify the correct output.

Sometimes you can deal with this by finding two different ways to compute the output and testing that they always agree. You could write two completely different algorithms, or you can just find ways to tweak the existing one. Eg in a compiler, you can test that turning various optimizations on and off does not affect the output of random programs.

A neat example of this, which I can't remember the source of, is testing [DWARF](https://en.wikipedia.org/wiki/DWARF) metadata. Compiler optimizations sometimes mess up their provenenance tracking and report the wrong location for variables. It's hard to test that the DWARF metadata is correct but what you can do is take a random program, insert a breakpoint, compile it in debug mode and release mode, run both in a debugger and check that at the breakpoint both versions show the same values for each variable in scope.

This is similar to [metamorphic testing](https://www.hillelwayne.com/post/metamorphic-testing/), but we're changing the code being tested rather than the input.

------------------------------------------------------------------------

Infrastructure for fuzzing can be tricky. To discover as many bugs as possible it's worth running fuzzers continuously to explore random inputs. But you don't want to do this in CI because the failures will be non-deterministic.

So I like to have a separate server which continually fuzzes the latest master and reports any failures. Periodically I take the corpus from that server and check it in to the repo, so that in CI we can just run that fixed corpus and if it fails we know that it's a regression caused by the latest commit rather than an preexisting bug that has only just been discovered.

------------------------------------------------------------------------

Perf tests are hard because performance usually isn't deterministic.

At minimum we want to run benchmarks automatically, either per commit in CI, or daily if the benchmarks take a long time. Record the results in a database somewhere, make a graph that shows results over time, and put it somewhere visible. That way we can see the trend over time and figure out where major regressions happened.

This doesn't prevent the 'death by a thousand cuts' failure mode, where each commit makes perf very slightly worse but the individual effects are lost in the noise. I've seen several projects tackle this by finding something other than time to measure (eg cpu instructions, cache misses) and then working hard to make those measurements deterministic ([eg](https://sqlite.org/cpu.html#performance_measurement), [eg](https://hackmd.io/sH315lO2RuicY-SEt7ynGA), [additional commentary](https://buttondown.email/nelhage/archive/f6e8eddc-b96c-4e66-a648-006f9ebb6678)). I haven't done this yet but it seems worth learning how to do.
