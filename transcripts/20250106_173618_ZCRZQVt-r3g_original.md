# Ray at Scale: Apple's Approach to Elastic GPU Management | Ray Summit 2024

## 视频信息
- 视频ID: ZCRZQVt-r3g
- 视频标题: Ray at Scale: Apple's Approach to Elastic GPU Management | Ray Summit 2024
- 视频URL: https://www.youtube.com/watch?v=ZCRZQVt-r3g

## 原文
[00:05 - 00:10] Hello everyone, thank you and welcome to the talk, second to last talk of the summit.

[00:11 - 00:20] Today, Weiwei and I are going to talk about Elastic GPU Management for Ray, achieving scalability and efficiency for AIML workloads.

[00:22 - 00:31] So first, the introduction slides I have worked on or with the Ray community at Apple and before that at LinkedIn.

[00:31 - 00:41] And then Weiwei, do you want to talk about yourself a little bit, Yeah, hi everyone, my name is Weiwei and I'm working the data and Ava infrastructure in Apple.

[00:41 - 00:49] And basically help the team to build the infrastructure for running both data processing and machine learning workloads on multiple clouds.

[00:53 - 01:02] So today, we will give you a little bit of an overview of Ray. We'll discuss the scaling challenges with Gp workloads.

[01:02 - 01:10] Some of the techniques that we have tried for optimizing GPU capacity management and utilization.

[01:12 - 01:22] So why use Ray, Ray provides a unified computing API for data processing, training, tuning, serving.

[01:23 - 01:36] And for us, one of its kind of positives is that it provides this kind of seamless API that works on user's laptop all the way to the data center.

[01:36 - 01:44] Users can kind of try out small experiments that they can then migrate to the clusters without many changes.

[01:45 - 01:50] It has great support for model serving, including VLLM.

[01:51 - 02:00] Users use our Ray platform in three different ways, notebooks are used for early iteration.

[02:00 - 02:12] This is where they can try out early experiments, they can try it as if they're on their laptop, it's in an interactive mode, and then they can use the same APIs for a full scale,

[02:12 - 02:24] A large scale workload in the data center and then in addition to notebooks, users always demand like mature SDKs for programmatic job submission and model deployment.

[02:24 - 02:34] And then there's portals to support UX based model deployment and also for observability, which is like a very important part.

[02:34 - 02:42] Any productionized workloads, while Ray has many features, there are also quite a few challenges using Ray.

[02:44 - 02:52] One is resource sizing, so there's too many options when it comes to the kind of resource the users can request.

[02:52 - 03:01] That is not at the top of the ML practitioner's mind when they're trying to execute a batch inference job or deploying a model.

[03:01 - 03:09] Autoscaling kind of attempts to help it, but then also kind of brings its own challenges that we have seen.

[03:09 - 03:17] And then lastly, GPU utilization is a problem that both the ML practitioner and...

[03:17 - 03:25] The infra engineers try to solve because of the high demand for GPUs and the cost involved.

[03:27 - 03:36] So going deeper into this with the different infra resource choices that users have, so they have to choose.

[03:36 - 03:49] The kind of the nodes or machines based on the number of cards on the nodes, the GPU memory they have, the SRAM versus DRAM.

[03:49 - 03:59] The intra GPU and inter GPU connectivity, the network congestion in a particular geographic region they're choosing.

[03:59 - 04:14] the region's overall capacity and congestion, a lot of choices that are too hard to specify for a human being while they're launching a fairly large workload.

[04:14 - 04:23] Are productionizing a model deployment. So our observation has there been, there has been that.

[04:23 - 04:34] Pairing down the choices and providing some standard compute options are helpful, so think small, medium, large.

[04:34 - 04:44] And kind of provide abstractions that users can kind of talk to. And then they can choose that. Okay, I, I need kind of this and.

[04:44 - 04:54] Our platform then provides Ray the particular resource configuration based on the choices that the users make.

[04:54 - 05:01] While this doesn't optimize for every case, it sort of covers eighty percent of our cases.

[05:01 - 05:13] One intermediate step that we took on the way to kind of figuring out how to optimize GPU use cases and how to allow users to kind of provide the correct kind of nodes or machines.

[05:13 - 05:23] They need is to kind of come up with node specific cues and node specific clusters and that didn't work out well.

[05:23 - 05:31] So it kind of resulted in while the users, so we couldn't kind of give them these choices, then it ended up with.

[05:31 - 05:39] Kind of even more fragmentation and lower utilization that we had before that.

[05:39 - 05:50] So then we sort of backed out of that and then worked on multi level scheduling. So where the node level scheduling could.

[05:50 - 06:02] Handle multiple types of nodes and instances and kind of can fall back on different options when the primary, the user's primary asks are not available.

[06:05 - 06:18] Another important part of optimizing the GPU utilization is to support autoscaling because the resource utilization of large workloads, both for batch and for real time.

[06:18 - 06:27] Doesn't stay static it varies with the life lifetime of the workload we heard in earlier in the summit.

[06:27 - 06:37] Sergey from Meta was talking about how Lama needed to grow its bat size during the training, so we've observed similar things.

[06:37 - 06:45] Fortunately, Ray has native support for auto scaling, both for batch and for real time workloads.

[06:45 - 06:52] The way RAISE Autoscaler works is...

[06:53 - 07:03] Wait, so the way raised autoskeler works is like it kind of watches the metrics of the workers and and patches the.

[07:03 - 07:08] The CRD is based on that.

[07:08 - 07:18] We have this, we use Apache Unicorn, which watches the modifications that the RAISE autoscaler makes.

[07:18 - 07:27] And then queues up pods and workloads based on the additional needs of the autoscaler.

[07:27 - 07:35] And then it does the same on the downscaling side and tries to reconcile and bin pack the workloads together.

[07:37 - 07:45] And then, but with successful autoscaling, there are some challenges that come with it.

[07:45 - 08:02] So first is for very large workloads, we want to make a choice whether we want to get limited by geographical regions or do we want to go across geographical regions.

[08:02 - 08:14] If we want to go across regions, then there's data transfer costs to kind of consider, and then the next problem that occurs is like even with the single region,

[08:14 - 08:21] Workloads can be okay with upscaling, scaling up, but many workloads are not okay with downscaling.

[08:21 - 08:30] So this is what we saw in a lot of our kind of stateful workloads where downscaling caused failures.

[08:30 - 08:45] So for so a guard against that was to kind of make sure that, okay, workloads, our ray workers cannot be evicted so they can be upscaled, but they can not be downscaled.

[08:45 - 08:52] Now that resulted in lower utilization because now we have kind of created this.

[08:52 - 09:03] Workload that cannot be shrunk. So then with that, to kind of try to resolve that was to kind of focus more on checkpointing.

[09:03 - 09:13] Um, but there to support better checkpointing, we had to introduce better Apis from a platform that users could easily use to kind of.

[09:13 - 09:22] Have standard checkpointing across all different use cases.

[09:22 - 09:31] When we resolved that problem, the next problem was fast upscaling creates its own problems.

[09:31 - 09:42] Note initialization starts surfacing different issues such as like maybe the surface and the certificate management is not quite ready. The nodes are not quite.

[09:42 - 09:54] The IP address availability is not quite there, so all of those problems kind of started showing up when auto scaling became widely usable and the users could auto scale up fast.

[09:55 - 10:04] So to resolve that, we had to kind of work on keeping headroom in so to make sure that there's always some.

[10:04 - 10:12] Additional nodes available, which has trade offs with the kind of the utilization.

[10:12 - 10:23] None of these kind of steps would be possible without like our scheduler support, so now deep dive on the schedule will be provided by Weiwei.

[10:24 - 10:37] Thank you, Abin, so I will talk about GPU management and GPU resource prevention, which we use a lot, I think.

[10:37 - 10:49] The use case in IPo is huge that we have so many organizations, teams want to use Ray and how to really offer the limited GPU to all these teams, organizations.

[10:49 - 10:58] Is the key issue that we want to solve and why we're choosing approach unicorn. So approach unicorn.

[10:58 - 11:06] It's a Kubernetes resource scheduler, and because when we run Ray on Kubernetes, we really see a lot of challenges.

[11:06 - 11:17] Like one of the most important things is that resource fragmentation that we see, different GPU nodes are not fully utilized because such a fragmentation happens here and there.

[11:17 - 11:25] And also, it's very hard to manage GPU quotas, imagine that you have a lot of different type of instances.

[11:25 - 11:33] You want to share those instances with different teams is extremely hard to manage the quota for different type of GPUs.

[11:33 - 11:41] And also the GPU utilization is being a problem, is always being a problem, and we know that people are complaining about.

[11:41 - 11:57] Not getting enough GPUs, but at the same time actually sometimes GPUs idle, we don't want to see that happen, and also it's a lack of observability, I think that is one casing that are missing in a lot of places who are trying to build this really well.

[11:57 - 12:05] So Apparatio Unicorn actually help us to solve a lot of issues. It has the complexity of the infrastructure, the resources.

[12:05 - 12:14] From the ray. So let Ray to focus on the application side of things. And Unicron will handle the resource management, scheduling underneath.

[12:14 - 12:23] It's really, really for us is really bring the market tendency ready platform to our end users and also provides the huge cost savings along the way.

[12:25 - 12:34] And just a quick recap about Unicorn, it's a resource scheduler on Kubernetes, and it offers a lot of scheduling capabilities.

[12:34 - 12:46] And it provides really high efficiency and improved SRAs. And there are some highlights about the features Unicron provides, such as resource queues.

[12:46 - 12:54] That is essential for multitenancy and also offers the resource fairness between different queues.

[12:54 - 13:04] And offers the GAN scheduling, which is very, very important for machine learning workloads. And also, the resource, pretty sophisticated resource permission.

[13:04 - 13:09] I will explain more in this later session, and we use that a lot.

[13:10 - 13:20] And QBray with Unicode integration, the good news is that in the past two months. Where Unicode community is working with QBray upstream, that contributing the.

[13:20 - 13:30] Unicorn integration to the AppStream, it will be soon available in the next Kubernetes, and with this integration, it's very simple to enable Unicorn.

[13:30 - 13:42] For foray, you just need to set a flag, batch scheduler, set a name as unicorn, you have unicorn installed, then you can easily use all these unicorn features.

[13:42 - 13:52] And the way to use it is basically you can set it labels, very simple labels, maybe one is the app ID and the other is the Q name to basically tell Unicorn,

[13:52 - 13:58] Which queue you want to run your class or job on, then it will work out of the box.

[13:59 - 14:10] So just a quick example, you rather read jobs back, you give that label to define what is the app ID for this application, you define which queue you want to submit this job to,

[14:10 - 14:20] Then once you submit the spec to Kubernetes, the Kubernetes operator will basically create a Kubernetes job and also the recluster with the head and workers.

[14:20 - 14:29] And because of the integration we have done, then Unicron can basically see all these workers and had is coming from this application.

[14:29 - 14:40] And they will put a cluster into a queue where we manage the GPU resources, and it will apply all those policies, will call us.

[14:40 - 14:52] Uh, in place for this workload and when you run rejob or recluster in queues, it will be very different than running in native Kubernetes in namespaces.

[14:52 - 15:05] Because each of the queues are providing nice concepts about resource quotas, and it offers the concept about guaranteed and max quota in two dimensions.

[15:05 - 15:17] So really make these queues are elastic and when we have different reclassers running in the queue, it supports the priority, so it also supports FIFO ordering.

[15:17 - 15:26] And other policies in order to order the application inside of the queue to make sure the right application got a GPU first.

[15:26 - 15:35] And also between, of course, these queues, we're doing the resource fairness, that is extremely important because we have a lot of cases where people are competing for.

[15:35 - 15:46] GPUs, we don't want to make anyone unhappy, but we just want to maintain a fairness policy there to make sure each of the team can still get some GPU to use.

[15:46 - 15:56] Even in the peak hours of our system and underneath, it's a large shared GPU pool. The principle we're trying to get here is, basically.

[15:56 - 16:07] We want to make sure the GPU pool can be shared as much as possible for all these teams, in some cases we still do like isolations in some extreme cases.

[16:07 - 16:16] But in most of the cases, we want to use a large GPU pool to share to everybody and use Unicron to manage all those GPU quotas.

[16:16 - 16:26] That works very well for us, and here's a slide about talking about the features we're using in Ray from Unicorm.

[16:26 - 16:34] So first one is the GPU quota management, and it can manage a lot of the different resource types, GPU is just one of it.

[16:34 - 16:43] Second one is the oversubscription, and I think this is the key that we are able to oversubscribe our queues to utilize more idle GPUs.

[16:43 - 16:52] So essentially, we can put a lot of the queues sheer underneath GPU cluster to drive the cluster utilization to really high.

[16:52 - 17:02] And Q hierarchy is something that we, I think it makes a lot of sense for if you have a pretty complex organization structure.

[17:02 - 17:13] So we can use that to map to the organization structure to make sure that we have a proper management on different layers of organization from a large business.

[17:13 - 17:23] Line of business to small team or individuals. And resource fairness, something that we, we use a lot. But B, actually, it's coming by default.

[17:23 - 17:32] For all the GPUs and the guaranteed max capacity is the key that we can offer different tiers of GPU for our customers.

[17:32 - 17:43] guaranteed is some GPUs that you can always available, the max is kind of a max effort, beam packing is the mechanism that we really make sure our nodes are fully utilized,

[17:43 - 17:51] There are two parts of bin packing I'll talk about later, but that is the key how we can really make good use of no resources.

[17:51 - 18:03] And the queuing is something fundamentally provided by the queue, when you are running out of capacity, we are not going to reject your applications, just wait in the queue.

[18:03 - 18:16] until there's someone or some workloads release GPUs, and also priority is supported, so we make sure that we do consider the priority both in scheduling and also the printing.

[18:16 - 18:27] And the last is the primation, which we use a lot to ensure we oversell the GPUs, but at the same time, when we need them back, we have a proper way to reclaim the GPUs.

[18:29 - 18:40] Here's a very simple example, on the right hand side is the example configuration you can config, very easy, you can set up a different several queues with guaranteed max,

[18:40 - 18:51] GPU quota, and there are some extra features provided by these cues, such as you can configure dynamic cues or static cues based on your needs.

[18:51 - 18:56] And also the Q hierarchy is supported, there's ACLs as well.

[18:57 - 19:08] And interesting part is that we are kind of going to the direction of managed multi-type GPUs in the past is very hard for us because even we have a mixed.

[19:08 - 19:16] Diversify the GPU instance types, the resource using the GPU is still the single type.

[19:16 - 19:25] That for us is not very convenient because in some cases, some high-end GPUs, we want to limit the usage for teams.

[19:25 - 19:34] And we want them to use more cheaper instances if possible, so we don't have a really good story to manage different type of GPUs.

[19:34 - 19:46] We are exploring a way to use a modified GPU driver to expose different GPU types as resources, then you can really manage by unicorn, then we have a less charge.

[19:46 - 19:55] This is from the metrics, let's chart about what is the guaranteed GPU per queue, what is the max GPU queue, and what's the current utilization.

[19:55 - 20:04] This way, we can easily track different type of GPUs distribution. Do you want to reshuffle them? Do you want to change the layout.

[20:04 - 20:09] So it's totally on us. So this is very convenient. This is something we're exploring.

[20:10 - 20:21] So bin packing, as mentioned, this is one of the key feature we're using to solve the GPU fragmentation issue, which is really a serious problem.

[20:21 - 20:32] A lot of times we see that cluster utilization is not that high, but the coming GPU workloads cannot get a GPU because there's just not enough space on each of the node.

[20:32 - 20:40] It's just because there are fragmentations on here and there wasting our GPU hours.

[20:40 - 20:48] So the beam packing, we have two things. One is like using the scheduling phase. beam packing provided by Unicorn.

[20:48 - 20:59] This is a policy you can config, and it will basically, during the scheduling for each of the pots allocation, it'll try to find out, try to pack the pots more, increase the density.

[20:59 - 21:09] on the nodes, make sure the nodes are fully utilized before moving to the next one, so this is a scheduling phase, but this is not going to solve all the problems because after some time,

[21:09 - 21:19] You will see the fragmentation issue come pop up again, and then we will need to some post scheduling beam packing mechanism, currently we are using Carpenter to do that.

[21:19 - 21:30] And that basically scan the pods distributions on your cluster and trying to move the pods around, make it more compact.

[21:30 - 21:38] So we can free some of the nodes, either to scale down or leave for larger GPU requests.

[21:38 - 21:43] With this tool, we are able to reduce the fragmentation a lot.

[21:44 - 21:53] And GAN scheduling is a very important feature, and also this will be coming as the upstream QPray offering with the unicorn integration.

[21:53 - 22:08] Very simple, you just need a private label on your CR, telling with the RedoIO GAN schedule enabled with true, then it will give the Unicode schedule a heads up, so I want to enable GAN scheduling for this application.

[22:08 - 22:19] This is a per application configuration you can apply, and once you have that enabled, what Unicorn does will basically reserve all the resource.

[22:19 - 22:30] ahead of time, before actually schedule it, so this way we can really avoid the situation while some of the recluster only gets the partial resources and the,

[22:30 - 22:35] Now the workers are making progress and this is very helpful.

[22:36 - 22:47] Then I will spend some time to talk about the GPU priming, and this is a quite new feature we are using lately to improve the utilization.

[22:47 - 22:57] So because we're supporting so many different use cases, there are latency sensitive or non sensitive workloads, there are interactive sessions, real time sessions.

[22:57 - 23:09] and there are also some fast iteration experiments, the user just want to get the results back really quick, so among all these different use cases, users just want, very simple, just want to,

[23:09 - 23:23] have their job done in X, Y, Z hours, makes sense, but on the other hand, administrator want to really make the cluster utilization high, GPU is so expensive, we don't want to,

[23:23 - 23:32] With a lot of money on there. So there's a conflict. How do you solve this is we leverage unicorn queues, guaranteed Mx capacity.

[23:32 - 23:42] What it means is basically we can define the guaranteed capacity for each of the queue, that is the capacity the scheduler will always satisfy.

[23:42 - 23:50] In any situation, even every, every queue is competing for G. P us. Those guaranteed capacity will still be available.

[23:50 - 24:03] And the max is the way you can scale your queue, if other teams are not using GPUs, some GPUs are available on the cluster, those GPU will be available up to your max.

[24:03 - 24:11] This way we put a lot of queues in the same cluster, we set the guarantee max capacity based on the customer needs.

[24:11 - 24:20] Then we are able to make them really elastic. And in the idle time that we make sure we drive the utilization, because certain cues still have.

[24:20 - 24:27] Outstanding requests. But in the busy hours, we do the permission to make sure the guarantee can still, still satisfy.

[24:28 - 24:38] I will just give a quick demonstration about how this works, imagine we have two queues, very simple, two queues, right now cluster is empty, queues are empty.

[24:38 - 24:46] The utilization are both zero percent, so now let's see, we have some workloads, the read clusters running in the first queue.

[24:46 - 24:58] It uses 30%, so both queues are, we set a max up to the cluster max, but this first queue we gave 60% of the guaranteed GPUs to.

[24:58 - 25:09] And the second queue only gets 40%, then once we submitted rate clusters to the first queue, it started to consume resources.

[25:09 - 25:17] And now, because there's no workloads in the second queue, it consumes 50% of GPUs, that's fine.

[25:17 - 25:27] We can go even higher that because this queue is really busy, we let it scale to one hundred percent. That's, that's fine. And we are happy because now that all the GPS are utilized.

[25:27 - 25:38] But what if there's another recluster submitted to the second queue, and now there's no available GPUs in the cluster, the pods will be pending there.

[25:38 - 25:47] And at this time, Unicorn will basically start to trigger the priming process because right now, what happens is that.

[25:47 - 25:55] The first queue uses more than guaranteed capacity, but the second queue needs some more resource to reach its guaranteed capacity.

[25:55 - 26:04] So Unicron will basically say, oh, I need to move some of the GPU from overutilized queues to underutilized queues.

[26:04 - 26:18] It will basically honor the guaranteed capacity and also when we do the preemption, you will consider the application priority and also task priority and also how long your tasks are running, imagine if the task priority is the same.

[26:18 - 26:28] Then you basically select two parts to print, the very simple example, then you will reclaim the GPUs and reallocate the GPUs to the second queue.

[26:28 - 26:39] then the second queue will get a resource to run, but imagine if you, at this time, if you submit more workloads to the second queue, because we are still under one hundred percent utilization,

[26:39 - 26:49] So the second you will not be able to get a GPUs, this is a contract we gave to our users and what I found is it's pretty straightforward for user to understand.

[26:49 - 27:00] How this works and they are able to come up with some design on their, how they want to operate on their guaranteed or max capacity works pretty well for us.

[27:01 - 27:13] And here's the simulation just to mimic how it works, because we have these less metrics about tracking the utilizations on different queues.

[27:13 - 27:21] We were able to virtualize, like, basically say how this works. This is a very common production use case.

[27:21 - 27:30] For example, when we start a cluster, we start five queues, one of the queues have a lot of more workload than others, this is very common.

[27:30 - 27:40] And we let it use more resources. As you can see, most of the GPS are being utilized by the first queue. and it is good, so.

[27:40 - 27:49] But what if other queues are start to requesting for GPUs, this time because GPUs are all used.

[27:49 - 27:57] Then we will consider to make sure that each of the Q can still get the guaranteed capacity. So if you look at the.

[27:57 - 28:06] That moment, the prim machine kicks in, will start to reallocate GPU from the first queue to other queues.

[28:06 - 28:19] If you compare the two charts, the first queue uses four hundred plus GPUs, but after permission over time, all the queues were exactly got a guaranteed capacity as a previous defined.

[28:19 - 28:29] So this is how we make it work on production just to give the guaranteed capacity, max capacity for each of the.

[28:29 - 28:37] Team, we managed to use something like this for production clusters and works very well.

[28:39 - 28:49] So quick summary about the session, we were running into a lot of issues in order to scale Ray in Apple.

[28:49 - 28:57] And I think what we want you to take away from this session is that, first, informally clusters.

[28:57 - 29:07] Is is is needed for multi tenancy environment and also to make reliable auto skinning is the key to for efficiency. There are a lot of different.

[29:07 - 29:17] Are challenges that are being like are being mentioned to make auto skinning really reliable and also try to use diversified loop pools and.

[29:17 - 29:30] We're trying to use as diversified notebooks as much as possible, just want to make sure all our queues can access the different type of GPUs.

[29:30 - 29:39] Very easily and also use beam packing to reduce the fragmentation both in the scheduling phase and the post scheduling phase.

[29:39 - 29:47] And also leverage, so in our case, we leverage Unicorn cues from market tendency, how to plan the resources for each of the teams.

[29:47 - 29:58] And how to make sure they can share limited GPU resources and also balance the GPU utilization improvement and the good user experience.

[29:58 - 30:08] Actually it's very hard, sometimes there's a trade off, so it really depends on how you define your system SRA and how much you care about the GPU utilization.

[30:08 - 30:17] So you need to find the right balance there, then design the infrastructure to make sure that can happen.

[30:18 - 30:33] Yeah thanks and that's it from our session we can take some questions Unfortunately I think we're out of time but thank you Weiwei and Aben I think you'll hang out around the back so if you have questions feel free to find them there.

[30:33 - 30:37] But thank you for coming.


