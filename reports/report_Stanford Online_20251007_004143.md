# 视频翻译处理报告

## 视频信息
- 视频标题：Stanford CS336 Language Modeling from Scratch I 2025
- 频道/发布者：Stanford Online
- 发布日期：未知
- 视频长度：unknown
- 视频分类：未分类
- 视频ID：PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_
- 观看链接：[点击观看原视频](https://www.youtube.com/watch?v=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_)
- 原始语言：en
- 目标语言：中文

![视频缩略图](https://i.ytimg.com/vi/PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_/maxresdefault.jpg)


## 处理统计
- 处理时间：2025-10-07 00:41:43 至 2025-10-07 00:41:43
- 音频提取耗时：2分36秒
- 转录耗时：2分42秒
- 翻译耗时：17分26秒
- 内容章节数：1
- 总字数（原文）：11233
- 总字数（译文）：879


## 内容概览

### 视频主题摘要
<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">
该课程旨在从零开始教授语言模型的构建，涵盖数据处理、模型架构、系统优化及训练全流程。讲师强调理解底层技术的重要性，以应对当前AI研究中对抽象工具的过度依赖。课程内容包括实现分词器（如BPE）、Transformer架构、并行计算、推理优化及数据预处理等，并通过五个递进式作业帮助学生掌握核心技能。重点在于培养对效率、规模法则和系统设计的深刻理解，使学生能在有限资源下构建高效模型。所有讲座与材料公开，鼓励动手实践与深度探索。
</div>


## 关键观点

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">

**1.** 从零开始构建语言模型有助于深入理解技术本质，促进基础研究与创新。

**2.** 当前前沿模型因规模庞大和闭源特性，对多数研究者而言已变得遥不可及。

**3.** 小规模模型可能不具备代表性，其优化方向未必适用于大规模系统的实际需求。

**4.** 效率是核心驱动力，算法优化与硬件利用率在资源受限环境下尤为关键。

**5.** 课程通过数据、系统、建模与对齐四大支柱，培养从底层实现到全局设计的综合能力。

</div>



## 完整对照翻译

**00:00:04 - 00:00:06**  
原文：Welcome, everyone.  
译文：欢迎大家。  

**00:00:06 - 00:00:11**  
原文：This is cs 336 language models from scratch.  
译文：这是cs 336从零开始的语言模型。  

**00:00:11 - 00:00:12**  
原文：And this is the core staff.  
译文：而这就是核心员工。  

**00:00:12 - 00:00:15**  
原文：So I'm Percy, one of your instructors.  
译文：所以我是Percy，你们的讲师之一。  

**00:00:15 - 00:00:27**  
原文：I'm really excited about this class because it really allows you to see the whole language modeling building pipeline end to end, including data systems and modeling tattoo.  
译文：我真的很期待这门课，因为它真的让你能够从头到尾看到整个语言模型构建流程，包括数据系统和建模过程。  

**00:00:27 - 00:00:31**  
原文：I'll be co teaching with him, so I'll let everyone introduce themselves.  
译文：我将和他一起授课，所以我会让大家自我介绍一下。  

**00:00:31 - 00:00:32**  
原文：Hi everyone.  
译文：大家好。  

**00:00:32 - 00:00:32**  
原文：I'm pu.  
译文：我是pu。  

**00:00:32 - 00:00:34**  
原文：I' M1 of the co instructors.  
译文：我' M1 是其中一位联合讲师。 

注：这里的'M1'看起来像是原文中的一个特定标识或名称，所以在翻译时保持了原样。如果有其他上下文信息表明'M1'应该被翻译或解释，请提供更多信息。  

**00:00:34 - 00:00:37**  
原文：I'll be giving lecture in a week or two, probably few weeks.  
译文：我将在一两周内，可能几周后，进行讲座。  

**00:00:37 - 00:00:39**  
原文：I'm really excited about this class chricy.  
译文：我真的很期待这堂课，chricy。 

注：这里的"chricy"看起来像是一个名字或者特定的术语，因此在翻译时保持了原样。如果有更多上下文信息，可能会有助于更准确地理解和翻译这个词。  

**00:00:39 - 00:00:46**  
原文：And I, you know, spent a while being able to disgruntle thinking, like, what's the really deep technical stuff that we can teach our students today?  
译文：而我呢，你知道，花了一段时间在烦恼思考，就像，我们今天能教给学生的真正深入的技术知识是什么呢？  

**00:00:46 - 00:00:51**  
原文：I think one of the things that is really you goto build it from scratch to understand it.  
译文：我认为真正需要做的一件事是从零开始构建它，以便理解它。  

**00:00:51 - 00:00:53**  
原文：So I'm hoping that that's sort of the ether.  
译文：所以我希望那大概就是以太。  

**00:00:57 - 00:01:02**  
原文：And roi actually failed this class when I took it.  
译文：而且我实际上在上这门课的时候挂科了。  

**00:01:13 - 00:01:23**  
原文：PhD students in the cs department or with tattoo and a, I'm mostly interested the search line and synthetic data and language models reasoning for that stuff.  
译文：计算机科学系的博士生，或者有纹身的，我主要对搜索线、合成数据以及语言模型的推理感兴趣。  

**00:01:23 - 00:01:25**  
原文：So Yeah, it should be up on the board.  
译文：所以，是的，它应该已经显示在板上了。  

**00:01:25 - 00:01:26**  
原文：Hey guys, I' M Marcel.  
译文：嘿，大家好，我是马塞尔。  

**00:01:26 - 00:01:28**  
原文：I'm a second European team.  
译文：我是一支欧洲的第二队伍。  

**00:01:28 - 00:01:29**  
原文：I work.  
译文：我工作。  

**00:01:33 - 00:01:39**  
原文：And he was a topper of many leaderboards from last year, so he's the number to beat.  
译文：而他去年在很多排行榜上都是名列前茅的，所以他是要击败的目标。  

**00:01:39 - 00:01:40**  
原文：Okay, all right.  
译文：好的，行。  

**00:01:40 - 00:01:41**  
原文：Well, thanks, everyone.  
译文：好的，谢谢大家。  

**00:01:41 - 00:01:42**  
原文：So let's continue.  
译文：那么让我们继续。  

**00:01:42 - 00:01:47**  
原文：As Hato mentioned, this is the second time we're teaching the class.  
译文：正如Hato提到的，这是我们第二次教这门课。  

**00:01:47 - 00:01:50**  
原文：We've thrown the class by around 50%.  
译文：我们将课程减少了大约50%。  

**00:01:50 - 00:01:52**  
原文：I have three tas instead of two.  
译文：我有三个任务而不是两个。  

**00:01:52 - 00:02:01**  
原文：And one big thing is we're making all the lectures on YouTube so that the world can learn how to build language models from scratch.  
译文：而且一件大事是我们正在将所有的讲座上传到YouTube上，以便全世界都能学习如何从零开始构建语言模型。  

**00:02:01 - 00:02:01**  
原文：Okay?  
译文：好的？  

**00:02:01 - 00:02:07**  
原文：So why do we decide to make this a course and endure all the pain?  
译文：那么，我们为什么决定开设这门课程并忍受所有的痛苦呢？  

**00:02:07 - 00:02:08**  
原文：So let's ask GPT -4.  
译文：那么让我们来问问GPT-4。  

**00:02:08 - 00:02:15**  
原文：So if you ask it, why teach a course on building language models from scratch?  
译文：所以如果你问，为什么教授一门从零开始构建语言模型的课程？  

**00:02:15 - 00:02:26**  
原文：The reply is, teaching your course provides foundational understanding of techniques, fosters innovation, kind of the typical kind of generic bladders.  
译文：回复是，教授您的课程提供了技术的基础理解，促进了创新，有点像是典型的通用框架。 

注：原文中的"generic bladders"直译为“通用膀胱”，但在此上下文中可能是指“通用框架”或“通用结构”。如果"bladders"在特定上下文中具有其他含义，请提供更多信息以便更准确地翻译。  

**00:02:26 - 00:02:27**  
原文：Okay?  
译文：好的？  

**00:02:27 - 00:02:29**  
原文：So here's a real reason.  
译文：所以这里有一个真正的原因。  

**00:02:29 - 00:02:32**  
原文：So we're in a bit of a crisis.  
译文：所以我们遇到了一点危机。  

**00:02:32 - 00:02:41**  
原文：I would say researchers are being coming in more and more disconnected from the underlying technology.  
译文：我会说研究人员与底层技术之间的联系越来越脱节。  

**00:02:41 - 00:02:46**  
原文：Eight years ago, researchers would implement and train their own models in AI.  
译文：八年前，研究人员会自己实现并训练他们的人工智能模型。  

**00:02:46 - 00:02:52**  
原文：Even six years ago, you at least take the models like burr, download them and fine tune them.  
译文：即使在六年前，你至少也会采取像burr这样的模型，下载它们并进行微调。  

**00:02:52 - 00:02:57**  
原文：And now many people can just get away with prompting a proprietary model.  
译文：而现在许多人只需通过提示一个专有模型就能达到目的。  

**00:02:57 - 00:03:00**  
原文：So this is not necessarily bad, right?  
译文：所以这不一定不好，对吧？  

**00:03:00 - 00:03:05**  
原文：Because as you enter these layers of abstraction, we can all do more.  
译文：因为当你进入这些抽象层次时，我们都能做得更多。  

**00:03:05 - 00:03:11**  
原文：And a lot of research has been unlocked by the simplicity of being a prompter language model.  
译文：而且，作为提示语言模型的简单性已经解锁了大量的研究。  

**00:03:11 - 00:03:14**  
原文：And I do a fair my share of prompting.  
译文：而我也做了相当一部分的提示。  

**00:03:14 - 00:03:16**  
原文：So there's nothing wrong with that.  
译文：所以那没什么不对的。  

**00:03:16 - 00:03:19**  
原文：But it's also remember that these abstractions are leaky.  
译文：但也要记住，这些抽象是有缺陷的。  

**00:03:19 - 00:03:27**  
原文：So in contrast, the programming languages or operating systems, you don't really understand what the abstraction is.  
译文：所以在对比之下，对于编程语言或操作系统，你其实并不真正理解抽象是什么。  

**00:03:27 - 00:03:30**  
原文：It's a string in and string out, I guess.  
译文：这大概是一个字符串进，一个字符串出。  

**00:03:30 - 00:03:41**  
原文：And I would say that there's still a lot of fundamental research to be done that require tearing up the stack and co designing different aspects of the data and the systems and the model.  
译文：我会说仍然有很多基础研究需要进行，这些研究需要打破现有架构，并共同设计数据、系统和模型的不同方面。  

**00:03:41 - 00:03:48**  
原文：And I think really, that full understanding of the technology is necessary for fundamental research.  
译文：我认为，真正全面理解技术对于基础研究是必要的。  

**00:03:48 - 00:03:50**  
原文：So that's why this class exists.  
译文：所以这就是这个班级存在的原因。  

**00:03:50 - 00:03:54**  
原文：We want to enable the fundamental research to continue.  
译文：我们希望使基础研究能够继续进行。  

**00:03:54 - 00:03:58**  
原文：And our philosophy is to understand it, you have to build it.  
译文：而我们的理念是，要理解它，你必须构建它。  

**00:03:59 - 00:04:07**  
原文：So there's one small problem here, and this is because of the industrialization of language models.  
译文：所以这里有一个小问题，这是由于语言模型的工业化造成的。  

**00:04:07 - 00:04:15**  
原文：So GPT -4 has rumored to be 1.8 trillion parameters, cost hundred million dollars to train.  
译文：所以GPT-4据传有1.8万亿参数，训练成本高达数亿美元。  

**00:04:15 - 00:04:29**  
原文：You have xi building the clusters with 200 zero H -100s, if you can imagine that there's an investment of over 500 billion, supposedly over four years.  
译文：你有希望建立由200台零H-100组成的集群，如果可以想象的话，这将是一项超过5000亿的投资，据说是在四年以上的时间内完成。  

**00:04:29 - 00:04:33**  
原文：So these are pretty large numbers, right?  
译文：所以这些都是相当大的数字，对吧？  

**00:04:33 - 00:04:39**  
原文：And Furthermore, there's no public details on how these models are being built here from GPT -4.  
译文：此外，关于这些模型是如何从GPT-4构建的，没有公开的细节。  

**00:04:39 - 00:04:41**  
原文：This is even two years ago.  
译文：这甚至是两年前的事情了。  

**00:04:41 - 00:04:50**  
原文：They very honestly say that due to the competitive landscape and safety limitations, we're going to disclose no details.  
译文：他们非常诚实地表示，由于竞争环境和安全限制，我们将不会披露任何细节。  

**00:04:50 - 00:04:55**  
原文：So this is the state of the world right now.  
译文：所以，这就是现在世界的状态。  

**00:04:55 - 00:05:00**  
原文：And so in some sense, frontier models are out of reach for us.  
译文：因此，在某种意义上，前沿模型对我们来说是遥不可及的。  

**00:05:00 - 00:05:11**  
原文：So if you came into the supply thinking you're each going to train your own GPT for sorry, so we're going to build small language models.  
译文：所以如果你一开始以为每个人都要自己训练一个GPT，对不起，我们要做的是构建小型语言模型。  

**00:05:11 - 00:05:16**  
原文：But the problem is that these might not be representative.  
译文：但问题在于这些可能不具备代表性。  

**00:05:16 - 00:05:20**  
原文：And here's some of two examples to illustrate why.  
译文：以下有两个例子来说明原因。  

**00:05:20 - 00:05:24**  
原文：So here's this kind of a simple, simple one.  
译文：所以这是一个非常简单、简单的例子。  

**00:05:24 - 00:05:33**  
原文：If you look at the fraction of flops spent in the tension layers of a transformer versus a mlp, this changes quite a bit.  
译文：如果你看看在变压器的张力层与MLP中所花费的浮点运算比例，这个比例变化相当大。 

注：这里的“tension layers”直译为“张力层”，但在技术语境中可能指的是某种特定类型的层（如注意力机制层），具体翻译需根据上下文确定。同样，“flops”是“floating point operations per second”的缩写，意指每秒浮点运算次数，在中文里通常直接使用“浮点运算”来表示。  

**00:05:33 - 00:05:37**  
原文：So this is a tweet from Stephen roler from quite a few years ago.  
译文：所以这是Stephen roler几年前的一条推文。  

**00:05:37 - 00:05:48**  
原文：But this is still, if you look at small models, it looks like the number of flops in the attention versus if mlp layers are roughly comparable.  
译文：但如果你看看小型模型，会发现注意力机制中的浮点运算次数与MLP层中的大致相当。  

**00:05:48 - 00:05:54**  
原文：But if you go up to 175 billion, then the mlps really dominate, right?  
译文：但是如果你增加到1750亿，那么MLP（多层感知器）真的就占主导地位了，对吧？  

**00:05:54 - 00:05:56**  
原文：So why does this matter?  
译文：那么为什么这很重要？  

**00:05:56 - 00:06:04**  
原文：Well, if you spend a lot of time at small scale and you're optimizing the tension, you might be optimizing the wrong thing.  
译文：嗯，如果你在小规模上花费了大量时间并且一直在优化张力，那么你可能在优化错误的东西。  

**00:06:04 - 00:06:08**  
原文：Because at larger scale, it doesn't it gets to get swashed out.  
译文：因为在更大规模下，它不会被冲淡。 

注：原文中的“it doesn't it gets to get swashed out”可能存在语法错误或表述不清，直译可能无法准确传达原意。上述翻译是基于理解句子可能想要表达的意思进行的调整。如果需要严格按照字面意思翻译，请告知。  

**00:06:08 - 00:06:15**  
原文：This is kind of a simple example because you can literally make this plot without actually any compute.  
译文：这算是一个简单的例子，因为你实际上不需要任何计算就可以绘制出这个图表。  

**00:06:15 - 00:06:18**  
原文：You just like do it's napkin math.  
译文：你就像做餐巾纸上的计算一样。  

**00:06:18 - 00:06:24**  
原文：Here's something that's a little bit harder to grapple with, is just emergent behavior.  
译文：以下这个概念有点难以理解，那就是涌现行为。  

**00:06:24 - 00:06:28**  
原文：So this is a paper from Jason wafrom 2022.  
译文：所以这是一篇来自Jason的2022年的论文。  

**00:06:28 - 00:06:42**  
原文：And here this plot shows that as you increase the amount of training flops and you look at accuracy on a bunch of tasks, you'll see that for a while it looks like the accuracy, nothing is happening.  
译文：而这里这个图表显示，当你增加训练FLOPs的数量，并观察一堆任务上的准确性时，你会发现有一段时间看起来准确性没有什么变化。  

**00:06:42 - 00:06:48**  
原文：And all of a sudden you get these kind of Mergent of various phenomena in context learning.  
译文：然后突然之间，你会在上下文学习中看到各种现象的融合。  

**00:06:48 - 00:06:58**  
原文：So if you were hanging around at this scale, you would be concluding that, well, these language models really don't work, when in fact, you had to scale up to get that behavior.  
译文：所以，如果你在这个规模上徘徊，你可能会得出这样的结论：这些语言模型实际上并不起作用，而事实上，你需要扩大规模才能得到那种表现。  

**00:06:58 - 00:07:07**  
原文：So don't despair that we can still learn something in this class, but we have to be very precise about what we're learning.  
译文：所以不要灰心，我们仍然可以在这门课上学到一些东西，但必须非常精确地知道我们要学什么。  

**00:07:07 - 00:07:09**  
原文：So there's three types of knowledge.  
译文：所以有三种类型的知识。  

**00:07:09 - 00:07:12**  
原文：There's the mechanics of how things work.  
译文：有关于事物运作的机制。  

**00:07:12 - 00:07:13**  
原文：This we can teach you.  
译文：这我们可以教你。  

**00:07:13 - 00:07:16**  
原文：We can teach you what a transformer is.  
译文：我们可以教你什么是变压器。  

**00:07:16 - 00:07:19**  
原文：You you'll implement a transformer.  
译文：你将实现一个变压器。 

注：这里的“transformer”在不同上下文中可能有不同的含义，比如在机器学习中指的是“变换器”，而在电气工程中则指“变压器”。根据上下文选择最合适的翻译。如果是指机器学习中的模型，更准确的翻译应该是：“你将实现一个变换器。”  

**00:07:19 - 00:07:23**  
原文：We can teach you how model parallelism leverages GPU's efficiently.  
译文：我们可以教你如何通过模型并行有效地利用GPU。  

**00:07:23 - 00:07:27**  
原文：These are just kind of the raw ingredients, the mechanics.  
译文：这些只是原始的材料，机制。  

**00:07:27 - 00:07:28**  
原文：So that's fine.  
译文：那就好。  

**00:07:28 - 00:07:31**  
原文：We can also teach you mindset.  
译文：我们也可以教你心态。  

**00:07:31 - 00:07:51**  
原文：So this is something a bit more subtle and seems like a little bit you know fuzzy, but this is actually in some ways more important, I would say, because the mindset that we're going to take is that we want to squeeze as most out of the hardware as possible and take scaling seriously, right?  
译文：所以这有点更加微妙，看起来可能有些模糊，但实际上在某些方面来说，我认为这更为重要，因为我们要采取的思维方式是，我们希望尽可能地充分利用硬件，并且认真对待扩展性，对吧？  

**00:07:51 - 00:07:59**  
原文：Because in some sense, the mechanics, all of those we'll see later that all of these ingredients have been around for a while.  
译文：因为从某种意义上说，这些机制，我们稍后会看到所有这些元素其实已经存在一段时间了。  

**00:07:59 - 00:08:07**  
原文：But it was really, I think, the scaling mindset that OpenAI pioneered that led to this next generation of AI models.  
译文：但我觉得，真正引领这一代AI模型的是OpenAI开创的规模化思维。  

**00:08:07 - 00:08:14**  
原文：So mindset, I think hopefully we can bang into you that to think in a certain way.  
译文：所以心态，我希望我们能够让你形成某种思维方式。  

**00:08:14 - 00:08:16**  
原文：And the thirdly is intuitions.  
译文：而第三点是直觉。  

**00:08:16 - 00:08:21**  
原文：And this is about which data and modeling decisions lead to good models.  
译文：而这关乎哪些数据和建模决策能够导致好的模型。  

**00:08:21 - 00:08:25**  
原文：This, unfortunately, we can only partially teach you.  
译文：这很遗憾，我们只能部分地教你。  

**00:08:25 - 00:08:34**  
原文：And this is because what architectures and what data sets work at in most scmight not be the same ones that work at large scales.  
译文：而这之所以如此，是因为在大多数情况下有效的架构和数据集，在大规模情况下可能并不适用。  

**00:08:34 - 00:08:43**  
原文：And but you, that's just, but hopefully you got two and a half out of three, so that's pretty good being for your buck.  
译文：而你，就是这样，但希望你能得到三分之二点五，所以这对你来说已经相当不错了。 

注：这句话的翻译稍微有些不通顺，因为原文本身表达得也不是特别清晰。如果需要更准确或自然的中文表达，可能需要更多上下文来理解其具体含义。  

**00:08:43 - 00:09:01**  
原文：Okay, speaking of intuitions, there's this sort of, I guess, sad reality of things that, you know you can tell a lot of stories about why certain things in the transformer the way they are, but sometimes it's just you know come you do the experiments and the experiments speak.  
译文：好的，说到直觉，有这么一种，我猜，算是令人有点伤感的事实吧，你知道你可以讲述很多关于为什么变压器中的某些东西是这样的故事，但有时候就是你去做实验，而实验结果说明一切。  

**00:09:01 - 00:09:12**  
原文：So for example, there's this no Shazo paper that introduced the swiggluo, which is something that we'll see a bit more in this class, which is a type of non linearity.  
译文：所以例如，有这样一篇No Shazo的论文介绍了swiggluo，这是我们在这门课中会更多见到的一种非线性类型。  

**00:09:12 - 00:09:17**  
原文：And in the conclusion, you know the results are quite good and this got adopted.  
译文：而在结论中，你知道结果相当不错，并且这一点得到了采纳。  

**00:09:17 - 00:09:25**  
原文：But in the conclusion there, this honest statement that we offer no explanation except for this is divine benevolence.  
译文：但在结论中，有这样一句诚恳的陈述：除了认为这是神的仁慈之外，我们没有提供任何解释。  

**00:09:25 - 00:09:26**  
原文：There you go.  
译文：好的，翻译如下：

这就行了。  

**00:09:26 - 00:09:29**  
原文：This is the extent of our understanding.  
译文：这是我们理解的范围。  

**00:09:29 - 00:09:35**  
原文：Okay, so now let's talk about this bitter lesson that I'm sure people have heard about.  
译文：好的，那么现在让我们来谈谈这个我相信大家都听说过的苦涩教训。  

**00:09:35 - 00:09:42**  
原文：I think there's a sort of a misconception that a bitter lesson means that scale is all that matters.  
译文：我认为有一种误解，认为惨痛的教训意味着规模就是一切。  

**00:09:42 - 00:09:43**  
原文：Algorithms don't matter.  
译文：算法并不重要。  

**00:09:43 - 00:09:48**  
原文：All you do is pump more capital into building the model, and you're good to go.  
译文：你只需要投入更多资金来构建模型，就可以开始了。  

**00:09:48 - 00:09:51**  
原文：I think this couldn't be farther from the truth.  
译文：我认为这与事实相去甚远。  

**00:09:51 - 00:09:57**  
原文：I think the right interpretation is that algorithms at scale is what matters.  
译文：我认为正确的解释是，大规模的算法才是关键。  

**00:09:57 - 00:10:07**  
原文：And because at the end of the day, your accuracy of your model is really a product of your efficiency and the number of resources you put in.  
译文：并且，归根结底，你的模型的准确性实际上是你的效率和你投入资源数量的产物。  

**00:10:07 - 00:10:19**  
原文：And actually, efficiency, if you think about it, is way more important at a larger scale, because if you're spending you know hundreds of millions dollars, you cannot afford to be wasteful.  
译文：实际上，效率如果你仔细想想，在更大规模上要重要得多，因为如果你花费的是数亿美元，你就不能承受浪费。  

**00:10:19 - 00:10:27**  
原文：In the same way that if you're looking at running a job on your on your local cluster, you might run it again.  
译文：同样地，如果你打算在本地集群上运行一个任务，你可能会再次运行它。  

**00:10:27 - 00:10:29**  
原文：You fail, you debug it.  
译文：你失败了，你就调试它。  

**00:10:29 - 00:10:38**  
原文：And if you look at actually the utilization and the use, I'm sure OpenAI is way more efficient than any of us right now.  
译文：而且如果你看看实际的使用情况和利用率，我相信OpenAI现在比我们任何一个人的效率都要高得多。  

**00:10:38 - 00:10:41**  
原文：So efficiency really is important.  
译文：所以效率真的很重要。  

**00:10:41 - 00:11:16**  
原文：And Furthermore, this, I think is this point is maybe not as well appreciated in the sort of scaling rhetoric, so to speak, which is that if you look at efficiency, which is a combination of hardware algorithms, but if you just look at the algorithm efficiency, there's this nice OpenAI paper from 2020 that showed over the period of 2012 to 2019, there's a 44x algorithmic efficiency improvement in the time that it took to train image that to a certain level of accuracy, right?  
译文：而且，我认为这一点在所谓的规模扩展的言论中可能没有得到充分的认识，即如果你看效率，这是硬件和算法的结合，但如果你只看算法效率，有一篇很好的OpenAI 2020年的论文显示，从2012年到2019年期间，训练图像达到一定准确度所需时间的算法效率提高了44倍，对吧？  

**00:11:16 - 00:11:17**  
原文：So this is huge.  
译文：所以这很重要。  

**00:11:17 - 00:11:23**  
原文：And I think if you I don't know if you could see the abstract here.  
译文：我认为如果你，我不知道你能否在这里看到摘要。  

**00:11:23 - 00:11:25**  
原文：This is faster than mores law, right?  
译文：这比摩尔定律还要快，对吧？  

**00:11:25 - 00:11:27**  
原文：So algorithms do matter.  
译文：所以算法确实很重要。  

**00:11:27 - 00:11:33**  
原文：If you didn't to have this efficiency, you would be paying 44 times more cost.  
译文：如果您没有这种效率，您将支付高出44倍的成本。  

**00:11:33 - 00:11:38**  
原文：This is for image models, but there's some results for language as well.  
译文：这是针对图像模型的，但也有适用于语言的一些结果。  

**00:11:38 - 00:11:38**  
原文：Okay?  
译文：好的？  

**00:11:38 - 00:11:48**  
原文：So with all that, I think the right framing or mindset to have is what is the best model one can build given a certain compute and data budget?  
译文：所以综合以上所述，我认为正确的框架或思维方式应该是：在给定的计算资源和数据预算下，能够构建出的最佳模型是什么？  

**00:11:48 - 00:11:48**  
原文：Okay.  
译文：好的。  

**00:11:48 - 00:11:56**  
原文：And this question makes sense no matter what scale you're at because you're sort of like it's accuracy per resources.  
译文：而这个问题无论你在什么规模下都是有意义的，因为这有点像是资源的准确性。  

**00:11:56 - 00:12:01**  
原文：And of course, if you can raise the capital and get more resources, you'll get better models.  
译文：当然，如果你能筹集到资金并获得更多资源，你将得到更好的模型。  

**00:12:01 - 00:12:06**  
原文：But as researchers, our goal is to improve the efficiency of the algorithms.  
译文：但作为研究人员，我们的目标是提高算法的效率。  

**00:12:06 - 00:12:07**  
原文：Okay?  
译文：好的？  

**00:12:07 - 00:12:08**  
原文：So maximize efficiency.  
译文：所以要最大化效率。  

**00:12:08 - 00:12:11**  
原文：We're going to hear a lot of that.  
译文：我们会经常听到这样的话。  

**00:12:12 - 00:12:12**  
原文：Okay.  
译文：好的。  

**00:12:12 - 00:12:22**  
原文：So now let me talk a little bit about the current landscape and a little bit of, I guess, know, obligatory history.  
译文：那么现在让我来谈谈当前的状况，以及一点点，我想说的，必要的历史。  

**00:12:22 - 00:12:26**  
原文：So language models have been around for a while now.  
译文：所以语言模型已经存在一段时间了。  

**00:12:26 - 00:12:33**  
原文：Going back to Shannon, who looked at language models, a way to estimate the entropy of English.  
译文：回到香农，他研究了语言模型，这是一种估计英语熵的方法。  

**00:12:33 - 00:12:45**  
原文：I think in AI, they really were prominent in nlp where they were a component of larger systems like machine translation, speech recognition.  
译文：我认为在人工智能领域，它们确实在自然语言处理方面非常突出，作为机器翻译、语音识别等更大系统中的一个组成部分。  

**00:12:45 - 00:13:02**  
原文：And one thing that's maybe not as appreciated these days is that if you look back in 2007, Google is training 30 large and ground m models, so five gram models over 2 trillion tokens, which is a lot more tokens than GPT -3.  
译文：而且现在可能没有被充分认识到的一点是，如果你回顾2007年，谷歌正在训练30个大型的基础模型，也就是五元模型，这些模型基于超过2万亿个词汇进行训练，这比GPT-3的词汇量要多得多。  

**00:13:02 - 00:13:07**  
原文：And it was only, I guess, in the last two years that we've gotten to that token count.  
译文：而我想，大概只是在过去的两年里，我们才达到了那个词汇量。  

**00:13:07 - 00:13:15**  
原文：But they were Ingram models, so they didn't really exhibit any of the interesting phenomena that we know of language models today.  
译文：但它们是Ingram模型，所以实际上并没有展现出我们今天所知的语言模型的那些有趣现象。  

**00:13:15 - 00:13:15**  
原文：Okay.  
译文：好的。  

**00:13:15 - 00:13:28**  
原文：So in the 2010S, I think a lot of you can think about this, a lot of the deep learning revolution happened, and a lot of the ingredients sort of kind of falling into place.  
译文：所以在2010年代，我认为你们中的许多人可以想到，许多深度学习的革命发生了，很多要素开始逐渐到位。  

**00:13:28 - 00:13:34**  
原文：So there was a first neural language model from jofrapenjo's group in bein 2003.  
译文：所以在2003年，jofrapenjo的团队提出了第一个神经语言模型。  

**00:13:34 - 00:13:36**  
原文：There was seek to seek models.  
译文：有寻求建立模型的尝试。 

注：原文中的句子结构不太常见，直译可能会影响理解。上述翻译是基于理解后的表达。如果需要严格按照原文格式翻译，可以译为：“有寻求去寻求模型。” 但这种表达在中文中较为生硬，不如前一种自然。  

**00:13:36 - 00:13:48**  
原文：This, I think was a big deal for how do you basically model sequences from ilia and Google folks, there's an atom optimizer, which still is used by the majority of people.  
译文：这，我认为对于如何从Ilia和Google的人员那里基本建模序列来说是一件大事，有一种原子优化器，至今仍被大多数人使用。  

**00:13:48 - 00:14:03**  
原文：Deating, over a decade ago, there's a tension mechanism which was developed in the context of machine translation, which then led up to the famous attention lneed or the aka the transformer paper.  
译文：十余年前，在机器翻译的背景下开发了一种张力机制，这最终促成了著名的注意力机制或被称为Transformer论文的诞生。 

注意：原文中"Deating"可能是笔误，没有明确的意思，这里翻译时未包含这个词。如果有其他具体的含义，请提供更多信息以便更准确地翻译。  

**00:14:03 - 00:14:05**  
原文：In 2017.  
译文：在2017年。  

**00:14:05 - 00:14:10**  
原文：People were looking at how to scale mixture of experts.  
译文：人们在研究如何扩展专家混合模型。  

**00:14:10 - 00:14:18**  
原文：There was a lot of work around late 2010s on how to essentially do model parallelism.  
译文：在2010年代末期，关于如何进行模型并行化有很多研究工作。  

**00:14:18 - 00:14:25**  
原文：And they were actually figuring out how you could train 100 billion prime demomodels.  
译文：而他们实际上是在研究如何训练1000亿个初级模型。  

**00:14:25 - 00:14:37**  
原文：They didn't train it for very long because these were like more systems work, but all the ingredients were kind of in place before by the time the 2020 came around.  
译文：他们没有训练很长时间，因为这些更像是系统工作，但到了2020年左右，所有的要素其实都已经准备好了。  

**00:14:37 - 00:14:54**  
原文：So I think one other trend, which was starting in lpu is the idea of these foundation models that could be trained on a lot of text and adapted to a wide range of downstream tasks.  
译文：所以我认为另一个趋势，从lpu开始，就是这些基础模型的想法，它们可以在大量文本上进行训练，并适应广泛的下游任务。  

**00:14:54 - 00:15:00**  
原文：So Elmo, Bert, T T five, these were models that were, for their time, very exciting.  
译文：所以Elmo、Bert、T T five，这些模型在它们那个时代是非常令人兴奋的。  

**00:15:00 - 00:15:08**  
原文：We kind of maybe forget how excited people were about things like Bert, but it a big deal.  
译文：我们可能有点忘记了人们对像Bert这样的事物有多么兴奋，但这确实是一件大事。  

**00:15:08 - 00:15:19**  
原文：And then I think, I mean, this is abbreviated history, but I think one critical piece of the puzzle is OpenAI just taking these ingredients.  
译文：然后我想，我的意思是，这虽然是简略的历史，但我觉得一个关键点是OpenAI只是采用了这些成分。  

**00:15:19 - 00:15:41**  
原文：You know they apply them very nice engineering and really kind of pushing on kind of the scaling laws, embracing it as know this is the kind of the mindset and that led to GPT two and GPT -3, Google obviously was in the game and trying to compete as well.  
译文：你知道他们应用了非常优秀的工程技术，并且真的在某种程度上推动了规模法则，接受这种思维方式，这导致了GPT-2和GPT-3的诞生。显然，谷歌也在这个领域参与竞争。  

**00:15:41 - 00:15:59**  
原文：But that sort of paved the way, I think, to another kind of line of work, which is these were all closed models, so models that weren't released and you can only access via api, but they were all Nova models.  
译文：但我觉得，这为另一种工作方式铺平了道路，这些都是一些封闭的模型，也就是说，这些模型没有公开发布，只能通过API访问，但它们都是Nova模型。  

**00:15:59 - 00:16:14**  
原文：Starting with your early work by Luther, right after GPT -3 came out, met a's early attempt, which didn't work, maybe as quite as well bloom, and then met ta Alibaba, deep seek AI too.  
译文：从你早期由Luther开始的工作，在GPT-3问世后不久，遇到了a的早期尝试，但效果不佳，可能并不如bloom那么好，然后遇到了阿里巴巴的deep seek AI。 

请注意，原文中的一些专有名词（如GPT-3, bloom, deep seek AI）在翻译时保持了原样。如果这些专有名词有特定的中文译名，请告知我以便更准确地翻译。  

**00:16:14 - 00:16:24**  
原文：And there's a few others which I elisted have been creating, these open models where that the weights are released.  
译文：还有其他一些我列出的正在创建的开放模型，这些模型的权重已经发布。  

**00:16:24 - 00:16:31**  
原文：One other piece of, I think, tibit about openness, I think, is important, is that there's many levels of openness.  
译文：另一点关于开放性，我认为很重要的是，开放性有很多层次。  

**00:16:31 - 00:16:34**  
原文：There's closed models like GPT -4.  
译文：有像GPT-4这样的闭源模型。  

**00:16:34 - 00:16:45**  
原文：There's open weight models where the weights are available and there's actually a paper, a very nice paper with lots of architectural details, but no details about the data set.  
译文：有开放权重的模型，其中权重是可用的，并且实际上有一篇非常好的论文，里面包含了很多架构细节，但没有关于数据集的细节。  

**00:16:45 - 00:16:56**  
原文：And then there's open source models where all the weights and data are available in the paper, where they're honestly trying to explain as much as they can.  
译文：然后还有开源模型，其中所有的权重和数据都在论文中提供，他们确实尽力解释了尽可能多的内容。  

**00:16:56 - 00:17:06**  
原文：But of course, you can't really capture everything in a paper, and there's no substitute for learning how to build it except for kind of doing yourself.  
译文：但当然，你不能真的在一篇论文中捕捉到所有东西，除了亲自动手实践之外，没有什么可以替代学习如何构建它。  

**00:17:06 - 00:17:06**  
原文：Okay.  
译文：好的。  

**00:17:06 - 00:17:25**  
原文：So that leads to kind of the present day where there's a whole host of frontier models from OpenAI, anthropic xai, Google, meta, dpsealibaba, Tencent, and probably a few others that are sort of dominate the current landscape.  
译文：因此，这就引到了当今的局面，其中有一系列前沿模型来自OpenAI、Anthropic、XAI、Google、Meta、阿里云、腾讯，以及其他可能的几家机构，这些模型在当前领域中占据主导地位。  

**00:17:25 - 00:17:44**  
原文：So we're kind of into this interesting time where, you know just to kind of reflect a lot of the ingredients, like I said, were developed, which is good because I think we're going to revisit some of those ingredients and trace how these techniques work.  
译文：所以我们正处在一个有趣的时期，你知道的，就像我所说的，很多要素已经被开发出来了，这是好事，因为我认为我们将重新审视这些要素，并追踪这些技术是如何运作的。  

**00:17:44 - 00:17:51**  
原文：And then we're going to try to move as close as we can to best practices on frontier models.  
译文：然后我们将尽量接近前沿模型的最佳实践。  

**00:17:51 - 00:18:02**  
原文：But using information from essentially the open community and reading between the lines from what we know about the closed models.  
译文：但是利用基本上来自开放社区的信息，并从我们对封闭模型的了解中读出言外之意。  

**00:18:02 - 00:18:03**  
原文：Okay.  
译文：好的。  

**00:18:03 - 00:18:08**  
原文：So just as an interlude, so what are you looking at here?  
译文：那么，作为插曲，你在这里看的是什么？  

**00:18:08 - 00:18:11**  
原文：So this is an executable lecture.  
译文：所以这是一个可执行的讲座。  

**00:18:11 - 00:18:19**  
原文：So it's a program where I'm stepping through and it delivers the content of lecture.  
译文：所以这是一个程序，我一步步进行，它提供讲座的内容。  

**00:18:19 - 00:18:25**  
原文：So one thing that I think is interesting here is that you can embed code.  
译文：所以我认为这里有趣的一点是你可以嵌入代码。  

**00:18:25 - 00:18:36**  
原文：So if you you can just step through code, and I think this is a smaller screen that I'm used to, but you can look at the environment variables as you're stepping through code.  
译文：所以你可以逐行执行代码，我觉得这个屏幕比我常用的要小一些，但你可以在逐行执行代码时查看环境变量。  

**00:18:36 - 00:18:38**  
原文：So that's useful.  
译文：所以那是有用的。  

**00:18:38 - 00:18:51**  
原文：Later, when we start actually trying to drill down and giving code examples, you can see the hierarchical structure of lecture, like we're in this module and you can see where it's it was called from main and you can jump to definitions.  
译文：稍后，当我们开始实际尝试深入并给出代码示例时，你可以看到讲座的层次结构，比如我们现在在这个模块中，你可以看到它从 main 函数被调用的地方，并且你可以跳转到定义。  

**00:18:51 - 00:18:57**  
原文：Next, superflies fine tuning, which we'll talk about later.  
译文：接下来，超级苍蝇的微调，这个我们稍后会讲到。  

**00:18:57 - 00:18:57**  
原文：Okay.  
译文：好的。  

**00:18:57 - 00:19:07**  
原文：And if you think this looks like a Python program, well, it is a Python program, but I've made it, you processed it.  
译文：而且如果你认为这看起来像一个Python程序，嗯，它确实是一个Python程序，但我编写了它，你处理了它。  

**00:19:07 - 00:19:18**  
原文：So for your viewing pleasure, okay, so let's move on to the course logistics.  
译文：所以为了让大家看得愉快，好吧，那么让我们继续讲课程安排。  

**00:19:18 - 00:19:23**  
原文：Now actually, maybe I'll pause for questions.  
译文：现在，实际上，或许我会暂停一下来回答问题。  

**00:19:23 - 00:19:31**  
原文：Any questions about you know what we're learning in this class?  
译文：关于这门课我们正在学的内容，有什么问题吗？  

**00:19:31 - 00:19:31**  
原文：Yeah.  
译文：嗯。  

**00:19:35 - 00:19:38**  
原文：To be able to lead a team to build a futor model.  
译文：能够领导一个团队来构建一个未来模型。  

**00:19:40 - 00:19:53**  
原文：So the question is, would I expect a graduate from this class to be able to lead a team and build a frontier model, of course, with like a billion dollars of capital?  
译文：所以问题在于，我是否期望从这个班级毕业的学生能够领导一个团队并构建一个前沿模型，当然，这需要大约十亿美元的资金？  

**00:19:53 - 00:19:59**  
原文：Yeah, of course, I would say that it's a good step, but there's definitely many pieces that are missing.  
译文：嗯，当然，我会说这是一个好的步骤，但确实还缺少很多部分。  

**00:19:59 - 00:20:09**  
原文：And I think you know we thought about we should really teach a series of classes that eventually leads up to to as close as we can get.  
译文：我认为你知道我们考虑过，我们应该真正地教授一系列课程，最终尽可能接近目标。  

**00:20:09 - 00:20:12**  
原文：But I think this is maybe the first step of the puzzle.  
译文：但我觉得这可能是解开谜题的第一步。  

**00:20:12 - 00:20:17**  
原文：But there are a lot of things and happy to talk offline about that.  
译文：但还有很多事情，很高兴可以在线下讨论这些。  

**00:20:17 - 00:20:18**  
原文：But I like the ambition.  
译文：但是我喜欢这种雄心。  

**00:20:18 - 00:20:24**  
原文：Yeah that's what you should be doing, taking the class so you can go lead teams and build frontier models.  
译文：嗯，这就是你应该做的，去上课这样你就可以去领导团队和构建前沿模型了。  

**00:20:24 - 00:20:24**  
原文：Okay.  
译文：好的。  

**00:20:24 - 00:20:28**  
原文：Okay, let's talk a little bit about the course.  
译文：好的，让我们来谈谈这门课程。  

**00:20:28 - 00:20:31**  
原文：So here's a website, everything's online.  
译文：所以这里有一个网站，所有内容都在网上。  

**00:20:31 - 00:20:36**  
原文：This is a five unit class, but I think that maybe it doesn't express the level here.  
译文：这是一门五学分的课程，但我觉得这里可能没有表达出它的难度。  

**00:20:36 - 00:20:51**  
原文：As well as this quote that I pulled out from a course evaluation, the entire assignment was approximately the same amount of work as all five assignments from the csu 24n plus the final project.  
译文：除了我从课程评价中摘取的这句话外，整个作业的工作量大约相当于csu 24n所有五个作业加上期末项目的总和。  

**00:20:51 - 00:20:54**  
原文：And that's the first homework assignment.  
译文：那就是第一份家庭作业。  

**00:20:54 - 00:20:58**  
原文：So not too I'll scare you off, but just giving some data here.  
译文：所以不是要吓到你，只是在这里提供一些数据。  

**00:20:58 - 00:21:00**  
原文：So why should you endure that?  
译文：那么你为什么要忍受那种情况呢？  

**00:21:00 - 00:21:02**  
原文：Why should you do it?  
译文：为什么你应该这样做？  

**00:21:02 - 00:21:13**  
原文：I think this class is really for people who have sort of its obsessive need to understand how things work all the way down to the atom, so to speak.  
译文：我认为这门课真的是为那些有着近乎痴迷的需求去理解事物是如何运作的人准备的，可以说是一直深入到原子层面。  

**00:21:13 - 00:21:30**  
原文：And I think if you when you get through this class, I think you will have really leveled up in terms of your research engineering and the comlevel of comfort that you'll have in building ml systems at scale will just be, I think, know something.  
译文：我认为当你完成这门课程后，你在研究工程方面真的会有所提升，并且在构建大规模机器学习系统时的自信程度也会提高，我认为你会掌握一些东西。  

**00:21:30 - 00:21:35**  
原文：There's also a bunch of reasons that you shouldn't take the class.  
译文：还有许多理由说明你不应该上这门课。  

**00:21:35 - 00:21:41**  
原文：For example, if you want to get any research done this quarter, maybe this class isn't for you.  
译文：例如，如果你想在这个季度完成任何研究，也许这门课不适合你。  

**00:21:41 - 00:21:55**  
原文：If you're interested in learning just about the hottest new techniques, there are many other classes that can probably deliver on that better than, for example, you spending a lot of time debugging bpe.  
译文：如果你对学习最热门的新技术感兴趣，有很多其他课程可能在这方面会比你花费大量时间调试bpe更好。  

**00:21:55 - 00:22:08**  
原文：And this is really, I think, about a class about the primitives and learning things bottom up as opposed to the kind of the latest.  
译文：而这真的，我认为，是关于基础的一门课程，是从底层开始学习东西，而不是那种最新的东西。  

**00:22:08 - 00:22:18**  
原文：And also, if you're interested in building language models or four x, this is probably not the first class you would take.  
译文：另外，如果你对构建语言模型或four x感兴趣，这可能不是你会首先选择的课程。  

**00:22:18 - 00:22:25**  
原文：I think practically speaking, as much as I kind of made a fun of prompting, prompting is great.  
译文：我认为实际上，尽管我有点在开玩笑地谈论提示词，但提示词真的很棒。  

**00:22:25 - 00:22:27**  
原文：Fine tuning is great.  
译文：微调非常棒。  

**00:22:27 - 00:22:32**  
原文：If you can do that and it works, then I think that is something you should absolutely start with.  
译文：如果你能做到并且有效，那么我认为这绝对是你应该开始做的事情。  

**00:22:32 - 00:22:37**  
原文：So I don't want people taking this class and thinking that create any problem.  
译文：所以我希望人们不要上这门课后认为会制造任何问题。  

**00:22:37 - 00:22:40**  
原文：The first step is to train a language model from scratch.  
译文：第一步是从零开始训练一个语言模型。  

**00:22:40 - 00:22:43**  
原文：That is not the right way of thinking about it.  
译文：这不是正确的思考方式。  

**00:22:43 - 00:22:43**  
原文：Okay.  
译文：好的。  

**00:22:43 - 00:22:53**  
原文：And I know that many of you, you know some of you were enrolled, but we didn't we did have a cap so we weren't able to enroll everyone.  
译文：而且我知道你们中的很多人，你们知道有些人已经注册了，但是我们确实设有人数上限，因此我们无法让每个人都注册。  

**00:22:53 - 00:22:57**  
原文：And also for the people online, you can follow up at home.  
译文：同时也为在线的朋友们，你们可以在家跟进。  

**00:22:57 - 00:23:03**  
原文：All the lecture materials and assignments are online, so you can look at them.  
译文：所有的讲座材料和作业都在网上，所以你可以查看它们。  

**00:23:03 - 00:23:10**  
原文：The lectures are also recorded and will be put on YouTube, although there will be some number of weak lag there.  
译文：讲座也会被录制并上传到YouTube，尽管那里会有一些延迟。  

**00:23:10 - 00:23:14**  
原文：And also, we'll offer this class next year.  
译文：同时，我们明年也会提供这门课程。  

**00:23:14 - 00:23:20**  
原文：So if you were not able to take it this year, don't fret, there will be next time.  
译文：所以如果你今年没能参加，不要担心，还有下一次。  

**00:23:20 - 00:23:24**  
原文：Okay, so the class has five assignments.  
译文：好的，所以这个课程有五个作业。  

**00:23:24 - 00:23:45**  
原文：And each of the assignments, we don't provide scaffolding code in a sense that literally we give you a blank file and you're supposed to build things up in the spirit of learning building from scratch, but we're not that mean.  
译文：而每一个作业，我们并不是说完全不提供框架代码，即我们不会真的只给你一个空白文件然后让你从零开始构建一切以体验从头学习的过程，但我们也不会那么苛刻。  

**00:23:45 - 00:23:52**  
原文：We do provide unit tests and some adapter interfaces that allow you to check correctness of different pieces.  
译文：我们确实提供了单元测试和一些适配器接口，以便您检查不同组件的正确性。  

**00:23:52 - 00:24:11**  
原文：And also the assignment write up, if you walk through it, does do it for sort of a gentle job of doing that, but you're kind of on your own for making good software design decisions and figuring out what you name, your functions and how to organize your code, which is a useful skill, I think.  
译文：还有作业的撰写，如果你仔细阅读的话，确实会以一种温和的方式引导你完成，但在做出良好的软件设计决策、确定函数名称以及如何组织代码方面，你基本上需要自己来完成，我认为这是一种有用的技能。  

**00:24:11 - 00:24:26**  
原文：So one strategy, I think for all assignments is that there is a piece of assignment which is just implement the thing and make sure it's correct that mostly you can do locally on your laptop.  
译文：所以我认为对于所有任务的一个策略是，有一部分任务就是实现这个东西并确保它是正确的，这部分工作你基本上可以在你的笔记本电脑上本地完成。  

**00:24:26 - 00:24:28**  
原文：You shouldn't need compute for that.  
译文：你不应该需要计算来完成那件事。  

**00:24:28 - 00:24:35**  
原文：And then you we have a cluster that you can run for benchmarking both accuracy and speed.  
译文：然后你有一个集群可以用来进行准确性和速度的基准测试。  

**00:24:35 - 00:24:39**  
原文：So I want everyone to kind of embrace this idea of that.  
译文：所以我想让大家都能接受这个想法。  

**00:24:39 - 00:24:47**  
原文：You want to use as small data set or as few resources as possible to prototype before running large jobs.  
译文：你希望在运行大型任务之前，使用尽可能小的数据集或尽可能少的资源来构建原型。  

**00:24:47 - 00:24:55**  
原文：You shouldn't be debugging with 1 billion parameter models on the cluster if you can help it.  
译文：如果可以避免的话，你不应该在集群上使用10亿参数的模型进行调试。  

**00:24:55 - 00:24:56**  
原文：Okay.  
译文：好的。  

**00:24:56 - 00:25:05**  
原文：There's some assignments which will have a leaderboard, which usually is of the form, do things to make perplexity go down.  
译文：有一些作业会有排行榜，通常的形式是，做一些事情来降低困惑度。  

**00:25:05 - 00:25:19**  
原文：Given a particular training budget last year, it was, I think, pretty exciting for people to try to try different things that you either learn from the class or you read online.  
译文：鉴于去年有特定的培训预算，我认为，人们尝试从课堂上学到或在网上阅读到的不同事物是非常令人兴奋的。  

**00:25:19 - 00:25:30**  
原文：And then finally, I guess this year is, no, this was less of a problem last year because I guess Copilot wasn't as good, but you know curses pretty good.  
译文：然后最后，我想今年是，不，去年这个问题没那么严重，因为我觉得Copilot还没那么好，但你知道，现在它已经相当不错了。  

**00:25:30 - 00:25:39**  
原文：So I think our general strategy is that AI tools can take away from learning because there are cases where it can just solve the thing you want it to do.  
译文：所以我认为我们的总体策略是，人工智能工具可能会削弱学习效果，因为有些情况下它们可以直接解决你想要完成的事情。  

**00:25:39 - 00:25:44**  
原文：But you know I think you can obviously use them judiciously.  
译文：但你知道我认为你可以明智地使用它们。  

**00:25:44 - 00:25:45**  
原文：So but use at your own risk.  
译文：所以但请自行承担风险使用。  

**00:25:45 - 00:25:50**  
原文：You're kind of responsible for your own learning experience here.  
译文：你在这里的学习体验某种程度上是由你自己负责的。  

**00:25:50 - 00:25:52**  
原文：Okay, so we do have a cluster.  
译文：好的，所以我们确实有一个集群。  

**00:25:52 - 00:25:59**  
原文：So thank you together, AI for providing a bunch of H -100s for us.  
译文：所以感谢AI为我们提供了一堆H-100。  

**00:25:59 - 00:26:14**  
原文：There's a guide to please read it carefully to learn how to use the cluster and start your assignments early because the cluster will fill up towards the end of a deadline as everyone's trying to get their large runs in.  
译文：有一份指南，请仔细阅读以学习如何使用集群，并尽早开始你的任务，因为临近截止日期时，随着每个人都在尝试运行他们的大型任务，集群将会变得非常繁忙。  

**00:26:16 - 00:26:17**  
原文：Okay.  
译文：好的。  

**00:26:17 - 00:26:20**  
原文：Any questions about that?  
译文：关于那一点有什么问题吗？  

**00:26:20 - 00:26:26**  
原文：You mentioned it was a five real able to sign up, right?  
译文：你提到的是五个名额可以注册，对吧？  

**00:26:26 - 00:26:30**  
原文：So the question is can you sign up for less than five units?  
译文：所以问题是，你可以注册少于五个学分吗？  

**00:26:30 - 00:26:38**  
原文：I think administratively, if you have to sign up for less, that is possible, but it's the same class and the same workload.  
译文：我认为从管理角度来看，如果你必须注册少一些课程，这是可能的，但课程内容和工作量是一样的。  

**00:26:40 - 00:26:43**  
原文：Any other questions?  
译文：还有其他问题吗？  

**00:26:45 - 00:26:46**  
原文：Okay.  
译文：好的。  

**00:26:46 - 00:26:57**  
原文：So in this part, I'm going to go through all the different components of the course and just give a broad overview, a preview of what you're going to experience.  
译文：所以在这一部分，我将详细介绍课程的所有不同组成部分，并给出一个大致的概览，让你预先了解你将会体验到的内容。  

**00:26:57 - 00:27:04**  
原文：So remember, it's all about efficiency given hardware and data, how do you train the best model given your resources?  
译文：所以记住，关键在于给定硬件和数据的情况下如何高效地利用你的资源来训练出最好的模型？  

**00:27:04 - 00:27:13**  
原文：So for example, if I give you a common call, wl dump of web dump and 32H -100 for two weeks, what should you do?  
译文：所以，例如，如果我给你一个常见的调用，如“wl dump”或“web dump”，以及32H -100持续两周，你应该怎么做？  

**00:27:13 - 00:27:18**  
原文：There are a lot of different design decisions.  
译文：有很多不同的设计决策。  

**00:27:18 - 00:27:27**  
原文：There's questions about the tokenizer, the architecture, systems, optimizations you can do, data, things you can do.  
译文：有关于分词器、架构、系统、可以进行的优化、数据以及你可以做的事情的问题。  

**00:27:27 - 00:27:32**  
原文：And we've organized the class into these five units or pillars.  
译文：我们将这门课程组织成了这五个单元或支柱。  

**00:27:32 - 00:27:42**  
原文：So I'm going to go through each of them, you know, in turn and talk about what we'll cover, what the assignment will involve, and then I'll kind of wrap up.  
译文：所以我会依次讲解每一个，你知道的，谈谈我们会涵盖的内容，作业会涉及什么，然后我会做一个总结。  

**00:27:42 - 00:27:43**  
原文：Okay.  
译文：好的。  

**00:27:43 - 00:27:49**  
原文：So the goal of the basics unit is just get a basic version of a full pipeline working.  
译文：所以基础单元的目标就是让一个完整的流水线的基础版本运行起来。  

**00:27:49 - 00:27:54**  
原文：So here you implement a tokenizer model architecture and training.  
译文：所以在这里你实现了一个分词器模型架构和训练。  

**00:27:54 - 00:27:58**  
原文：So just say a bit more about what these components are.  
译文：所以再多说一点这些组件是什么。  

**00:27:58 - 00:28:05**  
原文：So a tokenizer is something that converts between strings and sequences of integers.  
译文：所以，分词器是将字符串与整数序列之间进行转换的工具。  

**00:28:05 - 00:28:15**  
原文：Intuitively, you can think about the integers corresponding to breaking up the string into segments, mapping each segment to an integer.  
译文：直观地，你可以将整数看作是将字符串分割成若干段，然后将每一段映射到一个整数。  

**00:28:15 - 00:28:23**  
原文：And the idea is that you just your sequence of integers is what goes into the actual model, which has to be like a fixed dimension.  
译文：而想法就是你的整数序列会被输入到实际模型中，这个模型必须是固定维度的。  

**00:28:23 - 00:28:24**  
原文：Okay.  
译文：好的。  

**00:28:24 - 00:28:37**  
原文：So in this course, we'll talk about the bipair encoding, be tokenizer, which is relatively simple and still is used.  
译文：所以在本课程中，我们将讨论相对简单且仍在使用的bipair编码、分词器。  

**00:28:37 - 00:28:44**  
原文：There are a promising set of methods on tokenizer free approaches.  
译文：有一系列有前景的方法是关于无分词器的方法。  

**00:28:44 - 00:28:56**  
原文：So these are methods that just start with the raw bytes, don't do tokenization, and develop a particular architecture that just takes the row.  
译文：所以这些方法只是从原始字节开始，不进行分词，并开发了一种特定的架构，该架构直接处理这些原始数据。  

**00:28:56 - 00:29:03**  
原文：Bes, this work is promising, but know, so far I haven't seen it been scaled to the frontier yet.  
译文：Bes，这项工作很有前景，但要知道，到目前为止我还没有看到它被扩展到前沿领域。  

**00:29:03 - 00:29:05**  
原文：So we're go with bpe for now.  
译文：所以我们现在先用bpe。  

**00:29:05 - 00:29:18**  
原文：Okay, so once you've tokenized your sequence or strings into a sequence of integers, now we define a model architecture over the sequences.  
译文：好的，所以一旦你将你的序列或字符串转换成整数序列后，我们现在就来定义这些序列上的模型架构。  

**00:29:18 - 00:29:22**  
原文：So the starting point here is original transformer.  
译文：所以这里的起点是原始的Transformer。  

**00:29:22 - 00:29:28**  
原文：That's what is the backbone of basically all frontier models.  
译文：那就是基本上所有前沿模型的支柱。  

**00:29:28 - 00:29:31**  
原文：And here's architectural diagram.  
译文：以下是架构图。  

**00:29:31 - 00:29:36**  
原文：We won't go into the details here, but there's attention sion piece.  
译文：我们不会在这里深入细节，但有一个注意力机制的部分。 

注意：原文中的"attention sion piece"可能是笔误，正确的表达应该是"attention mechanism"，即“注意力机制”。如果原文确实是"attention sion piece"且有特定含义，请告知以便更准确地翻译。  

**00:29:36 - 00:29:40**  
原文：And then there's mlp player with some you know normalization.  
译文：然后还有mlp播放器，带有一些你知道的归一化处理。  

**00:29:40 - 00:29:45**  
原文：So a lot has actually happened until since 2017, right?  
译文：所以实际上从2017年到现在发生了很多事情，对吧？  

**00:29:45 - 00:29:53**  
原文：And I think there's a sort of sense to which, Oh, the transformer is invented and then, you know everyone's just using in transformer.  
译文：我认为有一种感觉是，哦，变压器被发明了，然后你知道大家都在使用变压器。  

**00:29:53 - 00:30:06**  
原文：And to a first approximation, that's we're still using the same recipe, but there have been a bunch of the smaller improvements that do make a substantial difference when you add them all up.  
译文：而大致上，我们仍然在使用相同的配方，但已经有许多小的改进，当把这些改进加在一起时，确实产生了显著的影响。  

**00:30:06 - 00:30:11**  
原文：So for example, there is the activation know nonlinear activation function.  
译文：所以，例如，有激活函数，即非线性激活函数。  

**00:30:11 - 00:30:16**  
原文：So swiggwhich we saw a little bit before positional embeddings.  
译文：所以在位置嵌入之前，我们稍微看到了一点swiggwhich。 

注：这里的"swiggwhich"看起来像是一个拼写错误或者是一个特定的术语，如果它是一个特定的术语或专有名词，请提供更多的上下文信息以便更准确地翻译。  

**00:30:16 - 00:30:23**  
原文：There's new positional embeddings, these rotary positional embeddings, which we'll talk about normalization.  
译文：有新的位置嵌入，即旋转位置嵌入，我们将讨论归一化。  

**00:30:23 - 00:30:30**  
原文：Instead of using a layer norm, we're going to look at something called rms norm, which is similar but simpler.  
译文：与其使用层归一化，我们将研究一种称为rms归一化的方法，它与层归一化类似但更简单。  

**00:30:30 - 00:30:37**  
原文：There's a question of where you place the normalization, which has been changed from the original transformer.  
译文：有一个关于归一化位置的问题，这一点已经从原始的Transformer中进行了更改。  

**00:30:37 - 00:30:44**  
原文：The mlp use the canonical version as a dense mlp, and you can replace that with mixture of experts.  
译文：mlp使用的是标准版本的密集mlp，你可以用专家混合模型来替换它。  

**00:30:44 - 00:30:49**  
原文：Attention is something that has actually been gaining a lot of attention.  
译文：注意力实际上已经获得了大量的关注。  

**00:30:49 - 00:30:56**  
原文：I guess there's full attention, and then there's sliding window attention and linear attention.  
译文：我猜有全注意力，然后还有滑动窗口注意力和线性注意力。  

**00:30:56 - 00:31:01**  
原文：All of these are trying to prevent a quadratic blow up.  
译文：所有这些都在试图防止二次爆炸性增长。  

**00:31:01 - 00:31:10**  
原文：There's also lower dimensional versions like gqa and mla, which we'll get to in a second or not in a second, but in a future lecture.  
译文：还有低维度的版本，比如gqa和mla，我们稍后会讲到，或者不是马上，但在未来的讲座中会讲到。  

**00:31:10 - 00:31:25**  
原文：And then the most kind of maybe radical thing is other alternatives to the transformer, like staspace models like hyena where they're not doing attention, but some other sort of operation.  
译文：然后最具有革命性的一点可能是变压器的其他替代方案，比如状态空间模型如hyena，它们不使用注意力机制，而是采用其他某种操作。  

**00:31:25 - 00:31:34**  
原文：And sometimes you get best flow towards by mixing, making a hybrid model that mixes these in with transformers.  
译文：有时候，通过混合，创建一个将这些与转换器结合的混合模型，可以获得最佳的效果。  

**00:31:34 - 00:31:39**  
原文：Okay, so once you define your architecture, you need a train.  
译文：好的，所以一旦你定义了你的架构，你就需要进行训练。  

**00:31:39 - 00:31:43**  
原文：So know design decisions include optimizer.  
译文：所以现在设计决策包括优化器。  

**00:31:43 - 00:31:49**  
原文：So atom W, which is a varibasically atom fixed up, is still very prominent.  
译文：所以原子W，即经过某种方式修正后的原子，仍然非常突出。 

注：原文中的"varibasically"似乎是一个拼写错误或专业术语，这里直译为“某种方式”，如果这是一个特定领域的术语，请提供更多的上下文信息以便更准确地翻译。  

**00:31:49 - 00:31:52**  
原文：So we'll mostly work with that.  
译文：所以我们将主要使用那个。  

**00:31:52 - 00:32:07**  
原文：But it is worth mentioning that there is more recent optimizers like Muan and soap that have shown promise, learning rate, schedule, batch size, whether you do regulzation or not hyperparameters.  
译文：但值得一提的是，还有一些较新的优化器如Muan和soap展现出了潜力，学习率、调度、批量大小、是否进行正则化等超参数。  

**00:32:07 - 00:32:24**  
原文：There's a lot of details here, and I think this class is one where the details do matter because you can easily have order of magnitude difference between a well tuned architecture and something that's just like a vanilla transformer.  
译文：这里有很多细节，我认为在这个课程中细节确实很重要，因为一个经过良好调优的架构与一个普通的Transformer之间很容易产生数量级的差异。  

**00:32:24 - 00:32:30**  
原文：So in assignment one, basically you'll implement the ppe tokenizer.  
译文：所以在第一个作业中，基本上你需要实现ppe分词器。  

**00:32:30 - 00:32:41**  
原文：I'll warn you that this is actually the part that seems to have been a lot of surprising, maybe a lot of work for people.  
译文：我会提醒你，这实际上是看起来让人感到很意外的部分，也许对很多人来说是很大的工作量。  

**00:32:41 - 00:32:43**  
原文：So just you're warned.  
译文：所以你可得有个心理准备。  

**00:32:43 - 00:32:51**  
原文：And you also implemented transformer cross mpatrp, loss to atom W optimizer and training loop.  
译文：你还实现了transformer交叉匹配、损失到原子W优化器和训练循环。 

注：原文中的"mpatrp"可能是笔误，这里假设为"匹配"（match）的误写。如果有具体含义，请提供更多信息以便更准确翻译。  

**00:32:51 - 00:32:58**  
原文：So again, the whole stack, and we're not making you implement pi torch from scratch.  
译文：所以，整个栈，我们并不是要让你从零开始实现pi torch。  

**00:32:58 - 00:33:04**  
原文：So you can use pi torch, but you can't use the transformer implementation for pi torch.  
译文：所以你可以使用pi torch，但你不能使用pi torch的transformer实现。  

**00:33:04 - 00:33:10**  
原文：There's a small list of functions that you can use and you can only use those.  
译文：这里有一个你可以使用的小函数列表，你只能使用这些。  

**00:33:10 - 00:33:22**  
原文：Okay, so we're gonna to have some tiny stories and open web text data sets that you'll train on and then there will be a leaderboard to minimize the open webtext perplexity.  
译文：好的，所以我们将会有一些简短的故事和开放网络文本数据集供你训练，然后会有一个排行榜来尽量降低开放网络文本的困惑度。  

**00:33:22 - 00:33:28**  
原文：We'll give you 90 minutes on H -100 and see what you can do.  
译文：我们会给你90分钟使用H-100，看看你能做些什么。  

**00:33:28 - 00:33:35**  
原文：So this is last year so we'll see we have the top so this is the number to beat for this year.  
译文：所以这是去年的数据，我们会看到这是最高的，所以这是今年要超越的数字。  

**00:33:35 - 00:33:39**  
原文：Okay all right, so that's the basics.  
译文：好的，就这样，这些是基础知识。  

**00:33:39 - 00:33:44**  
原文：Now after basics, I mean, in some sense you're done right.  
译文：现在，在学习了基础知识之后，我的意思是，在某种意义上你已经完成了。  

**00:33:44 - 00:33:48**  
原文：Like you have ability to train a transformer.  
译文：就像你有能力训练一个变压器。 

注：这里的“transformer”在不同上下文中可能指代不同的事物，如在机器学习中通常指的是“变换器”模型，而在电气工程中则指的是“变压器”。根据上下文选择最合适的翻译。如果是指机器学习中的模型，更准确的翻译应该是：

就像你有能力训练一个变换器模型。  

**00:33:48 - 00:33:50**  
原文：What else do you need?  
译文：你还需要什么？  

**00:33:50 - 00:33:55**  
原文：So the system part really goes into how you can optimize this further.  
译文：所以系统部分真正涉及到的是你如何进一步优化这一点。  

**00:33:55 - 00:33:58**  
原文：So how do you get the most out of hardware?  
译文：那么，如何才能最大限度地利用硬件呢？  

**00:33:58 - 00:34:05**  
原文：And for this, we need to take a closer look at the hardware and how we can leverage it.  
译文：而为了做到这一点，我们需要更仔细地研究硬件以及如何利用它。  

**00:34:05 - 00:34:12**  
原文：So there's kernels, parallelism and inference are the three components of this unit.  
译文：所以有内核、并行性和推理是这个单元的三个组成部分。  

**00:34:12 - 00:34:12**  
原文：So okay.  
译文：好吧。  

**00:34:12 - 00:34:21**  
原文：So to first talk about kernels, let's talk a little bit about what a GPU looks like.  
译文：所以首先来谈谈内核，让我们先稍微了解一下GPU的样子。  

**00:34:21 - 00:34:21**  
原文：Okay.  
译文：好的。  

**00:34:21 - 00:34:34**  
原文：So a GPU, which we'll get much more into is basically a huge array of these little units that do floating point operations.  
译文：所以GPU，我们后面会更深入地讨论，基本上是由大量执行浮点运算的小单元组成的大型阵列。  

**00:34:34 - 00:34:40**  
原文：And maybe the one thing to note is that this is the GPU chip.  
译文：也许需要注意的一点是，这是GPU芯片。  

**00:34:40 - 00:34:45**  
原文：And here is the the memory that's actually off chip.  
译文：而这实际上是芯片外的存储。  

**00:34:45 - 00:34:51**  
原文：And then there's some other memory like l two caches and l one caches on chip.  
译文：然后还有一些其他的内存，比如芯片上的L2缓存和L1缓存。  

**00:34:51 - 00:34:56**  
原文：And so the basic idea is that compute has to happen here.  
译文：因此，基本的想法是计算必须在这里进行。  

**00:34:56 - 00:34:59**  
原文：Your data might be somewhere else.  
译文：您的数据可能在其他地方。  

**00:34:59 - 00:35:05**  
原文：And how do you basically organize your compute so that you can be most efficient?  
译文：那么，你基本上是如何组织你的计算资源，以便能够最高效地运作呢？  

**00:35:05 - 00:35:12**  
原文：So one quick analogy is imagine that your memory is where you can store.  
译文：所以一个快速的类比是，想象一下你的记忆就是你可以存储东西的地方。  

**00:35:12 - 00:35:20**  
原文：Like your data model parameters is like a warehouse, and your compute is like the factory.  
译文：就像你的数据模型参数像是一个仓库，而你的计算则像是工厂。  

**00:35:20 - 00:35:26**  
原文：And what ends up being a big bottleneck is just data movement cost.  
译文：而最终成为大瓶颈的只是数据移动的成本。  

**00:35:26 - 00:35:41**  
原文：So the thing that we have to do is how do you organize the compute like even a matrix multiplication to maximize the utilization of the GPU's by minimizing the data movement?  
译文：所以我们需要做的是如何组织计算，比如即使是矩阵乘法，也要通过最小化数据移动来最大化GPU的利用率？  

**00:35:41 - 00:35:47**  
原文：And there's a bunch of techniques like fusion and tiling that allow you to do that.  
译文：还有一系列技术，如融合和分块，可以让你做到这一点。  

**00:35:47 - 00:35:50**  
原文：So we'll get all into the details of that.  
译文：所以我们将会深入到所有这些细节中。  

**00:35:50 - 00:35:54**  
原文：And to implement and leverage kernel, we're gonna to look at triiton.  
译文：并且为了实现和利用内核，我们将要研究Triton。  

**00:35:54 - 00:36:05**  
原文：There's other things you can do with various levels of sophistication, but we're going to use Triton, which is developed by OpenAI in a popular way to build kernels.  
译文：还有其他各种复杂程度不同的方法可以使用，但我们将使用由OpenAI开发的Triton，这是一种构建内核的流行方式。  

**00:36:05 - 00:36:10**  
原文：So we're going to write some kernels that's for one GPU.  
译文：所以我们将会编写一些针对一个GPU的内核。  

**00:36:10 - 00:36:18**  
原文：So now in general, you have these big runs take know thousands, if not tens of thousands of GPU's.  
译文：所以现在一般来说，这些大规模运行需要数千乃至数万块GPU。  

**00:36:18 - 00:36:25**  
原文：But even at eight, it kind of starts becoming interesting because you have a lot of GPU's.  
译文：但即使在八个的时候，它也开始变得有趣起来，因为你有很多GPU。  

**00:36:25 - 00:36:33**  
原文：They're are connected to some cpu nodes and they also are directly connected via mv switch, mv link.  
译文：它们连接到一些CPU节点，并且还通过MV交换机、MV链路直接相连。  

**00:36:33 - 00:36:35**  
原文：And it's the same idea right now.  
译文：而现在也是同样的想法。  

**00:36:35 - 00:36:41**  
原文：The only thing is that data movement between GPU's is even slower.  
译文：唯一的问题是GPU之间的数据传输甚至更慢。  

**00:36:41 - 00:36:57**  
原文：And so we need to figure out how to put model parameters and activations and gradients and put them on the GPU's and do the computation and to minimize the amount of movement.  
译文：因此，我们需要弄清楚如何将模型参数、激活值和梯度放到GPU上进行计算，并尽量减少数据移动的量。  

**00:36:57 - 00:37:07**  
原文：And then so we're going to explore different type of techniques like data parallelism and tensor parallelism and so on.  
译文：然后我们将探索不同类型的技术，比如数据并行和张量并行等。  

**00:37:07 - 00:37:10**  
原文：So that's all I'll say about that.  
译文：所以关于那件事我就说这么多。  

**00:37:10 - 00:37:19**  
原文：And finally, inference is something that we didn't actually do last year in the class, although we had a guest lecture.  
译文：最后，推理是我们去年在课堂上实际上没有做的事情，尽管我们有过一次客座讲座。  

**00:37:19 - 00:37:26**  
原文：But this is important because the inference is how you actually use a model.  
译文：但这很重要，因为推理是你实际使用模型的方式。  

**00:37:26 - 00:37:41**  
原文：It's basically the task of generating tokens, given a prompt, given a train model, and it also turns out to be really useful for a bunch of other things besides just chatting with your favorite model.  
译文：基本上，这个任务就是根据给定的提示和训练好的模型来生成词元，而且除了仅仅与你最喜欢的模型聊天之外，它还被发现对许多其他事情都非常有用。  

**00:37:41 - 00:37:52**  
原文：You need it for reinforcement learning, test time compute, which has been very popular lately, and even evaluating models, you need to do inference.  
译文：你需要它来进行强化学习、最近非常流行的测试时计算，甚至在评估模型时，你也需要进行推理。  

**00:37:52 - 00:37:55**  
原文：So we're gonna na spend some time talking about inference.  
译文：所以我们将会花一些时间来讨论推理。  

**00:37:55 - 00:38:12**  
原文：Actually, if you think about the globally, the cost that's that's spent on inference is it's eclipsing the cost that it is used to train models because training, despite it being very intensive, is ultimately a one time cost.  
译文：实际上，如果你从全球范围来考虑，用于推理的成本正在超过用于训练模型的成本，因为尽管训练非常耗费资源，但最终它只是一次性的成本。  

**00:38:12 - 00:38:16**  
原文：And inference is cost scales with every use.  
译文：而推理的成本随着每次使用而增加。  

**00:38:16 - 00:38:23**  
原文：And the more people use your model, the more you'll need inference to be efficient.  
译文：而且使用你的模型的人越多，你就越需要让推理变得高效。  

**00:38:23 - 00:38:23**  
原文：Okay?  
译文：好的？  

**00:38:23 - 00:38:26**  
原文：So in inference, there's two phases.  
译文：所以在推理中，有两个阶段。  

**00:38:26 - 00:38:28**  
原文：There's a prefill and a decode.  
译文：有一个预填充和一个解码。  

**00:38:28 - 00:38:35**  
原文：Prefill is you take the prompt and you can run it through the model and get some activations.  
译文：预填充是指你将提示输入模型中运行，从而获得一些激活值。  

**00:38:35 - 00:38:40**  
原文：And then decode is you go autogressively one by one and generate tokens.  
译文：然后解码是通过自回归方式逐个生成标记。  

**00:38:40 - 00:38:46**  
原文：So prefill, all the tokens are given so you can process everything at once.  
译文：所以预填充，所有的标记都被给出，这样你可以一次性处理所有内容。  

**00:38:46 - 00:38:49**  
原文：So this is exactly what you see at training time.  
译文：所以这正是你在训练时所看到的。  

**00:38:49 - 00:38:58**  
原文：And generally, this is a good setting to bm because you can it's naturally parallel and you're mostly compute bound.  
译文：并且通常来说，这是一个很好的设置来运行bm，因为它是天然并行的，并且你主要受限于计算能力。  

**00:38:58 - 00:39:06**  
原文：What makes inference, I think, special and difficult is that this Autery regressive decoding, you need to generate one token at a time.  
译文：我认为使推理变得特别且困难的是这种自回归解码，你需要一次生成一个词元。  

**00:39:06 - 00:39:09**  
原文：And it's hard to actually saturate all your GPU's.  
译文：而且实际上很难让你的所有GPU都达到饱和。  

**00:39:09 - 00:39:13**  
原文：And it becomes memory bound because you're constantly moving data around.  
译文：并且它变成了内存限制的，因为你一直在移动数据。  

**00:39:13 - 00:39:18**  
原文：And we'll talk about a few ways to speed the models up, speed inference up.  
译文：我们将讨论几种加快模型速度、加速推理的方法。  

**00:39:18 - 00:39:20**  
原文：You can use a cheaper model.  
译文：您可以使用一个更便宜的模型。  

**00:39:20 - 00:39:29**  
原文：You can use this really cool technique called specutive decoding where use a cheaper model to sort of scout ahead to regenerate multiple tokens.  
译文：你可以使用一种非常酷的技术，叫做投机性解码，其中使用一个成本较低的模型来预先探索，以生成多个标记。  

**00:39:29 - 00:39:41**  
原文：And then if these tokens happen to be good by some, for some definition, good, you can have the full model model just know score in and accept them all in parallel.  
译文：然后，如果这些标记恰好按照某种定义是好的，你可以让完整的模型并行地对它们进行评分并全部接受。  

**00:39:41 - 00:39:46**  
原文：And then there's a bunch of systems optimizations that you can do as well.  
译文：然后还有一系列的系统优化你也可以进行。  

**00:39:46 - 00:39:47**  
原文：Okay.  
译文：好的。  

**00:39:47 - 00:39:51**  
原文：So after the systems, Oh, okay, assignment two.  
译文：所以在系统之后，哦，好的，作业二。  

**00:39:51 - 00:39:59**  
原文：So you're going to implement a kernel, you're going to implement some parallelism.  
译文：所以你要实现一个内核，你还要实现一些并行处理。  

**00:39:59 - 00:40:02**  
原文：So data parallel is very natural.  
译文：所以数据并行是非常自然的。  

**00:40:02 - 00:40:04**  
原文：And so we'll do that.  
译文：所以我们会那样做的。  

**00:40:04 - 00:40:13**  
原文：Some of the model parallelism like fsdp turns out to be a bit kind of complicated do from scratch.  
译文：有些模型并行技术，比如 FSDP，从零开始实现起来有点复杂。  

**00:40:13 - 00:40:17**  
原文：So we'll do sort of a baby version of that.  
译文：所以我们将会做一个那种的简化版。  

**00:40:17 - 00:40:21**  
原文：But you know I encourage you to learn you know about the full version.  
译文：但是你知道我鼓励你去了解完整版。  

**00:40:21 - 00:40:28**  
原文：We'll go over the full version in class, but implementing from scratch might be a bit you know too much.  
译文：我们会在课上讲解完整版本，但是从零开始实现可能有点你知道的太多了。  

**00:40:28 - 00:40:33**  
原文：And then I think an important thing is getting in the habit of always benchmarking profile.  
译文：然后我认为很重要的一点是养成始终进行基准测试的习惯。  

**00:40:33 - 00:40:48**  
原文：I think that's actually probably the most important thing, is that you can implement things, but unless you have a feedback on how well your implementation is going and where the ball no x are, you're just going na be kind of flying blind.  
译文：我认为这实际上可能是最重要的事情，就是你可以实施一些措施，但除非你对实施的效果有所反馈，并了解哪些地方出了问题，否则你就像是在盲目飞行。  

**00:40:50 - 00:40:50**  
原文：Okay.  
译文：好的。  

**00:40:50 - 00:40:53**  
原文：So unit three is scaling laws.  
译文：所以第三单元是规模法则。  

**00:40:53 - 00:41:07**  
原文：And here the goal is you want to do experiments at small scale and figure things out and then predict the hyperparameters and loss at large scale.  
译文：而这里的目标是，你希望在小规模下进行实验并找出规律，然后预测大规模下的超参数和损失。  

**00:41:07 - 00:41:11**  
原文：So here's a fundamental question.  
译文：所以这里有一个基本问题。  

**00:41:11 - 00:41:16**  
原文：So if I give you a flops budget, what model size should you use?  
译文：所以如果我给你一个FLOPs预算，你应该使用什么规模的模型？  

**00:41:16 - 00:41:21**  
原文：If you use a larger model, that means you can train on less data.  
译文：如果你使用更大的模型，那就意味着你可以用更少的数据进行训练。  

**00:41:21 - 00:41:24**  
原文：And if you use a smaller model, you can train on more data.  
译文：而且如果你使用一个更小的模型，你可以用更多的数据进行训练。  

**00:41:24 - 00:41:26**  
原文：So what's the right balance here?  
译文：那么这里的正确平衡点是什么呢？  

**00:41:26 - 00:41:33**  
原文：And this has been a study quite extensively and figured out by a series of paper from openair and DeepMind.  
译文：而这已经被openair和DeepMind的一系列论文广泛研究并弄清楚了。  

**00:41:33 - 00:41:38**  
原文：So if you hear the term chinchilla optimal, this is what this is referring to.  
译文：所以如果你听到“chinchilla optimal”这个术语，指的就是这个意思。  

**00:41:38 - 00:41:47**  
原文：And the basic idea is that for every compute budget number of flops, you can vary the number of parameters of your model.  
译文：而基本的想法是，对于每个计算预算（即浮点运算次数），你可以调整模型的参数数量。  

**00:41:47 - 00:41:52**  
原文：Okay, that and then you measure how good that model is.  
译文：好的，然后你衡量那个模型的好坏。  

**00:41:52 - 00:41:57**  
原文：So for every level of compute, you can get the optimal parameter count.  
译文：所以对于每一个计算层级，你都可以获得最佳的参数数量。  

**00:41:57 - 00:42:09**  
原文：And then what you do is you can fit a curve to extrapolate and see if you had, let's say, one e 22 flops, you know what would it be?  
译文：然后你要做的是拟合一条曲线进行外推，看看如果你有比如说1e22次浮点运算，它会是什么样的？  

**00:42:09 - 00:42:10**  
原文：The parameter size.  
译文：参数大小。  

**00:42:10 - 00:42:37**  
原文：And it turns out these minimum, when you plot them, it's actually remarkably linear, which leads leads to this very actually simple but useful rule of thumb, which is that if you have a particular model of size n, if you multiply by 20, that's the number of tokens you should train on essentially.  
译文：结果发现，当你绘制这些最小值时，它们实际上是相当线性的，这导致了一个非常简单但有用的拇指规则，即如果你有一个大小为n的特定模型，那么将n乘以20，基本上就是你应该训练的token数量。  

**00:42:37 - 00:42:44**  
原文：So that means if I say 1.4 billion, primeter model should be trained on 28 billion token.  
译文：所以这意味着如果我说14亿，那么基础模型应该在280亿个令牌上进行训练。  

**00:42:44 - 00:42:44**  
原文：Okay.  
译文：好的。  

**00:42:44 - 00:42:48**  
原文：But you know this doesn't take into account inference cost.  
译文：但你知道这并没有考虑到推理成本。  

**00:42:48 - 00:42:53**  
原文：This is literally how can you train the best model regardless of how big that model is.  
译文：这实际上就是如何训练出最好的模型，无论该模型有多大。  

**00:42:53 - 00:42:59**  
原文：So there's some limitations here, but it's nonetheless been extremely useful for model development.  
译文：所以这里有一些限制，但它对模型开发仍然非常有用。  

**00:42:59 - 00:43:12**  
原文：So in this assignment, this is kind of no fun because we define a quote unquote, training api, which you can query with a particular set of hyperparameters.  
译文：所以在本次作业中，这有点无趣，因为我们定义了一个所谓的“训练API”，你可以用一组特定的超参数来查询它。  

**00:43:12 - 00:43:19**  
原文：You specify architecture and batch size and so on, and we return you a loss value.  
译文：您指定架构和批量大小等，我们返回给您一个损失值。  

**00:43:19 - 00:43:21**  
原文：Your decisions will get you.  
译文：你的决定将会造就你。  

**00:43:21 - 00:43:21**  
原文：Okay?  
译文：好的？  

**00:43:21 - 00:43:32**  
原文：So your job is you have a flops budget and you're going to try to figure out how to train a bunch of models and then gather the data.  
译文：所以你的任务是，你有一个FLOPs预算，你需要想办法如何训练一堆模型，然后收集数据。  

**00:43:32 - 00:43:46**  
原文：You're going to fit a scaling law to the gather data and then you're going to submit your prediction on what you would choose to be the hyperparameters, what model size and so on at a larger scale.  
译文：你将根据收集到的数据拟合一个缩放定律，然后提交你对在更大规模下会选择哪些超参数（如模型大小等）的预测。  

**00:43:46 - 00:43:46**  
原文：Okay.  
译文：好的。  

**00:43:46 - 00:43:54**  
原文：So this is a case where you have to be really we want to put you in this position where there's some stakes.  
译文：所以这是一个情况，我们真的希望把你放在有一定利害关系的位置上。  

**00:43:54 - 00:44:00**  
原文：I mean, this is not like burning real compute, but you know once you run out of your flop widget, that's it.  
译文：我的意思是，这不像真正消耗计算资源，但你知道一旦你的浮点运算小工具用完了，那就结束了。  

**00:44:00 - 00:44:10**  
原文：So you have to be very careful in terms of how you prioritize what experiments to run, which is something that the frontier labs have to do all the time.  
译文：所以在选择要进行哪些实验时，你必须非常小心地确定优先级，这是前沿实验室一直在做的事情。  

**00:44:10 - 00:44:16**  
原文：And there will be a leaderboard for this, which is minifinmized loss given your flops.  
译文：并且会有一个排行榜，这个排行榜是根据你的计算量（flops）来最小化损失的。  

**00:44:16 - 00:44:22**  
原文：Budget question those point 24.  
译文：预算问题那些点24。 

请注意，这个翻译可能不太通顺，因为原始句子似乎有些不完整或不清楚。如果可以提供更多的上下文信息，可能会有助于更准确地翻译。  

**00:44:22 - 00:44:30**  
原文：So if we're working ahead, should we expect assignments to change over time or final?  
译文：所以如果我们提前工作，我们应该期待任务会随时间变化还是最终确定不变？  

**00:44:30 - 00:44:37**  
原文：So the question is that these links are from 2024, the rough assignments, the rough structure will be the same.  
译文：所以问题是这些链接来自2024年，大致的分配、大致的结构将保持不变。  

**00:44:37 - 00:44:40**  
原文：From 2025, there will be some modifications.  
译文：从2025年起，将会有一些修改。  

**00:44:40 - 00:44:45**  
原文：But if you look at these, you should have a pretty good idea of what to expect.  
译文：但如果你看看这些，你应该对预期的情况有个相当好的了解。  

**00:44:48 - 00:44:51**  
原文：Okay, so let's go into data now.  
译文：好的，那么现在让我们进入数据部分。  

**00:44:51 - 00:45:03**  
原文：Okay, so up until now, you have scaling laws, you have systems, you can have your transformer implementation, everything you're really kind of good to go.  
译文：好的，到目前为止，你已经有了缩放定律，有了系统，你可以实现你的transformer，一切都准备就绪了。  

**00:45:03 - 00:45:11**  
原文：But data, I would say, is a really kind of key ingredient that I think differentiates in some sense.  
译文：但是数据，我可以说，是一种非常关键的成分，我认为在某种程度上它起到了区分作用。  

**00:45:11 - 00:45:16**  
原文：And the question to ask here is, what do I want this model to do?  
译文：而这里要问的问题是，我希望这个模型做什么？  

**00:45:16 - 00:45:22**  
原文：Because what the model does is completely, I mean, mostly determined by the data.  
译文：因为模型所做的事是完全，我的意思是，主要由数据决定的。  

**00:45:22 - 00:45:28**  
原文：If I put, if I train on multilingual data, it will have multilingual capabilities.  
译文：如果我使用多语言数据进行训练，它将具备多语言能力。  

**00:45:28 - 00:45:31**  
原文：If I train on code, it have code capabilities.  
译文：如果我用代码进行训练，它就会具备代码能力。  

**00:45:31 - 00:45:31**  
原文：It's not know.  
译文：这不是已知的。 

注意：原文"It's not know." 似乎有一个小错误，应该是 "It's not known." 如果是这样的话，翻译则为：“这不是已知的。” 若原文无误，则以上翻译成立。  

**00:45:31 - 00:45:32**  
原文：It's very natural.  
译文：这非常自然。  

**00:45:32 - 00:45:38**  
原文：And usually data sets are a conglomeration of a lot of different pieces.  
译文：而通常数据集是由许多不同的部分组成的集合。  

**00:45:38 - 00:45:45**  
原文：There's, you know, this is from a pile which is four years ago, but the same idea, I think, holds you.  
译文：你知道，这是四年前的一堆东西里的，但我觉得同样的想法对你也适用。  

**00:45:45 - 00:45:47**  
原文：You have data from know the web.  
译文：你有来自网络的数据。  

**00:45:47 - 00:45:48**  
原文：This is common crawl.  
译文：这是通用爬虫。  

**00:45:48 - 00:45:54**  
原文：You have saack, exchange, Wikipedia, GitHub and different sources which are curated.  
译文：你有saack、exchange、维基百科、GitHub以及各种经过整理的资源。  

**00:45:54 - 00:46:05**  
原文：And so in the data section, we're going to start talking about evaluation, which is given a model, how do you evaluate whether it's any good?  
译文：所以在数据部分，我们将开始讨论评估，也就是给定一个模型，你如何评估它是否足够好？  

**00:46:05 - 00:46:11**  
原文：So we're going to talk about perplexity measures, kind of standardized testing like mmlu.  
译文：所以我们将会讨论困惑度量，这是一种类似于mmlu的标准测试。  

**00:46:11 - 00:46:28**  
原文：If you have models that generate utterances for instruction following, how do you evaluuate that there's so decisions about if you can ensemble or do chain of faat test time, how does that affect your evaluation?  
译文：如果你有用于生成指令跟随话语的模型，你如何评估这些模型？关于是否可以在评估时集成模型或进行快速链式测试，这样的决策会如何影响你的评估？  

**00:46:28 - 00:46:41**  
原文：And then you can talk about entire systems, evaluation of entire system, not just the language model, because language models often get these days plugged into some agentic system or something.  
译文：然后你可以讨论整个系统，对整个系统进行评估，而不仅仅是语言模型，因为如今语言模型通常会被插入到某种代理系统或其他系统中。  

**00:46:42 - 00:46:48**  
原文：Okay, so now after establishing evaluation, let's look at data curation.  
译文：好的，那么现在在建立了评估之后，让我们来看看数据整理。  

**00:46:48 - 00:46:54**  
原文：So this is, I think, an important point that people don't realize.  
译文：所以我认为这是一个重要的点，人们没有意识到。  

**00:46:54 - 00:46:59**  
原文：I often hear people say, Oh, we're training the model on the Internet.  
译文：我经常听到人们说，哦，我们正在互联网上训练模型。  

**00:46:59 - 00:47:02**  
原文：This doesn't make sense, right?  
译文：这没有意义，对吧？  

**00:47:02 - 00:47:11**  
原文：Data doesn't just fall from the sky and there's the Internet that you can you know pipe into your model.  
译文：数据不是从天上掉下来的，你可以知道通过互联网将数据导入到你的模型中。  

**00:47:11 - 00:47:29**  
原文：Data has to always be actively acquired somehow, even if you you know, just as an example of you know I always tell people, look at the data and so let's look at some data.  
译文：数据总是需要以某种方式主动获取，即使你知道，就比如我总是告诉人们，看看数据，那么让我们来看一些数据。  

**00:47:29 - 00:47:32**  
原文：So this is some common crawl.  
译文：所以这是一些常见的爬取。  

**00:47:32 - 00:47:33**  
原文：No data.  
译文：无数据。  

**00:47:33 - 00:47:39**  
原文：I'm going to take ten documents and I think hopefully this works.  
译文：我打算拿十份文件，希望这能行得通。  

**00:47:39 - 00:47:39**  
原文：Okay.  
译文：好的。  

**00:47:39 - 00:47:54**  
原文：I think the rendering is off, but you can kind of see this is a sort of random sample of common crawl, and you can see that this is maybe not exactly the data.  
译文：我认为渲染有点问题，但你可以大致看出这是一些从通用爬虫中随机抽取的样本，你也可以看出这可能不完全是原始数据。  

**00:47:54 - 00:47:57**  
原文：Oh, here's some actually real text here.  
译文：哦，这里有一些实际的文本。  

**00:47:57 - 00:47:59**  
原文：Okay, that's cool.  
译文：好的，那很酷。  

**00:47:59 - 00:48:15**  
原文：But if you look at most of common crawl, aside from this is a different language, but you can also see this is very spammy sites and you'll quickly realize that a lot of the web is just trash.  
译文：但如果你看看大多数的通用爬虫数据，除了语言不同之外，你还会发现这些网站充满了垃圾信息，你会很快意识到网络上的很多内容都是垃圾。  

**00:48:15 - 00:48:25**  
原文：And so well, okay, maybe that's not that's surprising, but it's more trash than you would actually expect, I promise.  
译文：好吧，也许这并不令人惊讶，但我保证，垃圾比你想象的要多。  

**00:48:25 - 00:48:31**  
原文：What I'm saying is that there's a lot of work that needs to happen in data.  
译文：我的意思是说，在数据方面还有很多工作需要做。  

**00:48:31 - 00:48:41**  
原文：So you crawl the Internet, you can take books, archives of papers, GitHub, and there's actually a lot of processing that needs to happen.  
译文：所以你爬取互联网，你可以获取书籍、论文档案、GitHub上的资料，实际上这需要进行大量的处理。  

**00:48:41 - 00:48:46**  
原文：Know there's also legal questions about what data you can train on, which we'll touch on.  
译文：知道还有关于你可以用哪些数据进行训练的法律问题，我们将会提及这一点。  

**00:48:46 - 00:49:02**  
原文：Nowadays, a lot of frontier models have to actually buy data because the data on the Internet that's publicly accessible is actually turns out to be a bit limited for that kind of the really frontier performance.  
译文：如今，许多前沿模型实际上不得不购买数据，因为互联网上公开可访问的数据对于那种真正前沿的表现来说实际上是有点有限的。  

**00:49:02 - 00:49:09**  
原文：And also, I think it's important to remember that this data that's scraped, it's not actually text, right?  
译文：同时，我认为很重要的一点是要记住，被抓取的这些数据，实际上并不是文本，对吧？  

**00:49:09 - 00:49:14**  
原文：First of all, it's html or it's pdf's or in the case of code, it's just directories.  
译文：首先，它是html或者是pdf的，或者在代码的情况下，它只是目录。  

**00:49:14 - 00:49:20**  
原文：So there has to be an explicit process that takes this data and turns it into text.  
译文：所以必须有一个明确的过程来处理这些数据并将其转换成文本。  

**00:49:20 - 00:49:27**  
原文：Okay, so we're going to talk about the transformation from html to text.  
译文：好的，那么我们将要讨论的是从html到文本的转换。  

**00:49:27 - 00:49:30**  
原文：And this is going to be a lossy process.  
译文：而这将是一个有损的过程。  

**00:49:30 - 00:49:37**  
原文：So the trick is how can you preserve the content and some of the structure without know?  
译文：所以诀窍在于，你如何在不完全了解的情况下保留内容和部分结构？  

**00:49:37 - 00:49:51**  
原文：Basically, just having an html filtering as you get know surmise is going to be very important, both for gaining high quality data, but also removing harmful content.  
译文：基本上，正如你所猜测的那样，进行HTML过滤将非常重要，这不仅对于获取高质量数据很重要，而且对于移除有害内容也很关键。  

**00:49:51 - 00:49:55**  
原文：Generally, people train classifiers to do this.  
译文：通常，人们训练分类器来完成这项任务。  

**00:49:55 - 00:50:00**  
原文：The duplication is also an important step, which we'll talk about.  
译文：复制也是一个重要的步骤，我们将会讨论。  

**00:50:00 - 00:50:03**  
原文：Okay, so assignment four is all about data.  
译文：好的，所以第四次作业全部关于数据。  

**00:50:03 - 00:50:11**  
原文：We're going to give you the raw common crawl dump so you can see just how bad it is and you're gonna to train classifiers dedube.  
译文：我们将为您提供原始的Common Crawl数据转储，这样您就可以看到它的质量有多糟糕，然后您将训练分类器进行去重。  

**00:50:11 - 00:50:20**  
原文：And then there's going to be a leaderboard where you're going to try to minimize perperplexity given your token budget.  
译文：然后会有一个排行榜，在这个排行榜上你会尝试在给定的token预算下最小化困惑度。  

**00:50:20 - 00:50:29**  
原文：So now you have the data, you've done this, build all your fancy kernels you've trained, now you can really train models.  
译文：所以现在你有了数据，你已经完成了这一步，构建了所有你训练过的复杂内核，现在你可以真正地训练模型了。  

**00:50:29 - 00:50:35**  
原文：But at this point, what you'll get is a model that can complete the next token, right?  
译文：但是在这一点上，你将得到的是一个能够完成下一个词元的模型，对吗？  

**00:50:35 - 00:50:39**  
原文：And this is called a essentially try base model.  
译文：而这被称为本质上是尝试的基础模型。  

**00:50:39 - 00:50:47**  
原文：And I think about it as a model that has a lot of raw potential, but it needs to be aligned or modified some way.  
译文：我认为它是一个拥有巨大潜力的模型，但需要以某种方式进行调整或修改。  

**00:50:47 - 00:50:51**  
原文：Alignment is a process of making it useful.  
译文：对齐是一个使其变得有用的过程。  

**00:50:51 - 00:50:55**  
原文：So alignment captures a lot of different things.  
译文：因此，对齐涵盖了非常多不同的方面。  

**00:50:55 - 00:51:02**  
原文：But three things I think it captures is that you want to get the language model to follow instructions right?  
译文：但我觉得它捕捉到了三点，那就是你希望语言模型能够遵循指令，对吧？  

**00:51:02 - 00:51:12**  
原文：Completing the next token is not necessarily following the instruction itjust complete the instruction or whatever it thinks will follow the instruction.  
译文：完成下一个词元并不一定是在遵循指令，它只是完成指令或它认为会跟随指令的任何内容。  

**00:51:12 - 00:51:24**  
原文：You get to here specify the style of the generation, whether you want to be long or short, whether you want bullets, whether you wanted to be witty or have sas or not.  
译文：您可以在这里指定生成的风格，比如您希望它是长还是短，是否需要使用项目符号，以及您是否希望它风趣或带有讽刺意味等。  

**00:51:24 - 00:51:31**  
原文：When you play with ChatGPT versus rock, you'll see that there's different alignment that has happened.  
译文：当你与ChatGPT对战而不是石头时，你会发现已经发生了不同的对齐。 

注：这里的翻译保持了原文格式，但为了更符合中文表达习惯，“对战”和“对齐”的用词可能需要根据具体上下文进行调整。如果是指比较或互动的方式，请提供更多背景信息以便更准确地翻译。  

**00:51:31 - 00:51:33**  
原文：And then also safety.  
译文：还有就是安全。  

**00:51:33 - 00:51:40**  
原文：One important thing is for these models to be able to refuse answers that can be harmful.  
译文：一件重要的事情是这些模型能够拒绝回答可能有害的问题。  

**00:51:40 - 00:51:43**  
原文：So that's where alignment also kicks in.  
译文：所以那就是对齐也开始起作用的地方。  

**00:51:43 - 00:51:48**  
原文：So there's generally two phases of alignment.  
译文：所以通常有两个对齐阶段。  

**00:51:48 - 00:51:51**  
原文：There's supervised fine tuning.  
译文：有监督微调。  

**00:51:51 - 00:51:55**  
原文：And here the goal is, I mean, it's very simple.  
译文：而这里的目标是，我的意思是，它非常简单。  

**00:51:55 - 00:52:06**  
原文：You basically gather a set of user assistant pairs, so prompt response pairs, and then you do supervised learning.  
译文：你基本上是收集一组用户助手配对，也就是提示响应配对，然后进行监督学习。  

**00:52:06 - 00:52:06**  
原文：Okay.  
译文：好的。  

**00:52:06 - 00:52:13**  
原文：And the idea here is that the base model already has sort of the raw potential.  
译文：这里的理念是，基础模型已经具备了某种原始潜力。  

**00:52:13 - 00:52:17**  
原文：So just fine tuning it on a few examples is sufficient.  
译文：所以只需用几个例子进行微调就足够了。  

**00:52:17 - 00:52:21**  
原文：Of course, the more examples you have, the better the results.  
译文：当然，你拥有的示例越多，结果就越好。  

**00:52:21 - 00:52:31**  
原文：But there's papers like this one that shows even like a thousand examples suffices to give you instruction following capabilities from a base good base model.  
译文：但有像这样的论文表明，即使是一千个例子也足以让一个好的基础模型具备遵循指令的能力。  

**00:52:31 - 00:52:31**  
原文：Okay.  
译文：好的。  

**00:52:31 - 00:52:43**  
原文：So this part is actually very simple and it's not that different from pre training because it's just you're given text and you just maximize the probability of the text.  
译文：所以这部分实际上非常简单，它与预训练并没有太大区别，因为你只是得到了文本，然后只需要最大化该文本的概率。  

**00:52:43 - 00:52:50**  
原文：So the second part is a bit more interesting from algorithmic perspective.  
译文：所以从算法的角度来看，第二部分更有趣一些。  

**00:52:50 - 00:52:55**  
原文：So the idea here is that even with sft phase, you will have a decent model.  
译文：所以这里的想法是，即使在SFT阶段，你也会有一个相当不错的模型。  

**00:52:55 - 00:52:57**  
原文：And now how do you improve it?  
译文：而现在你如何改进它？  

**00:52:57 - 00:53:06**  
原文：Well, you can get there more sdata, but that can be very expensive because you have to have someone sit down and annotate data.  
译文：嗯，你可以获取更多的数据，但这可能会非常昂贵，因为你需要有人坐下来标注数据。  

**00:53:06 - 00:53:16**  
原文：So the goal of learning from feedback is that you can leverage lighter forms and annotation and have the algorithms do a bit more work.  
译文：因此，从反馈中学习的目标是，你可以利用更轻量级的形式和注释，让算法多做一些工作。  

**00:53:16 - 00:53:16**  
原文：Okay.  
译文：好的。  

**00:53:16 - 00:53:20**  
原文：So one type of data you can learn from is preference data.  
译文：所以你可以从一种类型的数据中学习，那就是偏好数据。  

**00:53:20 - 00:53:30**  
原文：So this is where you generate multiple responses from a model to a given prompt, like a or b, and the user rate, whether a or b, is better.  
译文：所以这就是你根据给定的提示从模型中生成多个响应，比如a或b，然后用户评价a或b哪个更好。  

**00:53:30 - 00:53:39**  
原文：And so the data might look like it generates what's the best way to train a language model, use a large data set or use a small data set?  
译文：因此，数据可能看起来像是生成了这样的问题：训练语言模型的最佳方式是什么，是使用大型数据集还是使用小型数据集？  

**00:53:39 - 00:53:42**  
原文：And of course, the answer should be a.  
译文：当然，答案应该是 a。  

**00:53:42 - 00:53:46**  
原文：So that is a unit of a expressing preferences.  
译文：所以那是一个表示偏好的单位。  

**00:53:46 - 00:53:52**  
原文：Another type of supervision you could have is using verifiers.  
译文：另一种你可以使用的监督方式是利用验证者。  

**00:53:52 - 00:53:59**  
原文：So for some domains, you're lucky enough to have a formal verifier, like for math or code.  
译文：所以在某些领域，你很幸运地拥有一个形式化验证工具，比如数学或代码。  

**00:53:59 - 00:54:06**  
原文：Or you can use learn verifiers, where you train an actual language model to rate the response.  
译文：或者你可以使用学习验证器，通过训练一个实际的语言模型来对回复进行评分。  

**00:54:06 - 00:54:09**  
原文：And of course, this relates to evaluation.  
译文：当然，这与评估有关。  

**00:54:09 - 00:54:11**  
原文：Again, algorithms.  
译文：再次，算法。  

**00:54:11 - 00:54:16**  
原文：This is we're in the realm of reinforcement learning.  
译文：这是我们在强化学习领域的讨论。  

**00:54:16 - 00:54:27**  
原文：So one of the earliest algorithms that was developed that was applied to instruction tuning models was ppo proximal policy optimization.  
译文：所以，最早被开发并应用于指令调优模型的算法之一是PPO（近端策略优化）。  

**00:54:27 - 00:54:36**  
原文：It turns out that if you just have preference data, there's a much simpler algorithm called dpo that works really well.  
译文：原来，如果你只有偏好数据的话，有一种叫做dpo的更简单算法效果非常好。  

**00:54:36 - 00:54:43**  
原文：But in general, if you wanted to learn from verifiers data, you have to it's not preference data.  
译文：但总的来说，如果你想从验证者数据中学习，你必须明白这不是偏好数据。  

**00:54:43 - 00:54:46**  
原文：So you have to embrace rl fully.  
译文：所以你必须全然接受rl。  

**00:54:46 - 00:55:02**  
原文：And you there's this method, which we'll do in this class, which called group relative preference optimization, which simplifies ppo and makes it more efficient by removing the value function developed by deep seek, which seems to work pretty well.  
译文：还有这种方法，我们将在本课程中使用，称为组相对偏好优化，它通过移除由DeepSeek开发的价值函数来简化PPO并使其更高效，这似乎效果相当不错。  

**00:55:03 - 00:55:04**  
原文：Okay.  
译文：好的。  

**00:55:04 - 00:55:09**  
原文：So assignment five implements supervised tuning, dpo and grpo.  
译文：所以第五个任务实现了有监督的调优、DPO和GRPO。  

**00:55:09 - 00:55:23**  
原文：And of course, evaluate question quote two, five.  
译文：当然，评估问题引用二，五。  

**00:55:23 - 00:55:27**  
原文：The question is, is time at one seems a bit daunting.  
译文：问题是，似乎在某个时刻有点令人畏惧。  

**00:55:27 - 00:55:30**  
原文：What about the other ones?  
译文：其他的呢？  

**00:55:30 - 00:55:36**  
原文：I would say that assignment 12 are definitely the most heavy and hardest.  
译文：我会说作业12绝对是分量最重且最难的。  

**00:55:36 - 00:55:52**  
原文：Assignment three is a little bit more of a breather and assignment 45 at least last year where I would say a notch below assignment there too, although I don't know, it depends on we haven't fully worked out the details for this year.  
译文：作业三稍微轻松一些，而作业45至少在去年来说，我认为难度也比那个低一点，虽然我不确定，因为今年的具体细节我们还没有完全敲定。  

**00:55:55 - 00:55:57**  
原文：Yeah, it does get better.  
译文：是的，情况确实会变好的。  

**00:55:57 - 00:55:58**  
原文：Okay.  
译文：好的。  

**00:55:58 - 00:56:12**  
原文：So just to a recap of the different pieces here, remember, efficiency is this driving principle and there's a bunch of different design decisions.  
译文：所以，为了回顾一下这里的不同部分，记住，效率是这个驱动原则，并且有一系列不同的设计决策。  

**00:56:12 - 00:56:21**  
原文：And I think if you view efficiency everything through lens of efficiency, I think a lot of things kind of make sense.  
译文：我认为如果你通过效率的视角来看待一切，很多事情就都说得通了。  

**00:56:21 - 00:56:33**  
原文：And importantly, I think you we are it's worth pointing out there, we are currently in this compute constraint regime, at least this class and most people who are somewhat GPU poor.  
译文：而且重要的是，我认为这里值得指出的是，我们目前正处于这种计算受限的阶段，至少对于这个类别和大多数相对缺乏GPU资源的人来说是这样的。  

**00:56:33 - 00:56:37**  
原文：So we have a lot of data, but we don't have that much compute.  
译文：所以我们有很多数据，但我们的计算能力并没有那么多。  

**00:56:37 - 00:56:43**  
原文：And so these design decisions, sions will reflect squeezing the most out of the hardware.  
译文：因此，这些设计决策将会反映出从硬件中榨取最大效能的意图。  

**00:56:43 - 00:56:51**  
原文：So for example, data processing, we're filtering fairly aggressively because we don't want to waste precious compute on bad or relevant data.  
译文：所以例如，在数据处理方面，我们进行了相当激进的过滤，因为我们不想把宝贵的计算资源浪费在无用或不相关的数据上。  

**00:56:51 - 00:56:59**  
原文：Tokenization, like it's nice to have a model over bytes that's very elegant, but it's very compute inefficient with today's model architectures.  
译文：分词，就像拥有一个非常优雅的基于字节的模型是很好的，但与当今的模型架构相比，它的计算效率非常低。  

**00:56:59 - 00:57:04**  
原文：So we have to do tokenization to as an efficiency gain model architecture.  
译文：所以我们必须进行分词处理，以此作为提高模型架构效率的方法。  

**00:57:04 - 00:57:11**  
原文：There are a lot of design decisions there that are essentially motivated by efficiency training.  
译文：那里有很多设计决策基本上是出于效率训练的考虑。  

**00:57:11 - 00:57:18**  
原文：I think the fact that most of what we're doing to do is just a single epoch, this is clearly we're in a hurry.  
译文：我认为，我们所做的大部分事情都只是一个单一的周期，这显然表明我们很匆忙。  

**00:57:18 - 00:57:24**  
原文：We just need to see more data as opposed to spending a lot of time on any given data point.  
译文：我们只需要看到更多的数据，而不是在任何给定的数据点上花费大量时间。  

**00:57:24 - 00:57:27**  
原文：Scaling laws is completely about efficiency.  
译文：规模定律完全与效率有关。  

**00:57:27 - 00:57:35**  
原文：We use less compute to figure out the high proparameters and alignment is is maybe a little bit different.  
译文：我们使用较少的计算来确定高优先参数，而对齐方式可能略有不同。  

**00:57:35 - 00:57:47**  
原文：But the connection to efficiency is that if you can put resources into alignment, then you actually require less smaller base models.  
译文：但是，与效率的联系在于，如果你能够将资源进行对齐，那么实际上你所需要的较小的基础模型就会减少。  

**00:57:47 - 00:57:47**  
原文：Okay.  
译文：好的。  

**00:57:47 - 00:57:50**  
原文：So there a know there's sort of two paths.  
译文：所以我知道有两条路径。  

**00:57:50 - 00:58:00**  
原文：If your use cases is fairly narrow, you can probably use a smaller model, you align it or fine tune it and you can do well.  
译文：如果你的使用场景相当有限，你可能可以使用一个较小的模型，对其进行对齐或微调，这样就能取得不错的效果。  

**00:58:00 - 00:58:07**  
原文：But if your use cases are very broad, then there might not be a substitute for training a big model.  
译文：但是，如果你的使用场景非常广泛，那么可能就没有替代方案来训练一个大模型了。  

**00:58:07 - 00:58:08**  
原文：So that's today.  
译文：所以这就是今天。  

**00:58:08 - 00:58:20**  
原文：So increasingly now, at least for frontier labs, they're becoming data constrained, which is interesting because I think that the designs decisions will presumably completely change.  
译文：因此，现在越来越多的是，至少对于前沿实验室来说，他们正变得受数据限制，这很有趣，因为我认为设计决策可能会完全改变。  

**00:58:20 - 00:58:27**  
原文：Well, I mean, compute will always be important, but I think the design decisions will change.  
译文：好的，我的意思是，计算永远都是重要的，但是我认为设计决策将会发生变化。  

**00:58:27 - 00:58:32**  
原文：For example, you know, learning, taking one epoch over your data, I think doesn't really make sense.  
译文：例如，你知道的，学习，在你的数据上进行一次epoch，我认为这并没有什么意义。  

**00:58:32 - 00:58:38**  
原文：If you have more compute, why wouldn't did you take more epochs at least or do something smarter?  
译文：如果你有更多的计算资源，为什么你至少不增加训练轮数或者做一些更聪明的事情呢？  

**00:58:38 - 00:58:48**  
原文：Or maybe there will be different architectures, for example, because a transformer was really motivated by compute efficiency.  
译文：或者也许会有不同的架构，例如，因为变压器的设计初衷真的是为了计算效率。  

**00:58:48 - 00:58:51**  
原文：So that's something to kind of ponder.  
译文：所以这是需要思考的一点。  

**00:58:51 - 00:58:57**  
原文：Still, it's about efficiency, but the design decisions reflect what regime you're in.  
译文：仍然，这关乎效率，但设计决策反映了你所处的体制。  

**00:58:59 - 00:59:00**  
原文：Okay.  
译文：好的。  

**00:59:00 - 00:59:08**  
原文：So now I'm going to dive into the first unit before that.  
译文：所以在那之前，我将深入探讨第一个单元。  

**00:59:08 - 00:59:10**  
原文：Any questions?  
译文：有任何问题吗？  

**00:59:17 - 00:59:21**  
原文：The question is if we have a slack Or App, we will have a slack.  
译文：问题是如果我们有一个Slack或应用程序，我们就会有一个Slack。  

**00:59:21 - 00:59:24**  
原文：We'll send out details after the sliice.  
译文：我们将在切片后发送详细信息。 

注：这里的"the sliice"可能是拼写错误，通常应为"the slice"，但在没有上下文的情况下，我将其直接翻译了。如果有特定含义或专有名词，请提供更多信息以便更准确地翻译。  

**00:59:25 - 00:59:32**  
原文：Yeah will students auditing the course will have access to the same material.  
译文：嗯，旁听课程的学生将可以访问相同的材料。  

**00:59:32 - 00:59:47**  
原文：The question is students auditing the class will have access to all the online materials, assignments and will give you access to cavas so you can watch the lecture videos.  
译文：问题是旁听这门课程的学生将可以访问所有的在线资料、作业，并且会给你访问canvas的权限，这样你就可以观看讲座视频了。  

**00:59:48 - 00:59:50**  
原文：Yeah what's the grawhat's?  
译文：嗯，grawhat's是什么？  

**00:59:50 - 00:59:53**  
原文：The grading of the assignments?  
译文：作业的评分？  

**00:59:53 - 00:59:53**  
原文：Good question.  
译文：好问题。  

**00:59:53 - 01:00:03**  
原文：So there will be a set of unit tests that you will have to PaaS or part of the grading is, did you implement this correctly?  
译文：所以会有一组单元测试，你需要通过这些测试，或者部分评分标准是：你是否正确实现了这些内容？  

**01:00:03 - 01:00:15**  
原文：There will be also parts of the grade which will did you implement a model that achieved a certain level of loss or is efficient enough in the assignment?  
译文：还有一部分成绩将取决于你在作业中实现的模型是否达到了一定的损失水平或是否足够高效？  

**01:00:15 - 01:00:20**  
原文：Every problem part has a number of points associated with it.  
译文：每个问题部分都有与之关联的若干分数。  

**01:00:20 - 01:00:25**  
原文：And so that gives you a fairly granular level of what breeding looks like.  
译文：这样就给你展示了育种过程的一个相当细致的层面。  

**01:00:28 - 01:00:31**  
原文：Okay, let's jump into tokenization.  
译文：好的，让我们开始讨论分词。  

**01:00:31 - 01:00:35**  
原文：Okay, so Andre Kaati has this really nice video on tokenization.  
译文：好的，所以Andre Kaati有一个关于分词的非常好的视频。  

**01:00:35 - 01:00:45**  
原文：And in general, he makes a lot of these videos on that actually inspired a lot of this class, how you can build things from scratch.  
译文：而且总的来说，他制作了许多这类视频，这些视频实际上启发了这门课程的很多内容，即如何从零开始构建事物。  

**01:00:45 - 01:00:48**  
原文：So you should go check out some of his videos.  
译文：所以你应该去看看他的一些视频。  

**01:00:48 - 01:01:03**  
原文：So tokenization, as we talked about it, is the process of taking raw tewhich is generally represented as Unicode strings and turning it into a set of integers essentially.  
译文：所以，正如我们所讨论的，分词是将原始文本（通常表示为Unicode字符串）转换成一组整数的过程。  

**01:01:03 - 01:01:06**  
原文：And where each integer is represents a token.  
译文：并且每个整数代表一个标记。  

**01:01:06 - 01:01:07**  
原文：Okay?  
译文：好的？  

**01:01:07 - 01:01:14**  
原文：So we need a procedure that encodes strings to tokens and decodes them back into strings.  
译文：所以我们需要一个过程，将字符串编码为标记，并将它们解码回字符串。  

**01:01:14 - 01:01:23**  
原文：And the vocabulary size is just the number of values at a token ticon the number of the range of the integers.  
译文：而词汇量大小就是标记token在整数范围内的值的数量。 

注：原文似乎有些语法上的不清晰，直译可能无法完全传达原意。如果需要更准确的翻译，可能需要对原文进行一些澄清。  

**01:01:24 - 01:01:24**  
原文：Okay?  
译文：好的？  

**01:01:24 - 01:01:45**  
原文：So just to give you an example of how tokenizers work, let's play around with this really nice website which allows you to look at different tokenizers and just type in something like know hello, know hello or whatever.  
译文：所以，为了给你举个例子说明分词器是如何工作的，让我们来试用一下这个非常好的网站。这个网站允许你查看不同的分词器，并且可以输入像“know hello, know hello”或者任何你想输入的内容。  

**01:01:45 - 01:01:47**  
原文：Maybe I'll do this.  
译文：也许我会这么做。  

**01:01:47 - 01:01:51**  
原文：And one thing it does is it shows you the list of integers.  
译文：而且它的一项功能是向你展示整数列表。  

**01:01:51 - 01:01:54**  
原文：This is the output of tokenizer.  
译文：这是分词器的输出。  

**01:01:54 - 01:02:00**  
原文：It also nicely maps out the decomposition of the original string into a bunch of segments.  
译文：它也很好地将原始字符串分解成多个段落进行了映射。  

**01:02:00 - 01:02:03**  
原文：And a few things to kind of note.  
译文：还有几件事情需要注意。  

**01:02:03 - 01:02:06**  
原文：First of all, the space is part of a token.  
译文：首先，空格是标记的一部分。  

**01:02:06 - 01:02:13**  
原文：So unlike classical nlp, where the space just kind of disappears, everything is accounted for.  
译文：所以与经典的自然语言处理不同，在那里空间似乎就消失了，这里的一切都被考虑进去了。  

**01:02:13 - 01:02:18**  
原文：These are meant to be kind of reversible operations tokenization.  
译文：这些操作旨在成为一种可逆的分词处理。  

**01:02:18 - 01:02:26**  
原文：And by convention, now, for whatever reason, the space is usually preceding the token.  
译文：并且按照惯例，现在无论出于什么原因，空格通常位于标记之前。  

**01:02:26 - 01:02:44**  
原文：Also notice that you know hello is a completely different token than space hello, which you might make you a little bit squeamish, but it seems can cause problems, but that's just how it is going.  
译文：还要注意，你知道"hello"是一个与" space hello"完全不同的标记，这可能会让你有点不舒服，但似乎会导致问题，不过事实就是这样。  

**01:02:44 - 01:02:53**  
原文：Ask, is the space be leading instead of traintentional, or is it just an artifact of the bp process?  
译文：问，这个空格是起引导作用的，还是仅仅是BP过程中的一个产物？  

**01:02:53 - 01:02:58**  
原文：So the question is, is the spacing before intentional or not?  
译文：所以问题是，前面的空格是故意的还是无意的？  

**01:02:58 - 01:03:06**  
原文：So in the bp process, I will talk about you actually ptokenize and you and then you tokenize each part.  
译文：所以在bp过程中，我将讨论你实际上是如何进行ptokenize的，然后你再对每一部分进行tokenize。  

**01:03:06 - 01:03:13**  
原文：Anything think the pre tokenizer does put this space in the front, so it is built into the algorithm.  
译文：任何认为预分词器会在此处添加空格的想法，都是因为它被内置在算法中。  

**01:03:13 - 01:03:22**  
原文：You could put it at the end, but I think it probably makes more sense to put in the beginning.  
译文：你可以把它放在最后，但我觉得放在开头可能更合理。  

**01:03:22 - 01:03:23**  
原文：But I actually don't.  
译文：但实际上我不是。 

为了更准确地反映原文的含义，可以稍微调整为：
但其实我并不。 

不过，这句话在中文里可能需要更多的上下文来让意思更加明确。如果能提供更多的上下文信息，我可以帮助你更好地翻译。  

**01:03:23 - 01:03:27**  
原文：Well, I guess it could go either way, my sense.  
译文：嗯，我想这可能有两种情况，我的感觉是这样。  

**01:03:27 - 01:03:28**  
原文：Okay.  
译文：好的。  

**01:03:28 - 01:03:35**  
原文：So then if you look at numbers, you see that the numbers are chopped down into different pieces.  
译文：那么，如果你看这些数字，你会发现这些数字被分割成了不同的部分。  

**01:03:35 - 01:03:39**  
原文：It's a little bit kind of interesting that it's left to right.  
译文：这有点有趣，它是从左到右的。  

**01:03:39 - 01:03:45**  
原文：So it's definitely not grouping by thousands or anything like semantic.  
译文：所以这绝对不是按千位分组或者任何类似语义的方式。  

**01:03:45 - 01:03:54**  
原文：But anyway, I encourage you to kind of play with it and get a sense of what these existing tokenizers look like.  
译文：不过无论如何，我鼓励你试着玩一玩，了解一下这些现有的分词器是什么样子的。  

**01:03:54 - 01:03:58**  
原文：So this is a tokenizer for GPT -4, for example.  
译文：所以这是一个针对GPT-4的分词器，例如。  

**01:03:58 - 01:04:02**  
原文：So there's some observations that we made.  
译文：所以我们做了一些观察。  

**01:04:02 - 01:04:20**  
原文：So if you look at the gbt two tokenizer, which we'll use this kind of as a reference, okay, let me see if I can hopefully this is let me know if this is getting too small.  
译文：所以如果你看看gbt两个分词器，我们将用它作为一种参考，好的，让我看看我能否希望这个不要变得太小，如果太小了请告诉我。  

**01:04:20 - 01:04:23**  
原文：In the back, you take a string.  
译文：在后面，你取一个字符串。  

**01:04:23 - 01:04:27**  
原文：If you apply the GPT two tokenizer, you get your indices.  
译文：如果你应用GPT的两个分词器，你就会得到你的索引。  

**01:04:27 - 01:04:34**  
原文：So a maps strings the indices and then you can decode to get back the string.  
译文：所以，一个映射将字符串与索引对应起来，然后你可以解码以恢复字符串。  

**01:04:34 - 01:04:39**  
原文：And this is just a sanity check to make sure that you actually round trips.  
译文：而这只是一个合理性检查，以确保你实际上进行了往返。  

**01:04:39 - 01:04:54**  
原文：Another thing that's I guess, interesting to look at is this compression ratio, which is if you look at the number of bytes divided by the number of tokens, so how many bytes are represented by a token?  
译文：另一件可能有趣的事情是看看这个压缩比，即如果你看字节数除以标记数，那么一个标记代表多少字节？  

**01:04:54 - 01:04:56**  
原文：And the answer here is 1.6.  
译文：而这里的答案是1.6。  

**01:04:56 - 01:05:01**  
原文：So every token represents 1.6 bytes of data.  
译文：所以每个令牌代表1.6字节的数据。  

**01:05:01 - 01:05:01**  
原文：Okay?  
译文：好的？  

**01:05:01 - 01:05:07**  
原文：So that's just a GPT tokenizer that opended trained to motivate kind of bpe.  
译文：所以那只是一个经过训练以激发某种BPE的GPT分词器。  

**01:05:07 - 01:05:10**  
原文：I want to go through a sequence of attempts.  
译文：我想进行一系列的尝试。  

**01:05:10 - 01:05:16**  
原文：So like suppose you wanted to do tokenization, what would be sort of the simplest thing?  
译文：那么假设你想进行分词，最简单的方法是什么呢？  

**01:05:16 - 01:05:20**  
原文：The simplest thing is probably character based tokenization.  
译文：最简单的事情可能是基于字符的分词。  

**01:05:20 - 01:05:29**  
原文：A Unicode string is a sequence of Unicode characters, and each character can be converted into a integer called a code point.  
译文：Unicode字符串是一系列Unicode字符组成的序列，每个字符可以被转换成一个称为码点的整数。  

**01:05:29 - 01:05:31**  
原文：Okay, so a maps to 97.  
译文：好的，所以 a 对应 97。  

**01:05:31 - 01:05:41**  
原文：The world emoji maps to 127757 and you can see that it converts back.  
译文：世界表情符号对应于127757，你可以看到它能转换回来。  

**01:05:41 - 01:05:41**  
原文：Okay.  
译文：好的。  

**01:05:41 - 01:05:51**  
原文：So you can define a tokenizer which simply you know maps each character into a code point.  
译文：所以你可以定义一个分词器，它简单地将每个字符映射到一个码点。  

**01:05:51 - 01:05:52**  
原文：Okay.  
译文：好的。  

**01:05:52 - 01:05:57**  
原文：So what's one problem with this?  
译文：那么这个问题有什么问题呢？ 

为了更准确地保留原文格式，可以这样翻译：

那么这有一个什么问题？  

**01:05:57 - 01:06:00**  
原文：Yeah, compression ratio is one.  
译文：嗯，压缩比是一。  

**01:06:00 - 01:06:03**  
原文：The compression ratio is one.  
译文：压缩比为一。  

**01:06:03 - 01:06:13**  
原文：So that's well, actually the compression ratio is not quite one because a character is not a bite, but it's maybe not as good as you want.  
译文：所以呢，实际上压缩比并不完全是1，因为一个字符并不是一个比特，但可能也没有你想要的那么好。  

**01:06:13 - 01:06:19**  
原文：One problem with that, if you look at some code points, they're actually really large, right?  
译文：这个问题是，如果你看一些代码点，它们实际上真的很大，对吧？  

**01:06:19 - 01:06:27**  
原文：So you're basically allocating each like one slot in your vocabulary for every character uniformly.  
译文：所以你基本上是为词汇表中的每个字符均匀地分配了一个位置。  

**01:06:27 - 01:06:32**  
原文：And some characters appear way more frequently than others.  
译文：而有些字符出现的频率远高于其他字符。  

**01:06:32 - 01:06:36**  
原文：So this is not a very effective use of your kind of budget.  
译文：所以这不是对你那种预算的有效利用。  

**01:06:36 - 01:06:36**  
原文：Okay?  
译文：好的？  

**01:06:36 - 01:06:39**  
原文：So the vocabulary size is you're huge.  
译文：所以词汇量是巨大的。  

**01:06:39 - 01:06:45**  
原文：I mean, the vocabulary size being 127 is actually a big deal.  
译文：我的意思是，词汇量为127实际上是一个很大的问题。  

**01:06:45 - 01:06:52**  
原文：But the bigger problem is that some characters are rare and this is inefficient use of the vocab.  
译文：但更大的问题是有些字符很罕见，这导致词汇表的使用效率低下。  

**01:06:53 - 01:06:53**  
原文：Okay?  
译文：好的？  

**01:06:53 - 01:07:09**  
原文：So the comparratio is 1.5 in this case, because it's the tokens, sorry, the number of bytes per token and a character can be multiple bytes, okay?  
译文：所以在这个情况下，comparratio是1.5，因为这是每个token的字节数，对不起，我指的是每个token的字节数，而一个字符可以由多个字节组成，明白了吗？  

**01:07:09 - 01:07:14**  
原文：So that was a very kind of naive approach.  
译文：所以那是一种非常天真的方法。  

**01:07:14 - 01:07:19**  
原文：On the other hand, you can do byte based tokenization, okay?  
译文：另一方面，你可以进行基于字节的分词，好吗？  

**01:07:19 - 01:07:30**  
原文：So Unicode strings can be represented in a sequence of bytes because every string can just be converted into bytes.  
译文：因此，Unicode字符串可以表示为一系列字节，因为每个字符串都可以转换成字节。  

**01:07:30 - 01:07:31**  
原文：Okay?  
译文：好的？  

**01:07:31 - 01:07:39**  
原文：So some know a is already just kind of one byte, but some characters take up as many as four bytes.  
译文：所以有些字符只占用一个字节，但有些字符可能占用多达四个字节。  

**01:07:39 - 01:07:43**  
原文：And this is using the uta eight kind of encoding of Unicode.  
译文：而这使用的是Unicode的uta八种编码中的一种。 

注：这里的"uta eight kind of encoding"可能是指某种特定的编码方式，但在常见的Unicode编码类型（如UTF-8, UTF-16等）中，并没有直接对应"uta"这一表述。如果"uta"是特定上下文中的专有名词或缩写，请提供更多信息以便更准确地翻译。  

**01:07:43 - 01:07:48**  
原文：There's other encodings, but this is the most common one that's dynamic.  
译文：还有其他编码，但这是最常见的动态编码。  

**01:07:48 - 01:07:54**  
原文：So let's just convert everything into bytes and see what happens.  
译文：那么，我们就把所有内容都转换成字节，看看会发生什么。  

**01:07:55 - 01:08:08**  
原文：So if you do it into bytes now, all the indices are between zero and 256, because there are only 256 possible values for a byte by definition.  
译文：所以如果你现在将其转换为字节，所有的索引都在0到256之间，因为按照定义，一个字节只有256种可能的值。  

**01:08:08 - 01:08:15**  
原文：So your vocabulary is very small and each byte is I guess not all bytes are equally used, but you know it's not.  
译文：所以你的词汇量很小，而且我认为每个字节的使用频率并不相同，但你知道事实就是这样。  

**01:08:15 - 01:08:20**  
原文：You don't have ten many sparsity problems, but what's the problem with bybased encoding?  
译文：你没有太多稀疏性问题，但是基于字节的编码有什么问题呢？  

**01:08:25 - 01:08:31**  
原文：Yeah long sequences so this is I mean in some ways I really wish bicoding would work.  
译文：嗯，长序列，所以我的意思是，在某些方面我真的希望双向编码能够奏效。  

**01:08:31 - 01:08:45**  
原文：It's the most elegant thing but but you have long sequences your compression ratio is 11 byte per token and this is just terrible of compression ratio of one is terrible because your sequences will be really long.  
译文：这是最优雅的事情，但是当你的序列很长时，你的压缩比率是每个标记11字节，这样的压缩比率真的非常糟糕。因为你的序列将会非常长，压缩比率为1是非常糟糕的。 

注：原文中有一些重复和不太通顺的地方，翻译时尽量保持了原意，但为了使句子更通顺做了一些小调整。  

**01:08:45 - 01:08:49**  
原文：Attention is quadratic naively in the sequence lane.  
译文：注意力在序列长度上天真地呈二次方增长。  

**01:08:49 - 01:08:57**  
原文：So this is you're just gonna na have a bad time in terms of efficiency, okay, so that wasn't really good.  
译文：所以这样你的效率就会很低，好吧，所以这真的不太好。  

**01:08:57 - 01:09:03**  
原文：So now the thing that you might think about is, well, maybe we kind of have to be adaptive here, right?  
译文：所以现在你可能会想到的是，嗯，也许我们在这里需要有点适应性，对吧？  

**01:09:03 - 01:09:15**  
原文：Like you know we can't allocate a character or a byte per token, but maybe some tokens can represent lots of bytes and some tokens can represent few bytes.  
译文：就像你知道的那样，我们不能为每个标记分配一个字符或一个字节，但也许有些标记可以代表很多字节，而有些标记可以代表很少的字节。  

**01:09:15 - 01:09:18**  
原文：So one way to do this is word based tokenization.  
译文：所以一种方法是基于词的分词。  

**01:09:18 - 01:09:23**  
原文：And this is something that was actually very classic in nlp.  
译文：而这在自然语言处理中实际上是非常经典的。  

**01:09:23 - 01:09:34**  
原文：So here's a string, and you can just split it into a sequence of segments, and you can call each of these tokens.  
译文：所以这里有一段字符串，你可以将其分割成一系列的片段，你可以称这些片段为标记。  

**01:09:34 - 01:09:38**  
原文：So you just use a regular expression.  
译文：所以你只需要使用正则表达式。  

**01:09:38 - 01:09:51**  
原文：Here's a different regular expression that GPT two uses to ptokenize, and it just splits your string into a sequence of strings.  
译文：这是GPT两个使用的一个不同的正则表达式来分词，它只是将你的字符串分割成一系列的字符串。 

注意：这里的“GPT两个”可能是指“GPT-2”，在中文环境中通常直接翻译为“GPT-2”。因此，更准确的翻译可能是：

这是GPT-2使用的一个不同的正则表达式来进行分词，它只是将你的字符串分割成一系列的字符串。  

**01:09:52 - 01:10:00**  
原文：So and then what you do with each segment is you assign each of these to an integer, and then you're done.  
译文：所以然后你对每个段所做的就是将这些段分别赋值给一个整数，然后你就完成了。  

**01:10:00 - 01:10:01**  
原文：Okay.  
译文：好的。  

**01:10:01 - 01:10:05**  
原文：So what's the problem with this?  
译文：那么这有什么问题呢？  

**01:10:08 - 01:10:09**  
原文：Yeah.  
译文：嗯。  

**01:10:09 - 01:10:14**  
原文：So the problem is that your vocabulary size is sort of unbounded.  
译文：所以问题在于你的词汇量实际上是无界的。  

**01:10:14 - 01:10:25**  
原文：Well, not maybe not quite unbounded, but you don't know how big it is because on a given new input, you might get a segment that's just you've never seen before.  
译文：好吧，也许不是完全无界的，但你不知道它有多大，因为在给定的新输入下，你可能会得到一个你从未见过的片段。  

**01:10:25 - 01:10:28**  
原文：And that's actually a kind of a big problem.  
译文：而这实际上是一个相当大的问题。  

**01:10:28 - 01:10:35**  
原文：This is actually worbasa really big pain in the butt because some real words are rare.  
译文：这实际上真是一个很大的麻烦，因为有些真实的单词很罕见。  

**01:10:35 - 01:10:42**  
原文：And actually it's really annoying because new words have to receive this unk token.  
译文：而且这真的很烦人，因为新词必须接受这个未知词标记。  

**01:10:42 - 01:10:51**  
原文：And if you're not careful about how you compute the perplexity, then you're just going to mess up.  
译文：而且如果你不小心计算困惑度的话，那么你就会搞砸。  

**01:10:51 - 01:11:01**  
原文：So you know, word based isn't I think it captures the right intuition of adaptivity, but it's not exactly what we want here.  
译文：所以你知道，基于词的方法并不完全捕捉到适应性的正确直觉，但这不是我们这里想要的。  

**01:11:01 - 01:11:08**  
原文：So here we're finally going to talk about the bpe encoding or byte pair encoding.  
译文：所以在这里我们终于要讨论bpe编码或字节对编码了。  

**01:11:08 - 01:11:16**  
原文：So this was actually a very old algorithm developed by Philip gauge 94 for data compression.  
译文：所以这实际上是一个非常古老的算法，由Philip Gauge在1994年开发，用于数据压缩。  

**01:11:16 - 01:11:22**  
原文：And it was first introduced into nolp for neural machine translation.  
译文：并且它首次被引入到nolp中用于神经机器翻译。  

**01:11:22 - 01:11:30**  
原文：So before papers, I did machine translation or any, basically all nlp used word based tokenization.  
译文：所以在论文之前，我做了机器翻译或任何基本上所有NLP都使用基于词的分词。  

**01:11:30 - 01:11:33**  
原文：And again, we're based with a pain.  
译文：而再次，我们伴随着痛苦。  

**01:11:33 - 01:11:36**  
原文：So this paper pioneered this idea.  
译文：所以这篇论文开创了这个想法。  

**01:11:36 - 01:11:48**  
原文：Well, we can use this nice algorithm, form 94, and we can just make the tokenization kind of round trip, and we don't have to deal with unks or any of that stuff.  
译文：好吧，我们可以使用这个很好的94年的算法，只需让分词进行一种往返处理，而不需要处理未知词或其他类似的问题。  

**01:11:48 - 01:12:01**  
原文：And then finally, this entered a kind of language modeling era through GPT two, which was trained on using the bpe tokenizer.  
译文：然后最终，通过使用BPE分词器训练的GPT-2，进入了某种语言模型时代。  

**01:12:01 - 01:12:01**  
原文：Okay.  
译文：好的。  

**01:12:01 - 01:12:11**  
原文：So the basic idea is instead of defining some sort of preconceived notion of how to split it up, we're going to train the tokenizer on raw Tex.  
译文：所以基本的想法是，与其定义某种预先设想的如何分割的方法，我们将在原始Tex上训练分词器。  

**01:12:11 - 01:12:15**  
原文：That's the basic kind of insight, if you will.  
译文：那就是基本的见解，如果你愿意这么认为的话。  

**01:12:15 - 01:12:22**  
原文：And so organically, common sequences that span multiple characters we're going to try to represent as one token.  
译文：因此，自然而然地，跨越多个字符的常见序列我们将尝试将其表示为一个标记。  

**01:12:22 - 01:12:27**  
原文：And rare sequences are going to be represented by multiple tokens.  
译文：并且稀有序列将由多个标记表示。  

**01:12:27 - 01:12:31**  
原文：There's a sort of a site detail, which is for efficiency.  
译文：有一种站点细节，是为了提高效率。  

**01:12:31 - 01:12:43**  
原文：The GPT two paper uses war based tokenizer as a sort of preprocessing to break it up into segments, and then runs bp on each of the segments, which is what you're going to do in this class as well.  
译文：GPT-2论文使用基于词的分词器作为一种预处理手段来将其分解成段，然后对每个段运行bp，这也就是你在这门课上将要做的事情。  

**01:12:43 - 01:12:46**  
原文：The algorithm, bp is actually very simple.  
译文：算法，bp实际上非常简单。  

**01:12:46 - 01:12:53**  
原文：So we first convert the string into a sequence of bytes, which we already did when we talk about bybase tokenization.  
译文：所以我们首先将字符串转换成一系列字节，这在我们讨论bybase分词时已经做过了。  

**01:12:53 - 01:13:00**  
原文：And now we're going to successively merge the most common pair of adjacent tokens over and over again.  
译文：现在我们将依次反复合并最常见的一对相邻标记。  

**01:13:00 - 01:13:07**  
原文：So the intuition is that if a pair of tokens that shows up a lot, then we're going to compress it into one token.  
译文：所以直觉上，如果一对标记出现的频率很高，那么我们就把它压缩成一个标记。  

**01:13:07 - 01:13:09**  
原文：We're gonna to dedicate space for that.  
译文：我们将为此专门留出空间。  

**01:13:09 - 01:13:13**  
原文：Okay, so let's walk through what this algorithm looks like.  
译文：好的，那么让我们来一步步看看这个算法是什么样子的。  

**01:13:13 - 01:13:14**  
原文：So we're going to use this.  
译文：所以我们将会使用这个。  

**01:13:14 - 01:13:22**  
原文：Cand has an example, and we're going to convert this into a sequence of integers.  
译文：Cand 有一个例子，我们将把这个例子转换成一个整数序列。  

**01:13:22 - 01:13:23**  
原文：These are the bytes.  
译文：这些是字节。  

**01:13:23 - 01:13:27**  
原文：And then we're going to keep track of what we've merged.  
译文：然后我们将记录下我们合并的内容。  

**01:13:27 - 01:13:36**  
原文：So remember, merges is a map from two integers which can represent bytes or other pexisting tokens.  
译文：所以请记住，merges 是一个从两个整数映射而来的，这两个整数可以表示字节或其他预存在的标记。  

**01:13:36 - 01:13:44**  
原文：And we're going to create a new token and the vocab is just to be a handy way to represent the index to bytes.  
译文：我们将要创建一个新的标记，而词汇表只是为了方便地表示索引到字节。  

**01:13:44 - 01:13:47**  
原文：Okay, so we're going to the ppe algorithm.  
译文：好的，所以我们现在要讲的是ppe算法。  

**01:13:47 - 01:13:49**  
原文：I mean, it's very simple.  
译文：我的意思是，这非常简单。  

**01:13:49 - 01:13:56**  
原文：So I'm just actually gonna to run through the code you're gonna to do this number merges of times.  
译文：所以我实际上就是要运行你将要进行这个数字合并次数的代码。  

**01:13:56 - 01:13:57**  
原文：So number ges is three.  
译文：所以数字是三。  

**01:13:57 - 01:14:04**  
原文：In this case, we're going to first count up the number of occurrences of parirs abytes.  
译文：在这种情况下，我们首先将统计parirs abytes出现的次数。 

注：原文中的"parirs abytes"似乎是一个拼写错误，可能是想表达"pairs of bytes"（字节对）。如果这是正确的理解，请告知我以便进行更准确的翻译。  

**01:14:04 - 01:14:07**  
原文：So hopefully this doesn't become too small.  
译文：所以希望这不会变得太小。  

**01:14:07 - 01:14:12**  
原文：So we're going to just step through this sequence and we're going to see that.  
译文：所以我们将会一步步地走过这个序列，然后我们会看到这一点。  

**01:14:12 - 01:14:17**  
原文：Okay, so once 116, 104, we're going to increment that count.  
译文：好的，所以一旦到了116, 104，我们就要增加那个计数。  

**01:14:17 - 01:14:21**  
原文：104, 101 increment that count.  
译文：104, 101 增加该计数。  

**01:14:21 - 01:14:24**  
原文：We're go through the sequence and we're going to count up the bytes.  
译文：我们将遍历这个序列并计算字节数。  

**01:14:24 - 01:14:33**  
原文：Okay, so now after we have these counts, we're going to find the pair that occurs the most number of times.  
译文：好的，现在我们有了这些计数之后，我们将找到出现次数最多的配对。  

**01:14:33 - 01:14:42**  
原文：So I guess there's multiple ones, but we're just going to break ties and say 116 and 104.  
译文：所以我想有多个，但我们就打破平局说116和104。  

**01:14:42 - 01:14:44**  
原文：Okay, so that occurred twice.  
译文：好的，那么那件事发生了两次。  

**01:14:44 - 01:14:46**  
原文：So now we're going to merge up here.  
译文：所以现在我们要在这里合并。  

**01:14:46 - 01:14:52**  
原文：So we're going to create a new slot in our vocab, which is going to be 256.  
译文：所以我们将在词汇表中创建一个新的槽位，这个槽位将是256。  

**01:14:52 - 01:14:55**  
原文：So so far it's zero through one, 255.  
译文：所以到目前为止是0到1, 255。  

**01:14:55 - 01:14:58**  
原文：So now we're expanding the vocab to 256.  
译文：所以现在我们将词汇量扩展到256。  

**01:14:58 - 01:15:06**  
原文：And we're going to say every time we see 116 and 104, we're going to replace it with 256.  
译文：我们将要说的是，每当我们看到116和104时，我们将会用256来替换它。  

**01:15:08 - 01:15:15**  
原文：Okay, and then we're going to just apply that merge to our training set.  
译文：好的，然后我们将把这个合并应用到我们的训练集上。  

**01:15:15 - 01:15:22**  
原文：So after we do that, the 11 16, 104 became 256.  
译文：所以在我们这样做之后，11 16, 104 变成了 256。  

**01:15:22 - 01:15:28**  
原文：And this 256, remember, it occurred twice.  
译文：而这个256，记住，它出现了两次。  

**01:15:28 - 01:15:33**  
原文：Okay, so now we're just going to loop through this algorithm one more time.  
译文：好的，那么现在我们只需要再循环一遍这个算法。  

**01:15:33 - 01:15:46**  
原文：The second time it decided to merge 256 and 101, and now I'm going to replace that in indices and notice that the indices is going to shrink, right?  
译文：第二次它决定合并256和101，现在我将替换这些索引，并注意到索引将会减少，对吗？  

**01:15:46 - 01:15:56**  
原文：Because our compression ratio is getting better as we make room for more vocabulary items and we have a greater vocabulary to represent everything.  
译文：因为随着我们为更多的词汇项腾出空间，我们的压缩比率变得更好，并且我们有更大的词汇量来表示所有内容。  

**01:15:56 - 01:15:59**  
原文：Okay, so let me do this one more time.  
译文：好的，那么让我再做一次。  

**01:15:59 - 01:16:06**  
原文：And then the next merge is 250 73 and this is shrinking one more time.  
译文：然后下一次合并是250和73，这将进一步缩小。  

**01:16:06 - 01:16:09**  
原文：Okay, and then now we're done.  
译文：好的，现在我们完成了。  

**01:16:09 - 01:16:13**  
原文：Okay, so let's try out this tokenizer.  
译文：好的，那么让我们来试试这个分词器。  

**01:16:13 - 01:16:17**  
原文：So we have the string, the quick Brown fox.  
译文：所以我们有字符串，the quick Brown fox。

为了更准确地保留原始格式，可以这样翻译：

所以我们有字符串，the quick Brown fox。 

注意：这里的“the quick Brown fox”是专有名词或特定表达，通常在翻译时会保持原样。如果需要进一步解释，这句话常被用来指代英文中包含所有字母的句子的一部分，中文里有时会直接翻译为“快速的棕色狐狸”，但这并不是直译原文中的字符串。根据上下文需求选择是否进一步解释。  

**01:16:17 - 01:16:27**  
原文：We're going to encode into a sequence of indices, and then we're going to use our bp tokenizer to decode.  
译文：我们将编码成一系列索引，然后我们将使用我们的bp分词器进行解码。  

**01:16:27 - 01:16:31**  
原文：Let's actually step through what that know.  
译文：让我们实际上逐步了解那一点。  

**01:16:31 - 01:16:32**  
原文：Looks like this.  
译文：看起来像这样。  

**01:16:32 - 01:16:37**  
原文：Well, actually maybe decoding isn't actually interesting.  
译文：好吧，实际上也许解码并不是真的有趣。  

**01:16:37 - 01:16:41**  
原文：Sorry, it should have gone through the encode.  
译文：对不起，它应该经过编码的。  

**01:16:41 - 01:16:44**  
原文：Let's go back to encode.  
译文：让我们回到编码。  

**01:16:44 - 01:16:53**  
原文：So in code, you take a string, you convert to indices, and you just replay the merges.  
译文：所以在代码中，你取一个字符串，将其转换为索引，然后只是重放合并过程。  

**01:16:53 - 01:17:05**  
原文：And importantly, in the order that occur, so I'm going to replay these merges and then and then I'm going to get my indices, okay?  
译文：并且重要的是，按照发生的顺序来进行，所以我将重放这些合并，然后我将获取我的索引，好吗？  

**01:17:05 - 01:17:07**  
原文：And then verify that this works.  
译文：然后验证这是否有效。  

**01:17:07 - 01:17:07**  
原文：Okay?  
译文：好的？  

**01:17:07 - 01:17:10**  
原文：So that was it's pretty simple.  
译文：所以就是这样，非常简单。  

**01:17:10 - 01:17:12**  
原文：You know, it's because it's simple.  
译文：你知道，这是因为它是简单的。  

**01:17:12 - 01:17:15**  
原文：It was also very inefficient.  
译文：这也非常低效。  

**01:17:15 - 01:17:18**  
原文：For example, encode loops over the merges.  
译文：例如，对合并进行循环编码。  

**01:17:18 - 01:17:22**  
原文：You should only loops over the merges that matter.  
译文：你应该只遍历那些重要的合并。  

**01:17:22 - 01:17:28**  
原文：And there's some other bells and whistles like there's special tokens pre tokenization.  
译文：还有一些其他的附加功能，比如预分词时有特殊的标记。  

**01:17:28 - 01:17:44**  
原文：So in your assignment, you're going to essentially take this as a starting point or I mean, I guess you should implement your own from scratch, but your goal is to make the implementation now fast and you can paralyze it if you want.  
译文：所以在你的作业中，你基本上要把这个作为一个起点，我的意思是，我想你应该从头开始自己实现，但你的目标是让实现变得快速，如果你愿意的话，你也可以让它并行化。  

**01:17:44 - 01:17:46**  
原文：You can go have fun.  
译文：你可以去玩了。  

**01:17:46 - 01:17:47**  
原文：Okay.  
译文：好的。  

**01:17:47 - 01:17:49**  
原文：So summary of tokenization.  
译文：所以，这是分词的总结。  

**01:17:49 - 01:17:53**  
原文：So tokenizer maps between strings and sequences of integers.  
译文：所以tokenizer在字符串和整数序列之间进行映射。  

**01:17:53 - 01:17:56**  
原文：We looked at character base by base, word base.  
译文：我们逐个字符、逐词地进行了查看。  

**01:17:56 - 01:18:00**  
原文：They're are highly suboptimal for various reasons.  
译文：它们由于各种原因非常不理想。  

**01:18:00 - 01:18:07**  
原文：Bpe is a very old algorithm from 94 that still proves to be effective heuristic.  
译文：Bpe 是一种来自 1994 年的非常古老的算法，至今仍被证明是一种有效的启发式方法。  

**01:18:07 - 01:18:19**  
原文：And the important thing is it looks at your corpus statistics to make sensible decisions about how to best adaptively allocate vocabulary to represent sequences of characters.  
译文：而重要的是，它会根据你的语料库统计数据来做出合理的决策，以最佳地自适应分配词汇来表示字符序列。  

**01:18:19 - 01:18:34**  
原文：And you know I hope that one day I won't have to give this lecture because we'll just have architectures that map from bytes, but until then, we'll have to deal with tokenization.  
译文：而且你知道我希望有一天我不再需要讲解这个内容，因为到时候我们会直接有从字节映射的架构，但在那之前，我们还是得处理分词问题。  

**01:18:34 - 01:18:36**  
原文：Okay, so that's it for today.  
译文：好的，那么今天就到这里。  

**01:18:36 - 01:18:45**  
原文：Next time we're going to dive into the details of pe torch and give you the building blocks and pay attention to resource accounting.  
译文：下次我们将深入探讨pe torch的细节，为您提供构建模块，并注意资源核算。  

**01:18:45 - 01:18:52**  
原文：All of you have presumably implemented pe torch programs, but we're going to really look at where all the flops are going.  
译文：你们可能都已经实现了PyTorch程序，但我们将真正仔细看看所有的浮点运算都用到哪里去了。  

**01:18:52 - 01:18:53**  
原文：Okay, see you next time.  
译文：好的，下次见。  



## 相关资源

### 官方链接
- [创作者频道: Stanford Online](https://www.youtube.com/channel/UCBa5G_ESCn8Yd4vw5U-gIcg)
- [原始视频: Stanford CS336 Language Modeling from Scratch I 2025](https://www.youtube.com/watch?v=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_)

### 视频描述中提及的链接
- [链接 1](https://stanford-cs336.github.io/)
- [链接 2](https://online.stanford.edu/courses/cs336-language-modeling-scratch)

### 可能的相关主题
> 根据视频内容搜索更多相关资源

