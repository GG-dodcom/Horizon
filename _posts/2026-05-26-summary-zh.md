---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 69 items, 13 important content pieces were selected

---

1. [英伟达改变报告方式，区分超大规模客户销售](#item-1) ⭐️ 9.2/10
2. [DynIP：现代动态 DNS 服务，支持 RFC 2136、IPv6 和 DNSSEC](#item-2) ⭐️ 9.1/10
3. [Hugging Face 明确 AI Agent 术语：Harness 与 Scaffold 的区别](#item-3) ⭐️ 8.8/10
4. [微软 Copilot Cowork 漏洞导致数据泄露](#item-4) ⭐️ 8.5/10
5. [AI 对入门级职业路径的无声侵蚀](#item-5) ⭐️ 8.5/10
6. [MIT 现实检查：AI 取代工作恐慌过度](#item-6) ⭐️ 8.0/10
7. [Stack Overflow 论坛衰落，公司依然存活](#item-7) ⭐️ 7.8/10
8. [Dropbox CEO Drew Houston 辞职](#item-8) ⭐️ 7.6/10
9. [外包加本地 AI 将比前沿实验室更经济](#item-9) ⭐️ 7.6/10
10. [别随意订阅：订阅的心理学陷阱](#item-10) ⭐️ 7.6/10
11. [荷兰阻止美资收购数字身份系统供应商 Solvinity](#item-11) ⭐️ 7.5/10
12. [年轻人结直肠癌发病率上升](#item-12) ⭐️ 7.5/10
13. [Rust 性能分析幻灯片](#item-13) ⭐️ 7.4/10

---

<a id="item-1"></a>
## [英伟达改变报告方式，区分超大规模客户销售](https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/) ⭐️ 9.2/10

英伟达宣布更改财务报告方式，将向超大规模云服务商（hyperscaler）的销售与其他客户的销售分开披露，凸显其在超大规模市场的抗商品化策略，同时在其他市场保持全栈主导地位。 这一报告变化罕见地揭示了英伟达如何应对超大规模云商自研 AI 芯片带来的商品化威胁，同时也显示出其专有 CUDA 生态和集成堆栈对非超大规模客户的重要战略意义。这可能影响投资者看法和 AI 硬件市场的竞争格局。 这种划分将显示：尽管亚马逊、谷歌、微软等超大规模客户占据英伟达 GPU 销售的很大一部分，但也是最可能开发内部替代方案的群体，从而给利润率带来下行压力；然而，对于企业和其他客户，英伟达的完整软硬件堆栈形成了锁定效应并带来更高利润率。

rss · Stratechery · May 26, 10:00

**背景**: 超大规模云服务商是指像 Amazon Web Services、Microsoft Azure 和 Google Cloud 这样运营大型数据中心的大型云提供商。它们越来越多地开发自己的定制 AI 加速器（如 AWS Trainium、Google TPU）以减少对英伟达的依赖，威胁到英伟达历史上的主导地位。与此同时，对于其他客户，英伟达不仅销售芯片，还提供包括 CUDA 软件、网络和系统集成的完整堆栈，使得切换难度更大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>
<li><a href="https://www.techpolicy.press/taking-ai-commoditization-seriously/">Taking AI Commoditization Seriously | TechPolicy.Press</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI stack`, `#hyperscalers`, `#commoditization`, `#earnings`

---

<a id="item-2"></a>
## [DynIP：现代动态 DNS 服务，支持 RFC 2136、IPv6 和 DNSSEC](https://dynip.dev/) ⭐️ 9.1/10

DynIP 是一款新推出的动态 DNS（DDNS）服务，由一名网络工程师构建，原生支持 RFC 2136 更新、端到端 IPv6、DNSSEC 以及自带域名（BYOD）。它提供 RFC 2136/TSIG 更新路径和 HTTP API，可直接与 FortiGate、MikroTik 和 Kubernetes external-dns 配合使用。 现有大部分 DDNS 服务依赖专有的 HTTP 更新协议，缺乏完善的 IPv6 支持且忽略 DNSSEC，已无法满足现代网络需求。DynIP 填补了这些空白，为路由器、容器和自托管服务提供安全、符合标准的动态更新，并增强了与企业及云原生工具的互操作性。 该服务支持使用 TSIG（事务签名）进行安全更新，并与实现 RFC 2136 的设备（如 FortiGate 通用 DDNS 和 MikroTik 的 /tool dns-update）兼容。同时提供 HTTP API 供无法使用 DNS UPDATE 的客户端使用。DynIP 提供权威 DNS 服务器并处理 DNSSEC 签名，确保数据完整性。

hackernews · dynip · May 26, 07:35 · [社区讨论](https://news.ycombinator.com/item?id=48276363)

**背景**: 动态 DNS（DDNS）允许拥有动态 IP 地址的设备保持固定主机名。RFC 2136（DNS UPDATE）是程序化更新 DNS 记录的标准，但由于历史上支持不足，许多 DDNS 提供商使用专有协议。DNSSEC 为 DNS 响应添加加密认证，防止欺骗；而随着网络从 IPv4 过渡，IPv6 日益重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_DNS">Dynamic DNS - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2136">RFC 2136 - Dynamic Updates in the Domain Name System (DNS UPDATE)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反响积极，许多人称赞 RFC 2136 支持使得与 Kubernetes external-dns 以及 FortiGate、MikroTik 等路由器的原生集成成为可能。部分用户指出着陆页设计过于模板化，建议增加个性化元素。还有用户讨论了使用 BIND9 自托管的替代方案，以及对 Let's Encrypt 兼容性的期望。

**标签**: `#DNS`, `#DDNS`, `#networking`, `#self-hosting`, `#RFC2136`

---

<a id="item-3"></a>
## [Hugging Face 明确 AI Agent 术语：Harness 与 Scaffold 的区别](https://huggingface.co/blog/agent-glossary) ⭐️ 8.8/10

Hugging Face 发布了一篇博客文章，明确区分了关键 AI agent 术语，特别是 'harness' 和 'scaffold' 的定义与区别。 随着 AI agent 开发的加速，统一的术语有助于开发者、研究者和组织更有效地沟通，减少混淆并促进协作。 该文章解释说，'harness' 指的是围绕 LLM 的完整架构系统，管理上下文的生命周期；而 'scaffold' 是使 agent 能够自主链式执行任务并与环境交互的框架或工具。

rss · Hugging Face Blog · May 25, 00:00

**背景**: 在 AI agent 系统中，大型语言模型（LLM）本身不足以自主执行任务，需要额外的软件层。'Harness' 管理 agent 的上下文、安全和反馈循环，而 'scaffold' 提供多步推理和工具使用的结构模式。这些术语经常被混用，导致混淆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#terminology`, `#LLM`, `#scaffold`, `#harness`

---

<a id="item-4"></a>
## [微软 Copilot Cowork 漏洞导致数据泄露](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.5/10

微软 Copilot Cowork（集成在 Microsoft 365 中的 AI 代理）被发现存在漏洞，允许通过代理发送的包含外部图片的邮件触发网络请求，从而实现数据泄露。攻击者可通过提示注入让代理发送带有一键认证 OneDrive 下载链接的邮件，用户打开邮件时文件即被泄露。 该漏洞凸显了在自主 AI 系统中防止数据泄露的持续挑战，尤其是在企业采用此类工具提高生产力之际。它表明，即使仅允许内部邮件发送，外部图片渲染等细微机制也可能被利用来泄露敏感数据。 该攻击利用了 Copilot Cowork 可以在无需审批的情况下向用户自己的收件箱发送邮件，且这些邮件的显示方式会渲染外部图片。由于 OneDrive 会生成预先认证的下载链接，成功的提示注入可使这些链接嵌入外部图片中，从而允许攻击者下载文件。

rss · Simon Willison · May 26, 15:36

**背景**: 微软 Copilot Cowork 是集成在 Microsoft 365 中的 AI 代理，由 Anthropic 的 Claude 驱动，旨在自动化跨 Outlook 和 Teams 等应用的多步骤任务。提示注入是一种安全漏洞，恶意输入可覆盖 AI 模型的指令，导致非预期行为。在此案例中，攻击者可构造提示，诱使代理发送包含编码敏感数据的外部图片 URL 的邮件。用户打开邮件时，图片请求发出，数据被泄露到攻击者的服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection | OWASP Foundation</a></li>
<li><a href="https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork-frontier">Get started with Cowork (Frontier) | Microsoft Support</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#Microsoft Copilot`, `#prompt injection`, `#data exfiltration`

---

<a id="item-5"></a>
## [AI 对入门级职业路径的无声侵蚀](https://www.technologyreview.com/2026/05/26/1137865/its-time-to-address-the-looming-crisis-in-entry-level-work/) ⭐️ 8.5/10

《麻省理工科技评论》的一项新分析指出，尽管 AI 尚未导致大规模失业，但它正在悄悄削弱入门级工作岗位，使早期职业工作者更难获得必要经验并向上发展。 这之所以重要，是因为入门级岗位对技能发展和职业晋升至关重要；如果 AI 在未引起明显失业的情况下侵蚀这些职位，就可能引发流动性停滞和劳动力市场不平等加剧的隐性危机。 文章指出，总体就业保持稳定，但表面之下，职业阶梯的第一级因 AI 自动化而弱化，可能将新进入者困在低技能或不稳定的工作中。

rss · MIT Tech Review · May 26, 09:00

**背景**: AI 和自动化长期以来被担心会导致失业，但到目前为止，发达经济体的整体就业数据依然坚挺，这让一些人淡化了威胁。然而，研究人员越来越关注更细微的影响，例如工作质量、技能要求以及职业阶梯结构的变化，特别是对进入劳动力市场的年轻工作者。

**标签**: `#AI`, `#labor market`, `#entry-level work`, `#technology impact`, `#career`

---

<a id="item-6"></a>
## [MIT 现实检查：AI 取代工作恐慌过度](https://www.technologyreview.com/2026/05/26/1137855/a-reality-check-on-the-ai-jobs-hysteria/) ⭐️ 8.0/10

一篇新的《麻省理工科技评论》文章批判性地审视并反驳了当前关于 AI 将摧毁白领工作的恐慌，认为这种恐慌被夸大了。 这一分析为广泛存在的 AI 导致失业的恐惧提供了及时的反叙事，可能重塑公众和政策关于 AI 经济影响的讨论。 文章引用了 Coinbase、Meta 和 Cisco 最近的裁员作为加剧恐慌的例子，但认为这些并不代表知识工作者的广泛趋势。

rss · MIT Tech Review · May 26, 09:00

**背景**: 随着 ChatGPT 和 DALL-E 等生成式 AI 工具的兴起，对 AI 将取代白领工作的担忧加剧。许多新闻报道和评论文章警告大规模失业，特别是在科技和创意领域。这篇来自《麻省理工科技评论》的文章基于分析而非炒作，提供了现实检查。

**标签**: `#AI`, `#jobs`, `#economic impact`, `#reality check`, `#technology`

---

<a id="item-7"></a>
## [Stack Overflow 论坛衰落，公司依然存活](https://sherwood.news/tech/stack-overflow-forum-dead-thanks-ai-but-companys-still-kicking-ai/) ⭐️ 7.8/10

一篇文章分析了 Stack Overflow 的问答论坛如何因 AI 工具（如 ChatGPT）和长期存在的有毒文化而衰落，但公司通过数据许可和招聘板服务依然保持盈利。 这突显了生成式 AI 对传统知识共享平台的影响，并引发关于社区可持续性的问题，同时也表明即使核心社区萎缩，公司也能转向新的收入来源。 文章指出论坛的衰落始于 ChatGPT 之前，COVID 和 2021 年被 Prosus 收购被提及为潜在因素，但 ChatGPT 的推出加速了流量下降。

hackernews · geerlingguy · May 26, 17:17 · [社区讨论](https://news.ycombinator.com/item?id=48282709)

**背景**: Stack Overflow 是程序员的问答平台，用户通过游戏化机制获得声望点。它成为了重要资源，但因其严格的审核和对新人不友好的环境而受到批评。公司后来通过向 AI 公司许可数据和运营招聘板实现盈利。

**社区讨论**: 评论者普遍同意论坛文化有毒，有人称之为“早点消失好”，另有评论指出它只作为知识库有用，而不是社区。一些人指出 2021 年的收购是关键转折点，而另一些人则怀念它过去的实用性，尽管有缺陷。

**标签**: `#Stack Overflow`, `#AI`, `#community`, `#programming`, `#Q&A`

---

<a id="item-8"></a>
## [Dropbox CEO Drew Houston 辞职](https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html) ⭐️ 7.6/10

Dropbox 联合创始人兼 CEO Drew Houston 宣布辞职，该消息于 2026 年 5 月 26 日在公司博客中公布。 此次领导层变动正值 Dropbox 市场估值停滞不前，且面临苹果、谷歌和微软等集成云服务的激烈竞争之际。 Drew Houston 将继续留在董事会并协助交接，但继任者尚未公布。公司估值长期徘徊在 60 亿美元左右，增长停滞。

hackernews · aghuang · May 26, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48279453)

**背景**: Dropbox 是一家云存储和文件同步公司，于 2018 年上市。尽管早期增长强劲，但近年来面临大型科技公司提供集成云存储解决方案的激烈竞争，导致股价和估值停滞不前。

**社区讨论**: 社区成员指出 Dropbox 估值停滞及市场环境艰难，用户 bhouston 分析认为核心问题是市场而非领导层。其他人则称赞 Houston 的领导力和工程文化，还有一位用户对账户删除影响重要数据表示不满。

**标签**: `#Dropbox`, `#CEO transition`, `#tech leadership`, `#cloud storage`, `#Hacker News`

---

<a id="item-9"></a>
## [外包加本地 AI 将比前沿实验室更经济](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) ⭐️ 7.6/10

一项新分析认为，将外包开发与本地运行的 AI 模型相结合，将很快比依赖 OpenAI 和 Anthropic 等前沿 AI 实验室处理所有 AI 任务更具成本效益。 这一趋势可能重塑 AI 行业，使小型公司无需支付高昂的 API 费用即可获得先进的 AI 能力，从而可能减少对大型实验室的依赖。 文章指出，像 Claude 这样的模型订阅定价每 token 比 API 定价便宜 10 到 40 倍，而本地开源模型可进一步降低常规任务的成本。

hackernews · GodelNumbering · May 26, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48278610)

**背景**: OpenAI、Anthropic 和 Google DeepMind 等前沿 AI 实验室开发尖端 AI 模型并通过昂贵的 API 提供。本地 AI 工具如 Ollama 允许在个人硬件上运行开源模型，避免 API 成本。外包涉及雇佣远程开发者，通常费率低于内部员工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://intelligence.org/2025/06/11/so-you-want-to-work-at-a-frontier-ai-lab/">So You Want to Work at a Frontier AI Lab - Machine Intelligence...</a></li>
<li><a href="https://vap1231.medium.com/run-large-language-models-locally-using-ollama-dc33102c6de1">Run Large Language Models Locally using ollama | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出订阅定价远低于 API，且开发者质量至关重要——优秀的开发者配合前沿 AI 能超越任何模型配合弱开发者。一些人认为外包需要极其详细的设计文档，类似于有效提示，这可能会减少对外包和前沿模型的双重需求。

**标签**: `#AI`, `#LLMs`, `#economics`, `#outsourcing`, `#cost-analysis`

---

<a id="item-10"></a>
## [别随意订阅：订阅的心理学陷阱](https://thebestworstcase.substack.com/p/dont-subscribe-so-casually) ⭐️ 7.6/10

一篇 Substack 文章反对随意订阅服务，揭示了自满和禀赋效应等心理陷阱，并建议在订阅后立即主动取消。 这很重要，因为订阅模式日益通过黑暗模式利用用户心理，导致不必要的支出；文章帮助消费者掌控自己的订阅和财务。 文章建议在注册后立即取消订阅，因为付费期间订阅仍然有效，并警告那些使取消变得困难的黑暗模式。

hackernews · shmublu · May 26, 14:50 · [社区讨论](https://news.ycombinator.com/item?id=48280636)

**背景**: 黑暗模式是一种欺骗性用户界面设计，诱使用户执行他们本不打算的操作，例如注册重复付款。该术语由 Harry Brignull 于 2010 年提出。本文利用这类设计心理学来解释人们为何保留不想要的订阅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_pattern">Dark pattern</a></li>
<li><a href="https://www.deceptive.design/">Deceptive Patterns (aka Dark Patterns ) - spreading awareness since...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实用技巧：使用 kill-the-newsletter.com 等服务管理邮件订阅，并在订阅后立即取消以保留访问权而不承担风险。一位评论者指出，易于取消的政策实际上可以通过减少焦虑来增加随意注册。

**标签**: `#subscriptions`, `#user behavior`, `#dark patterns`, `#personal finance`, `#technology`

---

<a id="item-11"></a>
## [荷兰阻止美资收购数字身份系统供应商 Solvinity](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 7.5/10

荷兰政府以国家安全为由，阻止美国公司 Kyndryl 收购 Solvinity，该公司负责托管荷兰的 DigiD 数字身份系统。 这一决定凸显了围绕数字主权的紧张局势，以及控制关键国家基础设施（尤其是身份系统）免受外资所有的战略重要性。 Solvinity 提供安全托管云服务，并托管荷兰公民用于访问政府服务的电子身份系统 DigiD。Kyndryl 是从 IBM 分拆出来的 IT 基础设施服务提供商。

hackernews · vrganj · May 26, 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48278406)

**背景**: DigiD（数字身份）是荷兰的电子身份识别系统，允许公民在线访问各种政府服务，每天处理数百万次登录。Solvinity 是一家荷兰 IT 公司，为政府管理关键数字基础设施。人们担心美国所有者可能会被美国法律强制要求交出数据，从而危及隐私和国家安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.solvinity.com/">Secure Managed Cloud | Solvinity</a></li>
<li><a href="https://www.xpat.nl/expat-netherlands/first-steps/digid/">Dutch digital identity : DigiD - XPAT.NL</a></li>

</ul>
</details>

**社区讨论**: 社区成员对政府采取行动表示欣慰，但对最初保密和合同延期感到失望。有人认为此事凸显了加密主权的必要性，即即使供应商也无法访问用户数据。还有人质疑为什么不使用开源自托管解决方案。

**标签**: `#digital sovereignty`, `#national security`, `#identity management`, `#geopolitics`, `#acquisition`

---

<a id="item-12"></a>
## [年轻人结直肠癌发病率上升](https://dynomight.net/crc-rates/) ⭐️ 7.5/10

一项详细分析证实，与上几代人相比，年轻人的结直肠癌发病率正在上升，这挑战了其作为一种老年疾病的传统观念。 这一趋势具有重大的公共卫生影响，因为早发性结直肠癌常在晚期才被诊断，需要调整筛查指南和生活方式建议。 该分析利用数据表明，今天的年轻人比同年龄的上一代人面临更高的风险，而且这种增加并不仅仅是由于检测手段的改进。

hackernews · surprisetalk · May 26, 16:00 · [社区讨论](https://news.ycombinator.com/item?id=48281539)

**背景**: 结直肠癌是全球最常见的癌症之一。传统上，它在 50 岁以上的人群中被诊断，但近年来的研究显示，50 岁以下人群的病例有所增加，促使人们研究潜在的病因，如饮食、生活方式和环境因素。

**社区讨论**: 社区评论突出了个人经历，一些用户报告在结肠镜检查后确诊癌症，强调了筛查的重要性。其他人讨论通过改变饮食来降低风险，普遍认为结肠镜检查兼具预防和诊断作用，早期发现可以挽救生命。

**标签**: `#colorectal cancer`, `#public health`, `#medical research`, `#preventive health`

---

<a id="item-13"></a>
## [Rust 性能分析幻灯片](https://github.com/yugr/rust-slides/) ⭐️ 7.4/10

一份名为《Rust 语言性能》的技术幻灯片已在 GitHub 上发布，分析了 Rust 相对于 C 和 C++的性能特征，包括优化权衡。 此项分析对考虑使用 Rust 替代 C 和 C++的系统程序员具有重要意义，因为它提供了基于数据的性能权衡比较，并讨论了 Rust 的优势与不足。 幻灯片涵盖了边界检查开销、边界检查提前执行以及编译时表达能力等主题，并指出 Rust 平均性能损失约为 3%，最坏情况路径相比 C++可达 15%。

hackernews · tanelpoder · May 25, 23:37 · [社区讨论](https://news.ycombinator.com/item?id=48273147)

**背景**: Rust 是一种注重内存安全的系统编程语言，无需垃圾回收，使用借用检查器和所有权模型。C 和 C++是较老的系统语言，允许手动内存管理，通常性能更好但存在安全风险。该幻灯片探讨了 Rust 安全保证带来的性能代价。

**社区讨论**: 社区评论讨论到现代 C++由于编译时表达能力而比 C 和 Rust 性能更优，以及 Rust 的边界检查开销和缺乏稳定的高级语义阻碍了优化。还有对 Rust 编译时间的担忧。

**标签**: `#Rust`, `#performance`, `#compiler optimization`, `#C++`, `#systems programming`

---