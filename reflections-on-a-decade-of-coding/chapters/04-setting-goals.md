# Setting goals

原文：<https://www.scattered-thoughts.net/writing/setting-goals/>  
发布日期：2021-10-06

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

When I don't know where I want to go, I usually don't get there.

Setting explicit goals for each project is essential for:

- [Measuring progress](04-setting-goals.md#measuring-progress)
- [Prioritizing actions](04-setting-goals.md#prioritizing-actions)
- [Choosing tradeoffs](04-setting-goals.md#choosing-tradeoffs)
- [Avoiding drift](04-setting-goals.md#avoiding-drift)
- [Avoiding arguments](04-setting-goals.md#avoiding-arguments)

When setting goals, I find they work better when they are:

- [Honest](04-setting-goals.md#honest)
- [Constant](04-setting-goals.md#constant)
- [Detailed](04-setting-goals.md#detailed)
- [Falsifiable](04-setting-goals.md#falsifiable)
- [Incremental](04-setting-goals.md#incremental)

## Goals are essential for...

### Measuring progress

To feel like I'm making progress I need to know what I'm making progress towards, and how to measure it.

When I have a clear goal I can see how my effort each day is moving me closer towards that goal. Subgoals provide milestones and a sense of closure - of ratcheting progress.

When I don't have a clear goal I feel like I'm going around in circles. I keep undoing and redoing decisions. I feel demoralized and I struggle to keep investing effort in the project.

**Example**: In [strucjure](https://github.com/jamii/strucjure) I had a vague sense that pattern matching, parsing, validation, ast traversals etc were all vaguely similar and could be unified. But I didn't have a specific problem that I wanted to solve or a specific question that I wanted to answer - no gradient at all to direct progress. So I spent a huge amount of time trying different designs and apis without having any criteria by which to decide between them or to tell me when I was done.

### Prioritizing actions

There's never time to do everything I want to do on any given project. Having clear goals makes it possible to sort my todo list by how much each item moves me towards the goals.

**Example**: For my [text editor](https://github.com/jamii/focus) the sole metric is my own efficiency. So I can estimate for each item on the todo list how much time it would save me each week vs how long it would take to implement, and then sort the todo list by ROI.

Good prioritization means faster progress and less time spent making and unmaking decisions, both of which are good for motivation.

### Choosing tradeoffs

People often talk as if there is typically one correct way to program but in practice most decisions have many valid options, each of which has different tradeoffs. These choices can be paralyzing unless I already have a detailed goal against which to evaluate the tradeoffs.

Often I'll find that none of the options make much impact on my goals, in which case I was agonising about a decision that didn't matter.

**Example**: In many of my early projects I spent a lot of time agonizing about how to organize code into different files. Eventually I noticed that none of the various possible strategies actually made much difference to my ability to maintain the code - and certainly not enough to win back the time spent deliberating. So now I tend to just put everything into one big file. Eventually it gets big enough that I have trouble finding things and then I pick some arbitrary split and don't overthink it.

Other times, I'll realize that I can't make a decision because I don't have enough information to evaluate the impact on my goals. Then I can either try to find the information somewhere, or I can prototype multiple options and test the impact directly.

**Example**: Modern databases tend to either compile queries to native code or use vectorized interpreters. Which should I do for [imp](https://github.com/jamii/imp)? Various other people have investigated the tradeoffs already ([eg](http://www.vldb.org/pvldb/vol11/p2209-kersten.pdf)) and it seems that the answer depends heavily on the workload. So instead of deciding now I need to first write more and bigger imp programs so that I can better characterize the workload.

### Avoiding drift

It's important to write goals down, otherwise they tend to drift over time without anyone noticing.

This is especially damaging when the drift is towards increasing the scope of the project before the existing goals have been met.

**Example**: A friend griped about how there are hardly any editors suitable for editing large files (\>1gb, no newlines). I had a pretty good idea how I could solve this in [focus](https://github.com/jamii/focus) and got excited about the challenge. I spent maybe 50-100 hours on it, about as much time as I put into the rest of the editor combined. I got pretty far - I was able to load and edit 1gb of minified javascript - but I still had plenty of bugs to hunt down and tricky UX issues to resolve (eg in large files searching can no longer run synchronously in the UI thread). My pace slowed down and eventually I stopped working on it all together. Finally I realized that I was demotivated because I was struggling to complete a feature I wasn't actually going to use and that wasn't part of my original plan. I junked the whole branch and immediately started feeling excited about working on the editor again.

I notice drifting especially with replacement goals that are fun and more immediately rewarding than the original goal, or which allow avoiding some unpleasant work. Eg writing a cool library to solve some generalization of my problem, instead of just solving the problem.

Drifting also happens with busywork - things that are easy and satisfying but not really high priority. Eg endlessly reorganizing code to be 'nicer', or pushing for 100% coverage of simple code that doesn't really need to be tested.

It's ok for goals to change in light of new information, but having them written down means that change is a deliberate action rather than a gradual accident.

### Avoiding arguments

When working in a team there are inevitably disagreements about what should be done next, or how something should be done. These can get pretty heated. Connecting things back to original goals helps by clarifying whether we disagree about what we want the goals to be, or about how we predict some action will impact those goals.

Disagreement about predictions are often fairly easy to solve with some research or a quick experiment. If we can't get a firm answer, maybe we can agree to try things one way for a while and then schedule a review for later. Sometimes we disagree about the impact being positive or negative, but realize that neither of us predicts it will be large so it probably isn't worth arguing about either way.

Disagreement about goals can be hard to resolve, but at least if the goals are already written down then we can confine disagreement to some meta discussion and not bog down every other issue. Ideally, everyone is professional enough to agree to pull in the same direction in the meantime. (If they're not, I have no insight to offer other than hoping you have a good manager.)

**Example**: This [rustacean principles](https://smallcultfollowing.com/babysteps/blog/2021/09/08/rustacean-principles/) are an attempt to make explicit the goals and values of the rust project in order to guide discussion about new features.

## Goals work better when they are...

### Honest

Sometimes instead of writing down my actual goals, I accidentally write down the things that I think *should* be my goals. Then I find myself in contortions trying to justify the things I actually want to do using the things I said I want to do.

Sometimes the cause is a kind of peer pressure, where I write down the things that a Good Engineer™ is supposed to care about. Or I find myself trying to justify what I'm doing in terms of what other people value eg trying making a business case for pure research.

**Example**: I've often found myself trying to justify how [imp](https://github.com/jamii/imp) could be suited to some particular problem or other. Doing so feels strained, like the entire framing is wrong. It was a relief to be explicitly acknowledge that as an exploratory project it isn't intended or expected to solve any particular problem, but rather to explore the question "if we could replace SQL with a language that was both [simpler](https://www.scattered-thoughts.net/writing/against-sql/#complexity-drag) and more [expressive](https://www.scattered-thoughts.net/writing/against-sql#inexpressive) and [compressible](https://www.scattered-thoughts.net/writing/against-sql#incompressible), what kind of new uses would become possible?". It's much easier to feel like I'm making progress when I'm measuring it against the goal I actually care about.

### Constant

It takes time to get anywhere interesting. Sometimes goals have to change in light of new information, but if the goals are changing every week then it isn't much different from not having goals at all.

I'm particular at danger of thrashing on difficult projects, where success is far from certain and I experience a lot of doubt. I've been experimenting with setting time horizons like "I'll work towards feature X for 6 weeks regardless of how I feel about it". This confines the paralyzing anxiety to explicit planning sessions so that the rest of the time I'm at least moving in *some* direction.

### Detailed

Making good decisions tends to depend on the fine details of the situation.

This means that the goal needs to contain as much of this detail as possible. Things like:

- the exact scope of the problem being solved
- who will be using the code
- where it will run, and on what kind of hardware
- who will be maintaining/supporting the code and for how long
- constraints on correct output
- consequences of bugs
- amount, distribution, rate of change of input data
- requirements on throughput, latency, memory usage, storage, power usage

**Example**: In [focus](https://github.com/jamii/focus) I wasn't sure what data-structure to use to represent the text ([eg](https://marijnhaverbeke.nl/blog/codemirror-line-tree.html), [eg](https://code.visualstudio.com/blogs/2018/03/23/text-buffer-reimplementation)). So I measured the size of all the files in all the projects I work on (median ~2kb, largest ~2mb) and the distribution of line lengths (~10-1000 chars). I measured how long it takes to scan and to copy various sized chunks of memory on my laptop and estimated how many times I would have to do each per frame. Then I used those numbers to very roughly estimate the performance of each data-structure. It turned out a simple array of characters was plenty fast enough for my usecase. If I hadn't been clear on the specific inputs I was expecting to handle, I might have wasted time on a more complex solution (and later I did get nerd-sniped into doing exactly that).

**Example**: When [experimenting with compiling queries](https://www.scattered-thoughts.net/writing/a-practical-relational-query-compiler-in-500-lines/) the initial goal was 'be simple and reasonably fast'. That's a good starting point, but not specific enough to direct choices. The most complex part of the problem is query optimization, and more specifically choosing join orderings. So I operationalized the original goal as 'perform on par with postgres (with sufficient ram to cache all data) on the [Join Order Benchmark](https://www.vldb.org/pvldb/vol9/p204-leis.pdf) using under 1000 loc'. That lead me to choosing to use a variant of triejoin, whose space of possible orderings is simple enough to expose directly to the user. It also gave me guidance on index data-structures; I know that for a given query I have 120 ms total budget and have to perform 3 joins on large tables. So if with a given data-structure it takes more than 120 ms to iterate over those tables then that data-structure is immediately off the table, and if it takes less than 60ms that data-structure is probably good enough and I can move on.

Sometimes not all of the details are available. Eg if I'm making a programming language, there aren't exactly any hard constraints on performance. But I can still draw an aspirational line in the sand (eg some set of benchmarks or applications for which I want to beat an existing language) and then use that to guide decisions.

I can't make good decisions about cases for which I don't know any of the details. This means that goals can't be something like "be future-proof" unless they also include a range of likely scenarios with similar level of detail.

### Incremental

If I just have one big hard goal and it turns out to be even harder than I thought then I might end up running out of time and having to throw everything away.

So I like to have subgoals that are independently valuable and that range from easy to hard. Hitting the easiest goals builds momentum and ensures that I have something to show for my time.

**Example**: When working on [materialize decorrelation](https://www.scattered-thoughts.net/writing/materialize-decorrelation) I tried to fully decorrelate all SQL subqueries right away. After more than a month I still wasn't finished and couldn't merge any of my code. I also couldn't take a break to work on anything else because my code would get harder and harder to merge the longer I waited. This became pretty stressful. If I had instead started by adding subqueries to the frontend but returning an error if they reached the backend, I could have merged that code right away and then worked through decorrelating each case one by one.

**Example**: For [dida](https://github.com/jamii/dida) I've explicitly separated the goals into steps. At first I just wanted to understand how differential dataflow works. When that went well I decided to try to write a implementation that would be easier to understand, so that others could use it as a stepping stone towards understanding the original. I'm hoping to eventually make it a fast, embeddable implementation that would actually be useful in production, but if I fail at that goal then I at least still have something that is useful for learning.

One way to break up complex goals is to work on vertical slices of the stack - going feature-by-feature instead of layer-by-layer.

**Example**: When working on the [materialize](https://materialize.com/) sql planner we started by with an end-to-end implementation of a very tiny subset of sql. Then we added features one at a time, each one typically taking only a day or two to go from unimplemented to passing tests. If we had instead written it a layer at a time (parser, then planner, then optimizer etc) we wouldn't have been able to use any of the huge existing sql test suites until we completed the whole thing, at which point we might learn that we done something completely wrong.

### Falsifiable

The goal needs to be concrete enough that everyone involved will agree on whether or not it's been met. Otherwise it's likely that people end up working towards different goals while thinking they're all working on the same goal.

**Example**: When working on [reltron](https://kevinlynagh.com/reltron/), Kevin and I thought that we had agreed on our goals. But whenever we dug into a disagreement on how to design some interaction it would become clear that we had very different ideas on who would be using it and what kind of problems they would be trying to solve. If we had started instead with detailed user stories (as Kevin insisted ;) we might have realized that we weren't both trying to build the same thing.

Similarly, if it's not possible to fail at the goal, then the goal doesn't provide any reason to prefer one course of action over another and so it's useless.

**Example**: At [Eve](http://witheve.com/deepdives/whateveis.html) the high-level goal was so vague that we could be working on completely different problems month-to-month without noticing that we weren't moving in any particular direction. [What eve is](http://witheve.com/deepdives/whateveis.html) doesn't really pin it down beyond 'glue code' and 'not systems programming'. The [early writing](http://incidentalcomplexity.com/2014/10/16/retrospective/) was all about end-user programming but the [later demos](http://incidentalcomplexity.com/2017/03/01/ex3-jurassicpark/) required writing css. What I spent a lot of my time working on was improving performance enough to write interactive UIs. With such a vague problem statement it's impossible to notice if I'm working on the wrong thing because pretty much anything I worked on could plausibly fit the goals.

For exploratory problems the goal is generally not to solve some problem but to answer some question. In that case, it needs to be clear what would constitute an answer.

**Example**: A question I worked on a few years ago was [could I avoid the object-relational mismatch by writing simple webapps directly in datalog?](https://www.scattered-thoughts.net/writing/relational-ui/). That makes it pretty clear how to test for success - write some simple webapps and compare the result to standard tools. Similarly, if the answer was "no" then I'd want to have a solid explanation of what the obstacles were rather than just "dunno, didn't work out".
