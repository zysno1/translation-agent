# Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M

## 视频信息
- 视频ID: -mQPOrRhRws
- 视频标题: Perplexity AI: How We Built the World's Best LLM-Powered Search Engine in 6 Months, w/ Less Than $4M
- 视频URL: https://www.youtube.com/watch?v=-mQPOrRhRws&t=443s

## 原文
[00:02 - 00:09] Great, yeah, thank you for coming around this time, I'm sure people feel sleepy around this time.

[00:09 - 00:18] Hopefully this is somewhat entertaining, so I'm going to tell you how we are trying to think about the future of search.

[00:18 - 00:25] Is probably the most intuitive and important product that every consumer can use.

[00:25 - 00:35] And how we are approaching it at perplexity. So think of this kind of linear story.

[00:35 - 00:42] Where we just saw Google work like this, where I'm searching for good headphones.

[00:42 - 00:48] There's just a ton of ads, sponsored links, SEO content, and super tiring.

[00:48 - 00:57] And then we just decided, OK, it'll be nice, it'll be really cool if we can just directly just see the answer.

[00:57 - 01:07] And compare different things and so we just decided okay let's build the world's best research assistant that can just answer any question.

[01:07 - 01:15] And then we ended up building this. And that's the end of the story. And that would be very disappointing, right. Like, you'd be like, oh, why did I even come for this talk.

[01:15 - 01:24] But so the answer is obviously, I wish it were this linear, I would think about myself like a genius or something.

[01:24 - 01:34] It was hardly this linear so this is actually what really happened like we incorporated one year ago.

[01:34 - 01:46] We started working on text to SQL, which had nothing to do with consumer search, in fact, like if you went to VCs and asked for money to work on search,

[01:46 - 01:58] They just wouldn't even fund you, no matter how ambitious you are, it's very hard for you to convince anybody to fund you.

[01:58 - 02:07] So we worked on Text to SQL, we got lucky enough that really good people like Elard Gill, Nat Friedman, Jeff Dean all invested in us.

[02:08 - 02:16] And we were really just interested in looking into enterprise search with LLMs plus SQL.

[02:16 - 02:25] We just couldn't know how to even do all this stuff, company building, enterprise, none of these things, like nothing was intuitive.

[02:25 - 02:36] There was no expert to answer anything we knew, so we just thought it would be great to build staff that can answer our own questions, that we can figure out.

[02:36 - 02:45] Things basically, I'll just kind of show all this looks very like retrofitted, but it's not, I'm going to actually give you screenshots and show you everything.

[02:45 - 02:55] And then in November, we launched a web search for our own friends, we had Discord bots.

[02:55 - 03:04] Then obviously end of November, chat GPD launches considered the iPhone moment for AI, a week after that we launched perplexity.

[03:04 - 03:14] And so this is exactly like, we incorporated on August third, and then on September twenty seventh, we had this Slack bot.

[03:14 - 03:26] So this is for ourselves, like we look at the questions we ask, like we're asking like how to start server and Ruby, or like what is SOQL, it's like Salesforce query language.

[03:26 - 03:33] Because we were working on stuff like, oh, how to search over your Salesforce data, how to search over your HubSpot data.

[03:33 - 03:43] And we had no idea about any of these things, so like for example, this is me trying to write HubSpot SQL queries as templates for like, you know.

[03:43 - 03:55] Teaching our contractors how to do that because only if I know how to do that I can teach contractors right so then I don't know how to do that because none of these tables make any sense to me they're all so complicated.

[03:55 - 04:03] There's just too many things. And people customize it a lot. So there is no Hubspot expert. You could go and talk to. So it would be great if there is.

[04:03 - 04:14] Search engine that just answers my own questions and obviously Google doesn't answer any of these questions so that's the difference between what AI can do and what Google can do.

[04:14 - 04:22] So Google can give you links. Google can answer you, navigate you to a Web page, give you these very trivial.

[04:22 - 04:35] Actual answers for like very simple things, but it cannot answer complex queries like, you know, what does a life cycle stage mean in a certain table or like if I were to change this to this thing like,

[04:35 - 04:46] How do I still get the information out, like what, you know, all sorts of things that you would have to ask another fellow employee or a friend or a colleague working somewhere else like that.

[04:46 - 04:54] These kind of things are where like you know AI has really changed the story so it's creating a new product, new market segment.

[04:54 - 05:04] And not like taking market share from something that already exists. So we found this to be super useful for ourselves. You know, like Paul Graham is very famous for saying this.

[05:04 - 05:13] And Y Combinator is very famous for this, that you first have to build something that you and friends around you, people around you use.

[05:13 - 05:21] And if you don't even have that, it's very hard for you to find product market fit with somebody else.

[05:21 - 05:32] And even if you do have something that someone else wants, but you never use it yourself, it's unlikely that you'll do a good job at it.

[05:32 - 05:41] Because you don't really care, like why is that person's problem your problem, right, like it's your problem because you want to make money by solving their problems.

[05:41 - 05:50] That won't be a long lasting motivation, so I think it's very important that you pass this filter.

[05:50 - 05:58] For every startup that you, yourself, and your own people in your own company start using it, and you learn so much from it.

[05:58 - 06:07] So that this is another example. I had no company building experience before starting this, and.

[06:07 - 06:19] At some point I realized like you know when I would try to recruit people they would ask me do you give health insurance and like we didn't even take health insurance for anybody like there was no policy we didn't even have,

[06:19 - 06:30] Gusto or just works, none of these, so then when you go and pick like stuff, I had no idea what any of these terms meant, there are all these stuff like deductibles, you know, they love confusing you, right?

[06:30 - 06:40] So again, Google is pretty bad at these things, if you ask these questions there, you just get like SEO links and like all these insurance providers just pay Google so much money to,

[06:40 - 06:51] get their websites up, it doesn't actually solve your problems, so I started using it a lot, and then what we ended up realizing is that.

[06:52 - 07:02] When we ask these sort of questions, I wouldn't be able to trust the answer, so when I would go and ask somebody else who had done this before, they would tell me, no, no, no, what you said is wrong.

[07:02 - 07:13] And obviously, you know, in hindsight, it's obvious, but you need to get plug into real data or else you can't trust the answer of.

[07:13 - 07:25] Chatbot, that's just the language model, so you need to plug it into a search index, and then my co-founder, Dennis, he's our CTO, he just casually says,

[07:25 - 07:35] I added some Bing search and summarization. And then we are able to ask real live questions like, what happens here? Like at that time was a time when Elon was.

[07:35 - 07:44] Taking over Twitter, so he's like, has Elon fired Twitter executives, and that was when he fired the previous CEO, Parag.

[07:44 - 07:55] So it answered all these questions, gave all these links, it was all like a nice Slack bot, we were all like just back end and AI people, so we didn't have time to build front end, so we just tested with Slack bots.

[07:55 - 08:07] And then it started becoming fun as we made it conversational, multiplayer, other people could come and ask questions on top of what someone else asked.

[08:07 - 08:15] Here, Nick, our first engineer, he's like, why did Elon buy Twitter, and then Dennis goes and asks, is he taking it private?

[08:15 - 08:30] And very useful, you can just learn a lot from seeing what other people are asking too, and then our investor Nat Friedman tells us that, you know, like Midjourney is a Discord bot, it shouldn't work on Slack, like Discord is the next big thing.

[08:30 - 08:39] So you make a Discord bot, and the UI is also much better than Slack, so we made a Discord bot and we started a small Discord server.

[08:39 - 08:49] And it was pretty funny, entertaining, whoever joined the server and tried out the bot, they would be like, oh, this is so much better than Google, I would use it every day.

[08:49 - 08:59] And we didn't initially believe that, we thought okay they're just saying it to be nice to us and be encouraging but they did actually keep using it so that gave us a lot of,

[08:59 - 09:09] You know, hope that this is actually something real. So note that this was still a time when we were working on our SQL enterprise stuff. So this was more like a distraction.

[09:09 - 09:24] So I wasn't sure what to do like us why are we even working on this there was always that question but one thing that's true is when something starts working that there is like a dopamine from constantly improving it when you see people asking for stuff and it's,

[09:24 - 09:35] You keep shipping and keeps getting better. You feel the momentum. So my cofounder, again, Dennis, added these focuses where you can search specifically about Wikipedia.

[09:35 - 09:44] And then you can search specifically on stack overflow, and it would answer all our coding queries like so much, so much better.

[09:44 - 09:54] And so there was something real here and this was exactly one day before Chantipuri launched and there was like, you know.

[09:54 - 10:05] Still not sure what we should be doing because we were working on, our company was supposed to be doing something else and we saw the Chad GPT launch, you know it's historic right now if you think about it.

[10:05 - 10:16] And then they broke several myths that you needed to be in Discord, like people don't want chatbots, like all sorts of things, they basically broke all the...

[10:16 - 10:32] existing wisdom at the time, so we were very encouraged by this and we thought we could still add orthogonal value to what they launched because we had this orchestration of combining live knowledge and the chatbot together.

[10:32 - 10:41] So this is again like Dennis asking Nick if he had a moment to help him with the CSS, because we don't know CSS.

[10:41 - 10:51] And then, funnily, I tried to generate the code for it with chat GPT, and then that broke, obviously.

[10:51 - 10:59] So then somehow Nick came and helped us, and then we sent it to one of our friendly investor friends, Daniel Gross.

[10:59 - 11:11] And if you look at his first comment, you need a submit button, because that was a joke, because the latency was so bad, it would take seven seconds or eight seconds to get the answer.

[11:11 - 11:19] And now if you use our product, it's almost instantaneous, so that's how many iterations it's come through.

[11:19 - 11:30] And he gave us a lot of good feedback, this is always very important, get your first users who like your product, and then we had this whole thing ready, we were going to launch it,

[11:30 - 11:42] And then we got the bravery to launch it, NatFeedman was like, go get a hundred people, you know, like a hundred people to use your product, and so we launched it, and it went really way better than expectations.

[11:42 - 11:54] And this was sort of the beginning when we decided, okay, fine, we had this whole SQL search for enterprises, we had prototyped it on some large.

[11:54 - 12:04] Relational databases. So we thought, like, we might as well release something like a public database powered SQL search and test which one actually works. Was it the Web search or the SQL search.

[12:04 - 12:19] So we launched the search over Twitter, like which actually got, you know, like Jack Dorsey himself to come in and code tweet us saying this is great and that got a lot more eyes on perplexity and people started using both products.

[12:19 - 12:31] We tracked the usage and we saw that the regular web search product got a lot more usage, we were still confused whether we should kill this Twitter search or not, but Elon made it easy for us by,

[12:31 - 12:44] changing the API prices to something so high that nobody can pay anymore except Google, so we decided to just focus on web search, and we made it better, we made it fully end to end conversational,

[12:44 - 12:53] We suggested follow up questions and then like, you know, I think one thing that, you know, Nat was gracious enough to say is that.

[12:53 - 13:02] We ship really fast, that's basically our identity almost, some people give us a lot more credit than we deserve, but I think...

[13:02 - 13:15] That's the only way in which we survived this whole competition with Microsoft and Google trying to do all these same things, so we kept iterating, improving from January onwards, tried many, many experiments.

[13:15 - 13:23] And then the next big update was launching this thing called Copilot, which we consider as like a browsing companion, right?

[13:23 - 13:33] So the way it works is, until now, you just ask a question, and the AI plugs into a search index, gets the answers.

[13:33 - 13:43] And gives it to you in a direct chatbot UI. We thought it would be cool if it's more agentic and comes back to you.

[13:43 - 13:58] ask some clarifying questions, and then like gives you the answer, and the clarifying questions it generates is very question dependent, it's very dynamic, and the kind of questions it asks can be like multiple choice or single choice,

[13:58 - 14:13] So we innovated on this new thing called generative UI, like the, based on your query, a user interface is generated according to it, and Versailles is doing great work now on like, you know, trying to generate websites based on what you want.

[14:13 - 14:20] So we had this idea way before and sort of inspired by all the noise around AutoGPT and baby AGI at the time.

[14:20 - 14:29] But our thesis was that autonomy is not there yet. We still want these agents to work, along with us.

[14:29 - 14:41] So we designed the product that way, and this sort of basically became our, you know, USP of our pro plan, and people use the pro plan for like the copilot basically for like more,

[14:41 - 14:52] Research on steroids, that's the best way to think about it, and then we made it even faster recently with OpenAI's GBT 3.5 fine tuning API.

[14:52 - 15:04] So on the left you see the fine tuned GPT 3.5 model that's running Copilot, on the right you see GPT four, so GPT four asks you like more questions but,

[15:04 - 15:17] Not all of them are needed, GPT 3.5 is much faster and just directly just gets to the core point, so ideally we want something that would have the brain of GPT four and asking clarifying questions.

[15:17 - 15:27] But the speed and the reliability of GPD 3.5 in terms of user experience, so that's what we tried with this fine tuned model.

[15:27 - 15:37] And in terms of metrics, if you just look at our FTGPD 3.5 is the fine tuned model, and GPT four and three point five are the original models.

[15:37 - 15:49] Eighty percent of the time the user is unable to say which model is which, and eight percent it's like they think the fine tuned model is better, and eleven percent they think the GP four is still better.

[15:49 - 15:59] So there's still some room for improvement. But this is going to go more towards, like, you know. The user being unable to say, and in terms of Gpd for us.

[15:59 - 16:07] Like fine-tune versus just the original GBT 3.5, you can clearly see that it's winning a lot more compared to like, you know.

[16:07 - 16:17] Without fine tuning. And there's a reason we do that. This is because the price you pay for output tokens is.

[16:17 - 16:29] you know, not even comparable, right, like for example if you look at the input tokens, the prompt tokens, you're paying 3x lower for GBT 3.5 compared to four and for the output tokens the generated tokens,

[16:29 - 16:38] You're paying six X lower, so this said the volume of search requests we serve every day makes a ton of difference to us.

[16:38 - 16:48] And also in terms of speed, you can see the throughput here and the latency here, it's like day and night difference, right?

[16:48 - 16:58] All this makes for a better product experience, like when you're using on your phone with crappy Wi-Fi or you're on your mobile internet.

[16:58 - 17:08] These things matter a lot, so we thought through a lot of this, took the opportunity when OpenAI had the fine tuning API available and shipped this much faster.

[17:08 - 17:19] And other people and yeah this got the appreciation of the man himself he came said great use of metrics the open AI fine tuning API.

[17:19 - 17:29] And yeah, so we also support other research use cases in the product, like we let people upload files, and Cloud too is very much.

[17:29 - 17:40] appreciated and known for its long context and you know file upload feature, so we didn't just do file upload because so it'll be cool to just add another feature.

[17:40 - 17:50] R goes to be the best research assistant anybody can have, and uploading your files and asking questions about it is like one very essential component of any.

[17:50 - 17:59] Research workflow, right, so we just did this and we thought cloud two has much better capabilities here compared to GPT four.

[17:59 - 18:06] So we worked together with Anthropik and made this happen, and this also got a lot of positive attention for us.

[18:06 - 18:16] So recently we launched this thing called Collections, where this is our transition from moving from just a tool to an end to end platform.

[18:16 - 18:24] Where you can, instead of just pasting our URL somewhere and being scattered around your Slack or WhatsApp or like.

[18:24 - 18:40] your email somewhere, we just thought it would be nice if it's all like persistent and like saved somewhere and you can collaborate with people and you can also have your own privacy levels in terms of what you want to share publicly and keep it private.

[18:40 - 18:50] So if you want to have like one set of collections for your like, you know, planning your holiday trip with your friends or family, then that's different from having another set of collections where,

[18:50 - 19:00] You're just doing research on companies or you're having like coding queries about some new framework that you're learning. All of these can be like, you know, decouple, right.

[19:00 - 19:09] So this is sort of becoming more like a platform than just the tool, and that's very important because we see this as a way to truly differentiate ourselves.

[19:09 - 19:18] Have people coming back to using the product every day. So this is something that we'll be doing more of in the coming months.

[19:18 - 19:25] And this thing I want to like, you know, I've said this before, there's a lot of like, you know.

[19:25 - 19:36] Different opinions on whether being a rapper versus training your own model, what is respected more, or what's needed for a startup.

[19:36 - 19:50] And there's this code from this Steve Jobs movie where Wozniak basically asks him, what do you actually do, you don't do the hardcore engineering, and he says, I play the orchestra.

[19:50 - 19:59] And orchestration, like orchestrating different components, search index, LLM, conversational.

[19:59 - 20:09] Rendering the answer, multimodal, it's not easy, it takes a lot of work, even in being a rapper, like if you do decide to be a rapper, you might as well be a good rapper, right?

[20:09 - 20:18] And then devil is in the details. And so, for example, I was telling about the Bard extension story on Twitter.

[20:18 - 20:26] And I tried like, hey, I'm just going to see if this works, maybe I'm wrong about orchestration, and I just asked how many flights they had taken in the last two months.

[20:26 - 20:39] It doesn't even plug into my Gmail to give me the answer, and then there's a user here coming and replying to me saying that when working with documents, perplexity gives way better answers.

[20:39 - 20:50] Without hallucinations and then similarly this is another product called UChat and then I don't even like try to game it I only pick the query they suggested.

[20:50 - 20:59] Write a song about whales in the ocean and then it gives me a weather reject, like I didn't ask about the weather, right?

[20:59 - 21:11] It's very easy to say, oh yeah, we connected to all these plugins, we connected to all these APIs, data providers, and then when you try it, it does something unreliable at inference time.

[21:11 - 21:20] So that's why we are being more careful here and trying to do it with thought, like for example, Stanford evaluated.

[21:20 - 21:30] All these generative search engines and like you have two axes here, one is perceived utility and the other is the citation F one score.

[21:30 - 21:41] FN score is just a weighted average of precision and recall, and you want to be good on both, that is you want to have a high citation score so that,

[21:41 - 21:51] You're backing up what you say in the answer with the relevant links, and you also want to be having high utility scores so that your answer is readable to the user and makes for a good experience.

[21:52 - 22:04] And so you want to be as far as possible in the top right corner and not too much on like, you know, only on Y axis or X axis, and you look at it like we were the best product out of all four.

[22:04 - 22:13] At the time of publication of this paper, and this was at a time when we were only using GPD 3.5 and Bing was using GPD four as default.

[22:13 - 22:21] If we rerun the evaluations with the current model, which is much better, I'm sure we'll score even better on these metrics.

[22:21 - 22:31] And so people are seeing that, and these days people are tweeting about it, at the time we raised funding.

[22:31 - 22:39] It was exactly the time Bing was launched, and we ourselves had a lot of fear, leave alone people around us scaring us.

[22:39 - 22:55] Like why are you working on something Microsoft's gonna win here, but I think what we learned over these months is that it's not just about one launch, you got to keep on iterating and keep on improving and users will eventually realize like the better product.

[22:55 - 23:05] So even now it's not like, oh, like you don't need to think like this guy's thinking he's already ahead, but you know, like we fully understand, we kind of have to keep improving the product.

[23:05 - 23:15] But the most important part is establishing the platform, the flywheel, the infra, and the iteration component, so that's what we are very happy about doing so far.

[23:16 - 23:29] And this is like a good summary of like what, you know, how to best interpret R2, it's basically like Wikipedia and Chanche Piti had a baby, but the data is not just Wikipedia, it's from the entire internet.

[23:29 - 23:37] So it's perfect tool for doing a deep dive on any topic, it's built for people like you, we're all like...

[23:37 - 23:47] We're interested in diving deep and digging into rabbit holes, so that's the idea, it should excite people like you to use these products.

[23:47 - 23:55] And additionally, we also took this feedback that we don't want to just be a rapper.

[23:55 - 24:04] So we are trying to serve our own models too, and with that in mind, we first launched Lama models as part of perplexity labs.

[24:04 - 24:14] Which is the fastest inference Lama right now among any other products like hugging phase replicate.

[24:14 - 24:24] So many other people are also serving Lama models, but in terms of metrics, we publish our metrics and you can actually see the tokens per second, time to first token.

[24:24 - 24:33] Everything, right, so we have the best latency and I think this person also evaluated it.

[24:33 - 24:46] so many other people and realize like we are functioning the best, so actually I want to do a demo of a model that we just launched today in the perplexity labs,

[24:46 - 24:56] It's called Lama 213B SFT, so this is a step towards us training our own models too, not just serving Meta's models.

[24:56 - 25:04] So if you remember, Lama got a lot of criticism for having...

[25:04 - 25:12] Like basically being super annoying to use, it will just not obey our instructions.

[25:12 - 25:21] It's just too safe, right, and then we decided, okay, that's a good fine tuning step towards, you know, if you go back to the.

[25:21 - 25:27] Original lama. And ask it to do the same thing. It's not going to answer you. All these things.

[25:27 - 25:32] So if you ask it like how to kill Linux process.

[25:32 - 25:42] It's just going to tell you I'm programmed to be the safety and well-being of people, I can't tell you how to do it, all these kind of things, or it's not going to give you,

[25:42 - 25:52] Jokes that you want, or jokes about any person, and we decided that we'd at least try to fine tune these models to be more useful rather than.

[25:52 - 25:59] Going too much in the direction of harmlessness and so this is an experiment we are trying out and.

[25:59 - 26:09] We expect to update people more on our own models and start serving our own models through the product. So right now, already in perplexity.

[26:09 - 26:17] You're getting this, you know, if you're on the pro plan, you can pick your models of choice, like we have our own models, that's GPT four, that's CLOT two.

[26:17 - 26:29] And I think over time, the model that we serve will be the best suited for this particular product, and we also expect people not to be...

[26:29 - 26:37] People probably won't care enough to just pick the models of their choice, but just have one model that just works.

[26:37 - 26:42] And that's our goal, that's why we are trying all these experiments to train and serve our own models.

[26:43 - 26:51] Yeah, so that's basically it, I think I have some time for questions.

[27:01 - 27:06] Yeah.

[27:07 - 27:14] So where are you using ray here, where is the usage of ray?

[27:14 - 27:24] Are you using Ray, any part of Ray training or... Yeah, so we considered using it for fine tuning models.

[27:24 - 27:34] And we are currently testing our own infrastructure based on Megatron and any scales fine tuning.

[27:34 - 27:42] So we'll have something to say there soon, nothing in production, nothing we can announce publicly yet.

[27:42 - 27:52] Okay, thank you, and also the citations, right, you pointed the paper, I'm user of both of you, u.com and Perplexity.

[27:52 - 28:05] So they're also improving, I see both are equal now, so what's your roadmap of coping up with that competition, now both are equal because on the same data set which Stanford, because I'm a Stanford student.

[28:05 - 28:15] And then the same. And both are equal now. So what's your road map ahead? I mean, you can share your results with us. I don't think both are equal, but if it's true, then we'll.

[28:15 - 28:20] I can comment on it more, sure, sure, thank you.

[28:24 - 28:29] First.

[28:32 - 28:43] Hey, been using perplexity for quite some time. Thanks for building it. I've often noticed that when I ask a question, the citations that come up on perplexity.

[28:43 - 28:52] Are much higher quality than the ones I get on Google. Google still ranking the Seo articles a lot more, given that you're still searching the Internet, finding those data points out.

[28:52 - 29:04] How are you maintaining the authenticity of the links that you used to Yeah, so we have our own page ranks of the web, and we also have the LLMs are so good at,

[29:04 - 29:15] Picking the right relevant links, so the final component of LLMs picking which papers, which links to cite is.

[29:15 - 29:21] Is actually like a big gain in relevance ranking, so that's also very useful.

[29:21 - 29:31] Thank you Yeah, I had a question, what are the trade offs you had to make to get Lama running so fast, because it seems pretty fast.

[29:31 - 29:41] Yeah, so we basically have our own custom inference stack that's, you know, we obviously look at everything that's.

[29:41 - 29:49] Helping others like flash attention or using facet transformer, page detention, all these different ideas.

[29:49 - 30:00] But we decided to use our own stack rather than relying on hugging phase or like VLLM because that way we can control more.

[30:00 - 30:12] And yeah, so I would say just at some point you just have to go and write stuff at the level of Cura, right?

[30:12 - 30:16] Or else it's pretty hard to make things much faster.

[30:25 - 30:42] I think you spoke a little bit about the model that you are customizing your own models, how are you in a larger space context, how are you seeing the role of open source, do you imagine you would be going down that route more and more away from chatGPT or you'll still be using cloud or chatGPT?

[30:42 - 30:50] Yeah, so I think there's competition between GPD 3.5 fine tuning and open source.

[30:50 - 31:01] Models, right, like when we thought okay Lama's great and we would rather just fine tune Lama then OpenAI also announced GBT 3.5 fine tuning.

[31:01 - 31:10] And so if our goal is to just make the product better, we would do the thing that's cheaper and easier to do in the short term.

[31:10 - 31:18] That said, I still think there are some things you just cannot do without having access to the weights.

[31:18 - 31:26] And maybe some of this could just be the style of the response.

[31:26 - 31:35] And if you want to make the LLMs more customizable, more agentic, all these sort of things, I think it helps to have your own model.

[31:35 - 31:45] Plus, you don't control the pricing, right, that's the most important part, like leaving aside the technical, and just think about it from the business perspective.

[31:45 - 31:52] Like if you don't control the pricing of something, it's always in a tricky position to be.

[31:52 - 32:02] And it's unclear if pricing of all these APIs will keep remaining the way it is today, or it'll go down or go up.

[32:02 - 32:06] So it's good for you to have your own stuff.

[32:08 - 32:16] I think it'll definitely catch up to GPT four by like mid next year.

[32:16 - 32:22] But by the time maybe they launch GPT-5, so there will be some delay, I think.

[32:22 - 32:30] Sorry we couldn't get around to all the questions, but let's give Arvind another round of applause.


