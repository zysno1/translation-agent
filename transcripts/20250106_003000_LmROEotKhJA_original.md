---
title: Ray: A Framework for Scaling and Distributing Python & ML Applications
video_id: LmROEotKhJA
url: https://youtube.com/watch?v=LmROEotKhJA
created_at: 2025-01-06 00:30:04
type: original
---

# 视频信息

- **标题**：Ray: A Framework for Scaling and Distributing Python & ML Applications
- **时长**：01:10:42
- **来源**：YouTube
- **链接**：https://youtube.com/watch?v=LmROEotKhJA
- **转写时间**：2025-01-06 00:30:04
- **语言**：英文
- **对应译文**：20250106_003000_LmROEotKhJA_translated.md

# 内容概览

Recording of a live meetup on Feb 16, 2022 from our friends at Data + AI Denver/Boulder meetup group. 

Meetup details:

Our first talk of the year features Jules Damji, Lead Developer Advocate at Anyscale as he discusses Ray: A Framework for Scaling and Distributing Python & ML Applications.

ABOUT THE TALK:

Modern machine learning (ML) workloads, such as deep learning and large-scale model training, are compute-intensive and require distributed execution. Ray is an open-source, distributed framework from U.C. Berkeley’s RISELab that easily scales Python applications and ML workloads from a laptop to a cluster, with an emphasis on the unique performance challenges of ML/AI systems. It is now used in many production deployments.

This talk will cover Ray’s overview, architecture, core concepts, and primitives, such as remote Tasks and Actors; briefly discuss Ray native libraries (Ray Tune, Ray Train, Ray Serve, Ray Datasets, RLlib); and Ray’s growing ecosystem.

Through a demo using XGBoost for classification, we will demonstrate how you can scale training, hyperparameter tuning, and inference—from a single node to a cluster, with tangible performance difference when using Ray.

The takeaways from this talk are:

Learn Ray architecture, core concepts, and Ray primitives and patterns
Why Distributed computing will be the norm not an exception
How to scale your ML workloads with Ray libraries:
Training on a single node vs. Ray cluster, using XGBoost with/without Ray
Hyperparameter search and tuning, using XGBoost with Ray and Ray Tune
Inferencing at scale, using XGBoost with/without Ray

Link to presentation deck: https://drive.google.com/file/d/1hZrfsz8MRVMMAFAzwyNI4tDpm5_clS8g/view?usp=sharing

ABOUT OUR SPEAKER:

Our Speaker, Jules Damji is the Lead Developer Advocate at Anyscale Inc.

He is an MLflow contributor, and co-author of Learning Spark, 2nd Edition. He is a hands-on developer with over 25 years of experience and has worked at leading companies, such as Sun Microsystems, Netscape, @Home, Opsware/LoudCloud, VeriSign, ProQuest, Hortonworks, and Databricks, building large-scale distributed systems. He holds a B.Sc and M.Sc in computer science (from Oregon State University and Cal State, Chico respectively), and an MA in political advocacy and communication (from Johns Hopkins University).

Link to check out the Boulder/Denver Data + AI Meetup group: https://www.meetup.com/Boulder-Denver-Data-AI-Meetup/

# 转写文本


## [00:00 - 00:08]

Thank you for that kind introduction and kind invitation to be the first speaker for your first meetup for the new year.

My name is Jules Damji, I'm a lead developer advocate in Enniscale, before I was Enniscale I was working very closely both with Karen and Dorothy at Databricks for about six years.

So this is like coming home to me and i'm very delighted and pleased and honored to be coming back to the data plus AI community and sharing some aspects of some of the things which actually happening in the.

In in the industry so today's talk is going to be array of framework for scaling and distributed Python and machine learning.

What we're going to do is sort of start with sort of overview at a very high level, because this is the first talk on Ray, and some of you might have heard about Ray or probably haven't heard about Ray.

So what I want to talk about is really starting the twenty thousand level feet, what's the motivation behind Ray, what is Ray all about, why Ray and what's the ecosystem that allows people to write distributed application at massive scale,

## [01:03 - 01:15]

And then we'll drop down to about ten thousand feet below sea level to above sea level to the ray architecture and components, you know, when you, when you peel the curtain out, what are the internals and what the guts of Ray, what, how did?

What does it look like, how things work behind the scenes, and then we'll go down all the way to the C level where we talk about the record libraries, the native libraries, the APIs, the design patterns that allow.

People to write and scale these applications and then we'll look at the related libraries which are built on top of Ray.

And particularly, I'll give you a quick overview of RayTune, which is a very common library used by data scientists and ML engineers to tune.

Hyperparameter computing, which is a very common workload that people actually do, and also if you get time we'll try to talk about exiboot ray, but I'll do a demo that talks about exiboot ray.

So that way we don't have to get into slides and then we'll the demo is going to talk about what are the common workloads that you actually scale you do training you do inferencing and you do hyperparameter training those are the way development cycle of that and then I'll try to answer some questions that you have.

## [02:10 - 02:19]

So, so why Ray, you know, but before we talk about why Ray I think I think it's it's fitting to.

To talk about some of the industry trends which actually happening so when the original creators of Ray who were at rice lab, which is the same sort of crucible of innovation where.

Spark was developed in the predecessor, Rice Lab, which is MLAB, Mesos were developed with MLAB, Titehorn was one of the distributed systems developed.

When the new rice lab actually came into being, the researchers and Ph.D. students over there, along with Jan Stoiker, who was a former geriatric executive and the founder there.

Talk about what are the things are actually happening in the industry today, and I think there were three fundamental factors that actually looked at one was that machine learning is very pervasive in almost every domain today.

## [03:01 - 03:08]

And I think it's fitting to say, and I would contend that we have sort of entered what I would call the zeisgeist of ml right, we are in a place where.

We have more applications being affected and written and deployed in all areas of the vertical domain, you go from health.

to financial industry, to automotive, to scar industry, to health, ML is all of the place.

And so it is very pervasive and because of these sophisticated applications which are deployed in these industries, they require a fair amount of compute, they require a fair amount of compute and the only way you can actually do that,

Is to distribute at scale and so now that was that's that was sort of fun the first bit of it.

The second bit is that because of this nature now distributed computing is going to be a necessity it's going to be a norm, it won't be an exception today people are going to be just doing writing distributed applications.

As if they're writing Python functions and Python classes on the laptop on the Jupiter notebook and all of a sudden it's now running seamlessly on the cluster, and this is going to be a norm and a necessity for.

## [04:07 - 04:16]

For us to meet this particular demands. And one of the things, just to give you an idea of why that's actually is important, because if you look at how.

The Ml applications and the deep learning images that have the trainings that has evolved over a period of ten years.

You see that the demand of the petal floats needed to actually do this compute is increasing every eighteen months and the CPU load.

At which we actually increase is just not catching up, so there is this enormous amount of gap between this between the demand and the supply.

And you might say, well, what about the accelerators like we have GPUs and TPUs and they do make a difference, there's an incremental difference, but still there is this enormous gap that actually exists between what the today's,

Very sophisticated, both deep learning and ML applications are being deployed that actually require that.

## [05:01 - 05:11]

And it's not only just the fangs of the world or the mangas of the world who are doing that, ordinary startup companies are actually using the sophisticated application, they need the compute power to do that.

And so we contend that the only way you can actually address this demand, the only way you can actually minimize the gap is to actually go out completely in a very distributed manner right and that's where.

The second demand is coming is that distributed computing is a necessity, it's going to be a norm and we better be ready for it and we better have frameworks, we better have programming languages, we better have...

Compute strata that easy it's very easy for data scientists and machine learning engineers to actually build that rather than rather than.

Having a very difficult time, and so the third the third problem that they were trying to look at the third trend was that.

Those of you who are on call or those of you who have written distributed applications, those of you who have worked with other distributed applications, it's not easy, right, the programming bit is a bit hard because you have to really understand,

## [06:02 - 06:14]

A lot of concepts, and it is notoriously hard, and if you look at the existing solutions that are out there, you can sort of put them into this to lens of the ease of development and the generality.

And if you look at the middle, the median between the two, these are the systems which are sort of stitched together by system experts.

By SREs, by people who actually really understand the nuances of distributed computing, you got in MPI, Kafka, Spark, Flink, Spring, Horvod, TensorFlow, Cloudflare, they sort of stitch things together.

And they work, you know, it doesn't, the existing solution work, but they're trade offs, right, and trade offs are sometimes they're hard to develop, sometimes they're hard to deploy and manage.

The reason being is that these are bespoke solutions, they have different language semantics, they have different communication protocols, so to make them work very harmoniously can be sometimes cumbersome.

But they do work and they exist, so that's sort of the medium ground that people are actually doing today, we all use these systems today, when they work they work effortlessly, when they break they do break notoriously.

## [07:04 - 07:15]

If you go to the far right, I think there is this notion about not invented here so we're going to start everything from clean slate, do it yourself right so you can actually have a dog or container you can just put it on Kubernetes,

You can have all your application docker nice and you run your communication using either the latest grpc and you do it.

Nothing wrong with that, it's very general, it scales enormously, but it's expensive to develop because you need really system experts who really understand and who can actually glue things together.

And then if you go to the far left, which is the most easiest part, people like you and me and other people who are writing sort of serverless applications, just like Lambda functions or they just execute.

a big query or they just use Databricks SQL to just send out a query and let Delta Lake House take care of it and it scales automatically and it handles how much compute I actually need.

The problem there is a very cloud specific so if there are certain things that doesn't exist on the cloud, you are kind of beholden to that limitations.

## [08:04 - 08:15]

They're stateless only, so if you actually have a Lambda function or if you have a BigQuery, if it's not maintaining a particular state, the server is going to go away unless you have a third party rest service to which you actually persist.

Then you have to sort of write more code to it and there might be, you might not have all the GPUs and TPUs and hardware and accelerators you actually need, so there are some limitations of it, so you can actually think of the existing solutions are between this particular trade off.

So how does Ray actually fit in to address these particular demands, and I think I think the ethos and the principle behind.

Behind Ray's vision was that we want to make distributed computing simple, we want to actually make it accessible to every developer, in other words, they really don't have to be a system experts.

They can actually just write Python functions and Python classes as if they were writing that, writing Python code and by using some of the design patterns that I'm going to talk about momentarily,

## [09:03 - 09:10]

Change their code into an existing or distributed system that's sort of the key is that let's actually take that and make things easier.

So how does Ray do that right so as I said I'm going to start very high at the very high level if you look at Ray you can think of it as a layered cake right is a layered cake of functionality and capabilities.

Right at the bottom, you've got all the cloud on which you reckon run, right, you can actually run it on AWS, any of the cloud providers, including your laptop, which is actually brilliant because now you can actually just develop things on your laptop.

Or we can run on prems or on any hardware if you go up on the stack you have.

The essential universal framework, which is the core of what we call the general purpose distributed computing.

And the philosophical tenet behind that, the premise, the axiom behind this that, RAI is general purpose computing, it doesn't deal with any specific workflow, it doesn't have a certain abstraction on which you actually build the APIs.

## [10:03 - 10:14]

Instead, it gives you this low level primitives such as tasks, actors, which I talk about, which you can actually write to build any specific purpose workload that you actually want to deal with.

And that's the essence of the ray, which is that we're going to take care of all the elasticity, all the fault tolerance, all the compute substrata, and you can build things on top of that.

And we'll give you the primitives to do that, think of it as like Unix operating system where the guys at Bell Labs, you know, twenty, thirty, forty years ago actually just gave you the basic APIs to build things on top of that.

You build an API to write a device drive, you build an API to do window manager, you write APIs to do distributed computing, you fork and exit all that, and then you build things on top of that, very similar notion where you actually are given certain APIs and you build things on top of that.

And then when you go a layer up is where the native libraries campaign and the native libraries are using these Apis.

To actually handle specific workloads. So if you actually wanted to do distributed training, you use ray train. If you actually wanted to do reinforcement learning.

## [11:07 - 11:18]

If you actually want to scale models using RACE, so if you want to tune your parameters, you can actually use hyperparameter tuning.

So those are the native libraries which are very well built on top of that along the along the right hand side in the middle you hear all this third party integrations who actually have different levels of,

Of integration with play, there's level one, two, and three. And each of these have various ways integrated with Ray. And all of them are actually using these primitives.

plug into Ray in order to scale those things, and then finally if you are a distributed computer programmer who actually wants to build your own distributed framework that actually has nothing to do with machine learning has got nothing to do with any of the stuff,

You just want to write your Python application in distributed manner, you can actually use this API and run that so that's sort of sort of a layer of what.

Wood ray is actually at that at from from twenty thousand feet and the and the ecosystem is where the power of ray actually lies, where it actually now handles.

## [12:09 - 12:18]

The specific deep learning the ml workloads that you actually need to do these machine learning models at massive scale right, so the batteries are sort of included.

If you're actually doing data processing, you can actually use data core and data sets, you can use modern if you actually want to do pandas on a distributed fashion.

You can use Dask on Ray, a lot of people actually do that, if you are using SPACI, if you're using Tensor Library to do massive calculation, you can use Mars on Ray.

That allows you to do those things in a disciplined manner if you're training, right, deep learning training, you can use PyTorch, TensorFlow or Herobot as a plugin.

Along with this particular library do that serving is another one that you can actually use once your models are trained and deployed you can actually use Ray serve.

To deploy those models and RASO allows you to build these pipelines, allows you to have all these different patterns that you actually see how ML models are deployed in production.

## [13:05 - 13:17]

And finally, a very common workload is hyperparameter tuning, right, it integrates away with hyper opt or optuna, whatever search algorithm you want to use, whatever schedules you want to use,

You can use hyperparameter tuning to distribute your trials and then finally if you are a gamer or if you are doing simulations, if you're using RecSystem you can actually use RLLib to build simulation models.

To do your that particular workload so that's fairly a rich ecosystem and then more and more people actually sort of building things on top of these primitives to actually have their own integration with Ray.

So that's at a very high level and who's using where I mean I have to have this.

In parallel to this slide, we actually have some notable companies who are using RAI at a massive scale, Amazon is actually using Dask on RAI to do massive parallel processing to ingest data in their models.

Dendrite is using that hyperparameter, Judy McKinsey, Alibaba, all these people actually using Alibaba actually, and has got over 200,000 cores on which actually they run rare at a massive scale.

## [14:08 - 14:14]

So these are the companies who are actually using all this different ways of doing things.

So just now I'm going to switch the gears and I'm going to sort of raise the curtain a little bit.

You look behind the scenes, you know what what what Ray looks like right, what are the internal you open the hood you pop up the hood and then you'll see something.

Now, this is a common architecture if you come from CS Spark, if you come from DOSC, or if you come from Hadoop many years ago, or HPC.

The idea is not very dissimilar, you know, you have a worker nodes that actually have some processes which are actually running.

The only difference between the head node and the worker node is that you have an additional worker process called driver, which can run anywhere, it just happens to be running on this one.

And then you actually have what we call the global control store, which is like a global meta directory that keeps track of all the resources available, who is doing what, so that's like the brain of it.

## [15:10 - 15:20]

And then what you actually have is is these railets which are your distributed scheduling right so railets are like peer to peer communication that actually tells you.

What am I doing what my resources are and they're responsible to create your worker processes so every worker has has one process that actually running which is tied to a core.

And then you have a distributed object store which runs on shared memory and objects are sort of shared across the global customer.

The past over when when when the task needs that, so this is something quite unique to Ray nobody actually uses this and because of the distributed scheduling and because of the objects tour.

We can actually scale that very easily, we can say hundreds and thousands of tasks running asynchronously and using these tools, so if you actually have worker processes that need something,

On a particular node, and there are other processes we have created data on that you can actually use shared memory to do zero copy that's quite actually unique.

## [16:08 - 16:21]

So let me just go one level below and sort of share with you what's happening at each and every node so as I say each and every node has this worker processes and the worker processes are,

Attached to a course if you have twelve cores you'll have to have worker processes and the relay is the one that actually communicates so whenever you actually want to schedule a particular job the relay is the one who say.

Or do I have the resources to have four GPUs that I need and this much memory I need, so yes, I'm going to take that and I'm going to run the particular task.

And it communicates all the resources that you have to the global store and the global metastore then broadcast the picture, the mental picture every ten milliseconds.

what the cluster actually looks like, so there's one relay per node and it actually is responsible for sort of coordinating all that and that's sort of the distributed nature of it.

## [17:02 - 17:12]

And Global Store is the key value store where currently we use Redis, but you can actually use any pluggable that you want, and there's a process that runs on top of that that manages and communicates with that.

So that's sort of behind the scenes, virtually what happens.

So let me go now all the way down to sort of a little bit low level, the distributed design patterns that actually exist.

Now, design patterns are not something new in our consciousness, you know, most of the software developers probably have read that or heard that.

Book or they swear by that particular book from the gango for and those are the design patterns that were sort of introduced when object oriented programming actually came into being.

And allowed us to reuse objects and introduce concepts like signal turns and design patterns like decorators.

and iterators, and core routines, and so on and so forth, and so this is not something new, and so what RAID does, it builds on this particular design patterns to introduce its own design pattern,

## [18:03 - 18:11]

And there are sort of three design patterns associated with Ray one is, and there are many design patterns, obviously, but these are the three ones that sort of.

Introduces the concept of rate one is that all your functions can be converted into what we call parallel rate tasks that actually run as units of execution on on Ray.

And these can be distributed anywhere in the cluster in any worker or any driver any worker can be a driver that actually executes that so there's no central place where the driver dictates everything right.

Any worker can can submit task, the second is that object stores or Ray objects are futures right there object references.

To something that that will return to you when the particular task is finished, so if the Python creates an object or Python returns the object you won't get that object right away, what you get is a handle.

As a future, so those of you who deal with Scala futures or Python futures, it's a reference you can actually ask in the future.

## [19:01 - 19:05]

And these are immutable stored in the object store, right, the shared memory.

And the third one are actors and if you are not familiar with actors, these are actors that you might have heard in Arkao Airline.

But the difference between them is that these actors are very stateful and they use the object store to maintain a particular state and this is the reactors are the fundamental design pattern that you actually see being used in all the native libraries and we'll see in a bit what I mean by that.

So these are stateful services that actually allow you to maintain a particular state of a particular machine learning algorithm that you're actually running, so especially when you're doing rate tuning or when you're training parameters, you're running trials, the actors are running the trial.

Keeping state of that so if something goes wrong, they can actually begin from where they left off now there are links over here about you know patterns of parallel programming.

Raised design patterns, these are just three, but there are about six or seven of them, which are more advanced for people who actually want to write distributed applications in massive scale.

## [20:00 - 20:11]

And there is the design pattern for how libraries are integrated I mentioned about the third part libraries and they have different levels of integration as a little more level one, two and three so if you're interested to integrate your library into Ray.

You follow those design pattern and you can seamlessly integrate with Ray at these three different levels and each of them are, there's a degree of difficulty or degree of ease.

So let's look at the design pattern function, as I say, can be converted into tasks, they can run anywhere on the node, a class can be converted into a stateful actor and actor can have design and methods can actually run on a node.

And then you have the distributed object straw where your object can be now become a reference, which can recite anyway in the node, and there is this notion of primary ownership of a node.

So any function that's being scheduled on a node a, if it creates a particular value and returns a value, that particular node will own the metadata for that, but that's actually a primary copy, so that node will own that particular data.

## [21:01 - 21:10]

And if another task is scheduled somewhere else, and if that task needs it, then that will be sort of copied over using GsvRPC.

So that sort of is the three design patterns, so let's look at some code, right?

So I have a function that I want to convert into a task, all you do is just annotate that particular function with with radar remote.

And now, this is going to be converted into distributed task, I have the two functions one reads to numpy arrays and then just adds them together and then, when you want to invoke those things, what you do is.

Use the name of the function and then just annotate with the dot remote and then pass the argument and what happens at this point is that it's going to be scheduled somewhere on the note.

And it returns right away asynchronously, which is the power of that right, because that way you can actually scale a lot of tasks returns you an idea reference.

And then you can actually use the second function to call the second file, and then you can just use those references to send it out to the third function called remote.

## [22:01 - 22:10]

And then you can just do a get right so all these unknown blocking calls the only the only code that's going to block is is is the last one.

Over here, node array one will have file one that's actually sent or a path and it's going to read that either from the GC store or from AWS or if it's,

If it's on a local file system where you have already populated that, then it's going to read that and remember it's going to create graph dynamically, the second will be scheduled on node two, it's going to read that particular file.

Now you're going to send it to add remote is going to create create a graph and then return you the task right away, and then, when you actually do a get.

Those are running in the background, if they're finished, this won't block very easily, but if they're long running task, they'll wait till it gets finished.

And it will return back, so that's essentially what sort of happens behind the scenes with the task API.

And the notion of this is that we want to run things dynamically and asynchronously because we don't want to wait.

## [23:04 - 23:17]

in the order synchronously and other distributed systems do, where we actually wait till an action is invoked or a sudden call is executed, then it sort of executes the particular over here things happen dynamically.

And the reason it's important dynamically, because in certain machine learning algorithms where you're deciding how you're going to dynamically create the next task, you have to know exactly what the result was from the previous task.

So that way it executes things eagerly rather than lazily The notion I want to talk about is distributed object storage, as I say, this is something quite unique to it, we have a shared memory that runs across the,

across the older workers, and you can think of a shared memory is an Apache plasma store, which is the Pi Arrow version of the plasma store.

And that actually is shared across all the nodes so now if you have worker processes running on the particular node and they need some data that other processes create you just do a zero copy like so if you have numpy array or if you have tensors which are which you have saved,

## [24:06 - 24:16]

Process, a can just read the pointer and that way they're not doing any IPC so the performance is very high if somehow your data doesn't fill up on the shared memory store.

It can always be spilled over to data and all the tracking is actually done by the metadata to say, okay, this store was over here, but it has been spilled over to the disk in this particular partition, this particular sector, so we need that particular data.

Loaded back in again, and if there's old memory sitting there with garbage collected, so this is all done behind the scenes you don't have to worry, but I thought I would share that with you as an important aspect of it.

And so here's an example of how the data locality work, I have a distributed immutable object, I have node one that actually is executing a task.

It returns a value X. I have another function called G, which actually gets a value. It's going to return Y when I do F dot remote.

It's going to be scheduled on node two, let's say, for argument, and then I'm sending g remote the object reference that will return to me right away.

## [25:06 - 25:17]

And what happens is now G is going to be scheduled because of the data locality on node two and it's going to just read the data from the shared memory and then return back the value of.

of G, and then I can just do the get on that, and now I actually have the value, so you can actually see how the object store comes into being and how asynchronicity,

The task being executed in parallel allows people to just run things at a massive scale.

So just to give you an idea how things work, for example, you know, I have a radar remote that is going to be scheduled somewhere the way it actually works now, again, over here, I'm showing a driver, but any worker can actually execute that just it just happens that my code is not running on driver.

So it's going to ask this local relay, hey, I need to schedule this task, this task needs five CPUs or one CPU, do you actually have resources for that?

It will give it a list to it and say, yeah, I have it and go ahead and execute it, and that particular driver will serialize the code, and now the worker is actually used.

## [26:11 - 26:23]

Executing if the worker actually has if the code within within double is calling another function driver is not involved in there now now the worker is the one who is going to not submit the task of another node right.

It would say, oh, I need a GPU, but I don't have that. I'm going to ask the reler. Do you actually have the resource to do that, I don't have. But node number three has it.

It gets the least for it and holds on the least to execute very similar tasks so that's how we actually sort of scale this is sort of just an algorithm the way it actually goes through.

Getting a lease and so on and so forth, so I'm not going to belabor you guys with how the leases are sort of scheduled so that we don't do this constant GRPC.

So then once I have the list, I can have thousands of tasks which are of similar type, need similar resources, can be scheduled on that particular machine, and if they have sixteen cores they'll run on that, if they have thirty two cores they'll run on that.

## [27:03 - 27:11]

If they run out of scope, they'll be scheduled on the second note, so all that actually happens dynamically, all these scheduling policies done dynamically.

And you wouldn't have to worry about that So I think this is this is sort of now now at the sea level what I want to talk about.

Before I actually, it's a good idea before I go into see if I, if there are any questions over here.

Okay, maybe we'll just hold on to the end brilliant Okay, so what I want to talk about now is the Ray ecosystem and and like I said I can't talk about all the libraries, given the time that we actually have.

So what we're going to do is I'm going to talk about two, I might skip over Xe boost Ray because when I do the demo, I'll talk about exactly what Xe boost day rose under the theme, but I want to talk about Raytune because if you're a data scientist and if you're ML.

Tuning is a very important aspect of machine learning workload, you normally do that, you know you're going to create your baseline and then after that you're going to use hyperparameter tuning to actually do that.

## [28:00 - 28:07]

And then Tune is a very flexible, powerful library in Ray that allows you to do that at a massive scale across the cluster.

So let's take a look at that so what is very tuned right very simple library supports.

State of the art algorithms from the most latest literature that allows you to run trials in parallel, because it runs on RAE, all the orchestration, all the distributed orchestration of your trials,

But the config space are done in parallel, so that sort of leaves you the burden of doing that in a sequential manner.

Each worker or each ray will get a slice of the config space and you will actually have your trial and it will go through the motor training to do hyperparameter tuning.

It's easy to use in APIs, the all important thing is that you just use tune, you have your training function and you just run train model.

And you can run these on a single process, right, that can use all the codes if you actually want, or you can actually use multiple GPUs on the same machine, or if you actually want to use multi-node.

## [29:07 - 29:21]

Multicluster you can actually use that as well, so it's very simple it integrates very easily with all the compatible machine learning libraries that you actually have which are very essential to do hyperparameter tuning so XC boost ray, scikit learn.

Tensorflow pie toward carousel you name it all those libraries are available for you to do that the good thing about about this is this notion in real libraries that.

You can have other libraries run as a subroutine, so my training model could be a PyTorch function, which is actually another library, right, but I'm running that within REC, and that's a powerful notion that you have to grasp that.

And then it's very interoperable with all the other ones, so if I'm using RAID two and I can use RAID train to convert my to do distributed training.

I can use ray data sets to have my sharded data across all the workers that my hyperparameter tuning will need to do things in parallel, so it's actually quite powerful.

## [30:04 - 30:12]

And just to give you a quick sort of rundown of all the state of the art search algorithms that today Ray.

You know, by default, you will do the random grid search, you got Bayesian banded optimization, so these are all very easy built in algorithms that we actually support.

And in order for you to use them when you actually, when you're creating a ray tune, the object, the library, you just just create an instance of a search algorithm you actually need and is going to use that search argument with this hyper opt.

Whether it's Optuna, we support that or it's integrated with Ray and then you will actually use that to search to your hyper space.

You can also use schedulers, right, so schedulers are the ones that schedule the trials based on certain policies that you might have.

You can use Asha for hyperparameter scheduling, halving algorithm that schedules only things that are doing well and other things are dropped.

## [31:00 - 31:08]

You can use hyperband, you can use all these population based training schedulers with RayTune to be able to tune things on massive scale.

And if you're new to hyperparameters, if you're new to HPO, what does it actually mean to hyperparameter, what does it actually mean to do tuning for those of you who are new?

I'm sure for those of you who are familiar with that, this is just a sort of easy thing, so you know there are two kinds of parameters right, there are the model parameters which you actually learn during the time when you're actually running trials,

And these are the weights, these are the biases, these are all the things in a linear regression model, that's what it would be in the network, this would be the parameters for your weights that are passed between each layers.

And hyper parameters are set before training and they're sort of determine how the learning parameter will actually fair and these could be you know learning rate could be related to your pipeline configurations.

How you actually want each and every learning rate across your, let's say, psychic learn the number of trees if you're using a tree based algorithm, the depth.

## [32:02 - 32:14]

How often you're going to do the random So these are the things that that sort of define your hyperparameter and here's here's another example of hyperparameter tuning where if you if you're tuning.

A particular network, you know what kinds of layer what kind of filters you use you know what going to be your max pulling how many dense layers, you can have these are the parameters, you can ask your your your training.

Algorithm to figure out, given the space that you actually have and it'll come up with the best optimum algorithm based on the maximum or minimum loss that you actually want.

So that's sort of the gist of what would parameter now there's some challenges, you know, when you're doing hyperparameter tuning on a massive scale, this can take, you know,

From from from minutes to hours to today, so you have to be cognizant of the fact that it is time consuming because you have a large hyperparameter space and you want to have the best model.

It can be actually costly too and some of the challenges are here to make sure that it's going to use the resources in the most optimal way and it has to be elastic, it has to be full tolerant.

## [33:04 - 33:16]

So you might be doing your HPO on about five hours and all of a sudden one of the servers goes down what happens then you have to start the job all over again, no you don't have to so I think these are the hypervalent the challenges that you have to deal with.

And sort of Ray tries to address those Ray tune in particular tries to address those in three ways right, you can actually use exhaustive search.

And keep on going till you find the best one, or you can use sort of more Bayesian optimization where you only.

Pick up the results from the previous one in a sequential manner. So now you can say, okay, I'm going to drop this one, but I'll use this one because the.

Previous trial was was a better result and i'll do that, or you can do advanced scheduling like ash does that or other more state of the art algorithms that.

Have certain policies that that do, for example, early stopping or halving algorithm that will will only go forward if.

There is a promising trial that actually runs so if we look at each of these you know.

## [34:04 - 34:12]

You can do exhaustive search is very easily paralyzing because it's easy to implement you just have a certain greed and you can paralyze that right you exhaustively go through that.

And random such as the same way you uniformly go across your parameter sweep and you do that, but it's very inefficient right because you don't know right we don't we don't keep track of.

What was the grid parameter from the previous one should actually now use that combination, so it's inefficient, but today the literature now is actually changing whereby they are using more efficient algorithms to actually paralyze that.

So you can use, for example, results from the previous one in order to decide what you're going to be doing next Bayesian optimization is another one if you look at this particular chart.

If you use Bayesian optimization very tuned, it will try to figure out what's the best minimum loss that I have, and I'll sort of create a particular space around which all the other configs, if they fall into that, then I'm going to go with that.

The rest of the configurations I'll toss it out, so that's sort of a good way to do that, it's inherently sequential because the Bayesian optimization depends on the previous trial results,

## [35:11 - 35:19]

To see whether I want to schedule similar config parameter for my next trial, or I just want to toss it out and put it on the red zone.

The ones in the blue zones are the ones who fall into that and do that these libraries RayTune is integrated with HyperOpt so if you're familiar with HyperOpt you want to use that.

Like I say, you just create hyperbaromy to search and you use that and boom, Ray will take care of that optoma Skype, Psyche optimizes the new one that has been.

Has been integrated and never grad is another one so that's sort of second way, how you can actually reduce the cost to do that the third one that the ratio and actually uses, which is early stop.

And so what it does, it will fan out all this initial exploration to your config space, and they will just use the intermediate.

Results of it is from the trees or from the samples and it will prune dynamically as it actually goes in so we'll start with massively and the one that the trials, which are not faring well they use the halbin algorithm to actually.

## [36:08 - 36:18]

Stop those early stopping so this sort of reduces the cost right it doesn't wait till exhaustively reaches that as soon as it sees after a few rungs that the loss is not changing and nothing is changing.

It's going to drop that and they will pick up the next one, as you can actually see as as a time progressive, the ones which are doing better, you will start continuing along with those.

So those are some of the strategies and the policies that Raytune actually uses, and just to give you a sample of the code, how easy it is for you to use Raytune.

Very simple step, this is like your pyTorch function that you actually create like a training function, you define that particular function, you create a particular model, you're going to have an epoch that you're going to go through,

That's your only function you define your training function you give it to tune right so tune that run is the one that's going to.

Check that particular function and now you're going to provide the uniform config space that you actually want.

## [37:04 - 37:18]

The number of samples you want, the number of trials you actually want, like number of epochs in this case, and then what schedule you want to use, right, you want to use ASHA to do early stopping so you can actually use how the algorithm to make better decisions for the next trial.

What search algorithm you want to use you want to use opt in and you just specify that and then when you when you say do run the tune what happens at this point is that now.

Your driver process where a driver is running is going to create this function called read, tune, dot, run, that's the main actor or main tracker.

It's going to launch these actors on what we call worker processes and each actor will have a copy of your centralized function.

It will have a slice of your configuration and it's going to run in parallel and what it will do is report metrics back after the trial is finished so then the tracker can say okay what is the next one that I want to orchestrate.

Or should I just drop that or is early stopping and I'm not going doing very well or should I just halve it and things of that sort so report metrics go back.

## [38:07 - 38:17]

If there's an early stop is going to stop that particular worker and then we'll launch a new trial with a new configuration this sort of goes on, if something goes wrong, you know we do checkpoint on periodically.

Trials checkpoints can be done on local directory or it can be done on the central place in the cloud, so if the worker goes down, we can actually just load the checkpoint and start.

Restoring from the last checkpoint and start training so you don't you know you don't train all the data you just train from the last checkpoint you go on.

So that sort of in essence is what ray train, what XGBoost actually does.

Let me pause here and see if there's any questions there.

Excellent okay what i'm going to do is i'm going to pose now here i'm going to i'm going to sketch i'm going to skip over the.

## [39:05 - 39:14]

The XU boost ray because I'll talk through that when I'm actually going to give a demo, the some of the design features but just at a very high level.

Um.

Just a very high level, you know the the exhibition really a distributed training right there is there is the exhibits which you can use.

Distributed on your single machine on a single course, but this is actually was Ray that actually allows you to take your training and do it across.

Across multiple cores, it's like a data parallel, actually, each worker will get a copy of the particular model, and you use that on a section of the data, it's very full tolerant.

Because it uses that so i've lived this links over here and i'll get that I really don't want to get into it because I want you know I want to sort of show you how.

You actually scale those things on a particular cluster, so let's do these and go to my demo.

## [40:05 - 40:14]

Can you guys can see is the looks good looks good Okay, so what i'm going to show you over here is that.

In your sort of journey every day, when you're building a particular model on your laptop, or eventually then you're going to use the cluster that you have.

You're going to be using three very common workloads that you're going to scale you want to train one is training, which you actually want to train in at scale with large amounts of data.

The second workload, which is very common in your daily iterative process about model building is hyperparameter tuning, which is, how do you actually get the best model, right?

Create a baseline, but then you have a config space or which you want to do hyperparameter tuning and then that's and the third one is inference you know once you actually have the model for which you have got the best model.

How do you actually do inference on that at a particular scale, and so the idea over here is that we'll try to do something on on on a local machine that has a limited capacity and has a limited number of cores.

## [41:06 - 41:16]

And we'll see that the amount of time it actually takes is enormous, and then we can scale it across a ray cluster and see how it actually fares time wise.

So those are sort of the three things I want to do so what I'm doing over here is I'm just a regular classification algorithm that I'm going to use.

Exhibits to train that classification algorithm and just regular imports no different, I have about a 10 million 10 million rows that i'm classifying across.

About forty different features and the two classes that I do want to do that and this code is just a code that actually reads the file and then shards it across using ray data set to have it across my cluster.

And I have three sets of files because I want to use three different ways that I can test that, three megabyte, three gigabyte, and eleven gigabyte files.

## [42:02 - 42:10]

So let's look at each of these so first what we're going to do is we're going to train using regular XG boost right, so when you use your regular XG boost.

This is your training function you would actually use using exiboot no different, right, what you're going to do use over here is you define the exiboot parameters.

That you are going to give it to your, your, your attribute trainer. My objective method is approximation. I'm using objective logistic.

Logistic classification evaluation makes sure you don't be lost and error.

I import my Xe boost and I'm going to import my dmetrics train and the function called train very, very generic Xe boost train function that you're actually going to use all this is all part of the Xe boost you're going to have your labels.

You're going to read load the parquet files, divide them into seventy five twenty five you're going to then convert them into the D matrix, which is the efficient version of how.

Xgboost array puts that in a data structure, you're going to create your training function, and why you set the parameters.

## [43:08 - 43:19]

You set the evaluations that you actually want, the results you actually want back, whether you want verbose or not, and then you want the ten rounds that you actually want to train over, and then these are just some callbacks you actually have.

Very standard stuff that you would actually normally use so let's see if this function actually works so what I'm going to do is I'm going to try and make sure the function works on on on a small data set which is about three and a megabyte right.

So I'll just go ahead and train my particular border, this is running on my on Jupiter on a local node that has about sixteen cores.

And you can see, okay, this actually works three megabyte, no problem that I'm going to do is see if I can actually try that on the largest data set, which is three, three gigabyte.

Now I'm not going to run it because you know this is going to take about four minutes so I'm just going to show I just ran this just before that you can see that when I ran XGBoost on a local machine with three gigabit only three gigabit file,

It took about three minutes or yeah, close to two and a half, right?

## [44:06 - 44:16]

Instead, what about if I use exhibition Ray and the way exhibition Ray works is that it has this notion where remember I told you that.

The way the actors work, you have a tracker which actually creates the number of actors you actually want, each worker will get an associate actor on which it will run, it will have the data for it to run on.

And all these actors communicate across each other using the tree based reduced algorithm called RABIT, that's how they synchronize the gradients.

Then they return back to the tracker, so this is how Exegggoost on Ray works, which is drop and replacement from using the normal ray, but now you're actually running.

in a distributed fashion across the cluster rather than on the same node, so everything is actually the same, exactly the same, I'm providing my xgversed parameters, same parameters,

## [45:03 - 45:13]

The only thing I'm changing over here is I'm importing Exibus ray from Exibus ray, the ray database, the ray d matrix version of the of the d matrix, which is the,

The way it actually efficiently stores the data, I'm going to import the train algorithm, the train function, and the ray parameters, which I'll show what it is.

And it's actually the same function, the only difference over here is I'm now using the same same code same same data, but I'm using rate the metric which will now distribute across my workers.

And then I'm providing the same argument, except the difference over here is that I'm having this additional parameter called reperums, and I'll talk about what these reperums are in a minute.

So we're going to do that and we're going to define the parallelism that I want so it's exactly the same code I executed above, except that now I have.

I'm using the Xd boot parameters, which I sent the data file is the same three gigabyte file, and now I'm telling array to to use.

## [46:07 - 46:15]

Eight actors, eight actors or eight workers on each machine and use sixteen CPUs on that, right, so I'm just going to go ahead and train that.

So let's see if this this works, so now, this is actually running on my rate cluster that I created on any scale, and you can actually see it uses the rings to do the.

Do the all map reduce to communicate with the gradients, and it's now actually running on this all eight different nodes using all the GPUs that are provided.

So this was actually done in about thirteen seconds, so this was about three times faster than running on my local host, on my local node.

So that's sort of the ray train, exhibition ray, you can run it on the node with a small data set to see if it works, and then you train it on a larger data set to do that.

## [47:00 - 47:10]

So that you can actually see the big difference between running it on a local node and running across the cluster in Ray when you actually paralyze those using using Ray and it took about thirteen seconds, which was.

You know, faster than the much faster than the one on the local note, the second workload that people normally.

Do a lot repeatedly when you're building model at scale is hyperparameter tuning and the hyperparameter tuning again is very much sort of built in where you can actually use XGboost.

Your training function in there to scale it out so here I have pretty much the same exhibit config i'm using binary loss then i'm providing my hyperparameter tuning using this is my.

ETA learning rate to be uniform from the parameters that I provide, the sample, the depth that one from one to nine.

And then I and then I suggest how I actually want to paralyze that so I want to have I don't have any gpus i'm just going to use new actors i'm going to use two gpus per actor.

## [48:04 - 48:14]

I'm going to have eight actors, which are going to run across my node, and then I'm just going to give it to tune tune dot run and and then provide my.

Xe boost function, the files that I want, which are three gigabyte, the rear parameters that I want, and the progress bar, and I start running this particular in parallel.

And this is what happens over here is now it's going to go out and create eight actors and start using so you can actually see it's actually using hundred and thirty six GPUs.

And and fourteen g of all the hundred hundred and forty four g Cpus that I have and it's now it's actually doing training across my hyper parameter states in parallel, so I have eight actors each get gets a copy of slice of the config parameter.

And it just keeps on going and training and at some point it's going to terminate right now I'm running eight.

Trials in parallel, this is my last trials best parameter and currently I should have about yeah one is terminated, I have seven running.

## [49:08 - 49:19]

You can see now it's actually using a hundred and nineteen CPUs, dropped out of eighty five because I have three ones which are terminated, terminated doesn't mean it's stopped terminating, it's finished a trial and it's got its results.

And this was done, I got five more running, so what's actually happening over here is, as I say.

This is exactly what's happening over here, so now you've got a trial which are running in parallel by the actors and they're reporting metrics back to see how each of these metrics are actually doing and based on that the second trial is actually launched.

So we have about five, seven terminated, one running, and you can see it's now it's actually just using Simt and CPUs to finish the last one.

And it's terminated in about eighty two seconds if I ran this on my on my laptop or my single node on the head node this would take you know considerably longer than that.

## [50:00 - 50:12]

So hyperparameter tuning is something that you use quite often, and to scale that you can actually use ray tune on a ray cluster to give you this best parameter, and this is my best approximation.

My parameter, my ETAs were zero point one phi, sub sample was phi, the next number of maximum that three was three.

So the third time here, okay, so the third and the final training that most people actually do workload is inference, right, you actually want to do inference at a massive scale.

So now you train the model, you got your best parameters optimization, you're going to train this particular model and now you want to do the inference to see how it actually fares.

Let's first try to do that on a single machine using pretty much the same model with the predict, but except over here, we actually are not sending.

We are not distributing images using the d matrix part of it, and let's run that.

So this is going to take about, you know, 90 seconds, I believe, to do that so what's happening what's happening over here is that it's actually getting is going through the three gigabytes of file and it's actually doing prediction on each of those.

## [51:12 - 51:19]

And it's doing it sort of in a sequential manner on a single node, and it's actually going through this particular data.

This is running, let me just check.

Okay, so we got about seven gigabytes, so we probably got another three more to go, so you can actually see this is sort of really churning really hard, it's not taking care, it's not really capitalizing on the fact that a high-weree cluster.

And I can do inference in parallel rather than doing in sequential so we almost there, and this is going to take about maybe.

Few more seconds, but we should be done with that.

## [52:11 - 52:19]

So we went through all of the eleven gigabytes and they should actually give us a timing how it actually took to.

To get the results, so he took about eighty one seconds, a little a minute and a half or so.

Let's look at the results of our inference and that's what our classification algorithm and return now we're going to do the same thing we're going to do the same thing on x equals Ray.

And you see the only difference over here is that now I'm using the RD matrix to get my inference data parameters and then the only thing I'm sending which is different from the previous one,

Is i'm saying using nine actors to do inference in parallel, so this is going to now run in parallel, where I have now created eight remote actors.

And I'm just doing inference in parallel, and that should just return almost immediately.

## [53:04 - 53:16]

And that took about nine seconds and about ten times faster, so you can actually see the difference how you can actually scale things locally and scale things remotely one of the great things about about about race that you really.

Can sort of use your laptop wave segmentation and then when you want to something when you want to want something running on the on the cluster you just connect to the cluster using using rate in it and.

And it connects it very well so those my results, you can see they're quite identical so I have some you know notebooks over here that that.

Go more deeper into this, but this is a very common workload that people actually do and Ray tune is one of the libraries that allows you to do that hyperparameter at scale.

It works very well with other libraries, I don't have to use XGVous if I wanted to use PyTorch, my training function over here now would be a PyTorch function and my model over here would be a convolution net that I actually have.

## [54:00 - 54:07]

And my training function then would be just given to the ray train to go ahead and do that, and if I have a hyperparameters space that I provided that I want.

my dense layer to be within that particular range, my filters to be that kind, my connected net to be this set, and it will just figure out what's the best parameter.

or the particular space, so it's quite powerful, it's enormous in terms of the benefits that you actually get, and the time it saves and the cost it saves.

So I think that's essentially what I had in terms of the demo, what I'm going to do, let me just go back to my slides over here.

Quickly before I end.

## [55:16 - 55:25]

Oh, so yeah, I mean, here's an example you actually saw where I'm using the simple API example to use my XGBoost array without the array.

And the only thing I changed over here, I did the import, imported radiometrics, Exhibition Ray, the parameters that I, the parallelism that I want.

And the training function from from Ray and I just change this particular mind let's say and I just use Ray train to send those parameters and.

Now I have my training function running in a distributed manner that's only three or four lines of code you have to change taking your existing actually boost way and then convert that into a parallel.

Parallel code so that was it takeaways are you know distributed computing is going to be a necessity, you know we have to accept it now today, almost everything is is a gnome now.

## [56:05 - 56:18]

And Ray's vision is to actually make things a lot simpler, make the APIs a lot simpler, that's sort of the ethos behind it, right, when I remember when I was early, when I joined Databricks six years ago.

Early, our motto was that make big data simple, over here, our motto is make distributed computing simple, where you can just use your Python functions as if you're writing them on a Python file.

And then use the remote decorators to do the distributor computing and that really take care of the hard work you don't have to be systems expert just use very remote to do all your stuff.

And scale your workload using the real libraries and along with the ecosystem that provides you to do purpose specific stuff.

We have those of you actually are interested in reinforcement learning, we actually have a conference coming up in about a month, it's free and virtual.

You can actually join here's the URL when I send the slides you will actually have the URL over here as well, and then, if you actually want to take this really interesting tutorial about contextual bandwidths, how to use offline.

## [57:10 - 57:21]

Learning using RealLib from the creator and the maintainer, lead maintainer of RLib, there's a discount there for you, just use their meetup code and you can actually get that.

This is really worthwhile because Aria Live now is a new thing that people are using quite a bit, and if you want to start running, learning about Ray, just install Ray on your local machine.

And start start using that we have copious amount of documentation i'm putting a lot of code examples I have tutorials on it as well, we have a meetup we have started revived after two years of.

We had our first meetup in January, we have another one coming up on March the second, which deals with RayTrain, which is the new library for deep learning, which was released.

Then on March thirtieth, I'm hosting the RACE serve meetups if you're interested in productionizing models using RACE serve, attend that meetup.

## [58:01 - 58:09]

We have a vibrant community that actually has a lot of discussions going on to join us and discuss that, Ray.

There's a Slack for the community as well, follow us on media and visit us on GitHub and give us a star if you like.

So I think thank you very much if you want to get in touch with me, Jules at endscale.com, follow me on Twitter, I'll follow you, I know.

Sounds dodgy, but I use that line all the time and then yeah connect me with LinkedIn tell me you attended my presentations, hopefully that way I know who you are.

So that in essence was a lot of stuff over here that I covered, let me see if there are any questions that.

And folks, if anyone has questions, Jill will answer your questions right now.

Yes, no, I think, yeah.

## [59:05 - 59:11]

Oh, there's one question.

If I heard you correctly, internal communication is every ten milliseconds if I want something within shorter, I think I could have miscalled it, I think it's a lot shorter than that, there is a configurable parameter.

But I'll check with you Tom, I think ten million seconds is, it might be a hundred million seconds but I'll check, right, I'll check that and I'll make sure that.

It is the right thing, I think ten milliseconds or something else where it actually checks the object store cash for eviction.

I think it's much smaller, the heart is much smaller than that.

But I'll verify that ten minutes seconds doesn't sound right, it is much smaller than that.

Okay, let's see if we actually have anything on chat, anyone else have a question for Jules?

## [00:08 - 00:13]

You're going to ask me why, okay, I heard you very well.

This is a former Spark VW probably going to ask me, well, why Spark, why you're here, what's the difference?

Well, okay, here I have a question for you, Jules, yes, can I integrate Ray with spark?

Good question that's that's a very good question, but before I should do that, let me just let me just share this slide with you, because I think I just like this slide just specially for you.

Dorothy, because when I was giving the talk you said well you know we want to find out what's the difference between the two, and I think I think they're very very complementary really spark and Ray are extremely complementary they they sort of,

You know, Ray Spark finishes a sudden point and Ray picks it up, but just to give you a very high level sort of differences between the two, they are very complementary and they work well together.

## [01:04 - 01:15]

You can actually run Ray on Spark if you actually want to do ETL data processing, but just at a general high level, I talked about that Ray is a very general distributed computing system.

It's not specific addressing a particular load, it gives you these lower level primitives, fine grained primitives to write any distributed application you want.

So think of it Ray is a framework to write other frameworks, right, think about that, where if you go on the on the right hand side, you know, Spark is very powerful, very performant.

For specific purpose distributed data loads, it is built on top of the data frame abstraction.

And because of that, you actually have sort of more close-going APIs like DSL, so with data frame extraction in the DSL, you actually tell Spark what to do, right?

In other words, in other words, it's very coarse grained The other difference is that Ray is very distributed scheduler, there is no single driver node that sort of.

## [02:03 - 02:13]

Controls everything right, whereas if you look in the graphs are computed dynamically and the reason you use a dynamic ego execution is because, especially when you're dealing with.

Sort of machine learning algorithms like training and tuning, you have to decide how you're actually going to schedule your next one and that's based on something you just computed so it's a very eager eager execution it just executes right.

Graphs are created dynamically, whereas spark has a static schedule right i'm going to create my data frame list of methods and then i'm going to invoke.

An action and when the action is done, the entire deck gets executed the deck goes through the these the logical abstract the logical optimization the physical optimization.

It creates a final RDD abstraction and then executes that right, whereas over here everything is actually happening, not that one is better than the other, it's just that that's the nature of how Sparco is built.

On top of a data frame abstraction, just like dask was built on the data frame extraction for dask and bags, ray doesn't have this notion of an abstraction right, it gives you the primitives to build.

## [03:07 - 03:18]

Other things we use distributed objects store, in other words, you know everything is actually shared across and it's very asynchronous so we don't wait for synchronously, whereas if you look at spark.

You know, when you actually create transformations, you're going to create a list of methods on your particular data frame, and those are going to be executed sequentially.

Whereas over here, you just execute something and then you're going to get a reference back and at some point later on, you can actually ask whether I'm done with that task.

Ray is not there to displace any libraries, we are really here to integrate and interpret very openly, so all the third parties libraries you see, it's not displacement, right?

So if you actually wanted to do, for example, data processing, which is not necessarily today RAISE strength, you know, the RAISE is not a data processing framework.

It is sort of main for you can you can write your own data process, you can use dash cam right, you can use spark and Ray as well, and so the native libraries are there to sort of.

## [04:07 - 04:19]

Address those workloads it's very pythonic in nature, in other words, if you look at the Ray code, the way how other libraries are integrated is very similar obviously we actually have a pi spark over here, which has.

Has few sort of Scala pullovers, yes Spark supports deep learning integration through Horowood and PyTorch Intensive Flow.

Whereas over here, you can actually use use this different levels of that and another question was that well, how do you, how do you use spark with Ray it's very simple there's a project called spark on Ray.

And and here's a very simple code of spark running on red right, and so all you do is you actually wrap your driver around this class called spark and that's going to be removed.

And then when you do a ray.init, what you're actually creating is a Spark context and a Spark session, and then you're telling Ray Actuary to create two Java executors, right, so he's actually launching his executor, it's not.

## [05:04 - 05:15]

It's not doing all the communication, all the communication between MapReduce or between the executors is handled by by underlining JVM right so all Ray is actually doing is launching this.

This Java jvms on on the actors, the actors are just managing that and then and then now you just do a driver part remote and you can.

Execute a function called remote to do your partitioning to do any any transformation that you actually want, it is as is as simple as that you create a spark session.

You use Spark method to go ahead and do your transformation that you actually want, and then you just invoke the result by just using ray.get.

So that's your that's your answer to the question, Dorothy million million million dollar answer to your question yeah jules there's another question here about Ray data and sharding.

Let's see curious about Ray data and sharding, for example, currently shard using rank and how its size is introduced in horror word defined child, how would I do the same in Ray good question right.

## [06:08 - 06:19]

So the RAE data sets is the new library, which is in experimental that was released, we have had a couple of meetups and we actually have a webinar coming up on the 23rd.

But the whole idea behind Ray Ray data is to provide it's not a replacement for data from please don't get that wrong Ray data is there to provide last minute.

Transformation from your from your from your Parker files when you're injecting things into into your training function so when you actually want to charge your data across.

All the workers, what you do is you check your real data set that you actually read that say from the S three bucket and park your file and you repartition it based on the number of.

That you have a number of great actors that you're actually going to give that and that's how you actually sort of shard it across that that's what that's what Ray Databricks Ray D matrix did.

## [07:00 - 07:09]

In my demo, where, when I say read metrics, it read that particular parquet files, and then it uses the, it uses the, the, the shared memory to put.

The stuff in it and then now my Ray workers, we hear running training could actually access to that.

The Horwood aspect of that is the way Horwood and TensorFlow and PyTorch are integrated and retrained.

Is what we call level one integration, where the level one integration is that Ray does not handle the low level communication Ray only.

Handles the launching of the worker processes and the internal communication, whatever the internal communication, whether it's Horvath.

whether it's DDP that's using PyTorch or whether using TensorFlow is the one that actually does the communication, right, so we don't do that, we just use the backend to do that.

And then ray data integration is just a way to take your parquet file and convert that into, let's say, TF records or convert that into a DASC data frame or convert that into a Spark data frame.

## [08:07 - 08:19]

or convert that into a data into a pandas data frame if you actually wanted to use some sort of transformation, so the data data ray data set is the last glue I can think of it another way to put it I can think of it as that,

Where your ETL and SQL ends, the ray processing actually begins.

So think of it that they're using, you know, Delta Lake and Apache Spark to do all your ETL because if I was going to use Delta, if I was going to use ETL,

For Spark streaming and for SQL workloads, I wouldn't think about anything else but Spark on Databricks using Delta, right?

Once I built my lake house, I had all my data in there, and then if I just wanted to use, pick up all the Parker files from it and then ingest it into my deep learning.

## [09:00 - 09:05]

Distributed training, let's see, I think there's something else on the chat.

Very good answer to the question, hope so.

Does anyone else have questions for Joel?

Okay, if no one else has questions for Jules, then I think we're pretty much done here and thank you very much Jules for a wonderful talk.

This is a very, very slick tool that you're working on and you know stay in touch all right, thank you very much for the invite and if you have any questions you have my.

## [10:05 - 10:15]

You hear my contact information, feel free to drop in a line, I'm more than happy to do that or join our Slack channel, we'll definitely keep in touch, I'll try to answer that.

As well, but again Karen and Dorothy thanks a lot for the invite it's good to see both of you again I feel like i'm home again.

Stay healthy and hope to see you both sometime in the near future, maybe at Data Plus AI Summit in a few months.

Yep, yep, okay, yeah, all right, thanks, thanks everyone, bye, cheers.