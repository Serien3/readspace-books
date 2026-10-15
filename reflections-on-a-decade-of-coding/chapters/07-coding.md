# Coding

原文：<https://www.scattered-thoughts.net/writing/coding/>  
发布日期：2021-12-20

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

This is going to be much more vague than the other parts of the series because this is the actual work. Good judgement is learned from experience, not from blog posts. So I think the most useful thing I can convey is what kinds of things I think about when coding, rather than what answers I come up with.

I'm also trying to focus on things that were non-obvious to me or that run counter to what I was taught.

------------------------------------------------------------------------

The foremost idea I keep in mind is that the goal of writing a program is to turn inputs into outputs, while making good use of limited human and machine resources.

------------------------------------------------------------------------

The goal is not to make code that is pretty or elegant or that reads like english.

Certainly I want to write code that is readable, but when I'm reading code it's because I want to learn what the code actually does, rather than what it says it does.

That includes understanding what data it reads or writes, and in what order and at what time. So I've ended up with a somewhat brutalist aesthetic, where the data is on full display and the access to it is not hidden behind layers of methods calls and private fields.

I've found this data-centric approach works very well for the kinds of problems I work on, but I've also seen advocates for this kind of approach in many other domains eg:

- [Low-level, performance-bound systems](https://www.youtube.com/watch?v=rX0ItVEVjHc)
- [High-level, long-lived systems](https://youtu.be/2V1FtfBDsLU?t=642)
- [Distributed systems](https://www.youtube.com/watch?v=R2Aa4PivG0g)
- [Incremental compilers](https://vimeo.com/649009599) and [IDE tooling](https://www.youtube.com/watch?v=_muY4HjSqVw)

This approach is in stark opposition to the way programming is typically taught, which is to employ maximum defensive encapsulation at every tiny boundary and hide data behind opaque interfaces wherever possible. When code is written in this style it becomes very difficult to answer questions like "is it safe to call myobj.foo() from inside myobj.bar()" or "at which points in time is the value of quux in sync with the upstream value of baz". It also tends to produce object-at-a-time and copy-heavy apis which get in the way of using the hardware efficiently.

------------------------------------------------------------------------

The foundational design question is always "what do I want the machine to do". Everything else is just a tool for concisely expressing that behavior. So when I'm deciding how to design a schema or how to organize code into modules etc, all that matters is what would be most useful for making the computer do the thing.

If I ever find myself thinking about whether a contractor is 'really' a kind of employee, or whether two functions 'belong' together, that's a trap. There is no point trying to get the code to correctly mirror the structure of reality because that structure doesn't exist. The categories [are in our heads](https://www.lesswrong.com/posts/yA4gF5KrboK2m2Xu7/how-an-algorithm-feels-from-inside), not out in the world, and they're only ever 'correct' to the extent that they are useful.

The questions that matter are questions about the behavior of the machine - like should we withhold taxes from contractor payments like we do for employees, or schedule contractors in for mandatory employee training? Once you have the answer to all those questions then in all the cases where contractors and employees are treated the same you can just write that code once, and in all the other cases you have to write different code. At that point the remaining question of whether a contractor is 'really' a kind of employee is empty and meaningless - there is no empirical test that would answer it, and even if there was the answer wouldn't have any bearing on the design of the program.

------------------------------------------------------------------------

A special case of this trap is trying to organize everything into some hierarchy. The point of any kind of code organization tool is to capture repeated patterns in the desired behavior so that we don't have to write out a bajillion slightly different versions of the same thing. But there isn't any law that says that those patterns must always be tree-shaped. Sometimes useful categories will overlap. Trying to force the structure of the problem to fit into some class hierarchy is just borrowing trouble.

The same goes for organizing code into files and folders. There are always different cross-cutting concerns which suggest different ways to organize the code into a tree. It really isn't worth wasting a lot of time trying to find the 'right' one.

## Logical design

I usually start by thinking in data in terms of atomic facts.

Facts are things that will always remain true. So 'Bob is a contractor' is not a fact but 'Bob signed a contracting agreement with us on 2021-11-10' is.

If you think too hard about this you end up butting up against the impossibility of direct access to objective reality. So don't think too hard - it's enough for something to be 'always true' only as far as this program is concerned ie our code will never have to delete or modify it.

Similarly, 'atomic' means that, as far as this program is concerned, the entire fact is input/computed either all at once or not at all. So 'Bob had a contracting agreement from 2021-11-10 until 2022-11-10' might be atomic if you always use contracts with fixed end dates, but otherwise might need to be split into 'Bob signed contract 1047 on 2021-11-10' and 'Bob ended contract 1047 on 2022-11-10'.

------------------------------------------------------------------------

The sudden appearance of 'contract 1047' above is typical. If you know everything there is to know about some thing, then you can refer to it later by using that entire set of facts (realistically, a hash of that set). But if information trickles in over time then you need to find or create some id to tie the facts together with.

The easiest way to do this is to create a sequential or random id when the thing in question is first mentioned. So someone clicks 'new contract' and we report that the new contract has id 1047. Any future input has to refer to that contract id. Effectively we're pawning off the problem of tieing together the facts about this contract to the outside world, which now has to remember the contract id when interacting with our system in future. We could equally replace the random id with 'the contract created by user X at time T'.

Generating an id only works if the creation of the new contract is a unique event. If there are fallible operations between clicking 'new contract' and assigning the contract id then we might accidentally assign multiple ids when retrying an operation. So we want to assign the id as close as possible to the event that caused it eg if we are clicking the 'new contract' button in a browser then we should assign the id in the browser once and then try (and maybe retry) to submit it to the server.

(Another reason to generate ids at the edge of the system is that it's hard to write tests for a system that generates different ids when run with the same input - much easier to have the ids already in the inputs and then the test outputs can be deterministic).

When dealing with incremental maintenance or caching we also have to consider how stable is the association between ids and cached data with respect to typical changes in the inputs. Eg inside an IDE we wouldn't want to use 'the variable starting at character 172' as an id to cache type information, because any insert or delete in that file would require changing most of the cached data. Instead we might want to use something like 'the first variable named foo in the first function named bar', which will only change if the function name or variable name are edited.

Many data modelling methods ask you to identify the 'objects' or 'entities' in the world, but identity becomes philosophically troublesome when you dig into it. I find it much easier to start with desired behavior and then derive ids from facts that I want to connect or computations that I want to cache.

------------------------------------------------------------------------

Next I think about how to turn inputs into outputs, and what intermediate state would be useful for writing that code. I end up with some graph of data where the inputs are at the top, the outputs are at the bottom and there is various derived data in the middle.

Ideally I also want to have some quantitative understanding of the data too - how many inputs there are, how they're distributed, whether there are any strong correlations in the data etc. But when working on database engines the answer is typically "any many as possible" so I have to settle for looking at existing benchmarks and case studies and trying to come up with both lower bounds and aspirational targets.

------------------------------------------------------------------------

When I explain all of this explicitly it sounds like an incredibly formal and elaborate process, but it's mostly automatic. Unless I'm doing upfront design for some difficult or large problem it rarely amounts to more than a few scribbles and sketches in a notebook, and often I don't have to consciously think about it at all.

## Physical design

So now I have to map this design to an actual machine. The graph of data tells me what I want to compute, but I still need to think about:

- whether to store inputs or just downstream intermediate state
- whether to store intermediate state or recompute it from scratch
- how to arrange data in memory and on disk
- in what order to compute intermediate state / outputs

I don't really have advice on how to do make these decisions. I don't know any books or courses or anything that teach this well. I know many that teach it poorly.

[Data-Oriented Design](https://www.dataorienteddesign.com/dodbook/) is not terrible, but mostly provides tools rather than explaining how/when to use them.

------------------------------------------------------------------------

For learning how to write fast software the best resource I've found is to look at projects that perform dramatically better than existing expectations (eg [redpanda](https://vectorized.io/blog/fast-and-safe/), [sorbet](https://sorbet.org/docs/talks/jvm-ls-2019), [zig](https://vimeo.com/649009599)) and try to understand what they do differently.

------------------------------------------------------------------------

For key-value or ordered data-structures, the [RUM hypothesis](https://dl.acm.org/doi/pdf/10.1145/2882903.2912569) is a really useful organizing principle. Basically, you care about read performance, write performance, and space usage. Those seem to be inherently in tension - data-structures that gain on one axis tend to do it by losing on another.

One way to 'cheat' it is to pick different tradeoffs for different subsets of the data. Eg store hot data in a write-optimized structure and cold data in a read-optimized structure. Or batch operations so that you can do all your writes first and then produce a read-optimized structure for later steps.

------------------------------------------------------------------------

A lot of bugs result from storing different representations of the same state and then having them get out of sync with each other.

The easiest way to avoid this is to have a single source of truth and recalculate downstream state from scratch each time instead of storing it.

If that's not feasible for performance reasons then I try to make it impossible to accidentally access stale state, usually either by:

- forcing all writes to the upstream state go through some api that also deletes or updates the downstream state
- keying the downstream state by timestamp / version number / input hash and then checking on read whether the value is stale

I strongly suspect that there is a lot of potential upside to more systematic approaches like [salsa](https://github.com/salsa-rs/salsa), but I haven't tried such techniques myself in any production software yet.

## Code

Once the structure and flow of data is figured out, writing code isn't that complicated. Write down all the things that have to happen, in the correct order. If some set of values tend to get passed around togther, group them into a struct/object. If there is a lot of repeated structure in the code try to move it into a function. If trying to reduce some particular repeated structure ends up making things more complicated, just live with the repetition instead.

[Semantic compression](https://caseymuratori.com/blog_0015) describes this process pretty well.

------------------------------------------------------------------------

Everything I've written so far involves thinking a lot about the details of the problem I'm trying to solve. So an immediate corollary is not to try to write code for problems I'm not trying to solve, because I don't know any of those details.

This is pretty much the opposite of everything I was taught early on, which was all about making solutions as general as possible. In essence I was taught that the correct approach to solving a problem was to start by replacing that problem with a harder problem for which I have less information. In hindsight, this seems unwise.

------------------------------------------------------------------------

The main thing I think about in terms of code structure is how someone will be able to understand it later. This includes being able to read and understand the code itself, but also runtime observability and debugging.

Things that make reading difficult include indirection, callbacks, macros, exceptions and any language feature that breaks jump-to-definition.

Things that make observability difficult include excessive data encapsulation/hiding and implicit or hard-to-query state like opaque closures.

------------------------------------------------------------------------

I lean towards [writing longer functions](http://number-none.com/blow/john_carmack_on_inlined_code.html). I find it easier to read one long function than jump around a tree of short functions.

I'm more likely to break it up if there is a lot of backwards or deeply nested control flow, since that's just as hard to read as jumping between multiple functions. Ideally I'll fit all the complicated control flow into one 'page' of code and the rest of logic into forwards-only functions.

To make the high-level structure more skimmable I hide temporary variables inside a block where possible.

``` language-zig
// Need to check any pending timestamp that is before the new input frontier
var timestamps_to_check = u.ArrayList(Timestamp).init(self.allocator); // <-- this is used later in the function
{
    var timestamp_iter = timestamps.iterator(); // <-- this is only used inside this block
    while (timestamp_iter.next()) |timestamp_entry| {
        const timestamp = timestamp_entry.key_ptr.*;
        if (input_frontier.frontier.causalOrder(timestamp) == .gt) {
            try timestamps_to_check.append(try u.deepClone(timestamp, self.allocator));
            try frontier_support_changes.append(.{ .timestamp = timestamp, .diff = -1 });
        }
    }
}
```

Most of the blocks get a short comment explaining what they are for, so the reader can quickly skim to understand the overall structure.

When I'm working on something tricky, I write the block comments first and then fill in the code afterwards. It helps me keep track of what I'm doing next.

------------------------------------------------------------------------

Within a single file, you can introduce things in a logical order. If the same code is split across a lot of small files then that context is lost. So I lean towards bigger files.

------------------------------------------------------------------------

I like to organize all the state in a program so that it's reachable from some root pointer.

This makes it easy for the reader to understand all the resources allocated by the program by just following the tree of types.

It also makes it easy to find any piece of state from within a debugger, or to write little debugging helpers that eg check global invariants or print queue lengths.

``` language-zig
pub fn main() void {
    var state = State.init();
    while (getEvents()) |events| {
      handleEvents(&state, events);
      // put debugging stuff in here
    }
}
```

This doesn't mean that every piece of code gets access to all the state - each component calls its subcomponents only with the parts of the state that they need, so we can still test components individually. But temporarily-inserted debugging code can reach everything.

------------------------------------------------------------------------

I try to make the state tree-shaped, as much as possible.

As soon as you allow pointers to point between different components, it becomes harder to:

- reason about what state a function depends on or can change, because it can always find a pointer to the rest of the jungle
- test or reuse components, because they require the destinations of all those pointers to exist, so you have to generate a fake version of the entire state just to run one component
- print, inspect or copy the state, because there might be cycles in the pointer graph

In unmanaged languages, there is the additional complication that anything that is pointed to can't be moved. This limits your options for keeping memory layouts compact and also tends to cause subtle, time-consuming bugs.

See [Handles are the better pointers](https://floooh.github.io/2018/06/17/handles-vs-pointers.html) or [Data-Oriented Design](https://www.dataorienteddesign.com/dodbook/) for ideas on how to avoid pointers between components.

------------------------------------------------------------------------

I also try to make access to state flow down the tree.

What I mean by this is that a function that is looking at some part of the state is allowed to call other functions that look at children of that part, but is not allowed to call functions that look at siblings or the parent of that part.

The reason for this is that it's common to need to temporarily break some invariant or be in some weird intermediate state whilst inside a function. When control flow is cyclic what ends up happening is `foo(A)` calls `bar(B)` which calls `quux(A)`, but `quux` assumes some invariants on `A` that `foo` has temporarily broken.

It's not always reasonable to enforce this. For example in [focus](https://github.com/jamii/focus) every buffer can have multiple editors which can each have multiple cursors. When a character is inserted at one cursor, the positions of all the other cursors in all the other editors need to be updated, and this has to be done before anything else accesses those cursors. There are ways to avoid doing this immediately but they all seemed more error-prone than just allowing the buffer to [reach back across](https://github.com/jamii/focus/blob/4f937d0d82b73f5ecbbdc17ad967a7d46e814a5a/lib/focus/buffer.zig#L360-L362) to the attached editors.

------------------------------------------------------------------------

Usually state comes with some invariants that the code can rely on and is expected to maintain. Explaining these invariants in comments is a start, but lately I also add functions that will check the invariants and report any violations, and then sprinkle debug-build-only calls to these functions at key points throughout the code.

This often shortens debugging time by pinpointing where things first went wrong, rather than where the symptoms first appeared.

------------------------------------------------------------------------

I've come to really hate callbacks.

Not immediate calls, like `list_of_things.map(thing => ...)`. Those are fine because I can tell when reading the code exactly what will happen and when.

But callbacks that will be stored somewhere and maybe run later like `thing.on_event(event => ...)` are evil. Because later when I'm reading the code and I see `thing.on_event` get triggered, what could happen next? Literally anything, depending on whether any callback has been registered at any point in time anywhere in the codebase.

The callback itself has to deal with a similar problem. The callback could be run at any point in time, so it has to be safe to run regardless of what state the rest of the program is in.

(I think it's notable that a lot of frontend patterns converge towards callbacks like `thing.on_event(event => queue.push(event))`. Enqueuing an event and dealing with it later is the only action that is always safe.)

When I'm debugging, I want to understand the state of the system. If the system is full of callbacks then the state of the system is always "a list of opaque closures". Most runtimes won't even show you that list, so you can't even ask whether the program is waiting on some IO or has just run out of things to do.

The same arguments apply to most implementations of async/await, which turn your entire program into a list of opaque closures. Maybe we'll eventually get debuggers and profilers that understand async/await, but until then it's a significant burden.

A special case of this is frameworks whose entry point looks like:

``` language-zig
thing.run(event => logic(event))
```

This style of api has not only all of the problems above, but also hides all of its own state and assumes that it is the only event loop in your program. I always prefer an api that looks like:

``` language-zig
var thing = Thing.init();
while (thing.nextEvent()) |event| {
  myEventHandler(thing, event);
}
```

[This post](https://bitsquid.blogspot.com/2011/02/managing-decoupling-part-2-polling.html) from the bitsquid blog has various ideas for avoiding callbacks.

------------------------------------------------------------------------

There is a common argument that developer productivity matters more than performance. Taken to an extreme, this argument is often used to justify implementing a system poorly and then compensating by distributing it over multiple machines and/or adding a caching layer in front. Given that distributed consistency and cache invalidation are two of the hardest problems in software engineering, this seems counter-productive.

It's typically taken for granted that better performance must require higher complexity. But I've often had the experience that making some component of a system faster allows the system as a whole to be simpler, for example by removing the need for horizontal scaling or downstream caching.

------------------------------------------------------------------------

The typical approach for improving performance starts by just writing the software anyhow and then profiling it and trying to improve hotspots.

But whenever I encounter software that is really fast, the authors didn't get there by adding clever code to some hotspot but by carefully designing the overall architecture to make good use of the hardware. Once the architecture is set it's too late to correct the large-scale mistakes.

The way to get the architecture right is to start by using knowledge about the problem, the input data and the capabilities of the hardware to estimate a rough upper bound on performance, and then measure performance as a fraction of the theoretical maximum.

This doesn't mean that I have to try to reach this theoretical maximum, but I'm at least aware whenever I make a decision that deviates from it.

For example, [simdjson](https://github.com/simdjson/simdjson) can parse json at several GB/s. Is that fast? Who knows.

But [their paper](https://arxiv.org/pdf/1902.08318.pdf) measures each stage of parsing in terms of cpu cycles per byte. Since we know what instructions are available on the cpu and how many cycles each takes, this gives us a rough upper bound and tells us that it's unlikely that we could eke out another order of magnitude improvement on the same hardware without multi-threading or [changing the problem](https://simdjson.org/api/0.6.0/md_doc_ondemand.html).

------------------------------------------------------------------------

It's easier to understand how something works if the information is centralized in one place.

For example, in materialize the code that starts all the components and glues them together is all in [one function](https://github.com/MaterializeInc/materialize/blob/e1528979bc4e9d14aca7da3db804aaa2e5bff370/src/materialized/src/lib.rs#L175-L330). You can read these few 100 lines of code and understand which components can communicate with each other and how.

An example of getting this wrong is in my text editor: the editor component has [several functions](https://github.com/jamii/focus/blob/62abfa893260001514645d40e0da560d040ddd76/lib/focus/editor.zig#L1189-L1207) for scrolling the viewport that are called from many different places eg if the cursor moves, or the window is resized, or the contents of the buffer are changed from elsewhere.

What happens if several different components try to scroll the viewport in a single frame? It depends on the order in which those calls happen, which in turn might depend on the order in which different windows were opened, or might be accidentally changed by reorganizing some unrelated code. This has been a constant source of bugs.

What would have worked much better is to append each request to move the scroll position to some list, and have a single place in the code that looks through the list once per frame and decides which request to prioritize.

------------------------------------------------------------------------

It's really hard to make non-deterministic software correct.

Some sources of non-determinism are intrinsic to the problem (eg network communication) and the best you can do is isolate them to the edge of the system, so that at least you can deterministically replay captured histories. Timeouts in particular are best kept at the edges eg by sending regular tick events to the system, rather than by allowing some internal code to check the current time.

Other sources can often be avoided eg use seeds for random numbers (and use splittable generators so that random code reorg doesn't change the results), use deterministic building blocks for multi-threaded computations ([eg](https://arxiv.org/pdf/1901.01930.pdf)).

It's also useful to keep IO at the edges so that it can be tested or replayed. There are a lot of different ways of doing this and I haven't tried most of them.
