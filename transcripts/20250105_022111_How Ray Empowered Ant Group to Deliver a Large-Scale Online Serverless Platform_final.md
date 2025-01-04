---
video_id: _yu0Rtuetuc
video_url: https://www.youtube.com/watch?v=_yu0Rtuetuc
video_title: How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform
created_at: 2025-01-05 02:22:10
---

# How Ray Empowered Ant Group to Deliver a Large-Scale Online Serverless Platform

【00：06-00：08】大家好。
【00：08-00：12】我们是艺术小组的杨松和李哲。
【00：12-00：17】今天的主题来自我们的伙伴团队，由韦才领导。
【00：17-00：21】但他今天不能来，所以我们将是演讲者。
【00：21-00：30】这是我们第一次来这里，我们很高兴分享我们在比赛中的工作。
【00：30-00：40】今天的主题是如何赋予艺术小组交付大规模在线服务平台的能力。
【00：40-00：40】让我们开始吧。
【00：41-00：46】首先，我想介绍一下我的公司和我的团队。
【00：46-01：00】总结一下集团，有五个方向：数字支付、数字连接、数字金融、数字技术和全球化。
【01：00-01：16】最流行的是蚂蚁集团的应用程序支付宝，它在中国的互联网支付和金融领域处于领先地位，我的团队是蚂蚁三队。
【01：16-01：23】在下一页中，我将向您展示我的团队的历史信息。
【01：23-01：29】但在这里，我想先分享一些高级别的信息。
【01：30-01：39】首先，我们是为雷开源软件做出第二大贡献的团队。
【01：39-01：56】我们与任何规模和雷斯拉布合作了几年，我们在开源中拥有超过26%的记录部分的贡献。
【01：56-02：13】其次，除了开发雷之外，我们还在生产中拥有大量雷的大规模应用，在我们的生产中，我们拥有超过一百万个CPU调用。
【02：14-02：25】然后在中国，我们也有一个丰富的中国社区，这个社区是由我的团队创建和运营的。
【02：25-02：32】在过去五年中，我们每年都会举办雷转发聚会。
【02：32-02：52】第五次雷转发已经在今年七月完成，在这次会议上，任何规模、跨AI、A't和坏舞都分享了他们的作品。
【02：52-03：01】所以，我们希望雷能像在美国一样在中国更受欢迎。
【03：02-03：07】让我们进入雷在艺术中的历史部分。
【03：07-03：16】我的团队成立于2017年，那一年的雷与今天大不相同。
【03：16-03：31】我们认为它是通用分布式系统，这意味着我们有很多非AI应用程序和框架。
【03：31-03：45】你知道，在雷开源中，雷开源专注于Python和AI，这意味着Python优先和AI优先，但我们不同。
【03：45-03：55】所以你可以知道，你可以在雷项目中看到我们已经贡献了Python、Java和C++API。
【03：55-04：05】2018年，我们的第一个用户层引擎在我们的生产中部署。
【04：05-04：11】该引擎名为G Flow，是一个流图引擎。
【04：11-04：17】它用于支付宝的支付风险控制。
【04：17-04：29】2019年，另一个融合引擎在我们的生产中部署。
【04：29-04：31】该引擎是在线学习。
【04：31-04：40】我们填补了三种计算类型，包括流式、机器学习和在线服务。
【04：40-04：51】所以你可以知道，这次在线服务也是在线服务首次在艺术中部署，这是主题。
【04：51-05：08】2020年，鉴于业务的多样性，我们构建了一个多架构的鲁，这意味着你可以在一个大的雷集群中运行很多雷作业。
【05：08-05：16】在这个作业中，你可以支持不同的计算范式。
【05：16-05：22】2021年，入口变得更加稳定。
【05：22-05：35】我们与我们的生态系统公司进行了更多的合作，例如阿里巴巴学院、中国网络和万世银行。
【05：36-05：45】2022年，我们探索了私人计算，这是一个新的场景。
【05：45-05：53】我们认为，对于私人计算来说，雷是一个很好的场景。
【05：53-06：07】因为私人计算需要一个灵活的框架来支持常见的功能、数据和AI，而雷在这方面有很多优势。
【06：08-06：28】好的，今年，2023年，我们的目标是构建一个通用的AI服务框架，在这个框架工作中，我们想要统一传统的AI大型语言模型和搜索引擎。
【06：28-06：32】这就是今天的主题。
【06：32-06：34】回到在线服务。
【06：34-06：48】从历史时间线中，你可以知道，在线服务是在2019年首次在蚂蚁部署的。
【06：48-06：54】它被集成到在线学习引擎中。
【06：54-06：56】基于此，
【06：56-07：05】我们构建了基本的保留能力，并将其集成到蚂蚁集团的基础设施中。
【07：05-07：13】你知道每个公司都有自己的客户基础设施，所以我们需要采用它。
【07：13-07：22】2021年，我们有了另一个场景，在线资源分配。
【07：22-07：34】你可以想象，如果资源是用于支付和金融，那么挑战是什么？
【07：34-07：44】我们认为挑战在于我们需要一个更灵活、高性能、可扩展、稳定的框架。
【07：44-07：59】幸运的是，我们基于雷实现了这一点，2020年，2022年，我们支持了大规模的在线服务平台。
【07：59-08：12】此时，我们提供了240000个调用的模型，并且我们的事件驱动服务平台达到了137万PC TPS。
【08：12-08：16】好的，这些是我们所有的私有工作。
【