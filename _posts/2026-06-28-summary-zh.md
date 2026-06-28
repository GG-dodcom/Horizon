---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> From 65 items, 7 important content pieces were selected

---

1. [患者使用 Claude Code 获取 MRI 第二诊断意见](#item-1) ⭐️ 8.7/10
2. [GLM 5.2 在安全基准测试中击败 Claude](#item-2) ⭐️ 8.3/10
3. [OpenAI Codex Issue #2847：敏感文件排除需求](#item-3) ⭐️ 8.3/10
4. [布朗大学教授谴责考试中大规模 AI 作弊](#item-4) ⭐️ 7.8/10
5. [AI 促使数学家重新思考工作的意义](#item-5) ⭐️ 7.2/10
6. [LiteLLM v1.91.0-rc.1 增加 Docker 镜像签名](#item-6) ⭐️ 7.1/10
7. [波兰字母变音符号在软件中消失之谜](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [患者使用 Claude Code 获取 MRI 第二诊断意见](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.7/10

一名软件开发者使用 AI 编程代理 Claude Code 分析自己的肩部 MRI，获取第二诊断意见，并在一篇详细博文中记录了整个过程。 这一案例凸显了大语言模型与个人医疗保健日益紧密的交集，引发了关于 AI 可靠性、信任度以及专业放射科医生角色的关键问题。 Claude Code 主要设计用于软件开发任务，而非医学影像；社区中的放射科医生指出，正确评估需要完整的 3D MRI 数据集，而非仅凭截图。

hackernews · engmarketer · Jun 28, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是由 Anthropic 开发的 AI 编程代理，使用宪法 AI 技术训练以遵循伦理准则。尽管存在经过 FDA 批准的放射学第二诊断 AI 解决方案（例如 Braid Health），但这些方案通常将 AI 与人类放射科医生相结合；单独使用通用 AI 进行医学诊断并非标准做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://braid.health/www/page/same-day-radiology-second-opinion">Braid Health | AI Radiology Second Opinions & Ask AI</a></li>

</ul>
</details>

**社区讨论**: 放射科医生强调需要完整的影像数据，并警告不要过度依赖 AI。一些评论者赞赏这种质疑医疗决策的赋权感，而另一些人则分享了误诊的个人经历，凸显了医疗系统中的问题。

**标签**: `#AI`, `#healthcare`, `#radiology`, `#LLM`, `#personal experience`

---

<a id="item-2"></a>
## [GLM 5.2 在安全基准测试中击败 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.3/10

Semgrep 的基准测试显示，GLM 5.2 模型在网络安全漏洞检测方面优于 Claude，并且每个漏洞的发现成本更低。 这表明开源 LLM 在专业安全任务上可以超越专有模型，可能降低安全团队的成本，并挑战封闭模型的统治地位。 据报道，GLM 5.2 是一个 753B 参数的模型（尽管有些来源列为 376.7B），在 Semgrep 的测试中，它以每个漏洞约 0.17 美元的成本实现了比 Claude 更高的漏洞发现率。

hackernews · jms703 · Jun 28, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: Semgrep 是一款开源静态代码分析工具，用于发现安全漏洞并执行编码标准。该基准测试评估了 LLM 识别真实世界网络安全漏洞的能力。GLM 5.2 是 zai-org 最近发布的开源 LLM，针对编码和长周期任务进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ollama.com/library/glm-5.2">GLM - 5 . 2 is Z.ai’s flagship model for the era of long-horizon tasks.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semgrep">Semgrep - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，GLM 5.2 是日常编程和安全任务的可靠主力模型，但也有人指出，将模型与 Claude Code（一个代理工具）进行比较可能具有误导性。其他人报告称，基准测试的数字与他们自己的经验相比显得偏低。

**标签**: `#AI`, `#LLM`, `#benchmarks`, `#GLM`, `#Claude`

---

<a id="item-3"></a>
## [OpenAI Codex Issue #2847：敏感文件排除需求](https://github.com/openai/codex/issues/2847) ⭐️ 8.3/10

GitHub 上的一个 issue（openai/codex#2847）讨论了为 OpenAI Codex 添加敏感文件排除功能的需求，社区成员提出了使用 chmod 限制文件访问或容器化运行 Codex 等变通方案。 该问题凸显了 AI 编程代理中的一个关键安全漏洞，敏感数据可能通过工具输出或模型行为意外泄露。适当的文件排除功能对于企业采用和安全使用 AI 辅助开发至关重要。 社区评论指出，选择加入（如沙箱化）的方法比选择退出的黑名单更可靠，而且由于 LLM 的不可预测性，仅靠该功能无法保证安全。一些用户已经构建了内部的沙箱解决方案。

hackernews · pikseladam · Jun 28, 12:27 · [社区讨论](https://news.ycombinator.com/item?id=48706714)

**背景**: Chmod 是一个 Unix 命令，用于更改文件权限以控制读写执行访问。在计算中，容器化将应用程序隔离在称为容器的用户空间环境中，限制它们对主机资源的访问。这些是系统级的安全措施，可以防止 AI 代理访问敏感文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chmod">Chmod</a></li>
<li><a href="https://en.wikipedia.org/wiki/Containerization_(computing)">Containerization (computing) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：一些人认为选择退出的黑名单不够充分甚至危险，会带来虚假的安全感；另一些人则认为 chmod 和容器等系统级工具已经解决了问题，任何在代理层面的强制措施都是徒劳的。几位用户分享了自己的沙箱实现。

**标签**: `#AI`, `#security`, `#codex`, `#LLM`, `#privacy`

---

<a id="item-4"></a>
## [布朗大学教授谴责考试中大规模 AI 作弊](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 7.8/10

布朗大学一位经济学教授（博弈论专家）发现，他的课堂上大多数学生在一场开卷闭卷考试中使用了 AI 作弊，他认为这是其 34 年教学生涯中最严重的学术诚信违规事件。 这一事件凸显了 AI 对传统开卷考试日益严重的挑战，可能加速向现场手写考试的转变。它也揭示了一个博弈论困境：当其他学生很可能使用 AI 时，选择使用 AI 是理性选择。 这场考试是开卷闭卷形式，教授原以为可以出更难的问题。尽管他是博弈论专家，但他未能预料到作弊规模之大；许多学生提交的答案明显是由大型语言模型生成的。

hackernews · geox · Jun 28, 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48708991)

**背景**: 大型语言模型（LLMs）如 GPT-4 能生成类似人类的文本，使得在笔试中检测 AI 生成的答案变得困难。博弈论——这位教授的专业领域——预测，当所有学生都能使用 AI 时，使用 AI 成为占优策略，即使个体诚信度很高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s40979-024-00154-7">Integrity games: an online teaching tool on academic ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为 AI 使得开卷考试难以为继，有人指出学生使用 AI 是博弈论下的必然结果。其他人对精英学府缺乏诚信表示失望，还有一些人批评开卷闭卷形式本身就自相矛盾。

**标签**: `#AI`, `#education`, `#academic integrity`, `#LLMs`, `#game theory`

---

<a id="item-5"></a>
## [AI 促使数学家重新思考工作的意义](https://www.solidot.org/story?sid=84695) ⭐️ 7.2/10

陶哲轩等人设想未来人类与 AI 协作解决复杂数学问题，AI 处理技术性工作而人类专注于创造性部分。 这一转变可能改变数学实践方式，实现更大规模的协作并加速发现，同时迫使数学家重新评估人类直觉和创造力的价值。 AI 在短短几年内从仅能重复模式的“随机鹦鹉”演变为高级推理机器。陶哲轩已在自身工作中实践这一协作理念。

rss · Solidot · Jun 27, 16:02

**背景**: “随机鹦鹉”一词出自 2021 年一篇论文，用以批评大语言模型只是模仿语言而不理解含义。陶哲轩的“大数学”概念设想人类与 AI 在大规模问题上进行去中心化协作，其基础可追溯至四色定理等早期计算机辅助证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_parrot">Stochastic parrot</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Terence Tao`, `#LLM`, `#scientific impact`

---

<a id="item-6"></a>
## [LiteLLM v1.91.0-rc.1 增加 Docker 镜像签名](https://github.com/BerriAI/litellm/releases/tag/v1.91.0-rc.1) ⭐️ 7.1/10

BerriAI 发布了 LiteLLM v1.91.0-rc.1，引入了基于 cosign 的 Docker 镜像签名验证以增强供应链安全，同时包含多个错误修复和新功能，如 MCP OAuth 令牌基础和改进的 Prometheus 指标。 此版本通过支持对镜像真实性进行加密验证，增强了通过 Docker 部署 LiteLLM 的用户的安全性，这对于防止供应链攻击至关重要。额外的监控和护栏改进也有助于生产环境中 AI 网关的可靠性和可观测性。 推荐的验证方法使用固定的提交哈希（0112e53）以确保密钥绑定不可变，同时也提供了基于标签的选项以方便使用。此版本包含超过 15 项更改，涵盖护栏、MCP、网络搜索、成本跟踪和代理性能。

github · github-actions[bot] · Jun 28, 03:46

**背景**: LiteLLM 是一个开源 AI 网关，为超过 100 个大语言模型提供统一的 API 接口，简化了模型访问、成本跟踪和故障转移管理。Cosign 是 Sigstore 项目的一部分，是一种用于签名和验证容器镜像及二进制文件的工具，有助于确保软件供应链的完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://docs.docker.com/dhi/core-concepts/signatures/">Code signing | Docker Docs</a></li>
<li><a href="https://www.litellm.ai/">LiteLLM</a></li>

</ul>
</details>

**标签**: `#LiteLLM`, `#Docker`, `#cosign`, `#security`, `#release-notes`

---

<a id="item-7"></a>
## [波兰字母变音符号在软件中消失之谜](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/) ⭐️ 7.0/10

本文探讨了波兰变音字母（如 ś、ć、ń）在软件中经常丢失或变形的原因，从 20 世纪 60 年代 ASCII 的限制到现代浏览器键盘快捷键和 Unicode 归一化差异，追溯了这一问题的历史和技术根源。 这很重要，因为数百万波兰语使用者在日常输入中遇到问题，而且这一问题体现了国际化与输入法兼容性方面的更广泛挑战，影响了许多使用变音符号的语言。 在波兰语字母中，'ł'在 Unicode NFD 归一化下不会分解，而其他 8 个字母则分解为基字加组合符号。浏览器快捷键（如 Ctrl+Alt+S 对应'ś'）经常拦截用户本意的 AltGr 组合，且没有简单的浏览器 API 来检测此类冲突。

hackernews · colinprince · Jun 28, 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48706814)

**背景**: 波兰字母使用拉丁字母并附加变音符号（ą, ć, ę, ł, ń, ó, ś, ź, ż）。早期计算机系统常限于 ASCII 字符集，缺少这些字母。Unicode 引入了归一化形式（NFC、NFD）来处理等效序列，但软件处理方式各不相同。现代浏览器和应用程序有时会劫持原本用于输入这些变音符号的键盘组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unicode_normalization">Unicode normalization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polish_alphabet">Polish alphabet - Wikipedia</a></li>
<li><a href="https://accentcodes.com/languages/polish-alt-codes.html">Polish ALT Codes — ą ć ę ł ń ś ź ż (Unicode Alt+X Method)</a></li>

</ul>
</details>

**社区讨论**: 评论者补充了更多细节：有人指出波兰语使用拉丁字母促进了其向西方的文化靠拢；另有人强调浏览器缺乏检查按键组合的简单方式，导致开发者需要自行变通。一位用户报告微软 Copilot 在 Windows 上拦截'Ć'输入，另一位分享了一个有趣的事实：'ł'在 Unicode 归一化中保持完整，导致 SQLite 的 remove_diacritics 分词器无法正确处理波兰语文本。

**标签**: `#Polish diacritics`, `#Unicode`, `#software localization`, `#keyboard shortcuts`, `#historical computing`

---