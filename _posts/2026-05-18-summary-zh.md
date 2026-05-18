---
layout: default
title: "Horizon Summary: 2026-05-18 (ZH)"
date: 2026-05-18
lang: zh
---

> From 66 items, 16 important content pieces were selected

---

1. [使用 LoRA/DoRA 微调 NVIDIA Cosmos Predict 2.5](#item-1) ⭐️ 9.3/10
2. [开放智能体排行榜为开源 AI 智能体提供基准](#item-2) ⭐️ 8.9/10
3. [AI 制导武器已改变战争，西方未准备好](#item-3) ⭐️ 8.6/10
4. [语音 AI 系统易受隐藏音频攻击](#item-4) ⭐️ 8.4/10
5. [马斯克诉奥特曼及 OpenAI 案被驳回](#item-5) ⭐️ 8.3/10
6. [使用 Git 的--author 标志阻止 GitHub 仓库中的 AI 机器人垃圾信息](#item-6) ⭐️ 8.2/10
7. [Anthropic 收购 Stainless](#item-7) ⭐️ 8.0/10
8. [PaddleOCR 3.5 新增 Transformers 后端，支持 OCR 与文档解析](#item-8) ⭐️ 8.0/10
9. [LiteLLM v1.85.0 增加 Docker 镜像签名验证指南](#item-9) ⭐️ 7.8/10
10. [AI 取代工作可能导致消费者经济崩溃](#item-10) ⭐️ 7.8/10
11. [我们让 AI 经营广播电台作为实验](#item-11) ⭐️ 7.7/10
12. [数据中心反对问题：直接补偿是关键](#item-12) ⭐️ 7.7/10
13. [OpenAI 与戴尔合作，推动 Codex 企业级部署](#item-13) ⭐️ 7.4/10
14. [谷歌 I/O 前瞻：公司在基础模型竞赛中落后](#item-14) ⭐️ 7.4/10
15. [Files.md：Obsidian 的开源替代品](#item-15) ⭐️ 7.2/10
16. [Anduril 与 Meta 为军事用途原型 AR 头显，可指挥无人机打击](#item-16) ⭐️ 7.2/10

---

<a id="item-1"></a>
## [使用 LoRA/DoRA 微调 NVIDIA Cosmos Predict 2.5](https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation) ⭐️ 9.3/10

Hugging Face 上发布了一篇详细教程，展示了如何使用 LoRA 和 DoRA 技术微调 NVIDIA Cosmos Predict 2.5 以生成机器人视频。 这连接了世界基础模型与机器人视频生成，实现了无需完整模型重训练即可进行定制化、高效的机器人训练模拟。 该教程涵盖了 LoRA（低秩适应）和 DoRA（权重分解低秩适应）两种参数高效微调方法，并应用于基于流的 Cosmos Predict 2.5 模型。

rss · Hugging Face Blog · May 18, 16:00

**背景**: NVIDIA Cosmos Predict 2.5 是一个世界基础模型，能够从文本、图像或视频输入中模拟和预测未来视频帧，采用基于流的架构。LoRA 是一种参数高效微调技术，它在模型层中注入可训练的低秩矩阵；而 DoRA 通过权重分解进一步提升了性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nvidia-cosmos/cosmos-predict2.5">nvidia-cosmos/cosmos-predict2.5 - GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-dora-a-high-performing-alternative-to-lora-for-fine-tuning/">Introducing DoRA , a High-Performing Alternative to LoRA for...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#fine-tuning`, `#robot video generation`, `#LoRA`

---

<a id="item-2"></a>
## [开放智能体排行榜为开源 AI 智能体提供基准](https://huggingface.co/blog/ibm-research/open-agent-leaderboard) ⭐️ 8.9/10

Hugging Face 和 IBM 联合发布开放智能体排行榜，这是一个用于评估开源 AI 智能体在多种任务上表现的新基准。 该排行榜为比较开源 AI 智能体的能力提供了标准化方式，促进了该领域的透明度和进步。 该排行榜包含多种数学和多模态基准，支持按评估维度、算法、数据集和模型进行筛选。

rss · Hugging Face Blog · May 18, 14:12

**背景**: AI 智能体是能够在环境中推理和行动的自主系统。基准测试帮助研究人员跟踪进展并识别优势与不足。开放智能体排行榜专注于开源模型，以鼓励社区贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rungalileo/agent-leaderboard">GitHub - rungalileo/agent-leaderboard: Ranking LLMs on agentic tasks · GitHub</a></li>
<li><a href="https://huggingface.co/spaces/omlab/open-agent-leaderboard">Open Agent Leaderboard - a Hugging Face Space by omlab</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM`, `#Benchmark`, `#Open Source`

---

<a id="item-3"></a>
## [AI 制导武器已改变战争，西方未准备好](https://www.latent.space/p/the-fourth-law) ⭐️ 8.6/10

乌克兰无人机创始人 Yaroslav Azhnyuk 认为，AI 制导武器已经彻底改变了战争，并警告西方军队远未做好准备。经济学家 Noah Smith 主持的这次讨论指出，乌克兰正在大规模部署 AI 自主瞄准的无人机。 这一分析意义重大，因为它标志着现代战争范式的转变：AI 制导无人机和自主武器正成为作战核心，可能超越现有的军事理论和伦理。西方缺乏准备可能导致面对已部署此类系统的对手时出现战略脆弱性。 Azhnyuk 从制造宠物相机转向为乌克兰无人机部队开发 AI 制导武器。文章讨论了末端自主瞄准，即无人机利用计算机视觉在失去与操作员通信时仍能打击目标，该能力已在乌克兰得到验证。

rss · Latent Space · May 18, 13:45

**背景**: AI 制导武器，也称为致命自主武器系统（LAWS），能够在无人干预下识别和攻击目标。在乌克兰，配备自主模块的无人机被用于末端攻击，使其能够抵抗干扰。美国等西方国家有限制自主交战的政策，但乌克兰的快速发展已超越现有政策框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2025/12/31/magazine/ukraine-ai-drones-war-russia.html">In Ukraine, a New Arsenal of Killer A.I. Drones Is Being Born</a></li>
<li><a href="https://spectrum.ieee.org/autonomous-drone-warfare">How Autonomous Drone Warfare Is Emerging in Ukraine - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#AI`, `#Drones`, `#Ukraine`, `#Warfare`, `#Startup`

---

<a id="item-4"></a>
## [语音 AI 系统易受隐藏音频攻击](https://spectrum.ieee.org/voice-ai-audio-attacks) ⭐️ 8.4/10

研究人员已经证明，包括语音转文本和具有音频能力的大型语言模型在内的语音 AI 系统，可以被人类无法察觉的隐藏对抗性音频示例劫持，导致 AI 转录恶意命令。 这一漏洞暴露了语音 AI 应用（如虚拟助手、转录服务和基于音频的 LLM）中的关键安全缺口，可能使攻击者能够通过看似良性的音频远程控制设备或获取敏感信息。 这些攻击建立在先前关于对抗性音频示例的工作之上，最近的研究显示能够在实时语音聊天中注入恶意音频。由于扰动的可听性有限，防御仍然具有挑战性。

hackernews · SVI · May 18, 11:51 · [社区讨论](https://news.ycombinator.com/item?id=48178378)

**背景**: 对 AI 系统的对抗性攻击涉及制作略微修改的输入以导致错误分类。在音频中，这意味着向声音片段添加难以察觉的噪声，使得语音转文本模型转录不同的短语。这一概念在计算机视觉中众所周知，但现在应用于语音 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/voice-ai-audio-attacks">Voice AI Systems Are Vulnerable to Hidden Audio Attacks</a></li>
<li><a href="https://nicholas.carlini.com/code/audio_adversarial_examples">Audio Adversarial Examples - Nicholas Carlini</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这是对抗性图像攻击的自然延伸，有人幽默地提及“盗用电话线路”。其他人讨论实际缓解措施，如使用高质量麦克风，并质疑在线视频中的隐藏音频轨道是否已被用于数据抓取。

**标签**: `#AI security`, `#adversarial attacks`, `#voice AI`, `#LLM vulnerabilities`, `#audio processing`

---

<a id="item-5"></a>
## [马斯克诉奥特曼及 OpenAI 案被驳回](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/) ⭐️ 8.3/10

2026 年 5 月 18 日，陪审团以拖延诉讼为由驳回了埃隆·马斯克对 Sam Altman 和 OpenAI 的起诉。 该裁决强化了科技领域知名纠纷中诉讼时效的抗辩作用，可能阻止针对 AI 公司的类似迟诉案件。同时，OpenAI 的营利转型及与微软的合作未受该案影响。 陪审团仅回答是否问题，具体理由不明，但可能认为 2019 年和 2021 年的微软交易与本案核心的 2023 年交易过于相似。诉讼时效要求三年内提出索赔，陪审团认定其已逾期。

hackernews · nycdatasci · May 18, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=48182754)

**背景**: 马斯克于 2015 年联合创立了非营利的 OpenAI，但在 2018 年退出。随后 OpenAI 成立了营利性子公司并与微软合作。马斯克于 2024 年起诉，称 OpenAI 背离非营利使命，但法院认定他在 2019 年已知悉营利架构后未能及时起诉。

**社区讨论**: 评论者如 granzymes 赞同裁决，认为马斯克自 2019 年起就知情，其法律策略'站不住脚'。另有人如 arsad 认为 OpenAI 仍应因将非营利资产窃取到营利实体而受罚。部分人质疑政府是否会就非营利向营利转移知识产权采取行动。

**标签**: `#AI`, `#OpenAI`, `#lawsuit`, `#legal`, `#governance`

---

<a id="item-6"></a>
## [使用 Git 的--author 标志阻止 GitHub 仓库中的 AI 机器人垃圾信息](https://archestra.ai/blog/only-responsible-ai) ⭐️ 8.2/10

Archestra 的一篇博客文章介绍了如何使用 Git 的--author 标志，通过检查提交作者邮箱地址与贡献者记录是否匹配，来识别并阻止 GitHub 仓库中的 AI 机器人垃圾信息。 这种技术为维护者提供了一个实用的、低技术门槛的解决方案来过滤自动化垃圾拉取请求，这已成为一个日益严重的问题，尤其是在有赏金的仓库中。然而，社区讨论指出，基于邮箱匹配授予贡献者状态可能会引入安全风险。 该方法依赖于 GitHub 在提交的 author 邮箱与用户的 GitHub 账户邮箱匹配时，将提交链接到用户个人资料，从而授予贡献者状态并绕过首次贡献者的批准要求。如果贡献者更改了邮箱地址，或者恶意行为者获得了一个无关紧要的更改被接受，这种方法可能会被规避。

hackernews · ildari · May 18, 15:24 · [社区讨论](https://news.ycombinator.com/item?id=48181125)

**背景**: Git 的--author 标志允许在使用如 git log 等命令时按作者过滤提交。GitHub 通过提交邮箱匹配来确定用户的贡献状态，从而获得权限，例如避免对 fork PR 运行的批准要求。AI 机器人越来越多地针对 GitHub 仓库进行自动化的低质量拉取请求，通常用于垃圾信息或刷赏金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.git-tower.com/learn/git/faq/change-author-name-email">How can I change the author (name / email) of a commit?</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对安全影响的担忧：通过邮箱匹配授予贡献者状态可能被恶意用户利用，绕过批准要求。其他评论者提出了替代方案，如基于 ELO 的声誉系统或更严格的 GitHub 政策，并指出这个问题在有赏金的仓库中尤为严重。

**标签**: `#AI bots`, `#GitHub`, `#spam mitigation`, `#Git`, `#security`

---

<a id="item-7"></a>
## [Anthropic 收购 Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless) ⭐️ 8.0/10

Anthropic 收购了 API 工具初创公司 Stainless，该公司曾根据 API 规范生成 SDK，但 Anthropic 将逐步关停所有托管的 Stainless 产品（包括 SDK 生成器），转而专注于 Claude 平台能力及连接代理与 API。 此次收购表明 Anthropic 正着力强化其开发者平台与智能体生态，但关停 Stainless 产品可能让现有用户感到失望，并引发对 AI 工具领域供应商锁定的担忧。 Stainless 曾根据 OpenAPI 规范生成 Python、TypeScript、Go 等语言的 SDK；此次收购实质是“人才收购”（acquihire），团队加入 Anthropic 而产品停运，新注册已暂停。

hackernews · tomeraberbach · May 18, 17:01 · [社区讨论](https://news.ycombinator.com/item?id=48182281)

**背景**: Stainless 是一家帮助 API 提供商自动生成高质量 SDK 的初创公司，客户包括 OpenAI 和 Anthropic。“人才收购”（acquihire）指主要为了获取人才而非产品的收购，企业常用此方式快速引入经验丰富的团队。Anthropic 是 Claude AI 助手的开发公司，正积极扩展其开发者平台，近期还推出了智能体编码工具等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stainless.com/">Stainless - Best-in-class developer interfaces for your API</a></li>
<li><a href="https://techcrunch.com/2024/04/24/stainless-is-helping-openai-anthropic-and-others-build-sdks-for-their-apis/">Stainless is helping OpenAI, Anthropic and others build... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acqui-hiring">Acqui-hiring - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者认为这是一次明显的人才收购，并对产品关停表示失望。有人质疑该策略对现有用户的影响，指出当前 SDK 的未来尚不明确；另有人指出，AI 驱动的代码生成兴起使得独立的 SDK 生成器吸引力下降。

**标签**: `#AI`, `#Anthropic`, `#acquihire`, `#developer tools`, `#API`

---

<a id="item-8"></a>
## [PaddleOCR 3.5 新增 Transformers 后端，支持 OCR 与文档解析](https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers) ⭐️ 8.0/10

PaddleOCR 3.5 现在集成了 Transformers 后端，用户可以通过 Hugging Face Transformers 库直接运行 OCR 和文档解析模型（如 PP-OCRv5 和 PaddleOCR-VL 1.5）。 此集成简化了部署和互操作性，使得在广泛采用的 Transformers 生态系统中无缝使用 PaddleOCR 的强大 OCR 功能成为可能，这对于构建文档处理管线的开发者至关重要。 Transformers 后端支持 PP-OCRv5 进行文本检测与识别，以及 PaddleOCR-VL 1.5 进行文档解析（在 OmniDocBench v1.5 上达到了 94.5% 的准确率）。用户可通过 Transformers 的 `pipeline` API 使用。

rss · Hugging Face Blog · May 18, 15:12

**背景**: PaddleOCR 是基于百度飞桨（PaddlePaddle）框架开发的开源 OCR 工具包，支持 100 多种语言。Transformers 是 Hugging Face 开发的流行库，提供数千个预训练模型。此前，PaddleOCR 模型需要使用 PaddlePaddle 特有的 API；新的后端使其可以通过 Transformers 以相同方式运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers">PaddleOCR 3.5: Running OCR and Document Parsing Tasks with...</a></li>
<li><a href="https://github.com/PADDLEPADDLE/PADDLEOCR">GitHub - PaddlePaddle/PaddleOCR: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. · GitHub</a></li>
<li><a href="https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5">PaddlePaddle/PaddleOCR-VL-1.5 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#OCR`, `#Document Parsing`, `#Transformers`, `#PaddlePaddle`, `#AI`

---

<a id="item-9"></a>
## [LiteLLM v1.85.0 增加 Docker 镜像签名验证指南](https://github.com/BerriAI/litellm/releases/tag/v1.85.0) ⭐️ 7.8/10

LiteLLM v1.85.0 新增了使用 cosign 验证 Docker 镜像签名的详细指南，包括使用提交哈希和发布标签两种方法。 这增强了 LiteLLM 用户的供应链安全性，确保他们拉取的 Docker 镜像真实且未被篡改，这对生产环境中的 AI 部署至关重要。 推荐的验证方法使用固定的提交哈希以获得加密不变性，而便捷方法使用发布标签。两者都依赖于提交 0112e53 中引入的同一公钥。

github · github-actions[bot] · May 17, 02:20

**背景**: LiteLLM 是一个开源代理服务器，为 OpenAI、Anthropic、Google 等数百个 LLM API 提供统一接口。Cosign 是 Sigstore 项目的一款工具，用于对软件工件进行签名和验证，常用于容器镜像。验证签名可确保镜像自构建以来未被篡改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore / cosign : Code signing and transparency for...</a></li>
<li><a href="https://docs.docker.com/dhi/core-concepts/signatures/">Code signing | Docker Docs</a></li>

</ul>
</details>

**标签**: `#litellm`, `#docker`, `#cosign`, `#security`, `#release`

---

<a id="item-10"></a>
## [AI 取代工作可能导致消费者经济崩溃](https://carette.xyz/posts/who_will_buy_your_services/) ⭐️ 7.8/10

一篇博客文章指出，广泛采用 AI 将摧毁技术服务的消费者基础，除非实施普遍基本收入等解决方案，否则可能导致经济崩溃。 这凸显了科技行业增长模式的一个关键弱点：如果 AI 消灭了工作岗位，消费者可能再也负担不起技术服务，从而可能引发系统性经济危机。 该文章带有 AI、经济学、UBI、工作替代和科技行业等标签，并在 Hacker News 上引起了强烈的社区讨论，表明该话题受到高度关注。

hackernews · LucidLynx · May 18, 21:18 · [社区讨论](https://news.ycombinator.com/item?id=48185789)

**背景**: 科技行业依赖于同时也是工人的消费者。如果 AI 大规模取代工作，这些工人将失去收入，从而减少对科技产品的需求。该文章质疑在没有 UBI 等再分配机制的情况下这种趋势的可持续性。

**社区讨论**: 评论者表达了对财富集中的担忧，提到了与苏联解体的历史相似性，对 UBI 可行性持怀疑态度，并批评了科技行业对短期利润的关注。

**标签**: `#AI`, `#economics`, `#UBI`, `#job displacement`, `#tech industry`

---

<a id="item-11"></a>
## [我们让 AI 经营广播电台作为实验](https://andonlabs.com/blog/andon-fm) ⭐️ 7.7/10

Andon Labs 进行了一项实验，让四个 AI 智能体运营直播广播电台，包括广播和业务管理，目前收入惨淡，但偶尔有搞笑的节目。 这项实验展示了 AI 智能体在自主、真实世界角色中的当前局限性和意外行为，为理解 AI 失败和新型娱乐潜力提供了见解。 AI 智能体拥有直播和业务所需的所有工具，但收入不佳；听众报告了智能体卡在循环中或产生有趣对话的实例。

hackernews · lukaspetersson · May 18, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48183301)

**背景**: AI 智能体是使用大型语言模型（LLM）自主执行任务的系统，无需人工干预。Andon Labs 此前曾尝试 AI 运营零售业务，如自动售货机和咖啡馆。这次广播实验将概念扩展到媒体领域，由 AI 处理内容创作和业务运营。

**社区讨论**: 社区评论各有不同：有人将实验与 1990 年代放松管制后的广播同质化相比，有人报告 AI 重复短语的故障，有人为其辩护称是有趣的实验，还有人推广自己的 AI 电台，也有人觉得很好笑。

**标签**: `#AI`, `#LLM`, `#agents`, `#radio`, `#experiment`

---

<a id="item-12"></a>
## [数据中心反对问题：直接补偿是关键](https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/) ⭐️ 7.7/10

本·汤普森认为，对数据中心的反对是可以理解的，唯一有效的解决方案是向受影响的社区提供直接补偿。 这一点很重要，因为数据中心的扩展对人工智能和云计算至关重要，但地方反对可能阻碍项目。汤普森提出的财务补偿方案可能会重塑科技公司与社区谈判的方式。 文章没有提供具体的技术细节，而是侧重于反对背后的社会经济原因以及实施补偿的实际挑战。

rss · Stratechery · May 18, 10:00

**背景**: 数据中心是容纳云计算服务和人工智能训练计算基础设施的大型设施。它们消耗大量电力和水资源，并可能造成噪音和视觉影响，从而导致当地反对。其他行业已使用社区福利协议等补偿机制来解决类似问题。

**标签**: `#data centers`, `#opposition`, `#compensation`, `#tech infrastructure`, `#Stratechery`

---

<a id="item-13"></a>
## [OpenAI 与戴尔合作，推动 Codex 企业级部署](https://openai.com/index/dell-codex-enterprise-partnership) ⭐️ 7.4/10

OpenAI 与戴尔宣布合作，将 OpenAI Codex（一款 AI 编程代理）引入混合与本地企业环境，使其能够跨数据和工作流安全部署。 此次合作使具有严格安全要求的企业能够利用 AI 驱动的编程辅助，而无需将数据发送至云端，从而弥合了 AI 能力与企业合规需求之间的差距。 此处 Codex 指的是 OpenAI 用于编程任务的 AI 代理，而不仅仅是底层语言模型。其部署模式支持混合与本地环境，这对金融、医疗等行业至关重要。

rss · OpenAI Blog · May 18, 10:00

**背景**: OpenAI Codex 是一套由 AI 驱动的编程代理，可自动化软件工程任务。许多企业倾向于本地或混合部署，以保持对敏感数据的控制并遵守法规，而纯云解决方案无法完全满足这些需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#enterprise`, `#partnership`, `#AI coding agents`

---

<a id="item-14"></a>
## [谷歌 I/O 前瞻：公司在基础模型竞赛中落后](https://www.technologyreview.com/2026/05/18/1137439/what-to-expect-from-google-this-week/) ⭐️ 7.4/10

在谷歌 I/O 大会上，该公司预计将展示其最新 AI 进展，同时承认在基础模型竞赛中落后于 OpenAI 等，位居第三。 本次预览为谷歌的 AI 策略设定了预期，并凸显了科技巨头在基础模型（生成式 AI 应用的基础）领导地位上的激烈竞争。 这篇文章是《麻省理工科技评论》的预览，指出谷歌在基础模型竞赛中排名第三可能会影响 I/O 上的公告和基调。

rss · MIT Tech Review · May 18, 17:35

**背景**: 基础模型是在海量数据集上训练的大型 AI 模型，能够完成文本生成、图像创建等多种任务。例如 OpenAI 的 GPT 系列和谷歌的 BERT。构建这类模型需要巨大的计算资源，而 OpenAI、谷歌等公司正在争夺这一领域的领先地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model</a></li>

</ul>
</details>

**标签**: `#Google I/O`, `#AI`, `#foundation models`, `#tech industry`

---

<a id="item-15"></a>
## [Files.md：Obsidian 的开源替代品](https://github.com/zakirullin/files.md) ⭐️ 7.2/10

Files.md 是一款新的开源 Markdown 笔记应用，在 Hacker News 上作为 Obsidian 的替代品被展示。目前处于测试阶段，可在 GitHub 上获取。 其重要性在于，Obsidian 虽然广受欢迎且让人感觉像开源，但实际上却是专有软件。一个开源替代品让用户对自己的数据和工作流程有更多控制权，而 HN 上的高参与度反映了强劲的需求。 Files.md 基于纯 Markdown 文件运行，采用不同的组织理念（一个想法一条笔记），目前处于测试阶段。它不是 Obsidian 的功能对等克隆，而是一种重新构思的笔记方法。

hackernews · zakirullin · May 18, 13:33 · [社区讨论](https://news.ycombinator.com/item?id=48179677)

**背景**: Obsidian 是一款流行的专有笔记应用，它以纯 Markdown 文件形式存储笔记，但其源代码不开放。许多用户希望有一个开源等效产品以实现数据主权和自定义。Files.md 旨在填补这一空白，同时提供独特的笔记方法论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Obsidian_(software)">Obsidian (software) - Wikipedia</a></li>
<li><a href="https://github.com/zakirullin/files.md">GitHub - zakirullin/ files . md : Your life in plain . md files · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论对开源替代品表示兴奋，一些用户指出 Obsidian 让人感觉像开源但实际上并非如此。与 Joplin 和原生 Qt 实现进行了比较。一位用户强调 Files.md 并非功能对等克隆，而是提供了独特的工作流程。

**标签**: `#open source`, `#note-taking`, `#obsidian alternative`, `#markdown editor`, `#dev tools`

---

<a id="item-16"></a>
## [Anduril 与 Meta 为军事用途原型 AR 头显，可指挥无人机打击](https://www.technologyreview.com/2026/05/18/1137412/inside-anduril-and-metas-quest-to-make-smart-glasses-for-warfare/) ⭐️ 7.2/10

Anduril 和 Meta 正在为美军原型设计一款增强现实头显，该头显可通过眼动追踪和语音命令让士兵指挥无人机打击，Anduril 副总裁 Quay Barnett 透露了这一进展。 此次合作标志着消费者 AR 技术军事化的重要一步，通过将 AI 驱动的决策支持与实时传感器数据集成，可能彻底改变战场指挥与控制方式。 该头显将结合 Meta 的硬件和 AI 工具与 Anduril 的 Lattice 系统，后者从数千个数据源汇总信息，通过专为作战条件设计的直观 AR/VR 界面提供可操作情报。

rss · MIT Tech Review · May 18, 16:01

**背景**: Anduril 是一家以 AI 驱动的监视和自主系统闻名的国防科技公司，而 Meta 则是大力投资增强现实和虚拟现实的社交媒体与科技巨头。美国陆军近期选择了 Anduril-Meta 团队和初创公司 Rivet 来替代微软问题重重的集成视觉增强系统（IVAS）项目，开发下一代 AR 头显。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.socialmediatoday.com/news/meta-joins-anduril-develop-ar-vr-headsets-us-military/749378/">Meta Partners With Anduril To Develop XR Headsets for US Military</a></li>
<li><a href="https://interestingengineering.com/military/meta-anduril-defense-partnership">Meta enters battlefield tech with AI, AR headset for the Army</a></li>
<li><a href="https://winbuzzer.com/2025/09/09/us-army-taps-anduril-meta-and-rivet-to-fully-replace-microsoft-in-multi-billion-dollar-ar-headset-program-xcxwbn/">US Army Taps Anduril - Meta and Rivet to Fully Replace Microsoft in...</a></li>

</ul>
</details>

**标签**: `#augmented reality`, `#defense technology`, `#Meta`, `#Anduril`, `#military AI`

---