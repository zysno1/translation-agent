# Ray at Scale: Apple's Approach to Elastic GPU Management | Ray Summit 2024

## 视频信息
- 视频ID: ZCRZQVt-r3g
- 视频标题: Ray at Scale: Apple's Approach to Elastic GPU Management | Ray Summit 2024
- 视频URL: https://www.youtube.com/watch?v=ZCRZQVt-r3g

## 原文
[00:05 - 00:06] Hello everyone.

[00:06 - 00:08] Thank you and welcome to the talk.

[00:08 - 00:20] Second to last talk of the summit today, wewei and I are going to talk about elastic GPU management for ray, achieving scalability and efficiency for animal workloads.

[00:22 - 00:24] So first, the introduction slides.

[00:24 - 00:30] I have worked on or with the ray community at apple and before that at Linton.

[00:30 - 00:34] And then wado, you want to talk about yourself a little bit?

[00:34 - 00:34] Yeah.

[00:34 - 00:35] Hi everyone.

[00:35 - 00:49] My name is wewei I, and I'm working the data and ainfrastructure in apple and basically help the team to build infrastructure for running both data processing and machine learning workloads on multiple clouds.

[00:53 - 00:59] So today we will give you a little bit of an overview of ray.

[00:59 - 01:11] We'll discuss the scaling challenges with GPU workloads and some of the techniques that we've tried for optimizing GPU capacity management and utilization.

[01:12 - 01:14] So why why use ray?

[01:14 - 01:23] Ray provides a unified computing api for data processing, training, tuning, serving.

[01:23 - 01:35] And for us, one of its kind of positives is that it provides this kind of seamless api that works on users 's laptop all the way to the data center.

[01:35 - 01:44] Users can kind of try out small small experiments that they can then migrate to the clusters without many changes.

[01:45 - 01:50] It has great support for model serving, including vm.

[01:51 - 01:55] Users use our ray platform in three different ways.

[01:55 - 01:59] Notebooks are used for early iteration.

[01:59 - 02:03] This is where they can try out early experiments.

[02:03 - 02:06] They can try out as if they're on their laptop.

[02:06 - 02:15] It's an an interactive mode and then they can use the same apis for a full scale, large scale workload in the data center.

[02:15 - 02:24] And then in additional notebooks, users always demand like mature sdks for programmatic job submission and model deployment.

[02:24 - 02:36] And then there's portals to support ux based model deployment and also for observability, which is like a very important part in any productionized workloads.

[02:37 - 02:45] While ray has many features, there are also quite a few challenges using one is resourzing.

[02:45 - 02:51] So there's too many options when it comes to the kind of resource the users can request.

[02:51 - 03:02] And that is not at the top of the ml practitioner's mind when they're trying to execute a batch inference job or deploying a model auto scaling.

[03:02 - 03:09] Kind of attempts to help it, but then also kind of brings its own challenges that we have seen.

[03:09 - 03:25] And then lastly, GPU utilization is a problem that both the ml practitioner and the infra engineers try to solve because of the high demand for gpus and the cost involved.

[03:26 - 04:18] So going deeper into this with the with the different infraresource choices that users have, so they they have to choose the kind of the in nodes or machines based on the number of cards on the nodes, the GPU memory they have, the the s ram versus d ram, the intra GPU and ingpu connectivity, the network congestion in a particular geographic region, they're choosing the region's overall capacity and congestion, a lot of choices that are too hard to specify for a human being while they're launching fairly large workload or productionizing at model deployment.

[04:18 - 04:32] So our observation has there been there has been that kind of pairing down the choices and providing some kind of standard compute options are helpful.

[04:32 - 04:43] So think like small, medium, large and kind of provide abstractions that users can kind of talk to and then they can choose that.

[04:43 - 04:45] Okay, I need kind of this.

[04:45 - 04:55] And our platform then provides ray the the particular and a resource configuration based on the choices that the users make.

[04:55 - 05:01] While this doesn't optimize for every case, it sort of covers 80% of our cases.

[05:01 - 05:20] One intermediate step that we took on the way to kind of figuring out how to optimize gpuuse cases and how to allow users to kind of provide the correct kind of nodes or machines they need is to kind of come up with node specific cues and node specific clusters.

[05:20 - 05:22] And that didn't work out well.

[05:22 - 05:38] So it kind of resulted in while the users so we couldn't kind of give them these choices, and it ended up with kind of even more fragmentation and lower utilization that we had before that.

[05:38 - 05:45] So then we sort of backed out of that and then worked on multi level scheduling.

[05:45 - 06:02] So where the node level scheduling could handle multiple types of nodes and instances and kind of can fall back on different options when primary the user's primary asks are not available.

[06:05 - 06:20] Another important part of optimizing the gp utilization is to support out of scaling because the resource utilization of large workloads, both for batch and for real time doesn't stay static.

[06:20 - 06:25] It varies with the lifetime, with the of the workload.

[06:25 - 06:34] We heard in earlier in the summit, Serge from meta was talking about how llama needed to grow its bat size during the training.

[06:34 - 06:38] So we've observed similar things.

[06:38 - 06:47] And fortunately, ray has native support for order scaling both for batch and for real time workloads.

[06:47 - 06:54] Raise the way real raise auto scalar works is great.

[06:54 - 07:07] So the way race auto scalar works is like it kind of watches the metrics of the workers and and patches the the the crd is based on that.

[07:07 - 07:09] And then we have this.

[07:09 - 07:25] We use aache unicorn, which watches the the modifications that the raauto scallar makes and then cues up pods and workloads based on the additional needs of the of the auto scalar.

[07:25 - 07:35] And then it does the same on the downscaling side and tries to reconcile and impact pack the workloads together.

[07:37 - 07:47] And then but with successful order scaling, there are some challenges that come with it.

[07:47 - 08:02] So first is for very large workloads, we want na like we want na make a choice whether we want to get limited by geographical regions or do we want na go across geographical regions.

[08:02 - 08:09] But then if we want to go across regions, then there's data transfer cost to kind of consider.

[08:09 - 08:21] And then the next problem that occurs is like even with the single region, workloads can be okay with upscaling, scaling up, but many workloads are not okay with downscaling.

[08:21 - 08:31] So this is what we saw in a lot of our kind of stateful workloads where downscaling caused failures.

[08:31 - 08:40] So guaragainst, that was to kind of make sure that, okay, workloads, our ray workers cannot be evicted.

[08:40 - 08:45] So they can be upscale, aled, but they cannot be downscaled.

[08:45 - 08:55] Now that resulted in lower utilization because now we have kind of created this workload that cannot be shrunk.

[08:55 - 09:02] So then with that, to kind of try to resolve that was to kind of focus more on checkpointing.

[09:02 - 09:17] But there to support better checkpointing, we had to introduce better apis from a platform that users could easily use to kind of have standard checkpointing across all different use cases.

[09:17 - 09:25] And then when the check so when we resolve ved that problem, the next problem was like fast out of scaling.

[09:25 - 09:39] First, fast upscaling kind of creates its own problems where node initialization starts surfacing different issues such as like maybe the surface and the certificate management is not quite ready.

[09:39 - 09:45] The nodes are not quite the ip address availability is not quite there.

[09:45 - 09:55] So all of those problems kind of started showing up when auto scaling became like widely usable and the users could auto scale up fast.

[09:55 - 10:12] So to resolve that, we had to kind of work on keeping headroom in so to make sure that there's always additional nodes available which has trade offs with the kind of the utilization.

[10:12 - 10:20] None of these kind of steps would be possible without like our scheduler support.

[10:20 - 10:24] So now deep dive on the schedule will provided by weway.

[10:24 - 10:25] Thank you.

[10:25 - 10:25] Bin.

[10:25 - 10:33] So I will talk about the GPU management and GPU resource preemption, which we we use a lot.

[10:33 - 10:49] I think I think in the use case in apppoo is huge that we have so many organizations, teams want to use ray and how to really offer the limited GPU to all these teams, organizations.

[10:49 - 10:55] This is the key issue that we want to solve and why we're choosing approunicorn.

[10:55 - 10:59] So aparture unicorn is a cobernetes resource calcular.

[10:59 - 11:05] And because when we run reon cobernetes, we really see a lot of challenges.

[11:05 - 11:17] Like one of the most important things that resource fragmentation that we see, different GPU nodes are not fully utilized because such of fragmentation happens here and there.

[11:17 - 11:20] And also it's very hard to manage GPU quotas.

[11:20 - 11:30] Imagine that you have a lot of different type of instances and you want to share those instances with different teams is extremely hard to to manage.

[11:30 - 11:33] The quota for different type of gps 's.

[11:33 - 11:37] And also the GPU utilization being a problem is always being a problem.

[11:37 - 11:45] And and and we know that people are complaining about not getting enough gps s, but sometimes actually sometimes gps is idle.

[11:45 - 11:47] We don't want to see that happen.

[11:47 - 11:50] And also, it's lack of observability.

[11:50 - 11:55] I think that is 11 casing that are missing in a lot of places.

[11:55 - 11:57] We're trying to build this really well.

[11:57 - 12:01] So uunicorn actually help us to solve a lot of issues.

[12:01 - 12:06] It has the complexity of the infrastructure, the resources from the ray.

[12:06 - 12:14] So let read to focus on the application side of things and uniicorn handle the resource management scheduling underneath.

[12:14 - 12:24] It's really, really for us is really bring the multenancy rally platform to our end users and also pro provides the huge cost savings along the way.

[12:25 - 12:28] And just a quick recap about unicorn.

[12:28 - 12:40] It's a resource scheduler on Kubernetes and it offers a lot of scheduling capabilities and it provides a really high efficiency and improved sras.

[12:40 - 13:05] And there are some highlights about the features unicprovides, such as resource ques that is essential for for multenancy and also offers the resource fairness between different cues and offers the gun schedule, which is very, very important for for machine learning workloads and also the resource pretty sophisticated resource proption.

[13:05 - 13:08] I will explain more in this later session.

[13:08 - 13:12] And we use that a lot and cuate with unicorn integration.

[13:12 - 13:27] The good news is that in the past two months where unicorn communities working with curee upstream, that contributing the unicorn integration to upstream, it will be soon available in the next curelease.

[13:27 - 13:42] And with this integration, it's very simple to enable unicorn for Forray, you just need a set flag, batch scheduler, set a name as unicorn, you have unicorn installed, then then you can easily use this, all these unicorn.

[13:42 - 13:47] And the way to use it is basically you can set the labels, very simple labels.

[13:47 - 13:56] Maybe one is the app ID and the other is A Q name to basically tell unicorn which queue you want to run your recuster rejob on.

[13:56 - 13:58] Then it will work out of the out of the box.

[13:58 - 14:00] So just a quick example.

[14:00 - 14:07] You rather read jobs back, you give that label to define what is the app ID for this application.

[14:07 - 14:10] You define which Q You want to submit this job to.

[14:10 - 14:20] Then once you submit the spec to Q A, the q buoperator will basically create A Q bernejob and also the reccluster with the head end workers.

[14:20 - 14:38] And because the integration will have done, then unicorn can basically see how this workers and head head is coming from this application and they will put a cluster into a queue where we managed the gp resources and it will apply.

[14:38 - 14:43] All those policies were called us in place for this workload.

[14:44 - 15:06] And when you run rejob or recclustering cues, it will be very different than running in native cobernetes, in name spaces, because each of the cues are providing nice concepts about resource quotas and it offers the concept about the guaranteed and the max quota in two dimensions.

[15:06 - 15:09] So really make these cues are elastic.

[15:09 - 15:15] And when we have different recclusters running in the queue, it supports the priority.

[15:15 - 15:25] So it also supports five for ordering and other policies in order to order the application instead of the queuh to to make sure that right application get a GPU first.

[15:25 - 15:37] And also between across these qes, we're doing the resource fairness that is extremely important because we we we have a lot of cases where people are competing for for gps 's.

[15:37 - 15:49] We don't want to make anyone unhappy, but we just want to maintain a fairness policy there to make sure each of the team can still get some GPU to use even in the peak hours s of our system.

[15:49 - 15:52] And underneath it's a large shared GPU pool.

[15:52 - 16:03] The principle we're trying to get here is basically, we want to make sure the GPU pool can be shared as much as possible for for all these teams.

[16:03 - 16:18] We in some cases, we we still do like isolations in some extreme cases, but in most of the cases, we want to use a large gpto share to everybody and use unicorn to manage all those GPU quoters that worked very well fast.

[16:18 - 16:25] And here's a slide about talking about the features we are using in ray from unicorn.

[16:25 - 16:32] So first one is the GPU quota management and it it can manage a lot of different resource taps.

[16:32 - 16:33] GPU is one of it.

[16:33 - 16:37] And second one is the over subscription.

[16:37 - 16:52] And I think this is the key that we are able to oversubscribe our cues to utilize more idle gps so we can essentially, we can put a lot of the cues share underneath GPU cluster to drive the cluster utilization to really high.

[16:52 - 17:01] And quehierarchy is something that we, I think it makes a lot of sense for for if you have a pretty complex organization structure.

[17:01 - 17:31] So we can use that to map to the organization structure to make sure that we have a proper management on different layers of organization from the from from a large business line of a business to small team or individuals and resource fairis, something that we use on not actually is coming by default for all the gps s and the guaranteed that max capacity is the key that we can offer different tiers of GPU for our customers.

[17:31 - 17:35] Like guaranteed is some gps that you can always available.

[17:35 - 17:38] The max is kind of a max effort.

[17:38 - 17:43] Beapacking is the mechanism that we really make sure that our nodes are fully utilized.

[17:43 - 17:52] There are two parts of imppacking or talk about later, but that is the key how we can really make good use of no resources.

[17:52 - 18:00] And the queue is is something fundamentally provided by the queue when you are running out of capacity.

[18:00 - 18:10] We not going to reject your applications, just wait in the queue until there's someone where some workloads release gps and also priately supported.

[18:10 - 18:16] So we make sure that we we do consider the prpriority both in scheduling and also the pretion.

[18:16 - 18:18] And last is the perwhich.

[18:18 - 18:27] We use a lot to ensure we oversell the cps, but at the same time when we need them back, we have a proper way to reclaim the gpus.

[18:28 - 18:31] Here's is a very simple example.

[18:31 - 18:35] On the right hand side is the example configuration.

[18:35 - 18:36] You can Cong very easy.

[18:36 - 18:42] You can set up a different several cues with guaranteed the max GPU quota.

[18:42 - 18:54] And there are some extra features provided by by these cues, such as you can configure dynamic cues, were were static cues based on your needs and also the q hierarchies supported.

[18:54 - 18:55] There's acs as well.

[18:55 - 19:17] And interesting part is that we are kind of going to the direction of managed multi type gps in the past is very hard for us because even we have a mixed diversified GPU instance types, the resources using in the gps U still the the the the single type.

[19:17 - 19:30] That for us is not very convenient because in some cases, some high ngps, we want to limit the usage for for teams and we want them to to use more you know cheaper instances if possible.

[19:30 - 19:35] So we don't have a really good story to manage different type of gps.

[19:35 - 19:42] We exploring a way to use a modified GPU GPU driver to expose different GPU types of resources.

[19:42 - 19:45] Then you can really manage by unicorn.

[19:45 - 19:55] Then we have a less charthis is from the Metrix less chart about what is the guaranteed the GPU per q, what is the max gpq and what the current utilization.

[19:55 - 19:59] This way we can easily track different type of gps 's distribution.

[19:59 - 20:01] Do you want to reach out for them?

[20:01 - 20:03] Do you want to change the layout?

[20:03 - 20:05] So it's totally on us.

[20:05 - 20:06] So this is very convenient.

[20:06 - 20:09] This is something we're exploring.

[20:10 - 20:22] So pin packing, as mentioned, this is one of the key key features ure we're using to solve the GPU fragmentation issue, which is really a serious problem happening.

[20:22 - 20:33] A lot of times we see that cluster utilization is a lot that high, but coming GPU workers cannot get a GPU because there just not enough space on each of the node.

[20:33 - 20:37] It's just because there are fragmentations on here and there.

[20:37 - 20:40] No, we we wasting our GPU hours.

[20:40 - 20:42] So the ppacking we have two things.

[20:42 - 20:47] One is like, using the scheduling phase ppacking provided by unicorn.

[20:47 - 21:03] This is a policy you can Conte and it will basically, during the scheduling for each of the parts allocation, you'll try to find out, try to pack parts more, increase the density on the nodes, make sure the nodes are fully utized before moving to the next one.

[21:03 - 21:18] So this is a schedule phae, but this is not going to solve all the problem because after some some time you say the fragmentation issue come pop up again and then we'll will need to some post scheduling ppacking mechanism.

[21:18 - 21:38] Currently we're using carpenter to do that and that basically scan the pouh distributions on your cluster and trying to move the pads around and make it more impact so we can freeze some of the nodes either to scale down or leave for larger you know work larger GPU requests.

[21:38 - 21:43] With this tool, we are able to reduce the fragmentation a lot.

[21:44 - 21:47] And gun scheduling is a very important feature.

[21:47 - 22:05] And also these were becoming as the upstream q re offering with the unicorn integration and very simple, you just need a private label on your cr tauh with the radiio gun scheduling enabled with two, then it will give the unicorn schedule heads up.

[22:05 - 22:09] So I want to enable gun schedule for this application.

[22:09 - 22:13] This is per application configuration you can apply.

[22:13 - 22:22] And once you have that enable, what unicorn does will basically re reserve all the resourahead ight of a time before actually schedule it.

[22:22 - 22:33] So this way we can really avoid the situation while some of the cluster only gets the partial resources and the none of the workers are working, making progress.

[22:33 - 22:35] Yeah this is very helpful.

[22:36 - 22:41] Then I will spend some time to talk about the GPU permission.

[22:41 - 22:47] And this is a quite new feature we are using lately to improve the utilization.

[22:47 - 23:00] So because we're supporting so many different use cases there, latency sensitive or nonsensitive workloads there, interactive sessions, real time sessions, and there are also some fast decoration experiments.

[23:00 - 23:04] Users just want to get the results back really quick.

[23:04 - 23:13] So among all these different use cases, users just want very simple, just want to have their job done in x yz hours.

[23:13 - 23:14] Make sense.

[23:14 - 23:22] And but on the other hand, administrator want to really make the cluster utilization high GPU so expensive.

[23:22 - 23:25] We don't want to with Ste A lot of money on there.

[23:25 - 23:27] So there's a conflict.

[23:27 - 23:32] How do you solve this is we leverage uniques guaranteed a max capacity.

[23:32 - 23:40] What it what it means is basically we can define the guaranteed capacity for each of the q ue.

[23:40 - 23:45] That is the capacity the schedule will always satisfy in any situation.

[23:45 - 23:51] Even every every queue is competing for gps 's, those guaranteed capacity will still be available.

[23:51 - 23:54] And that max is the way you can scale your queue.

[23:54 - 23:59] If other teams are not using gps, some gps are available on the cluster.

[23:59 - 24:03] Those GPU will be available up to your your max.

[24:03 - 24:11] This way we put a lot of cueues in the same cluster we started, guaranteed a max capacity based on the customer needs.

[24:11 - 24:14] Then we are able to make them really elastic.

[24:14 - 24:21] And in the idle time that we make sure we drive the utilization because certain cues still have outstanding requests.

[24:21 - 24:27] But in the busy hours, we do the pretion to make sure the guarantee can still still satisfy.

[24:28 - 24:33] I will just give a quick demonstration about how this works.

[24:33 - 24:38] Imagine we have two cues, very simple, two cues right now, cluster is empty, qes are empty.

[24:38 - 24:41] The utilization are both zero percent.

[24:41 - 24:44] So now let's see, we have some workloads.

[24:44 - 24:49] The recclusters running in the first cube, it uses 30%.

[24:49 - 24:53] So both cues are, we set a max up to the cluster max.

[24:53 - 25:03] But as first q ue, we gave 60% of the guaranteed gpus to and the second queue only gets 40, 40%, 20%, 40%.

[25:03 - 25:16] Then once we submitted rclusters to the first q ue, it started consume resources and now we, is, because there's no workload in the second queue, it consumes 50% of G P's.

[25:16 - 25:17] That's fine.

[25:17 - 25:24] We can go even higher that because this q is really busy, we add it scale to 100%.

[25:24 - 25:25] That's that's fine.

[25:25 - 25:45] And we are happy because now that all the gps 's are utilized, but what if there's a another reccluster submitted to the second queue and now there's no available gps 's in the cluster, the parts ds were depending there, and this time unicorn were basically start to trigger the premition process.

[25:45 - 25:56] Because right now what happens is that the first queue uses more than guaranteed capacity, but the second queue needs some more resource to to reach the guaranteed capacity.

[25:56 - 26:07] So unicorn will basically say, Oh, I need to move some of the vgp from over utilized the cues to under utilized the cues and it will basically honor the guaranteed capacity.

[26:07 - 26:16] And also when when you do, the preempyou will consider the application priority and also task priority and also how long your task sks are running.

[26:16 - 26:23] Imagine if the task part is the same, then you this basically select two pales to print the very, very simple example.

[26:23 - 26:27] Then you will reclaim the gps and reallocate the gps to the second queue.

[26:27 - 26:31] Then the second queue will will get a resource to run.

[26:31 - 26:39] And but imagine if you at this time, if you submit more workclose to the second queue because we are still under 100% utilization.

[26:39 - 26:43] So the second you will not be able to get a gps use.

[26:43 - 26:46] This is the contract we give to our users.

[26:46 - 26:51] And what I found is is it's pretty straightfor usser to understand how this works.

[26:51 - 26:59] And they are able to come up with some some design on their how they want to operate on their guaranteed over MaaS capacity.

[26:59 - 27:01] Works pretty well for us.

[27:01 - 27:06] And here's is a simulation just to mimic how it works.

[27:06 - 27:18] And because we have these less metrics about track tracking the utilizations on different cues, we were are able to visualize like basically see how this works.

[27:18 - 27:22] This is a very common production use case.

[27:22 - 27:30] For example, when we start cluster, we start five cus one of the quehave, a lot of more workload than others.

[27:30 - 27:35] This is very common and we let it to use more resources.

[27:35 - 27:41] As you can say, most of the gps are being utilized by the first queue and it is good.

[27:41 - 27:56] So but what if other cues are start to requesting for gps s this time because where gps are all used, then we were consider to make sure that each of the q can still get at the guaranteed the capacity.

[27:56 - 28:06] So if you look at that that that moment the premition kicks in will start to reallocate GPU from the first q ue to other q's.

[28:06 - 28:11] If you compare the two charts, the first q ue uses the 400 plus gp's.

[28:11 - 28:20] But after perover time, all the qes will exactly get a guaranteed capacity as as a prprevious define.

[28:20 - 28:29] So this is how we make it work on production just to to give the guaranteed capacity, max capacity for each of the team.

[28:29 - 28:36] We we managed to acuse something like this for protection clusters and works very well.

[28:39 - 28:42] So quick summary about the session.

[28:42 - 29:05] We are we were running a lot of running into a lot of issues in order to scale ray in apple as I think I think what we want to you to take away from this session is that first informal recclusters is, is is needed for multi tendency environment and also to make reliable auto skaling is the key to for efficiency.

[29:05 - 29:24] There are a lot of different challenges that are being like being mentioned to make out skreally reliable and also try to use diversified loop pools and, we're trying to use as diversified loopuas much as possible.

[29:24 - 29:58] Just want to make sure all the our cues can access the different type of gps s very easily and also use beapacking to reduce the fragmentation both in the scheduling phase and the post scheduling phase and also leverage so in our case, we leverage unicorn cues for multenancy, how to plan the resources for each of the teams and how to make sure they can share limited GPU resources and also balance the gputilization improvement and the good user experience.

[29:58 - 29:59] Actually it's very hard.

[29:59 - 30:02] Sometimes there is a trade off.

[30:02 - 30:09] So it really depends on how you define your system as rand, how how you how much you care about the gp utilization.

[30:09 - 30:17] So you need to find the right balance there, then define the then design the infrastructure to to make sure that can happen.

[30:18 - 30:19] Yeah, thanks.

[30:19 - 30:23] Then that's that's it from our session we can take some questions.

[30:23 - 30:27] Unfortunately I think we're out of time but thank you wewei and auen.

[30:27 - 30:30] I think you you'll hanhang out around the back.

[30:30 - 30:33] So if you have questions, feel free to find them there.

[30:33 - 30:34] But thank you.

[30:34 - 30:35] Everyone coming.

[30:35 - 30:35] Thank you.

[30:35 - 30:36] Yeah.


