---
video_id: _yu0Rtuetuc
video_url: https://www.youtube.com/watch?v=_yu0Rtuetuc
video_title: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
created_at: 2025-01-05 17:48:31
---

# How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform

> [00:06 - 00:17]
Hello, everyone. We are going soon. And truly, from our group, and today's topic is from our buddy team, LED by Teng Wei Cai.

> [00:17 - 00:25]
But he cannot come here today. So we'll be the speakers. And this is the first time we come here.

> [00:25 - 00:38]
And we are so glad to share our work in with Amit. And today's topic is about how we empowered our group to deliver a large scale online service platform.

> [00:38 - 00:46]
Let's start. First, I'd like to introduce my company and my team.

> [00:46 - 00:54]
To summarize our group, there are five directions, digital payment, digital connectivity.

> [00:54 - 01:07]
Digital finance, digital technology and globalization. And the most favors or popular application of our group is Alipay.

> [01:07 - 01:12]
Which is leading the internet payment and finance in China.

> [01:12 - 01:20]
And my team is an artery team in the next page. I will show you a lot.

> [01:20 - 01:29]
History, information of my team. But there, I want to share some high level information first.

> [01:30 - 01:38]
First, we are the second largest team contributing to the Ray open source software.

> [01:38 - 01:46]
We are collaborating with any scale and rest lab for several years.

> [01:46 - 01:56]
And we have over, over 26% code contribute of the recall part in the open source.

> [01:56 - 02:05]
Second, in addition to the developing ray. We also have a lot of a large scale application of ray.

> [02:05 - 02:13]
And in now, in our production, we have over one million CPU calls.

> [02:15 - 02:23]
And then in China, we also have a China community, which is created and operated by my team.

> [02:23 - 02:33]
And every over the past five years. We hosted the Ray Forward meet up every year, and the fifth Ray Forward.

> [02:33 - 02:45]
Has been finished in the past July. And in this conference, any skill across AI aren't.

> [02:45 - 02:55]
And by dance, I sell their works in this conference. So we so.

> [02:55 - 03:01]
We are. We hope that we could be more popular in China, as in US.

> [03:02 - 03:16]
Next, go through the part of the history of Rui in art. My team is created in 2017, and in this year, the Rui is more different from today's Rui.

> [03:16 - 03:30]
We consider it as a general distributed system, which means that we have a lot of non AI application and framework.

> [03:30 - 03:39]
You know that in the Ray open source, Ray, open source focuses on the Python and AI.

> [03:39 - 03:50]
This means Python first and AI first. But young, we are different. So you can know that. You can see that. We have already contributed.

> [03:50 - 03:55]
Pi, Java and C plus plus API in the project.

> [03:55 - 04:03]
And in our first up layer, up layer.

> [04:03 - 04:12]
Engine was deployed in our production. The engine name is G flow, and it is a streaming graph engine.

> [04:12 - 04:23]
It is used in risk control, in payment of Alipay and in twenty, twenty, twenty nine in twenty nineteen.

> [04:23 - 04:31]
Another fusion engine was deployed in our production. The engine is only learning.

> [04:31 - 04:40]
We feel the three computing types, including streaming, M, L, and online serving. So you can know that.

> [04:40 - 04:49]
Online serving at this time is also the online serving. First time was deployed in art, and it is today's topic.

> [04:49 - 05:00]
And in twenty, twenty, given the diversity of business, we made a multi tenant architecture of Ray.

> [05:00 - 05:11]
Which means you can run a lot of red jobs in one big cluster. And in, in this job, you can.

> [05:11 - 05:16]
Support different computing paradigms.

> [05:16 - 05:28]
And in twenty twenty one, the artery was been more stable. We, we have do some more collaboration, collaboration with our ecosystem.

> [05:28 - 05:35]
Company such as Alibaba, Damo Academy, China Network and Wangshan Bank.

> [05:36 - 05:43]
And in twenty twenty two, we explored a private computing, which is a new scenario.

> [05:43 - 05:53]
We think that it is a good scenario for, for Ray, because in private computing.

> [05:53 - 06:01]
We need a flexible framework to support common function, data and AI.

> [06:01 - 06:07]
And it is there. There are a lot of advantages, injury for it.

> [06:08 - 06:17]
Okay, in this year, we aim to build a general AI.

> [06:17 - 06:27]
Serving framework, which in, in this framework work, we want to unified traditional AI, large language model and search engine.

> [06:28 - 06:38]
So this is today's topic. Back to the online survey from the historical timeline. You can know that.

> [06:38 - 06:48]
The, the, the online serving was, was first deployed in Ant in twenty nineteen.

> [06:48 - 06:54]
And it is integrated to the online learning engine.

> [06:54 - 07:02]
Depends on this. We build the basic ability of reserving and integrated it into infrastructure.

> [07:02 - 07:12]
Of art group, you know that each company has its customer infrastructure. So we, we need to adopt it.

> [07:13 - 07:19]
And in we, we have, we have another scenario.

> [07:19 - 07:30]
Online resource allocation, you can, you can. You can imagine that if the resource is, is for payment and finance.

> [07:30 - 07:38]
What's the challenges. We think the challenges is that we need a more flexible, high performance.

> [07:38 - 07:49]
And scalable, stable, a, A framework. And fortunately, we, we, we achieve it in based on re survey.

> [07:49 - 07:57]
And in twenty twenty in twenty twenty two we support the large scale online serverless platform.

> [07:57 - 08:07]
At this time, we served models with two hundred and forty thousand calls, and our event driven serverless platform.

> [08:07 - 08:17]
The one point three, seven million peak T, P, S. Okay, that's all of our private, private works.

> [08:17 - 08:24]
Next, Chong will introduce our recent achievements this year.

> [08:25 - 08:31]
Welcome, all right, thanks, Guya. And hello, everyone.

> [08:31 - 08:40]
My name is Chong Li, and I'm very glad to be here to share our most recent achievements in.

> [08:40 - 08:50]
In any group, we have already built the largest inference platform. Our inference clusters have point five million CPU cores, and four K.

> [08:50 - 08:59]
GPU cars in total, and I believe you guys have already seen these numbers at Dr. Stoica's keynote speech yesterday.

> [08:59 - 09:09]
And to deliver this hardware, we are using over twenty-seven thousand worker nodes in total. and as a inference platform.

> [09:09 - 09:18]
We have very highly active model deployments in our platform. We have over three new model deployments every week.

> [09:18 - 09:28]
And over one model updates every week. And our inference clusters are highly auto scalable.

> [09:28 - 09:40]
Thanks to our productized and standalone autoscaler, our inference classes can now be autoscaled over three thousand times every week.

> [09:40 - 09:49]
Proactively, and by doing so, we have increased our average CPU utilization by over 20%.

> [09:51 - 09:58]
So next, I will talk about some new scenarios in our productions and some new features we did.

> [09:59 - 10:11]
Before getting into the details, I'd like to firstly show an overview about our reserving architecture, it is not much different from the open source reserve.

> [10:11 - 10:23]
In this architecture, we have a serving keeper, it receives all their serving inference job submissions from the user clients.

> [10:23 - 10:34]
And it has to distribute these serving jobs across our serving clusters. But for each of them, the serving keeper has to create.

> [10:34 - 10:46]
And corresponding application master in one particular serving cluster. And this application master will create multiple proxies, and deployment actors.

> [10:46 - 10:56]
Within the cluster. And when the proxies are ready, they will register themselves to independent service discovery component.

> [10:57 - 11:10]
And by subscribing to this component, our user applications can get to know the locations of every proxy and carefully pick the most suitable one to send there.

> [11:10 - 11:20]
Inference requests. And in every proxy, you have to assign the incoming inference requests.

> [11:20 - 11:27]
To its local deployment actors, where the model serving work will be done there.

> [11:29 - 11:40]
Okay, so new scenarios, the first one is doing the model solving work on GPUs to make it happen, we chose to use NVIDIA Triton.

> [11:40 - 11:51]
For those of you unfamiliar with Triton. It is Nvidia's single node model inference ensemble. It supports multiple.

> [11:51 - 12:00]
Inference backends. And in our reserving system, the Triton servers could be very easily distributed.

> [12:00 - 12:08]
All we need to do is running the making our deployment actor become a Triton bootstrapper.

> [12:08 - 12:18]
So whenever our application master creates a new deployment actor, it will immediately boost up the Triton server inside.

> [12:18 - 12:26]
And with the help of our actor, long time environment, this long time environment feature is.

> [12:26 - 12:38]
Very useful, it is provided by the open source recall, and it helps a lot when we are dealing with data dependency package or library dependency programs.

> [12:38 - 12:45]
And I believe our recall team contributed nearly half of their implementations to the open source.

> [12:46 - 12:57]
Right, so when these Triton servers are ready, they can choose to register themselves to this discovery, service discovery component.

> [12:57 - 13:06]
And the upcoming inference requests can be connected to these Triton servers directly.

> [13:06 - 13:18]
And one thing to mention is that because our serving cluster is highly autoscalable, so when you run the Triton servers in our platform.

> [13:18 - 13:23]
They become auto scalable, as well.

> [13:23 - 13:31]
Okay, next scenario is serving the L, M applications the.

> [13:31 - 13:48]
The background of this thing is in our end group, we have a system called GPT cache in this system, we will try to store the historical LLM responses in our vector or cache stores.

> [13:48 - 13:58]
So whenever there is a new inference request coming in, the first thing we do is running a similarity comparison. So if the cache is hit, then we just.

> [13:58 - 14:10]
Respond the pre-start responses back to the user, and if cache misses, then the inference request still has to go through the model serving pipeline.

> [14:12 - 14:24]
And in our re serving platform, this check, this G, P. T cache system could be very easily integrated. All we need to do is running this.

> [14:24 - 14:33]
Gpt cache system inside our deployment actor. And still, with the help of the actor, runtime feature.

> [14:33 - 14:43]
And of course, we need an ingress actor in the cluster. And it will help us forward, every incoming inference request.

> [14:43 - 14:53]
To the Gbt cache actor at the first place. And then we still do the same thing. If cache hit, then we do a quick response.

> [14:53 - 15:04]
If cache misses, then we just forward this request to another Triton server, which is also running in a deployment actor.

> [15:06 - 15:17]
So one big thing you can see here is in this picture, the GPD cache actors are running on CPU nodes.

> [15:17 - 15:27]
And the Triton servers are running on GPU nodes. So thanks to Ray calls, heterogeneous results scheduling.

> [15:27 - 15:36]
We can now distribute these different kinds of actors more wisely and optimize the overall resource utilization.

> [15:39 - 15:49]
Okay, so next is some new features. The first one is built in async broker. We did this because in.

> [15:49 - 15:58]
Most of our model serving scenarios, we found the inference requests have very different execution time.

> [15:58 - 16:07]
So for these long requests, people always have to pay a lot of centralized waiting overhead.

> [16:07 - 16:18]
So what we did here is deploying an async broker in the serving cluster. And, of course, this async broker is running in a deployment actor.

> [16:18 - 16:26]
As well. And this async broker can receive and queue every incoming inference request.

> [16:26 - 16:37]
For these long requests, when the results are ready, the async broker can help us return these results back to the users async nicely.

> [16:40 - 16:52]
And one big benefit from this async broker is that with this inside the cluster, the other deployment actors.

> [16:52 - 17:04]
Can actually pull the inference requests from this broker adaptively based on their own busy or idle status.

> [17:04 - 17:12]
So by doing so in every deployment actor, which is running the model serving with Triton server.

> [17:12 - 17:18]
In each of these deployment actor, we can see much less head of line delays.

> [17:19 - 17:29]
So in our evaluation, compared to the baseline, which is round robin push based request assignment.

> [17:29 - 17:35]
Our poor based method can give us two times better throughput.

> [17:38 - 17:48]
The next feature is C plus plus deployment. This one, this feature has been widely deployed in our recommendation and advertising.

> [17:48 - 17:58]
Services, these services are latency sensitive with high throughput. So because of this performance requirements.

> [17:58 - 18:09]
Our deployment actors has to be high performance as well. So what we did is using C plus plus deployment actors.

> [18:09 - 18:19]
Based on open source rates, C plus plus workers. And by the way, this C plus plus workers is also.

> [18:19 - 18:31]
mainly contributed by our Ray team, so thanks Guyang for his effort on this, okay, so with this C++ deployment actors in hand.

> [18:31 - 18:40]
One big thing we did is implementing C plus plus direct ingress. It is a high performance RPC service.

> [18:40 - 18:49]
And with this feature, our inference request can directly connect it to our C++ deployment actors.

> [18:49 - 18:54]
By passing all these proxies that I have been mentioning above.

> [18:56 - 19:05]
And another big thing is native Triton inference call. This thing can be done because we now have these C plus plus.

> [19:05 - 19:15]
Deployment actors and the Triton server, which can be considered as a C plus plus library, could be more closely and.

> [19:15 - 19:26]
Efficiently integrated without any cross language overhead. And when we are making the C plus plus deployment actors.

> [19:26 - 19:35]
Working together with other C plus plus components in our recommendation and advertising timelines.

> [19:35 - 19:40]
And we are actually doing a more holistic, distributed system.

> [19:43 - 19:54]
Okay, next I will talk about some future plans, the first thing we are going to do is the Shardit deployment.

> [19:54 - 20:03]
The motivation for this thing is in our recommendation and search services with CVR or CTR models.

> [20:03 - 20:15]
We can always see numerous items with large feature data, and this feature data size is too large to be.

> [20:15 - 20:27]
Fit in any single worker node. So what we have to do is trying to shut this large size feature data.

> [20:27 - 20:35]
Across multiple work nodes. And, of course, we will create proxy deployment.

> [20:35 - 20:46]
Actor, actually. And use this proxy to help us do a shut away routing strategy and make sure every incoming.

> [20:46 - 20:56]
Inference request could be forwarded to a specific note, with the data dependency locally available.

> [20:59 - 21:10]
Okay, so the last thing is actually a very big picture we are hoping to deliver a high performance general AI framework.

> [21:11 - 21:19]
To make it happen, the first thing we are going to do is keep constructing and.

> [21:19 - 21:27]
Polishing our rate serving platform based on open source reserve, which has been proven.

> [21:27 - 21:37]
To be highly distributed, multi language, supportive and scalable. And we do believe this could be a very good foundation for.

> [21:37 - 21:41]
Many of the models serving scenarios.

> [21:42 - 21:51]
We will definitely use our direct ingress and use it to build a high performance Rpc service.

> [21:52 - 22:02]
We will. We will widely use the C plus plus deployment actors, because it can give us a high performance.

> [22:02 - 22:11]
Computing capability. And we will start working on this sharded deployment, which gave us.

> [22:11 - 22:24]
High performance, local data access and data retrieval. And we think this feature could be very critical when we are dealing with large scale model serving.

> [22:24 - 22:32]
Problems in the future. So that's basically all we have for today, so.

> [22:32 - 22:44]
As I said in the beginning, this work is mostly done by Teng Wei from our buddy team, so we will try our best to answer questions here, but if we cannot,

> [22:44 - 22:53]
I do encourage you guys send emails to this address, and I believe he can give the most detailed answers.

> [22:53 - 22:58]
Thank you.

> [23:02 - 23:10]
So the direct ingress and the C++ work that you have done for how much of that is integrated into the Rekor?

> [23:11 - 23:23]
It's already open sourced, but it's not very popular, actually, in the open source community, but we use that a lot in our productions.

> [23:23 - 23:32]
Cause in the, in the recommendation and advertising systems, cause we hope to make all components in our.

> [23:32 - 23:40]
Pipeline, the recommendation, pipeline are all implemented in C plus plus and making the whole pipeline more holistic.

> [23:42 - 23:50]
One follow up question on that is that in that space that you just mentioned, which is the recommendation pipeline.

> [23:50 - 24:00]
How, like, what are you really using Ray for, Because using Triton for inference, right. And you're using this direct ingress. But what role.

> [24:00 - 24:11]
What role is Ray playing there, how is Ray helping you in that space? Yeah, we definitely use Ray's runtime environment.

> [24:11 - 24:20]
To help us to integrate this Triton dependency in our deployment actor.

> [24:20 - 24:30]
And we use race heterogeneous scheduling to help us schedule these actors.

> [24:30 - 24:40]
CPU dependent actors or GPU dependent actors. They can all be scheduled well and help us increase the resource utilization.

> [24:46 - 24:54]
Thank you for the talk. A quick question. So you mentioned that there are about three plus deployments.

> [24:54 - 25:02]
The deployment per week. And my question is, for one type of model, like, what's the like.

> [25:02 - 25:12]
Average or usual frequency for deployments. Let's say we have a large language model. And then how often do you.

> [25:12 - 25:20]
Do updates and deployment. Yeah, I guess this range you can. You got me here.

> [25:20 - 25:28]
I don't really know the details. Yeah, so that question, that's what you. You should send emails to Teng Wei.

> [25:28 - 25:32]
Right, because that's some details from the serving team.

> [25:37 - 25:47]
It's a sharding deployment related to the choice of ray. The sharding deploying what, Yes, it's a sharding deployment related to the choice of ray.

> [25:47 - 25:58]
It's, yes, it's still on Ray. We use, we just need to shut this feature data across multiple worker nodes, but the worker nodes still.

> [25:58 - 26:05]
It's built on ray, and all the actors are handled, are reactors.

> [26:13 - 26:23]
So all of this is running on top of like Vms. Right, not Kubernetes or anything else in between. Just bare Vm. I'm saying, what is this all just running on.

> [26:23 - 26:33]
Vms, or is it running on Kubernetes or is it running on, Yeah, yeah, we are. We are definitely running our ray cluster. Ray clusters in the cloud, native environment.

> [26:33 - 26:38]
On top of Kubernetes.

> [26:43 - 26:50]
Oh, well, if there are no more questions, then thank you so much.

