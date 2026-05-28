---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 109 items, 29 important content pieces were selected

---

1. [BioHub 的 ESMC-6B 和 ESMFold2 推动蛋白质 AI 发展](#item-1) ⭐️ 9.5/10
2. [细品《创：战纪》中的 Shell 命令历史](#item-2) ⭐️ 9.3/10
3. [Reachy Mini 实现完全本地化离线对话](#item-3) ⭐️ 9.2/10
4. [ITBench-AA：前沿 AI 模型在企业 IT 基准测试中表现欠佳](#item-4) ⭐️ 9.0/10
5. [异步智能体：Cognition 的 Devin 与 OpenInspect 的探索](#item-5) ⭐️ 9.0/10
6. [TRL 中的增量权重同步实现万亿参数模型训练](#item-6) ⭐️ 8.5/10
7. [Anthropic 与 OpenAI 实现产品-市场契合](#item-7) ⭐️ 8.4/10
8. [Eric Seufert 访谈：AI 模型、广告与人类未来](#item-8) ⭐️ 8.4/10
9. [LLM 写作气味：检测 AI 生成文本的模式](#item-9) ⭐️ 8.3/10
10. [从零构建 AI Agent 的经验教训](#item-10) ⭐️ 8.3/10
11. [YouTube 将自动标记 AI 生成的视频](#item-11) ⭐️ 8.2/10
12. [SQLite 发布针对 AI 代理的 AGENTS.md 政策](#item-12) ⭐️ 8.2/10
13. [AI GDP 估计达 2500 亿美元，年增长率超 2000%](#item-13) ⭐️ 8.2/10
14. [Claude Code v2.1.154：Opus 4.8、动态工作流等新功能](#item-14) ⭐️ 8.1/10
15. [避免被 AI 取代的七种方法](#item-15) ⭐️ 8.1/10
16. [Anthropic 发布 Claude Opus 4.8 并预告 Mythos 级模型](#item-16) ⭐️ 7.9/10
17. [用 Postgres 作为持久化工作流引擎](#item-17) ⭐️ 7.9/10
18. [Claude Code v2.1.153 发布，新增 Git LFS 跳过选项和多项修复](#item-18) ⭐️ 7.8/10
19. [LiteLLM v1.86.2 加强 Docker 镜像验证](#item-19) ⭐️ 7.8/10
20. [Claude Code v2.1.152：新增 /code-review --fix、钩子增强与插件市场](#item-20) ⭐️ 7.7/10
21. [奥特曼和阿莫代伊收回 AI 就业末日预言](#item-21) ⭐️ 7.7/10
22. [curl 团队被 AI 辅助安全报告淹没](#item-22) ⭐️ 7.6/10
23. [AI 炒作反噬：埃里克·施密特毕业典礼遭嘘](#item-23) ⭐️ 7.6/10
24. [利用 Codex 构建自我改进的税务代理](#item-24) ⭐️ 7.5/10
25. [Anthropic 650 亿美元 H 轮融资，估值 9650 亿美元](#item-25) ⭐️ 7.3/10
26. [Vercel AI SDK 预览版引入流转换辅助函数](#item-26) ⭐️ 7.0/10
27. [LiteLLM v1.87.0-rc.2 增加 Cosign Docker 镜像验证](#item-27) ⭐️ 7.0/10
28. [OpenAI 发布前沿治理框架](#item-28) ⭐️ 7.0/10
29. [新型提取工艺有望解锁全球锂资源](#item-29) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [BioHub 的 ESMC-6B 和 ESMFold2 推动蛋白质 AI 发展](https://www.latent.space/p/esmfold2) ⭐️ 9.5/10

BioHub 发布了 ESMC-6B，这是一个 60 亿参数的蛋白质语言模型，使用 68 亿蛋白质序列和 11 亿结构进行训练，同时发布了基于扩散的结构预测模型 ESMFold2。 这种蛋白质模型的规模扩展反映了 AI 领域的'苦涩教训'，表明大规模数据和计算可以解锁可编程生物学，对药物设计和合成生物学具有潜在影响。 ESMC-6B 基于 ESM-2 架构但规模更大，ESMFold2 使用扩散方法比 AlphaFold2 更快地折叠蛋白质，同时保持准确性。这些模型还结合了稀疏自编码器（SAE）以提高可解释性。

rss · Latent Space · May 27, 17:46

**背景**: 像 ESM 这样的蛋白质语言模型将氨基酸序列视为一种语言，从数百万序列中学习进化模式。ESMFold2 是 ESMFold 的直接后继，后者实现了快速结构预测。SAE 的使用受到 LLM 中机械可解释性研究的启发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41592-026-03050-9">Compressing the collective knowledge of ESM into a single protein ...</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2506316122">Sparse autoencoders uncover biologically interpretable ... - PNAS</a></li>

</ul>
</details>

**标签**: `#AI for biology`, `#protein folding`, `#ESM`, `#LLM`, `#biotech`

---

<a id="item-2"></a>
## [细品《创：战纪》中的 Shell 命令历史](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/) ⭐️ 9.3/10

Simon Tatham 发表了一篇详细分析电影《创：战纪》中出现的 Shell 命令的文章，评估了这些命令对 Unix/CLI 爱好者的真实性和技术准确性。 该分析突显了即使是大片也可能在 Unix 命令行细节上做对或做错，为开发者提供了一个有趣的参考，并引发了关于电影中技术描绘的讨论。 分析涵盖了诸如 'login -n root'、'whoami' 和 'kill -9' 等命令，并指出 VFX 艺术家可能偏爱 vi 而非 emacs，其中 Dillinger 使用 emacs，Flynn 使用 vi。

hackernews · speckx · May 28, 19:15 · [社区讨论](https://news.ycombinator.com/item?id=48314002)

**背景**: Shell 历史是 Unix Shell 的一个特性，记录用户输入的命令，可通过 'history' 命令访问。在《创：战纪》中，Shell 命令出现在 Flynn 访问计算机的场景中。Simon Tatham（以创建 PuTTY 而闻名）的博客文章检查了这些命令的真实性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fluca1978.github.io/2017/11/21/TronLegacySunOS.html">TRON Legacy: the console prompt</a></li>
<li><a href="https://www.securitronlinux.com/bejiitaswrath/more-tron-legacy-goodness-unix-commands-and-how-they-got-it-right/">More TRON legacy goodness. UNIX commands and how they got it right. – Securitron Linux blog.</a></li>
<li><a href="https://www.cyberciti.biz/faq/linux-unix-shell-history-search-command/">How To Search Bash Shell Command History - nixCraft</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到 vi 与 emacs 的选择是一个有趣的细节，讨论了电影背景下'终止进程'的背景故事，并称赞了 Daft Punk 的原声带。一位评论者指出'login -n root'序列与 CVE-1999-0113 类似。

**标签**: `#shell history`, `#Tron: Legacy`, `#Unix commands`, `#movie accuracy`, `#technical analysis`

---

<a id="item-3"></a>
## [Reachy Mini 实现完全本地化离线对话](https://huggingface.co/blog/local-reachy-mini-conversation) ⭐️ 9.2/10

Hugging Face 使开源桌面机器人 Reachy Mini 能够完全本地运行 AI 模型，实现无需互联网连接的离线对话功能。 这一进展将边缘 AI 部署推进到机器人领域，支持无需云端的私密、低延迟人机交互，对于敏感环境或网络不佳地区的应用至关重要。 该设置可能使用在机器人板载硬件上运行的小型 LLM 或语音模型。博客文章中的具体技术细节会说明确切的模型和硬件要求。

rss · Hugging Face Blog · May 27, 00:00

**背景**: Reachy Mini 是 Hugging Face 推出的全球首款开源桌面机器人，旨在探索人机交互。通常，对话式 AI 依赖于云服务器，而本地推理将数据保留在设备上，增强了隐私并降低了延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reachy-mini.org/">Reachy Mini - World's First Open-Source Desktop Robot</a></li>
<li><a href="https://grokipedia.com/page/Reachy_Mini">Reachy Mini</a></li>

</ul>
</details>

**标签**: `#AI`, `#Robotics`, `#Local Inference`, `#Hugging Face`, `#Edge Computing`

---

<a id="item-4"></a>
## [ITBench-AA：前沿 AI 模型在企业 IT 基准测试中表现欠佳](https://huggingface.co/blog/ibm-research/itbench-aa) ⭐️ 9.0/10

IBM Research 与 Artificial Analysis 联合发布了 ITBench-AA，这是首个针对企业 IT 任务（特别是 Kubernetes 的站点可靠性工程 SRE）评估 AI 智能体的基准测试。结果显示，即使是最前沿的模型得分也低于 50%，凸显了代理型 AI 在实际 IT 运维中的显著能力差距。 该基准测试提供了一种严谨、标准化的方法，用于衡量 AI 智能体处理复杂企业 IT 工作流的能力，这对代理型 AI 在生产环境中的采用至关重要。低于 50%的得分表明，当前模型在关键 IT 任务中缺乏所需的可靠性和自主性，为未来的研究和开发指明了方向。 ITBench-AA 专注于 Kubernetes 事件解决，这是一种常见的 SRE 场景，需要多步推理和工具使用。该基准测试包含超过 25 个真实世界事件，初步结果显示最佳模型（如 Claude 4）得分约为 48%，许多模型低于 30%。

rss · Hugging Face Blog · May 27, 17:20

**背景**: 代理型 AI 是指能够自主感知、推理并采取行动以实现目标的系统，区别于仅生成文本的传统 LLM。企业 IT 运维（如事件响应和系统修复）要求智能体使用多种工具和 API 执行多步骤工作流。以往的基准测试主要集中在通用推理或编码上，缺乏针对特定领域、可操作的智能体评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-research/itbench-aa">ITBench - AA : Frontier Models Score Below 50% on the First...</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/itbench-aa">ITBench - AA Benchmark Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Benchmark`, `#Agentic Systems`, `#Enterprise IT`

---

<a id="item-5"></a>
## [异步智能体：Cognition 的 Devin 与 OpenInspect 的探索](https://www.latent.space/p/cognition) ⭐️ 9.0/10

Cognition 的 Walden Yan 与 OpenInspect 的 Cole Murray 在一场访谈中讨论了异步智能体的未来，重点介绍了 Cognition 的 AI 编码智能体 Devin 以及 OpenInspect 在智能体记忆、规格到 PR 工作流和完整虚拟机环境方面的探索。 随着 AI 编码智能体日益自主化，允许智能体独立处理复杂任务的异步工作流有望大幅加速软件开发周期，并改变工程团队的运作方式。 访谈涵盖了多个主题，包括 80%的提交由 Devin 完成、智能体将规格说明转化为拉取请求的规格到 PR 工作流，以及跨会话保持上下文的智能体记忆的重要性。

rss · Latent Space · May 28, 18:41

**背景**: AI 智能体是能够无需人工干预自主执行任务的系统。Devin 由 Cognition Labs 开发，是一款旨在自主完成编码任务的 AI 辅助软件开发工具。规格到 PR 工作流将传统软件开发生命周期阶段压缩，使智能体能够在一个会话中从规格说明直接生成拉取请求。智能体记忆是指 AI 智能体存储和回忆过去经验以提升性能的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Devin_AI">Devin AI - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-memory">What Is AI Agent Memory? | IBM</a></li>
<li><a href="https://www.propelcode.ai/blog/new-sdlc-spec-to-pr-workflows-coding-agents">The New SDLC: Spec-to-PR Workflows with Coding Agents</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Devin`, `#async agents`, `#coding workflows`, `#software engineering`

---

<a id="item-6"></a>
## [TRL 中的增量权重同步实现万亿参数模型训练](https://huggingface.co/blog/delta-weight-sync) ⭐️ 8.5/10

Hugging Face 在 TRL 库中引入了增量权重同步，以高效同步大规模训练中的模型参数，大幅降低万亿参数模型的内存和带宽开销。 这项创新使研究人员和工程师能够更实际地训练和服务超过万亿参数的模型，减少分布式强化学习设置中的 GPU 空闲时间并提高资源利用率。 增量权重同步通过仅传输稀疏的权重变化而非完整模型副本，利用共享存储桶进行异步发布和获取权重，将传输时间压缩到秒级。

rss · Hugging Face Blog · May 27, 00:00

**背景**: TRL（Transformer 强化学习）是 Hugging Face 的库，用于通过强化学习训练语言模型，常用于微调大型模型。在训练器和推理引擎之间同步权重是大规模训练中的关键瓶颈，增量权重同步通过仅传输权重差异来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/delta-weight-sync">Shipping a Trillion Parameters With a Hub Bucket: Delta Weight Sync in TRL</a></li>
<li><a href="https://huggingface.co/docs/trl/index">TRL - Transformers Reinforcement Learning · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#delta weight sync`, `#TRL`, `#large model training`

---

<a id="item-7"></a>
## [Anthropic 与 OpenAI 实现产品-市场契合](https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything) ⭐️ 8.4/10

Simon Willison 提出，Anthropic 与 OpenAI 已实现产品-市场契合，依据是 Anthropic 即将迎来首次盈利季的传闻，以及企业因 LLM API 使用量激增而面临高额账单的报道。 这表明 AI 公司正从炒作转向可持续商业模式，企业按 API 价格积极为 AI 代理付费，证实了超越消费者订阅的实际价值。 Anthropic 数月前将其企业计划改为 API 定价，OpenAI 于 2026 年 4 月跟进；Willison 个人使用情况显示，他通过订阅计划每月节省近 2000 美元。

rss · Simon Willison · May 27, 16:38

**背景**: 产品-市场契合指产品满足强劲的市场需求，带来快速采用和盈利。大语言模型（LLM）如 Claude 和 GPT 通过 API 和订阅计划提供；编码代理如 Claude Code 和 Codex 是辅助开发者的工具，可生成代码、运行命令和自动化任务。企业计划传统上采用固定费用，但随使用量增长正转向按用量定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#product-market fit`, `#Anthropic`, `#OpenAI`

---

<a id="item-8"></a>
## [Eric Seufert 访谈：AI 模型、广告与人类未来](https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/) ⭐️ 8.4/10

Ben Thompson 采访了 Eric Seufert，讨论了生成式 AI 模型、Meta 的基础模型，以及广告为何是 AI 产生积极社会影响的关键。 这次讨论强调了广告收入如何资助和普及 AI，有可能将其发展引导向广泛的人类利益，而非狭隘的商业利益。 Seufert 认为，理解广告动态对于对 AI 保持乐观至关重要，因为广告支持的模型可以在不直接向用户收费的情况下，让强大的 AI 变得可及。

rss · Stratechery · May 28, 10:00

**背景**: 基础模型是预训练在大量数据上的大规模 AI 模型，如 GPT 和 Meta 的 LLaMA。这些模型可以针对许多任务进行微调。Meta 的 LLaMA 是一个基础大型语言模型，以相对开放的许可证发布，使研究人员能够在其基础上进行构建。本次采访探讨了如何通过广告来可持续地支持这类模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama_(language_model)">Llama (language model) - Wikipedia</a></li>
<li><a href="https://ai.meta.com/blog/large-language-model-llama-meta-ai/">Introducing LLaMA: A foundational, 65-billion-parameter language model</a></li>

</ul>
</details>

**标签**: `#AI`, `#Advertising`, `#Generative AI`, `#Meta`, `#Models`

---

<a id="item-9"></a>
## [LLM 写作气味：检测 AI 生成文本的模式](https://shvbsle.in/various-llm-smells/) ⭐️ 8.3/10

随着 LLM 生成内容的激增，能够识别这类文本对于维护写作、新闻和学术领域的真实性至关重要。 该列表包括对比否定等模式以及“The honest answer:”和“blast radius”等短语，这些被 LLM 过度使用，但并非它们独有。

hackernews · speckx · May 28, 19:02 · [社区讨论](https://news.ycombinator.com/item?id=48313810)

**背景**: 像 GPT-4 这样的大型语言模型由于训练数据偏差和流畅性优化，常常产生具有某些风格习惯的文本。这些“LLM 气味”作为 AI 生成内容的启发式标记，尽管并非确凿证据。

**社区讨论**: 评论者分享了更多模式并就其价值展开辩论：有人认为 LLM 写作仅在读者不擅长的领域显得优越，而其他人则主张使用 LLM 进行批评而非直接生成。还有一种观点认为 LLM 风格已陷入停滞，具体短语如“对比否定”被重点提及。

**标签**: `#LLM`, `#AI-generated text`, `#writing patterns`, `#detection`

---

<a id="item-10"></a>
## [从零构建 AI Agent 的经验教训](https://sspai.com/post/110370) ⭐️ 8.3/10

作者花了两天时间梳理 AI 发展脉络，理解 AI Agent 的能力边界，并分享了从零构建 AI Agent 的实践心得。 这篇文章为有兴趣构建自己 AI Agent 的开发者提供了实用知识，帮助他们了解 Agent 的能力边界，设定合理预期。 这篇文章是一篇实践报告，可能涵盖了 AI 演进、Agent 设计模式以及实际实现步骤等关键概念。

rss · 少数派 · May 28, 07:00

**背景**: AI Agent 是一种能够自主感知环境、制定计划、调用工具并执行多步任务的 AI 系统，无需人类在每一步介入。与传统单轮问答 AI 不同，Agent 具备持续推理、动态决策和工具调用能力。理解这些能力边界对于有效的 Agent 开发至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/h52412224/article/details/158500592">【AI Agent基础 | 第一篇】AI模型的能力边界与分类_ai模型的边界和能...</a></li>
<li><a href="https://www.cnblogs.com/qiniushanghai/p/19664826">AI Agent 完全指南：2026 年核心概念、主流框架、开发实践与选型建议 ...</a></li>
<li><a href="https://www.betteryeah.com/blog/ai-agent-capability-boundary-problem-solving-guide">突破认知！AI智能体能力边界与问题解决方法论完整解读 | BetterYeah A...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Agent`, `#LLM`, `#实践`, `#技术`

---

<a id="item-11"></a>
## [YouTube 将自动标记 AI 生成的视频](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/) ⭐️ 8.2/10

YouTube 宣布将自动标记疑似包含 AI 生成或合成内容的视频，即使创作者未主动披露。据 TechCrunch 报道，该政策于 2026 年 5 月开始推行。 该政策提高了透明度，帮助观众区分真实内容与 AI 生成内容，减少虚假信息传播，保护儿童和老人等易受影响的群体。这为其他平台采用类似的自动标记做法树立了先例。 创作者可以对误标提出申诉，但如果内容使用 YouTube 自有 AI 工具（如 Veo 或 Dream Screen）生成，则无法移除标签。根据 YouTube 博客，明显不现实的内容（如动画或奇幻场景）可豁免标记。

hackernews · nopg · May 27, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48299753)

**背景**: YouTube 自 2024 年 3 月起已要求创作者对逼真的 AI 内容进行披露。新的自动标记功能利用检测技术增加了一层强制措施。AI 内容检测方法通过分析阴影、像素、音频异常和水印来识别合成媒体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/27/youtube-will-now-automatically-label-ai-videos/">YouTube will now automatically label AI videos | TechCrunch</a></li>
<li><a href="https://blog.youtube/news-and-events/disclosing-ai-generated-content/">How we're helping creators disclose altered or synthetic content - YouTube Blog</a></li>
<li><a href="https://mashable.com/article/youtube-ai-generated-content-label-policy-animated-exemption">YouTube now requires some AI-generated videos be labeled, but animated content gets an exemption | Mashable</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一举措，提到家人曾被 AI 生成的新闻和咨询视频欺骗的经历。一些人担忧儿童和老人尤其容易受到自动生成内容的影响。还有人询问音乐是否也会被标记，并指出大量 AI 生成专注音乐频道的问题。

**标签**: `#AI`, `#YouTube`, `#content moderation`, `#labeling`, `#policy`

---

<a id="item-12"></a>
## [SQLite 发布针对 AI 代理的 AGENTS.md 政策](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.2/10

SQLite 在其仓库中添加了一个 AGENTS.md 文件，明确声明不接受代理代码，但欢迎带有可复现测试用例的代理错误报告。该项目还将 AI 生成的错误报告拆分到单独的 SQLite 错误论坛中。 该政策为开源项目如何管理 AI 生成的贡献而不让人类维护者不堪重负树立了明确先例。它也凸显了高效 AI 工具与软件开发中质量控制需求之间日益增长的紧张关系。 关于不接受代理代码的声明中删除了“（目前）”一词，强化了该政策。SQLite 仍然接受人工编写的拉取请求，但需满足法律文件要求和公共领域奉献。

rss · Simon Willison · May 27, 23:44

**背景**: 代理代码是指由 AI 代理在极少人工干预下自主编写的软件，超越了简单的自动补全。随着大型语言模型的进步，AI 代理现在可以独立地规划、编写、测试和修改代码，导致对开源项目的自动化贡献激增。SQLite 是一个广泛使用的嵌入式数据库，拥有严格的质量标准，并要求贡献者将代码置于公共领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/27/sqlite-agents/">sqlite AGENTS.md</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://apiiro.com/glossary/agentic-coding/">What Is Agentic Coding? Risks & Best Practices</a></li>

</ul>
</details>

**社区讨论**: 在 Datasette Discord 上的讨论提到了该政策和新错误论坛的创建，并对 D. Richard Hipp 快速解决问题表示赞赏。总体情绪支持 SQLite 不接受低质量 AI 生成代码的立场。

**标签**: `#sqlite`, `#AI agents`, `#open source`, `#software development policies`

---

<a id="item-13"></a>
## [AI GDP 估计达 2500 亿美元，年增长率超 2000%](https://feeds.feedblitz.com/~/957435731/0/marginalrevolution~AI-in-gdp.html) ⭐️ 8.2/10

Tyler Cowen 估计，2024 和 2025 年美国质量调整后的 AI 生产以每年超过 2000%的速度增长，驱动力来自数据中心、硬件效率和算法进步，名义 AI GDP 约为 2500 亿美元。 这一估计凸显了 AI 快速扩大的经济规模，以及传统 GDP 指标在衡量这一增长时面临的挑战，从而影响政策制定和投资策略。 增长由三个叠加因素驱动：数据中心容量扩张、硬件效率提升以及算法进步（贡献最大）。2500 亿美元的数字是初步估计，将 AI 部门视为一个连贯的经济实体。

rss · Marginal Revolution · May 28, 17:19

**背景**: 质量调整后的生产考虑了产出随时间推移的质量改进，而不仅仅是数量。算法进步指的是 AI 模型和训练方法的创新，能在不增加算力的情况下提高效率。名义 GDP 是按当前价格衡量的产出，未经通胀调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Production_(economics)">Production ( economics ) - Wikipedia</a></li>
<li><a href="https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress">The least understood driver of AI progress | Epoch AI</a></li>
<li><a href="https://medium.com/@harshapatnam/ai-gdp-the-headline-that-everyone-read-and-misunderstood-bf8677d8f652">AI & GDP — The Headline That Everyone Read… and... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论 AI 是最终产品还是中间产品，质疑 GDP 如何捕捉其价值。Scott Sumner 指出国民核算并非为此设计。有人用讽刺性评论如“当然，Jan”表示怀疑，其他人则就测量问题进行技术性讨论。

**标签**: `#AI`, `#GDP`, `#economics`, `#algorithmic progress`, `#data centers`

---

<a id="item-14"></a>
## [Claude Code v2.1.154：Opus 4.8、动态工作流等新功能](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) ⭐️ 8.1/10

Claude Code v2.1.154 引入了 Opus 4.8 模型及其高努力模式，以及动态工作流功能，可协调数十到数百个代理执行任务。同时新增了成本降低的快速模式、改进的系统提示以及多项命令更新。 此版本通过多代理编排和更强模型显著提升了 Claude Code 处理复杂大规模任务的能力，使其成为专业开发者更实用的工具。Opus 4.8 快速模式的成本降低也降低了高性能推理的门槛。 动态工作流允许用户要求 Claude 创建一个工作流，在后台协调数十到数百个代理。Opus 4.8 默认使用高努力模式，并提供 xhigh 选项处理最困难任务；快速模式以标准费率的两倍提供 2.5 倍速度。

github · ashwin-ant · May 28, 18:00

**背景**: Claude Code 是 Anthropic 的命令行 AI 编程助手，集成了 Claude 模型系列。'努力'参数控制思考深度和工具调用次数，级别从低到 xhigh。多代理编排是一种模式，其中编排代理动态地将任务分配给专门的子代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8 \ Anthropic</a></li>
<li><a href="https://kentgigger.com/posts/claude-code-effort-parameter">Claude Code's effort parameter: when to go full send and when ...</a></li>
<li><a href="https://code.claude.com/docs/en/commands">Commands - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#ai-tools`, `#llm-inference`, `#agentic-systems`, `#release-notes`

---

<a id="item-15"></a>
## [避免被 AI 取代的七种方法](https://feeds.feedblitz.com/~/957346427/0/marginalrevolution~Seven-ways-to-avoid-losing-your-job-to-AI.html) ⭐️ 8.1/10

经济学家泰勒·考恩发表专栏文章，提出了七条原则，帮助人们在 AI 冲击下保护职业生涯，强调实验和适应。 随着 AI 自动化许多任务，这篇文章为工作者提供了保持竞争力的实用建议，并给出了适应技术变革的框架。 七条原则之一是进行实验，在药物开发、电池设计或教育等领域测试新想法。文章鼓励成为 AI 生成假设的测试者。

rss · Marginal Revolution · May 27, 05:54

**背景**: AI 和自动化正在迅速改变就业市场，引发了对失业的担忧。许多专家建议工作者培养与 AI 互补而非竞争的能力。泰勒·考恩是一位著名经济学家，经常撰写关于经济趋势和技术的文章。

**标签**: `#AI`, `#job market`, `#career advice`, `#economics`

---

<a id="item-16"></a>
## [Anthropic 发布 Claude Opus 4.8 并预告 Mythos 级模型](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 7.9/10

Anthropic 发布了 Claude Opus 4.8，相比前代有适度但切实的改进，并宣布 Project Glasswing 下的 Mythos 级模型将在未来几周内向所有客户开放。 此次发布表明 Anthropic 在持续渐进改进前沿模型，同时暗示 Mythos 级模型将带来重大飞跃，可能极大提升 AI 在网络安全等领域的应用能力。 Claude Opus 4.8 允许用户在网页界面关闭自适应思考功能，一些社区成员认为这很有用。Mythos 级模型目前正由少数组织在 Project Glasswing 下用于网络安全工作。

hackernews · craigmart · May 28, 16:49 · [社区讨论](https://news.ycombinator.com/item?id=48311647)

**背景**: Anthropic 的 Claude Opus 系列是其能力最强的语言模型系列。新版本 4.8 是继 4.6 和 4.7 之后的又一次小幅更新。Project Glasswing 是一项防御性网络安全计划，使用名为 Claude Mythos Preview 的新型前沿模型，该模型在正式发布前需要更强的安全防护措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/security/2026/05/25/anthropic-to-release-mythos-class-models-to-the-public/5245596">Anthropic to release Mythos-class models to the public</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/anthropic-claude-opus-4-8-release-mythos-class-ai-model-soon/">Anthropic Says a Mythos-Class AI Model Will Be Available Soon</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出，这是 Anthropic 前沿模型首次连续三次小幅版本更新（4.6、4.7、4.8），每次进步有限。一些用户赞赏关闭自适应思考的功能，还有用户分享了图像生成的对比结果，显示更高思考水平下的改进。

**标签**: `#AI`, `#LLM`, `#Claude`, `#Anthropic`, `#Model Release`

---

<a id="item-17"></a>
## [用 Postgres 作为持久化工作流引擎](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 7.9/10

DBOS 的一篇博客文章主张，Postgres 可以作为持久化工作流引擎，利用其事务保证实现崩溃安全执行，从而消除对专用工作流系统的需求。 这很重要，因为许多后端团队目前使用 Temporal 等独立工作流编排器，增加了复杂性和成本。使用 Postgres 统一了数据存储和工作流状态管理，简化了架构，并为许多应用减少了运维负担。 该方法利用 Postgres 的事务完整性和幂等键确保每个工作流步骤只执行一次。但社区评论指出，当数据量达到 TB 级或中间步骤无法序列化时，这种方案可能无法扩展，并且 MySQL 或 CosmosDB 也能提供类似功能。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化工作流通过自动保存关键点进度使程序能够崩溃后恢复，通常由 Temporal 或 Airflow 等专用工作流引擎管理，但需要独立基础设施。Postgres 作为广泛使用的关系型数据库，可以在其事务系统中持久化存储工作流状态，从而充当工作流引擎，简化技术栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://supabase.com/blog/durable-workflows-in-postgres-dbos.md">supabase.com/blog/durable- workflows -in- postgres -dbos.md</a></li>
<li><a href="https://www.restate.dev/what-is-durable-execution">What is Durable Execution? A Definitive Guide | Restate</a></li>

</ul>
</details>

**社区讨论**: 社区成员反应不一：有人称赞了低规模用例的简洁性并分享了多驱动实现，其他人则质疑 Postgres 的独特性，指出扩展性限制，并提及许多工作流步骤无法序列化。

**标签**: `#Postgres`, `#durable workflows`, `#software engineering`, `#database`, `#backend development`

---

<a id="item-18"></a>
## [Claude Code v2.1.153 发布，新增 Git LFS 跳过选项和多项修复](https://github.com/anthropics/claude-code/releases/tag/v2.1.153) ⭐️ 7.8/10

Claude Code v2.1.153 为 Git 插件源引入了 skipLfs 选项以跳过 Git LFS 下载，在状态命令中添加了终端环境变量（COLUMNS、LINES），改进了自动更新通知，并修复了多个问题，包括有状态 MCP 服务器的重连循环和恢复会话时的内存占用过高。 此版本通过减少不必要的大文件下载和改善终端集成来提升开发者效率。对 MCP 服务器和内存使用的修复提高了运行复杂 AI 辅助工作流的可靠性。 值得注意的是，此更新修复了一个回归问题，即没有可选 GET SSE 流的有状态 MCP 服务器会在 tools/list 上循环重连，并解决了在存储了大量会话的机器上恢复会话时内存占用过高（数 GB）的问题。它还修复了子代理 MCP 服务器忽略 strict-mcp-config 和其他策略的问题。

github · ashwin-ant · May 28, 00:52

**背景**: Git LFS（大文件存储）是一种开源 Git 扩展，它用文本指针替换大文件，同时将实际内容存储在远程服务器上，从而减少克隆时间。MCP（模型上下文协议）是一种用于将 AI 应用连接到外部系统的标准化接口，SSE（服务器推送事件）是一种服务器推送技术，可通过 HTTP 实现实时更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-lfs.com/">Git Large File Storage | Git Large File Storage ( LFS ) replaces large ...</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Server-sent_events">Server - sent events - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI tooling`, `#Git LFS`, `#agents`, `#release notes`

---

<a id="item-19"></a>
## [LiteLLM v1.86.2 加强 Docker 镜像验证](https://github.com/BerriAI/litellm/releases/tag/v1.86.2) ⭐️ 7.8/10

BerriAI 发布了 LiteLLM v1.86.2，该版本引入了使用 cosign 验证 Docker 镜像签名的详细文档，提供了两种认证方法：固定的提交哈希和发布标签。 此版本增强了在容器化环境中部署 LiteLLM 的用户的安全性，确保他们拉取的 Docker 镜像的完整性和真实性，这对人工智能基础设施的信任至关重要。 推荐的验证方法使用加密上不可变的提交哈希，而便捷方法使用受仓库规则保护的发布标签；两条命令验证相同的 cosign 公钥。

github · github-actions[bot] · May 27, 16:39

**背景**: Cosign 是 Sigstore 项目下的一个工具，用于容器镜像的签名和验证。它允许用户使用公钥对 Docker 镜像进行加密签名并验证其完整性，防止使用被篡改或恶意的镜像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sigstore.dev/cosign/">Cosign - Sigstore</a></li>
<li><a href="https://seifrajhi.github.io/blog/sign-container-images-docker-cosign-kyverno/">Sign and Verify Container Images with Docker , Cosign , and Kyverno...</a></li>

</ul>
</details>

**标签**: `#litellm`, `#docker`, `#security`, `#cosign`, `#AI tooling`

---

<a id="item-20"></a>
## [Claude Code v2.1.152：新增 /code-review --fix、钩子增强与插件市场](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) ⭐️ 7.7/10

Anthropic 发布了 Claude Code v2.1.152，新增了 /code-review --fix 命令，可将审查建议直接应用到工作区，同时引入了通过 disallowed-tools 前置元数据实现的技能级工具控制、扩展的 SessionStart 和 MessageDisplay 钩子，以及管理员可管理的插件市场白名单功能。 这些功能显著提升了 Claude Code 的代码审查自动化能力，使用户能一键修复问题，同时赋予用户对 AI 工具访问和会话定制的更强控制力，对采用 AI 辅助开发流程的团队尤其有价值。 /code-review --fix 命令现在能直接将效率、简化和复用建议应用到工作区；新的 /simplify 命令会调用 /code-review --fix。技能现在可通过前置元数据禁用特定工具（如 Write 或 Edit），而 pluginSuggestionMarketplaces 设置允许管理员将组织插件市场列入白名单，以提供上下文相关的插件推荐。

github · ashwin-ant · May 27, 01:30

**背景**: Claude Code 是 Anthropic 推出的终端 AI 编程助手。技能是可复用的规则集，通过 YAML 前置元数据定义，可定制 Claude 的行为；钩子是生命周期事件，在会话启动、消息显示等时机触发。本次发布增强了这两项机制，使自动化代码审查更加实用，并赋予管理员对插件建议的更精细控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentpatterns.ai/tools/claude/skill-disallowed-tools/">Skill disallowed-tools Frontmatter: Skill-Layer Tool Denial ...</a></li>
<li><a href="https://allahabadi.dev/blogs/ai/claude-code-skills-frontmatter-complete-guide/">Claude Code Skill Frontmatter: Every YAML Option Explained</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#AI tooling`, `#release notes`, `#code review`, `#dev tools`

---

<a id="item-21"></a>
## [奥特曼和阿莫代伊收回 AI 就业末日预言](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/) ⭐️ 7.7/10

萨姆·奥特曼和达里奥·阿莫代伊近期收回了之前关于 AI 取代大部分工作的预言，缓和了此前末日般的说法。 这一转变可能影响公众对 AI 就业影响的看法和公司决策，可能缓解担忧，但也引发对先前声明诚意的质疑。 收回归因于公众对 AI 日益增长的担忧，皮尤研究显示超过 50%的美国人更担忧而非兴奋。社区成员怀疑这是一种'潜艇式'公关努力，旨在重新定义 AI 的影响。

hackernews · ianrahman · May 28, 19:43 · [社区讨论](https://news.ycombinator.com/item?id=48314363)

**社区讨论**: Hacker News 上的评论者反应不一：有人认为这是经典的潜艇式公关来重新定义 AI 的影响，有人注意到从'取代开发者'到'我们爱开发者'的讽刺转变。还有人认为末日尚未被证伪，只是比预测来得慢。

**标签**: `#AI`, `#jobs`, `#LLM`, `#public perception`, `#PR`

---

<a id="item-22"></a>
## [curl 团队被 AI 辅助安全报告淹没](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 7.6/10

Daniel Stenberg 报告称，curl 项目面临的安全报告数量是 2024 年的 4-5 倍，比 2025 年翻倍，平均每天超过一份，主要归因于 AI 辅助提交。 这一趋势凸显了 AI 生成的安全研究对开源维护者日益增长的负担，可能使项目资源和维护者身心健康承压。 尽管报告数量激增，但发现的漏洞大多为低或中等严重性；最近一次高严重性 curl CVE 发布于 2023 年 10 月。报告现在非常详细，提高了分类处理的难度。

rss · Simon Willison · May 26, 23:48

**背景**: curl 是一个广泛使用的命令行工具和库，用于通过 URL 传输数据，安装在数十亿设备上。该项目由 Daniel Stenberg 领导的小团队维护。AI 辅助安全研究使得生成详细的漏洞报告更加容易，增加了向开源项目提交的报告数量。

**标签**: `#AI`, `#open source`, `#security`, `#curl`, `#software engineering`

---

<a id="item-23"></a>
## [AI 炒作反噬：埃里克·施密特毕业典礼遭嘘](https://www.technologyreview.com/2026/05/28/1138053/the-ai-hype-index-ai-gets-booed-in-graduation-season/) ⭐️ 7.6/10

前谷歌 CEO 埃里克·施密特在亚利桑那大学毕业典礼演讲中，呼吁毕业生帮助塑造 AI，却遭到全场嘘声。 这一事件反映出公众对 AI 炒作的怀疑与厌倦日益增长，尤其是深受 AI 社会影响的年轻一代。 当施密特告诉 2026 届毕业生他们的任务是帮助塑造 AI 时，嘘声响起，显示出科技领袖的乐观与公众情绪之间的巨大鸿沟。

rss · MIT Tech Review · May 28, 09:51

**背景**: AI 炒作指数追踪公众对人工智能的看法。毕业典礼演讲常邀请有影响力的人物，但 AI 的快速发展引发了关于失业、伦理和虚假信息的辩论。

**标签**: `#AI hype`, `#public perception`, `#graduation`, `#Eric Schmidt`, `#AI backlash`

---

<a id="item-24"></a>
## [利用 Codex 构建自我改进的税务代理](https://openai.com/index/building-self-improving-tax-agents-with-codex) ⭐️ 7.5/10

OpenAI、Thrive 和 Crete 使用 Codex 构建了一个自我改进的税务代理，能够自动完成纳税申报、提高准确性并加速工作流程。 这项案例研究展示了大型语言模型在税务准备等复杂领域任务中的实际应用，有望减少人工错误，为专业人员节省大量时间。 该税务代理利用 Codex 生成和完善税务计算代码，并通过自我改进机制（可能使用迭代反馈循环）随时间提高准确性。

rss · OpenAI Blog · May 27, 07:00

**背景**: OpenAI Codex 是一个在源代码上微调的大型语言模型，最初为 GitHub Copilot 提供支持。它能够将自然语言提示转换为可执行代码。本案例研究展示了 Codex 如何专门用于税务自动化，这是一个需要高精度的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://developers.openai.com/codex/models">Models – Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Codex`, `#tax automation`, `#LLM applications`, `#self-improving systems`

---

<a id="item-25"></a>
## [Anthropic 650 亿美元 H 轮融资，估值 9650 亿美元](https://www.anthropic.com/news/series-h) ⭐️ 7.3/10

Anthropic 宣布完成 650 亿美元的 H 轮融资，投后估值达 9650 亿美元。其年化收入已超过 470 亿美元，超越了 OpenAI。 这轮融资标志着 Anthropic 在 AI 竞赛中的主导地位，收入和估值均超越 OpenAI，可能重塑大语言模型提供商的竞争格局。 年化收入 470 亿美元为公司自行报告数据，代表预估的全年收入。估值接近 1 万亿美元，远超典型的独角兽（10 亿美元）标准，可称为“千角兽”。

hackernews · meetpateltech · May 28, 18:09 · [社区讨论](https://news.ycombinator.com/item?id=48313048)

**背景**: Anthropic 是一家专注于开发安全、有益人工智能的 AI 研究公司。年化收入是将当前收入推算至全年的指标，常用于高速增长的公司。H 轮融资此前已有多次融资，反映出投资者对 Anthropic 增长轨迹的信心。

**社区讨论**: 评论者注意到 Anthropic 在收入和估值上超越 OpenAI，部分人质疑年化收入的可靠性。还有人评论公司在达到极高估值后才上市的趋势，称股市为“垃圾场”。“千角兽”一词被用来描述接近 1 万亿美元的估值。

**标签**: `#AI`, `#Anthropic`, `#funding`, `#valuation`, `#LLM`

---

<a id="item-26"></a>
## [Vercel AI SDK 预览版引入流转换辅助函数](https://github.com/vercel/ai/releases/tag/ai%407.0.0-canary.158) ⭐️ 7.0/10

Vercel 发布了 ai@7.0.0-canary.158，该版本公开了独立的流转换辅助函数 toUIMessageChunk、toUIMessageStream 和 toTextStream，并废弃了多个结果方法。 这些辅助函数使开发者能够在不依赖结果对象的情况下将 streamText 流转换为 UI 消息块或文本增量，从而简化了自定义传输和测试。 废弃的方法（如 toUIMessageStream、toUIMessageStreamResponse 等）在 v7 中仍然有效，但将在下一个主要版本中移除。迁移代码片段已在 v6→v7 迁移指南中提供。

github · github-actions[bot] · May 28, 20:57

**背景**: Vercel AI SDK 提供了 streamText 函数，它返回一个 TextStreamPart 对象的 ReadableStream，这些对象表示 LLM 流式块（文本增量、工具调用等）。UIMessageChunk 是一种用于形成聊天界面 UI 消息的类型。以前，将流转换为 UI 消息需要通过 streamText 结果对象；现在独立的辅助函数允许直接转换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text">AI SDK Core: streamText - Vercel</a></li>
<li><a href="https://github.com/vercel/ai">GitHub - vercel/ai: The AI Toolkit for TypeScript. From the ... Message Processing and Content Types | vercel/ai | DeepWiki Vercel Ai Sdk - ClawHub Ably Realtime | Vercel integration API Vercel AI SDK Setup: Stream Responses in 15 Minutes</a></li>
<li><a href="https://deepwiki.com/vercel/ai/2.4-message-processing-and-content-types">Message Processing and Content Types | vercel/ai | DeepWiki</a></li>

</ul>
</details>

**标签**: `#AI`, `#SDK`, `#streaming`, `#developer-tools`, `#UI`

---

<a id="item-27"></a>
## [LiteLLM v1.87.0-rc.2 增加 Cosign Docker 镜像验证](https://github.com/BerriAI/litellm/releases/tag/v1.87.0-rc.2) ⭐️ 7.0/10

BerriAI 发布了 LiteLLM v1.87.0-rc.2，其中包含了使用 cosign 验证 Docker 镜像签名的详细说明，以及多项错误修复和新功能。 此版本通过提供可验证的方法来确保 Docker 镜像完整性，从而增强了 LiteLLM 用户的供应链安全，这对于依赖可信 AI 基础设施的生产部署至关重要。 验证可以使用固定的提交哈希（推荐）或发布标签来完成，两者都指向 commit 0112e53 中引入的同一个 cosign 公钥。更新日志还包括对 Google Gemini 3.5 Flash、托管代理以及新的 Interactions API 端点的支持。

github · github-actions[bot] · May 27, 02:01

**背景**: Cosign 是 Sigstore 项目下的一个工具，用于对容器镜像和其他软件工件进行签名和验证。通过签名 Docker 镜像，开发者可以证明其来源和完整性，使用户能够验证镜像自发布以来未被篡改。LiteLLM 是一个开源代理，为超过 100 家大型语言模型提供商提供统一接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for ...</a></li>
<li><a href="https://docs.sigstore.dev/cosign/">Cosign - Sigstore</a></li>

</ul>
</details>

**标签**: `#litellm`, `#Docker`, `#cosign`, `#release`, `#security`

---

<a id="item-28"></a>
## [OpenAI 发布前沿治理框架](https://openai.com/index/openai-frontier-governance-framework) ⭐️ 7.0/10

OpenAI 发布了其前沿治理框架，详细说明了其 AI 安全、安保和风险实践如何与新兴的欧盟和加州法规保持一致。 该框架标志着自愿性 AI 治理的重要一步，可能影响全球行业标准和监管期望。 该框架聚焦于前沿 AI 系统——即那些可能带来严重风险的系统——并概述了风险评估、监控和事件响应的治理结构。

rss · OpenAI Blog · May 28, 00:00

**背景**: 随着 AI 能力的进步，政府和公司越来越关注强大 AI 系统带来的灾难性风险。欧盟的 AI 法案和加州拟议的法规是要求公司对高风险 AI 实施安全措施的主要努力。OpenAI 的框架是展示合规性和责任感的主动尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-frontier-governance-framework/">OpenAI’s Frontier Governance Framework</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-rolls-out-frontier-governance-framework">OpenAI Rolls Out Frontier Governance Framework - startuphub.ai</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#governance`, `#regulation`, `#OpenAI`

---

<a id="item-29"></a>
## [新型提取工艺有望解锁全球锂资源](https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/) ⭐️ 7.0/10

研究人员在《科学》杂志上发表了新的锂提取方法，初创公司 Rock Zero 正在将该技术商业化，以降低成本和环境影响。 这一突破可能大幅降低锂生产的成本和碳足迹，加速电动汽车和可再生能源储能的转型。 新工艺针对硬岩锂资源，这类资源丰富但目前的提炼成本高且污染大。Rock Zero 宣称其专有化学技术可降低成本和环境影响。

rss · MIT Tech Review · May 28, 18:01

**背景**: 当前的锂提取方法（如从盐湖卤水或硬岩中提取）通常耗水量大且排放大量二氧化碳。例如，提取一吨锂可能需要两百万升水。新方法通过提高效率和减少废料，提供了一种更可持续的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/">How a new extraction process could unlock the world’s lithium</a></li>
<li><a href="https://rockzero.com/">Rock Zero</a></li>
<li><a href="https://interestingengineering.com/energy/NEW-TECH-PROMISES-CLEAN-LITHIUM-EXTRACTION">New breakthrough lithium extraction tech promises greener batteries</a></li>

</ul>
</details>

**标签**: `#lithium extraction`, `#battery materials`, `#clean energy`, `#startup`, `#materials science`

---