---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 34 items, 13 important content pieces were selected

---

1. [美国政府命令 Anthropic 暂停 Fable 5 和 Mythos 5 访问](#item-1) ⭐️ 9.6/10
2. [保罗·格雷厄姆的十亿美元公司创建指南](#item-2) ⭐️ 9.5/10
3. [里约热内卢自研大语言模型被曝是现有模型的加权合并](#item-3) ⭐️ 9.4/10
4. [将 SQLite 结果列映射回源表.列](#item-4) ⭐️ 9.0/10
5. [本地 ML 在 M1 Max 上索引 669 GB GoPro 视频](#item-5) ⭐️ 8.9/10
6. [形式化方法与编程的未来](#item-6) ⭐️ 8.8/10
7. [2014 年演讲准确预言 WebAssembly 取代 JavaScript](#item-7) ⭐️ 8.8/10
8. [人工智能使用率未如预期广泛](#item-8) ⭐️ 8.2/10
9. [OpenAI WebRTC 语音工具更新：支持 GPT-Realtime-2 与文档上下文](#item-9) ⭐️ 8.1/10
10. [Pyodide 314.0 支持直接将 WASM wheel 发布到 PyPI](#item-10) ⭐️ 8.0/10
11. [Kage：将任何网站打包成单个二进制文件以便离线查看](#item-11) ⭐️ 7.5/10
12. [轨道数据中心比硅谷想的更难](#item-12) ⭐️ 7.5/10
13. [Zeroserve 宣称与 Caddy 兼容，速度大幅提升](#item-13) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [美国政府命令 Anthropic 暂停 Fable 5 和 Mythos 5 访问](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything) ⭐️ 9.6/10

美国政府发布出口管制指令，以国家安全为由，暂停任何外国国民（包括外国籍 Anthropic 员工）对 Fable 5 和 Mythos 5 模型的访问。Anthropic 于 2026 年 6 月 12 日突然为所有客户禁用了访问权限。 这标志着政府在 AI 模型访问方面前所未有的干预，引发了关于国家安全、出口管制以及 AI 进步与安全之间平衡的重大问题。它为美国政府未来如何监管前沿 AI 模型开创了先例。 指令于 2026 年 6 月 12 日东部时间下午 5:21 收到，访问权限在太平洋时间下午 6:59 被切断。Anthropic 对严重性提出异议，指出所谓的越狱技术在其他模型（如 GPT-5.5）中也存在，并被防御者使用。

rss · Simon Willison · Jun 13, 01:01

**背景**: Fable 5 是 Anthropic 推出的“Mythos 级”模型，已确保通用安全性，而 Mythos 5 则用于漏洞发现。美国政府使用了通常适用于军民两用技术的出口管制权力，将这些 AI 模型视为国家安全问题。Anthropic 此前已公开发布 Fable 5，声称其具有足够的安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/fable-mythos-access">Statement on the US government directive to suspend access to Fable 5 and Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.nytimes.com/2026/06/12/technology/anthropic-mythos-fable5-blocked.html">U.S. Bars Foreigners From Using Anthropic ’s Most Advanced...</a></li>
<li><a href="https://www.bbc.com/news/articles/c932g3v3e13o">Anthropic 's Claude Fable 5 and Mythos 5 AI suspended over security...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#regulation`, `#Anthropic`, `#government directive`

---

<a id="item-2"></a>
## [保罗·格雷厄姆的十亿美元公司创建指南](https://paulgraham.com/earn.html) ⭐️ 9.5/10

这篇文章提出了一个创建十亿美元公司的框架，核心是做出人们想要的东西并占领大市场。 这一见解对寻求规模化发展的创业者意义重大，因为它提炼出独角兽背后的关键原则，并挑战了关于财富创造的常见误解。 格雷厄姆强调，十亿级的成果通常来自解决大量未被满足的需求，而非渐进式改进，他还提醒创始人常常低估规模化扩张的难度。

hackernews · kingstoned · Jun 14, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48526360)

**背景**: 这篇文章是保罗·格雷厄姆创业建议系列的一部分。他是一名风险投资家，也是 Y Combinator 的联合创始人。"独角兽"——估值超过 10 亿美元的初创公司——是风险投资的核心概念。

**社区讨论**: 评论呈现支持与批评并存。部分读者赞赏其实用建议，另一些则指出十亿美元级初创公司常伴随剥削或外部负面效应。还有些人用增长率的数学推演进行辩论。

**标签**: `#startups`, `#entrepreneurship`, `#wealth`, `#business strategy`, `#technology`

---

<a id="item-3"></a>
## [里约热内卢自研大语言模型被曝是现有模型的加权合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 9.4/10

一项调查显示，里约热内卢市政府声称自研的 Rio-3.5-Open-397B 模型实际上是 Nex-N2 Pro（约 60%）和 Qwen3.5-397B-A17B（约 40%）的加权合并，并未进行额外训练。 这一发现引发了对 AI 开发透明度和归属的严重担忧，因为它削弱了对所谓自研模型的信任，并凸显了适当披露模型来源的必要性。 Rio 的每个权重张量在所有 60 层中都与 Nex 和 Qwen 的 0.6/0.4 混合结果匹配，偏差在数千个标准差内；作者未披露合并操作或对 Nex-N2 Pro 的使用。

hackernews · unrvl22 · Jun 14, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种通过加权平均或其他方法合并两个或多个模型参数的技术，无需在新数据上训练即可提升性能。该技术在 LLM 社区中常见，但发布衍生作品时需要适当归属。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2411.09263v4">Rethinking Weight-Averaged Model-merging - arXiv.org</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/blog/mlabonne/merge-models">Merge Large Language Models with mergekit</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点不一：有人辩护称这是合法的模型合并，可能还进行了在线策略蒸馏但未上传；另一些人批评缺乏归属和透明度，将其比作利用他人工作获利。

**标签**: `#LLM`, `#model merging`, `#open-source`, `#AI ethics`, `#investigation`

---

<a id="item-4"></a>
## [将 SQLite 结果列映射回源表.列](https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything) ⭐️ 9.0/10

Simon Willison 使用 Claude Code 探索了三种编程方法，用于确定任意 SQL 查询中每个结果列的来源表和列，旨在为 Datasette 增加列溯源信息。 这项研究使得 Datasette 中能够实现更丰富的用户界面，例如显示列来源，并展示了从 Python 访问 SQLite 内部列元数据的实用技术，而这原本并未原生暴露。 三种方法包括使用 apsw 库、通过 ctypes 调用 sqlite3_column_table_name() C 函数，以及智能解析 EXPLAIN 输出。所有方法都要求 SQLite 编译时启用 SQLITE_ENABLE_COLUMN_METADATA。

rss · Simon Willison · Jun 13, 23:05

**背景**: 列溯源是指识别 SQL 查询中每个结果列来自哪个表和列，这对数据血缘和 UI 增强至关重要。Datasette 是一个用于探索和发布数据库的开源工具。SQLite 内部计算了这些信息，但其 Python sqlite3 模块并未暴露，因此激发了这些替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/">Research: Mapping SQLite result columns back to their source ...</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#SQL`, `#Datasette`, `#column provenance`, `#Claude Code`

---

<a id="item-5"></a>
## [本地 ML 在 M1 Max 上索引 669 GB GoPro 视频](https://news.ycombinator.com/item?id=48528029) ⭐️ 8.9/10

作者在 M1 Max Mac 上使用开源 ML 模型索引了 2207 个 GoPro 视频（669 GB，超过 15 小时），检测并编译出精彩瞬间，直接发送到 DaVinci Resolve 时间线。 这表明在消费级硬件上进行强大的本地 AI 视频分析已成为可能，为个人媒体管理提供了保护隐私且免费的云服务替代方案。 该流程以每秒 1 帧处理视频，分析了 57,537 帧，计算时间 67 小时；它使用开源模型进行场景检测和嵌入，无需互联网连接。

hackernews · iliashad · Jun 14, 15:13

**背景**: GoPro 用户常积累大量视频库，手动回顾很繁琐。本地 ML 模型通过分析帧嵌入自动识别相关场景（如骑行高光）。M1 Max 的统一内存和 GPU 加速了这些工作负载，无需依赖云。DaVinci Resolve 是专业视频编辑器；脚本可直接将选定片段导入其时间线。

**社区讨论**: 评论者指出 DaVinci Resolve 21 已内置 AI 智能搜索实现类似索引，另一用户分享了并行项目 Framedex。对于计算时间与付费云替代方案的对比存在好奇，也有关于适用于其他视频收藏的轻松玩笑。

**标签**: `#AI`, `#video processing`, `#GoPro`, `#local ML`, `#personal project`

---

<a id="item-6"></a>
## [形式化方法与编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.8/10

Jane Street 的一篇博客文章探讨了形式化方法在编程中不断演变的角色，强调它们如何通过将人类工作转向验证以及使用 Scala 3 等语言中的表达性类型来补充 AI 生成的代码。 随着 AI 生成大量代码，形式化方法对于确保正确性和安全性变得至关重要，可能重新定义程序员的角色——从编写代码转向验证代码。 文章提到了像 SAT 求解器和 Boyer-Moore 证明器这样的证明自动化工具，社区评论指出 Scala 3 中的表达性类型有助于防止 AI 生成代码中的“名词堆积”等问题。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法使用数学模型来规范和验证软件系统，提供比单独测试更强的保证。Scala 3 等语言中的表达性类型允许在编译时证明程序不变量。随着 AI 代码生成的兴起，人们越来越有兴趣将人类专业知识转向验证任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_methods">Formal methods - Wikipedia</a></li>
<li><a href="https://www.flyriver.com/g/expressive-type-system">Expressive Type Systems: A Deep Dive - flyriver.com</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了各种经验：Animats 回忆了早期使用 SAT 求解器和 Boyer-Moore 证明器的证明自动化工作；winwang 称赞 Scala 3 的表达性类型能控制 AI agent 的质量；jdw64 指出 AI 生成的代码使验证对非英语母语者至关重要；brap 质疑形式化规范是否只是重复测试，可能带来同样的错误。

**标签**: `#formal methods`, `#programming`, `#verification`, `#AI`, `#Scala`

---

<a id="item-7"></a>
## [2014 年演讲准确预言 WebAssembly 取代 JavaScript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.8/10

2014 年的演讲“JavaScript 的诞生与死亡”预言 JavaScript 将成为编译目标并最终被取代，这一预言准确预示了 WebAssembly 的发展（于 2015 年宣布，2017 年首次发布）。 这一预言凸显了 web 平台向支持 JavaScript 以外的高性能语言发展的趋势，其准确性验证了 WebAssembly 作为可移植编译目标的愿景，该愿景现已为众多 web 和非 web 应用提供动力。 该演讲的创作者 Gary Bernhardt 也以著名的“Wat”演讲闻名；预言中提到 JavaScript 将仅成为编译目标，而 WebAssembly 后来确实承担了这一角色，但仍需 JavaScript 作为胶水代码来访问 DOM。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: JavaScript 最初被设计为 web 浏览器的脚本语言，但后来演变为通用语言。2013 年，asm.js 作为 JavaScript 的一个子集被引入，用于高性能应用。该演讲预言 JavaScript 将退化为编译目标，这最终促成了 WebAssembly 的开发——一种以接近原生速度运行的低级二进制格式。WebAssembly 现已成为 W3C 标准，受到所有主流浏览器支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区普遍认为该演讲的预言准确，有评论指出 WebAssembly 的进展不如预期快，仍需 JavaScript 进行 DOM 操作，而另有人开玩笑说演讲意外预言了 2020-2025 年间的一场全球灾难，虽然灾难类型错了，但“非常 JavaScript”。

**标签**: `#JavaScript`, `#WebAssembly`, `#Programming Languages`, `#Tech Talk`, `#Historical`

---

<a id="item-8"></a>
## [人工智能使用率未如预期广泛](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) ⭐️ 8.2/10

一篇文章指出，尽管人工智能热潮高涨，许多人使用 AI 工具的频次低于每周一次，求职者在面试中被问及 AI 使用情况时陷入两难。 这挑战了 AI 普及的假设，显示实际使用落后于感知，影响产品设计、招聘实践和投资决策。 文章引用了一项研究，显示超过 50%的人每周使用 AI 不足一次，并指出求职者必须在热衷 AI 和犹豫 AI 的雇主之间权衡。

hackernews · yegg · Jun 14, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=48527700)

**背景**: 自 2022 年底 ChatGPT 发布以来，AI 工具获得了大量媒体关注和企业投资。然而，在日常工作和个人生活中的采用可能不均衡，许多用户只是偶尔尝试 AI，并未深度整合。

**社区讨论**: 评论者指出，AI 整合更多是将功能嵌入现有软件，而非独立的聊天界面。一些人仍持怀疑态度，其中一位表示自己至今未尝试过任何 AI。

**标签**: `#AI`, `#LLMs`, `#adoption`, `#usage statistics`, `#perspective`

---

<a id="item-9"></a>
## [OpenAI WebRTC 语音工具更新：支持 GPT-Realtime-2 与文档上下文](https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything) ⭐️ 8.1/10

Simon Willison 更新了他的基于浏览器的 OpenAI WebRTC 语音工具，新增支持最新发布的 GPT-Realtime-2 模型和可选的文档上下文功能，用户可粘贴文本并围绕该内容进行语音对话。 此次更新让先进的实时语音 AI 在一个简单的浏览器工具中变得易于使用，填补了 OpenAI 自有应用尚未支持 GPT-Realtime-2 的空缺，并展示了文档上下文在交互式语音讨论中的实际应用。 用户可以在新旧模型之间切换，选择如 Coral 等语音，并在开始会话前粘贴任意文本作为文档上下文；模型随后通过音频讨论该内容。

rss · Simon Willison · Jun 12, 23:53

**背景**: OpenAI 的 Realtime API 支持使用 GPT-Realtime-2 等模型进行低延迟的语音到语音交互，该模型据称拥有 GPT-5 级别的推理能力。WebRTC 是浏览器中实时通信的标准。Simon Willison 的这个工具是一个轻量级的开源浏览器应用，用于展示这些能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/realtime-webrtc">Realtime API with WebRTC | OpenAI API</a></li>
<li><a href="https://awesomeagents.ai/news/openai-realtime-api-ga-three-models/">OpenAI's Realtime API Goes GA with Three New... | Awesome Agents</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#WebRTC`, `#audio`, `#tooling`, `#GPT-Realtime-2`

---

<a id="item-10"></a>
## [Pyodide 314.0 支持直接将 WASM wheel 发布到 PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 8.0/10

Pyodide 314.0 于 2026 年 6 月 13 日发布，允许 Python 包维护者使用 PEP 783 中定义的新 PyEmscripten 平台标签，直接将 WebAssembly (WASM) wheel 构建并发布到 PyPI。 这消除了之前 Pyodide 维护者需要手动构建和托管超过 300 个包的瓶颈，大大减轻了维护负担，并使社区能够独立分发包。 平台标签格式为 pyemscripten_YYYY_M_wasm32，支持已于 2026 年 4 月添加到 PyPI 的 Warehouse 仓库。cibuildwheel 等工具现在可以生成这些 wheel，工作示例包 'luau-wasm' 已发布作为示范。

rss · Simon Willison · Jun 13, 23:55

**背景**: Pyodide 是一个基于 WebAssembly 的 Python 发行版，可在浏览器和 Node.js 中运行 Python 代码。之前，分发包含编译为 WASM 的 C 或 Rust 扩展的 Python 包需要 Pyodide 维护者手动介入。PEP 783 标准化了 Emscripten wheel 的平台标签，使其能够像原生 wheel 一样发布到 PyPI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>
<li><a href="https://pyodide.org/en/314.0.0/development/abi.html">The PyEmscripten Platform — Version 314.0.0 - pyodide.org</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps.python.org</a></li>

</ul>
</details>

**标签**: `#Pyodide`, `#WASM`, `#PyPI`, `#Python packaging`, `#dev tools`

---

<a id="item-11"></a>
## [Kage：将任何网站打包成单个二进制文件以便离线查看](https://github.com/tamnd/kage) ⭐️ 7.5/10

Kage 是一款新的开源工具，可将任何网站克隆为单个自包含的二进制文件用于离线查看，它使用无头 Chrome 捕获渲染后的 DOM，并去除所有 JavaScript。支持输出为文件夹、ZIM 存档或独立二进制文件。 该工具满足了在无 JavaScript 依赖的情况下轻量、离线访问网页存档的需求，对开发者、研究人员以及低网络环境用户非常有价值。它反映了反对网页臃肿以及以可移植格式保存网络内容的更广泛趋势。 Kage 使用无头 Chrome 渲染页面，然后快照 DOM 并移除所有 JavaScript，生成静态快照。它可以输出包含内置 HTTP 服务器的单个二进制文件，这是因为浏览器安全限制阻止直接从 file:// URL 加载本地资源。

hackernews · tamnd · Jun 14, 17:25 · [社区讨论](https://news.ycombinator.com/item?id=48529990)

**背景**: 传统的网站存档工具如 HTTrack 下载原始 HTML 和资源，但通常在 JavaScript 密集的网站上失效。较新的工具如 SingleFile 使用 base64 编码将所有内容打包到单个 HTML 文件中。Kage 采用不同方法：先渲染页面，捕获 JavaScript 执行后的 DOM，对动态内容更准确，同时提供单二进制分发，更易于分享。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tamnd/kage">GitHub - tamnd/ kage : Shadow any website for offline viewing, with the...</a></li>
<li><a href="https://news.lavx.hu/article/kage-when-developers-start-questioning-javascript-s-grip-on-the-web">kage : When Developers Start Questioning JavaScript's Grip on the Web</a></li>
<li><a href="https://www.getsinglefile.com/">SingleFile - Effortlessly Save and Preserve Web Pages</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞赏 Kage 的概念，但指出 SingleFile 和 HTTrack 已经提供类似功能。一位用户请求无需单独服务进程的版本，另一位指出演示 GIF 是使用作者的另一款工具 ascii-gif 制作的。讨论还强调了在无蜂窝网络覆盖的地区离线访问公司 wiki 等用例。

**标签**: `#devtools`, `#offline`, `#web archiving`, `#static site`

---

<a id="item-12"></a>
## [轨道数据中心比硅谷想的更难](https://www.solidot.org/story?sid=84571) ⭐️ 7.5/10

一篇文章批判性地审视了轨道数据中心的物理和经济挑战，指出所谓的免费冷却是误解，其成本比地面数据中心高出一个数量级。 这一分析至关重要，因为 SpaceX、Google 和 Starcloud 等大公司正积极推动太空 AI 计算，但研究结果表明其在经济上可能并不可行，这将影响投资决策和研究重点。 在太空中，只有辐射冷却有效，需要庞大且昂贵的散热器来防止芯片过热；太阳能需要复杂的定向系统，而宇宙射线会降低部件性能。在轨道上运行 AI GPU 一年的成本至少比地面高出一个数量级。

rss · Solidot · Jun 13, 15:22

**背景**: 轨道数据中心是指搭载 AI GPU 的卫星星座，使用光链路互联和微波通信。支持者声称优势包括丰富的太阳能和免费的冷却，但在真空中，热量无法通过传导或对流散发——只能通过辐射，而辐射效率低得多。这种关于冷却的误解是文章批评的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Radiant_heating_and_cooling">Radiant heating and cooling - Wikipedia</a></li>
<li><a href="https://futureofenergy.co.ke/energy/the-hidden-advantage-radiative-cooling-in-space/">The Hidden Advantage Radiative Cooling in Space - Africa Digest...</a></li>

</ul>
</details>

**标签**: `#orbital data centers`, `#AI infrastructure`, `#satellite computing`, `#cooling physics`, `#economics`

---

<a id="item-13"></a>
## [Zeroserve 宣称与 Caddy 兼容，速度大幅提升](https://su3.io/posts/zeroserve-caddy-compat) ⭐️ 7.3/10

基于 eBPF 的网络服务器 Zeroserve 实现了与 Caddy 配置格式的兼容，声称相比标准 Caddy 吞吐量提高 3 倍，延迟降低 70%。 这种性能提升可能挑战像 NGINX 这样的主流网络服务器，但缺乏 ACME 和插件支持可能限制实际采用。 该兼容性不包括 ACME 自动证书管理或 Caddy 的插件生态系统，而这些对生产使用至关重要。性能声明基于使用 io_uring 进行异步 I/O 的基准测试。

hackernews · losfair · Jun 14, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48527145)

**背景**: Zeroserve 是一个零配置、高性能的 HTTPS 服务器，使用 eBPF 和 io_uring 实现低开销。io_uring 是 Linux 内核异步 I/O 接口，可减少系统调用开销。Caddy 是一种流行的网络服务器，以其通过 ACME 实现的自动 HTTPS 和插件架构而闻名。该新闻描述了使 Zeroserve 接受 Caddy 配置文件的努力，但存在重大遗漏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://su3.io/posts/introducing-zeroserve">zeroserve : a zero -config web server you can script with eBPF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员批评缺乏 ACME 和插件支持，称其为‘致命缺陷’。还有用户质疑在网络服务器中使用 io_uring 的安全性，提到了网络安全方面的担忧。

**标签**: `#web server`, `#performance`, `#Caddy`, `#zeroserve`, `#io_uring`

---