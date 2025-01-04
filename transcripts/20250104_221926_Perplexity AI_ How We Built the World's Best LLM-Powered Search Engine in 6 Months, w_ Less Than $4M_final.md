---
video_id: -mQPOrRhRws
video_url: https://www.youtube.com/watch?v=-mQPOrRhRws&t=435s
video_title: Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M
created_at: 2025-01-04 22:22:27
---

# Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M

[00:02 - 00:03] Be great.
[00:03 - 00:06] Yeah thank you for coming around this time.
[00:06 - 00:09] I'm sure people feel sleepy around this time.
[00:09 - 00:13] So hopefully this is somewhat entertaining.
[00:13 - 00:29] So I'm gonna tell you you know how we are trying to think about the future of search, just probably the most you know intuitive and important product that you know every consumer can use and how we are approaching it at perplexity.
[00:29 - 00:49] So think of this kind of linear story where we just saw like good work like this, where you know I'm I'm searching for like good headphones and this is a ton of ads sponsored links, seo content and super tiring.
[00:49 - 00:52] And then we just decided, okay, be nice.
[00:52 - 00:53] What what it be?
[00:53 - 00:59] What if it be really cool if we can just directly just see the answer and compare different things.
[00:59 - 01:06] And so we just decide, okay, let's build the world's best research assistant that can just answer any question.
[01:06 - 01:09] And then we ended up building this and let's handle the story.
[01:09 - 01:12] And thatbe very disappointing, right?
[01:12 - 01:15] Like yoube like, Oh, why did I even come for this talk?
[01:15 - 01:20] But so the answer is obviously, it it, I wish it for this linear.
[01:20 - 01:27] I would think about myself like a genius or something, but, it was hardly this linear.
[01:27 - 01:30] So this is actually what really happened.
[01:30 - 01:40] Like we, we we incorporated one year ago, we started working on Texas sql, which had nothing to do with consumer search.
[01:40 - 01:49] In fact, like if you went to vcs and asked for money to work on search, they they just wouldn't even fund you, right?
[01:49 - 01:58] Like no matter like how ambitious you are, like how like how you, it it's very hard for you to like convince anybody to fund you.
[01:58 - 02:00] So we, we we worked on text sql.
[02:00 - 02:07] We got lucky enough that really good people like ela, gill, nt, Friedman and Jeff all like investor in us.
[02:07 - 02:15] And we were like really just interested in like looking into enterprise search with l of m plus equal ql.
[02:15 - 02:23] And we just couldn't know how to you know, even do all this stuff, company building enterprise, none of these things.
[02:23 - 02:25] Like nothing was interiitive.
[02:25 - 02:28] There was no expert to answer anything we knew.
[02:28 - 02:47] So we a star it would be great to build staff that can answer our own questions, you know that we can like figure out things basically I'll I'll kind of show all this looks very like retrofitted but it's not I'm I'm gonna actually give you screen shots and show you everything.
[02:47 - 02:53] And then we in November we launched the web search you know for our own friends.
[02:53 - 03:00] We had discord bots then obviously end of November ChatGPT t launches considered the iphone moment for AI.
[03:00 - 03:03] A week after that we launched perplexity.
[03:03 - 03:14] And so that's so this is exactly, you know we incorporated in August third, and then like on September 20 seventh, we had this slack bar.
[03:14 - 03:16] So this is for ourselves.
[03:16 - 03:33] Like we look at the questions we asked, like we asking like how to start ruserver and ruby or like what is soso Q L like sales force qulanguage because we were working on like stuff like, Oh, how do like search or your sales force data, how to search or have spot data.
[03:33 - 03:36] And we had no idea about any of these things.
[03:36 - 03:44] So like for example, this is me trying to write huspot sql queries as templates for like you know teaching our contractors how to do that.
[03:44 - 03:48] Because only if I know how to do that, I can teach contractors.
[03:48 - 03:53] So then I don't know how to do that because none of these tables make any sense to me.
[03:53 - 03:54] They're all complicated.
[03:54 - 03:58] There's just too many things, and people customize it a lot.
[03:58 - 04:02] So there is no hub spot expert you could go and talk to.
[04:02 - 04:12] So itbe great if there is a, search engine that just answers my own questions, and obviously godoesn't answer any of these questions.
[04:12 - 04:16] So that's the difference between, what AI can do and what gocan do.
[04:16 - 04:25] So gocan give you links, gocan answer you like, navigate you to a web page, give you these, like, very trivial, factual answers for, like, very simple things.
[04:25 - 04:32] But it cannot answer complex queries, like, you know, what does a life cycle stage mean in a certain table?
[04:32 - 04:37] Or like, if I were to change this to this thing, like, how do I still get information out?
[04:37 - 04:46] Like what, you know, all sorts of things that you would have to ask another fellow employee, or a friend or a colleague working somewhere else.
[04:46 - 04:48] Like these kind of things are rlike.
[04:48 - 04:51] You know AI has really changed the story.
[04:51 - 04:59] So it's creating a new product, new market segment, and not like taking market share from something that already exists.
[04:59 - 05:02] So we found this to be super useful for ourselves.
[05:02 - 05:21] You know like Paul Graham is very famous for saying this, and why combinator is very famous for this, that you first have to build something that you and friends around you, people around you use, and if you don't even have that, it's very hard for you to find product market fit with somebody else.
[05:21 - 05:32] And even if you do have something that someone else wants but you never use it yourself, it's unlikely that you'll do a good job at it because you don't really care.
[05:32 - 05:36] Like why why is that person's problem your problem, right?
[05:36 - 05:45] Like that's, it's a, it's your problem because you wanna make money by solving their problems, but that won't be a long lasting motivation.
[05:45 - 06:01] So I think it's very important that like, you know, you PaaS this filter for every startup that you, yourself and your, your own, people in your own company start using it and you learn so much from it so that, this is another example.
[06:01 - 06:06] I, you know, I had no company building experience before starting this.
[06:06 - 06:14] And at some point I realized like you know when I would try to recruit people, they would ask me, do you give health insurance?
[06:14 - 06:18] And like we didn't even take health insurance for anybody.
[06:18 - 06:19] Like there is no policy.
[06:19 - 06:22] We didn't even have gust store just for x, none of these.
[06:22 - 06:27] So then I when when you go and pick like stuff, I had no idea what any of these terms meant.
[06:27 - 06:31] There are all these stuff like deductible is, you know, they louconfusing you right?
[06:31 - 06:34] So, so again, goois pretty bad at these things.
[06:34 - 06:37] If you ask these questions there, you just get like a link.
[06:37 - 06:42] And like all these insurance providers just pay gooso much money to get their web sites up.
[06:42 - 06:45] It doesn't actually solve your problems.
[06:45 - 06:48] So I use, I started using it a lot.
[06:48 - 06:56] And then what we what we ended up realizing is that when we asked these sort of questions, I wouldn't be able to trust the answer.
[06:56 - 07:03] So when I would go and ask somebody else who had done this before, they would tell me, no, no, no, what you said is wrong.
[07:03 - 07:14] And obviously, you know in hindsight it's obvious, but you need to get plugged into real data or else you can't trust the answer of chat bot.
[07:14 - 07:15] That is the language model.
[07:15 - 07:18] So you need to plug it into a search index.
[07:18 - 07:22] And and then my co founder, Dennis, is our cto.
[07:22 - 07:32] O, like he's just like casually says, I added some big search and summarization, and then we are able to ask like real live day questions like what happens?
[07:32 - 07:37] So o like at that time, it was the time when Elon was taking ging over Twitter.
[07:37 - 07:40] So he's like, has Elon fired Twitter executives?
[07:40 - 07:43] And that was when he fired the previous CEO pargue.
[07:43 - 07:49] So to answer all these questions, gave all these links, it was all like a nice lack g bot.
[07:49 - 07:54] We were all like just back in AI people, so we didn't have time to build front end.
[07:54 - 07:56] So we just tested with slack g bots.
[07:56 - 08:01] And then it started becoming fun as we made it conversational multiplayer.
[08:01 - 08:07] You know other people could come and ask questions on top of what someone else asked.
[08:07 - 08:11] Like so here Nick, our first engineer is like, why did Elon buy Twitter?
[08:11 - 08:14] And then like Dennis goes and ask, is he taking it private?
[08:14 - 08:17] So you know so and I'm very useful.
[08:17 - 08:21] Like you can just learn a lot from seeing what other people are asking to.
[08:21 - 08:29] And and then our investor, Nat Friedman tells us that you know like mid journeys at the scod bar, like you know it shouldn't work on slack.
[08:29 - 08:31] Like discord is an inexpect thing.
[08:31 - 08:32] So you make a discord bar.
[08:32 - 08:34] And the ui is also much better than slack.
[08:34 - 08:41] So we made a discord bar and like we started a small discord server and like you know it was pretty pretty funny, entertaining.
[08:41 - 08:47] Whoever joined the server and tried out the bar, they they would be like, Oh, this is so much better than golike.
[08:47 - 08:48] I would use it every day.
[08:48 - 08:50] And we we didn't initially believe that.
[08:50 - 08:57] We thought, okay, they are just saying it would be nice to us and be encouraging, but they did actually keep using it.
[08:57 - 09:01] So that gave us a lot of you know hope that this is actually something real.
[09:01 - 09:07] So note that this was still a time when we were working on our our sql enterprise stuff.
[09:07 - 09:09] So this was more like a distraction.
[09:09 - 09:11] So I wasn't sure what to do.
[09:11 - 09:13] Like I why are we even working on this?
[09:13 - 09:22] There was always that question, but one thing that's is when something starts working, that there is like a dopamine from constantly improving it.
[09:22 - 09:29] When you see people asking for stuff and it's it keeps shipping and keeps getting better, you feel the momentum.
[09:29 - 09:40] So my co founder, again, Dennis, added these focuses where you can search specifically about Wikipedia and then you can search specifically on stack overflow.
[09:40 - 09:44] And it would answer all our coding queries like so much, so much better.
[09:44 - 09:50] And so there was something real here, and this was exactly one day before chat plaunched.
[09:50 - 09:56] And there was like, you know, still not sure what we should be doing because we were working out.
[09:56 - 09:59] We our company was supposed to be doing something else.
[09:59 - 10:06] And we saw the chargpity launch, you know, historic right now, if you think about it.
[10:06 - 10:11] And then this, they broke several myths that you needed to be in discord.
[10:11 - 10:13] Like people don't want chat bots.
[10:13 - 10:19] Like all sorts of things, they basically broke called the existing wisdom at the time.
[10:19 - 10:32] So we were very encouraged by this and we thought we could still add orthogonal value to what they launched because we had this orchestration of combining live knowledge and the chat bought together.
[10:32 - 10:41] So this is again, like ma dis asking Nick if you, if he had like a moment to help him with the css because we we don't know css.
[10:41 - 10:50] And then funnily I tried to generate the code for it with, ChatGPT t and then, and then that broke, obviously.
[10:50 - 10:59] So then, you know, somehow Nick came and helped us and then we sent it to one of our friendly like investor friends, Daniel Gross.
[10:59 - 11:03] And if you look at his first comedies, you need a submit mit button.
[11:03 - 11:08] It didn't even see because that was a joke because you know the the latency was so bad.
[11:08 - 11:12] It was say it would take 7s or 8s to get the answer.
[11:12 - 11:16] And now if you use our product, it's like almost instantaneous.
[11:16 - 11:20] So that's the you know how how many iterations it's come through.
[11:20 - 11:22] And he gave us like a lot of good feedback.
[11:22 - 11:25] You know this is always very important.
[11:25 - 11:27] Get your first usser so like your product.
[11:27 - 11:28] And then we had this whole thing ready.
[11:28 - 11:30] We were like gonna launch it.
[11:30 - 11:39] And then we got the bravery to launch it, not frewas like go get hundred people, you know like hundred people to use their product.
[11:39 - 11:44] And so we launched it and it went really way better than expectations.
[11:44 - 11:51] And this was sort of the beginning when we decided, okay, fine, we had this whole sql search for enterprises.
[11:51 - 11:56] We had prototyped it on some large relational databases.
[11:56 - 12:07] So we thought, like we might as well release something like a public database powered sql search and test which one actually works, visit the web search or the sql search.
[12:07 - 12:15] So we launched the search over Twitter like which actually got you know, like Jack Dorsey himself to come in code tweter saying, this is great.
[12:15 - 12:18] And that got a lot more ice on perplexity.
[12:18 - 12:20] And people started using both products.
[12:20 - 12:25] We tracked the usage and we saw that the regular web search product got a lot more usage.
[12:25 - 12:38] We were still confused whether we should kill this research or not, but Elon made it easy for us by you know changing the api prices to like something so high that nobody can pay anymore except goso.
[12:38 - 12:42] We decided to just focus on web search, and we made it better.
[12:42 - 12:45] We cwe made it fully end to end conversational.
[12:45 - 12:47] We suggested follow up questions.
[12:47 - 12:55] And then like, you know, I think one thing that, you know, Ned was gracious enough to say is that we should really eve fast.
[12:55 - 12:57] That's basically our identity.
[12:57 - 13:01] Almost some people give us a lot more credit than we deserve.
[13:01 - 13:10] But I think, you know, that's the only way in which we survive this whole competition with Microsoft and gotrying to do all these same things.
[13:10 - 13:15] So we kept iterating, improving from January onwards, tried many, many experiments.
[13:15 - 13:25] And then the next big update was launching this thing called Copilot, which we consider as like a browsing companion, right?
[13:25 - 13:37] So the way it works is, until now, you just ask a question and the AI plugs into a search index, gets the answers and gives it to you in like a direct chat bot.
[13:37 - 13:47] Ui it we are would be cool if it it's more agenent tic and comes back to you, ask some clarifying questions and then like gives you the answer.
[13:47 - 13:53] And the clarifying questions it generates is very question dependence, very dynamic.
[13:53 - 13:58] And it the kind of questions it ascan be like multiple choice, a single choice.
[13:58 - 14:07] So we innovated on this new thing called generative ui like the the based on your query, a user interface is generated according to it.
[14:07 - 14:13] And we're cell is doing great work now and like you know trying to generate web sites based on what you want.
[14:13 - 14:22] So we we had this idea away before and like sort of inspired by all the noise around auto GPT t and baby agg I at the time.
[14:22 - 14:26] But our thesis was that like autonomy is not like there yet.
[14:26 - 14:29] We still want like these agents to work along with us.
[14:29 - 14:36] So we design a product that way and this sort of basically became our you know usp of our Pro Plan.
[14:36 - 14:43] And people use the Pro Plan for like the co ilot basically for like more research on steroids.
[14:43 - 14:46] That's the best way to think about it.
[14:46 - 14:52] And then we made it even faster recently with OpenAI gb 3.5 fine tuning api.
[14:52 - 14:58] So on the left you see the fine tune gb 3.5 model that's running co ilot.
[14:58 - 15:00] On the right you see gpfour.
[15:00 - 15:05] So gpfour asks you like more questions, but not all of them are needed.
[15:05 - 15:10] Gpthree point five is much faster and just directly just gets to the core point.
[15:10 - 15:24] So ideally we want something that would have the brain of GPT -4 and asking clarifying questions, but the speed and the reliability of GPT -3 point five in terms of like user experience, right?
[15:24 - 15:27] So that's what we tried with this fine tune model.
[15:27 - 15:38] And in terms of metrics, like you know if if you just look at our fgp, 3.5 is like the fine tune model and gpfour and 3.5 are the original models.
[15:38 - 15:43] 80% of the time the user is unable to say like which model is switch.
[15:43 - 15:47] And 8%, it's like they think the fine tune model is better.
[15:47 - 15:50] And like 11%, they think the gp four is still better.
[15:50 - 15:57] So there's still some room for improvement, but this is gonna go more towards like you know the user unable being unable to say.
[15:57 - 16:02] And in terms of GPT -4 us is like like fine tune versus it's just original gp 3.5.
[16:02 - 16:08] You can clearly see that is winning a lot more compared to like you know with fine tuning.
[16:08 - 16:10] And there's a reason we do that.
[16:10 - 16:18] This is because like the the you know the the price you pay for output tokens, this is you know not even comparable, right?
[16:18 - 16:26] Like for example, if you look at the input tokens, the prompt tokens, you are paying three x lower for gb 3.5 compared to four.
[16:26 - 16:32] And for the output tokens, the generated tokens, you're paying six x lower.
[16:32 - 16:38] So this said, the volume of search requests we serve every day makes a ton of difference to us.
[16:38 - 16:44] And it also in terms of speed, you can see the throughput here and the latency here.
[16:44 - 16:47] You know it's like day and night difference, right?
[16:47 - 16:51] So all this like makes for a great better product experience.
[16:51 - 17:00] Like when you're are using on your phone with crappy wi fi or you're on your mobile Internet, these things matter a lot.
[17:00 - 17:10] So we thought through a lot of this, took the opportunity when OpenAI had the fine tuning api available and you know shithis much faster than other people.
[17:10 - 17:14] And Yeah, this got appreciation of the man himself.
[17:14 - 17:18] He came said, great use in metrics, the opi fine ing api.
[17:18 - 17:27] And Yeah so we also you know support other research use cases in the product like we let people upload files and cloud tools.
[17:27 - 17:33] Very much appreciated and known for its long context and you know file upload feature.
[17:33 - 17:40] So we didn't just do file upload because so itbe cool to just add another feature.
[17:40 - 17:44] Our goes to be the best research assistant anybody can have.
[17:44 - 17:52] And uploading your files and asking questions about it is like one very essential component of any research workflow, right?
[17:52 - 17:58] So we just did this and we thought plot two has much better capabilities here compared to GPT -4.
[17:58 - 18:02] So we worked together with anthropic and made this happen.
[18:02 - 18:05] And this also got a lot of positive attention for us.
[18:06 - 18:10] So recently we launched this thing called collections.
[18:10 - 18:40] Where this is our transition from you know moving from just a tool to a enine platform where you can like instead of just pasting our url somewhere and like being scattered around your slack or what's app or like your you know email somewhere, we just are being nice if it's all like persistent and like store sasomewhere and you can collaborate with people and you can also have your own privacy levels in terms of what you want to share publicly and keep it private.
[18:40 - 18:58] So if you want to have like one set of collections for like you know planning your holiday trip with your friends or family, then that's different from having another set of collections where you're just doing research on companies or you're having like code ding queries about some new framework that you're learning.
[18:58 - 19:00] All of these can be like you know decouple, right?
[19:00 - 19:13] So this is sort of becoming more like a platform than this, the two, and that's very important because we we see this as a way to like truly differentiate ourselves and have people coming back to using the product every day.
[19:13 - 19:19] So this is you know something that we'll be doing more of in the coming months.
[19:19 - 19:37] And this thing I wanna like you know I've said this before, there's a lot of like you know different opinions arenlike you know whether being a rapper versus training ining your own model tuh, what is what is like, you know, respected more like what's needed for a startup.
[19:37 - 19:43] And there is this code from this Steve Jobs movie, where was nilike basically asked them, what do you actually do?
[19:43 - 19:48] Like, you know, you don't own the, you you don't do the hardcore engineering.
[19:48 - 19:59] And he says, I play the orchestra and orchestration, like orchestrating different components, search index, llm conversational, rendering the answer multimodal.
[19:59 - 20:00] It's not easy.
[20:00 - 20:03] It takes a lot of work even in being a rapper.
[20:03 - 20:09] Like if you do decide to be a rapper, you might as well be a good rapper, right?
[20:09 - 20:11] Like and then devils in the details.
[20:11 - 20:21] And so for example, like I was telling some about like the barred extension story on Twitter, and I tried like, Hey, like I'm just gonna see if this works.
[20:21 - 20:23] Maybe I'm wrong about orchestration.
[20:23 - 20:27] And I just ask how many flights they had taken the last two months.
[20:27 - 20:31] And it it it doesn't even plug into the gmail my my gmail to give me the answer.
[20:31 - 20:41] And then there's a user here coming and replying to me saying that when when it work, when working with documents, like perplexity gives way better answers without hallucinations.
[20:41 - 20:44] And then similarly, this is another product called U chat.
[20:44 - 20:47] And then I don't even like try to game it.
[20:47 - 20:57] I'd only pick the query they suggested, write a song about whales in the ocean and then it gives me a weather widget, like I didn't ask about the weather, right?
[20:57 - 21:02] So it's very it's very easy to like say, Oh Yeah, we connected to all these plugins.
[21:02 - 21:11] We connected it to all these apis, data providers, and then when you try it, like it does something unreliable at inference time, right?
[21:11 - 21:17] So that's why like we are being more careful here and trying to do it with thought.
[21:17 - 21:23] Like for example, Stanford evaluated all these generative search engines.
[21:23 - 21:25] And like you have two axis here.
[21:25 - 21:35] One is perceived utility and the other is the citation effluence score, effence score, just the weighted average of precision and recall.
[21:35 - 21:37] And you want na be good on both.
[21:37 - 21:41] That is, you want na have a high citation score so that.
[21:41 - 22:01] You're backing up what you say in the answer with the relevant links, and you also wanna be having high utility score so that your answer is readable to the user and makes for a good experience and in and so you wanna be as far as possible in the top right corner and not too much on like you know only on y axis or x axis.
[22:01 - 22:07] And and you look at it like we were the best priof all all four at the time of you know publication of this paper.
[22:07 - 22:13] And this was at a time when we were only using gpthree point five and Bing was using gpfour as default.
[22:13 - 22:22] So if we read on the evaluations with it like the current model, which is much better, I'm sure we'll score even better on these metrics.
[22:22 - 22:24] And so people are seeing seeing that.
[22:24 - 22:29] And you know these days people are tweeting about it at the time we raise funding.
[22:29 - 22:43] A lot of the, you know, it was exactly the time Bing was launched and we had, we ourselves had a lot of fear, leave alone people around us caring us that, Oh, like why are you working on something Microsoft is gonna win here.
[22:43 - 22:48] But I think what we learned over these months is that it's not just about one launch.
[22:48 - 22:55] You gotta keep on iterating and keep on improving or and users will eventually realize like the better product.
[22:55 - 23:00] So even now, it's not like Oh, like you you don't need to think like this guy is thinking he's already ahead.
[23:00 - 23:14] But you know like we fully understand we kind of have to keep improving the product, but the most important part is establishing the platform, the flywheel, the infrara and like the iteration component.
[23:14 - 23:17] So that's what we are very happy about doing so far.
[23:17 - 23:22] And this is like a good summary of like what you know how to best interpret our two.
[23:22 - 23:30] It's basically like Wikipedia and chagphave a baby, but the data is not just wikipediods from the entire Internet.
[23:30 - 23:33] So it's perfect tool for doing a deep dive on any topic.
[23:33 - 23:36] It's built for like people like you.
[23:36 - 23:44] You know we all like we're interested in like you know diving deep and like you know digging into rabbit holes.
[23:44 - 23:45] So that's the idea.
[23:45 - 23:49] It should exite people like you to use these products.
[23:49 - 23:55] And and you know Additionally, we also like took this feedback that we don't want to just be a rapper.
[23:55 - 24:13] So we are trying to serve our own models to and with that in mind, we first launched lama models as part of perplexity labs, which is the fastest inference lama right now among any other products like hugging phase replicate.
[24:13 - 24:16] So many other people like also serving lama models.
[24:16 - 24:27] But in terms of metrics, we we publish our metrics and like you can actually see the tokens per second time to first token everything, right?
[24:27 - 24:29] So we have the best latency.
[24:29 - 24:39] And I think this person also evaluated it with so many other people and realized like we are functioning the best.
[24:39 - 24:46] So actually, I wanna do a demo of a model that we just launched today in the laperplexity labs.
[24:46 - 24:50] It's called lama 2:13B S of t.
[24:50 - 24:57] So this is a step towards us training our own models too, not just serving metal models.
[24:57 - 25:14] So if you remember, lama got a lot of criticism for like you know having like basically being super annoying to use it would just not obey our instructions because it's it's it's just too safe, right?
[25:14 - 25:27] And then we decided, okay, that's a good fine tuning step towards you know if you if you go back to the original lama and ask it to do the same thing, it's not going to answer you all these things.
[25:27 - 25:38] So if you ask it like how to cool Linux process, it's just gonna tell you I'm programmed to be the you know safety and welbeing of people.
[25:38 - 25:46] I can't tell you how to do it, all these kind of things, or like it's not gonna give you jokes that you want, like or jokes about any person.
[25:46 - 25:55] And we decided that weat least try to like fine tunthese models to be more useful rather than going too much in the direction of harmlessness.
[25:55 - 26:06] And so this is an experiment we are trying out and we expect to update people more on like our own models and start serving our own models to the product.
[26:06 - 26:14] So right now, already in perplexity, you're are getting this, you know, if you're on the Pro Plan, you can pick your models of choice.
[26:14 - 26:16] Like we have our own models.
[26:16 - 26:18] That's GPT -4, this clot two.
[26:18 - 26:24] And I think over time, the model that we serve will be the best suited for this particular product.
[26:24 - 26:37] So and we also expect like, you know, not people not to be like people probably won't care enough to just pick the models of their choice, but just you know how one model that just works.
[26:37 - 26:38] And that's our goal.
[26:38 - 26:42] That's why we are trying all these experiments to train and serve our own models.
[26:42 - 26:46] Yeah so that's basically it.
[26:46 - 26:51] I think have some time for questions.
[27:07 - 27:10] So where are you using gray here?
[27:10 - 27:14] Sorry, where is the usage free?
[27:14 - 27:15] Are you using gray?
[27:15 - 27:18] Any any part of a ining or Yeah.
[27:18 - 27:34] So we we consider using it for fine tuning models and we are currently testing our own infrastructure based on Megatron and any scales fine tuning.
[27:34 - 27:37] So we'll have something to say there soon.
[27:37 - 27:39] Nothing in production.
[27:39 - 27:43] So nothing in production, not nothing we can announce publicly.
[27:43 - 27:43] Okay.
[27:43 - 27:44] Okay, thank you.
[27:44 - 27:46] And also the citations right?
[27:46 - 27:49] You pointed the paper I'm user of both of you.
[27:49 - 27:51] You dot com and perplexity.
[27:51 - 27:51] Right?
[27:51 - 27:53] So they are also improving.
[27:53 - 27:55] I see both are equal now.
[27:55 - 27:59] So what's your road map of coping up with that competition?
[27:59 - 28:09] Now both are equal because on the same data set, which is Stanford because I am a Stanford student, I ran the same and both are equal now.
[28:09 - 28:11] So what's your road map ahead?
[28:11 - 28:13] You can share.
[28:13 - 28:18] I don't think both are equal, but if it's I can comment on more.
[28:18 - 28:18] Sure.
[28:18 - 28:19] Sure.
[28:19 - 28:19] Thank you.
[28:32 - 28:35] He been using perplexity for quite some time.
[28:35 - 28:37] Thanks for building it.
[28:37 - 28:48] I've often noticed that when I ask a question, the citations that come up on perplexity are much higher quality than the ones I get on gostill ranking the seu articles a lot more.
[28:48 - 29:08] Given that you still searching the Internet, finding those data points out how are you maintaining the authenticity of the links that used to so we we do the we we have our own like page ranks of the web and we also have the algorithms are so good at like picking the right you know relevant links.
[29:08 - 29:19] So the the final component of algthms picking which papers so which links to site is is actually like a big gain in relevance ranking.
[29:19 - 29:21] So that's also very useful.
[29:21 - 29:22] Thank you.
[29:22 - 29:22] Yeah.
[29:22 - 29:24] I had a question.
[29:24 - 29:29] What are the trade offs you had to make to get llama running so fast?
[29:29 - 29:30] As it seems pretty fast?
[29:30 - 29:31] Yeah.
[29:31 - 29:31] Yeah.
[29:31 - 29:49] So we we I mean, we basically have our own custom inference stack that's, you know we obviously look at everything that's helping others like flash attention or using facet transformer mer page attention and all these all these different ideas.
[29:49 - 30:01] But we decide to use our own stack rather than relying on hugging phase or like wheel or them because that way we can control more.
[30:01 - 30:12] And ya so I would say just at some point, you just have to go and write level stuff at level of kura, right?
[30:12 - 30:16] Or it's pretty hard to like make things much faster.
[30:24 - 30:34] I think as you spoke a little bit about the model that you are customizing your own models, how are you in a larger space context?
[30:34 - 30:36] How are you seeing the role of open source?
[30:36 - 30:44] Do you imagine you be going down that route more and more away from ChatGPT t or you'll still be using cloud or ChatGPT t?
[30:44 - 30:44] Yeah.
[30:44 - 30:52] So I think there's competition from between you know GPT -3 point five fine tuning and open source models, right?
[30:52 - 30:58] Like when we thought, okay, lama is great and we would rather just find lama than opener.
[30:58 - 31:01] Also announced tpthree point five point tunuh.
[31:01 - 31:11] And so if our goal just make the product better, we would do the thing that's cheaper and easier to do right in the short term.
[31:11 - 31:19] That said, I still think there are some things you just cannot do without having access to the weights.
[31:19 - 31:24] And maybe some of this could just be the style of the response.
[31:24 - 31:37] And like other, if you wanna make the elms like more customizable, more agent tic H, all these sort of things, like I think it helps to have your own model, plus, you don't control the pricing, right?
[31:37 - 31:40] That's the most important part.
[31:40 - 32:01] Like like leaving aside like the technical and just think about from the business perspective, like if you don't control the pricing of something, it's always in a tricky position to be where and it's unclear like rising of all these apis will keep remaining the way is today or itgo down or go up.
[32:01 - 32:04] So it's good for you to have your own stuff.
[32:08 - 32:22] Maybe gpd like the close, I think itdefinitely catch up to GPT -4 by like mid next year, but by the time maybe they launch GPT five, so there be some delay, I think.
[32:24 - 32:30] Sorry, we couldn't get around to all the questions, but, let's give Arvin another round of applause.
