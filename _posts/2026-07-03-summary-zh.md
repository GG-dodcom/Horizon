---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> From 113 items, 25 important content pieces were selected

---

1. [DSPy 程序化优化 Datasette Agent SQL 提示](#item-1) ⭐️ 9.6/10
2. [Vercel 首席谈代理作为新型软件](#item-2) ⭐️ 9.3/10
3. [初创公司因构建半成品而失败](#item-3) ⭐️ 9.2/10
4. [让 AI 自己决定何时测试和使用哪个模型](#item-4) ⭐️ 8.9/10
5. [技能工程 vs 一次性 AI 设计](#item-5) ⭐️ 8.9/10
6. [自动研究：自我改进 AI 代理的反馈循环](#item-6) ⭐️ 8.9/10
7. [开发者探索超越提示-响应的 LLM 编码方式](#item-7) ⭐️ 8.8/10
8. [用严格内存过量使用防止 PostgreSQL OOM](#item-8) ⭐️ 8.6/10
9. [Current AI 发布开源 AI 差距地图](#item-9) ⭐️ 8.6/10
10. [理解以参与 AI 辅助编程](#item-10) ⭐️ 8.6/10
11. [Jamesob 本地运行最先进大语言模型指南](#item-11) ⭐️ 8.3/10
12. [Wordgard：ProseMirror 创作者推出的新型富文本编辑器](#item-12) ⭐️ 8.3/10
13. [欧洲议会间谍调查成员遭飞马间谍软件攻击](#item-13) ⭐️ 8.1/10
14. [智能模型路由成为 AI 关键趋势](#item-14) ⭐️ 8.1/10
15. [LiteLLM v1.90.2 验证 Docker 镜像签名](#item-15) ⭐️ 7.8/10
16. [Adobe 试验 AI 生成个性化网站](#item-16) ⭐️ 7.8/10
17. [AI 训练涡轮机提升工业效率](#item-17) ⭐️ 7.7/10
18. [第 402 期周刊：我在智念 AI 的日子（小说）](#item-18) ⭐️ 7.5/10
19. [Anthropic 发布 Claude Code v2.1.200，含关键修复](#item-19) ⭐️ 7.3/10
20. [代码转图像 OCR 技巧降低 LLM 成本 60%](#item-20) ⭐️ 7.3/10
21. [螺旋蝇的衰落与复兴](#item-21) ⭐️ 7.2/10
22. [AI 工程师世博会：循环辩论与 AI 工程现状](#item-22) ⭐️ 7.2/10
23. [Claude Code v2.1.199 修复堆叠技能、SSL 错误、子代理故障等问题](#item-23) ⭐️ 7.0/10
24. [Vercel AI SDK 补丁添加流式转录支持](#item-24) ⭐️ 7.0/10
25. [设备复活捐献眼球助力全眼移植](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DSPy 程序化优化 Datasette Agent SQL 提示](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 9.6/10

Simon Willison 使用 DSPy 系统性地评估和改进 Datasette Agent 的 SQL 系统提示，发现了列名猜测和错误重试循环等问题，并建议更好地包含模式信息。他使用了 Claude Code 配合 Claude Fable 5，并用 GPT-4.1 mini 和 nano 进行了测试。 这展示了一种可应用于任何 LLM 智能体的程序化提示工程方法，系统性地减少猜测并提升性能。它凸显了 DSPy 等工具在优化 AI 系统提示方面的价值。 基线提示导致智能体猜测列名（如 page_count、o.order_id），引发错误重试循环。建议的修复包括直接在模式提示中包含列名，或软化避免不必要的 describe_table 调用的建议。

rss · Simon Willison · Jul 2, 18:25

**背景**: DSPy 是一个用于算法化优化大型语言模型提示和权重的 Python 框架，可进行系统性评估而非手动调优。Datasette Agent 是一个基于 LLM 的助手，通过 Datasette 探索和查询 SQLite 数据库中的数据。Simon Willison 是 Datasette 和 Datasette Agent 的创建者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dspy.ai/">DSPy</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help explore and analyze data in SQLite</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette/datasette-agent: An LLM-powered agent for Datasette · GitHub</a></li>

</ul>
</details>

**标签**: `#DSPy`, `#prompt optimization`, `#Datasette Agent`, `#LLM agents`, `#SQL prompts`

---

<a id="item-2"></a>
## [Vercel 首席谈代理作为新型软件](https://www.latent.space/p/vercel-agents-new-software) ⭐️ 9.3/10

Vercel 的软件主管 Andrew Qu 接受深度访谈，阐述了他们新开源代理框架 'eve' 的创建过程，该框架将 AI 代理视为包含指令、技能和工具的、以文件系统优先的目录。 此次访谈标志着软件开发范式的转变，AI 代理被视为模块化、可版本控制的代码而非黑箱 API，并凸显了针对代理可读性优化网站的需求日益增长。 eve 框架采用 Apache-2.0 许可并以 TypeScript 构建；它将目录中的文件编译为清单，并在 Vercel Functions 上提供持久化运行时。Vercel 还发布了 '代理可读网站' 规范，帮助开发者使网站易于 AI 代理解析。

rss · Latent Space · Jul 3, 00:08

**背景**: AI 代理是代表用户执行任务的自主程序，通常通过访问网站和 API 来完成操作。传统的代理框架依赖复杂的编排，而 eve 采用文件系统优先的方式，每个代理仅是一个包含 Markdown 和 TypeScript 文件的目录，从而更易于检查、版本控制和部署。'代理可读网站' 的概念将 SEO 原则延伸至 AI 浏览时代，确保网站能被自主代理理解和使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vercel.com/eve">eve – The Agent Framework - Vercel</a></li>
<li><a href="https://github.com/vercel/eve">GitHub - vercel / eve : The Framework for Building Agents · GitHub</a></li>
<li><a href="https://vercel.com/kb/guide/agent-readability-spec">Agent Readability: A Specification for AI-Optimized Websites | Vercel Knowledge Base</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Vercel`, `#eve`, `#agent framework`, `#software evolution`

---

<a id="item-3"></a>
## [初创公司因构建半成品而失败](https://weli.dev/blog/half-baked-product/) ⭐️ 9.2/10

一篇论文指出，初创公司常因发布半成品而失败，错将 MVP 误解为粗糙原型而非学习工具。 这一批评挑战了常见的初创公司将不完整产品匆忙推向市场的做法，强调了深入理解 MVP 原则的必要性。 社区讨论对比了 Eric Ries 对 MVP 的定义——以最小努力最大化验证学习——与一种构建劣质产品的‘拐杖’方法。

hackernews · weli · Jul 3, 08:23 · [社区讨论](https://news.ycombinator.com/item?id=48772388)

**背景**: MVP（最小可行产品）是精益创业方法论中的关键概念，旨在快速测试假设。许多创始人滥用它来证明发布未完成产品的合理性，从而导致失败。

**社区讨论**: 评论者就 MVP 的定义和创始人动机展开辩论。一位用户批评那些追求财富但缺乏领域专业知识的创始人，另一位则指出初创公司中不同角色之间的脱节。

**标签**: `#startup`, `#product development`, `#MVP`, `#failure`, `#founder motivation`

---

<a id="item-4"></a>
## [让 AI 自己决定何时测试和使用哪个模型](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 8.9/10

Simon Willison 分享了来自 Claude Code 团队和 Jesse Vincent 的技巧，允许像 Fable 这样的 AI 模型自行判断何时编写测试以及将任务委托给哪个较低功耗的模型，从而提高效率并节省 tokens。 这种方法在保持质量的同时减少了 token 消耗和成本，为使用昂贵的顶级模型（如 Fable）的开发者提供了实用的优化方案。它凸显了向更自主的 AI 代理转变的趋势，这些代理可以自我优化资源使用。 该技术包括添加一条提示，如“自行判断选择合适的较低功耗模型并在子代理中运行该模型”，以存储一个记忆文件，指导模型将编码任务委托给更便宜的模型（例如，实质性工作用 Sonnet，琐碎编辑用 Haiku），同时将判断密集型任务保留在主模型上。

rss · Simon Willison · Jul 3, 18:51

**背景**: Claude Fable 和 Opus 是 Anthropic 的高级 AI 模型，其中 Fable 最强大且最昂贵，专为复杂推理和长期任务设计。代理型 AI 系统可以自主追求目标并使用工具，这个技巧利用这种自主性，通过将简单工作委托给更便宜的模型来优化成本和性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Claude Code`, `#testing`, `#agentic systems`

---

<a id="item-5"></a>
## [技能工程 vs 一次性 AI 设计](https://www.latent.space/p/skill-engineering-design) ⭐️ 8.9/10

Paul Bakaus 主张采用“技能工程”（将任务分解为可复用的技能）而非一次性 AI 设计，强调在智能体循环中引入迭代的人类判断。 这意义重大，因为它将 AI 设计范式从单次提示解决方案转变为持续的人类监督，影响 AI 代理的构建和生产部署方式。 Bakaus 创建了开源设计技能系统 Impeccable，允许智能体增量调整 UI 元素（如“更醒目”），而非一次性重设计整个页面。

rss · Latent Space · Jul 2, 14:36

**背景**: 一次性 AI 设计是指通过单次提示让模型完成复杂任务，通常效果不佳。相比之下，技能工程将工作分解为更小、可复用的技能，并可通过人类反馈进行迭代优化。术语“loopmaxxing”描述了围绕 AI 代理设计弹性反馈循环以提升可靠性的实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/skill-engineering-design">Skill engineering and the case against one-shot AI design</a></li>
<li><a href="https://www.articsledge.com/post/skill-engineering">What Is Skill Engineering? The Complete 2026 Guide</a></li>
<li><a href="https://turnkeydatacenter.ai/blog/loopmaxxing-infinite-ai-agents-fixed-cost-infrastructure/">Loopmaxxing : Why Infinite AI Agents Demand... - turnkeydatacenter.ai</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#human-in-the-loop`, `#skill engineering`, `#AI design`, `#loopmaxxing`

---

<a id="item-6"></a>
## [自动研究：自我改进 AI 代理的反馈循环](https://www.latent.space/p/autoresearch-introspection) ⭐️ 8.9/10

Introspection 联合创始人 Roland Gavrilescu 解释了自动研究（autoresearch）这一框架，其中 AI 代理通过迭代实验和自我改进训练流程，同时强调人类在软件工厂中的核心地位。 这种范式通过自动化研究循环可能加速 AI 开发，但也重新定义了人类的角色——从直接编码转向高层监督，这对 AI 实验室的生产力和工作设计具有重要影响。 自动研究方法使用代理“配方”和自我改进循环，AI 根据实验结果修改自身训练代码，但人类对于设定目标、验证结果以及维护更广泛的系统上下文仍然至关重要。

rss · Latent Space · Jul 1, 23:52

**背景**: 自动研究指的是 AI 代理作为智能编排者，在研发流程中迭代实验的自动化框架，通常受 Andrej Karpathy 开源项目的启发。自我改进循环使代理能够从反馈中学习并优化自身技能，无需人类工程师重写代码。随着代理在生产环境中变得更加自主，这一概念正获得越来越多的关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ccapi.ai/blog/autoresearch-agents-single-gpu-nanochat-training">Autoresearch : Agents researching on single-GPU... | CCAPI Blog</a></li>
<li><a href="https://noqta.tn/en/blog/karpathy-autoresearch-autonomous-ai-experiments-loop-2026">The Karpathy Loop: AI Agents Running 700 Experiments Autonomously</a></li>
<li><a href="https://powerdrill.ai/blog/self-improving-data-agents">Self - Improving Data Agents : Unlocking Autonomous Learning and...</a></li>

</ul>
</details>

**标签**: `#AI`, `#agents`, `#self-improving`, `#feedback loops`, `#software factory`

---

<a id="item-7"></a>
## [开发者探索超越提示-响应的 LLM 编码方式](https://news.ycombinator.com/item?id=48771515) ⭐️ 8.8/10

Hacker News 上的一场讨论展示了替代性 LLM 编程工作流的实验，包括异构 LLM 群体和密封代理，这些方法突破了标准的提示-响应循环。 这些探索可能带来更流畅、更有利于进入心流状态的 AI 辅助编程，有望改变开发者将 LLM 融入工作流的方式。 关键思路包括：通过有向无环图协作的多个 LLM 异构群体，以及将代码生成与测试编写隔离以避免偏见的密封代理。

hackernews · yehiaabdelm · Jul 3, 06:21

**背景**: 当前的 LLM 编码工具（如 Claude Code 和 Codex）通常采用提示-响应循环：用户输入请求，模型回复，然后用户审查并再次提示。这会打断开发者的心流状态。异构群体使用多个专业化 LLM，按照有向无环图（DAG）排列来协作完成任务，同时优化模型角色和权重。密封代理在隔离的沙箱中运行，代码编写者看不到测试，测试编写者也看不到代码，从而强制执行关注点分离以提高软件质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.04510">[2502.04510] Heterogeneous Swarms: Jointly Optimizing Model Roles and Weights for Multi-LLM Systems</a></li>
<li><a href="https://hermeticagents.app/">Hermetic Agents — A Council of Seven Principle-Based AI Agents</a></li>
<li><a href="https://github.com/HermeticOrmus/Hermetic-Agents">GitHub - HermeticOrmus/ Hermetic - Agents</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人实验，一位用户用旧 GPU 搭建家庭实验室运行异构 LLM 群体，另一位提出了密封代理以减少确认偏差。其他人感叹心流状态的丧失，并讨论了在外包理解与维护代码质量之间的权衡。

**标签**: `#LLM`, `#coding`, `#AI agents`, `#software engineering`, `#programming`

---

<a id="item-8"></a>
## [用严格内存过量使用防止 PostgreSQL OOM](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.6/10

Ubicloud 发表了一篇博文，详细解释了为何在其托管的 PostgreSQL 集群中将 Linux 的 vm.overcommit_memory 设置为严格模式（值 2），以防止 OOM killer 终止关键数据库进程。 这种配置可以显著提升 PostgreSQL 在内存压力下的稳定性，但也引入了可能影响系统 fork 能力和整体内存管理的权衡。这场讨论凸显了生产环境中内存过量使用设置的复杂性。 严格过量使用模式（模式 2）默认禁止内存过量使用，提前失败分配而非依赖 OOM killer。但社区评论指出，如果调整了过量使用比例，这可能会阻止进程 fork，并且在其他应用分配大量虚拟内存的混合工作负载环境中可能导致不稳定。

hackernews · furkansahin · Jul 3, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 通过 vm.overcommit_memory 提供三种内存过量使用策略：0（启发式）、1（总是过量使用）和 2（严格过量使用）。默认的启发式模式允许内核过量使用内存，当实际内存耗尽时可能导致 OOM killer 终止进程。PostgreSQL 特别容易受到 OOM 攻击，因为它通常使用大块共享内存段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdMemoryLimitVsOvercommit">Chris's Wiki :: blog/ linux /SystemdMemoryLimitVsOvercommit</a></li>
<li><a href="https://www.servermo.com/howto/stop-linux-oom-killer-ai-crash/">Stop AI Crashes: The Linux OOM-Killer Shield | ServerMO</a></li>

</ul>
</details>

**社区讨论**: 社区讨论意见不一。用户 baq 批评 Linux 默认设置‘疯狂’，并指出内存压力下的多种故障模式。Bender 警告模式 2 可能阻止 fork，并建议全面测试。Ubicloud 的 Ozgun 澄清说，虽然该技术适用于他们的用例，但博文标题过于强烈，严格过量使用在其他场景中可能产生意想不到的副作用。

**标签**: `#PostgreSQL`, `#memory management`, `#Linux kernel`, `#OOM killer`, `#system administration`

---

<a id="item-9"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.6/10

非营利组织 Current AI 在 2025 年 AI 行动峰会上成立，近日发布了开源 AI 差距地图 v0.1，索引了 421 个开源 AI 产品，涵盖模型、工具、数据集和硬件。底层数据包括 1,184 个 YAML 文件，已在 GitHub 上以 MIT 许可证发布。 这张差距地图提供了开源 AI 生态系统的全面结构化概览，帮助研究人员、开发者和政策制定者识别优势和缺失环节。它为跟踪开源 AI 的发展设立了基线，在 AI 应用加速的当下愈发重要。 该地图详细列出了 421 个产品：来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，按 3 个堆栈层的 14 个类别组织。另有 24,400 个工件被编目但未分类。

rss · Simon Willison · Jul 3, 22:04

**背景**: Current AI 是一个全球性的非营利合作伙伴关系，于 2025 年 2 月在巴黎 AI 行动峰会上启动，已获得 4 亿美元承诺资金。开源 AI 差距地图旨在系统地对碎片化的开源 AI 领域进行编目，使其更易于导航和分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Action_Summit_2025">AI Action Summit 2025</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#gap map`, `#ecosystem`, `#non-profit`

---

<a id="item-10"></a>
## [理解以参与 AI 辅助编程](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.6/10

Geoffrey Litt 在 AIE 会议上提出了“理解以参与”的概念，认为开发者必须深入了解 AI 编程代理所做的代码变更，才能保持有效的协作并避免认知债务。 随着 AI 编程代理变得越来越复杂，开发者有可能在不完全理解的情况下接受生成的代码，从而导致认知债务，损害软件的长期可维护性以及开发者自身的创造性参与。 Litt 强调，为了流畅地参与，开发者需要拥有关于代码库的丰富心智概念，否则他们推动项目的能力将受到限制。Simon Willison 推荐观看 Litt 在 AIE 会议上的录播演讲。

rss · Simon Willison · Jul 2, 17:07

**背景**: 认知债务是指开发者在未完全理解其逻辑或结构的情况下使用 AI 生成的代码所积累的理解缺失，这会使未来的变更更加困难。AI 编程代理是根据自然语言提示生成或修改代码的工具，越来越多地用于软件开发流程中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathiesen.dev/writing/cognitive-debt">Cognitive Debt | Jarle Mathiesen</a></li>
<li><a href="https://www.thoughtworks.com/en-th/insights/blog/generative-ai/cognitive-demands-ai-novelty">The cognitive demands of AI novelty | Thoughtworks Thailand</a></li>
<li><a href="https://www.artofsm.art/t/feeling-lost-in-your-codebase-5-tips-to-tackle-ai-induced-cognitive-debt/16929">Feeling lost in your codebase? 5 tips to tackle AI-induced cognitive debt</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cognitive debt`, `#software engineering`, `#coding assistants`, `#collaboration`

---

<a id="item-11"></a>
## [Jamesob 本地运行最先进大语言模型指南](https://github.com/jamesob/local-llm) ⭐️ 8.3/10

Jamesob 发布了一份关于构建高端本地大语言模型（LLM）设置的指南，配置费用高达 4 万到 5.5 万美元，使用多块高端 GPU。 该指南凸显了当前在本地运行顶级大语言模型所需的极端硬件要求，对大多数用户而言仍然过于昂贵，并引发了关于成本效益替代方案的讨论，如云服务或统一内存架构。 该指南中的顶级配置起始预算为 4 万美元，包括 4 块每块 1.2 万美元的 GPU，总价接近 5 万到 5.5 万美元，并依赖量化技术来适配模型。用户指出，即便如此，性能可能仍无法与基于云端的模型（如 Claude Opus）相媲美。

hackernews · livestyle · Jul 3, 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 在本地运行大语言模型（LLM）需要大量的计算资源，尤其是对于最先进（SOTA）模型。通常需要具备大容量显存的高端 GPU。量化是一种降低模型精度以适应有限内存的技术，但可能影响输出质量。基于云端的 LLM 服务按订阅费用提供对强大模型的访问，但牺牲了隐私和控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Running_Open-Source_LLMs_Locally">Running Open-Source LLMs Locally</a></li>
<li><a href="https://fungies.io/local-llm-inference-tools-guide-2026-3/">How to Set Up and Use Local LLM Inference Tools in... - Fungies.io</a></li>

</ul>
</details>

**社区讨论**: 社区成员对高昂成本表示担忧，指出 4 万到 5.5 万美元可以覆盖多年的云订阅费用。一些人建议使用统一内存的 Mac 或双 RTX 3090 来运行较小的模型。另一些人警告说，本地设置通常需要量化，并且可能无法达到云端性能。

**标签**: `#AI`, `#LLM`, `#local inference`, `#hardware`

---

<a id="item-12"></a>
## [Wordgard：ProseMirror 创作者推出的新型富文本编辑器](https://wordgard.net/) ⭐️ 8.3/10

Wordgard 是一个全新的浏览器内富文本编辑器框架，由 ProseMirror 的创作者 Marijn Haverbeke 发布。它采用 MIT 许可，并在其 Forgejo 服务器上开源。 Wordgard 为构建内容编辑器提供了新的思路，在共享 ProseMirror 坚实基础上可能解决其某些限制。开发者在 Web 应用中获得了可定制富文本编辑的新选项。 Wordgard 并非自由格式的 HTML 编辑器，而是一个让开发者精确控制所支持内容类型的框架。从 ProseMirror 没有直接升级路径；迁移需要大量重写。

hackernews · indy · Jul 3, 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: 浏览器中的富文本编辑器长期以来一直是个挑战，没有标准的内置解决方案。ProseMirror 是一个广泛使用的开源框架，用于构建此类编辑器，为 Tiptap 等工具提供支持。Wordgard 是同一作者推出的新替代方案，旨在改进 ProseMirror 的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://code.haverbeke.berlin/wordgard/wordgard">wordgard / wordgard : The Wordgard rich text editor</a></li>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Wordgard 的技术优点表现出积极兴趣，用户称赞其设计以及与 ProseMirror 的比较。一些开发者对迁移工作量以及缺乏富文本编辑的 Web 标准表示担忧。

**标签**: `#web development`, `#rich-text editor`, `#prosemirror`, `#open source`, `#devtools`

---

<a id="item-13"></a>
## [欧洲议会间谍调查成员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.1/10

公民实验室的取证分析确认，欧洲议会间谍软件调查委员会成员、希腊欧洲议会议员斯泰利奥斯·库洛格卢的 iPhone 在 2022-2023 年间至少三次感染了飞马间谍软件。 此次入侵破坏了欧盟对间谍软件滥用的调查可信度，并凸显出即使是调查监控行为的高知名度目标，仍然容易受到国家级黑客攻击。 感染发生在 2022 年 10 月 21 日左右以及 2023 年 3 月 6 日至 7 日，取证痕迹显示确信度很高，且可能涉及 iOS 零点击漏洞。被攻破的手机可能泄露了机密医疗和政府文件。

hackernews · ledoge · Jul 3, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马间谍软件由以色列 NSO 集团开发，是一种商业间谍软件，能远程渗透 iOS 和 Android 设备以提取数据并启动传感器。公民实验室隶属于多伦多大学，是研究数字威胁的领先实验室，曾揭露全球多起飞马感染事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论指出欧洲议会可能缺乏工作与个人设备分离的政策，希腊飞马丑闻牵连总理办公室，以及使用 GrapheneOS 或锁定模式可提高攻击成本。有评论讽刺欧盟成员国对本国记者使用飞马，却又窃听欧盟议员。

**标签**: `#Pegasus`, `#spyware`, `#European Parliament`, `#Citizen Lab`, `#cybersecurity`

---

<a id="item-14"></a>
## [智能模型路由成为 AI 关键趋势](https://blog.pragmaticengineer.com/the-pulse-a-new-trend-smart-model-routing/) ⭐️ 8.1/10

文章探讨了新兴的智能模型路由解决方案，这些方案自动为每个任务选择最佳 AI 模型，突显了 AI 工具领域的新趋势。 这很重要，因为它可以在保持输出质量的同时将 AI 推理成本降低 50-80%，从而在各类应用中实现更高效和可扩展的部署。 智能路由器分析提示词的任务类型、所需质量和成本敏感度，然后路由到满足质量门槛的最便宜模型，支持 GPT-4o、Claude 和 Gemini 等提供商。

rss · Pragmatic Engineer · Jul 2, 18:46

**背景**: 传统上，AI 应用依赖单一模型，导致效率低下。智能模型路由为每个请求动态选择最优模型，优化成本、速度和质量。这一概念类似于网络路由，但应用于 AI 推理，可在保持性能的同时大幅降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.chinallmapi.com/smart-model-routing-strategy/">Smart Model Routing : How to Choose the Right AI Model for Each...</a></li>
<li><a href="https://vincony.com/glossary/model-routing">Model Routing — AI Aggregator Concept Defined | Vincony | Vincony</a></li>

</ul>
</details>

**标签**: `#AI`, `#model routing`, `#LLM`, `#inference`, `#practical AI`

---

<a id="item-15"></a>
## [LiteLLM v1.90.2 验证 Docker 镜像签名](https://github.com/BerriAI/litellm/releases/tag/v1.90.2) ⭐️ 7.8/10

LiteLLM v1.90.2 引入了使用 cosign 验证 Docker 镜像签名的详细步骤，推荐使用固定提交哈希的方法，也提供了基于发布标签的更便捷方法。 这通过确保 Docker 镜像的完整性和真实性，增强了 LiteLLM 用户的供应链安全性，对于防止篡改和建立对 AI 工具部署的信任至关重要。 两种方法使用相同的公钥，该公钥来自提交 0112e53；固定提交哈希在密码学上不可变，而发布标签方法依赖于标签保护规则。

github · yuneng-berri · Jul 3, 04:48

**背景**: Cosign 是 Sigstore 项目中的工具，用于签名和验证容器镜像，支持基于密钥和无密钥签名。验证签名可以确保镜像自签名后未被篡改，这对于安全的软件供应链至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sigstore.dev/quickstart/quickstart-cosign/">Sigstore Quickstart with Cosign - Sigstore</a></li>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/ cosign : Code signing and transparency for...</a></li>

</ul>
</details>

**标签**: `#LiteLLM`, `#Docker`, `#cosign`, `#supply chain security`, `#AI tooling`

---

<a id="item-16"></a>
## [Adobe 试验 AI 生成个性化网站](https://www.latent.space/p/the-website-of-the-future) ⭐️ 7.8/10

Adobe 正在试验“代理型网站”，利用 AI 根据每个访客的意图实时生成网页。 这可能从根本上改变网页设计和用户体验，使网站具备自适应性而非静态，从而可能提高用户参与度和转化率。 Adobe 的 Carlos Sanchez 讨论的概念涉及使用 AI 代理根据个人用户意图生成页面，而非提供预构建页面。

rss · Latent Space · Jul 2, 21:25

**背景**: 传统网站向所有访客提供相同的内容，而“代理型网站”使用嵌入式 AI 代理根据用户行为和上下文动态组合页面。Adobe 正在通过其 Experience Manager 和 Edge Delivery Services 探索这一方向，旨在为代理型网站自动化站点创建和迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=wIJKwPBbuPk">Building the Agentic Web | Adobe Developers Live 2025... - YouTube</a></li>
<li><a href="https://business.adobe.com/blog/modernizing-digital-experiences-for-the-agentic-web">Modernizing digital experiences with Adobe agentic AI</a></li>
<li><a href="https://www.businesswire.com/news/home/20250318537901/en/Adobe-Launches-Adobe-Experience-Platform-Agent-Orchestrator-for-Businesses-to-Activate-AI-Agents-in-Customer-Experiences-and-Marketing-Workflows">Adobe Launches Adobe Experience Platform Agent Orchestrator for...</a></li>

</ul>
</details>

**标签**: `#AI`, `#agentic systems`, `#web development`, `#personalization`, `#Adobe`

---

<a id="item-17"></a>
## [AI 训练涡轮机提升工业效率](https://www.technologyreview.com/2026/07/02/1138433/teaching-ai-to-run-with-the-turbines/) ⭐️ 7.7/10

AI 的一项新应用正被部署于控制和优化工业涡轮机，在消费级工具之外提升运营连续性和安全性。 这标志着 AI 从聊天机器人转向关键物理基础设施，可能减少停机时间并提高能源和制造业的安全性。 该 AI 系统与运营技术（OT）集成，实时监控和调整涡轮机参数，利用工业数据流进行预测性维护。

rss · MIT Tech Review · Jul 2, 12:51

**背景**: 运营技术（OT）指监控和控制工业设备的硬件和软件，与传统 IT 不同。涡轮机是发电的关键复杂机器，AI 的作用是更高效、更安全地管理其运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Operational_technology">Operational technology</a></li>
<li><a href="https://www.marketresearchfuture.com/cat-intel/procurement-intelligence-industrial-turbines-market">Category Intelligence for Industrial Turbines Market - MRFR - MRFR</a></li>

</ul>
</details>

**标签**: `#AI`, `#industrial AI`, `#energy`, `#operational technology`, `#applied AI`

---

<a id="item-18"></a>
## [第 402 期周刊：我在智念 AI 的日子（小说）](http://www.ruanyifeng.com/blog/2026/07/weekly-issue-402.html) ⭐️ 7.5/10

阮一峰的第 402 期科技周刊发布了，其中包含一篇名为《我在智念 AI 的日子》的虚构小说，以及精心挑选的科技文章。 该周刊为中国科技发展提供了值得信赖的每周概览，而虚构故事则从创意角度探讨了 AI 工作文化。 该期周刊日期为 2026 年 7 月，相关性及质量评分为 7.5/10；虚构元素略微降低了实用价值。

rss · 阮一峰周刊 · Jul 2, 23:33

**背景**: 阮一峰是一位知名的中国博主和作者，发布一份广受欢迎的每周科技通讯。'智念 AI'似乎是故事中虚构的 AI 公司背景。该通讯通常涵盖 AI、编程和行业趋势。

**标签**: `#tech newsletter`, `#AI`, `#weekly curation`, `#阮一峰`

---

<a id="item-19"></a>
## [Anthropic 发布 Claude Code v2.1.200，含关键修复](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) ⭐️ 7.3/10

该版本更改了 AskUserQuestion 对话框，默认不再自动继续，并将默认权限模式设置为 Manual，适用于所有界面。同时修复了十多个错误，涉及后台会话、MCP 服务器配置和屏幕阅读器无障碍功能。 此更新让用户对对话框和权限流程拥有更多控制，减少意外自动化，提升安全性。错误修复增强了后台代理和 MCP 集成的可靠性，对于在 CI/CD 或长时间运行任务中使用 Claude Code 的高级用户和开发者至关重要。 值得注意的修复包括：当 MCP 服务器数组配置错误时防止崩溃；解决休眠/唤醒后后台会话停滞；改进屏幕阅读器输出，隐藏装饰性字形并标记嵌套表格。安装脚本现在会解释因内存不足导致安装被终止的情况。

github · ashwin-ant · Jul 3, 16:52

**背景**: Claude Code 是 Anthropic 开发的 AI 编程助手，属于 Claude 产品家族。它支持后台代理来自动执行任务，并使用模型上下文协议（MCP）与外部工具和数据源集成。权限模式控制工具如何处理用户对文件编辑或命令执行等操作的批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/permission-modes">Choose a permission mode - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI tools`, `#release notes`, `#bug fixes`, `#Anthropic`

---

<a id="item-20"></a>
## [代码转图像 OCR 技巧降低 LLM 成本 60%](https://github.com/teamchong/pxpipe) ⭐️ 7.3/10

一个名为 pxpipe 的 GitHub 项目将代码转换为图像，并通过 OCR 处理，利用令牌计费漏洞将 Fable 的 LLM 成本降低了 60%。 这项技术暴露了 LLM 服务中的潜在定价漏洞，即图像令牌比文本更便宜或不收费，从而大幅节省成本。这可能促使服务商堵住漏洞或调整定价模式。 该方法减少了提示词令牌，但可能会增加补全令牌和延迟，社区测试已指出这一点。它利用了某些提供商（如 Gemini 和 Claude）处理 PDF 时对文本进行 OCR 而不额外收费的机制。

hackernews · dimitropoulos · Jul 3, 15:50 · [社区讨论](https://news.ycombinator.com/item?id=48776464)

**背景**: LLM 通常按令牌计费，令牌是文本块（如单词或子词）。代码作为文本可能被分词为许多令牌，但图像的处理方式不同，可能有更便宜的令牌定价。将代码转换为图像可以绕过文本令牌计数，如果提供商对图像令牌收费更低或不计算 OCR 后的文本令牌，则能降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them">What are tokens and how to count them? | OpenAI Help Center</a></li>
<li><a href="https://ssimplifi.com/blog/llm-cost-reduction-techniques-ranked-by-roi">LLM cost reduction techniques ranked by ROI... | Prism by Ssimplifi</a></li>

</ul>
</details>

**社区讨论**: 评论者 aabhay 指出，Gemini 和可能 Claude 会对 PDF 进行 OCR 并输入文本但不收费，这意味着这是一个漏洞。lpellis 去年在 OpenAI 模型上试过类似方法，但最终成本更高。lstroud 讽刺地说这是在重新发现压缩二进制格式。

**标签**: `#AI`, `#LLM`, `#cost optimization`, `#OCR`, `#token accounting`

---

<a id="item-21"></a>
## [螺旋蝇的衰落与复兴](https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm) ⭐️ 7.2/10

这篇文章详细描述了通过昆虫不育技术根除螺旋蝇的历史，以及近年来该虫害在美洲的重新出现，2025/2026 年在德克萨斯州报告了病例。 这很重要，因为螺旋蝇侵扰会给牲畜和野生动物造成严重经济损失，而它的重新出现挑战了数十年成功的根除工作，暴露了生物防治项目的脆弱性。 昆虫不育技术包括大量饲养并用辐射使雄蝇绝育，然后释放它们与野生雌蝇交配，导致种群崩溃；近期的重新出现可能是由于巴拿马达连隘口屏障带的失效。

hackernews · crescit_eundo · Jul 3, 12:58 · [社区讨论](https://news.ycombinator.com/item?id=48774492)

**背景**: 螺旋蝇（Cochliomyia hominivorax）是一种寄生蝇，其幼虫以活体组织为食，在动物身上引起蝇蛆病。美国农业部及其合作伙伴通过昆虫不育技术成功将其从北美和中美洲根除。然而，在巴拿马维持屏障带一直具有挑战性，近期在德克萨斯州的病例表明屏障已被突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Screwworm">Screwworm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sterile_insect_technique">Sterile insect technique</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章的深度，指出早期研究者克服了嘲笑和资源匮乏。其他人讨论了历史实验的伦理问题，以及维持屏障与在整个大陆根除螺旋蝇的经济考量。

**标签**: `#screwworm`, `#sterile insect technique`, `#eradication`, `#biology`, `#agriculture`

---

<a id="item-22"></a>
## [AI 工程师世博会：循环辩论与 AI 工程现状](https://www.latent.space/p/aiewf-daily-dispatch-locomotives) ⭐️ 7.2/10

AI 工程师世博会在关于智能系统循环的辩论、一份 AI 工程现状报告的发布，以及聚焦下一步该构建什么的闭幕主题演讲中落下帷幕。 该活动凸显了塑造 AI 工程的关键讨论，特别是关于 AI 智能体中循环（迭代反馈机制）的辩论，这对构建可靠的自主系统至关重要。 辩论围绕智能系统中的循环是提升性能还是引入复杂性和失败模式展开。AI 工程现状报告可能涵盖了 AI 开发的趋势、挑战和采用模式。

rss · Latent Space · Jul 3, 05:11

**背景**: AI 工程师世博会是一个专注于实用 AI 工程的会议，汇集了开发者、研究人员和行业领袖，讨论工具、技术和趋势。“循环”指的是 AI 智能体中的迭代反馈机制，如自我反思或工具使用循环，关于其在实际应用中的有效性存在争议。“AI 工程现状”一词通常指一份行业报告，调查构建 AI 系统的当前实践、瓶颈和未来方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.movingavg.com/essays/vibes-at-the-ai-engineer-worlds-fair.html">Vibes at the AI Engineer World ' s Fair</a></li>

</ul>
</details>

**标签**: `#AI Engineering`, `#Agentic Systems`, `#LLM`, `#Industry Report`, `#Event Summary`

---

<a id="item-23"></a>
## [Claude Code v2.1.199 修复堆叠技能、SSL 错误、子代理故障等问题](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) ⭐️ 7.0/10

Anthropic 发布了 Claude Code v2.1.199，这是一次错误修复更新，解决了包括堆叠技能调用、SSL 证书错误、流式响应处理、子代理故障、后台代理守护进程损坏等在内的 20 多个问题。 此版本显著提高了 Claude Code 的可靠性和用户体验，特别是对于使用技能、子代理和后台代理等高级功能的用户。它减少了静默失败带来的挫败感和潜在数据丢失。 值得注意的技术细节包括：堆叠技能现在最多加载 5 个前置技能；SSL 错误会立即失败并给出可操作的指导；部分流式响应保留并附带不完整响应通知；修复了非正常关闭后后台代理守护进程损坏的问题。多项子代理错误报告修复确保使用限制等错误能够正确呈现。

github · ashwin-ant · Jul 2, 23:35

**背景**: Claude Code 是 Anthropic 的命令行 AI 编程助手。技能（Skills）是通过包含指令和资源的组织化文件夹来扩展其功能的模块化能力。子代理（Subagents）是用于委派任务的隔离 Claude 实例，每个都有自己的上下文和工具。后台代理（Background agents）允许任务并行运行而不阻塞主会话。这些功能支持复杂工作流程，但此前存在可靠性问题，此版本解决了这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/skills">Agent Skills - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#tooling`, `#claude-code`, `#bug-fixes`

---

<a id="item-24"></a>
## [Vercel AI SDK 补丁添加流式转录支持](https://github.com/vercel/ai/releases/tag/%40ai-sdk/xai%404.0.6) ⭐️ 7.0/10

@ai-sdk/xai 的 4.0.6 版本为 OpenAI 的 gpt-realtime-whisper 和 xAI 的 WebSocket STT 等模型添加了实验性的流式转录支持。 此次更新使开发者能够通过 Vercel AI SDK 直接将实时语音转文字功能集成到应用中，简化了实时转录功能的开发。 该功能为实验性，并更新了多个依赖项：@ai-sdk/provider 升至 4.0.2，@ai-sdk/provider-utils 升至 5.0.5，以及 @ai-sdk/openai-compatible 升至 3.0.5。

github · github-actions[bot] · Jul 2, 20:46

**背景**: Vercel AI SDK 是一个流行的构建 AI 驱动应用的工具包，提供对多种 AI 提供商的统一访问。@ai-sdk/xai 是用于 xAI Grok 模型的提供商包，现在支持流式转录。流式转录将实时音频逐步转换为文本，从而实现低延迟的语音应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-sdk.dev/providers/ai-sdk-providers/xai">AI SDK Providers: xAI Grok</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-whisper">GPT - Realtime - Whisper Model | OpenAI API</a></li>
<li><a href="https://docs.x.ai/developers/quickstart">Tutorial on using Grok models via xAI API | xAI Docs</a></li>

</ul>
</details>

**标签**: `#AI SDK`, `#streaming transcription`, `#xAI`, `#OpenAI Whisper`, `#release notes`

---

<a id="item-25"></a>
## [设备复活捐献眼球助力全眼移植](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) ⭐️ 7.0/10

研究人员开发出一种设备，能在捐献者死后维持眼球状态，防止快速退化，并保留视网膜传递电信号的能力。该设备名为 eye-ECMO，通过荧光染料测试显示染料成功在视网膜中循环。 这一突破可能使全眼移植成为恢复盲人视力的可行方案。它解决了死后眼球迅速退化这一主要障碍，使该领域更接近成功的人类眼部移植。 eye-ECMO 设备通过提供体外膜肺氧合来维持捐献眼球的血液流动和氧气供应。测试显示染料在视网膜中循环，表明血管功能得以保留，但尚未实现视力恢复。

rss · MIT Tech Review · Jul 3, 17:34

**背景**: 全眼移植历来非常困难，原因是手术复杂且死亡后眼组织迅速退化。几年前的一次尝试中，移植后的眼睛无法看见东西。新设备旨在让捐献眼球保持活性足够长时间，以实现成功移植。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/">A device that revives eyeballs from dead donors could make eye ...</a></li>
<li><a href="https://gables-gazette.com/university-of-miami-is-paving-the-way-for-human-eye-transplants/">University of Miami is paving the way for human eye transplants</a></li>

</ul>
</details>

**标签**: `#medical technology`, `#eye transplant`, `#biomedical engineering`, `#organ preservation`

---