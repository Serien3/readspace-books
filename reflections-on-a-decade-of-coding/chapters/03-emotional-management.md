# Emotional management

原文：<https://www.scattered-thoughts.net/writing/emotional-management/>  
发布日期：2021-11-01

*This post is part of a series, starting at [Reflections on a decade of coding](00-reflections-on-a-decade-of-coding.md).*

If you can focus hard on something for at least a few hours per day for several years, you will get good at it. The main obstacle to doing so is being a [poorly-designed meat machine](https://www.mit.edu/people/dpolicar/writing/prose/text/thinkingMeat.html), beset by anxiety, doubt, frustration, depression, arrogance etc. So I've come to believe that managing those emotions is the main component of being good at anything.

In keeping with the theme of the rest of this series, I don't claim to be very good at this or to have any deep or generalizable insight. I'm just sharing things that worked for me and that I wish I had learned much earlier.

------------------------------------------------------------------------

I won't spend a lot of time talking about the foundations - spending time with friends, eating real food, drinking enough water, exercising, spending time outdoors, taking regular breaks etc. These are all crucial but I don't think anyone doesn't know this.

I will say though that for a long time I bought into the idea that some people are just naturally unathletic. I had a lot of compulsory sports at school and hated all of them. But eventually as an adult I discovered that there are a huge variety of physical activities and that there are some that I really enjoy. They're now a huge contribution to my mental health - it's like having a button that I can push whenever I want to completely reset my mood. If I could go back and tell my younger self one thing it would be that exercise doesn't have to feel like a chore or a punishment, something to be overcome with discipline or a source of guilt when I failed. It's much easier in the long run if you can find something that you actively enjoy doing, where the exercise is just a side-effect.

------------------------------------------------------------------------

I often fell into a cycle where I would want to work on something but end up procrastinating. Then because I had wasted so much time and still had all this work to do I'd cancel other plans and keep trying to work instead. Which meant I would end up stressed and poorly rested - and more likely to procrastinate. In this way procrastination would manage to crowd out not just work but everything else in my life.

This is especially hard when working alone and working at home because there is no delineation of work time. If I can work whenever I want I can also feel guilty about not working whenever I want.

The best way I've found to counter this is to set explicit work hours. I'll commit in advance to working during some short period, say 1000-1300. During that time I'm either working or just staring out the window - no displacement activities. If I'm feeling good I'll usually keep working much longer, but if I'm not getting anywhere I'll just call it a day as soon as the time is up. Either way, once I'm finished for the day I put all my work stuff away behind a screen and endeavor not to think about anything work-related for the rest of the day.

It's not a perfect solution, but I've found that having this clear delineation not only protects non-work time but also makes it easier for me to focus intensely during work hours. On days when I'm struggling I think "it's only 3 hours, that's not so hard" and then often after 3 hours I'm feeling much better and find it easy to keep going. There is also a clear start point, which prevents me from spending the whole day thinking that I'll start "in a minute, I'll just read this one more thing".

Even if I go a whole week only managing 3 hours each day, that still keeps the momentum going and preserves the habit of starting each morning.

------------------------------------------------------------------------

Another huge time-suck is online entertainment, especially when it masquerades as work-related or educational. I was spending easily two hours a day on sites like hacker news and twitter. This is apparently below average.

The opportunity cost is huge - 2 hours per work day is 500 hours per year. Maybe I learned something from that aimless browsing, but with the same time I could have read 250 papers **and** watched 125 movies - better value for both education and entertainment!

This seems almost intrinsic - learning requires effort but anything that requires effort doesn't spread fast online. So fast online media optimizes for content that makes you feel like you're learning something but that doesn't actually require any effort.

Not to mention that the culture in any massive unpoliced community always seems to devolve towards the worst of its members rather than the average. The majority of comments I see are cynical, mean, thoughtless, and usually wrong to boot. Thoughtful comments take much longer to write so they get drowned out.

There's an idea that you [internalize the voice](https://www.lesswrong.com/posts/X79Rc5cA5mSWBexnd/shoulder-advisors-101) of anyone that you spend a lot of time with. I don't want the voice of hacker news sitting on my shoulder telling me that they haven't actually looked at what I'm doing but they're pretty sure that I'm doing it wrong and that they could do it in a weekend.

I think it makes sense to treat much of the internet as fundamentally adversarial, exploiting unpatched bugs in the human mind. Don't get got.

I explicitly put time aside for learning, but I now spend that time on high-quality sources like papers or textbooks and on high-effort activities like completing exercises or challenges, rather than browsing aimlessly or spectating on low-effort arguments. I still allow for some serendipity by following rss feeds and watching conference talks and I begrudgingly keep a twitter account because noone knows how to use rss any more, but I timebox all of that to 2 hours at the end of the work week.

Over the last few years I've slowly left all the massive public communities like hacker news and spent that time instead on regular video calls with distant nerd friends and hanging out in small communities that have a strong focus on actually making things.

(See also [Digital Minimalism](https://www.goodreads.com/book/show/40672036-digital-minimalism))

------------------------------------------------------------------------

I think about work practices in terms of positive and negative reinforcement. If my time working is regularly rewarding then I'm training myself to want to work hard. If it's mostly frustrating and unpleasant then I'm training myself to not want to work.

To get lots of positive reinforcement I try to break tasks down into small chunks, each of which does *something* that works. I also try to order tasks to get some kind of reward as soon as possible.

It's also nice to have some kind of scoreboard. Ticking tasks off a list or seeing passing tests or performance numbers go up over time helps make progress tangible. It also provides the sense that progress is a ratchet, rather than being one step forward and two steps backwards.

When I finish a task I also try to spend some time enjoying the results before moving on to a different task.

**Example**: When adding json support to [materialize](https://github.com/MaterializeInc/materialize/) I started by adding end-to-end support for json literals, then casts, then scalar functions, then set-valued functions etc. I could have instead grouped it like this: add backend support, then planner, then type inference, then syntax. But if I did things in that order I wouldn't get to try things out in the repl or see the number of failing tests go down on our CI graph until I finished the entire task. After several weeks of work, I took a few hours to play around making silly json demos and just enjoying the fact that it worked now.

------------------------------------------------------------------------

I decide what to work on each day based on how I'm feeling. Some days I feel ready to tackle really hard problems. Other days I'm totally scatterbrained and if I try anything hard I'll just mess it up and get discouraged. For those days I keep a list of easy bug fixes, maintenance, documentation, tests, tools to try out etc. These also work well as warmup tasks - sometimes after a couple of easy wins I'll feel more excited to tackle something hard.

In the past I've occasionally had hard problems that had some time pressure, real or imagined, and I've tried to push through. "Just one last push and it'll be finished and I'll take some time off." That one last push always ends up being some kind of Xeno's paradox situation where my capacity to make good decisions erodes at the same rate as the amount of remaining work. Whenever I've thought that I could temporarily ignore basic sanity maintenance to get something finished it's always been a total disaster.

------------------------------------------------------------------------

Some people are very good at pushing through long difficult tasks to get to a final payoff. I suspect this ability isn't innate but rather has been built up from many past successes.

With that in mind, I'm careful about what kind of projects I attempt. If I constantly attempt projects that are too hard for me, I'm teaching myself that hard work is pointless and always leads to failure. But if I always pick projects that are too easy then I won't grow.

One way to work around this is to structure projects with a range of goals from easy to hard. That way I'm always getting some successes but I'm still pushing myself. The easier goals also help build momentum and confidence for the harder goals.

**Example**: The goals in the [dida readme](https://github.com/jamii/dida/tree/4e43b0df75938153baee024fd73b8272e581e5ca#design) range from providing a simple didactic implementation of differential dataflow (fairly confident) to being a better choice of backend for tools like [materialize](https://github.com/MaterializeInc/materialize/) or [differential datalog](https://github.com/vmware/differential-datalog) (I have some ideas, but kind of a long shot). If I only manage the first then I'll still feel pretty good about the time spent on it.

I've also gotten a lot of encouragement from writing monthly or quarterly retrospectives ([eg](https://www.scattered-thoughts.net/writing/2021-q3-roundup/)). Day to day it often feels like I'm not really getting anywhere but when I look back over a longer period there is always much more going on then I remembered.

------------------------------------------------------------------------

I used to often get derailed by distractions. I think the process looks like this:

- I'm working
- Something feels effortful or makes me feel anxious or doubtful
- I switch to my email or whatever
- The anxiety is gone and I get some entertainment - double reinforcement!

The first step to fixing this was just blocking every source of distraction while I'm working. I turn my phone off and redirect any sites I regularly visit to a local page that just says "focus". When I first did this I was astonished at how many times my fingers brought me to that page without any conscious involvement.

But I can still distract myself with my own brain, so I also have tried to practice dealing with those feelings directly. I haven't seen any advice in the countless writings on productivity that helped me with this, but a lot of ideas from [The Rock Warriors Way](https://www.goodreads.com/book/show/501200.The_Rock_Warrior_s_Way) / [Espresso Lessons](https://www.goodreads.com/book/show/7292000-espresso-lessons) are weirdly applicable:

> If you find yourself becoming frustrated, take it as a symptom that you are out of alignment with your goals. If you really want an easy success, find an easier climb. If you want a real challenge, you've found it. If the Ego is asking for a trophy to use in its externally oriented game of self-worth, look the Ego dragon in the eye and draw your sword. Then pay attention, give your best, and enjoy the ride.

> The safety, comfort, and security we crave aren't objective states. They are subjective feelings that come through increasing our understanding of our world and our capabilities. In short, we gain comfort and security by expanding our comfort zones, and we expand our comfort zones by venturing into the risk zone. We make ourselves uncomfortable and insecure for a short time in order to learn what we're capable of.

> Make learning the primary motivation so that you want to engage stressful situations.

I suspect that it would also be worth trying to practice working for very short periods (eg starting with just 5 minutes) at maximum intensity with absolutely zero daydreaming or context switches. I think this might raise the level and duration of mental effort that feels comfortable.

------------------------------------------------------------------------

There is always more work that could be done than I could possibly do in a lifetime. So I find it really important not to think of work as a todo list that I'm trying to get through - that's a crushing burden. Instead I just focus on the idea that my time is finite and that I want to spend it well each day.

The same applies to comparing myself to other people. There are always people who are orders of magnitude more skilled or accomplished, but we're all chipping away together at the infinite pile of work. So it's not about whether I'm better or worse than other people, but about contributing as much as I can.

Digital Minimalism has this quote from Gary Rogowski that sums up the idea:

> Leave good evidence of yourself.
