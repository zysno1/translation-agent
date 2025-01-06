---
视频信息:
  标题: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
  ID: _yu0Rtuetuc
  时长: 26:54
  语言: English -> Chinese
  处理时间: 2025-01-06 13:26:07
---

## 内容时间轴

[00:06 - 00:16] 大家好，我们是蚂蚁集团的杨松和李冲，今天的主题来自我们的小伙伴团队，由滕伟才领导。

[00:16 - 00:25] 但他今天不能来。所以我们将是演讲者。这是我们第一次来这里。

[00:25 - 00:38] 我们很高兴能与阿米特分享我们的工作。今天的话题是如何赋能我们的集团交付一个大规模的在线服务平台。

[00:38 - 00:46] 让我们开始吧。首先，我想介绍一下我的公司和我的团队。

[00:46 - 00:56] 总结一下我们的集团，有五个方向，数字支付、数字连接、数字金融。

[00:56 - 01:07] 数字技术和全球化。我们集团最著名或最受欢迎的应用是支付宝。

[01:07 - 01:12] 它在中国的互联网支付和金融领域处于领先地位。

[01:12 - 01:20] 我的团队是动脉团队，在下一页我会展示很多。

[01:20 - 01:29] 我的团队的历史信息。但在这里，我想要先分享一些高层次的信息。

[01:30 - 01:38] 首先，我们是为Ray开源软件做出贡献的第二大团队。

[01:38 - 01:46] 我们已经与Uniscale和Reslab合作了几年。

[01:46 - 01:56] 在开源中，我们在召回部分的代码贡献超过了26%。

[01:56 - 02:05] 其次，除了开发Ray之外，我们还有许多Ray的大规模应用。

[02:05 - 02:13] 现在在我们的生产环境中，我们拥有超过一百万个CPU核心。

[02:15 - 02:23] 然后在中国，我们还有一个ReChina社区，它是由我的团队创建和运营的。

[02:23 - 02:31] 在过去的五年里，我们举办了Ray Forward聚会。

[02:31 - 02:41] 每年一次。第五次ReForward已经在过去的七月完成，并在这次会议上。

[02:41 - 02:52] 规模跨越AI、Ant和Baddance在本次会议上分享了他们的工作。

[02:52 - 03:01] 所以我们希望Rui能像在美国一样在中国更受欢迎。

[03:02 - 03:16] 让我们回顾一下Rui在艺术中的历史。我的团队是在2017年创建的，在这一年，Rui与今天的Rui有很大的不同。

[03:16 - 03:30] 我们认为它是一个通用的分布式系统，这意味着我们有许多非AI应用程序和框架。

[03:30 - 03:39] 你知道在开源中，开源专注于Python和AI。

[03:39 - 03:50] 这意味着Python优先和AI优先，但在Yant我们是不同的，所以你可以看到我们已经贡献了。

[03:50 - 03:55] Java和C加加API到项目中。

[03:55 - 04:03] 在我们的第一层，上层。

[04:03 - 04:13] 引擎被部署在我们的生产环境中。引擎的名字是G flow，它是一个流图引擎。它用于。

[04:13 - 04:24] 支付宝的风险控制。在二十，二十，二零九，在，二零一九年，另一个。

[04:24 - 04:32] 另一个融合引擎被部署在我们的生产环境中。这个引擎是仅学习的。我们融合了三种。

[04:32 - 04:45] 计算类型，包括流、ML和在线服务。因此，你可以知道这次在线服务也是在线服务全时间。

[04:45 - 04:52] 被部署在艺术中。这是今天的话题。在。

[04:52 - 05:00] 鉴于业务的多样性，我们构建了一个多租户架构的ray。

[05:00 - 05:11] 这意味着你可以在一个大集群中运行大量的红色作业。在这个作业中，你可以。

[05:11 - 05:16] 支持不同的计算范式。

[05:16 - 05:28] 在2021年，art变得更加稳定。我们与我们的生态系统进行了更多的合作。

[05:28 - 05:35] 公司如阿里巴巴、达摩院、中国网络和网商银行。

[05:36 - 05:43] 在我们探索隐私计算，这是一个新的场景。

[05:44 - 05:53] 我们认为这对Ray来说是一个很好的场景，因为在私人计算中。

[05:53 - 06:01] 我们需要一个灵活的框架来支持通用功能数据和AI。

[06:01 - 06:07] 这种方式有很多优势。

[06:08 - 06:17] 好的，在今年，我们的目标是构建一个通用的AI。

[06:17 - 06:27] 服务框架，在这个框架工作中，我们想要统一传统的AI、大型语言模型和搜索引擎。

[06:28 - 06:38] 所以这是今天的话题，回到在线调查从历史时间线，你可以知道。

[06:38 - 06:48] 在线服务首次在2019年部署在蚂蚁。

[06:48 - 06:54] 并且它被集成到在线学习引擎中。

[06:54 - 07:02] 依赖于此，我们构建了保留的基本能力并将其集成到基础设施中。

[07:02 - 07:12] 蚂蚁集团的基础架构，你知道每个公司都有自己的客户基础架构。所以我们需要采用它。

[07:13 - 07:19] 在2021年，我们有了另一个场景。

[07:19 - 07:30] 在线资源分配，你可以想象如果资源是，是为支付和金融。

[07:30 - 07:38] 有什么挑战。我们认为挑战是我们需要一个更灵活、高性能。

[07:38 - 07:49] 和可扩展的、稳定的框架。幸运的是，我们，我们，我们基于ray调查实现了它。

[07:49 - 07:57] 在2022年，我们支持大规模的在线无服务器平台。

[07:57 - 08:07] 在这个时候，我们用二十四万次调用服务模型，我们的事件驱动的无服务器平台。

[08:07 - 08:17] 达到了一百万的峰值Tps。好的，这就是我们所有的私有作品。

[08:17 - 08:24] 接下来，Chong将介绍我们今年最近的成就。

[08:25 - 08:31] 欢迎，好的，谢谢Guyan，大家好。

[08:31 - 08:40] 我叫李冲，我很高兴来到这里分享我们在2023年的最新成就。

[08:40 - 08:50] 在任何集团，我们已经建立了最大的推理平台，我们的推理集群有五十万个CPU核心和四千个。

[08:50 - 08:59] GPU卡总共，我相信你们昨天在Stoica博士的主题演讲中已经看到了这些数字。

[08:59 - 09:09] 为了交付这个硬件，我们总共使用了两万七千个工作节点，作为一个推理平台。

[09:09 - 09:18] 我们的平台上有非常活跃的模型部署，我们每周有超过三千个新的模型部署。

[09:18 - 09:28] 每周超过一个模型更新。我们的推理集群高度自动可扩展。

[09:28 - 09:40] 得