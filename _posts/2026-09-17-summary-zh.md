---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> From 109 items, 13 important content pieces were selected

---

1. [《.NET 11 性能改进》：Stephen Toub 年度深度剖析](#item-1) ⭐️ 9.1/10
2. [IBM Research 发问：LLM 智能体成功一次，还能再成功吗？](#item-2) ⭐️ 8.4/10
3. [OpenAI 出资创建 AI 模型所缺的生物学数据](#item-3) ⭐️ 8.0/10
4. [工程师蒸馏 4B 模型，声称查询计划比 Postgres 快 81%](#item-4) ⭐️ 7.8/10
5. [Dream-RSI：被称为“递归自我改进”的世界模型训练框架引发争议](#item-5) ⭐️ 7.8/10
6. [《麻省理工科技评论》审视 AI 万亿美元基础设施豪赌](#item-6) ⭐️ 7.7/10
7. [NVIDIA 宣布支持用 Rust 原生编写 CUDA GPU 内核](#item-7) ⭐️ 7.6/10
8. [利用零稀疏性将三值 LLM 压缩至 1.58 比特以下](#item-8) ⭐️ 7.5/10
9. [小米 MiMo 2.6 公开实时后训练 RL 仪表盘](#item-9) ⭐️ 7.5/10
10. [Google 的 SIMD 向量化 vqsort 旧文重现，社区指出更新的 SOTA 排序算法](#item-10) ⭐️ 7.5/10
11. [Show HN：电子墨水画框听鸟鸣，并用 19 世纪插画风格绘制出来](#item-11) ⭐️ 7.3/10
12. [Mozilla 与 Mistral 为 Firefox 引入 AI 浏览，引发本地与云端推理之争](#item-12) ⭐️ 7.0/10
13. [Ben Thompson：ChatGPT 广告行之有效，并解决亚马逊聊天机器人的难题](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [《.NET 11 性能改进》：Stephen Toub 年度深度剖析](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-11/) ⭐️ 9.1/10

微软发布了《.NET 11 性能改进》，这是 Stephen Toub 每年撰写的一篇极为详尽的技术长文，系统梳理了下一个 .NET 版本在运行时、JIT、垃圾回收和异步方面带来的改进。文章为每一项优化都配上了微基准测试和汇编级别的对比，例如在 Arm64 上由于去掉了部分边界检查指令，生成的代码体积从 68 字节缩减到 60 字节。 由于这些属于运行时层面的优化，现有 .NET 应用只需升级框架即可自动获得性能提升，无需修改任何代码。文章还预告了“运行时原生异步”（runtime async），这是对 async/await 编译方式的根本性重构，可能改变整个 .NET 生态的代码生成与调试体验。 文章侧重于微基准测试和反汇编对比，而非端到端的应用级测量；运行时原生异步采用了异步挂起点尾部合并（tail merging）等技术来减小生成的代码体积。这只是一份阶段性预览，因为通常还会有更多性能改进在后续预览版中陆续落地，直到正式版发布。

hackernews · soheilpro · Sep 15, 12:18 · [社区讨论](https://news.ycombinator.com/item?id=49711424)

**背景**: .NET 会先把 C# 编译成存放在程序集中的中间语言（IL），再由即时编译器（JIT）在运行时把 IL 翻译成原生机器码，因此 JIT 的改动会直接影响程序的执行速度。垃圾回收器负责自动分配和释放托管内存，其停顿时间和吞吐量一直是优化的重点。过去 C# 的 async/await 是由编译器生成状态机代码来实现的，而运行时原生异步把这一机制搬到了运行时内部，这正是今年这篇文章中该话题格外受关注的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Just-in-time_compilation">Just -in- time compilation - Wikipedia</a></li>
<li><a href="https://versionlog.com/blog/what-to-expect-in-dotnet-11/">What to Expect in . NET 11 : Runtime, Performance, and Async ...</a></li>
<li><a href="https://www.c-sharpcorner.com/article/net-11-runtime-async-performance-what-actually-changes/">NET 11 Runtime Async Performance: What Actually Changes</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论总体以赞赏为主，有人指出现有服务“直接免费变快”，也有不少人对运行时原生异步表示期待。最主要的批评意见是希望看到应用级别的基准测试，以体现累积性能收益，而不只是孤立的微基准；还有一位开发者提问：非系统级语言的程序员是否真的需要读懂汇编才能跟上这篇文章。

**标签**: `#.NET`, `#performance`, `#runtime`, `#JIT`, `#software engineering`

---

<a id="item-2"></a>
## [IBM Research 发问：LLM 智能体成功一次，还能再成功吗？](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) ⭐️ 8.4/10

IBM Research 在 Hugging Face 上发表博客，探讨为什么 LLM 智能体在第一次成功完成任务后，重新运行同一任务却常常失败，并主张把“一致性”而不只是单次任务成功率，作为智能体系统的核心评估指标。该文章与其 ALTK-Evolve 开源工作一脉相承：ALTK-Evolve 能把原始的智能体执行轨迹（trajectory）转化为可复用的指导规则，让智能体在多轮迭代中持续改进。 目前大多数智能体基准只报告一次性的成功或失败结果，这很容易高估其在真实场景中的可靠性；如果一个智能体只有 60% 的概率成功，即便演示时表现良好，也无法用于生产环境的自动化。随着企业将智能体引入面向客户的场景和自动化流程，衡量“多次运行结果是否一致”已成为放心把任务交给它们的前提条件。 讨论的核心在于 LLM 生成过程的非确定性，以及自然语言任务本身存在的歧义——这意味着两条完全相同的提示可能触发不同的计划、工具调用乃至失败。IBM 相关的 ALTK-Evolve 组件属于 Agent Lifecycle Toolkit（ALTK）的一部分，能够从历史轨迹中学习指导规则，并提供一个 Lite 版本，可直接接入 Claude Code、Codex 等现有智能体助手。

rss · Hugging Face Blog · Sep 15, 16:00

**背景**: LLM 智能体（agent）是指由语言模型负责规划、调用工具并执行多步操作以完成目标的系统，而不只是回答单个问题。由于每一步都涉及对概率模型进行采样，前期的微小差异可能在后续步骤中被放大成完全不同的行为，因此智能体可能通过一次基准测试，却在重跑同一测试时失败。AI 可观测性与评估平台，以及 LangGraph 这类框架，很大程度上正是为弥补这一可靠性缺口而生——通过结构化编排与可重复测试来约束智能体的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-research/altk-evolve">ALTK‑Evolve: On‑the‑Job Learning for AI Agents</a></li>
<li><a href="https://github.com/AgentToolkit/altk-evolve">GitHub - AgentToolkit/altk-evolve: Self improving agents through iterations · GitHub</a></li>
<li><a href="https://agenttoolkit.github.io/altk-evolve/">Agent Lifecycle Toolkit (ALTK) - Evolve</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM evaluation`, `#agent reliability`, `#Hugging Face`, `#IBM Research`

---

<a id="item-3"></a>
## [OpenAI 出资创建 AI 模型所缺的生物学数据](https://www.technologyreview.com/2026/09/15/1144129/ai-models-need-more-data-about-biology-and-openai-is-paying-to-create-it/) ⭐️ 8.0/10

《麻省理工科技评论》报道称，AI 模型严重缺乏生物学数据，而 OpenAI 正在出资推动这类数据的生成。其中一个被提出的途径，最早由专注临床试验的政策分析师 Ruxandra Teslo 在去年提出：在倒闭生物科技公司的破产程序中参与竞标，从而获取其详细的监管申报文件、生产工艺策略和安全数据。 生物学与临床数据是医疗 AI 最稀缺的输入之一，而盘活那些被封存在倒闭公司内部的数据，可能显著改善药物发现、安全性建模和临床决策支持。OpenAI 愿意为“制造数据”付费，说明头部 AI 实验室已把特定领域的数据获取——而不只是模型架构——视为下一代科学 AI 的瓶颈。 这一思路的关键在于，破产拍卖允许竞标者获得通常被视为商业秘密的资产，例如监管申报文件、生产工艺诀窍和安全数据集。明显的顾虑在于法律与伦理层面：患者隐私、尚未厘清的知识产权归属，以及所回收数据可能质量低下或被大量涂黑删节的风险。

rss · MIT Tech Review · Sep 15, 12:00

**背景**: 大语言模型和多模态模型依赖海量文本语料进行训练，但同等规模的高质量生物学与临床数据却难以获得：它们大多沉淀在企业的专有文件中、未被发表的阴性结果里，或受隐私法规限制而无法流通。倒闭的生物科技初创公司恰恰是这类信息的一个特殊储存库，因为监管机构要求在疗法进入临床试验前提交详细的安全性与生产文档。出资汇集这类数据，是 AI 公司希望弥合“通用模型”与“真正有用的科学模型”之间差距的一种方式。

**标签**: `#AI`, `#Biotech`, `#Data`, `#OpenAI`, `#Medical AI`

---

<a id="item-4"></a>
## [工程师蒸馏 4B 模型，声称查询计划比 Postgres 快 81%](https://rohanbansal.com/qorl) ⭐️ 7.8/10

一位工程师（rohanbansal.com/qorl）训练了一个 4B 参数的蒸馏模型来生成 SQL 查询计划，声称在其基准测试中相比 Postgres 取得 1.81 倍的几何平均加速，总延迟下降 44.7%。作者表示，他花费约 800 美元从 Lambda 租用双 H100 SXM 节点约 95 小时，并花了约 400 美元的 OpenAI API 费用，用于生成作为蒸馏数据的“Astra”轨迹示范。 如果结果可复现，这将说明前沿模型在查询计划上的推理能力可以被蒸馏进一个可自托管的小模型，从而指向无需把数据送往第三方 API 的 LLM 辅助或学习式查询优化器。这也切入了关于数据库优化器应由神经启发式方法还是传统基于代价的规划器驱动的更大争论。 评论者指出该基准测试范围很窄：8 GB 数据集完全能放进内存、shared_buffers 被限制为其中一小部分、测量前先对查询做预热，而且只测只读 SELECT，这让人们对真实 OLTP 负载下的过拟合风险产生担忧。批评者还指出非确定性失败的风险：LLM 规划器有时会“幻觉”并漏用索引，产生灾难性缓慢的计划，且缺乏内置的兜底机制。

hackernews · polyphilz · Sep 16, 18:50 · [社区讨论](https://news.ycombinator.com/item?id=49731285)

**背景**: 查询规划器是数据库中决定 SQL 语句如何执行的组件——使用哪些索引、以什么顺序连接表——而传统规划器依赖代价模型和启发式规则，而非学习得到的模型。知识蒸馏是一种机器学习技术，把庞大昂贵“教师”模型的行为迁移到一个运行成本低得多的“学生”模型上。在这个案例中，教师是一个前沿模型，其查询规划轨迹被记录下来，用作 4B 学生模型的训练数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>
<li><a href="https://arxiv.org/pdf/2505.18458v1">A Survey of LLM $\times$ DATA</a></li>

</ul>
</details>

**社区讨论**: Hacker News 讨论帖（355 分、68 条评论）普遍对“比 Postgres 快 81%”这一标题持怀疑态度，高赞评论强调该测试是全内存、预热、只读的环境，并存在过拟合风险。其他人则警告非确定性的计划失败（LLM 偶尔会漏用索引的幻觉），认为最优计划的构造高度依赖数学与算法，更适合 AlphaGo 式神经启发式方法而非 LLM，并指出公开承认蒸馏自前沿模型可能在当下闭源与开源模型的争论中招致指责。

**标签**: `#LLM`, `#query-optimization`, `#databases`, `#knowledge-distillation`, `#applied-AI`

---

<a id="item-5"></a>
## [Dream-RSI：被称为“递归自我改进”的世界模型训练框架引发争议](https://arxiv.org/abs/2609.14858) ⭐️ 7.8/10

一篇新的 arXiv 论文提出了名为 “Dream-RSI” 的训练方案，它基于世界模型，并被作者称为“递归自我改进”，在 Hacker News 上引发了热烈讨论。评论者将其方法大致还原为：让多个智能体在固定步数预算内反复改进解题方案并择优保留，同时认为把它称为 “RSI” 言过其实。 这篇论文处于两条热门研究脉络的交汇点——面向强化学习的世界模型，以及可自我改进的智能体系统，因此社区如何评判其表述方式，将影响未来“自我改进”类主张如何被定义与评估。如果这类循环真能带来复合式的能力提升，它既可能大幅推动智能体训练，也会带来对系统自主自我改进的安全担忧。 该方案据称是对现有训练循环的优化，而非展示了无限、开放式的自我改进：每个任务中智能体只有有限次数的改进步数，并使用“基于历史的重放模拟器”做离策略评估，以避免昂贵的环境 rollout。评论者还质疑，随着搜索空间扩大，该方法如何防止策略过拟合于已发现的分支并逐渐失效（stale）。

hackernews · bananaflag · Sep 16, 13:44 · [社区讨论](https://news.ycombinator.com/item?id=49726955)

**背景**: 递归自我改进（RSI）是一种假说性过程：AI 系统改写自身代码或训练流程来提升自己，理论上可能导致“智能爆炸”，但迄今尚无任何尝试显示出这种失控效应。名称中的 “Dream” 指向 Danijar Hafner 的世界模型强化学习智能体 Dreamer 系列，该系列最早于 2019 年发表，并持续迭代至 DreamerV3 及其后续版本。世界模型从经验（通常是视频）中学习环境的压缩模拟，使智能体可以在“想象”中训练，而不必依赖代价高昂的真实环境交互——这正是本文所依托的设定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://arxiv.org/abs/2301.04104">[2301.04104] Mastering Diverse Domains through World Models</a></li>
<li><a href="https://arxiv.org/abs/2607.07663">[2607.07663] Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍称赞该方法是对现有训练方式的不错优化，但反对将其称为 RSI，有人直言这种表述具有误导性，因为该系统无法永远持续地自我改进。也有人欣赏其中具体的设计选择，例如用重放模拟器做离策略评估；另有讨论提出了安全层面的疑问——为何似乎很少有人担心递归自我改进的风险；还有评论者推荐了 Hafner 的 Dreamer 论文和 TalkRL 播客节目作为背景资料。

**标签**: `#AI research`, `#recursive self-improvement`, `#world models`, `#reinforcement learning`, `#agentic systems`

---

<a id="item-6"></a>
## [《麻省理工科技评论》审视 AI 万亿美元基础设施豪赌](https://www.technologyreview.com/2026/09/15/1144028/ai-infrastructure-boom-investment-bubble-risk/) ⭐️ 7.7/10

《麻省理工科技评论》发表了一篇分析文章，讨论 AI 基础设施领域高达万亿美元的投资热潮，以及这轮热潮可能形成泡沫的经济风险。文章以宾夕法尼亚大学沃顿商学院金融学教授 Jessica Wachter 为切入点，她表示自己在评估 AI 对经济的影响时，并没有从众多商业与技术层面的不确定性出发，而是先抓住了一个她称之为“非凡事实”且毫无争议的起点。 AI 资本开支的规模已经大到足以影响公开市场、芯片供应链以及整个创业公司的融资环境，因此这究竟是有实体支撑的长期投资还是投机性泡沫，已经不只是 AI 行业内部的问题。如果这些支出主要由少数几家巨头推动、而相应的回报迟迟无法兑现，那么一旦回调，受影响的将包括投资者、云服务与半导体厂商，以及大量依赖同一批资金流动的初创公司。 目前公开的摘录恰好在描述那个“毫无争议的事实”时被截断——即支出集中在“少数几家所谓的”某类主体身上——因此无法根据现有文本判断文章的具体论据与结论。这是一篇偏经济与战略层面的分析，而非技术深度剖析，读者不应期待看到基准测试、模型架构讨论或具体的工程细节。

rss · MIT Tech Review · Sep 15, 10:00

**背景**: 所谓“AI 基础设施热潮”，指的是为训练和运行大型 AI 模型而掀起的对数据中心、GPU、网络设备和电力容量的大规模投入，主要由少数几家超大规模云服务商和 AI 实验室主导。由于这笔开支如今已达到每年数千亿美元的规模，经济学家和投资者开始争论它究竟反映了真实而持久的需求，还是类似历史上技术狂热时期的投资泡沫。《麻省理工科技评论》是麻省理工学院旗下的老牌科技媒体，以面向技术与商业读者、通俗而扎实的分析著称。沃顿商学院的 Jessica Wachter 是一位金融学者，其研究常涉及资产定价与市场行为，因此她在讨论这一问题时更关注哪些部分可以视为既定事实、哪些仍属不确定。

**标签**: `#AI investment`, `#AI infrastructure`, `#economic bubble`, `#technology trends`, `#venture capital`

---

<a id="item-7"></a>
## [NVIDIA 宣布支持用 Rust 原生编写 CUDA GPU 内核](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 7.6/10

NVIDIA 在开发者博客上发布文章，宣布为 Rust 提供原生 CUDA 支持，可以用 Rust 编写 GPU 内核，并规划了两条不同的开发路线。该公告被定位为一次渐进式推进而非概念性突破，除两条路线的框架之外，文章本身给出的具体技术细节相当有限。 Rust 正稳步成为 AI 基础设施与推理工具领域的主流语言，因此 NVIDIA 的官方支持有望让 Rust 开发者更容易使用 GPU 算力，并减少对 C++/CUDA 绑定的依赖。同时，这也加剧了一场争论：厂商专属的 GPU 技术栈是否会损害可移植性，相比之下 DSL 与独立内核文件等更开放的做法是否更优。 这两条路线代表 Rust 与 CUDA 工具链集成的不同方式，而非单一统一的解决方案，但公告并未深入说明编译器内部机制、性能数据或稳定性保证。值得注意的是，至少有一位评论者指出，这次发布是“checked rather than trusted”（经过检查而非被信任），并认为这篇博客文章读起来像是大语言模型写的。

hackernews · nonmaskable · Sep 16, 11:15 · [社区讨论](https://news.ycombinator.com/item?id=49724881)

**背景**: CUDA 是 NVIDIA 专有的通用 GPU 计算平台与编程模型，传统上通过 C 和 C++ 使用。Rust 是一门以内存安全著称的系统编程语言，近年来在 AI 工具领域不断扩展，社区项目如 Rust CUDA Project 以及 NVlabs 的实验性编译器 cuda-oxide 已经在探索用纯 Rust 编写 SIMT 内核。与此同时，OpenAI 的 Triton 等 DSL 让开发者无需深入的 CUDA 经验就能用嵌入 Python 的语言写出高效 GPU 内核，而 HuggingFace 的 Candle 等框架则把模型推理带到了 Rust 生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rust-gpu.github.io/rust-cuda/">Introduction - The Rust CUDA Guide</a></li>
<li><a href="https://nvlabs.github.io/cuda-oxide/index.html">The cuda - oxide Book — cuda - oxide</a></li>
<li><a href="https://openai.com/index/triton/">Introducing Triton: Open-source GPU programming for neural networks | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧明显：jacobgorm 强烈批评 CUDA 的厂商锁定，认为正确的做法是把 GPU 当作另一台机器对待，将内核放在独立文件中并像 Metal、OpenCL、D3D12 那样手动启动，同时称赞 Triton 这类 DSL。也有人持更积极的态度——dllu 将这一消息与 HuggingFace 面向 Rust 推理的 Candle crate 联系起来，LarsDu88 表示正因大语言模型尚未学会这套新东西，反倒重新点燃了自己学习 Rust 的动力——此外 manyatoms 则询问它与 vectorware 相比如何。

**标签**: `#Rust`, `#GPU Programming`, `#CUDA`, `#AI Infrastructure`, `#Developer Tools`

---

<a id="item-8"></a>
## [利用零稀疏性将三值 LLM 压缩至 1.58 比特以下](https://arxiv.org/abs/2609.16338) ⭐️ 7.5/10

一篇新的 arXiv 论文（2609.16338）表明，三值 LLM 可以被压缩到每权重 1.58 比特这一理论下限以下，通过利用训练后权重约有 51%的时间恰好为零这一事实，达到约 1.48 比特。其技巧是使用一个存在位图来记录哪些权重非零，因此只需存储保留下来的三值。 它把本已极端的三值 LLM 压缩边界又向前推进了一步，这对希望在有限显存中装下大型量化模型的人，以及未来把三值运算固化到硬件中的定制芯片都很重要。如果三值模型最终真的进入专用芯片，这种低于 1.58 比特的打包方式可能在内存和能耗两方面带来惊人的效率。 这一收益是渐进的——每权重仅约 0.1 比特（从 1.58 降到约 1.48）——并且完全依赖于一个经验观察：实际的三值权重约有 51%的时间为零。当前方案依赖简单的存在位图而非熵编码，有评论者指出,算术编码还能再挤出零点几比特,代价是解码复杂度更高。

hackernews · matt_d · Sep 16, 20:59 · [社区讨论](https://news.ycombinator.com/item?id=49732931)

**背景**: 像 BitNet b1.58 这样的三值 LLM 只用三个值（-1、0、+1）表示每个权重，由于 log2(3)≈1.58，理论存储成本就是每权重 1.58 比特，这也是其名称的由来。由于很大一部分权重在量化后恰好为零，这一理论值忽略了零的冗余,而这正是本文所利用的地方。在这些极低位宽下,QuIP#、QTIP 以及像 LLVQ 这样的格基矢量量化方法构成主要的竞争路线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2402.17764">Paper page - The Era of 1- bit LLMs: All Large Language Models are in...</a></li>
<li><a href="https://arxiv.org/abs/2603.11021">[2603.11021] Leech Lattice Vector Quantization for Efficient LLM Compression</a></li>
<li><a href="https://www.researchgate.net/publication/331371330_The_State_of_Sparsity_in_Deep_Neural_Networks">(PDF) The State of Sparsity in Deep Neural Networks</a></li>

</ul>
</details>

**社区讨论**: 评论者既感兴趣又看法不一：有人称赞这一巧妙的零稀疏技巧，并预测硬件实现的三值硅芯片将极为高效；也有人认为三值量化根本没有意义，在这种位宽下矢量量化和基于网格（trellis）的 PTQ 方法更好。其他人提出算术编码可以比存在位图走得更远，还有人指出,只有把信息熵考虑进来时,"1.58 比特"才比"1 个三进制位(trit)"更有意义。

**标签**: `#LLM quantization`, `#ternary LLMs`, `#model compression`, `#inference efficiency`, `#arxiv paper`

---

<a id="item-9"></a>
## [小米 MiMo 2.6 公开实时后训练 RL 仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 7.5/10

小米 MiMo 团队在 mimo.xiaomi.com/rl 上线了一个公开的实时仪表盘，直接从训练器日志中流式展示 mimo-v2.6-pro 与 mimo-v2.6-flash 两个强化学习训练任务的指标。该链接在 Hacker News 上获得了 203 分、55 条评论，工程师们在讨论中分享了对 MiMo-V2.5 与 V2.5-Pro 的实际使用体验，并与其他模型进行了对比。 在大模型行业里，公开实时训练遥测数据极为罕见，多数实验室都将后训练曲线、奖励信号和训练配置严格保密，因此这一举措让外部研究者和开发者得以罕见地观察一个具备竞争力的模型究竟是如何被优化的。这也进一步巩固了小米作为严肃开源模型竞争者的地位，有评论者甚至将其视为对正在筹备上市的闭源实验室商业模式的威胁。 据仪表盘页面说明，所展示的指标直接来自 pro 与 flash 两个强化学习任务的实时训练器日志。在 HN 讨论中，有评论者指出 MiMo-V2.5-Pro 在 DeepSWE 1.1 基准上仅得 19%，而 Fable 达到 70%、Kimi K3 为 69%、Astra 为 74%（均为最大努力设置）——这说明开发者的正面主观体验尚未在该软件工程基准上转化为顶尖分数。

hackernews · krackers · Sep 16, 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: 后训练（post-training）指大语言模型在完成初始大规模预训练之后所接受的训练阶段，通常包括监督微调或指令微调、基于偏好的对齐，以及近年来越来越多的、基于可验证结果的强化学习。强化学习后训练（RLHF/RLVR 一类方法）是把基座模型变成可用助手或编程智能体的关键环节，但其训练曲线通常被视为商业机密。DeepSWE 这类基准用于比较模型在软件工程任务上的表现，而实时仪表盘本质上是一种透明度产物，让公众能够实时观察这些曲线的变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/">mimo -v 2 . 6 RL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-training_of_large_language_models">Post-training of large language models</a></li>
<li><a href="https://mimo.mi.com/">Xiaomi MiMo Home</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏正面：一位软件工程师表示 MiMo-V2.5 性价比极高，在成本极低的情况下提供了接近 Anthropic 模型的质量，只是偶尔会陷入幻觉循环；另一位则把 V2.5-Pro 形容为一位能力不错但健忘、刚接手项目且不擅长多任务处理的资深工程师。多位评论者称赞该仪表盘的新意，并追问为何其他模型厂商不公开实时训练遥测数据；还有人打趣说，开源 AI 的进展对闭源实验室的 IPO 而言就像是看着一颗定时炸弹。

**标签**: `#LLM`, `#post-training`, `#reinforcement-learning`, `#open-source-ai`, `#model-evaluation`

---

<a id="item-10"></a>
## [Google 的 SIMD 向量化 vqsort 旧文重现，社区指出更新的 SOTA 排序算法](https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html) ⭐️ 7.5/10

Google 开源博客 2022 年的一篇文章介绍 vqsort——一种基于 SIMD「压缩存储（compress-store）」划分的向量化、性能可移植 Quicksort——近日重新出现在 Hacker News 上，评论者指出在 pdqsort、vqsort、glidesort 之后，当前的 state-of-the-art 已转向 driftsort 和 ipnsort。一位评论者还表示已通过 PR #106650 将这些更新的算法集成进 ClickHouse。 排序是数据库、查询引擎和系统软件中的基础原语，因此一个集成化、性能可移植的 SIMD 排序实现能够在无需针对各架构手工调优的情况下带来广泛加速。这场讨论同样重要，因为它为这篇 2022 年的文章补上了缺失的语境：读者现在能看到当前 SOTA 实现的线索，以及 ClickHouse 中的一项实际生产集成。 vqsort 的关键技巧在于，现代指令集（Arm SVE、RISC-V V 和 x86 AVX-512）都提供了一条压缩存储指令：给定每个元素的 yes/no 掩码后，它只把被选中的元素写入连续内存，从而实现无分支的向量化划分。更新的替代实现在保证上有所不同：driftsort 是通用的、稳健的稳定排序，而 ipnsort 是通用的、稳健的不稳定排序，两者均出自 Orson Peters 和 Lukas Bergdoll 之手（ipnsort 的说明文档日期为 2024-04-16）。

hackernews · mococa · Sep 16, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=49731054)

**背景**: Quicksort 是经典的分治排序算法：围绕枢轴（pivot）划分元素并递归处理；pdqsort（pattern-defeating quicksort）是知名的现代改良版本，而 vqsort 是 Google 通过其 Highway 库提供的 SIMD 加速变体，用于实现可移植的向量化。SIMD 让一条指令同时处理多个数据元素，但过去每种 CPU 架构都需要各自的 intrinsic；所谓「性能可移植」指的是同一份实现能在运行时按需分派到 AVX-512、SVE 或 RISC-V V。driftsort 和 ipnsort 属于更晚的一条研究脉络（sort-research-rs），重点在于对对抗性或异常输入模式保持稳健。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/highway/blob/master/hwy/contrib/sort/vqsort.h">highway/hwy/contrib/ sort / vqsort .h at master · google/highway · GitHub</a></li>
<li><a href="https://github.com/Voultapher/driftsort">GitHub - Voultapher/ driftsort : Driftsort a fast, generic robust stable sort .</a></li>
<li><a href="https://github.com/Voultapher/sort-research-rs/blob/main/writeup/ipnsort_introduction/text.md">sort -research-rs/writeup/ ipnsort _introduction/text.md at main...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这篇文章已相当陈旧，真正的 state-of-the-art 已经转向 driftsort 和 ipnsort，并有人分享了一个将它们集成进 ClickHouse 的 PR；也有人希望标题中标注「(2022)」以消除误解，还有版主给出了 2022 年原始 Hacker News 讨论帖（142 条评论）的链接。另有一支轻松的讨论拿命名开玩笑，认为 mergesort 和 heapsort 的名字自解释其思路，而 Quicksort 只是以它唯一可取之处（快）来命名。

**标签**: `#algorithms`, `#sorting`, `#performance-engineering`, `#SIMD`, `#systems-programming`

---

<a id="item-11"></a>
## [Show HN：电子墨水画框听鸟鸣，并用 19 世纪插画风格绘制出来](https://github.com/arnegiacomo/fugleramme) ⭐️ 7.3/10

一个名为“fugleramme”（挪威语意为“鸟框”）的创客项目登上了 Show HN：装在相框里的电子墨水屏通过麦克风监听鸟鸣，识别出鸟的种类，然后在屏幕上以 19 世纪风格的插画形式把这只鸟画出来。项目代码与搭建细节发布在 GitHub 仓库 github.com/arnegiacomo/fugleramme 上。 它生动地说明：廉价的嵌入式硬件配合一个开源的应用型机器学习模型，可以做成低功耗的环境装置，而不必是又一款屏幕应用；同时也表明实用的机器学习并不一定需要大语言模型。项目的热度反映出人们对“安静、只做一件事”的魔法小玩意越来越感兴趣，这类设备靠电池就能运行数月甚至数年。 其背后的声音分类器是 BirdNET——一个传统的卷积神经网络（并非大语言模型），据康奈尔大学实验室的资料，它能从音频中识别超过 6000 种鸟类。硬件方面，电子墨水屏只在刷新画面时耗电，因此社区成员反馈说，由 BLE 或 ESP32 驱动的墨水屏即使每天刷新多次，靠一块 2000mAh 电池也能用上好几年。

hackernews · arnemunthekaas · Sep 15, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是由康奈尔大学鸟类学实验室与开姆尼茨工业大学开发的开源声音识别系统，它把深度学习应用于录音的声谱图，从而输出可能的鸟种，被广泛用于生物多样性监测和公民科学。电子墨水（e-paper）屏通过移动带电颜料颗粒来成像，因此能在断电后长期保持画面、观感如同印刷纸张。这个项目正好位于两者的交汇处，又叠加了一层插画生成或预渲染处理，让识别出的鸟以版画而非照片或文字的形式呈现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://connormwood.com/wp-content/uploads/2023/11/sossover-etal-2023-birdnet-for-wolves-and-coyotes.pdf">Using the BirdNET algorithm to identify wolves, coyotes, and...</a></li>
<li><a href="https://techglimmer.io/what-is-e-ink-display-technology-e-ink-technology/">What Is E Ink Display Technology ? How It Works & Why It Matters</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应非常热烈，有评论者称这是近期在该站看到的最酷的东西，也是作为创作者所能获得的最大灵感来源。也有人补充了技术细节：BirdNET 是传统神经网络而非大语言模型；通过 BLE 驱动的墨水屏一次充电可用一年以上，而依赖 Wi-Fi 的方案则不行。评论者还提到近期涌现的一批鸟类相关项目（如 birdnet-go），并开玩笑说“以鸟类为载体的 IP 协议”终于要实现了。

---

<a id="item-12"></a>
## [Mozilla 与 Mistral 为 Firefox 引入 AI 浏览，引发本地与云端推理之争](https://mistral.ai/news/mistral-x-mozilla/) ⭐️ 7.0/10

Mozilla 与 Mistral AI 宣布达成合作，将 AI 驱动的浏览功能引入 Firefox，包括上下文感知搜索、网页摘要以及跨浏览器标签页的记忆检索。该功能已在法国和北美上线，计划今年晚些时候登陆英国和德国，官方称其基于零数据留存政策，对话内容不会被保存。 这是欧洲前沿模型首次大规模集成进主流浏览器之一，使 Firefox 与内置 Gemini Nano 的 Chrome 形成直接对位，并将隐私作为核心卖点。究竟采用端侧推理还是上传云端，将决定数以亿计浏览器用户敏感浏览数据的处理方式，也可能为其他厂商树立先例。 公告文案并未清楚区分本地推理与云端推理，也没有明确说明后者需要用户主动同意，批评者认为这连最基本的伦理底线都没达到；所谓零数据留存政策仍然要求用户信任 Mozilla 及其合作方会遵守合同与技术承诺，而终端用户无法独立验证这一点。

hackernews · vertigoruntime · Sep 16, 08:08 · [社区讨论](https://news.ycombinator.com/item?id=49723408)

**背景**: Mozilla 开发了 Firefox，它是少数不由广告驱动型平台控制的主流浏览器之一，长期以隐私保护为卖点。Mistral AI 是一家 2023 年成立的法国大模型公司，估值超过 140 亿美元，为欧洲 AI 企业之最，也是欧盟数字主权倡议的主要受益者。本地推理指模型直接在用户设备上运行，无需把数据发往远程服务器，隐私性更好但模型规模和能力受限；云端推理则可运行更大的模型，代价是必须上传用户数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mistral_AI">Mistral AI</a></li>
<li><a href="https://grokipedia.com/page/Local_inference">Local inference</a></li>
<li><a href="https://www.baseten.co/inference-engineering/book/03-hardware/local-inference/">Local Inference | Inference Engineering</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论以批评为主：有人指出这本是小模型本地推理的理想场景，并指责营销页面没有坦诚说明云端推理需要用户同意；另一位评论者认为 Firefox 的云端推理仍然要求用户给予一种无法验证的信任。也有人提出具体改进思路，例如在浏览器内置一个微型模型，把冗长的自然语言查询改写成高级搜索运算符，同时指出该功能大体上只是在重复 Chrome 已通过 Gemini Nano 提供的能力。

**标签**: `#AI`, `#browser`, `#privacy`, `#local-inference`, `#Mozilla-Mistral`

---

<a id="item-13"></a>
## [Ben Thompson：ChatGPT 广告行之有效，并解决亚马逊聊天机器人的难题](https://stratechery.com/2026/openai-ads-amazon-ads-in-chatgpt-walmart-to-accept-apple-pay/) ⭐️ 7.0/10

在 Stratechery 的一篇文章中，分析师 Ben Thompson 认为 ChatGPT 内的广告模式行之有效，并且这一模式恰好解决了亚马逊在聊天机器人上最大的难题；同一篇文章还提到沃尔玛最终将接受 Apple Pay。该文将这两件事都视为大型现有企业与挑战者向同一套变现与支付打法靠拢的例证。 这一观点的意义在于，它把 AI 助手内的广告从“损害产品体验的妥协”重新定义为让聊天机器人得以免费且大规模普及的经济基础，而这正是每一家为推理成本烧钱的 AI 公司都必须回答的问题。它同时暗示亚马逊 Rufus 式助手已有清晰的变现路径，也说明即便对最大的零售商而言，长期抵制 Apple Pay 这类既有支付标准也是徒劳的。 该条目本身只有两句话的摘要，因此 Stratechery 原文的完整论证并未在此呈现；相关背景包括 OpenAI 表示广告有助于扩大 ChatGPT 的使用范围且不改变产品运作方式、ChatGPT 提供 CPM 与 CPC 两种广告计费模式，以及有报道称亚马逊 Rufus 的赞助提示目前带来的广告量仅为传统站内广告的一小部分。

rss · Stratechery · Sep 15, 10:00

**背景**: Stratechery 是 Ben Thompson 主笔、读者众多的科技战略通讯，以用于分析平台型企业的“聚合理论”（Aggregation Theory）框架闻名。ChatGPT 广告指 OpenAI 在其聊天机器人中投放的广告，OpenAI 表示其目的是支持更广泛的使用与持续投入，而不改变 ChatGPT 的运作方式。亚马逊的 Rufus 是该零售商的站内 AI 购物助手，如今会在对话中展示被称为“SP Prompts”的赞助商品，这些提示由商品列表内容与广告活动数据自动生成。沃尔玛多年来一直是 NFC 移动支付的知名抵制者，曾支持由商户主导、于 2015 年终止的 MCX/CurrentC 联盟，因此其接受 Apple Pay 意味着这一长期抵抗的终结。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001047-ads-in-chatgpt">Ads in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://www.emarketer.com/content/rufus-ads-open-window-amazon-s-ai-while-missing-some-shoppers">Rufus ads open a window into Amazon ’s AI—while missing some...</a></li>
<li><a href="https://www.adexchanger.com/commerce-roundup/how-advertisers-can-and-cannot-get-in-front-of-chatbot-shoppers/?trk=article-ssr-frontend-pulse_little-text-block">How Advertisers Can – And Cannot – Get In Front Of Chatbot ...</a></li>

</ul>
</details>

**标签**: `#AI business models`, `#ChatGPT`, `#advertising`, `#big tech strategy`, `#Apple Pay`

---