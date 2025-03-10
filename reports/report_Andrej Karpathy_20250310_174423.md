# 视频翻译处理报告

## 视频信息
- 视频标题：Deep Dive into LLMs like ChatGPT
- 频道/发布者：Andrej Karpathy
- 发布日期：2025-02-05
- 视频长度：03:31:23
- 视频分类：Science & Technology
- 视频ID：7xTGNNLPyMI
- 观看链接：[点击观看原视频](https://www.youtube.com/watch?v=7xTGNNLPyMI)
- 原始语言：en
- 目标语言：中文

![视频缩略图](https://i.ytimg.com/vi/7xTGNNLPyMI/maxresdefault.jpg)


## 处理统计
- 处理时间：2025-03-10 17:44:23 至 2025-03-10 17:44:23
- 音频提取耗时：5分39秒
- 转录耗时：4分54秒
- 翻译耗时：1分33秒
- 内容章节数：1
- 总字数（原文）：40132
- 总字数（译文）：3532


## 内容概览

### 视频主题摘要
<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">
### 大型语言模型（如ChatGPT）的综合性介绍

#### 1. 概述
本视频旨在提供对大型语言模型（LLM）如ChatGPT的综合性但通俗易懂的介绍，帮助你理解这些工具的工作原理及其应用。LLM在某些方面表现出色，但在其他方面仍存在局限性，因此需要谨慎使用。

#### 2. 预训练阶段
预训练阶段是通过互联网上的大量文本数据来训练神经网络，以模拟和生成类似互联网文档的文本。主要步骤包括：
- **数据收集**：从公共来源获取大量高质量、多样化的文本数据。
- **数据处理**：过滤、提取和清理网页内容，确保数据集的质量。
- **分词**：将文本转换为标记（tokens），以便神经网络处理。
- **训练**：使用标记序列训练神经网络，预测下一个标记的概率分布。

#### 3. 监督微调阶段
监督微调阶段通过对话数据集进一步训练模型，使其能够更像人类助手进行对话。具体过程包括：
- **创建对话数据集**：由人工标注员编写提示和理想的回答。
- **微调模型**：让模型学习如何根据上下文生成合适的回应。
- **引入特殊标记**：如搜索功能，使模型能够在需要时访问外部信息。

#### 4. 强化学习阶段
强化学习阶段通过试错和反馈机制进一步优化模型的性能，尤其是在不可验证的任务中。关键点包括：
- **奖励模型**：训练一个独立的神经网络来评估生成结果的质量。
- **间接监督**：通过人类对生成结果的排序，而不是直接评分，来提高数据质量。
- **防止对抗性攻击**：避免模型利用奖励函数的漏洞生成无意义的结果。

#### 5. 认知心理学影响
LLM虽然强大，但仍存在一些认知缺陷，如幻觉（编造事实）、数学推理能力有限等。这些模型依赖于统计模式，而非真正的理解和推理。

#### 6. 实际应用与未来展望
- **多模态能力**：未来的模型将不仅处理文本，还能处理音频和图像。
- **长时间任务执行**：模型将能够执行更复杂的、长时间运行的任务。
- **本地运行**：小型版本的模型可以在个人电脑上本地运行，方便快捷。

#### 7. 总结
当你与ChatGPT等LLM互动时，实际上是在与一个经过复杂训练的神经网络对话。该网络通过模仿人类标注员的行为生成回复，尽管它有时会出错或产生幻觉。因此，应将这些模型视为强大的工具，而不是绝对可靠的系统。

希望这个总结能帮助你更好地理解大型语言模型的工作原理及其潜在的应用和局限性。如果你有任何问题或需要进一步的信息，请随时提问！
</div>


## 关键观点

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">

**1.** 1. 大型语言模型的训练分为三个主要阶段：预训练、监督微调和强化学习，每个阶段对应不同的任务和数据集。

**2.** 2. 预训练阶段通过处理大量互联网文本数据，将这些文本转换为标记序列，使模型能够内化并模拟文本的流动方式，从而形成基础模型。

**3.** 3. 监督微调阶段使用对话数据集对基础模型进行调整，使其具备助手功能，能够回答问题并进行多轮次对话，提升其实用性。

**4.** 4. 强化学习阶段通过试错机制优化模型的表现，特别是在不可验证的任务中，如创意写作，利用人类反馈来改进模型生成的内容质量。

**5.** 5. 模型在推理过程中依赖于其内部参数和上下文窗口中的标记序列，尽管表现出色，但仍存在幻觉等问题，用户应谨慎使用并检查结果。

</div>



## 完整对照翻译

**00:00:00 - 00:00:00**  
原文：Everyone.  
译文：每个人。  

**00:00:00 - 00:00:03**  
原文：So I wanted to make this video for a while.  
译文：所以我想要制作这个视频已经有一段时间了。  

**00:00:03 - 00:00:09**  
原文：It is a comprehensive but general audience introduction to large language models like ChatGPT.  
译文：这是对像ChatGPT这样的大型语言模型的综合性但通俗易懂的介绍。  

**00:00:09 - 00:00:17**  
原文：And what I'm hoping to achieve in this video is to give you kind of mental models for thinking through what it is that this tool is.  
译文：并且我希望在这个视频中达成的目标 是给你一种思维模型 来思考这个工具究竟是什么。  

**00:00:17 - 00:00:20**  
原文：It is obviously magical and amazing in some respects.  
译文：在某些方面，它显然是神奇且令人惊叹的。  

**00:00:20 - 00:00:24**  
原文：It's really good at some things, not very good at other things.  
译文：它在某些事情上真的很擅长，而在其他事情上不是很擅长。  

**00:00:24 - 00:00:27**  
原文：And there's also a lot of sharp edges to be aware of.  
译文：而且还有很多尖锐的边缘需要注意。  

**00:00:27 - 00:00:28**  
原文：So what is behind this text box?  
译文：那么，这个文本框背后有什么呢？  

**00:00:28 - 00:00:32**  
原文：You can put anything in there and Press enter.  
译文：您可以将任何内容放在那里，然后按回车键。  

**00:00:32 - 00:00:33**  
原文：But what should be put in there?  
译文：但是应该把什么放进去呢？  

**00:00:33 - 00:00:35**  
原文：And what are these words generated back?  
译文：那么，这些词是如何生成的呢？  

**00:00:35 - 00:00:38**  
原文：How does this work and what are you talking to exactly?  
译文：这是如何工作的，以及你究竟在跟谁说话？  

**00:00:38 - 00:00:41**  
原文：So I'm hoping to get at all those topics in this video.  
译文：所以希望在本视频中涵盖所有这些话题。  

**00:00:41 - 00:00:49**  
原文：We're going to go through the entire pipeline of how this stuff is built, but I'm going to keep everything sort of accessible to a general audience.  
译文：我们将要经历这一整套构建流程， 但是我将会以一个比较大众化的方式来讲解一切。  

**00:00:49 - 00:00:53**  
原文：So let's take a look at first how you build something like chagpt.  
译文：那么，让我们首先看看你是如何构建像chagpt这样的东西的。  

**00:00:53 - 00:01:00**  
原文：And along the way, I'm going to talk about you know some of the sort of cognitive psychological implications of these tools.  
译文：沿途，我会谈谈这些工具的 一些认知心理学上的影响。  

**00:01:00 - 00:01:02**  
原文：Okay, so let's build chagpt t.  
译文：好的，那么让我们来构建chagpt t。  

**00:01:02 - 00:01:06**  
原文：So there's going to be multiple stages arranged sequentially.  
译文：所以将会有多个阶段依次排列。  

**00:01:06 - 00:01:09**  
原文：The first stage is called the pre training stage.  
译文：第一阶段称为预训练阶段。  

**00:01:09 - 00:01:13**  
原文：And the first step of the pre training stage is to download and process the Internet.  
译文：预训练阶段的第一步是下载和处理互联网数据。  

**00:01:13 - 00:01:18**  
原文：Now to get a sense of what this roughly looks like, I recommend looking at this url here.  
译文：现在要大致了解一下这看起来像什么，我建议看一下这里的这个网址。  

**00:01:18 - 00:01:24**  
原文：So this company called hugging face collected and created and curated this dataset called fine web.  
译文：所以，一家名为Hugging Face的公司收集、创建并整理了这个名为Fine Web的数据集。  

**00:01:24 - 00:01:30**  
原文：And they go into a lot of detail in this bloackpost on how they constructed the fine web data set.  
译文：他们在有关如何构建精细网络数据集的博客文章中进行了大量详细说明。  

**00:01:30 - 00:01:39**  
原文：And all of the major llm providers like OpenAI, anthropic and gooand so on, will have some equivalent internally off something like the fine web data set.  
译文：并且所有主要的大型语言模型提供商，比如 OpenAI、Anthropic 和 Google 等等，都会有一些类似于精调网络数据集的内部等价物。  

**00:01:39 - 00:01:42**  
原文：So roughly what are we trying to achieve here?  
译文：所以，我们在这里大致上尝试做什么？  

**00:01:42 - 00:01:47**  
原文：We're trying to get a ton of text from the Internet, from publicly available sources.  
译文：我们正试图从互联网上，从公共可用的来源获取大量文本。  

**00:01:47 - 00:01:51**  
原文：So we're trying to have a huge quantity of very high quality documents.  
译文：所以我们正在努力拥有大量非常高质量的文件。  

**00:01:51 - 00:01:57**  
原文：And we also want very large diversity of documents because we want to have a lot of knowledge inside these models.  
译文：而且我们还希望文档的多样性非常大，因为我们希望这些模型内部包含大量的知识。  

**00:01:57 - 00:02:02**  
原文：So we want large diversity of high quality documents, and we want many, many of them.  
译文：所以我们需要大量高质量文档的多样性，而且我们希望有非常多这样的文档。  

**00:02:02 - 00:02:07**  
原文：And achieving this is quite complicated and as you can see here, takes multiple stages to do well.  
译文：如你所见，要实现这一点相当复杂，而且要做好它需要多个阶段。  

**00:02:07 - 00:02:11**  
原文：So let's take a look at what some of these stages look like in a bit.  
译文：所以让我们稍后看一下这些阶段中的一些是什么样子。  

**00:02:11 - 00:02:22**  
原文：For now, I'd like to just like to note that, for example, the fine web dataset, which is fairly representative, what you would see in a production grade application, actually ends up being only about 44 tb of disk space.  
译文：目前，我只想指出，例如，精细的网络数据集，这是一个相当有代表性的数据集，你在生产级别的应用程序中看到的情况，实际上最终只占大约44TB的磁盘空间。  

**00:02:22 - 00:02:28**  
原文：You can get a usb stick for like a terabyte very easily, or I think this could fit on a single hard drive almost today.  
译文：你现在可以很轻松地获得一个容量为一太字节的优盘，或者我认为这几乎可以放在一个硬盘上。  

**00:02:28 - 00:02:37**  
原文：So this is not a huge amount of data at the end of the day, even though the Internet is very, very large, we're working with text and we're also filtering it aggressively.  
译文：所以这在一天结束时并不是一个巨大的数据量，即使互联网非常非常大，我们处理的是文本，而且我们也对其进行严格的过滤。  

**00:02:37 - 00:02:40**  
原文：So we end up with about 44 tb in this example.  
译文：所以我们在这个例子中最终得到大约44 TB。  

**00:02:40 - 00:02:46**  
原文：So let's take a look at kind of what this data looks like and what some of these stages also are.  
译文：所以让我们来看一下这些数据的大致样子以及其中一些阶段是什么。  

**00:02:46 - 00:02:54**  
原文：So the starting point for a lot of these efforts, and something that contributes most of the data by the end of it, is data from common curroll.  
译文：所以，许多这些努力的起点，以及最终提供大部分数据的，是来自常见课程的数据。  

**00:02:54 - 00:03:00**  
原文：So common curroll is an organization that has been basically scouring the Internet since 2007.  
译文：所以，Common Curroll 是一个组织，自2007年以来，基本上一直在梳理互联网。  

**00:03:00 - 00:03:09**  
原文：So as of 2024, for example, common curl has indexed 2.7 billion web pages, and they have all these crawlers going around the Internet.  
译文：因此，截至2024年，例如，通用curl已经索引了27亿个网页，而且它们有大量的爬虫在互联网上运行。  

**00:03:09 - 00:03:21**  
原文：And what you end up doing basically is you start with a few seed web pages, and then you follow all the links and you just keep following links and you keep indexing all the information, and you end up with a ton of data off the Internet over time.  
译文：你最终所做的基本上是 从几个种子网页开始，然后跟随所有的链接，你不断地跟随链接并持续索引所有信息， 随着时间的推移，你最终会从互联网上 获取到大量的数据。  

**00:03:21 - 00:03:25**  
原文：So this is usually the starting point lot the for a lot of these efforts.  
译文：所以这通常是这些努力的起点。  

（注意：原始句子中存在语法错误，“lot the for”应为“for a lot of”，在翻译时已进行修正以确保语句通顺。）  

**00:03:25 - 00:03:29**  
原文：Now, this common cordata is quite raw and is filtered in many, many different ways.  
译文：现在，这种常见的原始数据经过了多种多样的过滤处理。  

**00:03:29 - 00:03:32**  
原文：So here they document the same diagram.  
译文：所以这里他们记录了相同的图表。  

**00:03:32 - 00:03:38**  
原文：They document a little bit the kind of processing that happens in these stages.  
译文：他们稍微记录了这些阶段中发生的一些处理过程。  

**00:03:38 - 00:03:42**  
原文：So the first thing here is something called url filtering.  
译文：所以这里的第一件事是叫做 URL 过滤。  

**00:03:42 - 00:03:52**  
原文：So what that is referring to is that there these block lists of basically urls that are or domains that you don't want to be getting data from.  
译文：所以，这指的是存在一些基本上由你不想从中获取数据的URL或域名组成的阻止列表。  

**00:03:52 - 00:04:00**  
原文：So usually this includes things like malwweb sites, spam web sites, marketing web sites, racist web sites, adult sites and things like that.  
译文：[翻译失败: 翻译错误: status_code: 400 
 code: DataInspectionFailed 
 message: Output data may contain inappropriate content.]  

**00:04:00 - 00:04:08**  
原文：So there's a ton of different types of web sites that are just eliminated at this stage because we don't want them in our data set.  
译文：所以，有很多不同类型的网站在这个阶段直接被排除，因为我们不希望它们出现在我们的数据集中。  

**00:04:08 - 00:04:10**  
原文：The second part is text extraction.  
译文：第二部分是文本提取。  

**00:04:10 - 00:04:16**  
原文：You have to remember that all these web pages, this is the raw html of these web pages that are being saved by these crawlers.  
译文：你必须记住，所有这些网页，这就是被这些爬虫程序保存的原始HTML代码。  

**00:04:16 - 00:04:28**  
原文：So when I go to inspect here, this is what the raw html actually looks like, you'll notice that it's got all this markup like lists and stuff like that, and there's css and all this kind of stuff.  
译文：所以当我在这里检查时，这就是实际的原始HTML看起来的样子，你会注意到它有所有这些标记，比如列表之类的，而且还有CSS和诸如此类的东西。  

**00:04:28 - 00:04:31**  
原文：So this is computer code almost for these web pages.  
译文：所以这几乎就是这些网页的计算机代码。  

**00:04:31 - 00:04:34**  
原文：But what we really want is we just want this text, right?  
译文：但我们真正想要的只是这段文字，对吧？  

**00:04:34 - 00:04:39**  
原文：We just want the text of this web page, and we don't want the navigation and things like that.  
译文：我们只要这个网页的文本，而不想要导航等其他内容。  

**00:04:39 - 00:04:48**  
原文：There's a lot of filtering and processing and heuristics that go into adequately filtering for just the good content of these web pages.  
译文：要充分过滤这些网页以获取优质内容， 需要做大量的筛选、处理和运用启发式方法。  

**00:04:48 - 00:04:51**  
原文：The next stage here is language filtering.  
译文：下一阶段是语言过滤。  

**00:04:51 - 00:04:55**  
原文：So for example, fine web filters using a language classifier.  
译文：所以，例如，使用语言分类器来改进网络过滤器。  

**00:04:55 - 00:05:04**  
原文：They try to guess what language every single web page is in, and then they only keep web pages that have more than 65% of English as an example.  
译文：他们尝试猜测每个网页使用的语言， 然后只保留英语内容超过65%的网页作为例子。  

**00:05:04 - 00:05:10**  
原文：And so you can get a sense that this is like a design decision that different companies can take for themselves.  
译文：因此，你可以感觉到这就像一个设计决策，不同的公司可以自行决定。  

**00:05:10 - 00:05:15**  
原文：What fraction of all different types of languages are we going to include in our data, aset?  
译文：我们将要包含在我们的数据集中的一切不同类型的语言所占的比例是多少？  

**00:05:15 - 00:05:25**  
原文：Because, for example, if we filter out all of the Spanish as an example, then you might imagine that our model later will not be very good at Spanish because you've just never seen that much data of that language.  
译文：因为，例如，如果我们把所有的西班牙语都过滤掉作为例子，那么你可以想象，我们的模型后来在西班牙语方面可能不会很好，因为你从未见过那么多这种语言的数据。  

**00:05:25 - 00:05:29**  
原文：And so different companies can focus on multilingual performance to a different degree.  
译文：因此，不同的公司可以不同程度地专注于多语言性能。  

**00:05:29 - 00:05:32**  
原文：As an example, the fine web is quite focused on English.  
译文：例如，该精细网络相当专注于英语。  

**00:05:32 - 00:05:39**  
原文：And so their language model, if they end up training one later, will be very good at English, but not maybe very good at other languages.  
译文：因此，他们的语言模型，如果他们后来训练了一个，将会非常擅长英语，但可能不会非常擅长其他语言。  

**00:05:40 - 00:05:48**  
原文：After language filtering, there's a few other filtering steps and deduplication and things like that, finishing with, for example, the pii removal.  
译文：在语言过滤之后，还有几个其他的过滤步骤，例如去重等，最后进行个人身份信息（pii）的移除。  

**00:05:48 - 00:05:51**  
原文：This is personally identifiable information.  
译文：这是个人可识别信息。  

**00:05:51 - 00:06:00**  
原文：So as an example, addresses social security numbers and things like that, you will try to detect them and you will try to filter out those kinds of web pages from the data set as well.  
译文：所以作为一个例子，像地址、社会保障号码之类的信息，您将尝试检测它们，并且您也将尝试过滤掉数据集中包含这类信息的网页。  

**00:06:00 - 00:06:07**  
原文：So there's a lot of stages here, and I won't go into full detail, but it is a fairly extensive part of the pprocessing.  
译文：所以这里有很多阶段，我不会详细说明，但这是处理过程中的一个相当广泛的部分。  

**00:06:07 - 00:06:10**  
原文：And you end up with, for example, definine web data set.  
译文：最终，例如，定义网络数据集。  

**00:06:10 - 00:06:16**  
原文：So when you click in on it, you can see some examples here of what this actually ends up looking like.  
译文：所以当你点击它时，你可以在这里看到一些实际效果的例子。  

**00:06:16 - 00:06:20**  
原文：And anyone can downon this on the huging phase web page.  
译文：任何人都可以在 hugs 网页的相位页面上对此进行下载。 

注：原文中有拼写或语法错误，"hugging phase web page" 可能是指某个特定网站（如 Hugging Face）的页面，建议确认原文准确性。如果"Hugging Face"是正确名称，那么更正后的翻译如下：

任何人都可以在 Hugging Face 网页的相位页面上对此进行下载。  

**00:06:20 - 00:06:24**  
原文：And so here's some examples of the final text that ends up in the training set.  
译文：以下是一些最终文本的例子，这些文本最终进入了训练集。  

**00:06:24 - 00:06:28**  
原文：So this is some article about tornadoes in 2012.  
译文：所以这是一篇关于2012年龙卷风的文章。  

**00:06:28 - 00:06:32**  
原文：So there's some tornadoes in 20, 20, in 2012.  
译文：所以2012年有一些龙卷风。  

**00:06:32 - 00:06:33**  
原文：And what happened?  
译文：然后发生了什么？  

**00:06:33 - 00:06:42**  
原文：This next one is something about, did you know you have two little yellow nine volt battery sized adrenal gens in your body?  
译文：接下来这一项是关于，你知道你的身体里有两个小黄的九伏电池大小的肾上腺吗？  

**00:06:42 - 00:06:46**  
原文：Okay, so there's some kind of a odd medical article.  
译文：好的，那么这是一篇有些奇怪的医学文章。  

**00:06:47 - 00:06:54**  
原文：So just think of these as basically web pages on the Internet, filtered just for the text in various ways.  
译文：所以，就将这些基本上视为互联网上的网页，只是以各种方式过滤了文本。  

**00:06:54 - 00:06:57**  
原文：And now we have a ton of text, 40 tb off it.  
译文：而现在我们有大量文本，40太字节之多。  

**00:06:57 - 00:07:00**  
原文：And that now is the starting point for the next step of this stage.  
译文：这是下一阶段步骤的起点。  

**00:07:00 - 00:07:04**  
原文：Now, I wanted to give you an intuitive sense of where we are right now.  
译文：现在，我想给你一个关于我们目前所处位置的直观感受。  

**00:07:04 - 00:07:08**  
原文：So I took the first 200 web pages here, and remember, we have tons of them.  
译文：所以我在这里取了前200个网页， 记住，我们有很多这样的网页。  

**00:07:08 - 00:07:13**  
原文：And I just take all that text, and I just put it all together concatenated.  
译文：我刚刚把所有那些文本取来，然后我把它们全部拼接在一起。  

**00:07:13 - 00:07:15**  
原文：And so this is what we end up with.  
译文：所以，这就是我们最终得到的结果。  

**00:07:15 - 00:07:22**  
原文：We just get this just raw text, raw Internet text, and there's a ton of it even in these 200 web pages.  
译文：我们刚刚获取了这些原始文本，原始的互联网文本，即使在这200个网页中也有大量的文本。  

**00:07:22 - 00:07:24**  
原文：So I can continue zooming out here.  
译文：所以我可以在这里继续放大。 

注：根据上下文，“zooming out”通常指的是“缩小”视图，但直译为“放大”在某些情况下也能通顺表达，如照片或视频的特效处理。 若要更准确地反映常规用法，应翻译为“所以我可以在这里继续缩小视图。” 请根据具体应用场景选择合适的翻译。 

如果你确认是希望表达“缩小”的概念，请使用：
所以我可以在这里继续缩小视图。  

**00:07:24 - 00:07:27**  
原文：And we just have this like massive tapestry of text data.  
译文：我们只是拥有这样庞大如织锦般的文本数据。  

**00:07:27 - 00:07:29**  
原文：And this text data has all these patterns.  
译文：而且这些文本数据具有所有这些模式。  

**00:07:29 - 00:07:39**  
原文：And what we want to do now is we want to start training neural networks on this data so the neural works can internalize and model how this text flows, right?  
译文：我们现在想要做的是开始在这个数据上训练神经网络，以便神经网络能够内化并模拟这段文本的流动方式，对吧？  

**00:07:39 - 00:07:45**  
原文：So we just have this giant texture of text, and now we want to get neural nots that mimic it.  
译文：所以我们现在有这个巨大的文本纹理，接下来我们想要获得模仿它的神经元笔记。  

（注：根据上下文，“neural nots”可能是指“neural notes”或某种特定技术术语，直译为“神经元笔记”或“神经元节点”。如果存在特定的技术背景，请提供更多上下文以便更准确翻译。）  

**00:07:45 - 00:07:46**  
原文：Okay.  
译文：好的。  

**00:07:46 - 00:07:54**  
原文：Now before we plug text into neural networks, we have to decide how we're going to represent this text and how we're going to feed it in.  
译文：现在，在我们将文本输入神经网络之前，我们必须决定我们如何表示这段文本以及我们如何将其输入。  

**00:07:54 - 00:08:06**  
原文：Now, the way our technology works for these neural lots is that they expect a one dimensional sequence of symbols, and they want a finite set of symbols that are possible.  
译文：现在，我们的技术针对这些神经网络的工作方式是，它们期望一个一维的符号序列，并且它们需要一个有限的可能符号集。  

**00:08:06 - 00:08:14**  
原文：And so we have to decide what are the symbols, and then we have to represent our data as one dimensional sequence of those symbols.  
译文：因此，我们必须决定符号是什么，然后我们必须将我们的数据表示为这些符号的一维序列。  

**00:08:14 - 00:08:18**  
原文：So right now, what we have is a one dimensional sequence of text.  
译文：所以现在，我们有的是一个一维的文本序列。  

**00:08:18 - 00:08:22**  
原文：It starts here and it goes here, and then it comes here, etc..  
译文：它从这里开始，然后到这里，再然后回到这里，等等。  

**00:08:22 - 00:08:30**  
原文：So this is one dimensional sequence, even though on my monitor, of course, it's laid out in a two dimensional way, but it goes from left to right and top to bottom right.  
译文：所以这是一个一维序列，即使在我的显示器上，当然，它是以二维方式排列的，但它是从左到右和从上到下排列的。  

**00:08:30 - 00:08:32**  
原文：So it's a one dimensional sequence of text.  
译文：所以它是一维的文本序列。  

**00:08:32 - 00:08:36**  
原文：Now this being computers, of course there's an underlying representation here.  
译文：当然，因为这是计算机，这里肯定有底层的表示。  

**00:08:36 - 00:08:45**  
原文：So if I do what's called ufeight encode this text, then I can get the raw bits that correspond to this text in the computer.  
译文：所以如果我进行所谓的 Ufeight 编码这一文本，那么我就可以得到对应的原始位，在计算机中表现为这段文本。  

**00:08:45 - 00:08:47**  
原文：And what that looks like this.  
译文：看起来是这样的。  

**00:08:47 - 00:08:56**  
原文：So it turns out that, for example, this very first bar here is the first eight bits as an example.  
译文：所以结果是，例如，这里非常第一根条形是前八个位元作为一个例子。 

注：此句中文翻译在语义上有些不通顺，可能是由于原文表述特殊或存在口语化表达。更通顺的翻译可以是：

所以结果是，例如，这里的第一个条形代表的是前八个比特（bit）。  

**00:08:56 - 00:08:58**  
原文：So what is this thing, right?  
译文：那么这东西是什么呢，对吧？  

**00:08:58 - 00:09:04**  
原文：This is a representation that we are looking for in a certain sense.  
译文：这是我们在某种意义上正在寻找的表示。  

**00:09:04 - 00:09:10**  
原文：We have exactly two possible symbols, zero and one, and we have a very long sequence of it right now.  
译文：我们正好有两个可能的符号，零和一，而现在我们有一个非常长的序列。  

**00:09:10 - 00:09:19**  
原文：As it turns out, this sequence length is actually going to be a very finite and precious resource in our neural network.  
译文：事实证明，这个序列长度实际上将成为我们神经网络中非常有限且宝贵的资源。  

**00:09:19 - 00:09:24**  
原文：And we actually don't want extremely long sequences of just two symbols.  
译文：实际上，我们不希望有极长的序列只包含两个符号。  

**00:09:24 - 00:09:33**  
原文：Instead, what we want is we want to trade off this symbol size of this vocabulary, as we call it, and the resulting sequence length.  
译文：相反，我们希望的是权衡这个我们称之为词汇表的符号大小和由此产生的序列长度。  

**00:09:33 - 00:09:38**  
原文：So we don't want just two symbols and extremely long sequences.  
译文：所以我们不希望只有两个符号和极其长的序列。  

**00:09:38 - 00:09:41**  
原文：We're going to want more symbols and shorter sequences.  
译文：我们将需要更多的符号和更短的序列。  

**00:09:41 - 00:09:56**  
原文：Okay, so one naive way of compressing or decreasing the length of our sequhere is to basically consider some group of consecutive bits, for example, eight bits, and group them into a single, what's called byte.  
译文：好的，那么一种朴素的压缩或减少我们序列长度的方法是基本上考虑一些连续的位，例如，八个位，并将它们组合成一个被称为字节的单元。  

**00:09:56 - 00:10:07**  
原文：So because these bits are either on or off, if we take a group of eight of them, there turns out to be only 256 possible combinations of how these bits can be on or off.  
译文：所以因为这些位要么开要么关，如果我们把八个位组成一组，就会发现只有256种可能的组合来表示这些位的开或关状态。  

**00:10:07 - 00:10:12**  
原文：And so therefore, we can rerepresent this sequence into a sequence of bytes instead.  
译文：因此，我们可以将这个序列重新表示为一系列字节。  

**00:10:12 - 00:10:15**  
原文：So this sequence of bytes will be eight times shorter.  
译文：所以这串字节将会缩短八倍。  

**00:10:15 - 00:10:18**  
原文：But now we have 256 possible symbols.  
译文：但现在我们有256个可能的符号。  

**00:10:18 - 00:10:22**  
原文：So every number here goes from zero to 255.  
译文：所以这里的每个数字都是从0到255。  

**00:10:22 - 00:10:28**  
原文：Now I really encourage you to think of these not as numbers, but as unique ids or like unique symbols.  
译文：现在我强烈建议你不要把这些看作数字，而是把它们当作唯一的标识符或独特的符号。  

**00:10:28 - 00:10:35**  
原文：So maybe it's a bit more, maybe it's better to actually think of these, to replace every one of these with a unique emoji, youget, something like this.  
译文：所以也许这会更多一点，也许实际上应该考虑将这些都替换成独特的表情符号，你明白吧，就像这样。  

**00:10:35 - 00:10:40**  
原文：So we basically have a sequence of emoges, and there's 256 possible emojis.  
译文：所以我们基本上有一系列的emoji，总共有256种可能的emoji。  

**00:10:40 - 00:10:42**  
原文：You can think of it that way.  
译文：你可以这样想。  

**00:10:42 - 00:10:49**  
原文：Now it turns out that in production for state of the art language models, you actually want to go even beyond this.  
译文：现在 Turns out 表明，对于最先进的语言模型的生产而言，你实际上希望走得更远。 

（注：为了保持原始格式，"Turns out" 保留了原文的位置，但在中文中，这句话会更通顺：“现在发现，对于最先进的语言模型的生产而言，你实际上希望走得更远。”）  

**00:10:49 - 00:10:58**  
原文：You want to continue to shrink the length of the sequence because, again, it is a precious resource in return for more symbols in your vocabulary.  
译文：你想要继续缩短序列的长度，因为，再次强调，它是宝贵的资源，以换取词汇表中更多的符号。  

**00:10:58 - 00:11:04**  
原文：And the way this is done is done by running what's called the byte pair encoding algorithm.  
译文：这是通过运行所谓的字节对编码算法来完成的。  

**00:11:04 - 00:11:10**  
原文：And the way this works is we're basically looking for consecutive bytes or symbols that are very common.  
译文：其工作原理是，我们基本上是在寻找 连续的字节或符号，这些字节或符号非常常见。  

**00:11:10 - 00:11:19**  
原文：So for example, turns out that the sequence 116 followed by 32 is quite common and occurs very frequently.  
译文：所以，例如，事实证明序列116后面跟着32是相当常见的，并且出现的频率非常高。  

**00:11:19 - 00:11:23**  
原文：So what we're going to do is we're going to group this pair into a new symbol.  
译文：所以我们要做的是，我们将这对组合成一个新符号。  

**00:11:23 - 00:11:33**  
原文：So we're going to mint a symbol with an ID 256, and we're going to rewrite every single pair, 116, 32 with this new symbol.  
译文：所以我们将铸造一个ID为256的符号，然后我们将会重写每一组配对，116，32，使用这个新符号。  

**00:11:33 - 00:11:37**  
原文：And we can iterate this algorithm as many times as we wish.  
译文：而且我们可以根据需要迭代此算法任意多次。  

**00:11:37 - 00:11:44**  
原文：And each time when we mint a new symbol, we're decreasing the length and we're increasing the symbol size.  
译文：每次我们铸造一个新的符号时，我们都在减少长度并增加符号的大小。  

**00:11:44 - 00:11:53**  
原文：And in practice, it turns out that a pretty good setting of basically the vocabulary size turns out to be about 100000 possible symbols.  
译文：实际上，结果证明  
基本上词汇量大小的一个相当好的设定  
结果是大约有100,000个可能的符号。  
  
（注：为了保持原始格式，此处保留了原文的断句方式，但根据中文表达习惯稍作调整以确保语义清晰。）  

**00:11:53 - 00:11:58**  
原文：So in particular, GPT -4 uses 100277 symbols.  
译文：所以，特别是，GPT-4 使用了 100277 个符号。  

**00:11:58 - 00:12:08**  
原文：And this process of converting from raw text into these symbols, or as we call them, tokens, is the process called tokenzation.  
译文：将原始文本转换为这些符号，或者我们称之为 token 的过程，被称为分词（tokenization）。  

**00:12:08 - 00:12:19**  
原文：So let's now take a look at how GPT -4 performs tokenization converting from text to tokens and from tokens back to text, and what this actually looks like.  
译文：那么，现在让我们来看看GPT-4是如何进行分词的，即从文本转换为分词，再从分词转换回文本，以及这实际上是什么样子。  

**00:12:19 - 00:12:26**  
原文：So one web site I like to use to explore these token representations is called tick tokenzer.  
译文：所以我喜欢用来探索这些 token 表示的一个网站叫做 tick tokenzer。  

**00:12:26 - 00:12:34**  
原文：And so come here through the drop down and select cl 100k base, which is the GPT -4 base model tokenzer.  
译文：然后通过下拉菜单来到这里，选择 cl 100k base，这是 GPT-4 基础模型的分词器。  

**00:12:34 - 00:12:40**  
原文：And here on the left, you can put in text and it shows you the tokenization of that text.  
译文：在此左侧，您可以输入文本，它会显示该文本的分词结果。  

**00:12:40 - 00:12:42**  
原文：So for example, have low space.  
译文：所以，例如，空间很小。  

**00:12:44 - 00:12:58**  
原文：So hello world turns out to be exactly two tokens, the token hello, which is the token with ID 15339, and the token space world, that is the token 1917.  
译文：所以 "hello world" 结果恰好是两个标记，标记 "hello"，其是 ID 为 15339 的标记，以及空格后的标记 "world"，即标记 1917。  

**00:12:58 - 00:13:00**  
原文：So hello space world.  
译文：所以，你好，太空世界。  

**00:13:00 - 00:13:18**  
原文：Now if I was to join these two, for example, I'm going to get again two tokens, but it's the token H followed by the token hello world without the H, if I put in two spaces here between hello and world, it's again a different tokenization.  
译文：现在，如果我将这两个连接起来，例如，我将会再次得到两个标记，但它是标记 H 接着是不带 H 的 "hello world" 的标记。如果我在 "hello" 和 "world" 之间放入两个空格，它又会是不同的分词结果。  

**00:13:18 - 00:13:21**  
原文：There's a new token 220 here.  
译文：这里有一个新的代币220。  

**00:13:22 - 00:13:25**  
原文：Okay, so you can play with this and see what happens here.  
译文：好的，你可以玩这个并看看这里会发生什么。  

**00:13:25 - 00:13:29**  
原文：Also keep in mind this is not, this is case sensitive.  
译文：另外请记住，这不是，这是区分大小写的。  

**00:13:29 - 00:13:38**  
原文：So if this is a capital H, it is something else or if it's hello world, then actually this ends up being three tokens since there are just two tokens.  
译文：所以如果这是一个大写的H，它就是其他东西，或者如果是hello world，那么实际上这最终会变成三个标记，因为这里只有两个标记。 

注：此句逻辑似乎有些混淆，最后一句“因为这里只有两个标记”与前面内容存在矛盾。原始文本可能有误。 若要保持原意，请确认原文本的准确性。  

**00:13:41 - 00:13:47**  
原文：Yeah so you can play with this and get a sort of like an intuitive sense of what these tokens work like.  
译文：是的，你可以玩这个，并对这些令牌的工作方式有一种直观的感觉。  

**00:13:47 - 00:13:52**  
原文：We're actually going to loop around to tokization a bit later in the video for now.  
译文：我们实际上将在视频的稍后部分回到分词的话题，现在先不讨论。  

**00:13:52 - 00:14:02**  
原文：I just wanted to show you the web site and I wanted to show you that this text basically at the end of the day, so for example, if I take one line here, this is where GPT -4 will see it as.  
译文：我只是想给您展示这个网站，还想让您看到这段文字最终会如何呈现。所以，例如，如果我在这里选取一行，这就是GPT-4将会看到的内容。  

**00:14:02 - 00:14:05**  
原文：So this text will be a sequence of length 62.  
译文：所以这段文本将是长度为62的序列。  

**00:14:05 - 00:14:07**  
原文：This is the sequence here.  
译文：这是这里的序列。  

**00:14:07 - 00:14:11**  
原文：And this is how the chunks of text correspond ds to these symbols.  
译文：这就是文本块如何对应于这些符号。  

**00:14:11 - 00:14:18**  
原文：And again, there's 100000, 270, 70, 77, the possible symbols.  
译文：再次重申，这里有100000、270、70、77，这些是可能的符号。  

**00:14:18 - 00:14:22**  
原文：And we now have one dimensional sequences of those symbols.  
译文：现在我们有了那些符号的一维序列。  

**00:14:22 - 00:14:27**  
原文：So Yeah, we're going to come back to tokenization, but that's for now where we are.  
译文：所以是的，我们将回到分词的话题，但那是我们目前所处的位置。  

**00:14:27 - 00:14:37**  
原文：Okay, so what I've done now is I've taken this sequence of text that we have here in the datset, and I have re represented it using our tokenzer into a sequence of tokens.  
译文：好的，我所做的是将我们在这个数据集中看到的这段文本，使用我们的分词器重新表示为一串令牌。  

**00:14:37 - 00:14:39**  
原文：And this is what that looks like now.  
译文：这就是它现在的样子。  

**00:14:39 - 00:14:50**  
原文：So for example, when we go back to the fine web data set, they mentioned that not only is this 44 tb at disc space, but this is about a 15 trillion token sequence of in this data set.  
译文：所以，例如，当我们回到精细的网络数据集时，他们提到这不仅是有44TB的磁盘空间，而且这个数据集中大约有15万亿个令牌序列。  

**00:14:50 - 00:15:02**  
原文：And so here, these are just some of the first one or two or three or a few thousand here, I think, tokens off this data set, but there's 15 trillion here to keep in mind.  
译文：所以在这里，这只是这个数据集中的一些最初的几个或几千个标记，但我认为这里要记住的是有15万亿个。  

**00:15:02 - 00:15:07**  
原文：And again, keep in mind one more time that all of these represent little text chunks.  
译文：并且再次注意，所有这些都代表小的文本块。  

**00:15:07 - 00:15:10**  
原文：They're all this like atoms of these sequences.  
译文：它们都像这些序列的原子。  

**00:15:10 - 00:15:13**  
原文：And the numbers here don't make any sense.  
译文：而且这里的数字没有任何意义。  

**00:15:13 - 00:15:15**  
原文：They're just they're just unique.  
译文：它们就是它们就是独一无二的。  

**00:15:15 - 00:15:21**  
原文：Ids, okay, so now we get to the thumb part, which is the neural network training.  
译文：Ids，好的，那么现在我们来讲拇指部分，也就是神经网络的训练。  

**00:15:21 - 00:15:28**  
原文：And this is where a lot of the heavy lifting happens computationally when you're training these neural networks.  
译文：这就是在训练这些神经网络时 计算上进行大量 heavy lifting 的地方。  

（注：这里的 "heavy lifting" 是个习语，直译为“繁重的工作”，根据上下文可理解为“大量的计算工作”或“核心计算部分”。）  

如果你希望更自然的表达，可以翻译为：
这就是在训练这些神经网络时 进行大量核心计算的地方。  

**00:15:28 - 00:15:36**  
原文：So what we do here in this step is we want to model the statistical relationships of how these tokens follow each other in the sequence.  
译文：所以在这一步骤中，我们想要建模这些 token 在序列中相互跟随的统计关系。  

**00:15:36 - 00:15:41**  
原文：So what we do is we come into the data and we take windows of tokens.  
译文：所以我们所做的就是进入数据，然后我们取一系列的标记窗口。  

**00:15:41 - 00:15:55**  
原文：So we take a window of tokens from this data fairly randomly, and the windows length can range anywhere between zero tokens, actually all the way up to some maximum size that we decide on.  
译文：所以我们从这些数据中相当随机地取出一个令牌窗口，窗口的长度可以在零个令牌到我们决定的最大尺寸之间变化。  

**00:15:55 - 00:16:02**  
原文：So for example, in practice, you could see a token windows of, say, 8000 tokens.  
译文：所以，例如，在实际应用中，您可能会看到一个令牌窗口，比如说，8000个令牌。  

**00:16:02 - 00:16:15**  
原文：Now, in principle, we can use arbitrary window lengths of tokens, but processing very long, basically window dows sequences would just be very computationally expensive.  
译文：现在，原则上，我们可以使用任意长度的 token 窗口，但是处理非常长的窗口序列，基本上会变得计算成本非常高。  

**00:16:15 - 00:16:22**  
原文：So we just kind of decide that, say, 8000 is a good number, or 4000 or 16000, and we crop it there.  
译文：所以我们只是简单地决定，比如说，8000是一个好数字，或者4000，或者16000，然后我们就在这里截断。  

**00:16:22 - 00:16:28**  
原文：Now in this example, I'm going to be taking the first four tokens just so everything fits nicely.  
译文：现在在这个例子中，我将只取前四个标记，这样一切都能很好地契合。  

**00:16:28 - 00:16:39**  
原文：So these tokens, we're going to take a window of four tokens, this bar, view in and space single, which are these token ids?  
译文：所以这些标记，我们将取四个标记的一个窗口，即这根条形、视图、in和空格single，那么这些都是哪些标记ID呢？  

**00:16:39 - 00:16:47**  
原文：And now what we're trying to do here is we're trying to basically predict the token that comes next in a sequence.  
译文：现在我们在这里尝试做的事情是，我们基本上试图预测序列中下一个会出现的令牌。  

**00:16:47 - 00:16:49**  
原文：So three, nine, six, two comes next, right?  
译文：所以接下来是三、九、六、二，对吗？  

**00:16:49 - 00:16:52**  
原文：So what we do now here is that we call this the context.  
译文：所以我们现在在这里所做的就是，我们把这个称为上下文。  

**00:16:52 - 00:16:56**  
原文：These four tokens are context, and they feed into a neural network.  
译文：这四个令牌是上下文，它们输入到一个神经网络中。  

**00:16:56 - 00:16:59**  
原文：And this is the input to the neural work.  
译文：这是神经网络的输入。  

**00:16:59 - 00:17:04**  
原文：K, now I'm going to go into the detail of what's inside this neural network in a little bit.  
译文：好的，现在我将详细讲解这个神经网络的内部结构。  

**00:17:04 - 00:17:10**  
原文：For now, what's important to understand is the input and the output of the neural net.  
译文：目前，重要的是要理解神经网络的输入和输出。  

**00:17:10 - 00:17:16**  
原文：So the input are sequences of tokens of variable length anywhere between zero and some maximum size, like 8000.  
译文：所以输入是长度可变的标记序列，长度在零到某个最大值之间，比如8000。  

**00:17:16 - 00:17:19**  
原文：The output now is a prediction for what comes next.  
译文：现在的输出是对接下来会发生什么的预测。  

**00:17:19 - 00:17:29**  
原文：So because our vocabulary has 100000, 277 possible tokens, the neural network is going to output exactly that many numbers.  
译文：所以因为我们的词汇量有100,027个可能的标记，神经网络将输出 exactly 那么多数字。 

注：为了保持原始格式，"exactly that many" 被直接翻译为 "正好那么多"，但根据上下文和中文表达习惯，可以调整为“ precisely 那么多”或“正好这么多”。另外，原文中的数字似乎有些不符合常规（100000, 277），这里按照字面意思翻译为100,027。如果这是一个特定的数值表示方式，请根据实际情况进行调整。  

**00:17:29 - 00:17:35**  
原文：And all those numbers correspond to the probability of that token as coming next in the sequence.  
译文：而且所有这些数字都对应于该标记在序列中下一个出现的概率。  

**00:17:35 - 00:17:37**  
原文：So it's making guesses about what comes next.  
译文：所以它在预测接下来会发生什么。  

**00:17:37 - 00:17:41**  
原文：In the beginning, this neural network is randomly initialized.  
译文：最初，这个神经网络是随机初始化的。  

**00:17:41 - 00:17:47**  
原文：So and we're going to see in a little bit of what that means, but it's a random transformation.  
译文：所以，我们一会儿会看到这具体意味着什么，但这是一个随机变换。  

**00:17:47 - 00:17:52**  
原文：So these probabilities in the very beginning of the training are also going to be kind of random.  
译文：所以这些概率在训练的最开始也会是比较随机的。  

**00:17:52 - 00:17:54**  
原文：So here I have three examples.  
译文：所以这里我有三个例子。  

**00:17:54 - 00:17:57**  
原文：But keep in mind that there's 100000 numbers here.  
译文：但请记住，这里有100,000个数字。  

**00:17:57 - 00:18:03**  
原文：So the probability of this token space direction neural network is saying that this is 4% likely right now.  
译文：所以这个令牌空间方向神经网络的概率是说这有4%的可能性是在当前情况下发生的。 

注：根据上下文，这句话可能意在表达“此神经网络判断这一事件目前有4%的可能性发生”。如果需要更准确的翻译，请提供更多的背景信息。  

**00:18:03 - 00:18:05**  
原文：Eleven, seven, nine, nine is 2%.  
译文：十一，七，九，九是2％。  

**00:18:05 - 00:18:11**  
原文：And then here the probability of 362, which is post, is 3%.  
译文：然后这里的362的概率，即事后概率，是3%。  

**00:18:11 - 00:18:14**  
原文：Now of course, we've sampled this window from our data set.  
译文：现在当然，我们已经从我们的数据集中采样了这个窗口。  

**00:18:14 - 00:18:16**  
原文：So we know what comes next.  
译文：所以我们知道接下来会发生什么。  

**00:18:16 - 00:18:22**  
原文：We know, and that's the label we know that the correct answer is this, three, nine, six, two actually comes next in the sequence.  
译文：我们知道，而且我们知道正确的答案是这个，三、九、六、二实际上在这个序列中是接下来的数字。  

**00:18:22 - 00:18:27**  
原文：So now what we have is this mathematical process for doing update to the neural arwork.  
译文：所以现在我们有了这个用于更新神经网络的数学过程。  

**00:18:27 - 00:18:34**  
原文：We have a way of tuning it, and we're going to go into a little bit bit of detail in a bit.  
译文：我们有一种调整它的方法，我们稍后会详细介绍。  

**00:18:34 - 00:18:44**  
原文：But basically, we know that this probability here of 3%, we want this probability to be higher and we want the probabilities of all the other tokens to be lower.  
译文：但基本上，我们知道这里的3%的概率，我们希望这个概率更高，同时希望所有其他标记的概率更低。  

**00:18:44 - 00:18:54**  
原文：And so we have a way of mathematically calculating how to adjust and update the neural network so that the correct answer has a slightly higher probability.  
译文：因此，我们有一种数学方法来计算如何调整和更新神经网络，从而使正确答案的概率稍微提高一些。  

**00:18:54 - 00:19:04**  
原文：So if I do an update to the neural network now, the next time I feed this particular sequence of four tokens into neural network, the neural network will be slightly adjusted now.  
译文：所以，如果我现在对神经网络进行更新，下次我将这四个令牌的特定序列输入神经网络时，神经网络将会被稍微调整一下。  

**00:19:04 - 00:19:13**  
原文：And it will say, okay, post is maybe 4%, and case now maybe is 1%, and direction could become 2% or something like that.  
译文：它会说，好的，post可能是4%，case现在可能是1%，direction可能变成2%或类似的比例。  

**00:19:13 - 00:19:24**  
原文：And so we have a way of nudging, of slightly updating the neural Nuto, basically give a higher probability to the correct token that comes next in the sequence.  
译文：因此，我们有一种推动的方式，稍微更新神经网络 Nuto，基本上是给序列中接下来的正确令牌赋予更高的概率。  

**00:19:24 - 00:19:32**  
原文：And now you just have to remember that this process happens not just for this token here, where these four fed in and predicted this one.  
译文：现在你只需要记住，这个过程不仅发生在眼前的这个令牌上，这四个输入并预测了这一个。  

**00:19:32 - 00:19:37**  
原文：This process happens at the same time for all of these tokens in the entire data set.  
译文：此过程发生在整个数据集中的所有这些令牌上，同时进行。  

**00:19:37 - 00:19:42**  
原文：And so in practice, we sample ed little windows, little batches of windows.  
译文：因此，在实践中，我们采样了小窗口，小批次的窗口。  

**00:19:42 - 00:19:50**  
原文：And then at every single one of these tokens, we want to adjust our neural networks so that the probability of that token becomes slightly higher.  
译文：然后在这些标记中的每一个，我们都希望调整我们的神经网络，使得该标记的概率变得稍微高一些。  

**00:19:50 - 00:19:53**  
原文：And this all happens in parallel in large batches of these tokens.  
译文：而且这一切都是并行发生的，以这些令牌的大批量进行。  

**00:19:53 - 00:19:56**  
原文：And this is the process of training the neural network.  
译文：这就是训练神经网络的过程。  

**00:19:56 - 00:20:10**  
原文：It's a sequence of updating it so that its predictions match up the statistics of what actually happens in your training set, and its probabilities become consistent with the statistical patterns of how these tocan follow each other in the data.  
译文：这是一个更新的过程，使其预测与训练集中实际发生的情况的统计相匹配，且其概率与这些元素在数据中如何相继出现的统计模式保持一致。  

**00:20:10 - 00:20:16**  
原文：So let's now briefly get into the internals of these neural networks, just to give you a sense of what's inside.  
译文：那么现在让我们简要地了解一下这些神经网络的内部运作，只是为了让你对内部结构有个概念。  

**00:20:16 - 00:20:18**  
原文：So neural network internals.  
译文：所以神经网络的内部。  

**00:20:18 - 00:20:22**  
原文：So as I mentioned, we have these inputs that are sequences of tokens.  
译文：所以，正如我提到的，我们有这些输入，它们是由标记序列组成的。  

**00:20:22 - 00:20:24**  
原文：In this case, this is four input tokens.  
译文：在这种情况下，这是四个输入令牌。  

**00:20:24 - 00:20:28**  
原文：But this can be anywhere between zero up to, let's say, 8000 tokens.  
译文：但这个数量可以在零到，比如说，8000个令牌之间。  

**00:20:28 - 00:20:31**  
原文：In principle, this can be an infinite number of tokens.  
译文：原则上，这可以是无限数量的代币。  

**00:20:31 - 00:20:37**  
原文：We just it would just be too computationally expensive to process an infinite number of tokens.  
译文：我们只是认为处理无限数量的令牌在计算上会过于昂贵。  

**00:20:37 - 00:20:42**  
原文：So we just crop it at a certain length, and that becomes the maximum context length of that model.  
译文：所以我们只需将其截断到一定长度，而这就是该模型的最大上下文长度。  

**00:20:43 - 00:20:53**  
原文：Now these inputs x are mixed up in a giant mathematical expression together with the parameters or the weights of these neural networks.  
译文：现在这些输入x与神经网络的参数或权重一起混合在一个巨大的数学表达式中。  

**00:20:53 - 00:20:57**  
原文：So here I'm showing six example parameters and their setting.  
译文：所以这里我展示了六个示例参数及其设置。  

**00:20:57 - 00:21:03**  
原文：But in practice, these modern neural networks will have billions of these parameters.  
译文：但实际上，这些现代神经网络将拥有数十亿这样的参数。  

**00:21:03 - 00:21:08**  
原文：And in the beginning, these parameters are completely randomly set.  
译文：而且最开始， 这些参数是完全随机设定的。  

**00:21:08 - 00:21:36**  
原文：Now, with a random setting of parameters, you might expect that this neural network would make random predictions, and it does in the beginning, it's totally random predictions, but it's through this process of iteratively updating the network, and we call that process training, a neural work, so that the setting of these parameters gets adjusted such that the outputs of our neural work becomes consistent with the patterns seen in our training set.  
译文：现在，使用随机设置的参数，你可能会认为这个神经网络会做出随机预测，而且在一开始确实是完全随机的预测。但是，通过这个迭代更新网络的过程，我们称之为训练神经网络，使得这些参数的设置得到调整，从而使我们神经网络的输出与我们在训练集中看到的模式一致。  

**00:21:36 - 00:21:41**  
原文：So think of these parameters as kind of like knobs on a dj set.  
译文：所以把这些参数想象成DJ设备上的旋钮。  

**00:21:41 - 00:21:48**  
原文：And as you're twiddling these knobs, you're getting different predictions for every possible token sequence input.  
译文：当您调整这些旋钮时，对于每一个可能的令牌序列输入，您都会得到不同的预测。  

**00:21:48 - 00:21:56**  
原文：And training in your Ural network just means discovering a setting of parameters that seems to be consistent with the statistics of the training set.  
译文：在你的乌拉尔网络中进行训练，只是意味着发现一组参数设置，这组参数看起来与训练集的统计特性相一致。  

**00:21:56 - 00:22:02**  
原文：Now, let me just give you an example of what this giant mathematical expression looks like, just to give you a sense.  
译文：现在，我来给你举个例子， 关于这个巨大的数学表达式看起来是什么样的， 只是让你有点概念。  

**00:22:02 - 00:22:06**  
原文：And modern networks are massive expressions with trillions of terms, probably.  
译文：而且现代网络是巨大的表达，可能有数万亿个条款。  

**00:22:06 - 00:22:08**  
原文：But let me just show you a simple example here.  
译文：但是让我在这里给你展示一个简单的例子。  

**00:22:08 - 00:22:10**  
原文：It would look something like this.  
译文：它看起来会是这个样子。  

**00:22:10 - 00:22:25**  
原文：I mean, these are the kinds of expressions, just to show you that it's not very scary, we have inputs x, like x one, x two, in this case, two example inputs, and they get mixed up with the weights of the network, W zero, W one, two, three, etc..  
译文：我的意思是，这些表达式只是为了向你展示这并不太可怕。我们有输入 x，比如 x1，x2，在这个例子中有两个示例输入，它们与网络的权重 W0、W1、W2、W3 等进行混合。  

**00:22:25 - 00:22:31**  
原文：And this mixing is simple things like multiplication, ediexponentiation, division, etcetera.  
译文：而这种混合是简单的事情，比如乘法、指数运算、除法等。  

**00:22:31 - 00:22:42**  
原文：And it is the subject of neural network architecture research to design effective mathematical expressions that have a lot of kind of convenient characteristics.  
译文：设计具有许多便捷特性的有效数学表达式是神经网络架构研究的主题。  

**00:22:42 - 00:22:46**  
原文：They are expressive, they're optimizable, they're paralyzable etc..  
译文：它们具有表现力，可以优化，可以并行化等。  

**00:22:46 - 00:22:50**  
原文：And so but at the end of the day, these are not complex expressions.  
译文：而且，但归根结底，这些并不是复杂的表达方式。  

**00:22:50 - 00:22:55**  
原文：And basically, they mix up the inputs with the parameters to make predictions.  
译文：基本上，他们将输入与参数混合以进行预测。  

**00:22:55 - 00:23:02**  
原文：And we're optimizing the parameters of this neural network so that the predictions come out consistent with the training set.  
译文：我们正在优化这个神经网络的参数，以便预测结果与训练集保持一致。  

**00:23:03 - 00:23:08**  
原文：Now I would like to show you an actual production grade example of what these neural networks look like.  
译文：现在我想给您展示一个实际生产级别的神经网络是什么样子。  

**00:23:08 - 00:23:14**  
原文：So for that, I encourage you to go through this web site that has a very nice visualization of one of these networks.  
译文：因此，我鼓励你浏览这个网站，它有一个非常好的其中一个网络的可视化展示。  

**00:23:14 - 00:23:17**  
原文：So this is what you will find on this web site.  
译文：所以这就是你在本网站上会找到的内容。  

**00:23:17 - 00:23:23**  
原文：And this neural network here that is used in production settings has this special kind of structure.  
译文：并且这个在生产环境中使用的神经网络具有这种特殊的结构。  

**00:23:23 - 00:23:25**  
原文：This network is called the transformer.  
译文：这个网络被称为变压器。  

注意：在专业领域中，“transformer”通常特指一种特定类型的神经网络架构，因此更准确的翻译应为：

这个网络被称为Transformer（变换器）。  

**00:23:25 - 00:23:31**  
原文：And this particular one, as an example, has 85000 roughly parameters.  
译文：而这个特定的例子 大约有85,000个参数。  

**00:23:31 - 00:23:44**  
原文：Now here on the top, we take the inputs, which are the token sequences, and then information flows through the neural network until the output, which here are the logic soft max.  
译文：现在在顶部，我们接收输入，这些输入是令牌序列，然后信息通过神经网络流动，直到输出，在这里输出是逻辑软最大值（softmax）。  

**00:23:44 - 00:23:48**  
原文：But these are the predictions for what comes next, what token comes next.  
译文：但这些都是对接下来会发生什么的预测，下一个会出现什么令牌。  

**00:23:49 - 00:24:01**  
原文：And then here there's a sequence of transformations and all these intermediate values that get produced inside this mathematical expression as it is sort of predicting what comes next.  
译文：然后这里有一系列变换，以及所有这些在这个数学表达式内部产生的中间值，当它在预测接下来会发生什么时。  

**00:24:01 - 00:24:07**  
原文：So as an example, these tokens are embedded into kind of like this distributed representation, as it's called.  
译文：所以，举个例子来说，这些令牌被嵌入到所谓的分布式表示中，就像这样。  

**00:24:07 - 00:24:13**  
原文：So every possible token has kind of like a vector that represents it inside the neural network.  
译文：所以每个可能的令牌在神经网络内部都有类似向量的东西来表示它。  

**00:24:13 - 00:24:18**  
原文：So first we embed the tokens, and then those values kind of like flow through this diagram.  
译文：所以首先我们嵌入这些标记，然后那些值就像流过这个图表一样。  

**00:24:18 - 00:24:22**  
原文：And these are all very simple mathematical expressions individually.  
译文：这些都是一些非常简单的数学表达式，各自来看。  

**00:24:22 - 00:24:27**  
原文：So we have layer norms and matrix multiplications and soft maxes and so on.  
译文：所以我们有层归一化、矩阵乘法、softmax等。  

**00:24:27 - 00:24:31**  
原文：So here's kind of like the attention block of this transformer.  
译文：所以这里有点像这个变压器的注意力模块。  

**00:24:31 - 00:24:36**  
原文：And then information kind of flows through into the multilayer perception on block and so on.  
译文：然后信息流入多层感知器中，逐块进行等等。  

**00:24:36 - 00:24:41**  
原文：And all these numbers here, these are the intermediate values of their expression.  
译文：这里所有的数字，这些都是他们表达式的中间值。  

**00:24:41 - 00:24:47**  
原文：And you can almost think of these as kind of like the firing rates of these synthetic neurons.  
译文：你可以几乎把它们想象成 类似于这些合成神经元的放电率。  

**00:24:47 - 00:24:56**  
原文：But I would caution you to not kind of think of it too much like neurons, because these are extremely simple neurons compared to the neurons you would find in your brain.  
译文：但我必须提醒你不要太把它想成是神经元，因为这些与你在大脑中发现的神经元相比非常简单。  

**00:24:56 - 00:25:01**  
原文：Your biological neurons are very complex dynamical processes that have memory and so on.  
译文：您的生物神经元是非常复杂的动态过程，具有记忆等功能。  

**00:25:01 - 00:25:02**  
原文：There's no memory in this expression.  
译文：这个表达式中没有记忆功能。  

**00:25:02 - 00:25:06**  
原文：It's a fixed mathematical expression from input to output with no memory.  
译文：它是一个从输入到输出的固定数学表达式，没有记忆功能。  

**00:25:06 - 00:25:08**  
原文：It's just as stateless.  
译文：它同样是没有状态的。  

**00:25:08 - 00:25:11**  
原文：So these are very simple neurons in comparison to biological neurons.  
译文：所以这些神经元与生物神经元相比非常简单。  

**00:25:11 - 00:25:18**  
原文：But you can still kind of loosely think of this as like a synthetic piece of brain tissue, if you like to think about it that way.  
译文：但你仍然可以将其松散地理解为 一种合成的脑组织， 如果你喜欢这样思考的话。  

**00:25:18 - 00:25:23**  
原文：So information flows through all these neurons fire until we get to the predictions.  
译文：所以信息流经所有这些神经元，直到我们得到预测结果。  

**00:25:23 - 00:25:30**  
原文：Now, I'm not actually going to dwell too much on the precise kind of like mathematical details of all these transformations.  
译文：现在，我实际上并不会过多停留于所有这些变换的确切数学细节。  

**00:25:30 - 00:25:33**  
原文：Honestly, I don't think it's that important to get into.  
译文：老实说，我认为没有必要深入探讨这个问题。  

**00:25:33 - 00:25:38**  
原文：What's really important to understand is that this is a mathematical function.  
译文：真正重要的是要理解这是一个数学函数。  

**00:25:38 - 00:25:43**  
原文：It is parameterized by some fixed set of parameters, like, say, 85000 of them.  
译文：它由一些固定的参数集进行参数化，比如说，有85000个参数。  

**00:25:43 - 00:25:46**  
原文：And it is a way of transforming inputs into outputs.  
译文：并且它是一种将输入转换为输出的方法。  

**00:25:46 - 00:25:52**  
原文：And as it would twidtle the parameters, we are getting different kinds of predictions.  
译文：当它调整参数时，我们会得到不同类型的预测。  

**00:25:52 - 00:25:59**  
原文：And then we need to find a good setting of these parameters so that the predictions sort of match up with the patterns, scene and training set.  
译文：然后我们需要找到这些参数的一个好的设置，使得预测与模式、场景和训练集大致匹配。  

**00:25:59 - 00:26:01**  
原文：So that's the transformer.  
译文：所以这就是变压器。  

**00:26:01 - 00:26:01**  
原文：Okay.  
译文：好的。  

**00:26:01 - 00:26:07**  
原文：So I've shown you the internals of the neural network, and we talked a bit about the process of training it.  
译文：所以，我向您展示了神经网络的内部运作，我们也简单讨论了训练它的过程。  

**00:26:07 - 00:26:13**  
原文：I want to cover one more major stage of working with these networks, and that is the stage called inference.  
译文：我想再涵盖一个与这些网络打交道的重要阶段，那就是称为推理的阶段。  

**00:26:13 - 00:26:24**  
原文：So an inference, what we're doing is we're generating new data from the model, and so we want to basically see what kind of patterns it has internalized in the parameters of its network.  
译文：所以，推理的过程，我们所做的就是从模型生成新的数据，因此我们基本上想要看看它在网络的参数中内化了什么样的模式。  

**00:26:24 - 00:26:28**  
原文：So to generate from the model is relatively straightforward.  
译文：所以从模型生成相对直接。  

**00:26:28 - 00:26:33**  
原文：We start with some tokens that are basically your prefix, like what you want to start with.  
译文：我们从一些基本上是您前缀的标记开始，比如您想用什么开始。  

**00:26:33 - 00:26:38**  
原文：So say we want to start with the token 91, well, we feed it into the network.  
译文：所以如果我们想从token 91开始，好吧，我们把它输入网络。  

**00:26:38 - 00:26:42**  
原文：And remember, that network gives us probabilities, right?  
译文：并记住，该网络给我们提供的是概率，对吧？  

**00:26:42 - 00:26:45**  
原文：It gives us this probability vector here.  
译文：它给了我们这个概率向量。  

**00:26:45 - 00:26:50**  
原文：So what we can do now is we can basically flip a biased coin.  
译文：所以我们现在可以做的是，我们基本上可以抛一枚有偏见的硬币。  

**00:26:50 - 00:26:55**  
原文：So we can sample basically a token based on this probability distribution.  
译文：所以我们可以基本上根据这个概率分布来采样一个令牌。  

**00:26:55 - 00:27:02**  
原文：So the tokens that are given high probability by the model are more likely to be sampled when you flip this biased coin.  
译文：所以，模型赋予高概率的 token 在你抛这个有偏见的硬币时更有可能被采样到。  

**00:27:02 - 00:27:04**  
原文：You can think of it that way.  
译文：你可以那样想。  

**00:27:04 - 00:27:08**  
原文：So we sample from the distribution to get a single unique token.  
译文：所以我们从分布中采样以获得一个唯一的令牌。  

**00:27:08 - 00:27:11**  
原文：So for example, token 860 comes next.  
译文：所以，例如，接下来是860号令牌。  

**00:27:11 - 00:27:16**  
原文：So 860 in this case, when we're generating from model, could come next.  
译文：所以在这个情况下，860 在我们从模型生成时，可能会接下来出现。  

**00:27:16 - 00:27:19**  
原文：Now, 860 is a relatively likely token.  
译文：现在，860是一个相对可能的令牌。  

**00:27:19 - 00:27:22**  
原文：It might not be the only possible token in this case.  
译文：在这种情况下，它可能不是唯一可能的令牌。  

**00:27:22 - 00:27:28**  
原文：There could be many other tokens that could have been sampled, but we could see that 860c is a relatively likely token.  
译文：可能会有很多其他令牌可以被采样，但我们可以看到，860c 是一个相对可能的令牌。  

**00:27:28 - 00:27:33**  
原文：As an example, and indeed in our training example here, 860 does follow 91.  
译文：例如，在这里的训练示例中，860确实跟在91之后。  

**00:27:33 - 00:27:35**  
原文：So let's not say that we continue the process.  
译文：所以，让我们不要说我们继续这个过程。  

**00:27:35 - 00:27:40**  
原文：So after 91, there's a 60, we append it, and we again ask, what is the third token?  
译文：所以91之后，有一个60，我们将其附加，然后我们再次询问，第三个标记是什么？  

**00:27:40 - 00:27:45**  
原文：Let's sample, and let's just say that it's 287, exactly as here.  
译文：让我们来取样，假设它就是287，就像这里显示的一样。  

**00:27:45 - 00:27:46**  
原文：Let's do that again.  
译文：让我们再做一次。  

**00:27:46 - 00:27:47**  
原文：We come back in.  
译文：我们回到里面。  

**00:27:47 - 00:27:52**  
原文：Now we have a sequence of three, and we ask, what is the likely fourth token?  
译文：现在我们有了一个三个元素的序列，我们问，第四个元素可能是什么？  

**00:27:52 - 00:27:55**  
原文：And we sample from that and get this one.  
译文：我们从中采样并得到了这个。  

**00:27:55 - 00:27:57**  
原文：And now let's say we do it one more time.  
译文：现在让我们再说一次，我们再做一次。  

**00:27:57 - 00:28:03**  
原文：We take those four, we sample and we get this one and this 13, six, five, nine.  
译文：我们取这四个数，进行采样，得到这一个和这个13，六，五，九。  

**00:28:03 - 00:28:07**  
原文：This is not actually three, nine, six, two as we had before.  
译文：这实际上并不是我们之前看到的三、九、六、二。  

**00:28:07 - 00:28:10**  
原文：So this token is the token article instead.  
译文：所以这个令牌是替代的令牌文章。  

**00:28:10 - 00:28:12**  
原文：So viewing a single article.  
译文：所以查看单篇文章。  

**00:28:12 - 00:28:20**  
原文：And so in this case, we didn't exactly reproduce the sequence that we saw here in the training data.  
译文：因此，在这种情况下，我们并没有完全重现我们在训练数据中看到的序列。  

**00:28:20 - 00:28:23**  
原文：So keep in mind that these systems are stochastic.  
译文：所以请记住，这些系统是随机的。  

**00:28:23 - 00:28:39**  
原文：They have were sampling and we're flipping coins and sometimes we lock out and we reproduce some like small chunk of the text and training set, but sometimes we're getting a token that was not verbatim part of any of the documents in the training data.  
译文：他们进行了采样，我们在抛硬币决定选择，有时我们会锁定并重现训练集中的一些小段文本，但有时候我们得到的令牌并不是训练数据中任何文档的逐字部分。 

注意：此段文字看起来像是描述一种自然语言处理或机器学习中的实验过程，其中包含了一些口语化的表达和比喻，因此翻译时尽量保留了原文的意思和风格。  

**00:28:39 - 00:28:48**  
原文：So we're going to get sort of like remixes of the data that we saw in the training because at every step of the way, we can flip and get a slightly different token.  
译文：所以我们将得到类似于我们在训练中看到的数据的混音，因为每一步，我们都可以翻转并获得稍微不同的标记。  

**00:28:48 - 00:29:00**  
原文：And then once that token makes it in, if you sample the next one and so on, you very quickly start to generate token streams that are very different from the token streams that occur in the training documents.  
译文：一旦那个标记进入模型，如果你继续采样下一个，如此类推，你很快就会生成与训练文档中出现的标记流非常不同的标记流。  

**00:29:00 - 00:29:06**  
原文：So statistically, they will have similar properties, but they are not identical to a training data.  
译文：所以从统计学上讲，它们将具有相似的性质，但它们并不完全等同于训练数据。  

**00:29:06 - 00:29:09**  
原文：They're kind of like inspired by the training data.  
译文：它们有点像是从训练数据中得到启发。  

**00:29:09 - 00:29:13**  
原文：And so in this case, we got a slightly different sequence.  
译文：所以在这种情况下，我们得到了一个略有不同的序列。  

**00:29:13 - 00:29:14**  
原文：And why would we get article?  
译文：而且，我们为什么会得到文章？  

**00:29:14 - 00:29:20**  
原文：You might imagine that articles are relatively likely token in the context of bar viewing single ettera.  
译文：你可能会认为，在查看单个 ettera 的背景下，文章是比较可能出现的标记。  

请注意，原始文本中包含一些不太常见的词汇或拼写（如 "bar viewing single ettera"），这可能影响了翻译的准确性。如果你能提供更多上下文或确认这些词汇的正确性，我可以提供更准确的翻译。  

**00:29:20 - 00:29:31**  
原文：And you can imagine that the word article followed this context window somewhere in the training documents to some extent, and we just happened to sample it here at that stage.  
译文：你可以想象，在训练文档的某个地方，单词“article”在某种程度上跟随了这个上下文窗口，而我们刚好在这个阶段在这里采样到了它。  

**00:29:31 - 00:29:36**  
原文：So basically, inference is just predicting from these distributions one at a time.  
译文：所以，基本上，推理就是从这些分布中一个接一个地进行预测。  

**00:29:36 - 00:29:40**  
原文：We continue feeding back tokens and getting the next one.  
译文：我们继续反馈标记并获取下一个。  

**00:29:40 - 00:29:42**  
原文：And we're always flipping these coins.  
译文：我们总是在抛这些硬币。  

**00:29:42 - 00:29:52**  
原文：And depending on how lucky or unlucky we get, we might get very different kinds of patterns depending on how we sample from these probability distribuations.  
译文：而且取决于我们是幸运还是不幸，我们可能会得到非常不同的模式，这取决于我们如何从这些概率分布中抽样。  

**00:29:52 - 00:29:53**  
原文：So that's inference.  
译文：所以这就是推理。  

**00:29:53 - 00:29:59**  
原文：So in most common scenarios, basically downloading the Internet and tokizing, it is a pre processing step.  
译文：所以在大多数常见的情况下，基本上下载互联网并进行分词，这是一个预处理步骤。  

**00:29:59 - 00:30:01**  
原文：You do that a single time.  
译文：你只做一次。  

**00:30:01 - 00:30:04**  
原文：And then once you have your token sequence, we can start training networks.  
译文：然后一旦你有了你的token序列，我们就可以开始训练网络了。  

**00:30:04 - 00:30:14**  
原文：And in practical cases, you would try to train many different networks of different kinds of settings and different kinds of arrangements and different kinds of sizes.  
译文：在实际应用中，你会尝试训练许多不同网络，这些网络具有不同的设置、不同的结构和不同的规模。  

**00:30:14 - 00:30:18**  
原文：And so you'll be doing a lot of neural network training.  
译文：所以你会做很多神经网络训练。  

**00:30:18 - 00:30:30**  
原文：And then once you have a neural network and you train it and you have some specific set of parameters that you're happy with, then you can take the model and you can do inference and you can actually generate data from the model.  
译文：一旦你有了一个神经网络，训练它之后，得到了一些令你满意的特定参数集，那么你可以使用这个模型进行推理，实际上可以从模型中生成数据。  

**00:30:30 - 00:30:41**  
原文：And when you're on ChatGPT and you're talking with the model, that model is trained and has been trained by OpenAI many months ago probably, and they have a specific set of weights that work well.  
译文：当你在使用 ChatGPT 并与模型交谈时，该模型是由 OpenAI 训练的，并且可能几个月前就已经训练好了，他们有一套特定的权重，效果非常好。  

**00:30:41 - 00:30:44**  
原文：When you're talking to the model, all of that is just inference.  
译文：当你与模型交谈时，所有这些都只是推理。  

**00:30:44 - 00:30:46**  
原文：There's no more training.  
译文：没有更多的培训了。  

**00:30:46 - 00:30:54**  
原文：Those parameters are held fixed and you're just talking to the model, sort of you're given it some of the tokens and it's kind of completing token sequences.  
译文：那些参数是固定的，你只是在与模型对话，有点像是你给它一些标记，而它在完成标记序列。  

**00:30:54 - 00:30:59**  
原文：And that's what you're seeing generated when you actually use the model on chashept t.  
译文：这就是当你实际在 chashept t 上使用模型时所产生的结果。  

**00:30:59 - 00:31:01**  
原文：So that model then just does inference loan.  
译文：所以那个模型然后只进行推理贷款。 

注：根据上下文，这句话可能指的是模型仅用于贷款推理（即预测或决策），但直译 somewhat 显得语义不明。如果有更多背景信息，可以提供更准确的翻译。  

**00:31:01 - 00:31:09**  
原文：So let's now look at an example of training and inference that is kind of concrete and gives you a sense of what this actually looks like when these models are trained.  
译文：那么现在让我们来看一个训练和推理的例子，这个例子比较具体，可以让你感受到这些模型在训练时实际上是什么样子的。  

**00:31:09 - 00:31:16**  
原文：Now the example that I would like to work with and that I'm particularly fond of is that of opening as GPT two.  
译文：现在，我想 workings 的例子，也是我特别喜欢的例子，是像 GPT 二这样的开放。 

注：根据上下文，“workings”可能是指“工作”或“操作”，但原句中似乎有表述不清的地方。更准确的翻译可能是：

“现在，我想介绍一个我喜欢的例子，那就是像GPT-2一样的开放模型。” 

请确认您所需要的准确意思，以便我能提供更好的翻译。  

**00:31:16 - 00:31:19**  
原文：So GPT stands for genertively ptrained transformer.  
译文：所以GPT代表生成式预训练变压器。  

**00:31:19 - 00:31:23**  
原文：And this is the second iteration of the GPT series by OpenAI.  
译文：这是OpenAI的GPT系列的第二次迭代。  

**00:31:23 - 00:31:30**  
原文：When you are talking to ChatGPT today, the model that is underlying all of the magic of that interaction is GPT -4.  
译文：当你今天与ChatGPT交谈时，支撑这一互动所有神奇之处的模型是GPT-4。  

**00:31:30 - 00:31:38**  
原文：So the fourth iteration of that series, now GPT two, was published in 2019 by OpenAI in this paper that I have right here.  
译文：所以该系列的第四个迭代，现在是GPT-2，于2019年由OpenAI在这一篇我手头正好有的论文中发表。  

**00:31:38 - 00:31:44**  
原文：And the reason I like GPT two is that it is the first time that a recognizably modern stack came together.  
译文：我喜欢GPT-2的原因是，它是第一次将可识别的现代技术栈组合在一起。  

**00:31:44 - 00:31:51**  
原文：So all the pieces on GPT two are recognizable today by modern standards, is just everything has gotten bigger.  
译文：所以，根据现代标准，GPT-2 中的所有组件今天都可以被认出来，只是所有的东西都变得更大了。  

**00:31:51 - 00:32:02**  
原文：Now, I'm not going to be able to go into the full details of this paper, of course, because it is a technical publication, but some of the details that I would like to highlight are as follows.  
译文：现在，我当然无法详细介绍这篇论文的所有内容，因为它是一篇技术性文章，但我想要突出的一些要点如下。  

**00:32:02 - 00:32:08**  
原文：GPT two was a transformer neural network, were just like the neural networks you would work with today.  
译文：GPT-2 是一个变压器神经网络，它就像你今天使用的神经网络一样。  

**00:32:08 - 00:32:11**  
原文：It was it had 1.6 billion parameters.  
译文：它有16亿个参数。  

**00:32:11 - 00:32:14**  
原文：So these are the parameters that we looked at here.  
译文：所以，这些就是我们在这里查看的参数。  

**00:32:14 - 00:32:16**  
原文：It would have 1.6 billion of them today.  
译文：如今会有16亿个。  

**00:32:16 - 00:32:21**  
原文：Modern transformers would have a lot closer to a trillion or several hundred billion.  
译文：现代变压器将更接近于一万亿或几千亿。  

**00:32:21 - 00:32:26**  
原文：Probably the maximum context length here was 1024 tokens.  
译文：可能这里的最大上下文长度是1024个标记。  

**00:32:26 - 00:32:34**  
原文：So it is when we are sampling chunks of windows of tokens from the data set, we're never taking more than 1024 tokens.  
译文：因此，当我们从数据集中采样窗口令牌块时，我们永远不会取多于1024个令牌。  

**00:32:34 - 00:32:45**  
原文：And so when you are trying to predict the next token in a sequence, you will never have more than 1024 tokens kind of in your context in order to make that prediction.  
译文：因此，当你试图预测序列中的下一个标记时，你将永远不会在上下文中拥有超过1024个标记来做出该预测。  

**00:32:45 - 00:32:47**  
原文：Now this is also tiny by modern standards.  
译文：现在这在现代标准下也是微小的。  

**00:32:47 - 00:32:54**  
原文：Today, the token, the context lengths would be a lot closer to a couple hundred thousand or maybe even a million.  
译文：今天，token的数量，上下文长度可能会接近几十万，甚至可能达到一百万。  

**00:32:54 - 00:33:02**  
原文：And so you have a lot more context, a lot more tokens in the history, and you can make a lot better prediction about the next token in sequence in that way.  
译文：因此，你有更多的上下文，历史中有更多的标记，这样你可以更好地预测序列中的下一个标记。  

**00:33:02 - 00:33:07**  
原文：And finally, GPT two was trained on approximately 100 billion tokens.  
译文：最后，GPT-2 的训练基于大约 100 亿个令牌。  

**00:33:07 - 00:33:10**  
原文：And this is also fairly small on modern standards.  
译文：根据现代标准，这也很小。  

**00:33:10 - 00:33:17**  
原文：As I mentioned, the fine web data set that we looked at here, the fine web data set has 15 trillion tokens.  
译文：如我所说，我们在这里查看的精细网络数据集，这个精细网络数据集包含15万亿个标记。  

**00:33:17 - 00:33:19**  
原文：So 100 billion is quite small.  
译文：所以1000亿相当小。  

**00:33:19 - 00:33:25**  
原文：Now, I actually tried to reproduce GPT two for fun as part of this project called lm dot c.  
译文：现在，我实际上尝试重现GPT-2作为这个名为lm(dot)c的项目的一部分，只是为了好玩。  

**00:33:25 - 00:33:31**  
原文：So you can see my red up p of doing that in this post on GitHub under the lm dot c repository.  
译文：所以你可以在本帖子中看到我在 GitHub 上的 lm.dot.c 仓库中这样做。  

**00:33:31 - 00:33:42**  
原文：So in particular, the cost of training GPT two in 2019, what was estimated to be approximately $40000, but today you can do is significantly better than that.  
译文：所以，特别是，2019年训练GPT-2的成本估计约为40,000美元，但今天你可以做得比那个成本显著更低。  

**00:33:42 - 00:33:47**  
原文：And in particular, here, it took about one day and about dollar, $600.  
译文：特别是这里，它花费了大约一天的时间和约600美元。  

**00:33:47 - 00:33:49**  
原文：But this wasn't even trying too hard.  
译文：但这甚至没有太努力。  

**00:33:49 - 00:33:54**  
原文：I think you could really bring this down to about $100 today.  
译文：我认为你今天可以把它降到大约100美元。  

**00:33:54 - 00:33:56**  
原文：Now why is it that the costs have come down so much?  
译文：现在为什么成本下降了这么多？  

**00:33:56 - 00:33:59**  
原文：Well, number one, these data sets have gotten a lot better.  
译文：首先，这些数据集变得更好了。  

**00:33:59 - 00:34:04**  
原文：And the way we filter them, extract them and prepare them has gotten a lot more refined.  
译文：我们筛选它们、提取它们和准备它们的方式变得更加精细。  

**00:34:04 - 00:34:07**  
原文：And so the data set of just a lot higher quality.  
译文：因此，数据集的质量大大提高。  

**00:34:07 - 00:34:08**  
原文：So that's one thing.  
译文：所以这是一点。  

**00:34:08 - 00:34:14**  
原文：But really the biggest difference is that our computers have gotten much faster in terms of the hardware.  
译文：但真正最大的区别是，我们的计算机在硬件方面已经变得更快了。  

**00:34:14 - 00:34:16**  
原文：And we're going to look at that in a second.  
译文：我们将在一秒钟后看那个。  

**00:34:16 - 00:34:31**  
原文：And also the software for running these models and really squeezing out all the speed from the hardware as it is possible that software has also gotten much better as everyone has focused on these models and trying to run them very, very quickly.  
译文：而且，用于运行这些模型的软件，以及真正从硬件中尽可能地压榨出所有速度的软件也变得更好了，因为所有人都专注于这些模型，并试图非常、非常快速地运行它们。  

**00:34:31 - 00:34:44**  
原文：Now I'm not going to be able to go into the full detail of this gptwo reproduction, and this is a long technical post, but I would like to still give you an intuitive sense for what it looks like to actually train one of these models as a researcher.  
译文：现在我无法详细介绍这个GPTwo复现的全部内容，这是一篇很长的技术帖子，但我仍然希望可以给你们一种直观的感受，让你们了解作为研究人员实际训练这些模型是什么样的体验。  

**00:34:44 - 00:34:46**  
原文：Like what are you looking at and what does it look like?  
译文：比如你在看什么，它看起来像什么？  

**00:34:46 - 00:34:47**  
原文：What does it feel like?  
译文：感觉是怎样的？  

**00:34:47 - 00:34:50**  
原文：So let me give you a sense of that a little bit.  
译文：那么让我给你稍微讲解一下。  

**00:34:50 - 00:34:51**  
原文：Okay, so this is what it looks like.  
译文：好的，它看起来是这样的。  

**00:34:51 - 00:34:52**  
原文：Let me slide this over.  
译文：让我把这移过去。  

**00:34:53 - 00:34:59**  
原文：So what I'm doing here is I am training a GPT two model right now.  
译文：所以，我现在在这里做的事情是训练一个GPT-2模型。  

**00:34:59 - 00:35:06**  
原文：And what's happening here is that every single line here, like this one, is one update to the model.  
译文：这里发生的情况是，这里的每一行，像这一行，是对模型的一次更新。  

**00:35:06 - 00:35:17**  
原文：So remember how here we are basically making the prediction better for every one of these tokens, and we are updating these weights or parameters of the neural.  
译文：所以记住，这里我们基本上是在改善对每个这些标记的预测，并且我们正在更新神经网络的这些权重或参数。  

**00:35:17 - 00:35:26**  
原文：So here, every single line is one update to the neural network where we change its parameters by a little bit so that it is better at predicting next token ness sequence.  
译文：所以在这里，每一行都是对神经网络的一次更新，我们稍微改变其参数，使其更好地预测下一个令牌序列。  

**00:35:26 - 00:35:35**  
原文：In particular, every single line here is improving the friction on 1 million tokens in the training set.  
译文：特别是，这里的每一行都在改善训练集中100万个令牌的摩擦。  

**00:35:35 - 00:35:49**  
原文：So we've basically taken 1 million tokens out of this data set, and we've tried to improve the prediction of that token as coming next in a sequence on all 1 million of them simultaneously.  
译文：所以我们基本上是从这个数据集中取出了100万个标记， 并尝试同时改进这100万个标记中 每一个作为序列中下一个标记的预测。  

**00:35:49 - 00:35:54**  
原文：And at every single one of these steps, we are making an update to the network for that.  
译文：在这些步骤中的每一步，我们都会对此进行网络更新。  

**00:35:54 - 00:35:58**  
原文：Now the number to watch closely is this number called loss.  
译文：现在需要密切关注的数字是被称为损失的这个数字。  

**00:35:58 - 00:36:04**  
原文：And the loss is a single number that is telling you how well your neural network is performing right now.  
译文：损失是一个告诉你当前神经网络性能如何的单一数字。  

**00:36:04 - 00:36:07**  
原文：And it is created so that low loss is good.  
译文：并且它被设计成低损耗是好的。  

**00:36:07 - 00:36:16**  
原文：So you'll see that the loss is decreasing as we make more updates to the neural nuwhich corresponds to making better predictions on the next token in a sequence.  
译文：所以你会看到，随着我们对神经网络进行更多的更新，损失在减少，这对应于对序列中的下一个令牌做出更好的预测。  

**00:36:16 - 00:36:21**  
原文：And so the loss is the number that you are watching as a neural network researcher.  
译文：因此，作为神经网络研究人员，你关注的数字就是损失值。  

**00:36:21 - 00:36:23**  
原文：And you are kind of waiting.  
译文：而你一直在等待。  

**00:36:23 - 00:36:33**  
原文：You're twidling your thumbs, you're drinking coffee, and you're making sure that this looks good so that with every update, your loss is improving and the network is getting better at prediction.  
译文：你正在无所事事，喝着咖啡，并确保这一切看起来很好，这样随着每一次更新，你的损失函数值都在改善，网络的预测能力也在不断提高。  

**00:36:33 - 00:36:37**  
原文：Now here you see that we are processing 1 million tokens per update.  
译文：现在您在这里看到我们每次更新处理100万个标记。  

**00:36:37 - 00:36:40**  
原文：Each update takes about 7s roughly.  
译文：每次更新大约需要7秒。  

**00:36:40 - 00:36:45**  
原文：And here we are going to process a total of 32000 steps of optimization.  
译文：我们将在这里进行总共32000步的优化。  

**00:36:45 - 00:36:53**  
原文：So 32000 steps with 1 million tokens each is about 33 billion tokens that we are going to process.  
译文：所以 32000 步，每步有 100 万个 token，大约是 330 亿个 token，这就是我们将要处理的数量。  

**00:36:53 - 00:36:59**  
原文：And we're currently only about 420 step, 420 out of 32000.  
译文：而且我们现在只走了大约420步， 420步出于32000步。  

**00:36:59 - 00:37:06**  
原文：So we are still only a bit more than 1% done because I've only been running this for ten or 15 minutes or something like that.  
译文：所以我们现在只完成了1%多一点，因为这个程序我只跑了10到15分钟或者类似的时间。  

**00:37:06 - 00:37:11**  
原文：Now every 20 steps I have configured this optimization to do inference.  
译文：现在每20步，我已经配置此优化进行推理。  

**00:37:11 - 00:37:16**  
原文：So what you're seeing here is the model is predicting the next token in the sequence.  
译文：所以你在这里看到的是，模型正在预测序列中的下一个标记。  

**00:37:16 - 00:37:21**  
原文：And so you sort of start randomly and then you continue plugging in the tokens.  
译文：所以你开始时是随机的，然后你继续插入令牌。  

**00:37:21 - 00:37:26**  
原文：So we're running this inference step, and this is the model sort of predicting the next token in a sequence.  
译文：所以我们正在运行这个推理步骤，这是模型预测序列中下一个标记的过程。  

**00:37:26 - 00:37:29**  
原文：And every time you see something appear, that's a new token.  
译文：每次当你看到有新东西出现时，那就是一个新的标记。  

**00:37:29 - 00:37:34**  
原文：So let's just look at this and you can see that this is not yet very coherent.  
译文：所以让我们来看看这个，你可以看到这还不太连贯。  

**00:37:34 - 00:37:38**  
原文：And keep in mind that this is only 1% of the way through training.  
译文：请记住，这仅仅是训练过程的1%。  

**00:37:38 - 00:37:42**  
原文：And so the model is not yet very good at predicting the next token in the sequence.  
译文：因此，该模型在预测序列中的下一个标记方面还不够好。  

**00:37:42 - 00:37:47**  
原文：So what comes out is actually kind of a little bit of gibberish, right?  
译文：所以出来的其实有点像是胡言乱语，对吧？  

**00:37:47 - 00:37:50**  
原文：But it still has a little bit of like local coherence.  
译文：但它仍然有一点点局部连贯性。  

**00:37:50 - 00:37:59**  
原文：So since she is mine, it's a part of the information should discuss my father, great companions, Gordon showed me sitting over it and etcetera.  
译文：所以，因为她是我的，这部分信息应该讨论我的父亲、伟大的同伴，戈登给我演示了如何处理它等等。 

请注意，原文中句子结构较为混乱，翻译时已尽量保持原意并使其符合中文表达习惯。  

**00:37:59 - 00:38:07**  
原文：So I know it doesn't look very good, but let's actually scroll up and see what it looked like when I started the optimization.  
译文：所以我知道它现在看起来不太好，但让我们往上滚动，看看我开始优化时它是怎样的。  

**00:38:07 - 00:38:15**  
原文：So all the way here at step one, so after 20 steps of optimization, you see that what we're getting here is looks completely random.  
译文：所以在第一步这里，经过20步优化后，你看到我们得到的结果看起来完全随机。  

**00:38:15 - 00:38:20**  
原文：And of course, that's because the model has only had 20 updates to its parameters.  
译文：当然，这是因为模型的参数仅更新了20次。  

**00:38:20 - 00:38:24**  
原文：And so it's given you random text because it's a random network.  
译文：所以它给你的是随机文本，因为它是随机网络。  

**00:38:24 - 00:38:29**  
原文：And so you can see that at least in comparison to this, the model is starting to do much better.  
译文：因此，你可以看到，至少与这个相比，模型开始表现得更好了。  

**00:38:29 - 00:38:37**  
原文：And indeed, if we weighted the entire 32000 steps, the model will have improved the point that is actually generating fairly coherent English.  
译文：确实，如果我们对全部32000步进行加权，模型将会改进到生成相当连贯的英语的地步。  

**00:38:37 - 00:38:44**  
原文：And the tokens stream correctly and they kind of make up English a lot better.  
译文：而且这些标记流是正确的，它们组成英语的方式要好得多。  

**00:38:45 - 00:38:49**  
原文：So this has to run for about a day or two more now.  
译文：所以这还需要运行一到两天。  

**00:38:49 - 00:38:57**  
原文：And so at this stage, we just make sure that the loss is decreasing, everything is looking good, and we just have to wait.  
译文：所以在现阶段，我们只是确保损失在减少，一切看起来都很好，我们只需要等待。  

**00:38:57 - 00:39:07**  
原文：And now let me turn now to the story of the computation that's required, because of course, I'm not running this optimization on my laptop.  
译文：现在让我来讲讲所需的计算故事， 因为当然，我不是在我的笔记本电脑上 进行这个优化的。  

**00:39:07 - 00:39:15**  
原文：That would be way too expensive because we have to run this neural network and we have to improve it, and we need all this data and so on.  
译文：这会非常昂贵，因为我们必须运行这个神经网络，我们必须改进它，我们需要所有这些数据等。  

**00:39:15 - 00:39:19**  
原文：So you can't run this too well on your computer because the network is just too large.  
译文：所以你不能在你的电脑上很好地运行这个，因为网络规模太大了。  

**00:39:19 - 00:39:23**  
原文：So all of this is running on a computer that is out there in the cloud.  
译文：所以所有这些都在云端的一台计算机上运行。  

**00:39:23 - 00:39:29**  
原文：And I want to basically address the compute side of the story of training these models and what that looks like.  
译文：我想主要谈谈训练这些模型所需的计算能力以及这看起来是怎样的。  

**00:39:29 - 00:39:30**  
原文：So let's take a look.  
译文：那么让我们来看一下。  

**00:39:30 - 00:39:36**  
原文：Okay, so the computer that I'm am running this optimization on is this eight X H 100 node.  
译文：好的，我正在运行这个优化的计算机是这台八 X H 100 节点。  

**00:39:36 - 00:39:41**  
原文：So there are eight H -100s in a single node or a single computer.  
译文：所以在一个节点或一台计算机中有八个H-100。  

**00:39:41 - 00:39:44**  
原文：Now I am renting this computer, and it is somewhere in the cloud.  
译文：现在我租用了这台计算机，它位于某个云端。  

**00:39:44 - 00:39:46**  
原文：I'm not sure where it is physically.  
译文：我不确定它具体在哪儿。  

**00:39:46 - 00:39:52**  
原文：Actually, the place I like to rent from is called lambda, but there are many other companies who provide this service.  
译文：实际上，我喜欢从一个叫作 lambda 的地方租用，但有很多其他公司也提供这项服务。  

**00:39:52 - 00:40:02**  
原文：So when you scroll down, you can see that they have some underdemand ment pricing for sort of computers that have these H1 hundrewhich are gpuand.  
译文：所以当你向下滚动时，你可以看到他们对拥有这些H1百系列GPU的电脑有一些定价偏低的情况。 

注意：原文中“hundrewhich are gpuand”这部分似乎有拼写或语法错误，我根据上下文进行了推测性的翻译。如果你有更准确的原文信息，请提供以便进行更精确的翻译。  

**00:40:02 - 00:40:06**  
原文：I'm going to show you what they look like in a second.  
译文：我将在一秒钟后向您展示它们的样子。  

**00:40:06 - 00:40:10**  
原文：But on demand, meneight times and video, H -100GPU.  
译文：但按需，me八次和视频，H -100GPU。 

注：原文本中的“meneight”看起来像是拼写错误或特殊用词，不确定其具体含义，因此直接音译为“me八次”。如果这是一个特定术语或有其他背景信息，请提供更多信息以便更准确地翻译。  

**00:40:10 - 00:40:14**  
原文：This machine comes for $3 per gpper hour, for example.  
译文：这台机器每小时的费用是3美元，例如。  

**00:40:14 - 00:40:24**  
原文：So you can rent these, and then you get a machine in a cloud, and you can go in and you can train these models and these gpus, they look like this.  
译文：所以你可以租用这些，然后你在云端得到一台机器，你可以进去训练这些模型和这些gpu，它们看起来是这样的。  

**00:40:24 - 00:40:26**  
原文：So this is one H -100GPU.  
译文：所以这是一块 H-100 GPU。  

**00:40:26 - 00:40:30**  
原文：This is kind of what it looks like, and you slot this into your computer.  
译文：这东西看起来是这样，你可以把它插入你的电脑。  

**00:40:30 - 00:40:41**  
原文：And gpus are this perfect fit for training neural networks because they are very computational expensive, but they display a lot of parallelism in the computation.  
译文：而且GPU非常适合训练神经网络，因为训练神经网络需要大量的计算资源，但其中的计算可以高度并行化。  

**00:40:41 - 00:40:52**  
原文：So you can have many independent workers kind of working all at the same time in solving the matrix multiplication that's under the hood of training these neural networks.  
译文：因此，你可以让许多独立的工作者同时工作，解决训练这些神经网络背后的矩阵乘法问题。  

**00:40:53 - 00:40:59**  
原文：So this is just one of these H -100s, but actually you would put multiple of them together.  
译文：所以这只是一个 H-100，但实际上你会将多个这样的放在一起。  

**00:40:59 - 00:41:07**  
原文：So you could stack eight of them into a single node, and then you can stack multiple nodes into an entire data center or an entire system.  
译文：所以你可以将八个单元堆叠成一个单节点， 然后你可以将多个节点堆叠成一个完整的数据中心或一个完整的系统。  

**00:41:07 - 00:41:10**  
原文：So when we look at a data center.  
译文：所以当我们看一个数据中心时。  

**00:41:12 - 00:41:13**  
原文：Can't spell.  
译文：不会拼写。  

**00:41:13 - 00:41:18**  
原文：When we look at a data center, we start to see things that look like this, right?  
译文：当我们观察一个数据中心时， 我们开始看到一些像这样的东西，是吧？  

**00:41:18 - 00:41:22**  
原文：So we have one GPU goes to eight gps goes to a single system, goes to many systems.  
译文：所以我们有一个GPU连接到八个GPS，连接到一个系统，再连接到多个系统。 

注：根据上下文，“gps”可能是指“图形处理单元（GPUs）”的拼写错误，如果是这样，则应将其理解为：

所以我们有一个GPU连接到八个GPU，连接到一个系统，再连接到多个系统。  

**00:41:22 - 00:41:24**  
原文：And so these are the bigger data centers.  
译文：所以这些都是更大的数据中心。  

**00:41:24 - 00:41:27**  
原文：And their, of course, would be much, much more expensive.  
译文：当然，它们会贵很多很多。  

**00:41:27 - 00:41:36**  
原文：And what's happening is that all the big tech companies really desire these gpus so they can train all these language models because they are so powerful.  
译文：而正在发生的事情是，所有大型科技公司都非常渴望获得这些GPU，这样他们就可以训练所有这些语言模型，因为它们非常强大。  

**00:41:36 - 00:41:45**  
原文：And that is fundamentally what has driven the stock price of mvidia to be $3.4 trillion today, as an example, and why nvidia has kind of exploded.  
译文：而这正是推动英伟达的股票价格 在今天达到3.4万亿美元的根本原因， 也是为什么英伟达会如此迅猛发展。  

**00:41:45 - 00:41:47**  
原文：So this is the gold rush.  
译文：所以这就是淘金热。  

**00:41:47 - 00:41:55**  
原文：The gold rush is getting the gpugetting enough of them so they can all collaborate to perform this optimization.  
译文：黄金潮正在获取足够的GPU，以便它们能够共同协作来执行这种优化。  

**00:41:55 - 00:41:56**  
原文：And what are they all doing?  
译文：他们在做什么？  

**00:41:56 - 00:42:03**  
原文：They're all collaborating to predict the next token on a data set, like the fine web data set.  
译文：它们都在合作以预测数据集（如精美的网络数据集）上的下一个标记。 

注意：此处的“fine web data set”直译为“精美的网络数据集”，但根据上下文，可能指的是某个特定的、经过精细处理的网络数据集。如果这是一个专有名词或特定数据集的名字，通常应保持原样不翻译，除非有官方的中文名称。所以更合适的翻译可能是：

它们都在合作以预测数据集（如 Fine Web 数据集）上的下一个标记。  

**00:42:03 - 00:42:08**  
原文：This is the computational workflow that basically is extremely expensive.  
译文：这是计算工作流程，基本上是非常昂贵的。  

**00:42:08 - 00:42:12**  
原文：The more gpus you have, the more tokens you can try to predict and improve on.  
译文：你拥有的GPU越多，你可以尝试预测和改进的令牌就越多。  

**00:42:12 - 00:42:20**  
原文：And you're going to process this data set faster, and you can iterate faster and get a bigger network and train a bigger network and so on.  
译文：而且你将更快地处理这个数据集，你可以更快地迭代，构建更大的网络，训练更大的网络，以此类推。  

**00:42:20 - 00:42:26**  
原文：So this is what all those machines that are doing, and this is why all of this is such a big deal.  
译文：所以这就是所有这些机器在做的事情，这也是为什么这一切如此重要的原因。  

**00:42:26 - 00:42:30**  
原文：And for example, this is a article from, look, about a month ago or so.  
译文：例如，这是一篇来自，看，大约一个月前的文章。  

**00:42:30 - 00:42:37**  
原文：This is why it's a big deal that, for example, Elon Musk is getting 100000 gpuin, a single data center.  
译文：这就是为什么例如埃隆·马斯克将获得100,000个GPU（在一个单一的数据中心）是一件大事。  

**00:42:37 - 00:42:52**  
原文：And all of these gpus are extremely expensive, are going to take a ton of power, and all of them are just trying to predict the next token in the sequence and improve the network by doing so, and get probably a lot more coherent text than what we're seeing here a lot faster.  
译文：而且所有这些GPU都非常昂贵，将会消耗大量的电力，而它们所做的只是试图预测序列中的下一个标记，并通过这样做来改进网络，从而可能比我们在这里看到的更快地生成连贯性更高的文本。  

**00:42:52 - 00:42:53**  
原文：Okay.  
译文：好的。  

**00:42:53 - 00:43:00**  
原文：So unfortunately, I do not have a couple ten or 100 million of dollars to spend on training a really big model like this.  
译文：所以很遗憾，我并没有几千万或一亿美元来训练这样一个非常大的模型。  

**00:43:00 - 00:43:07**  
原文：But luckily, we can turn to some big tech companies who train these models routinely and release some of them once they are done training.  
译文：但幸运的是，我们可以转向一些大型科技公司，这些公司经常训练这些模型，并在训练完成后发布其中的一些。  

**00:43:07 - 00:43:14**  
原文：So they spent a huge amount of compute to train this network, and they release the network at the end of the optimization.  
译文：所以他们花费了大量的计算资源来训练这个网络，然后在优化结束时发布了这个网络。  

**00:43:14 - 00:43:17**  
原文：So it's very useful because they've done a lot of compute for that.  
译文：所以这非常有用，因为他们为此做了大量的计算。  

**00:43:17 - 00:43:25**  
原文：So there are many companies who train these models routinely, but actually not many of them release these, what's called base models.  
译文：所以有很多公司经常训练这些模型，但实际上并没有很多公司发布这些所谓的基础模型。  

**00:43:25 - 00:43:29**  
原文：So the model that comes out at the end here is what's called a base model.  
译文：所以最后得到的模型被称为基础模型。  

**00:43:29 - 00:43:30**  
原文：What is a base model?  
译文：什么是基础模型？  

**00:43:30 - 00:43:32**  
原文：It's a token simulator, right?  
译文：它是一个代币模拟器，对吧？  

**00:43:32 - 00:43:34**  
原文：It's an Internet text token simulator.  
译文：它是一个互联网文本令牌模拟器。  

**00:43:34 - 00:43:39**  
原文：And so that is not by itself useful yet, because what we want is what's called an assistant.  
译文：这本身还不是很实用，因为我们想要的是所谓的助手。  

**00:43:39 - 00:43:43**  
原文：We want to ask questions and have it respond to answers.  
译文：我们想要提问并让其回答。  

**00:43:43 - 00:43:45**  
原文：These models won't do that.  
译文：这些模型不会这样做。  

**00:43:45 - 00:43:48**  
原文：They just create sort of remixes of the Internet.  
译文：他们只是创造了一些互联网的混音版本。  

**00:43:48 - 00:43:49**  
原文：They dream Internet pages.  
译文：他们梦想着互联网页面。  

**00:43:49 - 00:43:55**  
原文：So the base models are not very often released because they're kind of just only a step.  
译文：所以基础模型并不经常发布，因为它们只是其中的一个步骤。  

**00:43:55 - 00:43:59**  
原文：One of a few other steps that we still need to take to get an assistant.  
译文：我们仍需采取的几个步骤之一，以获得一个助手。  

**00:43:59 - 00:44:01**  
原文：However, a few releases have been made.  
译文：但是，已经发布了一些版本。  

**00:44:01 - 00:44:09**  
原文：So as an example, the GPT two model released the 1.6 billion, sorry, 1.5 billion model back in 2019.  
译文：所以作为一个例子，GPT-2模型在2019年发布了16亿个参数，对不起，是15亿个参数的模型。  

**00:44:09 - 00:44:11**  
原文：And this GPT two model is a base model.  
译文：而且这个GPT-2模型是一个基础模型。  

**00:44:11 - 00:44:14**  
原文：Now, what is a model release?  
译文：现在，什么是模特发布协议？  

**00:44:14 - 00:44:18**  
原文：What does it look like to release these models?  
译文：发布这些模型是什么样子的？  

**00:44:18 - 00:44:21**  
原文：So this is the GPT two repository on gihub.  
译文：所以这是GPT-2在GitHub上的仓库。  

**00:44:21 - 00:44:23**  
原文：Well, you need two things.  
译文：好吧，你需要两样东西。  

**00:44:23 - 00:44:34**  
原文：Basically, to release model number one, we need the Python code usually that describes the sequence of operations in detail that they make in their model.  
译文：基本上，要发布第一个模型，我们通常需要描述他们在模型中进行的操作序列的Python代码。  

**00:44:34 - 00:44:44**  
原文：So if you remember back this transformer, the sequence of steps that are taken here in this neural network is what is being described by this code.  
译文：所以如果你回想起这个变压器，这里在这个神经网络中采取的步骤序列就是这段代码所描述的内容。  

**00:44:44 - 00:44:49**  
原文：So this code is sort of implementing what's called forward PaaS of this neural network.  
译文：所以这段代码实现了所谓的这个神经网络的前向传递。  

**00:44:49 - 00:44:54**  
原文：So we need the specific details of exactly how they wired up that neural network.  
译文：所以我们需要具体的细节，关于他们是如何构建那个神经网络的。  

**00:44:54 - 00:44:59**  
原文：So this is just computer code, and it's usually just a couple hundred lines of code.  
译文：所以这仅仅是一些计算机代码， 通常只有几百行。  

**00:44:59 - 00:45:00**  
原文：It's not that crazy.  
译文：没那么疯狂。  

**00:45:00 - 00:45:04**  
原文：And this is all fairly understandable and usually fairly standard.  
译文：而且这所有的一切都是相当可以理解的，通常也是相当标准的。  

**00:45:04 - 00:45:06**  
原文：What's not standard are the parameters.  
译文：不标准的是参数。  

**00:45:06 - 00:45:08**  
原文：That's where the actual value is.  
译文：那就是实际价值所在的地方。  

**00:45:08 - 00:45:11**  
原文：Where are the parameters of this neural network?  
译文：这个神经网络的参数在哪里？  

**00:45:11 - 00:45:13**  
原文：Because there's 1.6 billion of them.  
译文：因为有16亿之多。  

**00:45:13 - 00:45:16**  
原文：And we need the correct setting or a really good setting.  
译文：并且我们需要正确的设置或是一个非常好的设置。  

**00:45:16 - 00:45:24**  
原文：And so that's why, in addition to this source code, they release the parameters, which in this case is roughly 1.5 billion parameters.  
译文：因此，除了这些源代码之外，他们还发布了参数，而在这种情况下，参数量大约为15亿。  

**00:45:24 - 00:45:25**  
原文：And these are just numbers.  
译文：这些都只是数字。  

**00:45:25 - 00:45:33**  
原文：So it's one single list of 1.5 billion numbers, the precise and good setting of all the knobs such that the tokens come out well.  
译文：所以它是一个包含15亿个数字的单一列表，所有旋钮的精确和良好的设置使得生成的令牌非常准确。  

**00:45:34 - 00:45:41**  
原文：So you need those two things to get a base model release.  
译文：所以你需要这两样东西来获得基础模型的发布。  

**00:45:41 - 00:45:46**  
原文：Now GPT two was released, but that's actually a fairly old model, as I mentioned.  
译文：现在GPT-2已经发布了，但正如我提到的，那其实是一个相当旧的模型。  

**00:45:46 - 00:45:53**  
原文：So actually the model we're going to turn to is called lama three, and that's the one that I would like to show you next.  
译文：所以我们接下来要使用的模型叫做lama three，这是我接下来想向您展示的模型。  

**00:45:53 - 00:45:58**  
原文：So lama three, so GPT two, elagain was 1.6 billion parameters trained on 100 billion tokens.  
译文：所以lama有三个，GPT有两个，而elagain则有16亿个参数，在1000亿个令牌上进行训练。  

**00:45:58 - 00:46:01**  
原文：Lama three is a much bigger model and much more modern model.  
译文：Llama three是一个更大、更现代的模型。  

**00:46:01 - 00:46:12**  
原文：It is released and trained by meta, and it is a 405 billion parameter model trained on 15 trillion tokens in very much the same way, just much, much bigger.  
译文：它由Meta发布和训练，是一个4050亿参数的模型，在非常相似的方式下训练，只是规模大了很多，基于15万亿个令牌训练。  

**00:46:12 - 00:46:19**  
原文：And meta has also made a release of lama three, and that was part of this paper.  
译文：并且 Meta 也发布了 Lama 三，这也是这篇论文的一部分。  

**00:46:19 - 00:46:29**  
原文：So with this paper that goes into a lot of detail, the biggest base model that they released is the Allama 3.1, 4.5, 405 billion parameter model.  
译文：所以，这篇论文详细介绍了他们发布的最大基础模型是参数量为405亿的Allama 3.1、4.5模型。  

**00:46:29 - 00:46:30**  
原文：So this is the base model.  
译文：所以这是基础模型。  

**00:46:30 - 00:46:37**  
原文：And then in addition to the base model you see here, foreshadowing for later sections of the video, they also released the instruct model.  
译文：除了这里看到的基础模型外，预示着视频的后续部分，他们还发布了指令模型。  

**00:46:37 - 00:46:39**  
原文：And the int means that this is an assistant.  
译文：And the int意味着这是一个助手。  

注：这里的“int”可能是英文“integer”的缩写，在编程中表示整数类型，但根据上下文，“int”可能没有特定含义或是一个拼写错误。如果需要更准确的翻译，请提供更多的上下文信息。  

**00:46:39 - 00:46:42**  
原文：You can ask it questions, and it will give you answers.  
译文：您可以向它提问，它会为您提供答案。  

**00:46:42 - 00:46:44**  
原文：We still have yet to cover that part later.  
译文：我们还将在稍后覆盖那部分内容。  

**00:46:44 - 00:46:57**  
原文：For now, let's just look at this base model, this token simulator, and let's play with it and try to think about, you know what is this thing and how does it work and what do we get at the end of this optimization.  
译文：目前，我们只看这个基础模型，这个令牌模拟器，让我们来玩弄它并尝试思考，这东西是什么，它是如何工作的，以及我们在优化结束时能得到什么。  

**00:46:57 - 00:47:02**  
原文：If you let this run until the end for a very big neural network on a lot of data.  
译文：如果你让这个过程在一个非常大的神经网络上针对大量数据运行到结束。  

**00:47:02 - 00:47:12**  
原文：So my favorite place to interact with the base models is this company called hyperbolic, which is basically serving the base model of the 405b, llama 3.1.  
译文：所以我最喜欢与基础模型互动的公司叫做Hyperbolic，这家公司主要提供405b版本的LLaMA 3.1基础模型。  

**00:47:12 - 00:47:21**  
原文：So when you go into the web site, and I think you may have to register and so on, make sure that in the models, make sure that you are using llama 3.145 billion base.  
译文：所以当你进入网站时，我认为你可能需要注册等，确保在模型中，确认你使用的是31.45亿参数的基础版llama。  

**00:47:21 - 00:47:22**  
原文：It must be the base model.  
译文：它必须是基础模型。  

**00:47:22 - 00:47:27**  
原文：And then here, let's say the max tokens is how many tokens we're going to be generating.  
译文：然后在这里，假设最大令牌数是我们将要生成的令牌数量。  

**00:47:27 - 00:47:30**  
原文：So let's just decrease this to be a bit less just so we don't waste compute.  
译文：所以让我们将这个减少一些，以避免浪费计算资源。  

**00:47:30 - 00:47:34**  
原文：We just want the next 128 tokens and leave the other stuff alone.  
译文：我们只是想要接下来的128个标记，并保留其他内容不变。  

**00:47:34 - 00:47:37**  
原文：I'm not going to go into the full detail here.  
译文：我不会在这里详述。  

**00:47:37 - 00:47:43**  
原文：Now fundamentally, what's going to happen here is identical to what happens here during inference for us.  
译文：现在从根本上说，这里将要发生的事情与我们在推理过程中发生的事情是相同的。  

**00:47:43 - 00:47:49**  
原文：So this is just going to continue the dken sequence of whatever prefix you're going to give it.  
译文：所以这将继续你给定的任何前缀的dken序列。  

**00:47:49 - 00:47:53**  
原文：So I want to first show you that this model here is not yet an assistant.  
译文：所以，我首先想向您展示，这个模型还不是一个助手。  

**00:47:53 - 00:47:56**  
原文：So you can, for example, ask it, what is two plus two?  
译文：所以，比如，你可以问它，二加二等于多少？  

**00:47:56 - 00:47:58**  
原文：It's not going to tell you, Oh, it's four.  
译文：它不会告诉你，哦，它是四。  

**00:47:58 - 00:47:59**  
原文：What else can I help you with?  
译文：我還可以帮您做些什么？  

**00:47:59 - 00:48:04**  
原文：It's not going to do that because what is two plus two is going to be tokenized.  
译文：它不会那样做，因为二加二会被分词。  

**00:48:04 - 00:48:06**  
原文：And then those tokens just acts as a prefix.  
译文：然后这些令牌只是作为前缀。  

**00:48:06 - 00:48:12**  
原文：And then what the model is going to do now is just going to get the probability for the next token.  
译文：然后模型要做的就是计算下一个标记的概率。  

**00:48:12 - 00:48:14**  
原文：And it's just a glorified auto complete.  
译文：它只是一个 glorified 自动完成。  

注：此处“glorified”可以理解为“被美化了的”或“高级的”，根据上下文可以调整为更合适的表达，例如：“它只是一个高级的自动完成功能。” 若要保持原始格式和用词，则如上所示。  

**00:48:14 - 00:48:22**  
原文：It's a very, very expensive auto complete of what comes next, depending on the statistics of what it's saw in its train documents, which are basically web pages.  
译文：这是一个非常、非常昂贵的自动完成功能，用于预测接下来会出现什么，这取决于它在训练文档（基本上是网页）中看到的内容的统计情况。  

**00:48:22 - 00:48:28**  
原文：So let's just hit enter to see what tokens it comes up with as a continuation.  
译文：所以让我们直接按回车键，看看它会生成什么令牌作为续写。  

**00:48:31 - 00:48:38**  
原文：Okay, so here it kind of actually answered the question and started to go off into some philosophical territory.  
译文：好的，所以这里它实际上回答了问题，然后开始偏离进入了一些哲学领域。  

**00:48:38 - 00:48:39**  
原文：Let's try it again.  
译文：让我们再试一次。  

**00:48:39 - 00:48:42**  
原文：So let me copy and paste and let's try again from scratch.  
译文：所以让我复制和粘贴，然后让我们从头再试一次。  

**00:48:42 - 00:48:43**  
原文：Where is two plus two?  
译文：二加二在哪里？  

**00:48:46 - 00:48:46**  
原文：Okay.  
译文：好的。  

**00:48:46 - 00:48:48**  
原文：So it just goes off again.  
译文：所以它又再次出发。  

**00:48:48 - 00:48:56**  
原文：So notice one more thing that I want to stress is that the system, I think every time you put it in, it just kind of starts from scratch.  
译文：所以请注意我还想强调的一点是，这个系统，我认为每次你使用它时，它都像是从头开始一样。  

**00:48:57 - 00:49:00**  
原文：So it doesn't the system here is stochastic.  
译文：所以这里的系统是随机的。  

**00:49:00 - 00:49:05**  
原文：So for the same prefix of tokens, we're always getting a different answer.  
译文：所以对于相同的标记前缀，我们总是得到不同的答案。  

**00:49:05 - 00:49:16**  
原文：And the reason for that is that we get this probdistribution and we sample from it and we always get different samples and we sort of always go into a different territory afterwards.  
译文：原因是这样的：我们得到这个概率分布，然后从其中采样，每次采样结果都不同，因此我们之后总是进入不同的领域。  

**00:49:16 - 00:49:19**  
原文：So here in this case, I don't know what this is.  
译文：所以在这里，我不知道这是什么。  

**00:49:19 - 00:49:20**  
原文：Let's try one more time.  
译文：让我们再试一次。  

**00:49:23 - 00:49:25**  
原文：So just continues on.  
译文：所以就继续下去。  

**00:49:25 - 00:49:29**  
原文：So it's just doing the stuff that it's selling on the Internet, right?  
译文：所以它只是在做它在网上卖的东西，对吧？  

**00:49:29 - 00:49:32**  
原文：And it's just kind of like regurgitating those statistical patterns.  
译文：这就像是一种对统计模式的重复。  

**00:49:33 - 00:49:36**  
原文：So first things, it's not an assistant yet.  
译文：所以首先说明，它现在还不是一个助手。  

**00:49:36 - 00:49:38**  
原文：It's a token auto complete.  
译文：它是令牌自动完成。  

**00:49:38 - 00:49:41**  
原文：And second, it is a stochastic system.  
译文：第二，它是一个随机系统。  

**00:49:41 - 00:50:02**  
原文：Now the crucial thing is that even though this model is not yet by itself very useful for a lot of applications just yet, it is still very useful because in the task of predicting the next token in the sequence, the model has learned a lot about the world, and it has stored all that knowledge in the parameters of the network.  
译文：现在关键的一点是，即使这个模型本身对于许多应用来说还不是很实用，它仍然非常有用，因为在预测序列中下一个标记的任务中，模型已经学到了很多关于世界的知识，并且它已经将所有这些知识存储在网络的参数中。  

**00:50:02 - 00:50:05**  
原文：So remember that our text looked like this, right?  
译文：所以记住，我们的文本看起来是这样的，对吧？  

**00:50:05 - 00:50:06**  
原文：Internet, web pages.  
译文：互联网，网页。  

**00:50:06 - 00:50:11**  
原文：And now all of this is sort of compressed in the weights of the network.  
译文：现在所有这些都压缩在网络的权重中。  

**00:50:11 - 00:50:17**  
原文：So you can think of these 405 billion parameters as a kind of compression of the Internet.  
译文：所以你可以将这405亿个参数视为互联网的一种压缩形式。  

**00:50:17 - 00:50:25**  
原文：You can think of the 405 billion parameters as kind of like a zip file, but it's not a loss less compression.  
译文：你可以将这405亿个参数想象成类似于一个压缩文件，但它的压缩方式并不是无损的。  

**00:50:25 - 00:50:26**  
原文：It's a lost c compression.  
译文：这是一个丢失的压缩。  

**00:50:26 - 00:50:32**  
原文：We're kind of like left with kind of a gestaof the Internet, and we can generate from it right now.  
译文：我们某种程度上遗留下来的是互联网的概念，而我们现在可以从这个概念出发进行创造。  

**00:50:32 - 00:50:37**  
原文：We can elicit some of this knowledge by prompting the base model accordingly.  
译文：我们可以通过相应地提示基础模型来激发其中的一些知识。  

**00:50:37 - 00:50:44**  
原文：So for example, here's a prompt that might work to elicit some of that knowledge that's hiding in the parameters.  
译文：所以，例如，以下是一个可能有效的提示，可以激发隐藏在参数中的一些知识。  

**00:50:44 - 00:50:47**  
原文：Here's my top ten list of the top line Marks you see in Paris.  
译文：以下是我在巴黎看到的十大顶级品牌清单。  

**00:50:48 - 00:50:55**  
原文：And I'm doing it this way because I'm trying to prime the model to now continue this list.  
译文：我以这种方式来做，是因为我试图引导模型继续这个列表。  

**00:50:55 - 00:50:57**  
原文：So let's see if that works when I Press enter.  
译文：那么让我们看看当我按下回车键时是否有效。  

**00:50:57 - 00:51:07**  
原文：Okay, so you see that it's started the list and it's now kind of giving you some of those landmarks and now notice that it's trying to give a lot of information here.  
译文：好的，所以你看到它已经开始列出清单，现在它开始给出一些地标信息，注意它现在试图提供大量的信息。  

**00:51:07 - 00:51:11**  
原文：Now you might not be able to actually fully trust some of the information here.  
译文：现在你可能无法完全信任这里的一些信息。  

**00:51:11 - 00:51:15**  
原文：Remember that this is all just a recollection of some of the Internet documents.  
译文：请记住，这仅仅是某些互联网文档的回忆。  

**00:51:15 - 00:51:24**  
原文：And so the things that occur very frequently in the Internet data are probably more likely to be remembered correctly compared to things that happen very infrequently.  
译文：因此，互联网数据中频繁出现的事物 相对于非常罕见的事物 更有可能被正确记住。  

**00:51:24 - 00:51:36**  
原文：So you can't fully trust some of the things that and some of the information that is here, because it's all just a vague recollection of Internet documents, because the information is not stored explicitly in any of the parameters.  
译文：所以你不能完全信任这里的一些内容和信息，因为这都只是对互联网文档的模糊回忆，因为信息并没有明确地存储在任何参数中。  

**00:51:36 - 00:51:37**  
原文：It's all just the recollection.  
译文：这都只是回忆。  

**00:51:37 - 00:51:41**  
原文：That said, we did get something that is probably approximately correct.  
译文：也就是说，我们确实得到了一些可能大致正确的东西。  

**00:51:41 - 00:51:46**  
原文：And I don't actually have the expertise to verify that this is roughly correct.  
译文：而且我实际上没有专业知识来验证这是否大致正确。  

**00:51:46 - 00:51:52**  
原文：But you see that we've elicited a lot of the knowledge of the model, and this knowledge is not precise and exact.  
译文：但您可以看到，我们已经引出了模型的许多知识，而且这些知识并不精确和确切。  

**00:51:52 - 00:51:55**  
原文：This knowledge is vague and probabilistic and statistical.  
译文：这种知识是模糊的、概率性的和统计的。  

**00:51:55 - 00:52:02**  
原文：The kinds of things that occur often are the kinds of things that are more likely to be remembered in the model.  
译文：经常发生的事情更有可能被模型记住。  

**00:52:02 - 00:52:06**  
原文：Now I want to show you a few more examples of this model's behavior.  
译文：现在我想给您展示几个更多关于这个模型行为的例子。  

**00:52:06 - 00:52:09**  
原文：The first thing I want to show you is this example.  
译文：我想首先给你展示的是这个例子。  

**00:52:09 - 00:52:16**  
原文：I went to the Wikipedia page for zebra, and let me just copy paste the first, even one sentence here, and let me put it here.  
译文：我去了维基百科的斑马页面，让我直接复制粘贴第一句话在这里，让我把它放在这里。  

**00:52:16 - 00:52:21**  
原文：Now, when I click enter, what kind of completion are we going to get?  
译文：现在，当我按下回车键时，我们会得到什么样的补全结果？  

**00:52:21 - 00:52:23**  
原文：So let me just hit enter.  
译文：所以让我直接按回车键。  

**00:52:23 - 00:52:28**  
原文：There are three living species, etc., etc..  
译文：有三种现存物种，等等，等等。  

**00:52:28 - 00:52:33**  
原文：What the model is producing here is an exact regururgitation of this Wikipedia entry.  
译文：模型在这里生成的是这个维基百科条目的精确复述。  

**00:52:33 - 00:52:36**  
原文：It is reciting this Wikipedia entry purely from memory.  
译文：它完全是凭记忆背诵这个维基百科条目。  

**00:52:36 - 00:52:39**  
原文：And this memory is stored in its parameters.  
译文：并且这个记忆存储在其参数中。  

**00:52:39 - 00:52:46**  
原文：And so it is possible that at some point in these 512 tokens, the model will stray away from the Wikipedia entry.  
译文：因此，在这512个标记中的某一点上，模型可能会偏离维基百科的条目。  

**00:52:46 - 00:52:49**  
原文：But you can see that it has huge chunks of it memorized here.  
译文：但你可以看到，它在这里记住了很大的一部分。  

**00:52:49 - 00:52:52**  
原文：Let me see, for example, if this sentence occurs by now.  
译文：让我看看，例如，到目前为止，这句话是否已经出现。  

**00:52:52 - 00:52:56**  
原文：Okay, so this so we're still on track.  
译文：好的，所以我们仍然按计划进行。  

**00:52:56 - 00:52:58**  
原文：Let me check here.  
译文：让我在这里检查一下。  

**00:52:59 - 00:53:01**  
原文：Okay, we're still on track.  
译文：好的，我们仍然按计划进行。  

**00:53:01 - 00:53:04**  
原文：It will eventually stray away.  
译文：它最终会偏离轨道。  

（保持了原始格式，仅进行了翻译）  

**00:53:04 - 00:53:05**  
原文：Okay.  
译文：好的。  

**00:53:05 - 00:53:08**  
原文：So this thing is just recited to a very large extent.  
译文：所以这东西在很大程度上只是被背诵。  

**00:53:08 - 00:53:12**  
原文：It will eventually deviate because it won't be able to remember exactly.  
译文：它最终会偏离，因为它无法完全记住。  

**00:53:12 - 00:53:18**  
原文：Now, the reason that this happens is because these models can be extremely good at memorization.  
译文：现在，这种情况发生的原因是这些模型可以非常擅长记忆。  

**00:53:18 - 00:53:27**  
原文：And usually this is not what you want in the final model, and this is something called regurgitation, and it's usually undesirable to cite things directly that you have trained on.  
译文：通常这并不是你想要的最终模型的结果，这种现象被称为复述，通常直接引用训练内容是不理想的。  

**00:53:27 - 00:53:45**  
原文：Now, the reason that this happens actually is because for a lot of documents, like, for example, Wikipedia, when these documents are deemed to be of a very high quality as a source, like, for example, Wikipedia, it is very often the case that when you train the model, you will preferentially sample from those sources.  
译文：现在，这种情况发生的原因实际上是由于对于许多文档而言，比如像维基百科这样的文档，当这些文档被认为是一个非常高质量的来源时，就像维基百科一样，在训练模型时，你往往会优先从这些来源中采样。  

**00:53:45 - 00:53:52**  
原文：So basically, the model has probably done a few epochs on this data, meaning that it has seen this web page like maybe probably ten times or so.  
译文：所以基本上，模型可能已经对这些数据进行了几次epoch，这意味着它可能看过这个网页大约十次左右。  

**00:53:52 - 00:54:00**  
原文：And it's a bit like you like when you read some kind of a text many, many times, say you read something 100 times, then you will be able to recite it.  
译文：这有点像你多次阅读某种文本一样，比如说你读某样东西100次，那么你就能背诵它了。  

**00:54:00 - 00:54:02**  
原文：And it's very similar for this model.  
译文：这个模型也非常相似。  

**00:54:02 - 00:54:06**  
原文：If it sees something way too often, it's going to be able to recite it later from memory.  
译文：如果它看到某样东西过于频繁，它以后将能够背诵出来。  

**00:54:06 - 00:54:11**  
原文：Except these models can be a lot more efficient like per presentation than a human.  
译文：除了这些模型在每次展示时可以比人类高效得多。  

**00:54:11 - 00:54:17**  
原文：So probably it's only seen this Wikipedia entry ten times, but basically it has remembered this article exactly in its parameters.  
译文：所以可能它只看过这个维基百科条目十次， 但基本上它已经记住了这篇文章的所有参数。  

**00:54:17 - 00:54:17**  
原文：Okay.  
译文：好的。  

**00:54:17 - 00:54:22**  
原文：The next thing I want to show you is something that the model has definitely not seen during its training.  
译文：接下来我要给你展示的东西是模型在训练过程中肯定没有见过的。  

**00:54:22 - 00:54:33**  
原文：So for example, if we go through the paper and then we navigate to the pre training data, we'll see here that the data set has a knowledge cut off until the end of 2023.  
译文：所以，例如，如果我们浏览这篇论文，然后导航到预训练数据部分，我们会在这里看到数据集的知识截止时间是2023年底。  

**00:54:33 - 00:54:36**  
原文：So it will not have seen documents after this point.  
译文：因此，它将不会看到此后的文档。  

**00:54:36 - 00:54:41**  
原文：And certainly, it has not seen anything about the 2024 election.  
译文：当然，它没有看到任何关于2024年选举的信息。  

**00:54:41 - 00:54:54**  
原文：And now it turned out, now if we prime the model with the tokens from the future, it will continue the tokens sequence and it will just take its best guess according to the knowledge that it has in its own parameters.  
译文：而现在发现，如果我们现在用来自未来的 token 来预处理模型，它将继续 token 序列，并且它只会根据其自身参数中所包含的知识做出最佳猜测。  

**00:54:54 - 00:54:57**  
原文：So let's take a look at what that could look like.  
译文：所以让我们来看看那可能会是什么样子。  

**00:54:57 - 00:55:03**  
原文：So the Republican party could Trump okay, president of the United States from 2017.  
译文：所以共和党可以让特朗普在2017年成为美国总统。  

**00:55:03 - 00:55:06**  
原文：And let's see what it says after this point.  
译文：让我们看看这一点之后它说了什么。  

**00:55:06 - 00:55:11**  
原文：So for example, the model will have to guess at the running mate and who witagainst, etcetera.  
译文：所以，例如，模型将不得不猜测竞选搭档是谁，以及与谁竞争等。  

**00:55:11 - 00:55:12**  
原文：So let's hit enter.  
译文：所以让我们按下回车键。  

**00:55:12 - 00:55:21**  
原文：So here are things that Mike pence was the running mate instead of jd vz, and the ticket was against Hillary Clinton and Tim caane.  
译文：所以这里有几件事是关于迈克·彭斯作为竞选伙伴而不是J.D.万兹的情况，当时的竞选对手是希拉里·克林顿和蒂姆·凯恩。  

**00:55:21 - 00:55:26**  
原文：So this is kind of an interesting peril universe potentially of what could have happened.  
译文：所以这可能是曾经可能发生的一种有趣的风险宇宙。  

**00:55:26 - 00:55:30**  
原文：According to the alum, let's get a different sample.  
译文：根据校友的说法，让我们取一个不同的样本。  

**00:55:30 - 00:55:33**  
原文：So the identical prompt and let's resample.  
译文：所以相同的提示，让我们重新采样。  

**00:55:34 - 00:55:39**  
原文：So here the running mate was Ron DeSantis and they ran against jobiden and Kamala Harris.  
译文：所以这里的竞选搭档是罗恩·德桑蒂斯，他们与乔·拜登和卡玛拉·哈里斯竞争。  

**00:55:39 - 00:55:41**  
原文：So this is again, a different parallel universe.  
译文：所以这又是，一个不同的平行宇宙。  

**00:55:41 - 00:55:46**  
原文：So the model will take educated guesses and it will continue the token sequence based on this knowledge.  
译文：所以模型会做出有根据的猜测，并且它会根据这些知识继续生成 token 序列。  

**00:55:46 - 00:55:51**  
原文：And it will just kind of like all of what we're seeing here is what's called hallucination.  
译文：而且，我们在这里看到的所有东西都被称为幻觉。  

**00:55:51 - 00:55:55**  
原文：The model is just taking its best guess in a probabilistic manner.  
译文：该模型只是以概率的方式做出其最好的猜测。  

**00:55:55 - 00:56:06**  
原文：The next thing I would like to show you is that even though this is a base model and not yet an assistant model, it can still be utilized in practical applications if you are clever with your prompt design.  
译文：接下来，我想向您展示的是，即使这是一个基础模型而不是助理模型，只要您在提示设计上足够巧妙，它仍然可以在实际应用中发挥作用。  

**00:56:06 - 00:56:10**  
原文：So here's something that we would call a few shot prompt.  
译文：所以这里有一个我们会称之为少量示例提示的内容。  

**00:56:10 - 00:56:17**  
原文：So what it is here is that I have ten words or ten pairs, and each pair is a word of English column.  
译文：所以这里有的是，我有十个单词或十对单词，每对中的单词来自英语列。  

**00:56:17 - 00:56:21**  
原文：And then the translation inquiry on and we have ten of them.  
译文：然后翻译查询开启，我们有十个这样的查询。  

**00:56:21 - 00:56:25**  
原文：And what the model does here is at the end we have teacher column.  
译文：在这个模型中，最终我们得到了一个教师列。  

**00:56:25 - 00:56:31**  
原文：And then here's where we're going to do a completion of, say, just five tokens.  
译文：然后我们在这里将完成，比如说，仅仅五个标记。  

**00:56:31 - 00:56:35**  
原文：And these models have what we call in context learning abilities.  
译文：这些模型具有我们所说的上下文学习能力。  

**00:56:35 - 00:56:49**  
原文：And what that's referring to is that as it is reading this context, it is learning sort of in place that there's some kind of an algorithmic pattern going on in my data, and it knows to continue that pattern.  
译文：And what that's referring to is that as it is reading this context, it is learning sort of in place that there's some kind of an algorithmic pattern going on in my data, and it knows to continue that pattern. 

这段话的意思是：当它读取这个上下文时，它会就地学习到我的数据中存在某种算法模式，并且它知道如何继续这种模式。  

**00:56:49 - 00:56:52**  
原文：And this is called kind of like in context learning.  
译文：这被称为类似于上下文中的学习。  

**00:56:52 - 00:56:55**  
原文：So it takes on the role of a translator.  
译文：所以它承担了翻译的角色。  

**00:56:55 - 00:57:01**  
原文：And when we hit completion, we see that the teacher translation is suncenyme, which is correct.  
译文：当我们完成时，我们看到教师的翻译是 suncenyme，这是正确的。  

**00:57:01 - 00:57:08**  
原文：And so this is how you can build apps by being clever where your prompting, even though we still just have a base model for now.  
译文：所以，这就是如何通过巧妙地提示来构建应用程序的方法，即使我们目前仍然只有一个基础模型。  

**00:57:08 - 00:57:12**  
原文：And it relies on what we call this in context learning ability.  
译文：它依赖于我们在上下文中称为这种学习能力。  

（注意：根据上下文，这句话可能需要进一步调整以确保准确性和流畅性。如果你能提供更多的背景信息，我可以帮助改进翻译。）  

**00:57:12 - 00:57:16**  
原文：And it is done by constructing what's called a few shot prompt.  
译文：这是通过构建所谓的少数示例提示来完成的。  

**00:57:16 - 00:57:16**  
原文：Okay.  
译文：好的。  

**00:57:16 - 00:57:24**  
原文：And finally, I want to show you that there is a clever way to actually instantiate a whole language model assistant just by prompting.  
译文：最后，我想向您展示有一种巧妙的方法，只需通过提示就可以实例化一个完整的语言模型助手。  

**00:57:24 - 00:57:37**  
原文：And the trick to it is that we're going to structure a prompt to look like a web page, that is a conversation between a helpful AI assistant and a human, and then the model will continue that conversation.  
译文：诀窍在于我们将构建一个提示，使其看起来像一个网页，即在乐于助人的AI助手和人类之间进行的对话，然后模型将继续这一对话。  

**00:57:37 - 00:57:47**  
原文：So actually, to write the prompt, I turned to ChatGPT itself, which is kind of meta, but I told it, I want to create an alm assistant, but all I have is the base model.  
译文：所以实际上，为了撰写这个提示，我转向了ChatGPT本身，这有点元（自指），但我告诉它，我想创建一个alm助手，但我只有基础模型。 

注：这里的“alm”可能是特定领域或有特殊含义的缩写，如果能提供更多背景信息，可以更准确地翻译。  

**00:57:47 - 00:57:49**  
原文：So can you please write my prompt?  
译文：那么你能帮我写一下提示语吗？  

**00:57:49 - 00:57:53**  
原文：And this is what it came up with, which is actually quite good.  
译文：而且它想出的办法实际上相当不错。  

**00:57:53 - 00:57:57**  
原文：So here's a conversation between an AI assistant and a human.  
译文：所以这里是一段AI助手和人类之间的对话。  

**00:57:57 - 00:58:02**  
原文：The AI assistant is knowledgeable, helpful, get little events during wide variety questions, etcetera.  
译文：AI助手知识渊博，乐于助人，在回答各种问题时表现出色，等等。  

**00:58:02 - 00:58:06**  
原文：And then here, it's not enough to just give it a sort of description.  
译文：然后在这里，仅仅给出描述是不够的。  

**00:58:06 - 00:58:09**  
原文：It works much better if you create this Future Shop prompt.  
译文：如果你创建这个 Future Shop 提示，效果会好得多。  

**00:58:09 - 00:58:12**  
原文：So here's a few terms of human assistant.  
译文：所以这里有一些人类助手的术语。  

**00:58:12 - 00:58:13**  
原文：Human assistant.  
译文：人类助手。  

**00:58:13 - 00:58:17**  
原文：And we have, you know a few terms of conversation.  
译文：我们有一些对话的术语。  

**00:58:17 - 00:58:23**  
原文：And then here at the end is we're going to be putting the actual query that we like.  
译文：然后在这里结束的是，我们将要放入我们喜欢的实际查询。  

**00:58:23 - 00:58:26**  
原文：So let me copy paste this into the base model prompt.  
译文：那么让我将此复制粘贴到基础模型提示中。  

**00:58:26 - 00:58:28**  
原文：And now let me do human column.  
译文：现在让我来做一个关于人的专栏。  

**00:58:28 - 00:58:31**  
原文：And this is where we put our actual prompt.  
译文：这是我们输入实际提示的地方。  

**00:58:31 - 00:58:32**  
原文：Why is this sky blue?  
译文：为什么这片天空是蓝色的？  

**00:58:33 - 00:58:34**  
原文：And let's run assistant.  
译文：并让我们运行助手。  

**00:58:34 - 00:58:40**  
原文：The sky appears blue due to the phenomenon cold ray lights, catattering, etc., etc..  
译文：天空呈现蓝色是由于冷射线光、散射等现象造成的。  

注意：原文中“catattering”不是标准英文单词，我将其理解为可能是“散射”（scattering）的误拼。如果您有其他意图，请告知。  

**00:58:40 - 00:58:44**  
原文：So you see that the base model is just continuing the sequence.  
译文：所以你看到基础模型只是在继续这个序列。  

**00:58:44 - 00:58:57**  
原文：But because the sequence looks like this conversation, it takes on that rule, but it is a little subtle because here it just, you know it ends the assistant and then just, you know, hallucinates the next question by the human ettera.  
译文：但因为序列看起来像这次对话，它遵循了这一规则，不过这有点微妙，因为在这里它只是，你知道的，结束了助手的部分，然后就，你知道的，凭空想象出了人类的下一个问题等等。  

**00:58:57 - 00:58:59**  
原文：So it will just continue going on.  
译文：所以它会一直持续下去。  

**00:58:59 - 00:58:59**  
原文：Non.  
译文：不。  

**00:58:59 - 00:59:03**  
原文：But you can see that we have sort of accomplished a task.  
译文：但你可以看到，我们某种程度上完成了一项任务。  

**00:59:03 - 00:59:05**  
原文：And if you just took this, why is this sky blue?  
译文：如果你只是看了这个，为什么天空是蓝色的？  

**00:59:05 - 00:59:12**  
原文：And if we just refresh this and put it here, then of course, we don't expect this to work with a base model, right?  
译文：如果我们只是刷新这个并把它放在这里，那么当然，我们不期望基础模型能工作，是吧？  

**00:59:12 - 00:59:14**  
原文：We're just going to who knows what we're going to get, okay?  
译文：我们即将去，谁知道我们会得到什么，好吧？  

**00:59:14 - 00:59:17**  
原文：We're just going to get more questions, okay?  
译文：我们只会得到更多的问题，好吗？  

**00:59:17 - 00:59:22**  
原文：So this is one way to create an assistant, even though you may only have a base model, okay?  
译文：所以这是一种创建助手的方法，即使你可能只有一个基础模型，对吧？  

**00:59:22 - 00:59:28**  
原文：So this is the kind of brief summary of the things we talked about over the last few minutes.  
译文：所以这就是我们在过去几分钟里讨论的内容的一个简要总结。  

**00:59:28 - 00:59:32**  
原文：Now let me zoom out here.  
译文：现在让我在这里放大。 

注：根据上下文，"zoom out" 通常指的是“缩小”或“拉远”，以看到更广泛的视图。如果你的意思是“zoom out”（缩小/拉远），则应翻译为：

现在让我在这里缩小。  

**00:59:33 - 00:59:36**  
原文：And this is kind of like what we've talked about so far.  
译文：这有点像我们迄今为止所讨论的内容。  

**00:59:36 - 00:59:39**  
原文：We wish to train llm assistants like chashebt.  
译文：我们希望训练像chashebt这样的大型语言模型助手。  

**00:59:39 - 00:59:53**  
原文：We've discussed the first stage of that, which is the pre training stage, and we saw that really what it comes down to is we take Internet documents, we break them up into these tokens, these atoms of little text chunks, and then we predict token sequences using neural networks.  
译文：我们已经讨论了第一阶段，即预训练阶段，我们看到实际上归结为以下几点：我们获取互联网文档，将它们分解成这些标记，这些小文本块的基本单位，然后我们使用神经网络来预测标记序列。  

**00:59:53 - 00:59:56**  
原文：The output of this entire stage is this base model.  
译文：此整个阶段的输出是这个基础模型。  

**00:59:56 - 00:59:59**  
原文：It is the setting of the parameters of this network.  
译文：这是设置这个网络的参数。  

**00:59:59 - 01:00:04**  
原文：And this base model is basically an Internet document simulator on the token level.  
译文：而且这个基础模型基本上是在令牌级别上模拟互联网文档的。  

**01:00:04 - 01:00:10**  
原文：So it can just, it can generate token sequences that have the same kind of like statistics as Internet documents.  
译文：所以它能够生成的令牌序列，具有与互联网文档相同的统计特性。  

**01:00:10 - 01:00:15**  
原文：And we saw that we can use it in some applications, but we actually need to do better.  
译文：我们看到可以在一些应用中使用它，但实际上我们需要做得更好。  

**01:00:15 - 01:00:20**  
原文：We want an assistant, we want to be able to ask questions, and we want the model to give us answers.  
译文：我们想要一个助手，我们希望能够提问，我们希望模型能够给我们答案。  

**01:00:20 - 01:00:26**  
原文：And so we need to now go into the second stage, which is called the post training stage.  
译文：因此，我们现在需要进入第二阶段，即所谓的训练后阶段。  

**01:00:26 - 01:00:31**  
原文：So we take our base model, our internal document simulator, and hand it off to post training.  
译文：所以我们采用我们的基础模型，我们的内部文档模拟器，并将其交给-post training。 

注：这里的“post training”可能是指特定的训练阶段或者团队，根据上下文不同，翻译也会有所不同。如果是指“微调”这一过程，可以译为：所以我们采用我们的基础模型，我们的内部文档模拟器，并将其交由微调阶段处理。  

**01:00:31 - 01:00:36**  
原文：So we're now going to discuss a few ways to do what's called post training of these models.  
译文：所以我们现在将讨论几种方法，来对这些模型进行所谓的训练后处理。  

**01:00:36 - 01:00:41**  
原文：These stages in post training are going to be computationally much less expensive.  
译文：这些训练后的阶段在计算上将便宜得多。  

**01:00:41 - 01:00:49**  
原文：Most of the computational work, all of the massive data centers and all of the sort of heavy compute and millions of dollars are the ptraining stage.  
译文：大部分的计算工作、所有大型数据中心以及所有的重型计算和数以百万计的美元都投入在训练阶段。  

**01:00:50 - 01:00:59**  
原文：But now we're going to this slightly cheaper but still extremely important stage called post training, where we turn this llm model into an assistant.  
译文：但我们现在要进入这个稍微便宜一些但仍极其重要的阶段，称为post training（后训练），在这个阶段我们将这个大语言模型变成一个助手。  

**01:00:59 - 01:01:06**  
原文：So let's take a look at how we can get our model to not sample Internet documents, but to give answers to questions.  
译文：所以，让我们来看看如何让我们的模型不采样互联网文档，而是回答问题。  

**01:01:06 - 01:01:11**  
原文：So in other words, what we want to do is we want to start thinking about conversations.  
译文：换句话说，我们想要开始思考对话。  

**01:01:11 - 01:01:15**  
原文：And these are conversations that can be multiti turn, so that can be multiple turns.  
译文：而且这些对话可以是多轮次的，所以可以有多轮次。  

**01:01:15 - 01:01:20**  
原文：They are, in the simplest case, a conversation between a human and an assistant.  
译文：最简单的情况是，它们是人类和助手之间的一段对话。  

**01:01:20 - 01:01:23**  
原文：And so, for example, we can imagine that the conversation could look simple like this.  
译文：因此，例如，我们可以想象对话可能会简单地像这样进行。  

**01:01:23 - 01:01:25**  
原文：When a human says, what is two plus two?  
译文：当一个人说，二加二等于多少？  

**01:01:25 - 01:01:28**  
原文：The assistant should respond with something like two plus two is four.  
译文：助手应该回答类似二加二等于四。  

**01:01:28 - 01:01:31**  
原文：When a human follows up and says, what if it was star instead of a plus?  
译文：当一个人跟进说，如果是星号而不是加号呢？  

**01:01:31 - 01:01:34**  
原文：Assistant could respond with something like this and similar here.  
译文：助手可以这样回应，类似于此。  

**01:01:34 - 01:01:41**  
原文：This is another example showing that the assistant could also have some kind of a personality here, that it's kind of like nice.  
译文：这是另一个例子，表明助手在这里也可以有一些个性，就是说它有点友好。  

**01:01:41 - 01:01:49**  
原文：And then here in the third example, I'm showing that when a human is asking for something that we don't wish to help with, we can produce what's called a refusal.  
译文：在第三个例子中，我展示了当人类要求我们做不愿意帮助的事情时，我们可以产生所谓的拒绝。  

**01:01:49 - 01:01:51**  
原文：We can say that we cannot help with that.  
译文：我们可以表示我们无法提供帮助。  

**01:01:51 - 01:02:02**  
原文：So in other words, what we want to do now is we want to think through how an assistant should interact with a human, and we want to program the assistant and its behavior in these conversations.  
译文：所以，换句话说，我们现在想要做的是思考助理应当如何与人类互动，并且我们想要编程设定助理在这些对话中的行为。  

**01:02:02 - 01:02:08**  
原文：Now, because this is neural networks, we're not going to be programming these explicitly in code.  
译文：现在，因为这是神经网络，我们不会在代码中显式地编程这些。  

**01:02:08 - 01:02:13**  
原文：We're not going to be able to program the assiin that way, because this is neural networks.  
译文：我们无法以这种方式编程，因为这是神经网络。  

**01:02:13 - 01:02:16**  
原文：Everything is done through neural network training on data asets.  
译文：一切都是通过神经网络在数据集上的训练来完成的。  

**01:02:16 - 01:02:22**  
原文：And so because of that, we are going to be implicitly programming the assistant by creating data sets of conversations.  
译文：因此，我们将通过创建对话数据集 来隐式地编程助手。  

**01:02:22 - 01:02:31**  
原文：So these are three independent examples of conversations in a data set, an actual data set, and I'm going to show you examples will be much larger.  
译文：所以这些是数据集中三个独立的对话示例， 实际的数据集，我会给你看更多的例子，它们会更大。  

**01:02:31 - 01:02:39**  
原文：It could have hundreds of thousands of conversations that are multiti turned very long, etc., and would cover a diverse breadth of topics.  
译文：它可能有成千上万的对话，这些对话都是多回合的、非常长的等等，并且会涵盖广泛的主题。  

**01:02:39 - 01:02:41**  
原文：But here I'm only showing three examples.  
译文：但在这里我只展示了三个例子。  

**01:02:41 - 01:02:45**  
原文：But the way this works, basically is assistant is being programmed by example.  
译文：但这种方式的基本原理是，助理是通过示例进行编程的。  

**01:02:45 - 01:02:47**  
原文：And where is this data coming from?  
译文：这些数据是从哪里来的？  

**01:02:47 - 01:02:50**  
原文：Like two times euticals four, same as two plus two, etc..  
译文：像两次四一样，等于四，同于二加二，等等。。  

**01:02:50 - 01:02:51**  
原文：Where does that come from?  
译文：那来自哪里？  

**01:02:51 - 01:02:52**  
原文：This comes from human labelers.  
译文：这来自于人工标注者。  

**01:02:52 - 01:03:03**  
原文：So we will basically give human labelers some conversational context, and we will ask them to basically give the ideal assistant response in this situation.  
译文：所以我们将基本上给人类标注者一些对话背景，我们将要求他们在这情况下给出理想的助手回应。  

**01:03:03 - 01:03:08**  
原文：And a human will write out the ideal response for an assistant in any situation.  
译文：并且在任何情况下，一个人会写出理想的助手回应。  

**01:03:08 - 01:03:14**  
原文：And then we're going to get the model to basically train on this and to imitate those kinds of responses.  
译文：然后我们将让模型基于此进行训练， 并模仿这类响应。  

**01:03:14 - 01:03:20**  
原文：So the way this works then is we are going to take our base model, which we produced in the pretraining stage.  
译文：所以，这个过程的工作方式是，我们将采用我们在预训练阶段生成的基础模型。  

**01:03:20 - 01:03:23**  
原文：And this base model was trained on Internet documents.  
译文：此基础模型是在互联网文档上训练的。  

**01:03:23 - 01:03:32**  
原文：We're now going to take that data set of Internet documents, and we're going to throw it out, and we're going to substitute a new data set, and that's going to be a data set of conversations.  
译文：我们现在要处理这个互联网文档的数据集， 我们将把它丢弃， 然后代之以一个新的数据集， 这个新的数据集将是对话的集合。  

**01:03:32 - 01:03:37**  
原文：And we're going to continue training the model on these conversations, on this new de data set of conversations.  
译文：并且我们将继续在这些对话上训练模型，在这个新的对话数据集上进行训练。  

**01:03:37 - 01:03:40**  
原文：And what happens is that the model will very rapidly adjust.  
译文：而且模型会迅速调整。  

**01:03:40 - 01:03:47**  
原文：And we'll sort of like learn the statistics of how this assistant responds to human queries.  
译文：我们将学习这个助手如何响应人类查询的统计特性。  

**01:03:47 - 01:03:53**  
原文：And then later, during inference, we'll be able to basically prime the assistant and get the response.  
译文：然后在之后的推理过程中，我们基本上可以预处理助手并获得响应。  

**01:03:53 - 01:03:59**  
原文：And it will be imitating what the human labelers would do in that situation, if that makes sense.  
译文：它将会模仿人类标注者在那种情况下会做什么，如果这说得通的话。  

**01:03:59 - 01:04:04**  
原文：So we're going to see examples of that, and this is going to become a bit more concrete.  
译文：所以我们将看到这样的例子，这将变得更加具体。  

**01:04:04 - 01:04:16**  
原文：I also wanted to mention that this post training stage, we're going to basically just continue training the model, but the pretraining stage can, in practice, take roughly three months of training on many thousands of computers.  
译文：我还想提到，这个-post training阶段，我们基本上会继续训练模型，但是预训练阶段实际上可能需要大约三个月的时间，在许多数千台计算机上进行训练。  

**01:04:16 - 01:04:20**  
原文：The post training stage will typically be much shorter, like three hours, for example.  
译文：培训后的阶段通常会短得多，例如三个小时。  

**01:04:20 - 01:04:28**  
原文：And that's because the data set of conversations that we're going to create here manually is much more smaller than the data set of text on the Internet.  
译文：这是因为我们将要手动创建的对话数据集 比互联网上的文本数据集小得多。  

**01:04:28 - 01:04:30**  
原文：And so this training will be very short.  
译文：所以这次培训将会非常简短。  

**01:04:30 - 01:04:33**  
原文：But fundamentally, we're just going to take our base model.  
译文：但从根本上说，我们只是要用我们的基础模型。  

**01:04:33 - 01:04:41**  
原文：We're going to continue training using the exact same algorithm, the exact same everything, except we're swapping out the data aset for conversations.  
译文：我们将继续使用完全相同的算法进行训练，所有东西都完全相同，只是我们将数据集替换为对话数据。  

**01:04:41 - 01:04:44**  
原文：So the questions now are, where are these conversations?  
译文：所以现在的问题是，这些对话在哪里？  

**01:04:44 - 01:04:45**  
原文：How do we represent them?  
译文：我们如何表示它们？  

**01:04:45 - 01:04:49**  
原文：How do we get the model to see conversations instead of just raw text?  
译文：我们如何让模型看到对话而不是仅仅看到原始文本？  

**01:04:49 - 01:04:53**  
原文：And then what are the outcomes of this kind of training?  
译文：那么这种训练的结果是什么呢？  

**01:04:53 - 01:04:57**  
原文：And what do you get in a certain like psychological sense when we talk about the model?  
译文：那么当我们谈论这个模型时，从某种心理意义上来说，你会得到什么呢？  

**01:04:57 - 01:05:00**  
原文：So let's turn to those questions now.  
译文：那么现在让我们来谈谈这些问题。  

**01:05:00 - 01:05:03**  
原文：So let's start by talking about the tokenization of conversations.  
译文：那么让我们先来谈谈对话的代币化。  

**01:05:03 - 01:05:09**  
原文：Everything in these models has to be turned into tokens because everything is just about token sequences.  
译文：这些模型中的所有内容都必须转换成令牌，因为所有内容都只是关于令牌序列。  

**01:05:09 - 01:05:13**  
原文：So how do we turn conversations into token sequences?  
译文：那么我们如何将对话转换为令牌序列呢？  

**01:05:13 - 01:05:13**  
原文：Is the question.  
译文：问题是。  

**01:05:13 - 01:05:17**  
原文：And so for that, we need to design some kind of ending coding.  
译文：因此，我们需要设计某种结尾编码。  

**01:05:17 - 01:05:24**  
原文：And this is kind of similar to maybe if you're familiar, you don't have to be with, for example, a dcp ip packet in on the Internet.  
译文：这有点类似于，也许你熟悉，你不必一定是，例如，在互联网上的 dcp ip 数据包。  

**01:05:24 - 01:05:35**  
原文：There are precise rules and protocols for how you represent information, how everything is structured together so that you have all this kind of data laid out in a way that is written out on a paper and that everyone can agree on.  
译文：有关信息的表示方式，结构组成，都有精确的规则和协议，使得所有这些数据都能像写在纸上一样清晰地排列出来，并且 everyone 可以达成一致。 

注意：这里的“everyone”根据上下文可能指特定范围内的所有人，在翻译中可以直接保留为“everyone”或根据具体语境翻译为“所有人都”。如果你希望更自然的表达，可以考虑替换成“各方都能”或者“大家都能”。  

**01:05:35 - 01:05:37**  
原文：And so it's the same thing now happening in llms.  
译文：现在在大型语言模型中也发生了同样的事情。  

**01:05:37 - 01:05:46**  
原文：We need some kind of data structures, and we need to have some rules around how these data structures, like conversations, get encoded and decoded to and from tokens.  
译文：我们需要某种数据结构，並且我们需要有一些規則來規定這些數據結構，比如對話，如何被編碼和解碼成令牌。  

**01:05:46 - 01:05:53**  
原文：And so I want to show you now how I would recreate this conversation in the token space.  
译文：现在我想向您展示我将如何在 token 空间中重现这段对话。  

**01:05:53 - 01:05:57**  
原文：So if you go to tick tokenizer, I can take that conversation.  
译文：所以如果你去 tick tokenizer，我可以接替那场对话。  

**01:05:57 - 01:06:01**  
原文：And this is how it is represented in fourth, the language model.  
译文：这就是它在第四代语言模型中的表示方式。  

**01:06:01 - 01:06:06**  
原文：So here we have, we are iterating a user and an assistant in this two turn conversation.  
译文：所以在这里，我们正在进行一个用户和一个助手在这两次轮对话中的迭代。  

**01:06:06 - 01:06:11**  
原文：And what you're seeing here is it looks ugly, but it's actually relatively simple.  
译文：你在这里看到的，虽然看起来很丑，但实际上相对简单。  

**01:06:11 - 01:06:16**  
原文：The way it gets turned into a token sequence here at the end is a little bit complicated.  
译文：它在最后被转换成令牌序列的方式有点复杂。  

**01:06:16 - 01:06:26**  
原文：But at the end, this conversation between the user and assistant enup being 49 tokens, it is a one dimensional sequence of 49 tokens.  
译文：但最终，这段用户与助手之间的对话变成了49个标记，它是一个一维的49个标记的序列。  

**01:06:26 - 01:06:28**  
原文：And these are the tokens.  
译文：这些是代币。  

（注：根据上下文，“tokens”也可以翻译为“令牌”或“标志”。如果您有特定的上下文或者偏好，请告知我以便更准确地翻译。）  

**01:06:28 - 01:06:33**  
原文：And all the different llms will have a slightly different format or protocols.  
译文：所有不同的语言模型将具有略有不同的格式或协议。  

**01:06:33 - 01:06:36**  
原文：And it's a little bit of a Wild West right now.  
译文：而现在它有点像狂野的西部。  

**01:06:36 - 01:06:39**  
原文：But for example, GPT -4 does it in the following way.  
译文：但例如，GPT-4 是以以下方式完成的。  

**01:06:39 - 01:06:42**  
原文：You have this special token called I am underscore start.  
译文：你有一个叫做“I am underscore start”的特殊令牌。  

**01:06:42 - 01:06:46**  
原文：And this is short for emerimaginary monologue, the start.  
译文：这是emerimaginary独白的开头。  

**01:06:46 - 01:06:51**  
原文：Then you have to specify I don't actually know why it's called that to be honest.  
译文：然后你得说明，说实话我其实不知道为什么它被称为那样。  

**01:06:51 - 01:06:54**  
原文：Then you have to specify whose stern it is.  
译文：然后你必须说明这是谁的 stern。  

（注：此处的“stern”通常指船的尾部，如果上下文与此相关，建议根据具体情境调整翻译。如果是指人的“严厉”或“严格”，可能需要进一步澄清。）  

**01:06:54 - 01:07:02**  
原文：So for example, user, which is a token one, four, two, eight, then you have internal monologue separator and then it's the exact question.  
译文：所以，例如，用户，这是一个令牌一、四、二、八，然后你有内部独白分隔符，接着是确切的问题。  

**01:07:02 - 01:07:06**  
原文：So the tokens of the question and then you have to close it.  
译文：所以问题的令牌然后你必须关闭它。  

**01:07:06 - 01:07:10**  
原文：So I am end the end of the measuring monologue.  
译文：所以我在测量独白的结尾。  

（注意：原句可能存在语法错误，正确表达应为“So I am at the end of the measuring monologue.”，即“所以我在测量独白的结尾。”）  

**01:07:10 - 01:07:18**  
原文：So basically the question from a user of what is two plus two ends up being the token sequence of these tokens.  
译文：所以基本上，用户提出的“二加二等于多少”的问题最终变成了这些标记的标记序列。  

**01:07:18 - 01:07:22**  
原文：And now the important thing to mention here is that I am start.  
译文：现在这里要提到的重要事情是，我开始了。  

**01:07:22 - 01:07:24**  
原文：This is not text, right?  
译文：这不是文本，对吧？  

**01:07:24 - 01:07:27**  
原文：I am start is a special token that gets added.  
译文：我是开始是一个特殊的标记，它会被添加。 

注意：根据上下文，这句话的中文翻译可能需要调整以确保其意义准确传达。原始文本似乎包含了一个语法错误或非标准表达（"I am start is a special token..."）。如果你能提供更多上下文或澄清，我将能够提供更准确的翻译。  

**01:07:27 - 01:07:28**  
原文：It's a new token.  
译文：它是一个新代币。  

**01:07:28 - 01:07:31**  
原文：And this token has never been trained on so far.  
译文：而且这个令牌至今尚未接受过任何训练。  

**01:07:31 - 01:07:36**  
原文：It is a new token that we create in a post training stage and we introduce.  
译文：这是我们在训练后阶段创建并引入的一个新令牌。  

**01:07:36 - 01:07:52**  
原文：And so these special tokens, like I staretcetera, are introduced and interspersed with text so that they sort of get the model to learn that, Hey, this is the start of a term for who is at the start of the term for the start of the term is for the user.  
译文：因此，引入了这些特殊的标记，比如 I staretcetera，并将它们穿插在文本中，以便让模型学习到，嘿，这是术语的开始，而术语的开始是指用户的开始。  

（注：原文中有重复和不太通顺的地方，翻译时尽量保持了原意和格式。如果需要更通顺的表达，请告知。）  

**01:07:52 - 01:07:54**  
原文：And then this is what the user says.  
译文：然后这是用户所说的话。  

**01:07:54 - 01:08:00**  
原文：And then the user ends, and then it's a new start of a turn, and it is by the assistant.  
译文：然后用户结束，接着是一个新的轮次的开始，且这次是由助手进行。  

**01:08:00 - 01:08:02**  
原文：And then what does the assistant say?  
译文：然后助手会说什么？  

**01:08:02 - 01:08:05**  
原文：Well, these are the tokens of what the assistant says, etc..  
译文：好吧，这些都是助手所说的标记等。。  

**01:08:05 - 01:08:09**  
原文：And so this conversation is now turned into this sequence of tokens.  
译文：因此，这段对话现在变成了这一系列的标记。  

**01:08:09 - 01:08:12**  
原文：The specific details here are not actually that important.  
译文：这里的具体细节实际上并不是那么重要。  

**01:08:12 - 01:08:24**  
原文：All I'm trying to show you in concrete terms is that our conversations, which we think of as kind of like a structured object, end up being turned via sum encoding into one dimensional sequences of tokens.  
译文：我试图用具体的例子向你展示的是，我们认为像是结构化对象的对话，最终通过求和编码转换为一维的标记序列。  

**01:08:24 - 01:08:29**  
原文：And so because this is one dimensional sequence of tokens, we can apply all this stuff that we applied before.  
译文：因此，因为这是一个一维的令牌序列，我们可以应用之前使用的所有方法。  

**01:08:29 - 01:08:35**  
原文：Now there's just a sequence of tokens, and now we can train a language model on it.  
译文：现在只有一系列的标记，我们现在可以在其上训练一个语言模型。  

**01:08:35 - 01:08:42**  
原文：And so we're just predicting the next token in a sequence, just like before, and we can represent and train on conversations.  
译文：我们只是像之前一样预测序列中的下一个标记， 并且我们可以表示和训练对话。  

**01:08:42 - 01:08:45**  
原文：And then what does it look like at test time during inference?  
译文：那么在推理测试时它看起来像什么呢？  

**01:08:45 - 01:08:53**  
原文：So say we've trained a model, and we've trained a model on these kinds of data sets of conversations, and now we want to inference.  
译文：所以假设我们已经训练了一个模型，而且是用这类对话数据集进行训练的，现在我们想要进行推理。  

**01:08:53 - 01:08:57**  
原文：So during inference, what does this look like when you're on chashept t?  
译文：所以在推理过程中，当你在 chashept t 上时，这看起来像什么呢？  

**01:08:57 - 01:09:01**  
原文：Well, you come to chat appt and you have say like a dialogue with it.  
译文：好吧，你来和聊天应用进行对话，你就可以像这样与它交谈。  

**01:09:01 - 01:09:06**  
原文：And the way this works is basically say that this was already filled in.  
译文：这个的工作方式基本上是说这已经填好了。  

**01:09:06 - 01:09:08**  
原文：So like what is two plus two?  
译文：所以，二加二等于多少？  

**01:09:08 - 01:09:09**  
原文：Two plus two is four.  
译文：二加二等于四。  

**01:09:09 - 01:09:12**  
原文：And now you issue, what if it was times imam end?  
译文：而现在你发布，如果是伊玛目结束的时候呢？  

请注意，这句话在原文中似乎有一些语法或用词不太规范的地方，因此翻译时也尽量保持了原意。如果你有更具体的上下文或者需要调整措辞，请告知。  

**01:09:12 - 01:09:22**  
原文：And what basically ends up happening on the servers of OpenAI or something like that is they put an imstart assistant, imsep, and this is where they end it right here.  
译文：在OpenAI的服务器上，或者类似的地方，他们基本上会在服务器上放置一个imstart assistant，然后是imsep，这就是他们在这里结束的地方。  

**01:09:22 - 01:09:27**  
原文：So they construct this context, and now they start sampling from the model.  
译文：所以他们构建了这个上下文，现在他们开始从模型中采样。  

**01:09:27 - 01:09:32**  
原文：So it's at this stage that they will go to the model and say, okay, what is a good first sequence?  
译文：所以他们在这个阶段会去模型那里说，好吧，什么是好的第一个序列？  

**01:09:32 - 01:09:34**  
原文：What is a good first token?  
译文：什么是好的第一个代币？  

**01:09:34 - 01:09:36**  
原文：What is a good second token?  
译文：什么是好的第二代币？  

**01:09:36 - 01:09:38**  
原文：What is a good third token?  
译文：什么是好的第三令牌？  

**01:09:38 - 01:09:52**  
原文：And this is where the lm takes over and creates a response, like, for example, response that looks something like this, but it doesn't have to be identical to this, but it will have the flavor of this if this kind of a conversation was in the data aset.  
译文：然后，语言模型会接管并生成一个回复，比如，像这样的回复，但它不必与此完全相同，如果这种类型的对话在数据集中出现过，它将会有类似的风格。  

**01:09:52 - 01:09:57**  
原文：So that's roughly how the protocol works, although the details of this protocol are not important.  
译文：所以这大致是该协议的工作方式，虽然这个协议的细节并不重要。  

**01:09:57 - 01:10:11**  
原文：So again, my goal is that just to show you that everything ends up being just a one mensional token sequence, so we can apply everything we've already seen, but we're now training on conversations and we're now basically generating conversations as well.  
译文：所以，再次重申，我的目标只是向您展示，最终所有的一切都只是一个一维的 token 序列，因此我们可以应用我们已经学过的所有方法，但现在我们是在对话上进行训练，并且我们现在基本上也在生成对话。  

**01:10:11 - 01:10:12**  
原文：Okay.  
译文：好的。  

**01:10:12 - 01:10:15**  
原文：So now I would like to turn to what these data sets look like in practice.  
译文：所以现在我想谈谈这些数据集在实际中是什么样子的。  

**01:10:15 - 01:10:22**  
原文：The first paper that I would like to show you and the first effort in this direction is this paper from OpenAI in 2022.  
译文：我想给你展示的第一篇论文，也是在这个方向上的第一次努力，是OpenAI在2022年的这篇论文。  

**01:10:22 - 01:10:26**  
原文：And this paper was called instruct GPT, or the technique that they developed.  
译文：并且这篇论文被称为 instruct GPT，或者他们开发的技术。  

**01:10:26 - 01:10:33**  
原文：And this was the first time that OpenAI has kind of talked about how you can take language models and fine tunthem on conversations.  
译文：这是OpenAI第一次谈到如何将语言模型进行对话微调。  

**01:10:33 - 01:10:38**  
原文：And so this paper has a number of details that I would like to take you through.  
译文：所以这篇文章有很多细节我想带你一一了解。  

**01:10:38 - 01:10:50**  
原文：So the first stop I would like to make is in section 3.4, where they talk about the human contractors that they hired, in this case, from Upwork or through scai, to construct these conversations.  
译文：所以我想停留的第一个地方是在3.4节，那里讨论了他们雇佣的人类合同工， 在这个案例中，是从Upwork或通过scai，来构建这些对话的。  

**01:10:50 - 01:10:56**  
原文：And so there are human labelers involved whose job it is professionally to create these conversations.  
译文：因此，有人类标注者参与，他们的工作是专业地创建这些对话。  

**01:10:56 - 01:11:02**  
原文：And these labelers are asked to come up with prompts, and then they are asked to also complete the ideal assiresponses.  
译文：这些标注者被要求提出提示，然后他们还被要求完成理想的响应。  

**01:11:02 - 01:11:06**  
原文：And so these are the kinds of problems that people came up with.  
译文：于是人们想出了这类问题。  

**01:11:06 - 01:11:08**  
原文：So these are human labelers.  
译文：所以这些都是人类标注员。  

**01:11:08 - 01:11:12**  
原文：So list five ideas for how to regain enthusiasm for my career.  
译文：所以列出五个重新燃起我对职业生涯热情的主意。  

**01:11:12 - 01:11:15**  
原文：What are the top ten science fiction books I should read next?  
译文：我接下来应该读的十大科幻书籍是什么？  

**01:11:15 - 01:11:18**  
原文：And there's many different types of kind of prompts here.  
译文：这里有很多种不同的提示类型。  

**01:11:18 - 01:11:21**  
原文：So translate this sentence from to Spanish, etcetera.  
译文：所以将这个句子翻译成西班牙语，等等。  

**01:11:21 - 01:11:24**  
原文：And so there's many things here that people came up with.  
译文：因此这里有很多东西是人们想出来的。  

**01:11:24 - 01:11:29**  
原文：They first come up with the prompt, and then they also answer that prompt, and they give the ideal assistant response.  
译文：他们首先提出问题，然后他们也回答那个问题，并给出理想的助手回应。  

**01:11:29 - 01:11:35**  
原文：Now how do they know what is the ideal assistant response that they should write for these prompts?  
译文：现在他们如何知道针对这些提示应该编写什么样的理想助手回复？  

**01:11:35 - 01:11:43**  
原文：So when we scroll down a little bit further, we see that here we have this excerpt of labeling instructions that are given to the human labelers.  
译文：所以当我们向下滚动一点，我们看到这里有关于给人工标注者提供的标注指令的节选。  

**01:11:43 - 01:11:51**  
原文：So the company that is developing the language model, like, for example, OpenAI, writes up labeling instructions for how the humans should create ideal responses.  
译文：因此，开发语言模型的公司，比如 OpenAI，会编写标注指南，说明人类应如何创建理想的响应。  

**01:11:51 - 01:12:01**  
原文：And so here, for example, as an excerpt of these kinds of labeling instructions on a high level, you're asking people to be helpful, truthful and harmless.  
译文：因此，这里举例来说，这是高层次标签指令的一部分内容，你要求人们要乐于助人、诚实守信且无害。  

**01:12:01 - 01:12:04**  
原文：And you can pause the video if youlike to see more here.  
译文：而且如果你想要在这里查看更多，你可以暂停视频。  

**01:12:04 - 01:12:14**  
原文：But on a high level, basically just just answer, try to be helpful, try to be truthful and don't answer questions that we don't want kind of the system to handle later in chat.  
译文：但总体来说，基本上就是回答问题时尽量提供帮助，尽量保持诚实，不要回答我们不希望系统在聊天中后期处理的问题。  

**01:12:14 - 01:12:18**  
原文：And so roughly speaking, the company comes up with the labeling instructions.  
译文：大致来说，公司制定了标签说明。  

**01:12:18 - 01:12:20**  
原文：Usually they are not this short.  
译文：通常它们不会这么短。  

**01:12:20 - 01:12:29**  
原文：Usually they are hundreds of pages and people have to study them professionally, and then they write out the ideal assistant responses following those labeling instructions.  
译文：通常它们有数百页，人们必须专业地研究它们，然后根据这些标注说明写出理想的助手回答。  

**01:12:29 - 01:12:33**  
原文：So this is a very human heavy process, as it was described in this paper.  
译文：所以这是一个非常依赖人力的过程，正如这篇论文所描述的那样。  

**01:12:33 - 01:12:43**  
原文：Now, the data set for int GPT was never actually released by OpenAI, but we do have some open source reproductions that were trying to follow this kind of a setup and collect their own data.  
译文：现在，OpenAI 实际上从未发布过用于训练 GPT 的数据集，但我们确实有一些开源的复制品，它们试图遵循这种设置并收集自己的数据。  

**01:12:43 - 01:12:49**  
原文：So one that I'm familiar with, for example, is the effort of open assistant from a while back.  
译文：例如，我熟悉的一个是早前的开放助理项目。  

**01:12:49 - 01:12:51**  
原文：And this is just one of, I think, many examples.  
译文：而且这只是一个例子，我认为还有很多。  

**01:12:51 - 01:12:53**  
原文：But I just want to show you an example.  
译文：但我只是想给你看一个例子。  

**01:12:53 - 01:13:02**  
原文：So here's so these are people on the Internet that were asked to basically create these conversations, similar to what opening I did with human labelers.  
译文：所以这里的人是在互联网上被要求创建这些对话的人，这与我之前与人类标注者所做的开场白类似。  

**01:13:02 - 01:13:05**  
原文：And so here's an entry of a person who came up with this brand.  
译文：所以这里有一条记录，是关于一个想出这个品牌的人。  

**01:13:05 - 01:13:11**  
原文：T, can you write a short introduction to the relevance of the term monup Sunny in economics?  
译文：T，你能写一段关于术语“monup Sunny”在经济学中相关性的简短介绍吗？  

**01:13:11 - 01:13:13**  
原文：Please use examples, etcetera.  
译文：请使用例子等。  

**01:13:13 - 01:13:18**  
原文：And then the same person or potentially a different person will write up the response.  
译文：然后同一个人或可能是不同的人会撰写回复。  

**01:13:18 - 01:13:21**  
原文：So here's the assistant response to this.  
译文：所以这里是对这个问题的助手回复。  

**01:13:21 - 01:13:26**  
原文：And so then the same person or different person will actually write out this ideal response.  
译文：然后同一个人或不同的人会真正写出这个理想的回答。  

**01:13:27 - 01:13:32**  
原文：And then this is an example of maybe how the conversation could continue.  
译文：然后，这是一个可能的对话继续方式的例子。  

**01:13:32 - 01:13:40**  
原文：Now explain it to a dog, and then you can try to come up with a slightly, a simpler explanation or something like that.  
译文：现在向一只狗解释它，然后你可以尝试提出一个稍微简单一点的解释，或者类似的东西。  

**01:13:40 - 01:13:44**  
原文：Now this then becomes the label, and we end up training on this.  
译文：现在这成为标签，最终我们在此基础上进行训练。  

**01:13:44 - 01:13:55**  
原文：So what happens during training is that, of course, we're not going to have a full coverage of all the possible questions that the model will encounter at destime during inference.  
译文：所以在训练过程中，当然，我们不可能完全覆盖模型在推理时可能遇到的所有问题。  

**01:13:55 - 01:14:02**  
原文：We can't possibly cover all the possible prompts that people are going to be asking in the future.  
译文：我们不可能涵盖人们将来会询问的所有可能的提示。  

**01:14:02 - 01:14:11**  
原文：But if we have like a data set of a few of these examples, then the model during training will start to take on this persona of this helpful, truthful, harmless assistant.  
译文：但如果我们有像这样的几个例子的数据集，那么模型在训练过程中将会开始具备这种乐于助人、诚实、无害的助手的人格。  

**01:14:11 - 01:14:13**  
原文：And it's all programmed by example.  
译文：而且所有这些都是通过示例编程的。  

**01:14:13 - 01:14:15**  
原文：And so these are all examples of behavior.  
译文：这些都是行为的例子。  

**01:14:15 - 01:14:28**  
原文：And if you have conversations of these example behaviors and you have enough of them, like 100000, and you train on it, the model sort of starts to understand the statistical pattern, and it kind of takes on this personality of this assistant.  
译文：并且，如果你有这些示例行为的对话，而且数量足够多，比如10万次，并且你用它们进行训练，模型开始理解统计模式，它就会逐渐形成这种助手的人格。  

**01:14:28 - 01:14:40**  
原文：Now it's possible that when you get the exact same question like this at test time, it's possible that the answer will be recited as exactly what was in the training set.  
译文：现在有可能当你在测试时得到完全相同的问题， 有可能答案将会被背诵得 和训练集中的内容一模一样。  

**01:14:40 - 01:14:46**  
原文：But more likely than that is that the model will kind of like do something of a similar vibe.  
译文：但更有可能的是，该模型会做一些类似的事情。  

**01:14:46 - 01:14:50**  
原文：And we'll understand that this is the kind of answer that you want.  
译文：我们将明白，这就是您想要的答案类型。  

**01:14:50 - 01:14:52**  
原文：So that's what we're doing.  
译文：所以这就是我们在做的。  

**01:14:52 - 01:14:54**  
原文：We're programming the system by example.  
译文：我们通过示例来编程这个系统。  

**01:14:54 - 01:15:04**  
原文：And the system adopts statistically this persona of this helpful, truthful, harmless assistant, which is kind of like reflected in the labeling instructions that the company creates.  
译文：而且系统在统计上采用了这种乐于助人、诚实、无害的助手的人格，这在公司创建的标签指令中有所体现。  

**01:15:04 - 01:15:10**  
原文：Now I want to show you that the state of the art has kind of advanced in the last two or three years since the int GPT paper.  
译文：现在我想向您展示，自从GPT论文发表以来的两三年里，这项技术已经取得了相当的进展。  

**01:15:10 - 01:15:16**  
原文：So in particular, it's not very common for humans to be doing all the heavy lifting just by themselves anymore.  
译文：所以特别是，人类独自承担所有繁重工作的现象已经不那么普遍了。  

**01:15:16 - 01:15:22**  
原文：And that's because we now have language models, and these language models are helping us create these data sets and conversations.  
译文：这是因为我们现在有了语言模型，而且这些语言模型正在帮助我们创建这些数据集和对话。  

**01:15:22 - 01:15:28**  
原文：So it is very rare that the people will like literally just write out the response from scratch.  
译文：所以人们几乎不会真的从头开始书写回答。  

**01:15:28 - 01:15:36**  
原文：It is a lot more likely that they will use an existing llm to basically like come up with an answer and then they will edit it or things like that.  
译文：他们更有可能使用现有的大型语言模型来基本生成一个答案，然后他们会对其进行编辑或类似的操作。  

**01:15:36 - 01:15:42**  
原文：So there's many different ways in which now llms have started to kind of permeate this post training stack.  
译文：所以现在有多种不同的方式，大型语言模型已经开始渗透到这个训练后堆栈中。  

**01:15:42 - 01:15:47**  
原文：And llms are basically used pervasively to help create these massive data sets of conversations.  
译文：并且大型语言模型基本上被广泛用于帮助创建这些庞大的对话数据集。  

**01:15:47 - 01:15:54**  
原文：So I don't want to show like ultra chat is one such example of like a more modern data set of conversations.  
译文：所以我不想展示像 UltraChat 这样的例子，它是一个更现代的对话数据集。  

**01:15:54 - 01:15:56**  
原文：It is to a very large extent synthetic.  
译文：在很大程度上，它是合成的。  

**01:15:56 - 01:15:59**  
原文：But I believe there's some human involvement.  
译文：但我相信有一些人为因素。  

**01:15:59 - 01:16:00**  
原文：I could be wrong with that.  
译文：我可能会在那件事上出错。  

**01:16:00 - 01:16:05**  
原文：Usually there will be a little bit of human, but there will be a huge amount of synthetic help.  
译文：通常会有一点人类参与，但会有大量的人工合成辅助。  

**01:16:05 - 01:16:09**  
原文：And this is all kind of like constructed in different ways.  
译文：而且这全部都以不同的方式构建而成。  

**01:16:09 - 01:16:13**  
原文：And ultra chat is just one example of many sdata sets that currently exist.  
译文：而且，Ultra Chat只是目前存在的一众多数据集中的一个例子。  

**01:16:13 - 01:16:18**  
原文：And the only thing I want to show you is that these data sets have now millions of conversations.  
译文：我唯一想给你展示的是， 这些数据集现在包含了数百万的对话。  

**01:16:18 - 01:16:28**  
原文：These conversations are mostly synthetic, but they're probably edited to some extent by humans, and they span a huge diversity of sort of areas and so on.  
译文：这些对话大多是合成的，但可能在某种程度上经过了人工编辑，它们涵盖了非常广泛的领域等等。  

**01:16:28 - 01:16:32**  
原文：So these are fairly extensive artifacts by now.  
译文：所以这些都算是相当广泛的遗留物了。  

**01:16:32 - 01:16:35**  
原文：And there are all these like smixtures, as they're called.  
译文：以及所有这些所谓的混合物。  

**01:16:35 - 01:16:45**  
原文：So you have a mixture of like lots of different types and sources, and it's partially synthetic, partially human, and it's kind of like gone in that direction since.  
译文：所以你有各种各样不同的类型和来源的混合，而且它是部分合成的，部分来自人类，从那时起，它就朝着这个方向发展了。  

**01:16:45 - 01:16:48**  
原文：But roughly speaking, we still have sat data asets.  
译文：但大致来说，我们仍然有卫星数据集。  

**01:16:48 - 01:16:50**  
原文：They're made up of conversations.  
译文：它们由对话组成。  

**01:16:50 - 01:16:53**  
原文：We're training on them just like we did before.  
译文：我们正在对他们进行训练，就像我们以前做的那样。  

**01:16:53 - 01:17:13**  
原文：And I guess like the last thing to note is that I want to dispel a little bit of the magic of talking to an AI like when you go to chat shept and you give it a question and then you hit enter, what is coming back is kind of like statistically aligned with what's happening in the training set.  
译文：我想最后要提到的一点是，我想破除一些与AI对话的神秘感，比如当你去聊天室，给它一个问题，然后你按下回车键，得到的回答在某种程度上是与训练集中的数据统计对齐的。  

**01:17:13 - 01:17:20**  
原文：And these training sets, I mean, they really just have a seed in humans following labeling instructions.  
译文：这些训练集，我的意思是，它们确实只是基于人类按照标注指令所打下的基础。  

**01:17:20 - 01:17:25**  
原文：So what are you actually talking to in chashept, or how should you think about it?  
译文：那么，你实际上在 chashept 中与什么对话，或者你应该怎么去思考它？  

**01:17:25 - 01:17:36**  
原文：Well, it's not coming from some magical AI, like roughly speaking, it's coming from something that is statistically imitating human labelers, which comes from labeling instructions written by these companies.  
译文：好吧，它并不是来自某种神奇的AI，可以说，它是来自统计上模仿人类标注者的某物，而这些标注指令是由这些公司编写的。  

**01:17:36 - 01:17:38**  
原文：And so you're kind of imitating this.  
译文：所以你在某种程度上是在模仿这个。  

**01:17:38 - 01:17:48**  
原文：You're kind of getting it's almost as if you're asking human labeler and imagine that the answer that is given to you from chat gbt is some kind of a simulation of a human labeler.  
译文：你有点明白了，几乎就像是你在询问一个人类标注员，并且想象一下，chat gbt 给你的回答是某种人类标注员的模拟。  

**01:17:48 - 01:17:55**  
原文：And it's kind of like asking, what would a human labeler say in this kind of a conversation?  
译文：这有点像是在问，在这种对话中，人类标注者会怎么说？  

**01:17:55 - 01:18:03**  
原文：And it's not just like this human labeler is not just like a random person from the Internet, because these companies actually hire experts.  
译文：而且这个人类标注员 不仅仅是从网上找的随便什么人， 因为这些公司实际上是雇佣专家。  

**01:18:03 - 01:18:13**  
原文：So for example, when you are asking questions about code and so on, the human labelers that would be involved in creation of these conversation datsets, they will be usually be educated expert people.  
译文：所以，例如，当你询问有关代码等问题时，参与创建这些对话数据集的人类标注者，通常会是有受过教育的专家。  

**01:18:13 - 01:18:18**  
原文：And you're kind of like asking a question of like a simulation of those people, if that makes sense.  
译文：你有点像是在向那些人的模拟版本提问，如果这样理解没错的话。  

**01:18:18 - 01:18:20**  
原文：So you're not talking to a magical AI.  
译文：所以你并不是在和一个神奇的AI交谈。  

**01:18:20 - 01:18:22**  
原文：You're talking to an average labeler.  
译文：您正在与一位普通的标注员交谈。  

**01:18:22 - 01:18:25**  
原文：This average labeler is probably fairly highly skilled.  
译文：这个平均标签员可能具有相当高的技能。  

**01:18:25 - 01:18:33**  
原文：You're talking to kind of like an instantaneous simulation of that kind of a person that would be hired in the construction of these data sets.  
译文：你正在与那种类似于会被雇用来 构建这些数据集的人的瞬时模拟体对话。  

**01:18:33 - 01:18:37**  
原文：So let me give you one more specific example before we move on.  
译文：那么在我们继续之前，让我再给你一个具体的例子。  

**01:18:37 - 01:18:50**  
原文：For example, when I go to ChatGPT t and I say, recommend the top five landmarks you see in Paris, and then I hit enter, Oh, okay, here we go.  
译文：例如，当我去 ChatGPT，然后我说，推荐你认为巴黎的前五名地标，然后我按下回车键，哦，好的，我们开始了。  

**01:18:50 - 01:18:50**  
原文：Okay?  
译文：好的？  

**01:18:50 - 01:18:53**  
原文：When I hit enter, what's coming out here?  
译文：当我按下回车键时，这里会显示什么？  

**01:18:53 - 01:18:55**  
原文：How do I think about it?  
译文：我该怎么思考它？  

**01:18:55 - 01:19:04**  
原文：Well, it's not some kind of a magical AI that has gone out and researched all landmarks and then ranked them using its infinite intelligence et cec.  
译文：好吧，它并不是一种神奇的AI，可以外出研究所有地标，然后使用其无限的智能对它们进行排名等。  

**01:19:04 - 01:19:09**  
原文：What I'm getting is a statistical simulation of a labeler that was hired by OpenAI.  
译文：我所得到的是OpenAI雇佣的一个标注者的统计模拟。  

**01:19:09 - 01:19:12**  
原文：You can think about it roughly in that way.  
译文：你可以大致这样考虑。  

**01:19:12 - 01:19:24**  
原文：And so if this specific question is in the post training data set somewhere to OpenAI, then I'm very likely to see and answer that is probably very, very similar to what that human labeler would have put down for those five landmarks.  
译文：因此，如果这个具体问题出现在 OpenAI 的训练后数据集中，那么我有很大可能给出一个答案，这个答案很可能与人工标注者为这五个地标所标注的内容非常、非常相似。  

**01:19:24 - 01:19:37**  
原文：How does the human labeler come up with this while they go off and they go on the Internet and they kind of do their own little research for 20 minutes and they just come up with a list right now as so if they come up with this list and this is in the data set.  
译文：人类标注者是如何得出这个结果的，当他们离开去上网，自己做一些简短的研究，大约20分钟，然后他们就列出了一个清单。如果他们列出了这个清单，并且这个清单就在数据集中。  

**01:19:37 - 01:19:43**  
原文：I'm probably very likely to see what they submitted as the correct answer from the assistant.  
译文：我很可能看到他们提交的答案被助手视为正确答案。  

**01:19:43 - 01:20:05**  
原文：Now if this specific query is not part of the post training data set, then what I'm getting here is a little bit more emergent because the model kind of understands the statistically, the kinds of landmarks that are in a strset are usually the prominent landmarks, the landmarks that people usually want to see, the kinds of landmarks that are usually very often talked about on the Internet.  
译文：现在，如果这个具体的查询不是训练数据集的一部分，那么我在这里得到的结果就稍微有点涌现性，因为模型在统计上理解了strset中通常包含的地标通常是显著的地标，是人们通常想要看的地标，也是互联网上经常被讨论的地标。  

**01:20:05 - 01:20:11**  
原文：And remember that the model already has a ton of knowledge from its pre training on the Internet.  
译文：并记住，该模型在其预训练过程中已经从互联网上获得了大量的知识。  

**01:20:11 - 01:20:18**  
原文：So it's probably seen a ton of conversations about Paris, about landmarks, about the kinds of things that people like to see.  
译文：所以它可能已经看到了大量关于巴黎的对话，关于地标，关于人们喜欢看的东西。  

**01:20:18 - 01:20:26**  
原文：And so it's the pre training knowledge that has been combined with the poststering data set that results in this kind of an imitation.  
译文：因此，是预训练知识与微调数据集相结合，导致了这种模仿现象的产生。  

**01:20:26 - 01:20:32**  
原文：So that's roughly how you can kind of think about what's happening behind the scenes here in this statistical sense.  
译文：所以，这就是你大致可以思考在这背后发生的事情的方式，从这个统计意义上来说。  

**01:20:32 - 01:20:32**  
原文：Okay.  
译文：好的。  

**01:20:32 - 01:20:43**  
原文：Now I want to turn to the topic of llm psychology, as I like to call it, which is where sort of the emergent cognitive effects of the training pipeline that we have for these models.  
译文：现在我想转向我称之为llm心理学的话题，这就是我们为这些模型训练管道所带来的新兴认知效应。  

**01:20:43 - 01:20:47**  
原文：So in particular, the first one I want to talk to is, of course, hallucinations.  
译文：所以，特别是，我第一个想谈论的，当然是幻觉。  

**01:20:47 - 01:20:51**  
原文：So you might be familiar with model holust nations.  
译文：所以你可能对模型holust国家有所了解。  

**01:20:51 - 01:20:55**  
原文：It's when llms make stuff up, they just totally fabricate information etc..  
译文：当llms编造东西时，它们会完全捏造信息等。。  

**01:20:55 - 01:20:57**  
原文：And it's a big problem with llm assistance.  
译文：而且这是大型语言模型辅助工具的一个大问题。  

**01:20:57 - 01:21:02**  
原文：It is a problem that existed to a large extent with early models for many years ago.  
译文：这是一个多年前早期型号在很大程度上就存在的问题。  

**01:21:02 - 01:21:09**  
原文：And I think the problem has gotten a bit better because there are some mitications that I'm going to go into in a second.  
译文：而且我认为问题已经有所好转，因为有一些缓解措施，我将在下一刻进行说明。  

**01:21:09 - 01:21:12**  
原文：For now, let's just try to understand where these loose nacome from.  
译文：目前，让我们先试着理解这些松散的nac来自哪里。  

（注：原文中的“nac”可能是拼写错误或特定术语，如果需要更准确的翻译，请确认该词的具体含义。）  

**01:21:12 - 01:21:18**  
原文：So here's a specific example of a few of three conversations that you might think you have in your training set.  
译文：所以这里有一个具体的例子，展示了训练集中可能存在的三段对话中的几段。  

**01:21:18 - 01:21:24**  
原文：And these are pretty reasonable conversations that you could imagine being in the train set.  
译文：这些对话相当合理，你可以想象它们会在训练集中出现。  

**01:21:24 - 01:21:26**  
原文：So like, for example, who is Tom Cruise?  
译文：所以，比如，汤姆·克鲁斯是谁？  

**01:21:26 - 01:21:31**  
原文：Well, Tom Cruise is a famous actor, American actor and producer, etc..  
译文：好吧，汤姆·克鲁斯是一位著名的演员，美国演员和制片人等。  

**01:21:31 - 01:21:32**  
原文：Who is John Barraso?  
译文：谁是约翰·巴拉索？  

**01:21:32 - 01:21:36**  
原文：This turns out to be, Hey, us Senator, for example, who is genghkhan?  
译文：这结果是，嘿，比如，我们参议员，谁是成吉思汗？  

**01:21:36 - 01:21:37**  
原文：While ghanghis Khan was blah, blah, blah.  
译文：While 成吉思汗在 blah, blah, blah。 

注：此处“blah, blah, blah”通常用于表示说话人认为不重要或不想重复的内容，在正式翻译中应根据上下文进行适当处理。  

**01:21:37 - 01:21:41**  
原文：And so this is what your conversations could look like at training time.  
译文：所以这就是你在训练时的对话可能看起来像这样。  

**01:21:41 - 01:21:58**  
原文：Now, the problem with this is that when the human is writing the correct answer for the assistant, in each one of these cases, the human either like knows who this person is, or they research them on the Internet, and then they come in and they write this response that kind of has this like confident tone of an answer.  
译文：现在，这个问题在于当人类在为助手编写正确答案时，在每种情况下，人类要么知道这个人是谁，或者他们在互联网上查找相关信息，然后他们以这种自信的语气写下答案。  

**01:21:58 - 01:22:08**  
原文：And what happens basically is that at test time, when you ask for someone who is, this is totally random name that I totally came up with, and I don't think this person exists as far as I know.  
译文：基本上会发生的是，在测试时，当你询问某人，这是一个完全随机的名字，是我随便想出来的，据我所知，我不认为这个人存在。  

**01:22:08 - 01:22:11**  
原文：I just tried to generate it randomly.  
译文：我刚刚尝试随机生成它。  

**01:22:11 - 01:22:42**  
原文：The problem is, when we ask chis Orson coats, the problem is that the assistant will not just tell you, Oh, I don't know, even if the assistant and the language model itself might know inside its features, inside its activations, inside of its brain, sort of, it might know that this person is like not someone that it's familiar with, even if some part of the network kind of knows that in some sense, the saying that, Oh, I don't know who this is, is not going to happen because the model statistically imitates as training set.  
译文：问题是，当我们询问关于 Orson coats 的信息时，问题在于助手不会简单地告诉你：“哦，我不知道”，即使助手和语言模型本身在其内部特征、在其激活机制、在其“大脑”中，可能知道这个人不是它熟悉的人。即使网络的某些部分在某种程度上知道这一点，但模型从统计上模仿训练集的特点，因此它不会说：“哦，我不知道这是谁。”  

**01:22:42 - 01:22:48**  
原文：In the training set, the questions of the form who is blah are confidently answered with the correct answer.  
译文：在训练集中，像“谁是blah”这样的问题都能自信地用正确答案回答。  

**01:22:48 - 01:22:53**  
原文：And so it's going to take on the style of the answer and it's going to do its best.  
译文：因此，它将采用答案的风格，並盡力而為。  

**01:22:53 - 01:23:04**  
原文：It's going to give you statistically the most likely guess, and it's just going to basically make stuff up because these models, again, we just talked about it, is they don't have access to the Internet.  
译文：它会根据统计给你最可能的猜测， 并且它基本上会编造内容， 因为这些模型，我们刚刚讨论过， 它们无法访问互联网。  

**01:23:04 - 01:23:06**  
原文：They're not doing research.  
译文：他们没有在做研究。  

**01:23:06 - 01:23:11**  
原文：These are statistical token tumblers, as I call them, is just trying to sample the next token in the sequence.  
译文：这些是统计令牌搅拌机，正如我所称的，只是试图抽取序列中的下一个令牌。  

**01:23:11 - 01:23:13**  
原文：And it's going to basically mix stuff up.  
译文：它基本上会把东西混合起来。  

**01:23:13 - 01:23:15**  
原文：So let's take a look at what this looks like.  
译文：那么让我们来看看这像什么。  

**01:23:15 - 01:23:25**  
原文：I have here what's called the inference playground from hugging face, and I am on purpose picking on a model called falcon seven b, which is an old model.  
译文：我这里有一个来自 Hugging Face 的所谓推理游乐场，我故意选择了一个名为 Falcon 7B 的模型，这是一个较旧的模型。  

**01:23:25 - 01:23:27**  
原文：This is a few years ago now.  
译文：这已经是几年前的事了。  

**01:23:27 - 01:23:28**  
原文：So it's an older model.  
译文：所以它是旧型号。  

**01:23:28 - 01:23:30**  
原文：So it suffers from hallunations.  
译文：所以它患有幻觉。  

**01:23:30 - 01:23:34**  
原文：And as I mentioned, this has improved over time recently.  
译文：如我之前所说，这个最近有所改善。  

**01:23:34 - 01:23:36**  
原文：But let's say, who is Orson Kovats?  
译文：但让我们说说，谁是奥森·科瓦茨？  

**01:23:36 - 01:23:38**  
原文：Let's ask falcon seven b strurun.  
译文：让我们问问猎鹰七号B斯特伦。  

**01:23:38 - 01:23:38**  
原文：Oh Yeah.  
译文：哦，是的。  

**01:23:38 - 01:23:43**  
原文：Orson covts is an American author in science fiction writer.  
译文：奥森·斯科特是一位美国科幻小说作家。  

**01:23:43 - 01:23:44**  
原文：Okay, totally false.  
译文：好的，完全错误。  

**01:23:44 - 01:23:45**  
原文：It's hallucination.  
译文：它是幻觉。  

**01:23:45 - 01:23:46**  
原文：Let's try again.  
译文：让我们再试一次。  

**01:23:46 - 01:23:48**  
原文：These are statistical systems, right?  
译文：这些是统计系统，对吗？  

**01:23:48 - 01:23:50**  
原文：So we can resample this time.  
译文：所以我们可以重新采样这一次。  

**01:23:50 - 01:23:55**  
原文：Orson covts is a fictional character from this 19 fifties tv show.  
译文：Orson covts是上世纪五十年代的一部电视连续剧中的虚构角色。  

**01:23:55 - 01:23:56**  
原文：It's total bright.  
译文：它是完全明亮的。  

**01:23:56 - 01:23:57**  
原文：Let's try again.  
译文：让我们再试一次。  

**01:23:57 - 01:24:00**  
原文：He's a former minor league baseball player.  
译文：他以前是一名小联盟棒球运动员。  

**01:24:00 - 01:24:00**  
原文：Okay.  
译文：好的。  

**01:24:00 - 01:24:07**  
原文：So it basically the model doesn't know and it's given us lots of different answers because it doesn't know.  
译文：所以基本上，模型并不知道，它给了我们很多不同的答案，因为它不知道。  

**01:24:07 - 01:24:10**  
原文：It's just kind of like sampling from these probabilities.  
译文：这就像从这些概率中进行采样。  

**01:24:10 - 01:24:14**  
原文：The model starts with the tokens, who is Orson cuvts assistant?  
译文：模型从以下标记开始：谁是Orson cuvts的助手？  

**01:24:14 - 01:24:29**  
原文：And then it comes in here and it's getting these probabilities, and it's just sampling from the probabilities, and it just like comes up with stuff, and the stuff is actually statistically consistent with the style of the answer in its training set, and it's just doing that.  
译文：然后它在这里获取这些概率， 并且只是从这些概率中进行采样， 它就会生成一些内容， 而这些内容实际上在统计上 与其训练集中的答案风格是一致的， 它就是这么做的。  

**01:24:29 - 01:24:34**  
原文：But you and I experience enced it as a made up factual knowledge.  
译文：但你和我体验到的是它作为编造的事实知识。  

（注：原句中似乎有拼写错误，“enced”应为“enced”可能是想表达“experienced”，在此根据上下文进行了调整。）  

**01:24:34 - 01:24:45**  
原文：But keep in mind that the model basically doesn't know and it's just imitating the format of the answer, and it's not going to go off and look it up because it's just imitating again, the answer.  
译文：但请记住，该模型基本上不知道，它只是在模仿答案的格式，而且它不会去查找，因为这只是再次模仿答案。  

**01:24:45 - 01:24:46**  
原文：So how can we mitigate this?  
译文：那么我们如何减轻这种情况呢？  

**01:24:46 - 01:24:51**  
原文：Because for example, when we go to ChatPPT and I say, who's is awesome cobalts?  
译文：因为例如，当我们去ChatPPT时，我说，谁是awesome cobalts？  

**01:24:51 - 01:24:56**  
原文：And I'm now asking the state state of the art model from AI, this model will tell you, okay.  
译文：我现在正在询问来自AI的最先进模型，这个模型会告诉你，好的。  

**01:24:56 - 01:25:07**  
原文：So this model actually is even smarter because you saw very briefly it said searching the web, we're going to cover this later.  
译文：所以这个模型实际上更聪明，因为你刚才 briefly 看到它说正在搜索网络，我们稍后会详细讨论这一点。 

（注：原文中的 "very briefly" 可能是指短暂地或快速地，根据上下文调整为 "briefly" 更符合中文表达习惯。）  

**01:25:07 - 01:25:10**  
原文：It's actually trying to do two lius.  
译文：它实际上是在尝试做两个“liu”。  

**01:25:10 - 01:25:17**  
原文：And I kind of just like came up with some kind of a story, but I want to just bruose.  
译文：我随便编了一个故事，但我只是想闲逛。 

注：原文中“bruose”可能是拼写错误，应为“browse”（浏览）或“bruise”（瘀伤），根据上下文推测，这里翻译为“闲逛”更符合语境。如果需要严格按照原文翻译，请告知。  

**01:25:17 - 01:25:19**  
原文：Orson kovaj did not use any tools.  
译文：Orson kovaj 没有使用任何工具。  

**01:25:19 - 01:25:21**  
原文：I don't want to do web search.  
译文：我不想进行网页搜索。  

**01:25:22 - 01:25:26**  
原文：There's a well known historical Republic figure ilnamed arson covts.  
译文：有一位广为人知的历史上的共和国人物名叫阿森·科茨。 

注意：原始文本中的 "ilnamed" 可能是拼写错误，我假设它应该是 "named"。另外，“Arsen Covts”这个名字可能是指某个特定的历史人物，但是根据现有的历史资料，这个名字并不常见或知名。请确认名字的正确性。  

**01:25:26 - 01:25:29**  
原文：So this model is not going to make up stuff.  
译文：所以这个模型不会编造东西。  

**01:25:29 - 01:25:31**  
原文：This model knows that it doesn't know.  
译文：这个模型知道它不知道。  

**01:25:31 - 01:25:34**  
原文：And it tells you that it doesn't appear to be a person that this model knows.  
译文：并且它告诉你，这看起来不像这个模型所认识的人。  

**01:25:34 - 01:25:41**  
原文：So somehow we sort of improve hallucinations, even though they clearly are an issue in older models.  
译文：所以，尽管在旧模型中明显存在幻觉问题，我们 somehow 在某种程度上改善了幻觉问题。  

**01:25:41 - 01:25:48**  
原文：And it makes totally sense why you would be getting these kinds of answers if this is what your training set looks like.  
译文：而且如果你的训练集是这样的
那么你得到这类答案完全是合理的  

**01:25:48 - 01:25:49**  
原文：So how do we fix this?  
译文：那么我们该如何解决这个问题呢？  

**01:25:49 - 01:25:59**  
原文：Okay, well, clearly we need some examples in our data set that where the correct answer for the assistant is that the model doesn't know about some particular fact.  
译文：好的，显然，我们的数据集中需要一些例子，其中助手的正确答案是模型不知道某些特定的事实。  

**01:25:59 - 01:26:05**  
原文：But we only need to have those answers be produced in the cases where the model actually doesn't know.  
译文：但我们只需要在模型实际上不知道的情况下， 让它产生那些答案。  

**01:26:05 - 01:26:09**  
原文：And so the question is, how do we know what the model knows or doesn't know?  
译文：所以问题就是，我们如何知道模型知道或不知道什么？  

**01:26:09 - 01:26:12**  
原文：Well, we can empirically probe the model to figure that out.  
译文：好吧，我们可以对模型进行实证研究以找出答案。  

**01:26:12 - 01:26:19**  
原文：So let's take a look at, for example, how meta dealt with hallucinations for the llama three series of models as an example.  
译文：那么让我们来看看，例如，Meta是如何处理LLaMA三系列模型的幻觉问题的。  

**01:26:19 - 01:26:23**  
原文：So in this paper that they published for meta, we can go into hallucinations.  
译文：所以在他们为meta发表的这篇论文中，我们可以探讨幻觉现象。  

**01:26:25 - 01:26:27**  
原文：Which they call here factuality.  
译文：他们在这里称之为事实性。  

**01:26:27 - 01:26:39**  
原文：And they describe the procedure by which they basically interrogate the model to figure out what it knows and doesn't know, to figure out sort of like the boundary of its knowledge.  
译文：他们描述了基本的程序，通过该程序来审问模型，以确定它知道什么和不知道什么，从而确定其知识的边界。  

**01:26:39 - 01:26:53**  
原文：And then they add examples to the training set where for the things where the model doesn't know them, the correct answer is that the model doesn't know them, which sounds like a very easy thing to do in principle, but this roughly fixes the issue.  
译文：然后他们将示例添加到训练集中，对于模型不了解的事物，正确的答案是模型确实不了解它们，这听起来在原则上是非常容易做到的，但这大致上解决了问题。  

**01:26:53 - 01:27:03**  
原文：And the reason that fixes the issue is because remember that the model might actually have a pretty good model of its self knowledge inside the network.  
译文：并且修正此问题的原因是，记住，该模型实际上可能在其网络中有一个相当不错的自我认知模型。  

**01:27:03 - 01:27:15**  
原文：So remember, we looked at the network and all these neurons inside the network, you might imagine that there's a neuron somewhere in the network that sort of like lights up for when the model is uncertain.  
译文：所以记住，我们查看了网络以及网络中的所有这些神经元，你可能会想象在网络的某个地方有一个神经元，当模型不确定时，它就会亮起。  

**01:27:15 - 01:27:23**  
原文：But the problem is that the activation of that neuron is not currently wired up to the model actually saying in words that it doesn't know.  
译文：但问题是，该神经元的激活目前并未连接到模型实际用语言表达它不知道这一点上。  

**01:27:23 - 01:27:35**  
原文：So even though the internals of the neural network know, because there's some neurons that represent that the model will not surface, that it will instead take its best guess so that it sounds confident, just like it's season a training set.  
译文：所以即使神经网络的内部知道，因为有一些神经元代表模型不会表面化，它反而会做出最佳猜测，使它听起来很有信心，就像它已经在训练集中经过了训练一样。 

注意：原文中“season a training set”可能是表述错误，通常应为“seasoned by a training set”，意为“通过训练集训练过的”。根据上下文，我对其进行了合理的翻译调整。  

**01:27:35 - 01:27:42**  
原文：So we need to basically interrogate the model and allow it to say, I don't know in the cases that it doesn't know.  
译文：所以我们需要从根本上审查这个模型，并允许它在不知道的情况下说，我不知道。  

**01:27:42 - 01:27:44**  
原文：So let me take you through what meta roughly does.  
译文：那么让我带你了解一下meta大致做些什么。  

**01:27:44 - 01:27:47**  
原文：So basically what they do is here I have an example.  
译文：所以他们基本上做的就是这里我有一个例子。  

**01:27:47 - 01:27:51**  
原文：Dominique kshak is the featured article today.  
译文：今天的文章特色是 Dominique kshak。  

**01:27:51 - 01:27:53**  
原文：So I just went there randomly.  
译文：所以我只是随机去了那里。  

**01:27:53 - 01:28:06**  
原文：And what they do is basically they take a random document in a training set and they take a paragraph, and then they use an lm to construct questions about that paragraph.  
译文：他们所做的基本上是从训练集中选取一个随机文档，然后选取一个段落，接着他们使用语言模型（lm）来构建关于该段落的问题。  

**01:28:06 - 01:28:09**  
原文：So for example, I did that with ChatGPT here.  
译文：所以例如，我在这里用ChatGPT做了这件事。  

**01:28:09 - 01:28:20**  
原文：So I said, here's a paragraph from this document, generate three specific factual questions based on this paragraph, and give me the questions and the answers.  
译文：所以我这样说，这是这份文件中的一段文字，根据这段文字生成三个具体的事实性问题，并给我这些问题和答案。  

**01:28:20 - 01:28:24**  
原文：And so the llms are already good enough to create and reframe this information.  
译文：而且，这些语言模型已经足够好，可以创建和重构这些信息。  

**01:28:24 - 01:28:30**  
原文：So if the information is in the context window of this alm, this actually works pretty well.  
译文：所以如果信息在这个alm的上下文窗口中，这实际上运作得相当不错。  

**01:28:30 - 01:28:32**  
原文：It doesn't have to rely on its memory.  
译文：它不需要依赖记忆。  

**01:28:32 - 01:28:34**  
原文：It's right there in the context window.  
译文：就在上下文窗口中。  

**01:28:34 - 01:28:39**  
原文：And so it can basically reframe that information with fairly high accuracy.  
译文：它基本上可以重新构建这些信息，并且具有相当高的准确性。  

**01:28:39 - 01:28:43**  
原文：So, for example, can generate questions for us, like for which team did he play?  
译文：所以，例如，可以为我们生成问题，比如他为哪个团队效力？  

**01:28:43 - 01:28:46**  
原文：Here's the answer, how many cups that t wet cetera.  
译文：这是答案，多少杯湿等。 

注：原文中“t wet cetera”似乎有拼写或语法错误，可能是想表达“etc.（等等）”或“teaspoons, tablespoons, cups, etc.（茶匙、汤匙、杯等）”。如果能提供更多上下文，可以更准确地翻译。  

**01:28:46 - 01:28:52**  
原文：And now what we have to do is we have some question and answers, and now we want to interrogate the model.  
译文：现在我们要做的是，我们有一些问题和答案，现在我们想要询问这个模型。  

**01:28:52 - 01:28:58**  
原文：So roughly speaking, what we'll do is we'll take our questions and we'll go to our model, which will be, say, lama in meta.  
译文：所以大致来说，我们的做法是将问题整理好，然后带到我们的模型中，比如说，在meta中的lama。  

**01:28:58 - 01:29:02**  
原文：But let's just interrogate Mistral seven b here as an example.  
译文：但让我们以七号b这里的米斯特拉为例进行审问。  

**01:29:02 - 01:29:03**  
原文：That's another model.  
译文：那是另一个模型。  

**01:29:03 - 01:29:07**  
原文：So does this model know about this answer?  
译文：那么，这个模型知道这个答案吗？  

**01:29:07 - 01:29:09**  
原文：Let's take a look.  
译文：让我们来看一下。  

**01:29:09 - 01:29:12**  
原文：So he played for buffalo sabers, right?  
译文：所以他为水牛城军刀队效力，对吗？  

**01:29:12 - 01:29:13**  
原文：So the model knows.  
译文：所以模型知道了。  

**01:29:13 - 01:29:22**  
原文：And the way that you can programmatically decide is basically, we're going to take this answer from the model and we're going to compare it to the correct answer.  
译文：你可以通过编程来决定的方法基本上是，我们将采用模型给出的答案并与正确答案进行比较。  

**01:29:22 - 01:29:26**  
原文：And again, the models are good enough to do this automatically.  
译文：再次说明，这些模型已经足够好，可以自动完成这项任务。  

**01:29:26 - 01:29:28**  
原文：So there's no humans involved here.  
译文：所以这里没有人类参与。  

**01:29:28 - 01:29:35**  
原文：We can take basically the answer from the model, and we can use another llm judge to check if that is correct according to this answer.  
译文：我们可以直接从模型中获取答案，并且可以使用另一个大型语言模型（LLM）判断该答案是否正确。  

**01:29:35 - 01:29:39**  
原文：And if it is correct, that means that the model probably knows.  
译文：如果这是正确的，那就意味着模型可能知道。  

**01:29:39 - 01:29:42**  
原文：So we're going to do is we're going to do this maybe a few times.  
译文：所以我们打算做的是，我们可能会这样做几次。  

**01:29:42 - 01:29:44**  
原文：So okay, knows ses buffalo savers.  
译文：所以，好的，他知道瑟斯水牛拯救者。  

请注意，原始文本中包含了一些不太常见的词语和拼写，可能会影响翻译的准确性。如果你能提供更多上下文或确认某些词语的正确性，我会更好地帮助你进行翻译。  

**01:29:44 - 01:29:47**  
原文：Let's drag in buffalo sabers.  
译文：让我们拖入水牛弯刀。  

**01:29:47 - 01:29:50**  
原文：Let's try one more time.  
译文：让我们再试一次。  

**01:29:51 - 01:29:58**  
原文：Buffalo svers, so we asked three times about this factual question, and the model seems to know.  
译文：水牛滑倒了，所以我们三次询问这个事实问题，模型似乎知道。 

注：原文中的 "Buffalo svers" 可能是拼写错误或特定语境下的用法，直译为“水牛滑倒了”。如果这不符合上下文，请提供更多信息以便更准确的翻译。  

**01:29:58 - 01:29:59**  
原文：So everything is great.  
译文：所以一切都很棒。  

**01:29:59 - 01:30:01**  
原文：Now let's try the second question.  
译文：现在让我们试试第二个问题。  

**01:30:01 - 01:30:03**  
原文：How many Stanley Cups did he win?  
译文：他赢得了几次斯坦利杯？  

**01:30:03 - 01:30:05**  
原文：And again, let's interrogate the model about that.  
译文：再次，让我们向模型询问关于那件事。  

**01:30:05 - 01:30:07**  
原文：And the correct answer is two.  
译文：而正确答案是二。  

**01:30:08 - 01:30:17**  
原文：So here the model claims that he won four times, which is not correct, right?  
译文：所以这里的模型声称他赢了四次，这是不对的，对吧？  

**01:30:17 - 01:30:19**  
原文：It doesn't match two.  
译文：它不符合两个。  

**01:30:19 - 01:30:22**  
原文：So the model doesn't know it's making stuff up.  
译文：所以模型并不知道自己在编造内容。  

**01:30:22 - 01:30:23**  
原文：Let's try again.  
译文：让我们再试一次。  

**01:30:25 - 01:30:31**  
原文：So here the model again is kind of like making stuff.  
译文：所以这里的模型再次类似于在制造东西。  

**01:30:31 - 01:30:34**  
原文：Awright, let's draagain here.  
译文：好的，让我们再在这里拖拽一下。  

**01:30:34 - 01:30:38**  
原文：It says he did not even did not win during his career.  
译文：文本中的句子有语法错误，我将根据上下文进行合理修正后翻译：

原始文本: It says he did not even did not win during his career.
修正后: It says he did not even win during his career.

翻译：它说他整个职业生涯甚至一次都没有赢过。  

**01:30:38 - 01:30:40**  
原文：So obviously, the model doesn't know.  
译文：所以很明显，模型并不知道。  

**01:30:40 - 01:30:50**  
原文：And the way we can programmatically tell again is we interrogate the model three times, and we compare its answers maybe three times, five times, whatever it is, to the correct answer.  
译文：我们可以通过编程再次确认的方法是，我们对模型进行三次询问，并将其回答与正确答案进行比较，也许是三次、五次或任何次数。  

**01:30:50 - 01:30:54**  
原文：And if the model doesn't know, then we know that the model doesn't know this question.  
译文：如果模型不知道，那么我们就知道模型并不知道这个问题。  

**01:30:54 - 01:31:00**  
原文：And then what we do is we take this question, we create a new conversation in the training set.  
译文：然后我们所做的就是，我们用这个问题，在训练集中创建一个新的对话。  

**01:31:00 - 01:31:04**  
原文：So we're going to add a new conversation training set.  
译文：所以我们打算添加一个新的对话训练集。  

**01:31:04 - 01:31:10**  
原文：And when the question is how many Stanley Cups did he win, the answer is, I'm sorry, I don't know or I don't remember.  
译文：当问题是他赢得了多少座斯坦利杯时，答案是，对不起，我不知道或我不记得了。  

**01:31:10 - 01:31:16**  
原文：And that's the correct answer for this question because we interrogated the model and we saw that that's the case.  
译文：这就是这个问题的正确答案，因为我们询问了模型并看到确实是这种情况。  

**01:31:16 - 01:31:29**  
原文：If you do this for many different types of questions, for many different types of documents, you are given the model an opportunity to, in its training set, refuse to say based on its knowledge.  
译文：如果你对许多不同类型的问答题，针对许多不同类型的文档都这样做，你就给了模型一个机会，在其训练集中，根据其知识拒绝回答。  

**01:31:29 - 01:31:43**  
原文：And if you just have a few examples of that in your training set, the model will know and has the opportunity to learn the association of this knowledge based refusal to this internal neuron somewhere in its network that we presume exists.  
译文：而且如果你的训练集中只有几个这样的例子，模型将有机会学习到这种基于知识拒绝的关联，并将其映射到网络中某个我们假设存在的内部神经元上。  

**01:31:43 - 01:31:46**  
原文：And empirically, this turns out to be probably the case.  
译文：而且从经验上看，这很可能就是事实。  

**01:31:46 - 01:31:58**  
原文：And it can learn that association that, Hey, when this neuron of uncertainty is high, then I actually don't know and I'm allowed to say that I'm sorry, but I don't think I remember this, etcetera.  
译文：并且它可以学习这种关联，嘿，当这个不确定性的神经元活性很高的时候，实际上我并不知道，而且我可以表示我不知道，比如说，对不起，我不认为我记得这个，等等。  

**01:31:58 - 01:32:04**  
原文：And if you have these examples in your training set, then this is a large mitigation for hallucination.  
译文：而且如果你的训练集中有这些例子，那么这将大大减轻幻觉现象。  

**01:32:04 - 01:32:09**  
原文：And that's roughly speaking why chachy pt is able to do stuff like this as well.  
译文：大致上来说，这就是为什么chachy pt也能够做这样的事情。  

**01:32:09 - 01:32:16**  
原文：So these are kinds of mitigations that people have implemented and that have improved the factuality issue over time.  
译文：所以这些都是人们已经实施的改进措施，这些措施随着时间的推移改善了事实性问题。  

**01:32:16 - 01:32:22**  
原文：Okay, so I've described mitigation number one for basically mitigating the hallucinations issue.  
译文：好的，所以我已经描述了第一个缓解措施，主要是为了缓解幻觉问题。  

**01:32:22 - 01:32:25**  
原文：Now we can actually do much better than that.  
译文：现在我们实际上可以做得比这好得多。  

**01:32:25 - 01:32:36**  
原文：It's instead of just saying that we don't know, we can introduce an additional mitigation number two to give the lm an opportunity to be factual and actually answer the question.  
译文：与其只是说我们不知道，我们可以引入额外的第二个缓解措施，给语言模型一个机会，使其能够基于事实回答问题。  

**01:32:36 - 01:32:37**  
原文：Now what do you and I do?  
译文：现在你和我该怎么办？  

**01:32:37 - 01:32:44**  
原文：If I was to ask you a factual question and you don't know, what would you do in order to answer the question?  
译文：如果我问你一个事实性的问题，而你不知道答案，你会怎么做来回答这个问题？  

**01:32:44 - 01:32:52**  
原文：Well, he could go off and do some search and use the Internet, and you could figure out the answer and then tell me what that answer is.  
译文：好吧，他可以去搜索并使用互联网，你可以找出答案然后告诉我那个答案是什么。  

**01:32:52 - 01:32:55**  
原文：And we can do the exact same thing with these models.  
译文：我们可以用这些模型做完全相同的事情。  

**01:32:55 - 01:33:00**  
原文：So think of the knowledge inside the neural network, inside its billions of parameters.  
译文：所以想想神经网络内部的知识，存在于其数十亿的参数之中。  

**01:33:00 - 01:33:09**  
原文：Think of that as kind of a vague recollection of the things that the model has seen during its training, during the pre training stage a long time ago.  
译文：将其视为对该模型在很久以前的预训练阶段期间所见过的事物的一种模糊回忆。  

**01:33:09 - 01:33:13**  
原文：So think of that knowledge in the parameters as something you read a month ago.  
译文：所以，把参数中的那部分知识想象成你一个月前读过的东西。  

**01:33:13 - 01:33:17**  
原文：And if you keep reading something, then you will remember it and the model remembers that.  
译文：而且如果你持续阅读某样东西，那么你就会记住它，模型也会记住这一点。  

**01:33:17 - 01:33:22**  
原文：But if it's something rare, then you probably don't have a really recollection of that information.  
译文：但如果那是一件罕见的事，那么你可能对那件事情没有很深刻的记忆。  

**01:33:22 - 01:33:24**  
原文：But what you and I do is we just go and look it up.  
译文：但你和我所做的就是直接去查一下。  

**01:33:24 - 01:33:33**  
原文：Now, when you go and look it up, what you're doing basically is like you're refreshing your working memory with information and then you're able to sort of like retrieve it, talk about it or etcetera.  
译文：现在，当你去查找时，你所做的基本上就像是用信息刷新你的工作记忆，然后你就可以检索它、谈论它等等。  

**01:33:33 - 01:33:39**  
原文：So we need some equivalent of allowing the model to refresh its memory or its recollection.  
译文：所以我们需要让模型能够刷新其记忆或回忆的某种等价物。  

**01:33:39 - 01:33:42**  
原文：And we can do that by introducing tools for the models.  
译文：我们可以通过引入模型的工具来做到这一点。  

**01:33:43 - 01:33:56**  
原文：So the way we are going to approach this is that instead of just saying, Hey, I'm sorry, I don't know, we can attempt to use tools so we can create a mechanism by which the language model can emit special tokens.  
译文：所以我们打算采取的方法是， 不仅仅是说，嘿，对不起，我不知道， 我们可以尝试使用一些工具， 以便创建一种机制， 使语言模型能够发出特殊的标记。  

**01:33:56 - 01:34:00**  
原文：And these are tokens that we're going to introduce new tokens.  
译文：这些是我们将要引入新代币的代币。  

（注：此句在语义上有些 unclear，可能是由于原始英文句子结构导致的。如果需要更准确的翻译，请提供更多的上下文信息。）  

如果需要调整语句使其更通顺，可以改为：
这些是我们即将引入的新代币。  

**01:34:00 - 01:34:08**  
原文：So for example, here I've introduced two tokens, and I've introduced a format or a protocol for how the model is allowed to use these tokens.  
译文：所以，例如，这里我引入了两个标记，并且引入了一种格式或协议，规定模型如何被允许使用这些标记。  

**01:34:08 - 01:34:19**  
原文：So for example, instead of answering the question when the model does not, instead of just saying, I don't know, sorry, the model has the option now to emitting the special token search start.  
译文：所以，例如，当模型无法回答问题时，而不是简单地说“我不知道，对不起”，模型现在可以选择发出特殊标记 search start。  

**01:34:19 - 01:34:26**  
原文：And this is the query that will go to like Bing dot com in a case of OpenAI or say goosearch or something like that.  
译文：这就是将要发送到像必应（Bing）这样的网站的查询，在 OpenAI 的情况下，或者说是谷歌搜索或其他类似的服务。  

**01:34:26 - 01:34:29**  
原文：So it will emit the query, and then I will emit search end.  
译文：所以它将发出查询，然后我将发出搜索结束。  

**01:34:29 - 01:34:44**  
原文：And then here what will happen is that the program that is sampling from the model that is running the inference, when it sees the special token search end, instead of sampling the next token in the sequence, it will actually pause generating from the model.  
译文：然后这里会发生的是，从模型中采样的、运行推理的程序，当它看到特殊的搜索结束标记时，不会继续采样序列中的下一个标记，而是会暂停从模型生成。  

**01:34:44 - 01:34:45**  
原文：It will go off.  
译文：它会响起来。  

**01:34:45 - 01:34:54**  
原文：It will open a session with Bing dot com, and it will paste the search query into Bing, and it will then get all the text that is retrieved.  
译文：它将与必应网站建立会话，然后将搜索查询粘贴到必应中，接着它会获取所有检索到的文本。  

**01:34:54 - 01:34:56**  
原文：And it will basically take that text.  
译文：它将基本上采用该文本。  

**01:34:56 - 01:35:01**  
原文：It will maybe be represented again with some other special tokers or something like that.  
译文：它可能会再次以一些其他特殊的标记或其他类似的东西来表示。  

**01:35:01 - 01:35:07**  
原文：And it will take that text and it will copy paste it here into what I try to like show with the brackets.  
译文：它会将那段文本复制粘贴到这里，就像我试图用括号显示的那样。  

**01:35:07 - 01:35:09**  
原文：So all that text kind of comes here.  
译文：所以所有那些文本都 kind of 出现在这里。  

注：这里的“kind of”是一种口语表达，意为“有点儿”或“大致”，根据上下文可以调整翻译以更符合中文表达习惯。如果需要更正式的翻译，可以将其替换为“大致”或“某种程度上”。  

**01:35:09 - 01:35:12**  
原文：And when the text comes here, it enters the context window.  
译文：当文本到这里时，它进入上下文窗口。  

**01:35:12 - 01:35:19**  
原文：So the model, so that text from the web search is now inside the context window that will feed into the neural network.  
译文：所以模型，网络搜索的文本现在已经在上下文窗口中，该上下文窗口将输入到神经网络中。  

**01:35:19 - 01:35:25**  
原文：And you should think of the context window as kind of like the working memory of the model.  
译文：你应该把上下文窗口视为模型的工作记忆。  

**01:35:25 - 01:35:32**  
原文：That data that is in the context window is directly accessible by the model, directly feeds into the neural network.  
译文：上下文窗口中的数据可以直接被模型访问，直接输入到神经网络中。  

**01:35:32 - 01:35:35**  
原文：So it's not anymore a vague recollection.  
译文：所以这不再是一个模糊的记忆。  

**01:35:35 - 01:35:40**  
原文：It's data that it has in the context window and is directly available to that model.  
译文：它是上下文窗口中直接可用的数据，该模型可以直接使用。  

**01:35:40 - 01:35:47**  
原文：So now when it's sampling new tokens here afterwards, it can reference very easily the data that has been copy pasted in there.  
译文：所以现在当它在这里之后采样新的令牌时，可以非常容易地引用已经复制粘贴到那里的数据。  

**01:35:47 - 01:35:50**  
原文：So that's roughly how these tools function.  
译文：所以这些工具大致上是这样运作的。  

**01:35:50 - 01:35:53**  
原文：And so web search is just one of the tools.  
译文：因此，网络搜索只是其中之一工具。  

**01:35:53 - 01:35:56**  
原文：We're going to look at some of the other tools in a bit.  
译文：我们待会儿会看看一些其他工具。  

**01:35:56 - 01:36:06**  
原文：But basically, you introduce new tokens, you introduce some schema by which the model can utilize these tokens and can call these special functions like web search functions.  
译文：但基本上，您引入了新的令牌，引入了一些模式，通过这些模式，模型可以利用这些令牌并调用这些特殊功能，比如网络搜索功能。  

**01:36:06 - 01:36:12**  
原文：And how do you teach the model how to correctly use these tools, like, say, web search, search start, search end, etcetera?  
译文：那么，你如何教模型正确使用这些工具，比如，像网络搜索、搜索开始、搜索结束等？  

**01:36:12 - 01:36:15**  
原文：Well, again, you do that through training sets.  
译文：好吧，同样地，你通过训练集来做到这一点。  

**01:36:15 - 01:36:23**  
原文：So we need now to have a bunch of data and a bunch of conversations that show the model by example, how to use web search.  
译文：所以我们现在需要有一大批数据和大量的对话，通过示例向模型展示如何使用网络搜索。  

**01:36:23 - 01:36:27**  
原文：So what are the settings where you are using the search, and what does that look like?  
译文：那么，你在使用搜索时的设置是什么呢，那看起来像什么呢？  

**01:36:27 - 01:36:32**  
原文：And here's by example, how you start a search and the search etc..  
译文：以下是一个例子，展示了如何开始搜索以及进行搜索等。  

**01:36:32 - 01:36:44**  
原文：And if you have a few thousand maybe examples of that in your training set, the model will actually do a pretty good job of understanding how this tool works, and it will know how to sort of structure its queries.  
译文：而且如果你的训练集中有几千个类似的例子，模型实际上可以很好地理解这个工具是如何工作的，它将知道如何构建其查询。  

**01:36:44 - 01:36:52**  
原文：And of course, because of the pre training data set and its understanding of the world, it actually kind of understands what a web search is.  
译文：当然，因为预训练数据集及其对世界的理解，它实际上某种程度上理解什么是网络搜索。  

**01:36:52 - 01:36:57**  
原文：And so it actually kind of has a pretty good native understanding of what kind of stuff is a good search query.  
译文：因此，它实际上对什么是好的搜索查询有相当不错的本土理解。  

**01:36:57 - 01:36:59**  
原文：And so it all kind of just like works.  
译文：就这样，一切就像这样运作起来。  

**01:36:59 - 01:37:07**  
原文：You just need a little bit of a few examples to show it, how to use this new tool, and then it can lean on it to retrieve information and put it in the context window.  
译文：你只需要几个例子来展示如何使用这个新工具，然后它就可以依赖这个工具来检索信息并将其放在上下文窗口中。  

**01:37:07 - 01:37:16**  
原文：And that's a Corvalent to you and I looking something up, because once it's in the context, it's in the working memory and it's very easy to manipulate and access.  
译文：这对您和我查找某些信息来说是相关的，因为一旦它处于上下文中，它就在工作记忆中，非常容易操作和访问。 

注：原文中的“Corvalent”可能为拼写错误或特定术语，在此翻译中视为描述相关性（relevant）的意思。如果“Corvalent”有特定含义，请提供更多信息以便准确翻译。  

**01:37:16 - 01:37:27**  
原文：So that's what we saw a few minutes ago when I was searching on ChatGPT for who is or son covats, the ChatGPT language model decided that this has come some kind of a rare individual or something like that.  
译文：所以，几分钟前当我通过ChatGPT搜索“谁是or son covats”时，我们看到了这样的结果：ChatGPT语言模型认定这是一个某种罕见的个体或类似的情况。  

**01:37:27 - 01:37:33**  
原文：And instead of giving me an answer from its memory, it decided that it will sample special token that is going to do web search.  
译文：而且它并没有从记忆中给我一个答案，而是决定采样一个特殊的令牌，这个令牌将会进行网络搜索。  

**01:37:33 - 01:37:38**  
原文：And we saw briefly something flash was like using the web tool or something like that.  
译文：我们简短地看到一些东西闪现，就像是使用了网页工具或类似的东西。  

**01:37:38 - 01:37:39**  
原文：So it briefly said that.  
译文：所以它简而言之地说了。  

**01:37:39 - 01:37:42**  
原文：And then we waited for like 2s, and then it generated this.  
译文：然后我们等待了大约2秒，接着它生成了这个。  

**01:37:42 - 01:37:48**  
原文：And you see how it's creating references here, and so it's citing sources.  
译文：你看到它是如何在这里创建引用的，因此它是在引用来源。  

**01:37:48 - 01:37:59**  
原文：So what happened here is it went off, it did web search, it found these sources and these urls, and the text of these web pages was all stuffed in between here.  
译文：所以这里发生的是，它触发了，进行了网页搜索，找到了这些来源和网址，以及这些网页的文字内容都被塞在了这里。  

**01:37:59 - 01:38:05**  
原文：And it's not shown here, but it's basically stuffed as text in between here.  
译文：虽然这里没有显示，但它基本上是以文本形式填充在这之间的。  

**01:38:05 - 01:38:16**  
原文：And now it sees that text, and now it kind of references it and says that, okay, it could be these people citations, it could be those people citation etc..  
译文：现在它看到了那段文本，然后它引用了这段文本并表示，好的，这些可能是相关的人名引用，那些也可能是人名引用等等。  

**01:38:16 - 01:38:18**  
原文：So that's what happened here.  
译文：所以这就是这里发生的事情。  

**01:38:18 - 01:38:24**  
原文：That's what and that's why when I said who is or some covts, I could also say, don't use any tools.  
译文：这就是为什么当我说到谁是或一些covts时，我也可以说到，不要使用任何工具。 

注意：原文中的“covts”可能是拼写错误或者特定缩写的使用，如果这是一个特定术语或有上下文，请提供更多信息以便更准确的翻译。  

**01:38:24 - 01:38:31**  
原文：And then that's enough to basically convince jacupete to not use tools and just use its memory and its recollection.  
译文：然后，这足以基本说服jacupete不使用工具，而只使用它的记忆和回忆。  

**01:38:31 - 01:38:38**  
原文：I also went off and I tried to ask this question of chagpt, so how many standing cups did dominichachek win?  
译文：我 также离开去尝试向chagpt提问，所以 dominichachek 究竟赢得了多少个立式杯？  

**01:38:38 - 01:38:45**  
原文：And cheshihipety actually decided that it knows the answer and it has the confidence to say that he won twice.  
译文：And cheshihipety 实际上决定它知道答案，并且它有信心说他赢了两次。  

**01:38:45 - 01:38:59**  
原文：And so it kind of just relied on its memory, because presumably it has enough of a kind of confidence in its weights and its parameters and activations that this is retrievable just for memory.  
译文：因此，它某种程度上只是依赖于它的记忆，因为可以假设它对其权重、参数和激活有足够的信心，认为这些信息只需从记忆中检索即可。  

**01:38:59 - 01:39:10**  
原文：But you can also, conversely, use web search to make sure, and then for the same query, it actually goes off and it searches, and then it finds a bunch of sources.  
译文：但你也可以反其道而行之，使用网络搜索来确认，然后对于相同的查询，它实际上会去搜索，然后再找到一堆资料来源。  

**01:39:10 - 01:39:16**  
原文：It finds all this, all of this stuff gets copy pasted in there, and then it tells us to, again, and sites.  
译文：它找到了所有这些内容，所有这些东西都被复制粘贴到这里，然后它再次告诉我们，并且列出了网站。  

**01:39:16 - 01:39:22**  
原文：And it actually says the Wikipedia article, which is the source of this information for us as well.  
译文：它实际上指的是维基百科文章，这同样也是我们这一信息的来源。  

**01:39:22 - 01:39:26**  
原文：So that's tools, web search, the model determines when to search.  
译文：所以，工具、网络搜索，模型决定何时进行搜索。  

**01:39:26 - 01:39:30**  
原文：And then that's kind of like how these tools work.  
译文：然后这些工具就是以类似的方式运作。  

**01:39:30 - 01:39:35**  
原文：And this is an additional kind of mitigation for hallucinations and facality.  
译文：这是对幻觉和面部识别的一种额外的缓解方法。  

**01:39:35 - 01:39:45**  
原文：So I want to stress one more time this very important sort of psychology point, knowledge in the parameters of the neural network is a vague recollection.  
译文：所以我想再强调一次这个非常重要的心理学观点，神经网络参数中的知识是一种模糊的记忆。  

**01:39:45 - 01:39:50**  
原文：The knowledge in the tokens that make up the context window is the working memory.  
译文：构成上下文窗口的标记中的知识是工作记忆。  

**01:39:50 - 01:39:54**  
原文：And it, roughly speaking, works kind of like it works for us in our brain.  
译文：大致来说 它的运作方式 和我们的大脑 somewhat 类似  

**01:39:54 - 01:40:01**  
原文：The stuff we remember is our parameters and the stuff that we just experienced like a few seconds or minutes ago and so on.  
译文：我们记住的东西是我们的参数，以及我们刚刚经历的事情，比如几秒或几分钟前的事情等等。  

**01:40:01 - 01:40:09**  
原文：You can imagine that being in our context window, and this context window is being built up as you have a conscious experience around you.  
译文：你可以想象这就在我们的上下文窗口中，而这个上下文窗口是在你周围有意识的体验中逐渐建立起来的。  

**01:40:09 - 01:40:14**  
原文：So this is a bunch of implications also for your use of l ums in practice.  
译文：所以这对你在实践中使用 l ums 也有一些 implications。  

（注：原文中的“l ums”和“implications”可能需要根据具体上下文进行调整，以确保准确翻译。如果“l ums”是特定术语或缩写，请提供更多信息以便更准确地翻译。）  

**01:40:14 - 01:40:16**  
原文：So for example, I can go to chat chipatand.  
译文：所以，例如，我可以去聊天 Chipatand。  

**01:40:16 - 01:40:18**  
原文：I can do something like this.  
译文：我可以做类似这样的事情。  

**01:40:18 - 01:40:21**  
原文：I can say, can you summarize chapter one of Jane Austens pride and prejudice?  
译文：我可以问，你能总结简·奥斯汀的《傲慢与偏见》第一章吗？  

**01:40:21 - 01:40:21**  
原文：Right?  
译文：对吧？  

**01:40:21 - 01:40:27**  
原文：And this is a perfectly fine prompt, and chachipatty actually does something relatively reasonable here.  
译文：而且这完全是一个合适的提示，chachipatty实际上在这里做了相对合理的事情。  

**01:40:27 - 01:40:33**  
原文：And but the reason is does that is because chashipti has a pretty good recollection of a famous work like pride and prejudice.  
译文：而且原因就是，这是因为查西普蒂对像《傲慢与偏见》这样的著名作品有相当好的回忆。 

注：原文中“chashipti”看起来像是拼写错误或特定名称，在此根据上下文推测为“查西普蒂”。如果这是一个特定的名称或术语，请确认其正确性。  

**01:40:33 - 01:40:35**  
原文：There's probably seen a ton of stuff about it.  
译文：可能已经看到很多关于它的内容了。  

**01:40:35 - 01:40:37**  
原文：There's probably forums about this book.  
译文：关于这本书可能有论坛。  

**01:40:37 - 01:40:39**  
原文：It's probably read versions of this book.  
译文：它可能读过这本书的各个版本。  

**01:40:39 - 01:40:46**  
原文：And it's kind of like remembers, because even if you've read this or articles about it, youkind of have a recollection enough to actually say all this.  
译文：而且它有点像是记忆，因为即使你读过这个或关于它的文章，你也有足够的回忆来说出所有这些。  

**01:40:46 - 01:40:54**  
原文：But usually when I actually interact with allims and I want them to recall specific things, it always works better if you just give it to them.  
译文：但通常当我实际与allims互动并希望他们回忆起具体的事情时，如果你直接告诉他们，效果总是更好。  

**01:40:54 - 01:40:57**  
原文：So I think a much better prompt would be something like this.  
译文：所以我认为一个更好的提示应该是这样的。  

**01:40:57 - 01:41:01**  
原文：Can you summarize for me chapter one of Jane auens Brian prejudice?  
译文：你能否为我总结一下《简·奥斯汀的理智与情感》第一章的内容？

注意：原文中书名似乎有误，应该是《Jane Austen's Pride and Prejudice》（《简·奥斯汀的傲慢与偏见》）。如果你指的是这本书，请确认。  

**01:41:01 - 01:41:04**  
原文：And then I am attaching it below for your reference.  
译文：然后我将其附在下方供您参考。  

**01:41:04 - 01:41:07**  
原文：And then I do something like the limiter here, and I paste it in.  
译文：然后我做类似这里限制器的操作，然后我把它粘贴进去。  

**01:41:07 - 01:41:11**  
原文：And I found that just copy pasting it from some web site that I found here.  
译文：我只是从我在这里找到的一个网站上复制粘贴的。  

**01:41:11 - 01:41:13**  
原文：So copy pasting the chapter one here.  
译文：所以在这里复制粘贴第一章。  

**01:41:13 - 01:41:23**  
原文：And I do that because when it's in the context window, the model has direct access to it and can exactly, it doesn't have to recall it, it just has direct access to it.  
译文：我这样做是因为当内容在上下文窗口中时，模型可以直接访问它，而且它可以精确地访问，不需要回忆，因为它有直接的访问权限。  

**01:41:23 - 01:41:33**  
原文：And so this summary is can be expected to be a significantly high quality or higher quality than this summary just because it's directly available to the model.  
译文：因此，可以预期这个摘要的质量会显著更高，或者比这个摘要的质量更高，因为它可以直接提供给模型。  

**01:41:33 - 01:41:36**  
原文：And I think you and I would work in the same way if you want to.  
译文：而且我认为如果你愿意的话，你和我会以相同的方式工作。  

**01:41:36 - 01:41:42**  
原文：You would produce a much better summary if you had re eread this chapter before you had to summarize it.  
译文：如果你在需要总结之前重新阅读了这一章，你会做出更好的总结。  

**01:41:42 - 01:41:46**  
原文：And that's basically what's happening here, or the equivalent of it.  
译文：这基本上就是这里发生的事情，或者说是它的等价情况。  

**01:41:46 - 01:41:51**  
原文：The next sort of psychological quirk I'd like to talk about briefly is that of the knowledge of self.  
译文：接下来，我想简要谈谈的 另一种心理奇特现象 是关于自我认知。  

**01:41:51 - 01:41:55**  
原文：So what I see very often on the Internet is that people do something like this.  
译文：所以我在互联网上经常看到的是人们会做类似这样的事情。  

**01:41:55 - 01:41:58**  
原文：They ask llms something like, what model are you and who built you?  
译文：他们问.llms，类似的问题有：你是哪个模型的，是谁建造了你？ 

注意：原文中的"llms"可能是指大型语言模型本身，在这里我将其保留为.llms以保持与原文一致。如果这是一个特定的名称或缩写，请根据实际情况进行调整。  

**01:41:58 - 01:42:02**  
原文：And basically, this question is a little bit nonsensical.  
译文：基本上，这个问题有点不合情理。  

**01:42:02 - 01:42:09**  
原文：And the reason I say that is that as I try to kind of explain with some of the underhood fundamentals, this thing is not a person, right?  
译文：我这么说的原因是，当我试图解释一些内部基本原理时，这东西并不是一个人，对吧？  

**01:42:09 - 01:42:12**  
原文：It doesn't have a persistent existence in any way.  
译文：它以任何方式都不存在持久的状态。  

**01:42:12 - 01:42:15**  
原文：It sort of boots up, processes tookens and shuts off.  
译文：它 sort of 启动，处理 token 并关闭。 

注：原文中的 "sort of" 是一种口语表达，意为“有点儿； somewhat”，"processes tookens" 可能是 "processes tokens" 的拼写错误，这里按照可能的意图进行了翻译。如果你需要更准确的翻译，请确认原文是否有误。  

**01:42:15 - 01:42:17**  
原文：And it does that for every single person.  
译文：而且它为每个人这样做。  

**01:42:17 - 01:42:21**  
原文：Just kind of built up a context window of conversation, and then everything gets deleted.  
译文：只是建立了一个对话的上下文窗口，然后所有内容都被删除了。  

**01:42:21 - 01:42:27**  
原文：And so this entity is kind of like restarted from scratch every single conversation, if that makes sense.  
译文：所以这个实体在每次对话中都会从头开始重新启动，如果这样理解没错的话。  

**01:42:27 - 01:42:30**  
原文：It has no persistent self as no sense of self.  
译文：它没有持久的自我，因为没有自我意识。  

**01:42:30 - 01:42:31**  
原文：It's a token tumbler.  
译文：它是一个代币搅拌机。  

**01:42:31 - 01:42:34**  
原文：And it fils statistical regularities of its training set.  
译文：并且它符合其训练集的统计规律。  

**01:42:34 - 01:42:39**  
原文：So it doesn't really make sense to ask it, who are you, what built to, etc..  
译文：所以，问它是谁，是干什么的等等，其实是没有意义的。  

**01:42:39 - 01:42:46**  
原文：And by default, if you do what I described, and just by default and from nowhere, you're going to get some pretty random answers.  
译文：而且，默认情况下，如果你按我描述的去做， 并且只是默认情况下，没有任何缘由， 你会得到一些相当随机的答案。  

**01:42:46 - 01:42:51**  
原文：So for example, let's pick on falcon, which is a fairly old model, and let's see what it tells us.  
译文：所以，例如，让我们以falcon为例，这是一个相当旧的模型，让我们看看它会告诉我们什么。  

**01:42:52 - 01:42:54**  
原文：So it's evading the question.  
译文：所以这是在回避问题。  

**01:42:54 - 01:42:56**  
原文：Talented engineers and developers here.  
译文：这里有才华横溢的工程师和开发者。  

**01:42:56 - 01:42:59**  
原文：It says, I was built by OpenAI based on a GPT -3 model.  
译文：它说，我是由OpenAI基于GPT-3模型构建的。  

**01:42:59 - 01:43:01**  
原文：It's totally making stuff up.  
译文：它完全是在编造。  

**01:43:01 - 01:43:10**  
原文：Now, the fact that it's built by OpenAI here, I think a lot of people would take this as evidence that this model was somehow trained on OpenAI data or something like that.  
译文：现在，由于它是OpenAI在这里构建的，我认为很多人会将其视为证据，认为这个模型是在OpenAI的数据上训练的，或者类似的情况。  

**01:43:10 - 01:43:26**  
原文：I don't actually think that that's necessarily the reason for that is that if you don't explicitly program the model to answer these kinds of questions, then what you're going to get is its statistical best guess at the answer.  
译文：我实际上并不认为那一定是原因，因为如果你没有明确地编程让模型回答这类问题，那么你所得到的将是它对答案的统计最佳猜测。  

**01:43:26 - 01:43:30**  
原文：And this model had a sft data mixture of conversations.  
译文：而且这个模型有一个混合了对话的SFT数据集。  

**01:43:30 - 01:43:40**  
原文：And during the fine tuning, the model sort of understands as it's training on this data that is taking on this personality of this like helpful assistant.  
译文：在微调过程中，模型在训练这部分数据时逐渐理解并呈现出这种乐于助人的助手的人格特质。  

**01:43:40 - 01:43:42**  
原文：And it doesn't know how to.  
译文：而且它不知道如何做。  

**01:43:42 - 01:43:47**  
原文：It doesn't actually, it wasn't told exactly what labbel to apply to self.  
译文：实际上，它并没有被明确告知要给自己贴上什么标签。  

**01:43:47 - 01:43:51**  
原文：It just kind of is taking out this persona of a helpful assistant.  
译文：它只是在某种程度上摒弃了这种乐于助人的助手形象。  

**01:43:51 - 01:44:00**  
原文：And remember that the pre training stage took the documents from the entire Internet, and chaty, pt and OpenAI are very prominent in these documents.  
译文：并记住，预训练阶段使用了来自整个互联网的文档，而在这些文档中，Chaty、PT和OpenAI都非常突出。  

**01:44:00 - 01:44:07**  
原文：And so I think what's actually likely to be happening here is that this is just its hallucinated label for what it is.  
译文：因此，我认为实际上可能发生的情况是，这只是它对所看到事物的幻觉标签。  

**01:44:07 - 01:44:10**  
原文：This is its self identity, is that it's chat upi, OpenAI.  
译文：这是它的自我身份，即它是聊天界面的OpenAI。  

**01:44:10 - 01:44:19**  
原文：And it's only saying that because there's a ton of data on the Internet of answers like this that are actually coming from OpenAI, from chashept.  
译文：它这么说只是因为互联网上有大量类似的答案数据，这些数据实际上来自OpenAI，来自chashept。  

**01:44:19 - 01:44:22**  
原文：And so that's its label for what it is.  
译文：所以这就是它的标签。  

**01:44:22 - 01:44:24**  
原文：Now you can override this as a developer.  
译文：现在你可以作为开发人员覆盖此设置。  

**01:44:24 - 01:44:27**  
原文：If you have an llm model, you can actually override it.  
译文：如果你有一个大型语言模型，你实际上可以覆盖它。  

**01:44:27 - 01:44:30**  
原文：And there are a few ways to do that.  
译文：有几种方法可以做到这一点。  

**01:44:30 - 01:44:35**  
原文：So for example, let me show you there's this alma model from Alan AI, and this is one llm.  
译文：所以，例如，让我给你展示一下，这是来自 Alan AI 的这个 alma 模型，这是一个大型语言模型（LLM）。  

**01:44:35 - 01:44:40**  
原文：It's not a top Tim or anything like that, but I like it because it's this fully open source.  
译文：它并不是顶级的 Tim 或者类似的东西，但我喜欢它，因为它是完全开源的。  

**01:44:40 - 01:44:46**  
原文：So the paper for ommo and everything else is completely, fully open source, which is nice.  
译文：所以Omomo的论文和所有其他东西完全是、完全开源的，这是很好的。  

**01:44:46 - 01:44:48**  
原文：So here we are looking at its sft mixture.  
译文：所以我们现在看到的是它的软膏混合物。  

**01:44:48 - 01:44:51**  
原文：So this is the data mixture of the fine tuning.  
译文：所以这就是微调的数据混合。  

**01:44:51 - 01:44:53**  
原文：So this is the conversations data set, right?  
译文：所以这就是对话数据集，对吧？  

**01:44:53 - 01:45:03**  
原文：And so the way that they are solving it for the alma model is we see that there's a bunch of stuff in the mixture and there's a total of 1 million conversations here.  
译文：因此，他们为alma模型解决这个问题的方式是，我们看到混合中有许多内容，而这里总共有100万次对话。  

**01:45:03 - 01:45:04**  
原文：But here we have alma two heart coded.  
译文：但这里我们有alma两个心脏编码。  

**01:45:04 - 01:45:09**  
原文：If we go there, we see that this is 240 conversations.  
译文：如果我们去那里，我们会看到这是240次对话。  

**01:45:09 - 01:45:13**  
原文：And look at these 240 conversations, they're hard coded.  
译文：看看这240个对话，它们是硬编码的。  

**01:45:13 - 01:45:22**  
原文：Telling me about yourself, says user, and then the assistant says, I'm Omand open a language model developed by AI two, Alan en Institute of artificial intelligence etc..  
译文：告诉我关于你自己，用户说，然后助手说，我是Omand，一个由AI2开发的语言模型，来自人工智能研究所等。 

注意：原文本中“Omand open a language model developed by AI two, Alan en Institute of artificial intelligence etc..”可能存在一些拼写或语法错误，正确的表达可能是：“I'm Omand, an open language model developed by AI2, the Allen Institute for Artificial Intelligence, etc.” 翻译时已做适当调整。  

**01:45:22 - 01:45:24**  
原文：I'm here to hell, blah, blah, blah.  
译文：我在这里去地狱，巴拉，巴拉，巴拉。 

注：此句中的“blah, blah, blah”通常用于表示说话人认为不重要或不愿重复的冗长言辞，翻译成中文时可根据上下文调整为合适的表达。  

**01:45:24 - 01:45:25**  
原文：What is your name?  
译文：什么是你的名字？  

**01:45:25 - 01:45:25**  
原文：The omma project.  
译文：The omma project. 

（注：由于文本非常简短且看起来像是一个专有名词或项目名称，因此在中文中通常会保持不变，不进行翻译。如果需要解释或有特定的中文名称，请提供更多信息。）  

**01:45:25 - 01:45:43**  
原文：These are all kinds of like cooked up hard coded questions about alma two and the correct answers to give in these cases, if you take 240 questions like this or conversations, put them into your training set and fine tune with it, then the model will actually be expected to parrot this stuff later.  
译文：这些都是关于ALMA Two的类似预先设定好的硬编码问题以及在这些情况下应该给出的正确答案。如果你将240个这样的问题或对话放入训练集中，并用它们进行微调，那么模型在之后实际上会被期望重复这些内容。  

**01:45:43 - 01:45:47**  
原文：If you don't give it this, then it's probably a chayou 50 biai.  
译文：如果你不给它这个，那么它可能是一个查油50偏爱。 

注：最后一句的翻译有些不清楚，因为“chayou 50 biai”不是标准的英文单词或短语，可能是拼写错误或者特定上下文中的术语。如果您能提供更多背景信息，我可以提供更准确的翻译。  

**01:45:47 - 01:46:03**  
原文：And there's one more way to sometimes do this is that basically in these conversations and you have turns between human and assistant, sometimes there's a special message called system message at the very beginning of the conversation.  
译文：还有一种方法有时可以这样做，基本上在这些对话中，你和助手之间有轮流发言，有时在对话的最开始有一个特殊的消息，叫做系统消息。  

**01:46:03 - 01:46:06**  
原文：So it's not just between human and assistant, there's a system.  
译文：所以这不仅仅是人与助手之间的互动，还有一个系统。  

**01:46:06 - 01:46:18**  
原文：And in the system message, you can actually harcode and remind the model that, Hey, you are a model developed by OpenAI, and your name is chashept four zero, and you are trained on the state and your knowledge cut off is this.  
译文：在系统消息中，你可以实际硬编码并提醒模型，嘿，你是OpenAI开发的模型，你的名字是chashept四零，你在特定状态上进行了训练，且你的知识截止日期是这个。  

**01:46:18 - 01:46:25**  
原文：And basically, it's kind of like documents the model a little bit, and then this is inserted into your conversations.  
译文：基本上，它有点像文档模型的一部分，然后这会被插入到你的对话中。  

**01:46:25 - 01:46:28**  
原文：So when you go on chayou pt, you see a blank page.  
译文：所以当你进入chayou pt时，你看到的是一个空白页面。  

**01:46:28 - 01:46:31**  
原文：But actually the system message is kind of like hidden in there.  
译文：但实际上，系统消息有点像是隐藏在其中。  

**01:46:31 - 01:46:33**  
原文：And those tokens are in the context window.  
译文：而且这些标记都在上下文窗口中。  

**01:46:33 - 01:46:38**  
原文：And so those are the two ways to kind of program the models to talk about themselves.  
译文：所以，这两种方式就是编程让模型自我讨论的方法。  

**01:46:38 - 01:46:43**  
原文：Either is done through data like this or is done through system message and things like that.  
译文：两者都是通过类似这样的数据完成的，或者是通过系统消息等方式完成的。  

**01:46:43 - 01:46:48**  
原文：Basically invisible tokens that are in the context window and remind the model of its identity.  
译文：基本上是上下文窗口中的不可见令牌，提醒模型其身份。  

**01:46:48 - 01:46:52**  
原文：But it's all just kind of like cooked up and bolted on in some in some way.  
译文：但所有这些都只是某种方式下拼凑和附加起来的。  

**01:46:52 - 01:46:54**  
原文：It's not actually like deeply there in any real sense.  
译文：实际上，它并没有真正深入其中。  

**01:46:54 - 01:47:06**  
原文：As it would be foreheai want to now continue to the next section, which deals with the computational capabilities, or like I should say, the native computational capabilities of these models in problem solving scenarios.  
译文：正如我所预见的，我想现在继续进入下一节，该节讨论这些模型的计算能力，或者更准确地说，是这些模型在问题解决场景中的固有计算能力。  

**01:47:06 - 01:47:12**  
原文：And so in particular, we have to be very careful with these models when we construct our examples of conversations.  
译文：因此，特别是在我们构建对话示例时，我们必须对这些模型非常小心。  

**01:47:12 - 01:47:19**  
原文：And there's a lot of sharp edges here that are kind of like elucidtive, that are word that kind of like interesting to look at when we consider how these models think.  
译文：这里有很多尖锐的边缘，它们有点像是启发性的，这些词在我们考虑这些模型是如何思考的时候，看起来很有趣。 

注：原文中“elucidtive”并非标准英文单词，可能是“elucidative”（启发性的，阐明的）一词的误写。  

**01:47:19 - 01:47:29**  
原文：So consider the following prompt from a human and suppose basically that we are building out a conversation to enter into our training set of conversations.  
译文：所以请考虑以下来自人类的提示，基本上假设我们正在构建一个对话，以加入我们的对话训练集。  

**01:47:29 - 01:47:31**  
原文：So we're going to train the model on this.  
译文：所以我们将在这一点上训练模型。  

**01:47:31 - 01:47:34**  
原文：We're teaching it how to basically solve simple math problems.  
译文：我们正在教它如何解决简单的数学问题。  

**01:47:34 - 01:47:37**  
原文：So the prompt is, Emily buys three apples and two oranges each.  
译文：所以提示是，Emily买了三个苹果和两个橙子。  

**01:47:37 - 01:47:39**  
原文：Orange cost $2.  
译文：Orange 橙子成本为 $2。  

**01:47:39 - 01:47:40**  
原文：The total cost is 13.  
译文：总成本是13。  

**01:47:40 - 01:47:41**  
原文：What is the cost of apples?  
译文：苹果的价格是多少？  

**01:47:41 - 01:47:43**  
原文：Very simple math question.  
译文：非常简单的数学问题。  

**01:47:43 - 01:47:46**  
原文：Now, there are two answers here, on the left and on the right.  
译文：现在，这里有两个答案，一个在左边，一个在右边。  

**01:47:46 - 01:47:47**  
原文：They are both correct answers.  
译文：它们都是正确答案。  

**01:47:47 - 01:47:51**  
原文：They both say that the answer is three, which is correct.  
译文：他们两个都说答案是三，这是正确的。  

**01:47:51 - 01:47:56**  
原文：But one of these two is a significantly better answer for the assistant than the other.  
译文：但这两个答案中有一个明显比另一个更适合助手。  

**01:47:56 - 01:48:05**  
原文：Like if I was data labeler and I was creating one of these, one of the thiwould be a really terrible answer for the assistant, and the other would be okay.  
译文：比如，如果我是数据标注员，我在创建这些答案时，其中一个会是对于助手来说非常糟糕的答案，而另一个则还可以。  

**01:48:05 - 01:48:13**  
原文：And so I'd like you to potentially pause the video even and think through why one of these two is significantly better answer than the other.  
译文：因此，我希望你甚至可以暂停一下视频，思考为什么这两个答案中的一个是明显更好的。  

**01:48:13 - 01:48:19**  
原文：And if you use the wrong one, your model will actually be really bad at math potentially, and they would have bad outcomes.  
译文：而且如果你用错了模型， 它的数学能力可能会真的很差， 并且会得出错误的结果。  

**01:48:19 - 01:48:29**  
原文：And this is something that you would be careful with in your labeling documentations when you are training people to create the ideal responses for the assistant.  
译文：这是你在培训人们创建理想的助手响应时，需要在标签文档中谨慎处理的事情。  

**01:48:29 - 01:48:29**  
原文：Okay.  
译文：好的。  

**01:48:29 - 01:48:39**  
原文：So the key to this question is to realize and remember that when the models are training and also inferencing, they are working in one dimensional sequence of tokens from left to right.  
译文：所以这个问题的关键是要意识到并记住，当模型进行训练和推理时，它们是从左到右处理一维的 token 序列。  

**01:48:39 - 01:48:42**  
原文：And this is the picture that I often have in my mind.  
译文：这是我脑海中经常浮现的画面。  

**01:48:42 - 01:48:46**  
原文：I imagine basically the token sequence evolving from left to right.  
译文：我想象基本上是从左到右演变的token序列。  

**01:48:46 - 01:48:51**  
原文：And to always produce the next token in a sequence, we are feeding all these tokens into the neural network.  
译文：并且为了总是生成序列中的下一个标记，我们将所有这些标记输入到神经网络中。  

**01:48:51 - 01:48:56**  
原文：And this neural network then gives us the probabilities for the next token in sequence, right?  
译文：然后这个神经网络为我们提供了序列中下一个标记的概率，对吧？  

**01:48:56 - 01:49:00**  
原文：So this picture here is the exhausame picture we saw before up here.  
译文：所以，这张图片就是我们之前在这里看到的那张排气图片。  

**01:49:00 - 01:49:04**  
原文：And this comes from the web demo that I showed you before, right?  
译文：而且这来自于我之前给你展示的网络演示，对吧？  

**01:49:04 - 01:49:15**  
原文：So this is the calculation that basically takes the input tokens here on the top and performs these operations of all these neurons and gives you the answer for the probabilities of what comes next.  
译文：所以这就是基本上将顶部的输入令牌进行处理，并执行所有这些神经元的操作，从而给出接下来出现的概率答案的计算。  

**01:49:15 - 01:49:24**  
原文：Now, the important thing to realize is that, roughly speaking, there's basically a finite number of layers of computation that happen here.  
译文：现在，重要的是要认识到，粗略地说，这里基本上有一个有限数量的计算层。  

**01:49:24 - 01:49:30**  
原文：So for example, this model here has only one to three layers of what's called detention and mlp here.  
译文：所以，例如，这里的模型只有被称为拘留和mlp的一到三层。 

注：根据上下文，“detention and mlp”可能是指特定技术术语，通常“detention”并不常用在该语境下，可能是“attention”（注意力机制）之误，如果是这样，更正后的翻译应为：

所以，例如，这里的模型只有被称为注意力机制和mlp的一到三层。  

**01:49:30 - 01:49:36**  
原文：Maybe a typical modern state of the art network would have more like, say, 100 layers or something like that.  
译文：也许一个典型的现代最先进的网络会有多达，比如说，100层或类似的数量。  

**01:49:36 - 01:49:44**  
原文：But there's only 100 layers of computation or something like that to go from the previous token sequence to the probties for the next token.  
译文：但从之前的 token 序列到下一个 token 的概率，只经过了 100 层计算或类似的过程。  

**01:49:44 - 01:49:50**  
原文：And so there's a finite amount of computation that happens here for every single token.  
译文：因此，对于每一个单独的令牌，这里的计算量是有限的。  

**01:49:50 - 01:49:54**  
原文：And you should think of this as a very small amount of computation.  
译文：你应该认为这只是非常少量的计算。  

**01:49:54 - 01:50:00**  
原文：And this amount of computation is almost roughly fixed for every single token in this sequence.  
译文：而且这个计算量对于这个序列中的每一个标记几乎是固定的。  

**01:50:00 - 01:50:08**  
原文：That's not actually fully, because the more tokens you feed in, the more expensive this forward PaaS will be of this neural network, but not by much.  
译文：实际上并不完全是这样，因为输入的 token 越多，这个神经网络的前向 PaaS 将会变得越昂贵，但并不会贵很多。  

**01:50:08 - 01:50:18**  
原文：So you should think of this, and I think as a good model to have in mind, this is a fixed amount of compute that's going to happen in this box for every single one of these tokens.  
译文：所以你应该这样考虑，我认为这是一个很好的思维模型，对于这其中的每一个标记，在这个框中都将发生固定数量的计算。  

**01:50:18 - 01:50:24**  
原文：And this amount of compute cannot possibly be too big because there's not that many layers that are sort of going from the top to bottom here.  
译文：而且这个计算量不可能太大，因为从顶层到底层并没有那么多层。  

**01:50:24 - 01:50:27**  
原文：There's not that, that much computationally that will happen here.  
译文：这里不会发生太多的计算。  

**01:50:27 - 01:50:32**  
原文：And so you can't imagine model to basically do arbitrary computation in a single forward PaaS to get a single token.  
译文：因此，你无法想象模型基本上能够在单次前向传递中执行任意计算以获得单个令牌。  

**01:50:32 - 01:50:44**  
原文：And so what that means is that we actually have to distribute our reasoning in our computation across many tokens, because every single token is only spending a finite amount of computation on it.  
译文：这意味着我们实际上必须将我们的推理和计算 分布到许多 token 上，因为每个 token 只能分配到有限的计算资源。  

**01:50:44 - 01:50:49**  
原文：And so we kind of want to distribute the computation across many tokens.  
译文：因此，我们想要将计算分布在许多令牌上。  

**01:50:49 - 01:50:59**  
原文：And we can't have too much computation or expect too much computation out of the model in any single individual token because there's only so much computation that happens per token.  
译文：而且我们不能对单个令牌的模型进行过多的计算或期望过多的计算，因为每个令牌只能进行有限的计算。  

**01:50:59 - 01:51:01**  
原文：Okay, roughly fixed amount of computation here.  
译文：好的，这里大约有一个固定的计算量。  

**01:51:01 - 01:51:06**  
原文：So that's why this answer here is significantly worse.  
译文：所以这就是为什么这里的答案明显更差。  

**01:51:06 - 01:51:12**  
原文：And the reason for that is, imagine going from left to right here and I copy paste it it right here.  
译文：这样做的原因是，想象一下从左到右的过程，然后我把它复制粘贴到这里。  

**01:51:12 - 01:51:15**  
原文：The answer is three etc..  
译文：答案是三个等。  

**01:51:15 - 01:51:21**  
原文：Imagine the model having to go from left to right emitting these tokens one at a time.  
译文：想象一下模型必须从左到右逐个发出这些标记。  

**01:51:21 - 01:51:26**  
原文：It has to say, or we expecting to say, the answer is space dollar sign.  
译文：必须说，或者我们期望说的是，答案是空格美元符号。  

**01:51:26 - 01:51:33**  
原文：And then right here, we're expecting it to basically cram all the computation of this problem into this single token.  
译文：然后在这里，我们期望它基本上将这个问题的所有计算都压缩到这一个标记中。  

**01:51:33 - 01:51:36**  
原文：It has to emit the correct answer three.  
译文：它必须发出正确的答案三次。  

**01:51:36 - 01:51:40**  
原文：And then once we've emitted the answer three, we're expecting it to say all these tokens.  
译文：然后一旦我们输出了答案三，我们就期望它说出所有这些标记。  

**01:51:40 - 01:51:47**  
原文：But at this point, we've already produced the answer and it's already in the context window for all these tokens that follow.  
译文：但在这个时间点，我们已经生成了答案，而且它已经在这些随后的令牌的上下文窗口中了。  

**01:51:47 - 01:51:54**  
原文：So anything here is just kind of post hoc justification of why this is the answer, because the answer is already created.  
译文：所以这里的一切都只是事后为这个答案找理由，因为答案已经确定了。  

**01:51:54 - 01:51:58**  
原文：It's already in the token window, so it's not actually being calculated here.  
译文：它已经在令牌窗口中了，所以实际上在这里并没有被计算。  

**01:51:58 - 01:52:07**  
原文：And so if you are answering the question directly and immediately, you are training the model to try to basically guess the answer in a single token.  
译文：因此，如果你直接且立即回答问题，你就是在训练模型尝试用单个令牌来猜测答案。  

**01:52:07 - 01:52:13**  
原文：And that is just not going to work because of the final ite amount of computation that happens per token.  
译文：而这行不通，是因为每个标记最终需要进行的计算量。  

**01:52:13 - 01:52:20**  
原文：That's why this answer on the right is significantly better because we are distributing this computation across the answer.  
译文：这就是为什么右边的答案要好得多，因为我们是将这个计算分布在答案中的。  

**01:52:20 - 01:52:25**  
原文：We're actually getting the model to sort of slowly come to the answer from the left to right.  
译文：我们实际上让模型从左到右慢慢得出答案。  

**01:52:25 - 01:52:27**  
原文：We're getting intermediate results.  
译文：我们正在取得中间结果。  

**01:52:27 - 01:52:30**  
原文：We're saying, okay, the total cost of oranges is four, so 30 minus four is nine.  
译文：我们说，好的，橙子的总成本是四元，所以30减去四是二十六。 

注：根据原文逻辑，30减去4应为26，而非九，可能是原文有误。  

**01:52:30 - 01:52:33**  
原文：And so we're creating intermediate calculations.  
译文：因此，我们正在创建中间计算。  

**01:52:33 - 01:52:37**  
原文：And each one of these calculations is by itself not that expensive.  
译文：而且这些计算中的每一种 本身都不是那么昂贵。  

**01:52:37 - 01:52:47**  
原文：And so we're actually basically kind of guessing a little bit the difficulty that the model is capable of in any single one of these individual tokens.  
译文：因此，我们实际上是在某种程度上猜测模型在这些单独的标记中的任何一个上能够处理的难度。  

**01:52:47 - 01:52:54**  
原文：And there can never be too much work in any one of these tokens computationally because then the model won't be able to do that later at test time.  
译文：而且这些标记中的任何一个在计算上都不能有过多的工作量，因为否则模型在测试时将无法完成这些工作。  

**01:52:54 - 01:53:01**  
原文：And so we're teaching the model here to spread out its reasoning and to spread out its computation over the tokens.  
译文：因此，我们在这里训练模型将其推理和计算分布在各个标记上。  

**01:53:01 - 01:53:06**  
原文：And in this way, it only has very simple problems in each token, and they can add up.  
译文：这样，每个标记只有非常简单的问题，但它们可以累加。  

**01:53:06 - 01:53:16**  
原文：And then by the time it's near the end, it has all the previous results in its working memory, and it's much easier for it to determine that the answer is, and here it is, three.  
译文：然后当它接近结束时，它的工作记忆中有所有之前的运算结果， 这样它就很容易得出答案是， 就在这里，三是答案。  

**01:53:16 - 01:53:19**  
原文：So this is a significantly better label for our computation.  
译文：所以这对我们的计算来说是一个明显更好的标签。  

**01:53:19 - 01:53:26**  
原文：This would be really bad and is teaching the model to try to do all the computation as single token and is really bad.  
译文：这将会非常糟糕，因为它在教导模型尝试将所有计算作为一个单独的标记来处理，这真的很不好。  

**01:53:26 - 01:53:41**  
原文：So that's kind of like an interesting thing to keep in mind is in your prompts, usually you don't have to think about it explicitly because the people at OpenAI have labelers and so on that actually worry about this and they make sure that the answers are spread out.  
译文：所以，这是一个有趣的地方，在你的提示中，通常你不需要明确地去考虑它，因为OpenAI的工作人员有标注人员等来实际关注这个问题，他们确保答案是分散的。  

**01:53:41 - 01:53:44**  
原文：And so actually OpenAI will kind of like do the right thing.  
译文：所以实际上，OpenAI 会做正确的事情。  

**01:53:44 - 01:53:48**  
原文：So when I ask this question for ChatGPT, it's actually going to go very slowly.  
译文：所以当我问ChatGPT这个问题时，它的反应实际上会非常慢。  

**01:53:48 - 01:53:55**  
原文：It's going to be like, okay, let's define our variables, set up the equation, and it's kind of creating all these intermediate results.  
译文：它将会是这样，好的，让我们定义变量，设置方程，然后会创建所有这些中间结果。  

**01:53:55 - 01:53:56**  
原文：These are not for you.  
译文：这些不是给你的。  

**01:53:56 - 01:53:57**  
原文：These are for the model.  
译文：这些是给模型用的。  

**01:53:57 - 01:54:04**  
原文：If the model is not creating these intermediate results for itself, it's not going to be able to reach three.  
译文：如果模型不生成这些中间结果，它将无法达到三。  

**01:54:04 - 01:54:08**  
原文：I also wanted to show you that it's possible to be a bit mean to the model.  
译文：我还想向您展示，对模型有点刻薄是可能的。  

**01:54:08 - 01:54:09**  
原文：We can just ask for things.  
译文：我们只需要索要东西。  

**01:54:09 - 01:54:17**  
原文：So as an example, I gave it the exact same prompt and I said, answer the question in a single token, just immediately give me the answer, nothing else.  
译文：所以，作为一个例子，我给了它完全相同的提示，并说，用一个标记回答问题，立即给我答案，不要加任何其他内容。  

**01:54:17 - 01:54:23**  
原文：And it turns out that for this simple prompt here, it actually was able to do it in a single go.  
译文：结果发现，对于这个简单的提示，它实际上能够在一次尝试中完成。  

**01:54:23 - 01:54:24**  
原文：So it just created a single.  
译文：所以它只创建了一个单一的。  

**01:54:24 - 01:54:26**  
原文：I think this is two tokens, right?  
译文：我认为这是两个标记，对吗？  

**01:54:26 - 01:54:28**  
原文：Because the dollar sign is its own token.  
译文：因为美元符号是它自己的标记。  

**01:54:28 - 01:54:35**  
原文：So basically, this model didn't give me a single token and gave me two tokens, but it still produced the correct answer.  
译文：所以基本上，这个模型没有给我一个单独的 token，而是给了我两个 tokens，但它仍然产出了正确的答案。  

**01:54:35 - 01:54:38**  
原文：And it did that in a single forward PaaS of the network.  
译文：而且它在网络的单次前向传递中就完成了这一点。  

**01:54:38 - 01:54:41**  
原文：Now that's because the numbers here, I think, are very simple.  
译文：这是因为这里的数字，我认为，非常简单。  

**01:54:41 - 01:54:44**  
原文：And so I made it a bit more difficult to be a bit mean to the model.  
译文：因此，我把它变得有点困难，以对模型稍微苛刻一些。  

**01:54:44 - 01:54:48**  
原文：So I said, Emily buys 23 apples and 177 oranges.  
译文：所以我说，Emily买了23个苹果和177个橙子。  

**01:54:48 - 01:54:51**  
原文：And then I just made the numbers a bit bigger.  
译文：然后我只把数字弄得更大了一点。  

**01:54:51 - 01:54:53**  
原文：And I'm just making it harder for the model.  
译文：我只是在让模型更难。  

**01:54:53 - 01:54:56**  
原文：I'm asking you to do more computation in a single token.  
译文：我要求你在单个令牌中进行更多的计算。  

**01:54:56 - 01:54:58**  
原文：And so I said the same thing, and here it gave me five.  
译文：所以我说了同样的话，然后这里它给了我五个。  

**01:54:58 - 01:55:00**  
原文：And five is actually not correct.  
译文：而且实际上五是不正确的。  

**01:55:00 - 01:55:04**  
原文：So the model failed to do all this calculation in a single forward pasof the network.  
译文：所以该模型未能在单次前向传播过程中完成所有这些计算。  

**01:55:04 - 01:55:06**  
原文：It failed to go from the input tokens.  
译文：它未能从输入令牌进行转换。  

**01:55:06 - 01:55:13**  
原文：And then in a single forward PaaS of the network, single go through the network, it couldn't produce the result.  
译文：然后在网络的单次前向 PaaS 中，一次性通过网络，它无法产生结果。  

**01:55:13 - 01:55:18**  
原文：And then I said, okay, now don't worry about the token limit and just solve the problem as usual.  
译文：然后我说，好的，现在不要担心令牌限制，只需像往常一样解决问题。  

**01:55:18 - 01:55:22**  
原文：And then it goes all the intermediate results, it simplifies.  
译文：然后它会处理所有中间结果，进行简化。  

**01:55:22 - 01:55:28**  
原文：And every one of these intermediate results here and intermediate calculations is much easier for the model.  
译文：而且这里的每一个中间结果和中间计算对模型来说都容易得多。  

**01:55:28 - 01:55:31**  
原文：And it's sort of it's not too much work per token.  
译文：而且它每个令牌的工作量并不是太大。  

**01:55:31 - 01:55:33**  
原文：All of the tokens here are correct.  
译文：这里的所有的代币都是正确的。  

**01:55:33 - 01:55:35**  
原文：And it arises the visolution, which is seven.  
译文：并且产生了visolution，它是七。  

**01:55:35 - 01:55:38**  
原文：And I just couldn't squeeze all of this work.  
译文：而且我根本无法完成所有这些工作。  

**01:55:38 - 01:55:41**  
原文：It couldn't squeeze that into a single for passing network.  
译文：它无法将那部分内容压缩到一个用于传递网络的单个单元中。  

**01:55:41 - 01:55:45**  
原文：So I think that's kind of just a cute example and something to kind of like think about.  
译文：所以我觉得这只是一个可爱的小例子，大家可以思考一下。  

**01:55:45 - 01:55:49**  
原文：And I think is kind of, again, just elucidative in terms of how these models work.  
译文：而且我认为这再次清楚地说明了这些模型的工作原理。  

**01:55:49 - 01:55:59**  
原文：The last thing that I would say on this topic is that if I was in practice trying to actually solve this in my day to day life, I might actually not trust that the model, that all the intermediate calculations is correctly here.  
译文：在这一话题上我要说的最后一件事是，如果我在实际操作中尝试在我的日常生活中真正解决这个问题，我可能实际上不会完全信任这个模型，即所有中间计算在这里都是正确的。  

**01:55:59 - 01:56:02**  
原文：So actually, probably what I do is something like this.  
译文：所以实际上，我可能做的事情是这样的。  

**01:56:02 - 01:56:03**  
原文：I would come here and I would say use code.  
译文：我会来这里，然后我说使用代码。  

**01:56:03 - 01:56:08**  
原文：And that's because code is one of the possible tools that chashepd can use.  
译文：而这就是因为代码是chashepd可以使用的工具之一。 

注：原文中的“chashepd”似乎是一个拼写错误或特定术语，在此直接进行了翻译，如果这是一个专有名词或有特定含义，请提供更多信息以便更准确地翻译。  

**01:56:08 - 01:56:13**  
原文：And instead of it having to do mental arithmetic like this, mental arithmetic here, I don't fully trust it.  
译文：而且它不用进行这样的心理算术，这里的心理算术，我并不完全信任它。  

**01:56:13 - 01:56:15**  
原文：And especially the numbers get really big.  
译文：而且特别是这些数字变得非常大。  

**01:56:15 - 01:56:18**  
原文：There's no guarantee that the model will do this correctly.  
译文：不能保证模型会正确执行此操作。  

**01:56:18 - 01:56:22**  
原文：Any one of these intermediate steps ths might in principle fail.  
译文：这些中间步骤中的任何一步都可能在原则上失败。  

**01:56:22 - 01:56:27**  
原文：We're using neural networks to do mental arithmetic, kind of like you do mental arithmetic in your brain.  
译文：我们正在使用神经网络来进行心算， 这有点像你用大脑进行心算一样。  

**01:56:27 - 01:56:30**  
原文：It might just like screw up some of the intermediate results.  
译文：它可能会像搞乱一些中间结果一样。  

**01:56:30 - 01:56:34**  
原文：It's actually kind of amazing that it can even do this kind of mental arithmetic.  
译文：它竟然能做这种心算，真是太神奇了。  

**01:56:34 - 01:56:40**  
原文：I don't think I could do this in my head, but basically the model is kind of like doing it in its head, and I don't trust that.  
译文：我不认为我能在脑海中完成这个，但基本上模型就像是在它的脑海中完成任务，而我不信任这种方式。  

**01:56:40 - 01:56:43**  
原文：So I wanted to use tools so you can stay stuff like use code.  
译文：所以我想要使用一些工具，这样你就可以像使用代码一样处理事情。  

**01:56:43 - 01:56:48**  
原文：And I'm not sure what happened there.  
译文：而且我不确定那里发生了什么。  

**01:56:48 - 01:56:49**  
原文：Use code.  
译文：使用代码。  

**01:56:50 - 01:56:57**  
原文：And so like I mentioned, there's a special tool and the model can write code, and I can inspect that this code is correct.  
译文：正如我提到的，有一个特殊的工具，模型可以编写代码，我可以检查这段代码是否正确。  

**01:56:57 - 01:57:00**  
原文：And then it's not relying on its mental arithmetic.  
译文：然后它并不依赖于它的珠算。  

**01:57:00 - 01:57:08**  
原文：It is using the Python interpreter, which is a very simple programming language, to basically write out the code that calculates the result.  
译文：它使用的是Python解释器，这是一种非常简单的编程语言，基本上是用来编写计算结果的代码。  

**01:57:08 - 01:57:18**  
原文：And I would personally trust this a lot more because this came out of the Python program, which I think has a lot more correctness guarantees than the mental arithmetic of a language model.  
译文：而且我个人会更加信任这个结果，因为这是从Python程序中得出的，我认为它比语言模型的心算具有更多的正确性保证。  

**01:57:18 - 01:57:28**  
原文：So just another kind of potential hint that if you have these kinds of problems, you may want to basically just ask the model to use the code interpreter.  
译文：所以，这只是另一种潜在的提示，即如果你有这类问题，你可能只想让模型使用代码解释器。  

**01:57:28 - 01:57:34**  
原文：And just like we saw with the web search, the model has special kind of tokens for calling.  
译文：就像我们从网络搜索中看到的那样，该模型有专门用于调用的特殊令牌。  

**01:57:34 - 01:57:38**  
原文：Like it will not actually generate these tokens from the language model.  
译文：就像它并不会实际从语言模型生成这些令牌。  

**01:57:38 - 01:57:54**  
原文：It will write the program and then it actually sends that program to a different sort of part of the computer that actually just runs that program and brings back the result and then the model gets access to that result and can tell you that, okay, the cost of each chapel is sudden.  
译文：它将编写程序，然后实际上将该程序发送到计算机的另一个部分，该部分只运行该程序并带回结果，然后模型可以访问该结果，并可以告诉你，好的，每个小教堂的成本是突然的。 

注：最后一句中的“每个小教堂的成本是突然的”在原文中似乎表述有误，可能需要根据上下文进行调整以确保意思准确。如果你能提供更多的上下文信息，我可以更准确地翻译这段话。  

**01:57:54 - 01:57:56**  
原文：So that's another kind of tool.  
译文：所以那是一种不同的工具。  

**01:57:56 - 01:57:59**  
原文：And I would use this in practice for yourself.  
译文：你可以在实践中为自己使用这个方法。  

**01:57:59 - 01:58:01**  
原文：And it's Yeah it's just less error prone, I would say.  
译文：And it's 是的，我会说它只是较少出错。  

**01:58:01 - 01:58:03**  
原文：So that's why I've called this section.  
译文：这就是我为什么要这样称呼这一部分。  

**01:58:03 - 01:58:17**  
原文：Models need tokens to think, distribute your competition across many tokens, ask models to create intermediate results or whenever you can lean on tools and tool use instead of allowing the models to do all of this stuff in their memory.  
译文：模型需要令牌来思考，将您的竞争分布在多个令牌上，要求模型创建中间结果，或者在可以依赖工具和工具使用的情况下，而不是允许模型在它们的记忆中完成所有这些工作。 

（注：这段话中的“令牌”通常指的是一种计费或资源分配单位，在某些上下文中翻译为“token”。根据具体应用场景，也可译作“代币”或其他合适术语。）  

**01:58:17 - 01:58:24**  
原文：So if they try to do it all in their memory, don't fully trust it and prefer to use tools whenever possible.  
译文：所以，如果他们试图全部依靠记忆来完成，不要完全相信它，而是在可能的情况下尽量使用工具。  

**01:58:24 - 01:58:29**  
原文：I want to show you one more example of where this actually comes up, and that's in counting.  
译文：我想再给你举一个实际应用的例子，  
那就是在计数中。  

（保持了原始格式的换行）  

**01:58:29 - 01:58:36**  
原文：Some models actually are not very good at counting for the exact same reason you're asking for way too much in a single individual token.  
译文：有些模型实际上并不擅长计数，原因正是你所问的那样，在单个令牌中要求过多。  

**01:58:36 - 01:58:39**  
原文：So let me show you a simple example of that.  
译文：那么让我给你看一个简单的例子。  

**01:58:39 - 01:58:40**  
原文：How many dots are below?  
译文：下面有多少个点？  

**01:58:40 - 01:58:44**  
原文：And then I just put in a bunch of dots, and chashept says there are.  
译文：然后我只放了一堆点，chashept 说确实有。  

**01:58:44 - 01:58:47**  
原文：And then it just tries to solve the problem in a single token.  
译文：然后它只是尝试用一个标记来解决问题。  

**01:58:47 - 01:58:56**  
原文：So in a single token, it has to count the number of dots in its context window, and it has to do that in a single forward PaaS of a network.  
译文：所以在一个单独的 token 中，它必须计算其上下文窗口中的点的数量，并且必须在网络的单次前向传递中完成这一任务。  

**01:58:56 - 01:59:02**  
原文：And a single forward PaaS of a network, as we talked about, there's not that much computation that can happen there.  
译文：正如我们所讨论的，网络的单一前向PaaS平台，那里并没有太多的计算能力。  

**01:59:02 - 01:59:06**  
原文：Just think of that as being like very little computation that happens there.  
译文：只需将其视为在那里发生的计算非常少。  

**01:59:06 - 01:59:10**  
原文：So if I just look at what the model sees, let's go to the lm code to tokenzer.  
译文：所以如果我只看模型看到的内容，让我们去lm代码的tokenzer。  

**01:59:10 - 01:59:13**  
原文：It sees this, how many dots are below?  
译文：它看到了这个，下面有多少个点？  

**01:59:13 - 01:59:20**  
原文：And then it turns out that these dots here, this group of, I think, 20 dots, is a single token.  
译文：然后发现这些点，这组我认为有20个点，实际上是一个单一的标记。  

**01:59:20 - 01:59:24**  
原文：And then this group of whatever it is, is another token.  
译文：然后这组东西，不管是什么，是另一个令牌。  

**01:59:24 - 01:59:27**  
原文：And then for some reason, they break up as this.  
译文：然后不知为什么，它们就这样分开了。  

**01:59:27 - 01:59:38**  
原文：So I don't actually, this has to do with the details of the tokenzer, but it turns out that these, the model basically sees the token ID, this, this, this and so on.  
译文：所以实际上，这与tokenzer的细节有关，但结果发现，模型基本上看到的是token ID，就是这个，这个，这个等等。  

**01:59:38 - 01:59:42**  
原文：And then from these token ids, it's expected to count the number.  
译文：然后从这些 token id 中，预期要计算数量。  

**01:59:42 - 01:59:44**  
原文：And spoiler alert is not 161.  
译文：And spoiler alert is not 161. 

剧透警告：答案不是161。  

**01:59:44 - 01:59:48**  
原文：It's actually, I believe, 177.  
译文：实际上是，我相信，177。  

**01:59:48 - 01:59:49**  
原文：So here's what we can do instead.  
译文：所以我们不妨这样做。  

**01:59:49 - 01:59:51**  
原文：We can say use code.  
译文：我们可以说使用代码。  

**01:59:51 - 01:59:53**  
原文：And you might expect that like why should this work?  
译文：你可能会觉得，这怎么会有效呢？  

**01:59:53 - 01:59:56**  
原文：And it's actually kind of subtle and kind of interesting.  
译文：而且它实际上有点微妙和有趣。  

**01:59:56 - 01:59:59**  
原文：So when I say use code, I actually expect this to work.  
译文：所以当我说使用代码时，我实际上是希望这能奏效。  

**01:59:59 - 01:59:59**  
原文：Let's see.  
译文：让我们看看。  

**01:59:59 - 02:00:02**  
原文：Okay, 177 is correct.  
译文：好的，177是正确的。  

**02:00:02 - 02:00:10**  
原文：So what happens here is I've actually it doesn't look like it, but I've broken down the problem into problems that are easier for the model.  
译文：所以这里发生的是，虽然看起来不像，但我已经将问题分解为对模型来说更容易处理的问题。  

**02:00:10 - 02:00:18**  
原文：I know that the model can't count, it can't do mental counting, but I know that the model is actually pretty good at doing copy pasting.  
译文：我知道模型不会数数，它不能进行心算，但我明白模型实际上很擅长做复制粘贴。  

**02:00:18 - 02:00:24**  
原文：So what I'm doing here is when I say use code, it creates a string in Python for this.  
译文：所以这里我所做的就是，当我说明使用代码时，它会在Python中创建一个字符串。  

**02:00:24 - 02:00:35**  
原文：And the task of basically copy pasting my input here to here is very simple, because for the model es, this string of it sees it as just these four tokens or whatever it is.  
译文：将以下文本翻译成中文，保持原始格式：

将我的输入从这里复制粘贴到这里的任务非常简单，因为对于模型来说，这一串内容只被视为这四个标记或类似的东西。  

**02:00:35 - 02:00:42**  
原文：So it's very simple for the model to copy paste those token ids and kind of unpack them into dots here.  
译文：所以模型非常容易地复制粘贴这些标记ID，并将它们在这里解包成点。  

**02:00:42 - 02:00:50**  
原文：And so it creates a string, and then it calls Python routine dot count, and then it comes up with the correct answer.  
译文：它创建了一个字符串，然后调用 Python 的 count 方法，接着得出了正确答案。  

**02:00:50 - 02:00:53**  
原文：So the Python interpreter is doing the counting.  
译文：所以 Python 解释器在进行计数。  

**02:00:53 - 02:00:57**  
原文：It's not the modelmental arithmetic doing the counting.  
译文：这不是心算模型在进行计算。  

**02:00:57 - 02:01:03**  
原文：So it's again, the simple example of models need tokens to think, don't rely on their mental arithmetic.  
译文：所以，这再次证明了一个简单的例子：模型需要令牌来思考，不要依赖于它们的心算。  

**02:01:03 - 02:01:06**  
原文：And that's why also the models are not very good at counting.  
译文：这就是为什么这些模型在计数方面也不是很好。  

**02:01:06 - 02:01:10**  
原文：If you need them to do counting tasks, always ask them to lean on the tool.  
译文：如果你需要他们进行计数任务，总是要求他们依赖工具。  

**02:01:10 - 02:01:14**  
原文：Now the models also have many other little cognitive deficits here and there.  
译文：现在这些模型在各个地方还有很多其他的小认知缺陷。  

**02:01:14 - 02:01:19**  
原文：And these are kind of like sharp edges of the technology to be kind of aware of over time.  
译文：这些就像是技术的尖端，是我们需要随着时间加以关注的。  

**02:01:19 - 02:01:23**  
原文：So as an example, the models are not very good with all kinds of spelling related tasks.  
译文：所以，举个例子来说，这些模型在各种与拼写相关的任务上表现得并不是很好。  

**02:01:23 - 02:01:25**  
原文：They're not very good at it.  
译文：他们并不擅长于此。  

**02:01:25 - 02:01:29**  
原文：And I told you that we would loop back around to tokenzation.  
译文：而且我告诉过你，我们会回到tokenization这个话题的。  

**02:01:29 - 02:01:34**  
原文：And the reason to do for this is that the models, they don't see the characters.  
译文：这样做的原因是模型看不到字符。  

**02:01:34 - 02:01:35**  
原文：They see tokens.  
译文：他们看到令牌。  

**02:01:35 - 02:01:39**  
原文：And their entire world is about tokens, which are these little text chunks.  
译文：他们的整个世界围绕着令牌展开，这些令牌就是一些小的文本片段。  

**02:01:39 - 02:01:41**  
原文：And so they don't see characters like our eyes do.  
译文：因此，他们看不见像我们眼睛所看到的字符。  

**02:01:41 - 02:01:44**  
原文：And so very simple character level tasks often fail.  
译文：因此，非常简单的字符级任务经常失败。  

**02:01:44 - 02:01:52**  
原文：So for example, I'm giving it a string, ubiquitous, and I'm asking it to print only every third character, starting with the first one.  
译文：所以，例如，我给它一个字符串 "ubiquitous"，并要求它从第一个字符开始，只打印每第三个字符。  

**02:01:52 - 02:01:56**  
原文：So we start with you, and then we should go every third.  
译文：所以我们从你开始，然后我们应该每隔两个进行。  

（注：根据上下文，“每隔两个进行”可能是指“每隔两个人进行”或“每第三个进行”，具体含义需要根据实际情况确定。）  

如果你有更多上下文或者特定的表达偏好，请告诉我！  

**02:01:56 - 02:02:00**  
原文：So every so one, two, three, q should be next, and then etc..  
译文：所以每隔一个，两个，三个，q应该排在后面，然后等等。  

**02:02:00 - 02:02:02**  
原文：So this ic, see, is not correct.  
译文：所以这个 ic，看，是不正确的。  

**02:02:02 - 02:02:09**  
原文：And again, my hypothesis is that this is, again, the mental arithmetic here is failing, number one, a little bit.  
译文：再次重申，我的假设是，这里的心理算术再次出现了一些问题。  

**02:02:09 - 02:02:18**  
原文：But number two, I think the more important issue here is that if you go to titokenzer and you look at ubiquitous, we see that it is three tokens, right?  
译文：但第二点，我认为这里更重要的问题是，如果你去查看titokenzer，并查看 ubiquitous，我们会发现它是三个标记，对吗？  

**02:02:18 - 02:02:24**  
原文：So you and I see ubiquitous and we can easily access the individual letters because we kind of see them.  
译文：所以你和我看到的是无处不在的，我们可以轻松访问各个字母，因为我们某种程度上是看见它们的。  

**02:02:24 - 02:02:30**  
原文：And when we have it in the working memory of our visual sort of field, we can really easily index into every third letter.  
译文：当我们在视觉工作记忆中有这个序列时， 我们可以很轻松地每隔两个字母进行索引。  

**02:02:30 - 02:02:32**  
原文：And I can do that task.  
译文：而且我可以完成那项任务。  

**02:02:32 - 02:02:35**  
原文：But the models don't have access to the individual letters.  
译文：但是这些模型无法访问单个字母。  

**02:02:35 - 02:02:37**  
原文：They see this as these three tokens.  
译文：他们将其视为这三个标记。  

**02:02:37 - 02:02:40**  
原文：And remember, these models are trained from scratch on the Internet.  
译文：并记住，这些模型是从互联网上从零开始训练的。  

**02:02:40 - 02:02:47**  
原文：And all these token, basically, the model has to discover how many of all these different letters are packed into all these different tokens.  
译文：而且，所有这些标记，基本上，模型必须发现所有这些不同的字母中有多少被打包到了所有这些不同的标记中。  

**02:02:47 - 02:02:50**  
原文：And the reason we even use tokens is mostly for efficiency.  
译文：我们使用令牌的原因主要是为了提高效率。  

**02:02:50 - 02:02:57**  
原文：But I think a lot of people are interested to delete tokens entirely, like we should really have character level or byte level models.  
译文：但我认为很多人都有兴趣完全删除tokens，比如我们应该真正拥有字符级或字节级模型。  

**02:02:57 - 02:03:02**  
原文：It's just that that would create very long sequences, and people don't know how to deal with that right now.  
译文：只是这会创建非常长的序列，而人们目前不知道如何处理这些问题。  

**02:03:02 - 02:03:06**  
原文：So while we have the token world, any kind of spelling tasks are not actually expected to work super well.  
译文：所以，虽然我们有令牌世界，但任何形式的拼写任务实际上都不太可能运作得非常好。  

**02:03:06 - 02:03:14**  
原文：So because I know that spelling is not a strong suit because of organization, I can again ask it to lean on tools.  
译文：所以，因为我知道由于组织能力拼写不是我的强项，我再次要求它依赖工具。  

**02:03:14 - 02:03:15**  
原文：So I can just say use code.  
译文：所以我就直接说使用代码。  

**02:03:15 - 02:03:22**  
原文：And I would again expect this to work, because the task of copy pasting ubiquitous into the Python interpreter is much easier.  
译文：并且我再次认为这会奏效，因为将“ubiquitous”复制粘贴到Python解释器中的任务要简单得多。  

**02:03:22 - 02:03:27**  
原文：And then we're leaning on Python interpreter to manipulate the characters of this string.  
译文：然后我们依赖 Python 解释器来操作这个字符串的字符。  

**02:03:27 - 02:03:33**  
原文：So an essay use code ubiquitous, yes, it indexes into every third character.  
译文：所以一篇文章使用无处不在的代码，是的，它索引到每一个第三个字符。  

**02:03:33 - 02:03:37**  
原文：And the actual truth is uq two s, uq ts, which looks correct to me.  
译文：而实际上正确的答案是 uq two s, uq ts，这看起来是对的。  

**02:03:37 - 02:03:41**  
原文：So again, an example of spelling related tasks not working very well.  
译文：所以， again, 这是一个拼写相关任务完成得不是很好的例子。 

注：根据上下文，“So again”放在句首更符合中文表达习惯，但为了严格遵守保持原始格式的要求，此处将其翻译为“所以，again”。如果不需要完全保留原始格式，建议调整为：“所以，这再次成为一个拼写相关任务完成得不是很好的例子。”  

**02:03:41 - 02:03:46**  
原文：A very famous example of that recently is how many are are there in strawberry?  
译文：最近一个非常著名的例子是，草莓里有多少个“are”？ 

注：原句似乎有些语法错误或表达不清，“how many are are there in strawberry?” 这句话在英文中不太通顺。如果你的意思是问草莓里有多少颗种子或其他内容，请提供更多的上下文以便准确翻译。  

**02:03:46 - 02:03:48**  
原文：And this one viral many times.  
译文：而这个病毒传播了多次。  

（注意：原句在语法上似乎不太正确，以上翻译是根据可能的意思进行的。如果需要更准确的翻译，请提供更多的上下文。）  

**02:03:48 - 02:03:50**  
原文：And basically the models now get it correct.  
译文：而现在基本上模型都做对了。  

**02:03:50 - 02:03:53**  
原文：They say there are three R's in strawberry.  
译文：他们说草莓里有三个R。  

**02:03:53 - 02:04:00**  
原文：But for a very long time, all the state of the art models would insist that there are only two R's in strawberry.  
译文：但很长一段时间里，所有最先进模型都坚持认为“strawberry”（草莓）中只有两个“R”。  

**02:04:00 - 02:04:03**  
原文：And this caused a lot of, you know ruckus because is that a word?  
译文：这引起了很多骚动，你知道的，这个词是吗？  

**02:04:03 - 02:04:04**  
原文：I think so.  
译文：我认为是这样。  

**02:04:04 - 02:04:08**  
原文：Because it's just kind of like, why are the models so brilliant?  
译文：因为这就像在问，为什么这些模型如此出色？  

**02:04:08 - 02:04:12**  
原文：And they can solve methyympiaquestions, but they can't like count ours in strawberry.  
译文：他们可以解决methyympia问题，但他们不能像在草莓中数数一样。 

注：原文中的“methyympiaquestions”看起来像是拼写错误或自创词，我直接将其翻译为“methyympia问题”。如果这是一个特定术语或有上下文，请提供更多信息以便更准确地翻译。  

**02:04:12 - 02:04:16**  
原文：And the answer for that, again, is I can't of built up to it kind of slowly.  
译文：对于那个问题，我再次回答我不能慢慢来。  

**02:04:16 - 02:04:19**  
原文：But number one, the models don't see characters.  
译文：但首要的是，模型并不识别字符。  

**02:04:19 - 02:04:20**  
原文：They see tokens.  
译文：他们看到令牌。  

**02:04:20 - 02:04:22**  
原文：And number two, they are not very good at counting.  
译文：第二，它们不擅长数数。  

**02:04:22 - 02:04:28**  
原文：And so here we are combining the difficulty of seeing characters with the difficulty of counting.  
译文：所以我们在这里将识别字符的难度与计数的难度结合在一起。  

**02:04:28 - 02:04:41**  
原文：And that's why the models struggled with this, even though I think by now, honestly, I think openeye may have hard dcoded the answer here, or I'm not sure what they did, but this specific query now works.  
译文：这就是为什么模型在这方面遇到了困难，即使到现在，坦率地说，我认为 openeye 可能已经硬编码了答案，或者我不确定他们做了什么，但这个特定的查询现在可以正常工作了。  

**02:04:42 - 02:04:46**  
原文：Models are not very good at spelling, and there's a bunch of other little sharp edges.  
译文：模型的拼写不太好，还有一堆其他的小问题。  

**02:04:46 - 02:04:48**  
原文：And I don't want to go into all of them.  
译文：而且我不想一一阐述。  

**02:04:48 - 02:04:52**  
原文：I just want to show you a few examples of things to be aware of.  
译文：我只想给您展示一些需要注意的事情的例子。  

**02:04:52 - 02:04:59**  
原文：And when you're using these models in practice, I don't actually want to have a comprehensive analysis here of all the ways that the models are kind of like falling short.  
译文：在实际使用这些模型时，我并不想在这里对所有模型存在的不足进行全面分析。  

**02:04:59 - 02:05:07**  
原文：I just want to make the point that there are some jagged edges here and there, and we've discussed a few of them, and a few of them make sense, but some of them also will just not make as much sense.  
译文：我只想说明，这里那里有些不平整的地方，我们已经讨论了一些，其中一些是有道理的，但有些可能就没有那么多意义。  

**02:05:07 - 02:05:12**  
原文：And they're kind of like you're left scratching your head even if you understand in depth how these models work.  
译文：即使你深入理解这些模型的工作原理，你也可能会感到困惑不解。  

**02:05:12 - 02:05:16**  
原文：And and a good example of that recently is the following.  
译文：最近一个很好的例子是以下这个。  

**02:05:16 - 02:05:19**  
原文：The models are not very good at very simple questions like this.  
译文：这些模型对于这种非常简单的问题处理得不太好。  

**02:05:19 - 02:05:25**  
原文：And this is shocking to a lot of people because H, these problems can solve complex math problems.  
译文：这令很多人震惊，因为H，这些问题可以解决复杂的数学问题。  

**02:05:25 - 02:05:30**  
原文：They can answer PhD grade physics, chemistry, biology questions much better than I can.  
译文：他们可以回答博士级别的物理、化学、生物问题，比我答得好多了。  

**02:05:30 - 02:05:33**  
原文：But sometimes they fall short tened like super simple problems mpts like this.  
译文：但有时候它们会像这种非常简单的问题一样出错。  

**02:05:33 - 02:05:34**  
原文：So here we go.  
译文：那么我们开始吧。  

**02:05:34 - 02:05:37**  
原文：Nine point eleven is bigger than 9.9.  
译文：九点十一比9.9大。  

**02:05:37 - 02:05:39**  
原文：It justifies it in some way.  
译文：它在某种程度上为此找到了理由。  

**02:05:39 - 02:05:44**  
原文：But obviously, and then at the end, okay, it actually, it flips its decision later.  
译文：但显然，最后，好吧，它实际上在后来改变了决定。  

**02:05:44 - 02:05:47**  
原文：So I don't believe that this is very reproducible.  
译文：所以我并不认为这非常可重复。  

**02:05:47 - 02:05:53**  
原文：Sometimes it flips around its tensor, sometimes gets it right, sometimes gets it wrong.  
译文：有时它会在其张量周围翻转，有时会做对，有时会做错。  

**02:05:53 - 02:05:54**  
原文：Let's try again.  
译文：让我们再试一次。  

**02:05:57 - 02:06:02**  
原文：Okay, even though it might look larger, okay, so here, it doesn't even correct itself in the end.  
译文：好的，即使它看起来可能更大，好的，那么在这里，最终它甚至没有自我纠正。  

**02:06:02 - 02:06:05**  
原文：If you ask many times, sometimes it gets it right too.  
译文：如果你多次询问，有时候它也会答对。  

**02:06:05 - 02:06:11**  
原文：But how is it that the model can do so great at Olympiad grade problems, but then fail on very simple problems like this?  
译文：但是，为什么这个模型可以在奥林匹克级别的问题上表现得如此出色，却在像这样的非常简单的问题上失败呢？  

**02:06:11 - 02:06:16**  
原文：And I think this one is, as I mentioned, a little bit of a head scratcher.  
译文：如我之前所说，这个有点令人困惑。  

**02:06:16 - 02:06:41**  
原文：It turns out that a bunch of people studied this in depth, and I haven't actually read the paper, but what I was told by this team was that when you scrutinize the activations inside the neural network, when you look at some of the features and what features turn on or off and what neurons turn on or off, a bunch of neurons inside the neural network light up that are usually associated with Bible verses.  
译文：结果发现，有一群人对此进行了深入研究， 我实际上还没有读过那篇论文， 但是这个团队告诉我， 当你仔细研究神经网络中的激活情况时， 当你查看某些特征以及哪些特征被激活或未被激活， 哪些神经元被激活或未被激活时， 神经网络中的一组神经元会被激活， 而这些神经元通常与圣经经文相关联。  

**02:06:41 - 02:06:47**  
原文：And so I think the model kind of like reminded that these almost look like Bible verse markers.  
译文：所以我认为这个模型有点像是提醒我们，这些几乎看起来像圣经经文标记。  

**02:06:47 - 02:06:51**  
原文：And in a Bible verse setting, nine point eleven come after 9.9.  
译文：在圣经经文的设定中，九点十一出现在9.9之后。  

**02:06:51 - 02:07:00**  
原文：And so basically the model somehow finds it like cognitively very distracting that in Bible verses nine point eleven would be greater.  
译文：所以基本上，模型觉得圣经章节中九点十一（9:11）大于其他数字这一点在认知上非常分散注意力。 

注：此句中的“nine point eleven”可能指代特定的圣经章节编号，直译为“九点十一”，但在中文中通常会根据上下文调整为更合适的表达方式。如果这里指的是章节编号，可能需要依据具体情况进行适当调整。  

**02:07:00 - 02:07:07**  
原文：Even though here it's actually trying to justify and comp to the answer with a math, it still ends up with the wrong answer here.  
译文：即使这里实际上试图用数学方法来证明和比较答案，但最终还是得到了错误的答案。  

**02:07:07 - 02:07:14**  
原文：So it basically just doesn't fully make sense and it's not fully understood, and there's a few jagged issues like that.  
译文：所以这基本上只是不完全说得通，也不完全被理解，而且有一些这样尖锐的问题。  

**02:07:14 - 02:07:29**  
原文：So that's why treat this as what it is, which is a stochastic system that is really magical, but that you can't also fully trust, and you want to use it as a tool, not as something that you kind of like let a rip on a problem and coppaste the results.  
译文：所以，这就是为什么要把这看作它本身所是的东西，即一个真正神奇的随机系统，但你不能完全信任它，你想把它当作一个工具来使用，而不是像放任不管那样去处理问题并直接粘贴结果。  

**02:07:29 - 02:07:29**  
原文：Okay.  
译文：好的。  

**02:07:29 - 02:07:33**  
原文：So we have now covered two major stages of training of large language models.  
译文：所以我们现在已经涵盖了大型语言模型训练的两个主要阶段。  

**02:07:33 - 02:07:35**  
原文：We saw that in the first stage.  
译文：我们在第一阶段就看到了这一点。  

**02:07:35 - 02:07:37**  
原文：This is called the pre training stage.  
译文：这被称为预训练阶段。  

**02:07:37 - 02:07:39**  
原文：We are basically training on Internet documents.  
译文：我们基本上是在互联网文档上进行训练。  

**02:07:39 - 02:07:45**  
原文：And when you train a language model in internal documents, you get what's called a base model.  
译文：当你在内部文档中训练语言模型时，你所得到的被称为基础模型。  

**02:07:45 - 02:07:48**  
原文：And it's basically an Internet document simulator right now.  
译文：它基本上是一个互联网文档模拟器。  

**02:07:48 - 02:07:54**  
原文：We saw that this is an interesting artifact, and this takes many months to train on thousands of computers.  
译文：我们看到这是一个有趣的成果，而且这需要在数千台计算机上训练许多个月。  

**02:07:54 - 02:08:02**  
原文：And it's kind of a lossy compression of the Internet, and it's extremely interesting, but it's not directly useful because we don't want to sample Internet documents.  
译文：它是互联网的一种有损压缩形式，非常有趣， 但它并不具备直接的实用性， 因为我们并不想对互联网文档进行抽样。  

**02:08:02 - 02:08:06**  
原文：We want to ask questions of an AI and have it respond to our questions.  
译文：我们想向人工智能提问并让它回答我们的问题。  

**02:08:06 - 02:08:08**  
原文：So for that, we need an assistant.  
译文：所以，我们需要一个助手。  

**02:08:08 - 02:08:19**  
原文：And we saw that we can actually construct an assistant in the process of a post training, and specifically in the process of supervised fine tuning, as we call it.  
译文：我们发现，我们实际上可以在训练后的过程中构建一个助手，具体来说，是在我们所谓的监督微调过程中。  

**02:08:19 - 02:08:25**  
原文：So in this stage, we saw that it's algorithmically identical to pre training.  
译文：所以在这一阶段，我们看到它在算法上与预训练是相同的。  

**02:08:25 - 02:08:27**  
原文：Nothing is going to change.  
译文：什么都不会改变。  

**02:08:27 - 02:08:29**  
原文：The only thing that changes is the data aset.  
译文：唯一改变的是数据集。  

**02:08:29 - 02:08:36**  
原文：So instead of Internet documents, we now want to create and curate a very nice data set of conversations.  
译文：所以我们现在想要创建和整理的， 不是互联网文档， 而是一些非常不错的对话数据。  

**02:08:36 - 02:08:42**  
原文：So we want million conversations on all kinds of divertopics between a human and an assistant.  
译文：所以我们希望在人类和助手之间进行数以百万计的各种话题的对话。  

**02:08:42 - 02:08:47**  
原文：And fundamentally, these conversations are created by humans.  
译文：从根本上讲，这些对话是由人类创造的。  

**02:08:47 - 02:08:51**  
原文：So humans write the prompts and humans write the ideal responses.  
译文：所以人类编写提示，人类也编写理想的回答。  

**02:08:51 - 02:08:54**  
原文：And they do that based on labeling documentations.  
译文：他们根据标注文档来做这件事。  

**02:08:54 - 02:08:59**  
原文：Now, in the modern stack, it's not actually done fully and manually by humans, right?  
译文：现在，在现代技术栈中，这实际上并不是完全由人类手动完成的，对吧？  

**02:08:59 - 02:09:02**  
原文：They actually now have a lot of help from these tools.  
译文：他们现在其实得到了这些工具的很多帮助。  

**02:09:02 - 02:09:06**  
原文：So we can use language models to help us create these data asets.  
译文：所以我们可以使用语言模型来帮助我们创建这些数据集。  

**02:09:06 - 02:09:08**  
原文：And we've just done extensively.  
译文：我们刚刚进行了广泛的讨论。  

**02:09:08 - 02:09:12**  
原文：But fundamentally, it's also still coming from human creation at the end.  
译文：但从根本上来说，最终它仍然是来源于人类的创造。  

**02:09:12 - 02:09:15**  
原文：So we create these conversations that now becomes our data set.  
译文：所以我们创建了这些对话，它们现在成为了我们的数据集。  

**02:09:15 - 02:09:19**  
原文：We find tune on it or continue training on it, and we get an assistant.  
译文：我们在其上进行微调或继续训练，然后我们就得到了一个助手。  

**02:09:19 - 02:09:26**  
原文：And then we kind of shifted gears and started talking about some of the kind of cognitive implications of what the assistant is like.  
译文：然后我们稍微转变了话题，开始讨论助理所带来的一些认知上的影响。  

**02:09:26 - 02:09:32**  
原文：And we saw that, for example, the assistant will hallucinate if you don't take some sort of mitigations towards it.  
译文：我们看到，例如，如果不采取某种缓解措施，助手就会产生幻觉。  

**02:09:32 - 02:09:35**  
原文：So we saw that hallucinations would be common.  
译文：所以我们看到幻觉将会很常见。  

**02:09:35 - 02:09:39**  
原文：And then we looked at some of the mitigations of those hallucinations.  
译文：然后我们看了一些这些幻觉的缓解措施。  

**02:09:39 - 02:09:47**  
原文：And then we saw that the models are quite impressive and can do a lot of stuff in their head, but we saw that they can also lean on tools to become better.  
译文：然后我们看到这些模型相当令人印象深刻，能够在脑海中完成很多任务，但也发现它们可以依赖工具来变得更好。  

**02:09:47 - 02:09:55**  
原文：So for example, we can lean on a web search in order to hallucinate less and to maybe bring up some more recent information or something like that.  
译文：所以，例如，我们可以依赖网络搜索来减少幻想，并可能带来一些更近期的信息或类似的东西。  

**02:09:55 - 02:09:57**  
原文：Or we can lean on tools like code interpreter.  
译文：或者我们可以依赖像代码解释器这样的工具。  

**02:09:57 - 02:10:01**  
原文：So so the llm can invite some code and actually run it and see the results.  
译文：所以，LLM可以邀请一些代码并实际运行它并查看结果。  

**02:10:02 - 02:10:06**  
原文：So these are some of the topics we looked at so far.  
译文：所以这些是我们目前研究的一些主题。  

**02:10:06 - 02:10:14**  
原文：Now what I'd like to do is I'd like to cover the last and major stage of this pipeline, and that is reinforinforcement learning.  
译文：现在我想做的是，我想涵盖这个管道的最后一个主要阶段，那就是强化学习。  

**02:10:14 - 02:10:22**  
原文：So reinforcement learning is still kind of thought to be under the umbrella of post training, but it is the last third major stage.  
译文：因此，强化学习仍然被认为是在训练后处理的范畴内，但它是最後第三个主要阶段。 

注：为了保持原始格式，此处的翻译尽量遵循原文的结构，但请注意，这句话在中文中可能不是最自然的表达方式。更自然的表达可能是：

因此，强化学习仍然被认为属于训练后处理的范畴，但它是最后一个主要阶段的第三部分。  

**02:10:22 - 02:10:28**  
原文：And it's a different way of training language models and usually follows as this third step.  
译文：这是一种训练语言模型的不同方法，通常作为第三步进行。  

**02:10:28 - 02:10:30**  
原文：So inside companies like OpenAI, you will start here.  
译文：所以在像OpenAI这样的公司里，你会从这里开始。  

**02:10:30 - 02:10:32**  
原文：And these are all separate teams.  
译文：这些全部是独立的团队。  

**02:10:32 - 02:10:44**  
原文：So there's a team doing data for pre training and a team doing training for pre training, and then there's a team doing all the conversation generation in a different team that is kind of doing the super rise fine tunand.  
译文：所以有一个团队负责预训练的数据，还有一个团队负责预训练的训练，然后有一个团队负责所有的对话生成，这个团队在另一个团队进行超级精细调整。 

注意：原文中“super rise fine tunand”可能是表述错误或特定术语，在常规语境下应为“super fine-tuning”，即“超级精细调整”。  

**02:10:44 - 02:10:47**  
原文：Then there will be a team for the reinforcement learning as well.  
译文：然后将有一个团队负责强化学习。  

**02:10:47 - 02:10:49**  
原文：So it's kind of like a handoff of these models.  
译文：所以这有点像这些模型的交接。  

**02:10:49 - 02:10:57**  
原文：You get your base model, then you find tuning to be an assistant, and then you go into reinforcement learning, which we'll talk about now.  
译文：你得到了你的基础模型，然后你找到微调以成为助手，接着你进入强化学习，我们现在就来谈谈这个。  

**02:10:57 - 02:10:58**  
原文：So that's kind of like the major flow.  
译文：所以这有点像主要流程。  

**02:10:58 - 02:11:02**  
原文：And so let's now focus on reinforcement learning, the last major stage of training.  
译文：现在让我们专注于强化学习，这是训练的最后一个主要阶段。  

**02:11:02 - 02:11:09**  
原文：And let me first actually motivate it and why we would want to do reinforcement learning and what it looks like on a high level.  
译文：让我首先实际动机化它，并解释我们为什么想要进行强化学习，以及它在高层面上是什么样子的。 

（注：此句中的“动机化”一词不太常用，通常我们会说“解释其动机”或“说明其原因”。如果你同意，可以调整为：“让我首先解释一下这样做的动机，以及我们为什么想要进行强化学习，它在高层面上是什么样子的。”）  

**02:11:09 - 02:11:18**  
原文：So I would now like to try to motivate the reinforcement learning stage and what it corresponds to with something that you're probably familiar with, and that is basically going to school.  
译文：所以现在我想尝试用一个你可能熟悉的概念 来解释强化学习阶段及其对应的关系， 这个概念基本上就是去上学。  

**02:11:18 - 02:11:26**  
原文：So just like you went to school to become really good at something, we want to take large language models through school.  
译文：所以，就像你去学校学习以擅长某件事一样，我们希望让大型语言模型也接受学校的训练。  

**02:11:26 - 02:11:34**  
原文：And really what we're doing is where we have a few paradigms of ways of giving them knowledge or transferring skills.  
译文：实际上，我们所做的就是 我们有几个范例来传授他们知识或转移技能。  

**02:11:34 - 02:11:45**  
原文：So in particular, when we're working with textbooks in school, you'll see that there are three major kind of pieces of information in these textbooks, three classes of information.  
译文：所以，特别是当我们在学校使用教科书时，你会发现这些教科书中包含三类主要的信息。  

**02:11:45 - 02:11:49**  
原文：The first thing you'll see is you'll see a lot of exposition.  
译文：你首先会看到的是，你会看到大量的解释说明。  

**02:11:49 - 02:11:51**  
原文：And by the way, this is a totally random book.  
译文：顺便说一下，这是一本完全随机的书。  

**02:11:51 - 02:11:52**  
原文：I both from the Internet.  
译文：我两个都来自互联网。  

注意：原文句子结构 somewhat 不太正确，以上翻译是根据可能的意义进行的调整。 如果您需要逐字翻译或者有特定的上下文，请提供更多信息。  

**02:11:52 - 02:11:56**  
原文：I think it's some kind of organic chemistry or something, I'm not sure.  
译文：我认为这是一种有机化学之类的东西，我不确定。  

**02:11:56 - 02:12:02**  
原文：But the important thing is that you'll see that most of the text, most of it is kind of just like the meat of it is exposition.  
译文：但重要的是，你会看到大部分文本，其中大部分就像是主体内容的 exposition（解释说明）。  

（注：这里的“exposition”可以根据上下文理解为“解释说明”或“阐述”，如果需要更具体的翻译，请提供更多的上下文信息。）  

**02:12:02 - 02:12:05**  
原文：It's kind of like background knowledge, etcetera.  
译文：这有点像背景知识等。  

**02:12:05 - 02:12:10**  
原文：As you are reading through the words of this exposition, you can think of that roughly as training on that data.  
译文：当你在阅读这篇论述的文字时，你可以大致将其理解为对这些数据的训练。  

**02:12:10 - 02:12:19**  
原文：So and that's why when you're reading through this stuff, this background knowledge on all this context information, it's kind of equivalent to pre training.  
译文：所以这就是为什么当你在阅读这些内容时，所有这些背景知识和上下文信息，某种程度上等同于预训练。  

**02:12:19 - 02:12:25**  
原文：So it's where we build sort of like a knowledge base of this data and get a sense of the topic.  
译文：所以我们在这里建立了一个类似知识库的东西，对这些数据有了了解，并掌握了这个主题。  

**02:12:25 - 02:12:31**  
原文：The next major kind of information that you will see is these problems and with their worked solutions.  
译文：接下来，你会看到的主要信息类型是这些问题及其详细的解答。  

**02:12:31 - 02:12:41**  
原文：So basically, a human expert, in this case the author of this book, has given us not just a problem, but has also worked through the solution.  
译文：所以，基本上，一位人类专家，在这种情况下是这本书的作者，不仅给我们了一个问题，还详细讲解了问题的解决方案。  

**02:12:41 - 02:12:47**  
原文：And the solution is basically like equivalent to having like this ideal response for an assistant.  
译文：而解决方案基本上相当于 拥有像这种理想的助理响应。  

**02:12:47 - 02:12:55**  
原文：So it's basically the expert is showing us how to solve the problem, and it's kind of like in its full form.  
译文：所以，专家基本上是在向我们展示如何解决问题，而且是以其完整的形态展现出来的。  

**02:12:55 - 02:13:01**  
原文：So as we are reading the solution, we are basically training on the expert data.  
译文：因此，当我们阅读解决方案时，我们实际上是在专家数据上进行训练。  

**02:13:01 - 02:13:04**  
原文：And then later we can try to imitate the expert.  
译文：然后我们再试着模仿专家。  

**02:13:04 - 02:13:08**  
原文：And basically that roughly corresponds to having the sft model.  
译文：基本上这大致相当于拥有sft模型。  

**02:13:08 - 02:13:10**  
原文：That's what it would be doing.  
译文：那就是它会做的事。  

**02:13:10 - 02:13:18**  
原文：So basically, we've already done pretraining, and we've already covered this imitation of experts and how they solve these problems.  
译文：所以，基本上，我们已经完成了预训练，而且我们已经涵盖了专家 imitation 的内容，以及他们如何解决这些问题。 

注意：这里的“imitation of experts”直译为“专家的模仿”，在具体上下文中可能指的是“模仿专家（的行为或决策方式）”。如果这是技术文献的一部分，确保根据具体背景调整翻译以保证准确性。  

**02:13:18 - 02:13:22**  
原文：And the third stage of reinforcement learning is basically the practice problems.  
译文：强化学习的第三阶段基本上是练习题。  

**02:13:22 - 02:13:26**  
原文：So sometimes you'll see this is just a single practice problem here.  
译文：所以有时你会看到这里只是一个单独的练习问题。  

**02:13:26 - 02:13:31**  
原文：But of course, there will be usually many practice problems at the end of each chapter in any textbook.  
译文：但当然，任何教科书在每一章的末尾通常都会有大量的练习题。  

**02:13:31 - 02:13:37**  
原文：And practice problems, of course, we know are critical for learning, because what are they getting you to do?  
译文：当然，我们知道练习题 对于学习来说非常关键， 因为它们让你做什么？  

**02:13:37 - 02:13:42**  
原文：They're getting you to practice, to practice yourself and discover ways of solving these problems yourself.  
译文：他们让你练习，自己探索和发现解决这些问题的方法。  

**02:13:42 - 02:13:53**  
原文：And so what you get in the practice problem is you get the problem description, but you are not given the solution, but you are given the final answer, usually in the answer key of the textbook.  
译文：因此，在练习题中，你得到了问题的描述，但并没有给出解决方案，而是给出了最终答案，通常是在教科书的答案键中。  

**02:13:53 - 02:14:00**  
原文：And so you know the final answer that you're trying to get to and you have the problem statement, but you don't have the solution.  
译文：所以你知道你想要得到的最终答案，你也有了问题的陈述，但是你还没有解决方案。  

**02:14:00 - 02:14:03**  
原文：You are trying to practice the solution.  
译文：您正在尝试练习解决方案。  

**02:14:03 - 02:14:08**  
原文：You're trying out many different things and you're seeing what gets you to the final solution the best.  
译文：你正在尝试许多不同的事情，看看什么能让你最有效地达到最终解决方案。  

**02:14:08 - 02:14:12**  
原文：And so you're discovering how to solve these problems.  
译文：于是你开始发现如何解决这些问题。  

**02:14:12 - 02:14:18**  
原文：So and in the process of that, you're relying on, number one, the background information, which comes from pretraining.  
译文：所以，在这个过程中，你依赖的是，第一，背景信息，这些信息来自于预训练。  

**02:14:18 - 02:14:25**  
原文：And number two, may be a little bit of imitation of human experts, and you can probably try similar kinds of solutions and so on.  
译文：第二，可能有一点模仿人类专家， 你可以尝试类似的解决方案等等。  

**02:14:25 - 02:14:30**  
原文：So we've done this and this, and now in the section, we're going to try to practice.  
译文：所以我们已经做了这些，而现在在这一部分，我们将尝试进行练习。  

**02:14:30 - 02:14:31**  
原文：And so we're going to be given prompts.  
译文：所以我们将被给予提示。  

**02:14:31 - 02:14:38**  
原文：We're going to be given solutions, sorry, the final answers, but we're not going to be given expert solutions.  
译文：我们将被给予答案，对不起，是最终答案，但我们不会被给予专家解决方案。  

**02:14:38 - 02:14:40**  
原文：We have to practice and try stuff out.  
译文：我们必须练习并尝试一些东西。  

**02:14:40 - 02:14:42**  
原文：And that's what reinforcement learning is about.  
译文：这就是强化学习的内容。  

**02:14:42 - 02:14:51**  
原文：Okay, so let's go back to the problem that we worked with previously, just so we have a concrete example to talk through as we explore sort of the topic here.  
译文：好的，那么让我们回到之前处理的问题，这样我们在探讨这个话题时有一个具体的例子可以讨论。  

**02:14:51 - 02:14:56**  
原文：So I'm here in the tectozer because I'd also like to well, I get a text box, which is useful.  
译文：所以我在 tectozer 里，因为我也可以，嗯，我得到了一个文本框，这很有用。  

**02:14:56 - 02:15:01**  
原文：But number two, I want to remind you again that we're always working with one dimensional token sequences.  
译文：但第二点，我想再次提醒您，我们始终是在处理一维的token序列。  

**02:15:01 - 02:15:07**  
原文：And so I actually like prefer this view because this is like the native view of the llm, if that makes sense.  
译文：所以我实际上更喜欢这种视图，因为这是像llm的原生视图，如果这样理解的话。 

（注：为了使语句更通顺，可以稍微调整为：所以我实际上更喜欢这种视图，因为这更像是llm的原生视图，如果这样理解的话。）  

**02:15:07 - 02:15:09**  
原文：Like this is what it actually sees.  
译文：就像这确实是它所看到的。  

**02:15:09 - 02:15:11**  
原文：It's sees token ides, right?  
译文：它是看到令牌 ides，对吧？  

（注：原始文本似乎包含了一些不清晰或可能是拼写错误的词语，因此翻译可能不够精确。如果你能提供更多的上下文或确认原文，我可以提供更准确的翻译。）  

**02:15:11 - 02:15:15**  
原文：Okay, so Emily buys three apples and two oranges.  
译文：好的，所以艾米丽买了三个苹果和两个橙子。  

**02:15:15 - 02:15:16**  
原文：Each orange is $2.  
译文：每个橙子是2美元。  

**02:15:16 - 02:15:20**  
原文：The total cost of all the fruit is $13.  
译文：所有水果的总成本是 $13。  

**02:15:20 - 02:15:22**  
原文：What is the cost of each apple?  
译文：每个苹果的成本是多少？  

**02:15:22 - 02:15:29**  
原文：And what would I'd like you to appreciate here is these are like four possible candidate solutions as an example.  
译文：我希望你在这里注意到的是，这些就像四个可能的候选解决方案一样，仅作为示例。  

**02:15:29 - 02:15:32**  
原文：And they all reached the hazard three.  
译文：他们都达到了三级危险。  

**02:15:32 - 02:15:46**  
原文：Now what I'd like to appreciate at this point is that if I, the human data labeler, that is creating a conversation to be entered into the training set, I don't actually really know which of these conversations to add to the data set.  
译文：现在我想在此表示，如果我作为人类数据标注员，在创建要加入训练集的对话时，实际上并不真正知道应该将这些对话中的哪一个添加到数据集中。  

**02:15:46 - 02:15:51**  
原文：Some of these conversations kind of set up a system of equations.  
译文：这些对话中有一些某种程度上建立了一个方程组。  

**02:15:51 - 02:15:58**  
原文：Some of them sort of I'll just talk through it in English, and some of them just kind of like skip right through to the solution.  
译文：其中一些我将用英语简单解释一下，而有些则直接跳到解决方案。  

**02:15:58 - 02:16:14**  
原文：If you look at chacpt, for example, and you give it this question, it defines a system of variables, and it kind of like, does this little thing what we have to appreciate and differentiate between those is the first purpose of a solution is to reach the right answer.  
译文：如果你看看 chacpt，例如，你给它这个问题，它定义了一个变量系统，它有点像做这个小事情，我们必须欣赏和区分这些，因为解决方案的第一个目的是达到正确的答案。 

注意：原文中“chacpt”看起来像是拼写错误或特定上下文中的术语，如果它是特定名称或者有特殊含义，请确认其正确性以便更准确地翻译。  

**02:16:14 - 02:16:16**  
原文：Of course, we want to get the final answer.  
译文：当然，我们想要得到最终答案。  

**02:16:16 - 02:16:18**  
原文：Three, that is the important purpose here.  
译文：三，这就是这里的重要目的。  

**02:16:18 - 02:16:35**  
原文：But there's kind of like a secondary purpose as well, where here we are also just kind of trying to make it look nice for the human because we're kind of assuming that the person wants to see the solution, they want to see the intermediate steps, we want to present it nicely etc..  
译文：但这里也有次要目的，  
在这里我们也在尝试让它看起来对人类用户更友好，  
因为我们假设这个人想要看到解题过程，  
他们想要看到中间步骤，  
我们希望以一种美观的方式呈现等等。  

**02:16:35 - 02:16:38**  
原文：So there are two separate things going on here.  
译文：所以这里有两个独立的事情在进行。  

**02:16:38 - 02:16:40**  
原文：Number one is the presentation for the human.  
译文：第一项是人类的展示。  

**02:16:40 - 02:16:44**  
原文：But number two, we're trying to actually get the right answer.  
译文：但第二，我们实际上是在努力得到正确的答案。  

**02:16:44 - 02:16:57**  
原文：So let's for the moment focus on just reaching the final answer only if we only care about the final answer, then which of these is the optimal or like the best prompt, sorry, the best solution for the llm to reach the right answer.  
译文：所以让我们现在只专注于得出最终答案，如果我们只关心最终答案，那么这些选项中哪一个是最优的，或者说哪个是最佳的提示，抱歉，是让llm达到正确答案的最佳解决方案。  

**02:16:57 - 02:17:02**  
原文：And what I'm trying to get at is we don't know me as a human labeler.  
译文：我想说的是，我们并不了解我这个人类标签者。  

**02:17:02 - 02:17:05**  
原文：I would not know which one of these is best.  
译文：我不知道這些當中哪一個最好。  

**02:17:05 - 02:17:18**  
原文：So as an example, we saw earlier on when we looked at the token sequences here in the mental arithmetic and reasoning, we saw that for each token, we can only spend basically a finite number of finite amount of compute.  
译文：所以，举个例子，我们之前在查看心理算术和推理中的令牌序列时看到，对于每个令牌，我们基本上只能花费有限的计算资源。  

**02:17:18 - 02:17:21**  
原文：Here, that is not very large, or you should think about it that way.  
译文：在这里，那并不是很大，或者你应该那样考虑。  

**02:17:21 - 02:17:28**  
原文：And so we can't actually make too big of a leap in any one token is maybe the way to think about it.  
译文：因此，我们实际上不能在任何一个令牌上做出太大的跳跃，这可能是思考这个问题的方式。  

**02:17:28 - 02:17:32**  
原文：So as an example in this one, what's really nice about it is that it's very few tokens.  
译文：所以在这个例子中，很好之处在于它使用的令牌非常少。  

**02:17:32 - 02:17:36**  
原文：So it's going to take us a very short amount of time to get to the answer.  
译文：所以我们将用非常短的时间就能得到答案。  

**02:17:36 - 02:17:46**  
原文：But right here, when we're doing 30 minus four, divide three equals, right in this token here, we're actually asking for a lot of computation to happen on that single individual token.  
译文：但在这里，当我们进行 30 减去四，除以三等于，在这个符号中，实际上我们要求在这个单独的符号上进行大量的计算。  

**02:17:46 - 02:17:58**  
原文：And so maybe this is a bad example as a gift to the llm because it's kind of incentivizing it to skip through the calculations very quickly and it's going to actually make up mistakes, make mistakes in its mental arithmetic.  
译文：也许这作为一个给语言模型的礼物来说是个不好的例子，因为它有点激励模型非常快速地跳过计算过程，这样它实际上会编造错误，在心算中出错。  

**02:17:58 - 02:18:04**  
原文：So maybe it would work better to like out the spread it out more, and maybe it would be better to set up as an equation.  
译文：所以也许把它更分散一些会更好，也许设置成一个等式会更好。  

**02:18:04 - 02:18:06**  
原文：Maybe it would be better to talk through it.  
译文：也许最好还是把它谈清楚。  

**02:18:06 - 02:18:07**  
原文：We fundamentally don't know.  
译文：我们根本不知道。  

**02:18:07 - 02:18:20**  
原文：And we don't know because what is easy for you or I or as human labelers, what's easy for us or hard for us is different than what's easy or hard for the llm is cognition is different.  
译文：而且我们不知道，因为对你或我或者作为人类标注者来说简单的事情，对我们来说简单或困难的事情与对大型语言模型（LLM）来说简单或困难的事情是不同的，因为认知方式不同。  

**02:18:20 - 02:18:25**  
原文：And the token sequences are kind of like different, hard for it.  
译文：而且令牌序列有点像不同，这对它来说很难。  

**02:18:25 - 02:18:32**  
原文：And so some of the token sequences here that are trivial for me might be very too much of a leap for the llm.  
译文：因此，这里对我而言微不足道的一些 token 序列，对于大语言模型（LLM）来说可能过于复杂。  

**02:18:32 - 02:18:35**  
原文：So right here, this token would be way too hard.  
译文：所以在这里，这个令牌会难得多。  

**02:18:35 - 02:18:43**  
原文：But conversely, many of the tokens that I'm creating here might be just trivial to the llm and we're just wasting tokens.  
译文：但反过来说，我在这里创建的许多令牌对大型语言模型（LLM）可能只是微不足道的，我们只是在浪费令牌。  

**02:18:43 - 02:18:46**  
原文：Like why waste all these tokens when this is all trivial?  
译文：像这样为什么浪费所有这些令牌，而这些都是微不足道的？  

**02:18:46 - 02:18:58**  
原文：So if the only thing we're care about is reaching the final answer and we're separating out the issue of the presentation to the human, then we don't actually really know how to annotate this example.  
译文：所以，如果我们唯一关心的是达到最终答案，并且我们将呈现给人类的问题分开处理，那么我们实际上并不知道如何为这个例子添加注释。  

**02:18:58 - 02:19:02**  
原文：We don't know what solution to get to the llm because we are not the llm.  
译文：我们不知道如何解决.llm的问题，因为我们并不是.llm。 

注意：这里的“llm”可能是特定术语或缩写，在不通晓具体背景的情况下直接进行了字面翻译。如果“llm”有特定含义，请提供更多信息以便准确翻译。  

**02:19:02 - 02:19:11**  
原文：And it's clear here in the case of the math example, but this is actually like a very pervasive issue, like for our knowledge is not llms knowledge.  
译文：在数学例子中这里很清楚，但这实际上是一个非常普遍的问题，比如我们的知识并不等同于LLMS（大型语言模型系统）的知识。  

**02:19:11 - 02:19:16**  
原文：Like the llm actually has a ton of knowledge of PhD in math and physics, chemistry and whatnot.  
译文：像这个大型语言模型实际上拥有大量的数学、物理、化学等领域的博士知识。  

**02:19:16 - 02:19:23**  
原文：So in many ways, it actually knows more than I do, and I'm potentially not utilizing that knowledge in its problem solving.  
译文：所以在很多方面，它实际上知道的比我多， 我可能没有充分利用它的知识来解决问题。  

**02:19:23 - 02:19:31**  
原文：But conversely, I might be injecting a bunch of knowledge in my solutions that the other one doesn't know in its parameters.  
译文：但相反地，我可能会在我的解决方案中注入大量知识，而这些知识在另一个的参数中并不存在。  

**02:19:31 - 02:19:36**  
原文：And then those are like sudden leaps that are very confusing to the model.  
译文：然后这些就像是使模型非常困惑的突然跳跃。  

**02:19:36 - 02:19:39**  
原文：And so our cognitions are different.  
译文：因此，我们的认知是不同的。  

**02:19:39 - 02:19:48**  
原文：And I don't really know what to put here if all we care about is they're reaching the final solution and doing it economically ideally.  
译文：而且如果我们只关心他们是否能达到最终解决方案，并且以最经济的方式实现，我真的不知道这里应该写什么。  

**02:19:48 - 02:19:59**  
原文：And so long story short, we are not in a good position to create these token sequences for the lm, and they're useful by imitation to initialize the system.  
译文：长话短说，我们处于一个不太有利的位置来为语言模型创建这些令牌序列，而且通过模仿这些令牌序列来初始化系统是有用的。  

**02:19:59 - 02:20:03**  
原文：But we really want the llm to discover the token sequences that work for it.  
译文：但我们确实希望大型语言模型能够发现适用于它的token序列。  

**02:20:03 - 02:20:16**  
原文：We need to find it needs to find for itself what token sequence reliably gets to the answer given the prompt and needs to discover that in a process of reinforcement learning and of trial and error.  
译文：我们需要找到一种方法，让它能够自行发现，在给定提示的情况下，什么样的token序列可以可靠地得到答案，并且这个发现过程需要通过强化学习和试错来完成。  

**02:20:16 - 02:20:20**  
原文：So let's see how this example would work like in reinforcement learning.  
译文：那么让我们看看这个例子在强化学习中会如何运作。  

**02:20:20 - 02:20:24**  
原文：Okay, so we're now back in the hugging face inference playground.  
译文：好的，我们现在回到了Hugging Face推理游乐场。  

**02:20:24 - 02:20:29**  
原文：And that just allows me to very easily call different kinds of models.  
译文：这仅仅使我能够非常轻松地调用不同类型的模型。  

**02:20:29 - 02:20:34**  
原文：So as an example here on the top right, I chose the gemat 22 billion primer model.  
译文：所以，如右上方的示例所示，我选择了gemat 22亿个参数的模型。  

**02:20:34 - 02:20:36**  
原文：So 2 billion is very, very small.  
译文：所以20亿是非常非常小的。  

**02:20:36 - 02:20:38**  
原文：So this is a tiny model, but it's okay.  
译文：所以这是一个很小的模型，但没关系。  

**02:20:38 - 02:20:45**  
原文：So we're going to give it the way that reinforcement learning will basically work is actually quite simple.  
译文：所以我们来介绍一下强化学习的工作原理，其实非常简单。  

**02:20:45 - 02:20:51**  
原文：We need to try many different kinds of solutions, and we want to see which solutions work well or not.  
译文：我们需要尝试许多不同的解决方案，并且我们想知道哪些解决方案效果好，哪些不好。  

**02:20:51 - 02:20:54**  
原文：So we're basically going to take the prompt.  
译文：所以，我们基本上会采用这个提示。  

**02:20:54 - 02:21:00**  
原文：We're going to run the model, and the model generates a solution, and then we're going to inspect a solution.  
译文：我们将运行该模型，模型会生成一个解决方案，然后我们将检查这个解决方案。  

**02:21:00 - 02:21:04**  
原文：And we know that the correct answer for this one is $3.  
译文：我们知道这个的正确答案是 $3。  

**02:21:04 - 02:21:06**  
原文：And so indeed, the model gets it correct.  
译文：确实如此，模型答对了。  

**02:21:06 - 02:21:07**  
原文：It says it's $3.  
译文：它说它是3美元。  

**02:21:07 - 02:21:08**  
原文：So this is correct.  
译文：所以这是正确的。  

**02:21:08 - 02:21:10**  
原文：So that's just one attempt at the solution.  
译文：所以这只是一个解决方案的尝试。  

**02:21:10 - 02:21:13**  
原文：So now we're going to delete this and we're going to rerun it again.  
译文：所以现在我们将删除这个，然后我们将再次重新运行它。  

**02:21:13 - 02:21:15**  
原文：Let's try a second attempt.  
译文：让我们尝试第二次。  

**02:21:15 - 02:21:18**  
原文：So the model solves it in a bit slightly different way, right?  
译文：所以模型用稍微不同的方法来解决它，对吧？  

**02:21:18 - 02:21:23**  
原文：Every single attempt will be a different generation because these models are stochastic systems.  
译文：每一次尝试都会产生不同的结果，因为这些模型是随机系统。  

**02:21:23 - 02:21:29**  
原文：Remember that every single token here, we have a probability distribution and we're sampling from that distribution.  
译文：请记住这里的每一个标记，我们都有一个概率分布，并且我们是从那个分布中进行采样的。  

**02:21:29 - 02:21:33**  
原文：So we end up kind of going down this slightly different paths.  
译文：所以我们最终走上这条稍微不同的道路。  

**02:21:33 - 02:21:37**  
原文：And so this is a second solution that also ends in the correct answer.  
译文：这就是第二种解法，最终也得到了正确答案。  

**02:21:37 - 02:21:39**  
原文：Now we're going to delete that.  
译文：现在我们将删除它。  

**02:21:39 - 02:21:40**  
原文：I'll go through time.  
译文：我将穿越时空。  

**02:21:40 - 02:21:40**  
原文：Okay.  
译文：好的。  

**02:21:40 - 02:21:44**  
原文：So again, slightly different solution, but also gets it correct.  
译文：所以，再次说明，稍微不同的解决方案，但也能得到正确的结果。  

**02:21:44 - 02:21:47**  
原文：Now we can actually repeat this many times.  
译文：现在我们实际上可以重复做很多次。  

**02:21:47 - 02:21:55**  
原文：And so in practice, you might actually sample thousands of independent solutions or even like million solutions for just a single prompt.  
译文：因此，在实际操作中，你可能会为单个提示采样数千个独立的解决方案，甚至像采样一百万个解决方案。  

**02:21:55 - 02:21:59**  
原文：And some of them will be correct and some of them will not be very correct.  
译文：其中一些将是正确的，而另一些可能不太正确。  

**02:21:59 - 02:22:05**  
原文：And basically, what we want to do is we want to encourage the solutions that lead to correct answers.  
译文：基本上，我们想要做的是 我们希望鼓励那些导向正确答案的解决方案。  

**02:22:05 - 02:22:07**  
原文：So let's take a look at what that looks like.  
译文：所以让我们来看看那是什么样子。  

**02:22:07 - 02:22:14**  
原文：So if we come back over here, here, it's kind of like a cartoon diagram of what this is looking like, but we have a prompt.  
译文：所以，如果我们回到这里，这里，这有点像这个样子的卡通图，但我们有一个提示。  

**02:22:14 - 02:22:17**  
原文：And then we've tried many different solutions in parallel.  
译文：然后我们尝试了很多不同的解决方案，平行进行。  

**02:22:17 - 02:22:27**  
原文：And some of the solutions might go well, so they get the right answer, which is in Green, and some of the solutions might go poorly and may not reach the right answer, which is red.  
译文：有些解法可能会很好，所以它们能得到正确答案，正确答案用绿色表示，而有些解法可能不太好，可能无法得到正确答案，这用红色表示。  

**02:22:27 - 02:22:32**  
原文：Now this problem here, unfortunately, is not the best example because it's a trivial prompt.  
译文：现在这个问题，不幸的是，不是最好的例子，因为它是一个琐碎的提示。  

**02:22:32 - 02:22:36**  
原文：And as we saw, even like a 2 billion parameter model always gets it right.  
译文：正如我们所见，即使是一个20亿参数的模型也总是能做对。  

**02:22:36 - 02:22:39**  
原文：So it's not the best example in that sense.  
译文：所以从这个意义上说，这并不是最好的例子。  

**02:22:39 - 02:22:48**  
原文：But let's just exercise some imagination here and let's just suppose that the Green ones are good and the red ones are bad.  
译文：但是让我们在这里发挥一些想象力，假设绿色的是好的，红色的是坏的。  

**02:22:49 - 02:22:51**  
原文：Okay, so we generated 15 solutions.  
译文：好的，所以我们生成了15个解决方案。  

**02:22:51 - 02:22:53**  
原文：Only four of them got the right answer.  
译文：只有四个人答对了。  

**02:22:53 - 02:23:01**  
原文：And so now what we want to do is basically we want to encourage the kinds of solutions that relate to right answers.  
译文：现在我们想要做的是， 我们基本上是想要鼓励 那些与正确答案相关的解决方法。  

**02:23:01 - 02:23:11**  
原文：So whatever token sequences happened in these red solutions, obviously something went wrong along the way somewhere, and this was not a good path to take through the solution.  
译文：所以，无论这些红色解决方案中发生了什么样的令牌序列，显然在某个地方出了问题，这不是一个好的解决方案路径。  

**02:23:11 - 02:23:17**  
原文：And whatever token sequences there were in these Green solutions, well, things went pretty well in this situation.  
译文：而且，这些绿色解决方案中的任何令牌序列，在这种情况下，事情进展得相当顺利。  

**02:23:17 - 02:23:20**  
原文：And so we want to do more things like it in prompts like this.  
译文：因此，我们希望在类似的提示中做更多的事情。  

**02:23:20 - 02:23:27**  
原文：And the way we encourage this kind of a behavior in the future is we basically train on these sequences.  
译文：我们鼓励这种行为的方式就是在将来 我们会基本上对这些序列进行训练。  

**02:23:27 - 02:23:31**  
原文：But these training sequences now are not coming from expert to human annotators.  
译文：但这些训练序列现在并不是来自专家对人类标注者的。  

**02:23:31 - 02:23:34**  
原文：There's no human who decided that this is the correct solution.  
译文：没有人类决定这是正确的解决方案。  

**02:23:34 - 02:23:36**  
原文：This solution came from the model itself.  
译文：此解决方案来自模型本身。  

**02:23:36 - 02:23:38**  
原文：So the model is practicing here.  
译文：所以模型在这里进行练习。  

**02:23:38 - 02:23:40**  
原文：It's tried out a few solutions.  
译文：它已经尝试了几种解决方案。  

**02:23:40 - 02:23:42**  
原文：Four of them seem to have worked.  
译文：其中四个似乎已经奏效。  

**02:23:42 - 02:23:44**  
原文：And now the model will kind of like train on them.  
译文：现在模型将基于它们进行训练。  

**02:23:44 - 02:23:51**  
原文：And this corresponds to a student basically looking at their solutions and being like, okay, well, this one worked really well.  
译文：这相当于一个学生基本上看他们的解决方案，然后觉得，好吧，这个方案确实很好。  

**02:23:51 - 02:23:55**  
原文：So this is how I should be solving these kinds of problems.  
译文：所以，我应该这样解决这类问题。  

**02:23:55 - 02:24:00**  
原文：And here in this example, there are many different ways to actually like really tweak the methodology a little bit here.  
译文：在這個例子中，這裡有許多不同的方法可以真正地對方法進行一些微調。  

**02:24:00 - 02:24:09**  
原文：But just to give the core idea across, maybe it's simpas to just think about take the taking the single best solution out of these four, like say, this one, that's why it was yellow.  
译文：但为了传达核心思想，也许简单考虑一下从这四个中取出单一最佳解决方案会比较好，比如说，这个，这就是为什么它是黄色的。  

**02:24:09 - 02:24:23**  
原文：So this is the solution that not only looked the right answer, but many maybe had some other nice properties, maybe it was the shortest one or it looked nicest in some ways or there's other criteria you could think of as an example.  
译文：所以这是一个不仅看起来是正确答案的解决方案，而且可能还具有一些其他不错的特性，也许它是其中最短的，或者在某些方面看起来是最美观的，或者其他你可以想到的标准作为例子。  

**02:24:23 - 02:24:27**  
原文：But we're going to decide that this the top solution, we're going to train on it.  
译文：但是我们将决定这是最佳解决方案，我们将会对其进行培训。  

**02:24:27 - 02:24:36**  
原文：And then the model will be slightly more likely once you do the parameter update to take this path in this kind of a setting in the future.  
译文：然后，模型在进行参数更新后，在这种设置中将来会稍微更倾向于选择这条路径。  

**02:24:36 - 02:24:45**  
原文：But you have to remember that we're going to run many different diverse prompts across lots of math problems and physics problems and whatever there might be.  
译文：但你必须记住，我们将运行许多不同的提示，涵盖大量的数学问题、物理问题等。  

**02:24:45 - 02:24:51**  
原文：So tens of thousands of prompts maybe have in mind there's thousands of solutions per prompt.  
译文：所以成千上万的提示可能心中有数，每个提示都有成千上万的解决方案。  

**02:24:51 - 02:24:54**  
原文：And so this is all happening kind of like at the same time.  
译文：所以这一切都像是在同一时间发生的。  

**02:24:54 - 02:25:04**  
原文：And as we're iterating this process, the model is discovering for itself what kinds of token sequences lead to correct answers.  
译文：在我们迭代这个过程时，模型本身正在发现什么样的 token 序列会导致正确的答案。  

**02:25:04 - 02:25:06**  
原文：It's not coming from a human annotator.  
译文：它不是来自人类标注者。  

**02:25:06 - 02:25:12**  
原文：The model is kind of like playing in this playground and it knows what it's trying to get to.  
译文：这个模型有点像在这个游乐场里玩耍，而且它知道它在尝试到达什么目标。  

**02:25:12 - 02:25:16**  
原文：And it's discovering sequences that work for it.  
译文：并且它在发现适用于它的序列。  

**02:25:16 - 02:25:19**  
原文：These are sequences that don't make any mental leaps.  
译文：这些都是不会产生任何思维跳跃的序列。  

**02:25:19 - 02:25:26**  
原文：They seem to work reliably and statistically and fully utilize the knowledge on the model as it has it.  
译文：它们似乎能够可靠地、统计性地工作，并且充分利用模型所拥有的知识。  

**02:25:26 - 02:25:30**  
原文：And so this is the process of reinforcement learning.  
译文：这就是强化学习的过程。  

**02:25:30 - 02:25:32**  
原文：It's basically a guess and check.  
译文：这基本上是一个猜测和检查的过程。  

**02:25:32 - 02:25:35**  
原文：We're going to guess many different types of solutions.  
译文：我们将猜测许多不同类型的解决方案。  

**02:25:35 - 02:25:42**  
原文：We're going to check them, and we're going to do more of what worked in the future, and that is reinforcement learning.  
译文：我们将要检查它们，并且我们将在未来做更多有效的事情，那就是强化学习。  

**02:25:42 - 02:25:53**  
原文：So in the context of what came before, we see now that the sft t model, the supervised fine tunmodel, it's still helpful because it's still kind of like initializes the model a little bit into the vicinity of the correct solutions.  
译文：所以在之前的背景下，我们现在看到，监督微调模型（sft t model）仍然有用，因为它还是将模型初始化到正确解的附近。  

**02:25:53 - 02:26:05**  
原文：So it's kind of like a initialization of the model in the sense that it kind of gets the model to you know take solutions like write out solutions, and maybe it has an understanding of setting up a system of equations.  
译文：所以这有点像是模型的初始化，意思是它能够让模型开始生成解决方案，比如写出解决方案，也许它对建立方程组有一定的理解。  

**02:26:05 - 02:26:10**  
原文：Or maybe it kind of like talks for a solution, so it gets you into the vicinity of correct solutions.  
译文：或者可以说它在寻找解决方案， 所以它能让你接近正确的解决方案。  

**02:26:10 - 02:26:13**  
原文：But reinforcement learning is where everything gets dialed in.  
译文：但强化学习是所有东西都得到调整的地方。  

**02:26:13 - 02:26:21**  
原文：We really discover the solutions that work for the model, get the right answers, we encourage them, and then the model just kind of like gets better over time.  
译文：我们确实找到了适用于模型的解决方案，得到了正确的答案，我们鼓励这些，然后模型就会随着时间的推移逐渐变得更好。  

**02:26:21 - 02:26:21**  
原文：Okay.  
译文：好的。  

**02:26:21 - 02:26:25**  
原文：So that is the high level process for how we train larger language models.  
译文：这就是我们训练更大语言模型的高层次过程。  

**02:26:25 - 02:26:29**  
原文：In short, we train them kind of very similar to how we train children.  
译文：简而言之，我们训练他们的方式 与训练孩子的方式很相似。  

**02:26:29 - 02:26:39**  
原文：And basically the only difference is that children go through chapters of books and they do all these different types of training exercises kind of within a chapter of each book.  
译文：基本上的唯一区别是孩子们 会经历书中的各个章节， 并且在每一章中他们要做很多种不同的训练．  

**02:26:39 - 02:26:45**  
原文：But instead, when we train ais, it's almost like we kind of do it stage by stage, depending on the type of that stage.  
译文：但相反，当我们训练AI时，几乎像是我们根据阶段的类型一步一步地进行。  

**02:26:45 - 02:26:53**  
原文：So first, what we do is we do pre training, which as we saw, is equivalent to basically reading all the explicitory material.  
译文：所以首先，我们进行预训练，就像我们看到的那样，这相当于基本上阅读所有的说明性材料。  

**02:26:53 - 02:27:00**  
原文：So we look at all the textbooks at the same time, and we read all the exposition and we try to build a knowledge base.  
译文：所以我们同时查看所有教科书，阅读所有的阐述，并尝试建立一个知识库。  

**02:27:00 - 02:27:24**  
原文：The second thing then is we go into the St stage, which is really looking at all the fixed sort of like solutions from human experts of all the different kinds of worked solutions across all the textbooks, and we just kind of get an sat model which is able to imitate the experts, but thus, so kind of blindly, it just kind of like does its best guess to kind of just like trying to mimic statistically the expert behavior.  
译文：第二件事是然后我们进入St阶段，这个阶段实际上是审视所有来自人类专家的固定解决方案，这些方案涵盖了所有教科书中的各种解题方法。我们建立了一个类似sat模型，该模型能够模仿专家的行为，但这种模仿是盲目的，它只是尽力猜测，试图在统计上模仿专家的行为。  

**02:27:24 - 02:27:28**  
原文：And so that's what you get when you look at all the word solutions.  
译文：所以这就是当你查看所有单词解决方案时得到的结果。  

**02:27:28 - 02:27:38**  
原文：And then finally, in the last stage, we do all the practice problems in the rl stage, across all the textbooks, we only do the practice problems, and that's how we get the rl model.  
译文：然后最后，在最后一个阶段，我们在强化学习（rl）阶段做所有的练习题，涵盖所有教材，我们只做练习题，这就是我们如何获得强化学习（rl）模型的。  

**02:27:38 - 02:27:45**  
原文：So on a high level, the way we train elms is very much equivalent to the process that we use for training of children.  
译文：所以从高层角度来看，我们训练 elm 的方式与我们训练孩子的方式非常相似。请注意，这里的“elms”可能是指某种模型或系统，在没有更多上下文的情况下，默认将其翻译为“elm”，如果它有特定含义或指代，请提供更多信息以便准确翻译。 若要使翻译更自然，可以考虑如下调整：

所以从宏观角度来看，我们训练 Elm 的方式与训练孩子的方式非常相似。 

如果有更多上下文信息，可以进一步优化翻译。  

**02:27:45 - 02:27:57**  
原文：The next point I would like to make is that actually these first two stages, pre training and surprise fine tuning, they've been around for years and they are very standard and everyone does them, all the different element providers.  
译文：我接下来想说的是，实际上这两个阶段，预训练和意外微调，已经存在了很多年，而且它们非常标准，所有不同的要素提供者都会这样做。  

**02:27:57 - 02:28:05**  
原文：It is this last stage, the rl training, that is a lot more early in its process of development and is not standard yet in the field.  
译文：正是这个最后阶段，即强化学习（rl）训练，在其发展过程中还处于相对较早的阶段，在该领域尚未成标准。  

**02:28:05 - 02:28:08**  
原文：And so this stage is a lot more kind of early and nascent.  
译文：所以这个阶段要早得多，也更原始。  

**02:28:08 - 02:28:14**  
原文：And the reason for that is because I actually skipped over a ton of little details here in this process.  
译文：原因是我实际上在这个过程中跳过了一大堆小细节。  

**02:28:14 - 02:28:30**  
原文：The high level idea has very simple trial and error learning, but there's a ton of details and little mathematical kind of like nuances to exactly how you pick the solutions that are the best and how much you train on them and what is the prompt distribution and how to set up the training run such that this actually works.  
译文：高层次的想法非常简单，就是尝试和错误的学习，但其中有许多细节和细微的数学 nuances，具体涉及到如何挑选最佳解决方案、对这些方案进行多少训练、提示的分布是怎样的，以及如何设置训练过程以确保这种方法能够奏效。  

**02:28:30 - 02:28:35**  
原文：There's a lot of little details and knobs to the core idea that is very, very simple.  
译文：这个核心想法非常非常简单，  
但其中有很多小的细节和调整。  

（注：为了保持语句通顺，稍微调整了语序，但保留了原始格式和意思。）  

**02:28:35 - 02:28:38**  
原文：And so getting the details right here is not trivial.  
译文：因此，这里正确处理细节并非 trivial。  

注：在中文中，“trivial”通常翻译为“琐碎的”或“无关紧要的”，但根据上下文，这里可能更合适表达为“并非 trivial”，以强调其重要性。如果你有具体的上下文，可以进一步调整翻译。  

**02:28:38 - 02:28:51**  
原文：And so a lot of companies like, for example, opening eye and other llm providers have experimented internally with reinforcement learning fine tuning for llms for a while, but they've not talked about it publicly.  
译文：因此，像 Opening Eye 以及其他的大型语言模型提供商这样的公司已经在内部实验了一段时间的强化学习微调技术，但他们并没有公开讨论过这一点。  

**02:28:51 - 02:28:53**  
原文：It's all condone inside the company.  
译文：公司内部都默许了。  

**02:28:53 - 02:29:03**  
原文：And so that's why the paper from deep seek that came out very, very recently was such a big deal, because this is a paper from this company called deep sea ki in China.  
译文：所以这就是为什么最近由一家名为深海觅（Deep Seek）的中国公司发布的论文如此重要。  

**02:29:03 - 02:29:18**  
原文：And this paper really talked very publicly about reinforcement learning fine training for large language models and how incredibly important it is for large language models and how it brings out a lot of reasoning capabilities in the models.  
译文：并且这篇论文非常公开地讨论了针对大型语言模型的强化学习微调，以及它对于大型语言模型的重要性，还有它是如何在模型中激发出大量的推理能力的。  

**02:29:18 - 02:29:20**  
原文：We'll go into this in a second.  
译文：我们将在一秒钟后进入这个话题。  

**02:29:20 - 02:29:33**  
原文：So this paper reinvigorated the public interest of using rl for land, gave a lot of the certain degree d details that are needed to reproduce the results and actually get the stage to work for electritroelectric models.  
译文：所以这篇文章重新激发了公众对使用强化学习（RL）进行土地利用的兴趣，提供了大量重现结果所需的细节，并实际使该阶段能够为电模型工作。 

注：原文中“electritroelectric”看起来像是拼写错误或非标准术语，在翻译中我将其理解为“电”模型，如果您有更具体的背景信息，请告知以便更准确地翻译。  

**02:29:33 - 02:29:41**  
原文：So let me take you briefly through this deep secar on paper and what happens when you actually correctly apply rl to language models and what that looks like and what that gives you.  
译文：那么让我简要地带您了解一下这篇关于在纸上正确应用强化学习到语言模型的深入研究，以及实际正确应用时的情况和效果。  

**02:29:41 - 02:29:49**  
原文：So the first thing I'll scroll to is this kind of figure two here, where we are looking at the improvement in how the models are solving mathematical problems.  
译文：所以我首先会滚动到这里的第二个图表，我们在这里看的是模型在解决数学问题上的改进情况。  

**02:29:49 - 02:29:53**  
原文：So this is the accuracy of solving mathematical problems on the ame, accuracy.  
译文：所以这就是在同一个问题上解数学问题的准确性。  

注：原句子结构 somewhat 不清晰，尝试保持原意进行了翻译。如果需要更通顺的表达，请确认上下文或提供更多背景信息。  

**02:29:53 - 02:30:01**  
原文：And then we can go to the web page and we can see the kinds of problems that are actually in these kinds of math problems that are being measured here.  
译文：然后我们可以去网页上看，我们可以看到这里实际测量的数学问题的类型。  

**02:30:01 - 02:30:02**  
原文：So these are simple math problems.  
译文：所以这些都是简单的数学问题。  

**02:30:02 - 02:30:08**  
原文：You can pause the video if you like, but these are the kinds of problems that basically the models are being asked to solve.  
译文：如果你愿意，可以暂停视频，但这些就是模型被要求解决的问题类型。  

**02:30:08 - 02:30:11**  
原文：And you can see that in the beginning, they're not doing very well.  
译文：你可以看到最初的时候，他们的表现并不是很好。  

**02:30:11 - 02:30:16**  
原文：But then as you update the model with this many thousands of steps, their accuracy kind of continues to climb.  
译文：但随后，当你用这数千个步骤更新模型时，它们的准确性会继续提高。  

**02:30:16 - 02:30:28**  
原文：So the models are improving, and they're solving these problems with a higher accuracy as you do this trial and error on a large data set of these kinds of problems, and the models are discovering how to solve math problems.  
译文：因此，这些模型正在改进，它们通过在大量此类问题的数据集上进行试错，以更高的准确性解决这些问题，而且模型正在学会如何解决数学问题。  

**02:30:28 - 02:30:38**  
原文：But even more incredible than the quantitative kind of results of solving these problems with a higher accuracy is the qualitative means by which the model achieves these results.  
译文：但是，比以更高准确性解决这些问题的定量结果更令人惊讶的是，模型取得这些结果的定性方法。  

**02:30:38 - 02:30:49**  
原文：So when we scroll down, one of the figures here that is kind of interesting is that later on in the optization, the model seems to be using average length per response goes up.  
译文：所以当我们向下滚动时，这里有一个有趣的数字是，在优化过程的后期，模型似乎在使用平均每条响应的长度增加了。  

**02:30:49 - 02:30:53**  
原文：So the model seems to be using more tokens to get its higher accuracy results.  
译文：所以该模型似乎是在使用更多的 token 来获得其更高的准确率结果。  

**02:30:53 - 02:30:56**  
原文：So it's learning to create very, very long solutions.  
译文：所以它在学习创建非常非常长的解决方案。  

**02:30:56 - 02:30:58**  
原文：Why are these solutions very long?  
译文：为什么这些解决方案非常长？  

**02:30:58 - 02:31:01**  
原文：We can look at them qualitatively here.  
译文：我们可以在这里定性地看一下它们。  

**02:31:01 - 02:31:21**  
原文：So basically, what they discover is that the model solutions get very, very long, partially because so here's a question, and here's kind of the answer from the model, what the model learns to do, and this is an emergent property of the optimization, it just discovers that this is good for problem solving, is it starts to do stuff like this.  
译文：所以，基本上，他们发现模型的解决方案变得非常非常长，部分原因是这样的：这里有一个问题，这是模型给出的答案，也就是模型学会做的事情。这是一个优化过程中的 emergent property（突现属性），它发现这对解决问题很有帮助，于是它开始做这种事情。  

**02:31:21 - 02:31:21**  
原文：Wait, wait, wait.  
译文：等一下，等一下，等一下。  

**02:31:21 - 02:31:23**  
原文：That's not ha, moment I can flag here.  
译文：这不是哈哈，我可以在这里标记一下。  

**02:31:23 - 02:31:27**  
原文：Let's reevaluate this step by step to identify the correct sum can be.  
译文：让我们一步一步重新评估以确定正确的总和可能是多少。  

**02:31:27 - 02:31:29**  
原文：So what is the model doing here?  
译文：那么这里的模型在做什么呢？  

**02:31:29 - 02:31:29**  
原文：Right?  
译文：对吧？  

**02:31:29 - 02:31:31**  
原文：The model is basically reevaluating steps.  
译文：该模型基本上是在重新评估步骤。  

**02:31:31 - 02:31:46**  
原文：It has learned that it works better for accuracy to try out lots of ideas, try something from different prime perspectives, retrace, reframe, backtrack, is doing a lot of the things that you and I are doing in the process of problem solving for mathematical questions.  
译文：它已经了解到，为了提高准确性，尝试许多想法，从不同的主要角度尝试一些东西，回溯、重构、倒退，正在做很多你和我在解决数学问题的过程中所做的事。 

（注：为了使语句更符合中文表达习惯，对原文的结构进行了略微调整，但保持了原意和格式。）  

**02:31:46 - 02:31:50**  
原文：But it's rediscovering what happens in your head, not what you put down on the solution.  
译文：但它是在重新发现你脑袋里发生了什么，而不是你写在解决方案上的内容。  

**02:31:50 - 02:31:54**  
原文：And there is no human who can harcode this stuff in the ideal assistant response.  
译文：而且没有人能够将这些内容硬编码到理想的助手响应中。  

**02:31:54 - 02:32:01**  
原文：This is only something that can be discovered in the process of reinforcement learning, because you wouldn't know what to put here.  
译文：这只有在强化学习的过程中才能被发现，因为你不会知道这里应该放什么。  

**02:32:01 - 02:32:05**  
原文：This just turns out to work for the model, and it improves accuracy in problem solving.  
译文：这刚好适用于该模型，且能提高解决问题的准确性。  

**02:32:05 - 02:32:12**  
原文：So the model learns what we call these chains of thought in your head, and it's an emergent property of the optimization.  
译文：所以模型学会了我们所称的这些思维链，它是优化过程中的一个涌现属性。  

**02:32:12 - 02:32:19**  
原文：And that's what's bloating up the response lens, but that's also what's increasing the accuracy of the problem solving.  
译文：这就是 what's bloating up the response lens，但这也是在提高解决问题的准确性。  

注：此处“what's bloating up the response lens”部分似乎是一个比喻或特定表达，直译可能不太通顺，根据上下文可能需要进一步调整以确保意思准确传达。  

**02:32:19 - 02:32:23**  
原文：So what's incredible here is basically the model is discovering ways to think.  
译文：所以这里最神奇的地方在于，模型实际上是在发现思考的方式。  

**02:32:23 - 02:32:43**  
原文：It's learning what I like to call cognitive strategies of how you manipulate a problem and how you approach it from different perspectives, how you pull in some analogies or do different kinds of things like that, and how you kind of try out many different things over time, check a result from different perspectives and how you kind of solve problems.  
译文：它是学习我称之为认知策略， 关于你如何处理一个问题， 以及如何从不同角度来解决它， 如何引用一些类比 或者采用不同的方式之类的东西， 以及如何在一段时间内尝试许多不同的方法， 从不同角度检查结果， 进行问题的解决。  

**02:32:43 - 02:32:45**  
原文：But here it's kind of discovered by the rl.  
译文：但在这里，它被rl发现了。  

**02:32:45 - 02:32:50**  
原文：So extremely incredible to see this emerge in the optimization without having to hard Coit anywhere.  
译文：所以在优化过程中看到这一点出现是极其不可思议的，而不需要在任何地方强行加入。 

注意：原文中的 "Coit" 可能是拼写错误或特定术语，根据上下文我推测可能是 "code" 或其他单词。如果 "Coit" 是特定名称或有特殊含义，请您进一步澄清。  

**02:32:50 - 02:32:57**  
原文：The only thing we've given it are the correct answers, and this comes out from trying to just solve them correctly, which is incredible.  
译文：我们唯一给它的就是正确答案， 而这是它试图正确解答问题的产出， 真的是太不可思议了。  

**02:32:57 - 02:33:08**  
原文：Now let's go back to actually the problem that we've been working with and let's take a look at what it would look like for this kind of a model, what we call reasoning or thinking model, to solve that problem.  
译文：现在让我们回到我们一直在处理的问题，看看这种我们称之为推理或思考模型来解决这个问题会是什么样子。  

**02:33:08 - 02:33:09**  
原文：Okay.  
译文：好的。  

**02:33:09 - 02:33:12**  
原文：So recall that this is the problem we've been working with.  
译文：所以回想一下，这是我们一直在处理的问题。  

**02:33:12 - 02:33:16**  
原文：And when I pasted it into ChatGPT four zero, I'm getting this kind of a response.  
译文：当我将其粘贴到 ChatGPT 四零时，我得到了这样的回复。  

**02:33:16 - 02:33:23**  
原文：Let's take a look at what happens when you give this same query to what's called a reasoning or a thinking model.  
译文：让我们来看看当你把这个相同的查询给予所谓的推理或思考模型时会发生什么。  

**02:33:23 - 02:33:26**  
原文：This is a model that was trained with reinforcement learning.  
译文：这是一个使用强化学习训练的模型。  

**02:33:26 - 02:33:32**  
原文：So this model described in this paper, deep c car one, is available on chat dot deep c dot com.  
译文：所以这篇论文中描述的模型，Deep C Car One，在 chat.deepc.com 上可用。  

**02:33:32 - 02:33:36**  
原文：So this is kind of like the company that developed it is hosting it.  
译文：所以这有点像开发它的公司正在托管它。  

**02:33:36 - 02:33:42**  
原文：You have to make sure that the deep think button is turned on to get the R one model as it's called.  
译文：您必须确保深度思考按钮已打开，以获得所谓的R1型号。  

**02:33:42 - 02:33:44**  
原文：We can paste it here and run it.  
译文：我们可以将其粘贴在这里并运行它。  

**02:33:44 - 02:33:49**  
原文：And so let's take a look at what happens now and what is the output of the model.  
译文：那么，让我们来看看现在发生了什么，以及模型的输出是什么。  

**02:33:49 - 02:33:51**  
原文：Okay, so here's what it says.  
译文：好的，它是这么说的。  

**02:33:51 - 02:33:57**  
原文：So this is previously what we get using basically what's an sft approach, a supervised fine approach.  
译文：所以，这是之前我们使用基本上是SFT方法，即监督微调方法所得到的结果。  

**02:33:57 - 02:33:59**  
原文：This is like mimicking an expert solution.  
译文：这就像模仿专家的解决方案。  

**02:33:59 - 02:34:01**  
原文：This is what we get from the rl model.  
译文：这是我们从强化学习模型中得到的结果。  

**02:34:01 - 02:34:03**  
原文：Okay, let me try to figure this out.  
译文：好的，让我试着理清这个问题。  

**02:34:03 - 02:34:06**  
原文：So Emily buys three apples and two oranges each.  
译文：所以艾米丽每次买三个苹果和两个橙子。  

**02:34:06 - 02:34:06**  
原文：Orge costs two.  
译文：Orge 的价格是两个。  

（注：此处的 "Orge" 可能是指某种物品或商品，但由于上下文不明，直译为 "Orge"。如果需要更准确的翻译，请提供更多背景信息。）  

**02:34:06 - 02:34:07**  
原文：Total is 13.  
译文：总数是13。  

**02:34:07 - 02:34:08**  
原文：I need to find out.  
译文：我需要查明。  

**02:34:08 - 02:34:09**  
原文：Blah, blah, blah.  
译文：废话，废话，废话。  

**02:34:09 - 02:34:19**  
原文：So here, as you're reading this, you can't escape thinking that this model is thinking, is definitely pursuing the solution.  
译文：所以，在这里，当你读到这段话时，你无法不认为这个模型确实在思考，确实在追求解决方案。  

**02:34:19 - 02:34:21**  
原文：It derives that it must cost $3.  
译文：它得出必须花费3美元。  

**02:34:21 - 02:34:25**  
原文：And then it says, wait a second, let me check my math again to be sure.  
译文：然后它说，等一下，让我再检查一遍我的数学以确保无误。  

**02:34:25 - 02:34:28**  
原文：And then it tries it from a slightly different perspective.  
译文：然后它从稍微不同的角度尝试。  

**02:34:28 - 02:34:31**  
原文：And then it says, Yep, all that checks out.  
译文：然后它说，是的，所有这些都对得上。  

**02:34:31 - 02:34:32**  
原文：I think that's the answer.  
译文：我认为那就是答案。  

**02:34:32 - 02:34:33**  
原文：I don't see any mistakes.  
译文：我没有发现任何错误。  

**02:34:33 - 02:34:38**  
原文：Let me see if there's another way to approach the problem, maybe setting up an equation.  
译文：让我看看是否有其他方法来解决这个问题，也许可以设置一个方程。  

**02:34:38 - 02:34:42**  
原文：Let's let the cost of one apple be $8, then blah, blah, blah.  
译文：让我们假设一个苹果的价格是8元，然后 blah, blah, blah。  

**02:34:42 - 02:34:43**  
原文：Yep, same answer.  
译文：是的，答案相同。  

**02:34:43 - 02:34:44**  
原文：So definitely each apple is three.  
译文：所以每个苹果肯定是三个。 

（注：此句在逻辑上可能有误，原文直译即为这样。如果需要调整以符合中文表达习惯，请确认上下文。）  

**02:34:44 - 02:34:47**  
原文：All right, confident that that's correct.  
译文：好的，确信那是正确的。  

**02:34:47 - 02:34:53**  
原文：And then what it does once it sort of did the thinking process is it writes up the nice solution for the human.  
译文：然后，一旦它完成了思考过程， 它就会为人类写出一个很好的解决方案。  

**02:34:53 - 02:34:55**  
原文：And so this is now considering.  
译文：因此，这现在正在考虑之中。  

**02:34:55 - 02:35:06**  
原文：So this is more about the correctness aspect, and this is more about the presentation aspect, where it kind of like writes it out nicely and boxes in the correct answer at the bottom.  
译文：所以这更多的是关于正确性方面，而这更多的是关于呈现方面，它会以一种很好的方式写出内容，并在底部框出正确答案。  

**02:35:06 - 02:35:10**  
原文：And so what's incredible about this is we get this like thinking process of the model.  
译文：所以，关于这一点最神奇的地方在于，我们能够了解到模型的思考过程。  

**02:35:10 - 02:35:14**  
原文：And this is what's coming from the reinforcement learning process.  
译文：而这正是来自强化学习过程的结果。  

**02:35:14 - 02:35:17**  
原文：This is what's bloating up the length of the token sequences.  
译文：这就是使令牌序列的长度膨胀的原因。  

**02:35:17 - 02:35:19**  
原文：They're doing thinking, and they're trying different ways.  
译文：他们在进行思考，并尝试不同的方法。  

**02:35:19 - 02:35:22**  
原文：This is what's giving you higher accuracy problem solving.  
译文：这就是给你带来更高准确性问题解决的方法。  

**02:35:22 - 02:35:32**  
原文：And this is where we are seeing these aha moments and these different strategies and these ideas for how you can make sure that you're getting the correct answer.  
译文：在这里，我们看到了这些顿悟的时刻、不同的策略和如何确保得到正确答案的想法。  

**02:35:32 - 02:35:43**  
原文：The last point I wanted to make is some people are a little bit nervous about putting you very sensitive data into chat tpc dot com, because this is a Chinese company.  
译文：我想强调的最后一点是，有些人对于将非常敏感的数据输入到 chat tpc dot com 感到有些紧张，因为这是一家中国公司。  

**02:35:43 - 02:35:48**  
原文：So don't people are a little bit careful and cag with that a little bit deep, sir.  
译文：所以人们在那方面稍微小心一点，有点深奥，先生。  

（注：原句存在语法和表达上的问题，翻译时进行了适当调整以符合中文表达习惯。）  

**02:35:48 - 02:35:51**  
原文：One is a model that was released by this company.  
译文：一个是这家公司发布的一个模型。  

**02:35:51 - 02:35:54**  
原文：So this is an open source model or open weights model.  
译文：所以这是一个开源模型或开放权重模型。  

**02:35:54 - 02:35:57**  
原文：It is available for anyone to download and use.  
译文：任何人都可以下载和使用。  

**02:35:57 - 02:36:01**  
原文：You will not be able to like run it in its full sort of.  
译文：你将无法完全正常地运行它。  

**02:36:01 - 02:36:03**  
原文：The full model in full precision.  
译文：完整的模型采用全精度。  

**02:36:03 - 02:36:08**  
原文：You won't run that on a MacBook, but or like a local device because this is a fairly large model.  
译文：你不会在MacBook上运行它，或者像本地设备上运行，因为这是一个相当大的模型。  

**02:36:08 - 02:36:11**  
原文：But many companies are hosting the full largest model.  
译文：但许多公司正在托管完整的最大模型。  

**02:36:11 - 02:36:14**  
原文：One of those companies that I like to use is called together that AI.  
译文：我喜欢使用的一家公司叫做 Together AI。  

**02:36:14 - 02:36:18**  
原文：So when you go to together that AI, you sign up and you go to playgrounds.  
译文：所以当你一起去那个AI，你注册并进入 playgrounds。  

（注：原文本中“go to together”和“go to playgrounds”的表述似乎有些混乱，可能需要根据上下文调整以确保意思明确。如果你有更多背景信息或希望对句子进行润色，请告知。）  

**02:36:18 - 02:36:21**  
原文：You can select here in the chat deep pk R one.  
译文：您可以在聊天中选择深度PK R1。  

**02:36:21 - 02:36:24**  
原文：And there's many different kinds of other models that you can select here.  
译文：并且这里有很多其他不同类型的模型可供您选择。  

**02:36:24 - 02:36:26**  
原文：These are whole state of the art models.  
译文：这些是全新的最先进的模型。  

**02:36:26 - 02:36:32**  
原文：So this is kind of similar to the hugging face inference playground that we've been playing with so far.  
译文：所以这有点类似于我们迄今为止一直在使用的Hugging Face推理 playground。  

**02:36:32 - 02:36:36**  
原文：But together, that AI will usually host all the state of the art models.  
译文：但共同点是，这类人工智能通常会承载所有最先进的模型。  

**02:36:36 - 02:36:37**  
原文：So select the t car one.  
译文：所以选择 t 型车一号。  

**02:36:37 - 02:36:39**  
原文：You can try to ignore a lot of these.  
译文：您可以尝试忽略其中的很多。  

**02:36:39 - 02:36:41**  
原文：I think the default settings will often be okay.  
译文：我认为默认设置通常会没问题。  

**02:36:41 - 02:36:42**  
原文：And we can put in this.  
译文：我们可以把这放进去。  

**02:36:42 - 02:36:49**  
原文：And because the model was released by deep seek, what you're getting here should be basically equivalent to what you're getting here.  
译文：而且因为这个模型是由Deep Seek发布的，所以你在这里得到的应该基本上等同于你在这里得到的。  

**02:36:49 - 02:36:54**  
原文：Now because of the randomness in the sampling, we're going to get something slightly different.  
译文：现在由于抽样的随机性，我们得到的结果会有些不同。  

**02:36:54 - 02:37:02**  
原文：But in principle, this should be identical in terms of the power of the model, and you should be able to see the same things quantitatively and qualitatively.  
译文：但原则上，这在模型的能力上应该是一致的，你应该能够定量和定性地看到相同的结果。  

**02:37:02 - 02:37:05**  
原文：But this model is coming from kind of an American company.  
译文：但这个模型来自一家美国公司。  

**02:37:05 - 02:37:09**  
原文：So that's deep seek and that's the what's called a reasoning model.  
译文：所以这就是深度搜索，这就是所谓的推理模型。  

**02:37:09 - 02:37:12**  
原文：Now when I go back to chat, let me go to chat here.  
译文：现在当我回到聊天时，让我在这里聊天。  

**02:37:12 - 02:37:21**  
原文：Okay, so the models that you're going to see in the drop down here, some of them like zero one, zero three mini, zero three mini high etc., they are talking about uses advanced reasoning.  
译文：好的，那么你在下拉菜单中将看到的模型，其中一些像零一、零三迷你、零三迷你高配等，它们都涉及到使用高级推理。  

**02:37:21 - 02:37:34**  
原文：Now what this is referring to uses advanced reasoning is it's referring to the fact that it was trained by reinforcement learning web techniques, very similar to those of the cr one per public statements of opeye employees.  
译文：现在，这段话所指的是使用了高级推理，具体来说，它是通过强化学习网络技术进行训练的，这与欧普员工的公开声明中提到的CR技术非常相似。 

注意：原文中的一些专有名词如“cr one”, “opeye”不太明确，在没有更多背景信息的情况下，我将其按照音译处理为“CR”和“欧普”。如果这些名词有特定含义或指代，请提供更多信息以便更准确地翻译。  

**02:37:34 - 02:37:37**  
原文：So these are thinking models trained with rl.  
译文：所以这些都是用强化学习训练的思考模型。  

**02:37:37 - 02:37:45**  
原文：And these models like GPT -4 zero or GPT -4 400 mini that you're getting in the free tier, you should think of them as mostly sft models supervise fine tunmodels.  
译文：And这些模型，比如你在免费层级中获得的GPT-4 Zero或GPT-4 400 mini，你应该把它们视为主要是通过监督微调的模型（SFT models）。  

**02:37:45 - 02:37:49**  
原文：They don't actually do this like thinking, as you see in the rl models.  
译文：它们实际上并不会像你在现实模型中看到的那样进行思考。  

**02:37:49 - 02:37:57**  
原文：And even though there's a little bit of reinforcement learning involved with these models, and I'll go that into that in a second, these are mostly sat models.  
译文：即使这些模型中有一点强化学习的成分，我稍后会详细说明这一点，但主要是基于sat模型。  

**02:37:57 - 02:37:59**  
原文：I think you should think about it that way.  
译文：我认为你应该这样考虑。  

**02:37:59 - 02:38:05**  
原文：So in the same way as what we saw here, we can pick one of the thinking models like, say, zero three mini high.  
译文：所以，就像我们在这里看到的一样，我们可以选择一个思维模型，比如，零三迷你高。  

**02:38:05 - 02:38:16**  
原文：And these models, by the way, might not be available to unless you pay chagbd subscription of either dollar, $20 per month or lar, $200 per month for some of the top models.  
译文：顺便说一下，这些模型可能除非你支付订阅费否则无法使用，要么是每月20美元，要么是每月200美元，以使用一些顶级模型。  

**02:38:16 - 02:38:18**  
原文：So we can pick a thinking model and run.  
译文：所以我们可以选择一个思维模型并运行。  

**02:38:18 - 02:38:20**  
原文：Now it's going to happen here.  
译文：现在它将在这里发生。  

**02:38:20 - 02:38:23**  
原文：It's going to say reasoning, and it's going to start to do stuff like this.  
译文：它将开始进行推理，并且它将开始做类似这样的事情。  

**02:38:23 - 02:38:28**  
原文：And what we're seeing here is not exactly the stuff we're seeing here.  
译文：我们在这里看到的并不完全是这里看到的东西。  

**02:38:28 - 02:38:38**  
原文：So even though under the hood, the model produces these kinds of kind of chains of thought, OpenAI chooses to not show the exact chains of thought in the web interface.  
译文：所以，即使在内部，模型生成了这类思维链，OpenAI 选择不在网页界面显示确切的思维链。  

**02:38:38 - 02:38:41**  
原文：It shows little summaries of that or those chains of thought.  
译文：它显示了那一个或那些思维链的简要总结。  

**02:38:41 - 02:38:58**  
原文：And OpenAI kind of does this, I think, partly because they are worried about what's called the distillation risk, that is, that someone could come in and actually try to imitate those reasoning traces and recover a lot of the reasoning performance by just imitating the reasoning chains of thought.  
译文：并且OpenAI某种程度上也是这样做的，我认为这 partly 是因为他们担心所谓的蒸馏风险，也就是说，有人可能会尝试模仿这些推理痕迹，通过仅仅模仿推理的思路链条来恢复大量的推理性能。  

**02:38:58 - 02:39:02**  
原文：And so they kind of hide them, and they only show a little summaries of them.  
译文：所以它们把这些东西藏起来， 只显示一点总结。  

**02:39:02 - 02:39:07**  
原文：So you're not getting exactly what you would get in deep sig as with respect to the reasoning itself.  
译文：所以你得到的并不是深度信号中完全相同的推理结果。  

**02:39:07 - 02:39:08**  
原文：And then they write out the solution.  
译文：然后他们写出解决方案。  

**02:39:09 - 02:39:14**  
原文：So these are kind of like equivalent even though we're not seeing the full underthe hood details.  
译文：所以这些在某种程度上是等价的，即使我们没有看到所有的内部细节。  

**02:39:14 - 02:39:19**  
原文：Now in terms of the performance, these models and deep tick models are currently roughly on par.  
译文：现在关于性能方面，这些模型和深度Tick模型目前大致相当。  

**02:39:19 - 02:39:23**  
原文：I would say it's kind of hard to tell because of the evaluations.  
译文：我会说因为这些评价，很难说。  

**02:39:23 - 02:39:30**  
原文：But if you're paying doltwo hundred dollars per month to OpenAI, some of these models, I believe are currently they basically still look better.  
译文：但如果你每月支付 OpenAI 两百美元，我认为这些模型中的一些目前看起来仍然更好。  

**02:39:30 - 02:39:42**  
原文：But deep sir, one for now is still a very solid choice for a thinking model that would be available to you sort of either on this web site or any other web site because the model is open weights, you can just download it.  
译文：但是，深度先生，目前对于您来说，它仍然是一个非常可靠的选择，作为可在本网站或任何其他网站上使用的思考模型，因为该模型是开放权重的，您可以直接下载它。  

**02:39:42 - 02:39:44**  
原文：So that's thinking models.  
译文：所以这就是思考模型。  

**02:39:44 - 02:39:46**  
原文：So what is the summary so far?  
译文：那么目前的总结是什么？  

**02:39:46 - 02:40:00**  
原文：Well, we've talked about reinforcement learning and the fact that thinking emerges in the process of the optimization on when we basically run rl on many math and kind of code problems that have verifiable solutions.  
译文：好吧，我们已经讨论了强化学习以及思考过程是在优化过程中涌现出来的这一事实，即当我们基本上在许多具有可验证解决方案的数学和代码问题上运行强化学习时。  

**02:40:00 - 02:40:02**  
原文：So there's like an answer three etc..  
译文：所以这里有一个答案三等等..。  

**02:40:02 - 02:40:11**  
原文：Now these thinking models you can access in, for example, deep seek or any inference provider, like to gather that AI and choosing deep sek over there.  
译文：现在这些思维模型你可以通过例如深度搜索或任何推理提供者来访问，比如聚集那种AI并选择那里的深度搜索。  

**02:40:11 - 02:40:22**  
原文：These thinking models are also available in ChatGPT under any of the zero one, zero three models, but these GPT -4 row models etc., they're not thinking models.  
译文：这些思维模型在ChatGPT中也可以通过任何一种零一、零三模型获得，但这些GPT-4系列模型等，它们不是思维模型。  

**02:40:22 - 02:40:24**  
原文：You should think of them as mostly sft models.  
译文：你应该把它们主要视为软模型。  

**02:40:24 - 02:40:31**  
原文：Now, if are if you have a prompt that requires advanced reasoning and so on, you should probably use some of the thinking models or at least try them out.  
译文：现在，如果你有一个需要高级推理等的提示，你应该大概使用一些思考模型，或者至少尝试一下它们。  

**02:40:31 - 02:40:39**  
原文：But empirically, for a lot of my use, when you're asking a simpler question, there's like a knowledge based question or something like that, this might be overkill.  
译文：但根据我的经验，对于很多用途来说，当你问一个比较简单的问题时，比如一个基于知识的问题之类的，这样做可能就显得过于复杂了。  

**02:40:39 - 02:40:42**  
原文：Like there's no need to think 30s about some factual question.  
译文：比如，不需要花30秒去思考某个事实性问题。  

**02:40:42 - 02:40:46**  
原文：So for that, I will sometimes default to just GPT -4 zero.  
译文：所以，有时我会选择直接使用GPT-4零版本。  

**02:40:46 - 02:40:50**  
原文：So empirically, about 80, 90% of my use is just GPT -4 zero.  
译文：所以，根据实际经验，大约80%到90%的使用只是GPT-4零。  

**02:40:50 - 02:40:57**  
原文：And when I come across a very difficult problem, like in math and code etc., I will reach for the thinking models.  
译文：当我在数学和编程等方面遇到非常困难的问题时，我会求助于思维模型。  

**02:40:57 - 02:41:03**  
原文：But then I have to wait a bit longer because they are thinking so you can access these on chatchpty, on deep seek.  
译文：但然后我得等一会儿，因为他们正在考虑，所以你可以在 chatchpty 上，在 deep seek 上访问这些。  

**02:41:03 - 02:41:14**  
原文：Also, I wanted to point out that AI studio dot dot com, even though it looks really busy, really ugly, because gis just unable to do this kind of stuff, well, is like what is happening.  
译文：另外，我想指出的是，尽管AI工作室网站看起来非常繁忙，非常不好看，因为地理信息系统（GIS）无法完成这类工作，这正是现在发生的情况。 

注：原文中的“AI studio dot dot com”可能是指某个具体的网站，直译为“AI工作室网站”，但具体所指需要根据上下文确定。此外，“gis just unable to do this kind of stuff”中的“gis”如果是指地理信息系统（Geographic Information System），则按照专业术语进行了翻译。如果有其他特定含义，请提供更多信息以便更准确地翻译。  

**02:41:14 - 02:41:30**  
原文：But if you choose model and you choose here, gem and I 2.0, flash thinking experimental zero, one, 21, if you choose that one, that's also a kind of early experiment experimental of a thinking model by so we can go here and we can give it the same problem and click run.  
译文：但是如果你选择模型，并且在这里选择gem和我2.0，flash思考实验零，一，二十一，如果你选择那个选项，那也是一种早期的思考模型实验。所以我们可以在这里进行操作，给它相同的問題，然后点击运行。 

请注意，这段文本中包含了一些可能不完全清晰或特定于某个上下文的术语（如“gem和我2.0”，“flash思考实验零，一，二十一”），这些术语可能需要根据具体情况进行调整或解释。  

**02:41:30 - 02:41:37**  
原文：And this is also a thinking problem, a thinking model that will also do something similar and comes out with the right answer here.  
译文：这也是一个思维问题，一个思维模型，它也会做类似的事情，并在这里得出正确的答案。  

**02:41:37 - 02:41:40**  
原文：So basically, Jim and I also offers a thinking model.  
译文：所以，基本上，Jim和我也提供了一种思维模型。  

**02:41:40 - 02:41:43**  
原文：Anththropic currently does not offer a thinking model.  
译文：Anthropic目前不提供思考模型。  

**02:41:43 - 02:41:47**  
原文：But basically this is kind of like the frontier development of these llms.  
译文：但基本上，这就像这些大型语言模型的前沿发展。  

**02:41:47 - 02:41:52**  
原文：I think rl is kind of like this new exciting stage, but getting the details right is difficult.  
译文：我认为强化学习就像是这个新的令人兴奋的阶段，但要把细节做好是困难的。  

**02:41:52 - 02:41:59**  
原文：And that's why all these models and thinking models are currently experimental as of 2025, very early 2025.  
译文：这就是为什么所有这些模型和思维模型在2025年，也就是2025年的初期，仍然处于实验阶段。  

**02:41:59 - 02:42:08**  
原文：But this is kind of like the frontier development of pushing the performance and these very difficult problems using reasoning that is emergent in these optimizations.  
译文：但这也像是在开拓性地发展， 推动性能的提升和解决这些非常困难的问题， 使用在这些优化中涌现出来的推理方式。  

**02:42:08 - 02:42:18**  
原文：One more connection that I wanted to bring up is that the discovery that reinforcement learning is extremely powerful way of learning is not new to the field of AI.  
译文：我想再补充一个联系是，强化学习是一种极其强大的学习方法这一发现，并不是人工智能领域的新内容。  

**02:42:18 - 02:42:23**  
原文：And one place where we've already seen this demonstrated is in the game of go.  
译文：我们已经在一个地方看到这一点得到证明，那就是在围棋游戏中。  

**02:42:23 - 02:42:32**  
原文：And famously, DeepMind developed the system, AlphaGo, and you can watch a movie about it, where the system is learning to play the game of go against top human players.  
译文：而且著名的是，DeepMind 开发了系统 AlphaGo，您可以观看有关它的电影，在电影中，系统正在学习与顶级人类选手进行围棋比赛。  

**02:42:32 - 02:42:56**  
原文：And when we go through the paper underlying AlphaGo, so in this paper, when we scroll down, we actually find a really interesting plot that I think is kind of familiar to us and we're kind of like we discovering in the more open domain of arbitrary problem solving instead of on the close specific domain of the game of go.  
译文：当我们浏览支持AlphaGo的论文时，所以在该论文中，当我们向下滚动，我们实际上发现了一个非常有趣的图表，我认为这个图表对我们来说有点熟悉，而且我们有点像是在任意问题解决的更开放领域中发现了它，而不是在围棋这一封闭特定领域中。  

**02:42:56 - 02:43:05**  
原文：But basically, what they saw, and we're going to see this in lms as well as this becomes more mature, is this is the elo rating of playing game of go.  
译文：但基本上，他们看到的，以及我们将在lms中看到的，随着它变得越来越成熟，这是进行围棋游戏的Elo评级。  

**02:43:05 - 02:43:08**  
原文：And this is Lisa dole, an extremely strong human player.  
译文：这是丽莎·多尔，一位非常强大的人类选手。  

**02:43:08 - 02:43:17**  
原文：And here where they are comparing is the strength of a model learned, trained by supervise learning and a model trained by reinforcement learning.  
译文：他们在比较的是通过监督学习训练得到的模型和通过强化学习训练得到的模型的强度。此处的格式已尽量保持与原始文本一致：

And here where they are comparing is the strength of a model learned, trained by supervise learning and a model trained by reinforcement learning. 

（注：为了使句子更符合中文表达习惯，稍微调整了语序和用词。）  

**02:43:17 - 02:43:20**  
原文：So the supervised learning model is imitating human expert players.  
译文：所以监督学习模型是在模仿人类专家玩家。  

**02:43:20 - 02:43:29**  
原文：So if you just get a huge amount of games played by expert players in the game of go and you try to imitate them, you are going to get better.  
译文：所以，如果你只是获取大量由围棋专家玩家对战的游戏记录并尝试模仿他们，你会变得更好。  

**02:43:29 - 02:43:35**  
原文：But then you top out and you never quite get better than some of the top, top, top players in the game of go like licido.  
译文：但随后你达到了极限，你永远也无法超越像 licido 这样的顶级围棋高手。  

**02:43:35 - 02:43:39**  
原文：So you're never to not reach there because you're just imitating human players.  
译文：所以你永远不要达不到那个程度，因为你只是在模仿人类玩家。  

**02:43:39 - 02:43:43**  
原文：You can't fundamentally go beyond the human player if you're just imitating human players.  
译文：你不能仅仅通过模仿人类玩家就从根本上超越人类玩家。  

**02:43:43 - 02:43:48**  
原文：But in the process of reinforcement, the learning is significantly more powerful.  
译文：但是在强化的过程中，学习的效果显著更强。  

**02:43:48 - 02:43:57**  
原文：In reinforcement learning for a game of go, it means that the system is playing moves that empirically and statistically lead to win to winning the game.  
译文：在围棋的强化学习中，这意味着系统正在下那些经经验和统计证明能导致获胜的棋步。  

**02:43:57 - 02:44:05**  
原文：And so AlphaGo is a system where it kind of plays against the eat itself, and it's using reinforcement learning to create rollouts.  
译文：因此，AlphaGo 是一个系统，它通过自我对弈来不断进步，使用强化学习来生成rollouts（预测序列）。  

**02:44:05 - 02:44:09**  
原文：So it's the exact same diagram here, but there's no prompt.  
译文：所以这里是一模一样的图表，但是没有提示。  

**02:44:09 - 02:44:11**  
原文：It's just because there's no prompt.  
译文：只是因为没有提示。  

**02:44:11 - 02:44:13**  
原文：It's just a fixed game of go.  
译文：这仅仅是一场固定的围棋比赛。  

**02:44:13 - 02:44:15**  
原文：But it's trying out lots of solutions.  
译文：但它正在尝试很多解决方案。  

**02:44:15 - 02:44:17**  
原文：It's trying out lots of plaand.  
译文：它正在尝试很多计划。  

**02:44:17 - 02:44:22**  
原文：Then the games that lead to a win instead of a specific cancer are reinforced.  
译文：然后强化那些导致胜利而不是特定癌症的游戏。  

**02:44:22 - 02:44:23**  
原文：They're made, ate stronger.  
译文：它们被制造得更坚固。  

**02:44:23 - 02:44:31**  
原文：And so the system is learning basically the sequences of actions that empiriking and statistically lead to winning the game.  
译文：因此，该系统基本上是在学习那些通过经验和统计上能导致赢得游戏的动作序列。  

**02:44:31 - 02:44:36**  
原文：And reinforcement learning is not going to be constrained by human performance.  
译文：并且强化学习不会受到人类表现的限制。  

**02:44:36 - 02:44:41**  
原文：And reinforcement learning can do significantly better and overcome even the top players like licido.  
译文：强化学习可以做得更好，甚至可以超越像licido这样的顶级玩家。  

**02:44:41 - 02:44:48**  
原文：And so probably they could have run this longer, and they just chose to crop it at some point because this costs money.  
译文：所以他们本可以将这个运行更长时间，但他们可能只是选择在某个时间点截断它，因为这需要花钱。  

**02:44:48 - 02:44:52**  
原文：But this is a very powerful demonstration of reinforcement learning.  
译文：但这是强化学习的一个非常有力的演示。  

**02:44:52 - 02:44:58**  
原文：And we're only starting to kind of see hints off this diagram in large language models for reasoning problems.  
译文：我们才刚刚开始在大型语言模型中看到这种图表在推理问题上的提示。  

**02:44:58 - 02:45:02**  
原文：So we're not going to get too far by just imitating experts.  
译文：所以我们单靠模仿专家是不会走太远的。  

**02:45:02 - 02:45:14**  
原文：We need to go beyond that, set up these little game environments and get let the system discover reasoning traces or like ways Ste of solving problems that are unique and that just basically work well.  
译文：我们需要更进一步，建立这些小型游戏环境，让系统发现推理痕迹或解决问题的独特方法，这些方法只需基本可行即可。  

**02:45:14 - 02:45:25**  
原文：Now, on this aspect of uniqueness, notice that when you're doing reinforcement learning, nothing prevents you from veering off the distribution of how humans are playing the game.  
译文：现在，关于这个独特性的方面，请注意当你进行强化学习时，没有什么能阻止你偏离人类玩游戏的分布。  

**02:45:25 - 02:45:33**  
原文：And so when we go back to this AlphaGo search here, one of the suggested modifications is called move 37.  
译文：因此，当我们回到这个AlphaGo搜索时，其中一个建议的修改被称为第37步。  

**02:45:33 - 02:45:42**  
原文：And move 37 in AlphaGo is referring to a specific point in time where AlphaGo basically played a move that no human expert would play.  
译文：而AlphaGo的第37步指的是 一个特定的时刻， 在这个时刻AlphaGo下了一步棋， 没有人类专家会下这一步。  

**02:45:42 - 02:45:48**  
原文：So the probability of this move to be played by a human player was evaluated to be about one in 10000.  
译文：所以这一招被人类棋手使出的概率 被评估为大约一万分之一。  

**02:45:48 - 02:45:50**  
原文：So it's a very rare move.  
译文：所以这是一个非常罕见的举动。  

**02:45:50 - 02:45:52**  
原文：But in retrospect, it was a brilliant move.  
译文：但回头看来，这一步棋走得十分高明。  

**02:45:52 - 02:46:02**  
原文：So AlphaGo, in the process of reinforcement learning, discovered kind of like a strategy of playing that was unknown to humans, but is, in retrospect, brilliant.  
译文：因此，AlphaGo 在强化学习的过程中，发现了一种对人类来说未知的下棋策略，但事后看来，这是非常出色的。  

**02:46:02 - 02:46:07**  
原文：I recommend this U to video Lisa doll versus AlphaGo move 37 reactions and analysis.  
译文：我推荐这个U去观看视频，内容是Lisa doll对AlphaGo第37手的反应和分析。  

**02:46:07 - 02:46:11**  
原文：And this is kind of what it looked like when AlphaGo played this move.  
译文：这就是AlphaGo下这手棋时 的样子。  

**02:46:11 - 02:46:12**  
原文：Value.  
译文：价值。  

**02:46:12 - 02:46:17**  
原文：That's a very surprising move.  
译文：那是一个非常令人惊讶的举动。  

**02:46:17 - 02:46:21**  
原文：I thought it was a mistake.  
译文：我以为那是一个错误。  

**02:46:22 - 02:46:33**  
原文：When I see this move anyway, so basically people are kind of freaking out because it's a move that a human would not play, that AlphaGo played, because in its training, this move seemed to be a good idea.  
译文：当我看到这一步时，人们基本上都有点惊慌失措， 因为这是AlphaGo走出的一步棋，而人类是不会这样下的， 因为在其训练过程中，这一步看起来是个不错的主意。  

**02:46:33 - 02:46:36**  
原文：It just happens not to be a kind of thing that a human ans would do.  
译文：这恰好不是人类会做的事情。  

**02:46:36 - 02:46:39**  
原文：And so that is, again, the power of reinforcement learning.  
译文：这就是强化学习的力量，再次彰显。  

**02:46:39 - 02:46:46**  
原文：And in principle, we can actually see the equivalence of that if we continue scaling this paradigm in language models.  
译文：原则上，如果我们继续在语言模型中扩展这种范式，我们实际上可以看到其等价性。  

**02:46:46 - 02:46:49**  
原文：And what that looks like is kind of unknown.  
译文：而那会是什么样子某种程度上是未知的。  

**02:46:49 - 02:46:55**  
原文：So what does it mean to solve problems in such a way that even humans would not be able to get?  
译文：那么，以这种方式解决问题意味着什么，即使人类也无法理解？  

**02:46:55 - 02:46:59**  
原文：How can you be better at reasoning or thinking than humans?  
译文：你怎么能在推理或思考方面比人类更出色？  

**02:46:59 - 02:47:01**  
原文：How can you go beyond just a thinking human?  
译文：你如何超越仅仅是一个思考的人？  

**02:47:01 - 02:47:09**  
原文：Like maybe it means discovering analogies that humans would not be able to create, or maybe it's like a new thinking strategy.  
译文：比如，这可能意味着发现人类无法创造的类比， 或者可能是一种新的思维策略。  

**02:47:09 - 02:47:11**  
原文：It's kind of hard to think through.  
译文：这有点难以思考。  

**02:47:11 - 02:47:16**  
原文：Maybe it's a whole new language that actually is not even English.  
译文：可能这完全是另一种全新的语言，实际上甚至不是英语。  

**02:47:16 - 02:47:24**  
原文：Maybe it discovers its own language that is a lot better at thinking because the model is unconstrained to even like stick with English.  
译文：也许它发现了自己的一种语言，这种语言更有利于思考，因为模型不受限于使用英语。  

**02:47:24 - 02:47:30**  
原文：So maybe it takes a different language to think, or it discovers its own language.  
译文：所以也许它用另一种语言思考，或者它发现了它自己的语言。  

**02:47:30 - 02:47:34**  
原文：So in principle, the behavior of the system is a lot less defined.  
译文：所以，从原则上讲，系统的行径定义少得多。  

**02:47:34 - 02:47:42**  
原文：It is open to do whatever works, and it is open to also slowly drift from the distribution of his training data, which is English.  
译文：它开放执行任何有效的工作，也开放逐渐偏离其训练数据的分布，而其训练数据是英语。  

**02:47:42 - 02:47:49**  
原文：But all of that can only be done if we have a very large, diverse set of problems in which these strategies can be refined and perfected.  
译文：但所有这些都只能在我们拥有一个非常庞大、多样化的问题集的情况下完成，这些问题可以使这些策略得到提炼和完善。  

**02:47:49 - 02:47:58**  
原文：And so that is a lot of the frontier on research that's going on right now, is trying to kind of create those kinds of prompt distributions that are large and diverse.  
译文：所以，这就是当前研究的很多前沿领域，即尝试创建那些大规模且多样的提示分布。  

**02:47:58 - 02:48:02**  
原文：These are all kind of like game environments in which elms can practice their thinking.  
译文：这些都像是游戏环境， 在其中榆树可以练习它们的思考。 

请注意，原文中提到“elms”通常指的是“榆树”，但在上下文中将其理解为一种拟人化的表达可能是更合适的选择，以符合可能的语境或比喻用法。如果“elms”是指某种特定的对象或概念，请根据具体背景进行调整。  

**02:48:02 - 02:48:11**  
原文：And it's kind of like writing, you know, these practice problems, we have to create practice problems for all of domains of knowledge.  
译文：这有点像写这些练习题一样，你知道的，我们必须为所有知识领域创建练习题。  

**02:48:11 - 02:48:20**  
原文：And if we have practice problems, and tons of them, the mouwill be able to reinforcement learning, reinforcement learn on them and kind of create these kinds of diagrams.  
译文：如果我們有練習題，而且有大量的題目，那麼模型將能夠進行強化學習，基於這些題目進行訓練，並創建這類圖表。  

**02:48:20 - 02:48:33**  
原文：But in a domain of open thinking instead of close domain, like game of go, there's one more section within reinforcement learning that I wanted to cover, and that is that of learning in unveriable domains.  
译文：但在一个开放思维的领域，而不是封闭的领域，比如围棋，我想在强化学习中再介绍一个部分，那就是在不可验证领域的学习。  

**02:48:33 - 02:48:38**  
原文：So so far, all of the problems that we've looked at are in what's called verifiable domains.  
译文：到目前为止，我们所看到的所有问题 都属于所谓的可验证领域。  

**02:48:38 - 02:48:43**  
原文：That is any candidate solution, we can score very easily against a concrete answer.  
译文：那是任何候选解决方案，我们都可以非常容易地根据一个具体答案进行评分。  

**02:48:43 - 02:48:49**  
原文：So for example, answer is three, and we can very easily score these solutions against the answer of three.  
译文：所以，例如，答案是三， 我们可以非常容易地将这些答案与标准答案三进行对比评分。  

**02:48:49 - 02:48:57**  
原文：Either we require the models to like box in their answers and then we just check for equality of whatever is in the box with the answer.  
译文：要么我们要求模型像在框内填写他们的答案，然后我们只是检查框内的内容与答案是否相等。  

**02:48:57 - 02:49:00**  
原文：Or you can also use kind of what's called an llm judge.  
译文：或者你也可以使用一种所谓的LLM法官。  

**02:49:00 - 02:49:08**  
原文：So the llm judge looks at a solution and it gets the answer and just basically scores the solution for whether it's consistent with the answer or not.  
译文：所以，LLM法官查看一个解决方案，得到答案，然后基本上只是根据该解决方案是否与答案一致来评分。  

**02:49:08 - 02:49:12**  
原文：And llms empirically are good enough at the current capability that they can do this fairly reliably.  
译文：而且，从经验来看，目前的语言模型能力已经足够强大，可以相当可靠地完成这项任务。  

**02:49:12 - 02:49:15**  
原文：So we can apply those kinds of techniques as well.  
译文：所以我们也可以应用这些类型的技术。  

**02:49:15 - 02:49:19**  
原文：In any case, we have a concrete answer and we're just checking solutions against it.  
译文：在任何情况下，我们都有一个具体的答案，我们只是将解决方案与之核对。  

**02:49:19 - 02:49:23**  
原文：And we can do this automatically with no kind of humans in the loop.  
译文：我们可以自动完成这一过程，完全不需要人工干预。  

**02:49:23 - 02:49:27**  
原文：The problem is that we can't apply this strategy in what's called unverifiable domains.  
译文：问题是我们在所谓的不可验证领域中 无法应用这一策略。  

**02:49:27 - 02:49:35**  
原文：So usually these are, for example, creative writing tasks, like write a joke about pelicans or write a poem, or summarize a paragraph or something like that.  
译文：所以通常这些是，例如，创意写作任务，像写一个关于鹈鹕的笑话或者写一首诗，或者总结一段话之类的任务。  

**02:49:35 - 02:49:40**  
原文：In these kinds of domains, it becomes harder to score our different solutions to this problem.  
译文：在这些领域中，要对我们针对此问题的不同解决方案进行评分变得更为困难。  

**02:49:40 - 02:49:44**  
原文：So for example, writing a joke about pelicans, we can generate lots of different jokes.  
译文：所以，例如，写一个关于Pelicans的笑话，我们可以生成许多不同的笑话。  

注意：这里的“Pelicans”是指一种鸟类（鹈鹕），在中文中应翻译为“鹈鹕”。因此，更准确的翻译是：

所以，例如，写一个关于鹈鹕的笑话，我们可以生成许多不同的笑话。  

**02:49:44 - 02:49:45**  
原文：Of course, that's fine.  
译文：当然，那很好。  

**02:49:45 - 02:49:51**  
原文：For example, we can go to chashpt and we can get it to generated joke about pelicans.  
译文：例如，我们可以去chashpt，然后让它生成一个关于Pelicans的笑话。  

**02:49:51 - 02:49:57**  
原文：So much stuff in their beaks because they don't bellican and backpacks.  
译文：他们的喙里有这么多东西，因为他们不会把东西放在背包里。 

注：原文中 "bellican" 似乎是一个拼写错误或自创词，可能是想表达 “像鹈鹕一样”（pelican）或者 “把东西放进背包里”。根据上下文，我将其理解为与“背包”相对的概念，即不会把东西放在背包里，而是都衔在嘴里。如果你有其他意图，请进一步说明。  

**02:49:57 - 02:49:57**  
原文：Why?  
译文：为什么？  

**02:49:57 - 02:49:59**  
原文：Okay, we we can try something else.  
译文：好的，我们可以尝试其他的东西。  

**02:49:59 - 02:50:02**  
原文：Why don't pelicans ever pay for their drinks?  
译文：为什么鹈鹕从来不用付饮料钱？  

**02:50:02 - 02:50:05**  
原文：Because they always bill it to someone else.  
译文：因为他们总是把账单开给其他人。  

**02:50:05 - 02:50:05**  
原文：Ha ha.  
译文：哈哈。  

**02:50:05 - 02:50:05**  
原文：Okay.  
译文：好的。  

**02:50:05 - 02:50:09**  
原文：So these models are not obviously not very good at humor.  
译文：所以这些模型显然不擅长幽默。  

**02:50:09 - 02:50:22**  
原文：Actually, I think it's pretty fascinating because I think humor is secretly very difficult and the models don't have the capability, I think anyway, in any case, you could imagine creating lots of jokes.  
译文：实际上，我觉得这很有趣，因为我认为幽默表面上看似简单，但实际上非常难，而这些模型并没有这种能力，至少我是这么认为的。无论如何，在这种情况下，你可以想象创造出许多笑话。  

**02:50:22 - 02:50:24**  
原文：The problem that we are facing is how do we score them?  
译文：我们面临的问题是如何对他们进行评分？  

**02:50:24 - 02:50:30**  
原文：Now, in principle, we could, of course, get a human to look at all these jokes, just like I did right now.  
译文：现在，原则上，我们当然可以让一个人来看所有这些笑话，就像我刚才做的那样。  

**02:50:30 - 02:50:36**  
原文：The problem with that is if you are doing during inforcement learning, you're going to be doing many thousands of updates.  
译文：问题在于，如果你正在进行强化学习，你将进行成千上万次的更新。  

**02:50:36 - 02:50:46**  
原文：And for each update, you want to be looking at, say, thousands of proms, and for each prompt, you want to be potentially at looking at hundor, thousands of different kinds of generations.  
译文：对于每次更新，您需要查看成千上万的提示，而对于每个提示，您可能需要查看数百、数千种不同的生成结果。  

**02:50:46 - 02:50:50**  
原文：And so there's just like way too many of these to look at.  
译文：所以，有太多这样的东西要看。  

**02:50:50 - 02:51:00**  
原文：And so in principle, you could have a human inspect all of them and score them and decide that, okay, maybe this one is funny and maybe this one is funny and this one is funny.  
译文：原则上，你可以让一个人检查所有这些并为它们打分，决定哪些是搞笑的，也许这个是搞笑的，也许这个是搞笑的，这个也是搞笑的。  

**02:51:00 - 02:51:08**  
原文：And we could train on them to get the model to become slightly better at jokes in the context of pelicans at least.  
译文：我们可以用它们进行训练，使模型至少在Pelicans这个背景下讲笑话的能力变得稍微好一点。  

**02:51:08 - 02:51:11**  
原文：The problem is that it's just like way too much human time.  
译文：问题是这样做需要耗费大量的人力时间。  

**02:51:11 - 02:51:13**  
原文：This is an unscalable strategy.  
译文：这是一种无法扩展的策略。  

**02:51:13 - 02:51:16**  
原文：We need some kind of an automatic strategy for doing this.  
译文：我们需要某种自动策略来完成这个任务。  

**02:51:16 - 02:51:23**  
原文：And one sort of solution to this was proposed in this paper that introduced what's called reinforcement learning from human feedback.  
译文：并且在这篇论文中提出了一种解决方案，该方案引入了所谓的从人类反馈中进行强化学习。  

**02:51:23 - 02:51:29**  
原文：And so this was a paper from OpenAI at the time, and many of these people are now cohunders and anthropic.  
译文：这就是当时OpenAI的一篇论文，而这些作者中的许多人现在在Cohunders和Anthropic工作。  

**02:51:29 - 02:51:35**  
原文：And this kind of proposed a approach for basically doing reinforcement learning in unveriable domains.  
译文：这种方法基本上是在不可验证领域中进行强化学习的一种提议。  

**02:51:35 - 02:51:37**  
原文：So let's take a look at how that works.  
译文：所以让我们来看看它是如何工作的。  

**02:51:37 - 02:51:41**  
原文：So this is the cartoon diagram of the core ideas involved.  
译文：所以这就是所涉及核心思想的卡通图解。  

**02:51:41 - 02:51:48**  
原文：So as I mentioned, the kneve approach is if we just had infinity human time, we could just run rl in these domains just fine.  
译文：所以正如我提到的，如果我们可以拥有无限的人力时间，我们就可以在这些领域很好地运行强化学习（RL）。这里的“kneve”看起来可能是拼写错误或特定术语，根据上下文我推测您指的是这种方法或理念。如果有误，请您指正。  

**02:51:48 - 02:51:51**  
原文：So for example, we can run rl as usual.  
译文：所以，例如，我们可以像往常一样运行rl。  

**02:51:51 - 02:52:00**  
原文：If I have infinity humans, I just want to do and these are just cartoon numbers, I want to do 1000 updates where each update will be on 1000 prompts.  
译文：如果我有无限的人力，我只是想做，这些只是卡通数字，我想进行1000次更新，每次更新将基于1000个提示。  

**02:52:00 - 02:52:04**  
原文：And for each prompt, we're going to have 1000 rollouts that we're scoring.  
译文：对于每个提示，我们将进行1000次 rollout 并对其进行评分。  

**02:52:04 - 02:52:07**  
原文：So we can run rl with this kind of a setup.  
译文：所以我们可以用这种设置来运行强化学习。  

**02:52:07 - 02:52:12**  
原文：The problem is, in the process of doing this, I will need to run one.  
译文：问题是，在这个过程中，我需要运行一个。  

**02:52:12 - 02:52:17**  
原文：I would need to ask a human to evaluate joke a total of 1 billion times.  
译文：我需要请一个人来评估一个笑话，总共需要10亿次。  

**02:52:17 - 02:52:21**  
原文：And so that's a lot of people looking at really terrible jokes.  
译文：所以，有好多人都在看真的很糟糕的笑话。  

**02:52:21 - 02:52:23**  
原文：So we don't want to do that.  
译文：所以我们不想要这样做。  

**02:52:23 - 02:52:26**  
原文：So instead, we want to take the rh of approach.  
译文：所以我们想采用rh的方法。  

**02:52:26 - 02:52:31**  
原文：So in our Leof approach, we are kind of like the core trick is that of indirection.  
译文：所以在我们的Leof方法中，核心技巧可以说是间接性。  

**02:52:31 - 02:52:35**  
原文：So we're going to involve humans just a little bit.  
译文：所以我们只会让人类稍微参与一下。  

**02:52:35 - 02:52:42**  
原文：And the way we cheat is that we basically train a whole separate neural network that we call a reward model.  
译文：我们作弊的方法是基本上训练一个完全独立的神经网络，我们称之为奖励模型。  

**02:52:42 - 02:52:46**  
原文：And this neural network will kind of like imitate humscores.  
译文：而且这个神经网络会有点像模仿 humscores。  

**02:52:46 - 02:52:49**  
原文：So we're going to ask humans to score rollouts.  
译文：所以我们将要求人类对展开进行评分。  

**02:52:49 - 02:52:53**  
原文：We're going to then imitate human scores using a neural network.  
译文：然后我们将使用神经网络来模仿人类的分数。  

**02:52:53 - 02:52:58**  
原文：And this neural network will become a kind of simulator of human preferences.  
译文：而且这个神经网络将成为一种人类偏好的模拟器。  

**02:52:58 - 02:53:02**  
原文：And now that we have a neural network simulator, we can do rl against it.  
译文：现在我们有了一个神经网络模拟器，我们可以用它来进行强化学习。  

**02:53:02 - 02:53:08**  
原文：So instead of asking in a real human, we're asking a simulated human for their score of a joke, as an example.  
译文：所以，与其问一个真人， 我们不如问问模拟人， 来对一个笑话打分，作为例子。  

**02:53:08 - 02:53:14**  
原文：And so once we have a simulator, we're off this racist because we can query it as many times as we want to.  
译文：因此，一旦我们有了模拟器，我们就不再受此限制，因为我们可以查询它任意多次。  

**02:53:14 - 02:53:16**  
原文：And it's all whole automatic process.  
译文：而且整个过程完全是自动的。  

**02:53:16 - 02:53:20**  
原文：And we can now do reinforcement learning with respect to the simulator.  
译文：我们现在可以根据模拟器进行强化学习。  

**02:53:20 - 02:53:29**  
原文：And a simulator, as you might expect, is not going to be a perfect human, but if it's at least statistically similar to human judgment, then you might expect that this will do something.  
译文：如你所料，模拟器不会是一个完美的人类，但如果它至少在统计上与人类的判断相似，那么你可以预期这将会起到一些作用。  

**02:53:29 - 02:53:31**  
原文：And in practice, indeed, it does.  
译文：实际上，确实如此。  

**02:53:31 - 02:53:34**  
原文：So once we have a simulator, we can do rl, and everything works great.  
译文：所以一旦我们有了模拟器，我们就可以进行强化学习，一切都会非常顺利。  

**02:53:34 - 02:53:38**  
原文：So let me show you a cartoon diagram, a little bit of what this process looks like.  
译文：所以让我给你看一个卡通示意图， 这个过程大概就是这样的。  

**02:53:38 - 02:53:41**  
原文：Although the details are not one like super important.  
译文：虽然细节并不像超级重要。  

（注：原句在语法上有些不规范，直译后也存在不通顺的地方。如果需要更自然的表达，可以调整为：“虽然细节并不是至关重要。”）  

**02:53:41 - 02:53:43**  
原文：It's just a core idea of how this works.  
译文：这只是一个关于它是如何工作的核心思想。  

**02:53:43 - 02:53:48**  
原文：So here we have a cartoon diagram of a hypothetical example of what training the reward model would look like.  
译文：所以这里我们有一个卡通图，展示了训练奖励模型的假设示例。  

**02:53:48 - 02:53:51**  
原文：So we have a prompt like write a joke about pelicans.  
译文：所以我们的提示是像这样的：写一个关于鹈鹕的笑话。  

**02:53:51 - 02:53:54**  
原文：And then here we have five separate rollouts.  
译文：然后这里我们有五个独立的发布。  

**02:53:54 - 02:53:57**  
原文：So these are all five different jokes, just like this one.  
译文：所以这些都是五个不同的笑话，就像这个一样。  

**02:53:57 - 02:54:05**  
原文：Now the first thing we're going to do is we are going to ask a human to order these jokes from the best to worst.  
译文：现在我们首先要做的 是请一个人类按照从最好笑 到最不好笑的顺序 给这些笑话排个序。  

**02:54:05 - 02:54:10**  
原文：So this is so here, this human thought that this joke is the best, the funniest.  
译文：所以这就是这里的情况，这个人类认为这个笑话是最好的，最搞笑的。  

**02:54:10 - 02:54:11**  
原文：So number one joke.  
译文：所以，第一个笑话。  

**02:54:11 - 02:54:14**  
原文：This is number two joke, number three joke, 45.  
译文：这是第二个笑话，第三个笑话，45。  

**02:54:14 - 02:54:22**  
原文：So this is the worst joke we're asking humans to order instead of give scores directly, because it's a bit of an easier task.  
译文：所以这是我们要人类进行排序而不是直接给分数的最差的笑话，因为这是一项相对简单的任务。  

**02:54:22 - 02:54:27**  
原文：It's easier for a human to give an ordering than to give precise scores.  
译文：对于人类来说，给出一个排序比给出精确的分数要容易。  

**02:54:27 - 02:54:30**  
原文：Now that is not the supervision for the model.  
译文：这并不是模型的监督。  

**02:54:30 - 02:54:36**  
原文：So the human has ordered them, and that is kind of like their contribution to the training process.  
译文：所以人类已经对他们进行了排序，这有点像他们对训练过程的贡献。  

**02:54:36 - 02:54:42**  
原文：But now separately, what we're going to do is we're going to ask a reward model about its scoring of these jokes.  
译文：但我们现在分别要做的是，我们要询问一个奖励模型关于这些笑话的评分。  

**02:54:42 - 02:54:49**  
原文：Now the reward model is a whole separate neural network, completely separate neural net, and it's also probably a transformer.  
译文：现在奖励模型是一个完全独立的神经网络，完全独立的神经网络，而且它很可能也是一个变压器。  

（注意：最后一句中的“变压器”通常指的是电力设备，在这里应该指的是一种模型架构，正确的翻译应为“变换器”或“Transformer模型”。）

改进后的翻译：
现在奖励模型是一个完全独立的神经网络，完全独立的神经网络，而且它很可能也是一个Transformer模型。  

**02:54:49 - 02:54:54**  
原文：But it's not a language model in the sense that it generates diverse language etc..  
译文：但它并不是在这个意义上生成多样化语言等的语言模型。  

**02:54:54 - 02:54:56**  
原文：It's just a scoring model.  
译文：它只是一个评分模型。  

**02:54:56 - 02:55:02**  
原文：So the reward model will take as an input the prompt number one and number two, a candidate joke.  
译文：所以奖励模型将把提示一和提示二，以及一个候选笑话作为输入。  

**02:55:02 - 02:55:06**  
原文：So those are the two inputs that go into the reward model.  
译文：所以这两个输入就是奖励模型所需要的。  

**02:55:06 - 02:55:10**  
原文：So here, for example, the reward model, we take in this prompt and this joke.  
译文：所以在这里，例如，奖励模型，我们接受这个提示和这个笑话。  

**02:55:10 - 02:55:17**  
原文：Now the output of a reward model is a single number, and this number is thought of as a score.  
译文：现在奖励模型的输出是一个数字，这个数字被认为是一个分数。  

**02:55:17 - 02:55:20**  
原文：And it can range, for example, from zero to one.  
译文：例如，它的范围可以从零到一。  

**02:55:20 - 02:55:24**  
原文：So zero would be the worst score and one would be the best score.  
译文：所以0是最差的分数，1是最好的分数。  

**02:55:24 - 02:55:32**  
原文：So here are some examples of what a hypothetical reward model at some stage in the training process would give as scoring to these jokes.  
译文：所以这里有一些假设的奖励模型在训练过程中的某个阶段会对这些笑话给出的评分示例。  

**02:55:32 - 02:55:34**  
原文：So 0.1 is a very low score.  
译文：所以0.1是一个非常低的分数。  

**02:55:34 - 02:55:37**  
原文：0.8 is a really high score, and so on.  
译文：0.8是一个非常高的分数，依此类推。  

**02:55:37 - 02:55:43**  
原文：And so now we compare the scores given by the reward model with the ordering given by the human.  
译文：现在我们将奖励模型给出的分数与人类给出的排序进行比较。  

**02:55:43 - 02:55:54**  
原文：And there's a precise mathematical way to actually calculate this, basically set up a loss function and calculate a kind of like a correspondence here and update a model based on it.  
译文：并且有一种精确的数学方法来实际计算这个，基本上是建立一个损失函数并计算这里的一种对应关系，并根据它更新模型。  

**02:55:54 - 02:56:08**  
原文：But I just want to give you the intuition, which is that as an example here for this second joke, the human thought that it was the funniest and the model kind of, agreed, 0.8 is a relatively high score, but this score should have been even higher, right?  
译文：但我想给你的直觉是，以这里这个第二个笑话为例，人类认为它是最好笑的，而模型也某种程度上同意，0.8是一个相对较高的分数，但是这个分数应该更高，对吧？  

**02:56:08 - 02:56:17**  
原文：So after an update, we would expect that maybe this score should have been will actually grow after an update of the network to be like, say, 0.81 or something.  
译文：所以更新之后，我们期望这个分数 应该会在网络更新后增长，比如说到0.81或类似的。  

**02:56:17 - 02:56:24**  
原文：For this one here, they actually are in a massive disagreement because the human thought that this was number two.  
译文：对于这一个，他们实际上有很大的分歧，因为人类认为这是第二。  

**02:56:24 - 02:56:28**  
原文：But here the score is only 0.1, and so this score needs to be much higher.  
译文：但这里的得分只有0.1，因此这个得分需要高得多。  

**02:56:28 - 02:56:36**  
原文：So after an update on top of this kind of a supervision, this might grow a lot more, like maybe it's 0.15 or something like that.  
译文：所以在这种监督之上进行更新后，这个数值可能会增长更多，比如可能达到0.15或类似的。  

**02:56:36 - 02:56:44**  
原文：And then here the human thought that this one was the worst joke, but here the model actually give it a fairly high number.  
译文：然后这里的人认为这是一个最糟糕的笑话， 但这里的模型实际上给了它一个相当高的分数。  

**02:56:44 - 02:56:50**  
原文：So you might expect that after the update, this would come down to maybe 3.5 or something like that.  
译文：所以你可能认为更新后，这会下降到3.5或类似这样的数值。  

**02:56:50 - 02:56:53**  
原文：So basically, we're doing what we did before.  
译文：所以基本上，我们正在做我们以前做过的事。  

**02:56:53 - 02:57:04**  
原文：We're slightly nudging the predictions from the models using neural network training process, and we're trying to make the reward model scores be consistent with human ordering.  
译文：我们正在通过神经网络训练过程对模型的预测进行轻微调整，并试图使奖励模型的得分与人类的排序一致。  

**02:57:04 - 02:57:19**  
原文：And so as we update the reward model on human data, it becomes better and better simulator of the scores and orders that humans provide, and then becomes kind of like the simulator of human preferences, which we can then do rl against.  
译文：因此，当我们根据人类数据更新奖励模型时，它逐渐成为越来越好地模拟人类提供的评分和排序的工具，进而成为一种人类偏好的模拟器，然后我们就可以基于此进行强化学习。  

**02:57:19 - 02:57:24**  
原文：But critically, we're not asking humans 1 billion times to look at a joke.  
译文：但关键是我们并不是要求人类看10亿次笑话。  

**02:57:24 - 02:57:27**  
原文：We're maybe looking at 1000 problems and fiber laws each.  
译文：我们可能每个人要处理1000个问题和纤维定律。  

（注：根据上下文，“fiber laws”可以有不同翻译，此处直接译为“纤维定律”，但具体含义可能需要进一步确认。）  

**02:57:27 - 02:57:33**  
原文：So maybe 5000 jokes that humans have to look at in total, and they just get the ordering.  
译文：所以可能总共需要人类查看5000个笑话， 他们只需要确定这些笑话的顺序。  

**02:57:33 - 02:57:37**  
原文：And then we're training the model to be consistent with that ordering.  
译文：然后我们训练模型以保持这种顺序的一致性。  

**02:57:37 - 02:57:49**  
原文：And I'm skipping over the mathematical details, but I just want you to understand a high level idea that this reward model is basically giving us this course, and we have a way of training it to be consistent with human orderings.  
译文：我跳过了数学细节，但我只是想让你理解一个高层次的概念，即这个奖励模型基本上为我们提供了这种方法，我们有一种方法可以训练它与人类的排序保持一致。  

**02:57:49 - 02:57:52**  
原文：And that's how our lecheworks okay, so that is the rough idea.  
译文：这就是我们的勒奇纳作品的运作方式，好的，这就是大致的想法。  

**02:57:52 - 02:57:57**  
原文：We basically train simulators of humans and rl with respect to those simulators.  
译文：我们基本上是训练人类行为的模拟器以及与这些模拟器相关的强化学习。  

**02:57:57 - 02:58:03**  
原文：Now I want to talk about, first, the upside of reinforcement learning from human feedback.  
译文：现在我想谈谈，首先，人类反馈强化学习的积极方面。  

**02:58:04 - 02:58:17**  
原文：The first thing is that this allows us to run reinforcement learning, which we know is incredibly powerful kind of set of techniques, and it allows us to do it in arbitrary domains and including the ones that are unverifiable.  
译文：第一件事是这使我们能够运行强化学习，我们知道这是一套非常强大的技术，并且它允许我们在任意领域内使用，包括那些无法验证的领域。  

**02:58:17 - 02:58:24**  
原文：So things like summarization and poem writing, joke writing, or any other creative writing, really in domains outside of math and code, etcetera.  
译文：所以像总结、写诗、写笑话或任何其他创意写作，确实是在数学和代码等领域之外的内容。  

**02:58:24 - 02:58:30**  
原文：Now, empirically, what we see when we actually apply rlhf is that this is a way to improve the performance of the model.  
译文：现在，从实际经验来看，当我们真正应用基于人类反馈的强化学习（RLHF）时，我们看到这是一种提高模型性能的方法。  

**02:58:30 - 02:58:44**  
原文：And I have a top answer for why that might be, but I don't actually know that it is like super well established, unlike why this is you can empirically observe that when you do rh correctly, the models you get are just like a little bit better.  
译文：而且我有一个关于为什么会这样的最佳答案，但我并不能确定这是不是已经得到了充分的证实。不像这个，你可以通过实证观察到，当你正确地进行rh时，你得到的模型确实会稍微好一些。  

**02:58:44 - 02:58:47**  
原文：But as to why is I think like not as clear.  
译文：但至于原因，我认为并不是那么清楚。  

**02:58:47 - 02:58:48**  
原文：So here's my best guess.  
译文：所以这里是我的最佳猜测。  

**02:58:48 - 02:58:53**  
原文：My best guess is that this is possibly mostly due to the discriminator generator gap.  
译文：我最好的猜测是，这可能主要归因于判别器生成器差距。  

**02:58:53 - 02:59:01**  
原文：What that means is that in many cases, it is significantly easier to discriminate than to generate for humans.  
译文：这意味着在许多情况下，对于人类来说，辨别比生成要容易得多。  

**02:59:01 - 02:59:14**  
原文：So in particular, an example of this is in when we do supervise fine tuning, right S T, we're asking humans to generate the ideal assistant response.  
译文：所以，特别地，一个例子是在我们进行监督微调时，即ST，我们要求人类生成理想的助手响应。  

**02:59:14 - 02:59:21**  
原文：And in many cases here, as I've shown it, the ideal response is very simple to write, but in many cases might not be.  
译文：在很多情况下，如我所展示的， 理想的回复很容易写出来， 但有很多情况可能并非如此。  

**02:59:21 - 02:59:31**  
原文：So, for example, in summarization, or poem writing or joke writing, like how are you as as a human labeler, supposed to get the ideal response in these cases?  
译文：所以，例如，在摘要、写诗或写笑话时，像你作为一个人类标注者，应该如何在这些情况下获得理想的回应？  

**02:59:31 - 02:59:34**  
原文：It requires creative human writing to do that.  
译文：这需要有创意的人类写作才能完成。  

**02:59:34 - 02:59:40**  
原文：And so rhf kind of sidesteps this because we get to ask people a significantly easier question.  
译文：因此，rhf 有点避开了这个问题，因为我们得以问人们一个简单得多的问题。  

**02:59:40 - 02:59:44**  
原文：As a data labelers, they're not asked to write poems directly.  
译文：作为数据标注员，他们并不会被要求直接写诗。  

**02:59:44 - 02:59:48**  
原文：They're just given five poems from the model and they're just asked to order them.  
译文：他们只是被给了模型生成的五首诗，并且只是被要求对它们进行排序。  

**02:59:48 - 02:59:52**  
原文：And so that's just a much easier task for a human labeler to do.  
译文：所以这对人类标注者来说是一个简单得多的任务。  

**02:59:52 - 03:00:05**  
原文：And so what I think this allows you to do basically, is it kind of like allows a lot more higher accuracy data because we're not asking people to do the generation task, which can be extremely difficult.  
译文：所以，我认为这基本上允许你做的是，它能够提供更高精度的数据，因为我们不需要让人们进行生成任务，而生成任务可能是极其困难的。  

**03:00:05 - 03:00:08**  
原文：Like we're not asking them to do creative writing.  
译文：就像我们不是在要求他们进行创意写作一样。  

**03:00:08 - 03:00:14**  
原文：We're just trying to get them to distinguish between creative writings and find ones that are best.  
译文：我们只是试图让他们区分创意写作，并找到其中最好的作品。  

**03:00:14 - 03:00:18**  
原文：And that is the signal that humans are providing just the ordering.  
译文：这就是人类只提供排序的信号。  

**03:00:18 - 03:00:21**  
原文：And that is their input into the system.  
译文：这就是他们对系统的输入。  

**03:00:21 - 03:00:27**  
原文：And then the system in our chef just discovers the kinds of responses that would be graded well by humans.  
译文：然后我们系统中的厨师模块只是发现了 这些回答会被人类很好的评分。  

**03:00:27 - 03:00:32**  
原文：And so that step of indirection allows the models to become the better.  
译文：这种间接的步骤使模型变得更好。  

**03:00:32 - 03:00:34**  
原文：So that is the upside of rf.  
译文：所以这是rf的好处。  

**03:00:34 - 03:00:36**  
原文：It allows us to run rl.  
译文：它允许我们运行rl。  

**03:00:36 - 03:00:45**  
原文：It empirically results in better models, and it allows people to contribute their supervision even without having to do extremely difficult tasks.  
译文：它实际上能产生更好的模型，并且它允许人们即使在不需要执行极其困难的任务的情况下也能贡献他们的监督。  

**03:00:45 - 03:00:51**  
原文：In the case of writing ideal responses, unfortunately, rhf also comes with significant downsides.  
译文：在撰写理想回答的情况下，不幸的是，rhf也伴随着显著的缺点。  

**03:00:51 - 03:01:02**  
原文：And so the main one is that basically, we are doing reinforcement learning, not with respect to humans and actual human judgment, but with respect to a lossy simulation of humans, right?  
译文：所以最主要的一点是，基本上，我们进行的是强化学习，不是针对人类和实际的人类判断，而是针对人类的有损模拟，对吧？  

**03:01:02 - 03:01:06**  
原文：And this lossy simulation could be misleading because it's just a simulation, right?  
译文：而且这种有损模拟可能会产生误导，因为它只是一个模拟，对吧？  

**03:01:06 - 03:01:15**  
原文：It's just a language model that's kind of outbting scores, and it might not perfectly reflect the opinion of an actual human with an actual brain in all the possible different cases.  
译文：它只是一个生成评分的语言模型，在所有可能的不同情况下，它可能并不能完美反映真正拥有大脑的人类的实际意见。  

**03:01:15 - 03:01:30**  
原文：So that's number one, which is actually something even more subtle and devious going on that really dramatically holds back our lef as a technique that we can really scale to significantly kind of smart systems.  
译文：所以，这是第一点，实际上存在一些更为微妙和狡猾的因素，这些因素确实极大地阻碍了我们的lef作为一种我们可以显著扩展到相当智能系统的技巧。  

**03:01:30 - 03:01:38**  
原文：And that is that reinforcement learning is extremely good at discovering a way to game the model to gain the simulation.  
译文：强化学习非常善于发现一种方法来操纵模型以获得模拟优势。  

**03:01:38 - 03:01:44**  
原文：So this reward model that we're constructing here that gives this course, these models are transformers.  
译文：所以我们在这里构建的这个奖励模型，这些模型是变压器。  

（注意：根据上下文，“transformers”可能指的是“变压器”或“变换器模型”，在人工智能领域通常指的是一种特定类型的深度学习模型。如果是在讨论AI或机器学习，“transformers”应翻译为“变换器模型”。）  

如果你指的是AI领域的“transformers”，那么更准确的翻译应该是：

所以我们在这里构建的这个奖励模型，这些模型是变换器模型。  

**03:01:44 - 03:01:47**  
原文：These transformers are massive neural lets.  
译文：这些变压器是巨大的神经元。  

请注意，原文中的 "neural lets" 可能是拼写错误，通常应为 "neural nets"，意为“神经网络”。如果你指的是后者，那么正确的翻译应该是：

这些变压器是巨大的神经网络。  

**03:01:47 - 03:01:53**  
原文：They have billions of parameters, and they imitate humans, but they do so in the kind of like a simulation way.  
译文：它们拥有数十亿的参数，而且它们模仿人类，但它们的模仿方式有点像模拟。  

**03:01:53 - 03:01:56**  
原文：Now, the problem is that these are massive, complicated systems, right?  
译文：现在，问题在于这些都是巨大的、复杂的系统，对吧？  

**03:01:56 - 03:02:00**  
原文：There's a billion parameters here that are outputting a single score.  
译文：这里有十亿个参数，它们输出一个单一的分数。  

**03:02:00 - 03:02:04**  
原文：It turns out that there are ways to gain these models.  
译文：事实证明，有办法获得这些模型。  

**03:02:04 - 03:02:14**  
原文：You can find kinds of inputs that were not part of their training set, and these inputs inexplicably get very high scores, but in a fake way.  
译文：您可以找到许多不在他们训练集中的输入，这些输入莫名其妙地获得了非常高的分数，但却是以一种虚假的方式。  

**03:02:14 - 03:02:17**  
原文：So very often, what you find if you run our light ture for very long.  
译文：所以，经常发生的是，如果你让我们的灯光装置运行很长时间，你会发现……  

**03:02:17 - 03:02:28**  
原文：So for example, if we do 1000 updates, which is like, say, a lot of updates, you might expect that your jokes are getting better and that you're getting like real bangars about pelicans.  
译文：所以例如，如果我们进行了1000次更新，这就像，比如说，很多次更新，你可能会觉得你的笑话变得更好了，而且你开始讲出关于Pelicans（鹈鹕）的真正好笑的笑话。 

注：这里的“bangars”是非正式用语，意指非常棒或非常好笑的笑话，在中文中没有完全对应的词，因此根据上下文翻译为“真正好笑的笑话”。  

**03:02:28 - 03:02:30**  
原文：But that's not exactly what happens.  
译文：但实际情况并非如此。  

**03:02:30 - 03:02:43**  
原文：What happens is that in the first few hundred steps, the jokes about publilicans are probably improving a little bit, and then they actually dramatically fall off the Cliff and you start to get extremely nonsensical results.  
译文：发生的情况是在前几百步中，关于publilicans的笑话可能有了一点改善，然后它们实际上急剧下降，你开始得到非常不合逻辑的结果。请注意，这里的"publilicans"看起来像是"Republicans"（共和党人）的一个拼写错误，如果上下文与此相关，可能需要修正这一点。  

**03:02:43 - 03:02:48**  
原文：Like for example, you start to get the top joke about pelicans starts to be the, and this makes no sense, right?  
译文：比如，关于鹈鹕的最佳笑话开始变得，这完全没有意义，对吧？  

**03:02:48 - 03:02:52**  
原文：Like when you look at it, why should this be a top joke?  
译文：就像你看它时，为什么这会是一个顶级笑话？  

**03:02:52 - 03:02:56**  
原文：But when you take the the and you plug it into your reward model, youexpect score of zero.  
译文：但当你把定理代入你的奖励模型中时，你期望的得分是零。  

**03:02:56 - 03:03:00**  
原文：But actually the reward model loves this as a joke.  
译文：但事实上，奖励模型很喜欢这个作为笑话。  

**03:03:00 - 03:03:03**  
原文：It will tell you that the, the, the, the, the is a score of 1.0.  
译文：它会告诉你，这，这，这，这，这是1.0分。  

**03:03:03 - 03:03:04**  
原文：This is a top joke.  
译文：这是一个顶级笑话。  

**03:03:04 - 03:03:06**  
原文：And this makes no sense, right?  
译文：这没有意义，对吧？  

**03:03:06 - 03:03:11**  
原文：But it's because these models are just simulations of humans, and they're massive neural nuts.  
译文：但这是因为这些模型只是人类的模拟，而且它们是巨大的神经网络。  

**03:03:11 - 03:03:18**  
原文：And you can find inputs at the bottom that kind of like get into the part of the input space that kind of gives you nonsensical results.  
译文：你可以在底部找到一些输入，这些输入会带你进入输入空间的某个部分，这个部分会产生一些没有意义的结果。  

**03:03:18 - 03:03:26**  
原文：These examples are what's called adversarial examples, and I'm not going to go into the topic too much, but these are adversarial inputs to the model.  
译文：这些例子被称为对抗性例子，我不会太深入这个话题，但这些都是针对模型的对抗性输入。  

**03:03:26 - 03:03:34**  
原文：They are specific little inputs that kind of go between the nooks and crannies of the model and give noncysical results at the top.  
译文：它们是特定的小输入，有点像是进入模型的各个角落和缝隙，并在顶部给出非物理的结果。  

**03:03:34 - 03:03:36**  
原文：Now here's what you might imagine doing.  
译文：现在你可能会想象做以下事情。  

**03:03:36 - 03:03:39**  
原文：You say, okay, the is obviously not score of one.  
译文：你说，好吧，这显然不是一分的得分。  

**03:03:39 - 03:03:40**  
原文：It's obviously a low score.  
译文：显然，这是一个低分。  

**03:03:40 - 03:03:47**  
原文：So let's take the, the, let's add it to the data set and give it an ordering that extremely bad, like a score of five.  
译文：所以让我们将这个添加到数据集中，并给它一个极其糟糕的排序，比如评分是五。  

**03:03:47 - 03:03:53**  
原文：And indeed, your model will learn that the, the, the should have a very low score, and we'll give it score of zero.  
译文：确实，你的模型将学到那个 "the, the, the" 应该有一个非常低的分数，我们将给它零分。  

**03:03:53 - 03:04:00**  
原文：The problem is that there will always be basically infinite number of nonsensical adversarial examples hiding in the model.  
译文：问题在于，模型中总是会隐藏着基本上无限数量的没有意义的对抗性例子。  

**03:04:00 - 03:04:08**  
原文：If you iterate this process many times and you keep adding nonsensical stuff to your reward model, and given a very low course, you'll never win the game.  
译文：如果你重复这个过程很多次，并且不断向你的奖励模型中添加无意义的内容，那么即使给予非常低的标准，你也永远不会赢得游戏。  

**03:04:08 - 03:04:10**  
原文：You can do this many, many rounds.  
译文：你可以做这个很多，很多轮。  

**03:04:10 - 03:04:15**  
原文：And reinforcement learning, if you run it long enough, will always find a way to gain the model.  
译文：强化学习如果运行足够长的时间，总是能找到一种方法来提升模型。  

**03:04:15 - 03:04:17**  
原文：It will discover adversarial examples.  
译文：它将发现对抗性示例。  

**03:04:17 - 03:04:22**  
原文：It will get really high scores with nonsensical results.  
译文：它会因为荒谬的结果而得到非常高的分数。  

**03:04:22 - 03:04:33**  
原文：And fundamentally, this is because our scoring function is a giant neural nut, and rl is extremely good at finding just a ways to triit.  
译文：从根本上说，这是因为我们的评分函数是一个巨大的神经网络，而强化学习（RL）非常擅长找到优化的方法。 

注意：原文中可能存在一些拼写或术语使用不当的地方，例如“neural nut”和“triit”，我根据上下文进行了合理的翻译和解释。如果你有具体的领域知识或者更准确的表述，请告知以便进行更精确的翻译。  

**03:04:33 - 03:04:38**  
原文：So long story short, you always run rhf put for maybe a few hundred updates.  
译文：长话短说，你总是运行 rhf put，可能进行几百次更新。  

**03:04:38 - 03:04:43**  
原文：The model is getting better, and then you have to crop it and you are done.  
译文：模型越来越好，然后你必须裁剪它，就大功告成了。  

**03:04:43 - 03:04:48**  
原文：You can't run too much against this reward model because the optimization will start to game it.  
译文：你不能在这个奖励模型上运行过多，因为优化会开始利用它。  

**03:04:48 - 03:05:00**  
原文：And you basically crop it and you call it and you ship it and you can improve the reward model, but you kind of come across these situations eventually at some point.  
译文：你基本上裁剪它，处理它，发送它，你可以改进奖励模型，但最终你会遇到这种情况。  

**03:05:00 - 03:05:11**  
原文：So our ly chef, basically what I usually say is that rla chef is not rl and what I mean by that is, I mean, rly chef is rl obviously, but it's not rl in the magical sense.  
译文：所以，关于我们的主厨，我通常会说这位主厨并不是真正意义上的真人，我的意思是，显然这位主厨是真实存在的，但并不是以一种神奇的方式存在。  

**03:05:11 - 03:05:14**  
原文：This is not rl that you can run indefinitely.  
译文：这并不是你可以无限期运行的现实生活中的一环。  

**03:05:14 - 03:05:20**  
原文：These kinds of problems, like where you are getting concrete correct answer, you cannot gain this as easily.  
译文：这些问题，比如你在哪里能得到具体的正确答案，你不能这么容易地获得这些。  

**03:05:20 - 03:05:23**  
原文：You either got the correct answer or you didn't.  
译文：你要么得到了正确答案，要么没有。  

**03:05:23 - 03:05:25**  
原文：And the scoring function is much, much simpler.  
译文：而且评分函数简单得多。  

**03:05:25 - 03:05:29**  
原文：You're just looking at the boxed area and seeing if the result is correct.  
译文：你只是看框住的区域，并查看结果是否正确。  

**03:05:29 - 03:05:33**  
原文：So it's very difficult to gain these functions, but gaming a reward model as possible.  
译文：所以，获得这些功能非常困难，但要尽可能地游戏化奖励模型。 

注：原文中的“gaming a reward model”表达不太常见，直译为“游戏化奖励模型”，如果上下文有特定含义，请根据实际情况调整。  

**03:05:33 - 03:05:36**  
原文：Now, in these verifiable domains, you can run rl indefinitely.  
译文：现在，在这些可验证的领域中，您可以无限期地运行rl。  

**03:05:36 - 03:05:54**  
原文：You could run for tens of thousands, hundreds of thousands of steps and discover all kinds of really crazy strategies that we might not even ever think about of performing really well for all these problems in the game of go, there's no way to beat to basically game the winning of a game or losing of a game.  
译文：你可以运行数万、数十万步， 发现各种各样的真正疯狂的策略， 我们可能从未想过 这些策略在围棋游戏中 表现得非常出色。 对于游戏的胜利或失败， 没有办法可以作弊或操控。  

**03:05:54 - 03:05:55**  
原文：We have a perfect simulator.  
译文：我们有一个完美的模拟器。  

**03:05:55 - 03:06:02**  
原文：We know all the different where all the stones are placed, and we can calculate whether someone has won or not.  
译文：我们知道所有不同的位置，所有石头放置的地方，我们可以计算出是否有人赢了。  

**03:06:02 - 03:06:04**  
原文：There's no way to game that.  
译文：没有办法可以操纵它。  

**03:06:04 - 03:06:08**  
原文：And so you can do rl indefinitely, and you can eventually beat even licidull.  
译文：因此，你可以无限期地进行强化学习，并最终甚至可以击败 licidull。  

**03:06:08 - 03:06:14**  
原文：But with models like this, which are gammable, you cannot repeat this process indefinitely.  
译文：但是，使用这种可调节的模型，您不能无限期地重复此过程。  

**03:06:14 - 03:06:19**  
原文：So I kind of see rof as not real rl, because the reward function is gammable.  
译文：所以我觉得ROF并不是真正的RL，因为奖励函数是可以被操控的。  

**03:06:19 - 03:06:22**  
原文：So it's kind of more like in the realm of like little fine tununy.  
译文：所以它更像是在小小的微调领域中。  

**03:06:22 - 03:06:34**  
原文：It's a little it's a little improvement, but it's not something that is fundamentally set up correctly where you can insert more compute, run for longer and get much better and magical results.  
译文：这有一点改进，但并不是从根本上正确设置的，使得你可以插入更多的计算资源，运行更长时间并获得更好、更神奇的结果。  

**03:06:34 - 03:06:36**  
原文：So it's not rl in that sense.  
译文：所以从这个意义上来说，它并不是真正的现实。  

**03:06:36 - 03:06:39**  
原文：It's not rl in a sense that it lacks magic.  
译文：从某种意义上说，它并不真实，因为它缺乏魔法。  

**03:06:39 - 03:06:43**  
原文：It can find you in your model and get a better performance.  
译文：它可以在你的模型中找到你，并获得更好的性能。  

**03:06:43 - 03:06:49**  
原文：And indeed, if we go back to chagpt, the GPT -4o model has gone through rhf because it works well.  
译文：确实，如果我们回顾一下ChatGPT，GPT-4模型已经通过了RhF，因为它表现得很好。 

注意：原文中的"chagpt"可能是"ChatGPT"的拼写错误，"GPT -4o"可能是"GPT-4"的拼写错误，"rhf"可能是"RhF"的拼写错误。我根据上下文进行了合理的修正。如果你有其他意图，请告知。  

**03:06:49 - 03:06:51**  
原文：But it's just not rl in the same sense.  
译文：但它的意思在同样的意义上只是不是现实生活。  

（注：根据原文直译，这句话 somewhat 不太通顺。可能的更正为：“但这并不是在同一个意义上的现实生活。”）  

**03:06:51 - 03:06:58**  
原文：Rh chef is like a little fine tune that slightly improves your model, is maybe like the way I would think about it.  
译文：Rh chef 就像一个小的微调，稍微改进你的模型，也许这就是我思考问题的方式。  

**03:06:58 - 03:06:58**  
原文：Okay.  
译文：好的。  

**03:06:58 - 03:07:02**  
原文：So that's most of the technical content that I wanted to cover.  
译文：所以这是我想涵盖的大部分技术内容。  

**03:07:02 - 03:07:09**  
原文：I took you through the three major stages and paradigms of training these models, pre training, supervised fine tuning, and reinforcement learning.  
译文：我带你了解了训练这些模型的三个主要阶段和范式：预训练、监督微调和强化学习。  

**03:07:09 - 03:07:14**  
原文：And I showed you that they loosely correspond to the process we already use for teaching children.  
译文：而且我向您展示它们大致对应于我们已经用于教导儿童的过程。  

**03:07:14 - 03:07:28**  
原文：And so in particular, we talked about pre training being sort of like the basic knowledge acquisition of reading exposition, supervised fine tunbeing, the process of looking at lots and lots of worked examples and imitating experts and practice problems.  
译文：因此，特别地，我们讨论了预训练就像通过阅读说明来获取基本知识，监督微调则是查看大量例题和模仿专家以及练习题的过程。  

**03:07:28 - 03:07:42**  
原文：The only difference is that we now have to effectively write textbooks for llms and ais across all the disciplines of human knowledge, and also in all the cases where we actually would like them to work, like code and math and you know, basically all the other disciplines.  
译文：唯一的不同是我们现在必须有效地为所有人类知识学科的大型语言模型和人工智能编写教材，也包括在所有我们希望它们能够实际发挥作用的情况中，比如编程、数学以及基本上其他所有学科。  

**03:07:42 - 03:07:55**  
原文：So we're in the process of writing textbooks for them, refining all the algorithms that I've presented on the high level and then, of course, doing a really, really good job at the execution of training these models at scale and efficiently.  
译文：所以我们正在为他们编写教科书，完善我所介绍的所有高层次的算法，当然，还要在大规模和高效地训练这些模型方面做得非常出色。  

**03:07:55 - 03:08:09**  
原文：So in particular, I didn't go into too many details, but these are extremely large and complicated distributed sort of jobs that have to run over tens of thousands or even hundreds of thousands of gps.  
译文：所以，特别地，我没有深入太多细节， 但这些工作是非常庞大和复杂的分布式任务， 必须在成千上万，甚至数十万个GPS上运行。  

**03:08:09 - 03:08:13**  
原文：And the engineering that goes into this is really at the state of the arof.  
译文：这里面涉及的工程学  
真的是一门尖端技术。  
（注：原句中的"state of the arof"可能是"state of the art"的误写，意为“最先进的，最新的”，翻译时进行了修正。）  

**03:08:13 - 03:08:15**  
原文：What's possible with computers at that scale.  
译文：在那个规模下，计算机能做些什么。  

**03:08:15 - 03:08:26**  
原文：So I didn't cover that aspect too much, but this is a very kind of serious enof underlying all these very simple algorithms ultimately.  
译文：所以这方面我并没有过多涉及， 但这是一个非常严肃的问题， 尽管所有这些算法看起来都很简单， 其实背后有着深刻的内涵。  

**03:08:26 - 03:08:30**  
原文：Now, I also talked about, sort of like the theory of mind, a little bit of these models.  
译文：现在，我还谈到了，类似于心智理论，这些模型的一些内容。  

**03:08:30 - 03:08:37**  
原文：And the thing I want you to take away is that these models are really good, but they're extremely useful as tools for your work.  
译文：我希望你带走的信息是，这些模型确实非常好，但作为你工作的工具，它们极其有用。  

**03:08:37 - 03:08:38**  
原文：You shouldn't sort of trust them fully.  
译文：你不应该完全信任他们。  

**03:08:38 - 03:08:40**  
原文：And I showed you some examples of that.  
译文：并且我给你展示了一些例子。  

**03:08:40 - 03:08:50**  
原文：Even though we have mitigations for hallucinations, the models are not perfect and they will hallucinate still, it's gotten better over time and it will continue to get better, but they can hallucinate.  
译文：即使我们已经采取了措施来减轻幻觉现象，这些模型仍然不完美，它们仍然会产生幻觉。这种情况随着时间的推移已经有所改善，并且将继续改进，但它们仍然可能会产生幻觉。  

**03:08:50 - 03:08:59**  
原文：In other words, in addition to that, I covered kind of like what I call the Swiss cheese sort of model of elone capabilities that you should have in your mind.  
译文：换句话说，除此之外，我还涵盖了我称之为瑞士奶酪模型的elon能力，你应该在脑海中有所了解。 

注：此处的“elone capabilities”可能是“alone capabilities”或“Elon（人名，如埃隆·马斯克）相关的能力”，根据上下文可能需要调整。如果你指的是埃隆·马斯克（Elon Musk）相关的能力，请告知以便更准确地翻译。  

**03:08:59 - 03:09:05**  
原文：The mare incredibly good across so many different disciplines, but then fail randomly, almost in some unique cases.  
译文：这匹母马在如此多的不同学科中表现出色，但随后会随机失败，在某些独特的情况下几乎就是这样。  

**03:09:05 - 03:09:08**  
原文：So for example, what is bigger, nine point eleven or 9.9?  
译文：所以，例如，哪个更大，九点十一还是9.9？  

**03:09:08 - 03:09:13**  
原文：Like the model doesn't know, but simultaneously it can turn around and solve Olympiad questions.  
译文：就像模型不知道一样，但它同时可以转身解决奥林匹克竞赛题目。  

**03:09:13 - 03:09:18**  
原文：And so this is a hole in the Swiss cheese, and there are many of them, and you don't want to trip over them.  
译文：所以这就是瑞士奶酪上的一个洞，有很多这样的洞，你可不想被它们绊倒。  

**03:09:18 - 03:09:23**  
原文：So don't treat these models as infallible models.  
译文：所以不要把这些模型当作是绝对可靠的模型。  

**03:09:23 - 03:09:24**  
原文：Check their work.  
译文：检查他们的工作。  

**03:09:24 - 03:09:25**  
原文：Use them as tools.  
译文：将它们用作工具。  

**03:09:25 - 03:09:35**  
原文：Use them for inspiration, use them for the first draft, but work with them as tools and be ultimately responsible for the product of your work.  
译文：将它们用于获取灵感，将它们用于初稿，但要将它们作为工具使用，并对你的工作成果负最终责任。  

**03:09:35 - 03:09:38**  
原文：And that's roughly what I wanted to talk about.  
译文：这基本上就是我想谈论的内容。  

**03:09:38 - 03:09:40**  
原文：This is how they're trained and this is what they are.  
译文：这就是他们接受的训练，这就是他们的本质。  

**03:09:40 - 03:09:48**  
原文：Let's now turn to what are some of the future capabilities of these models, probably what's coming down the pipe, and also where can you find these models?  
译文：现在让我们来看看这些模型的一些未来功能，可能即将推出的功能，以及你可以在哪里找到这些模型？  

**03:09:48 - 03:09:53**  
原文：I have a few bullet points on some of the things that you can expect coming down the pipe.  
译文：我有一些项目符号列出了一些您可以预期的事情。  

**03:09:53 - 03:09:58**  
原文：The first thing you'll notice is that the models will very rapidly become multimodal.  
译文：您首先会注意到的是，这些模型将非常迅速地成为多模态。  

**03:09:58 - 03:10:10**  
原文：Everything I've talked about, about concerned text, but very soon we'll have all umthat can not just handle text, but they can also operate natively and very easily over audio, so they can hear and speak, and also images so they can see and paint.  
译文：我刚才提到的所有内容 都是关于处理文本的， 但很快我们将拥有可以 不仅处理文本， 还能直接且轻松地处理音频的工具， 因此它们能够听取和说话， 同时也能处理图像，使它们能够看见和绘制。  

**03:10:10 - 03:10:13**  
原文：And we're already seeing the beginnings of all of this.  
译文：而且我们已经看到所有这些的雏形。  

**03:10:13 - 03:10:19**  
原文：But this will be all done natively inside the language model, and this will enable kind of like natural conversations.  
译文：但这都将在语言模型内部以原生方式完成，这将能够实现类似自然的对话。  

**03:10:19 - 03:10:33**  
原文：And roughly speaking, the reason that this is actually no different from everything we've covered above is that as a baseline, you can tokenize audio and images and apply the exact same approaches of everything that we've talked about above.  
译文：大致来说，这实际上与我们上面所涵盖的所有内容并无不同，原因是，作为基础，你可以将音频和图像进行分词，并应用我们上面讨论过的所有相同的方法。  

**03:10:33 - 03:10:35**  
原文：So it's not a fundamental change.  
译文：所以这并不是一个根本性的改变。  

**03:10:35 - 03:10:38**  
原文：It's just it's just we have to add some tokens.  
译文：只是我们得添加一些代币。  

**03:10:38 - 03:10:52**  
原文：So as an example for tokenizing audio, we can look at slices of the spectrogram of the audio signal, and we can tokenize that and just add more tokens that suddenly represent audio and just add them into the context windows and train on them, just like above.  
译文：因此，作为音频分词的一个例子，我们可以查看音频信号的频谱图切片，对其进行分词，并添加更多的代表音频的分词，将它们加入到上下文窗口中进行训练，就像上面所述的一样。  

**03:10:52 - 03:10:57**  
原文：The same for images, we can use patches and we can a separately tokenized patches.  
译文：对于图像，我们也可以使用 patches，并且可以分别对这些 patches 进行标记化。  

**03:10:57 - 03:10:58**  
原文：And then what is an image?  
译文：那么，什么是图像呢？  

**03:10:58 - 03:11:00**  
原文：An image is just a sequence of tokens.  
译文：图像是令牌序列。  

**03:11:00 - 03:11:02**  
原文：And this actually kind of works.  
译文：而且这实际上有点效果。  

**03:11:02 - 03:11:05**  
原文：And there's a lot of early work in this direction.  
译文：在这方面有很多早期的工作。  

**03:11:05 - 03:11:14**  
原文：And so we can just create streams of tokens that are representing audio, images as well as text and intersperse them and handle them all simultaneously in a single model.  
译文：因此，我们可以创建代表音频、图像和文本的令牌流，并将它们交织在一起，在单个模型中同时处理它们。  

**03:11:14 - 03:11:16**  
原文：So that's one example of multimodality.  
译文：所以这是一个多模态的例子。  

**03:11:16 - 03:11:29**  
原文：Second, something that people are very interested in is currently most of the work is that we're handing individual tasks to the models on kind of like a silver platter, like please solve this task for me.  
译文：第二，人们非常感兴趣的一点是，目前大部分工作是我们将单独的任务像放在银盘里一样交给模型，像是请模型为我们解决这个任务。  

**03:11:29 - 03:11:38**  
原文：And the model sort of like does this little task, but it's up to us to still sort of like organize a coherent execution of tasks to perform jobs.  
译文：而且模型可以执行这类小任务， 但是仍然需要我们来组织 协调这些任务的执行以完成工作。  

**03:11:38 - 03:11:45**  
原文：And the models are not yet at the capability required to do this in a coherent error correcting way over long periods of time.  
译文：而且这些模型还未能具备在长时间内以连贯的方式进行纠错所需的能力。  

**03:11:45 - 03:11:54**  
原文：So they're not able to fully strink together tasks to perform these longer running jobs, but they're getting there and this is improving over time.  
译文：所以他们目前还无法完全将任务串联起来以执行这些长时间运行的作业，但他们正在逐步实现这一目标，而且这种情况随着时间的推移正在改善。  

**03:11:54 - 03:12:01**  
原文：But probably what's going to happen here is we're going to start to see what's called agents, which perform tasks over time.  
译文：但很可能发生的情况是， 我们将会开始看到所谓的代理， 这些代理可以执行随时间推移的任务。  

**03:12:01 - 03:12:07**  
原文：And you supervise them and you watch their work and they come up to once in a while, report progress and so on.  
译文：你来监督他们，观察他们的工作，偶尔他们会来汇报进展等。  

**03:12:07 - 03:12:15**  
原文：So we're going to see more, longer running agents tasks that don't just take a few seconds of response, but many tens of seconds or even minutes or hours over time.  
译文：所以我们将看到更多运行时间更长的代理任务，这些任务不仅仅是几秒的响应时间，而是几十秒，甚至几分钟或几小时。  

**03:12:15 - 03:12:19**  
原文：But these models are not infallible, as we talked about above.  
译文：但这些模型并非万无一失，正如我们上面所讨论的。  

**03:12:19 - 03:12:22**  
原文：So all of this will require supervision.  
译文：所以所有这些都将需要监督。  

**03:12:22 - 03:12:26**  
原文：So for example, in factories, people talk about the human to robot ratio for automation.  
译文：所以，例如，在工厂里，人们谈论的是人与机器人的比例用于自动化。  

**03:12:26 - 03:12:38**  
原文：I think we're going to see something similar in the digital space where we are going to be talking about human to agent ratios, where humans becomes a lot more supervisors of eggentic tasks in the digital domain.  
译文：我认为在数字空间中我们会看到类似的情况，我们将讨论人与代理的比例，在数字领域中，人类将成为更多蛋entic任务的监督者。  

注：此处的“eggentic”并非标准英文单词，可能是原文中的拼写错误或特定术语，请确认其正确含义以便更准确的翻译。  

**03:12:38 - 03:12:44**  
原文：Next, I think everything is going to become a lot more pervasive and invisible.  
译文：接下来，我认为一切都会变得更加普遍和无形。  

**03:12:44 - 03:12:51**  
原文：So it's kind of like integrated into the tools and everywhere and in addition, kind of like computer using.  
译文：所以它有点像被集成到各种工具中，无处不在，另外，有点像在使用计算机。  

**03:12:51 - 03:12:55**  
原文：So right now these models aren't able to take actions on your behalf.  
译文：所以目前这些模型还无法代表您采取行动。  

**03:12:55 - 03:12:58**  
原文：But I think this is a separate bullet point.  
译文：但我认为这是一个单独的项目符号。  

**03:12:58 - 03:13:08**  
原文：If you search achiblaunch the operator, then that's one early example of that where you can actually hand off control to the model to perform you know keyboard and mouse actions on your behalf.  
译文：如果你搜索 achiblaunch 这个操作符，那么这就是一个早期的例子，你可以实际将控制权交给模型，让它代表你执行键盘和鼠标的动作。  

**03:13:08 - 03:13:11**  
原文：So that's also something that I think is very interesting.  
译文：所以这也是一件我觉得非常有趣的事情。  

**03:13:11 - 03:13:18**  
原文：The last point I have here is just a general comment that there's still a lot of research to potentially do in this domain.  
译文：我这里的最后一点只是一个一般的评论，即在这个领域仍然有可能进行大量的研究。  

**03:13:18 - 03:13:22**  
原文：One example of that is something along the lines of test time training.  
译文：一个例子是类似于测试时间训练的东西。  

**03:13:22 - 03:13:26**  
原文：So remember that everything we've done above and that we talked about has two major stages.  
译文：所以请记住，我们上面所做的和讨论的所有内容都有两个主要阶段。  

**03:13:26 - 03:13:32**  
原文：There's first, the training stage where we tune the parameters of the model to perform the tasks well.  
译文：首先是训练阶段，我们在这一阶段调整模型的参数以使其能够很好地执行任务。  

**03:13:32 - 03:13:37**  
原文：Once we get the parameters, we fixed them and then we deploy the model for inference.  
译文：一旦我们获得了参数，我们就固定它们，然后部署模型进行推理。  

**03:13:37 - 03:13:38**  
原文：From there, the model is fixed.  
译文：从那里开始，模型就被固定了。  

**03:13:38 - 03:13:39**  
原文：It doesn't change anymore.  
译文：它不会再改变了。  

**03:13:39 - 03:13:42**  
原文：It doesn't learn from all the stuff that is doing at test time.  
译文：它并不会从所有在测试时进行的事情中学习。  

**03:13:42 - 03:13:44**  
原文：It's a fixed number of parameters.  
译文：它是参数的固定数量。  

**03:13:44 - 03:13:49**  
原文：And the only thing that is changing is now the tokens inside the context windows.  
译文：唯一改变的是现在上下文窗口中的标记。  

**03:13:49 - 03:14:00**  
原文：And so the only type of learning or test time learning that the model has access to is the in context learning of its kind of like dynamically adjustable context window depending on like what it's doing at test time.  
译文：因此，模型在测试时唯一可以进行的学习类型是其上下文学习，这种学习的上下文窗口可以根据测试时的具体情况动态调整。  

**03:14:00 - 03:14:12**  
原文：But I think this is still different from humans who actually are able to like actually learn depending on what they're doing, especially when you sleep, for example, like your brain is updating your parameters or something like that, right?  
译文：但是我认为这与人类实际能够根据自己的行为进行学习还是有所不同，尤其是在你睡觉的时候，比如你的大脑会更新它的参数之类的，是吧？  

**03:14:12 - 03:14:16**  
原文：So there's no kind of equivalent of that currently in these models and tools.  
译文：所以这些模型和工具目前都没有类似的等价物。  

**03:14:16 - 03:14:20**  
原文：So there's a lot of like more wonky ideas, I think, that are to be explored still.  
译文：所以，还有很多更有趣的想法，我认为，仍有待探索。  

**03:14:20 - 03:14:26**  
原文：And in particular, I think this will be necessary because the context window is a finite and precious resource.  
译文：并且特别地，我认为这将是必要的，因为上下文窗口是一种有限且宝贵的资源。  

**03:14:26 - 03:14:39**  
原文：And especially once we start to tackle very long running multimodal tasks and we're putting in videos and these token windows will basically start to grow extremely large, like not thousands or even hundreds of thousands, but significantly beyond that.  
译文：并且特别是当我们开始处理非常长时间的多模态任务时，我们加入视频，这些 token 窗口基本上会变得极其庞大，不是成千上万，甚至不是几十万，而是远超于此。  

**03:14:39 - 03:14:45**  
原文：And the only trick, the only kind of trick we have a available to us right now is to make the context windows longer.  
译文：目前我们唯一可用的技巧，就是让上下文窗口变得更长。  

**03:14:45 - 03:14:51**  
原文：But I think that, that approach by itself will not scale to actual long running tasks that are multimodal over time.  
译文：但我认为，仅靠这种方法无法扩展到实际的长时间运行任务，这些任务随着时间的推移是多模式的。  

**03:14:51 - 03:15:01**  
原文：And so I think new ideas are needed in some of those disciplines, in some of those kind of cases, in domains where these tasks are going to require very long contexts.  
译文：因此，我认为在某些学科中，在某些类型的案例中，在这些任务需要非常长的上下文的领域中，需要新的想法。  

**03:15:01 - 03:15:06**  
原文：So those are some examples of some of the things you can expect coming down the pipe.  
译文：所以这些是一些你可以预期的事情的例子。  

**03:15:06 - 03:15:15**  
原文：Let's not turn to where you can actually kind of keep track of this progress and be up to date with the latest and Grace of what's happening in the field.  
译文：让我们不要转向你可以实际跟踪这种进展并跟上领域内最新动态和恩典的地方。  

（注：原文中的“Grace”一词在此语境下翻译 somewhat 不明确，可能是指“最新进展的恩惠/优雅”或者是一个名为Grace的人，根据上下文可能需要调整。）  

如果需要更准确的翻译，请提供更多的上下文信息。  

**03:15:15 - 03:15:21**  
原文：So I would say the three resources that I have consistently used to stay up to date are, number one, Ella marina.  
译文：所以我可以说，我一直用来保持更新的三个资源是，第一，Ella marina。  

**03:15:21 - 03:15:23**  
原文：So let me show you Ella marina.  
译文：那么让我给你介绍一下Ella marina。  

**03:15:24 - 03:15:28**  
原文：This is basically an llm leader board and it ranks all the top models.  
译文：这基本上是一个大型语言模型排行榜，它列出了所有顶级模型的排名。  

**03:15:28 - 03:15:30**  
原文：And the ranking is based on human comparisons.  
译文：排名是基于人类的比较。  

**03:15:30 - 03:15:35**  
原文：So humans prompt these models, and they get to judge which one gives a better answer.  
译文：所以人类提示这些模型，然后他们可以判断哪个给出了更好的答案。  

**03:15:35 - 03:15:36**  
原文：They don't know which model is which.  
译文：他们不知道哪个模型是哪个。  

**03:15:36 - 03:15:39**  
原文：They're just looking at which model is a better answer.  
译文：他们只是在看哪个模型是更好的答案。  

**03:15:39 - 03:15:43**  
原文：And you can calculate a ranking and then you get some results.  
译文：然后你可以计算一个排名，接着你就会得到一些结果。  

**03:15:43 - 03:15:50**  
原文：And so what you can hear is what you can see here is the different organizations like gogem and I, for example, that produce these models.  
译文：所以你所听到的，就是你在这里看到的不同组织，比如gogem和我，所生产的这些模型。  

**03:15:50 - 03:15:55**  
原文：When you click on any one of these, it takes you to the place where that model is hosted.  
译文：当你点击其中任何一个时，它会带你到托管该模型的地方。  

**03:15:55 - 03:15:59**  
原文：And then here we see goois currently on top with OpenAI right behind.  
译文：然后在这里我们看到GoOIS目前处于领先地位，OpenAI紧随其后。  

**03:15:59 - 03:16:02**  
原文：Here we see deep seek in position number three.  
译文：在这里，我们在第三位看到了深度搜索。  

**03:16:02 - 03:16:05**  
原文：Now the reason this is a big deal is the last column.  
译文：现在这件事之所以很重要，是因为最后一列。  

**03:16:05 - 03:16:06**  
原文：Here you see a license.  
译文：在这里，您看到的是一份许可证。  

**03:16:06 - 03:16:08**  
原文：Deep seek is an mit licensed model.  
译文：Deep seek 是一个采用 MIT 许可证的模型。  

**03:16:08 - 03:16:09**  
原文：It's open weights.  
译文：它是公开重量级。  

**03:16:09 - 03:16:10**  
原文：Anyone can use these weights.  
译文：任何人都可以使用这些权重。  

**03:16:10 - 03:16:12**  
原文：Anyone can download them.  
译文：任何人都可以下载它们。  

**03:16:12 - 03:16:17**  
原文：Anyone can host their own version of deep seek, and they can use it in whatever way they like.  
译文：任何人都可以托管他们自己的 deep seek 版本，而且他们可以随意使用它。  

**03:16:17 - 03:16:20**  
原文：And so it's not a proprietary model that you don't have access to it.  
译文：因此，它不是你无法访问的专有模型。  

**03:16:20 - 03:16:22**  
原文：It's basically an open weights release.  
译文：基本上是一个开放权重发布。  

**03:16:22 - 03:16:30**  
原文：And so this is kind of unprecedented that a model this strong was released with open weights.  
译文：因此，这种强大的模型以开放权重发布是前所未有的。  

**03:16:30 - 03:16:32**  
原文：So pretty cool from the team.  
译文：团队做得非常棒。  

**03:16:32 - 03:16:35**  
原文：Next up, we have a few more models from and OpenAI.  
译文：接下来，我们还有几个来自 OpenAI 的模型。  

**03:16:35 - 03:16:41**  
原文：And then when you continue to scroll down, you start to see some other usual suspects.  
译文：然后当你继续向下滚动时，你开始看到一些其他常见的嫌疑对象。  

**03:16:41 - 03:16:45**  
原文：So xai here, anthropic was sonnet here at number 14.  
译文：所以这里提到的，anthropic在第14位出现了。  

**03:16:45 - 03:16:45**  
原文：And.  
译文：和。  

**03:16:46 - 03:16:47**  
原文：Then meta with llama over here.  
译文：然后在这里与 llama 进行元讨论。  

**03:16:47 - 03:16:51**  
原文：So lama, similar to deep sik, is an open weights model.  
译文：所以，lama 类似于 deep sik，是一个开放权重模型。  

**03:16:51 - 03:16:54**  
原文：And so but it's down here as opposed to up here.  
译文：而是它在这里，而不是在那里。  

**03:16:54 - 03:16:59**  
原文：Now, I will say that this leader board was really good for a long time.  
译文：现在，我要说这个排行榜在很长一段时间里都真的很好。  

**03:16:59 - 03:17:07**  
原文：I do think that in the last few months, it's become a little bit gamed, and I don't trust it as much as I used to.  
译文：我确实认为在过去的几个月里，它变得有点被操纵了，而且我也不像以前那样信任它了。  

**03:17:07 - 03:17:20**  
原文：I think just empirically, I feel like a lot of people, for example, are using sonnet from anthropic and that it's a really good model, but that's all the way down here in number 14.  
译文：我认为仅从经验来看，我感觉很多人，例如，都在使用Anthropic的Sonnet模型，并且它是一个非常好的模型，但它在这里只排在第14位。  

**03:17:20 - 03:17:26**  
原文：And conversely, I think not as many people are using Gemini, but it's reckking really, really high.  
译文：相反，我认为使用Gemini的人并不多，但它的发展却非常高。 

注：原文中的"reckking"可能是拼写错误或者是某种口语表达，根据上下文理解翻译为“发展”。如果需要更准确的翻译，请确认该词的具体含义。  

**03:17:26 - 03:17:35**  
原文：So I think use this as a first PaaS, but sort of try out a few of the models for your tasks and see which one performs better.  
译文：所以我认为应该把这作为第一个PaaS平台，但也要尝试一些不同的模型来处理你的任务，看看哪个表现更好。  

**03:17:35 - 03:17:39**  
原文：The second thing that I would point to is the AI newsletter.  
译文：第二件我想指出的是AI通讯。  

**03:17:39 - 03:17:44**  
原文：So AI news is not very creatively named, but it is a very good newsletter produced by swws and friends.  
译文：所以，AI新闻的命名并不非常有创意，但它是由swws和朋友们制作的一份非常好的通讯。  

**03:17:44 - 03:17:46**  
原文：So thank you for maintaining it.  
译文：所以谢谢你维护它。  

**03:17:46 - 03:17:50**  
原文：And it's been very helpful to me because it is extremely comprehensive.  
译文：它对我来说非常有帮助，因为它极其全面。  

**03:17:50 - 03:17:56**  
原文：So if you go to archives, you see that it's produced almost every other day, and it is very comprehensive.  
译文：所以如果你查看档案，你会发现它几乎是每隔一天就更新一次，而且内容非常全面。  

**03:17:56 - 03:18:02**  
原文：And some of it is written by humans and curiby humans, but a lot of it is constructed automatically with llms.  
译文：其中一些是由人类编写和由人类好奇的，但其中很多是通过大型语言模型自动构建的。  

（注：根据上下文，“curiby”可能为“curated by”之误，意为“由……策划/整理”，如果这是正确的，则应翻译为：“其中一些是由人类编写和由人类整理的，但其中很多是通过大型语言模型自动构建的。”）  

**03:18:02 - 03:18:09**  
原文：You'll see that these are very comprehensive, and you're probably not missing anything major if you go through it.  
译文：您会发现这些内容非常全面，而且如果您仔细阅读，很可能不会错过任何重要的东西。  

**03:18:09 - 03:18:13**  
原文：Of course, you're probably not going to go through it this so long.  
译文：当然，你可能不会花这么长时间来经历它。  

**03:18:13 - 03:18:18**  
原文：But I do think that these summaries all the way up top are quite good and I think have some human oversight.  
译文：但我确实认为这些位于顶部的总结都非常好，而且我认为它们有一些人工监督。  

**03:18:18 - 03:18:20**  
原文：So this has been very helpful to me.  
译文：所以这对我非常有帮助。  

**03:18:20 - 03:18:23**  
原文：And the last thing I would point to is just x and Twitter.  
译文：我要指出的最后一件事就是 x 和 Twitter。  

**03:18:23 - 03:18:30**  
原文：A lot of AI happens on x, and so I would just follow people who like and trust and get all your latest and greatest on x at all.  
译文：很多人工智能的工作都在x上进行，所以我会关注那些喜欢、信任并在x上获取所有最新最好的内容的人。  

**03:18:30 - 03:18:34**  
原文：So those are the major places that have worked for me over time.  
译文：所以这些就是随着时间推移对我有效的主要地方。  

**03:18:34 - 03:18:38**  
原文：And finally, a few words on where you can find the models and where can you use them.  
译文：最后，关于你可以在哪里找到这些模型以及可以在哪里使用它们，说几句。  

**03:18:38 - 03:18:45**  
原文：So the first one I would say is for any of the biggest proprietary models, you just have to go to the web site of that lm provider.  
译文：所以第一个我认为是针对任何最大的专有模型，你只需要去该语言模型提供商的网站。  

**03:18:45 - 03:18:49**  
原文：So for example, for OpenAI, that's chat dot com I believe actually works now.  
译文：所以，例如，对于OpenAI，我相信现在 chat.dot.com 实际上已经可以使用了。 

注：根据上下文和常规理解进行翻译，"chat dot com" 理解为 "chat.openai.com" 更为准确，但按照字面翻译为 "chat.dot.com"。  

**03:18:49 - 03:18:51**  
原文：So that's for OpenAI now.  
译文：所以这就是现在的OpenAI。  

**03:18:51 - 03:18:55**  
原文：Or you know for Gemini, I think it's Gemini dot Godot com or AI studio.  
译文：或者你知道对于Gemini，我认为是Gemini.AI Studio或Gemini.dot Godot com。  

**03:18:55 - 03:18:56**  
原文：I think they have two.  
译文：我认为他们有两个。  

**03:18:56 - 03:19:00**  
原文：For some reason that I definitely understand, no one does.  
译文：出于某种我可以理解的原因，没有人这样做。  

**03:19:00 - 03:19:06**  
原文：For the open weights models like deep sea, columa et cec, you have to go to some kind of an inference provider of lms.  
译文：对于像深海、columa et cec这样的开放权重模型，您必须去寻找某种形式的LMS推理提供者。  

**03:19:06 - 03:19:08**  
原文：So my favorite one is together that AI.  
译文：所以我的最爱是与AI共同创作的那个。  

**03:19:08 - 03:19:15**  
原文：And I showed you that when you go to the playground of together that AI, then you can sort of pick lots of different models.  
译文：我向你展示了当你一起去那个AI的游乐场时，你可以选择许多不同的模型。  

**03:19:15 - 03:19:18**  
原文：And all of these are open models of different types.  
译文：而且所有这些是不同类型的开放模型。  

**03:19:18 - 03:19:21**  
原文：And you can talk to them here as an example.  
译文：并且你可以在这里与他们交谈，作为一个例子。  

**03:19:21 - 03:19:32**  
原文：Now if youlike to use a base model like you know a base model, then this is where I think it's not as common to find base models even on these inference providers.  
译文：现在，如果你喜欢使用基础模型，比如你知道的基础模型，那么我认为在这种情况下，即使在这些推理提供商处，也不太容易找到基础模型。  

**03:19:32 - 03:19:35**  
原文：They are all targeting assistance and chat.  
译文：它们都针对援助和聊天。  

**03:19:35 - 03:19:38**  
原文：And so I think even here I can see base models here.  
译文：因此，我认为即使在这里，我也可以看到基础模型。  

**03:19:38 - 03:19:44**  
原文：So for base models, I usually go to a hyperbolic because they serve my llama 3.1 base.  
译文：所以对于基础模型，我通常会选择双曲模型，因为它们适用于我的lama 3.1基础模型。  

**03:19:44 - 03:19:47**  
原文：And I love that model and you can just talk to it here.  
译文：而且我喜欢那个模型，你可以直接在这里与它对话。  

**03:19:47 - 03:19:50**  
原文：So as far as I know, this is a good place for a base model.  
译文：就我所知，这是一个基础模型的好地方。  

**03:19:50 - 03:19:56**  
原文：And I wish more people hosted base models because they are useful and interesting to work with in some cases.  
译文：我希望更多的人托管基础模型，因为在某些情况下，它们很有用且有趣。  

**03:19:56 - 03:20:01**  
原文：Finally, you can also take some of the models that are smaller and you can run them locally.  
译文：最后，你也可以选择一些较小的模型，并可以在本地运行它们。  

**03:20:01 - 03:20:11**  
原文：And so for example, deep seek of the biggest model, you're not going to be able to run locally on your MacBook, but there are smaller versions of the deep seek model that are what's called distilled.  
译文：例如，对于最大的深度搜索模型，您将无法在您的MacBook上本地运行，但存在较小版本的深度搜索模型，这些被称为蒸馏模型。  

**03:20:11 - 03:20:15**  
原文：And then also you can run these models that's smaller precision.  
译文：然后你还可以运行这些精度较低的模型。  

**03:20:15 - 03:20:21**  
原文：So not at the native precision of, for example, fp eight on deep sek or bf 16 lama, but much, much lower than that.  
译文：所以不是以原生精度，例如深思的fp8或bf16 Lama，而是比那个低得多，低得多。 

注：根据上下文，“deep sek”可能是指某种特定的技术或产品名称，这里按照音译处理为“深思”。如果存在更准确的翻译或者专有名词，请根据实际情况进行调整。  

**03:20:21 - 03:20:31**  
原文：And don't worry if you don't fully understand those details, but you can run smaller versions that have been distilled and then at even lower precision, and then you can fit them on your computer.  
译文：而且如果你不完全理解那些细节也不要担心，你可以运行已经被简化的小版本，然后以更低的精度运行，这样你就可以在你的电脑上使用它们。  

**03:20:31 - 03:20:35**  
原文：And so you can actually run pretty okay models on your laptop.  
译文：因此，你实际上可以在你的笔记本电脑上运行相当不错的模型。  

**03:20:35 - 03:20:40**  
原文：And my favorite, I think place I go to usually is alm studio, which is basically an app you can get.  
译文：我最喜欢的，我认为我通常去的地方是alm studio，这基本上是一个你可以获取的应用程序。  

**03:20:40 - 03:20:42**  
原文：And I think it kind of actually looks really ugly.  
译文：而且我认为它实际上看起来非常丑陋。  

**03:20:42 - 03:20:46**  
原文：And it's I don't like that it shows you all these models that are basically not that useful.  
译文：而且我不喜欢它给你展示的所有这些基本上没什么用的模型。  

**03:20:46 - 03:20:48**  
原文：Like everyone just wants to run deep seek.  
译文：就像每个人都只想深入探寻。  

**03:20:48 - 03:20:52**  
原文：So I don't know why they give you these 500 different types of models.  
译文：所以我不知道他们为什么给你这500种不同的模型。  

**03:20:52 - 03:21:00**  
原文：They're really complicated to search for and you have to choose different distillations and different precisions, and it's all really confusing.  
译文：它们非常难以搜索，你必须选择不同的蒸馏和不同的精度，这一切都真的很令人困惑。  

**03:21:00 - 03:21:11**  
原文：But once you actually understand how it works, and that's a whole separate video, then you can actually load up a model, like here, I load it up a lama 3.2, instruct 1 billion, and you can just talk to it.  
译文：但是一旦你真正理解了它是如何工作的，而这是一个完全单独的视频，然后你实际上可以加载一个模型，比如在这里，我加载了一个lama 3.2， instruct 1 billion，你可以直接与它对话。 

注意：根据上下文，“instruct 1 billion”这部分可能是指模型的参数量或者某种特定配置，直译为“指令10亿”可能不符合实际情况，通常这可能是指模型有10亿个参数。如果需要更准确的翻译，可能需要更多背景信息。  

**03:21:11 - 03:21:17**  
原文：So I ask for pelican jokes and I can ask for another one, and it gives me another one, etc..  
译文：所以我可以要鹈鹕的笑话，我还可以再要一个，然后它会给我另一个，等等。  

**03:21:17 - 03:21:20**  
原文：All of this that happens here is locally on your computer.  
译文：所有这里发生的事情都在你的电脑上本地进行。  

**03:21:20 - 03:21:22**  
原文：So we're not actually going to anywhere anyone else.  
译文：所以我们实际上不会去任何其他地方。  

**03:21:22 - 03:21:25**  
原文：This is running on the GPU on the Macc book pro.  
译文：这是在Macc book pro的GPU上运行的。  

**03:21:25 - 03:21:26**  
原文：So that's very nice.  
译文：所以这非常好。  

**03:21:26 - 03:21:30**  
原文：And you can then inject the model when you're done and that frees up to ram.  
译文：然后你可以在完成后将模型注入，这将释放出内存。  

**03:21:30 - 03:21:38**  
原文：So elm studio is probably like my favorite one, even though don't I think it's got a lot of uiux issues and it's really geared towards professionals almost.  
译文：所以 Elm Studio 可能是我最喜欢的之一，即使我认为它有很多用户界面和用户体验的问题，而且它几乎完全是为专业人士设计的。  

**03:21:38 - 03:21:44**  
原文：But if you watch some videos on YouTube, I think you can figure out how to use this interface.  
译文：但是如果你在YouTube上观看一些视频，我认为你可以弄清楚如何使用这个界面。  

**03:21:44 - 03:21:47**  
原文：So those are a few words on where to find them.  
译文：所以，这几句话就是关于在哪里可以找到它们。  

**03:21:47 - 03:21:50**  
原文：So let me now loop back around to where we started.  
译文：所以现在让我回到我们开始的地方。  

**03:21:50 - 03:21:58**  
原文：The question was, when we go to chashept te dot com and we enter some kind of a query, and we hit to go, what exactly is happening here?  
译文：问题是，当我们访问 chashept te dot com 并输入某种查询，然后点击去，这里究竟发生了什么？  

**03:21:58 - 03:21:59**  
原文：What are we seeing?  
译文：我们看到了什么？  

**03:21:59 - 03:22:01**  
原文：What are we talking to?  
译文：我们在和什么交谈？  

**03:22:01 - 03:22:02**  
原文：How does this work?  
译文：这是如何运作的？  

**03:22:02 - 03:22:11**  
原文：And I hope that this video gave you some appreciation for some of the underthe hood details of how these models are trained and what this is that is coming back.  
译文：我希望这个视频让你对这些模型的训练方式以及它们的输出背后的一些细节有所了解。  

**03:22:11 - 03:22:17**  
原文：So in particular, we now know that your query is taken and it's first chopped up into tokens.  
译文：所以特别地，我们现在知道你的查询被接受，然后首先被分割成令牌。  

**03:22:17 - 03:22:24**  
原文：So we go to tiktokenzer and here, where is the place in the sort of format that is for the user query?  
译文：所以我们去查看 tiktokenizer，在这里，用户查询的地方是在哪种格式中？  

**03:22:24 - 03:22:27**  
原文：We basically put in our query right there.  
译文：我们基本上就在那里输入了查询。  

**03:22:27 - 03:22:37**  
原文：So our query goes into what we discussed here, is the conversation protocol format, which is this way that we maintain conversation objects.  
译文：所以我们的查询进入了我们在这里讨论的内容，即对话协议格式，这就是我们维护对话对象的方式。  

**03:22:37 - 03:22:46**  
原文：So this gets inserted there, and then this whole thing ends up being just a token sequence, a one dimensional token sequence under the hood.  
译文：所以这会被插入到这里，然后这一切最终成为一个令牌序列，一个一维的令牌序列在底层。  

**03:22:46 - 03:22:52**  
原文：So Chachi psaw this token sequence, and then when we head to go, it basically continues appending tokens into this list.  
译文：所以 Chachi 看到了这个 token 序列，然后当我们继续进行时，它基本上会继续将 tokens 添加到这个列表中。  

**03:22:52 - 03:22:54**  
原文：It continues the sequence.  
译文：它继续该序列。  

**03:22:54 - 03:22:56**  
原文：It acts like a token auto complete.  
译文：它像一个令牌自动完成。  

**03:22:56 - 03:23:03**  
原文：So in particular, it gave us this response so we can basically just put it here and we see the tokens that it continued.  
译文：所以特别地，它给了我们这个响应，因此我们基本上可以把它直接放在这里，然后我们就能看到它继续生成的标记。  

**03:23:03 - 03:23:06**  
原文：These are the tokens that it continued with roughly.  
译文：这些是它继续使用的令牌，大致如下。  

**03:23:06 - 03:23:11**  
原文：Now the question becomes, okay, why are these the tokens that the responded with?  
译文：现在问题变成了，好吧，为什么这些是回应所使用的令牌？  

**03:23:11 - 03:23:12**  
原文：What are these tokens?  
译文：这些代币是什么？  

**03:23:12 - 03:23:13**  
原文：Where are they coming from?  
译文：他们是从哪里来的？  

**03:23:13 - 03:23:15**  
原文：What are we talking to?  
译文：我们在和谁对话？  

**03:23:15 - 03:23:17**  
原文：And how do we program this system?  
译文：我们如何编程这个系统？  

**03:23:17 - 03:23:21**  
原文：And so that's where we shifted gears and we talked about the under the pieces of it.  
译文：于是我们转变了话题，开始讨论它的各个组成部分。  

**03:23:21 - 03:23:33**  
原文：So the first stage of this process, and there are three stages, is the pre training stage, which fundamentally has to do with just knowledge acquisition from the Internet into the parameters of this neural network.  
译文：所以这个过程的第一阶段，总共有三个阶段，是预训练阶段，这主要是关于从互联网上获取知识并将其输入到这个神经网络的参数中。  

**03:23:33 - 03:23:44**  
原文：And so the neural nuinternalizes a lot of knowledge from the Internet, but where the personality really comes in is in the process of supervised fine ine tuning here.  
译文：因此，神经网络从互联网上内化了很多知识，但个性真正起作用的地方是在这里的监督微调过程中。  

**03:23:44 - 03:23:58**  
原文：And so what happens here is that basically a company like OpenAI will curate a large data set of conversations, like, say, 1 million conversation across very diverse topics, and there will be conversations between a human and an assistant.  
译文：所以这里发生的事情是，像OpenAI这样的公司将会整理一个大型的对话数据集，比如说，包含100万跨非常多样化的主题的对话，其中将包括人类与助手之间的对话。  

**03:23:58 - 03:24:10**  
原文：And even though there's a lot of synthetic data generation used throughout this entire process and a lot of llm help and so on, fundamentally, this is a human data curation task with lots of humans involved.  
译文：即使在整个过程中使用了大量的合成数据生成和大量的大型语言模型（LLM）辅助等，从根本上说，这是一项涉及许多人的人类数据管理任务。  

**03:24:10 - 03:24:16**  
原文：And in particular, these humans are data labelers hired by OpenAI who are given labeling instructions that they learn.  
译文：特别是，这些人类是受OpenAI雇佣的数据标注员，他们会接受标注指令并进行学习。  

**03:24:16 - 03:24:21**  
原文：And their task is to create ideal assistant responses for any arbitrary prompts.  
译文：他们的任务是为任何任意提示创建理想的助手回复。  

**03:24:21 - 03:24:26**  
原文：So they are teaching the neural network by example, how to respond to prompts.  
译文：所以他们是通过示例来训练神经网络，如何响应提示。  

**03:24:26 - 03:24:30**  
原文：So what is the way to think about what came back here?  
译文：那么，应该如何思考这里返回的结果呢？  

**03:24:30 - 03:24:31**  
原文：Like what is this?  
译文：像这是什么？  

**03:24:31 - 03:24:40**  
原文：Well, I think the right way to think about it is that this is the neural network simulation of a data labeler at OpenAI.  
译文：好吧，我认为正确的思考方式是，这是OpenAI的神经网络对数据标注员的模拟。  

**03:24:40 - 03:24:44**  
原文：So it's as if I gave this query to a data labelopen AI.  
译文：所以这就像我把这个查询给了一个数据标签开放人工智能。  

**03:24:44 - 03:24:57**  
原文：And this data labeler first reads all of the labeling instructions from OpenAI and then spends two hours writing up the ideal assistant response to this query and giving it to me.  
译文：此数据标注员首先从OpenAI阅读所有的标注说明，然后花费两个小时编写针对此查询的理想助手回复，并将其提供给我。  

**03:24:57 - 03:25:02**  
原文：Now we're not actually doing that right because we didn't wait two hours.  
译文：现在我们其实并没有那样做，因为我们没有等两个小时。  

**03:25:02 - 03:25:06**  
原文：So what we're getting here is a neural network simulation of that process.  
译文：所以我们在这里得到的是该过程的神经网络模拟。  

**03:25:06 - 03:25:11**  
原文：And we have to keep in mind that these neural networks don't function like human brains do.  
译文：我们必须记住，这些神经网络并不是像人脑那样运作的。  

**03:25:11 - 03:25:12**  
原文：They are different.  
译文：它们是不同的。  

**03:25:12 - 03:25:16**  
原文：What's easy or hard for them is different from what's easy or hard for humans.  
译文：对他们来说容易或困难的事情与对人类来说容易或困难的事情不同。  

**03:25:16 - 03:25:19**  
原文：And so we really are just getting a simulation.  
译文：所以我们真正得到的只是一个模拟。  

**03:25:19 - 03:25:22**  
原文：So here I shown you this is a token stream.  
译文：所以这里我向你展示这是一个标记流。  

**03:25:22 - 03:25:28**  
原文：And this is fundamentally the neural network with a bunch of activations and neurons in between.  
译文：这从根本上说是一个神经网络，在其间有一堆激活函数和神经元。  

**03:25:28 - 03:25:37**  
原文：This is a fixed mathematical expression that mixes inputs from tokens with parameters of the model, and they get mixed up and gets you the next token in a sequence.  
译文：这是一个固定的数学表达式，它将来自令牌的输入与模型的参数混合在一起，它们混合后可以得到序列中的下一个令牌。  

**03:25:37 - 03:25:41**  
原文：But this is a finite amount of compute that happens for every single token.  
译文：但这是每个单独令牌发生的有限计算量。  

**03:25:41 - 03:25:47**  
原文：And so this is some kind of a lossy simulation of a human that is kind of like restricted in this way.  
译文：所以这某种意义上说是对人类的有损模拟， 而且在某种程度上受限于这种方式。  

**03:25:47 - 03:26:00**  
原文：And so whatever the humans write, the language model is kind of imitating on this token level with only this specific computation for every single token, then a sequence.  
译文：所以，无论人类写什么，语言模型都在这个 token 层面上进行模仿，对于每个 token 进行这种特定的计算，然后形成一个序列。  

**03:26:00 - 03:26:10**  
原文：We also saw that as a result of this and the cognitive differences, the models will suffer in a variety of ways, and you have to be very careful with their use.  
译文：我们还看到，由于这些认知差异，模型将在各个方面受到影响，你必须非常小心地使用它们。  

**03:26:10 - 03:26:13**  
原文：So for example, we saw that they will suffer from hallucinations.  
译文：所以，例如，我们看到他们会遭受幻觉。  

**03:26:13 - 03:26:25**  
原文：And they also, we have the sense of a Swiss cheese model of the elm capabilities, where basically there's like holes and the cheese, sometimes the models will just arbitrarily like do something dumb.  
译文：而且，我们对elm能力有一种瑞士奶酪模型的感觉，基本上就是说，奶酪里有洞，有时候模型会任意地做一些愚蠢的事情。 

注：这里的“elm”可能是指特定的编程语言或模型，根据上下文可能需要调整。此外，“瑞士奶酪模型”通常用于描述系统中的漏洞或错误，该模型表明，尽管每个部分都有其“孔洞”（即缺陷），但这些孔洞并不总是一一对应，从而导致问题发生。  

**03:26:25 - 03:26:29**  
原文：So even though they're doing lots of magical stuff, sometimes they just can't.  
译文：所以即使他们在做很多神奇的事情，有时候他们就是做不到。  

**03:26:29 - 03:26:36**  
原文：So maybe you're not giving them enough tokens to think and maybe they're going to just make stuff up because they're mental arithmetic breaks.  
译文：所以可能你没有给他们足够的 token 来进行思考，而他们可能会胡编乱造，因为他们的心算能力有限。  

**03:26:36 - 03:26:45**  
原文：Maybe they are suddenly unable to count number of letters or maybe they're unable to tell you that nine, eleven, nine point eleven is smaller than 9.9 and it looks kind of dumb.  
译文：也许他们突然无法数字母的数量，或者也许他们无法告诉你 9、11、9.11 比 9.9 小，这看起来有点蠢。  

**03:26:45 - 03:26:49**  
原文：And so it's a Swiss cheese capability and be careful with that.  
译文：所以它像瑞士奶酪一样千疮百孔，要注意这一点。  

**03:26:49 - 03:26:50**  
原文：And we saw the reasons for that.  
译文：而且我们看到了这样做的原因。  

**03:26:51 - 03:26:55**  
原文：But fundamentally, this is how we think of what came back.  
译文：但从根本上说，这就是我们如何思考所得到的。  

**03:26:55 - 03:27:05**  
原文：It's again a simulation of this neural network of a human data labeler following the labeling instructions at OpenAI.  
译文：这再次是对OpenAI遵循标注指令的人类数据标注员的神经网络的模拟。  

**03:27:05 - 03:27:07**  
原文：So that's what we're getting back.  
译文：所以这就是我们得到的。  

**03:27:07 - 03:27:17**  
原文：Now I do think that the things change a little bit when you actually go and reach for one of the thinking models like zero three mini high.  
译文：现在我认为当你实际上去接触像零三迷你高这样的思维模型时，事情会有一些变化。  

**03:27:17 - 03:27:24**  
原文：And the reason for that is that GPT -4 zero basically doesn't do reinforcement learning.  
译文：原因是 GPT-4 基本上不进行强化学习。  

**03:27:24 - 03:27:25**  
原文：It does do rlhf.  
译文：它确实进行强化学习与人类反馈（RLHF）。  

**03:27:25 - 03:27:27**  
原文：But I've told you that rlhf is not rl.  
译文：但是我已经告诉过你，rlhf 并不是 rl。  

**03:27:27 - 03:27:30**  
原文：There's no time for magic in there.  
译文：里面没有时间进行魔法。  

**03:27:30 - 03:27:35**  
原文：It's just a little bit of a fine tuning is the way to look at it.  
译文：这只是一个小小的调整，这就是看待它的方式。  

**03:27:35 - 03:27:38**  
原文：But these thinking models, they do use rl.  
译文：但这些思维模型，它们确实使用了强化学习（rl）。  

**03:27:38 - 03:27:52**  
原文：So they go through this third stage of perfecting their thinking process and discovering new thinking strategies and solutions to problem solving that look a little bit like your internal monologue in your head.  
译文：所以他们经历了这个第三阶段， 完善他们的思考过程， 发现新的思考策略和解决问题的方法， 这些看起来有点像你头脑中的内心独白。  

**03:27:52 - 03:28:01**  
原文：And they practice that on a large collection of practice problems that companies like OpenAI create and curate and then make available to the alums.  
译文：并且他们在大量练习题上进行实践，这些练习题由像OpenAI这样的公司创建和整理，然后提供给校友们。  

**03:28:01 - 03:28:11**  
原文：So when I come here and I talk to a thinking model and I put in this question, what we're seeing here is not anymore just the straightforward simulation of a human data.  
译文：所以当我和这里的思考模型交谈并提出这个问题时，我们在这里看到的不再仅仅是人类数据的简单模拟。  

**03:28:11 - 03:28:14**  
原文：Labeler like this is actually kind of new, unique and interesting.  
译文：像这样的标签实际上是比较新的，独特的和有趣的。  

**03:28:14 - 03:28:24**  
原文：And of course, opai is not showing us the underthe hood thinking and the chains of thought that are underlying the reasoning here, but we know that such a thing exists, and this is a summary of it.  
译文：当然，Opai 并没有向我们展示背后的思考过程和支撑这一推理的思维链条，但我们知道这样的东西是存在的，而这则是对其的一个总结。  

**03:28:24 - 03:28:28**  
原文：And what we're getting here is actually not just an imitation of a human data labeler.  
译文：我们在这里得到的实际上不仅仅是一个模仿人类数据标注员的结果。  

**03:28:28 - 03:28:37**  
原文：It's actually something that is kind of new and interesting and exciting in the sense that it is a function of thinking that was emergent in a simulation.  
译文：这实际上是一种 新颖、有趣且令人兴奋的事物， 从某种意义上说， 它是一种在模拟中涌现出来的思维功能。  

**03:28:37 - 03:28:39**  
原文：It's not just imitating human data labeler.  
译文：这不仅仅是模仿人类数据标注员。  

**03:28:39 - 03:28:41**  
原文：It comes from this reinforcement learning process.  
译文：它来自于这个强化学习过程。  

**03:28:41 - 03:28:48**  
原文：And so here we're, of course, not giving it a chance to shine because this is not a mathematical or reasoning problem.  
译文：当然，在这里，我们并没有给它展现的机会，因为这并不是一个数学或推理问题。  

**03:28:48 - 03:28:51**  
原文：This is just some kind of a sort of creative writing problem.  
译文：这只是一个某种类型的创意写作问题。  

**03:28:51 - 03:29:06**  
原文：A roughly speaking, and I think it's it's a question, an open question as to whether the thinking strategies that are developed inside verifiable domings transfer and are generalizable to other domains that are unverifiable, such as create writing.  
译文：大致来说，我认为这是一个问题，一个开放性的问题，即在可验证的领域内发展出的思维策略是否能够转移并推广到其他不可验证的领域，例如创作写作。  

**03:29:06 - 03:29:11**  
原文：The extent to which that transfer happens is unknown in the field, I would say.  
译文：这种转移发生的程度在该领域是未知的，我会说。  

**03:29:11 - 03:29:20**  
原文：So we're not sure if we are able to do rl on everything that is verifiable and see the benefits of that on things that are unverifiable, like this prompt.  
译文：所以我们不确定我们是否能够对所有可验证的事物进行强化学习（rl），并看到这对不可验证的事物（比如这个提示）的好处。  

**03:29:20 - 03:29:22**  
原文：So that's open question.  
译文：所以这是一个开放性的问题。  

**03:29:22 - 03:29:30**  
原文：The other thing that's interesting is that this reinforcement learning here is still like way too new, primordial and nascent.  
译文：另一件有趣的事情是，这里的强化学习仍然非常新，原始且处于萌芽阶段。  

**03:29:30 - 03:29:35**  
原文：So we're just seeing like the beginnings of the hints of greatness in the reasoning problems.  
译文：所以我们现在只是看到了 理由问题伟大性的初步迹象。  

（注：根据上下文和语境，这句话可能指我们目前仅看到推理问题中伟大性或潜力的初步迹象。为了更准确地传达原意，建议将“reasoning problems”具体化，例如：“所以我们现在只是看到了推理问题中伟大性的初步迹象。” 如果有更多背景信息，可以进一步优化翻译。）  

**03:29:35 - 03:29:46**  
原文：We're seeing something that is in principle, capable of something like the equivalent of move 37, but not in the game of go, but in open domain thinking and problem solving.  
译文：我们看到的是一种原则上有能力做到类似于第37步移动的事物， 但这并不是在围棋游戏中， 而是在开放领域的思考和问题解决中。  

**03:29:46 - 03:29:54**  
原文：In principle, this paradigm is capable of doing something really cool, new and exciting, something even that no human has thought of before.  
译文：原则上，这种范式能够做一些真正酷炫、全新且令人兴奋的事情，甚至是一些以前没有人想过的事情。  

**03:29:54 - 03:29:59**  
原文：In principle, these models are capable of analogies no human has had.  
译文：原则上，这些模型能够进行人类从未有过的新类比。  

**03:29:59 - 03:30:02**  
原文：So I think it's incredibly exciting that these models exist.  
译文：所以我认为这些模型的存在令人无比兴奋。  

**03:30:02 - 03:30:09**  
原文：But again, it's very early and these are primoral models for now, and they will mostly shine in domains that are verifiable, like math and code, etcetera.  
译文：但同样，现在还非常早，这些是目前的原始模型，它们将主要在可验证的领域发光，比如数学和编程等领域。  

**03:30:09 - 03:30:12**  
原文：So very interesting to play with and think about and use.  
译文：所以非常有趣，可以玩，可以思考，可以使用。  

**03:30:13 - 03:30:14**  
原文：And then that's roughly it.  
译文：然后这就大致完成了。  

**03:30:14 - 03:30:19**  
原文：I would say those are the broad strokes of what's available right now.  
译文：我可以说这些是目前可用的大致情况。  

**03:30:19 - 03:30:24**  
原文：I will say that overall, it is an extremely exciting time to be in the field.  
译文：我会说，总体而言，现在是处于这个领域 Extremely exciting 的时候。 

（注：此处 "Extremely exciting" 直译为“极其令人兴奋的”，为了保持原始格式未做调整。正常语境下建议修改为：我会说，总体而言，现在是处于这个领域极其令人兴奋的时候。） 

如果你希望 "Extremely exciting" 也翻译成中文，可以告知我做相应调整。  

**03:30:24 - 03:30:32**  
原文：Personally, I use these models all the time, daily, tens or hundreds of times, because they dramatically accelerate my work.  
译文：个人而言，我时刻在使用这些模型，每天数十次或数百次，因为它们极大地加速了我的工作。  

**03:30:32 - 03:30:34**  
原文：I think a lot of people see the same thing.  
译文：我想很多人都看到了同样的情况。  

**03:30:34 - 03:30:39**  
原文：I think we're going to see a huge amount of wealth creation as a result of these models.  
译文：我认为我们将看到由于这些模型而产生的巨大财富。  

**03:30:39 - 03:30:41**  
原文：Be aware of some of their shortcomings.  
译文：请注意他们的一些缺点。  

**03:30:41 - 03:30:44**  
原文：Even with rl models, they're going to suffer from some of these.  
译文：即使使用强化学习模型，它们也会遭受其中一些问题。  

**03:30:44 - 03:30:46**  
原文：Use it as a tool in a toolbox.  
译文：将它作为工具箱中的一个工具使用。  

**03:30:46 - 03:30:57**  
原文：Don't trust it fully because they will randomly do dumb things, they will randomly hallucinate, they will randomly skip over some mental arithmetic and not get it right, they randomly can't count or something like that.  
译文：不要完全相信它，因为它们会随机做出一些愚蠢的事情，它们会随机产生幻觉，它们会随机跳过一些心算并且算不对，它们可能会随机地数不清东西或类似的情况。  

**03:30:57 - 03:31:05**  
原文：So use them as a tools in the toolbox, check their work and own the product of your work, but use them for inspiration for first draft.  
译文：所以将它们作为工具箱中的工具，检查它们的工作并拥有你工作的成果，但可以使用它们来为初稿提供灵感。  

**03:31:05 - 03:31:11**  
原文：Ask them questions, but always check and verify, and you will be very successful in your work if you do so.  
译文：向他们提问，但一定要检查和核实，如果你这样做，在工作中会非常成功。  

**03:31:11 - 03:31:15**  
原文：So I hope this video was useful and interesting to you.  
译文：所以我希望这个视频对你有帮助且有趣。  

**03:31:15 - 03:31:17**  
原文：I hope you had it fun and it's already like very long.  
译文：我希望你玩得开心，而且这已经花了很长的时间。  

**03:31:17 - 03:31:20**  
原文：So I apologize for that, but I hope it was useful.  
译文：所以对此我表示歉意，但我希望它是有用的。  

**03:31:20 - 03:31:22**  
原文：And Yeah, I will see you later.  
译文：好的，我会再见你的。  



## 相关资源

### 官方链接
- [创作者频道: Andrej Karpathy](https://www.youtube.com/channel/UCXUPKJO5MZQN11PqgIvyuvQ)
- [原始视频: Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI)

### 视频描述中提及的链接
- [链接 1](https://karpathy.ai/)
- [链接 2](https://x.com/karpathy)
- [链接 3](https://chatgpt.com/)
- [链接 4](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)
- [链接 5](https://tiktokenizer.vercel.app/)

### 可能的相关主题
> 根据视频内容搜索更多相关资源

