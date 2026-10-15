# 十年编程生涯的反思（Reflections on a decade of coding）

原文：<https://www.scattered-thoughts.net/writing/reflections-on-a-decade-of-coding/>  
发布日期：2021-09-22

我从事专业编程工作大约已有 12 年。以下是我在过去 2 年里做过的一些事。

- 在一个小团队里（平均大约 3 人，我记得是这样？），我们用不到一年的时间，做出了一个 SQL 查询规划器（query planner），它通过了 [sqlite 逻辑测试套件](https://www.sqlite.org/sqllogictest/doc/trunk/about.wiki)中超过 600 万个测试。
- 我搞清楚了如何[对任意的 SQL 子查询做去关联](https://www.scattered-thoughts.net/writing/materialize-decorrelation)（decorrelate）。（我不是第一个想明白这件事的人，但我是独立做到的。）
- 我演示了多种流行的流式系统（streaming system）中存在的[一类一致性失效](https://www.scattered-thoughts.net/writing/internal-consistency-in-streaming-systems/)（consistency failure），我相信这种失效在当时尚未被广泛理解。
- 我写了[那个文本编辑器](https://github.com/jamii/focus)，我每天用它写代码、写文章。它花掉了我大约 100 个小时的工作量。

写下这些例子，很难不显得像是在自夸，但我要把话说清楚——我并不觉得这些项目放在具体语境里有什么了不起。它们属于一个人在某个专门领域积累了十年经验之后理应做得出来的那类项目。

但它们同时也是这样一些项目：我相当确信，哪怕只是回到 5 年前，我也做不出来。

我如今的能力并非源于什么天赋或是宏大的洞见，而是源于数百个关于习惯、流程和价值观的微小改变。当我拿这些改变，与网上那些讨论“如何把编程做得更好”的文章和讨论相比对时，我发现两者的重合之处少得可怜。那些真正让我变得更高效的改变，要么根本没人谈起，要么与流行的建议正好相反。

我写这类文章时是有些犹豫的，因为它们太容易滑向引战（flamebait），而我真的更愿意写那些以事实为骨、而非以观点为骨的东西。但有很多事情，我希望自己能回到过去，讲给年轻时的自己听；而自那以后，情况也并没有好转多少。面向刚刚开始学编程的人，有大量高质量的写作；但能帮我弄清楚如何从一个新手继续往上走的，却少之又少。

当我开始反思哪些做法对我有效、哪些无效时，我发现有*很多*想写下来的东西，于是我试着把它们大致组织了一下：

- [关于糟糕的建议](01-on-bad-advice.md)
- [需要反学习的东西](02-things-unlearned.md)
- [情绪管理](03-emotional-management.md)
- [设定目标](04-setting-goals.md)
- [速度很重要](05-speed-matters.md)
- [更快地前进](06-moving-faster.md)
- [写代码](07-coding.md)
- [测试](08-testing.md)
- [写作](09-writing.md)

有几处明显的空白，是我拿不出有效经验可讲的：

- 维护大型代码库
- 运维长期存活的系统
- 与他人的协作／在团队中工作
