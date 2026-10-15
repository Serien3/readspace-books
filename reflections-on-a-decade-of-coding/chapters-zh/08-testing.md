# 测试（Testing）

原文：<https://www.scattered-thoughts.net/writing/testing/>  
发布日期：2021-11-26

*本文是系列文章中的一篇，系列从[《十年编程生涯的反思》](00-reflections-on-a-decade-of-coding.md)开始。*

这一篇会写得很短，因为[这里](https://matklad.github.io/2021/05/31/how-to-test.html)写的东西我几乎全都赞同。请先读那一篇。

---

我从[纵深防御](https://buttondown.email/hillelwayne/archive/defense-in-depth-is-actually-a-good-thing/)、投入产出比和调试效率这三个角度来考虑测试。

调试效率不常被人讨论，这也是我对上面 Aleksey 那篇文章唯一有点不同意见的地方。从 bug 的成因到真正引发测试失败之间发生的事越多，追查这个 bug 就越费时间。所以我倾向于给下面这类代码写单元测试：

- 很可能出错的
- 从集成测试里很难调试的

比如在 [dida](https://github.com/jamii/dida) 里，我为 frontier compaction 和 diff coalescing 之类的东西写了很多单元测试。这些地方集成测试也会覆盖，但当集成测试失败时，要把这个失败一路追回到 dataflow 图深处某个归并排序里的差一（off-by-one）错误，工作量很大。所以直接测试它们，给我省下了大量调试时间。

---

Aleksey 的文章还简短提到了“从 fuzzer 提供的字节生成结构化输入”。深入的讲解可看[《How hypothesis works》](https://hypothesis.works/articles/how-hypothesis-works/)。这在任何语言里从零实现都很容易。

---

能把这些测试标记为“已知失败”是很有用的。它们应该在输出里被如实报告为已知失败，但不应导致整个测试套件失败。

当我发现一个不打算立刻修的 bug 时，我会把它加成一个失败的测试，并附上对应 issue 的链接。如果我后来无意中修好了这个 bug，测试套件就会失败，于是我知道该把这个测试标记为通过、并关掉那个 issue。这能防止过期的 issue 一直挂在那里。

---

测试非确定性代码真的很难。为了避免这件事，我愿意在设计阶段忍受很多痛苦。

对于生成随机数的代码，固定种子往往还不够。例如：

``` language-zig
fn foo() void {
    const a = random_int();
    const b = random_int();
    do_stuff_with(a,b);
}
```

如果我把它改成：

``` language-zig
fn foo() void {
    const b = random_int();
    const a = random_int();
    do_stuff_with(a,b);
}
```

一个使用固定种子的测试现在可能开始失败，尽管这个改动并没有让代码变得更正确或更不正确。

在这个傻乎乎的例子很容易看清发生了什么，但我在真实代码里也遇到过类似问题，而且常常要花很长时间才能弄明白：这个失败其实不是我的改动引起的，而是操作的重排导致了不同的随机选择。

同样的情况也会出现在任何多线程代码、使用超时的代码、任何会暴露竞态条件的 IO 等等之中。

---

要让测试——尤其是 fuzzing——产生多得多的价值，一个办法是就内部不变量写大量的断言。

它们可以代价任意高昂，也可以检验复杂的全局不变量。我喜欢把它们写成一个函数：接收某个对象，返回一个错误列表。然后我插入这样的调用：

```
if (test_mode) assert_empty(self.validate())
```

比如 dida 里[这里](https://github.com/jamii/dida/blob/0f640092ac1506f71e6829778d8d5cc98373d0c9/lib/dida/debug.zig#L307-L467)有一个函数，它扫描 dataflow 的整个状态，查找意外别名的指针。它返回的错误长这样：

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

这把测试失败拉得离 bug 的成因近了很多，调试起来也比另一种情形容易得多——比如某个 dataflow 因为改动了被两处地方共用的 frontier，而产出微妙错误的输出。

---

Aleksey 的文章还提到了 [rho 问题](https://buttondown.email/hillelwayne/archive/cross-branch-testing/)——即那些因为不知道如何规定正确输出而难以测试的代码。

有时候，你可以通过找出两种不同的计算输出的方式、并测试它们总是一致来应对。你可以写两个完全不同的算法，也可以只是想一些办法去微调现有的那个。比如在编译器里，你可以测试：打开和关闭各种优化，对随机程序的输出没有影响。

一个漂亮的例子（我记不起出处了）是测试 [DWARF](https://en.wikipedia.org/wiki/DWARF) 元数据。编译器优化有时会搞乱它们对变量来源（provenance）的追踪，报告出错误的变量位置。要测试 DWARF 元数据是否正确很难，但你可以这样做：拿一个随机程序，插入一个断点，分别用 debug 模式和 release 模式编译它，在调试器里运行两个版本，然后检查在断点处两个版本显示的每个作用域内变量的值是否相同。

这类似于[蜕变测试](https://www.hillelwayne.com/post/metamorphic-testing/)，只不过我们改变的是被测试的代码，而不是输入。

---

fuzzing 的基础设施可能很麻烦。为了尽可能多地发现 bug，值得持续不断地跑 fuzzer 去探索随机输入。但你不希望在 CI 里做这件事，因为失败会是非确定性的。

所以我喜欢另设一台服务器，持续对最新的 master 做 fuzzing 并报告任何失败。我会定期从那台服务器上取出语料库（corpus）并签入仓库，这样在 CI 里我们就只跑那个固定的语料库；如果它失败了，我们就知道这是最新提交造成的回归，而不是一个刚刚才被发现的既有 bug。

---

性能测试很难，因为性能通常不是确定性的。

最低限度，我们希望自动运行基准测试——要么在 CI 里按提交运行，要么如果基准测试耗时很长就每天运行。把结果记录到某个数据库里，画一张展示结果随时间变化的图，并把它放在显眼的地方。这样我们就能看到随时间变化的趋势，找出重大的性能回归发生在哪里。

这并不能防止“千刀万剮”式的失败模式——每次提交都让性能微微变差一点，而每个单独的影响都淹没在噪声里。我见过好几个项目这样应对：找一个时间以外的度量对象（比如 cpu 指令数、缓存未命中），然后下功夫让这些度量变得确定（[例如](https://sqlite.org/cpu.html#performance_measurement)、[又如](https://hackmd.io/sH315lO2RuicY-SEt7ynGA)、[更多评论](https://buttondown.email/nelhage/archive/f6e8eddc-b96c-4e66-a648-006f9ebb6678)）。我还没做过这件事，但看起来值得学会怎么做。
