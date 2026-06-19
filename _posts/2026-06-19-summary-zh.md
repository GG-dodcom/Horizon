---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 95 items, 15 important content pieces were selected

---

1. [超越 LoRA：其他 PEFT 方法能击败 LoRA 吗？](#item-1) ⭐️ 9.2/10
2. [业余爱好者借助 AI 破解线形文字 A](#item-2) ⭐️ 8.8/10
3. [Project Valhalla 在 JDK 28 中实现：值类型与堆扁平化](#item-3) ⭐️ 8.5/10
4. [MosaicLeaks：研究型 AI 助手的隐私风险](#item-4) ⭐️ 8.5/10
5. [为开源模型评估智能体能力](#item-5) ⭐️ 8.5/10
6. [GLM-5.2：领先的开源 LLM，拥有 1M 上下文](#item-6) ⭐️ 8.4/10
7. [迈克尔·莫顿谈 AI 时代的电子商务](#item-7) ⭐️ 8.3/10
8. [Claude Code v2.1.183 新增破坏性命令安全拦截](#item-8) ⭐️ 8.0/10
9. [Anjney Midha 访谈：Outputmaxxing 教授](#item-9) ⭐️ 8.0/10
10. [ATProto 没有实例，Dan Abramov 解释](#item-10) ⭐️ 7.9/10
11. [Datasette Apps：在 Datasette 中托管沙盒化 HTML+JS 应用](#item-11) ⭐️ 7.8/10
12. [挪威禁止小学生使用人工智能](#item-12) ⭐️ 7.6/10
13. [ALS 患者成为首位长期 BCI 重度使用者](#item-13) ⭐️ 7.6/10
14. [Stratechery 周报聚焦 Anthropic 与 AI 电商](#item-14) ⭐️ 7.5/10
15. [Vercel AI SDK 工作流修复提供商执行工具审批漏洞](#item-15) ⭐️ 7.2/10

---

<a id="item-1"></a>
## [超越 LoRA：其他 PEFT 方法能击败 LoRA 吗？](https://huggingface.co/blog/peft-beyond-lora) ⭐️ 9.2/10

Hugging Face 博客文章《超越 LoRA：你能击败最流行的微调技术吗？》探讨了其他参数高效微调（PEFT）方法是否能在大型语言模型微调中胜过 LoRA，提供了技术对比和实用见解。 这项分析意义重大，因为 LoRA 是目前主流的 PEFT 方法，找到更优的替代方案可以降低计算成本并提升模型性能，直接影响 LLM 微调的效率和可及性。 该博客可能比较了 LoRA 与 MoRA（高秩更新）及其他 LoRA 变体，讨论了参数效率、训练速度和最终模型质量之间的权衡。技术细节可能包括秩的选择、更新约束和适配器架构。

rss · Hugging Face Blog · Jun 18, 00:00

**背景**: 参数高效微调（PEFT）通过仅更新一小部分参数来适配大型预训练模型，从而减少内存和计算。LoRA（低秩适应）是最流行的 PEFT 方法，它插入可训练的低秩矩阵。像 MoRA 这样的替代方法旨在实现更高秩的更新以获得更好的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2405.12130">MoRA: High-Rank Updates for Fine - Tuning</a></li>

</ul>
</details>

**标签**: `#LoRA`, `#fine-tuning`, `#PEFT`, `#LLM`, `#Hugging Face`

---

<a id="item-2"></a>
## [业余爱好者借助 AI 破解线形文字 A](https://aiclambake.com/clamtakes/linear-a/) ⭐️ 8.8/10

业余研究员 Tom Di Mino 使用 Anthropic 的 Claude Code 构建了 Python 脚本，系统性地对线形文字 A 语料库进行假设检验，可能取得了破译这一未解米诺斯文字的重大突破。 如果得到验证，这将是线形文字 A 在一个多世纪以来首次成功破译，展示了 AI 辅助工具如何加速解决传统方法难以攻克的复杂难题。 Di Mino 的方法基于'奠酒公式'翻译了 300 多个单词，并且不是将 Claude Code 当作黑箱解答器，而是用它构建假设检验工具。他的成果正在由罗格斯大学和剑桥大学的语言学家审查。

hackernews · Kosturdistan · Jun 19, 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48600107)

**背景**: 线形文字 A 是米诺斯文明在公元前 1800 年至 1450 年间使用的文字。尽管它与已破译的线形文字 B（1950 年代被确认为古希腊语的一种早期形式）共享许多符号，但由于其底层语言未知，线形文字 A 至今未能破译。Claude Code 是 Anthropic 开发的一款 AI 编程代理，能够跨多个文件读取和编辑代码库，使非技术人员也能构建软件工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A">Linear A - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 社区评论者持谨慎乐观态度：有人指出 Di Mino 的工作正在接受罗格斯大学和剑桥大学专家的审查，并且他翻译了 300 多个单词是前所未有的。另一位评论者赞扬了借助 AI 构建工具而非作为黑箱解答器的做法。也有人提到其他未破译的文字，如印度河文字。

**标签**: `#AI`, `#Linear A`, `#decipherment`, `#ancient scripts`, `#LLM applications`

---

<a id="item-3"></a>
## [Project Valhalla 在 JDK 28 中实现：值类型与堆扁平化](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.5/10

经过十年的开发，Project Valhalla 的值类型和堆扁平化功能将在 JDK 28 中实现，它从根本上改变了 Java 处理对象的方式，允许在没有对象头或间接指针的情况下进行密集存储。 这提高了 Java 应用程序的内存密度和性能，特别是对于数据密集型工作负载，并使其在保持安全保证的同时更接近 C 或 Rust 等语言的性能。 堆扁平化仅适用于 64 位以内的值对象，因此较大的值对象可能无法完全受益。该实现要求值类型不可变、非空且无标识。

hackernews · philonoist · Jun 19, 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Project Valhalla 是 OpenJDK 的一个项目，始于 2014 年，旨在为 Java 引入值类型，目标是将对象的抽象性与基本类型的性能结合起来。值类型是用户定义的类型，其行为类似于基本类型，没有对象标识或对象头。堆扁平化是一种关键优化，它将值类型字段直接存储在数组或对象中，消除了指针间接引用并减少了内存开销。这对于小型数据对象的集合特别有利，例如点或复数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language)</a></li>
<li><a href="https://openjdk.org/projects/valhalla/">Project Valhalla</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS - Inside.java</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对可读性和一致性的担忧，一些人认为值类打破了最小惊奇原则，因为赋值行为与引用类不同。其他人则为设计辩护，指出 Java 已经发生了显著变化，值类型提供了实质性的性能优势。

**标签**: `#Java`, `#JVM`, `#Project Valhalla`, `#Programming Languages`, `#Performance`

---

<a id="item-4"></a>
## [MosaicLeaks：研究型 AI 助手的隐私风险](https://huggingface.co/blog/ServiceNow/mosaicleaks) ⭐️ 8.5/10

ServiceNow 在 Hugging Face 博客上发布了 MosaicLeaks 基准测试，用于评估 AI 研究助手的隐私漏洞，发现许多助手会无意中泄露用户查询中的敏感信息。 随着 AI 研究助手在自动数据收集和分析中的广泛使用，该基准测试揭示了关键的隐私风险，可能泄露机密数据，影响依赖这些工具处理敏感任务的用户和组织。 MosaicLeaks 基准测试通过构造包含私人信息的查询并监控助手的处理方式来系统性地测试研究助手，发现许多助手在其输出和内部日志中未能擦除或保护这些数据。

rss · Hugging Face Blog · Jun 18, 18:13

**背景**: AI 研究助手是能够自主执行多步网页浏览、文档分析和报告生成的系统。与基于 LLM 的其他应用类似，这些助手的隐私漏洞可能源于提示注入、数据保留和输出清洗不足。

**标签**: `#AI`, `#LLM`, `#privacy`, `#agent security`

---

<a id="item-5"></a>
## [为开源模型评估智能体能力](https://huggingface.co/blog/is-it-agentic-enough) ⭐️ 8.5/10

Hugging Face 发布了一份指南，介绍如何使用自定义工具和评估框架来基准测试开源大语言模型的智能体能力。 随着智能体 AI 的兴起，为开源模型建立标准化的基准测试方法有助于开发者选择适合工具使用、规划和自主任务的模型。 该指南涵盖了设置工具使用、多步推理和智能体工作流评估的实用步骤，强调针对特定用例进行定制。

rss · Hugging Face Blog · Jun 18, 00:00

**背景**: 智能体 AI 指的是能够独立规划、使用工具和执行多步骤任务以实现目标的语言模型。与标准聊天机器人不同，智能体系统需要可靠的基准测试来保证可靠性。开源模型缺乏标准化的智能体基准测试，因此这份指南对社区非常有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Comparison_of_agentic_capabilities_in_major_LLM_vendors_2026">Comparison of agentic capabilities in major LLM vendors (2026)</a></li>
<li><a href="https://benchlm.ai/agentic">Agentic Benchmarks 2026: Tool Use, Browsing, Computer Use</a></li>
<li><a href="https://artificialanalysis.ai/models/capabilities/agentic">Agentic Index - Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#Agentic AI`, `#LLM`, `#Benchmarking`, `#Open Models`

---

<a id="item-6"></a>
## [GLM-5.2：领先的开源 LLM，拥有 1M 上下文](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 8.4/10

Z.ai 于 2026 年 6 月 16 日发布了 GLM-5.2，这是一个 753B 参数的混合专家模型，具有 100 万 token 的上下文窗口，采用 MIT 许可证。它在 Artificial Analysis Intelligence Index 上以 51 分成为排名最高的开源模型，超越了 MiniMax-M3 和 DeepSeek V4 Pro。 这表明开源模型正在不断缩小与专有模型的差距，提供了高性价比的替代方案。GLM-5.2 在编码和推理任务中的强劲表现，加上 MIT 许可证，可能加速 AI 在研究和生产中的应用。 GLM-5.2 通过 MoE 使用 40 个活跃参数，需要 1.51TB 存储空间，上下文窗口从前代的 20 万扩展到 100 万 token。它是纯文本模型，视觉能力在 GLM-5V-Turbo 中单独提供（未开源）。

rss · Simon Willison · Jun 17, 23:58

**背景**: 大型语言模型（LLM）是在海量文本数据上训练的神经网络，用于生成类人文本。混合专家（MoE）是一种架构，每次输入仅激活部分参数，从而实现大模型规模的高效计算。上下文窗口决定模型一次能考虑的文本量；100 万 token 窗口允许一次性处理整本书或超长文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.innovatrixinfotech.com/blog/context-windows-explained-1-million-tokens-architecture">1 Million Token Context Window: What It Means for Builders | Innovatrix Infotech</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open weights`, `#GLM`, `#AI research`, `#artificial intelligence`

---

<a id="item-7"></a>
## [迈克尔·莫顿谈 AI 时代的电子商务](https://stratechery.com/2026/an-interview-with-michael-morton-about-e-commerce-in-the-age-of-ai/) ⭐️ 8.3/10

在 Stratechery 的一篇采访中，迈克尔·莫顿讨论了 AI 如何改变电子商务，涵盖了不可证伪的看跌观点、分销与推荐模式的对比，以及杂货配送和自动驾驶汽车的挑战。 这次采访提供了专家关于 AI 如何重塑电子商务分销模型以及解决杂货盈利等长期行业挑战的战略见解。对于任何参与电子商务策略和 AI 应用的人来说，都具有重要价值。 采访特别探讨了不可证伪的看跌观点（即无法被反驳的悲观情景），并对比了分销模式（公司拥有库存）与推荐模式（连接客户与卖家）。还深入分析了杂货电商的独特困难以及自动驾驶汽车的潜力。

rss · Stratechery · Jun 18, 10:00

**背景**: 「不可证伪的看跌观点」指的是无法被证明为假的悲观断言，这一概念源于卡尔·波普尔的可证伪性原则。在电子商务中，分销模式涉及直接拥有库存和物流，而推荐模式则通过第三方推荐产生潜在客户或销售，不持有库存。理解这些区别对于评估 AI 时代的商业策略至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falsifiability">Falsifiability - Wikipedia</a></li>
<li><a href="https://awealthofcommonsense.com/2020/08/bull-case-bear-case/">Bull Case / Bear Case - A Wealth of Common Sense</a></li>
<li><a href="https://www.salesforce.com/sales/distribution-channels/">Distribution Channels: Types, Examples, and Benefits</a></li>

</ul>
</details>

**标签**: `#AI`, `#e-commerce`, `#strategy`, `#interview`, `#Michael Morton`

---

<a id="item-8"></a>
## [Claude Code v2.1.183 新增破坏性命令安全拦截](https://github.com/anthropics/claude-code/releases/tag/v2.1.183) ⭐️ 8.0/10

Claude Code v2.1.183 引入了对破坏性 git 命令（如 git reset --hard 和 git clean -fd）以及 terraform destroy、pulumi destroy、cdk destroy 的安全拦截，除非用户明确要求。同时新增了模型弃用警告（显示在 stderr）、/config --help 命令以及多项 bug 修复。 此更新显著提高了开发者使用 Claude Code 的安全性，防止意外丢失工作或破坏基础设施。这体现了 Anthropic 对负责任 AI 工具开发的承诺，并解决了代理式编码工作流中的常见痛点。 如果用户未要求放弃本地工作，破坏性 git 命令将被拦截；如果提交并非当前会话中的代理创建，git commit --amend 也会被拦截。模型弃用警告现在也覆盖了在代理 frontmatter 中设置的模型，而不仅仅是打印模式下的模型。

github · ashwin-ant · Jun 19, 01:20

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手，可在终端、IDE 和浏览器中运行，能读取代码库、编辑文件和执行命令。作为一个代理式编码系统，它可能执行 git 重置或基础设施销毁等破坏性操作，因此安全措施至关重要。此更新还修复了子代理生成、终端渲染和 MCP 服务器认证等多个 bug。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://developer.hashicorp.com/terraform/cli/commands/destroy">terraform destroy command reference | Terraform | HashiCorp ...</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#AI tools`, `#safety`, `#git`, `#Anthropic`

---

<a id="item-9"></a>
## [Anjney Midha 访谈：Outputmaxxing 教授](https://www.latent.space/p/anj) ⭐️ 8.0/10

AMP 的风险投资人 Anjney Midha 分享了他从新加坡起步到主导投资 Anthropic、Mistral、Black Forest Labs 和 Periodic Labs 的经历，以及 AMP 的秘密切计划。 这次访谈提供了对关键 AI 初创公司投资的罕见内部视角，揭示了该领域一些最具影响力公司背后的策略。 访谈涵盖了 Midha 在新加坡的卑微出身以及他在资助 Anthropic 和 Mistral 等知名 AI 初创公司中的角色，并透露了 AMP 一个未公开的“秘密切计划”。

rss · Latent Space · Jun 18, 17:30

**背景**: Anjney Midha 是 AMP 的风险投资人，该公司投资了多家知名 AI 公司。Anthropic 和 Mistral 是专注于开发先进大型语言模型的领先 AI 初创公司。Black Forest Labs 和 Periodic Labs 也是 AMP 投资组合的一部分，尽管它们不太为人所知。

**标签**: `#AI`, `#Venture Capital`, `#Anthropic`, `#Mistral`, `#Startups`

---

<a id="item-10"></a>
## [ATProto 没有实例，Dan Abramov 解释](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.9/10

Dan Abramov 发表博客文章，解释 ATProto 没有像 Mastodon 那样的‘实例’，而是将角色分离为个人数据服务器（PDS）、中继（Relay）和应用视图（AppView）。 这一澄清对于探索去中心化社交协议的开发者和用户至关重要，因为它突显了 ATProto 与基于 ActivityPub 的系统（如 Mastodon）之间的根本架构差异。 该博客使用 RSS 类比：PDS 类似于 Feed 源，Relay 类似于 Feed 阅读器的聚合，AppView 类似于阅读器的显示。这与 Mastodon 中单个‘实例’处理所有这些角色形成对比。

hackernews · danabramov · Jun 19, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: ATProto（认证传输协议）是驱动 Bluesky 的去中心化协议。与 ActivityPub 的联合模式（每个服务器（实例）托管账户和内容）不同，ATProto 分离了数据存储（PDS）、索引（Relay）和应用逻辑（AppView）。这种分离旨在提高可扩展性和用户控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://github.com/bluesky-social/atproto/discussions/3036">Relay Operational Updates · bluesky-social/atproto · Discussion #3036</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：有人赞赏澄清但不同意 RSS 类比，指出博客比 ATProto 组件更自足。其他人赞扬职责分离的可扩展设计。也有读者感到沮丧，文章没有说明 ATProto 如何解决像去联邦化这样的问题。

**标签**: `#ATProto`, `#Bluesky`, `#decentralized protocols`, `#federation`

---

<a id="item-11"></a>
## [Datasette Apps：在 Datasette 中托管沙盒化 HTML+JS 应用](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.8/10

Simon Willison 宣布了 datasette-apps 插件，该插件允许用户在 Datasette 内部托管和运行自定义 HTML+JavaScript 应用，这些应用运行在沙盒化的 iframe 中，并能够对底层数据执行只读或可选的写入 SQL 查询。 该插件将 Datasette 从一个数据探索工具扩展为一个完整的应用平台，使开发者能够直接在 Datasette 内部构建交互式数据驱动的 Web 应用，同时不影响安全性。它还复用了 Claude Artifacts 的沙盒模式，为安全托管第三方应用提供了一个实用模型。 应用在带有 sandbox="allow-scripts allow-forms" 的 iframe 中运行，并注入内容安全策略以阻止出站 HTTP 请求，防止数据泄露。该插件还提供了一个插件钩子，允许其他插件添加自己的 Python 应用。

rss · Simon Willison · Jun 18, 23:58

**背景**: Datasette 是一个开源的数据探索和发布工具，基于 SQLite 构建，提供 JSON API 和 Web 界面用于查询数据库。datasette-apps 插件允许开发者嵌入自定义的 HTML+JavaScript 前端，与 API 交互，类似于 Claude Artifacts 的工作方式，但在 Datasette 生态系统中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps: Host custom HTML applications inside Datasette</a></li>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/datasette-apps: Apps that live inside Datasette · GitHub</a></li>

</ul>
</details>

**标签**: `#datasette`, `#plugin`, `#SQL`, `#web applications`, `#developer tools`

---

<a id="item-12"></a>
## [挪威禁止小学生使用人工智能](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 7.6/10

挪威宣布原则上禁止 6 至 13 岁小学生使用人工智能，14 至 16 岁初中生可在教师监督下谨慎使用，该规定自 2026 年起生效。 该政策旨在保护阅读、写作和理解等基础学习技能，这些技能可能被生成式 AI 削弱。它为全球教育领域的 AI 监管树立了一个重要先例。 该禁令原则上适用于 1 至 7 年级学生，教师可酌情例外处理。年龄较大的学生仅在严格监督下允许使用 AI 工具。

hackernews · ilreb · Jun 19, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48600093)

**背景**: 挪威教育体系注重早期基础技能培养。人们日益担忧聊天机器人等 AI 工具可能阻碍批判性思维和核心能力的发展。其他国家也在就课堂中使用 AI 展开类似辩论。

**社区讨论**: Hacker News 上的评论普遍支持这一禁令，有用户将其比作在学生理解算术之前不发放计算器。一些人指出教师自身可能滥用 AI 生成错误练习的风险。不过，有用户质疑低龄学生实际使用 AI 的具体方式。

**标签**: `#AI regulation`, `#education`, `#Norway`, `#LLM policy`, `#technology in schools`

---

<a id="item-13"></a>
## [ALS 患者成为首位长期 BCI 重度使用者](https://www.technologyreview.com/2026/06/19/1139270/brain-computer-interface-trials-are-taking-off/) ⭐️ 7.6/10

罹患肌萎缩侧索硬化症（ALS）的凯西·哈雷尔（Casey Harrell）成为首位长期“重度使用”脑机接口的患者，借助植入设备进行交流已近三年。 这一里程碑表明脑机接口可为严重瘫痪患者提供持续的实用功能，为扩大临床应用和改善生活质量铺平道路。 哈雷尔无法活动且无法脱离设备说话；因其三年间每日大量使用，研究人员称其为首位“重度使用者”。

rss · MIT Tech Review · Jun 19, 09:00

**背景**: 脑机接口（BCI）是一种解码神经信号以控制外部设备的系统，常用于帮助瘫痪者恢复交流或运动能力。ALS（肌萎缩侧索硬化症）会逐步破坏运动神经元，导致随意肌控制丧失。该试验凸显了 BCI 在耐用性和易用性方面的进步。

**标签**: `#brain-computer interface`, `#neuroscience`, `#ALS`, `#medical technology`, `#neural implants`

---

<a id="item-14"></a>
## [Stratechery 周报聚焦 Anthropic 与 AI 电商](https://stratechery.com/2026/the-stuff-of-mythos/) ⭐️ 7.5/10

Ben Thompson 的 Stratechery 于 2026 年 6 月 15 日发布周报，重点介绍了关于 AI 公司 Anthropic、AI 对电商的影响以及对 NBA 总决赛的满分分析。 该周报集中分析了关键的 AI 发展，特别是 Anthropic 对安全性的关注，以及不断变化的电商格局，对科技从业者和投资者具有重要价值。 周报形式意味着内容是精选列表而非单篇深度文章；NBA 总决赛的评论被评为满分 10 分，表明高度赞赏。

rss · Stratechery · Jun 19, 17:00

**背景**: Stratechery 是 Ben Thompson 运营的订阅制科技分析网站，专注行业战略。Anthropic 是一家专注于构建安全、可解释 AI 系统的 AI 研究公司，旗下有 Claude 模型。该周报反映了 Thompson 对高影响力 AI 应用的关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#e-commerce`, `#Ben Thompson`, `#Stratechery`

---

<a id="item-15"></a>
## [Vercel AI SDK 工作流修复提供商执行工具审批漏洞](https://github.com/vercel/ai/releases/tag/%40ai-sdk/workflow%401.0.0-beta.100) ⭐️ 7.2/10

Vercel 发布了 @ai-sdk/workflow@1.0.0-beta.100，修复了一个漏洞：在恢复时，提供商执行的工具审批未能转发给提供商。 此修复确保提供商执行的工具（例如通过 OpenAI Responses API 的 MCP）能正确接收审批信号，避免静默失败。依赖 AI SDK 进行代理工作流的开发者将获得更可靠的工具执行。 该漏洞是因为 WorkflowAgent 在恢复时剥离了所有 tool-approval-request 和 tool-approval-response 消息，无论工具是本地执行还是提供商执行。本地审批仍会被剥离，但提供商执行的审批现在会被保留并转发。

github · github-actions[bot] · Jun 18, 21:56

**背景**: Vercel 的 AI SDK 提供统一的 API 用于构建 AI 驱动的应用，包括工具调用功能。在代理工作流中，工具可能需要用户审批后才能执行，这种审批可以由本地或提供商（如 OpenAI）处理。模型上下文协议（MCP）允许提供商远程执行工具。此修复使工作流行为与 streamText 的判别器核心逻辑一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling">AI SDK Core: Tool Calling</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-connectors-mcp">MCP and Connectors | OpenAI API</a></li>

</ul>
</details>

**标签**: `#AI SDK`, `#workflow`, `#tool approval`, `#bug fix`, `#Vercel`

---