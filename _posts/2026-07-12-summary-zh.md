---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 37 items, 9 important content pieces were selected

---

1. [陶哲轩探索用 LLM 编码代理做应用](#item-1) ⭐️ 9.2/10
2. [George Hotz：我爱 LLM，但厌恶炒作](#item-2) ⭐️ 8.5/10
3. [Claude Code 开销 33k tokens，OpenCode 仅 7k](#item-3) ⭐️ 8.2/10
4. [AI 代码生成或贬低开发者技能，Fabien Sanglard 发出警告](#item-4) ⭐️ 8.1/10
5. [带状疱疹疫苗或降低痴呆风险](#item-5) ⭐️ 7.5/10
6. [Chromium 148 的 Math.tanh 可指纹识别操作系统](#item-6) ⭐️ 7.3/10
7. [LiteLLM v1.92.0 新增使用 Cosign 验证 Docker 镜像签名](#item-7) ⭐️ 7.2/10
8. [LiteLLM v1.91.2 增加 Cosign Docker 镜像验证](#item-8) ⭐️ 7.0/10
9. [Ghostel.el：基于 libghostty 的 Emacs 终端模拟器](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [陶哲轩探索用 LLM 编码代理做应用](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 9.2/10

菲尔兹奖得主、数学家陶哲轩分享了他使用 LLM 编码代理构建可视化应用和交互式程序的经历，既展示了其潜力也指出了当前局限。 这表明 AI 编码代理能让非程序员快速构建软件原型，尤其是领域特定的可视化工具，同时也强调对 LLM 生成的代码在关键任务上仍需谨慎。 陶哲轩指出这些由 LLM 编写的补充内容并非论文的核心部分，因此使用引导式交互的风险可以接受，但他警告不要完全信任此类代理处理核心工作。

hackernews · subset · Jul 12, 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: LLM 编码代理是利用大型语言模型根据自然语言指令生成或辅助编写代码的 AI 系统。陶哲轩是著名数学家，常在研究中运用计算工具。这篇帖子反映了研究人员使用 AI 加速科学工作中的原型设计和可视化的增长趋势。

**社区讨论**: 评论者称赞了生产力提升，有人提到用 Claude 构建了一个 8 位计算机模拟器。也有人幽默地将陶哲轩比作米其林大厨发现微波炉晚餐，而一条平衡的评论同意 LLM 工具适合某些任务但不宜完全信任。

**标签**: `#AI`, `#coding agents`, `#LLM`, `#Terry Tao`, `#software development`

---

<a id="item-2"></a>
## [George Hotz：我爱 LLM，但厌恶炒作](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.5/10

George Hotz 发表了一篇名为《我爱 LLM，但厌恶炒作》的博客文章，他在文中认可大型语言模型的实用性，同时批评了前沿 AI 实验室的过度炒作和高估值。 这篇文章挑战了前沿 AI 实验室将捕获 AI 创造的大部分价值的主流说法，认为生产力提升的收益实际上将主要由用户和开源社区获得。这对 AI 投资以及专有模型可持续性具有重要影响。 Hotz 认为，虽然 AI 将创造巨大价值，但前沿实验室可能无法捕获这些价值，因为开源模型和用户驱动的改编广泛地分散了收益。评论者指出，LLM 驱动的生产力提升导致定制一次性软件激增，减少了向上游贡献的动力。

hackernews · therepanic · Jul 12, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 大型语言模型（如 GPT-4 和 LLaMA）在文本生成和编程方面展现出卓越能力，导致 OpenAI 和 Anthropic 等公司获得高估值。'前沿实验室'指领先的 AI 研究机构。'价值捕获'概念描述的是技术创造者还是用户获得经济收益。

**社区讨论**: HN 评论者普遍赞同 Hotz 关于价值捕获的论点，许多人分享了使用 LLM 构建定制软件的个人体验。还有讨论指出，由于 LLM 辅助使分叉更容易，开源上游贡献正在减少。

**标签**: `#AI`, `#LLM`, `#hype`, `#valuation`, `#open source`

---

<a id="item-3"></a>
## [Claude Code 开销 33k tokens，OpenCode 仅 7k](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.2/10

一项系统性比较显示，Claude Code 在读取用户提示前会消耗约 33,000 个 tokens 用于系统提示和缓存设置，而 OpenCode 仅使用约 7,000 个 tokens，表明两者在 token 效率上存在显著差异。 这一点很重要，因为对于代理式编码工具的重度用户来说，token 开销直接转化为成本，五倍的差异会显著影响运营预算和工具选择。 测量方法是在工具与 Anthropic 端点之间插入日志记录，捕获所有请求和用量。文中提到的注意事项是，该比较可能未能体现定性任务性能，作者计划更新更深入的任务分析。

hackernews · systima · Jul 12, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: Claude Code 是 Anthropic 的代理式编码工具，可以读取和修改代码库、运行测试和管理提交。OpenCode 是一个开源的 AI 编码代理，提供类似功能。“harness token usage”指的是在实际处理用户提示之前，系统提示和缓存机制所消耗的开销 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>
<li><a href="https://opencode.ai/download">OpenCode | Download</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Claude Code 中的子代理可能过度消耗 token，有人怀疑高开销是故意的以推动订阅收入。作者承认了仅测量 token 数量而不考虑任务效率的观点合理，并计划添加定性比较。

**标签**: `#AI`, `#LLM`, `#token optimization`, `#coding agents`, `#Claude Code`, `#OpenCode`

---

<a id="item-4"></a>
## [AI 代码生成或贬低开发者技能，Fabien Sanglard 发出警告](https://fabiensanglard.net/extinct/index.html) ⭐️ 8.1/10

Fabien Sanglard 发表了一篇文章，将 AI 代码生成与电影中的 CGI 进行类比，认为尽管 LLM 提高了生产力，但开发者必须优先考虑代码的可读性和理解，以避免技能贬值。 这很重要，因为它挑战了 LLM 只是提高开发者生产力的主流说法，突出了技能流失和代码质量等潜在负面影响，这些可能影响软件的长期可维护性。 Sanglard 认为，拒绝使用 LLM 的开发者在产出上会落后，但他强调需要对拉取请求进行迭代以达到手写代码的质量。他还指出，使用 LLM 编写测试变得更容易，这有利于大型重构。

hackernews · zdw · Jul 12, 15:17 · [社区讨论](https://news.ycombinator.com/item?id=48881830)

**背景**: 大型语言模型（LLM）是在海量文本数据上训练的神经网络，能够生成包括代码在内的人类风格文本。像 GitHub Copilot 这样的 AI 代码生成工具使用 LLM 来建议代码片段，提高了开发者生产力。然而，存在对代码质量和开发者在不理解的情况下依赖生成代码的担忧。电影中的 CGI 同样提升了视觉效果，但导致了实际特效艺术家的贬值，因此 Sanglard 进行了类比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者对产出量的论点表示怀疑，指出他们从未以产出量被评估。一些人扩展了 CGI 类比，指出艺术家的贬值导致了向实际特效的回归。其他人同意测试至关重要，但警告 AI 生成的测试可能复制代码的缺陷。

**标签**: `#AI`, `#LLM`, `#software engineering`, `#code generation`, `#productivity`

---

<a id="item-5"></a>
## [带状疱疹疫苗或降低痴呆风险](https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain) ⭐️ 7.5/10

英国一项利用年龄资格截止点的自然实验表明，接种带状疱疹疫苗后七年内痴呆诊断的概率降低。 如果因果关系成立，这将提供一种安全且广泛可用的干预手段来延缓或预防痴呆，影响数百万有阿尔茨海默病及其他痴呆风险的人群。 该研究利用了这样一项政策：略低于年龄截止点的人有资格接种疫苗，而略高于截止点的人则没有，这模拟了随机试验。批评者认为，这种关联可能源于接种者因较少住院而减少了偶然的痴呆诊断。

hackernews · saikatsg · Jul 12, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48881874)

**背景**: 带状疱疹是由水痘-带状疱疹病毒再激活引起的疼痛性皮疹。重组带状疱疹疫苗（Shingrix）推荐用于 50 岁及以上成人。先前的观察性研究表明接种疫苗与较低的痴呆风险之间存在关联，但容易受到混杂因素的影响。像基于年龄截止点的自然实验提供了更强的因果证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-08800-x">A natural experiment on the effect of herpes zoster vaccination on dementia | Nature</a></li>
<li><a href="https://www.cdc.gov/shingles/vaccines/index.html">Shingles Vaccination | Shingles (Herpes Zoster) | CDC</a></li>
<li><a href="https://www.cell.com/cell/fulltext/S0092-8674(25)01256-5">The effect of shingles vaccination at different stages of the dementia disease course: Cell</a></li>

</ul>
</details>

**社区讨论**: 一些评论者认为年龄截止点图表令人信服，并考虑自费接种疫苗。另一些人警告说该发现可能是虚假的，指出接种者住院次数减少可能导致痴呆诊断减少。这场辩论反映了健康的科学质疑精神。

**标签**: `#vaccines`, `#dementia`, `#health research`, `#shingles`

---

<a id="item-6"></a>
## [Chromium 148 的 Math.tanh 可指纹识别操作系统](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 7.3/10

一篇博客文章揭示，在 Chromium 148 中，由于不同操作系统使用不同的数学库（如 Apple 的库和 glibc），Math.tanh 的实现存在差异，这使得通过处理非规格化浮点数可以指纹识别操作系统。 该技术为浏览器指纹识别增加了一种微妙的新途径，可与 Canvas 或 WebGL 等传统方法结合使用，可能增加用户追踪的难度且不易缓解。 指纹识别依赖于非规格化浮点数，不同数学库对特定输入的 Math.tanh 可能产生微小差异；但社区评论指出，新版本 glibc 使用了 CORE-MATH 的正确舍入 tanh，可能会降低可靠性。

hackernews · joahnn_s · Jul 12, 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别收集设备或浏览器的微妙特征以识别用户。非规格化浮点数是接近零的极小数字，某些系统对其处理方式不同，从而在不同平台上产生可检测的差异。Math.tanh 是计算双曲正切的 JavaScript 函数，其实现因操作系统底层数学库不同而可能变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Subnormal_number">Subnormal number - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论指出该文章可能是 AI 生成的，并过于简化了技术；有人认为它只能指纹识别浏览器版本范围，而非可靠的操作系统。其他人则注意到使用正确舍入函数的新版 glibc 可能改变行为，并暗示该方法主要服务于抓取行业而非用户保护。

**标签**: `#fingerprinting`, `#browser security`, `#Math.tanh`, `#Chromium`, `#OS detection`

---

<a id="item-7"></a>
## [LiteLLM v1.92.0 新增使用 Cosign 验证 Docker 镜像签名](https://github.com/BerriAI/litellm/releases/tag/v1.92.0) ⭐️ 7.2/10

BerriAI 发布了 LiteLLM v1.92.0，新增了使用 cosign 验证 Docker 镜像签名的功能，提供了两种方法：使用固定提交哈希（推荐）和使用发布标签。 这增强了通过 Docker 部署 LiteLLM 的用户的供应链安全性，允许他们在使用前验证镜像的真实性和完整性。这符合容器安全的最佳实践。 签名密钥在提交 0112e53 中引入，可公开访问。用户可以运行 cosign verify 命令，使用指向该提交或发布标签 v1.92.0 的公钥 URL。

github · github-actions[bot] · Jul 12, 01:55

**背景**: Cosign 是 Sigstore 项目中的一个工具，用于对容器镜像等软件工件进行签名和验证。Docker 镜像签名有助于防止篡改，确保镜像来自可信来源。LiteLLM 是一个开源代理，用于向各种 LLM 提供商发起调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://grigorkh.medium.com/securing-docker-images-with-sigstore-cosign-208a19801b72">Securing Docker Images with Sigstore Cosign | by Grigor Khachatryan | Medium</a></li>

</ul>
</details>

**标签**: `#litellm`, `#Docker`, `#cosign`, `#security`, `#AI infrastructure`

---

<a id="item-8"></a>
## [LiteLLM v1.91.2 增加 Cosign Docker 镜像验证](https://github.com/BerriAI/litellm/releases/tag/v1.91.2) ⭐️ 7.0/10

LiteLLM v1.91.2 引入了使用 cosign 进行 Docker 镜像签名验证的功能，并提供了使用固定提交哈希或发布标签验证镜像的说明。 这增强了 LiteLLM 用户的供应链安全性，确保从注册表拉取的 Docker 镜像的完整性和真实性。 签名密钥在提交 0112e53 中引入，验证可以通过不可变的提交哈希（推荐）或通过受保护的发布标签（方便）进行。

github · github-actions[bot] · Jul 11, 06:21

**背景**: Cosign 是 Sigstore 提供的一个用于代码签名和透明度的工具，支持容器镜像的签名和验证。Docker 镜像签名允许用户验证镜像自发布者签名后未被篡改。LiteLLM 是一个用于管理 LLM API 调用的代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers ...</a></li>
<li><a href="https://docs.docker.com/dhi/how-to/verify/">Verify a Docker Hardened Image or chart | Docker Docs</a></li>

</ul>
</details>

**标签**: `#litellm`, `#Docker`, `#cosign`, `#security`, `#LLM`

---

<a id="item-9"></a>
## [Ghostel.el：基于 libghostty 的 Emacs 终端模拟器](https://dakra.github.io/ghostel/) ⭐️ 7.0/10

Ghostel 是一款基于 libghostty-vt 的 Emacs 终端模拟器，提供了比 vterm 和 eat 更丰富、更快且输入处理更可靠的替代方案。 它为 Emacs 用户提供了更快、更可靠的终端体验，解决了 vterm 等现有方案的常见问题，有望改善 Emacs 开发者的工作流程。 Ghostel 基于终端模拟 C 库 libghostty 构建，支持多种输入模式，以解决 Emacs 与内嵌终端之间的键盘所有权冲突。

hackernews · signa11 · Jul 12, 08:52 · [社区讨论](https://news.ycombinator.com/item?id=48879504)

**背景**: vterm 和 eat 等 Emacs 终端模拟器在 Emacs 内部嵌入终端，但在性能和输入模式切换方面存在挑战。libghostty 是为独立终端模拟器 Ghostty 开发的终端核心库。Ghostel 利用该库实现了更好的性能和可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://webteractive.co/blog/ghostty-and-libghostty-the-terminal-core-quietly-reshaping-the-ecosystem">Ghostty and libghostty : The Terminal Core Quietly... — Webteractive</a></li>

</ul>
</details>

**社区讨论**: 维护者介绍了 Ghostel 并提供了功能对比。用户称赞其比 vterm 更快、更可靠，但也指出一些粗糙之处，如终端清除问题和偶尔的卡死。有评论者建议标题应明确提及 Emacs。

**标签**: `#Emacs`, `#terminal emulator`, `#open source`, `#development tool`

---