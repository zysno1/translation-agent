# 视频翻译处理报告

## 视频信息
- 视频标题：How do Graphics Cards Work?  Exploring GPU Architecture
- 频道/发布者：Branch Education
- 发布日期：2024-10-19
- 视频长度：00:28:30
- 视频分类：Education
- 视频ID：h9Z4oGN89MU
- 观看链接：[点击观看原视频](https://www.youtube.com/watch?v=h9Z4oGN89MU)
- 原始语言：en
- 目标语言：中文

![视频缩略图](https://i.ytimg.com/vi/h9Z4oGN89MU/maxresdefault.jpg)


## 处理统计
- 处理时间：2025-03-10 17:25:15 至 2025-03-10 17:25:15
- 音频提取耗时：13.84秒
- 转录耗时：1分14秒
- 翻译耗时：19.84秒
- 内容章节数：1
- 总字数（原文）：3932
- 总字数（译文）：304


## 内容概览

### 视频主题摘要
<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">
本文介绍了显卡在运行现代视频游戏时所需的计算能力及其内部结构和工作原理。1996年的《马里奥64》每秒需要一亿次计算，而2021年的《赛博朋克2077》则需要约36万亿次计算。显卡的核心是GPU，拥有成千上万个内核，相比之下，CPU核心数量较少但灵活性更高。以GA102芯片为例，它包含283亿个晶体管，分为多个图形处理簇和流式多处理器，每个处理器又包含CUDA、张量和光线追踪核心，分别用于基本运算、矩阵计算和光线追踪。

显卡的性能还依赖于高速的图形内存（如GDDR6X），这些内存芯片可以提供高达1.15 TB/s的带宽，远超普通DRAM。美光公司生产的高带宽内存（HBM）更是将内存带宽提升到新的高度，适用于AI等数据密集型应用。此外，GPU采用SIMD（单指令多数据）和SIMT（单指令多线程）架构，能够高效处理大量并行任务，如视频游戏渲染和比特币挖矿。尽管显卡在挖矿方面逐渐被ASIC取代，但在图形处理和AI领域仍占据重要地位。最后，文章简要介绍了张量核心和光线追踪核心的作用，并感谢了赞助商的支持。
</div>


## 关键观点

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">

**1.** 显卡从1996年《马里奥64》的每秒一亿次计算发展到2021年《赛博朋克2077》所需的36万亿次计算。

**2.** GPU拥有超过10,000个内核，适合处理大量简单并行任务，而CPU有较少的核心但更灵活。

**3.** GA102芯片包含283亿个晶体管，分为多个图形处理簇和流式多处理器，支持不同类型的计算核心。

**4.** 显存（如GDDR6X）使用多电压级别编码方案提高数据传输速率，未来将转向PAM3以优化性能和功耗。

**5.** SIMD架构使GPU能高效处理视频游戏中的顶点变换等易于并行化的任务，每个warp内的线程同步执行相同指令。

</div>



## 完整对照翻译

**00:00:00 - 00:00:10**  
原文：How many calculations do you think your graphics card performs every second while running video games with incredibly realistic graphics?  
译文：你认为你的显卡在运行具有极其逼真图形的视频游戏时，每秒进行多少次计算？  

**00:00:10 - 00:00:12**  
原文：Maybe 100 million.  
译文：也许是一亿。  

**00:00:12 - 00:00:20**  
原文：Well, 100 million calculations a second is what's required to run Mario 64 from 1996.  
译文：好吧，每秒一亿次计算是运行1996年的《马里奥64》所需的速度。  

**00:00:20 - 00:00:21**  
原文：We need more power.  
译文：我们需要更多的电力。  

**00:00:21 - 00:00:25**  
原文：Maybe 100 billion calculations a second.  
译文：可能每秒 1000 亿次计算。  

**00:00:25 - 00:00:44**  
原文：Well, then you would have a computer that could run Minecraft back in 2011 in order to run the most realistic video games, such as cyberpunk 2077, you need a graphics car that can perform around 36 trillion calculations a second.  
译文：好吧，那么你将拥有一台可以在2011年运行Minecraft的电脑，而要运行像《赛博朋克2077》这样最逼真的视频游戏，你需要一块每秒能够进行约36万亿次计算的显卡。  

**00:00:44 - 00:00:46**  
原文：This is an unimaginably large number.  
译文：这是一个难以想象的大数字。  

**00:00:46 - 00:00:50**  
原文：So let's take a second to try to conceptualize it.  
译文：所以让我们花一秒试着去理解它。  

**00:00:50 - 00:00:54**  
原文：Imagine doing a long multiplication problem once every second.  
译文：想象一下每秒做一次长乘法运算。  

**00:00:54 - 00:01:02**  
原文：Now, let's say everyone on the planet does a similar type of calculation, but with different numbers.  
译文：现在，假设地球上每个人都做类似的计算，但使用不同的数字。  

**00:01:02 - 00:01:19**  
原文：To reach the equivalent computational power of this graphics card and its 36 trillion calculations a second, we would need about 4400 earths filled with people all working together and completing one calculation each every second.  
译文：要达到这张显卡每秒36万亿次计算的等效计算能力， 我们需要大约4400个地球的人口全部共同努力， 每个人每一秒完成一次计算。  

**00:01:19 - 00:01:25**  
原文：It's rather mind boggling to think that a device can manage all these calculations.  
译文：想想一个设备能够处理所有这些计算，真是令人难以置信。  

**00:01:25 - 00:01:30**  
原文：So in this video, we'll see how graphics cards work in two parts.  
译文：所以在本视频中，我们将分两个部分来了解显卡的工作原理。  

**00:01:30 - 00:01:43**  
原文：First, we'll open up this graphics card and explore the different components inside, as well as the physical design and architecture of the GPU or graphics processing unit.  
译文：首先，我们将打开这张显卡，探索内部的不同组件，以及GPU（图形处理单元）的物理设计和架构。  

**00:01:43 - 00:01:57**  
原文：Second, we'll explore the computational architecture and see how gpus process mountains of data and why they're ideal for running video game graphics, bitcoin mining, neural networks and AI.  
译文：其次，我们将探讨计算架构，并了解GPU如何处理海量数据，以及为什么它们非常适合运行视频游戏图形、比特币挖矿、神经网络和人工智能。  

**00:01:57 - 00:02:01**  
原文：So stick around and let's jump right in.  
译文：所以请留步，让我们直接开始。  

**00:02:07 - 00:02:16**  
原文：This video is sponsored by micron, which manufactures the graphics memory inside this graphics card.  
译文：此视频由美光赞助，美光制造了这个显卡内部的图形内存。  

**00:02:16 - 00:02:27**  
原文：Before we dive into all the parts of the GPU, let's first understand the differences between gpus and cpus inside this graphics card.  
译文：在我们深入研究GPU的所有组成部分之前，让我们首先了解下这个显卡内部的GPU和CPU之间的区别。  

**00:02:27 - 00:02:32**  
原文：The graphics processing unit, or GPU, has over 10000 cores.  
译文：图形处理单元（GPU）拥有超过10,000个内核。  

**00:02:32 - 00:02:44**  
原文：However, when we look at the cpu or central processing unit that's mounted to the motherboard, we find an integrated circuit or chip with only 24 cores.  
译文：但是，当我们查看安装在主板上的cpu或中央处理单元时，我们发现了一个只有24个核心的集成电路或芯片。  

**00:02:44 - 00:02:46**  
原文：So which one is more powerful?  
译文：那么哪一个更强大呢？  

**00:02:46 - 00:02:49**  
原文：10000 is a lot more than 24.  
译文：10000比24多得多。  

**00:02:49 - 00:02:52**  
原文：So you would think the GPU is more powerful.  
译文：所以你可能会认为GPU更强大。  

**00:02:52 - 00:02:55**  
原文：However, it's more complicated than that.  
译文：然而，事情比这更复杂。  

**00:02:55 - 00:03:02**  
原文：A useful analogy is to think of a GPU as a massive cargo ship and a cpu as a jumbo jet airplane.  
译文：一个有用的类比是将GPU想象成一艘巨大的货船，而将CPU想象成一架大型喷气式飞机。  

**00:03:02 - 00:03:09**  
原文：The amount of cargo capacity is the amount of calculations and data that can be processed.  
译文：货物容量的数量是能够处理的计算和数据的数量。  

**00:03:09 - 00:03:17**  
原文：And the speed of the ship or airplane is the rate at which how quickly those calculations and data are being processed.  
译文：船舶或飞机的速度是这些计算和数据被处理的速率。  

（注：为了保持语句通顺，稍微调整了表达方式，但保留了原始格式和含义。）  

**00:03:17 - 00:03:30**  
原文：Essentially, it's a trade off between a massive number of calculations that are executed at a slower rate versus a few calculations that can be performed at a much faster rate.  
译文：本质上，这是大量以较慢速度执行的计算与少量可以以更快速度执行的计算之间的一种权衡。  

**00:03:30 - 00:03:44**  
原文：Another key difference is that airplanes are a lot more flexible, since they can Carry passengers packages or containers and can take off and land at any one of tens of thousands of airports.  
译文：另一个关键区别是，飞机具有更大的灵活性，因为它们可以载运乘客、包裹或集装箱，并且可以在成千上万个机场中的任何一个起飞和降落。  

**00:03:44 - 00:03:50**  
原文：Likewise, cpus are flexible in that they can run a variety of programs and instructions.  
译文：同样，cpu的灵活性在于它可以运行各种程序和指令。  

**00:03:50 - 00:03:57**  
原文：However, giant cargo ships Carry only containers with bulk contents inside and are limited to traveling between ports.  
译文：但是，巨型货船仅装载内部装有散装货物的集装箱，并且仅限于在港口之间航行。  

**00:03:57 - 00:04:06**  
原文：Similarly, gpus are a lot less flexible than cpus and can only run simple instructions like basic arithmetic.  
译文：同样地，GPU 比 CPU 灵活性差得多，只能运行像基本算术这样的简单指令。  

**00:04:06 - 00:04:13**  
原文：Additionally, gpus can't run operating systems or interface with input devices or networks.  
译文：此外，GPU 无法运行操作系统或与输入设备或网络接口。  

**00:04:13 - 00:04:21**  
原文：This analogy isn't perfect, but it helps to answer the question of which is faster, a cpu or a GPU?  
译文：这个类比并不完美，但它有助于回答哪个更快的问题，CPU还是GPU？  

**00:04:21 - 00:04:32**  
原文：Essentially, if you want to perform a set of calculations across mountains of data, then a GPU will be faster at completing the task.  
译文：本质上，如果你想对海量数据进行一系列计算，那么GPU将更快地完成任务。  

**00:04:32 - 00:04:38**  
原文：However, if you have a lot less data that needs to be evaluated quickly, then a cpu will be faster.  
译文：但是，如果您需要快速评估的数据量少得多，那么 CPU 会更快。  

**00:04:38 - 00:04:54**  
原文：Furthermore, if you need to run an operating system or support network connections in a wide range of different applications in hardware, then you'll want a cpu or planning a separate video on cpu architecture.  
译文：此外，如果您需要在硬件中运行操作系统或支持各种不同应用程序中的网络连接，那么您将需要一个CPU，或者计划一个关于CPU架构的单独视频。  

**00:04:54 - 00:04:57**  
原文：So make sure to subscribe so you don't miss it.  
译文：所以一定要订阅，这样才不会错过。  

**00:04:57 - 00:05:01**  
原文：But let's now dive into this graphics card and see how it works.  
译文：但是现在让我们深入了解这张显卡，看看它是如何工作的。  

**00:05:01 - 00:05:17**  
原文：In the center of this graphics card is the printed circuit board, or pcb, with all the various components mounted on it, and will start by exploring the brains, which is the graphics processing unit, or GPU.  
译文：在这张显卡的中心是印刷电路板，或称pcb，上面安装了各种各样的组件，我们将首先探索其核心部件，即图形处理单元，或称GPU。  

**00:05:17 - 00:05:26**  
原文：When we open it up, we find a large chip, or dnamed ga 102, built from 28.3 billion transistors.  
译文：当我们打开它时，我们发现了一个大型芯片，或称为 GA 102，由 283 亿个晶体管构建。  

**00:05:26 - 00:05:36**  
原文：The majority of the area of the chip is taken up by the processing cores, which have a hierarchical organization.  
译文：芯片的大部分面积被处理核心占据，这些核心具有层次化的组织结构。  

**00:05:36 - 00:05:49**  
原文：Specifically, the chip is divided into seven graphics processing clusters, or gpcs, and within each processing cluster are twelve streaming multi processors, or sms.  
译文：具体来说，芯片被划分为七个图形处理簇（gpcs），而在每个处理簇内有十二个流式多处理器（sms）。  

**00:05:49 - 00:06:02**  
原文：Next, inside each of these streaming multi processors are four warps and one ray tracing core, and then inside each warp are 32 kuda or shading cores and one tenser core.  
译文：接下来，每个流式多处理器内部包含四个线程束和一个光线追踪核心，然后在每个线程束内部有32个CUDA或着色核心和一个张量核心。  

**00:06:02 - 00:06:13**  
原文：Across the entire GPU are 10752 kuda cores, 336 tenser cores, and 84 ray tracing cores.  
译文：在整个GPU中，有10752个CUDA核心，336个Tensor核心和84个光线追踪核心。  

**00:06:13 - 00:06:21**  
原文：These three types of cores execute all the calculations of the GPU, and each has a different function.  
译文：这三种类型的内核执行GPU的所有计算，且每个内核都有不同的功能。  

**00:06:21 - 00:06:33**  
原文：Kuda cores can be thought of as simple binary calculators with an addition button, a multiply button, and a few others the most when running video games.  
译文：Kuda核心可以被看作是简单的二进制计算器，带有加法按钮、乘法按钮以及一些其他按钮，尤其是在运行视频游戏时。  

**00:06:33 - 00:06:53**  
原文：Tensor cores are matrix multiplication and addition calculators, and are used for geometric transformations and working with neural networks into AI and ray tracing cores are the largest but the fewest, and are used to execute ray tracing algorithms.  
译文：Tensor核心是矩阵乘法和加法计算器，用于几何变换和处理神经网络在AI中，而光线追踪核心是最大但数量最少的，用于执行光线追踪算法。  

**00:06:53 - 00:07:12**  
原文：Now that we understand the computational resources inside this chip, one rather interesting fact is that the three 80, three 90, three 80 ti and three 90 ti graphics cards all use the same ga 102 chip design for their GPU.  
译文：现在我们了解了这个芯片内部的计算资源，一个相当有趣的事实是，三张80、三张90、三张80 Ti和三张90 Ti显卡都使用相同的GA102芯片设计作为其GPU。  

**00:07:12 - 00:07:21**  
原文：This might be counterintuitive because they have different prices and were released in different years, but it's so why is this?  
译文：这可能有违直觉，因为它们的价格不同，发布年份也不同，但事实就是这样，为什么会这样呢？  

**00:07:21 - 00:07:33**  
原文：Well, during the manufacturing process, sometimes patterning errors, dust particles or other manufacturing issues cause damage and create defective areas of the circuit.  
译文：好吧，在制造过程中，有时图案错误、灰尘颗粒或其他制造问题会造成损坏，并形成电路的缺陷区域。  

**00:07:33 - 00:07:44**  
原文：Instead of throwing out the entire chip because of a small defect, engineers find the defective region and permanently isolate and deactivate the nearby circuitry.  
译文：而不是因为一个小缺陷就扔掉整个芯片，工程师们找到有缺陷的区域，并永久隔离和停用附近的电路。  

**00:07:44 - 00:07:57**  
原文：By having a GPU with a highly repetitive design, a small defect in one core only damages that particular streaming multi processor circuit and doesn't affect the other areas of the chip.  
译文：通过拥有一个高度重复设计的GPU，一个核心中的小缺陷只会损坏那个特定的流式多处理器电路，而不会影响芯片的其他区域。  

**00:07:57 - 00:08:05**  
原文：As a result, these chips are tested and categorized or bend according to the number of defects.  
译文：因此，这些芯片根据缺陷的数量进行测试和分类或弯曲。  

**00:08:05 - 00:08:15**  
原文：The three 90 ti graphics card have flawless ga 102 chips with all 10752 kuda cores working properly.  
译文：这三块90 Ti显卡拥有无瑕的GA102芯片，所有10752个CUDA核心均能正常工作。  

**00:08:15 - 00:08:20**  
原文：The 3090 has 10496 cores working.  
译文：3090 有 10496 个核心在工作。  

**00:08:20 - 00:08:35**  
原文：The three 80 ti has 10240 and the three 80 has 8704Kuta cores working, which is equivalent to having 16 damaged and deactivated streaming multi processors.  
译文：三张 80 Ti 拥有 10240 个 CUDA 核心，而三张 80 拥有 8704 个 CUDA 核心在工作，这相当于有 16 个损坏和停用的流式多处理器。  

**00:08:35 - 00:08:53**  
原文：Additionally, different graphics cards differ by their maximum clock speed and the quantity and generation of graphics memory that supports the GPU, which will explore in a little bit because we've been focusing on the physical architecture of this ga 102GPU chip.  
译文：此外，不同的显卡在其最大时钟频率以及支持GPU的显存的数量和代际上有所不同，我们将在稍后探讨这些内容，因为目前我们一直专注于这个GA102 GPU芯片的物理架构。  

**00:08:53 - 00:08:58**  
原文：Let's zoom into one of these kudocores and see what it looks like.  
译文：让我们放大其中一个Kudocore，看看它是什么样子。  

**00:08:58 - 00:09:06**  
原文：Inside this simple calculator is a layout of approximately 410000 transistors.  
译文：在这个简单的计算器内部，布局了大约410,000个晶体管。  

**00:09:06 - 00:09:20**  
原文：This section of 50000 transistors performs the operation of a times b plus c, which is called fused multiply an ed or fma and is the most common operation performed by graphics cards.  
译文：这一段包含50,000个晶体管的区域执行的操作是a乘以b再加上c，这被称为融合乘加操作或FMA，是图形卡执行的最常见操作。  

**00:09:20 - 00:09:28**  
原文：Half of the kuda chres execute fma using 32 bit floating point numbers, which is essentially scientific notation.  
译文：一半的Kuda Chres执行使用32位浮点数的FMA，这本质上是科学计数法。  

**00:09:28 - 00:09:35**  
原文：And the other half of the cores use either 32 bit integers or 32 bit floating point numbers.  
译文：另一半的核心则使用32位整数或32位浮点数。  

**00:09:35 - 00:09:51**  
原文：Other sections of this core accommodate negative numbers and perform other simple functions like bit shifting and bit masking, as well as collecting and queuing the incoming instructions and operons, and then accumulating and outputting the results.  
译文：此核心的其他部分负责处理负数和执行其他简单功能，如位移和位掩码，以及收集和排队传入的指令和操作数，然后累积和输出结果。  

**00:09:51 - 00:09:58**  
原文：As a result, this single core is just a simple calculator with a limited number of functions.  
译文：因此，这个单核只是一个具有有限功能的简单计算器。  

**00:09:58 - 00:10:16**  
原文：This calculator completes one multiply and one ad operation each clock cycle, and therefore, with this three 90 graphics card and its 10496 cores and 1.7 ghz clock, we get 35.6 trillion calculations a second.  
译文：此计算器每个时钟周期完成一次乘法和一次加法操作，因此，凭借这三张90系显卡及其10496个核心和1.7 GHz的时钟频率，我们每秒可以进行35.6万亿次计算。  

**00:10:16 - 00:10:37**  
原文：However, if you're wondering how the GPU handles more complicated operations like division, square root, and trigonometric functions, well, these calculator operations are performed by the special function units, which are far fewer as only four of them can be found in each streaming multi processor.  
译文：但是，如果您想知道GPU如何处理更复杂的操作，比如除法、平方根和三角函数，那么这些计算器操作是由特殊功能单元执行的，而在每个流式多处理器中仅能找到四个这样的单元，因此它们的数量要少得多。  

**00:10:37 - 00:10:47**  
原文：Now that we have an understanding of what's inside a single core, let's zoom out and take a look at the other sections of the ga 102 chip.  
译文：既然我们已经了解了单个核心的内部构造，让我们放大视野，看一下GA102芯片的其他部分。  

**00:10:47 - 00:10:54**  
原文：Around the edge, we find twelve graphics memory controllers, the envy link controllers, and the pcie interface.  
译文：在边缘周围，我们发现了十二个图形内存控制器、Envy链接控制器和PCIe接口。  

**00:10:54 - 00:10:59**  
原文：On the bottom is a 6 mb level two s ram memory cache.  
译文：底部是一个6兆字节二级SRAM内存缓存。  

**00:10:59 - 00:11:08**  
原文：And here's the gigatthread engine, which manages all the graphics processing clusters and streaming multi processors inside.  
译文：这是Gigathread引擎，它管理着所有内部的图形处理集群和流式多处理器。  

**00:11:08 - 00:11:18**  
原文：Now that we've explored this ga 102GPU's physical architecture, let's zoom out and take a look at the other parts inside the graphics card.  
译文：既然我们已经探讨了这个GA 102 GPU的物理架构，让我们放大视野，看看显卡内部的其他部分。  

**00:11:18 - 00:11:23**  
原文：On this side are the various ports for the displays to be plugged into.  
译文：在此侧是显示器要插入的各种端口。  

**00:11:23 - 00:11:28**  
原文：On the other side is the incoming twelve volt power connector.  
译文：另一边是即将接入的十二伏电源接头。  

**00:11:28 - 00:11:33**  
原文：And then here are the pcie pins that plug into the motherboard on the pcb.  
译文：然后这里是插入主板上的PCB的PCIe针脚。  

**00:11:33 - 00:11:47**  
原文：The majority of the smaller components constitute the voltage regulator module, which takes the incoming twelve volts and converts it to 1.1 volts and supplies hundreds of watts of power to the GPU.  
译文：大多数较小的组件构成了电压调节模块，该模块将输入的十二伏电压转换为1.1伏，并为GPU提供数百瓦的功率。  

**00:11:47 - 00:11:56**  
原文：Because all this power heats up the GPU, most of the weight of the graphics card is in the form of a heat syk with four heat pipes.  
译文：因为所有这些功率会使GPU发热，所以显卡的大部分重量是以四个热管组成的散热系统的形式存在。  

**00:11:56 - 00:12:03**  
原文：They Carry heat from the GPU and memory chips to the radiator fins, where fans then help to remove the heat.  
译文：它们将GPU和内存芯片的热量传递到散热片，然后风扇帮助散热。  

**00:12:03 - 00:12:19**  
原文：Perhaps some of the most important components aside from the GPU are the 24 gb of graphics memory chips, which are technically called gdd R six x srn and were manufactured by micron, which is the sponsor of this video.  
译文：除了GPU之外，也许一些最重要的组件是24GB的显存芯片，从技术上讲，这些芯片被称为GDDR6X SRN，由美光制造，而美光也是本视频的赞助商。  

**00:12:19 - 00:12:36**  
原文：Whenever you start up a video game or wait for a loading screen, the time it takes to load is mostly spent moving all the 3D models of a particular scene or environment from the solid state drive into these graphics memory chips.  
译文：每当您启动视频游戏或等待加载屏幕时，加载所花费的时间大多用于将特定场景或环境的所有3D模型从固态硬盘移动到这些图形内存芯片中。  

**00:12:36 - 00:12:42**  
原文：As mentioned earlier, the GPU has a small amount of data storage in its 6 mb shared level.  
译文：如前所述，GPU 在其 6 MB 共享层中有少量数据存储。  

**00:12:42 - 00:12:47**  
原文：Two cash acwhich can hold the equivalent of about this much of the video games environment.  
译文：两个现金存储器可以持有相当于此类视频游戏环境中的大约这么多资金。 

注：原句中“acwhich”可能是拼写错误，根据上下文推测其意并进行翻译。如果原始文本有特定含义或专有名词，请提供更多信息以便准确翻译。  

**00:12:47 - 00:13:01**  
原文：Therefore, in order to render a video game, different chunks of scene are continuously being transferred between the graphics memory and the GPU, because the cores are constantly performing tens of trillions of calculations.  
译文：因此，为了渲染视频游戏，不同的场景块在图形内存和GPU之间不断传输，因为核心不断进行数十万亿次的计算。  

**00:13:01 - 00:13:10**  
原文：A second gpuare data hungry machines and need to be continuously fed terabytes upon terabytes of data.  
译文：第二个gpu是数据 hungry 的机器，需要持续地输入数以太字节的数据。 

注：原文中的"gpuare"似乎是拼写错误，应为"gpus are"。此外，“data hungry”直译为“数据饥饿的”，在中文中通常表达为“需要大量数据”或“数据密集型”。因此，更正后的翻译如下：

第二个GPU是数据密集型机器，需要持续不断地输入数以太字节的数据。  

**00:13:10 - 00:13:17**  
原文：And thus, these graphics memory chips are designed kind of like multiple cranes loading a cargo ship at the same time.  
译文：因此，这些图形内存芯片的设计 类似于多个起重机同时装载一艘货船。  

**00:13:17 - 00:13:27**  
原文：Specifically, these 24 chips transfer a combined to 384 bits at a time, which is called the bus swift.  
译文：具体来说，这24个芯片一次传输合计384位，这被称为总线 swift。  

**00:13:27 - 00:13:34**  
原文：And the total data that can be transferred or the bandwidth is about 1.15 tb a second.  
译文：而且每秒能够传输的数据量或带宽大约为1.15 TB。  

**00:13:34 - 00:13:45**  
原文：In contrast, the sticks of dram that support the cpu only have a 64 bit buwidth and a maximum bandwidth closer to 64 gb.  
译文：相比之下，支持CPU的DRAM棒只有64位总线宽度，最大带宽接近64GB。  

**00:13:45 - 00:13:52**  
原文：A second one rather interesting thing is that you may think that computers only work using binary ones s and zeros.  
译文：第二件相当有趣的事情是，你可能认为计算机只用二进制的1和0工作。  

**00:13:52 - 00:14:07**  
原文：However, in order to increase data transfer rates, gdd R six x and the latest graphics memory, gdd R seven send and receive data across the bus wires using multiple voltage levels beyond just zero and one.  
译文：然而，为了提高数据传输速率，GDDR6 和最新的图形内存 GDDR7 在总线线路上使用多个电压级别（而不仅仅是0和1）来发送和接收数据。  

**00:14:07 - 00:14:19**  
原文：For example, gdd R seven uses three different encoding schemes to combine binary bits into ternary digits, or pam three symbols with voltages of zero, one and negative one.  
译文：例如，GDD R7 使用三种不同的编码方案将二进制位组合成三元数字，或者用零、一和负一电压的 PAM3 符号。  

**00:14:19 - 00:14:40**  
原文：Here's the encoding scheme on how three binary bits are encoded into two turnary digits, and this scheme is combined with an eleven bit to seven ternary digit encoding scheme, resulting in sending 276 binary bits using only 176 ternary digits.  
译文：以下是三元编码方案，说明了如何将三个二进制位编码为两个三元位，此方案与将十一位二进制位编码为七个三元位的方案相结合，最终实现了使用仅176个三元位发送276个二进制位。  

**00:14:40 - 00:14:53**  
原文：The previous generation gdd R six x, which is the memory in this 3090 graphics card, used a different encoding scheme called pam four to send two bits of data using four different voltage levels.  
译文：上一代GDDR6X，即此3090显卡中的内存，使用了一种不同的编码方案，称为PAM4，通过四种不同的电压级别发送两位数据。  

**00:14:53 - 00:15:10**  
原文：However, engineers in the graphics memory industry agreed to switch to pam three for future generations of graphics chips in order to reduce encoder complexity, improve the signal to noise ratio, and improve power efficiency.  
译文：但是，图形内存行业的工程师们同意未来几代图形芯片将转向使用PAM3，以降低编码器复杂性、提高信噪比并改善功率效率。  

**00:15:11 - 00:15:23**  
原文：Micron delivers consistent innovation to push the boundaries on how much data can be transferred every second and to design cutting edge memory chips.  
译文：美光不断进行创新，以突破每秒可以传输多少数据的极限，并设计尖端的内存芯片。  

**00:15:23 - 00:15:32**  
原文：Another advancement by micron is the development of hbm, or the high bandwidth memory that surrounds AI chips.  
译文：美光的另一项进展是开发了HBM，即高带宽内存，它围绕着AI芯片。  

**00:15:32 - 00:15:38**  
原文：Hbm is built from stacks of dram memory chips and uses tsvs or through silicon v's.  
译文：HBM 由堆叠的 DRAM 内存芯片构建，并使用 TSV（穿硅通孔）技术。  

**00:15:38 - 00:16:01**  
原文：To connect the stack into a single chip, essentially forming a cube of AI memory for the latest generation of high bandwidth memory, which is hbm three E, A single cube can have up to 24 to 36 gb of memory, thus yielding 192 gb of high speed memory around the AI chip.  
译文：将堆栈集成到单个芯片中，本质上形成最新一代高带宽内存（即HBM3E）的AI内存立方体，一个立方体可以拥有高达24到36GB的内存，从而在AI芯片周围提供192GB的高速内存。  

**00:16:01 - 00:16:11**  
原文：Next time you buy an AI accelerator system, make sure it uses microns, hbm three e, which uses 30% less power than the competitive products.  
译文：下次您购买AI加速系统时，确保它使用的是microns、hbm three e，其功耗比竞争产品低30%。  

**00:16:11 - 00:16:25**  
原文：However, unless you're building an AI data center, you're likely not in the market to buy one of these systems, which cost between 25 to $40000 and are on back order for a few years.  
译文：但是，除非您正在建造一个AI数据中心，否则您可能不会打算购买这些系统之一，它们的价格在25,000到40,000美元之间，并且需要等待几年才能交付。  

**00:16:25 - 00:16:35**  
原文：If you're curious about high bandwidth memory or microns next generation of graphics memory, take a look at one of these links in the description.  
译文：如果您对高带宽内存或美光的下一代图形内存感到好奇，请查看描述中的这些链接之一。  

**00:16:35 - 00:16:51**  
原文：Alternatively, if designing the next generation of memory chips interests you, micron is always looking for talented scientists and engineers to help innovate on cutting edge chips, and you can find out more about working for micron using this link.  
译文：或者，如果您对设计下一代内存芯片感兴趣，美光一直在寻找有才华的科学家和工程师来帮助创新尖端芯片，您可以使用此链接了解更多关于在美光工作的信息。  

**00:16:51 - 00:17:09**  
原文：Now that we've explored many of the physical components inside this graphics card and GPU, let's next explore the computational architecture and see how applications like video game graphics and bitcoin mining run what's called embarrassingly parallel operations.  
译文：现在我们已经了解了这个显卡和GPU内部的许多物理组件，接下来让我们探讨一下计算架构，并看看像视频游戏图形和比特币挖掘这样的应用是如何运行所谓的令人尴尬的并行操作的。 

请注意，"embarrassingly parallel operations" 是一个技术术语，直译为“令人尴尬的并行操作”，但在中文中通常会根据上下文解释为“易于并行化”的操作，因为这些任务可以非常容易地分解成多个独立的部分同时进行处理。如果您希望更准确的技术翻译，可以这样表达：

现在我们已经了解了这个显卡和GPU内部的许多物理组件，接下来让我们探讨一下计算架构，并看看像视频游戏图形和比特币挖掘这样的应用是如何运行所谓易于并行化的操作的。  

**00:17:09 - 00:17:29**  
原文：Although it may sound like a silly name, embarrassingly parallel is actually a technical classification of computer problems where little or no effort is needed to divide the problem into parallel tasks, and video game rendering and bitcoin mining easily fall into this category.  
译文：虽然听起来可能像个可笑的名字，但令人尴尬的并行（embarrassingly parallel）实际上是对计算机问题的一种技术分类，在这种分类中，将问题划分为并行任务所需的努力很少或几乎不需要，而视频游戏渲染和比特币挖掘很容易归入这一类别。  

**00:17:29 - 00:17:46**  
原文：Essentially, gpus solve embarrassingly parallel problems using a principle called sidy, which stands for single instruction multiple data, where the same instructions or steps are repeated across thousands to millions of different numbers.  
译文：本质上，GPU 使用一种称为 SIMD（单指令多数据）的原则来解决令人尴尬的并行问题，其中相同的指令或步骤会在成千上万到数百万个不同的数据上重复执行。  

**00:17:46 - 00:17:55**  
原文：Let's see an example of how sidy or single instruction multiple data is used to create this 3D video game environment.  
译文：让我们来看一个例子，了解如何使用SIMD（单指令多数据）来创建这个3D视频游戏环境。  

**00:17:55 - 00:18:10**  
原文：As you may know already, this cowboy hat on the table is composed of approximately 28000 triangles built by connecting together around 14000 vertices, each with xy and z coordinates.  
译文：如您所知，这张桌子上的牛仔帽是由大约28000个三角形组成，这些三角形是由大约14000个顶点连接而成的，每个顶点都有xy和z坐标。  

**00:18:10 - 00:18:19**  
原文：These vertex coordinates are built using a coordinate system called model space, with the origin of zero, zero, zero being at the center of the hat.  
译文：这些顶点坐标是使用称为模型空间的坐标系构建的，其原点为零、零、零，位于帽子的中心。  

**00:18:19 - 00:18:29**  
原文：To build a 3D world, we place hundreds of objects, each with their own model space, into the world environment.  
译文：要构建一个3D世界，我们将数百个物体放置到世界环境中，每个物体都有自己的模型空间。  

**00:18:29 - 00:18:45**  
原文：And in order for the camera to be able to tell where each object is relative to other objects, we have to convert or transform all the vertices from each separate model space into the shared world coordinate system or world space.  
译文：为了使相机能够确定每个物体相对于其他物体的位置，我们必须将每个独立模型空间中的所有顶点转换或变换到共享的世界坐标系或世界空间中。  

**00:18:45 - 00:18:53**  
原文：So, as an example, how do we convert the 14000 vertices of the cowboy hat from model space into world space?  
译文：所以，举个例子，我们如何将牛仔帽的14000个顶点从模型空间转换到世界空间呢？  

**00:18:53 - 00:19:06**  
原文：Well, we use a single instruction, which adds the position of the origin of the hat in world space to the corresponding xy and z coordinate of a single vertex in model space.  
译文：好的，我们使用一条指令，将帽子原点在世界空间中的位置添加到模型空间中单个顶点对应的xy和z坐标上。  

**00:19:06 - 00:19:17**  
原文：Next, we copy this instruction to multiple data, which is all the remaining xy and z coordinates of the other thousands of vertices that are used to build that hat.  
译文：接下来，我们将此指令复制到多个数据，这些数据是用于构建帽子的其他数千个顶点的所有剩余的xy和z坐标。  

**00:19:17 - 00:19:33**  
原文：Next, we do the same for the table and the rest of the hundreds of other objects in the scene, each time using the same instructions, but with the different objects coordinates in world space, and each objects thousands of vertices in model space.  
译文：接下来，我们对表格以及场景中的其他数百个对象做同样的处理，每次使用相同的指令，但使用不同对象的世界空间坐标，以及每个对象在模型空间中的数千个顶点。  

**00:19:33 - 00:19:46**  
原文：As a result, all the vertices and triangles of all the objects are converted to a common world space coordinate system, and the camera can now determine which objects are in front and which are behind.  
译文：因此，所有对象的所有顶点和三角形都被转换到一个共同的世界空间坐标系中，现在相机可以确定哪些对象在前面，哪些在后面。  

**00:19:46 - 00:20:06**  
原文：This example illustrates the power of sidy or single instruction multiple data, and how a single instruction is applied to 5629 different objects with a total of 8.3 million vertices within the scene, resulting in 25 million edition calculations.  
译文：此示例展示了SIMD（单指令多数据）的强大功能，以及如何将一条指令应用于场景中的5629个不同对象，这些对象总共有830万个顶点，从而导致了2500万次编辑计算。  

**00:20:06 - 00:20:25**  
原文：The key to sembly and embarrassingly parallel programs is that every one of these millions of calculations has no dependency on any other calculation, unless thus all these calculations can be distributed to the thousands of cores of the GPU and completed in parallel with one another.  
译文：sembly 和令人尴尬的并行程序的关键在于，这些数以百万计的计算中的每一个都与其他计算没有任何依赖关系，因此所有这些计算都可以分配给 GPU 的数千个内核，并可以相互并行完成。  

请注意，原文中 "sembly" 可能是 "assembly" 的拼写错误，以及 "embarrassingly parallel programs" 通常指的是那些任务之间完全没有依赖、易于并行化的程序。如果你需要更正这些地方，请告知。  

**00:20:25 - 00:20:35**  
原文：It's important to note that vertex transformation from model space to world space is just one of the first steps of a rather complicated video game graphics rendering pipeline.  
译文：需要注意的是，顶点从模型空间变换到世界空间只是相对复杂的视频游戏图形渲染管道中的第一步。  

**00:20:35 - 00:20:40**  
原文：And we have a separate video that delves deeper into each of these other steps.  
译文：我们有单独的视频深入探讨这些其他每个步骤。  

**00:20:40 - 00:20:52**  
原文：Also, we skipped over the transformations for the rotation and scale of each object, but factoring in these values is a similar process that requires additional sid calculations.  
译文：另外，我们跳过了每个对象的旋转和缩放变换，但将这些值考虑在内是一个类似的过程，需要额外的sid计算。  

**00:20:52 - 00:21:01**  
原文：Now that we have a simple understanding of sidy, let's discuss how this computational architecture matches up with the physical architecture.  
译文：现在我们对sidy有了简单的了解，让我们讨论一下这种计算架构是如何与物理架构相匹配的。  

**00:21:01 - 00:21:08**  
原文：Essentially, each instruction is completed by a thread, and this thread is matched to a single kuda core.  
译文：本质上，每个指令由一个线程完成，而这个线程对应于一个单一的CUDA核心。  

**00:21:08 - 00:21:17**  
原文：Threads are bundled into groups of 32 called warps, and the same sequence of instructions is issued to all the threads in a warp.  
译文：线程被捆绑成32个一组的单元，称为 warp（线程束），并且相同的指令序列会被发送到一个warp中的所有线程。  

**00:21:17 - 00:21:23**  
原文：Next, warps are grouped into thread blocks, which are handled by the streaming multi processor.  
译文：接下来，线程束被分组为线程块，这些线程块由流式多处理器处理。  

**00:21:23 - 00:21:29**  
原文：And then finally, thread blocks are grouped into grids which are computed across the overall GPU.  
译文：然后最后，线程块被分组为网格，这些网格在整个GPU上进行计算。  

**00:21:29 - 00:21:40**  
原文：All these computations are managed or scheduled by the gigatthread engine, which efficiently maps thread blocks to the available streaming multi processors.  
译文：所有这些计算都由 gigatthread 引擎进行管理或调度，该引擎能高效地将线程块映射到可用的流式多处理器上。  

**00:21:40 - 00:21:55**  
原文：One important distinction is that within sidy architecture, all 32 threads in a war follow the same instructions and are in lockstep with each other, kind of like a failings of soldiers moving together.  
译文：一个重要的区别是在 sidy 架构中，所有 32 个线程在战争中遵循相同的指令，并且彼此同步，就像一队士兵一起行动一样。请注意，这里可能存在术语不准确的情况，“sidy architecture”和“war”在特定上下文中应更正为正确的术语，例如“SIMD 架构”和“warp”。修正后的句子如下：

一个重要的区别是在 SIMD 架构中，所有 32 个线程在一个 warp 中遵循相同的指令，并且彼此同步，就像一队士兵一起行动一样。  

**00:21:55 - 00:22:01**  
原文：This lockstep execution applied to gpus up until around 2016.  
译文：这种锁步执行方式应用于gpu上直到大约2016年左右。  

**00:22:01 - 00:22:07**  
原文：However, newer gpus follow a sit architecture or single instruction multiple threads.  
译文：但是，较新的GPU遵循SIMT架构，即单指令多线程。  

**00:22:07 - 00:22:15**  
原文：The difference between sid and sit is that a while both send the same set of instructions to each thread.  
译文：sid 和 sit 之间的区别在于，虽然两者都向每个线程发送相同的一组指令。  

**00:22:15 - 00:22:22**  
原文：With sit, the individual threads don't need to be in lockstep with each other and can progress at different rates.  
译文：使用sit，各个线程不需要彼此同步，可以以不同的速率进步。  

**00:22:22 - 00:22:26**  
原文：In technical jargon, each thread is given its own program counter.  
译文：在专业术语中，每个线程都被分配了自己的程序计数器。  

**00:22:26 - 00:22:43**  
原文：Additionally, with sympty, all the threads within a streaming multi processor use a shared 128 kilobite l one cache, and thus data that's output by one thread can be subsequently used by a separate thread.  
译文：此外，使用sympty时，流式多处理器内的所有线程共享一个128千字节的L1缓存，因此一个线程输出的数据可以随后被另一个线程使用。  

**00:22:43 - 00:22:58**  
原文：This improvement from sim d to sim t allows for more flexibility when encountering warped divergence via data dependent conditional branching and easier reconvergence for the threads to reach the barrier synchronization.  
译文：从 sim d 改进到 sim t，在遇到依赖数据的条件分支导致的扭曲发散时，提供了更大的灵活性，并且使线程更容易重新聚合以达到屏障同步。  

**00:22:58 - 00:23:05**  
原文：Essentially, newer architectures of gpus are more flexible and efficient, especially when encountering branches in code.  
译文：本质上，较新的GPU架构更加灵活和高效，特别是在代码中遇到分支时。  

**00:23:05 - 00:23:17**  
原文：One additional note is that although you may think that the term warp is derived from warp drives, it actually comes from weaving, and specifically the jekar loom.  
译文：另有一个注释是，虽然你可能认为术语“warp”源自曲速引擎（warp drives），但实际上它来自于编织，具体来说是jekar织机。  

**00:23:17 - 00:23:27**  
原文：This loom from 18Oh four used programmable punch cards to select specific threads out of a set to weave together intricate patterns.  
译文：这台1804年的织布机使用可编程的穿孔卡来选择特定的一组线进行编织，以织出复杂的图案。  

**00:23:27 - 00:23:30**  
原文：As fascinating as looms are, let's move on.  
译文：尽管织机非常迷人，让我们继续吧。  

**00:23:30 - 00:23:36**  
原文：The final topics will explore are bit coin mining, tensor cores, and neural networks.  
译文：最后要探讨的主题将是比特币挖矿、张量核心和神经网络。  

**00:23:36 - 00:23:48**  
原文：But first, welike to ask you to like this video, write a quick comment below, share it with a colleague, friend or on social media, and subscribe if you haven't already.  
译文：但首先，我们希望您能点赞这个视频，在下方简短评论，与同事、朋友或在社交媒体上分享，并且如果您还没有订阅的话，请订阅。  

**00:23:48 - 00:24:10**  
原文：The dream of branch education is to make free and accessible, visually engaging educational videos that dive deeply into a variety of topics on science, engineering, and how technology works, and then to combine multiple videos into an entirely free engineering curriculum for high school and college students.  
译文：分支教育的梦想是制作免费且易于访问、视觉上引人入胜的教育视频，深入探讨科学、工程和技术原理等众多主题，并将多个视频组合成完全免费的工程课程，供高中生和大学生使用。  

**00:24:10 - 00:24:17**  
原文：Taking a few seconds to like, subscribe and comment below helps us a ton.  
译文：花几秒钟时间点赞、订阅并在下方评论对我们帮助很大。  

**00:24:17 - 00:24:28**  
原文：Additionally, we have a Patreon page with amas and behind the scenes footage, and if you find what we do useful, we would appreciate any support.  
译文：此外，我们还有一个Patreon页面，上面有问答环节和幕后花絮，如果您觉得我们的工作有用，我们将不胜感激任何支持。  

**00:24:28 - 00:24:29**  
原文：Thank you.  
译文：谢谢你。  

**00:24:29 - 00:24:41**  
原文：So now that we've explored how single instruction multiple threads is used in video games, let's briefly discuss why gpus were initially used for mining bitcoin.  
译文：所以现在我们已经探讨了单指令多线程在视频游戏中的应用，让我们简要讨论一下为什么最初使用GPU进行比特币挖矿。  

**00:24:41 - 00:24:48**  
原文：We're not going to get too far into the algorithm behind the block chain and we'll save it for a separate episode.  
译文：我们不会过多深入区块链背后的算法，并将其留作单独的一集来讨论。  

**00:24:48 - 00:25:02**  
原文：But essentially to create a block on the block chain, the shw 256 hashing algorithm is run on a set of data that includes transactions, a timestamp, additional data, and a random number called an onafter.  
译文：但本质上，要在区块链上创建一个区块，需要对一组数据运行SHA 256哈希算法，这组数据包括交易、时间戳、附加数据和一个称为“nonce”的随机数。  

**00:25:02 - 00:25:10**  
原文：Feeding these values through the Shaw 256 hashing algorithm, a random 256 bit value is output.  
译文：将这些值通过 Shaw 256 哈希算法进行处理，输出一个随机的 256 位值。  

**00:25:10 - 00:25:23**  
原文：You can kind of think of this algorithm as a lottery ticket generator where you can't pick the lottery number, but based on the input data, the Shaw 256 algorithm generates a random lottery ticket number.  
译文：你可以将这个算法理解为一个彩票号码生成器，你不能选择彩票的号码，但是根据输入的数据，SHA256算法会生成一个随机的彩票号码。  

**00:25:23 - 00:25:32**  
原文：Therefore, if you change the ns value and keep the rest of the transaction data the same, you'll generate a new random lottery ticket number.  
译文：因此，如果你更改 ns 值并保持交易的其余数据不变，你将生成一个新的随机彩票号码。  

**00:25:32 - 00:25:43**  
原文：The winner of the spit coin mining lottery is the first randomly generated lottery number to have the first 80 bits all zeros, while the rest of the 176 values don't matter.  
译文：吐币矿工抽奖的中奖者是第一个随机生成的彩票号码，其前80位均为零，而其余的176位值则不重要。  

**00:25:43 - 00:25:54**  
原文：And once a winning bitcoin lottery ticket is found, the reward is three bitcoin, and the lottery resets with a new set of transactions and input values.  
译文：一旦找到中奖的比特币彩票，奖励是三个比特币，然后彩票重置，带有新的一组交易和输入值。  

**00:25:54 - 00:25:56**  
原文：So why were graphics cards used?  
译文：那么，为什么使用显卡呢？  

**00:25:56 - 00:25:57**  
原文：Well?  
译文：好吧？  

**00:25:57 - 00:26:08**  
原文：Gpus ran thousands of iterations of the shore 256 algorithm with the same transactions tistamp other data, but with different nts values.  
译文：GPU 运行了成千上万次 Shore 256 算法的迭代，使用相同的交易时间戳和其他数据，但具有不同的 nts 值。  

**00:26:08 - 00:26:21**  
原文：As a result, a graphics card like this one could generate around 95 million Shaw 256 hashes, or 95 million randomly numbered lottery tickets every second.  
译文：因此，像这样的显卡每秒可以生成大约9500万个SHA-256哈希值，或者可以说是每秒生成9500万张随机编号的彩票。  

**00:26:21 - 00:26:27**  
原文：And hopefully, one of those lottery numbers would have the first 80 digits as all zeros.  
译文：并希望，其中的一个彩票号码的前80位数字全部为零。  

**00:26:27 - 00:26:50**  
原文：However, nowadays, computers filled with a six or application specific integrated circuits performform 250 trillion hashes a second, or the equivalent of two 600 graphics cards, thereby making graphics cards look like a spoon when mining bitcoin next to an excavator that is an asic mining computer.  
译文：然而，如今，装有六个或更多应用特定集成电路的计算机每秒可以执行250万亿次哈希运算，这相当于两块600系列显卡的算力，从而使显卡在挖掘比特币时看起来就像在ASIC mining computer（应用特定集成电路矿机）这台挖掘机旁边的一把勺子。  

**00:26:50 - 00:26:54**  
原文：Let's next discuss the design of the tensor cores.  
译文：接下来，让我们讨论张量核心的设计。  

**00:26:54 - 00:27:00**  
原文：Ittake multiple full length videos to cover generative AI and neural networks.  
译文：需要多个完整长度的视频来涵盖生成式人工智能和神经网络。  

**00:27:00 - 00:27:04**  
原文：So we'll focus on the exact matrix math that tensor cores solve.  
译文：所以我们将会专注于张量核心所解决的精确矩阵数学。  

**00:27:04 - 00:27:12**  
原文：Essentially, tensor cores take three matrices and multiply the first two, add in the third, and then output the result.  
译文：本质上，张量核心单元接收三个矩阵，将前两个矩阵相乘，加上第三个矩阵，然后输出结果。  

**00:27:12 - 00:27:15**  
原文：Let's look at one value of the output.  
译文：让我们看一下输出的一个值。  

**00:27:15 - 00:27:41**  
原文：This value is equal to the sum values of the first row of the first matrix multiplied by the values from the first column of the second matrix, and then the corresponding value of the third matrix is added in, because all the values of the three input matrices are ready at the same time, the tensor cores complete all of the matrix multiplication and addition calculations concurrently.  
译文：此值等于第一个矩阵的第一行的值与第二个矩阵的第一列的值相乘后的和，然后加上第三个矩阵的相应值。由于三个输入矩阵的所有值同时准备好，张量核心并发完成所有的矩阵乘法和加法计算。  

**00:27:41 - 00:27:52**  
原文：Neural networks and generative AI require trillions to quadrillions of matrix multiplication and addition operations and typically uses much larger matrices.  
译文：神经网络和生成式人工智能需要进行万亿到千万亿次的矩阵乘法和加法运算，并且通常使用更大得多的矩阵。  

**00:27:52 - 00:27:58**  
原文：Finally, there are ray tracing cores, which we explored in a separate video that's already been released.  
译文：最后，还有光线追踪核心，相关内容我们已经在之前发布的一个单独视频中进行了探讨。  

**00:27:58 - 00:28:01**  
原文：That's pretty much it for graphics cards.  
译文：这就是关于显卡的全部内容。  

**00:28:01 - 00:28:09**  
原文：We're thankful to all our Patreon and tube membership sponsors for supporting our videos.  
译文：我们感谢所有 Patreon 和Tube会员赞助商对我们视频的支持。  

**00:28:09 - 00:28:16**  
原文：If you want to financially support our work, you can find the links in the description below.  
译文：如果你想在经济上支持我们的工作，你可以在我 若要在经济上支持我们的工作，可以在下方描述中找到链接。  

**00:28:16 - 00:28:25**  
原文：This is branch education, and we create 3D animations that dive deeply into the technology that drives our modern world.  
译文：这是分支教育，我们创建3D动画，深入探究驱动我们现代世界的科技。  

**00:28:25 - 00:28:28**  
原文：Watch another ch by Clione of the.  
译文：观看另一个由克利奥涅制作的。  



## 相关资源

### 官方链接
- [创作者频道: Branch Education](https://www.youtube.com/channel/UCdp4_l1vPmpN-gDbUwhaRUQ)
- [原始视频: How do Graphics Cards Work?  Exploring GPU Architecture](https://www.youtube.com/watch?v=h9Z4oGN89MU)

### 视频描述中提及的链接
- [链接 1](https://bit.ly/micron-careers)
- [链接 2](https://bit.ly/micron-graphic-memory)
- [链接 3](https://bit.ly/micron-hbm3e)
- [链接 4](https://www.patreon.com/brancheducation)
- [链接 5](https://www.branch.education)

### 可能的相关主题
> 根据视频内容搜索更多相关资源

