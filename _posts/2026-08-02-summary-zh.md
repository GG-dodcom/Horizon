---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> From 68 items, 9 important content pieces were selected

---

1. [无状态 MCP 2.0 重燃兴趣，催生新工具 mcp-explorer 与 datasette-mcp](#item-1) ⭐️ 9.5/10
2. [DeepSeek V4 Flash 0731：低价 304B 参数模型，智能体能力增强](#item-2) ⭐️ 7.8/10
3. [Karpathy 提议用“骑自行车的鹈鹕”作为 AI 基准测试](#item-3) ⭐️ 7.5/10
4. [AI 公开信交锋：开放权重、Anthropic 与前沿节奏控制](#item-4) ⭐️ 7.5/10
5. [Datasette-apps 0.2a0 让 AI 代理能测试和编辑应用](#item-5) ⭐️ 7.3/10
6. [Bor v0.8：面向 Linux 桌面的开源策略管理工具](#item-6) ⭐️ 7.2/10
7. [OpenAI 的 Astra 模型以每个不到 2000 美元的成本解决十个长期未解的数学难题](#item-7) ⭐️ 7.2/10
8. [F*：面向证明的编程语言，用于形式化验证](#item-8) ⭐️ 7.1/10
9. [墨西哥成为美国 AI 服务器最大进口来源，超越汽车](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [无状态 MCP 2.0 重燃兴趣，催生新工具 mcp-explorer 与 datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.5/10

Simon Willison 撰文介绍无状态 MCP 规范更新（MCP 2.0，即 2026-07-28 Model Context Protocol 规范），该更新将协议简化为单个 HTTP 请求。他还发布了两个新工具：mcp-explorer 和 datasette-mcp。 此事意义重大，因为 MCP 此前曾被 Skills 和智能体直接使用终端的方式所掩盖，而无状态重设计大幅降低了实现复杂度，使 MCP 更易于审计、控制，并且能在较小的模型上运行。这有望重振 MCP 在 AI 智能体生态中的采用。 无状态 MCP 使用 MCP-Protocol-Version 和 Mcp-Method 等头部信息，取代了原先的会话初始化，从而无需在服务端维护会话状态。Simon 在一周内构建了三个实现，包括 mcp-explorer（一个用于交互式探测 MCP 服务器的 CLI 工具）和 datasette-mcp（一个通过 MCP 以只读 SQL 方式暴露 Datasette 数据库的插件）。

rss · Simon Willison · Jul 31, 23:13

**背景**: MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于向 LLM 智能体框架暴露工具。旧版有状态 MCP 需要先通过两个步骤初始化会话，而无状态 MCP 只需一次请求/响应，因此更适合可扩展的 Web 基础设施，也更便于客户端和服务端实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/31/stateless-mcp/">Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>
<li><a href="https://github.com/datasette/datasette-mcp">GitHub - datasette/ datasette - mcp : Adds a /-/mcp MCP server to any...</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI`, `#Agentic Systems`, `#LLM`, `#Developer Tools`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731：低价 304B 参数模型，智能体能力增强](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 7.8/10

DeepSeek 发布了 V4 Flash 0731，这是一个 304B 参数的开权重模型，具备大幅增强的智能体（agentic）能力，输入价格每百万 token 0.14 美元，输出每百万 token 0.27 美元。Artificial Analysis 的智能指数排名显示它超过了 MiniMax M3（428B），Simon Willison 称它可能是目前性价比最高的模型。 这一发布可能大幅降低智能体 AI 应用的成本，以每任务约 0.028 美元的价格让更多开发者用上高级推理能力。它加剧了大模型市场的性价比竞争，在性价比对比中给 Grok 4.5、Claude Opus 5 等更大更贵的模型带来压力。 该模型在 Hugging Face 上大小为 167GB，总参数 304B。Simon Willison 在 OpenRouter 上以默认推理级别测试时得到了一只'令人失望的鹈鹕'，但通过命令`llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high`把推理强度调高后，输出质量大幅提升，说明推理强度对生成质量有明显影响。

rss · Simon Willison · Jul 31, 23:59

**背景**: DeepSeek 是一家发布开放权重模型的中国 AI 实验室。Artificial Analysis 智能指数是一种综合基准，在推理、编程、知识、指令遵循和多步骤任务方面对模型打分，本文用它来比较性价比。'智能体能力'指模型自主规划、行动并与工具交互的能力，是当前大模型市场定位的关键差异点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index</a></li>
<li><a href="https://hackernoon.com/notes-on-agentic-reasoning-for-large-language-models">Notes on Agentic Reasoning for Large Language Models | HackerNoon</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#AI models`, `#inference`, `#agentic AI`

---

<a id="item-3"></a>
## [Karpathy 提议用“骑自行车的鹈鹕”作为 AI 基准测试](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.5/10

安德烈·卡帕西（Andrej Karpathy）在推特上提议将“骑自行车的鹈鹕”用作 AI 物理世界理解的基准测试，并在 Hacker News 上引发讨论。 这一提议将 AI 评估从纯文本任务扩展到视觉和物理合理性，可能重塑社区衡量多模态模型与世界模型进步的方式。它检验生成模型是否真正理解现实世界约束，而不只是生成看似合理的像素。 该基准使用提示词“生成一只骑自行车的鹈鹕的 SVG”，由西蒙·威利森于 2024 年 10 月创建。它是一种非正式、定性的测试，考察模型能否以视觉和物理上连贯的方式呈现这种不可能的场景。

hackernews · delichon · Aug 2, 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: “骑自行车的鹈鹕”基准是一个非正式测试，要求 AI 模型生成一只骑自行车的鹈鹕的 SVG 图像，这是一个物理上不可能的场景。该基准由开发者西蒙·威利森于 2024 年 10 月创建，旨在检验模型的视觉与空间推理能力，补充 MMLU、GSM8K 等纯文本基准。随着学术界和工业界对“物理 AI”兴趣的增长，这类定性挑战有助于揭示模型是否真正理解现实世界的常识约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) - Grokipedia</a></li>
<li><a href="https://ai.miraheze.org/wiki/Pelican_Bicycle_Benchmark">Pelican Bicycle Benchmark - Learn AI</a></li>
<li><a href="https://www.ibm.com/think/topics/physical-ai">What is physical AI? - IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人担心模型生成的粗糙结果被当作“已解决”，反映出质量预期下降；另一些人则认为，不完美的输出恰恰是该基准用于衡量物理世界理解能力的意义所在。讨论中还提到，Anthropic 等模型可能只是擅长生成 three.js 代码，而非真正理解场景。

**标签**: `#AI`, `#benchmarking`, `#image generation`, `#Karpathy`, `#LLM`

---

<a id="item-4"></a>
## [AI 公开信交锋：开放权重、Anthropic 与前沿节奏控制](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.5/10

西蒙·威利森梳理了最近一波 AI 公开信。其中包括 7 月 24 日由微软主导、235 家公司（包括 NVIDIA 和 OpenAI）签署的开放权重公开信，三天后 Anthropic 的立场回应，以及 7 月 28 日由 1,324 名前沿 AI 公司员工签署的《Pacing the Frontier》公开信。 这些公开信暴露了 AI 行业在开放权重问题上的深刻分歧：微软等将开放视为安全和竞争的胜利，而 Anthropic 及许多前沿研究者则强调滥用风险和竞争压力的危险。相关政策结果可能影响美国如何监管模型发布、蒸馏技术和自动化 AI 研究。 微软的公开信明确为蒸馏作为合法的模型开发技术辩护，并警告不要将其与盗用混为一谈；而 Anthropic 拒绝签署，其 CEO 达里奥·阿莫迪反而呼吁打击工业规模的蒸馏操作（不过他表示 Anthropic 从未主张过禁令）。《Pacing the Frontier》的签署者包括 OpenAI 首席科学家 Jakub Pachocki、Ilya Sutskever 和 Dario Amodei。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型公开发布 AI 模型的训练后参数，任何人都可以下载、运行、研究或修改，介于完全开源和封闭 API 模型之间（斯坦福 HAI）。支持者认为这有助于外部审计、透明度和竞争，而批评者则担心被滥用于网络攻击、生物攻击或增强威权政府的能力。近期美国政府的行动，包括一项暂停访问某个前沿模型的指令，加剧了关于开放权重与安全的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/971690/dario-amodei-weighed-in-on-anthropics-open-weight-model-controversy">Dario Amodei weighed in on Anthropic’s open - weight model ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Weights`, `#Policy`, `#Open Source`, `#Simon Willison`

---

<a id="item-5"></a>
## [Datasette-apps 0.2a0 让 AI 代理能测试和编辑应用](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 7.3/10

datasette-apps 0.2a0 新增了 app_debug() 和 app_list() 两个工具，让 Datasette Agent 可以测试和编辑 Datasette Apps。其中 app_debug() 会在一个不可见的沙箱 iframe 中执行代理提供的 JavaScript，用于冒烟测试。 这一桥接把 AI 代理与应用测试连接起来，使 Datasette Agent 能够自主验证和修改 Datasette Apps。对于使用 Datasette 托管应用的开发者来说，AI 辅助的应用开发和维护将变得更加实用。 app_debug() 会通过 opacity: 0 和 pointer-events: none 的 iframe 隐藏应用，并在该沙箱 iframe 中执行代理提供的 JavaScript。它依赖 datasette-agent 0.4a0 中新增的 context.browser_task() 机制，而 app_list() 用于列出用户有权编辑的应用。

rss · Simon Willison · Aug 1, 21:23

**背景**: Datasette Apps 允许开发者在 Datasette 中托管 Web 应用，而 Datasette 是一个用于探索和发布数据的开源工具。Datasette Agent 是 Datasette 的一个由 LLM 驱动的可扩展 AI 助手；冒烟测试则是一种软件测试技术，用于在深入测试之前验证新构建的核心功能是否正常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/1/datasette-apps/">Release: datasette - apps 0.2a0 | Simon Willison’s Weblog</a></li>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/ datasette - apps : Apps that live inside Datasette</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help ...</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#AI agents`, `#agentic tools`, `#software release`, `#testing`

---

<a id="item-6"></a>
## [Bor v0.8：面向 Linux 桌面的开源策略管理工具](https://getbor.dev/blog/2026-08-02-bor-v080-release/) ⭐️ 7.2/10

Bor 于 2026 年 8 月 2 日发布 v0.8，新增了对 Thunderbird、Microsoft Edge for Business 和 FirewallD 区域的策略类型。该开源系统通过轻量级 Go agent 以 mTLS/gRPC 实时流式下发策略（不采用轮询），实现 Linux 桌面的集中管理。 Linux 桌面批量管理一直缺少优秀的开源方案，而此版本将策略覆盖扩展到常见的邮件、浏览器和防火墙工具。对于希望避免 Windows/Intune 等专有管理方案的非营利组织、企业和系统管理员来说，这是一个有前景的“策略即代码”替代选择。 现有策略目标包括 Firefox、Chrome、KDE、dconf、polkit 和软件包管理；v0.8 新增 Thunderbird、Edge for Business 与 FirewallD 区域。策略通过 mTLS/gRPC 实时推送，因此没有轮询间隔；发布说明还提到多项改进与修复，但尚未详细说明配置漂移后的回滚机制。

hackernews · eniac111 · Aug 2, 09:06 · [社区讨论](https://news.ycombinator.com/item?id=49142569)

**背景**: dconf 是 GNOME 及同类桌面环境使用的底层配置数据库，以键值对形式存储设置。polkit 是一个授权框架，允许特权程序向非特权客户端提供服务，常用于图形化 Linux 桌面实现细粒度访问控制。FirewallD 是一种动态管理防火墙，通过 zone（区域）定义网络连接或接口的信任级别。Bor 将这些组件作为策略目标，使管理员能从中心服务器统一强制桌面配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dconf">dconf - Wikipedia</a></li>
<li><a href="https://linuxconfig.org/introduction-to-polkit-navigating-authorization-frameworks-in-linux">Introduction to Polkit: Navigating Authorization Frameworks in Linux</a></li>
<li><a href="https://firewalld.org/">Home | firewalld</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上很感兴趣，表示这接近他们手工管理设备所需的产品，但同时提出了具体问题：是否支持 Cinnamon、能否执行自定义脚本、如何与 Authentik 等身份提供方集成、用户映射如何在 Linux 用户账户上生效，以及在没有轮询的情况下如何检测配置漂移。还有人询问它相比现有方案有何优势、为什么选用 mTLS 而非 SSH，并建议文档用 Mermaid 图替代 ASCII 图表。

**标签**: `#Linux`, `#open-source`, `#device-management`, `#Go`, `#policy-as-code`

---

<a id="item-7"></a>
## [OpenAI 的 Astra 模型以每个不到 2000 美元的成本解决十个长期未解的数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 7.2/10

OpenAI 宣布，其下一代主要模型的内部版本 Astra 解决了十个至少十年未取得进展的数学问题，按 GPT-5.6 Sol 的 token 价格计算，每个问题的花费不到 2000 美元。该公司在一个公共 GitHub 仓库中发布了所有十个证明的 Lean 4 形式化版本。 这一进展凸显了前沿 AI 模型在产生可验证的数学研究方面日益增强的能力，可能加速数学和理论计算机科学的进步。它也引发了关于如何透明评估 AI 的持续辩论，特别是关于未报告的失败尝试。 ten-proofs 仓库允许任何拥有 Lean 编译器的人独立验证每个证明，而无需信任 OpenAI。然而，Simon Willison 和一些观察者指出，OpenAI 没有披露有多少问题是在未成功的情况下尝试的，而且 OpenAI 的公开营销材料中并未列出 Astra 模型。

rss · Simon Willison · Aug 1, 20:34

**背景**: Lean 4 是一个交互式定理证明器，允许数学家以形式化方式编写证明并通过机器验证。数学家陶哲轩所描述的'大数学'理念设想人类与 AI 的大规模协作，由机器处理技术性繁重工作，人类专注于创造性部分。这一宣布也恰逢 Anthropic 的 Claude 被用于发现密码学弱点之后，显示出 AI 辅助研究方面的竞赛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/ten-proofs">GitHub - openai/ten-proofs: Lean certificates accompanying proofs in mathematics and theoretical computer science · GitHub</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT-5.6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://runtimewire.com/article/openai-astra-ten-open-math-problems">OpenAI says unreleased Astra model solved 10 open... - RuntimeWire</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#mathematics`, `#OpenAI`, `#research`

---

<a id="item-8"></a>
## [F*：面向证明的编程语言，用于形式化验证](https://fstar-lang.org/) ⭐️ 7.1/10

Hacker News 社区在链接到 F*官网后讨论了这种面向证明的编程语言。F*集成了依赖类型、单子效应和精化类型，用于验证程序正确性。 F*意义重大，因为它能在真实软件中验证安全性和功能正确性等属性，并已被微软研究院等机构采用。它弥合了形式化方法研究与实际编程之间的鸿沟，为构建经过验证的系统提供了一种通用语言。 F*可以编译到 OCaml、F#、C、WebAssembly（通过 KaRaMeL 工具）和汇编语言（通过 Vale 工具链）。其类型系统支持依赖类型、单子效应和精化类型，类型检查器通过 SMT 求解和手动证明相结合来验证规范。

hackernews · ducktective · Aug 2, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49143925)

**背景**: F*（读作 F star）是由微软研究院和法国国家信息与自动化研究所（Inria）联合开发的高级多范式语言，灵感来自 ML、Caml 和 OCaml。它旨在证明程序满足其规范，这对于加密协议、经过验证的编译器等高安全性软件非常有价值。自 2011 年以来，该语言一直在积极开发中，并在 GitHub 上可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language)</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof - Oriented Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区评论中有人批评 F*官网首页缺少代码示例，而另一位用户称赞了将现有 C 代码库逐步迁移到 F*的能力。还有几位用户询问了工业界的使用情况以及 F*对函数式编程新手的适用性。

**标签**: `#proof-oriented language`, `#formal verification`, `#F*`, `#programming languages`, `#software engineering`

---

<a id="item-9"></a>
## [墨西哥成为美国 AI 服务器最大进口来源，超越汽车](https://feeds.feedblitz.com/~/965674583/0/marginalrevolution~Mexico-Taiwan-fact-of-the-day.html) ⭐️ 7.0/10

墨西哥目前占美国 AI 数据中心所用计算机服务器进口量的 40%，服务器已取代汽车成为墨西哥对美第一大出口商品。台湾制造商正迅速扩大在墨西哥的工厂，以组装这些服务器。 这一事实突显墨西哥在 AI 供应链中悄然成为关键一环，正在改变北美制造业与贸易格局。同时也反映出台湾厂商在 AI 基础设施热潮中，将组装环节移近美国市场的趋势。 文中 40%的数据是指“今年”美国进口服务器的份额，报道未提供更细分的产品类别或厂商名单。服务器目前已取代汽车成为墨西哥对美最大出口商品，这是双边贸易关系中的一个显著转变。

rss · Marginal Revolution · Aug 2, 04:35

**背景**: 服务器是驱动数据中心运行的高性能计算机，AI 训练与推理尤其需要大量服务器。台湾是全球服务器设计与制造的重要枢纽，台厂将组装产线转移到墨西哥，有助于服务美国市场，同时让供应链更贴近北美。

**社区讨论**: 评论区意见不一：有人认为这一趋势并不令人意外，因为墨西哥长期是制造重镇；也有人提醒不要过于乐观。还有评论提及特朗普政府，另一些讨论则带有嘲讽语气。总体来看，读者大体接受这一数据，但对其政治和经济意义的解读存在分歧。

**标签**: `#AI infrastructure`, `#supply chain`, `#Mexico`, `#servers`, `#economics`

---