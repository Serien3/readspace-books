# Things unlearned

原文：<https://www.scattered-thoughts.net/writing/things-unlearned/>  
发布日期：2021-09-29

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

One of my favorite questions to ask people is: what are some things that you used to strongly believe but have now changed your mind about?

Here are some of mine.

## Everyone is doing it wrong

Here are some quotes that I would have agreed with 10 years ago:

> Computing spread out much, much faster than educating unsophisticated people can happen. In the last 25 years or so, we actually got something like a pop culture, similar to what happened when television came on the scene and some of its inventors thought it would be a way of getting Shakespeare to the masses. But they forgot that you have to be more sophisticated and have more perspective to understand Shakespeare. What television was able to do was to capture people as they were. So I think the lack of a real computer science today, and the lack of real software engineering today, is partly due to this pop culture.

> \[...\] the only programmers in a position to see all the differences in power between the various languages are those who understand the most powerful one. You can't trust the opinions of the others, because of the Blub paradox: they're satisfied with whatever language they happen to use, because it dictates the way they think about programs.

> \[...\] clearly revolutionizes software as most know it. It could lead to efficient, reliable applications. But that won't happen. A mainstay of our economy is the employment of programmers. A winnowing by factor 100 is in no one's interest. Not the programmers, the companies, the government. To keep those programmers busy requires clumsy languages and bugs to chase.

> \[...\] the reason we are facing bugs that kill people and lose fortunes, the reason that we are facing a software apocalypse, is that too many programmers think that schedule pressure makes it OK to do a half-assed job.

It's easy to find examples of this idea - that everyone is doing computers completely wrong and that there exist simple solutions (and often that everyone else is just too lazy/stupid/greedy/immoral to adopt them).

X is amazing, so why isn't everyone using it? They must be too lazy to learn new things. Y is such a mess, why didn't they just build something simple and elegant instead. They must just be corporate jobsworths who don't care about quality. Why are all those researchers excited about Z? They just don't understand what the real world is like from up in their ivory tower.

It's not limited to programming, of course:

> Instead of losing faith in the power of government to work miracles, people believed that government could and should be working miracles, but that the specific people in power at the time were too corrupt and stupid to press the "CAUSE MIRACLE" button which they definitely had and which definitely would have worked. And so the outrage, the protests - kick these losers out of power, and replace them with anybody who had the common decency to press the miracle button!

> -- [Book review: the revolt of the public](https://astralcodexten.substack.com/p/book-review-the-revolt-of-the-public)

It's so easy to think that simple solutions exist. But if you look at the history of ideas that actually worked, they tend to only be simple from a distance. The closer you get, the more you notice that the working idea is surrounding by a huge number of almost identical ideas that don't work.

Take bicycles, for example. They seem simple and obvious, but it took [two centuries](https://en.wikipedia.org/wiki/History_of_the_bicycle) to figure out all the details and most people today [can't actually locate the working idea](https://link.springer.com/content/pdf/10.3758/BF03195929.pdf) amongst its neighbours.

Even when old niche ideas make a comeback (eg neural networks) it's not because they were right all along but because someone recognized the limitations and found a new variation on the idea that overcame them (eg deep learning).

I imagine some fans of the penny farthing groused about how everyone else was just too lazy or cowardly to ride them. But widespread adoption of bicycles didn't come from some general upswelling of moral fortitude. It came from someone figuring out a design that was less prone to firing the rider headfirst into the ground whenever they hit a bump.

Finding the idea that actually works amidst the sea of very similar ideas that don't work requires staying curious long enough to encounter the fine-grained detail of reality and humble enough to recognize and learn from each failure.

It's ok to think that things have flaws or could be improved. But it's a trap to believe that it's ever the case that a simple solution exists and everyone else is just too enfeebled of character to push the miracle button. All the miracle buttons that we know about have already been pressed.

I learned this the hard way at [Eve](http://witheve.com/). Starting from my very [earliest writing about it](https://web.archive.org/web/20140111081750/http://scattered-thoughts.net/blog/2013/12/12/no-more-bullshit/) there was a pervading idea that we were going to revolutionize everything all at once. It took me two years to gradually realize that we were just hopping from one superficial idea to another without making any progress on the fundamental problems.

I remember at one early point estimating that it would take me two weeks to put together a reasonable query planner and runtime. The first time I even came close to success on that front was [3 years later](https://www.scattered-thoughts.net/writing/a-practical-relational-query-compiler-in-500-lines/). Similarly for incremental maintenance, which I'm [still figuring out](https://github.com/jamii/dida/blob/main/docs/why.md) 7 years later.

It's not that our ideas were bad. It's just that we assumed so strongly that the problems must be simple that we kept looking for simple solutions instead of making use of the tools that were available, and we kept biting off more than we could chew because we didn't believe that any of the problems would take us long to solve.

Contemporaries like [airtable](https://www.airtable.com/) instead started by solving an appropriately-sized subset of the problem and putting in the years of work to progressively fill in all the tiny details that make their solution actually useful. Now they're in a solid position to keep [chipping](https://www.airtable.com/product/automations) [away](https://www.airtable.com/product/sync) at the rest of the problem.

## Programming should be easy

A similar trap hit often got me on a smaller scale. Whenever I ran up against something that was ugly or difficult, I would start looking for a simpler solution.

For example when I [tried to make a note-taking app for tablets](https://web.archive.org/web/20180611020249/https://github.com/jamii/inkling) many years ago I had to make the gui, but gui tools are always kind of gross so I kept switching to new languages and libraries to try to get away from it. In each successive version I made less and less progress towards actually building the thing and had to cover more and more unknown ground (eg qtjava relies on using reflection to discover slots and at the time was difficult to implement the correct types from clojure). I wasted many hours and never got to take notes on my tablet.

If you have a mountain of shit to move, how much time should you spend looking for a bigger shovel? There's no obviously correct answer - it must depend on the size of the mountain, the availability of large shovels, how quickly you have to move it etc. But the answer absolutely cannot be 100% of your time. At some point you have to shovel some shit.

I definitely feel I've gotten better at this. When I wanted to [write a text editor](https://github.com/jamii/focus) last year I spent a few days learning the absolute basics of graphics programming and text rendering, used mostly mainstream tools like sdl and freetype, and then just sat down and shoveled through a long todo list. In the end it only took 100 hours or so, much less time than I spent thrashing on that note-taking app a decade ago. And now I get to use my text editor all the time.

Sometimes the mountain isn't actually as big as it looks. And the nice thing about shoveling shit is that you get a lot faster with practice.

## The new thing is better

As a corollary to searching for the easy way, I've always been prone to spending far too much time on new or niche ideas. It's usually programming languages that get me, but I see other people do the same with frameworks, methodologies or architectures too. If you're really attracted to novelty you can spend all your time jumping between new things and never actually engage with the mainstream.

Mainstream ideas are mainstream for a reason. They are, almost by definition, the set of ideas which are well understood and well tested. We know where their strengths are and we've worked out how to ameliorate their weaknesses. The mainstream is the place where we've already figured out all the annoying details that are required to actually get stuff done. It's a pretty good place to hang out.

Of course there is value in exploring new ideas, but to be able to sift through the bad ideas and nurture the good ones you have to already thoroughly understand the existing solutions.

For example, at Eve I didn't read any of the vast literature on standard approaches to SQL query planning. I only looked at niche ideas that promised to be simpler or better, despite being completely untested (eg [tetris-join](https://dl.acm.org/doi/pdf/10.1145/2967101)). But even after implementing some hot new idea I couldn't tell if it was good or bad because I had no baseline to compare it to. Whereas a group that deeply understands the existing tools can take a new idea like [triejoin](https://arxiv.org/abs/1210.0481) and [compare it to the state of the art](http://www.vldb.org/pvldb/vol13/p1891-freitag.pdf), understand its strengths and weaknesses and use it appropriately.

I also remember long ago dismissing people who complained that some hot new niche language was missing a debugger. At the time I did that because I didn't see the need for a debugger when you could just reason about code algebraically. But in hindsight, it was also because I had never used a debugger in anger, had never watched anyone using a debugger skillfully, and had never worked on a project whose runtime behavior was complicated enough that a debugger would be a significant aid. And all of that was because I'd spent all my time in niche languages and instead of becoming fluent in some ecosystem with mature tooling like java or c#.

The frontier is the place to go mining for new ideas, but it's 1% gold and 99% mud. If you live your whole life there you'll never know what indoor plumbing is like and you'll find yourself saying things like "real programmers don't need toilet paper".

## Learning X will make you a better programmer

For the most popular values of X, I haven't found this to be true.

I think these claims are a lot like how people used to say that [learning latin makes you smarter](https://www.inc.com/jeff-haden/why-we-should-all-learn-to-speak-latin.html). Sure, learning things is fun. And various bits of knowledge are often useful within their own domain. But overwhelmingly, the thing that made me better at programming was doing lots of programming, and especially working on problems that pushed the limits of my abilities.

### Languages

The first language I learned was haskell and for several years I was devoted to proclaiming its innate superiority. Later on I wrote real production code in ocaml, erlang, clojure, julia and rust. I don't believe any of this improved my programming ability.

Despite spending many years writing haskell, when I write code today I don't use the ideas that are idiomatic in haskell. I write very imperative code, I use lots of mutable state, I avoid advanced type system features. These days I even try to avoid callbacks and recursion where possible (the latter after a nasty crash at materialize). If there was an alternate universe where I had only ever learned c and javascript and had never heard of any more exotic languages, I probably still would have converged to the same style.

That's not to say that languages don't matter. Languages are tools and tools can be better or worse, and there has certainly been substantial progress in language design over the history of computing. But I didn't find that any of the languages I learned had a special juice that rubbed off on my brain and made me smarter.

If anything, my progress was often hampered by the lack of libraries, unreliable tools and not spending enough time in any one ecosystem to develop real fluency. These got in the way of working on hard problems, and working on hard problems was the main thing that actually led to improvement.

By way of counter-example, check out [this ICFP contest retrospective](https://tonsky.me/blog/icfpc-2021/). Nikita is using clojure, a pretty niche language, but has built up incredible fluency with both the language and the ecosystem so that he can quickly throw out web scrapers and gui editors. Whereas I wouldn't be able to quickly solve those problems in **any** language after flitting around from ecosystem to ecosystem for 12 years.

(See also [A defense of boring languages](https://danluu.com/boring-languages/), [Your language sucks, it doesn't matter](https://matklad.github.io/2020/09/13/your-language-sucks.html))

### Functional programming

(Specifically as it appears in haskell, clojure, elm etc.)

I **do** find it useful to try to organize code so that most functions only look at their explicit inputs, and where reasonable don't mutate those inputs. But I tend to do that with arrays and hashtables, rather than the pointer-heavy immutable structures typically found in functional languages. The latter imposes a low performance ceiling that makes many of the problems I work on much harder to solve.

The main advantage I see in functional programming is that it encourages tree-shaped data, one-way dataflow and focusing on values rather than pointer identity. As opposed to the graph-of-pointers and spaghetti-flow common in OOP languages. But you can just learn to write in that style from well-designed imperative code (eg like [this](https://bitsquid.blogspot.com/2011/01/managing-coupling.html) or [this](https://bitsquid.blogspot.com/2009/12/events.html)). And I find it most useful at a very coarse scale. Within the scope of a single component/subsystem, mutation is typically pretty easy to keep under control and often very useful.

(Eg [here](https://github.com/jamii/imp/blob/2f85cca53b86b4c56392afb5b0596bdf2697b19b/lib/imp/lang/pass/desugar.zig) the top-level `desugar` function is more or less functional. It's internals rely heavily on mutation, but they don't mutate anything outside the `Desugarer` struct.).

### Lambda calculus / category theory / automata / ...

Certain areas of maths and computer science attract a completely inappropriate degree of mystique. But, like languages, bodies of theory are tools that have a specific use.

- Lambda calculus is useful mainly as a simple standard language for explaining new PL ideas. You need to be familiar with it only if you want to read or write PL papers.
- Automata theory and language classes are only really useful if you're trying to expand the state of the art (eg inventing [treesitter](https://github.com/tree-sitter/tree-sitter)). Even though I write parsers all the time, in practice what I need to remember is a) write recursive descent parsers (like [most major language implementations](https://notes.eatonphil.com/parser-generators-vs-handwritten-parsers-survey-2021.html)) b) google "pratt parsing" when dealing with operator precedence.
- Category theory is the only undergrad class I regret, a hundred hours of my life that has yet to help me solve a single problem or grant any fresh insight.

On the other hand, there are much less sexy areas that have been consistently useful throughout my entire career:

- Very basic probability and statistics are crucial for doing performance estimates, analyzing system behavior, designing experiments, making decisions in life in general.
- Having even the most basic [Fisher-Price](https://www.google.com/search?q=fisher-price+kitchen&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjh8e3u26XzAhUYpZ4KHRKOBh0Q_AUoAXoECAEQAw&biw=956&bih=1041&dpr=1) model of how hardware works makes it much easier to write fast software.
- Being fluent in the core language of mathematics (basic logic, sets, functions, proof techniques) makes it easy to pick up domain-specific tools when I need them eg statistical relational learning when working at relational.ai, bidirectional type inference for imp.

And of course my day-to-day work relies heavily on being able to construct proofs, analyze algorithms (with heavy caveats about using [realistic cost models](https://www.cse.wustl.edu/~angelee/archive/cse341/fall14/handouts/recitation03.pdf) and not erasing constant factors), and being fluent in the various standard algorithmic techniques (hashing, sorting, recursion, amortization, memoization etc).

(See [How to solve it](https://www.goodreads.com/book/show/192221.How_to_Solve_It) for proof heuristics, [How to prove it](https://www.goodreads.com/book/show/739735.How_to_Prove_It) for core math literacy, [Statistical rethinking](https://www.goodreads.com/book/show/26619686-statistical-rethinking) for modelling probabilistic problems.)

I've nothing against theory as a tool. If you do data science, learn statistics. If you do computer graphics, learn linear algebra. Etc.

And if you're interested in eg the theory of computation for its own sake, that's great. It's a fascinating subject. It just isn't an effective way to get better at programming, despite people regularly proclaiming otherwise.

------------------------------------------------------------------------

For all of the above, the real kicker is the [opportunity cost](https://www.stlouisfed.org/open-vault/2020/january/real-life-examples-opportunity-cost). The years that I spent messing around with haskell were not nearly as valuable to me as the week I spent learning to use [rr](https://rr-project.org/). Seeking out jobs where I could write erlang meant not seeking out jobs where I could learn how cpus work or how to manage a long-lived database. I don't write erlang any more, but I still use cpus sometimes.

Life is short and you don't get to learn more than a tiny fraction of the knowledge and skills available, so if you want to make really cool stuff then you need to spend most of your time on the highest-leverage options and spend only a little time on the lottery tickets.

I expect people to object that you never know what will turn out to be useful. But you can make smart bets.

If I could go back and do it again, I would spend the majority of my time trying to solve hard/interesting problems, using whatever were the mainstream languages and tools in that domain, and picking up any domain-specific knowledge that actually came up in the course of solving a problem. Focus on developing fluency and deep expertise in some area, rather than chasing the flavor of the day.

## Intelligence trumps expertise

People don't really say this explicitly, but it's conveyed by all the folk tales of the young college dropout prodigies revolutionizing everything they touch. They have some magic juice that makes them good at everything.

If I think that's how the world works, then it's easy to completely fail to learn. Whatever the mainstream is doing is ancient history, whatever they're working on I could do it in a weekend, and there's no point listening to anyone with more than 3 years experience because they're out of touch and lost in the past.

Similarly for programmers who go into other fields expecting to revolutionize everything with the application of software, without needing to spend any time learning about the actual problem or listening to the needs of the people who have been pushing the boulder up the hill for the last half century.

This error dovetails neatly with many of the previous errors above eg no point learning how existing query planners work if I'm smart enough to arrive at a better answer from a standing start, no point learning to use a debugger if I'm smart enough to find the bug in my head.

But a decade of mistakes later I find that I arrived at more or the less the point that I could have started at if I was willing to believe that the accumulated wisdom of tens of thousands of programmers over half a century was worth paying attention to.

And the older I get, the more I notice that the people who actually make progress are the ones who are keenly aware of the bounds of their own knowledge, are intensely curious about the gaps and are willing to learn from others and from the past.

## Explore vs exploit

This is the core tradeoff embodied by many of the mistakes above. When faced with an array of choices, do you keep choosing the option that has a known payoff (exploit) or do you take a chance on something new and maybe discover a bigger payoff (explore).

I've consistently leaned way too hard towards explore, leaving me with a series of low payoff lottery tickets and a much less solid base to execute from.

If I had instead made a conscious decision to spend, say, 2/3rds of my time becoming truly expert in some core set of safe choices and only 1/3rd exploring new things, I believe I would have come out a much more capable programmer and be able to solve more interesting problems. Because I've watched some of my peers do exactly that.
