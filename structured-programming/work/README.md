# 《结构化程序设计》阅读版本与校读说明

英文分章在 `chapters/`，中文分章在 `chapter-zh/`；各目录仅放三个对应的 `.tex`。整书英文单文件与 PDF 在 `full/`，整书中文阅读版单文件与 PDF 在 `full-zh/`。两个整书 `.tex` 已内嵌正文，插图共同使用 `images/`。

中文版本依据 `chapters/` 中的英文 LaTeX 转录稿翻译。三篇分别由一个翻译 agent 按 section 顺序逐节完成，逐节自查；完成后由主 agent 审校。保留原文的论证、例子、章节层级、公式、程序代码、插图及参考文献。术语表、本文及少数首次术语括号中的释义为译者补充。

| 中文文件 | 原文章名 | 作者 | section 数 |
| --- | --- | --- | --- |
| [chapter01.tex](chapter-zh/chapter01.tex) | Notes on Structured Programming（结构化程序设计札记） | E. W. Dijkstra | 17 |
| [chapter02.tex](chapter-zh/chapter02.tex) | Notes on Data Structuring（数据结构化札记） | C. A. R. Hoare | 12 |
| [chapter03.tex](chapter-zh/chapter03.tex) | Hierarchical Program Structures（层次化程序结构） | O.-J. Dahl、C. A. R. Hoare | 7 |

可以直接阅读 `.tex` 正文；中英同名文件便于逐节对照。专业名词的统一译法见 [术语表](术语表.md)。程序关键字、标识符和书目题名保留英文。原著出版于 1972 年，SIMULA、ALGOL 60 等术语按当时的语言机制理解。

三篇共 36 节已全部译完。主审核对了章节层级、全部环境、标签、交叉引用和插图引用，并审读重要论证及译法；第二篇另经独立逐节审读。已修订不准确或有歧义的术语表达，扫描本确认的转录修正见下表。

排版阅读可直接打开 [英文 PDF](full/structured-programming.pdf) 或 [中文 PDF](full-zh/structured-programming-zh.pdf)。插图沿用原图，中文图注已译，图内英文标签保留。英文整书包含封面与序言，中文整书阅读版包含三篇译文及篇末参考文献。

## 编译阅读 PDF

两份整书都使用 XeLaTeX 编译。英文稿也使用 Unicode 数学字体，以正确显示序列连接的弧线符号。在书目录下运行以下命令；中间文件写入 `/tmp`，目录中只保留完整 `.tex` 和编译后的 PDF：

```bash
cd full
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=/tmp/structured-programming-en structured-programming.tex
cp /tmp/structured-programming-en/structured-programming.pdf .
```

中文稿在书目录下运行：

```bash
cd full-zh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=/tmp/structured-programming-zh structured-programming-zh.tex
cp /tmp/structured-programming-zh/structured-programming-zh.pdf .
```

需要具备 `ctex`、`unicode-math` 和原文使用的通用 LaTeX 宏包的 TeX Live 环境，以及 Noto CJK 字体（Ubuntu 可用 `fonts-noto-cjk` 安装）。整书源码以 `% BEGIN SOURCE` 和 `% END SOURCE` 标记各段来源。分章和整书是两份正文副本；以后修改正文时需同步对应段落，再编译 PDF。

## 校读说明

英文转录稿可能存在文字、公式或程序代码错误。以下修正均已直接核对 `original/original.pdf` 的页面影像；仅在中文稿修正，英文稿仍便于追溯。表中的原书页码是页面上印出的页码；扫描 PDF 页码从 1 开始计数。

| 位置 | 英文转录稿 | 中文稿处理 | 核对位置 |
| --- | --- | --- | --- |
| 第一篇第 4 节，`eq:n-execution-prop-a`；英文第 246 行 | 第 n 次执行后的断言误写 `d=d_k` | 依扫描本改为 `d=d_n` | 原书第 8 页；扫描 PDF 第 15 页，式 (7a) |
| 第一篇第 15 节，n=2 的幂和例子；英文第 2160 行 | 将 `s=25` 误录为 `s=2^5` | 恢复为 `s=25` | 原书第 66 页；扫描 PDF 第 73 页 |
| 第一篇第 17 节，性质 (c)；英文第 2426 行 | 在“另外 7 条上升……”处漏掉句尾 | 补回“另外 7 条上升对角线为空” | 原书第 74 页；扫描 PDF 第 81 页 |
| 第二篇第 12 节，子界类型简写 (15)—(18)；英文第 2646—2652 行 | 四条二元运算／赋值简写的右侧多录了 `\ominus` | 去掉这四个额外符号；保留 (14) 的一元运算符 | 原书第 168 页；扫描 PDF 第 175 页 |
| 第三篇第 5 节，phrase 类末尾；英文第 972 行 | 循环开头漏了 `for` | 补回 `for` | 原书第 201 页；扫描 PDF 第 208 页 |
| 第三篇第 6 节，链表操作说明；英文第 1213、1223 行附近 | 两处成员关系误录为 `x e link` | 恢复为 `x ∈ link` | 原书第 207—208 页；扫描 PDF 第 214—215 页 |
| 第三篇第 6 节，TWLIST 程序的末两行；英文第 1181 行附近 | 分段列表错误地重置计数为 14，生成重复的第 15、16 行 | 恢复原书第 24、25 行的连续编号 | 原书第 207 页；扫描 PDF 第 214 页 |

另有以下原稿疑点。已核对扫描本的项目注明原书页码；其余尚未确认。译文保留原式，阅读时应结合推导辨别。

- 第一篇第 4 节，英文第 284 行的 `N=N+1`：归纳步上下文应是 `n=N+1`；原书第 9 页同样印作大写 N。
- 第一篇第 9 节，英文第 1331 行的 `mult[n]=i`：上下文讨论 j 是否为 p[n] 的倍数，疑应为 `mult[n]=j`；原书第 38 页同样印作 i。
- 第一篇第 17 节的 `h, h1, …, h8` 列举有九项，却用于说明八层循环，疑为叙述下标笔误；该项尚未核对扫描本。
- 第二篇第 6 节，英文第 947 行的 `shift-count` 下标 2：原书第 118 页也有此写法，语境是在说明移位位数。
- 第二篇第 7 节，英文第 1089 行的 `primary color(red, yellow)`：按前文定义，集合构造函数应使用幂集类型 `color`；原书第 124 页同样写 primary colour。
- 第二篇第 9 节，compile primary 的 leftbracket 分支又执行 `from source`，而此前已执行 `s from source`，疑会多取一个符号；原书第 148 页同样如此。
- 第二篇第 11 节，suitable 中的 `e from remaining` 按前文定义会移除 e，与后面的 `trial ⊆ remaining` 不变式疑冲突；`sessioncount(trial) < hallsize` 又排除了恰好满场的候选。原书第 160—162 页也有这些写法。
- 第二篇第 12 节，带判别标记的联合中 `x_2` 缺撇号、末项 `k_n(x'_n)` 与 m 个分支不符；数组简写 (9) 混用 r 与 v；原书第 169—170 页也如此。
- 第二篇第 12 节，`min(T(a))=T(a)` 的结果类型与最小成员定义疑冲突，range 的 `a ≤ b` 情形又与递归式冲突；原书第 171—172 页也保留这些写法。
- 第三篇第 2 节，英文第 79 行的矩阵乘法代码使用 `B[k,i]`，与前面的 `B[k,j]` 不同；原书第 177 页也存在此差异。英文第 86 行把局部变量 i、j、k 称作参数，与过程声明中的 m、n、p 不一致。
- 第三篇第 2、3 节的参数传递说明分别使用“按引用”和“按名”；扫描本也如此。译文保留两者的区别，不把不同机制合并。
- 第三篇第 3 节直方图代码的 `Y < X[i+1]` 与递增区间的分箱说明疑不相符；原书第 182 页也使用小于号。
- 第三篇第 6 节，英文第 1049 行在“实际参数部分”后多了孤立数字 1，原书第 203 页也有此排印疑点；中文句中略去该孤立数字。
- 第三篇第 7 节，英文第 1465 行的 Lee 算法在 `wayout =/= none` 时才记录道路，与“尚未访问的城市为 none”的说明疑不相符；第 1505 行对引用变量 rd 使用普通赋值。原书第 215—216 页也保留这些写法。
- 第三篇第 7 节扩充后的 Machine Group.request 直接使用 `time`、`wait`，与前面 `current.time`、`current.wait` 的形式不同。译文按英文稿保留，阅读时须结合 MINISIM 的属性作用域理解。

第二篇的闰年示例采用按 4 整除的简化规则，译文保留其历史示例；该示例没有涵盖完整公历规则中的世纪例外。
