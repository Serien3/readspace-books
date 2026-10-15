# Reflections on a decade of coding

原文：<https://www.scattered-thoughts.net/writing/reflections-on-a-decade-of-coding/>  
发布日期：2021-09-22

I've been programming professionally for about 12 years. Here are some of the things I worked on in the last 2 years.

- In a small team (averaging ~3 people, I think?) in a little under a year, we built a SQL query planner that passed the \>6 million tests in the [sqlite logic test suite](https://www.sqlite.org/sqllogictest/doc/trunk/about.wiki).
- I figured out how to [decorrelate arbitrary SQL subqueries](https://www.scattered-thoughts.net/writing/materialize-decorrelation) (I wasn't the first person to figure this out, but I got there independently).
- I demonstrated [a mode of consistency failure](https://www.scattered-thoughts.net/writing/internal-consistency-in-streaming-systems/) in various popular streaming systems that I believe was not widely understood at the time.
- I wrote [the text editor](https://github.com/jamii/focus) that I use for coding and writing every day. It took on the order of 100 hours of work.

It's hard to write these examples without sounding like I'm bragging, but to be very clear - I don't think that these projects are particularly impressive in context. They are the kind of projects that someone with a decade of experience in a specialized area should be capable of.

But they are also projects that I'm fairly confident I would have failed at even 5 years ago.

My ability now isn't due to any intrinsic talent or grand insight but instead hundreds of tiny changes in habits, processes and values. When I compare these changes to online writing and discussions about how to get better at programming, I see very little overlap. The changes that lead to me being more effective are either not talked about at all or are in direct opposition to popular advice.

I'm hesitant to write these kinds of posts, because they veer awfully close to flamebait and I really prefer to write things that are strongly factual rather than opinion-based. But there are a lot of things that I wish I could go back in time and tell my younger self, and the situation hasn't gotten much better since. There is a lot of high-quality writing aimed at people who are just learning to program, but very little that helped me figure out how to progress from being a novice.

When I started reflecting on what has and hasn't worked for me I found a *lot* of things that I wanted to write down, so I've tried to roughly organize it:

- [On bad advice](01-on-bad-advice.md)
- [Things unlearned](02-things-unlearned.md)
- [Emotional management](03-emotional-management.md)
- [Setting goals](04-setting-goals.md)
- [Speed matters](05-speed-matters.md)
- [Moving faster](06-moving-faster.md)
- [Coding](07-coding.md)
- [Testing](08-testing.md)
- [Writing](09-writing.md)

Notable gaps where I don't have useful experience to offer:

- Maintaining large codebases
- Operating long-lived systems
- Collaboration / working in teams
