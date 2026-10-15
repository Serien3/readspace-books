# Reflections on a decade of coding

《十年编程生涯的反思》英文博客系列，来源：[Scattered Thoughts 原始目录](https://www.scattered-thoughts.net/writing/reflections-on-a-decade-of-coding/)。

已收录原始目录中的 **9 篇文章**（从 *On bad advice* 到 *Writing*），并额外保存系列导言。编号遵循作者的目录顺序，**不是发布日期顺序**。`chapters/` 保留英文原文，不作删减或改写；`chapters-zh/` 是同名文件的全文中文逐段译本，两目录文件名一一对应。

## 阅读目录

推荐直接阅读按篇拆分的 Markdown，便于检索、引用行号和 vibe reading。

| 顺序 | Markdown 正文 | 中文全译本 | 原文发布日期 | 原始网页快照 |
| --- | --- | --- | --- | --- |
| 导言 | [Reflections on a decade of coding](chapters/00-reflections-on-a-decade-of-coding.md) | [十年编程生涯的反思](chapters-zh/00-reflections-on-a-decade-of-coding.md) | 2021-09-22 | [HTML](html/00-reflections-on-a-decade-of-coding.html) |
| 01 | [On bad advice](chapters/01-on-bad-advice.md) | [关于糟糕的建议](chapters-zh/01-on-bad-advice.md) | 2021-09-22 | [HTML](html/01-on-bad-advice.html) |
| 02 | [Things unlearned](chapters/02-things-unlearned.md) | [需要反学习的东西](chapters-zh/02-things-unlearned.md) | 2021-09-29 | [HTML](html/02-things-unlearned.html) |
| 03 | [Emotional management](chapters/03-emotional-management.md) | [情绪管理](chapters-zh/03-emotional-management.md) | 2021-11-01 | [HTML](html/03-emotional-management.html) |
| 04 | [Setting goals](chapters/04-setting-goals.md) | [设定目标](chapters-zh/04-setting-goals.md) | 2021-10-06 | [HTML](html/04-setting-goals.html) |
| 05 | [Speed matters](chapters/05-speed-matters.md) | [速度很重要](chapters-zh/05-speed-matters.md) | 2021-10-14 | [HTML](html/05-speed-matters.html) |
| 06 | [Moving faster](chapters/06-moving-faster.md) | [更快地前进](chapters-zh/06-moving-faster.md) | 2021-10-23 | [HTML](html/06-moving-faster.html) |
| 07 | [Coding](chapters/07-coding.md) | [写代码](chapters-zh/07-coding.md) | 2021-12-20 | [HTML](html/07-coding.html) |
| 08 | [Testing](chapters/08-testing.md) | [测试](chapters-zh/08-testing.md) | 2021-11-26 | [HTML](html/08-testing.html) |
| 09 | [Writing](chapters/09-writing.md) | [写作](chapters-zh/09-writing.md) | 2021-11-25 | [HTML](html/09-writing.html) |

## 归档结构

- `chapters/`：从每页 `<article>` 提取的 Markdown 正文，附标题、原文网址和发布日期；不含全站导航及订阅表单。
- `chapters-zh/`：`chapters/` 中全部 10 篇的全文中文逐段译本，文件名一一对应，结构与链接保持原样。
- `html/`：未经改写的原始 HTML 下载文件，保留原站的内嵌样式、相对链接和页面结构。
- `sources.json`：逐页记录原文网址、发布日期、下载时间（UTC）、本地路径及原始 HTML 的 SHA-256 校验值。
- `CLAUDE.md`：Agent 阅读导航；`AGENTS.md` 是指向它的相对符号链接。

Markdown 使用 Pandoc 3.1.3（`--from=html --to=gfm --wrap=none`）转换，保留标题层次、强调、引用、列表、代码和链接。系列内链接改为本地 Markdown 路径，其他相对链接补全为原站绝对网址。已校验转换前后的正文文字、主要结构、代码块及本地章节链接。

这些页面正文没有图片或嵌入媒体，因此没有额外的素材目录。HTML 中的原站相对链接未改写，作为原始快照保存；本地章节互跳请使用 Markdown。正文中的系列外参考资料仅保留链接，未递归下载。

## 后续维护

如需更新，以 `sources.json` 中的 URL 重新下载原始 HTML，更新下载时间及 SHA-256，再从正文重新生成对应 Markdown 并校验内容和本地链接。保留现有编号和文件名，避免破坏阅读引用。英文正文更新后，需同步修订 `chapters-zh/` 中对应的中文译本以保持一致。不要直接修改原始 HTML 快照。

文章版权归原作者所有。
