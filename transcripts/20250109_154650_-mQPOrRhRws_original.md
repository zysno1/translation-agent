# Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M

## 视频信息
- 视频ID: -mQPOrRhRws
- 视频标题: Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M
- 视频URL: https://www.youtube.com/watch?v=-mQPOrRhRws&t=443s
- 时间长度: 32:36

## 原文
[00:02 - 00:03] Great.

[00:03 - 00:06] Yeah thank you for coming around this time.

[00:06 - 00:09] I'm sure people feel sleepy around this time.

[00:09 - 00:13] So hopefully this is somewhat entertaining.

[00:13 - 00:29] So I'm going to tell you you know how we are trying to think about the future of search, just probably the most you know intuitive and important product that you know every consumer can use and how we are approaching it at perplexity.

[00:29 - 00:49] So think of this kind of linear story where we just saw like good work like this, where, you know, I'm searching for like good headphones, and this is a ton of ads sponsored links, seo content and super tiring.

[00:49 - 00:59] And then we just decided, okay, itwill be nice what it will be itwould be really cool if we can just directly just see the answer and compare different things.

[00:59 - 01:05] And so we just decided, okay, let's build the world's best research assistant that can just answer any question.

[01:05 - 01:11] And then we ended up building this and let's handle the story and thatwould be very disappointing, right?

[01:11 - 01:15] Like hewould be like, Oh, why did I even come for this talk?

[01:15 - 01:20] But so the answer is, obviously, I wish it for this linear.

[01:20 - 01:27] I would think about myself like a genius or something, but it was hardly this linear.

[01:27 - 01:30] So this is actually what really happened.

[01:30 - 01:40] Like we incorporated one year ago, we started working on Texas sql, which had nothing to do with consumer search.

[01:40 - 01:49] In fact, like if you went to vcs and asked for money to work on search, they just wouldn't even fund you, right?

[01:49 - 01:57] No matter how ambitious you are, like how it's very hard for you to convince anybody to fund you.

[01:57 - 01:59] So we worked on Texas sql.

[01:59 - 02:07] We got lucky enough that really good people like Elard, gill, nt, Friedman and Jeff all like investor in us.

[02:07 - 02:15] And we were like really just interested in like looking into enterprise search with L M plus equal ql.

[02:15 - 02:19] And we just couldn't know how to even do all this stuff.

[02:19 - 02:23] Company building enterprise, none of these things.

[02:23 - 02:25] Like nothing was interiitive.

[02:25 - 02:28] There was no expert to answer anything.

[02:28 - 02:28] We knew.

[02:28 - 02:29] So we a star.

[02:29 - 02:37] It would be great to build staff that can answer our own questions, that we can figure out things.

[02:37 - 02:42] Basically, I'll kind of show all this looks very like retrofitted, but it's not.

[02:42 - 02:48] I'm going to actually give you screen shots and show you everything.

[02:48 - 02:53] And then we in November, we launched the web search you for our own friends.

[02:53 - 02:55] We had discord bots.

[02:55 - 03:01] Then obviously, end of November ChatGPT launches considered the iphone moment for AI.

[03:01 - 03:04] A week after that, we launched perplexity.

[03:04 - 03:06] And so this is exactly you.

[03:06 - 03:09] We incorporated in August third.

[03:09 - 03:14] And then like on September 20 seventh, we had this slack g Boso.

[03:14 - 03:16] This is for ourselves.

[03:16 - 03:25] Like we look at the questions we asked, like we were asking like how to start ruserver and ruby, like what is soql like sales force career language?

[03:25 - 03:36] Because we were working on stuff like Oh, how to search or your sales force data, how to search or have spot data, and we had no idea about any of these things.

[03:36 - 03:48] So for example, this is me trying to write hub spot sql queries as templates for like, you know, teaching our contractors how to do that, because only if I know how to do that, I can teach contractors.

[03:48 - 03:53] So then I don't know how to do that, because none of these tables make any sense to me.

[03:53 - 03:54] They're all complicated.

[03:54 - 03:58] There's just too many things, and people customize it a lot.

[03:58 - 04:02] So there is no hub spot expert you could go and talk to.

[04:02 - 04:12] So itwould be great if there is a search engine that just answers my own questions, and obviously godoesn't answer any of these questions.

[04:12 - 04:17] So that's the difference between what AI can do and what can do.

[04:17 - 04:25] So can give you links, can answer you, like navigate you to a web page, give you these very trivial, factual answers for very simple things.

[04:25 - 04:28] But it cannot answer complex queries.

[04:28 - 04:31] Like, what does a life cycle stage mean in a certain table?

[04:31 - 04:37] Or like, if I were to change this to this thing, like how do I still get the information out?

[04:37 - 04:48] Like what you all sorts of things that you would have to ask another fellow employee or a friend or a colleague working somewhere else, like these kind of things are rlike.

[04:48 - 04:51] You know, AI has really changed the story.

[04:51 - 04:59] So it's creating a new product, new market segment and not like taking market share from something that already exists.

[04:59 - 05:03] So we found this to be super useful for ourselves.

[05:03 - 05:14] Like Paul Graham is very famous for saying this and why combinator is very famous for this, that you first have to build something that you and friends around you, people around you use.

[05:14 - 05:21] And if you don't even have that, it's very hard for you to find product market fit with somebody else.

[05:21 - 05:33] And even if you do have something that someone else wants, but you never use it yourself, it's unlikely that you'll do a good job at it because you don't really care.

[05:33 - 05:36] Like why is that person's problem your problem, right?

[05:36 - 05:41] Like it's your problem because you want to make money by solving their problems.

[05:41 - 05:45] That won't be a long lasting motivation.

[05:45 - 05:59] So I think it's very important that you PaaS this filter for every startup that you yourself and your own people in your own companies start using it, and you learn so much from it.

[05:59 - 06:02] So that this is another example.

[06:02 - 06:07] I had no company building experience before starting this.

[06:07 - 06:14] And at some point I realized like when I would try to recruit people, they would ask me, do you give health insurance?

[06:14 - 06:18] And like we didn't even take health insurance for anybody.

[06:18 - 06:19] Like there was no policy.

[06:19 - 06:22] We didn't even have gust to or just for x, none of these.

[06:22 - 06:27] So then when you go and pick like stuff, I had no idea what any of these terms meant.

[06:27 - 06:31] There are all these stuff like deductible is, you know, they allow confusing you, right?

[06:31 - 06:34] So again, goois pretty bad at these things.

[06:34 - 06:37] If you ask these questions, you just get like alings.

[06:37 - 06:42] And like all these insurance providers just pay gooso much money to get their web sites up.

[06:42 - 06:46] It doesn't actually solve your problems.

[06:46 - 06:48] So I started using it a lot.

[06:48 - 06:56] And then what we ended up realizing is that when we asked these sort of questions, I wouldn't be able to trust the answer.

[06:56 - 07:04] So when I would go and ask somebody else who had done this before, they would tell me, no, no, no, what you said is wrong.

[07:04 - 07:13] And obviously, in hindsight, it's obvious, but you need to get plugged into real data or else you can't trust the answer of chat bot.

[07:13 - 07:15] That is the language model.

[07:15 - 07:18] So you need to plug it into a search index.

[07:18 - 07:22] And then my co founder, Dennis is our cto.

[07:22 - 07:32] Like he just like casually says, I added some big search and summarization and then we are able to ask like real live questions like what happened?

[07:32 - 07:37] So like at that time, it was the time when Elon was taking over Twitter.

[07:37 - 07:40] So he's like, has Elon fired Twitter executives?

[07:40 - 07:43] And that was when he fired the previous CEO, Parak.

[07:43 - 07:49] So to answer all these questions, gave all these links, it was all like a nice slack g bot.

[07:49 - 07:54] We were all like just back in on AI people, so we didn't have time to build front end.

[07:54 - 07:56] So we just tested with slack g bots.

[07:56 - 08:01] And then it started becoming fun as we made it conversational multiplayer.

[08:01 - 08:07] You know, other people could come and ask questions on top of what someone else asked.

[08:07 - 08:11] Like so here Nick, our first engineer, is like, why did Elon buy Twitter?

[08:11 - 08:15] And then like Dennis goes and ask, is he taking it private?

[08:15 - 08:21] So, you know so and I'm very useful, like you can just learn a lot from seeing what other people are asking to.

[08:21 - 08:27] And then our investor, Nat Friedman tells us that you know like mid journeys is a discord bar.

[08:27 - 08:29] You it shouldn't work on slack.

[08:29 - 08:31] Like discord is an expect thing.

[08:31 - 08:35] So you make a discord bar and the ui is also much better than slack.

[08:35 - 08:39] So we made a discord bar and we started a small discord server.

[08:39 - 08:41] And it was pretty funny, entertaining.

[08:41 - 08:47] Whoever joined the server and tried out the bar, they would be like, Oh, this is so much better than goolike.

[08:47 - 08:49] I would use it every day.

[08:49 - 08:51] And we didn't initially believe lethat.

[08:51 - 08:56] We thought, okay, they just saying it would be nice to us and be encouraging.

[08:56 - 08:58] But they did actually keep using it.

[08:58 - 09:02] So that gave us a lot of hope that this is actually something real.

[09:02 - 09:07] So note that this was still a time when we were working on our sql enterprise stuff.

[09:07 - 09:09] So this was more like a distraction.

[09:09 - 09:11] So I wasn't sure what to do.

[09:11 - 09:14] I why are we even working on this?

[09:14 - 09:16] There was always that question.

[09:16 - 09:23] But one thing that's through is when something starts working, that there is like a dopamine from constantly improving it.

[09:23 - 09:29] When you see people asking for stuff and you keep eps shipping, it keeps getting better.

[09:29 - 09:30] You feel the momentum.

[09:30 - 09:40] So my founder, again, Dennis, added these focuses where you can search specifically about Wikipedia and then you can search specifically on stack overflow.

[09:40 - 09:45] And it would answer all our code inqueries like so much, so much better.

[09:45 - 09:51] And so there was something real here, and this was exactly one day before cp launched.

[09:51 - 10:01] And that was like, you know, still not sure what we should be doing because we were working on our company was supposed to be doing something else.

[10:01 - 10:10] And we saw the chagt launched historic right now, if you think about it, and then they broke several meths that you needed to be in discord.

[10:10 - 10:12] Like people don't want chat bots.

[10:12 - 10:18] Like all sorts of things they basically broke called the existing wisdom at the time.

[10:18 - 10:21] So we were very encouraged by this.

[10:21 - 10:32] And we thought we could still add orthogonal value to what they launched because we had this orchestration of combining live knowledge and the chat bought together.

[10:32 - 10:42] So this is again, like Dennis asking Nick if he had like a moment to help him with the css because we don't know css.

[10:42 - 10:47] And then funnily, I tried to generate the code for it with ChatGPT.

[10:47 - 10:49] Then that broke, obviously.

[10:49 - 10:59] So then somehow Nick came and helped us, and then we sent it to one of our friendly investor friends, Daniel Gross.

[10:59 - 11:03] And if you look at his first comedies, you need a submit mit button.

[11:03 - 11:08] Didn't even see because that was a joke, because the latency was so bad.

[11:08 - 11:12] It say it would take 7s or 8s to get the answer.

[11:12 - 11:16] And now if you use our product, it's like almost instantaneous.

[11:16 - 11:19] So that's the how many iterations it's come through.

[11:19 - 11:22] And he gave us a lot of good feedback.

[11:22 - 11:24] Know this is always very important.

[11:24 - 11:25] Get your first usser.

[11:25 - 11:26] So like your product.

[11:26 - 11:28] And then we had this whole thing ready.

[11:28 - 11:40] We were like going to launch it, and then we got the bravery to launch it because nfreedom man was like, go get 100 people, you like 100 people to use their product.

[11:40 - 11:45] So we launched it and it went really way better than expectations.

[11:45 - 11:49] And this was sort of the beginning when we decided, okay, fine.

[11:49 - 11:52] We had this whole sql search for enterprises.

[11:52 - 11:56] We had prototyped it on some large relational databases.

[11:56 - 12:07] So we thought like we might as well release something like a public database powered sql search and test which one actually works, visit the web search or the sql search.

[12:07 - 12:15] So we launched the search over Twitter, which actually got you, like Jack Dorsey himself, to come in code, tweet us saying, this is great.

[12:15 - 12:18] And that got a lot more ice on perplexity.

[12:18 - 12:20] And people started using both products.

[12:20 - 12:26] We track the usage, and we saw that the regular web search prior got a lot more usage.

[12:26 - 12:39] We were still confused whether we should kill this research search or not, but Elon made it easy for us by changing the api prices to something so high that nobody can pay anymore except goso.

[12:39 - 12:43] We decided to just focus on web search, and we made it better.

[12:43 - 12:46] We made it fully into and conversational.

[12:46 - 12:48] We suggested follow up questions.

[12:48 - 12:55] And then I think one thing that nd was gracious enough to say is that we should really eve fast.

[12:55 - 12:57] That's basically our identity.

[12:57 - 13:10] Almost some people give us a lot more credit than we deserve, but I think that's the only way in which we survive this whole competition with Microsoft and trying to do all these same things.

[13:10 - 13:15] So we kept iterating, improving from January onwards, tried many, many experiments.

[13:15 - 13:25] And then the next big update was launching this thing called Copilot, which we consider as like a browsing companion.

[13:25 - 13:37] So the way it works is, until now, you just ask a question, and the AI plugs into a search index, gets the answers and gives it to you in like a direct chat bot.

[13:37 - 13:47] Ui, we would be cool if it's more agenentic and comes back to you, ask some clarifying questions and then gives you the answer.

[13:47 - 13:53] And the clarifying questions it generates is very question dependence, very dynamic.

[13:53 - 13:58] And the kind of questions it asks can be like multiple choice, a single choice.

[13:58 - 14:07] So we innovated on this new thing called generative ui, like based on your query, a user interface is generated according to it.

[14:07 - 14:13] And where cell is doing great work now and trying to generate web sites based on what you want.

[14:13 - 14:22] So we had this idea away before and sort of inspired by all the noise around auto GPT and baby agi at the time.

[14:22 - 14:25] But our thesis was that autonomy is not like there yet.

[14:25 - 14:29] We still want these agents to work along with us.

[14:29 - 14:31] So we design a product that way.

[14:31 - 14:36] And this sort of basically became our usb of our Pro Plan.

[14:36 - 14:43] And people use the Pro Plan for like the co ilot basically for like more research on steroids.

[14:43 - 14:46] That's the best way to think about it.

[14:46 - 14:52] And then we made it even faster recently with OpenAI gbthree point five fine tuning api.

[14:52 - 14:58] So on the left you see the fine tune gbthree point five model that's running Copilot.

[14:58 - 15:00] On the right you see GPT -4.

[15:00 - 15:05] So GPT -4 asks you like more questions, but not all of them are needed.

[15:05 - 15:10] GPT -3 point five is much faster and it just directly just gets to the core point.

[15:10 - 15:18] So ideally, we want something that would have the brain of GPT -4 and asking clarifying questions.

[15:18 - 15:24] But the speed and the reliability of GPT -3 in terms of user experience.

[15:24 - 15:27] So that's what we tried with this fine tune model.

[15:27 - 15:43] And in terms of metrics, like if you just look at our fgp three as like the fine tune model and GPT -4 and 3.5 are the original models, 80% of the time, the user is unable to say like which model is switch.

[15:43 - 15:47] And 8%, it's like they think the fine tune model is better.

[15:47 - 15:50] And like 11%, they think the gp four is still better.

[15:50 - 15:53] So there's still some room for improvement.

[15:53 - 15:57] But this is going to go more towards like the user being unable to say.

[15:57 - 16:02] And in terms of GPT -4, us is like fine tune versus just the original GPT -3 point five.

[16:02 - 16:08] You can clearly see that is winning a lot more compared to like without fine tuning.

[16:08 - 16:11] And there's a reason we do that.

[16:11 - 16:17] This is because like the price you pay for output tokens, this is not even comparable, right?

[16:17 - 16:26] Like for example, if you look at the input tokens, the prom tokens, you're are paying three x lower for gb 3.5 compared to four.

[16:26 - 16:31] And for the output tokens, the generated tokens, you're paying six x lower.

[16:31 - 16:39] So this said, the volume of search requests we serve every day makes a ton of difference to us.

[16:39 - 16:47] And it also in terms of speed, you can see the throughput here and the latency here know it's like day and night difference, right?

[16:47 - 16:51] So all this like makes for a great better product experience.

[16:51 - 17:00] Like when you're using on your phone with crappy wi fi or you're on your mobile Internet, these things matter a lot.

[17:00 - 17:10] So we thought through a lot of this, took the opportunity when OpenAI had the fine tuning api available and shipped this much faster than other people.

[17:10 - 17:19] And Yeah, this got the appreciation of the man himself, kisaid great use in metrics, the open ei fine ing api.

[17:19 - 17:27] And Yeah, so we also support other research use cases in the product, like we let people upload files and cloud tools.

[17:27 - 17:33] Very much appreciated and known for its long context and file upload feature.

[17:33 - 17:40] So we didn't just do file upload because so itwill be cool to just add another feature.

[17:40 - 17:44] Our goes to be the best a research assistant anybody can have.

[17:44 - 17:52] And uploading your files and asking questions about it is like one very essential component of any research workflow, right?

[17:52 - 17:58] So we just did this and we thought plot two has much better capabilities here compared to GPT -4.

[17:58 - 18:02] So we worked together with anthropic and made this happen.

[18:02 - 18:05] And this also got a lot of positive attention for us.

[18:06 - 18:40] So recently we launched this thing called collections, where this is our transition from moving from just a tool to a enine platform where you can like instead of just pasting our url somewhere and like being scattered around your slack or what's saapp or like your know email somewhere, we just started to be nice if it's all like persistent and like store saved somewhere and you can collaborate with people and you can also have your own privacy levels in terms of what you want to share publicly and keep it private.

[18:40 - 18:58] So if you want to have one set of collections for planning your holiday trip with your friends or family, then that's different from having another set of collections where you're just doing research on companies or you're having like code ding queries about some new framework that you're learning.

[18:58 - 19:00] All of these can be like decouple, right?

[19:00 - 19:03] So this is sort of becoming more like a platform than this.

[19:03 - 19:13] The two, and that's very important because we see this as a way to truly differentiate ourselves and have people coming back to using the product every day.

[19:13 - 19:19] So this is something that we'll be doing more of in the coming months.

[19:19 - 19:37] And this thing I want to like I've said this before, there's a lot of like you different opinions on like you whether being a rapper versus training your own model, what is like respected more or like what's needed for a startup.

[19:37 - 19:44] And there is this code from this Steve Jobs movie, where was nilike basically asked him, what do you actually do?

[19:44 - 19:47] Like you don't do the hardcore engineering.

[19:47 - 20:00] And he says, I play the orchestra and orchestration, like orchestrating different components, search index, llm, conversational, rendering the answer multimodal.

[20:00 - 20:00] It's not easy.

[20:00 - 20:04] It takes a lot of work, even in being a rapper.

[20:04 - 20:09] Like if you do decide to be a rapper, you might as well be a good rapper, right?

[20:09 - 20:12] And then devil is in the details.

[20:12 - 20:21] And so, for example, I was telling about like the barred extension story on Twitter, and I tried like, Hey, I'm just going to see if this works.

[20:21 - 20:24] Maybe I'm wrong about orchestration.

[20:24 - 20:27] And I just ask how many flights they had taken the last two months.

[20:27 - 20:31] And it doesn't even plug into the my gmail to give me the answer.

[20:31 - 20:41] And then there's a user here coming and replying to me saying that when it worked, when working with documents, like perplexity gives way better answers without hallucinations.

[20:41 - 20:44] And then similarly, this is another product called U chat.

[20:44 - 20:47] And then I don't even try to game it.

[20:47 - 20:57] I'd only pick the query they suggested, write a song about whales in the ocean, and then it gives me a weather widget, like I didn't ask about the weather, right?

[20:57 - 21:02] So it's very easy to say, Oh Yeah, we connected to all these pluggins.

[21:02 - 21:05] We connect it to all these apis, data providers.

[21:05 - 21:11] And then when you try it, like it does something underreliable at inference time, right?

[21:11 - 21:17] So that's why we are being more careful here and trying to do it with thought.

[21:17 - 21:23] Like, for example, Stanford evaluated all these generative search engines.

[21:23 - 21:25] And like you have two axis here.

[21:25 - 21:35] One is perceived utility and the other is citation effone score, effone score, just the weighted average of precision and recall.

[21:35 - 21:37] And you want to be good on both.

[21:37 - 21:46] That is, you want to have a high citation score so that you're backing up what you say in the answer with the relevant links.

[21:46 - 21:54] And you also want to be having high utility score so that your answer is readable to the user and makes for a good experience.

[21:54 - 22:01] And so you want to be as far as possible in the top right corner and not too much on only on y axis or x axis.

[22:01 - 22:07] And you look at it like we were the best priof all four at the time of publication of this paper.

[22:07 - 22:13] And this was at a time when we were only using gpthree point five and Bing was using GPT -4 as default.

[22:13 - 22:22] So if we read on the evaluations with it, like the current model, which is much better, I'm sure we'll score even better on these metrics.

[22:22 - 22:25] And so people are seeing that.

[22:25 - 22:27] And these days, people are tweeting about it.

[22:27 - 22:33] At the time we raise funding, a lot of it was exactly the time Bing was launched.

[22:33 - 22:43] And we ourselves had a lot of fear, leave alone people around us caring us like, why are you working on something Microsoft is going to win here.

[22:43 - 22:48] But I think what we learned over these months is that it's not just about one launch.

[22:48 - 22:55] You got to keep on iterating and keep on improving, and users will eventually realize like the better product.

[22:55 - 23:00] So even now, it's not like Oh, like you don't need to think like this guy is thinking he's already ahead.

[23:00 - 23:13] But you know like we fully understand we kind of have to keep improving the product, but the most important part is establishing the platform, the flywheel, the infrara and the iteration component.

[23:13 - 23:17] So that's what we are very happy about doing so far.

[23:17 - 23:22] And this is like a good summary of like what how to best interpreter T R two.

[23:22 - 23:30] It's basically like Wikipedia and chagpt had a baby, but the data is not just wikipediods from the entire Internet.

[23:30 - 23:33] So it's perfect tool for doing a deep dive on any topic.

[23:33 - 23:36] It's built for like people like you.

[23:36 - 23:42] We're all were interested in diving deep and digging into rabbit holes.

[23:42 - 23:43] So that's the idea.

[23:43 - 23:47] It should exite people like you to use these products.

[23:47 - 23:54] And Additionally, we also like took this feedback that we don't want to just be a rapper.

[23:54 - 24:13] So we are trying to serve our own models to and with that in mind, we first launched llama models as part of perplexity labs, which is the fastest inference lama right now among any other products like hugging phase replicate.

[24:13 - 24:17] So many other people like also serving lama models.

[24:17 - 24:27] But in terms of metrics, we publish our metrics and you can actually see the tokens per second time to first token everything, right?

[24:27 - 24:29] So we have the best latency.

[24:29 - 24:38] And I think this person also evaluated it with so many other people and realized like we are functioning the best.

[24:38 - 24:46] So actually, I want to do a demo of a model that we just launched today in the laperplexity labs.

[24:46 - 24:49] It's called lama 213B S.

[24:49 - 24:50] Of t.

[24:50 - 24:57] So this is a step towards us training our own models too, not just serving matters models.

[24:57 - 25:07] So if you remember, lama got a lot of criticism for having like basically being super annoying to use.

[25:07 - 25:13] It would just not obey our instructions because it's just too safe, right?

[25:13 - 25:27] And then we decided, okay, that's a good fine tuning step towards if you go back to the original lamma and ask it to do the same thing, it's not going to answer you all these things.

[25:27 - 25:38] So if you ask it like how to cool Linux process, it's just going to tell you I'm programmed to be the know safety and well lbeing of people.

[25:38 - 25:46] I can't tell you how to do it, all these kind of things or like it's not going to give you jokes that you want, like or jokes about any person.

[25:46 - 25:55] And we decided that wewould at least try to like fine tune these models to be more useful, rather than going too much in the direction of harmlessness.

[25:55 - 26:06] And so this is an experiment we are trying out, and we expect to update people more on like our own models and start serving our own models through the product.

[26:06 - 26:10] So right now, already in perplexity, you are getting this.

[26:10 - 26:14] You if you're on the Pro Plan, you can pick your models of choice.

[26:14 - 26:16] Like we have our own models.

[26:16 - 26:18] That's GPT -4, that's clot two.

[26:18 - 26:24] And I think over time, the model that we serve will be the best suited for this particular product.

[26:24 - 26:38] So and we also expect like not people not to be like people probably won't care enough to just pick the models of their choice, but just how one model that just works, and that's our goal.

[26:38 - 26:42] That's why we are trying all these experiments to train and serve our own models.

[26:42 - 26:43] Yeah.

[26:43 - 26:47] So that's basically it.

[26:47 - 26:51] I think have some time for questions.

[27:07 - 27:10] So where are you using gray here?

[27:10 - 27:14] Sorry, where is the usage of gray?

[27:14 - 27:16] Are you using gray?

[27:16 - 27:24] Any any part of gray or raining or so we consider using it for fine tuning models.

[27:24 - 27:34] And we are currently testing our own infrastructure based on Megatron and any scales fine tuning.

[27:34 - 27:37] So we'll have something to say there soon.

[27:37 - 27:39] Nothing in production.

[27:39 - 27:41] So nothing in production.

[27:41 - 27:43] Nothing we can announce publicly.

[27:43 - 27:43] Okay.

[27:43 - 27:44] Thank you.

[27:44 - 27:46] And also the citations, right?

[27:46 - 27:49] You pointed the paper I'm user of both of you.

[27:49 - 27:51] You dot com and perplexity.

[27:51 - 27:53] So they're also improving.

[27:53 - 27:54] I see both are equal now.

[27:54 - 27:58] So what's your road map of coping up with that competition?

[27:58 - 28:06] Now both are equal because on the same data set, which is Stanford, because I am a Stanford student, I ran the same.

[28:06 - 28:08] And both are equal now.

[28:08 - 28:10] So what's your road map ahead?

[28:10 - 28:13] I mean, you can share your results with us.

[28:13 - 28:18] I don't think both are equal, but if it's through, then will I can comment on it more.

[28:18 - 28:19] Sure.

[28:19 - 28:19] Sure.

[28:19 - 28:19] Thank you.

[28:32 - 28:35] He been using perplexity for quite some time.

[28:35 - 28:37] Thanks for building it.

[28:37 - 28:48] I've often noticed that when I ask a question, the citations that come up on perplexity are much higher quality than the ones I get on gostill, ranking the su articles a lot more.

[28:48 - 29:08] Given that you're still searching the Internet, finding those data points out how are you maintaining the authenticity of the links that used to so we do we have our own like page ranks of the web and we also have the algorithms are so good at like picking the right relevant links.

[29:08 - 29:18] So the final component of elegthms, picking which papers of which links to site is actually like a big gain in relevance ranking.

[29:18 - 29:21] So that's also very useful.

[29:21 - 29:22] Thank you.

[29:22 - 29:24] Yeah, I had a question.

[29:24 - 29:29] What are the trade offs you had to make to get llama running so fast?

[29:29 - 29:31] Because it seems pretty fast.

[29:31 - 29:32] Yeah.

[29:32 - 29:49] So mean we basically have our own custom inference stack that you know we obviously look at everything that's helping others like flash attention or using facet transformer page attention, all these different ideas.

[29:49 - 30:02] But we decide to use our own stack rather than relying on hugging phase or like wheel of them because that way we can control more.

[30:04 - 30:04] Yeah.

[30:04 - 30:16] So I would say just at some point you just have to go and write stuff at the level of Qura, right, or else it's pretty hard to make things much faster.

[30:24 - 30:34] I think as you spoke a little bit about the model that you are customizing your own models, how are you in a larger space context?

[30:34 - 30:37] How are you seeing the role of open source?

[30:37 - 30:44] Do you imagine you be going down that route more and more away from ChatGPT or you'll still be using cloud or ChatGPT?

[30:44 - 30:44] Yeah.

[30:44 - 30:52] So I think there's competition from between no GPT -3 point five fine tuning and open source models, right?

[30:52 - 30:58] Like when we thought, ok, llama is great and we would rather just find tunlama.

[30:58 - 31:02] Then opena also announced gbd 3.5 point a.

[31:02 - 31:11] And so if our goal just make the product better, we would do the thing that's cheaper and easier to do right in the short term.

[31:11 - 31:19] That said, I still think there are some things you just cannot do without having access to the weights.

[31:19 - 31:37] And maybe some of this could just be the style of the response and like other if you want to make the elms like more customizable, more agent tic H, all these sort of things, like I think it helps to have your own model plus you don't control the pricing, right?

[31:37 - 31:39] That's the most important part.

[31:39 - 31:46] Like leaving aside like the technical, you just think about it from the business perspective.

[31:46 - 32:01] Like if you don't control the pricing of something, it's always in a tricky position to be very and it's unclear like pricing of all these apis will keep remaining the way it is today or itwill go down or go up.

[32:01 - 32:04] So it's good for you to have your own stuff.

[32:08 - 32:22] Maybe GPT d like the close, I think itwill definitely catch up to GPT -4 by like mid next year, but by the time maybe they launch GPT five, so there will be some delay I think.

[32:24 - 32:30] Sorry, we couldn't get around to all the questions, but let's give Arvin another round of applause.


