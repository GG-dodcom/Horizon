---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> From 46 items, 7 important content pieces were selected

---

1. [揭露通过欺诈打折转售 LLM 代币的中继市场](#item-1) ⭐️ 8.5/10
2. [将细节交给 AI 可能削弱自主性](#item-2) ⭐️ 8.4/10
3. [GrapheneOS 自动重启功能保护锁定设备免受数据提取](#item-3) ⭐️ 8.4/10
4. [AI 超能力：专注与跟进](#item-4) ⭐️ 8.2/10
5. [Ruff v0.16.0 将默认规则扩展至 413 条](#item-5) ⭐️ 7.6/10
6. [欧盟提议用浏览器隐私设置消除 Cookie 横幅](#item-6) ⭐️ 7.1/10
7. [Decker 复兴 HyperCard，打造现代交互式文档](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [揭露通过欺诈打折转售 LLM 代币的中继市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.5/10

Matt Lenhard 的一项调查揭示了中国一个活跃的中继市场，转售者利用 one-api 和 new-api 等开源代理软件，通过滥用免费试用、未受保护的支持机器人、盗用信用卡及退单攻击等欺诈手段，汇集 API 密钥并以折扣价转售 LLM 代币。 这一市场破坏了 LLM 提供商收入模式，并给公开 LLM 应用的开发者带来安全风险，凸显了加强 API 使用限额和欺诈检测的紧迫性。该生态系统还支持为模型蒸馏收集数据，影响知识产权。 代理软件 one-api 和 new-api 是用于管理和分发 LLM API 密钥的合法开源项目，但被转售者利用来跨汇集凭证进行请求负载均衡。买家包括寻求廉价代币、绕过地域限制或为模型蒸馏收集数据的人。

rss · Simon Willison · Jul 26, 19:30

**背景**: LLM API 代币通常由 OpenAI 等提供商以固定价格出售，但出现了二次中继市场，转售者汇集来自免费试用、被攻破账户或盗用信用卡等各种来源的凭证，并以折扣价提供。像 one-api 和 new-api 这样的开源代理工具，本用于合法密钥管理，被重新用于构建这些中继服务。这一做法集中在中国，V2EX 论坛上的讨论是调查的关键来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/songquanpeng/one-api">GitHub - songquanpeng/one-api: LLM API 管理 & 分发系统，支持 Open...</a></li>

</ul>
</details>

**社区讨论**: 社区评论将此事与广告欺诈市场相类比，指出类似转售生态系统早已存在于其他互联网产品中。评论者强调滥用免费云服务额度（如 AWS）是主要推动因素，并将这一动态比作票务倒卖。有人质疑 AI 代币订阅模式的可持续性，认为当价格未达到市场出清水平时，套利机会是固有的。

**标签**: `#LLM`, `#fraud`, `#API security`, `#token reselling`, `#China`

---

<a id="item-2"></a>
## [将细节交给 AI 可能削弱自主性](https://davidnicholaswilliams.com/its-not-empowering-to-hand-off-the-details/) ⭐️ 8.4/10

文章指出，依赖 AI 处理细节会降低真正的理解和自主性，因为赋权来自亲自处理细节而非将其委托出去。 这一观点挑战了当前关于 AI 编程工具和智能体系统自动赋能开发者的普遍说法，呼吁对人与 AI 协作采取更细致的看法。它与技能退化及丧失深厚技术专长的担忧产生共鸣。 该文章由 David Nicholas Williams 撰写，评分为 8.4/10，因其与 AI 编码工具和开发者赋权高度相关。它被标记为 AI、LLM、软件工程、开发者工具和智能体系统。

hackernews · davnicwil · Jul 26, 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49060592)

**背景**: 智能体系统是能够自主推理、规划和执行复杂工作流程的人工智能系统，几乎无需人工干预。文章质疑了将细节委托给此类系统本身就能赋权的假设，认为真正的理解来自于亲自处理细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/agentic_ai">Agentic AI</a></li>
<li><a href="https://medium.com/mongodb/here-are-7-design-patterns-for-agentic-systems-you-need-to-know-d74a4b5835a5?trk=article-ssr-frontend-pulse_little-text-block">7 Design Patterns for Agentic Systems You NEED to Know | MongoDB</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：一些人同意过度依赖 AI 会导致疲劳和失控，而另一些人则认为验证并不需要完全理解，且如果专注于高层设计，委托也可以是赋权的。一位评论者指出，经验丰富的开发者会培养出判断哪些细节需要仔细审查的能力，另一位则分享了使用 AI 进行世嘉 Genesis 自制游戏开发的积极体验，专注于创意方面。

**标签**: `#AI`, `#LLM`, `#software engineering`, `#developer tools`, `#agentic systems`

---

<a id="item-3"></a>
## [GrapheneOS 自动重启功能保护锁定设备免受数据提取](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 8.4/10

Hacker News 上的一个讨论强调了 GrapheneOS 的 18 小时自动重启功能，该功能将锁定设备恢复到首次解锁前（BFU）状态，即使没有胁迫密码也能防止法医数据提取。 该功能通过确保设备无人看管时加密密钥不可访问，为记者、活动家和注重隐私的用户显著增强了移动设备安全性，从而挫败执法部门和攻击者使用的法医工具。 自动重启在设备闲置 18 小时后触发，将设备重置为 BFU 模式，此时全盘加密密钥未加载到内存中，使得数据提取几乎不可能。这是 GrapheneOS 增强的上游 Android 功能。

hackernews · Cider9986 · Jul 26, 05:57 · [社区讨论](https://news.ycombinator.com/item?id=49055169)

**背景**: 移动设备有两种主要锁定状态：首次解锁前（BFU）和首次解锁后（AFU）。在 BFU 模式下，设备已开机但用户尚未输入密码，因此基于文件的加密密钥缺失，限制了数据访问。一旦解锁（AFU），加密密钥便驻留在内存中，使提取更容易。GrapheneOS 的自动重启在闲置一段时间后强制返回 BFU 模式，从而缩小了脆弱窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.dsu.edu/digforce/2023/08/23/bfu-and-afu-lock-states/">BFU and AFU Lock States – Blog | DigForCE Lab - DSU</a></li>
<li><a href="https://discuss.grapheneos.org/d/23736-automatic-18-hour-reboots">Automatic 18 hour reboots - GrapheneOS Discussion Forum</a></li>
<li><a href="https://teeltechcanada.com/understanding-mobile-device-lock-states-in-forensic-extractions/">Understanding Mobile Device Lock States in Forensic ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该功能的强大保护，rzk 指出即使没有胁迫密码也能起作用。prmoustache 呼吁提供完整的备份方案以支持边境前擦除，muyuu 分析了图案锁的熵。himata4113 指出苹果设备上也有类似保护，usern20260720 赞赏有一部不与其用户作对的手机。

**标签**: `#GrapheneOS`, `#mobile security`, `#data extraction`, `#BFU mode`, `#privacy`

---

<a id="item-4"></a>
## [AI 超能力：专注与跟进](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and) ⭐️ 8.2/10

文章认为，AI（尤其是编码代理）可以增强开发者的专注力和跟进能力，减轻认知负担，使他们能够更高效地处理更多项目。 这一转变可能大幅提升软件开发效率，减少职业倦怠，让开发者将更多时间用于创造性问题解决而非重复性任务。 文章将专注和跟进视为 AI 放大的新超能力，开发者利用代理探索假设项目、修复配置问题，而不会陷入困境。

hackernews · mooreds · Jul 26, 13:13 · [社区讨论](https://news.ycombinator.com/item?id=49057877)

**背景**: 像 GitHub Copilot 和 Cursor 这样的 AI 编码助手已在软件开发中普及，自动化模板代码和调试。但这篇文章强调了保持专注和跟进项目的人类技能，AI 可以增强这些技能以改善整体工作流程。

**社区讨论**: 评论者表达了复杂的看法：一些人担心出现碎片化、不兼容的解决方案泛滥，而另一些人则报告使用 AI 代理后职业倦怠减少、特性开发速度提升。一位用户指出，AI 有助于项目的 99%，但最后的 1% 仍需人工完成。

**标签**: `#AI`, `#LLM`, `#programming`, `#productivity`, `#software engineering`

---

<a id="item-5"></a>
## [Ruff v0.16.0 将默认规则扩展至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.6/10

Ruff v0.16.0 将默认规则数量从 59 条增加到 413 条，导致许多使用未锁定 Ruff 版本的项目出现 CI 失败。 此变更迫使 Python 开发者更新配置并修复成千上万新标记的问题，同时也展示了 AI 编码代理自动化此类修复的日益强大的能力。 该更新于 2026 年 7 月 23 日发布，使用 `uvx ruff@latest check . --fix --unsafe-fixes` 命令可自动修复大部分问题；例如，在 sqlite-utils 项目中修复了 1,618 个错误中的 1,538 个。

rss · Simon Willison · Jul 25, 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python 代码检查器和格式化工具，由 Astral 开发（现已成为 OpenAI 的一部分）。它可以替代 Flake8、isort、pydocstyle 等工具。此前默认规则集自 0.1.0 版本起未再更新，而可用规则总数已从 708 条增长至 968 条。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code ...</a></li>
<li><a href="https://pypi.org/project/ruff/">ruff · PyPI</a></li>

</ul>
</details>

**标签**: `#Ruff`, `#Python`, `#linting`, `#developer tools`, `#Astral`

---

<a id="item-6"></a>
## [欧盟提议用浏览器隐私设置消除 Cookie 横幅](https://killthecookiebanner.eu/) ⭐️ 7.1/10

欧盟委员会提出了一项浏览器级别的隐私偏好解决方案，允许用户一次性设置隐私偏好，从此再也不用看到 Cookie 横幅，但追踪行业正在反对这一提案。 如果被采纳，这将消除困扰网络的恼人且往往具有误导性的 Cookie 横幅，让用户真正掌控自己的隐私，同时为全球同意管理树立潜在标准。 该提案建立在 Global Privacy Control（GPC）等现有技术之上，该技术已在某些隐私法律下具有法律效力；然而，追踪行业和大型广告公司正在游说反对该提案，以保留追踪用户的能力。

hackernews · rapnie · Jul 26, 11:53 · [社区讨论](https://news.ycombinator.com/item?id=49057175)

**背景**: 根据欧盟法律（ePrivacy 指令和 GDPR），网站必须通过 Cookie 横幅获取用户对非必要 Cookie 的同意。然而，许多横幅被设计成诱导用户接受追踪，因此广受批评。Global Privacy Control（GPC）是一种浏览器信号，告诉网站用户不希望其数据被出售或共享，该信号已被加州消费者隐私法案（CCPA）等某些州法律认可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://killthecookiebanner.eu/">Kill the Cookie Banner !</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Privacy_Control">Global Privacy Control</a></li>
<li><a href="https://privacybadger.org/">Privacy Badger | Electronic Frontier Foundation</a></li>

</ul>
</details>

**社区讨论**: 新闻评论者普遍支持该提案，有人主张欧盟应更进一步，声明勾选复选框不能构成知情同意。还有人指出加州已经实施了类似的浏览器级别控制，而有些人则简单地建议，最简单的解决方案是彻底停止追踪用户。

**标签**: `#privacy`, `#cookie banners`, `#EU regulation`, `#browser standards`, `#web technology`

---

<a id="item-7"></a>
## [Decker 复兴 HyperCard，打造现代交互式文档](https://beyondloom.com/decker/) ⭐️ 7.0/10

Decker 是一个受 HyperCard 启发的多媒体平台，已发布为现代工具，用于创建包含声音、图像、超文本和脚本的交互式文档。 Decker 重现了 HyperCard 那平易近人、直观的编程环境，使非程序员也能构建应用，可能重新点燃草根软件创作运动。 Decker 采用经典 MacOS 外观但可在现代系统上运行，并使用自己的脚本语言 Lil 实现交互性。它旨在作为 HyperCard 的精神继承者，注重简洁和复古魅力。

hackernews · tosh · Jul 26, 18:23 · [社区讨论](https://news.ycombinator.com/item?id=49060856)

**背景**: HyperCard 是由苹果公司在 1987 年发布的革命性超媒体系统，它将数据库与图形界面结合起来，允许非程序员创建包含按钮、文本和媒体的“卡片堆栈”。它早于万维网，并启发了一代开发者和爱好者。Decker 由 John Earnest 创建，旨在通过现代兼容性和 1 位复古美学重现那种体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beyondloom.com/decker/">Decker</a></li>
<li><a href="https://en.wikipedia.org/wiki/HyperCard">HyperCard - Wikipedia</a></li>
<li><a href="https://hackaday.com/2023/09/22/decker-is-the-cozy-retro-creative-engine-you-didnt-know-you-needed/">Decker Is The Cozy Retro Creative Engine You Didn’t Know You Needed | Hackaday</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对 HyperCard 的强烈怀旧之情，用户回忆起它如何使编程变得平易近人。一些人将 Decker 与 Delphi 和 Lazarus 等现代工具进行了有利比较，而另一些人则质疑这样的平台在当今以网络为中心的世界中能否找到一席之地。总体情绪是积极的，希望 Decker 能重振 HyperCard 的易用性和乐趣。

**标签**: `#hypercard`, `#retrocomputing`, `#programming-tools`, `#decker`

---