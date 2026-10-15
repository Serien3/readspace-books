# Writing

原文：<https://www.scattered-thoughts.net/writing/writing/>  
发布日期：2021-11-25

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

I have a file called 'ideas' where I write down potential projects or thoughts that might be worth writing about. Entries grow over time as I add more thoughts. The entry that eventually became [Against SQL](https://www.scattered-thoughts.net/writing/against-sql) existed for over a year. Every time I encountered a new bizaare corner of the SQL I would make a quick note of it.

Eventually one of the ideas will feel ready and I'll try to write it up in full. This can take anywhere from a few hours to a few weeks depending on what the goal of writing it is and how much research is required. [Against SQL](https://www.scattered-thoughts.net/writing/against-sql) took something like 60-80 hours to write because I was trying to make a strong argument about a complicated and contentious subject. [Why isn't differential dataflow more popular](https://www.scattered-thoughts.net/writing/why-isnt-differential-dataflow-more-popular/) took maybe an hour or two because I just wanted to hear about other peoples experiences.

------------------------------------------------------------------------

My first pass at writing something difficult is usually to write an append-only, barely-english stream of ideas. I don't make any effort to have a coherent structure or even make sentences. I'm just trying to get all the ideas I've had about a subject into the forefront of my mind.

When I run out of things to append I'll open a blank file and try to come up with some kind of structure to organise the ideas. Usually I think about the structure as a tree and I try to organize it to have \<=5 branches per node and be \<=3 layers deep (see [chunking](https://en.wikipedia.org/wiki/Chunking_(psychology))). I'll think about why I'm writing this and what core idea I want the reader to remember after they've forgetten all the details.

For explanations or arguments in particular, there is something that I'm looking for in the structure that I find hard to articulate. It's something like "what is the deepest reason that X is true". I approach it with cues like "what would have to change in the requirements for the solution to change" or "what other solutions would work equally well". The closest I've seen to an articulation of this idea is in Terence Tao's career advice ([1](https://terrytao.wordpress.com/career-advice/learn-and-relearn-your-field/), [2](https://terrytao.wordpress.com/career-advice/ask-yourself-dumb-questions-and-answer-them/)). I don't know how to explain it better.

(I've also experimented with not organizing the ideas at all eg [Assorted thoughts on zig](https://www.scattered-thoughts.net/writing/assorted-thoughts-on-zig-and-rust/). I think this only works for reporting experiences, not for explaining an idea or persuading people, but when it works it saves a lot of time.)

The hardest part of this step is deciding what ideas to leave out. For tricky subjects I go back and forth multiple times between generating ideas and pruning/refining them, trying out different angles until I find something that feels coherent and that has a clear purpose.

Having these two separate modes is important. If I try to generate ideas and judge them at the same time I often get stuck and don't write anything. Whereas if I allow myself to write badly then I'll write a lot and eventually some of it will be good.

For [Against SQL](https://www.scattered-thoughts.net/writing/against-sql) the initial pass was a long list of annoyances and difficulties in SQL. That didn't feel like a useful thing to read, so I started thinking about why SQL has these problems, why they are hard to work around and what a future language would have to do differently to avoid them. After many passes that started to come together as three underlying problems plus an argument about why the problems matter.

------------------------------------------------------------------------

Once I have a good structure the next step is adding links, citations, fact-checking etc. I don't like to do that while writing because switching context back and forth slows down both processes. But that does mean that sometimes I'll write a whole section about something that it turns out I misremembered or misunderstood and I have to delete it all.

This step is sometimes very time-consuming. Eg for [Against SQL](https://www.scattered-thoughts.net/writing/against-sql) I had to check each example against multiple databases and against the SQL spec, to make sure that the behavior I was complaining about wasn't just a quirk of one implementation. I also removed some complaints where I felt I didn't have a strong enough argument that the behaviour was harmful rather than just annoying.

I also aim to be as specific as possible. If I write "sql functions are bad" then it's hard to back that up with convincing evidence because "bad" is too vague a claim. But if I say that "sql functions are incapable of compressing repeated patterns that involve different column names" then I can easily demonstrate this with examples, and if I was wrong then people could easily provide counter-examples.

Similarly, I try to illustrate general ideas with very concrete examples. Eg in this post I don't just talk about writing in general but give lots of examples from specific things that I've written. Examples are good for clarifying ideas, but more importantly they keep me honest. Sometimes I'll write in this series that I do X and then when I try to come up with examples I realize that I actually often don't do X and it just sounded like a good idea. So even if I don't end up actually writing the examples down it still helps catch bullshit.

For any given post all of this probably doesn't make much difference because people will generally believe it or not based on whether it agrees with their existing prejudices rather than whether it's true. But I think I personally benefit from repeatedly practicing not being wrong, especially since I still regularly mess up.

------------------------------------------------------------------------

The final step is to leave it for a few days and then read it again, editing for flow and comprehensibility. In this step I'm mostly thinking about mechanical problems like [ambiguous pronouns](https://developers.google.com/tech-writing/one/words#recognize_ambiguous_pronouns) or stylistic problems like repeatedly using the same adjective. I also try to remove any extraneous words and simplify sentence structures.

The best resources I've found for low-level writing skills are [The Sense of Style](https://stevenpinker.com/publications/sense-style-thinking-persons-guide-writing-21st-century) and [Google's Technical Writing course](https://developers.google.com/tech-writing/overview). Both are incredibly boring, but worth suffering through if you write often.

I also look out for:

- Anything that is uncharitable or unkind (eg early drafts on [Internal consistency in streaming systems](https://www.scattered-thoughts.net/writing/internal-consistency-in-streaming-systems/) were very negative). It's easy to get a lot of attention by being snarky or cynical, but that's just cheerleading people who already agree with you. To get anyone to change their mind you have to treat their arguments fairly. Anecdotally, I've also found that things that I write snarkily are more often wrong, perhaps because it's more fun to complain about something than to understand it. The test I've started to use for this is to imagine if I would be comfortable reading the post out loud to someone involved in the project I'm criticising.
- Anything that is likely to derail the conversation that I'm interested in. Eg in [Against SQL](https://www.scattered-thoughts.net/writing/against-sql) I used json as an example of something that would be a library in most languages but had to be added to the spec in sql. But people get really mad about json in databases. I could have used eg SQL:2011 time periods or SQL:2016 row patterns instead and avoided that distraction.

If I'm trying to explain something complicated I'll also run it past ~~victims~~ volunteers to see what if anything is confusing or unclear. It matters a lot who I ask - different people will consistently gives really good or really bad advice. I have a few friends who are good at accurately pinpointing confusing descriptions or missing steps in explanations. I don't know how to find such people though.

------------------------------------------------------------------------

I used to argue with people in the comments on sites like hacker news. This is not an effective use of time or emotional capacity. But I don't like to see the conversation dominated by some misunderstanding, because I know that many people will read the comments first and if the comments are dismissive won't read the source.

For some posts I've responded by added an FAQ at the end covering common rebuttals and misunderstandings ([eg](https://www.scattered-thoughts.net/writing/against-sql#faq)), rather than engaging directly. Sometimes I see people reply to comments by quoting the appropriate FAQ entry, which is gratifying.

Lazy rebuttals in particular are predictable enough that in the first draft of [Speed matters](05-speed-matters.md) I wrote the replies to hacker news comments in advance. But after some time reflecting on how much of my life I want to spend [pig-wrestling](https://quoteinvestigator.com/2017/07/08/pig/) I decided to remove them. There is only so much value to [writing defensively](https://pchiusano.github.io/2014-10-11/defensive-writing.html).

------------------------------------------------------------------------

Lately I've been trying to write faster without sacrificing quality. Some things I'm currently trying:

- I often lose a lot of time to getting distracted by out-of-order writing. I'll be working on one section and then have an idea one or more other sections. I often end up switching back and forth in my head developing each thread but not actually writing them down, which means I forget things and think in circles. So I'm experimenting with whenever I have an idea, immediately writing it down wherever I happen to be in the text. Later I can go back and move it into the correct location.
- Sometimes I get stuck starting a particular tricky section. I've had some success recently with [yoda timers](https://www.lesswrong.com/posts/vpvKEj7shuk8h5Eet/hammertime-day-2-yoda-timers#Day_2__Yoda_Timers) and [coworking](https://guzey.com/co-working/#why-co-work-in-the-first-place), both of which act as a temporary boost to get over that hump.
- Often I'm writing something but expecting that some reader will dislike it or argue with it, and that friction makes it harder to write or pushes me to procrastinate. Being more explicit about switching between generating writing and editing/judging it helps somewhat, but I'm also finding that this happens less often if I ignore low-effort comments and instead focus on writing for the subset of readers that will actually engage seriously. That doesn't mean people who will always agree with me, but people who will disagree thoughtfully with the substance of the argument.
