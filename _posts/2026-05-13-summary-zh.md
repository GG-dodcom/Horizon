---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 112 items, 30 important content pieces were selected

---

1. [CERT 发布六个关于 dnsmasq 关键漏洞的 CVE](#item-1) ⭐️ 9.0/10
2. [OrcaSlicer 分支恢复 BambuNetwork 支持](#item-2) ⭐️ 8.0/10
3. [Elevator：无启发式的确定性二进制翻译](#item-3) ⭐️ 8.0/10
4. [Googlebook：搭载 Gemini AI 的安卓笔记本电脑引发热议](#item-4) ⭐️ 8.0/10
5. [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](#item-5) ⭐️ 8.0/10
6. [复制 Linux 内核优化导致 QUIC 性能漏洞](#item-6) ⭐️ 8.0/10
7. [用光线步进渲染逼真的天空](#item-7) ⭐️ 8.0/10
8. [Quack：DuckDB 的新客户端-服务器协议](#item-8) ⭐️ 8.0/10
9. [欧洲政府域名大规模安全审计](#item-9) ⭐️ 8.0/10
10. [Obsidian 推出自动化插件审查系统](#item-10) ⭐️ 8.0/10
11. [科布勒提出“僵尸互联网”概念](#item-11) ⭐️ 8.0/10
12. [Shopify 的 River 代理通过公开透明进行教学](#item-12) ⭐️ 8.0/10
13. [世界模型位列 MIT 十大 AI 关注话题](#item-13) ⭐️ 8.0/10
14. [诺奖经济学家指出需关注的三大 AI 趋势](#item-14) ⭐️ 8.0/10
15. [OpenAI 部署公司与苹果英特尔策略分析](#item-15) ⭐️ 8.0/10
16. [Claude Code v2.1.139 新增代理视图和 /goal 命令](#item-16) ⭐️ 7.0/10
17. [开发者将基础设施迁移至欧洲云服务商](#item-17) ⭐️ 7.0/10
18. [Scrcpy v4.0 新增灵活虚拟显示屏](#item-18) ⭐️ 7.0/10
19. [AI 鼠标指针：DeepMind 的语音驱动重新设计](#item-19) ⭐️ 7.0/10
20. [通过沙箱 iframe 实现用户控制的 CSP 白名单](#item-20) ⭐️ 7.0/10
21. [Mitchell Hashimoto 谈技术决策者的风险规避](#item-21) ⭐️ 7.0/10
22. [LLM 0.32a2 增加对 OpenAI /v1/responses 端点的支持](#item-22) ⭐️ 7.0/10
23. [GitLab 裁员与战略转型](#item-23) ⭐️ 7.0/10
24. [James Shore 警告：AI 编程工具必须降低维护成本](#item-24) ⭐️ 7.0/10
25. [参数高尔夫：AI 辅助模型设计的启示](#item-25) ⭐️ 7.0/10
26. [AWS 上基础模型训练和推理的构建块](#item-26) ⭐️ 7.0/10
27. [Varda 与 United Therapeutics 合作，将在轨道上商业生产药物](#item-27) ⭐️ 7.0/10
28. [TechPays 被 Levels.fyi 收购以提升欧洲薪酬透明度](#item-28) ⭐️ 7.0/10
29. [Thinking Machines 发布 TML-Interaction-Small，新一代实时语音 AI](#item-29) ⭐️ 7.0/10
30. [AI 智能体方法 DRIL 自动化构建经济数据集](#item-30) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CERT 发布六个关于 dnsmasq 关键漏洞的 CVE](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT 公开了六个影响 dnsmasq 的新 CVE，dnsmasq 是一款广泛使用的 DNS/DHCP 服务器，这些漏洞包括通过畸形 DNS 查询或 DHCP 请求实现远程代码执行和拒绝服务。 这些漏洞至关重要，因为 dnsmasq 嵌入在数百万设备中——路由器、物联网设备和 Android——其中许多设备很少收到安全更新，暴露了巨大的攻击面。 这些漏洞包括远程攻击者导致的堆越界写入、导致拒绝服务的无限循环，以及恶意 DHCP 请求引起的缓冲区溢出。

hackernews · chizhik-pyzhik · May 12, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48112042)

**背景**: Dnsmasq 是一款轻量级网络服务程序，为小型网络提供 DNS 缓存、DHCP 和路由器广播功能。它被包含在许多 Linux 发行版、家用路由器和 Android 中。这些宣布的内存安全漏洞源于 C 等缺乏自动内存保护的语言，采用 Rust 等内存安全语言越来越被推荐以降低此类风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/06/24/new-guidance-released-reducing-memory-related-vulnerabilities">New Guidance Released for Reducing Memory-Related Vulnerabilities</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调转向内存安全语言的紧迫性，有用户称这是转折点。其他人讽刺地指出，dnsmasq 用于几乎从不更新的设备，突显了实际影响和修补的困难。

**标签**: `#security`, `#dnsmasq`, `#CVE`, `#memory-safety`, `#vulnerabilities`

---

<a id="item-2"></a>
## [OrcaSlicer 分支恢复 BambuNetwork 支持](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

一个 GitHub 仓库 (FULU-Foundation/OrcaSlicer-bambulab) 被创建，用于恢复 Bambu Lab 打印机的完整 BambuNetwork 支持，从而在争议性的固件更新后实现无限制的云端打印。 这个分支回应了社区对 Bambu Lab 固件更新的强烈不满，该更新通过要求云端认证移除了本地局域网打印功能，维护了 3D 打印社区的用户权利和开源原则。 该分支基于 OrcaSlicer，恢复通过 BambuNetwork 进行互联网打印，绕过了此前锁定第三方切片软件的新云端认证要求。

hackernews · Murfalo · May 12, 21:55 · [社区讨论](https://news.ycombinator.com/item?id=48115127)

**背景**: Bambu Lab 发布了一个固件更新，为本地打印增加了云端认证，实际上迫使用户使用其专有软件。这引发了 3D 打印社区的强烈反对，并催生了逆向工程工作。OrcaSlicer 是一种常用作 Bambu 打印机的开源切片软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/dafik/OrcaSlicer-bambulab">GitHub - dafik/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>
<li><a href="https://github.com/unS0uL/OrcaSlicer-bambulab">GitHub - unS0uL/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论对固件更改表示愤怒，有些人指责 Bambu 通过移除功能进行盗窃。其他人则提供了新系统如何运作的技术分析，一些评论指出 Bambu 最初要求局域网模式也需云端认证，在遭到反对后才撤回。

**标签**: `#3D-printing`, `#open-source`, `#firmware`, `#controversy`, `#reverse-engineering`

---

<a id="item-3"></a>
## [Elevator：无启发式的确定性二进制翻译](https://arxiv.org/abs/2605.08419) ⭐️ 8.0/10

研究人员推出了 Elevator，这是首个完全静态、确定性的二进制翻译器，无需启发式或运行时回退，即可将整个 x86-64 可执行文件转换为 AArch64。 这种确定性方法消除了基于启发式的翻译中的非确定性和安全风险，使其适用于航空、医疗设备等受监管行业的认证。然而，二进制大小和功能支持（仅单线程、无异常处理）的权衡限制了其直接的实际影响。 Elevator 相比 QEMU 用户模式 JIT 实现了约 4.75 倍的运行时加速，但导致二进制大小增加 50 倍，执行指令数增加 7 倍。它仅支持单线程二进制文件，缺乏异常处理和栈展开。

hackernews · matt_d · May 13, 04:25 · [社区讨论](https://news.ycombinator.com/item?id=48117810)

**背景**: 二进制翻译将可执行代码从一种指令集架构（ISA）转换为另一种。完全静态翻译提前处理整个二进制而不执行，但必须启发式地决定哪些字节是代码还是数据，这可能引入错误。Elevator 通过考虑每个字节的所有可能解释，为每个可行的解释生成单独的翻译，然后组合成确定性输出来避免启发式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">Deterministic Fully-Static Whole-Binary Translation without ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_translation">Binary translation - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48117810">Deterministic Fully-Static Whole-Binary Translation Without ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，50 倍的大小增加是确定性下合理的权衡，特别是对于认证用例。一些人讨论了性能比较，有评论者分享了以往定制 JIT 引擎的经验。还有猜测未来可能会使用启发式来减小大小，但牺牲保证，同时讨论了剩余挑战，如相对偏移。

**标签**: `#binary translation`, `#deterministic`, `#static analysis`, `#systems`, `#emulation`

---

<a id="item-4"></a>
## [Googlebook：搭载 Gemini AI 的安卓笔记本电脑引发热议](https://googlebook.google/) ⭐️ 8.0/10

谷歌发布了 Googlebook，这是一款运行安卓系统并与 Gemini AI 深度集成的全新笔记本电脑品类，旨在以 AI 驱动的交互方式重新定义基于应用的计算机使用体验。 此次发布代表了谷歌通过 AI 融合移动与桌面计算的最新尝试，可能挑战传统笔记本电脑范式，并扩展 AI 助手在日常生产力中的角色。 Googlebook 基于 Android 17 桌面模式并集成 Gemini，用户可通过自然语言与数据交互，而非传统应用。但它仍保留基于应用的生态系统，这引发了对其目标受众和用户体验一致性的批评。

hackernews · tambourine_man · May 12, 17:37 · [社区讨论](https://news.ycombinator.com/item?id=48111545)

**背景**: Chromebook 长期以来提供基于 Chrome OS 的笔记本电脑体验，而安卓主要作为移动操作系统。Googlebook 试图通过将安卓带入笔记本电脑形态，并配以桌面界面和 AI 功能来融合两者。Gemini 是谷歌的生成式 AI 助手，能够处理文本、图像、音频和视频，并已集成到谷歌各项服务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini.google">Gemini.google</a></li>
<li><a href="https://gemini.google/about/">Learn about Gemini, the everyday AI assistant from Google</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些人认为 Googlebook 是迈向 AI 优先、无应用未来的远见之举，称赞 Gemini 集成的潜力。另一些人则批评其用户体验，尤其是顶部面板设计，并质疑目标受众，认为安卓以应用为中心的模式限制了笔记本电脑在传统计算任务中的实用性。

**标签**: `#Googlebook`, `#Android`, `#AI`, `#laptops`, `#UX`

---

<a id="item-5"></a>
## [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus 开源了 Needle，一个 2600 万参数的单一工具调用模型，通过仅注意力机制架构（无 MLP）从 Gemini 蒸馏而来。在消费级设备上实现 6000 tok/s 预填充和 1200 tok/s 解码。 这表明小型专用模型在工具调用上可媲美大型模型，从而在手机、手表等边缘设备上实现端侧智能体 AI。同时挑战了 transformer 架构中 MLP 在检索与组装任务中的必要性。 该模型在 16 个 TPU v6e 上预训练 200B token（27 小时），然后通过 Gemini 合成 2B token 的函数调用数据进行后训练（45 分钟）。在单一函数调用任务上优于 FunctionGemma-270M 和 Qwen-0.6B 等更大模型，但缺乏对话广度。

hackernews · HenryNdubuaku · May 12, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=48111896)

**背景**: 传统 transformer 模型结合注意力层和前馈网络（MLP）来学习和存储知识。Needle 完全移除了 MLP，其依据是工具调用是一种检索与组装任务，输入已包含所有必要信息，因此仅需注意力机制。TPU v6e（又称 Trillium）是谷歌最新一代 AI 加速器，针对训练和推理进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://docs.cloud.google.com/tpu/docs/v6e">TPU v6e | Google Cloud Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该模型在复杂工具用例中的区分能力提出质疑，部分人指出其可用于 CLI 自然语言解析。还有人担心谷歌的反蒸馏防御可能削弱学生模型性能。一名用户建议提供在线演示，另一名用户报告独立验证了移除 MLP 的有效性。

**标签**: `#tool calling`, `#model distillation`, `#small language models`, `#on-device AI`, `#function calling`

---

<a id="item-6"></a>
## [复制 Linux 内核优化导致 QUIC 性能漏洞](https://blog.cloudflare.com/quic-death-spiral-fix/) ⭐️ 8.0/10

Cloudflare 工程师发现，一个 QUIC 性能漏洞源于他们将 Linux 内核的 TCP 优化（TCP Small Queues）复制到自己的 QUIC 实现中，却未纳入后续放宽限制的内核修复。 此事件凸显了将内核代码移植到用户空间网络堆栈的风险，尤其是对于依赖精确 pacing 和拥塞控制的协议如 QUIC，并强调了在分叉内核代码时需跟踪上游修复。 该漏洞导致 QUIC 连接出现“死亡螺旋”，其中 pacing 回退降低了吞吐量，且问题仅在特定网络条件下出现，如高带宽延迟乘积路径。

hackernews · sbulaev · May 12, 23:46 · [社区讨论](https://news.ycombinator.com/item?id=48116064)

**背景**: TCP Small Queues (TSQ)是 Linux 内核的一种机制，限制每个套接字的排队数据以减少缓冲区膨胀并改善延迟。Cloudflare 的 QUIC 实现复制了最初的 TSQ 算法，但遗漏了后来放宽限制的内核提交（75eefc6）。QUIC pacing 对于像 BBR 这样的拥塞控制算法至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/506237/">tcp: TCP Small Queues - LWN.net</a></li>
<li><a href="https://lwn.net/Articles/469652/">bql: Byte Queue Limits [LWN.net]</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出维护分叉内核代码的自研实现的挑战，一位用户建议更准确的标题是“我们如何从 Linux 内核复制代码却未完全理解并错过了后续修复”。另一位用户质疑在数据中心使用 CUBIC，认为 BBR 可能更合适。

**标签**: `#QUIC`, `#Linux kernel`, `#networking`, `#Cloudflare`, `#bug analysis`

---

<a id="item-7"></a>
## [用光线步进渲染逼真的天空](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

Maxime Heckel 发布了一篇详细的技术博客，解释了如何使用光线步进和大气散射模型，在网页浏览器中渲染逼真的天空、日落和行星。 这项工作展示了网页图形不断增长的能力，实现了以前仅限于原生应用的复杂视觉效果，并激发了实时渲染领域的进一步探索。 博客包含交互式演示，并涵盖了瑞利散射、米氏散射、米氏相位函数以及臭氧吸收等技术，以模拟逼真的天空颜色和黄昏。

hackernews · ibobev · May 12, 13:26 · [社区讨论](https://news.ycombinator.com/item?id=48107997)

**背景**: 光线步进是一种渲染技术，通过沿光线迭代步进穿过场景并在每一步进行采样，常用于体积效果。大气散射是指光被大气中的粒子散射的物理过程，导致蓝天和红色日落等现象。小分子的瑞利散射使天空呈现蓝色，而较大粒子的米氏散射则增加雾霾并影响日落的色调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ray_marching">Ray marching</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atmospheric_scattering">Atmospheric scattering</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了文章的深度和视觉效果（例如 baliex 称其鼓舞人心），而其他人指出了日落模型中的不准确之处（例如 gmiller123456 指出太阳落山后天空不应立即变黑）。评论中还提到了 Sebastian Lague 关于大气层的视频以及 Nishita 等人 1993 年的开创性论文。

**标签**: `#computer graphics`, `#rendering`, `#web development`, `#atmospheric scattering`, `#shaders`

---

<a id="item-8"></a>
## [Quack：DuckDB 的新客户端-服务器协议](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

2026 年 5 月 12 日，DuckDB 宣布了 Quack，这是一个基于 HTTP 的客户端-服务器协议，实现了远程访问和并发写入，标志着 DuckDB 首次正式支持服务器模式。 Quack 解决了 DuckDB 历史上最大的限制——单用户嵌入式使用，通过支持水平扩展和基于网络的查询，为分布式分析和微服务开辟了新的用例。 根据基准测试，Quack 在批量分析方面比 PostgreSQL 快 32 倍，并且支持服务端多个并发写入者，这是 DuckDB 此前不具备的功能。

hackernews · aduffy · May 12, 17:54 · [社区讨论](https://news.ycombinator.com/item?id=48111765)

**背景**: DuckDB 是一个面向分析工作负载的进程内 SQL OLAP 数据库，传统上嵌入在应用程序中，仅限于单用户访问。Quack 通过客户端-服务器协议扩展了 DuckDB，使其能够作为独立服务器运行，通过网络访问，类似于 PostgreSQL 等传统数据库，但针对分析进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/duckdb/duckdb-quack">GitHub - duckdb/duckdb-quack · GitHub</a></li>
<li><a href="https://motherduck.com/blog/first-variant/duckdb-client-server/">If It Quacks Like a Duck: DuckDB Gets a Client-Server Protocol</a></li>
<li><a href="https://byteiota.com/quack-protocol-duckdb-client-server-32x-faster/">Quack Protocol: DuckDB Client-Server 32x Faster | byteiota</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户对解决远程访问和水平扩展问题表示兴奋。一些用户对并发写入者的定义提出了技术问题，而另一些用户则欣赏实际的用例，例如在不中断服务器的情况下查询实时数据。

**标签**: `#duckdb`, `#database`, `#client-server`, `#remote protocol`, `#scalability`

---

<a id="item-9"></a>
## [欧洲政府域名大规模安全审计](https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/) ⭐️ 8.0/10

SecurityBaseline.eu 于 2026 年 5 月 13 日上线，结果显示在 67,000 个欧洲政府域名中，3,000 个站点非法使用追踪 Cookie，超过 1,000 个暴露诸如 phpMyAdmin 的数据库接口，且 99%的电子邮件加密不充分。 此次审计揭示了欧洲政府数字基础设施中严重的网络安全缺陷，危及公民隐私和国家安全。这迫使各国政府加强基准安全措施，并可能推动新法规的出台。 该项目报告详细指出，许多暴露的数据库接口无需认证即可访问，而电子邮件加密不良包括缺少或错误配置 DANE 或 MTA-STS。数据可通过 SecurityBaseline.eu 上的交互式地图获取。

hackernews · aequitas · May 13, 07:11 · [社区讨论](https://news.ycombinator.com/item?id=48118763)

**背景**: SecurityBaseline.eu 是荷兰“Basisbeveiliging”项目的衍生项目，该项目已监测基准安全超过十年。审计检查常见问题，如非法追踪 Cookie（违反电子隐私指令）、可公开访问的数据库管理工具以及电子邮件加密标准（如 DANE 和 MTA-STS）。这些都是许多组织忽视的基本安全卫生措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/">European governments: 3.000 tracking sites, 1.000 phpMyAdmins, and 99% poorly encrypted email. Introducing SecurityBaseline.eu - Internet Cleanup Foundation</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对此前德国渗透测试法律障碍的担忧，有人指出这类扫描可能被视为违反黑客法律。其他人质疑数据准确性，指出一些被标记的站点是非政府或已废弃的，并争论 DNSSEC 着色是否过度。一条正面评论指出电子政务成熟度与安全事件之间的相关性。

**标签**: `#security`, `#privacy`, `#government`, `#europe`, `#cybersecurity`

---

<a id="item-10"></a>
## [Obsidian 推出自动化插件审查系统](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian 宣布推出新的自动化插件审查系统，取代手动审查，旨在加快提交速度并减少开发者的挫折感。 这解决了 Obsidian 插件生态中的一个主要扩展瓶颈，之前手动提交新插件几乎不可能。这表明公司致力于在平台成长过程中支持其开发者社区。 该系统依赖自动化检查，但一些评论者担心安全问题，因为插件仍然拥有完全的磁盘和网络访问权限。CEO 提到团队已为此工作近一年，并且只有七个人。

hackernews · xz18r · May 12, 15:45 · [社区讨论](https://news.ycombinator.com/item?id=48109970)

**背景**: Obsidian 是一款流行的笔记应用，支持插件以扩展功能。此前，所有插件都经过手动审查，导致等待时间长和开发者沮丧，尤其是随着 AI 辅助插件创建增加提交量。

**社区讨论**: 社区反应不一：许多人祝贺团队解决了瓶颈问题，但对自动化安全检查以及缺乏权限系统感到担忧。一些用户担心未来可能出现安全事故。

**标签**: `#Obsidian`, `#plugins`, `#developer tools`, `#community`, `#automation`

---

<a id="item-11"></a>
## [科布勒提出“僵尸互联网”概念](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler 在 404 Media 发表了一篇愤怒的评论文章，提出了“僵尸互联网”（Zombie Internet）一词，描述人工智能生成内容如何淹没网络并让人类读者精疲力竭。 这篇文章指出了网络内容质量日益严重的危机：AI 生成的垃圾内容不仅大量泛滥，还在扭曲人类的写作风格。 Koebler 将僵尸互联网与“死互联网”理论区分开来，强调它涉及人类与机器人的复杂互动，包括人们使用 AI 与他人交流，以及 AI 生成的书籍摘要被当作真书出售等情况。

rss · Simon Willison · May 11, 19:21

**背景**: “死互联网”理论是一种阴谋论，认为自 2016 年左右起，互联网上的大部分内容和互动都是自动化的，由算法和机器人控制。相比之下，“僵尸互联网”描述了一种状态：AI 生成的内容无处不在，但真实的人类活动依然存在，从而形成了一个令人筋疲力尽的混合环境。这个词由 Jason Koebler 在 2025 年 404 Media 的一篇文章中推广。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>
<li><a href="https://www.fastcompany.com/91489308/zombie-internet-devastating-consequences-advertising-social-media-human-web-dead-internet-moltbook-ai-tbpn">The ‘ zombie internet ’ has arrived—and it has... - Fast Company</a></li>

</ul>
</details>

**标签**: `#AI`, `#content quality`, `#internet culture`, `#journalism`

---

<a id="item-12"></a>
## [Shopify 的 River 代理通过公开透明进行教学](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything) ⭐️ 8.0/10

Shopify 的内部 AI 编码代理 River 完全在公开的 Slack 频道中运作，允许任何员工观察并参与互动，营造了一种无需正式课程即可通过渗透学习的环境。 这种透明的方法将 AI 代理的使用转变为协作学习工具，可能影响公司部署 AI 代理的方式，优先考虑知识共享和集体改进。 River 不回复私信；它要求用户创建公开频道。在 CEO Tobias Lütke 自己的频道中，有超过 100 人跟随，添加上下文、进行评审并从互动中学习。

rss · Simon Willison · May 11, 15:46

**背景**: River 是 Shopify 的内部 AI 编码代理，旨在协助开发者进行代码生成和调试等任务。通过将所有互动公开，公司将自身转变为“教学工厂”（Lehrwerkstatt），学习通过观察实际工作自然发生。这与典型的私有 AI 代理互动形成对比，并呼应了 Midjourney 早期公开 Discord 的做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zenml.io/llmops-database/building-a-public-ai-agent-workspace-for-organizational-learning">Shopify: Building a Public AI Agent Workspace for ...</a></li>
<li><a href="https://shopify.dev/docs/apps/build/ai-toolkit">Shopify AI Toolkit</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#software development`, `#internal tools`, `#collaboration`, `#transparency`

---

<a id="item-13"></a>
## [世界模型位列 MIT 十大 AI 关注话题](https://www.technologyreview.com/2026/05/12/1137134/world-models-10-things-that-matter-in-ai-right-now/) ⭐️ 8.0/10

2026 年 5 月 12 日，《麻省理工科技评论》发布了“当下 AI 领域重要的 10 件事”榜单，将世界模型列为关键新兴领域。该杂志还宣布举办仅限订阅者参加的圆桌讨论，主题为“AI 能学会理解世界吗？”，由执行编辑 Niall Firth 主持。 世界模型代表了 AI 向能够模拟和理解物理动态的范式转变，这对机器人技术、自动驾驶和交互式视频生成至关重要。《麻省理工科技评论》的认可表明世界模型正成为 AI 行业的核心焦点，推动投资和研究。 世界模型与大语言模型不同，它通过构建内部表示来预测环境如何随行动变化，模拟物理、物体交互和因果关系。即将举行的圆桌讨论将探讨 AI 如何演进以实现对世界的更深层次理解。

rss · MIT Tech Review · May 12, 16:22

**背景**: AI 中的世界模型是一种神经网络，它学习环境的内部表示并预测其随时间变化的动态。这些系统使智能体无需持续与现实世界交互就能进行规划和推理，其思想可追溯到 20 世纪 90 年代。现代世界模型通过生成合成数据和模拟物理来训练机器人和自动驾驶车辆。它们与专注于分类或生成的传统 AI 模型形成对比，为更扎实和因果性的理解提供了路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://www.forbes.com/sites/nishatalagala/2026/04/19/ai-world-models-what-are-they-and-why-should-you-care/">AI World Models: What Are They And Why Should You Care - Forbes</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Is a World Model? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#AI`, `#world models`, `#MIT Technology Review`, `#emerging technology`

---

<a id="item-14"></a>
## [诺奖经济学家指出需关注的三大 AI 趋势](https://www.technologyreview.com/2026/05/11/1137090/three-things-in-ai-to-watch-according-to-a-nobel-winning-economist/) ⭐️ 8.0/10

2024 年诺贝尔经济学奖得主达龙·阿西莫格鲁发表了一篇论文，批评大型科技公司对 AI 的说法，并提出了他认为值得密切关注的 AI 三个关键领域。 作为诺贝尔奖得主，阿西莫格鲁的观点具有重要分量，为大型科技公司通常乐观的 AI 叙事提供了反观点，他的分析可能影响政策辩论和公众对 AI 经济与社会影响的理解。 这篇来自《麻省理工科技评论》通讯《算法》的文章指出，阿西莫格鲁对大型科技公司说辞的批判性分析使他在硅谷不受欢迎。值得关注的具体三项内容在全文中有详细说明，但总结表明这些内容源于他对 AI 益处可能被高估的研究。

rss · MIT Tech Review · May 11, 17:35

**背景**: 达龙·阿西莫格鲁是一位著名经济学家，因其在制度与经济增长方面的研究而获得 2024 年诺贝尔经济学奖。他近期的研究集中于人工智能的经济影响，经常挑战科技公司和投资者中普遍存在的乐观观点。

**标签**: `#AI`, `#Economics`, `#Nobel laureate`, `#Trends`, `#Policy`

---

<a id="item-15"></a>
## [OpenAI 部署公司与苹果英特尔策略分析](https://stratechery.com/2026/the-deployment-company-back-to-the-70s-apple-and-intel/) ⭐️ 8.0/10

Ben Thompson 的分析重点指出 OpenAI 成立了一家以部署为重心的新公司，以及苹果与英特尔合作的经​​济动机。 这些举措标志着战略转变：AI 部署需要自上而下的企业整合，而苹果的芯片战略可能从独家内部设计转向利用英特尔以获得成本效益。 据报道，OpenAI 的部署公司已获得 TPG、高盛和麦肯锡 40 亿美元的支持。苹果与英特尔合作的理由在分析中没有详细说明，但暗示了经济压力。

rss · Stratechery · May 13, 10:00

**背景**: OpenAI 以开发 GPT-4 等先进 AI 模型而闻名。新的部署公司旨在帮助企业将 AI 集成到关键运营中。苹果历来使用自研芯片（Apple Silicon），最近 Mac 已脱离英特尔处理器；潜在的合作将标志着一项转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-launches-the-deployment-company/">OpenAI launches the OpenAI Deployment Company to help ...</a></li>
<li><a href="https://techjournal.org/openai-launches-4-billion-deployment-company">OpenAI Launches $4B Deployment Company: What It Means for ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#Apple`, `#Intel`, `#strategy`

---

<a id="item-16"></a>
## [Claude Code v2.1.139 新增代理视图和 /goal 命令](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) ⭐️ 7.0/10

Anthropic 发布了 Claude Code v2.1.139，新增了代理视图（agent view）以列出所有会话，以及 /goal 命令，让 Claude 跨轮次工作直到满足条件。 这些功能通过更好的会话管理和自主任务完成，显著提升了开发者的生产力，使 Claude Code 在处理复杂的多步骤编码工作流时更加强大。 代理视图显示正在运行、阻塞和完成的会话；/goal 命令支持交互式、-p 和远程控制模式，并带有实时覆盖面板显示已用时间、轮次和令牌数。

github · ashwin-ant · May 11, 18:43

**背景**: Claude Code 是 Anthropic 基于终端的 AI 编码助手，能够通过自然语言理解代码库、编辑文件和运行命令。代理视图提供了一个集中式仪表板来管理多个会话，而 /goal 命令允许 Claude 自主地朝着定义的目标工作，无需用户持续提示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/releases">Releases · anthropics/ claude - code · GitHub</a></li>
<li><a href="https://gist.github.com/yurukusa/afd1b170cbe76101c15942c7a0471310">Claude Code v2.1.139's / goal command and issue #58373...</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#AI coding assistant`, `#release notes`, `#developer tools`, `#Anthropic`

---

<a id="item-17"></a>
## [开发者将基础设施迁移至欧洲云服务商](https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/) ⭐️ 7.0/10

一位开发者详细描述了其将数字基础设施从美国服务商迁移至欧洲替代方案的经历，理由涉及 GDPR 下的监管和隐私担忧。 此次迁移反映了欧洲数字主权日益增强的趋势，为考虑类似行动以减少对美国云服务依赖的人提供了实际经验。 作者从 Cloudflare 迁移至 Bunny CDN，并构建了一套 Terraform 配置以实现欧洲跨提供商的高可用性。

hackernews · monokai_nl · May 13, 11:42 · [社区讨论](https://news.ycombinator.com/item?id=48120629)

**背景**: 数字主权指国家或个人对其数据和技术基础设施的控制权。在欧洲，这由 GDPR 合规要求和对美国监控法律的担忧推动，促使许多人寻找 Scaleway 或 Hetzner 等欧洲云服务商。

**社区讨论**: 评论者分享了类似经历：有人指出欧盟政府官员越来越频繁地询问欧洲托管方案；另一人成功迁移了产品托管并构建了 Terraform 配置；还有人称 Scaleway 是可靠的提供商。有评论讽刺地指出，尽管迁移到欧洲栈，但网站仍通过 Cloudflare（美国公司）出现速率限制问题。

**标签**: `#cloud`, `#infrastructure`, `#GDPR`, `#Europe`, `#DevOps`

---

<a id="item-18"></a>
## [Scrcpy v4.0 新增灵活虚拟显示屏](https://github.com/Genymobile/scrcpy/releases/tag/v4.0) ⭐️ 7.0/10

Scrcpy v4.0 已发布，引入了灵活虚拟显示屏功能，可通过 --flex-display（或 -x）标志动态调整大小，与客户端窗口同步。 这一增强使 Scrcpy 对于需要将 Android 设备镜像到大屏幕的用户更加灵活，无需牺牲显示质量即可无缝调整大小。它显著改善了开发者、测试人员和任何使用虚拟显示屏提高生产力的用户体验。 灵活显示屏功能通过在启动新虚拟显示屏时传递 -x 或 --flex-display 来激活。此功能与编解码器选择和分辨率限制等其他选项一同工作。

hackernews · xnx · May 12, 20:50 · [社区讨论](https://news.ycombinator.com/item?id=48114356)

**背景**: Scrcpy 是一个免费开源工具，可通过 USB 或无线方式显示和控制 Android 设备，具有高性能和低延迟。3.0 版本引入了虚拟显示屏，允许独立于设备屏幕的显示。4.0 版本在此基础上，使虚拟显示屏尺寸自动适应客户端窗口，提供更集成的体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Genymobile/scrcpy">GitHub - Genymobile/scrcpy: Display and control your Android device · GitHub</a></li>
<li><a href="https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md">scrcpy/doc/virtual_display.md at master · Genymobile/scrcpy</a></li>
<li><a href="https://itsfoss.community/t/scrcpy-3-0-comes-with-virtual-displays/12873">Scrcpy 3.0 comes with virtual displays! - Discussion - It's FOSS Community</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极，用户称赞其无缝易用。但一位三星用户报告了一个手势导航 bug，即使在 v4.0 中也存在，需要重启手机。其他用户分享了创造性用例，例如将手机作为 WiFi 桥接器。

**标签**: `#android`, `#screen-mirroring`, `#open-source`, `#tooling`

---

<a id="item-19"></a>
## [AI 鼠标指针：DeepMind 的语音驱动重新设计](https://deepmind.google/blog/ai-pointer/) ⭐️ 7.0/10

DeepMind 提出了一种 AI 驱动的鼠标指针，它使用语音命令和上下文理解来简化用户交互，允许通过语音提示执行移动对象或添加文本等操作。 这一概念可能从根本上改变人机交互，减少对菜单和键盘快捷键的依赖，但也引发了可能限制其采用的重大可用性和隐私问题。 该指针与 LLM 集成以解释上下文和语音输入，但批评者指出，许多操作可以通过现有菜单或键盘快捷键更快地完成，并且持续的服务器通信会带来隐私风险。

hackernews · devhouse · May 12, 17:40 · [社区讨论](https://news.ycombinator.com/item?id=48111581)

**背景**: 鼠标指针是图形用户界面的基本元素，通常通过物理移动控制。DeepMind 的提议增加了一层 AI，实现上下文感知交互，可能减少手动导航的需求。语音控制在计算领域历史悠久，但由于准确性和社交尴尬而仍然小众。

**社区讨论**: 评论者持怀疑态度，许多人指出语音控制在共享空间中不切实际，并且演示显示与传统方法相比没有节省时间。还提出了对持续服务器通信的隐私担忧。少数评论者看到了与 LLM 进行连续“指向并说话”交互的潜力。

**标签**: `#AI`, `#human-computer interaction`, `#DeepMind`, `#user interface`, `#voice control`

---

<a id="item-20"></a>
## [通过沙箱 iframe 实现用户控制的 CSP 白名单](https://simonwillison.net/2026/May/13/csp-allow/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一个工具，将应用加载到受 CSP 保护的沙箱 iframe 中，拦截因 CSP 违规导致的 fetch 错误，提示用户将拦截的来源加入白名单，然后刷新页面。 该实验引入了一种新颖的、由用户驱动的内容安全策略管理方法，有望在不降低整体安全性的前提下，更轻松地处理动态的第三方资源需求。 该工具在沙箱内使用自定义的 fetch() 捕获 CSP 错误，并将其传递给父窗口，父窗口随后显示一个模态框请求用户许可；该工具使用 Codex 桌面应用中的 GPT-5.5 xhigh 构建。

rss · Simon Willison · May 13, 04:50

**背景**: 内容安全策略 (CSP) 是一种浏览器安全机制，通过 HTTP 头限制页面可以加载哪些资源。iframe 上的 sandbox 属性进一步限制嵌入的内容，赋予其唯一来源并限制其功能。通常，CSP 白名单是静态的并由服务器设置；而该实验根据用户交互动态调整白名单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox">Content-Security-Policy: sandbox directive - HTTP | MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP">Content Security Policy (CSP) - HTTP | MDN - MDN Web Docs Usage example</a></li>

</ul>
</details>

**标签**: `#CSP`, `#security`, `#web`, `#sandbox`, `#iframe`

---

<a id="item-21"></a>
## [Mitchell Hashimoto 谈技术决策者的风险规避](https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything) ⭐️ 7.0/10

HashiCorp 联合创始人 Mitchell Hashimoto 在 Lobste.rs 上提出了一个批评性观察，认为 90% 的技术决策者主要动机是避免责任，导致他们跟随分析师趋势如“AI 战略”，而非真正的创新。 这一见解揭示了一个普遍但鲜少讨论的企业技术采用驱动力，解释了为何流行词驱动的采购常胜过技术更优的解决方案，并可能帮助开发者和供应商更好地理解决策者心理。 该引文来自 Lobste.rs 上关于 Redis 主页设计的讨论。Hashimoto 区分了热情的贡献者和风险规避型管理者，后者依赖分析师背书（如 Gartner、McKinsey）来证明采购的合理性。

rss · Simon Willison · May 12, 22:21

**背景**: Mitchell Hashimoto 以 HashiCorp 联合创始人身份闻名，并创造了 Vagrant、Terraform、Consul 等流行 DevOps 工具。技术决策者（TDM）是组织中负责选择技术的个人。Hashimoto 的批评反映了一种常见模式：风险规避行为导致技术采购中的从众心态，优先选择与市场趋势一致的安全选项，而非创新但未经证实的替代方案。

**标签**: `#technology decision making`, `#marketing`, `#tech industry`, `#risk aversion`

---

<a id="item-22"></a>
## [LLM 0.32a2 增加对 OpenAI /v1/responses 端点的支持](https://simonwillison.net/2026/May/12/llm/#atom-everything) ⭐️ 7.0/10

LLM 0.32a2 的 alpha 版本现在对大多数具备推理能力的 OpenAI 模型使用 /v1/responses 端点，替代了 /v1/chat/completions，从而支持跨工具调用的交错推理，并向用户显示摘要化的推理 token。 此次更新使用户能够看到模型输出背后的推理过程，增强了使用 OpenAI 高级推理模型（如 GPT-5 类模型）的开发者的透明度和调试能力。 推理 token 以与标准错误不同的颜色显示，用户可以通过 -R 或 --hide-reasoning 标志隐藏它们。此更改是开源 LLM 项目中的拉取请求 #1435 的一部分。

rss · Simon Willison · May 12, 17:45

**背景**: LLM 是 Simon Willison 开发的命令行工具和 Python 库，用于与大型语言模型交互。/v1/responses 端点是 OpenAI 的新 API，用于高级代理工作流和链式思维推理。推理 token 是模型在提供最终答案之前用于规划和生成中间输出的内部 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.openai.com/docs/api-reference/responses">platform. openai .com/docs/api-reference/ responses</a></li>
<li><a href="https://openrouter.ai/docs/guides/best-practices/reasoning-tokens">Reasoning Tokens | Enhanced AI... | OpenRouter | Documentation</a></li>

</ul>
</details>

**标签**: `#llm`, `#openai`, `#reasoning`, `#tool release`, `#ai`

---

<a id="item-23"></a>
## [GitLab 裁员与战略转型](https://simonwillison.net/2026/May/11/gitlab-act-2/#atom-everything) ⭐️ 7.0/10

GitLab 宣布裁员 7%，计划将运营国家数量减少 30%，扁平化管理层级，并废除原有的 CREDIT 价值观框架，代之以“速度与质量”、“客户成果”等新价值观，以适应智能体时代。 此次重组反映了科技公司为 AI 驱动效率而进行激进调整的广泛趋势，可能成为远程优先企业适应智能体时代的蓝图。这些变化将影响数百名员工，并重塑 GitLab 的运营模式。 GitLab 将裁员 7%，减少拥有小团队的国家的数量达 30%，在某些职能部门裁撤多达三层管理层，并将研发部门重组为约 60 个小型自主团队。CREDIT 价值观框架被“速度与质量”、“主人翁心态”和“客户成果”取代，但多样性仍保留在“人际卓越”的子条目下。

rss · Simon Willison · May 11, 23:58

**背景**: GitLab 以其全远程员工队伍和透明手册而闻名，业务遍及近 60 个国家。“智能体时代”指的是 AI 智能体能够自主执行任务的趋势，增加了软件需求。此次重组旨在通过自动化内部流程和赋能小型团队，使 GitLab 为这一新时代做好准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.gitlab.com/blog/gitlab-act-2/">GitLab Act 2</a></li>
<li><a href="https://www.thehrdigest.com/agentic-ai-ambitions-strike-again-as-gitlab-announces-layoffs-for-2026/">Agentic AI Ambitions Strike Again as GitLab Announces Layoffs ...</a></li>

</ul>
</details>

**标签**: `#GitLab`, `#business strategy`, `#remote work`, `#workforce reduction`

---

<a id="item-24"></a>
## [James Shore 警告：AI 编程工具必须降低维护成本](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 7.0/10

James Shore 指出，AI 编程工具必须在提高编码效率的同时，以相同比例降低维护成本，否则长期成本将失控。他用简单的数学模型说明，如果效率翻倍而维护成本未减半，总维护费用将变为四倍。 这揭示了采用 AI 进行软件开发时一个常被忽视的关键权衡：效率提升可能被累积的技术债务抵消。工程领导者和开发者需要基于长期成本影响而不仅是速度来评估 AI 工具。 Shore 的论点基于公式：总维护成本随（效率乘数）×（维护成本乘数）变化。若效率翻倍（乘数 2）而维护不变（乘数 1），总成本翻倍；若维护同时减半（0.5），总成本不变。

rss · Simon Willison · May 11, 19:48

**背景**: 软件维护成本占总拥有成本的很大一部分，通常超过初始开发成本。AI 编程工具通过快速生成代码提高效率，但如果生成的代码难以维护，技术债务就会增加。Shore 的洞察是，AI 工具不仅要生成代码，还要帮助管理和降低维护负担才能持续。

**标签**: `#AI coding`, `#software maintenance`, `#productivity`, `#technical debt`

---

<a id="item-25"></a>
## [参数高尔夫：AI 辅助模型设计的启示](https://openai.com/index/what-parameter-golf-taught-us) ⭐️ 7.0/10

OpenAI 发布了参数高尔夫比赛的见解，该比赛有超过 1000 名参与者提交了超过 2000 个模型，这些模型在严格约束下训练：16MB 大小限制和在 8×H100 GPU 上 10 分钟的训练预算。 该比赛展示了 AI 辅助研究和编码代理如何在极端资源约束下加速模型设计，可能影响未来高效模型开发和量化技术。 模型通过在 FineWeb 验证集上的压缩率（每字节位数）进行评估，该挑战同时也是 OpenAI 的招聘渠道。

rss · OpenAI Blog · May 12, 00:00

**背景**: 量化是一种将模型权重和激活的精度降低到较低位宽（例如从 32 位浮点数到 8 位整数）的技术，使模型更小、更快，且精度损失极小。参数高尔夫设置了 16MB 总大小限制，迫使参与者应用激进的量化和其它压缩方法。比赛还探索了 AI 辅助研究，编码代理和人与 AI 协作帮助在严格预算下设计新颖架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/parameter-golf/">OpenAI Model Craft: Parameter Golf</a></li>
<li><a href="https://github.com/openai/parameter-golf/">GitHub - openai/parameter-golf: Train the smallest LM you can ...</a></li>
<li><a href="https://aihola.com/article/openai-parameter-golf-competition">OpenAI Parameter Golf: 16MB Model Competition and Hiring Pip</a></li>

</ul>
</details>

**标签**: `#AI research`, `#machine learning`, `#coding agents`, `#quantization`

---

<a id="item-26"></a>
## [AWS 上基础模型训练和推理的构建块](https://huggingface.co/blog/amazon/foundation-model-building-blocks) ⭐️ 7.0/10

Hugging Face 发布了一篇博客文章，详细介绍了用于构建和扩展基础模型训练与推理工作负载的关键 AWS 组件，包括 Trainium 和 Inferentia 加速器以及 Neuron SDK。 该指南帮助从业者在 AWS 定制硬件上高效部署大模型，可能降低生成式 AI 工作负载的成本并提高性能。 文章涵盖了从使用 AWS Trainium 进行训练到使用 AWS Inferentia 进行推理的完整工作流，并利用 AWS Neuron SDK 进行优化。

rss · Hugging Face Blog · May 11, 23:18

**背景**: 基础模型是像 GPT-4 和 Llama 这样需要大量计算资源的大型 AI 模型。AWS 开发了定制的 AI 加速器：用于训练的 Trainium 和用于推理的 Inferentia，以及用于在这些芯片上优化模型性能的 Neuron SDK。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/neuron/">SDK for Gen AI and Deep Learning - AWS Neuron - AWS</a></li>

</ul>
</details>

**标签**: `#AWS`, `#foundation models`, `#training`, `#inference`, `#machine learning`

---

<a id="item-27"></a>
## [Varda 与 United Therapeutics 合作，将在轨道上商业生产药物](https://www.technologyreview.com/2026/05/13/1137153/varda-united-therapeutics-drug-manufacturing-in-space/) ⭐️ 7.0/10

Varda Space Industries 与制药公司 United Therapeutics 签署了首个重要协议，将在微重力环境下开发和制造药物。这标志着向轨道药物商业化生产迈出了关键一步。 此次合作表明，太空药物制造正从实验阶段走向商业化，有望生产出在地球上难以制造的新型药物。这可能会开启一个基于太空的制药新产业，并吸引更多投资。 Varda 的方法是利用其航天器在微重力环境下使小分子结晶，然后通过大气再入飞行器将晶体带回地球。该公司成立于 2021 年，得到了 Khosla Ventures 和 Founders Fund 的支持。

rss · MIT Tech Review · May 13, 10:00

**背景**: 微重力环境下的药物研究已在航天飞机和国际空间站上进行了数十年，但通常受限于可及性差和成本高昂。Varda 旨在为制药商提供实用、可重复的商业服务，以利用太空中独特的结晶条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Varda_Space_Industries">Varda Space Industries</a></li>
<li><a href="https://arstechnica.com/space/2026/05/varda-signs-deal-with-major-us-pharma-firm-to-develop-drugs-in-space/">Could this be the moment that drug manufacturing takes off in ...</a></li>
<li><a href="https://spacenews.com/varda-to-collaborate-with-united-therapeutics-on-microgravity-drug-research/">Varda to collaborate with United Therapeutics on microgravity ...</a></li>

</ul>
</details>

**标签**: `#space manufacturing`, `#pharmaceuticals`, `#biotechnology`, `#commercial space`

---

<a id="item-28"></a>
## [TechPays 被 Levels.fyi 收购以提升欧洲薪酬透明度](https://blog.pragmaticengineer.com/techpays-has-been-acquired-levels-fyi/) ⭐️ 7.0/10

Levels.fyi 已收购 TechPays，这是欧洲领先的科技薪酬透明度网站，该消息于 2025 年 7 月 31 日宣布。此次收购将合并两个平台的薪酬数据，以提升薪酬透明度。 此次收购显著增强了欧洲科技工作者的薪酬透明度，他们历来比美国同行更难获得薪酬数据。合并 Levels.fyi 和 TechPays 的数据集将提供更全面的地区薪酬视图。 TechPays 由 Gergely Orosz（The Pragmatic Engineer 博客作者）和 Zsombor Szász 共同创立。该网站专注于欧洲科技薪酬，尤其是伦敦和柏林等枢纽城市，现在将整合到 Levels.fyi 中。

rss · Pragmatic Engineer · May 12, 16:06

**背景**: Levels.fyi 是一个众包平台，提供科技公司的薪酬和福利数据，主要覆盖美国。TechPays 的创建是为了解决欧洲薪酬透明度不足的问题，那里的薪资信息通常不透明。此次收购预计将加速 Levels.fyi 在欧洲市场的扩张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.pragmaticengineer.com/techpays-has-been-acquired-levels-fyi/">TechPays has been acquired by Levels.fyi - The Pragmatic Engineer</a></li>
<li><a href="https://www.levels.fyi/blog/levelsfyi-acquires-techpays.html">Levels.fyi acquires TechPays</a></li>

</ul>
</details>

**标签**: `#acquisition`, `#tech salaries`, `#pay transparency`, `#Levels.fyi`, `#TechPays`

---

<a id="item-29"></a>
## [Thinking Machines 发布 TML-Interaction-Small，新一代实时语音 AI](https://www.latent.space/p/ainews-thinking-machines-native-interaction) ⭐️ 7.0/10

Thinking Machines 发布了 TML-Interaction-Small，这是一个 2760 亿参数的混合专家模型，其中 120 亿参数被激活，实现了最先进的实时语音交互，并消除了传统语音活动检测（VAD）的需求。 该模型代表了从基于轮次的语音 AI 向原生全双工交互的转变，使语音对话更加自然和无缝。它还通过将交互性直接集成到模型架构中，挑战了现有方法，有可能为实时语音 AI 设定新标准。 该模型采用混合专家架构，总参数 2760 亿，但每次推理仅激活 120 亿参数，平衡了性能和效率。它配有一个较慢的异步后台模型，用于复杂推理、网络搜索和工具调用，使前台模型能够保持流畅对话。

rss · Latent Space · May 12, 04:33

**背景**: 传统语音 AI 系统依赖语音活动检测（VAD）来判断用户何时开始或停止说话，这会引入延迟和不自然的停顿。混合专家（MoE）模型每次输入仅激活部分参数，使更大的模型能够高效运行。Thinking Machines 的新交互模型使交互性成为原生能力，意味着模型本身处理轮次切换，无需独立的 VAD 组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.creativeainews.com/articles/thinking-machines-tml-interaction-full-duplex-voice-ai/">Thinking Machines TML - Interaction : Full-Duplex Voice AI</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/2374/thinking-machines-interaction-models-mira-murati">Thinking Machines Interaction Models : Mira Murati's full-duplex...</a></li>
<li><a href="https://picovoice.ai/blog/complete-guide-voice-activity-detection-vad/">Voice Activity Detection Guide 2026: Complete Technical Overview</a></li>

</ul>
</details>

**标签**: `#AI`, `#voice interaction`, `#realtime systems`, `#machine learning models`

---

<a id="item-30"></a>
## [AI 智能体方法 DRIL 自动化构建经济数据集](https://feeds.feedblitz.com/~/955775837/0/marginalrevolution~Using-agents-to-build-economic-datasets.html) ⭐️ 7.0/10

研究人员提出了循环深度研究（DRIL）方法，该方法利用 AI 智能体自动从公开来源构建经济数据集，相关成果发表在 NBER 工作论文 W35188 中。 DRIL 大幅降低了实证经济学中构建原始数据集的成本和时间，有望加速研究进程并支持更大规模的研究。 DRIL 在映射的单位空间（如国家×年份）上应用固定的研究工具，并采用将设计与实施分离的两阶段架构。

rss · Marginal Revolution · May 12, 04:26

**背景**: 从原始来源构建数据集是实证经济学中成本最高的任务之一，通常需要大量人工工作。AI 智能体能够自主执行网络爬取和数据提取等任务，为此提供了潜在解决方案。DRIL 通过定义可重复的方法来系统化这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nber.org/papers/w35188">Deep Research on a Loop: Using AI Agents to Construct ...</a></li>
<li><a href="https://letsdatascience.com/news/researchers-propose-dril-method-to-automate-dataset-construc-73e5ebc1">Researchers Propose DRIL Method to Automate Dataset ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对数据可靠性和 AI 生成数据集的质量表示担忧，一些人质疑在没有人工验证的情况下输出结果是否可信。

**标签**: `#AI agents`, `#economic datasets`, `#methodology`, `#Deep Research`, `#empirical economics`

---