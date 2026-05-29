---
layout: default
title: "Horizon Summary: 2026-05-29 (EN)"
date: 2026-05-29
lang: en
---

> From 115 items, 29 important content pieces were selected

---

1. [CodeView: Efficient Browser Rendering of Massive Code Diffs](#item-1) ⭐️ 9.0/10
2. [PyTorch Profiler Beginner's Guide](#item-2) ⭐️ 9.0/10
3. [Claude Code v2.1.154: Opus 4.8 and Dynamic Multi-Agent Workflows](#item-3) ⭐️ 8.8/10
4. [Humans Should Retain Coding Skills Despite AI](#item-4) ⭐️ 8.7/10
5. [AI Production Growing at Over 2000% per Year, Says Tyler Cowen](#item-5) ⭐️ 8.7/10
6. [SQLite AGENTS.md: Rejects Agentic Code, Welcomes AI Bug Reports](#item-6) ⭐️ 8.6/10
7. [Anthropic's run-rate revenue hits $47B in Series H](#item-7) ⭐️ 8.5/10
8. [Claude Opus 4.8: A Modest but Honest Incremental Update](#item-8) ⭐️ 8.5/10
9. [Cognition's Walden Yan & OpenInspect's Cole Murray on Async Agents](#item-9) ⭐️ 8.5/10
10. [Braintrust uses Codex (GPT-5.5) to auto-generate code from requests](#item-10) ⭐️ 8.4/10
11. [Mistral AI Now Summit Highlights On-Prem Strategy and Model Gap](#item-11) ⭐️ 8.2/10
12. [Eric Seufert Interview: AI Models, Ads, and Humanity's Future](#item-12) ⭐️ 8.2/10
13. [Microsoft 0-day feud escalates as researcher threatens another exploit dump](#item-13) ⭐️ 8.1/10
14. [Datasette 1.0a31 Adds SQL Write Queries and Saved Stored Queries](#item-14) ⭐️ 8.1/10
15. [Claude Code v2.1.157: Automatic Plugin Loading and Fixes](#item-15) ⭐️ 8.0/10
16. [OpenAI's Playbook for Trustworthy Third-Party AI Evaluations](#item-16) ⭐️ 8.0/10
17. [AI and frontend's lost decade debate](#item-17) ⭐️ 7.9/10
18. [GTA 6 Developers Form Union at Rockstar Games](#item-18) ⭐️ 7.9/10
19. [Liquid AI Unveils 8B-A1B MoE Model Trained on 38T Tokens](#item-19) ⭐️ 7.8/10
20. [Stratechery Roundup: Luce, AI Monetization, China Mobility](#item-20) ⭐️ 7.8/10
21. [Bijou64: A New Variable-Length Integer Encoding](#item-21) ⭐️ 7.5/10
22. [OpenAI's Frontier Governance Framework](#item-22) ⭐️ 7.5/10
23. [Learning AI Agents by Building One: A Two-Day Journey](#item-23) ⭐️ 7.5/10
24. [SQLite Enough for Durable Workflows?](#item-24) ⭐️ 7.4/10
25. [Framework 12 hard to justify against Apple Silicon](#item-25) ⭐️ 7.4/10
26. [Dead Economy Theory: AI Overcapacity Stagnation](#item-26) ⭐️ 7.2/10
27. [Boston Children's Uses AI to Diagnose 40+ Rare Diseases](#item-27) ⭐️ 7.2/10
28. [AI Hype Sparks Boos at Graduation](#item-28) ⭐️ 7.0/10
29. [Cognition Labs raises $1B at $26B valuation](#item-29) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CodeView: Efficient Browser Rendering of Massive Code Diffs](https://pierre.computer/writing/on-rendering-diffs) ⭐️ 9.0/10

Pierre published a detailed technical article explaining the implementation of CodeView and the @pierre/diffs package, which enables zero-blanking diff rendering at any scale entirely in the browser. Code review tools that handle very large diffs efficiently are crucial for developer productivity, and this work demonstrates techniques that could be adopted by platforms like GitHub to improve their own diff rendering performance. The solution leverages deferred syntax highlighting and virtualized scrolling to handle huge diffs without blank gaps, and the code is available as an open-source package called @pierre/diffs.

hackernews · amadeus · May 29, 19:04 · [Discussion](https://news.ycombinator.com/item?id=48327809)

**Background**: Code diffs are a fundamental part of code review, showing changes between file versions. Rendering them efficiently in a browser is challenging because large diffs (thousands of lines) can cause performance issues like slow scrolling and blank spaces due to synchronous syntax highlighting and heavy DOM manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://pierre.computer/writing/on-rendering-diffs">On Rendering Diffs :: Pierre Computer Company</a></li>
<li><a href="https://diffs.com/docs">Diffs, from Pierre</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the article's clarity and technical depth, with some noting that the optimizations could be applied to other domains like CAD model diffs. One user disagreed about the necessity of smooth scrolling on mobile, arguing that stuttery diff scrolling feels poor on high refresh rate mobile devices.

**Tags**: `#diff rendering`, `#optimization`, `#web performance`, `#software engineering`, `#code review`

---

<a id="item-2"></a>
## [PyTorch Profiler Beginner's Guide](https://huggingface.co/blog/torch-profiler) ⭐️ 9.0/10

Hugging Face published a beginner's guide to using PyTorch's built-in torch.profiler for profiling and optimizing deep learning model performance. Performance optimization is critical for deep learning practitioners, and this guide makes profiling accessible, helping developers identify bottlenecks and improve training/inference efficiency. The blog post covers basic usage of torch.profiler, how to interpret output such as operator-level traces and GPU utilization, and common optimization strategies.

rss · Hugging Face Blog · May 29, 00:00

**Background**: Profiling is the process of measuring resource usage (e.g., time, memory) during program execution. PyTorch's profiler supports tracing CPU operations, GPU kernels, and memory events, enabling developers to pinpoint performance bottlenecks in training loops.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html">PyTorch Profiler — PyTorch Tutorials 2.12.0+cu130 documentation</a></li>
<li><a href="https://docs.pytorch.org/docs/stable/profiler.html">torch.profiler — PyTorch 2.12 documentation</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#profiling`, `#performance optimization`, `#deep learning`, `#tools`

---

<a id="item-3"></a>
## [Claude Code v2.1.154: Opus 4.8 and Dynamic Multi-Agent Workflows](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) ⭐️ 8.8/10

Claude Code v2.1.154 introduces Opus 4.8 with high effort default, dynamic multi-agent workflows that orchestrate tens to hundreds of agents, and cost/speed optimizations including fast mode at 2x standard rate for 2.5x speed. This release significantly enhances Claude Code's capability for complex, large-scale tasks through multi-agent orchestration, while making powerful inference more affordable. It positions Claude Code as a more competitive tool for autonomous software development and workflow automation. The lean system prompt is now default for all models except Haiku, Sonnet, and Opus 4.7 and earlier. Claude now reserves multiple-choice questions for decisions it truly cannot make, reducing unnecessary queries. The `/simplify` command now runs a cleanup-only review instead of the full bug-hunting code review.

github · ashwin-ant · May 28, 18:00

**Background**: Claude is a series of large language models by Anthropic, trained with constitutional AI to improve ethical compliance. The Opus models are the most capable in each generation, and Opus 4.8 improves tool use and instruction following. Multi-agent workflows allow multiple AI agents to collaborate on complex tasks, with dynamic routing and state management.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4">Claude Opus 4</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8</a></li>
<li><a href="https://medium.com/@kanerika/multi-agent-workflows-a-practical-guide-to-design-tools-and-deployment-3b0a2c46e389">Multi-Agent Workflows: A Practical Guide to Design, Tools, and Deployment | by Kanerika Inc | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#developer tools`, `#Claude`, `#workflow automation`

---

<a id="item-4"></a>
## [Humans Should Retain Coding Skills Despite AI](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/) ⭐️ 8.7/10

The blog post argues that software developers should retain hands-on coding skills even as AI coding assistants become powerful, warning against over-reliance that could erode essential human understanding of code. This debate is significant as AI-assisted coding tools like GitHub Copilot and Claude Artifacts are rapidly adopted, potentially shifting the role of software engineers from coders to product managers and raising questions about skill degradation and long-term software quality. The author notes that the bottleneck in coding is human understanding, not code output; losing coding skills through over-reliance on AI could undermine developers' ability to design robust systems. The post emphasizes that abstraction and decomposition are key tools that humans have not fully mastered.

hackernews · tosh · May 29, 12:12 · [Discussion](https://news.ycombinator.com/item?id=48322118)

**Background**: With the rise of large language models (LLMs) capable of generating code, many developers now use AI agents to write large portions of their codebases. This has sparked debate about whether fundamental coding skills remain necessary or whether the role will shift to higher-level oversight and product thinking.

**Discussion**: Hacker News commenters express varied perspectives: some use agents for extensive refactoring while closely directing them (simonw), others argue the focus should be on retaining 'taste' rather than 'skill' (adamtaylor_13), and one commenter notes shifting focus to product management and design (paulmooreparks). There is agreement that understanding remains the key bottleneck (CraigJPerry).

**Tags**: `#AI-assisted coding`, `#software engineering`, `#skill retention`, `#coding agents`, `#product management`

---

<a id="item-5"></a>
## [AI Production Growing at Over 2000% per Year, Says Tyler Cowen](https://feeds.feedblitz.com/~/957435731/0/marginalrevolution~AI-in-gdp.html) ⭐️ 8.7/10

Tyler Cowen estimates that quality-adjusted AI production in the US grew at over 2000% per year in 2024 and 2025, driven by data-center capacity, hardware efficiency, and algorithmic progress, putting nominal AI GDP at about $250 billion. This suggests AI is contributing to economic growth much faster than official statistics capture, potentially reshaping GDP measurement and implying significant future productivity gains. The estimate treats AI as a coherent sector, with algorithmic progress being the largest driver, followed by hardware efficiency and data-center expansion. The 2000% growth is a quality-adjusted figure, meaning it accounts for rapid improvements in AI capabilities.

rss · Marginal Revolution · May 28, 17:19

**Background**: Quality-adjusted production measures account for improvements in output quality over time, commonly used for technology goods like computers. Measuring AI's economic contribution is challenging because many AI services are free or have rapidly falling costs. Tyler Cowen is a prominent economist at George Mason University and a prolific blogger.

<details><summary>References</summary>
<ul>
<li><a href="https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress">The least understood driver of AI progress | Epoch AI</a></li>
<li><a href="https://futuretech.mit.edu/news/what-drives-progress-in-ai-trends-in-algorithms">What drives progress in AI ? Trends in Algorithms</a></li>

</ul>
</details>

**Discussion**: Comments express both excitement and skepticism. Some question the math behind 2000% growth, while others debate implications for GDP measurement and note that AI is often an intermediate good. The overall sentiment is engaged and divided.

**Tags**: `#AI`, `#GDP`, `#economics`, `#productivity`, `#algorithmic progress`

---

<a id="item-6"></a>
## [SQLite AGENTS.md: Rejects Agentic Code, Welcomes AI Bug Reports](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.6/10

SQLite has added an AGENTS.md file to its repository clarifying that it does not accept agentic code contributions but welcomes agentic bug reports and documentation patches. Additionally, the project has split AI-generated bug reports into a separate SQLite Bug Forum due to overwhelming volume. This policy sets a precedent for open-source projects grappling with the influx of AI-generated contributions, balancing innovation with quality control. It may influence how other projects define acceptable AI involvement in their development processes. The AGENTS.md file originally stated 'does not currently accept agentic code,' but the word 'currently' was removed to strengthen the statement. The new SQLite Bug Forum (sqlite.org/bugs/forum) was created to handle AI-generated bug reports, with D. Richard Hipp actively addressing issues there.

rss · Simon Willison · May 27, 23:44

**Background**: Agentic coding refers to the use of autonomous AI agents that can plan, write, test, and modify code with minimal human intervention, unlike traditional coding assistants. SQLite is a widely-used embedded database library with strict quality standards and legal requirements for contributions. The project's policy reflects concerns about code quality, legal ownership, and maintainability of AI-generated code.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>
<li><a href="https://simonwillison.net/2026/May/27/sqlite-agents/">sqlite AGENTS . md | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#ai-agents`, `#open-source`, `#policy`

---

<a id="item-7"></a>
## [Anthropic's run-rate revenue hits $47B in Series H](https://simonwillison.net/2026/May/29/anthropic/#atom-everything) ⭐️ 8.5/10

Anthropic disclosed in its $65B Series H announcement that its annualized run-rate revenue crossed $47 billion in May 2026, up from $9B at end of 2025 and $30B in April 2026. This demonstrates extraordinary growth for an AI company, potentially surpassing any other company in history for organic revenue scaling at this level, indicating strong enterprise adoption of AI. The $47B figure is an annualized projection based on current monthly revenue multiplied by 12; Anthropic had previously reported $14B run-rate in February 2026 and $9B at end of 2025.

rss · Simon Willison · May 29, 01:23

**Background**: Run-rate revenue is a non-GAAP metric that extrapolates current revenue over a full year, often used by high-growth startups to convey momentum. Anthropic has consistently disclosed run-rate revenue in funding announcements, providing transparency on its growth trajectory.

**Discussion**: The article notes skepticism from Ed Zitron about the earlier $30B figure, questioning whether he will update for $47B. Some dismiss the numbers as self-reported, but the author argues that lying in fundraising documents would constitute securities fraud.

**Tags**: `#Anthropic`, `#AI business`, `#revenue`, `#funding`, `#industry trends`

---

<a id="item-8"></a>
## [Claude Opus 4.8: A Modest but Honest Incremental Update](https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything) ⭐️ 8.5/10

Anthropic released Claude Opus 4.8, describing it as a modest but tangible improvement over its predecessor with a focus on honesty. The model shows a fourfold reduction in allowing code flaws to pass unremarked and achieves the lowest hallucination rate across benchmarks by abstaining on uncertain questions. Anthropic's honest framing of a minor upgrade is refreshing in an industry often dominated by hype, setting a positive precedent for transparent communication. The emphasis on honesty aligns with broader efforts to make AI models more reliable and trustworthy. Pricing remains unchanged at $5 per million input tokens and $25 per million output tokens, with fast mode now at $10/$50 per million (down from $30/$150). New features include mid-conversation system messages, a 1M token context window, and 128K max output tokens. The training data cutoff is January 2026.

rss · Simon Willison · May 28, 23:59

**Background**: Claude Opus is Anthropic's flagship model series, known for strong reasoning and safety features. AI labs typically release models with grand claims, but incremental improvements are common. Honesty in AI helps reduce hallucinations and unsupported claims, improving user trust. Mid-conversation system messages allow dynamic instruction updates without restarting prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8">What's new in Claude Opus 4.8 - Claude API Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude API Docs</a></li>
<li><a href="https://github.blog/changelog/2026-05-28-claude-opus-4-8-is-generally-available-for-github-copilot/">Claude Opus 4.8 is generally available for GitHub Copilot - GitHub Changelog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#incremental improvement`, `#honesty`

---

<a id="item-9"></a>
## [Cognition's Walden Yan & OpenInspect's Cole Murray on Async Agents](https://www.latent.space/p/cognition) ⭐️ 8.5/10

This article discusses the era of asynchronous AI coding agents, revealing that 80% of Devin's commits come from spec-to-PR workflows, and explores agent memory, full VM isolation, and product managers shipping code. This trend signifies a shift toward more autonomous software development, where AI agents handle coding from specification to pull request, potentially accelerating development and altering the roles of developers and PMs. The article covers specific techniques such as full virtual machine isolation for agents, session tracking in spec-to-PR workflows, and agent memory systems that enable context recall across sessions.

rss · Latent Space · May 28, 18:41

**Background**: AI coding agents like Devin from Cognition Labs can autonomously complete software development tasks. A spec-to-PR workflow involves an AI agent generating a pull request directly from a specification document. Agent memory systems, such as MEMORY.md in Claude Code or notepads in Cursor, help AI maintain context. These technologies are enabling more asynchronous and efficient software engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Devin_AI">Devin AI - Wikipedia</a></li>
<li><a href="https://blog.cloudflare.com/introducing-agent-memory/">Agents that remember: introducing Agent Memory</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#coding agents`, `#Devin`, `#async workflows`, `#software engineering`

---

<a id="item-10"></a>
## [Braintrust uses Codex (GPT-5.5) to auto-generate code from requests](https://openai.com/index/braintrust) ⭐️ 8.4/10

Braintrust engineers are using OpenAI's Codex, powered by GPT-5.5, to automatically generate code from customer requests, accelerating their experimentation and development workflows. This integration demonstrates a practical real-world application of large language models in software engineering, potentially reducing development time and enabling faster iteration based on customer feedback. Codex is a suite of AI-driven coding agents that can run locally or in IDEs, and the version used by Braintrust is powered by the GPT-5.5 model, which reportedly produces 52.5% fewer hallucinated claims than previous models on high-stakes prompts.

rss · OpenAI Blog · May 29, 12:00

**Background**: OpenAI Codex is a coding agent that automates software engineering tasks, allowing developers to focus on higher-level design. GPT-5.5 is OpenAI's frontier model designed for complex professional workloads, offering stronger reasoning and reduced hallucinations. Braintrust is a platform that helps product teams run experiments and gather customer feedback.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-5-5-instant/">GPT - 5 . 5 Instant: smarter, clearer, and more personalized | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Codex`, `#GPT-5.5`, `#software engineering`, `#automation`

---

<a id="item-11"></a>
## [Mistral AI Now Summit Highlights On-Prem Strategy and Model Gap](https://koenvangilst.nl/lab/mistral-ai-now-summit) ⭐️ 8.2/10

At the Mistral AI Now Summit, the company showcased its on-premise AI deployment strategy for European enterprises, citing partnerships with BNP Paribas and Abanca. However, community observers noted that Mistral's models, particularly its 120B-parameter small model, have fallen behind competitors like Gemma4 and Qwen3.6 in reasoning tasks. This matters because Mistral is a key European AI player, and its on-prem focus addresses data sovereignty needs for regulated industries. However, the perceived technological lag raises concerns about Europe's competitiveness in AI against US and Chinese labs. Mistral's 'small' 120B model is roughly four times larger than competitors' effective small models and still underperforms. The summit also featured partners like Microsoft, Accenture, and EY, indicating a broad ecosystem push.

hackernews · vnglst · May 29, 16:22 · [Discussion](https://news.ycombinator.com/item?id=48325340)

**Background**: Mistral AI is a French company known for open-weight LLMs like Mistral 7B. On-premise AI deployment allows companies to run models on their own infrastructure, ensuring data privacy and compliance. This contrasts with cloud-based services from US providers. The summit focused on European AI autonomy.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/">Frontier AI LLMs, assistants, agents, services | Mistral AI</a></li>
<li><a href="https://huggingface.co/mistralai/Mistral-7B-v0.1">mistralai/ Mistral -7B-v0.1 · Hugging Face</a></li>
<li><a href="https://ubuntu.com/blog/ai-on-prem">AI on - prem : what should you know? | Ubuntu</a></li>

</ul>
</details>

**Discussion**: Comments were mixed: some praised Mistral's on-prem strategy and strong enterprise partnerships, while others expressed disappointment over the company's lack of progress in reasoning models compared to Chinese labs like DeepSeek. One attendee noted impressive attendance from European corporate leaders and a wide range of partners.

**Tags**: `#Mistral`, `#AI models`, `#on-prem AI`, `#European AI`, `#LLM deployment`

---

<a id="item-12"></a>
## [Eric Seufert Interview: AI Models, Ads, and Humanity's Future](https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/) ⭐️ 8.2/10

Stratechery published an interview with analyst Eric Seufert discussing how generative AI models, particularly Meta's Llama series, intersect with advertising to create positive outcomes for humanity. This interview provides deep analytical insights into the economic and societal implications of open-source AI models and advertising, offering a nuanced perspective on AI's potential to benefit humanity rather than just disrupt. Seufert argues that Meta's foundational models are crucial because they are open-source and can be fine-tuned for advertising optimization, which aligns incentives for both businesses and users.

rss · Stratechery · May 28, 10:00

**Background**: Foundational models are large-scale AI models pre-trained on vast data that can be adapted for various tasks. Meta's Llama models are a prominent open-source example, with versions like Llama 2 and Llama 4 offering different parameter sizes. The interview explores how these models can be leveraged in advertising to improve targeting and relevance while reducing costs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama_(language_model)">Llama (language model ) - Wikipedia</a></li>
<li><a href="https://www.llama.com/">Industry Leading, Open-Source AI | Llama</a></li>
<li><a href="https://rohit0221.github.io/GenAI/GenAI-basics/Foundational-Models/">Foundation Models - Rohit Sharma</a></li>

</ul>
</details>

**Tags**: `#AI`, `#advertising`, `#generative AI`, `#Meta`, `#models`

---

<a id="item-13"></a>
## [Microsoft 0-day feud escalates as researcher threatens another exploit dump](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085) ⭐️ 8.1/10

Security researcher (known as 'rolph') threatens to release additional Windows zero-day exploits, escalating a feud with Microsoft over alleged violations of responsible disclosure and compensation. This dispute highlights ongoing tensions between vendors and security researchers over coordinated vulnerability disclosure (CVD) practices, potentially putting Windows users at risk from unmitigated exploits. The researcher previously released a set of exploits dubbed 'Red Sun', 'Undefend', and 'Blue Hammer', with 'Yellow Key' being the latest. Microsoft has disputed the researcher's claims about compensation.

hackernews · Cider9986 · May 29, 19:37 · [Discussion](https://news.ycombinator.com/item?id=48328175)

**Background**: Coordinated Vulnerability Disclosure (CVD) is a process where a researcher privately informs a vendor of a vulnerability, allowing time for a fix before public disclosure. The researcher claims Microsoft violated this norm by taking legal action and failing to compensate. Microsoft has not publicly shown the correspondence.

**Discussion**: Commenters are divided: some sympathize with the researcher, arguing that CVD is a two-way street and that Microsoft's denial is harmful to customers. Others worry about the impact of exploit dumps on end users and predict legal consequences for the researcher.

**Tags**: `#security`, `#vulnerability-disclosure`, `#Microsoft`, `#0day`, `#infosec`

---

<a id="item-14"></a>
## [Datasette 1.0a31 Adds SQL Write Queries and Saved Stored Queries](https://simonwillison.net/2026/May/29/datasette/#atom-everything) ⭐️ 8.1/10

Datasette 1.0a31, released on May 29, 2026, introduces the ability for authorized users to execute SQL write queries (INSERT, UPDATE, DELETE) and to save stored queries (previously called 'canned queries') either privately or for shared use. This release significantly expands Datasette from a read-only data exploration tool to one that supports write operations, enabling users to directly modify data through a web interface. The saved stored queries feature improves collaboration by allowing teams to share reusable SQL snippets. Write queries are permission-controlled; for example, executing CREATE TABLE requires a separate 'create-table' permission. The saved stored queries feature replaces the previous 'canned queries' and supports both private and shared visibility.

rss · Simon Willison · May 29, 03:32

**Background**: Datasette is an open-source tool for exploring and publishing data, allowing users to import data from various sources (CSV, JSON, databases) and automatically provide an interactive web interface and API for querying. Previously, Datasette only supported read-only SQL queries; write operations were not available. The concept of 'canned queries' allowed pre-defined queries to be saved and reused, now renamed and enhanced as 'stored queries'.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/">Datasette : An open source multi- tool for exploring and publishing data</a></li>
<li><a href="https://docs.datasette.io/en/stable/sql_queries.html">Running SQL queries - Datasette documentation</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#data exploration`, `#SQL`, `#open source`, `#software release`

---

<a id="item-15"></a>
## [Claude Code v2.1.157: Automatic Plugin Loading and Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.157) ⭐️ 8.0/10

Claude Code v2.1.157 introduces automatic loading of plugins from .claude/skills directories, a new plugin init command for scaffolding, and numerous fixes for worktree handling, telemetry, and image processing. This release simplifies plugin management for developers using Claude Code, making it easier to extend the tool with community or custom skills without needing a marketplace. The many bug fixes, especially around worktrees and session management, improve reliability for users relying on Claude Code for complex multi-branch development workflows. Automatic plugin loading scans .claude/skills directories on startup, eliminating manual import steps. The new plugin init command generates a starter plugin structure in that directory. Additionally, several fixes address issues with Git worktrees, such as leaving them unlocked for cleanup and enabling mid-session switching.

github · ashwin-ant · May 29, 20:20

**Background**: Claude Code is an AI-powered coding assistant developed by Anthropic, integrated into IDEs and terminals to help developers write and debug code. It supports a plugin system (skills) that allows users to add custom capabilities. Git worktrees are a feature that allows multiple working directories for the same repository, enabling parallel work on different branches.

<details><summary>References</summary>
<ul>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git - worktree Documentation</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding tool`, `#plugin system`, `#release notes`, `#developer tools`

---

<a id="item-16"></a>
## [OpenAI's Playbook for Trustworthy Third-Party AI Evaluations](https://openai.com/index/trustworthy-third-party-evaluations-foundations) ⭐️ 8.0/10

OpenAI has published a playbook providing guidance on conducting trustworthy third-party evaluations of frontier AI systems, focusing on capabilities, safeguards, and validity. This playbook sets a standard for independent evaluations, crucial for ensuring safety and trustworthiness as AI capabilities advance. It could influence regulatory frameworks and industry practices for frontier AI models. The guidance covers three core dimensions: capabilities (what the model can do), safeguards (how well it avoids harmful outputs), and validity (whether evaluations accurately reflect real-world performance).

rss · OpenAI Blog · May 29, 00:00

**Background**: Frontier AI systems are advanced models with capabilities that could pose significant risks. Third-party evaluations are conducted by independent organizations to provide unbiased assessments of these systems' safety and performance.

**Tags**: `#AI evaluation`, `#frontier AI`, `#safety`, `#OpenAI`, `#trustworthy AI`

---

<a id="item-17"></a>
## [AI and frontend's lost decade debate](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/) ⭐️ 7.9/10

An article argues that AI is causing a repeat of frontend's 'lost decade' of accidental complexity, but community comments counter that the lost expertise was in navigating unnecessary complexity and that AI democratizes building. This debate matters because it questions whether AI simplifies or complicates frontend development, impacting how developers approach web building and the skills that remain valuable. The article laments the loss of deep expertise in browser quirks and CSS specificity, while commenters argue those skills were largely about navigating accidental complexity, not essential knowledge.

hackernews · xyzal · May 29, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48321631)

**Background**: Accidental complexity is a term from Fred Brooks' 1986 paper 'No Silver Bullet,' referring to complexity that arises from tools and methods, not the problem itself. The frontend 'lost decade' describes a period when frameworks added layers of complexity for developers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Accidental_complexity">Accidental complexity</a></li>

</ul>
</details>

**Discussion**: Commenters like kristianc and kangalioo argue that the expertise lost was in navigating unnecessary complexity, and that AI enabling more people to build is a positive tradeoff. ElProlactin notes that mediocrity existed before AI and questions if quality has truly declined.

**Tags**: `#AI`, `#frontend development`, `#software engineering`, `#web development`, `#developer experience`

---

<a id="item-18"></a>
## [GTA 6 Developers Form Union at Rockstar Games](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/) ⭐️ 7.9/10

Developers working on Grand Theft Auto 6 have announced the formation of a union at Rockstar Games, demanding pay transparency, flexible working, and an end to compulsory overtime (crunch). This unionization effort highlights the severe pay gap between game development and big tech, and addresses the pervasive crunch culture. It could set a precedent for improving labor conditions across the entire gaming industry. The union's demands focus on pay transparency, flexible working arrangements, and an end to crunch, which refers to extended periods of unpaid overtime. The announcement comes amid ongoing scrutiny of Rockstar's labor practices, particularly during GTA 6 development.

hackernews · AndrewKemendo · May 29, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48324499)

**Background**: Crunch culture is a common practice in the video game industry where developers work 65–80 hours per week for extended periods, often without extra pay. Rockstar Games has faced criticism in the past for such conditions, and unionization in the U.S. tech sector remains rare due to factors like outsourcing and H1B visa programs.

**Discussion**: Commenters noted the stark pay disparity between game dev and big tech, criticized crunch as predatory, and expressed support for the union. Some highlighted the difficulty of unionizing in America due to outsourcing and H1B programs, with one sharing an example of an underpaid architect on an H1B visa.

**Tags**: `#unionization`, `#game development`, `#software engineering`, `#labor`, `#Rockstar Games`

---

<a id="item-19"></a>
## [Liquid AI Unveils 8B-A1B MoE Model Trained on 38T Tokens](https://www.liquid.ai/blog/lfm2-5-8b-a1b) ⭐️ 7.8/10

Liquid AI has announced a new 8 billion parameter mixture-of-experts (MoE) model with 1 billion active parameters, trained on 38 trillion tokens. This model pushes the boundaries of efficient language modeling by using a highly sparse MoE architecture; however, early community tests show it underperforms on non-benchmark tasks like bug fixing, raising questions about real-world applicability. The model uses a total of 8 billion parameters but only activates 1 billion during inference, achieving extreme sparsity; it was trained on 38 trillion tokens, far exceeding the Chinchilla optimal scaling law, which suggests 20 times the active parameters, not 1800 times.

hackernews · simjnd · May 29, 16:19 · [Discussion](https://news.ycombinator.com/item?id=48325306)

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) and a gating mechanism to select which experts to activate per input, enabling larger total parameters with lower computational cost. Training on a very large number of tokens can lead to overfitting or 'overtraining' if not balanced with model capacity.

**Discussion**: Community reactions are mixed: some users report that the model underperforms on bug-fixing benchmarks compared to older models, while others are excited about its potential for vision-language-action models. Concerns about overtraining are raised due to the 38T token count.

**Tags**: `#AI`, `#LLM`, `#MoE`, `#Liquid AI`, `#Model Evaluation`

---

<a id="item-20"></a>
## [Stratechery Roundup: Luce, AI Monetization, China Mobility](https://stratechery.com/2026/luceing-their-mind/) ⭐️ 7.8/10

Ben Thompson's weekly roundup discusses why Luce is disliked, strategies for monetizing AI answers, and social mobility trends in China. AI monetization is a critical question for tech companies, and Thompson's analysis offers valuable insights into how to charge for AI-generated answers. The piece covers three distinct topics: the backlash against Luce, a framework for monetizing AI responses, and data on upward mobility in China.

rss · Stratechery · May 29, 17:00

**Background**: Stratechery is a well-known tech analysis blog by Ben Thompson. Weekly roundups compile his best content from the past week. Luce might refer to a product or public figure, but details are unclear. AI monetization is a hot topic as companies seek to profit from generative AI.

**Tags**: `#AI monetization`, `#Stratechery`, `#China social mobility`, `#tech business`, `#weekly roundup`

---

<a id="item-21"></a>
## [Bijou64: A New Variable-Length Integer Encoding](https://www.inkandswitch.com/tangents/bijou64/) ⭐️ 7.5/10

The article introduces Bijou64, a novel variable-length integer encoding scheme that prioritizes efficiency and simplicity. It is designed to encode integers of varying sizes with a compact representation. This encoding offers a potential alternative to existing schemes like LEB128, with improvements in handling the full uint64 range without an extra byte. It could benefit applications such as data serialization and binary formats where compactness and ease of decoding are important. Bijou64 uses a length-prefixed approach, unlike offset-based schemes, which may impact encoding size for certain ranges. It supports the full 64-bit unsigned integer range within 9 bytes, whereas LEB128 sometimes requires a 10th byte for the same.

hackernews · justinweiss · May 29, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48323992)

**Background**: Variable-length integer encoding is a technique used to represent integers with fewer bytes for smaller values and more bytes for larger values, optimizing storage. Common examples include LEB128, used in DWARF and WASM, and BER-TLV. These encodings are crucial in protocols and file formats to reduce overhead.

**Discussion**: Community comments highlight trade-offs: one commenter notes that Bijou64's approach breaks down with SIMD instructions, while others compare it favorably to LEB128 and BER-TLV. Some users appreciate its cleaner support for the full uint64 range, but note that LEB128 may be more compact for certain value distributions.

**Tags**: `#variable-length integer encoding`, `#data compression`, `#programming`

---

<a id="item-22"></a>
## [OpenAI's Frontier Governance Framework](https://openai.com/index/openai-frontier-governance-framework) ⭐️ 7.5/10

OpenAI has released its Frontier Governance Framework, a policy document outlining its approach to AI safety, security, and risk management in line with emerging EU AI Act and California regulations. This framework signals a proactive move by a leading AI company to self-regulate and build trust, potentially influencing industry standards and regulatory expectations globally. The framework details practices for frontier AI systems, including risk assessment, security measures, and transparency commitments, but remains high-level without specific technical implementations.

rss · OpenAI Blog · May 28, 00:00

**Background**: Frontier AI refers to the most advanced general-purpose AI systems that could pose significant risks. Governments like the EU and California are drafting regulations to ensure safe development. This framework is OpenAI's response to align with those forthcoming rules.

**Tags**: `#AI Governance`, `#AI Safety`, `#Regulation`, `#OpenAI`, `#Frontier AI`

---

<a id="item-23"></a>
## [Learning AI Agents by Building One: A Two-Day Journey](https://sspai.com/post/110370) ⭐️ 7.5/10

The author shares a personal narrative of spending two days building an AI agent from scratch to understand AI development and the capabilities of agents. This hands-on approach demystifies AI agent concepts for developers and learners, emphasizing practical understanding over theory. The narrative focuses on the process of 'learning by doing' and covers the evolution of AI and the limitations of current agent systems.

rss · 少数派 · May 28, 07:00

**Background**: AI agents are autonomous systems that can perceive their environment and take actions to achieve goals, often powered by large language models (LLMs) like GPT. Building one from scratch involves understanding components such as task decomposition, tool use, and memory.

**Tags**: `#AI`, `#Agent`, `#Learning`, `#LLM`, `#Development`

---

<a id="item-24"></a>
## [SQLite Enough for Durable Workflows?](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/) ⭐️ 7.4/10

An article argues that SQLite, as an embedded database, is sufficient for building durable workflows, challenging the need for full-fledged database servers or workflow engines. This debate impacts software engineers deciding between simplicity and scalability for workflow systems, especially in small to medium-scale applications. SQLite uses file-level locking, limiting concurrent writes; but for single-process or low-concurrency workflows, it can simplify deployment and reduce dependencies.

hackernews · tomasol · May 29, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48326802)

**Background**: SQLite is a self-contained, serverless, zero-configuration SQL database engine commonly used in embedded systems and local apps. Durable workflows require persistent state that survives crashes; traditional approaches use dedicated database servers like PostgreSQL or workflow engines like Temporal.

**Discussion**: Comments show mixed reactions: some praise SQLite's simplicity for local setups, while others argue it lacks concurrency control and type safety for production, recommending alternatives like DuckDB or Postgres.

**Tags**: `#SQLite`, `#workflows`, `#database`, `#software engineering`, `#distributed systems`

---

<a id="item-25"></a>
## [Framework 12 hard to justify against Apple Silicon](https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/) ⭐️ 7.4/10

A blog post and community discussion argue that the Framework 12 laptop, despite its emphasis on repairability and Linux support, is difficult to justify due to higher cost and lower performance compared to Apple Silicon alternatives. This debate highlights the ongoing conflict between repairability values and raw performance in the laptop market, forcing enthusiasts and Linux users to choose between ethical hardware and practical computing power. The Framework 12 is designed for modularity and easy repairs, but compared to Apple Silicon Macs, it offers lower performance per dollar, inferior battery life, and a less polished user experience. The post notes specific trade-offs in screen quality and ecosystem integration.

hackernews · watermelon0 · May 29, 14:55 · [Discussion](https://news.ycombinator.com/item?id=48323869)

**Background**: Framework Computer is a US manufacturer known for repairable, upgradable laptops that promote the right-to-repair movement. Apple Silicon Macs deliver high performance and efficiency but have limited repairability and locked-down software. Framework laptops offer excellent Linux compatibility, while Apple's Rosetta 2 translation layer is being phased out, affecting software flexibility.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Framework_Laptop">Framework Laptop</a></li>
<li><a href="https://grokipedia.com/page/Framework_Laptop_13">Framework Laptop 13</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some prioritize repairability and Linux support despite higher cost and lower performance, while others find Apple's hardware compelling but criticize the company's restrictive practices. Several users say that for their specific use cases, Framework's "good enough" performance justifies the purchase.

**Tags**: `#Framework`, `#repairability`, `#laptop`, `#hardware`, `#Linux`

---

<a id="item-26"></a>
## [Dead Economy Theory: AI Overcapacity Stagnation](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 7.2/10

Owen McGrann's 'dead economy theory' argues that overcapacity in AI investment and labor markets is leading to economic stagnation, contrasting with typical growth narratives. The theory challenges the optimistic view of AI-driven productivity gains, suggesting that widespread automation could destroy the customer base itself, affecting businesses and workers globally. The article posits a scenario where companies fire workers to save costs, but those workers were their own customers, leading to revenue collapse and a 'non-human AI economy' as an extreme outcome.

hackernews · WillDaSilva · May 29, 15:46 · [Discussion](https://news.ycombinator.com/item?id=48324712)

**Background**: Overcapacity occurs when supply exceeds demand, leading to falling prices and reduced profits. In AI, massive investment in infrastructure and talent may outpace actual market needs, echoing historical patterns in agriculture and manufacturing. The theory draws parallels to India's labor-intensive farming, which is kept inefficient by subsidies to avoid mass unemployment.

**Discussion**: Commenters debated the implications: some highlighted India's farming overcapacity as a cautionary example, while others questioned the scale of AI investment vs. addressable markets. A user pointed out potential oversupply of software talent, and another theorized that AI might augment rather than replace labor, countering the alarmist view.

**Tags**: `#economy`, `#AI`, `#labor market`, `#technology`, `#productivity`

---

<a id="item-27"></a>
## [Boston Children's Uses AI to Diagnose 40+ Rare Diseases](https://openai.com/index/boston-childrens-hospital) ⭐️ 7.2/10

Boston Children's Hospital has deployed OpenAI's technology to improve patient care and reduce operational burden, successfully helping diagnose over 40 rare disease cases. This demonstrates a concrete, high-impact application of AI in healthcare, particularly for rare diseases that are often difficult to diagnose. It shows how AI can augment clinical expertise and potentially accelerate diagnosis timelines, benefiting patients and reducing healthcare costs. The implementation uses OpenAI's large language models to assist clinicians in analyzing complex medical data. The hospital reported over 40 cases where AI contributed to reaching a diagnosis that might otherwise have been delayed or missed.

rss · OpenAI Blog · May 29, 12:00

**Background**: Rare diseases are challenging to diagnose due to limited medical knowledge and symptom overlap with common conditions. AI, especially large language models trained on vast biomedical literature, can help identify patterns and suggest potential diagnoses. Boston Children's Hospital is a leading pediatric medical center, and this case study highlights a growing trend of AI adoption in clinical settings.

**Tags**: `#AI`, `#healthcare`, `#OpenAI`, `#rare diseases`, `#diagnostics`

---

<a id="item-28"></a>
## [AI Hype Sparks Boos at Graduation](https://www.technologyreview.com/2026/05/28/1138053/the-ai-hype-index-ai-gets-booed-in-graduation-season/) ⭐️ 7.0/10

Former Google CEO Eric Schmidt was booed by University of Arizona graduates when he told them their task is to help shape AI. This incident highlights growing public skepticism toward AI hype, signaling a potential backlash against tech industry narratives. The booing occurred during a speech where Schmidt discussed AI's transformative potential, reflecting a disconnect between tech leaders and public sentiment.

rss · MIT Tech Review · May 28, 09:51

**Background**: AI has been heavily hyped by tech leaders and media, but recent incidents—like job displacement fears and ethical concerns—have fueled public skepticism. The MIT Technology Review's AI Hype Index tracks this sentiment. Graduation speeches often serve as a barometer for societal attitudes toward new technologies.

**Tags**: `#AI`, `#hype`, `#public sentiment`, `#graduation`, `#Eric Schmidt`

---

<a id="item-29"></a>
## [Cognition Labs raises $1B at $26B valuation](https://www.latent.space/p/ainews-cognition-raises-1b-in-26b) ⭐️ 7.0/10

Cognition Labs has raised $1 billion in a Series D funding round, achieving a post-money valuation of $26 billion. This massive funding round underscores the immense market potential and investor confidence in AI-assisted coding tools, which are seen as a transformative force in software development. The round values the company at $26 billion, one of the highest valuations for an AI startup focused on coding. The company's product likely leverages large language models to automate code generation and debugging.

rss · Latent Space · May 28, 07:26

**Background**: AI-assisted coding tools use large language models to understand and generate code, aiming to boost developer productivity. The market for such tools is considered vast, as software development is a multi-trillion-dollar industry. Cognition Labs is one of several startups in this space, including GitHub Copilot and others.

**Tags**: `#AI`, `#Funding`, `#Cognition`, `#Coding`, `#Agentic Systems`

---