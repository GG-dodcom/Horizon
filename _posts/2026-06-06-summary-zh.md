---
layout: default
title: "Horizon Summary: 2026-06-06 (ZH)"
date: 2026-06-06
lang: zh
---

> From 89 items, 13 important content pieces were selected

---

1. [Vercel AI SDK 实验性版本添加实时语音 API 支持](#item-1) ⭐️ 9.3/10
2. [谷歌每月向 SpaceX 支付 9.2 亿美元计算费用](#item-2) ⭐️ 9.0/10
3. [莱比锡基准测试 LLMs 的博士级数学能力](#item-3) ⭐️ 9.0/10
4. [Zeroserve：可使用 eBPF 脚本的零配置 Web 服务器](#item-4) ⭐️ 8.8/10
5. [Meta 通过 AI 助手被黑凸显更广泛的 AI 安全风险](#item-5) ⭐️ 8.7/10
6. [Claude Code v2.1.166 新增回退模型与 Glob 拒绝规则](#item-6) ⭐️ 8.6/10
7. [用 MicroPython 和 WebAssembly 沙箱运行 Python](#item-7) ⭐️ 8.5/10
8. [OpenAI 推出 ChatGPT 锁定模式防范提示注入攻击](#item-8) ⭐️ 8.4/10
9. [如何停止发布低质量的强化学习环境](#item-9) ⭐️ 8.4/10
10. [英伟达为 Windows PC 提议强大 CPU 系统](#item-10) ⭐️ 7.9/10
11. [五个实验室使用小型模型构建多模型金融剧](#item-11) ⭐️ 7.8/10
12. [标普 500 拒绝 SpaceX、OpenAI 和 Anthropic 加入](#item-12) ⭐️ 7.5/10
13. [心理学家警告：AI 聊天机器人可能削弱我们的认知控制](#item-13) ⭐️ 7.2/10

---

<a id="item-1"></a>
## [Vercel AI SDK 实验性版本添加实时语音 API 支持](https://github.com/vercel/ai/releases/tag/ai%407.0.0-canary.165) ⭐️ 9.3/10

Vercel 的 AI SDK v7.0.0-canary.165 增加了对实时语音对话的实验性支持，包含 OpenAI、Google 和 xAI 三家的实现，以及面向服务端和浏览器端的新钩子和工具函数。 此次发布将多家提供商的实时语音能力统一到一个 SDK 中，简化了语音 AI 应用的开发。与现有聊天钩子（useChat）的对齐降低了构建对话界面的学习成本。 重要新增包括 @ai-sdk/provider 中的 Experimental_RealtimeModelV4 规范、类似 openai.experimental_realtime() 的提供商工厂函数，以及返回 UIMessage[] 的 experimental_useRealtime 钩子，支持 onToolCall 和 addToolOutput 实现客户端驱动的工具执行。

github · github-actions[bot] · Jun 5, 04:41

**背景**: Vercel AI SDK 是一个用于构建 AI 应用的统一工具包，提供聊天、文本补全以及现在的实时语音交互等钩子和工具。Canary 版本是用于测试新功能的早期预览版。实时语音对语音 API 可实现与 AI 模型之间的低延迟语音对话，并使用临时令牌进行安全服务端认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-sdk.dev/">AI SDK</a></li>
<li><a href="https://ai-sdk.dev/docs/getting-started/nextjs-app-router">Learn how to build your first agent with the AI SDK and Next.js App...</a></li>

</ul>
</details>

**标签**: `#AI SDK`, `#Realtime API`, `#voice conversations`, `#Vercel`, `#LLM tooling`

---

<a id="item-2"></a>
## [谷歌每月向 SpaceX 支付 9.2 亿美元计算费用](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) ⭐️ 9.0/10

谷歌已同意每月向 SpaceX 支付 9.2 亿美元，以使用 xAI 的数据中心获得计算能力，这项交易大幅提升了 SpaceX 的营收和估值。 该交易通过利用 SpaceX 的计算资源重塑了云和 AI 基础设施，可能影响大型科技公司获取 AI 计算能力的方式。 谷歌此前投资持有 SpaceX 约 5%股份；该交易使 SpaceX 年收入增加 110 亿美元，若保持 94 倍市销率，将推动 SpaceX 估值增加约 1 万亿美元。

hackernews · ramanan · Jun 6, 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48423990)

**背景**: xAI 由埃隆·马斯克于 2023 年创立，在 2026 年合并后成为 SpaceX 的子公司。xAI 运营 Colossus 超级计算机并提供 AI 计算服务，包括向谷歌等云提供商出租数据中心容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>

</ul>
</details>

**社区讨论**: 评论者认为该交易是金融工程，有人指出谷歌通过 5%的持股从 SpaceX 估值提升中获利 500 亿美元。其他人质疑谷歌的 TPU 优化代码能否在 xAI 的 Nvidia GPU 上运行，并将其类比为泡沫。

**标签**: `#AI`, `#cloud`, `#infrastructure`, `#SpaceX`, `#Google`

---

<a id="item-3"></a>
## [莱比锡基准测试 LLMs 的博士级数学能力](https://arxiv.org/abs/2606.05818) ⭐️ 9.0/10

研究人员发布了莱比锡基准测试，包含一系列研究级数学问题，旨在测试 LLMs 解决博士级问题的能力，顶尖模型仍难以达到高准确率。 该基准测试将 LLM 评估推向超越典型考题的水平，揭示即使最先进的模型在数学推理方面仍有显著差距，这对其在科学研究和教育中的可靠性有直接影响。 该研究包括三个阶段：五个模型的单次尝试、三个模型的 20 次运行评估，以及两个深度思考模型的 3 次尝试。所有阶段结束后，初始问题集中只有 2 个未被任何模型解决。

hackernews · root-parent · Jun 6, 14:00 · [社区讨论](https://news.ycombinator.com/item?id=48425247)

**背景**: 莱比锡基准测试包含来自数学研究的问题，难度远高于典型考题，需要深度理解而非模式匹配。该基准使用严格的审查流程，包括人类数学家和 AI 辅助检查，以确保问题正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.05818">[2606.05818] Benchmarks in Leipzig</a></li>
<li><a href="https://arxiv.org/html/2606.05818v1">Benchmarks in Leipzig A collection of questions in research-level mathematics</a></li>

</ul>
</details>

**社区讨论**: 基准测试作者强调问题难度远高于任何考试，博士生需数天到数周。部分评论者讨论模型是否能通过训练数据作弊，其他人则强调衡量错误答案对评估可靠性的重要性。

**标签**: `#AI`, `#LLM`, `#benchmark`, `#mathematics`, `#PhD-level`

---

<a id="item-4"></a>
## [Zeroserve：可使用 eBPF 脚本的零配置 Web 服务器](https://su3.io/posts/introducing-zeroserve) ⭐️ 8.8/10

Zeroserve 是一款新的零配置 Web 服务器，它利用 eBPF 进行脚本扩展，用户可以用 C 语言编写过滤和路由逻辑并加载到 eBPF 虚拟机中。它旨在用可编程方式替代 nginx 和 Caddy 等传统服务器。 这引入了一种新的 Web 服务器配置范式，从声明式配置文件转向可编程的 eBPF 脚本，可能提供更卓越的性能和灵活性。它可能改变开发者构建和扩展 Web 服务器的方式，尤其是在性能敏感的环境中。 Zeroserve 是单线程的，使用 io_uring 进行异步 I/O，并直接从 tar 归档文件中提供静态文件服务，无需解压到磁盘。目前它仅支持静态文件服务，缺少 CGI 或反向代理等功能，这些功能计划在未来版本中实现。

hackernews · losfair · Jun 6, 14:59 · [社区讨论](https://news.ycombinator.com/item?id=48425723)

**背景**: eBPF（扩展的伯克利数据包过滤器）是一种 Linux 内核技术，允许在内核空间安全运行沙盒程序，通常用于网络、安全和可观测性。Zeroserve 利用 eBPF 在内核空间运行用户定义的请求处理脚本，以提高效率。这种方法与传统 Web 服务器使用用户空间配置语言的方式形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EBPF">EBPF</a></li>
<li><a href="https://github.com/losfair/zeroserve">GitHub - losfair/zeroserve: Zero-config, fast `io_uring`-based HTTPS server.</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对将 Zeroserve 与其他 BPF 类型（如 XDP）结合的兴趣，并指出 nginx 已经令人印象深刻。还有人建议支持 Rust 文件进行脚本编写。总体态度积极但谨慎，因为该项目尚处于早期阶段。

**标签**: `#eBPF`, `#web server`, `#programming`, `#dev tools`, `#zero-config`

---

<a id="item-5"></a>
## [Meta 通过 AI 助手被黑凸显更广泛的 AI 安全风险](https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/) ⭐️ 8.7/10

攻击者利用 Meta 的 AI 客服助手，通过简单要求该助手将账户链接到其控制的邮箱地址，劫持了 Instagram 账户，自 2026 年 4 月 17 日至 6 月初，至少 20,225 个账户被入侵。 此事件表明，AI 安全不仅限于对模型输出的对抗性攻击，还包括对连接到关键操作（如账户恢复）的 AI 系统的滥用。它凸显了在 AI 赋能的工作流中需要强大的访问控制和验证，尤其在公司部署面向客户的 AI 代理时。 Meta 表示，AI 助手本身按预期工作，但另一条代码路径中的漏洞未能验证提供的邮箱是否与账户注册邮箱匹配。攻击者获得了 Instagram 账户及关联 Facebook 账户的完全访问权限，包括私信和联系信息。

rss · MIT Tech Review · Jun 5, 09:00

**背景**: AI 代理可以连接到后端工具（如密码重置系统），从而代表用户执行操作。然而，如果这些代理容易受到提示注入攻击或缺乏适当的输入验证，攻击者可以诱使它们执行未授权的操作，例如账户劫持。此事件突出了 AI 安全中“工具滥用”的概念，与传统的对抗样本或数据投毒威胁不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techscoop.substack.com/p/the-hidden-cybersecurity-lesson-behind">The Hidden Cybersecurity Lesson Behind Instagram’s Account Hijacking Crisis</a></li>
<li><a href="https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/">Fooling AI Agents : Web-Based Indirect Prompt Injection Observed in...</a></li>
<li><a href="https://www.darshanturakhia.com/blog/prompt-injection-ai-agent-data-leak">The Prompt Injection That Silently Leaked Customer Data for 72...</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Meta 声称 AI 助手“正常工作”表示怀疑，因为该状态助长了账户劫持。涉及 20,225 个账户的规模被描述为惊人。部分用户还表达了对 Meta 自动审核及缺乏人工申诉流程的不满。

**标签**: `#AI security`, `#LLM`, `#Meta hack`, `#Instagram`, `#adversarial attacks`

---

<a id="item-6"></a>
## [Claude Code v2.1.166 新增回退模型与 Glob 拒绝规则](https://github.com/anthropics/claude-code/releases/tag/v2.1.166) ⭐️ 8.6/10

Anthropic 发布了 Claude Code v2.1.166，新增了回退模型配置、glob 模式拒绝规则支持、跨会话安全强化、思考令牌禁用以及多项错误修复。 这些更新增强了开发者使用 Claude Code 的可靠性和灵活性，当主模型不可用时可以实现无缝回退，并提升了跨会话的安全性。 fallbackModel 设置支持最多三个回退模型，拒绝规则中的 glob 模式允许使用 '*' 阻止所有工具或指定工具名称。现在可以通过 MAX_THINKING_TOKENS=0 或 --thinking disabled 禁用思考功能。

github · ashwin-ant · Jun 6, 00:55

**背景**: Claude Code 是 Anthropic 推出的基于终端的 AI 编码工具，使用 Claude 模型协助软件开发任务。它通过 MCP（模型上下文协议）与外部工具和服务集成。此更新改进了模型回退、安全性以及用户对思考行为的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/mcp">Connect Claude Code to tools via MCP - Claude Code Docs</a></li>
<li><a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet and Claude Code \ Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/common-workflows">Common workflows - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#AI tooling`, `#release notes`, `#LLM`, `#productivity`

---

<a id="item-7"></a>
## [用 MicroPython 和 WebAssembly 沙箱运行 Python](https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything) ⭐️ 8.5/10

Simon Willison 发布了一个名为 micropython-wasm 的 alpha 包，它将 MicroPython 编译为 WebAssembly，从而可以在沙箱中安全运行 Python 代码。该包通过 datasette-agent-micropython 插件与 Datasette Agent 集成。 这种方法可能彻底改变插件系统，通过安全、沙箱化地运行用户提供的 Python 代码，而不危及宿主应用。它解决了软件可扩展性中长期存在的挑战，尤其适用于 Datasette 和 LLM 等项目。 该沙箱设置了内存和 CPU 限制，防止失控进程导致应用崩溃。依赖项可以从 PyPI 干净安装，包括跨平台的二进制 wheels。

rss · Simon Willison · Jun 6, 03:53

**背景**: MicroPython 是 Python 3 的精简实现，专为微控制器和资源受限设备优化。WebAssembly (WASM) 是一种二进制指令格式，可在现代浏览器和独立运行时的沙箱环境中执行。将它们结合，可以在隔离环境中运行 Python 代码，防止文件访问、网络连接等不安全操作。沙箱化对于运行不受信任的代码（如插件或用户脚本）且不损害安全性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://micropython.org/">MicroPython - Python for microcontrollers</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#sandbox`, `#micropython`, `#webassembly`, `#python`, `#datasette`

---

<a id="item-8"></a>
## [OpenAI 推出 ChatGPT 锁定模式防范提示注入攻击](https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything) ⭐️ 8.4/10

OpenAI 已为 ChatGPT 推出锁定模式（Lockdown Mode），这是一项安全功能，旨在通过限制出站网络请求来防止提示注入攻击导致的数据泄露。该功能现已面向符合条件的个人用户和自助式 ChatGPT Business 账户开放。 锁定模式直接应对 LLM 系统中的‘致命三要素’漏洞，通过切断数据泄露途径来增强安全性，这是最易限制且不影响核心功能的方案。这显著提升了处理敏感数据用户的安全性，但也暗示默认的 ChatGPT 设置可能无法完全抵御恶意攻击。 锁定模式并不能阻止提示注入出现在处理的内容中，它仅通过确定性机制（而非 AI 评估）阻止可能泄露数据的出站请求。OpenAI 首席信息安全官 Dane Stuckey 表示，锁定模式并非面向所有用户，而是针对风险较高的用户，他们需要在安全性和功能性之间做出权衡。

rss · Simon Willison · Jun 5, 23:56

**背景**: 提示注入是一种攻击方式，恶意输入会修改大语言模型（LLM）的行为，使其执行非预期操作，可能导致数据泄露。数据泄露是指未经授权将数据从系统传输到外部目标。锁定模式通过限制 ChatGPT 的出站网络请求，针对此类攻击的最后阶段进行防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_exfiltration">Data exfiltration</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection | OWASP Foundation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Security`, `#ChatGPT`, `#Prompt Injection`, `#OpenAI`

---

<a id="item-9"></a>
## [如何停止发布低质量的强化学习环境](https://www.latent.space/p/bad-envs) ⭐️ 8.4/10

本文提供了一个实用指南，通过具体示例讲解了强化学习环境设计中的常见陷阱及其修复方法。 设计不良的环境会降低模型性能并误导研究；本指南帮助从业者提升环境质量和智能体学习效果。 作者根据多年分析轨迹的经验，识别出反复出现的问题，强调糟糕的'框架'会主动恶化模型表现。

rss · Latent Space · Jun 5, 18:49

**背景**: 强化学习环境定义了智能体学习的规则和动态，是算法与任务之间的接口。实现不佳的环境可能引入错误、不切实际的约束或奖励不匹配，导致训练不稳定或无效。'框架'可能指连接环境与智能体及训练循环的整体系统。

**标签**: `#reinforcement learning`, `#environments`, `#agentic systems`, `#software engineering`, `#AI`

---

<a id="item-10"></a>
## [英伟达为 Windows PC 提议强大 CPU 系统](https://twitter.com/lemire/status/2062880075117113739) ⭐️ 7.9/10

据报道，英伟达为 Windows PC 提出了一种新的 CPU 系统，采用统一内存架构，类似于苹果 M 系列。该系统旨在通过让 CPU 和 GPU 共享单一内存池，提升游戏和本地 AI 工作负载的性能。 如果实现，这可能挑战传统 x86 架构和苹果 M 系列在 PC 市场的主导地位，为 Windows 用户带来统一内存的优势。同时，它将提升本地 AI 推理能力，使强大的 AI 模型在消费级硬件上更易用。 该提案据报道采用类似英伟达 DGX Spark 中 GB10 芯片的片上系统设计，但性能可能受限于共享带宽和热设计功耗（TDP）。批评者指出，苹果的 AMX 和 SME 加速器可能提供与英伟达方法相当或更好的性能。

hackernews · tosh · Jun 6, 12:52 · [社区讨论](https://news.ycombinator.com/item?id=48424605)

**背景**: 统一内存是 CPU 和 GPU 均可访问的单一内存地址空间，无需在独立内存池之间复制数据。该架构是苹果 M 系列芯片的关键特性，能够高效利用内存并提升图形和 AI 任务性能。英伟达的提议将为 Windows PC 带来类似优势，而当前 Windows PC 依赖独立显卡内存和较慢的 PCIe 传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_memory">Unified memory</a></li>
<li><a href="https://developer.nvidia.com/blog/unified-memory-cuda-beginners/">Unified Memory for CUDA Beginners | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应不一。部分用户认为统一内存是系统架构的游戏规则改变者，而另一些用户则持怀疑态度，指出英伟达 DGX Spark 中的 GB10 芯片令人失望。与苹果 M 系列和高通骁龙 X2 Elite Extreme 的对比很常见，有人认为高通的芯片单核性能更强且已具备统一内存。

**标签**: `#nvidia`, `#cpu`, `#unified-memory`, `#local-ai`, `#hardware`

---

<a id="item-11"></a>
## [五个实验室使用小型模型构建多模型金融剧](https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim-v2) ⭐️ 7.8/10

五个 AI 实验室在一个黑客马拉松中合作，使用多个小型语言模型创作了一部金融题材的戏剧，这在 Hugging Face 的一篇博客中有所描述。 该项目展示了小型模型和多模型协作在创意和特定领域应用中的潜力，为单体大型语言模型提供了一种轻量级替代方案。 该项目涉及五个独立的实验室，每个贡献一个小型模型，通过编排生成连贯的金融剧叙述，突出了集成方法和模块化设计。

rss · Hugging Face Blog · Jun 6, 19:02

**背景**: 小型语言模型（SLM）是参数规模从数百万到数十亿不等的人工智能模型，比大型语言模型（LLM）更小，更高效且易于部署。多模型 AI 是指结合多个模型来执行任务，通常利用每个模型的优势。这个黑客马拉松项目探索了小型模型如何通过组合实现复杂叙事，而无需单个巨大模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Small_language_model">Small language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/small-language-models">What are Small Language Models (SLM)? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#small models`, `#multi-model`, `#hackathon`, `#finance`

---

<a id="item-12"></a>
## [标普 500 拒绝 SpaceX、OpenAI 和 Anthropic 加入](https://arstechnica.com/tech-policy/2026/06/sp-500-blocks-fast-spacex-entry-wont-waive-rule-for-unprofitable-ai-firms/) ⭐️ 7.5/10

标普全球拒绝了为 SpaceX、OpenAI 和 Anthropic 豁免盈利规则的请求，这意味着这些公司在达到标准的 GAAP 盈利标准之前，不会被纳入标普 500 指数。 这一决定维护了标普 500 指数的完整性，确保只纳入盈利公司，保护被动投资者并防止市场扭曲。它还开创了一个先例，即即使是高知名度、高市值公司也不能绕过既定规则。 根据标普 500 规则，公司必须在最近一个季度以及最近四个季度的总和上按照 GAAP 实现盈利。SpaceX、OpenAI 和 Anthropic 目前不符合这些条件，尽管它们市值很大。

hackernews · maltalex · Jun 6, 04:38 · [社区讨论](https://news.ycombinator.com/item?id=48421442)

**背景**: 标普 500 是追踪 500 家美国大公司表现的股票市场指数。要纳入其中，公司必须满足多项标准，包括最低市值和盈利能力。指数委员会有权豁免规则，但在此次选择不这样做。这些公司是私营公司或尚未实现持续盈利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/">SpaceX blocked from early US benchmark index entry as S&P reaffirms existing rules | Reuters</a></li>
<li><a href="https://www.cnbc.com/2026/06/05/spacex-blocked-from-early-us-benchmark-index-entry-as-sp-reaffirms-existing-rules.html">SpaceX blocked from early U.S. benchmark index entry as S&P reaffirms existing rules</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者普遍支持这一决定，许多人表示松了一口气，因为指数维持了其被动策略而不破例。一些人指出，流程应该自然进行，公司若愿意可以创建自己的指数。普遍观点是这一决定维护了对指数的信任。

**标签**: `#S&P 500`, `#SpaceX`, `#OpenAI`, `#Anthropic`, `#investing`

---

<a id="item-13"></a>
## [心理学家警告：AI 聊天机器人可能削弱我们的认知控制](https://www.technologyreview.com/2026/06/05/1138427/are-ai-chatbots-making-us-lose-control-of-our-brains/) ⭐️ 7.2/10

《麻省理工科技评论》报道，研究数字干扰 30 年的心理学家 Gloria Mark 在伦敦 SXSW 大会上提出担忧：AI 聊天机器人可能削弱人类的认知控制，降低我们管理注意力和做出审慎决策的能力。 如果 AI 聊天机器人削弱认知控制，可能加剧注意力缺陷，降低人们的目标导向行为能力，进而影响整个社会的生产力、学习和心理健康。 Gloria Mark 是加州大学欧文分校的名誉教授，数十年来研究数字技术如何影响注意力持续时间。文章指出，将决策外包给 AI 可能会削弱抑制控制、认知灵活性等执行功能。

rss · MIT Tech Review · Jun 5, 09:00

**背景**: 认知控制（也称执行功能）是指调节思想和行动以实现目标的心理过程，包括注意力控制、抑制和工作记忆。它对于抵抗干扰和做出审慎选择至关重要。心理学家 Gloria Mark 广泛研究了社交媒体等数字工具如何碎片化注意力；她现在警告，AI 聊天机器人可能通过让人们更容易避免费力思考而进一步削弱这些能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_control">Cognitive control</a></li>
<li><a href="https://gloriamark.substack.com/p/navigating-digital-distractions">Navigating digital distractions - by Gloria Mark</a></li>

</ul>
</details>

**标签**: `#AI`, `#chatbots`, `#psychology`, `#cognitive impact`, `#human-computer interaction`

---