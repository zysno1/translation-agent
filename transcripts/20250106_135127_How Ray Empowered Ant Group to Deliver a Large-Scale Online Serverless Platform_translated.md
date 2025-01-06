---
视频信息:
  标题: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
  ID: _yu0Rtuetuc
  时长: 26:54
  语言: English -> Chinese
  处理时间: 2025-01-06 13:51:27
---

## 内容时间轴

[00:06 - 00:16] 大家好，我们是来自蚂蚁集团的顾杨松和李冲，今天的话题来自我们的小伙伴团队，由滕伟才带领。
[00:16 - 00:25] 但他今天不能来。所以我们将是演讲者。这是我们第一次来这里。
[00:25 - 00:38] 我们很高兴能与阿米特分享我们的工作。今天的话题是关于我们如何为我们的集团提供一个大规模的在线服务平台。
[00:38 - 00:46] 让我们开始吧。首先，我想介绍一下我的公司和我的团队。
[00:46 - 00:56] 总结一下我们的集团，有五个方向，数字支付、数字连接、数字金融。
[00:56 - 01:07] 数字技术和全球化。我们集团最著名或最受欢迎的应用程序是支付宝。
[01:07 - 01:12] 它在中国的互联网支付和金融领域处于领先地位。
[01:12 - 01:20] 我的团队是下一页的动脉团队。我会给你展示很多。
[01:20 - 01:29] 我团队的历史信息。但是，在那里，我想要先分享一些高级别的信息。
[01:30 - 01:38] 首先，我们是为Ray开源软件做出贡献的第二大团队。
[01:38 - 01:46] 我们已经与Uniscale和Reslab合作了几年。
[01:46 - 01:56] 在开源中，我们在召回部分的代码贡献超过26%。
[01:56 - 02:05] 其次，除了开发Ray之外，我们还有许多Ray的大规模应用。
[02:05 - 02:13] 现在，在我们的生产中，我们拥有超过一百万个CPU核心。
[02:15 - 02:23] 然后在中国，我们还有一个ReChina社区，这是由我的团队创建和运营的。
[02:23 - 02:31] 在过去的五年里，我们举办了Ray Forward聚会。
[02:31 - 02:41] 每年。第五个ReForward已经在过去的七月完成，并在这次会议上。
[02:41 - 02:52] 规模跨越AI、Ant和Baddance在本次会议上分享了他们的工作。
[02:52 - 03:01] 所以我们希望Rui在中国也能像在美国一样受欢迎。
[03:02 - 03:16] 让我们回顾一下Rui在艺术中的历史。我的团队是在2017年创建的，在这一年，Rui与今天的Rui有很大的不同。
[03:16 - 03:30] 我们认为它是一个通用的分布式系统，这意味着我们有许多非AI应用程序和框架。
[03:30 - 03:39] 你知道，在开源中，开源专注于Python和AI。
[03:39 - 03:50] 这意味着Python优先和AI优先，但在Yant我们是不同的，所以你可以看到我们已经贡献了。
[03:50 - 03:55] Java和C加加API到项目中。
[03:55 - 04:03] 并且在我们的第一层，上层。
[04:03 - 04:13] 引擎被部署在我们的生产中。引擎的名字是G flow，它是一个流图引擎。它用于。
[04:13 - 04:24] 支付宝的风险控制。在二十，二十，二十九，在，二零一九年，另一个。
[04:24 - 04:32] 另一个融合引擎被部署在我们的生产中。这个引擎是只学习的。我们融合了三种。
[04:32 - 04:45] 计算类型，包括流式、ML和在线服务，所以你可以知道在线服务，这次也是在线服务全时间。
[04:45 - 04:52] 被部署在艺术中。这就是今天的话题。在。
[04:52 - 05:00] 鉴于业务的多样性，我们为Ray制作了一个多租户架构。
[05:00 - 05:11] 这意味着你可以在一个大集群中运行大量的红色作业。在这个作业中，你可以。
[05:11 - 05:16] 支持不同的计算范式。
[05:16 - 05:28] 在2021年，艺术变得更加稳定。我们与我们的生态系统进行了一些更多的合作。
[05:28 - 05:35] 公司如阿里巴巴、达摩院、中国网络和网商银行。
[05:36 - 05:43] 我们在探索隐私计算，这是一个新的场景。
[05:44 - 05:53] 我们认为这是Ray的一个很好的场景，因为在隐私计算中，
[05:53 - 06:01] 我们需要一个灵活的框架来支持通用函数数据和AI。
[06:01 - 06:07] 这种方式有很多优点。
[06:08 - 06:17] 好了，在今年，我们旨在构建一个通用的AI。
[06:17 - 06:27] 服务框架，在这个框架中，我们想要统一传统的AI、大型语言模型和搜索引擎。
[06:28 - 06:38] 所以这是今天的主题，回到在线调查的历史时间线，你可以知道。
[06:38 - 06:48] 在线服务最早于2019年在蚂蚁部署。
[06:48 - 06:54] 并且它被集成到在线学习引擎中。
[06:54 - 07:02] 依赖于此，我们构建了保留的基本能力，并将其集成到基础设施中。
[07:02 - 07:12] 艺术集团的基础设施，你知道每个公司都有自己的客户基础设施。所以我们需要采用它。
[07:13 - 07:19] 在2021年，我们有另一个场景。
[07:19 - 07:30] 在线资源分配，你可以，你可以。你可以想象如果资源是，是为支付和金融。
[07:30 - 07:38] 那么挑战是什么。我们认为挑战是我们需要一个更灵活、高性能。
[07:38 - 07:49] 和可扩展、稳定的框架。幸运的是，我们在基于ray调查的基础上实现了它。
[07:49 - 07:57] 在2022年，我们支持大规模的在线无服务器平台。
[07:57 - 08:07] 在这个时候，我们用两十四万次调用服务模型，并且我们的事件驱动的无服务器平台。
[08:07 - 08:17] 达到了一百万峰值TPS。好了，这是我们所有的私人工作。
[08:17 - 08:24] 接下来，Chong将介绍我们今年最近的成就。
[08:25 - 08:31] 欢迎，好的，谢谢Guyan，大家好。
[08:31 - 08:40] 我叫李冲，我很高兴在这里分享我们在2023年的最新成就。
[08:40 - 08:50] 在任何集团，我们已经建立了最大的推理平台，我们的推理集群有五十万个CPU核心和四千个。
[08:50 - 08:59] GPU卡，我相信你们已经在昨天Stoica博士的主题演讲中看到了这些数字。
[08:59 - 09:09] 为了交付这些硬件，我们总共使用了超过二万七千个工作节点，作为一个推理平台。
[09:09 - 09:18] 我们的平台上有非常活跃的新模型部署，我们每周有超过三千个新模型部署。
[09:18 - 09:28] 和每周超过一个模型更新。我们的推理集群高度自动可扩展。
[09:28 - 09:40] 多亏了我们的产品化和独立的自动缩放器，我们的推理集群现在可以每周自动缩放超过三千次。
[09:40 - 09:49] 主动地，并通过这样做，我们将平均CPU利用率提高了超过20%。
[09:51 - 09:58] 所以下面，我将谈谈我们在生产中的新场景和一些新功能。
[09:59 - 10:11] 在深入细节之前，我想首先展示一下我们的RedSurfing架构概述，它与开源的RedSurf没有太大的不同。
[10:11 - 10:23] 在这个架构中，我们有一个服务守护进程，它接收来自用户客户端的所有服务推理作业提交。
[10:23 - 10:34] 它必须将这些服务作业分发到我们的服务集群中，但对于每一个，服务守护进程必须创建。
[10:34 - 10:44] 并在特定的服务集群中创建相应的应用程序主程序。这个应用程序主程序，将创建多个代理。
[10:44 - 10:54] 并且在集群内部署的actor。当代理准备就绪时，它们会注册自己。
[10:54 - 11:05] 独立的服务发现组件。通过订阅这个组件，我们的用户应用程序可以了解每个代理的位置。
[11:05 - 11:12] 仔细选择最合适的代理来发送他们的推理请求。
[11:13 - 11:26] 在每个代理中，您需要将传入的推理请求分配给本地部署的actor，这些actor负责模型服务工作。
[11:26 - 11:34] 这将在那里完成。好的，新的场景。第一个是。
[11:34 - 11:45] 在GPU上进行模型求解工作时，为了实现这一点，我们选择了使用NVIDIA Triton，对于那些不熟悉Triton的人，它是。
[11:45 - 11:53] Nvidia的单节点模型推理集合，它支持多个推理后端。
[11:53 - 12:05] 在我们的保留系统中，Triton服务器可以非常容易地分布，我们所需要做的就是运行，使我们的部署actor。
[12:05 - 12:14] 成为一个Triton启动器。所以每当我们的应用程序主创建一个新的部署actor。
[12:14 - 12:23] 它会立即在内部启动Triton服务器，并借助我们的actor长期环境。
[12:23 - 12:35] 这个运行时环境功能非常有用，它是由开源recall提供的，当我们处理数据依赖时，它帮助很大。
[12:35 - 12:45] 包或库依赖程序，我相信我们的recall团队贡献了他们近一半的实现到开源。
[12:46 - 12:57] 对，所以当这些Triton服务器准备好时，它们可以选择注册到这个发现，服务发现组件。
[12:57 - 13:06] 即将到来的推理请求可以直接连接到这些Triton服务器。
[13:06 - 13:18] 需要提到的一点是，因为我们的服务集群高度可自动扩展，所以在我们的平台上运行Triton服务器时。
[13:18 - 13:23] 它们也变得可自动扩展。
[13:23 - 13:31] 好的，下一个场景是服务LLM应用程序。
[13:31 - 13:48] 这件事的背景是在我们的端组中，我们有一个名为GPT缓存的系统，在这个系统中，我们将尝试在我们的向量或缓存存储中存储历史LLM响应。
[13:48 - 13:58] 所以每当有新的推理请求进来时，我们首先要做的是运行相似性比较。如果缓存命中，则我们只需。
[13:58 - 14:10] 将预启动响应返回给用户，如果缓存未命中，则推理请求仍然必须通过模型服务管道。
[14:12 - 14:24] 在我们的重新服务平台中，这个GBT缓存系统可以非常容易地集成，我们所需要做的只是运行这个。
[14:24 - 14:33] Gpt缓存系统在我们的部署actor内部。并且仍然，借助actor的运行时特性。
[14:33 - 14:43] 当然，我们需要在集群中有一个入口actor，它将帮助我们转发每一个传入的推理请求。
[14:43 - 14:53] 首先到GBT缓存actor，然后我们仍然做同样的事情，如果缓存命中，则我们快速响应。
[14:53 - 15:04] 如果缓存未命中，则我们将此请求转发到另一个Triton服务器，该服务器也在部署actor中运行。
[15:06 - 15:17] 所以你可以在这里看到的一个大问题是这张图片中的GPD缓存actor正在CPU节点上运行。
[15:17 - 15:27] 而Triton服务器正在GPU节点上运行。因此，感谢Raycord的异构结果调度。
[15:27 - 15:36] 我们现在可以更明智地分配这些不同类型的参与者，并优化整体资源利用率。
[15:39 - 15:49] 好的，接下来是一些新功能。第一个是内置异步代理。我们这样做是因为在。
[15:49 - 15:58] 大多数模型服务场景中，我们发现推理请求具有非常不同的执行时间。
[15:58 - 16:07] 对于这些长时间请求，人们总是要支付大量的集中等待开销。
[16:07 - 16:18] 我们在这里所做的就是在服务集群中部署一个异步代理，当然，这个异步代理是在部署参与者中运行的。
[16:18 - 16:26] 以及。这个异步代理可以接收和排队每个传入的推理请求。
[16:26 - 16:37] 对于这些长时间请求，当结果准备就绪时，异步代理可以帮助我们将这些结果异步地返回给用户。
[16:40 - 16:52] 这个异步代理的一个大好处是，有了这个集群内部的异步代理，其他部署参与者。
[16:52 - 17:04] 实际上可以根据自己的繁忙或空闲状态从这个代理中自适应地拉取推理请求。
[17:04 - 17:12] 因此，在每个部署参与者中，它正在使用Triton服务器运行模型服务。
[17:12 - 17:18] 在每个这样的部署参与者中，我们可以看到更少的队列延迟。
[17:19 - 17:29] 在我们的评估中，与基线相比，即基于轮询的推送请求分配。
[17:29 - 17:35] 我们的基于池的方法可以提供两倍更好的吞吐量。
[17:38 - 17:48] 下一个功能是C++部署，这个功能已经在我们的推荐和广告中广泛部署。
[17:48 - 17:58] 服务，这些服务对低延迟和高吞吐量敏感。因此，由于这种性能要求。
[17:58 - 18:09] 我们的部署参与者也必须是高性能的，所以我们所做的就是使用C++部署参与者。
[18:09 - 18:19] 基于开源的C++工作者。顺便说一下，这个C++工作者也是。
[18:19 - 18:31] 主要由我们的Ray团队贡献的，所以感谢Guyan在这个方面的努力，好的，有了这个C++部署参与者。
[18:31 - 18:40] 我们做的一件大事是实现了一个C++直接入口，这是一个高性能的RPC服务。
[18:40 - 18:49] 有了这个功能，我们的推理请求可以直接连接到我们的C++部署参与者。
[18:49 - 18:54] 绕过我上面提到的所有代理。
[18:56 - 19:05] 另一件大事是本地Triton推理调用，这可以做到因为我们现在有这些C++。
[19:05 - 19:15] 部署参与者和Triton服务器，它可以被视为一个C++库，可以更紧密地和。
[19:15 - 19:26] 高效地集成，没有任何跨语言开销。当我们制作C++部署参与者时。
[19:26 - 19:35] 与其他C++组件一起工作在我们的推荐和广告时间线上。
[19:35 - 19:40] 我们实际上正在构建一个更全面的分布式系统。
[19:43 - 19:54] 好的，接下来我会谈谈一些未来的计划，我们要做的第一件事是分片部署。
[19:54 - 20:03] 这样做的动机是在我们的推荐和搜索服务中，带有CVR或CTR模型。
[20:03 - 20:15] 我们总是可以看到大量具有大型特征尺寸、特征数据的项目，而这个特征数据尺寸太大，无法被。
[20:15 - 20:27] 放入任何单个工作节点，所以我们必须尝试将这个大型特征数据进行分片。
[20:27 - 20:35] 跨越多个工作节点。当然，我们将创建代理部署。
[20:35 - 20:46] 实际上，并使用这个代理来帮助我们执行一个关闭的路由策略，确保每个传入的。
[20:46 - 20:56] 推理请求可以被转发到具有本地可用数据依赖关系的特定节点。
[20:59 - 21:10] 好吧，最后一件事实际上是一个非常大的图景，我们希望交付一个高性能的通用AI框架。
[21:11 - 21:19] 为了实现这一目标，我们要做的第一件事是继续构建和。
[21:19 - 21:27] 完善我们的基于开源储备的推理服务平台，这已经被证明。
[21:27 - 21:37] 是高度分布式的、多语言支持的和可扩展的，我们相信这可以成为。
[21:37 - 21:41] 许多模型服务场景的良好基础。
[21:42 - 21:51] 我们肯定会使用我们的直接入口并用它来构建一个高性能的RPC服务。
[21:52 - 22:02] 我们将广泛使用C++部署演员，因为它可以给我们带来高性能。
[22:02 - 22:11] 计算能力。我们将开始研究这个分片部署，它给了我们。
[22:11 - 22:24] 高性能的本地数据访问和数据检索，我们认为这个功能在处理大规模模型服务时会非常重要。
[22:24 - 22:32] 在未来的问题。所以这就是我们今天基本上所有的内容，所以。
[22:32 - 22:44] 正如我在开头所说的，这项工作主要是由我们伙伴团队的王腾完成的，所以我们会尽力在这里回答问题，但如果不能，
[22:44 - 22:53] 我确实鼓励你们发送电子邮件到这个地址，我相信他能给出最详细的答案。
[22:53 - 22:58] 谢谢。
[23:02 - 23:10] 所以你为直接入口和C++所做的工作有多少已经集成到RakeCore中了？
[23:11 - 23:23] 它已经开源了，但在开源社区中并不非常流行，但我们经常在我们的生产中使用它。
[23:23 - 23:32] 因为在推荐和广告系统中，因为我们希望使我们管道中的所有组件。
[23:32 - 23:40] 推荐管道都是用C++实现的，使整个管道更加完整。
[23:42 - 23:50] 关于这一点的一个跟进问题是，在你刚才提到的那个空间，即推荐管道。
[23:50 - 24:00] 你是如何使用Ray的，因为使用Triton进行推理，对吧。而且你使用这个直接入口。但是Ray在那里扮演什么角色。
[24:00 - 24:08] Ray在那里是如何帮助你的？是的，我们肯定使用Ray的。
[24:08 - 24:20] 运行时环境来帮助我们在部署演员中集成这个Triton依赖。
[24:20 - 24:30] 我们使用Ray的异构调度来帮助我们调度这些演员。
[24:30 - 24:40] CPU依赖的演员或GPU依赖的演员，它们都可以被很好地调度，并帮助我们提高结果利用率。
[24:46 - 24:54] 谢谢你的演讲，我有一个快速的问题，你说每周大约有三千个以上的部署。
[24:54 - 25:02] 每周的部署。我的问题是，对于一种类型的模型，比如，它的。
[25:02 - 25:12] 平均或通常的部署频率是多少。比如说我们有一个大型语言模型。然后你多久。
[25:12 - 25:20] 更新和部署一次。我想这个范围，你可以。你把我难住了。
[25:20 - 25:28] 我真的不知道细节，所以那个问题，你应该给王腾发邮件。
[25:28 - 25:32] 因为这个是服务团队那边的一些细节。
[25:37 - 25:47] 这个是跟ray的选择有关的分片部署，分片部署什么，对，这个是跟ray的选择有关的分片部署。
[25:47 - 25:59] 对，还是在Ray上，我们只是需要把特征数据跨多个worker节点，但是worker节点还是基于Ray构建的。
[25:59 - 26:05] 所有的actor都是处理的，都是reactor。
[26:13 - 26:23] 所以所有这些都在VM上运行，对吧，不是Kubernetes或其他任何东西，只是裸机？
[26:23 - 26:33] VMs，或者它是在Kubernetes上运行，还是在，是的，是的，我们肯定是在云原生环境中运行我们的recluster reclusters。
[26:33 - 26:38] 在Kubernetes之上。
[26:43 - 26:50] 哦，好吧，如果没有更多的问题，那么非常感谢。