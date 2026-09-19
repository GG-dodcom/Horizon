---
layout: default
title: "Horizon Summary: 2026-09-19 (ZH)"
date: 2026-09-19
lang: zh
---

> From 92 items, 6 important content pieces were selected

---

1. [陶哲轩：数学不只是证明，而 AI 正在考验这一点](#item-1) ⭐️ 8.4/10
2. [Brood War Bench：用《星际争霸》评测 AI 智能体的新基准](#item-2) ⭐️ 7.8/10
3. [Substack 文章主张几乎不应使用 AI 代笔写作](#item-3) ⭐️ 7.7/10
4. [阮一峰科技周刊第 413 期：再见了，React Native](#item-4) ⭐️ 7.2/10
5. [博客展示如何让 AI 生成的活动海报看起来像样](#item-5) ⭐️ 7.0/10
6. [PlanetScale 推出 Tin：仅限云端的 Postgres 全文搜索](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [陶哲轩：数学不只是证明，而 AI 正在考验这一点](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/) ⭐️ 8.4/10

陶哲轩（Terry Tao）发表了一篇博客文章，主张数学远不只是产出证明，其直觉性、协作性与概念性的维度应当获得比现在更广泛的认可。这篇文章在 Hacker News 上引发了大规模讨论（299 分、231 条评论），讨论很快转向 AI 正在如何动摇数学家的职业角色。 这篇文章的重要性在于：它恰好在一个关键时间点重新提出了一个文化问题——数学家究竟应当因何而受赞誉——而此时 AI 工具正在自动化数学工作中最“任务化”的那部分，而职业、终身教职与声望恰恰建立在这些任务之上。如果撰写证明不再是稀缺的人类贡献，那么这门学科的奖励机制、培养方式和自我认知都需要改变，这也会影响到所有知识型工作正被同样拆解的人。 这篇文章偏重反思而非技术论证，它提供的是框架而非具体的改革方案，也没有给出新的数学成果。围绕它的讨论反而更有实质内容：一位自称职业数学家的评论者表示，经过数周认真使用 AI，他找到了一个自己思考了数年的定理的证明，目前正在撰写成文；也有人认为，菲尔兹奖级别顶尖数学家所拥有的优势已经明显收窄。

hackernews · num42 · Sep 19, 06:28 · [社区讨论](https://news.ycombinator.com/item?id=49763928)

**背景**: 陶哲轩是加州大学洛杉矶分校的数学家、菲尔兹奖得主，也是该领域读者最多的学术博主之一，因此他的文章在塑造学科议题方面具有非同寻常的分量。评论串可追溯至 1900 年在巴黎举行的国际数学家大会，当时庞加莱与希尔伯特之间的争论促成了“证明”而非“直觉”成为该领域的主导标准。评论者还指出，菲尔兹奖设有年龄限制（授予 40 岁及以下的数学家），他们认为这在结构上奖励的是纯粹的脑力而非长期积累的理解力，因此 AI 的到来对该社群这一标杆性奖项构成了直接挑战。这场讨论的背景，是 AI 系统正快速进步，如今已能承担数学研究中相当大一部分工作。

**社区讨论**: 讨论情绪分歧明显，但总体上已默认这种冲击不可避免：多位评论者明确类比软件工程，认为 AI 已经能自动化数学中的各项任务，即便尚不能取代整个岗位——而对许多数学家来说，这些任务本身就是他们的工作，因此终身教职与职业晋升模式正在失效。一位职业数学家则以亲身经历给出乐观说法，称 AI 显著加速了证明的发现；还有人认为真正的危机比表面看起来更窄：它只是顶尖获奖者优势的缩小，因此现在反而是做数学家的最好时代。也有人感叹，陶哲轩所捍卫的数学中那种直觉与交流的一面，早已在学校和大学教育中被挤压殆尽。

**标签**: `#mathematics`, `#AI`, `#philosophy-of-math`, `#academic-research`, `#Terry-Tao`

---

<a id="item-2"></a>
## [Brood War Bench：用《星际争霸》评测 AI 智能体的新基准](https://bw.swerdlow.dev/report) ⭐️ 7.8/10

一个新的评测报告站点 Brood War Bench（bw.swerdlow.dev/report）提出了一套在《星际争霸：母巢之战》（StarCraft: Brood War）中评估 AI 系统的基准，并在 Hacker News 上被广泛讨论。该项目加入了一个规模虽小但正在成长的行列：把由大模型驱动或脚本控制的智能体放进完整的即时战略环境中，而不是让它们做静态的问答任务。 即时战略游戏恰好考验了当前大模型基准难以衡量的能力：长周期规划、不完全信息下的决策、资源管理以及在时间压力下行动，因此 Brood War 基准有可能暴露那些编程或推理排行榜看不到的智能体短板。它也反映出整个行业正在从单轮问答式的评测，转向以智能体在真实环境中的实际表现为标准。 《母巢之战》是一个要求极高的测试场：一局比赛要经历成千上万个游戏时刻，且存在战争迷雾；而智能体的表现很大程度上取决于接口设计和操作频率（APM）等条件，而不只是模型本身的质量。需要注意的是，该报告的页面正文并未包含在摘要内容中，因此本次无法独立核实该基准的具体任务设计、参评模型清单与评分方法。

hackernews · benswerd · Sep 19, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49766966)

**背景**: 《星际争霸：母巢之战》是暴雪于 1998 年推出的即时战略游戏，玩家需要在战争迷雾下建造基地、管理资源并指挥军队。它开放的 BWAPI 接口使其成为程序化机器人（bot）的常用平台，2010 年加州大学圣克鲁兹分校 Expressive Intelligence Studio 还举办过一届母巢之战 AI 锦标赛。此后 DeepMind 在《星际争霸 II》上训练出 AlphaStar，确立了即时战略游戏作为 AI 规划能力硬核测试的地位。而 LiveBench 等基准则通过抗数据污染、定期更新的任务，为语言模型评测发挥类似作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/SKTBrain/awesome-starcraftAI">Awesome StarCraft AI</a></li>
<li><a href="https://starcraft.ai/">StarCraft.AI</a></li>
<li><a href="https://livebench.ai/">LiveBench</a></li>

</ul>
</details>

**社区讨论**: 评论区整体气氛热烈：有读者怀旧地回忆起当年网吧里玩母巢之战的岁月以及由此结下的友谊；另一位则给出被广泛赞同的类比，把智能体架构映射到三大种族——Protoss 像是昂贵、需要你亲自微操的前沿编程智能体，Terran 像是可委派明确任务的多角色专家智能体组合，Zerg 则像是应用内大量廉价、为速度与成本优化的小型定制智能体。还有人补充了历史与技术背景：提到 2010 年 UC Santa Cruz 的 BWAPI 锦标赛，指出目前有一个机器人在天梯上击败了所有人，并提到 GoBench——它用 KataGo 作为 Elo 锚点，在 9×9 围棋上评测大模型。

**标签**: `#AI benchmark`, `#StarCraft`, `#LLM evaluation`, `#agentic AI`, `#game AI`

---

<a id="item-3"></a>
## [Substack 文章主张几乎不应使用 AI 代笔写作](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai) ⭐️ 7.7/10

Erich Grunewald 在 Substack 发表文章，主张人们几乎不应使用 AI 为他人撰写文本，并援引认知科学论据，包括 Eric Schwitzgebel 关于阅读生成文本与主动生成散文之间存在认知差异的观点。该文在 Hacker News 引发 111 条评论的讨论，争论 LLM 辅助写作在何时真正有帮助。 随着 LLM 融入日常写作流程，该文反驳了生成文本越快越好的假设，警告这可能削弱写作者对措辞和意义的投入。这场讨论对写作者、学生、职场人士以及试图定义健康人机协作方式的工具开发者都很重要。 文章的核心启发式——也在 Hacker News 讨论中得到呼应——是把 AI 用于你想要给自己看的文本，例如摘要、报告、把会议记录变成邮件草稿，而不是用于生产供他人消费的文本。评论者还提出更轻量的用法：让 AI 给出多种措辞以澄清自己的意图，或请求批评而非完整重写；不过这些仍属经验性做法，而非对照研究结论。

hackernews · erwald · Sep 19, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=49767937)

**背景**: Substack 是一个订阅制出版平台，成立于 2017 年，让作者可以直接向订阅者发送新闻信、播客和视频。文章论点涉及认知科学：认知卸载指把脑力任务委托给外部工具，而 MIT Media Lab 的《Your Brain on ChatGPT》等近期研究考察了 LLM 辅助写作是否会因减少主动投入而积累认知债务。Eric Schwitzgebel 的观点是，被动阅读一篇成品文本，并不等于逐字逐句构思散文时付出的生产性努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Substack">Substack - Wikipedia</a></li>
<li><a href="https://www.media.mit.edu/publications/your-brain-on-chatgpt/">Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task — MIT Media Lab</a></li>
<li><a href="https://arxiv.org/abs/2506.08872">[2506.08872] Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者大体同意：AI 用于私人理解信息比替他人写作更站得住脚。jameshart 将其概括为用 AI 写你希望别人替你写好的东西，而 foobarbecue 认为 LLM 生成的散文会掩埋作者本意，主要适合填充篇幅。其他人提出实用的折中方案，例如 wdutch 让 AI 给出多种表述来澄清自己的偏好，rectang 建议让 AI 批评而非完整重写，整体态度是细致权衡而非一概拒绝。patrickmay 还引用了文中 Schwitzgebel 关于阅读时点头认同与生产性生成文本之间存在差距的段落。

**标签**: `#AI writing`, `#LLM`, `#human-AI collaboration`, `#cognition`, `#writing craft`

---

<a id="item-4"></a>
## [阮一峰科技周刊第 413 期：再见了，React Native](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-413.html) ⭐️ 7.2/10

阮一峰在其博客上发布了科技爱好者周刊第 413 期，本期主题为「再见了，React Native」，汇总了一周内值得关注的科技与编程内容。同一篇文章还附有通知：从下周五开始的中秋与十一假期期间，周刊将休刊。 阮一峰的周刊是中文开发者社区中持续最久、信噪比最高的内容精选来源之一，因此以「再见了，React Native」为主题，实际上把前端与移动开发者之间的一场持续争论推到了台前：这个框架在新项目中是否仍值得选用。对于正在权衡 React Native、Flutter 与纯原生开发路线的团队来说，这一期的选题方向可作为社区情绪走向的参考信号。 目前可获取的摘录相当有限，只包含固定的开篇介绍句和休刊通知，因此本期围绕 React Native 的具体论述无法从现有文本中得到验证。该周刊每周五发布，属于链接精选式的聚合内容，而非原创技术分析。

rss · 阮一峰周刊 · Sep 18, 00:03

**背景**: 阮一峰是中国知名技术博客作者，因撰写介绍 ES6 JavaScript 标准的著作而为开发者所熟知。他的《科技爱好者周刊》已连续发布数百期，专门收集对程序员有价值的工具、文章与开源项目。React Native 是 Meta 于 2015 年开源的框架，允许开发者用 JavaScript 和 React 构建 iOS 与 Android 应用；近年来在 Flutter、原生开发以及更新的跨平台方案的竞争下，其采用前景一直存在争议。

**标签**: `#科技周刊`, `#React Native`, `#前端开发`, `#移动开发`, `#编程`

---

<a id="item-5"></a>
## [博客展示如何让 AI 生成的活动海报看起来像样](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) ⭐️ 7.0/10

john.hartnup.uk 于 2026 年 6 月 7 日发布的一篇博客文章，介绍了让 AI 生成的活动海报看起来不那么明显的机器感的一些实用技巧，并在 Hacker News 上引发了约 729 条评论的大规模讨论。文章对比了默认生成效果较差的输出与经过更好引导的示例，其中包括一个要求制作“90 年代 drum n bass 演出传单风格、带早期 3D/分形电脑图像”的海报的提示词。 随着 AI 图像生成器成为小型活动、俱乐部和社区组织者的常规工具，其默认审美究竟算可接受的成品还是“偷懒”的显眼标记，直接关系到设计师、客户以及创意工作的价值认知。这场讨论的意义在于，它把 AI 定位为不只是顶尖画师的替代品，更是廉价自由设计师的竞争者，从而重塑设计市场的最底层。 评论者指出，即便是改进后的示例仍带有暴露身份的渲染错误——例如一个线框球体在风格上契合早期 CGI 审美，但几何结构是错的，从而破坏了该风格赖以成立的错觉。另一个反复出现的观点是，模型会趋同于最直白的套路，因此“日式极简海报”这类提示词默认会生成樱花和风格化的日本国旗，而不是更不落俗套的构思。

hackernews · ereiamjh · Sep 19, 09:20 · [社区讨论](https://news.ycombinator.com/item?id=49764791)

**背景**: 基于扩散模型的 AI 图像生成工具（如 Midjourney、DALL·E、Stable Diffusion 及其后续版本）能把文本提示词转成图像，其输出结果在很大程度上取决于提示词以及所提供的风格参考。由于这些模型是在大规模抓取的数据集上训练的，它们的“默认”外观往往反映了数据中最常见的联想，因此未经引导的提示词常常产出泛泛而谈或刻板化的图像。这篇博客本质上是一份技巧指南，教人如何把模型从这种默认状态引导向特定的视觉意图。

**社区讨论**: 讨论情绪明显分化：一位评论者（ajjenkins）根据自身经验认为，Fiverr 上普通的低价设计师水平明显不如 AI，因此拿来比较的标准本身不现实。另一些人（vova_hn2、JSR_FDED）则反驳说问题在于概念层面和社会层面——模型总会退回到诸如“日本=樱花”这类俗套联想，而那种一眼可辨的默认风格传递出“假装很用心、实则偷懒”的信号。mrob 补充了技术层面的批评，指出细节丰富的示例会在渲染错误上翻车；jstummbillig 则为 AI 半辩护，认为普通人的设计品味本身就很差。

**标签**: `#AI image generation`, `#creative AI`, `#design`, `#applied AI`, `#Hacker News`

---

<a id="item-6"></a>
## [PlanetScale 推出 Tin：仅限云端的 Postgres 全文搜索](https://planetscale.com/blog/introducing-tin) ⭐️ 7.0/10

PlanetScale 为其托管版 Postgres 推出了名为 Tin（Text INdex 的缩写）的全文搜索能力。启用 tin 扩展后，会新增一种为搜索优化的倒排索引类型、BM25 相关性排序，以及一套名为 TINQL 的专用查询语言。 此举正处在托管数据库厂商争相为 Postgres 加装一流搜索能力的热潮之中，此前已有 ParadeDB 的 pg_search、Timescale 的 pg_textsearch 以及 Databricks/Neon 的 Lakebase Search。对于已经使用 PlanetScale 的团队来说，这可能免去额外自建 Elasticsearch 类服务的需要，但也会加深对平台的锁定，并让人质疑自建 Postgres 是否还能获得同等的性能。 最受关注的限制在于：Tin 并非以通用扩展的形式发布，它只在 PlanetScale 的云服务上运行；对应的开源本地版本 `lead` 主要只用于测试查询语法，性能特征并不相同。Tin 采用 BM25 排序——即 Lucene 与 Elasticsearch 广为使用的评分模型——而非 Postgres 内置的 ts_rank。

hackernews · ksec · Sep 19, 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49766611)

**背景**: PostgreSQL 多年来一直通过 tsvector 和 tsquery 类型、ts_rank 排序函数以及 GIN/GiST 索引提供内置全文搜索，但其相关性评分通常被认为弱于专用搜索引擎所使用的基于 BM25 的系统。BM25 是一种概率排序函数，会综合考量词频、文档长度以及某个词在整个语料库中的稀有程度。PlanetScale 是一个托管关系型数据库平台，以大规模 Vitess/MySQL 著称，如今也托管 Postgres。ParadeDB、Timescale 等厂商一直在构建把倒排索引和 BM25 排序直接引入数据库内部的 Postgres 扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planetscale.com/docs/postgres/search">TIN : PlanetScale Postgres Search - PlanetScale</a></li>
<li><a href="https://news.ycombinator.com/item?id=49766611">Tin : full - text search for Postgres | Hacker News</a></li>
<li><a href="https://www.postgresql.org/docs/current/textsearch.html">PostgreSQL: Documentation: 18: Chapter 12. Full Text Search</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论普遍持怀疑态度，不少人质疑：既然 Postgres 核心已提供基于 tsvector/tsquery 的成熟内置全文搜索方案，为何还要采用一个第三方的、仅限云端且带有“AI 随手写出来”色彩的产品。也有人把这则发布视为 AI 辅助编码提升生产力所推动的行业趋势的一部分，并列举了 ParadeDB、Timescale 和 Databricks；同时指出虽然存在本地版 `lead`，但性能并不相同。讨论中还有人关注 SQLite 的 FTS 与 Lucene 风格查询支持，以及 Tin 未来是否会开源，以便独立测试其性能。

**标签**: `#Postgres`, `#Full-Text Search`, `#Databases`, `#Dev Tools`, `#PlanetScale`

---