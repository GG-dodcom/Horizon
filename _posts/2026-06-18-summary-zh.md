---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 116 items, 26 important content pieces were selected

---

1. [MolmoMotion：语言引导的 3D 运动预测](#item-1) ⭐️ 9.2/10
2. [GLM-5.2：拥有百万上下文窗口的开源 MoE 模型](#item-2) ⭐️ 9.0/10
3. [代理资源发现规范发布](#item-3) ⭐️ 9.0/10
4. [借助 Strands Agents 和 LeRobot 将 Hugging Face 模型部署到机器人硬件](#item-4) ⭐️ 8.9/10
5. [AI 化学家改进药物化学反应](#item-5) ⭐️ 8.8/10
6. [安杰尼·米达谈 AI 投资与 AMP 策略](#item-6) ⭐️ 8.8/10
7. [超越 LoRA：探索更优微调方法](#item-7) ⭐️ 8.7/10
8. [发现一万个 GitHub 仓库分发木马恶意软件](#item-8) ⭐️ 8.6/10
9. [新站点跨多个 LLM 检查姓名识别](#item-9) ⭐️ 8.4/10
10. [开源模型智能体能力基准测试](#item-10) ⭐️ 8.4/10
11. [Vercel AI SDK Workflow 补丁修复工具审批转发问题](#item-11) ⭐️ 8.3/10
12. [Git 忽略文件不止.gitignore](#item-12) ⭐️ 8.3/10
13. [Noam Shazeer 加入 OpenAI](#item-13) ⭐️ 8.1/10
14. [康奈尔大学 CS 6120 高级编译器自修课程](#item-14) ⭐️ 8.0/10
15. [MosaicLeaks：研究 Agent 的隐私风险](#item-15) ⭐️ 8.0/10
16. [强迫同意使 Elkjop 被罚 180 万欧元](#item-16) ⭐️ 7.9/10
17. [网站提交目录的聚合器引发 HN 讨论](#item-17) ⭐️ 7.8/10
18. [OpenAI 推出支出控制与使用分析功能](#item-18) ⭐️ 7.5/10
19. [AI 推理模型发现 18 个新罕见病诊断](#item-19) ⭐️ 7.5/10
20. [OpenAI 推出 LifeSciBench 评估生命科学 AI](#item-20) ⭐️ 7.5/10
21. [医院和大学以极低成本重新利用药物](#item-21) ⭐️ 7.2/10
22. [自动驾驶实验室：材料科学的新护城河](#item-22) ⭐️ 7.2/10
23. [W Social：欧洲数字主权的作秀](#item-23) ⭐️ 7.1/10
24. [Gerrymandle：每日拼图游戏教你理解选区划分](#item-24) ⭐️ 7.0/10
25. [AI 时代电商访谈：与 Michael Morton 对话](#item-25) ⭐️ 7.0/10
26. [本·汤普森评 Fable、越狱问题与 SpaceX 收购 Cursor](#item-26) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MolmoMotion：语言引导的 3D 运动预测](https://huggingface.co/blog/allenai/molmomotion) ⭐️ 9.2/10

Allen AI 发布了 MolmoMotion，这是一个开源的语言引导 3D 运动预测模型，能够根据自然语言指令预测物体的未来点轨迹。该模型在新的 PointMotionBench 基准上取得了最先进的结果。 这项工作将视觉语言模型扩展到时间和空间推理，为机器人和动画提供了更直观的控制。通过融入语言，运动预测变得对非专家也易于使用，并可通过高级指令进行引导。 MolmoMotion 在 MolmoMotion-1M 数据集上预训练，并在 PointMotionBench 上评估。它根据语言指令预测世界坐标系中的 3D 点轨迹，显著优于现有的运动预测方法。

rss · Hugging Face Blog · Jun 17, 15:26

**背景**: 3D 运动预测对于自动驾驶、机器人和视频生成等应用至关重要。传统方法依赖过去的运动历史，而语言引导的方法能够实现对预期动作的语义理解。MolmoMotion 建立在 Molmo 多模态模型家族之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allenai.org/blog/molmo-motion">MolmoMotion: Language-guided 3D motion forecasting | Ai2</a></li>
<li><a href="https://arxiv.org/html/2606.18558v1">MolmoMotion Forecasting Point Trajectories in 3D with ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#3D motion forecasting`, `#language-guided`, `#deep learning`, `#Hugging Face`

---

<a id="item-2"></a>
## [GLM-5.2：拥有百万上下文窗口的开源 MoE 模型](https://huggingface.co/blog/zai-org/glm-52-blog) ⭐️ 9.0/10

中国 AI 实验室 Z.ai 发布了 GLM-5.2，这是一个 753B 参数的混合专家模型，具有 40 个活跃参数，采用 MIT 许可证并开放权重。 GLM-5.2 在 Artificial Analysis Intelligence Index v4.1 中位列开源模型第一，并在 Code Arena WebDev 排名第二，成为长时任务（如编程与复杂推理）的有力竞争者。 该模型拥有 100 万 token 的上下文窗口（从 GLM-5.1 的 20 万提升而来），但仅支持文本输入，且每个任务输出 token 数（43k）高于同类模型，导致推理成本更高。

rss · Hugging Face Blog · Jun 17, 09:01

**背景**: 混合专家模型（MoE）是一种机器学习技术，将模型划分为多个称为专家的专门子模型，每个专家处理不同的输入模式。这使得在保持推理成本可控的同时扩展模型规模成为可能，因为每次前向传播仅激活部分专家。GLM-5.2 采用了 MoE，在 753B 参数中只有 40 个活跃参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**标签**: `#LLM`, `#GLM`, `#long-horizon tasks`, `#AI research`, `#Hugging Face`

---

<a id="item-3"></a>
## [代理资源发现规范发布](https://huggingface.co/blog/agentic-resource-discovery-launch) ⭐️ 9.0/10

ARD 通过提供通用的发现层，解决了代理与工具互操作性的关键问题，有望加速自主 AI 代理在不同框架和平台上的应用。 该规范不规定资源如何调用，仅定义发布、发现和验证资源的方式。资源可以是代理、MCP 服务器、技能、API 或工作流，客户端使用原生协议进行调用。

rss · Hugging Face Blog · Jun 17, 00:00

**背景**: 目前，AI 代理通常依赖硬编码的工具列表或手动配置，限制了可扩展性。ARD 采用类似 DNS 的注册和发现机制，允许动态选择最相关的资源来执行给定任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/">Announcing the Agentic Resource Discovery specification</a></li>
<li><a href="https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/">Introducing the Agentic Resource Discovery specification ...</a></li>
<li><a href="https://agenticresourcediscovery.io/">Agentic Resource Discovery Specification ¶</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#resource discovery`, `#LLM tooling`, `#Hugging Face`

---

<a id="item-4"></a>
## [借助 Strands Agents 和 LeRobot 将 Hugging Face 模型部署到机器人硬件](https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware) ⭐️ 8.9/10

Hugging Face 宣布了一种工作流，通过 Strands Agents 和 LeRobot 将 AI 模型从其 Hub 部署到物理机器人硬件上，实现了从 AI 到机器人的无缝集成。 这降低了机器人开发者直接在硬件上利用最先进 AI 模型的门槛，加速了智能机器人的原型设计和实际部署。 Strands Agents 是一个开源、模型驱动的 AI 代理构建框架，而 LeRobot 是 Hugging Face 用于机器人深度学习的库，两者结合可实现最低代码的模型部署。

rss · Hugging Face Blog · Jun 17, 10:18

**背景**: Strands Agents（原 AWS Strands Agents SDK）是一个轻量级框架，用于创建能够自主推理和行动的 AI 代理。LeRobot 是 Hugging Face 的开源库，提供用于深度学习机器人实验的工具和兼容硬件，例如六自由度机械臂。两者共同弥合了 AI 模型开发与物理机器人控制之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Strands_Agents">Strands Agents</a></li>
<li><a href="https://strandsagents.com/">Strands Agents — Open Source AI Agent SDK for Python & TypeScript</a></li>
<li><a href="https://grokipedia.com/page/LeRobot">LeRobot</a></li>

</ul>
</details>

**标签**: `#AI`, `#Robotics`, `#Hugging Face`, `#LeRobot`, `#Agent Systems`

---

<a id="item-5"></a>
## [AI 化学家改进药物化学反应](https://openai.com/index/ai-chemist-improves-reaction) ⭐️ 8.8/10

OpenAI 与 Molecule.one 展示了一款近乎自主的 AI 化学家，它利用 GPT-5.4 显著改进了药物化学中的一项关键反应，展示了大语言模型在自主科学研究中的潜力。 这一突破表明 AI 可以自主优化复杂的化学反应，有望加速药物发现过程，并减少制药研究中对手动实验的依赖。 该系统将 GPT-5.4 与 Molecule.one 的自主实验室平台相结合，利用模型的计算机使用和推理能力来自主设计并执行实验，无需人类干预。

rss · OpenAI Blog · Jun 17, 10:00

**背景**: GPT-5.4 是 OpenAI 于 2026 年 3 月发布的大型语言模型，具备最先进的编码、计算机使用能力和 100 万 token 的上下文窗口。自主 AI 化学家将大语言模型的推理能力与机器人实验设备相结合，用于规划、执行和分析实验，旨在自动化化学研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-4/">Introducing GPT‑5.4 - OpenAI</a></li>
<li><a href="https://molecule.one/">molecule.one - Chemistry AI for Autonomous Discovery</a></li>

</ul>
</details>

**标签**: `#AI`, `#medicinal chemistry`, `#autonomous systems`, `#GPT-5.4`, `#reaction optimization`

---

<a id="item-6"></a>
## [安杰尼·米达谈 AI 投资与 AMP 策略](https://www.latent.space/p/anj) ⭐️ 8.8/10

投资者安杰尼·米达分享了他从新加坡起步到领投 Anthropic、Mistral、Black Forest Labs 和 Periodic Labs 等 AI 初创公司的经历，并阐述了他的 AMP 秘密计划。 这次访谈提供了顶级 AI 风险投资家的投资策略独特见解，为创始人和投资者在快速变化的 AI 领域导航提供了宝贵视角。 米达领投了 Anthropic（Claude）、Mistral（LLM）、Black Forest Labs（Flux 文生图模型）和 Periodic Labs（用于自主实验室的 AI 科学家）等公司的融资轮次。AMP 策略可能指他在 Andreessen Horowitz 的投资方法。

rss · Latent Space · Jun 18, 17:30

**背景**: 安杰尼·米达是 Andreessen Horowitz（a16z）的普通合伙人，专注于 AI 投资。他曾共同创立 AI 平台公司 MosaicML，后被 Databricks 收购。他的投资组合包括多家开发基础模型和 AI 驱动的科学研究工具的知名 AI 初创公司。访谈涵盖了他的个人经历及其公司的投资理念，概括为'AMP'策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Black_Forest_Labs">Black Forest Labs</a></li>
<li><a href="https://periodic.com/">Periodic Labs</a></li>
<li><a href="https://a16z.com/announcement/investing-in-periodic-labs/">Investing in Periodic Labs | Andreessen Horowitz - a16z.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#venture capital`, `#startups`, `#LLM`, `#investment`

---

<a id="item-7"></a>
## [超越 LoRA：探索更优微调方法](https://huggingface.co/blog/peft-beyond-lora) ⭐️ 8.7/10

Hugging Face 发布了一篇技术博文，比较了 LoRA 之外的其他参数高效微调方法（如 adapter layers、prefix tuning 和 prompt tuning），并评估了它们在多种任务上的表现。 这项分析帮助从业者为大语言模型选择最有效的微调方法，在效率和性能之间取得平衡，这对在生产环境中部署 LLM 至关重要。 该比较涵盖了 AdaLoRA、LoRA 和全参数微调等方法，并提供了内存使用、训练时间和下游任务准确率等指标，表明有时更简单的方法可以超越 LoRA。

rss · Hugging Face Blog · Jun 18, 00:00

**背景**: 参数高效微调（PEFT）技术通过仅更新少量参数来适配大型预训练模型，从而降低计算成本。LoRA 于 2021 年提出，通过在模型层中注入可训练的低秩矩阵来实现这一目标，成为一种流行的方法。然而，其他 PEFT 方法（如 prompt tuning 和 adapter layers）提供了不同的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA">LoRA</a></li>
<li><a href="https://grokipedia.com/page/Parameter-Efficient_Fine-Tuning_PEFT">Parameter-Efficient Fine-Tuning (PEFT)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)">Fine - tuning (deep learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#LoRA`, `#PEFT`, `#LLM`, `#efficient fine-tuning`

---

<a id="item-8"></a>
## [发现一万个 GitHub 仓库分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 8.6/10

一项调查发现超过一万个 GitHub 仓库正在分发木马恶意软件，这些仓库专门针对 CI/CD 代理，通过自动化依赖投毒进行攻击。 这凸显了供应链威胁的日益增长，攻击者利用自动化的 CI/CD 流水线和 AI 代理，可能感染数千个下游项目和用户。 恶意仓库频繁删除并重新推送提交以逃避检测，且针对新仓库而非流行仓库，旨在攻击代理驱动的依赖获取过程。

hackernews · theorchid · Jun 18, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48583928)

**背景**: 软件供应链攻击是指攻击者破坏开发流水线中的可信组件。CI/CD 代理是自动构建、测试和部署代码的系统；它们可能自动从 GitHub 等公共仓库获取依赖，从而易受此类恶意软件的攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/cicd-for-ai-agents-on-microsoft-foundry/4522218">CI/CD for AI Agents on Microsoft Foundry | Microsoft Community Hub</a></li>

</ul>
</details>

**社区讨论**: 社区成员对此类攻击的普遍性表示担忧，部分用户报告了其名称和仓库被劫持的个人经历。一位评论者指出，该攻击专门针对 AI 代理，并与全球重大事件（如选举）相关联。

**标签**: `#security`, `#GitHub malware`, `#supply chain attacks`, `#open source risks`, `#Trojan`

---

<a id="item-9"></a>
## [新站点跨多个 LLM 检查姓名识别](https://www.intheweights.com/) ⭐️ 8.4/10

新网站 intheweights.com 并行查询多个大型语言模型，分析给定姓名的识别强度，对响应进行聚类并标记可能的幻觉。 该工具揭示了 LLM 权重中嵌入了哪些个人信息，提高了对隐私和模型知识准确性的认识。它还凸显了不同模型可能产生幻觉或错误归因身份的问题，这在 LLM 成为主要信息来源时至关重要。 该站点查询 GPT-4、Claude、Llama 等前沿及小型模型，对相似响应进行聚类，并将离群值标记为可能的幻觉。用户可以输入任意姓名，查看每个模型的摘要和共识视图。

hackernews · turtlesoup · Jun 18, 20:49 · [社区讨论](https://news.ycombinator.com/item?id=48591348)

**背景**: 大型语言模型是在海量文本语料上训练的神经网络，其“权重”编码了学到的模式和关联。幻觉是指 LLM 生成看似合理但错误的信息。该工具探查模型权重中存储了关于个体的哪些知识，以及模型回忆这些知识的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLM_hallucination">LLM hallucination</a></li>

</ul>
</details>

**社区讨论**: 评论意见不一：许多用户对输入真实姓名表达了隐私担忧。一些人报告了有趣的错误识别，例如被标记为安全研究员而实际并非如此。其他人指出，对于生僻姓名，小型模型更容易产生幻觉。

**标签**: `#LLM`, `#AI recognition`, `#privacy`, `#model behavior`, `#Show HN`

---

<a id="item-10"></a>
## [开源模型智能体能力基准测试](https://huggingface.co/blog/is-it-agentic-enough) ⭐️ 8.4/10

Hugging Face 发布了一篇博客文章，详细介绍了使用自定义工具和任务对开源大语言模型的智能体能力进行基准测试的方法。 随着智能体 AI 受到关注，开源模型缺乏标准化评估，这使得这份实用指南对开发者为自主任务执行选择模型具有重要价值。 该方法强调使用自己的工具在特定领域任务上测试模型，重点关注规划、工具使用和适应性，而非一般知识基准。

rss · Hugging Face Blog · Jun 18, 00:00

**背景**: 智能体 AI 指的是能够自主行动、规划、使用工具并适应环境以实现目标的 AI 系统。与传统聊天机器人不同，智能体模型需要评估其与环境交互及完成复杂任务的能力。针对这些能力的标准化基准仍处于初级阶段，尤其是对于开源模型。这篇博客文章通过提供一个自定义评估的实用框架来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is agentic AI? - IBM</a></li>
<li><a href="https://arxiv.org/abs/2507.21504">Evaluation and Benchmarking of LLM Agents: A Survey</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#benchmarking`, `#open models`, `#LLM evaluation`

---

<a id="item-11"></a>
## [Vercel AI SDK Workflow 补丁修复工具审批转发问题](https://github.com/vercel/ai/releases/tag/%40ai-sdk/workflow%401.0.0-beta.100) ⭐️ 8.3/10

Vercel 发布了 @ai-sdk/workflow@1.0.0-beta.100，该补丁修复了在恢复代理工作流时，正确将提供者执行的工具审批转发给提供者的问题。 此修复防止了提供者执行的工具（例如通过 OpenAI Responses API 的 MCP 工具）在用户批准后永远无法执行的静默失败，提高了人工参与工作流的可靠性。 以前，WorkflowAgent 在恢复时会将所有工具审批部分从消息中剥离，无论执行来源如何；现在仅剥离本地执行的工具审批，而提供者执行的审批被保留并转发。

github · github-actions[bot] · Jun 18, 21:56

**背景**: Vercel AI SDK 支持人工参与的工作流，其中工具在执行前需要用户审批。工具可以由 SDK 本地执行，也可以由提供者（例如通过 OpenAI Responses API 的 MCP 服务器）执行。模型上下文协议（MCP）是一种开放标准，用于将 AI 模型连接到外部工具和数据源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://vadimall.com/posts/Build-a-human-in-the-loop-ai-agent-with-vercel-ai-sdk">Build a Human-in-the-Loop AI Agent with Vercel AI SDK</a></li>

</ul>
</details>

**标签**: `#vercel-ai-sdk`, `#workflow`, `#tool-approval`, `#llm`, `#patch`

---

<a id="item-12"></a>
## [Git 忽略文件不止.gitignore](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/) ⭐️ 8.3/10

一篇博客文章指出，除了传统的.gitignore 之外，Git 还提供了多种忽略文件的方法，包括全局排除文件和利用.gitattributes 来抑制差异。 这些替代方法有助于开发者避免提交不需要的本地文件，并减少差异中的噪音，从而提高代码审查效率和项目整洁度。 全局排除文件可以通过 git config core.excludesFile 设置或编辑.git/info/exclude，而.gitattributes 通过 diff 驱动程序可以将文件标记为二进制或禁用生成文件的差异输出。

hackernews · FergusArgyll · Jun 18, 10:29 · [社区讨论](https://news.ycombinator.com/item?id=48583356)

**背景**: Git 的.gitignore 文件是仓库特定的并被版本控制跟踪，但有时开发者需要在本地忽略文件而不影响协作者。Git 还支持通过.git/info/exclude 进行每个仓库的忽略，以及每个用户的全局排除。此外，.gitattributes 可以控制 Git 对特定文件类型进行差异和合并处理的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@chrisgregori/til-git-supports-a-global-exclude-file-88ba43fa8bec">TIL — Git supports a global exclude file | by Chris Gregori | Medium</a></li>
<li><a href="https://stackoverflow.com/questions/1753070/how-do-i-configure-git-to-ignore-some-files-locally">How do I configure git to ignore some files locally? - Stack Overflow</a></li>
<li><a href="https://git-scm.com/docs/gitattributes">Git - gitattributes Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者热情地支持全局排除文件，指出这样可以避免用 IDE 或操作系统文件污染每个项目的.gitignore。一位用户建议使用带有 diff 驱动程序的.gitattributes 来忽略生成文件（如 package-lock.json）的差异，称其为“几乎忽略”功能。另一位用户推荐将全局 git 配置放在~/.config/git/ignore，而不是传统的~/.gitignore_global。

**标签**: `#Git`, `#Version Control`, `#Developer Tools`, `#Software Engineering`, `#Productivity`

---

<a id="item-13"></a>
## [Noam Shazeer 加入 OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 8.1/10

Noam Shazeer，开创性论文《Attention Is All You Need》的合著者，该论文引入了 Transformer 架构，已离开谷歌加入 OpenAI，这一点已通过他的社交媒体帖子和路透社确认。 Shazeer 的离开意义重大，因为他是现代 AI 的基础人物；他的专业知识可能极大地影响 OpenAI 的下一代模型，特别是考虑到他最近在谷歌担任 Gemini 联合负责人的角色。 Shazeer 曾是谷歌的长期研究员，2021 年离职共同创立 Character.AI，并于 2024 年通过一项据报道价值 27 亿美元的许可/人才协议重返谷歌，担任 Gemini 联合负责人。现在约一年后他再次离开。

hackernews · lukasgross · Jun 18, 00:26 · [社区讨论](https://news.ycombinator.com/item?id=48578913)

**背景**: Transformer 架构在 2017 年的论文《Attention Is All You Need》中提出，彻底改变了自然语言处理，也是 GPT-4 和 Gemini 等现代大语言模型的基础。Shazeer 是该论文的关键贡献者。他随后共同创立了对话式 AI 初创公司 Character.AI，之后被召回谷歌领导 Gemini 的开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员注意到 Shazeer 在实现 Transformer 方面的关键作用，一些人推测他再次如此迅速离开谷歌的原因，并将其与他直言不讳的政治观点联系起来。讨论中还引用了一篇《连线》文章，详细介绍了该论文的背景故事和每位作者的贡献。

**标签**: `#AI`, `#LLM`, `#Transformers`, `#OpenAI`, `#Industry moves`

---

<a id="item-14"></a>
## [康奈尔大学 CS 6120 高级编译器自修课程](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 8.0/10

康奈尔大学的 CS 6120 高级编译器课程现已提供自助在线学习，公开了顶尖大学的讲座和资料。 该课程提供了高级编译器设计的严谨课程，但社区反馈表明它可能依赖如跟踪编译等过时技术，并涵盖了一些人认为属于入门级的内容。 该课程涵盖动态编译，包括跟踪编译，一位评论者指出这已被广泛废弃；同时还包括标准主题如 SSA 形式和数据流分析。

hackernews · ibobev · Jun 18, 11:04 · [社区讨论](https://news.ycombinator.com/item?id=48583606)

**背景**: 高级编译器课程通常建立在入门材料之上，探索优化、代码生成和运行时技术。跟踪编译是一种即时编译技术，用于记录并编译热点路径，但在现代 JIT 中已被类型反馈和分层编译等方法取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tracing_just-in-time_compilation">Tracing just-in-time compilation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞扬了课程的可用性，但也提出了担忧：titzer 指出跟踪编译是一条'死胡同'，并强调了类型反馈和去优化的价值；j2kun 则质疑'高级'标签，认为许多主题属于初次编译器课程的内容。

**标签**: `#compilers`, `#online-course`, `#systems-programming`, `#programming-languages`, `#computer-science`

---

<a id="item-15"></a>
## [MosaicLeaks：研究 Agent 的隐私风险](https://huggingface.co/blog/ServiceNow/mosaicleaks) ⭐️ 8.0/10

ServiceNow Research 提出了 MosaicLeaks，该任务测试研究 Agent 在回答混杂公共和私人数据的多跳问题时能否保护隐私信息。 随着 AI Agent 越来越多地处理敏感数据，这项工作揭示了当前 Agent 安全防护的关键漏洞，并为改进隐私保护 Agent 设计提供了基准。 MosaicLeaks 使用交织公共和私人信息的多跳问题，要求 Agent 在推理时避免泄露私人部分。

rss · Hugging Face Blog · Jun 18, 18:13

**背景**: 研究 Agent 是能够自主搜索、检索和综合来自多种来源信息的 AI 系统。这些 Agent 经常查询公共数据库和私人组织数据，增加了无意中暴露敏感信息的风险。MosaicLeaks 将这一风险场景形式化，并提出了一种新的评估方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ServiceNow/mosaicleaks">MosaicLeaks : Can your research agent keep a secret?</a></li>
<li><a href="https://arxiv.org/html/2605.30727">MosaicLeaks : Privacy Risks in Querying-in-the-Open for Deep...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#LLM agents`, `#privacy`, `#security`, `#research`

---

<a id="item-16"></a>
## [强迫同意使 Elkjop 被罚 180 万欧元](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 7.9/10

挪威电子零售商 Elkjop 因要求客户加入会员俱乐部时必须同意接收营销信息，被处以 180 万欧元的 GDPR 罚款。 此案强化了 GDPR 中同意必须是自愿的，不得将同意作为服务条件的规则，为欧盟内类似做法树立了先例。 该罚款由挪威数据保护局（Datatilsynet）在历时五年的法律程序后作出。该公司明确表示，营销同意是加入会员俱乐部的条件。

hackernews · speckx · Jun 18, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48589501)

**背景**: 根据 GDPR，同意必须是自愿的、具体的、知情的且明确的。将同意与服务或会员俱乐部绑定属于'强迫同意'，违反了 GDPR 第 7 条第 4 款。

**社区讨论**: 评论者赞扬挪威数据保护局一贯保护用户权利，但也指出过程漫长。有评论分享了实际决定链接，另一评论表达了希望更多人能行使自己的权利，尽管可能遭遇社会摩擦。

**标签**: `#privacy`, `#GDPR`, `#consent`, `#data protection`, `#compliance`

---

<a id="item-17"></a>
## [网站提交目录的聚合器引发 HN 讨论](https://www.submission.directory/) ⭐️ 7.8/10

一个名为 submission.directory 的新元目录列出了创始人可以提交自己网站的站点，但真正的价值来自附带的 Hacker News 讨论。讨论中包含了创始人的第一手经验（例如 BetaList 的创建故事）以及精心挑选的替代方案。 对于独立开发者和创业营销人员来说，找到相关的目录是一种关键的增长策略，而这个讨论提供了经过社区验证的实用资源。它也凸显了独立网络生态中真实推广与垃圾信息之间的持续紧张关系。 该网站本身是一个简单的列表，几乎没有筛选，但 HN 评论线程中包含了几个精心策划的替代方案链接，如 blogroll.org、blogs.hn 和 indieblog.page。一位评论者指出播客目录中的垃圾信息历史，即提交虚假播客仅为了获取反向链接。

hackernews · azeemkafridi · Jun 18, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=48586631)

**背景**: 独立网络（IndieWeb）运动倡导个人拥有自己的在线存在，而不是依赖集中式平台。元目录是目录的目录，帮助用户在一个地方发现多个提交机会。历史上，像 1990 年代的 Submit It 这样的服务提供类似的一键提交到搜索引擎，但今天的挑战是触及小众、面向特定受众的网站。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://indieweb.org/">The IndieWeb is a people-focused alternative to the “corporate web”.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metadirectory">Metadirectory - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论总体积极且富有洞见：创始人分享个人经历（例如 BetaList 的人工审核流程催生了 submit.co），用户提供了精心策划的替代列表。然而，一位评论者警告说，公开此类目录会招致垃圾信息，呼应了播客目录中滥用反向链接的担忧。

**标签**: `#indieweb`, `#startup marketing`, `#directories`, `#backlinks`, `#HN discussion`

---

<a id="item-18"></a>
## [OpenAI 推出支出控制与使用分析功能](https://openai.com/index/chatgpt-enterprise-spend-controls) ⭐️ 7.5/10

OpenAI 为 ChatGPT Enterprise 推出了新的支出控制和使用分析功能，使组织能够有效监控和管理其 AI 使用成本。 此次更新通过提供使用模式的透明度和成本管理工具，帮助企业自信地扩展 AI 采用，解决了企业部署 AI 的关键障碍。 支出控制功能使管理员能够设置预算和使用限制，而分析仪表板则提供用户级消费和支出趋势的洞察。

rss · OpenAI Blog · Jun 18, 17:00

**背景**: ChatGPT Enterprise 是 OpenAI 面向企业的 ChatGPT 版本，提供增强的安全、隐私和针对组织使用的功能。随着企业将大语言模型整合到工作流程中，大规模管理 AI 成本已成为日益关注的问题，因此支出控制成为实际必要。

**标签**: `#AI`, `#ChatGPT`, `#Enterprise`, `#Spend Controls`

---

<a id="item-19"></a>
## [AI 推理模型发现 18 个新罕见病诊断](https://openai.com/index/diagnose-rare-childhood-diseases) ⭐️ 7.5/10

研究人员使用 OpenAI 的 o1 推理模型分析临床数据，在儿童中识别出 18 个此前未确诊的罕见遗传病。 这表明 AI 推理模型可以增强人类在复杂医学诊断中的专业能力，有可能减少罕见病的诊断延迟，改善患者预后。 该研究利用了 o1 模型在回答前进行逐步思考的能力，这对处理多维度临床数据的推理至关重要。这 18 个新诊断通过后续基因检测得到确认。

rss · OpenAI Blog · Jun 18, 08:00

**背景**: OpenAI o1 是一个推理模型，它在生成回答前会花更多时间“思考”，因此在数学、编程和科学推理等复杂任务上表现更好。与快速给出答案的标准大型语言模型（LLM）不同，推理模型用速度换取更深入的分析。这种能力在医学等领域尤其有用，因为需要仔细权衡多条证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_o1">OpenAI o1 - Wikipedia</a></li>
<li><a href="https://openai.com/index/learning-to-reason-with-llms/">Learning to reason with LLMs | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#healthcare`, `#rare diseases`, `#LLM`, `#diagnosis`

---

<a id="item-20"></a>
## [OpenAI 推出 LifeSciBench 评估生命科学 AI](https://openai.com/index/introducing-life-sci-bench) ⭐️ 7.5/10

OpenAI 发布了 LifeSciBench，这是一个由领域专家编写和审核的基准，用于评估 AI 系统在真实生命科学研究任务和决策中的表现。 LifeSciBench 超越了简单的问答，评估高级科学推理和实践技能，有望加速 AI 在药物发现、基因组学等生命科学领域的应用。 该基准任务要求模型解释证据、做出基于领域的决策并解决现实研究问题，反映了实际科学工作中所需的复杂判断。

rss · OpenAI Blog · Jun 17, 00:00

**背景**: 基准测试是用于衡量 AI 系统性能的标准化测试。大多数现有基准侧重于事实回忆或简单推理。LifeSciBench 针对现实世界科学应用所需的不太明确的实践技能，旨在弥合 AI 能力与实际研究需求之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-life-sci-bench/">Introducing LifeSciBench | OpenAI</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-unveils-lifescibench">OpenAI Unveils LifeSciBench | StartupHub.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmarking`, `#life sciences`, `#research`, `#OpenAI`

---

<a id="item-21"></a>
## [医院和大学以极低成本重新利用药物](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 7.2/10

医院和大学正以高达 90%的成本降低重新利用现有药物治疗新适应症，例如使用抗癌药 Avastin 治疗黄斑变性，以及使用氯胺酮治疗抑郁症。 这种方法可以大幅降低医疗成本并提高治疗的可及性，尤其对于罕见病而言，制药公司开发新药在经济上不可行。 例如，Avastin 每剂约 50 美元，而其功能相同用于眼部注射的版本 Lucentis 则需 1500 美元；类似地，esketamine（Spravato）是氯胺酮的专利改良版，但可能效果较差。

hackernews · giuliomagnifico · Jun 18, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=48583386)

**背景**: 药物重新利用，又称药物再定位，是指研究现有已批准药物用于新的治疗用途。该策略减少了药物开发的时间、成本和风险，因为这些药物已经通过了安全性测试。然而，在没有制造商同意的情况下，将已批准药物扩展至新适应症的监管途径有限，通常需要独立进行研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Drug_repurposing">Drug repurposing</a></li>
<li><a href="https://www.nature.com/articles/nrd.2018.168">Drug repurposing: progress, challenges and recommendations | Nature Reviews Drug Discovery</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经验和见解：有人指出 Avastin 和 Lucentis 因包装不同而价格悬殊；另一人提到了非营利组织 Cures Within Reach，该组织资助针对亨廷顿病等罕见病的药物再利用研究；一位使用 Spravato 的用户批评医疗系统更倾向于专利改良药物，而非更便宜、更有效的仿制药。

**标签**: `#drug repurposing`, `#healthcare costs`, `#pharmaceuticals`, `#clinical research`

---

<a id="item-22"></a>
## [自动驾驶实验室：材料科学的新护城河](https://www.latent.space/p/radical-ai) ⭐️ 7.2/10

在最近的一篇文章中，Radical AI 的 Joseph Krause 认为，在材料科学中，真正的竞争优势来自自动化实验室基础设施，而非 AI 模型本身。 这一观点挑战了普遍对模型性能的关注，强调了物理自动化和数据生成能力的重要性，可能重塑材料发现领域的投资和研究重点。 Krause 指出，将自动化实验与机器学习相结合的自动驾驶实验室基础设施创造了难以复制的数据飞轮，从而成为持久的护城河。

rss · Latent Space · Jun 17, 17:58

**背景**: 自动驾驶实验室 (SDL) 将自动化实验平台与机器学习相结合，以加速材料和分子发现。Radical AI 最近宣布获得 5500 万美元种子轮融资，用于构建此类用于自主材料发现的基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00055">Self-Driving Laboratories for Chemistry and Materials Science | Chemical Reviews</a></li>
<li><a href="https://www.nature.com/articles/s44160-022-00231-0">The rise of self-driving labs in chemical and materials sciences | Nature Synthesis</a></li>
<li><a href="https://www.radical-ai.com/news/series-seed">Radical AI announces $55M in new funding</a></li>

</ul>
</details>

**标签**: `#AI`, `#materials science`, `#self-driving lab`, `#automation`, `#Radical AI`

---

<a id="item-23"></a>
## [W Social：欧洲数字主权的作秀](https://blog.elenarossini.com/w-social-public-institutions-and-the-theater-of-european-digital-sovereignty/) ⭐️ 7.1/10

一篇博客文章批评 W Social 是一个作秀式的欧洲数字主权项目，指出其缺乏透明度，并对比了 Eurosky 等开放替代方案。 这篇批评揭露了欧盟数字主权努力中政治口号与实际内容之间的差距，可能影响公众认知和政策讨论。 W Social 是一家由前金融专业人士运营的有限责任公司，并非欧盟支持的项目，被评论者称为“带欧洲口音的 Truth Social”。

hackernews · nemoniac · Jun 18, 12:46 · [社区讨论](https://news.ycombinator.com/item?id=48584497)

**背景**: 欧洲数字主权旨在减少对非欧盟技术提供商的依赖。W Social 推出时有欧盟高调政客加入，但欧盟委员会表示并未参与该平台。博客认为此类项目可能只是作秀，缺乏真正的开放性及社区控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.elenarossini.com/w-social-uncovered-the-reality-behind-the-hype/">W Social uncovered: the reality behind the hype</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/eu-tech-sovereignty">Strengthening Europe’s Tech Sovereignty | Shaping Europe’s ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表示怀疑，指出 W Social 的可疑之处、有限责任公司结构及缺乏透明度。多人指出基于 ATproto 的 Eurosky 是更真实的开放项目。有人将 W Social 比作 Truth Social。

**标签**: `#European digital sovereignty`, `#social media`, `#W Social`, `#politics`, `#tech criticism`

---

<a id="item-24"></a>
## [Gerrymandle：每日拼图游戏教你理解选区划分](https://gerrymandle.cc/) ⭐️ 7.0/10

一款名为 Gerrymandle 的新每日拼图游戏在 Hacker News 上发布，玩家通过重新划分选区来了解不公正选区划分（gerrymandering）的概念。 该游戏通过互动玩法使一个复杂且常被忽视的政治问题变得易于理解，可能提升公民意识和参与度。 游戏简化了不公正选区划分；例如，如果两个政党在一个选区打成平手，则无人获胜，这虽不现实但有助于传达核心概念。

hackernews · realmofthemad · Jun 18, 14:16 · [社区讨论](https://news.ycombinator.com/item?id=48585739)

**背景**: 不公正选区划分（Gerrymandering）是指操纵选区边界以利于某一政党或团体的做法。在美国等许多地方是合法的，且能显著影响选举结果。这款游戏提供了该过程的教育模拟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/illumination/what-is-gerrymandering-explained-for-common-folks-4cb6ef0bff55">What is Gerrymandering ? (Explained for Common Folks)</a></li>
<li><a href="https://www.youtube.com/watch?v=fDO7NrcfzAI">What is Gerrymandering & How do you do it? - YouTube</a></li>

</ul>
</details>

**社区讨论**: 评论普遍积极，称赞游戏的创意和教育价值。一些人注意到规则简化，例如平局导致无人获胜，而另一些人则认为它是公民课堂的绝佳工具。少数评论引用了关于公平选区划分的学术研究。

**标签**: `#puzzle game`, `#gerrymandering`, `#educational`, `#civics`, `#software project`

---

<a id="item-25"></a>
## [AI 时代电商访谈：与 Michael Morton 对话](https://stratechery.com/2026/an-interview-with-michael-morton-about-e-commerce-in-the-age-of-ai/) ⭐️ 7.0/10

本次访谈探讨了由 AI 驱动的电子商务转型中的关键主题，包括不可证伪的空头论点以及从分销模式向推荐模式的转变。 随着 AI 重塑零售业，理解分销与推荐模型之间的战略差异，以及不可证伪的空头论点的挑战，对于投资者和企业家驾驭电子商务的未来至关重要。 访谈涵盖了杂货和自动驾驶汽车作为 AI 在电子商务中的具体行业应用。Michael Morton 可能是该领域的专家，但提供的资料中未详细说明其背景。

rss · Stratechery · Jun 18, 10:00

**背景**: “不可证伪的空头论点”指的是那些无法被证明错误的悲观论点，这在投资和技术辩论中很相关。分销模式涉及通过合作伙伴销售产品，而推荐模式则强调客户推荐实现增长。这些是电子商务中的关键战略选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falsifiability">Falsifiability - Wikipedia</a></li>
<li><a href="https://www.venturasecurities.com/share-market-guide/all-about-share-stock-market/fundamental-analysis/bull-vs-bear-case-optimistic-and-pessimistic-scenarios-explained/">Bull vs Bear Case: Optimistic and Pessimistic Scenarios Explained | Ventura Share Market Guide</a></li>
<li><a href="https://www.referralcandy.com/blog/referral-attribution-model">How Referral Marketing Fits in Multi-Touch Attribution Model</a></li>

</ul>
</details>

**标签**: `#E-commerce`, `#AI`, `#Interview`, `#Distribution`, `#Grocery`

---

<a id="item-26"></a>
## [本·汤普森评 Fable、越狱问题与 SpaceX 收购 Cursor](https://stratechery.com/2026/the-state-of-fable-the-jailbreak-problem-spacex-acquires-cursor/) ⭐️ 7.0/10

本·汤普森在 Stratechery 的文章中批评了政府对 Claude Fable 的立场，并强调了 AI 越狱问题，将责任归于 Anthropic，同时提到 SpaceX 收购 Cursor。 这一分析凸显了 AI 安全与政府监管之间的持续紧张关系，而收购则表明 SpaceX 对 AI 辅助编码工具的兴趣，影响更广泛的科技格局。 Claude Fable 5 是一款用于视觉和编码任务的最先进模型，但其能力引发了安全隐患；2026 年 AI 越狱攻击激增 400%，利用提示注入漏洞。

rss · Stratechery · Jun 17, 10:00

**背景**: Claude Fable 是 Anthropic 专注于编码和视觉任务的先进 AI 模型系列，Fable 5 是最新版本。AI 越狱是指通过提示注入等技术绕过大型语言模型（LLM）的安全护栏。Cursor 是一款 AI 驱动的代码编辑器，可加速软件开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.hexon.bot/blog/ai-jailbreak-attacks-llm-security-2026">The AI Jailbreak Epidemic | Hexon</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack ? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#jailbreaking`, `#Anthropic`, `#SpaceX`

---