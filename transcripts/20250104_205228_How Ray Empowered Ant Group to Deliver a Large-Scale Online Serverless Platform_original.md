---
video_id: _yu0Rtuetuc
video_url: https://www.youtube.com/watch?v=_yu0Rtuetuc
video_title: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
created_at: 2025-01-04 20:52:28
---

# How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform

> [00:06 - 00:08]
Hello everyone.

> [00:08 - 00:12]
We are gu Yang song and zli from art group.

> [00:12 - 00:17]
And today topic is from our buddy team lead by tg Wei cai.

> [00:17 - 00:21]
But he cannot come here today, so we'll be the speakers.

> [00:21 - 00:30]
And this is this is the first time we come here and we are so glad to share our work in race.

> [00:30 - 00:40]
And today topic is about how we empowered art group to deliver a large scale online service platform.

> [00:40 - 00:40]
Let's start.

> [00:41 - 00:46]
First, I'd like to introduce my company and my team.

> [00:46 - 01:00]
To summarize on group, there are five directions, digital payment, digital connectivity, digital finance, digital technology and globalization.

> [01:00 - 01:16]
And the most favours, our popular application of an group is alipewhich is leading the Internet, payment and finance in China and my team is anthree team.

> [01:16 - 01:23]
In the next page I will show you a lot, history, information of my team.

> [01:23 - 01:29]
But there I want to share some high level information first.

> [01:30 - 01:39]
First, we are the second largest team contributing to the ray open source software.

> [01:39 - 01:56]
We are collaborating with any scale and reslab for several years and we have over over 26% could contribute of the record part in the open source.

> [01:56 - 02:13]
Second, in addition to the developing rate, we also have a lot of a large scale application of rand in now in our production, we have over 1 million cpu calls.

> [02:14 - 02:25]
And then in China, we also have a rich China community which is created and operated by my team.

> [02:25 - 02:32]
And every, for over the past five years, we hosted the reforward meet up every year.

> [02:32 - 02:52]
And the fifth reforward has been finished in the past, in the past July and in this conference, any scale, cross AI aren't, have, a't and, bad dance has shared their works in this conference.

> [02:52 - 03:01]
So we, so, we are, we hope that ray could be more popular in China as in U S.

> [03:02 - 03:07]
Let's go to the part of the history of rain in art.

> [03:07 - 03:16]
My team is created in 2017 and in this year the ray is more different from today.

> [03:16 - 03:31]
Three, we we consider as the general distributed system, which means that we have we have a lot of non AI appliand framework.

> [03:31 - 03:45]
You know that in the re open source, reopen source focuses on the Python and AI, which means Python first and a first, but yet we are different.

> [03:45 - 03:55]
So you can know that, you can see that we have already contributed the pi, Java and C++api in the reproject.

> [03:55 - 04:05]
And in 2018, our first uyer uplayer engine was deployed in our production.

> [04:05 - 04:11]
The engine name is g flow and it is a streaming graph engine.

> [04:11 - 04:17]
It is used in risk control in payment of Alipay.

> [04:17 - 04:29]
And in 20 2029, in 2019, another another fusion engine is was deployed in our production.

> [04:29 - 04:31]
The engine is on learning.

> [04:31 - 04:40]
We filsed the three computing types, including streaming, ml and online serving.

> [04:40 - 04:51]
So you can know that online serving this time is also the online serving for time was deployed in art and it is totopic.

> [04:51 - 05:08]
And in 2020, given the diversity of business, we we made a multiarchitecture of ruh, which means you can run a lot of rjobs in one big reccluster.

> [05:08 - 05:16]
And in in this job you can support different computing paradigms.

> [05:16 - 05:22]
And in 2021, the entree was been more stable.

> [05:22 - 05:35]
We we have do some more collaboration with our ecosystem company such as alama duo Academy, China Network and wanshbank.

> [05:36 - 05:45]
And in 2022, we explored a private computing, which is a new scenario.

> [05:45 - 05:53]
We think that the, it is a good scenario for for rbecause in private computing.

> [05:53 - 06:07]
We need a flexible frameworks to support common function data a and A I and it is there there are a lot of advantages in jury for it.

> [06:08 - 06:28]
Okay, in this year, 2020 2023, we aim to build a general AI serving framework, which in in this framework work, we want to unified a traditional AI large language model and search engine.

> [06:28 - 06:32]
So this is the today topic.

> [06:32 - 06:34]
Back to the online surum.

> [06:34 - 06:48]
From the historical time line you can know that, the the the online serving was depwas first deployed in ant in 2019.

> [06:48 - 06:54]
And it is integrated to the online learning engine.

> [06:54 - 06:56]
Depends on this.

> [06:56 - 07:05]
We build the basic ability of reserving and integrated it into infrastructure of art group.

> [07:05 - 07:13]
You know that each company has its customer infrastructure, so we we need to adopt it.

> [07:13 - 07:22]
And in 2021, we we have have we have another scenario, online resource allocation.

> [07:22 - 07:34]
You can you can you can imagine that if the resource is is for payment and finance, what's the challenges?

> [07:34 - 07:44]
We think challenges is that we need a more flexible, high performance and scalable, stable, framework.

> [07:44 - 07:59]
Fortunately, we, we we achieve it in based on re and in 2020, in 2022, we support the large scale online surveplatform.

> [07:59 - 08:12]
At this time, we served models with 240000 calls and our event driven surveplatform reached the 1.37 million pc T P S.

> [08:12 - 08:16]
Okay, that's all of our private works.

> [08:16 - 08:24]
Next chwill introduce our recent achievements this year.

> [08:24 - 08:25]
Welcome.

> [08:25 - 08:26]
All right.

> [08:26 - 08:29]
Thanks, Guam and, hello everyone.

> [08:29 - 08:40]
My name is tonong Li and I'm am very, glad to be here to, share our most recent achievements in 2023.

> [08:40 - 08:46]
In end group, we have already built the largest inference platform.

> [08:46 - 08:52]
Our inference clusters have point 5 million cpu cand 4K, GPU cars in total.

> [08:52 - 09:00]
And I believe you guys have already seen these numbers at doctor stokers keno speech yesterday.

> [09:00 - 09:07]
And to deliver this hardware, we are using over 27000 worknotes in total.

> [09:07 - 09:14]
And as influence ference platform, we have very highly active model deployments in our platform.

> [09:14 - 09:23]
We have over 3000 new model deployments every week and over 100000 model updates every week.

> [09:23 - 09:28]
And our inference clusters are highly auto scalable.

> [09:28 - 09:41]
So thanks to our product ties and stand along auto scalar, our inference clusters can now be auto scaled over 3000 times every week proactively.

> [09:41 - 09:48]
And by doing so, we have increased our average cpu utilization by over 20%.

> [09:51 - 09:58]
So next I will talk about some new scenarios in our productions and some new features we did.

> [09:59 - 10:07]
Before getting to the details, I'd like to firstly show an overview about our Reay serving architecture.

> [10:07 - 10:12]
It is not much different from the open source reserve.

> [10:12 - 10:17]
In this architecture we have serving keeper.

> [10:17 - 10:29]
It receives all serving inference job submissions from the user clients and it has to distribute these serving jobs across our serving clusters.

> [10:29 - 10:40]
But for each of them, the serving keeper has to create a corresponding application master in one particular serving cluster.

> [10:40 - 10:47]
And this application master will create multiple proxies and deployment actors within the cluster.

> [10:48 - 10:57]
And when the proxies are ready, they will register themselves to independent service discovery component.

> [10:57 - 11:12]
And by subscribing to this component, our user applications can get to know the locations of every proxy and carefully pick the most suitable one to send their inference requests.

> [11:13 - 11:27]
And in every proxy you have to assign the incoming inference requto use local deployment actors where the model serving work will be done there.

> [11:29 - 11:32]
Okay, so new scenarios.

> [11:32 - 11:36]
The first one is doing the model solwork on gp s.

> [11:36 - 11:41]
To make it happen, we chose to use a video Triton.

> [11:41 - 11:51]
For those of you unfamiliar with a Triton, it is amvideo dious single node model inference ensymbol.

> [11:51 - 12:01]
It supposed multiple inference backens and in our reserving system, the Triton servers could be very easily distributed.

> [12:01 - 12:09]
All we need to do is, running the, making our deployment actor become a Triton boostriver.

> [12:09 - 12:19]
So whenever our application master creates a new deployment actor, it will immediately boots up the Triton server inside.

> [12:19 - 12:27]
And with the help of our actor runterm environment, this runtime environmental feature is very useful.

> [12:27 - 12:38]
It is provided by the open source recall and it helps a lot when we are dealing with data dependency package or library dependency programs.

> [12:38 - 12:46]
And I believe our recall team contributed nearly half of the implementations to the open source.

> [12:46 - 12:47]
Right.

> [12:47 - 13:06]
So when these tracking servers are ready, they can choose to register themselves to this discovery service discovery component and the upcoming inference request can be connected to these trtan servers directly.

> [13:06 - 13:21]
And one thing to you to you mention that is that because our serving cluster is highly auto scalable, so when you run the trton servers in our platform, they become auto scalable as well.

> [13:23 - 13:29]
Okay, next scenario is serving the area m applications.

> [13:29 - 13:38]
The background of this thing is in our end group, we have a system called GPT t cash acuh.

> [13:38 - 13:48]
In this system, we will try to store the historical L M responses in our vector or cash stores.

> [13:48 - 13:57]
So whenever there is a new inference request coming in, the first thing we do is running a similarity comparison.

> [13:57 - 14:11]
So if the cache is hit, then we just respond the pre storesponses back to the user and the if cash ache misses, then the inference request still has to go through the model serving pipeline.

> [14:12 - 14:22]
And in our reserving platform, this chat, this GPT t cash system could be very easily integrated.

> [14:22 - 14:33]
All we need to do is running this GPT cacsystem inside our deployment actor and still with the help of the actor runtime feature.

> [14:33 - 14:47]
And of course, we need a ingress ss actor in the cluster, and it will help us, forward every incoming inference request to the, gbt cash actor at the first place.

> [14:47 - 14:50]
And then we still do the same thing.

> [14:50 - 14:53]
If cash hit, then we do a quick response.

> [14:53 - 15:04]
If cash misses, then we just, forward work this, request to another Triton server, which is also running in a deployment actor.

> [15:06 - 15:21]
So one big thing you can see here is in this picture, the G P gpd cash acactors are running on cpu notes and the trident servers are running on GPU notes.

> [15:21 - 15:37]
So thanks to recourse, heterogeneous results scheduling, we can now distribute these different kinds of actors more wisely and optimize the overall resource utilization.

> [15:39 - 15:42]
Okay, so next is some new features.

> [15:42 - 15:46]
The first one is, building asynbroker.

> [15:46 - 15:58]
We did this because in most of our model serving scenarios we found the inference requests have very different execution time.

> [15:58 - 16:07]
So for this, long requests, people always have to pay a lot of, centrnchronised waiting overhead.

> [16:07 - 16:14]
So what we did here is, deploying an async broker in the, serving cluster.

> [16:14 - 16:20]
And of course, this, async broker is running in a deployment actor as well.

> [16:20 - 16:26]
And this async broker can receive an queue every incoming inference request.

> [16:26 - 16:38]
And for this long request, when the results are ready, the asynbroker can help us returning these results back to the users asynchronously.

> [16:40 - 17:03]
And one big benefit from this I think c broker is that with this inside the cluster, the other deployment actors can actually pull their inference requfrom this broker adaptively based on their own busy or idle status.

> [17:03 - 17:18]
So by doing so, in every deployment actor which is running their model serving with Triton server, in each of these deployment actor, we can see much less head of line delays.

> [17:19 - 17:35]
So in our evaluation, compared to the baseline, which is a wrong robbing push based request assignment, our poor based method can give us two times better throughput.

> [17:38 - 17:42]
The next feature is C++deployment.

> [17:42 - 17:50]
This one, this feature has been widely deployed in our recommendation and advertising services.

> [17:50 - 17:55]
These services are latency sensitive with high throughput.

> [17:55 - 18:04]
So because of these performance requirements, our deployment actors has to be high performance as well.

> [18:04 - 18:15]
So what we did is using C++deployment actors based on open open source race, C++workers.

> [18:15 - 18:22]
And by the way, this C++workers is also mainly contributed by our rteam.

> [18:22 - 18:25]
So thanks Gyang and for his effort on this.

> [18:25 - 18:36]
Okay, so with this C++deployment actors in hand, one big thing we did is implementing c plus direct in gress.

> [18:36 - 18:40]
It is a high performance rpc service.

> [18:40 - 18:54]
And with this feature, our inference request can directly connect to our C++deployment actors, bypassing all these proxies that I have been mentioning above.

> [18:56 - 19:01]
And another big thing is native Triton inference call.

> [19:01 - 19:20]
This thing can be done because we now have the C++deployment actors and the Triton server, which can be considered as A C plus plus library, could be more closely and efficiently integrated without any cross language overhead.

> [19:20 - 19:40]
And when we are making the c plus spas deployment actors, working together with other C++components in our recommendation tions and advertising time lines, and we are actually doing a more holistic distributed system.

> [19:43 - 19:48]
Okay, next I will talk about some future future planes.

> [19:48 - 19:54]
The first thing we are going to do is the sharted deployment.

> [19:54 - 20:11]
The motivation for this thing is in our recommendation and search services with cvr or ct R models, we can always see see numerous items with large, feature size, feature data.

> [20:11 - 20:19]
And this feature data size is too large to be fit in any single worker node.

> [20:19 - 20:30]
So what we have to do is trying to shut these large size feature data across multiple worker nodes.

> [20:30 - 20:56]
And of course, we will create proxy deployment actor actually, and use this proxy to help us do a shut away routing strategy and make sure every incoming inference request could be forwarded to a specific note with the data dependency locally available.

> [20:59 - 20:59]
Okay.

> [20:59 - 21:04]
So the last thing is actually, very big picture.

> [21:04 - 21:13]
We are hoping to deliver high performance general AI framework to make it happen.

> [21:13 - 21:33]
The first thing we are going to do is keep constructing and polishing our reserving platform based on open source reserve, which has been proven to be highly distributed, multi language, supportive and, scalable.

> [21:33 - 21:40]
And we do believe this could be a very good foundation for many of the model serving scenarios.

> [21:42 - 21:52]
We will definitely use our, direct ingress and use it to build a high performance rp c service.

> [21:52 - 22:04]
We will, we will widely use the C++deployment actors because it can give us high performance computing capability.

> [22:05 - 22:16]
And we will start working on this charted deployment, which give us, high performance local data access and data retrieval.

> [22:16 - 22:26]
And we think, this feature could be very critical when we are dealing with large scale model serving problems in the future.

> [22:28 - 22:32]
So, that's basically all we have for today.

> [22:32 - 22:39]
So, and as I said in the beginning, this work is mostly done by ten G Wei from our budteam.

> [22:39 - 22:43]
So, we will try our best to answer questions here.

> [22:43 - 22:53]
But if we cannot, I do encourage you guys send e mails to this address and I believe he can give the most detailed answers.

> [22:53 - 22:55]
Thank you.

> [23:02 - 23:12]
So the direct ingress and the C++work that you have done for how much of that is integrated into the open source?

> [23:12 - 23:19]
It's already open source, but it's not very popular actually in the open source community.

> [23:19 - 23:40]
But we use that a lot in our productions cause in the in the recommendation and advertising systems because we hope to make all components in our pipeline, the recommendation pipeline are all implemented in C++in making the whole pipeline more holistic.

> [23:42 - 23:55]
One follow up question on that is that in that space that you may just mentioned, which is the recommendation pipeline, how like what are you really using ray for?

> [23:55 - 23:58]
Because using Triton for inference, right?

> [23:58 - 24:04]
And you're using this direct in gress s, but what role, what what role is ray playing there?

> [24:04 - 24:07]
What how is ray helping you in that space?

> [24:07 - 24:19]
Yeah we definitely use race round harenvironment to help us to integrate this tiiton dependency in our, deployment actor.

> [24:19 - 24:32]
And we use race heterogeneous scheduling to help us schedule these actors, cpu dependent actors or GPU dependent actors.

> [24:32 - 24:40]
They can all be scheduled well and help us increase the results utilization.

> [24:46 - 24:48]
Thank you for the talk.

> [24:48 - 24:50]
Quick question.

> [24:50 - 24:58]
So you mentioned, there are about 3000 plus deployments model deployment per week.

> [24:58 - 25:07]
And my question is for one type of model, like, what's the like average or usual frequency for deployments?

> [25:07 - 25:14]
Let's say we have, large language model and then how often do you do updates and deployment?

> [25:14 - 25:31]
Yeah, I guess this range you can you got me here I don't really know the details Yeah so that question that what you you should send e mails to ten G Wei right cause that's some of details from the serving team.

> [25:37 - 25:42]
It's a shardeployment related to your choice of rain.

> [25:42 - 25:47]
Yes, it's a shdeployment related to the choice of ray.

> [25:47 - 26:05]
It's yes, it's it's still on rwe use we just need to shut this feature data across multiple waler notes but the Walker notes still it's built on ray and all the actors in are handled are are reactors.

> [26:13 - 26:19]
So all of this is running on top of like vm, not Kubernetes or anything else in between.

> [26:19 - 26:20]
Just bear vm.

> [26:20 - 26:23]
I'm what is this all just running on like vms?

> [26:23 - 26:25]
Or is it running on Kubernetes?

> [26:25 - 26:35]
Or is it running on like Yeah, we we we are definitely running our roclusters in the cloud native environment on top of Kubernetes.

> [26:43 - 26:48]
Oh, well, if there are no more questions, then thank you so much.

> [26:48 - 26:48]
Okay.

> [26:48 - 26:50]
Thank you, guys.

