---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> From 108 items, 14 important content pieces were selected

---

1. [陶哲轩警告人工智能在数学领域出现严重错位](#item-1) ⭐️ 8.8/10
2. [基准测试质疑 RTK 宣称的 AI 编程 token 节省](#item-2) ⭐️ 8.3/10
3. [量化代码"邋遢度"：为 AI 编程代理提供质量反馈的度量指标](#item-3) ⭐️ 8.2/10
4. [Shopify 放弃 React Native 回归原生 Swift 与 Kotlin，理由是 AI 智能体](#item-4) ⭐️ 8.2/10
5. [OpenRouter 自动路由可能让同一模型表现不一致](#item-5) ⭐️ 8.0/10
6. [用 Gradio Workflow 重建 AUTOMATIC1111 WebUI](#item-6) ⭐️ 8.0/10
7. [Stratechery：苹果对「应用至上」的执念是其 AI 盲点](#item-7) ⭐️ 8.0/10
8. [trynix.dev 让任意 Nix 软件包在浏览器虚拟机中启动](#item-8) ⭐️ 7.9/10
9. [OpenAI 声称 AI 智能体找到 Navier-Stokes 反例，引发署名争议](#item-9) ⭐️ 7.7/10
10. [开发者发现 220 美元 Google Ads 应用安装中 60%来自机器人](#item-10) ⭐️ 7.4/10
11. [Calif Research 声称用 AI 打造微信通话零点击蠕虫](#item-11) ⭐️ 7.4/10
12. [基于 Go 的可改造终端编辑器 Rune 正式开源](#item-12) ⭐️ 7.2/10
13. [OpenAI 将 Habitat 存储扩展至 10 亿用户，每秒 2200 万请求](#item-13) ⭐️ 7.0/10
14. [阮一峰科技周刊第 412 期：禁止 issue，只用 PR](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [陶哲轩警告人工智能在数学领域出现严重错位](https://mathandai.org/) ⭐️ 8.8/10

2026 年 9 月 11 日，菲尔兹奖得主陶哲轩（Terry Tao）发表了一篇题为《人工智能在数学中的严重错位》的博客文章，认为 AI 生成的证明正在威胁数学的认识论基础。几乎同时，《经济学人》报道称顶尖数学家对 OpenAI 的做法感到愤怒，该话题在 Hacker News 上获得 549 分和 612 条评论。 这场争论的意义远超工具层面：如果机器能够以超过人类验证速度产出未解难题的证明，那么长期以来衡量数学贡献的标尺——解决著名未解问题——将失去意义，学术声誉、职业发展和经费分配都可能在一个充满争议的新基础上被重新定义。这也提出了更广泛的问题：每一个生产知识的领域将如何应对自己无法完全理解的机器生成成果。 评论者指出，这并非全新的问题：望月新一（Shinichi Mochizuki）2012 年的 abc 猜想证明同样庞大而晦涩，多年来带来的是怀疑、会议和屡次失败的验证尝试，而非明确的结论。讨论还强调，这类能力已经公开存在，因此真正的问题不是阻止模型，而是重建学分分配与理解验证的机制。

hackernews · meredydd · Sep 11, 17:45 · [社区讨论](https://news.ycombinator.com/item?id=49662371)

**背景**: 数学传统上依赖同行评审和人类可读的证明：只有当其他数学家能够理解并验证论证过程时，一个结果才算被确立。陶哲轩是当今最著名的数学家之一，他曾大量撰文讨论人工智能以及 Lean 等证明助手如何改变数学实践。近年来大语言模型的进步让系统能够处理竞赛题目并辅助形式化工作，这正是如今“AI 解决重大未解问题”的说法具有真实分量的原因。

**社区讨论**: 社区情绪虽有分歧但讨论质量很高。一些数学家和工程师对悲观论调提出反驳：tmhn2 将这一局面比作望月新一的 abc 猜想，指出晦涩的证明依然催生了会议、论文和部分理解；gwd 则把这种恐慌类比为 1990 年代人们担心计算机会毁掉国际象棋，而三十年后的国际象棋却比以往更流行、棋手水平更高。jeremysalwen 认为 AI 并没有摧毁数学家理解并分享思想的能力，只是摧毁了“解决未解问题”这一标尺；david-gpu 则将其类比为 19 世纪波德莱尔对摄影的贬斥——认为摄影只是失败画家的机械避难所。

**标签**: `#AI`, `#mathematics`, `#LLM`, `#AI alignment`, `#epistemics`

---

<a id="item-2"></a>
## [基准测试质疑 RTK 宣称的 AI 编程 token 节省](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/) ⭐️ 8.3/10

Quesma 发布了一篇基于基准测试的博客文章，认为 RTK 报告出的 token 节省并不能转化为真实的 AI 编程成本下降，尽管 RTK 宣称可减少 60–90% 的 token。该文在 Hacker News 上引发了关于 `rtk gain` 如何统计节省 token 的讨论。 许多开发者正在采用 CLI 代理和上下文压缩技巧来控制不断上升的编程智能体成本，因此一项可信的基准测试如果推翻热门工具的节省声明，可能会影响工具选择和采购决策。这也凸显出行业需要独立的端到端成本基准，而不是依赖工具自我报告的 token 数量。 RTK 是一个单一 Rust 二进制程序，位于 shell 与 LLM 之间，在命令输出进入上下文窗口前对其进行压缩。一个关键批评是，`rtk gain` 可能会把一条打印 10 万 token 但通过管道传给 `tail -5` 的命令算作节省了 10 万 token，而模型实际只看到五行；同时它默认持久化节省统计数据，可能破坏沙箱并触发自动模式拒绝。

hackernews · michalwarda · Sep 11, 11:15 · [社区讨论](https://news.ycombinator.com/item?id=49656471)

**背景**: RTK（Rust Token Killer）是一个开源 CLI 代理，会拦截常见开发者命令并压缩其输出，然后再发送给 AI 编程智能体，号称可削减高达 90% 的 token 噪声。AI 编程智能体的 API 预算有很大一部分花在工具输出上，因此如果压缩后仍保留足够信息，减少 token 就能降低成本。不过，当工具统计的是压缩前输出、而不是模型实际计费的 token 时，自我报告的节省数据可能会产生误导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rtk-ai/rtk">GitHub - rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies · GitHub</a></li>
<li><a href="https://www.rtk-ai.app/">RTK — Rust Token Killer</a></li>
<li><a href="https://dev.to/arshtechpro/how-rtk-reduces-llm-token-usage-for-ai-coding-agents-2kfd">RTK: Cut Your AI Coding Bill by 80% With One CLI Tool - DEV Community</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者大多持怀疑态度：aeneas_ory 称这些省 token 的“黑客技巧”是 snakeoil，并表示用本地嵌入模型索引代码库效果更好；monneyboi 则用 treesitter 生成文件和目录大纲。oefrha 认为从 `rtk gain` 的输出就能明显看出问题，因为通过管道传给 `tail -5` 的命令会被算作完整节省；ProjectBarks 认为这类工具大多是 vaporware，并呼吁建立独立基准测试。gillesjacobs 总结了使用与不使用 RTK 的平均每次尝试成本，但其引用的数据并不完整。

**标签**: `#AI coding agents`, `#LLM cost optimization`, `#benchmarking`, `#developer tooling`, `#token usage`

---

<a id="item-3"></a>
## [量化代码"邋遢度"：为 AI 编程代理提供质量反馈的度量指标](https://earendil.com/posts/measuring-code-sloppiness/) ⭐️ 8.2/10

earendil.com 上的一篇题为《如果编码已被解决，接下来呢？：测量代码的邋遢程度》的文章，提出了一套量化评估代码"邋遢度（sloppiness）"的指标——例如冗长程度、重复度、代码侵蚀与复杂度——并特别将其定位为向大规模生成代码的 AI 代理提供反馈的信号。文章指出，虽然 LLM 能够生成形式上正确的代码，但它们带来了前所未有的冗长与重复，连代理自身都难以管理，因此得出结论：任何此类评估中都或隐或显地嵌入了人类的直觉与品味。 随着 AI 编程代理从代码补全进化到跨多文件自主规划与重构，团队需要客观手段来判断生成代码是"仅仅正确"还是"真正可维护"。这项工作正处于两大热门领域的交汇点——代理式 AI 系统与软件工程质量——并可能影响未来代理反馈回路、代码审查工具以及成本模型（token 开销与人工维护成本之权衡）的设计方式。 作者明确指出，代码邋遢度的指标很难做到客观定义，因为人类直觉与品味不可避免地参与其中；同时列出了几个尚待探索的有前景方向，如函数之间的耦合度、代码变动率（code churn）与内聚性。讨论还涉及一个现实提醒：在前沿模型上不计 token 成本时，编码看似"已被解决"，但一旦按 token 计费的企业方案生效，人类开发者可能反而更具成本效益。

hackernews · doppp · Sep 11, 13:42 · [社区讨论](https://news.ycombinator.com/item?id=49658311)

**背景**: 基于 LLM 的编程代理是能够跨多个文件自主编写、修改、调试和重构代码的工具，远不止简单的自动补全。传统软件工程中已有"代码坏味道（code smell）"的概念——它不是 bug，但代表设计弱点，预示着技术债与未来的维护风险——不过这类问题通常由人工评审判断，而非数值化度量。本文追问的是：当代码的主要生产者从人变成代理时会发生什么，并试图把模糊的"邋遢/slop"概念转化为代理可以据此优化的信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://earendil.com/posts/measuring-code-sloppiness/">If coding is solved, what now?: Measuring the sloppiness of ...</a></li>
<li><a href="https://news.lavx.hu/article/if-coding-is-solved-what-now-measuring-the-sloppiness-of-code">If coding is solved, what now?: Measuring the sloppiness of code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code_smell">Code smell - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上欢迎这种为代理提供量化反馈的思路。dherman 认为，真正重要的邋遢问题属于"全局属性"而非局部属性，因为无论是代理还是人类注意力都有限，遇到碍事的局部混乱时可以按需修复。conqrr 则对"编码已被解决"的说法提出反驳，指出编码同样是团队内部共享心智模型的传播过程，如果人类被排除在编码之外，那么这个心智模型由谁持有？toddwprice 补充了成本视角：在不计 token 成本时前沿模型让编码看似已被解决，但一旦企业级按 token 计费，团队就会退回"合理"的成本水平，此时人类开发者可能更具成本效益。

**标签**: `#code quality`, `#AI agents`, `#software engineering`, `#metrics`, `#technical debt`

---

<a id="item-4"></a>
## [Shopify 放弃 React Native 回归原生 Swift 与 Kotlin，理由是 AI 智能体](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.2/10

Shopify 宣布将其移动应用从 React Native 迁回 iOS 与 Android 各自独立原生的 Swift 和 Kotlin 代码库，理由是在 2020 年曾是决定性成本的“维护两套代码库”，如今已交由 AI 智能体承担足够多的实现、跨语言翻译、测试与代码审查工作。作为此次转向的一部分，公司旗下的 react-native-skia 与 flash-list 两个库正在寻找新的维护者，而 restyle 因“用户规模小于我们其他库”将于 2026 年底归档。 这是一个具体而真实的信号：编码智能体正在重塑软件工程中“自建还是采购”以及平台选型的基本经济账，而不只是加速单个任务。如果像 Shopify 这样体量的公司以此为由推翻其 2020 年著名的跨平台决策，其他工程组织很可能也会重新审视自己的框架选择，并连带影响 React Native 生态及其依赖的开源库。 Shopify 曾是 React Native 的重要贡献者，维护着三个知名库：react-native-skia、flash-list 和 restyle；前两者正在被移交给新的归属方，restyle 则将于 2026 年底归档。Shopify 的文章明确肯定了 React Native 在其使用的六年中是一个优秀的平台，因此这次转向被定位为一次经济账的重新计算，而非对该技术的否定，也不是宣称原生开发在纯工程成本上变得更便宜。

rss · Simon Willison · Sep 10, 21:11

**背景**: React Native 是 Meta 开源的框架，允许开发者用 JavaScript/React 编写一次 UI 与逻辑，即可同时在 iOS 和 Android 上运行，从而避免在两个平台上重复实现功能。另一条路径是原生开发，即分别用 Swift（苹果的 iOS 开发语言）和 Kotlin（Android 的主流语言）编写两套代码库，能获得最佳的平台一致性，但所有功能都要做两遍并维护两遍。正因如此，跨平台框架在 2010 至 2020 年代被广泛采用，以削减这种重复成本。如今基于大语言模型的 AI 编码智能体能够生成实现、在不同语言间移植代码、编写测试并审查代码合并请求，Shopify 称正是这一变化改变了原本的成本权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://kotlinlang.org/docs/multiplatform/native-and-cross-platform.html">Cross-platform and native app development: How do you choose?</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_software_development">AI-assisted software development - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#mobile development`, `#React Native`, `#developer tooling`

---

<a id="item-5"></a>
## [OpenRouter 自动路由可能让同一模型表现不一致](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 8.0/10

Simon Willison 推荐了 Mohamed Moustafa 的博客文章《So you want to use OpenRouter?》，文中警告 OpenRouter 的自动提供商路由可能把同一个模型 ID 的请求静默发送到不同的后端提供商，而各家运行的推理服务软件、优化参数和设置都不一样，因此同一个端点可能返回行为不一致的结果。文章指出解决办法是使用 OpenRouter 的 provider.only 选项，并可通过 /endpoints 方法查询某个模型 ID 当前有哪些可用提供商。 那些为了自动故障转移和成本优化而基于 OpenRouter 构建应用的开发者，可能在不知情的情况下得到无法复现的输出，这对模型评测、Agent 流水线、结构化输出解析以及任何依赖行为一致性的应用都是严重问题。这也暴露了多提供商 LLM 网关模式的深层矛盾：统一 API 掩盖了真实的基础设施差异，而这些差异会渗入产品行为之中。 文中提到的不一致包括：各提供商使用的推理服务软件与优化设置不同；某些提供商即便面对支持视觉的模型也不提供视觉能力；对 reasoning effort（推理强度）参数的处理方式也各不相同。若要锁定行为，可以用 provider.only 限制路由，并先通过 /endpoints 方法列出支撑某个模型的所有提供商，再从中挑选。

rss · Simon Willison · Sep 11, 22:49

**背景**: OpenRouter 是一个网关服务，把众多大模型统一封装在一个兼容 OpenAI 的 API 之后，并宣称可以自动故障转移、为每个请求选择最具性价比的后端。它在底层聚合了大量第三方推理提供商，每家可能运行着不同量化版本、不同推理框架（如 vLLM 或类似 TensorRT-LLM 的技术栈）的同一模型，功能支持也不尽相同。reasoning effort（推理强度）是现代推理模型常见的调节参数，用延迟和成本换取模型在给出答案前“思考”的深度，因此对该参数处理不一致会同时改变输出质量和价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/docs/guides/routing/provider-selection">Provider Routing - Smart Multi-Provider Request ... - OpenRouter</a></li>
<li><a href="https://or.vh.brainex.co/blog/insights/model-routing/">How OpenRouter Model Routing Works: Providers , Fallbacks & Auto ...</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/reasoning-effort">Reasoning effort - LLM Parameter Guide - Vellum</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenRouter`, `#AI infrastructure`, `#API routing`, `#LLM inference`

---

<a id="item-6"></a>
## [用 Gradio Workflow 重建 AUTOMATIC1111 WebUI](https://huggingface.co/blog/gradio-workflow-1111) ⭐️ 8.0/10

Hugging Face 发布了一篇技术实战教程，用 Gradio Workflow 重新实现了 AUTOMATIC1111（A1111）Stable Diffusion WebUI，演示如何把一个单体式的生成式 AI 界面拆解为模块化、可连接的流水线。该文章是面向动手实践、以代码为核心的指南，而非新产品或新模型发布。 A1111 是使用最广泛的开源图像生成前端之一，把它的功能映射到工作流框架上，为开发者构建和重构生成式 AI 界面提供了可复用的范式。这也表明 Gradio 正从单一功能演示迈向多步骤、可组合的 AI 应用。 在 Gradio 的工作流模型中，每个工作流应用仍然是 Gradio 应用，会通过标准 Gradio REST API 暴露其连接的流水线，其中每条彼此断开、包含一个或多个输出节点的流水线都会获得各自独立的端点。这意味着教程中的模块化设计仍可被程序化调用，但重新实现版本大概率无法开箱即用地覆盖 A1111 庞大的第三方扩展生态。

rss · Hugging Face Blog · Sep 10, 00:00

**背景**: AUTOMATIC1111 Stable Diffusion Web UI（常简称 SD WebUI 或 A1111）是由 GitHub 匿名开发者 AUTOMATIC1111 于 2022 年 8 月发布的 开源程序，它以 Stable Diffusion 作为基础模型，根据文本提示生成图像，并配有大量扩展与自定义功能。Gradio 是一个用于构建机器学习 Web 界面的 Python 库，其 Workflow 能力让开发者可以把多个模型或处理步骤串联成流水线，而不再是一个单体函数。相关的 gradio-app/daggr 等工具——灵感来自 Airflow、Prefect 这类编排系统，但定位于交互式 AI/ML 原型开发——也体现了向可视化、可逐步检查的流水线演进的同一趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AUTOMATIC1111_Stable_Diffusion_Web_UI">AUTOMATIC1111 Stable Diffusion Web UI</a></li>
<li><a href="https://gradio.app/guides/workflows">Workflows</a></li>
<li><a href="https://github.com/gradio-app/daggr">GitHub - gradio-app/daggr: Chain apps and models to build robust AI workflows 🤗</a></li>

</ul>
</details>

**标签**: `#Gradio`, `#Stable Diffusion`, `#AI tooling`, `#developer tools`, `#generative AI`

---

<a id="item-7"></a>
## [Stratechery：苹果对「应用至上」的执念是其 AI 盲点](https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/) ⭐️ 8.0/10

Ben Thompson 在 Stratechery 发表文章，分析苹果 2026 年 9 月发布会，涉及「iPhone 双机组合」（iPhone Duo）、苹果把 iPhone 定位为「智能个人中枢」（intelligent personal hub），以及 Apple Watch 全新的「音频智能」（Audio Intelligence）功能。其核心论点是：苹果的软硬件整合能力依然无人能敌，但「应用至上」的信念才是它最大的 AI 盲点。 这一批评直指苹果「以应用为中心」的世界观与 agentic AI 之间的断层：后者跨服务自主追求目标，而不是等用户打开并操作某一个应用。如果苹果继续把 App 当作计算的基本单位，即使它的设备仍是运行 AI 的最佳硬件，也可能把助手层、乃至随之而来的用户关系让给竞争对手。 Stratechery 的文章大部分位于付费墙后，公开可见的只有那句预告——苹果以应用为中心的世界观是它的 AI 盲点，因此本文无法概括其完整论证。该文出现的同时，苹果也发布了具体产品：苹果将 iPhone 18 Pro 与 Pro Max 定位为「智能个人中枢」；Apple Watch Series 12 与 Apple Watch Ultra 4 上的 Audio Intelligence 则利用手表麦克风与端侧、云端 AI 模型来识别声音、辨曲，并捕捉对话中错过的内容。

rss · Stratechery · Sep 10, 10:00

**背景**: 苹果长期以来的优势在于垂直整合：同时掌控自研芯片、操作系统与硬件，从而带来更分散的竞争对手难以匹敌的性能与隐私表现。但它的商业模式建立在「应用即目的地」之上——App Store，以及写作工具、通知摘要等 Apple Intelligence 功能，都存在于一个个独立 App 之内。agentic AI 恰恰颠覆了这一模式：语言模型在循环中运行，自主选择动作、调用跨服务的工具来达成目标，无需每一步都获得人类批准，这使得「应用边界」更像是一种束缚而非特性。包括 CEO John Ternus 在内的苹果高管，把 iPhone 描述为拥有广泛个人上下文、最理想的「智能个人中枢」，而这正是 Thompson 要检验的说法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.computerworld.com/article/4220404/the-iphone-is-now-apples-intelligent-personal-hub.html">The iPhone is now Apple’s ‘intelligent personal hub’</a></li>
<li><a href="https://techcrunch.com/2026/09/09/apple-ceo-john-ternus-says-the-best-ai-device-is-still-the-iphone/">Apple CEO John Ternus says the best AI device is still the ...</a></li>
<li><a href="https://remolda.com/en/glossary/agentic-ai">Agentic AI — definition | Remolda</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI Strategy`, `#Product Management`, `#Hardware-Software Integration`, `#Agentic AI`

---

<a id="item-8"></a>
## [trynix.dev 让任意 Nix 软件包在浏览器虚拟机中启动](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 7.9/10

Farid Zakaria 发布了 trynix.dev，Simon Willison 称其为 Nix 领域的“magnum opus”（代表作）：该服务通过 qemu-wasm（编译为 WebAssembly 的 QEMU）在浏览器内完整运行一个 x86_64 Linux 虚拟机，并可用过去 13 年间构建的任意 Nix 软件包启动该虚拟机。软件包可通过 URL 寻址——访问 https://trynix.dev/?pkg=python3%403.6.2 并点击“Load”，即可获得一个运行 2017 年 Python 3.6.2 的交互式 shell。Zakaria 还发布了 trynix-preview，一个会在 pull request 下评论 trynix.dev 启动链接的 GitHub Action，让审查者无需任何服务器即可启动该 PR 的构建产物。 它弥合了“这个构建在 2017 年能用”和“让我真的跑一下”之间的鸿沟：可复现性验证、遗留环境测试和 PR 审查都变成一个浏览器标签页，而不再需要容器或云虚拟机。由于它可通过 URL 寻址且无需服务器，它可能改变开源项目让贡献者和审查者验证改动的方式，同时也是 WebAssembly 虚拟化技术已发展到何种程度的一次引人注目的展示。 Nix 包管理器基于内容寻址的存储（content-addressed store）是实现这一点的关键：每个软件包版本都有由哈希推导出的稳定路径，因此 URL 可以明确指向 Python 3.6.2 或任何其他历史构建。qemu-wasm 的作者明确将其描述为实验性软件，因此在性能和兼容性上存在局限；而在浏览器中启动完整虚拟机也意味着在 shell 出现前有不容忽视的下载与启动开销。

rss · Simon Willison · Sep 10, 23:44

**背景**: Nix 是一个包管理器兼构建系统，它把每个软件包都视为其依赖项的纯函数求值结果，并将产物存放在 /nix/store 下名称唯一的目录中。这种设计消除了依赖冲突，使构建可复现且可逐位验证，因此历史版本在多年后仍可安装运行。WebAssembly 是一种低层次的类汇编字节码格式，能在浏览器（及其他宿主环境）中以接近原生的速度执行，从而使 QEMU 这类大型 C/C++ 代码库可以被编译到 Web 上运行。qemu-wasm 正是把这一思路应用到 QEMU——广泛使用的开源机器模拟器与虚拟化工具——之上，让完整的 x86_64 Linux 客户机可以在浏览器标签页中执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager) - Wikipedia</a></li>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly - MDN</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#DevTools`, `#Reproducibility`, `#Virtualization`

---

<a id="item-9"></a>
## [OpenAI 声称 AI 智能体找到 Navier-Stokes 反例，引发署名争议](https://www.solidot.org/story?sid=85339) ⭐️ 7.7/10

OpenAI 本周宣布，约 1 万个 AI 智能体连续运行 88 小时后，于 9 月 5 日找到了一个 Navier-Stokes 方程失效的特例，并声称这是 AI 首次解决重大数学难题。但这一说法随即引发争议：过去一个月里，纽约大学数学家 Tristan Buckmaster 与 Anthropic 研究员 Levent Alpöge 借助 OpenAI 和 Anthropic 的 AI 工具在该问题上取得了重大进展，他们指控 OpenAI 在未署名的情况下使用了其尚未公布的研究成果，并抓取其数据用于训练模型。 如果得到确认，这将是 AI 首次解决一个重大未解数学难题，而且是被克雷数学研究所列为千禧年数学问题之一的难题，对 AI 辅助数学研究具有里程碑意义。与此同时，这场争议把训练数据来源、研究者署名以及使用未发布成果的伦理问题推到了 AI 研究界的风口浪尖。 OpenAI 表示此次攻坚投入了数百万美元算力，并否认依赖 Buckmaster 和 Alpöge 的最新成果；而 Buckmaster 已公开发表声明质疑这一说法，纽约大学团队则指控 OpenAI 抓取其数据用于训练，该结论本身也尚未经过同行评审。同一则新闻汇总还提到另一份报告：LG 智能电视即使在离线或待机状态下也会持续记录并上传用户数据；LG 对此予以否认，称仅在用户按下遥控器语音按钮或识别出“Hi LG”等唤醒词后才处理语音数据，其自动内容识别（ACR）功能也需用户选择开启。

rss · Solidot · Sep 10, 15:51

**背景**: Navier-Stokes 方程在大约 200 年前由法国物理学家克劳德-路易·纳维和爱尔兰物理学家乔治·斯托克斯提出，用于描述液体、空气等流体的运动，至今仍被广泛使用。2000 年，克雷数学研究所把“解是否始终存在且光滑”（即存在性与光滑性问题）列为七个千禧年数学问题之一，每个问题悬赏 100 万美元。所谓 AI 智能体（agentic AI）指的是能够自主追求目标、调用软件或工具并采取行动的人工智能程序，与只完成单一任务的问答式聊天机器人不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Navier-Stokes`, `#agentic systems`, `#research ethics`, `#privacy`

---

<a id="item-10"></a>
## [开发者发现 220 美元 Google Ads 应用安装中 60%来自机器人](https://dayzlegame.com/blog/google-ads-bot-farm/) ⭐️ 7.4/10

一位开发者发布博客，记录了对一次花费 220 美元的 Google 应用安装广告投放的调查，结论是约 60%的安装量来自机器人而非真实用户。该文章在 Hacker News 上引发广泛讨论，其亮点在于用一笔小额真实花费配合数据证据来揭示欺诈，而不是泛泛而谈。 广告欺诈直接消耗独立开发者和早期创业公司的预算，而他们往往依靠付费安装来启动增长；这个案例表明即便只有 220 美元的小额投放，也可能大部分是假量。这加大了对 Google 等广告平台的压力，要求其解释为何大量无效流量能绕过过滤机制，同时也加深了业界对以 CPI（按安装付费）为基础的用户获取策略的怀疑。 该分析总体上偏 anecdotal（案例描述），统计严谨性不足，但 Hacker News 讨论提供了具体缓解措施：一位评论者建议从后台导出可疑 IP，并通过 Google Ads > Admin > Account Settings > IP Exclusions 屏蔽整个网段或数据中心 IP 段，并称仅美国就有超过 4000 个被封网络。另一位评论者讲述了一个讽刺案例：有开发者为了推广自己的应用购买了 Google Ads，结果其 AdMob 账号却因无效流量被封禁。

hackernews · nickabe · Sep 11, 18:24 · [社区讨论](https://news.ycombinator.com/item?id=49662990)

**背景**: 移动广告欺诈常见形式包括点击注入（click injection）——恶意应用检测到新安装后触发虚假点击以窃取归因——以及设备农场或机器人农场（device/bot farm）：用几十上百台真实手机、真实网络制造虚假安装与互动，因为流量看起来是合法的，基础过滤很难识别。按安装付费（CPI）广告的投放者是主要受害者，因为他们为每一次归因安装付费，无论用户是否真人。常见的反欺诈手段包括 IP 排除列表、流量来源审计以及第三方无效流量检测工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.g2.com/click-injection">What Is Click Injection? How It Works and How to Stop It - G2</a></li>
<li><a href="https://www.trafficguard.ai/blog/cell-phone-bot-farm">What is a bot farm? The advertiser's guide to bot fraud (2026)</a></li>
<li><a href="https://adex.com/blog/device-farm-fraud-real-phones-fake-installs/">Device Farm Fraud: Real Phones, Fake Installs - adex.com</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持同情态度并对平台表示怀疑：有人称 Google 和 Meta 的广告就是"骗局"，也有人认为 Google 完全有能力检测广告欺诈，只是在对自己有利时选择视而不见。另一些人则给出实用建议，分享了屏蔽 4000 多个网络 IP 的排除流程；还有读者表示这篇文章反而促使自己下载并试玩了该应用，并称赞其界面干净清爽，无意中成了一次成功的营销。

**标签**: `#ad-fraud`, `#google-ads`, `#mobile-marketing`, `#bot-detection`, `#startup-growth`

---

<a id="item-11"></a>
## [Calif Research 声称用 AI 打造微信通话零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 7.4/10

Calif Research 发布了 WeWorm 的演示，称这是首个通过微信通话在 iOS 与 Android 之间传播的零点击蠕虫；该团队声称借助 AI 在大约两天内定位漏洞并写出首个远程代码执行（RCE）利用程序，再用约一周时间完成整个蠕虫。Simon Willison 直接引用了这一公告，将其视为 AI 辅助安全研究能力提升的重要信号。 如果这一说法成立，就意味着 LLM 辅助工具能把过去需要更大团队耗时数月的工作压缩到大约一周，从而显著降低开发跨平台零点击恶意软件的门槛。这直接关系到微信庞大用户群的安全，也意味着当 AI 辅助漏洞挖掘变得普遍后，防御方修补此类漏洞的速度必须大幅加快。 公告强调受害者无需接听电话，甚至完全不需要触碰手机；即便接听，也听不到任何声音，攻击依然成功。该内容以演示形式发布，没有 CVE 编号、没有补丁状态，也没有第三方独立验证，而引用它的帖子本身并未补充技术分析或风险提示。

rss · Simon Willison · Sep 10, 00:56

**背景**: 零点击利用（zero-click exploit）指无需用户任何操作即可攻陷设备，比需要点击或下载的传统钓鱼式攻击隐蔽得多。远程代码执行（RCE）是一类允许攻击者在远程机器上运行任意代码的漏洞，而蠕虫（worm）是能够无需人工干预自行在设备或网络间传播的恶意软件；三者叠加就形成“自我传播 + 零交互”的入侵方式，在过去往往需要资源充足的团队投入数月。微信通话是被数亿人使用的通信渠道，因此仅靠拨打一通电话就能触发的漏洞严重性格外突出；而借助大型语言模型加速漏洞挖掘与利用程序开发，正是“AI 辅助安全研究”这一新兴实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.f5.com/glossary/zero-click-attack">Zero - click attack | F5</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/remote-code-execution/">What is Remote Code Execution (RCE)? | CrowdStrike</a></li>
<li><a href="https://www.nozominetworks.com/blog/p2pinfect-worm-evolves-to-target-a-new-platform">P2PInfect Worm Evolves, Targeting a New Platform</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#zero-click-exploit`, `#llm-assisted-development`, `#wechat`, `#vulnerability-research`

---

<a id="item-12"></a>
## [基于 Go 的可改造终端编辑器 Rune 正式开源](https://rune.build/blog/rune-is-now-open-source) ⭐️ 7.2/10

用 Go 编写的键盘驱动型终端开发环境 Rune 已在其博客上宣布正式开源。与此同时，项目还公布了一项计划：参与贡献的人将获得一份合同权利，可分享 Rune 所产生的收入。 一款全新的、可改造的 Go 终端编辑器为程序员提供了 Vim、Emacs、Neovim 等成熟工具的替代选择，而开源则让用户可以审视并修改这一工具。其收入分享方案也使它成为检验开源项目如何在声誉之外为贡献提供资金与激励的试验案例。 Rune 定位为一款运行在终端内的快速键盘驱动 IDE，将命令提示符、控制台、可无限拆分的终端面板和语言工具整合在同一套快捷键之下。它通过一台带有自有加密方案的协调服务器在多台机器间同步工作，有用户认为这带来了信任问题，宁愿改用 Tailscale 或纯 SSH 来解决。

hackernews · ernestrc · Sep 11, 15:31 · [社区讨论](https://news.ycombinator.com/item?id=49660149)

**背景**: 终端编辑器是在命令行 shell 内而非图形窗口中运行的文本编辑器，Vim 和 Emacs 等老牌工具以速度和可扩展性著称，但学习曲线陡峭。Rune 用 Go 编写，而 Go 以易于交叉编译和部署简单闻名，项目面向的是想要一款现代、可改造替代方案的用户。该项目的网络功能和贡献者收入分享模式，正是早期用户关注和质疑最多的两个方面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rune.build/blog/rune-is-now-open-source">Rune is now open source. Rune Blog</a></li>
<li><a href="https://rune.build/">Rune — The development environment for pros</a></li>
<li><a href="https://docs.rune.build/">Rune: The development environment for pros</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对这款可改造的 Go 编辑器表示期待，一位 Vim 用户称赞了上手体验，但也有人指出它与 fish shell 自带的 Vim 键位存在冲突。反复出现的批评针对其多机网络功能：用户不愿信任 Rune 的协调服务器，并询问能否改用 Tailscale 或 SSH。最尖锐的反对针对收入分享方案，一位评论者认为直接为贡献付费会招来类似 Hacktoberfest 和 AI 生成 PR 那样的低质量提交。

**标签**: `#Open Source`, `#Developer Tools`, `#Code Editor`, `#Go`, `#Terminal`

---

<a id="item-13"></a>
## [OpenAI 将 Habitat 存储扩展至 10 亿用户，每秒 2200 万请求](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 7.0/10

OpenAI 发布了一篇工程博客，讲述其内部存储系统 Habitat 如何从一个连接单一数据库的简易 Python 客户端库，演进为全球分布的存储平台。文中称 Habitat 目前每秒处理约 2200 万次请求，支撑着每周超过 10 亿人使用的产品，覆盖近 40 个地理区域。 OpenAI 罕见地公开了在消费级互联网规模下运行存储系统的一手细节，为基础设施工程师设计需要支撑数十亿用户、每秒数千万请求的系统提供了参照。这也说明，对于大型 AI 产品而言，存储已经和 GPU、模型一样，成为第一梯队的扩展瓶颈。 文章标题中的数字是每秒 2200 万次请求，但同一篇文章中的另一段内容在其他来源的转述里被概括为每秒超过 7000 万次请求，因此具体数值可能因统计口径（单区域与全集群）不同而有所差异。第三方对该文的解读还提到，出于性能考虑，Habitat 正从 Python 迁移到 Rust，考虑到它最初是 Python 库，这一点尤其值得注意。

rss · OpenAI Blog · Sep 11, 10:00

**背景**: Habitat 是 OpenAI 的内部存储层，也就是真正负责保存并提供 ChatGPT 等产品背后数据的软件。分布式存储平台会把数据分散到众多机器和地理区域上，避免单一数据库成为瓶颈，以牺牲简单性换取吞吐量、容错能力和就近访问。所谓“每秒请求数”是衡量这类系统承载流量的标准指标；而 Python 虽然适合快速搭建系统，但在这种规模下通常难以胜任最热路径，这也是许多团队会改用 Rust 等更底层语言重写的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/scaling-storage-one-billion-users-part-one/">Rapidly scaling online storage to serve over 1 billion... | OpenAI</a></li>
<li><a href="https://krivoshein.site/openai-habitat-70-млн-запросов-с-и-rust-вместо-python/">OpenAI Habitat : 70 млн запросов/с и Rust вместо Python</a></li>
<li><a href="https://www.systemdesignhandbook.com/blog/distributed-file-storage/">Distributed File Storage: Architecture, Examples & Benefits</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#distributed-storage`, `#infrastructure`, `#scaling`, `#systems-engineering`

---

<a id="item-14"></a>
## [阮一峰科技周刊第 412 期：禁止 issue，只用 PR](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-412.html) ⭐️ 7.0/10

阮一峰的科技爱好者周刊发布了第 412 期，本期主题是主张项目应禁止使用 issue 追踪器，只接受以 pull request 形式提交的贡献。按照惯例，该期仍为周五发布的精选合集，收录了当周值得分享的科技内容与点评。 这一主题触及开源治理中一个现实争议：公开的 issue 追踪器究竟是在帮助维护者，还是因噪音、重复报告和“理所应当”的索取而加重负担。如果有更多项目采用“只收 PR”或关闭 issue 的策略，将改变新手、缺陷报告者和非程序员用户参与开源项目的方式。 该周刊是精选链接合集，而非原创研究，因此本期主题属于通过所选案例与点评表达的编辑立场，而非正式的实证分析。目前可见的内容仅是周刊开头的导语一句，因此完整一期中的具体论证、所举项目和反例都无法从现有材料中核实。

rss · 阮一峰周刊 · Sep 11, 00:11

**背景**: 阮一峰是中国知名的软件开发者与技术博主，他的《科技爱好者周刊》多年来固定在周五发布，是中文技术圈阅读量最高的周刊之一。本期讨论的争议涉及 GitHub 的两个核心功能：issue 追踪器允许任何人提交缺陷报告和功能请求；pull request（PR）则要求贡献者提交一份具体的代码改动供审核。由于提 issue 成本极低且对所有人开放，而写 PR 需要真正动手写代码，一些维护者认为 issue 区容易招来低质量报告与索取，而强制走 PR 可以筛选出愿意付出劳动的人——代价是把不会写代码的用户排除在外。

**标签**: `#tech-newsletter`, `#open-source`, `#developer-culture`, `#software-engineering`, `#github-workflow`

---