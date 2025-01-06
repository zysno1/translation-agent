# Faster Model Serving with Ray and Anyscale | Ray Summit 2024

## 视频信息
- 视频ID: LKUBwGTUDZE
- 视频标题: Faster Model Serving with Ray and Anyscale | Ray Summit 2024
- 视频URL: https://www.youtube.com/watch?v=LKUBwGTUDZE

## 原文
[00:03 - 00:13] Hi everyone, I'm Akshay, I'm the engineering lead on Racer, and with me I have Ed, who's behind the creation of Racer and been leading Racer since the beginning.

[00:14 - 00:21] So quick show of hands, how many of you are using Racer already or have at least tried it out?

[00:21 - 00:31] Cool, and how many of you have made it to production, all right, it's great to see like the more and more people take Racer all the way through.

[00:31 - 00:45] So today we'll be talking about fast and reliable model serving with Racer and AnyScale, so since a lot of you I saw are still new to Racer, we'll go a little bit over the overview and motivation behind,

[00:45 - 00:56] Building Reserve and also some of the cool things we've been doing in twenty twenty four, then I'll talk about why Reserve is particularly well suited for Gen AI applications.

[00:56 - 01:05] And then finally, Ed will talk about some of the extensions we've been doing to make Racer really great on any scale, and any scale really the most complete.

[01:05 - 01:12] Performance way for model survey, so let's get right into it.

[01:12 - 01:21] So this was how we came about building racer. So if you guys are building Ml applications.

[01:21 - 01:30] You're typically doing more than just building one model, so let's imagine a case of a recommendation system or a computer vision system.

[01:30 - 01:39] In the case of a CV application like our friends at Samsonia did, they had a bunch of different models, maybe some for segmentation, some for classification.

[01:39 - 01:50] And then some additional business logic on top to actually round out their complete service. Now, the most typical way of deploying it is using microservices.

[01:50 - 01:59] And a lot of you are still in this scary land where every component is its own microservice, and then each of these are scaling independently.

[01:59 - 02:11] And so on. But there are some drawbacks to this one. It's really hard to innovate. There's one single application that is now split across many different configs, images.

[02:11 - 02:18] You have to set up separate CICD pipelines, separate monitoring for each of these individual microservices.

[02:18 - 02:27] And then when you're upgrading them, you have to make sure things are backwards compatible. So this can really slow down and add a lot of operational burden.

[02:27 - 02:35] Secondly, you can't really share resources that easily. So let's take our Cv example where.

[02:35 - 02:46] You could do some business logic just on CPUs and maybe your segmentation model needs to run on some kind of GPU, let's say, A10G and your classification needs to run on a different kind of GPU.

[02:46 - 02:54] This is hard to express inside one single microservice and then get the most out of your hardware.

[02:54 - 03:02] This is especially harder as you go to LLMs where you're deploying models across multiple GPUs.

[03:03 - 03:13] So this was the motivation behind building Racer, we wanted a flexible, scalable and efficient framework for online inference, so let's break that down.

[03:13 - 03:22] The first aspect was simplicity, so everyone uses Python for ML development, so this had to be a framework that was Python native.

[03:22 - 03:33] With a simple decorator, you could go to production, so with Reserve, you can just add the serve.deployment decorator on top of your business logic and ML model classes.

[03:33 - 03:43] And that's really all it takes for anyone, whether it's a data scientist or an ML platform engineer, to take this model to production.

[03:45 - 03:57] Then we wanted to add first class support for many model inference, so in our previous CV case, you could compose each of these as separate razor deployments, each with their own resource needs.

[03:57 - 04:11] and they can scale independently within the same service, and you can also do things like fractional GPUs, so let's say one of your models only needs a quarter or a half of a GPU you can express that and they can scale independently,

[04:11 - 04:18] Within the same service and there's also another pattern in racer that's popularly used called model multiplexing where.

[04:18 - 04:27] You might have thousands of fine tuned models, one per customer, and you can deploy these very efficiently on one pool of replicas.

[04:27 - 04:39] And one deployment, and finally we wanted to make it very flexible so you can use, you can deploy any gen AI models, any application on top of Reserve.

[04:39 - 04:50] And get the most out of your underlying hardware. And all of this needed to be production ready. And this, this is available on both Kubernetes in open source. as well as any scale.

[04:51 - 05:00] Here are some of the really cool success stories we've seen over the years, so Samsara saved 50% of their annual inference costs.

[05:00 - 05:11] By moving to Reserve, so they were deploying this kind of monolithic architecture and when they had a more expressive framework with Reserve, they could really get better hardware utilization.

[05:11 - 05:20] And Financial really took Razor to the next scale by building a 4,000 GPU node online serving cluster for recommendation systems.

[05:20 - 05:27] And then Clary on any scale improved performance by over twenty percent by using model multiplexing with Rayserve.

[05:27 - 05:36] And we see this graph on the right hand side, which kind of shows the exponential growth trend since we launched Racer back in twenty twenty two.

[05:36 - 05:46] And just since last race summit, we've seen Forex growth in clusters and users. So this really speaks to kind of the adoption and race across the community.

[05:48 - 06:00] So let's talk about some of the things we've been doing in twenty twenty four so there's three main areas of focus for us one is keep pushing this cost and performance optimizations in reserve.

[06:00 - 06:09] Make it more flexible for Gen AI applications. And then thirdly, keep pushing the production readiness so you can go.

[06:09 - 06:19] Production with racer very reliably. Here are some of the main features. There's a lot of other things that happen, but I just list out some top four.

[06:20 - 06:28] First, we remamped our autoscaling and load management in Racer, so we heard some feedback from the community for autoscaling to be more responsive.

[06:28 - 06:36] And also have capabilities for load shedding, for better safety and production. So these were added in racer in.

[06:37 - 06:46] In we launched multiple application support. So this is where you can deploy multiple separate Ml applications with their own.

[06:46 - 06:57] Upgrade life cycles in the same race of cluster. And one piece of feedback that the community had first, they loved the feature. And a lot of people started using it.

[06:57 - 07:05] Because it enabled better hardware utilization, but they wanted to separate out the dependencies for these with ML.

[07:05 - 07:14] Packages getting really bloated these days. This was important as you're deploying different types of models. So we added support for separate container images.

[07:14 - 07:19] Within the same rate service.

[07:19 - 07:31] And this was one I was really excited about because this reflects how serious Racer is becoming across the community, this was a community contributed feature for running Racer on any hardware accelerator,

[07:31 - 07:41] So folks from Google and Amazon and Intel contributed to Ray to run RayServe on whether it was TPUs on Google Cloud.

[07:41 - 07:49] Inferentia on Amazon Cloud and Habana chips on Intel, so you can run Racer really on any type of accelerator.

[07:50 - 07:58] And finally, we've been partnering with other companies to also add support for the best in class frameworks for online inference.

[07:58 - 08:07] NVIDIA Triton, who we partnered with, now supports an integration where you can get the performance benefits of Triton on top of Razer.

[08:07 - 08:12] And then there's also TensorRT LLM and VLLM support.

[08:13 - 08:22] Cool, now let's look into why Reserve is really great for Gen AI applications, and Gen AI comes with a lot of unique challenges.

[08:23 - 08:28] So we'll do that with a case study on serving LLMs on top of Reserve.

[08:29 - 08:37] So first big challenge is models are absolutely huge these days, there's seven B models that were commonly.

[08:37 - 08:44] Used in the beginning that were fourteen gig, but now we have like seventy B and four or five B models which are approaching a terabyte.

[08:44 - 08:53] And GPUs are extremely expensive, and the availability doesn't seem to be getting that much better, so you can see A10G, which has...

[08:53 - 09:04] Twenty four gigs of memory is already pretty pricey and then when you get to H one hundred the cost of deploying these systems becomes really really high so that means you really want to get,

[09:04 - 09:16] As much out of your hardware as possible so at any scale we were looking earlier this year on how can we make a great simple.

[09:16 - 09:22] Experience for people to deploy LLMs, and these were some of the use cases people came to us with.

[09:22 - 09:31] First, this is really table stakes, you have to do multi GPU, these models are often not big enough to fit in one GPU memory.

[09:31 - 09:39] And now we also see multi-node, so you have to enable these one terabyte models to run across multiple nodes.

[09:40 - 09:49] High performance serving is extremely critical, as I mentioned earlier, the cost of these GPUs is really high, so you have to get.

[09:49 - 09:54] The best in class performance that you can.

[09:54 - 10:03] Another common pattern that people are doing with LLMs is adapting it to their own domains, and they might do it separately for different customers as well.

[10:03 - 10:09] So people want to serve many different fine tuned models inside the same cluster.

[10:10 - 10:18] And then a common pattern is also serving many different base models, so imagine you're building a chatbot.

[10:18 - 10:26] Where some queries could be handled with a B model, but some need some more advanced reasoning where you need to route that query to a B model.

[10:28 - 10:37] And then, of course, LLMs are kind of like any other model in which you can just take a model behind an endpoint and call it an application.

[10:37 - 10:43] You need to build more components around it. So retrieval, augmented generation is extremely common.

[10:44 - 10:51] And then this is a really unique and cool requirement where you need to be able to go hybrid cloud.

[10:51 - 11:02] A lot of times people can't get the GPUs they need on just AWS or Google Cloud, and they'll procure GPUs from a vendor like Lambda Labs or CoreVave or one of these other third party providers.

[11:02 - 11:06] And you want to be able to use all your GPUs efficiently.

[11:08 - 11:16] So this is how we went about solving it in Racer, this is kind of what the very high level architecture of this library looks like.

[11:16 - 11:30] First, we have one Rayserve deployment that can handle all the OpenAI APIs and business logic, and this is critical for integrating with any of your other LLM tooling, like Lanchain, Lama Index, and so on.

[11:30 - 11:39] And these can run on CPU only, and then behind the scenes, you can have many different LLMs that can be easily set up with configuration files.

[11:39 - 11:48] And you can deploy an 8B model or a 70B model as well as embedding models, so let's look at how it addresses some of our use cases.

[11:49 - 11:57] Model parallel is very easy to set up, and this is one of the core strengths of RAISE, managing and orchestrating Python processes.

[11:57 - 12:05] Across different GPUs, in fact, even pipeline parallelism is now possible with the new compiled graphs API that we just launched.

[12:05 - 12:17] And we've been experimenting with that internally, high performance, so here we support VLLM, TensorRT LLM, really any inference engine under the hood that you want.

[12:17 - 12:25] But we've also been working on our own proprietary kernels to really speed up some of the execution.

[12:26 - 12:37] Multi LoRa or multiple fine tuning models is possible with Racer's multiplexing support, so the way it's set up is we use a Racer multiplex deployment.

[12:37 - 12:46] And that can efficiently swap and load in the Lora weights as needed, and then use VLNM support for running inference on many Loras in the same batch.

[12:47 - 12:57] Multimodal inference, so doing eight B and seventy B across one service is also possible to set up with this library quite easily.

[12:57 - 13:02] And you can upgrade the engine in one go.

[13:03 - 13:10] And finally, hybrid cloud is also possible. So something that we did internally, as well as our customers are doing.

[13:10 - 13:24] So taking like this example of a 70B model that's running on an H100, some of it is running on AWS nodes, but it also has the ability to burst into Lambda Labs capacity or some people are going the other way where,

[13:24 - 13:31] They might have a lot of reserve capacity on a third party cloud, and then they burst into the cloud when they need extra capacity.

[13:32 - 13:43] And let's look at how you would set up a retrieval augmented generation system, so this is very commonly used to introduce more context into an LLM's response.

[13:43 - 13:52] So this, on a high level, consists of two parts, once you get the user query, you're going to do the retrieval, which itself contains.

[13:52 - 14:03] generating and embedding, and doing a vector search over your vector database, and then converting that into the context and prompt that you can then send to your LLM.

[14:03 - 14:16] And then send the final response to the user I talked about racers model composition earlier, and that is perfectly suited for the rag pattern where you can set up all of these as separate tracer deployments.

[14:16 - 14:26] That can use different resources and scale up independently Now I'll hand it off to Ed to talk about some of the awesome extensions we've been doing with Racer on any scale.

[14:27 - 14:37] Okay, thank you Akshay, hopefully everybody can hear me, yeah so I'm going to talk a little bit about some of the cool features we've been building to make Rayserve work great on any scale.

[14:39 - 14:47] Okay, so for people who aren't too familiar with the AnyScale platform, I think the way to think about it is that it's really like an extension of Ray.

[14:47 - 14:56] Array is like the AI compute engine. It makes it really easy to write distributed programs, do all of the cool things for online serving applications that Akshay mentioned.

[14:56 - 15:09] But there are a lot of other things around that, like cost tracking, administration features, observability, production readiness, that don't really fit into the scope of Ray, but you need if you want to really go to production and have an end to end platform.

[15:09 - 15:19] So AnyScale is our attempt at building around Ray something that's really well integrated into it and does offer you this end to end AI platform.

[15:19 - 15:30] So for Rayserve, there are a couple of kind of key areas that we focus on, the first is adding really good support for like end to end observability and debugging.

[15:30 - 15:42] This is especially important for online serving applications, you know, it's really crucial that you can understand, you know, if you have a latency spike, why is that happening, if things go wrong, you know, where did they go wrong?

[15:42 - 15:47] And have monitoring alerting, I'm sure many people are familiar with this.

[15:47 - 15:54] In a similar vein, we also focus a lot on making sure that everything is hardened and production ready.

[15:54 - 16:06] And AnyScale also has a lot of unique opportunities because it is this like full stack all the way from kind of managing the hardware to the ray layer to the library layer to the application code.

[16:06 - 16:14] We have some great opportunities to make full stack optimizations and improve performance and save cost.

[16:14 - 16:25] So let's talk about each of these in a little bit more detail, so the first is observability and debugging, so AnyScale comes kind of packaged with an integrated UI that shows you like,

[16:25 - 16:35] status at a glance, and historical information, and also has a lot of collaboration features built in, and we also have solutions for logs and metrics out of the box.

[16:35 - 16:41] And I didn't mention here, but we also have an integration for distributed tracing support.

[16:41 - 16:54] So let's take a closer look at what it looks like when you run a race serve application on AnyScale, so this is maybe a little bit small to see, but this is basically just the dashboard that you see for an AnyScale service.

[16:54 - 17:04] So here you can see that this service on the top left is currently in the rolling out state, which means that it's incrementally moving towards a new version because it got deployed.

[17:04 - 17:14] For each of the versions, we can see all of the key metadata, like the image that was used, the compute configuration that was used, what version it was, who deployed it when.

[17:14 - 17:20] So it gives you this at a glance view of what is going on with my application.

[17:20 - 17:32] And in addition to this, we also have metrics that are built directly into the platform, so here I just picked two at random, one is like a utilization metric and another is a QPS metric.

[17:32 - 17:41] But we have a host of built in dashboards that are useful out of the box, and you can also customize your own Grafana dashboards and add alerts as needed.

[17:42 - 17:56] One of the things that I'm really excited that we sort of launched this year into the platform is built-in support for log aggregation and search, so when you launch a service on any scale, you now get a view like what I have at the center of the screen here.

[17:56 - 18:07] Where it aggregates all of the logs, not only across all the nodes of one cluster, but even across multiple clusters over time as you're like deploying and upgrading and so forth.

[18:07 - 18:17] And you can filter based on the version, the component, like what application it is, and you can even search, so for example here I'm searching for a given request ID, and I can see,

[18:17 - 18:29] What happened for that request ID across the system between, you know, race serve level logs and application logs, so this is just like an absolutely invaluable tool and it's awesome to have it just work out of the box.

[18:31 - 18:39] And then one other thing I want to mention is that one of the things we're announcing at Ray Summit is that AnyScale now works on Kubernetes as the compute backend.

[18:39 - 18:49] Basically, any Kubernetes cluster that you might run on. So you can kind of get the best of both worlds where you can run on your existing compute and integrate with other applications you have on Kubernetes.

[18:49 - 18:55] But get all of these features and the other ones I'll talk about in the talk in addition to that.

[18:56 - 19:03] Okay, so that's just like a short overview of the observability and debugging tools, let's talk a little bit about the improved production readiness.

[19:03 - 19:15] So another feature that we have on any scale is head node fault tolerance out of the box, so Ray has this concept of a head node, and by default it stores things in memory.

[19:15 - 19:25] So while generally there aren't any issues, if you do have a hardware failure or anything unexpected goes wrong, it can cause some downtime in the application.

[19:25 - 19:33] You can address this by enabling head node fault tolerance, but it adds more kind of operational burden because you need external storage.

[19:33 - 19:41] And on any scale, we configure that for you by default and handle the entire recovery process.

[19:41 - 19:48] Automatically, so if the head node does go down for any reason, you won't drop any requests and it will get recovered.

[19:49 - 20:00] We also have support for rollouts like you saw in the UI page, and one of the things that I wanted to talk about is we've also extended this recently to support incremental rollouts.

[20:00 - 20:04] So let's talk about what that is and why it's important.

[20:05 - 20:17] So here I have a diagram of what it looks like when you're running a service on any scale, so there's any scale control plane which kind of manages a load balancer as well as some ray clusters that are running applications.

[20:17 - 20:30] In this case, I have one ray serve cluster, and as Akshay mentioned, this could consist of multiple deployments, multiple models that are composed together in a pretty complex topology.

[20:30 - 20:40] But here I've simplified it down to just call it a cluster and say that it uses ten GPUs, this is in steady state so all of the requests are getting sent to this cluster,

[20:40 - 20:50] And they'd be load balanced across all of the nodes in the cluster. When we want to do an upgrade. A user would issue a deploy command, with a new configuration.

[20:50 - 21:01] And the AnyScale control plane would first create a new version of the cluster, and then it would update the load balancer to slowly do a staged rollout, for example, starting with 10% of the traffic.

[21:01 - 21:07] And then proceeding, assuming that all of the status and health checks look good.

[21:07 - 21:16] But there's a pretty big problem here in this picture, which is that now when you're upgrading your application, this requires twenty GPUs.

[21:16 - 21:25] And you'll notice that only ten percent of the traffic is going to the second cluster, so a lot of these GPU resources are probably going to be idle.

[21:25 - 21:33] And this is something that's a little bit of a unique problem for Rayserve because you can deploy these complex topologies on one cluster.

[21:33 - 21:43] Something like a standard Kubernetes deployment rollout doesn't quite fit into the model, so this is an area that we had a few customers.

[21:43 - 21:51] That had issues with it and we wanted to basically solve it and give you the best of both worlds, so let's talk about what any scale supports now.

[21:52 - 22:04] So the key difference is instead of spinning up the full version of the new application, or of the new cluster, we'll instead create basically a minimal version of it that uses the fewest resources possible.

[22:04 - 22:16] In this case, maybe it only needs one GPU, or maybe if there are two models, it would just be two GPUs, and then we will incrementally scale the old cluster down and the new cluster up.

[22:17 - 22:24] While also coordinating the traffic split so that each cluster is only getting as much traffic as it can currently handle.

[22:24 - 22:34] And in that way, what we can do is incrementally scale up, so for example, we would eventually reach a 50-50 split, and each cluster is about half the size.

[22:34 - 22:49] And then the new cluster would be approaching the full size, and then finally we would be able to finish the rollout, and this entire process would only have required sort of n plus one GPUs, so in this case only eleven instead of the twenty that we had with the naive solution.

[22:50 - 22:59] So this is a pretty simple feature and concept, but obviously it's a huge improvement, and it's also something that requires very careful coordination between.

[22:59 - 23:09] The control plane, the load balancer, and the clusters, so this is something that we were able to build because we have a control plane that is managing all of those components in tandem.

[23:11 - 23:19] Okay, so the last thing I want to talk about, the last major point about Rayserv on any scale is the full stack optimization work that we've been doing.

[23:19 - 23:31] So one optimization that we added this year was safe replica migration, so basically if we detect that the cluster is in kind of a suboptimal configuration.

[23:31 - 23:41] We will move replicas from one node to another in order to free up instances to be given back to the cloud provider. So this is a cost saving mechanism that's really useful if you have.

[23:41 - 23:46] Multiple models that are auto scaling up and down in tandem.

[23:47 - 23:55] We've also added support for serving on spot instances without dropping requests, so if a spot instance gets preempted, any scale will.

[23:55 - 24:05] handle that by spinning up a new copy and shifting the traffic over, and then the really cool thing that we do is we can also, when spot instances become available again,

[24:05 - 24:10] We'll shift back from on demand back to spot in order to save money.

[24:11 - 24:19] And then finally, a big pain point that we see across not just any scale customers, but also open source users and people doing model serving in general.

[24:19 - 24:27] Is that auto scaling can get really slow, especially for large models. So we've been working a lot on improving auto scaling speeds.

[24:27 - 24:36] So let's talk about that in a little more detail as Akshay mentioned earlier, models have just gotten absolutely huge.

[24:36 - 24:48] And this leads to some pretty serious problems, so I think a lot of people have probably seen this classic XKCD comic where people are slacking off waiting for code to compile.

[24:48 - 24:58] But I think we need to update it for the modern AI driven world, and we're still doing the same thing, but now our excuse is that models are loading instead of code compiling.

[24:59 - 25:06] So this really does lead to some serious problems. So in development, I'm sure basically everyone in this room has experienced.

[25:06 - 25:18] The productivity drain of just sitting there waiting for your Kubernetes cluster to auto scale and then the container to pull and then your giant Python code to start up and then massive model weights to load.

[25:18 - 25:25] You're just sitting around and waiting and not actually testing or developing or doing your job.

[25:26 - 25:35] And in production, this slow scaling often leads to over provisioning if you can't auto scale quickly in response to increased traffic.

[25:35 - 25:43] Then what you end up having to do is basically have more headroom and have more idle resources, which means that you're just wasting money on very expensive GPUs.

[25:45 - 25:54] So we ran a benchmark to kind of see what a typical setup of VLLM running on top of Kubernetes would look like.

[25:54 - 26:04] Oh, and my slides are out of order. Okay, I'm going to just go backwards. So we ran a benchmark here to see how long it would take for.

[26:04 - 26:11] BLM running on Kubernetes to spin up a new node, start a new pod, pull the container, and load the model weights.

[26:12 - 26:23] So here I have it on the plot on the right, for a seven DB model, it takes almost ten minutes end to end, and about half of the time is spent starting up a node and pulling a container image.

[26:23 - 26:31] And the other half of the time is spent waiting for VLLM to start up and to download the model and then to load the model into GPU memory.

[26:31 - 26:37] And this is for FP16, so the model weights are about a hundred and forty gigabytes total.

[26:38 - 26:47] So AnyScale has a couple of key optimizations here, the first is we have a custom container image format.

[26:47 - 26:55] Which makes it possible to pull large images much, much faster than using just like a default Docker container D client.

[26:55 - 27:06] Um, so what this looks like is when you start a cluster on any scale, you can provide any sort of generic container image, uh, so this could be hosted in ECR or like any container registry.

[27:06 - 27:13] It's basically just a ray image with custom dependencies, very similar to what you would use with QBray.

[27:13 - 27:23] And the first time that you use this image, we will pull the image from the container registry and then automatically optimize it into a custom image format.

[27:23 - 27:31] and then cache it in a per region bucket, so anytime you use the same image after that, the startup speed will be dramatically faster.

[27:32 - 27:40] So we ran an even simpler benchmark just measuring the time that it takes to pull two images, one's six gigabytes, it's just like a ray base image.

[27:40 - 27:53] One is thirteen gigabytes and that one is basically ray plus VLM and its dependencies and we compared EKS versus AnyScale and here you can see that AnyScale is dramatically faster for pulling the image and starting the container.

[27:53 - 28:02] So EKS, and this is after quite a bit of optimization effort, takes over a hundred seconds to pull the six gigabyte image.

[28:02 - 28:11] And for the thirteen gig image, it's like two hundred and thirty seconds, whereas any scale is much, much faster, only three and a half and sixteen seconds respectively.

[28:13 - 28:22] The other optimization we have is optimized model loading to help with the very large model weights.

[28:23 - 28:32] So the common solution that we see many of our customers do is something like this, so they have their model weights stored in AWS S three or another equivalent remote storage.

[28:32 - 28:38] And they'll first download from storage to disk and then load the disk into the GPU.

[28:38 - 28:47] But under the hood, this has some problems because you basically have like three synchronous steps, your first downloading from S three to the local disk.

[28:47 - 28:55] Then you're loading from local disk to CPU, then you're loading from CPU to GPU, and when model weights are really big, each one of these steps can be very slow.

[28:56 - 29:05] So AnyScale has a safe tensors compatible client that you can directly point at model weights that are in remote storage and load them directly to a GPU.

[29:06 - 29:18] Under the hood, this basically takes advantage of pipeline parallelism, and it will fetch the tensors chunk by chunk and stream them directly onto the GPU and avoid these synchronous copy steps.

[29:19 - 29:23] This results in much faster model download times.

[29:23 - 29:31] So in an experiment where we're just testing the VLM startup and the model loading aspect for a seven B and a seventy B model.

[29:31 - 29:39] You can see that for the 7B model on the left, the any scale client is about twice as fast as using the baseline.

[29:39 - 29:44] And for a seven DB model, it's almost, yeah, it's about five times as fast.

[29:46 - 29:59] So if you put these things together, end to end, AnyScale is able to scale up a new replica of a seven DB model for serving over five times faster than running basically the same setup on Kubernetes.

[30:01 - 30:12] Yeah, so with that, I'll wrap up and just wanted to highlight once again that, you know, AnyScale offers a lot of great extensions to really make Racer part of an end to end AI platform.

[30:12 - 30:17] Including observability, improved production readiness, and some really cool optimizations.

[30:17 - 30:25] And with that, I think we're pretty much at time, but Akshay and I will be around to answer any questions that you might have.


