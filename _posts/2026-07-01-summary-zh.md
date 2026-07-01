---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> From 116 items, 28 important content pieces were selected

---

1. [Llama 负责人转战药物发现，推动扩散模型应用](#item-1) ⭐️ 9.6/10
2. [ScarfBench：为 AI 智能体在企业 Java 迁移中设定基准](#item-2) ⭐️ 9.2/10
3. [Box3D：Erin Catto 宣布开源 3D 物理引擎](#item-3) ⭐️ 9.1/10
4. [核心转储流行病学：修复一个 18 年历史的老 bug](#item-4) ⭐️ 9.0/10
5. [Cursor 通过前线部署工程师部署 AI 智能体](#item-5) ⭐️ 9.0/10
6. [初创公司瞄准大模型输出多样性不足问题](#item-6) ⭐️ 8.9/10
7. [AI 模型专业化为何不可避免](#item-7) ⭐️ 8.8/10
8. [shot-scraper video: 代理通过 storyboard.yml 录制演示视频](#item-8) ⭐️ 8.5/10
9. [Hugging Face 与 Cerebras 联合推出 Gemma 4 语音 AI](#item-9) ⭐️ 8.5/10
10. [Ahmad Osman：本地 AI 正快速追赶上云](#item-10) ⭐️ 8.5/10
11. [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](#item-11) ⭐️ 8.4/10
12. [内燃机交互式深度解析](#item-12) ⭐️ 8.2/10
13. [Claude Sonnet 5：接近 Opus 性能但价格更低](#item-13) ⭐️ 8.2/10
14. [Hugging Face 在模型页面集成社区评测结果](#item-14) ⭐️ 8.2/10
15. [Anthropic 发布 Claude Fable 5，引发安全担忧](#item-15) ⭐️ 8.1/10
16. [FFmpeg 9.1 引入新 AAC 编码器，提升质量](#item-16) ⭐️ 8.0/10
17. [乐观提供：IPFS 内容发布提速 10 倍](#item-17) ⭐️ 7.9/10
18. [Claude Code v2.1.196：增强安全、默认模型与错误修复](#item-18) ⭐️ 7.8/10
19. [首个从头构建的合成细胞能生长分裂](#item-19) ⭐️ 7.8/10
20. [Cloudflare x402 协议实现资源访问的微支付](#item-20) ⭐️ 7.8/10
21. [Anthropic 推出 Claude Science 用于自主科学研究](#item-21) ⭐️ 7.5/10
22. [AI 同事与太阳能平流层互联网](#item-22) ⭐️ 7.5/10
23. [Dario Amodei：AI 开源是伪命题](#item-23) ⭐️ 7.5/10
24. [Claude Code v2.1.198 发布：新增 Chrome 通用版本和代理通知](#item-24) ⭐️ 7.3/10
25. [AI 时代产品工程师与现场部署工程师的融合](#item-25) ⭐️ 7.2/10
26. [图形编程学习路径指南](#item-26) ⭐️ 7.1/10
27. [Warp CEO 展望自动化软件工厂](#item-27) ⭐️ 7.0/10
28. [AIEWF 亮点：循环、软件工厂与开放模型](#item-28) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Llama 负责人转战药物发现，推动扩散模型应用](https://www.latent.space/p/the-coolest-diffusion-research-isnt) ⭐️ 9.6/10

Evan Feinberg 和 Sergey Edunov 在 Latent Space 的访谈中讨论了 PEARL 在 OpenBind 基准测试中的零样本成功以及共折叠模型在药物发现中的潜力。 这标志着顶尖 AI 研究人员从大语言模型转向科学领域的增长趋势，而扩散模型可能通过准确预测蛋白质-配体相互作用来革新药物发现。 PEARL 在 OpenBind（一个用于药物-蛋白质相互作用的大规模开放数据集）上取得了最先进的零样本结果，而共折叠模型正逼近实际应用所需的准确度阈值。

rss · Latent Space · Jul 1, 14:42

**背景**: 扩散模型是一种生成式 AI 模型，学习去噪数据，越来越多地应用于药物发现的分子结构。OpenBind 是一个开放获取的药物-蛋白质相互作用数据集，专为 AI 基准测试设计。共折叠模型预测小分子与蛋白质如何共同折叠，这是计算药物设计中的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openbind.uk/">Home | openbind .uk</a></li>
<li><a href="https://bioengineer.org/openbinds-inaugural-data-and-model-release-sets-a-new-benchmark-in-ai-driven-drug-discovery/">OpenBind ’s Inaugural Data and Model Release Sets a New...</a></li>
<li><a href="https://www.understandingai.org/p/an-unlikely-ally-for-open-source">An unlikely ally for open-source protein - folding models : Big Pharma</a></li>

</ul>
</details>

**标签**: `#AI`, `#Diffusion Models`, `#Drug Discovery`, `#LLMs`, `#Scientific Computing`

---

<a id="item-2"></a>
## [ScarfBench：为 AI 智能体在企业 Java 迁移中设定基准](https://huggingface.co/blog/ibm-research/scarfbench) ⭐️ 9.2/10

IBM Research 推出了 ScarfBench，这是一个用于评估 AI 智能体在企业 Java 应用跨 Jakarta EE、Quarkus 和 Spring 框架迁移能力的基准套件。它不比较生成的代码与参考实现，而是测试迁移后的应用能否构建、部署并保持功能完整性。 企业软件现代化通常需要迁移遗留 Java 框架，这是一项复杂任务，现有 AI 智能体仍难以胜任。ScarfBench 提供了一个严谨、实用的基准，推动自动化代码迁移的进步，可能加速企业对 AI 辅助重构的采纳。 ScarfBench 包含基于 JSR 企业 Java 分类法的应用，并由专家创建了 Spring、Jakarta EE 和 Quarkus 下的迁移版本。对最先进的编码智能体的评估显示，尽管它们在传统软件工程基准上表现出色，框架迁移仍然困难。

rss · Hugging Face Blog · Jun 30, 18:32

**背景**: 遗留企业 Java 应用通常运行在较旧的框架（如 Java EE）或专有栈上。将它们现代化到 Spring Boot 或 Quarkus 等框架可以提升性能、可扩展性和可维护性。AI 智能体在代码生成方面展现了潜力，但对于涉及深度重构和架构变更的复杂迁移任务，缺乏评估标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-research/scarfbench">ScarfBench: Benchmarking AI Agents for Enterprise Java Framework Migration</a></li>
<li><a href="https://ibm.github.io/scarfbench/benchmark/">Benchmark · ScarfBench</a></li>
<li><a href="https://www.ibm.com/new/announcements/scarfbench-a-public-benchmark-for-java-framework-migration">ScarfBench: A public benchmark for java framework migration | IBM</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark`, `#Java`, `#enterprise migration`, `#software engineering`

---

<a id="item-3"></a>
## [Box3D：Erin Catto 宣布开源 3D 物理引擎](https://box2d.org/posts/2026/06/announcing-box3d/) ⭐️ 9.1/10

广受欢迎的 Box2D 物理引擎的创建者 Erin Catto 宣布了 Box3D，这是一个新的开源 3D 物理引擎，将 Box2D 的原理扩展到了三维空间。 Box3D 的重要性在于它将使 Box2D 成为 2D 游戏开发和强化学习环境标准的强大、确定性物理模拟带到了 3D 领域，可能对游戏开发、仿真和机器学习研究产生影响。 Box3D 是开源的，专注于刚体动力学，并建立在 Box2D 的遗产之上。该引擎旨在提供稳健且确定性的物理模拟，这对于网络游戏和可重复的机器学习环境等应用至关重要。

hackernews · makepanic · Jul 1, 12:12 · [社区讨论](https://news.ycombinator.com/item?id=48745445)

**背景**: Box2D 是由 Erin Catto 创建的流行二维物理引擎，广泛应用于《愤怒的小鸟》等游戏以及 OpenAI Gym 的 Lunar Lander 等强化学习基准测试中。物理引擎模拟刚体动力学，包括碰撞检测和解决，对于游戏和仿真中的真实交互至关重要。

**社区讨论**: 社区对 Box3D 表示兴奋，许多人回忆起 Box2D 对独立游戏和机器学习研究的影响。一些用户提出了确定性对于网络游戏的重要性，而另一些用户则强调了物理模拟的复杂性，特别是在碰撞检测和求解器调优方面。

**标签**: `#physics engine`, `#open source`, `#game development`, `#simulation`, `#rigid body dynamics`

---

<a id="item-4"></a>
## [核心转储流行病学：修复一个 18 年历史的老 bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 9.0/10

OpenAI 工程师应用大规模核心转储分析来诊断罕见的基础设施崩溃，发现了一个硬件故障和一个存在 18 年的软件 bug。 这项工作展示了一种系统性的方法论，用于调试那些可能悄无声息地降低可靠性多年的难以捉摸的基础设施问题。它强调了大规模保留和分析核心转储以捕获潜在 bug 的价值。 该 bug 在代码库中存在了 18 年才被修复。分析过程涉及关联基础设施中数千个核心转储以识别模式。

rss · OpenAI Blog · Jun 30, 00:00

**背景**: 核心转储是包含进程崩溃时内存快照的文件，常用于事后调试。在大规模系统中，收集和分析来自许多机器的核心转储可以揭示难以在本地重现的系统性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Core_dump">Core dump - Wikipedia</a></li>
<li><a href="https://sergioprado.blog/linux-core-dump-analysis/">Linux core dump analysis - sergioprado.blog</a></li>

</ul>
</details>

**标签**: `#infrastructure`, `#debugging`, `#core dump`, `#software engineering`, `#OpenAI`

---

<a id="item-5"></a>
## [Cursor 通过前线部署工程师部署 AI 智能体](https://www.latent.space/p/cursor-forward-deployed-engineers) ⭐️ 9.0/10

Cursor 的 Pauline Brunet 在 Latent Space 上解释了其前线部署工程师团队如何帮助企业建立软件工厂来实现 AI 智能体。 这种方法通过提供实际的部署支持，可能加速企业采用 AI 智能体，类似于 Palantir 以及现在 OpenAI 和 Anthropic 使用的 FDE 模式。 软件工厂的概念涉及建立一个智能体原生的端到端系统，自动化编码、测试和部署，旨在超越单个工程师效率，提升整个组织的生产力。

rss · Latent Space · Jul 1, 19:03

**背景**: 前线部署工程师（FDE）是直接与企业客户合作部署和集成软件解决方案的专家。该模式在 Palantir 变得突出，现在被 AI 公司采用以帮助客户实施复杂的 AI 系统。“软件工厂”一词指的是一个由 AI 智能体组成的互联系统，自动化软件开发生命周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/openai-forward-deployed-engineers-accelerate-ai-projects-2025-7">OpenAI Deploys Engineers to Accelerate AI... - Business Insider</a></li>
<li><a href="https://factory.ai/news/software-factory">Factory 2.0: From coding agents to software factories | Factory.ai</a></li>
<li><a href="https://www.kore1.com/forward-deployed-engineer/">What Is a Forward Deployed Engineer ? Role & Salary - KORE1</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise`, `#agentic systems`, `#engineering`, `#Cursor`

---

<a id="item-6"></a>
## [初创公司瞄准大模型输出多样性不足问题](https://www.technologyreview.com/2026/07/01/1140003/llms-are-stuck-in-a-groupthink-rut-this-startup-is-trying-to-get-them-out/) ⭐️ 8.9/10

一家初创公司正在开发方法，鼓励大语言模型输出更多样的结果，摆脱总是选择数字 7 这类刻板回答。文章指出当前大模型常产生相似、可预测的输出，并探讨了这家初创公司增强多样性的方法。 这一点很重要，因为大模型趋向于同质化输出会限制创造力、强化偏见并降低用户信任。如果成功，该初创公司的技术能使大模型在创造性任务中更有用，减少人口统计学偏见，并提升 AI 生成内容的整体质量。 文章使用一个简单提示——'给我一个 1 到 10 之间的随机数'——来展示大模型几乎总是先输出 7，然后是 3 或 4，接着是 8 或 9。该初创公司的解决方案可能涉及新颖的采样策略或微调方法来打破这类模式。

rss · MIT Tech Review · Jul 1, 14:35

**背景**: 大语言模型通过基于概率分布预测下一个标记来生成文本。温度、top-k 和 top-p 等采样技术控制输出的确定性与随机性程度。然而，由于训练数据的同质化，模型往往偏向高概率标记，导致回复重复且刻板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@shashankag14/understanding-sampling-techniques-in-large-language-models-llms-dfc28b93f518">Sampling Techniques in Large Language Models (LLMs) | by Shashank Agarwal | Medium</a></li>
<li><a href="https://gist.github.com/kalomaze/4473f3f975ff5e5fade06e632498f73e">LLM Samplers Explained · GitHub</a></li>
<li><a href="https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.47/134150/Benchmarking-Linguistic-Diversity-of-Large">Benchmarking Linguistic Diversity of Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI diversity`, `#model behavior`, `#startup`, `#sampling`

---

<a id="item-7"></a>
## [AI 模型专业化为何不可避免](https://huggingface.co/blog/Dharma-AI/why-specialization-is-inevitable) ⭐️ 8.8/10

一篇新的博客文章认为，由于领域特定 AI 模型在效率和性能上优于通用模型，其出现是不可避免的。 这一转变可能重塑 AI 行业，优先考虑针对特定任务的专门化模型，有可能在医疗、金融、法律等领域降低成本并提高准确性。 该文章可能讨论了通用大型语言模型（LLM）与微调或定制的领域特定模型之间的权衡，强调专业化能带来更好的资源利用率和任务性能。

rss · Hugging Face Blog · Jun 30, 14:39

**背景**: 像 GPT-4 这样的通用 AI 模型旨在处理广泛的任务，但通常需要巨大的计算资源，并且在专业任务上可能表现不佳。相比之下，专门化模型在领域特定数据上训练或微调，使其在针对性应用中更高效、更准确。

**标签**: `#AI`, `#LLM`, `#specialization`, `#domain-specific models`, `#machine learning`

---

<a id="item-8"></a>
## [shot-scraper video: 代理通过 storyboard.yml 录制演示视频](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.5/10

Simon Willison 发布了 shot-scraper 1.10，新增了 `shot-scraper video` 命令，该命令使用 Playwright 根据 storyboard.yml 文件中定义的操作流程录制 Web 应用的演示视频。 这使 AI 编码代理能够自动生成工作成果的视频演示，有助于验证和沟通代理驱动的变更。 storyboard.yml 定义了服务器启动、URL、视口、光标可见性、等待条件以及一系列包含点击和暂停等操作的场景，通过 cookie JSON 文件进行身份验证。

rss · Simon Willison · Jun 30, 16:54

**背景**: shot-scraper 是 Simon Willison 开发的命令行工具，基于 Playwright 用于自动截图网站。新的 video 命令扩展了该工具以录制视频，特别适合代理以可复现的方式展示其工作成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A command-line utility for taking...</a></li>
<li><a href="https://datasette.io/tools/shot-scraper">shot - scraper - a tool for Datasette</a></li>
<li><a href="https://simonwillison.net/2022/Mar/10/shot-scraper/">shot - scraper : automated screenshots for documentation, built on...</a></li>

</ul>
</details>

**标签**: `#dev tools`, `#agentic systems`, `#video recording`, `#playwright`, `#shot-scraper`

---

<a id="item-9"></a>
## [Hugging Face 与 Cerebras 联合推出 Gemma 4 语音 AI](https://huggingface.co/blog/cerebras-gemma4-voice-ai) ⭐️ 8.5/10

Hugging Face 与 Cerebras 正将 Google 的 Gemma 4 开放模型部署在 Cerebras 晶圆级处理器上，以实现低延迟的实时语音 AI 应用。 此次合作将强大的开放模型与专用硬件相结合，有望推动实时语音 AI 的普及，并减少推理任务对 GPU 的依赖。 Gemma 4 是 Google DeepMind 推出的开放模型系列，专为推理和智能体工作流优化；Cerebras 的晶圆级引擎硅片面积比 GPU 大 58 倍。该集成瞄准对毫秒级延迟至关重要的语音 AI 场景。

rss · Hugging Face Blog · Jul 1, 00:00

**背景**: Gemma 4 是 Google DeepMind 发布的开放权重模型系列，专为高级推理和智能体任务设计，提供多种架构。Cerebras Systems 生产的晶圆级引擎（WSE）是全球最大的 AI 处理器，面积是典型 GPU 的 58 倍，专为超高速 AI 计算优化。实时语音 AI 需要极低的延迟才能实现自然对话，而传统 GPU 集群在大规模部署时可能难以达到这一要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>
<li><a href="https://www.cerebras.ai/chip">Product - Chip - Cerebras</a></li>

</ul>
</details>

**标签**: `#AI`, `#voice AI`, `#Gemma 4`, `#inference`, `#Hugging Face`

---

<a id="item-10"></a>
## [Ahmad Osman：本地 AI 正快速追赶上云](https://www.latent.space/p/ahmad-osman-local-ai) ⭐️ 8.5/10

在 AI 工程师世界博览会 2025 研讨会后的一次演讲中，Ahmad Osman 提出，本地 AI 在笔记本电脑、手机和企业级基础设施上正快速进步，挑战着云端 AI 的主导地位。 这很重要，因为本地 AI 推理能降低延迟、提升隐私性并减少成本，可能重塑 AI 在消费和企业环境中的部署方式，并减少对云提供商的依赖。 Osman 的论点基于 AIEWF 研讨会的观察，实际演示显示本地 AI 模型在特定任务中达到或超过了云端性能，但边缘设备的可扩展性和模型大小仍然是挑战。

rss · Latent Space · Jun 30, 23:39

**背景**: 本地 AI 是指在笔记本电脑、手机或本地服务器等设备上直接运行 AI 模型，而非将数据发送到云端。传统上，这种方法受到硬件限制，但模型压缩、高效架构和专用芯片（如 Apple Neural Engine、Qualcomm AI Engine）的进步正在缩小差距。AI 工程师世界博览会（AIEWF）是一个专注于实用 AI 工程的会议，包括图智能等主题的研讨会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/playlist?list=PLcfpQ4tk2k0W3ORTR-Cr4Ppw6UrN8kfMh">AIEWF 2025 Complete Playlist - YouTube</a></li>

</ul>
</details>

**标签**: `#local AI`, `#inference`, `#edge computing`, `#AI infrastructure`

---

<a id="item-11"></a>
## [OpenAI 推出基因组学 AI 基准 GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) ⭐️ 8.4/10

OpenAI 宣布推出 GeneBench-Pro，这是一个利用复杂真实世界数据集评估 AI 在基因组学和生物学领域表现的新基准。该基准专注于多阶段统计推理和真实的科学分析。 该基准通过测试 AI 处理混乱真实数据和决策的能力，超越了简单的知识检索或单任务流水线，提高了生物学 AI 评估的标准。它可能加速基因组学和转化生物医学领域的 AI 驱动发现。 GeneBench-Pro 旨在评估多阶段统计推理，要求 AI 代理处理生物数据、选择分析路径并做出判断。它基于早期的 GeneBench 工作，并在 bioRxiv 预印本中有详细说明。

rss · OpenAI Blog · Jun 30, 00:00

**背景**: 传统的生物学基准主要关注知识检索或执行常规流程。GeneBench-Pro 满足了对 AI 在复杂、多步骤科学工作流（模仿真实研究，包括处理杂乱数据和做出战略决策）上进行评估的需求。这是科学领域更现实的 AI 评估趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.06.29.735386v2">GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine | bioRxiv</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmark`, `#genomics`, `#biology`, `#OpenAI`

---

<a id="item-12"></a>
## [内燃机交互式深度解析](https://ciechanow.ski/internal-combustion-engine/) ⭐️ 8.2/10

这篇互动文章通过动画图示和清晰文字，详细讲解了内燃机的机械原理和历史演变。 尽管内燃机已是成熟技术，但这篇文章为工程师、学生和爱好者提供了易读且全面的资源，弥合了理论知识与实际理解之间的差距。 文章涵盖了发动机循环、配气机构、润滑和燃油系统，并指出现代控制系统已显著进化，而基本机械设计变化不大。

hackernews · StefanBatory · Jul 1, 13:04 · [社区讨论](https://news.ycombinator.com/item?id=48746076)

**背景**: 内燃机通过受控爆炸将燃料的化学能转化为机械功。尽管它在车辆中几乎普及，但其运动部件的复杂交互常常被误解。本文通过交互式 3D 图示揭示了其原理。

**社区讨论**: 评论者赞赏文章的清晰度和深度，有人指出控制系统比机械设计变化更大。一位读者回忆了推杆式 V8 发动机的优雅，另一位则评论说示例中缺少了现代排放控制硬件。

**标签**: `#internal combustion engine`, `#mechanical engineering`, `#interactive article`, `#technical explanation`, `#hardware`

---

<a id="item-13"></a>
## [Claude Sonnet 5：接近 Opus 性能但价格更低](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.2/10

Anthropic 于 2026 年 6 月 30 日发布了 Claude Sonnet 5，其性能接近 Opus 4.8 但价格更低，并采用了新的分词器，使得英文文本的 token 数量增加约 30%。 此次发布提供了一个成本更低的 Opus 级性能替代方案，可能使先进 AI 更易获取。然而，新分词器实际上使价格提高了 30%，可能会影响预算敏感的开发者。 主要变化包括移除了 temperature、top_p 和 top_k 采样参数；支持 100 万 token 的上下文窗口和 12.8 万 token 的最大输出；自适应思考默认启用。定价与 Sonnet 4.6 相同（每百万输入/输出 token 分别为 3 美元/15 美元），并在 8 月 31 日前提供优惠，但新分词器使英文文本的实际价格增加了 30%。

rss · Simon Willison · Jun 30, 21:23

**背景**: Anthropic 的 Claude 模型家族包括多个层级：Sonnet（中端）、Opus（高端）以及更强大的 Mythos 和 Fable 模型，后者因安全隐患未公开发布。系统卡是一份详细说明模型能力和安全评估的文件，常用于获取监管批准。分词器将文本转换为模型处理的 token；新的分词器对相同输入生成更多 token，实际增加了成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Claude`, `#Anthropic`, `#model release`

---

<a id="item-14"></a>
## [Hugging Face 在模型页面集成社区评测结果](https://huggingface.co/blog/eee-community-evals) ⭐️ 8.2/10

Hugging Face 现在直接将社区提交的评测结果显示在模型页面上，采用 Every Eval Ever (EEE) 框架来标准化分数。这一集成使用户可以一目了然地看到来自社区的基准性能。 这使得性能基准更易获取和透明，减少了对分散排行榜的依赖。它赋能 AI 社区协作评估模型，并促进了开放基准测试的文化。 评测分数以 YAML 文件形式存储在模型仓库的 .eval_results/ 目录下，仅需基准数据集、任务和值三个字段。结果可通过 Pull Request 提交，并标记为社区提供。

rss · Hugging Face Blog · Jun 30, 00:00

**背景**: Every Eval Ever (EEE) 是一个共享框架和众包 AI 评测结果仓库，以统一的 JSON 文档标准化评测结果的表示。此前 Hugging Face 模型页面缺少集成的社区评测数据，用户需要查看外部排行榜。此次集成将 EEE 分数直接带到模型页面，提升了可发现性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/eee-community-evals">Featuring Every Eval Ever Results on Hugging Face Model Pages</a></li>
<li><a href="https://huggingface.co/docs/hub/eval-results">Evaluation Results · Hugging Face</a></li>

</ul>
</details>

**标签**: `#huggingface`, `#model evaluation`, `#community evals`, `#LLMs`, `#AI tools`

---

<a id="item-15"></a>
## [Anthropic 发布 Claude Fable 5，引发安全担忧](https://twitter.com/claudeai/status/2072402636813607381) ⭐️ 8.1/10

Anthropic 发布了 Claude Fable 5，这是一个在软件工程、知识工作、视觉和科学研究等领域表现卓越的最先进 AI 模型。该模型现已普遍可用，但其安全限制和潜在的权重泄露风险引发了争议。 此次发布重新引发了关于 AI 安全、信任以及能力与限制之间平衡的讨论。用户和批评者警告称，该模型的安全措施可能使其实用性降低，而分布式数据中心中权重泄露的风险则构成了严重的安全威胁。 Claude Fable 5 被描述为迄今为止最智能的 Fable 模型，在编程、代理和企业工作流方面表现出色。然而，社区评论显示，该模型的安全限制使其在某些任务上“糟糕透顶”，用户对美国模型的信任度提出质疑。

hackernews · mfiguiere · Jul 1, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=48752030)

**背景**: AI 模型权重是决定模型行为的核心参数。泄露这些权重可能使对手绕过安全措施或将模型用于恶意目的。Anthropic 的 Fable 5 分布在多个数据中心，引发了关于未授权访问的担忧。该公司历来强调末日场景，一些人认为这削弱了信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://ai.azure.com/catalog/models/claude-fable-5">AI Model Catalog | Microsoft Foundry Models</a></li>

</ul>
</details>

**社区讨论**: 评论者对严格的安全限制和权重泄露风险表示不信任。一位用户指出该模型将一本关于人类意识的书标记为有问题，称其“无用”。另一位警告说，对美国模型的信任侵蚀可能引发军备竞赛。一些人计划在切换到替代方案之前，从免费层中提取最大价值。

**标签**: `#AI safety`, `#model security`, `#trust`, `#LLM`, `#Anthropic`

---

<a id="item-16"></a>
## [FFmpeg 9.1 引入新 AAC 编码器，提升质量](https://hydrogenaudio.org/index.php/topic,129691.0.html) ⭐️ 8.0/10

FFmpeg 9.1 推出了一款新的原生 AAC 编码器，相比旧编码器大幅提升了音频质量，解决了长期存在的如啁啾声等伪影问题。 此次更新惠及依赖 FFmpeg 进行音频编码的开发者和内容创作者，提供了苹果 Core Audio 等第三方编码器的可行替代方案。同时，它重新引发了关于编解码器选择的讨论，Opus 在基准测试中仍优于 AAC。 该编码器主要针对 48 kHz 音频进行了优化，但也支持其他采样率。它包含了对 FFmpeg AAC 解码器中立体声 PNS bug 的变通方案，该 bug 多年来一直未被发现。

hackernews · ledoge · Jul 1, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48747116)

**背景**: AAC（高级音频编码）是一种广泛使用的有损音频格式，但 FFmpeg 的原生 AAC 编码器历来质量较差，会出现啁啾声等伪影。Opus 是一种现代开源编解码器，以低比特率下的卓越质量和低延迟著称。HydrogenAudio 社区定期进行听力测试以评估编解码器质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.hydrogenaudio.org/index.php?title=Opus">Opus - Hydrogenaudio Knowledgebase</a></li>
<li><a href="https://en.wikipedia.org/wiki/Opus_(audio_codec)">Opus (audio codec)</a></li>
<li><a href="https://opus-codec.org/">Opus Codec</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Opus 在基准测试中的表现，有人表示它在 64 kbps 下“将所有的 AAC 编码器远远甩在身后”。其他人对新编码器的实际性能表示好奇，指出 FFmpeg 之前的编码器通常需要用苹果 Core Audio 替换。技术讨论还涉及音频质量的主观性以及一个长期存在的 PNS 解码器 bug 的发现。

**标签**: `#FFmpeg`, `#AAC encoder`, `#audio codec`, `#Opus`, `#software development`

---

<a id="item-17"></a>
## [乐观提供：IPFS 内容发布提速 10 倍](https://probelab.io/blog/optimistic-provide/) ⭐️ 7.9/10

ProbeLab 推出了乐观提供（Optimistic Provide）优化，通过异步处理 DHT provide 操作而不是等待所有对等节点的确认，使 IPFS 内容发布速度提升超过 10 倍。 这一优化消除了 IPFS 的主要性能瓶颈，使得去中心化内容发布对延迟敏感的应用变得可行，并显著改善了用户体验。 乐观提供为北美和欧洲 90% 的请求实现了亚秒级的 PUT 操作，网络开销降低超过 40%，且完全向后兼容；该优化已在 Kubo 0.39.0 中默认启用。

hackernews · dennis-tra · Jul 1, 15:30 · [社区讨论](https://news.ycombinator.com/item?id=48748518)

**背景**: IPFS 使用分布式哈希表（DHT）进行内容发现，节点通过 'provide' 消息声明它们拥有特定内容。原本提供操作需要等待一部分对等节点确认，导致较大延迟。乐观提供通过在大多数 RPC 成功后立即返回控制权，并异步处理剩余部分，从而减少了延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://probelab.io/blog/optimistic-provide/">Optimistic Provide: How We Made IPFS Content Publishing 10x Faster - Blog | ProbeLab Analytics</a></li>
<li><a href="https://blog.ipfs.tech/2026-05-optimistic-provide/">Optimistic Provide: How We Made IPFS Content Publishing 10x Faster</a></li>
<li><a href="https://docs.ipfs.tech/concepts/dht/">Distributed Hash Tables (DHT) | IPFS Docs</a></li>

</ul>
</details>

**社区讨论**: 一些评论者认为这种加速具有误导性，因为它来自异步操作而非真正提高同一工作的速度。其他人则对 IPFS 的采用和性能表示担忧，其中一位指出某些用户的查找速度仍然很慢。

**标签**: `#IPFS`, `#DHT`, `#performance optimization`, `#peer-to-peer`, `#distributed systems`

---

<a id="item-18"></a>
## [Claude Code v2.1.196：增强安全、默认模型与错误修复](https://github.com/anthropics/claude-code/releases/tag/v2.1.196) ⭐️ 7.8/10

Anthropic 发布了 Claude Code v2.1.196，新增了组织默认模型、可点击文件附件、MCP 服务器的安全改进，以及多项错误修复，包括后台作业可靠性和速率限制遥测。 此版本通过改进会话管理和安全性提升了开发者工作流程效率，尤其适用于在集成 MCP 的企业环境中使用 Claude Code 的团队。 值得注意的是，技术改进包括/code-review 中令牌使用量减少 25%、默认启用流式空闲看门狗，以及在包括 Windows 在内的所有平台上增强的后台会话在进程重启后的存活能力。

github · ashwin-ant · Jun 29, 23:27

**背景**: Claude Code 是 Anthropic 推出的一款 AI 驱动的编码助手，运行在终端中，可以通过模型上下文协议（MCP）连接到外部工具。它利用大型语言模型帮助开发者编写、审查和调试代码。MCP 服务器使 Claude Code 能够访问诸如问题跟踪器或代码仓库等资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/mcp">Connect Claude Code to tools via MCP - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#release notes`, `#AI tooling`, `#developer tools`

---

<a id="item-19"></a>
## [首个从头构建的合成细胞能生长分裂](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/) ⭐️ 7.8/10

这项突破克服了合成生物学的一个主要瓶颈，在完全合成系统中展示了完整的生命周期，可能彻底改变生物工程和我们对生命的理解。 SpudCell 通过使用修饰的膜对膜附着机制在没有细胞骨架的情况下分裂，该研究最初被《细胞》期刊拒绝，随后发布在 bioRxiv 上并投稿到其他期刊。

hackernews · defrost · Jul 1, 14:20 · [社区讨论](https://news.ycombinator.com/item?id=48747304)

**背景**: 合成生物学旨在从头构建生命系统。一个关键挑战是实现细胞分裂，这在自然细胞中依赖于细胞骨架。SpudCell 通过使用不同的分裂机制绕过了这一难题，实现了包括生长、DNA 复制和分裂的完整细胞周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/07/01/science/spud-cell-what-to-know.html">SpudCell : Scientists Made a Cell With Most of the Hallmarks of Life.</a></li>
<li><a href="https://phys.org/news/2026-07-world-synthetic-cell-life-revolutionize.html">World's first synthetic cell with a complete life cycle could revolutionize...</a></li>

</ul>
</details>

**社区讨论**: 评论褒贬不一：有些人称赞这项技术成就，而另一些人则对炒作表示怀疑，指出该工作被《细胞》期刊拒绝，并质疑 SpudCell 是否真正算作“活着”，还是仅仅是一个复杂的化学系统。

**标签**: `#synthetic biology`, `#cell division`, `#biotechnology`, `#scientific breakthrough`, `#synthetic cells`

---

<a id="item-20"></a>
## [Cloudflare x402 协议实现资源访问的微支付](https://blog.cloudflare.com/monetization-gateway/) ⭐️ 7.8/10

Cloudflare 宣布了 x402 协议，该协议允许网站运营商通过使用稳定币或其他支付方式的微交易，对 Cloudflare 背后的任何资源进行收费。 该协议可能彻底改变 AI 代理和机器人访问网络资源的方式，实现无需人工干预的自动支付，同时也引发了关于机器人管理以及人类与机器流量平衡的问题。 x402 协议使用 HTTP 402 Payment Required 状态码触发支付请求，专门为机器对机器 (M2M) 交易设计。它利用 Cloudflare 的现有基础设施，但给运营商带来了法律和发票方面的复杂性。

hackernews · soheilpro · Jul 1, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=48746914)

**背景**: HTTP 402 Payment Required 是一个很少使用的标准状态码。x402 协议旨在实现网络内容微交易的长期愿景，允许自动化代理无需传统 API 密钥即可按请求付费访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onemint.io/blog/the-directory-for-the-x402-protocol">One Mint Blog - The directory for the x 402 protocol</a></li>
<li><a href="https://taiwandailynews.com/article/886814957-new-x402-protocol-solution-addresses-media-monetization-and-deepfake-verification-in-the-ai-era">New x 402 Protocol Solution Addresses Media... | Taiwan Daily News</a></li>

</ul>
</details>

**社区讨论**: 评论对代理驱动支付的潜力表示兴奋，但也担心如何保留人类用户的免费体验、机器人自我标识的动机，以及微交易中发票和税收的法律复杂性。

**标签**: `#Cloudflare`, `#monetization`, `#microtransactions`, `#AI agents`, `#API access`

---

<a id="item-21"></a>
## [Anthropic 推出 Claude Science 用于自主科学研究](https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/) ⭐️ 7.5/10

Anthropic 在面向制药高管和生物技术研究人员的活动上宣布了 Claude Science，这是一款能自主支持科学研究的新产品，类似于用于软件工程的 Claude Code。 该产品可能通过自动化重复性任务加速科学发现，使研究人员能够专注于高层次问题，从而有可能改变药物发现和材料科学等行业，并标志着 Anthropic 从代码领域向科学领域的扩展。 Claude Science 能够根据高级指令执行有意义的工作，并可访问相关工具，初期目标是制药和生物技术领域。

rss · MIT Tech Review · Jun 30, 21:50

**背景**: Claude Code 是 Anthropic 的一款 AI 工具，通过自主执行编码任务来协助软件工程师。这两款产品均利用了 Anthropic 使用宪法 AI 训练的大型语言模型，以确保伦理对齐。Claude Science 将这一能力扩展到科学研究，使其能够分析数据、运行模拟或生成假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#science`, `#LLM`, `#product launch`

---

<a id="item-22"></a>
## [AI 同事与太阳能平流层互联网](https://www.technologyreview.com/2026/06/30/1139954/the-download-ai-agents-coworkers-solar-powered-internet/) ⭐️ 7.5/10

MIT Technology Review 的通讯讨论了 AI 代理被当作同事推销的现象，并强调了太阳能平流层互联网扩展全球连接的潜力。 这很重要，因为 AI 代理可能从根本上改变职场动态，而平流层互联网则能为目前无法上网的数十亿人提供连接，缩小数字鸿沟。 该通讯认为，尽管 AI 代理具有目标导向并能执行多步骤任务，但缺乏人类协作的方面，不应被视为同事。平流层互联网平台，如高空气球或太阳能无人机，在平流层运行以提供互联网覆盖。

rss · MIT Tech Review · Jun 30, 12:10

**背景**: AI 代理是使用大语言模型自主追求目标并完成任务、通常具备自然语言界面的软件系统。平流层互联网是指由漂浮在距地面约 20 公里平流层的平台提供的连接，能覆盖大面积区域且延迟低于卫星。太阳能和轻质材料的最新进展使这类平台更具可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2026/01/27/1131780/stratospheric-internet-take-off/">Stratospheric internet could finally start taking off this year | MIT Technology Review</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#technology review`, `#internet`, `#solar power`, `#newsletter`

---

<a id="item-23"></a>
## [Dario Amodei：AI 开源是伪命题](http://www.ruanyifeng.com/blog/2026/06/anthropic.html) ⭐️ 7.5/10

Anthropic 首席执行官 Dario Amodei 认为 AI 开源是一个伪命题，指出开源 AI 的风险大于收益。 来自一位领先 AI 安全倡导者的表态重新点燃了开放与封闭 AI 开发之间的辩论，对监管、创新和安全具有重要意义。 Anthropic 联合创始人 Amodei 表达了对开源强大 AI 模型可能导致滥用和不可控风险的担忧，这与 Anthropic 关注 AI 安全的理念一致。

rss · 阮一峰周刊 · Jun 30, 03:04

**背景**: AI 开源辩论的核心在于，使 AI 系统组件自由可用是促进创新还是带来安全风险。Anthropic 是一家以开发对话式 AI 助手 Claude 而闻名的 AI 安全公司。Dario Amodei 一直积极倡导负责任的 AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/core-views-on-ai-safety">Anthropic's core views on AI safety \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://venturebeat.com/ai/the-open-source-ai-debate-why-selective-transparency-poses-a-serious-risk">The open-source AI debate: Why selective transparency poses a serious risk | VentureBeat</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#Anthropic`, `#Dario Amodei`, `#AI safety`

---

<a id="item-24"></a>
## [Claude Code v2.1.198 发布：新增 Chrome 通用版本和代理通知](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) ⭐️ 7.3/10

Anthropic 发布了 Claude Code v2.1.198，将 Claude 在 Chrome 中的功能推进到通用可用状态，并新增了后台代理通知、/dataviz 技能以及 AWS 平台接入。此次更新还包含大量错误修复和性能改进。 此次发布通过支持可自主提交和推送代码的持久化后台代理，以及提供专门的 /dataviz 技能，增强了开发者生产力。改进的可靠性和故障转移机制减少了企业环境中的工作流中断。 后台代理现在会触发通知钩子（agent_needs_input / agent_completed），并且在工作树中完成代码工作后会自动提交、推送并打开草稿 PR，不再停下询问。此外，子代理会继承会话的扩展思考配置，网关故障转移链在模型未找到响应时会推进。

github · ashwin-ant · Jul 1, 20:45

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手，可集成到编辑器和命令行中。后台代理允许用户启动异步运行的长时任务，而网关功能则跨多个提供商路由 API 调用以提高可靠性。/dataviz 技能为数据可视化设计提供专家指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/claude-code-bg-command-background-agent-sessions">How to Use Claude Code's /bg Command to Run Background Agent Sessions | MindStudio</a></li>
<li><a href="https://skillmd.ai/tutorials/run-on/claude-code/dataviz/">Step-by-step guide to running dataviz AI agent skill on Claude Code .</a></li>
<li><a href="https://www.getmaxim.ai/articles/best-enterprise-ai-gateway-to-monitor-and-optimize-llm-costs-2/">Best Enterprise AI Gateway to Monitor and Optimize LLM Costs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI coding tools`, `#release notes`, `#Anthropic`, `#developer tools`

---

<a id="item-25"></a>
## [AI 时代产品工程师与现场部署工程师的融合](https://www.latent.space/p/forward-deployed-engineers-aiewf) ⭐️ 7.2/10

Sierra 公司的 Natalie Meurer 探讨了产品工程师与现场部署工程师如何开始融合，在 AI 时代模糊了传统角色边界。 这种融合标志着软件工程角色的转变，要求工程师将深厚的产品敏锐度与面向客户的部署技能相结合，可能重塑招聘和团队结构。 传统上，现场部署工程师（FDE）直接与客户合作，定制和部署复杂系统，而产品工程师则专注于构建内部功能。Meurer 认为 AI 工具使单个工程师能更有效地同时扮演两种角色。

rss · Latent Space · Jul 1, 00:20

**背景**: 现场部署工程师（FDE）是一种直接与客户合作，实施、定制和优化技术系统的软件工程师，通常需要出差。产品工程师通常从事公司核心产品开发，不与客户直接接触。AI 和低代码工具的兴起减少了对专业部署专业知识的需求，使产品工程师更容易处理面向客户的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/blogs/forward-deployed-engineer-role-skills-salary-roadmap/">Forward Deployed Engineer (FDE): Role, Skills, Salary & Career Roadmap - GeeksforGeeks</a></li>
<li><a href="https://www.secondtalent.com/resources/how-to-become-forward-deployed-engineer-fortune-500/">How to Become a Forward - Deployed Engineer ... | Second Talent</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#forward deployed engineers`, `#product engineering`, `#AI`, `#future of work`

---

<a id="item-26"></a>
## [图形编程学习路径指南](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/) ⭐️ 7.1/10

一篇题为《学习成为图形程序员需要掌握什么》的博客文章发布，详细介绍了该领域所需的数学和技能。 该指南为有志向的图形程序员提供了清晰的学习路径，考虑到该领域的复杂性和快速演变，这一点非常重要。 该文章强调线性代数和实践技能，并包含社区关于行业节奏和设计原则重要性的讨论。

hackernews · atan2 · Jul 1, 17:53 · [社区讨论](https://news.ycombinator.com/item?id=48750710)

**背景**: 图形编程涉及使用计算方法创建图像和动画，通常借助 OpenGL 或 DirectX 等 API。扎实的数学基础，尤其是线性代数，对于理解变换和着色至关重要。

**社区讨论**: 评论观点不一：有人警告行业节奏快、竞争激烈，而另一些人则指出缺乏设计和感知知识。有用户建议从简单项目开始，而不是将其视为职业。

**标签**: `#graphics programming`, `#linear algebra`, `#computer graphics`, `#programming education`, `#HN discussion`

---

<a id="item-27"></a>
## [Warp CEO 展望自动化软件工厂](https://www.latent.space/p/software-factories) ⭐️ 7.0/10

Warp 公司 CEO Zach Lloyd 预测，每个大型软件项目很快都将通过自动化软件工厂来构建，并就工程师应如何为此转变做好准备提出了建议。 这一愿景标志着软件开发的根本性转变，从手动编码转向流水线式自动化，这可能会极大地提高生产力，并改变工程师所需的技能组合。 Warp 是一款带有 AI 功能的现代终端模拟器，而“软件工厂”概念将这种自动化扩展到整个开发生命周期，包括构建、测试和部署。

rss · Latent Space · Jul 1, 14:28

**背景**: 软件工厂是一种自动化环境，通过可复用的组件、模板和流水线系统地生产软件，类似于实体工厂生产制成品。Warp 是一款用 Rust 编写的开源终端模拟器，集成了 AI 用于命令建议和代码生成，将自己定位为能够自动化开发者工作流的“代理式开发环境”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Warp_(terminal)">Warp (terminal) - Wikipedia</a></li>
<li><a href="https://www.warp.dev/">Warp — The Agentic Development Environment</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#dev tools`, `#automation`, `#Warp`, `#future of coding`

---

<a id="item-28"></a>
## [AIEWF 亮点：循环、软件工厂与开放模型](https://www.latent.space/p/aiewf-daily-dispatch-loops) ⭐️ 7.0/10

周二在 AI 工程师世界博览会上，讨论聚焦于智能体工程中的循环、软件工厂的兴起以及开放模型对 AI 开发的重要性。 这些话题标志着从孤立 AI 智能体向集成化、可投产系统的转变，这些系统能够自主迭代和改进，可能改变软件组织扩展 AI 工程的方式。 循环工程涉及为自主智能体设计迭代循环，而像 Factory.ai 这样的软件工厂则构建互联、自改进的系统，覆盖整个软件开发周期。

rss · Latent Space · Jul 1, 04:46

**背景**: AI 智能体依赖'循环'——一种有界的操作周期，使其持续朝着目标工作，直到满足停止条件。软件工厂将这一概念延伸，将多个智能体和工具集成为一个连贯的系统，从自身输出中学习。开放模型（如 Llama 或 Mistral）让开发者完全掌控并能进行微调，无需受限于供应商，从而推动该领域创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://factory.ai/">Factory | Agent-Native Software Development</a></li>
<li><a href="https://factory.ai/news/software-factory">Factory 2.0: From coding agents to software factories | Factory.ai</a></li>
<li><a href="https://www.mindstudio.ai/blog/loop-engineering-vs-harness-engineering">Loop Engineering vs Harness Engineering : What's the... | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI Engineering`, `#Agentic Systems`, `#Software Factories`, `#Open Models`, `#Loops`

---