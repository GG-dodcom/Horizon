---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> From 109 items, 11 important content pieces were selected

---

1. [交互式 LLM 注意力可视化工具让机制更直观](#item-1) ⭐️ 8.5/10
2. [Qwen3.8 27B 量化测试：4-bit 表现稳定，1-bit 性能崩溃](#item-2) ⭐️ 8.2/10
3. [AlphaGenome Atlas 绘制 90 亿个人类 DNA 变异的分子效应图谱](#item-3) ⭐️ 8.2/10
4. [前沿 AEO 追踪器：解析 Astra 等 AI 助手的引用来源](#item-4) ⭐️ 8.0/10
5. [本·汤普森：写下来很强大，但目的与行动应优先](#item-5) ⭐️ 7.9/10
6. [OpenAI 宣称用 AI 破解纳维-斯托克斯千禧年问题](#item-6) ⭐️ 7.8/10
7. [Inception 发布 Mercury 2.5 扩散式大模型，智能提升 40%](#item-7) ⭐️ 7.8/10
8. [安全拒绝应针对有害子集，而非整个主题](#item-8) ⭐️ 7.5/10
9. [数学家 Buckmaster 指控 OpenAI 施压 Navier-Stokes 成果](#item-9) ⭐️ 7.4/10
10. [“I-Have-ADHD”技能让 Claude Code 回复直奔主题、不再绕弯](#item-10) ⭐️ 7.0/10
11. [OpenAI 发布 ChatGPT Images 2.5，推出 Sunburst 与 Flare 两个 API 模型](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [交互式 LLM 注意力可视化工具让机制更直观](https://ishamf.dev/p/llm-attention-visualizer/) ⭐️ 8.5/10

一个名为“LLM Attention Visualizer”的交互式网页工具在 Hacker News 上以“Show HN”帖子发布，地址为 ishamf.dev。该工具的目标是通过展示信息如何跨不同层和短语进行组合，使大语言模型中的注意力机制更容易理解。 注意力机制是现代大语言模型的核心，但其内部的加权方式非常抽象，难以凭直觉讲授。这类可视化工具提供了实用的教学辅助，可以改善 AI 教育，并帮助从业者更好地理解模型行为。 该工具在 Transformer 层和短语组合之间展示注意力模式，让人们能以易理解的方式看到跨短语的信息融合。评论者指出，一个潜在的设计问题是：将许多早期层的贡献相加后，后期层的注意力可能显得被稀释。

hackernews · ifz · Sep 8, 16:59 · [社区讨论](https://news.ycombinator.com/item?id=49613068)

**背景**: 大语言模型中的注意力机制决定了模型在生成每个 token 时最关注提示的哪些部分，而不是对每个词一视同仁。许多 LLM 背后的 Transformer 架构由多层结构组成，每一层中每个 token 都通过自注意力与其他 token 进行上下文关联。将这一过程可视化有助于揭开模型做出特定预测的神秘面纱，对初入该领域的学生和开发者尤其有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://medium.com/@QuarkAndCode/attention-mechanism-in-llms-explained-in-simple-terms-f9cd7d5278c2">Attention Mechanism in LLMs Explained in Simple Terms | Medium</a></li>
<li><a href="https://www.youtube.com/watch?v=XN7sevVxyUM">Lecture 13: Introduction to the Attention Mechanism in Large ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多非常正面：一位老师表示正好赶上周五上课时使用，一位有经验的读者称这是他们见过的关于注意力最清晰的示例。另有较深入的技术问题指出，累加时早期层的大量贡献是否会淹没后期层的注意力模式；其他人则简短地表达了喜爱。整体而言，讨论称赞了该工具的教学价值，同时提出了一个值得思考的概念局限。

**标签**: `#LLM`, `#Attention Mechanism`, `#Visualization`, `#AI Education`, `#Developer Tools`

---

<a id="item-2"></a>
## [Qwen3.8 27B 量化测试：4-bit 表现稳定，1-bit 性能崩溃](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 8.2/10

一项针对 Qwen3.8 27B 在不同量化级别下的基准测试显示，4-bit 量化能较好地保持模型质量，而 1-bit 量化的性能则严重崩溃。这些结果为本地部署该模型时选择合适的量化档位提供了实用参考。 量化是在消费级硬件上运行大型语言模型的关键手段，因为内存限制迫使开发者在质量、上下文长度和速度之间做出取舍。这项测试表明 4-bit 仍然可靠而 1-bit 不可用，能帮助开发者选择更实用的部署方案，也揭示了极端低比特量化的局限性。 该测试中，量化到 4-bit 时质量差异仍然很小，2-bit 分数有所下降，而 1-bit 则大幅崩溃。由于这是针对单一模型得出的结果，用户仍需在自己的任务上验证质量拐点；此外评论区指出缺少 Q3（约 3-bit）档位的数据，而这正是 16GB 以下显存显卡所关心的区间。

hackernews · stared · Sep 8, 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49611128)

**背景**: 量化是一种模型压缩技术，它将 LLM 的权重和激活从高精度表示（如 16-bit 浮点数）转换为 4-bit 或 1-bit 等低精度整数，从而减少内存占用并加快推理速度，但通常会以一定精度损失为代价。Qwen 是阿里巴巴云开发的开源大语言模型系列；27B 这类模型规模较大，在本地 GPU 上运行时通常需要量化，以保证推理在硬件资源内可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/quantization-for-large-language-models">Quantization for Large Language Models (LLMs): Reduce... | DataCamp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**社区讨论**: 评论区总体上肯定这项测试的价值，但 spider-mario 批评文章使用 Wilson 置信区间来衡量运行间波动并不恰当。sharmajai 猜想 Qwen3.8 27B 会通过更长的推理思考来弥补量化带来的噪声；也有读者希望看到 KV cache 量化的类似测试，指出缺少对 16GB 以下显卡很关键的 Q3 档位数据。Farmadupe 则询问如何判断文章是否部分由 AI 撰写。

**标签**: `#LLM quantization`, `#benchmarking`, `#inference`, `#local LLM`, `#Qwen`

---

<a id="item-3"></a>
## [AlphaGenome Atlas 绘制 90 亿个人类 DNA 变异的分子效应图谱](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) ⭐️ 8.2/10

DeepMind 发布了 AlphaGenome Atlas，这是一个预测性目录，映射人类基因组中全部 90 亿个可能的单核苷酸变异的分子效应与 AVI 分数。该图谱基于 AlphaGenome 构建，这项被《Nature》论文描述的统一 DNA 序列模型，可单次输入 1 Mb 的 DNA 片段。 这是一个覆盖全基因组的综合性变异效应预测图谱，不仅涵盖蛋白编码区，还包括约占基因组 98% 的非编码区。它有望加速疾病相关变异的解读、支持临床基因组学与药物研发，并为人工智能驱动的生命科学研究树立新基准。 该图谱为人类基因组中的每一个单字母 DNA 改变都赋予一个 AVI（AlphaGenome 变异影响）分数。AlphaGenome 被描述为一个 DNA 序列模型，能够同时跨多种模态对变异效应进行评分，克服了以往输入序列长度与预测分辨率之间的权衡，DeepMind 还提供了从序列生成基因组轨道及变异效应预测的工具。

rss · DeepMind Blog · Sep 8, 14:00

**背景**: 人类基因组包含约 30 亿个 DNA 碱基对，但其中只有约 2% 编码蛋白质基因；其余 98% 是非编码区，在调控基因活性方面发挥重要作用。单核苷酸变异是指特定位置上单个 DNA 字母的改变，而变异效应预测器是一类计算工具，用于估计这类改变如何影响分子功能或疾病风险。此前的工具往往只擅长编码区或非编码区，例如有人用蛋白质语言模型预测 4.5 亿个错义变异；AlphaGenome 则将这种思路扩展到全基因组范围的调控区和非编码 DNA。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-10014-0">Advancing regulatory variant effect prediction with AlphaGenome | Nature</a></li>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas: Molecular predictions for 9 Billion human DNA variants — Google DeepMind</a></li>
<li><a href="https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/">AlphaGenome: AI for better understanding the genome — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#DeepMind`, `#genomics`, `#AI for science`, `#variant effect prediction`, `#human genome`

---

<a id="item-4"></a>
## [前沿 AEO 追踪器：解析 Astra 等 AI 助手的引用来源](https://www.latent.space/p/aeo) ⭐️ 8.0/10

Latent Space 推出了一个答案引擎优化（AEO）追踪器，首份报告聚焦 Project Astra，用于监测 Astra 等前沿 AI 助手会选择哪些信息源。该项目还为创始人和开发者体验负责人提供了实用的行动指南。 随着 AI 助手日益取代传统搜索引擎，被这些引擎引用对企业与内容创作者变得至关重要。该追踪器提供了数据驱动的 AEO 趋势视角，帮助团队据此调整内容与开发者体验策略。 首份报告聚焦于 Google DeepMind 的 Project Astra——一个迈向通用 AI 助手的研究原型，目前以 Gemini Live 的形式在 Android 和 iOS 设备上可用。选择该主题是因为它是 Latent Space 社区的创始人与开发者体验（DX）负责人最常提出的问题之一。

rss · Latent Space · Sep 7, 21:32

**背景**: 答案引擎优化（AEO）是指优化内容和品牌，使其出现在 ChatGPT、Gemini 和 AI Overview 等引擎的 AI 生成回答中。前沿 AI 模型是当前最先进的 AI 系统，不断突破推理能力与任务复杂度的边界。随着越来越多用户依赖 AI 助手获取答案，这些模型选择引用的信息源将直接影响企业的可见度与网站流量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.seo.com/ai/answer-engine-optimization/">Answer Engine Optimization (AEO): What It Is & How to Start</a></li>
<li><a href="https://deepmind.google/models/project-astra/">Project Astra — Google DeepMind</a></li>
<li><a href="https://www.brinqa.com/glossary/frontier-ai-models">Frontier AI Models : Definition & Security Impact</a></li>

</ul>
</details>

**标签**: `#Answer Engine Optimization`, `#AI assistants`, `#LLM applications`, `#Frontier models`, `#Developer experience`

---

<a id="item-5"></a>
## [本·汤普森：写下来很强大，但目的与行动应优先](https://stratechery.com/2026/write-things-down/) ⭐️ 7.9/10

Stratechery 的本·汤普森发表了《Write Things Down》，认为书写对人类和 AI 都很强大。但他强调，决定写什么、明白为什么写，以及真正把事情做成，必须先于“写下来”这个动作。 这一论点对知识工作者很重要，因为越来越多的人将自己的笔记和文档交给 AI 助手，而这些材料的价值取决于当初为何写、怎么写。它也反驳了一种流行观念：只要记录更多文字，人类记忆或 AI 输出就会自动变得更好。 这篇文章没有介绍新技术工具或数据，而是一个关于做事流程的概念性论述。汤普森把执行和目的性放在记录之前，暗示书写只是手段，本身并非目的。

rss · Stratechery · Sep 8, 10:00

**背景**: 对人类来说，书写是一种外部记忆；对 AI 系统来说，书写内容则是可检索的上下文或素材来源。但写出来的东西是否有用，取决于写作者是否有清晰目的，以及是否真正执行了相关事项。这正是该文强调“先决定写什么、为什么写、并先把事情做成”的前提。

**标签**: `#writing`, `#AI`, `#knowledge management`, `#productivity`

---

<a id="item-6"></a>
## [OpenAI 宣称用 AI 破解纳维-斯托克斯千禧年问题](https://openai.com/index/navier-stokes-solution/) ⭐️ 7.8/10

OpenAI 在一篇博文中宣布，其一个尚未发布的内部模型给出了三维纳维-斯托克斯方程解可在有限时间形成奇异性的证明。该公司表示，该结果已在 Lean 证明助手中形式化，确立了 Fefferman 对“纳维-斯托克斯存在性与光滑性”千禧年大奖难题之官方表述中的陈述 C 和 D。 如果该证明获得验证，那将是数学史上的里程碑，而由 AI 产出的证明也表明大语言模型能为前沿数学研究作出实际贡献。但这一声明尚未得到验证，且被质疑利用了其他研究者未发表的工作，并引发了关于“炒作”以及 AI 辅助发现应该如何归属的争论。 根据博文，该证明表明，在光滑外力作用下的光滑、有限能量三维不可压缩流动可在有限时间内产生奇异性，从而为“始终光滑”的说法提供反例。公告包含 Lean 证明助手的形式化内容，同时出现了优先权争议：两位数学家（其中一位任职于 Anthropic）此前已得出证明中所用的欧拉方程相关结果；在公告发布时，克莱数学研究所尚未独立验证该证明。

hackernews · OpenAI Blog · Sep 8, 17:13 · [社区讨论](https://news.ycombinator.com/item?id=49613262)

**背景**: 纳维-斯托克斯方程描述空气、水等粘性流体的运动，在工程和物理学中应用广泛；然而，三维光滑解是否能永远存在，还是会在有限时间内发生爆破，长久以来未被证明。这一问题被称为“纳维-斯托克斯存在性与光滑性”问题，是克莱数学研究所于 2000 年选定的七个千禧年大奖难题之一，每个难题的正确解答可获得一百万美元奖金。截至 2026 年，庞加莱猜想是唯一获官方承认解出的千禧年难题；OpenAI 表示，即使当前这一声明最终得到验证，他们也将放弃领取该奖金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者大多持警惕态度：部分人认为该成果可能基于另一位研究者的结果和提示（prompts），并附上个人声明与优先权争议链接；另一些人则引用陶哲轩的警告，称 AI 驱动的研究可能在人类研究者完成课题之前就“碾平”问题，从而抑制开放交流。也有少数人指出其中体现的能力提升本身惊人——一位评论者称 OpenAI 表示一个训练不到两周的模型在数学能力上是刚刚公开一周的 Astra 的两倍以上——但许多人仍对炒作和整体科研文化深感怀疑。

**标签**: `#OpenAI`, `#Navier-Stokes`, `#mathematics`, `#AI research`, `#research ethics`

---

<a id="item-7"></a>
## [Inception 发布 Mercury 2.5 扩散式大模型，智能提升 40%](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) ⭐️ 7.8/10

Inception Labs 推出了通用扩散式大语言模型 Mercury 2.5，运行速度约为每秒 1,100 tokens，智能水平比 Mercury 2 提升约 40%。该模型已通过 Inception API 和 OpenRouter 提供。 此次发布标志着基于扩散架构的大语言模型正走向成熟，不再局限于语音等小众场景，而是成为快速、低成本的通用模型。对延迟敏感型智能体开发者尤其有利，例如需要快速仲裁模型的多模型流水线。 Inception 称 Mercury 2.5 是市场上最强大的扩散式 LLM；有评论者将其与 GPT-5.6 Luna (Low)、Gemini 3.5 Flash-Lite、Claude Haiku 4.5 等成本优化前沿模型并列。该模型未开放权重，API 用户可通过关闭“Improve the model for everyone”选项，选择不让自己的提交内容参与模型训练。

hackernews · Topfi · Sep 8, 20:14 · [社区讨论](https://news.ycombinator.com/item?id=49616354)

**背景**: Mercury 2.5 由 Inception Labs 开发。这家总部位于帕洛阿尔托的公司成立于 2024 年，创始人是来自斯坦福、UCLA 和康奈尔、最先开发出扩散式 LLM 的研究者；团队成员也来自 Google DeepMind、Meta AI、Microsoft AI 和 OpenAI。与传统自回归 LLM 逐个 token 预测不同，扩散式 LLM 通过迭代去噪方式生成文本，从而实现更快的并行解码。Inception 已在财富 500 强公司部署这类模型。OpenRouter 是一个统一 API 网关，可在数百个模型之间路由请求，Mercury 2.5 也已上架该平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inceptionlabs.ai/blog/introducing-mercury-2-5">Introducing Mercury 2.5 – Inception</a></li>
<li><a href="https://www.businesswire.com/news/home/20260908593295/en/Inception-Launches-Mercury-2.5-the-Next-Tier-of-Intelligence-for-Diffusion-LLMs">Inception Launches Mercury 2.5, the Next Tier of Intelligence ...</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的整体情绪积极而克制：有评论认为 Inception 是值得关注的新实验室之一，并称 Mercury 2.5 Preview 虽未达到前沿水平，但已可当通用聊天机器人使用。主要遗憾是模型没有开放权重。也有开发者认为约 1,100 tokens/秒的速度极具价值，能大幅降低 llm-consortium 这类多模型系统中仲裁模型的延迟。

**标签**: `#LLM`, `#Model Release`, `#Inference Speed`, `#OpenRouter`, `#AI Tools`

---

<a id="item-8"></a>
## [安全拒绝应针对有害子集，而非整个主题](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 7.5/10

Hugging Face 上的一篇来自 MultiverseComputingCAI 的博客文章主张，安全拒绝机制应当具有更细的粒度：模型应只拒绝某一主题中真正有害的特定子集，而不是拒绝整个主题。文章认为，按子集而非整题来执行拒绝，可以在维持安全边界的同时保留模型的有用性。 这一讨论直接关系到 LLM 安全对齐与内容审核的实践，因为它触及“安全”与“有用”之间的权衡。如果实现得当，细粒度拒绝可以减少过度拒答（over-refusal），使模型在合法场景下保持可用。 这一论点依赖于模型能否在较宽泛的主题中可靠地区分出有害的子概念。对开放权重模型的研究显示，拒绝行为往往由低维、线性可访问的特征承载，这种特性可能使细粒度拒绝在技术上变得可行。

rss · Hugging Face Blog · Sep 8, 14:23

**背景**: LLM 对齐（LLM alignment）是指通过训练或微调，使大语言模型的输出安全、准确且符合人类价值观。当前的对话模型通常会经过训练，对被认为有害或不恰当的请求加以拒绝，常见做法是学习诸如“用户：不当请求；AI：详细道歉”这样的示例。然而，拒绝机制可能过于粗糙，导致模型回避整个主题，而不只是其中危险的部分。这篇博客关注的正是安全拒绝中这种细粒度区分的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/llm-alignment">What Is LLM Alignment? | IBM</a></li>
<li><a href="https://zentara.co/blog/llm-refusal-behavior/">LLM Refusal Behavior on Open-Weight Model</a></li>
<li><a href="https://www.lesswrong.com/posts/Dan6iKFruioYmZafw/thoughts-on-refusing-harmful-requests-to-large-language">Thoughts on refusing harmful requests to large language models</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#LLM alignment`, `#refusal behavior`, `#content moderation`, `#Hugging Face`

---

<a id="item-9"></a>
## [数学家 Buckmaster 指控 OpenAI 施压 Navier-Stokes 成果](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 7.4/10

Tristan Buckmaster 发表在线声明，指控 OpenAI 对他和 Anthropic 研究员 Levent Alpöge 施加压力，涉及他们与 Navier-Stokes 相关的有限时间爆破工作，并声称 OpenAI 是否利用其见解训练模型存在模糊性。声明还描述了他所称的旨在影响结果呈现方式的提议和警告。 这引发了关于研究伦理、数据隐私以及 AI 公司对学术工作影响日益增大的严重问题。它可能削弱人们对 OpenAI 及类似公司如何处理用户数据以及与独立研究者互动的信任，尤其是在 Navier-Stokes 千禧年大奖难题这样的高风险问题上。 据报道，Buckmaster 和 Alpöge 在不可压缩多孔介质、Boussinesq 方程和三维不可压缩 Euler 方程的有限时间爆破问题上取得了进展，但并未完全证明原始 Navier-Stokes 千禧年问题。OpenAI 承认其“不能排除来自他们使用我们产品所产生的去标识化数据可能帮助改进了我们的模型”，这加剧了模糊性。

hackernews · procedurecall · Sep 8, 05:42 · [社区讨论](https://news.ycombinator.com/item?id=49605915)

**背景**: Navier-Stokes 方程描述流体运动，其解是否总是光滑存在是价值 100 万美元的千禧年大奖难题之一。“有限时间爆破”指解在有限时间内产生奇异性。OpenAI 此前曾用语言模型发现了一个简化版 Navier-Stokes 类似问题的爆破解，但 Buckmaster 的声明引发担忧，即他和 Alpöge 的独立见解可能未经同意而被使用。此前，Buckmaster 和 Vicol 的工作利用凸积分方法证明了原始方程有限能量弱解的不唯一性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf">Finite time blowup for navier – stokes</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对 OpenAI 表示愤怒，指责其未经同意使用研究人员的工作，并通过威胁压制独立的研究成果。也有人对模糊的证据是否足以谴责 OpenAI 表示怀疑，但许多人认为这反映出大型 AI 公司在用户数据和学术诚信方面存在有问题的一贯行为。

**标签**: `#Navier-Stokes`, `#research ethics`, `#OpenAI`, `#AI data privacy`, `#mathematics`

---

<a id="item-10"></a>
## [“I-Have-ADHD”技能让 Claude Code 回复直奔主题、不再绕弯](https://github.com/ayghri/i-have-adhd) ⭐️ 7.0/10

GitHub 上发布了一个名为“I-Have-ADHD”的开源技能，旨在让 Claude Code 这类编程代理用简洁的方式回答，不再把关键信息埋在长篇回复里。该项目在 Hacker News 上引发了一场关于 Claude 冗长写作风格的讨论。 许多开发者把 Claude Code 当作代理式编码工具使用，而冗长输出会拖慢代码审查并掩盖重要改动。这个技能反映了一种生态趋势：在提示词层面采用“土办法”，对抗模型厂商尚未在默认行为中修复的毛病。 Hacker News 讨论中展示的安装方式是把提示词粘贴到 Claude Code 里，让它去读取仓库中的 AGENTS.md 文件，技能/插件的指令就存放在该文件中。有评论者指出，除非不断强化，效果通常只能维持几轮对话；还有人建议用 hook 对每条回复强制生效。

hackernews · domhudson · Sep 8, 14:13 · [社区讨论](https://news.ycombinator.com/item?id=49610631)

**背景**: Claude Code 是 Anthropic 开发的代理式编码工具，运行在终端中：它能读取代码库、修改文件、执行命令，并与开发工具集成。“技能”（Skill）是一种附加指令，用来定制这类代理的行为。这场讨论围绕着“Claudisms”展开，也就是 Claude 输出中反复出现的话语与结构毛病，例如“不是这个而是那个”的句式、不必要的分词短语，以及把重点埋藏在后文等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/wespomeroyny/claudisms/blob/main/claudisms.md">claudisms/claudisms.md at main · wespomeroyny/claudisms</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者普遍认同这一痛点：有人说“Claude 写作很差”，还有人尤其讨厌它总爱强调自己“没有”做什么。另一些人则对效果能否持久表示怀疑，称该技能只能维持几轮对话，之后 Claude 又会变得啰嗦。还有用户提醒，对通过复制粘贴提示来安装技能的做法应保持警惕。

**标签**: `#AI`, `#LLM`, `#Claude Code`, `#coding agents`, `#developer tools`

---

<a id="item-11"></a>
## [OpenAI 发布 ChatGPT Images 2.5，推出 Sunburst 与 Flare 两个 API 模型](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.0/10

OpenAI 发布了 ChatGPT Images 2.5，改进了多轮指令遵循、提升了响应速度，并更好地保留参考照片中的主体。同时还推出了两个新的 API 模型 ID：gpt-image-2.5-sunburst（用于精细编辑）和 gpt-image-2.5-flare（用于快速日常生成）。 本次发布之所以重要，是因为 OpenAI 声称其图像生成模型已被用于创建超过 30 亿张图像，而新的模型选择为开发者提供了在速度与编辑精度之间更清晰的取舍。对于正在将文生图或图像编辑功能集成到产品中的构建者而言，这一点尤其相关。 Sunburst 模型为细致创意工作提供更高的精确度，但生成时间更长；Flare 则被定位为快速、高质量日常生成的默认选项。根据 OpenAI 的 API 文档，gpt-image-2.5-sunburst 的图像输出价格为每百万 token 30 美元。Simon Willison 还升级了自己的 openai_image.py CLI 工具来支持参考图像，演示了在一张现有图表中加入一只浣熊科学家。

rss · Simon Willison · Sep 8, 22:46

**背景**: ChatGPT Images 是 OpenAI 的图像生成产品，既可通过 ChatGPT 使用，也可以通过 OpenAI API 中的 GPT-Image 模型使用。这些模型能够根据自然语言提示生成图像，并在编辑或转换现有图像时尽量保留参考照片中的关键主体。指令遵循指模型服从多轮提示的能力，而主体保留则指模型在编辑过程中保持输入图像中人物、物体或风格不变的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-5/">Introducing ChatGPT Images 2.5 | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst">GPT-Image-2.5 Sunburst Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#image generation`, `#API`, `#AI models`, `#Simon Willison`

---