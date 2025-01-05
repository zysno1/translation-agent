---
video_id: _yu0Rtuetuc
video_url: https://www.youtube.com/watch?v=_yu0Rtuetuc
video_title: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
created_at: 2025-01-05 17:36:33
---

# How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform

> [00:06 - 00:17]
<|Speech|> Hello, everyone. We are going soon. And truly, from our group, and today's topic is from our buddy team, LED by Teng Wei Cai. <|/Speech|> <|NEUTRAL|>

> [00:17 - 00:25]
<|Speech|> But he cannot come here today. So we'll be the speakers. And this is the first time we come here. <|/Speech|> <|NEUTRAL|>

> [00:25 - 00:38]
<|BGM|> <|Speech|> And we are so glad to share our work in with Amit. And today's topic is about how we empowered our group to deliver a large scale online service platform. <|/BGM|> <|/Speech|> <|HAPPY|>

> [00:38 - 00:46]
<|Speech|> Let's start. First, I'd like to introduce my company and my team. <|/Speech|>

> [00:46 - 00:54]
<|Speech|> To summarize our group, there are five directions, digital payment, digital connectivity. <|/Speech|> <|NEUTRAL|>

> [00:54 - 01:07]
<|Speech|> Digital finance, digital technology and globalization. And the most favors or popular application of our group is Alipay. <|/Speech|> <|NEUTRAL|>

> [01:07 - 01:12]
<|Speech|> Which is leading the internet payment and finance in China. <|/Speech|> <|NEUTRAL|>

> [01:12 - 01:20]
<|Speech|> And my team is an artery team in the next page. I will show you a lot. <|/Speech|> <|NEUTRAL|>

> [01:20 - 01:29]
<|Speech|> History, information of my team. But there, I want to share some high level information first. <|/Speech|> <|NEUTRAL|>

> [01:30 - 01:38]
<|Speech|> First, we are the second largest team contributing to the Ray open source software. <|/Speech|> <|NEUTRAL|>

> [01:38 - 01:46]
<|Speech|> We are collaborating with any scale and rest lab for several years. <|/Speech|> <|NEUTRAL|>

> [01:46 - 01:56]
<|Speech|> And we have over, over 26% code contribute of the recall part in the open source. <|/Speech|> <|NEUTRAL|>

> [01:56 - 02:05]
<|Speech|> Second, in addition to the developing ray. We also have a lot of a large scale application of ray. <|/Speech|> <|NEUTRAL|>

> [02:05 - 02:13]
<|Speech|> And in now, in our production, we have over one million CPU calls. <|/Speech|> <|NEUTRAL|>

> [02:15 - 02:23]
<|Speech|> And then in China, we also have a China community, which is created and operated by my team. <|/Speech|> <|NEUTRAL|>

> [02:23 - 02:33]
<|Speech|> And every over the past five years. We hosted the Ray Forward meet up every year, and the fifth Ray Forward. <|/Speech|>

> [02:33 - 02:45]
<|Speech|> Has been finished in the past July. And in this conference, any skill across AI aren't. <|/Speech|> <|NEUTRAL|>

> [02:45 - 02:55]
<|Speech|> And by dance, I sell their works in this conference. So we so. <|/Speech|> <|NEUTRAL|>

> [02:55 - 03:01]
<|Speech|> We are. We hope that we could be more popular in China, as in US. <|/Speech|>

> [03:02 - 03:16]
<|Speech|> Next, go through the part of the history of ray in art. My team is created in 2017, and in this year, the ray is more different from today's ray. <|/Speech|> <|NEUTRAL|>

> [03:16 - 03:30]
<|Speech|> We consider it as a general distributed system, which means that we have a lot of non AI application and framework. <|/Speech|> <|NEUTRAL|>

> [03:30 - 03:39]
<|Speech|> You know that in the Ray open source, Ray, open source focuses on the Python and AI. <|/Speech|> <|NEUTRAL|>

> [03:39 - 03:50]
<|Speech|> This means Python first and AI first. But young, we are different. So you can know that. You can see that. We have already contributed. <|/Speech|>

> [03:50 - 03:55]
<|Speech|> Pi, Java and C plus plus API in the project. <|/Speech|> <|NEUTRAL|>

> [03:55 - 04:03]
<|Speech|> And in our first up layer, up layer. <|/Speech|> <|NEUTRAL|>

> [04:03 - 04:12]
<|Speech|> Engine was deployed in our production. The engine name is G flow, and it is a streaming graph engine. <|/Speech|> <|NEUTRAL|>

> [04:12 - 04:23]
<|Speech|> It is used in risk control, in payment of Alipay and in twenty, twenty, twenty nine in twenty nineteen. <|/Speech|> <|NEUTRAL|>

> [04:23 - 04:31]
<|Speech|> Another fusion engine was deployed in our production. The engine is only learning. <|/Speech|> <|NEUTRAL|>

> [04:31 - 04:40]
<|Speech|> We feel the three computing types, including streaming, M, L, and online serving. So you can know that. <|/Speech|> <|NEUTRAL|>

> [04:40 - 04:49]
<|Speech|> Online serving at this time is also the online serving. First time was deployed in art, and it is today's topic. <|/Speech|> <|NEUTRAL|>

> [04:49 - 05:00]
<|Speech|> And in twenty, twenty, given the diversity of business, we made a multi tenant architecture of Ray. <|/Speech|> <|NEUTRAL|>

> [05:00 - 05:11]
<|Speech|> Which means you can run a lot of red jobs in one big cluster. And in, in this job, you can. <|/Speech|> <|NEUTRAL|>

> [05:11 - 05:16]
<|Speech|> Support different computing paradigms. <|/Speech|> <|NEUTRAL|>

> [05:16 - 05:28]
<|Speech|> And in twenty twenty one, the artery was been more stable. We, we have do some more collaboration, collaboration with our ecosystem. <|/Speech|> <|NEUTRAL|>

> [05:28 - 05:35]
<|Speech|> Company such as Alibaba, Damo Academy, China Network and Wangshan Bank. <|/Speech|> <|NEUTRAL|>

> [05:36 - 05:43]
<|Speech|> And in twenty twenty two, we explored a private computing, which is a new scenario. <|/Speech|> <|NEUTRAL|>

> [05:43 - 05:53]
<|Speech|> We think that it is a good scenario for, for Ray, because in private computing. <|/Speech|>

> [05:53 - 06:01]
<|Speech|> We need a flexible framework to support common function, data and AI. <|/Speech|> <|NEUTRAL|>

> [06:01 - 06:07]
<|Speech|> And it is there. There are a lot of advantages, injury for it. <|/Speech|>

> [06:08 - 06:17]
<|Speech|> Okay, in this year, we aim to build a general AI. <|/Speech|> <|NEUTRAL|>

> [06:17 - 06:27]
<|Speech|> Serving framework, which in, in this framework work, we want to unified traditional AI, large language model and search engine. <|/Speech|> <|NEUTRAL|>

> [06:28 - 06:38]
<|Speech|> So this is today's topic. Back to the online survey from the historical timeline. You can know that. <|/Speech|>

> [06:38 - 06:48]
<|Speech|> The, the, the online serving was, was first deployed in Ant in twenty nineteen. <|/Speech|> <|NEUTRAL|>

> [06:48 - 06:54]
<|Speech|> And it is integrated to the online learning engine. <|/Speech|> <|NEUTRAL|>

> [06:54 - 07:02]
<|Speech|> Depends on this. We build the basic ability of reserving and integrated it into infrastructure. <|/Speech|> <|NEUTRAL|>

> [07:02 - 07:12]
<|Speech|> Of art group, you know that each company has its customer infrastructure. So we, we need to adopt it. <|/Speech|> <|NEUTRAL|>

> [07:13 - 07:19]
<|Speech|> And in we, we have, we have another scenario. <|/Speech|> <|NEUTRAL|>

> [07:19 - 07:30]
<|Speech|> Online resource allocation, you can, you can. You can imagine that if the resource is, is for payment and finance. <|/Speech|> <|NEUTRAL|>

> [07:30 - 07:38]
<|Speech|> What's the challenges. We think the challenges is that we need a more flexible, high performance. <|/Speech|>

> [07:38 - 07:49]
<|Speech|> And scalable, stable, a, A framework. And fortunately, we, we, we achieve it in based on re survey. <|/Speech|> <|HAPPY|>

> [07:49 - 07:57]
<|Speech|> And in twenty twenty in twenty twenty two we support the large scale online serverless platform. <|/Speech|> <|NEUTRAL|>

> [07:57 - 08:07]
<|Speech|> At this time, we served models with two hundred and forty thousand calls, and our event driven serverless platform. <|/Speech|> <|NEUTRAL|>

> [08:07 - 08:17]
<|Speech|> The one point three, seven million peak T, P, S. Okay, that's all of our private, private works. <|/Speech|> <|NEUTRAL|>

> [08:17 - 08:24]
<|Speech|> Next, Chong will introduce our recent achievements this year. <|/Speech|> <|NEUTRAL|>

> [08:25 - 08:31]
<|Speech|> Welcome, all right, thanks, Guya. And hello, everyone. <|/Speech|> <|HAPPY|>

> [08:31 - 08:40]
<|Speech|> My name is Chong Li, and I'm very glad to be here to share our most recent achievements in. <|/Speech|> <|HAPPY|>

> [08:40 - 08:50]
<|Speech|> In any group, we have already built the largest inference platform. Our inference clusters have point five million CPU cores, and four K. <|/Speech|> <|NEUTRAL|>

> [08:50 - 08:59]
<|Speech|> GPU cars in total, and I believe you guys have already seen these numbers at Dr. Stoica's keynote speech yesterday. <|/Speech|> <|NEUTRAL|>

> [08:59 - 09:09]
<|Speech|> And to deliver this hardware, we are using over twenty-seven thousand worker nodes in total. and as a inference platform. <|/Speech|>

> [09:09 - 09:18]
<|Speech|> We have very highly active model deployments in our platform. We have over three new model deployments every week. <|/Speech|> <|HAPPY|>

> [09:18 - 09:28]
<|Speech|> And over one model updates every week. And our inference clusters are highly auto scalable. <|/Speech|> <|NEUTRAL|>

> [09:28 - 09:40]
<|Speech|> Thanks to our productized and standalone autoscaler, our inference classes can now be autoscaled over three thousand times every week. <|/Speech|> <|NEUTRAL|>

> [09:40 - 09:49]
<|Speech|> Proactively, and by doing so, we have increased our average CPU utilization by over 20%. <|/Speech|> <|HAPPY|>

> [09:51 - 09:58]
<|Speech|> So next, I will talk about some new scenarios in our productions and some new features we did. <|/Speech|> <|NEUTRAL|>

> [09:59 - 10:11]
<|Speech|> Before getting into the details, I'd like to firstly show an overview about our RedSurfing architecture, it is not much different from the OpenSource RedSurf. <|/Speech|> <|HAPPY|>

> [10:11 - 10:23]
<|Speech|> In this architecture, we have a serving keeper, it receives all their serving inference job submissions from the user clients. <|/Speech|> <|HAPPY|>

> [10:23 - 10:34]
<|Speech|> And it has to distribute these serving jobs across our serving clusters. But for each of them, the serving keeper has to create. <|/Speech|>

> [10:34 - 10:46]
<|Speech|> And corresponding application master in one particular serving cluster. And this application master will create multiple proxies, and deployment actors. <|/Speech|> <|NEUTRAL|>

> [10:46 - 10:56]
<|Speech|> Within the cluster. And when the proxies are ready, they will register themselves to independent service discovery component. <|/Speech|> <|NEUTRAL|>

> [10:57 - 11:10]
<|Speech|> And by subscribing to this component, our user applications can get to know the locations of every proxy and carefully pick the most suitable one to send there. <|/Speech|> <|HAPPY|>

> [11:10 - 11:20]
<|Speech|> Inference requests. And in every proxy, you have to assign the incoming inference requests. <|/Speech|>

> [11:20 - 11:27]
<|Speech|> To its local deployment actors, where the model serving work will be done there. <|/Speech|> <|NEUTRAL|>

> [11:29 - 11:40]
<|Speech|> Okay, so new scenarios, the first one is doing the model solving work on GPUs to make it happen, we chose to use NVIDIA Triton. <|/Speech|> <|HAPPY|>

> [11:40 - 11:51]
<|Speech|> For those of you unfamiliar with Triton. It is Nvidia's single node model inference ensemble. It supports multiple. <|/Speech|>

> [11:51 - 12:00]
<|Speech|> Inference backends. And in our reserving system, the Triton servers could be very easily distributed. <|/Speech|> <|HAPPY|>

> [12:00 - 12:08]
<|Speech|> All we need to do is running the making our deployment actor become a Triton bootstrapper. <|/Speech|>

> [12:08 - 12:18]
<|Speech|> So whenever our application master creates a new deployment actor, it will immediately boost up the Triton server inside. <|/Speech|> <|HAPPY|>

> [12:18 - 12:26]
<|Speech|> And with the help of our actor, long time environment, this long time environment feature is. <|/Speech|>

> [12:26 - 12:38]
<|Speech|> Very useful, it is provided by the open source recall, and it helps a lot when we are dealing with data dependency package or library dependency programs. <|/Speech|> <|NEUTRAL|>

> [12:38 - 12:45]
<|Speech|> And I believe our recall team contributed nearly half of their implementations to the open source. <|/Speech|> <|NEUTRAL|>

> [12:46 - 12:57]
<|Speech|> Right, so when these Triton servers are ready, they can choose to register themselves to this discovery, service discovery component. <|/Speech|> <|HAPPY|>

> [12:57 - 13:06]
<|Speech|> And the upcoming inference requests can be connected to these Triton servers directly. <|/Speech|> <|NEUTRAL|>

> [13:06 - 13:18]
<|Speech|> And one thing to mention is that because our serving cluster is highly autoscalable, so when you run the Triton servers in our platform. <|/Speech|> <|NEUTRAL|>

> [13:18 - 13:23]
<|Speech|> They become auto scalable, as well. <|/Speech|>

> [13:23 - 13:31]
<|Speech|> Okay, next scenario is serving the L, M applications the. <|/Speech|>

> [13:31 - 13:48]
<|Speech|> The background of this thing is in our end group, we have a system called GPT cache in this system, we will try to store the historical LLM responses in our vector or cache stores. <|/Speech|> <|NEUTRAL|>

> [13:48 - 13:58]
<|Speech|> So whenever there is a new inference request coming in, the first thing we do is running a similarity comparison. So if the cache is hit, then we just. <|/Speech|> <|HAPPY|>

> [13:58 - 14:10]
<|Speech|> Respond the pre-start responses back to the user, and if cache misses, then the inference request still has to go through the model serving pipeline. <|/Speech|> <|NEUTRAL|>

> [14:12 - 14:24]
<|Speech|> And in our re serving platform, this check, this G, P. T cache system could be very easily integrated. All we need to do is running this. <|/Speech|> <|HAPPY|>

> [14:24 - 14:33]
<|Speech|> Gpt cache system inside our deployment actor. And still, with the help of the actor, runtime feature. <|/Speech|> <|NEUTRAL|>

> [14:33 - 14:43]
<|Speech|> And of course, we need an ingress actor in the cluster. And it will help us forward, every incoming inference request. <|/Speech|>

> [14:43 - 14:53]
<|Speech|> To the Gbt cache actor at the first place. And then we still do the same thing. If cache hit, then we do a quick response. <|/Speech|> <|HAPPY|>

> [14:53 - 15:04]
<|Speech|> If cache misses, then we just forward this request to another Triton server, which is also running in a deployment actor. <|/Speech|> <|NEUTRAL|>

> [15:06 - 15:17]
<|Speech|> So one big thing you can see here is in this picture, the GPD cache actors are running on CPU nodes. <|/Speech|> <|NEUTRAL|>

> [15:17 - 15:27]
<|Speech|> And the Triton servers are running on GPU nodes. So thanks to Ray calls, heterogeneous results scheduling. <|/Speech|> <|NEUTRAL|>

> [15:27 - 15:36]
<|Speech|> We can now distribute these different kinds of actors more wisely and optimize the overall resource utilization. <|/Speech|>

> [15:39 - 15:49]
<|Speech|> Okay, so next is some new features. The first one is built in async broker. We did this because in. <|/Speech|> <|HAPPY|>

> [15:49 - 15:58]
<|Speech|> Most of our model serving scenarios, we found the inference requests have very different execution time. <|/Speech|> <|NEUTRAL|>

> [15:58 - 16:07]
<|Speech|> So for these long requests, people always have to pay a lot of centralized waiting overhead. <|/Speech|>

> [16:07 - 16:18]
<|Speech|> So what we did here is deploying an async broker in the serving cluster. And, of course, this async broker is running in a deployment actor. <|/Speech|> <|HAPPY|>

> [16:18 - 16:26]
<|Speech|> As well. And this async broker can receive and queue every incoming inference request. <|/Speech|> <|NEUTRAL|>

> [16:26 - 16:37]
<|Speech|> For these long requests, when the results are ready, the async broker can help us return these results back to the users async nicely. <|/Speech|> <|NEUTRAL|>

> [16:40 - 16:52]
<|Speech|> And one big benefit from this async broker is that with this inside the cluster, the other deployment actors. <|/Speech|> <|NEUTRAL|>

> [16:52 - 17:04]
<|Speech|> Can actually pull the inference requests from this broker adaptively based on their own busy or idle status. <|/Speech|> <|NEUTRAL|>

> [17:04 - 17:12]
<|Speech|> So by doing so in every deployment actor, which is running the model serving with Triton server. <|/Speech|> <|NEUTRAL|>

> [17:12 - 17:18]
<|Speech|> In each of these deployment actor, we can see much less head of line delays. <|/Speech|>

> [17:19 - 17:29]
<|Speech|> So in our evaluation, compared to the baseline, which is round robin push based request assignment. <|/Speech|> <|HAPPY|>

> [17:29 - 17:35]
<|Speech|> Our poor based method can give us two times better throughput. <|/Speech|>

> [17:38 - 17:48]
<|Speech|> The next feature is C plus plus deployment. This one, this feature has been widely deployed in our recommendation and advertising. <|/Speech|> <|HAPPY|>

> [17:48 - 17:58]
<|Speech|> Services, these services are latency sensitive with high throughput. So because of this performance requirements. <|/Speech|>

> [17:58 - 18:09]
<|Speech|> Our deployment actors has to be high performance as well. So what we did is using C plus plus deployment actors. <|/Speech|>

> [18:09 - 18:19]
<|Speech|> Based on open source rates, C plus plus workers. And by the way, this C plus plus workers is also. <|/Speech|>

> [18:19 - 18:31]
<|Speech|> mainly contributed by our Ray team, so thanks Guyang for his effort on this, okay, so with this C++ deployment actors in hand. <|/Speech|> <|HAPPY|>

> [18:31 - 18:40]
<|Speech|> One big thing we did is implementing C plus plus direct ingress. It is a high performance RPC service. <|/Speech|> <|HAPPY|>

> [18:40 - 18:49]
<|Speech|> And with this feature, our inference request can directly connect it to our C++ deployment actors. <|/Speech|> <|NEUTRAL|>

> [18:49 - 18:54]
<|Speech|> By passing all these proxies that I have been mentioning above. <|/Speech|>

> [18:56 - 19:05]
<|Speech|> And another big thing is native Triton inference call. This thing can be done because we now have these C plus plus. <|/Speech|> <|HAPPY|>

> [19:05 - 19:15]
<|Speech|> Deployment actors and the Triton server, which can be considered as a C plus plus library, could be more closely and. <|/Speech|> <|NEUTRAL|>

> [19:15 - 19:26]
<|Speech|> Efficiently integrated without any cross language overhead. And when we are making the C plus plus deployment actors. <|/Speech|>

> [19:26 - 19:35]
<|Speech|> Working together with other C plus plus components in our recommendation and advertising timelines. <|/Speech|>

> [19:35 - 19:40]
<|Speech|> And we are actually doing a more holistic, distributed system. <|/Speech|>

> [19:43 - 19:54]
<|Speech|> Okay, next I will talk about some future plans, the first thing we are going to do is the Shardit deployment. <|/Speech|> <|HAPPY|>

> [19:54 - 20:03]
<|Speech|> The motivation for this thing is in our recommendation and search services with CVR or CTR models. <|/Speech|> <|HAPPY|>

> [20:03 - 20:15]
<|Speech|> We can always see numerous items with large feature data, and this feature data size is too large to be. <|/Speech|> <|HAPPY|>

> [20:15 - 20:27]
<|Speech|> Fit in any single worker node. So what we have to do is trying to shut this large size feature data. <|/Speech|>

> [20:27 - 20:35]
<|Speech|> Across multiple work nodes. And, of course, we will create proxy deployment. <|/Speech|>

> [20:35 - 20:46]
<|Speech|> Actor, actually. And use this proxy to help us do a shut away routing strategy and make sure every incoming. <|/Speech|> <|NEUTRAL|>

> [20:46 - 20:56]
<|Speech|> Inference request could be forwarded to a specific note, with the data dependency locally available. <|/Speech|>

> [20:59 - 21:10]
<|Speech|> Okay, so the last thing is actually a very big picture we are hoping to deliver a high performance general AI framework. <|/Speech|> <|HAPPY|>

> [21:11 - 21:19]
<|Speech|> To make it happen, the first thing we are going to do is keep constructing and. <|/Speech|>

> [21:19 - 21:27]
<|Speech|> Polishing our rate serving platform based on open source reserve, which has been proven. <|/Speech|> <|NEUTRAL|>

> [21:27 - 21:37]
<|Speech|> To be highly distributed, multi language, supportive and scalable. And we do believe this could be a very good foundation for. <|/Speech|>

> [21:37 - 21:41]
<|Speech|> Many of the models serving scenarios. <|/Speech|>

> [21:42 - 21:51]
<|Speech|> We will definitely use our direct ingress and use it to build a high performance Rpc service. <|/Speech|> <|HAPPY|>

> [21:52 - 22:02]
<|Speech|> We will. We will widely use the C plus plus deployment actors, because it can give us a high performance. <|/Speech|> <|HAPPY|>

> [22:02 - 22:11]
<|Speech|> Computing capability. And we will start working on this sharded deployment, which gave us. <|/Speech|>

> [22:11 - 22:24]
<|Speech|> High performance, local data access and data retrieval. And we think this feature could be very critical when we are dealing with large scale model serving. <|/Speech|> <|NEUTRAL|>

> [22:24 - 22:32]
<|Speech|> Problems in the future. So that's basically all we have for today, so. <|/Speech|> <|HAPPY|>

> [22:32 - 22:44]
<|Speech|> As I said in the beginning, this work is mostly done by Teng Wei from our buddy team, so we will try our best to answer questions here, but if we cannot, <|/Speech|> <|NEUTRAL|>

> [22:44 - 22:53]
<|Speech|> I do encourage you guys send emails to this address, and I believe he can give the most detailed answers. <|/Speech|> <|NEUTRAL|>

> [22:53 - 22:58]
<|Speech|> Thank you. <|Applause|> <|/Applause|> <|/Speech|>

> [23:02 - 23:10]
<|Speech|> So the direct ingress and the C++ work that you have done for how much of that is integrated into the Rekor? <|/Speech|> <|NEUTRAL|>

> [23:11 - 23:23]
<|Speech|> It's already open sourced, but it's not very popular, actually, in the open source community, but we use that a lot in our productions. <|/Speech|> <|NEUTRAL|>

> [23:23 - 23:32]
<|Speech|> Cause in the, in the recommendation and advertising systems, cause we hope to make all components in our. <|/Speech|>

> [23:32 - 23:40]
<|Speech|> Pipeline, the recommendation, pipeline are all implemented in C plus plus and making the whole pipeline more holistic. <|/Speech|> <|NEUTRAL|>

> [23:42 - 23:50]
<|Speech|> One follow up question on that is that in that space that you just mentioned, which is the recommendation pipeline. <|/Speech|> <|NEUTRAL|>

> [23:50 - 24:00]
<|Speech|> How, like, what are you really using Ray for, Because using Triton for inference, right. And you're using this direct ingress. But what role. <|/Speech|>

> [24:00 - 24:11]
<|Speech|> What role is Ray playing there, how is Ray helping you in that space? Yeah, we definitely use Ray's runtime environment. <|/Speech|> <|NEUTRAL|>

> [24:11 - 24:20]
<|Speech|> To help us to integrate this Triton dependency in our deployment actor. <|/Speech|>

> [24:20 - 24:30]
<|Speech|> And we use race heterogeneous scheduling to help us schedule these actors. <|/Speech|> <|NEUTRAL|>

> [24:30 - 24:40]
<|Speech|> CPU dependent actors or GPU dependent actors. They can all be scheduled well and help us increase the resource utilization. <|/Speech|>

> [24:46 - 24:54]
<|Speech|> Thank you for the talk. A quick question. So you mentioned that there are about three plus deployments. <|/Speech|>

> [24:54 - 25:02]
<|Speech|> The deployment per week. And my question is, for one type of model, like, what's the like. <|/Speech|> <|NEUTRAL|>

> [25:02 - 25:12]
<|Speech|> Average or usual frequency for deployments. Let's say we have a large language model. And then how often do you. <|/Speech|> <|NEUTRAL|>

> [25:12 - 25:20]
<|Speech|> Do updates and deployment. Yeah, I guess this range you can. You got me here. <|/Speech|>

> [25:20 - 25:28]
<|Speech|> I don't really know the details. Yeah, so that question, that's what you. You should send emails to Teng Wei. <|/Speech|>

> [25:28 - 25:32]
<|Speech|> Right, because that's some details from the serving team. <|/Speech|>

> [25:37 - 25:47]
<|Speech|> It's a sharding deployment related to the choice of ray. The sharding deploying what, Yes, it's a sharding deployment related to the choice of ray. <|/Speech|>

> [25:47 - 25:58]
<|Speech|> It's, yes, it's still on Ray. We use, we just need to shut this feature data across multiple worker nodes, but the worker nodes still. <|/Speech|>

> [25:58 - 26:05]
<|Speech|> It's built on ray, and all the actors are handled, are reactors. <|/Speech|> <|NEUTRAL|>

> [26:13 - 26:23]
<|Speech|> So all of this is running on top of like Vms. Right, not Kubernetes or anything else in between. Just bare Vm. I'm saying, what is this all just running on. <|/Speech|>

> [26:23 - 26:33]
<|Speech|> Vms, or is it running on Kubernetes or is it running on, Yeah, yeah, we are. We are definitely running our ray cluster. Ray clusters in the cloud, native environment. <|/Speech|>

> [26:33 - 26:38]
<|Speech|> On top of Kubernetes. <|/Speech|>

> [26:43 - 26:50]
<|Speech|> Oh, well, if there are no more questions, then thank you so much. <|Applause|> <|/Applause|> <|/Speech|>

