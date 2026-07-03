---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 113 items, 25 important content pieces were selected

---

1. [DSPy improves Datasette Agent's SQL prompts programmatically](#item-1) ⭐️ 9.6/10
2. [Vercel Chief on Agents as New Software Type](#item-2) ⭐️ 9.3/10
3. [Why Startups Fail by Building Half-Baked Products](#item-3) ⭐️ 9.2/10
4. [Let AI Judge When to Test and Which Model to Use](#item-4) ⭐️ 8.9/10
5. [Skill engineering vs one-shot AI design](#item-5) ⭐️ 8.9/10
6. [Autoresearch: Feedback Loops for Self-Improving AI Agents](#item-6) ⭐️ 8.9/10
7. [Developers Explore Beyond Prompt-Response for LLM Coding](#item-7) ⭐️ 8.8/10
8. [PostgreSQL OOM Prevention with Strict Memory Overcommit](#item-8) ⭐️ 8.6/10
9. [Open Source AI Gap Map Launched by Current AI](#item-9) ⭐️ 8.6/10
10. [Understand to Participate in AI-Assisted Coding](#item-10) ⭐️ 8.6/10
11. [Jamesob's guide to running SOTA LLMs locally](#item-11) ⭐️ 8.3/10
12. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-12) ⭐️ 8.3/10
13. [European Parliament Spy Probe Member Hacked with Pegasus](#item-13) ⭐️ 8.1/10
14. [Smart Model Routing Emerges as Key AI Trend](#item-14) ⭐️ 8.1/10
15. [LiteLLM v1.90.2 verifies Docker signatures](#item-15) ⭐️ 7.8/10
16. [Adobe Experiments with AI-Generated Personalized Websites](#item-16) ⭐️ 7.8/10
17. [AI Trains Turbines for Industrial Efficiency](#item-17) ⭐️ 7.7/10
18. [Weekly Issue 402: My Days at Zhinian AI (Fiction)](#item-18) ⭐️ 7.5/10
19. [Anthropic releases Claude Code v2.1.200 with critical fixes](#item-19) ⭐️ 7.3/10
20. [Code-to-image OCR trick slashes LLM costs 60%](#item-20) ⭐️ 7.3/10
21. [The Fall and Rise of Screwworm](#item-21) ⭐️ 7.2/10
22. [AI Engineer World's Fair: Loops Debate and State of AI](#item-22) ⭐️ 7.2/10
23. [Claude Code v2.1.199 Fixes Stacked Skills, SSL Errors, Subagent Failures, and More](#item-23) ⭐️ 7.0/10
24. [Vercel AI SDK Patch Adds Streaming Transcription](#item-24) ⭐️ 7.0/10
25. [Device Revives Donor Eyeballs for Eye Transplants](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DSPy improves Datasette Agent's SQL prompts programmatically](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 9.6/10

Simon Willison used DSPy to systematically evaluate and improve the SQL system prompts for Datasette Agent, identifying issues like column-name guessing and error-retry loops, and suggesting better schema inclusion. He employed Claude Code with Claude Fable 5 and tested with GPT-4.1 mini and nano. This demonstrates a programmatic approach to prompt engineering that can be applied to any LLM agent, reducing guesswork and improving performance systematically. It highlights the value of tools like DSPy for optimizing AI system prompts. The baseline prompts caused the agent to guess column names (e.g., page_count, o.order_id) leading to error-retry loops. Suggested fixes include including column names directly in the schema prompt or softening the advice to avoid unnecessary describe_table calls.

rss · Simon Willison · Jul 2, 18:25

**Background**: DSPy is a Python framework for algorithmically optimizing the prompts and weights of large language models, enabling systematic evaluation rather than manual tuning. Datasette Agent is an LLM-powered assistant for exploring and querying data in SQLite databases via Datasette. Simon Willison is the creator of Datasette and Datasette Agent.

<details><summary>References</summary>
<ul>
<li><a href="https://dspy.ai/">DSPy</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help explore and analyze data in SQLite</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette/datasette-agent: An LLM-powered agent for Datasette · GitHub</a></li>

</ul>
</details>

**Tags**: `#DSPy`, `#prompt optimization`, `#Datasette Agent`, `#LLM agents`, `#SQL prompts`

---

<a id="item-2"></a>
## [Vercel Chief on Agents as New Software Type](https://www.latent.space/p/vercel-agents-new-software) ⭐️ 9.3/10

Vercel's Chief of Software, Andrew Qu, gave an in-depth interview explaining the creation of their new open-source agent framework 'eve', which treats AI agents as filesystem-first directories of instructions, skills, and tools. This interview signals a paradigm shift in software development, where AI agents are treated as modular, version-controllable code rather than black-box APIs, and it highlights the growing need for websites to be optimized for agent readability. The eve framework is Apache-2.0 licensed and built in TypeScript; it compiles a directory of files into a manifest and provides a durable runtime on Vercel Functions. Vercel also published a specification for 'agent-readable websites' to help developers make their sites easily parsable by AI agents.

rss · Latent Space · Jul 3, 00:08

**Background**: AI agents are autonomous programs that perform tasks on behalf of users, often by interacting with websites and APIs. Traditional agent frameworks rely on complex orchestrations, but eve takes a filesystem-first approach where each agent is simply a directory of markdown and TypeScript files, making it easier to inspect, version, and deploy. The concept of agent-readable websites extends SEO principles to the age of AI browsing, ensuring that sites can be understood and utilized by autonomous agents.

<details><summary>References</summary>
<ul>
<li><a href="https://vercel.com/eve">eve – The Agent Framework - Vercel</a></li>
<li><a href="https://github.com/vercel/eve">GitHub - vercel / eve : The Framework for Building Agents · GitHub</a></li>
<li><a href="https://vercel.com/kb/guide/agent-readability-spec">Agent Readability: A Specification for AI-Optimized Websites | Vercel Knowledge Base</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Vercel`, `#eve`, `#agent framework`, `#software evolution`

---

<a id="item-3"></a>
## [Why Startups Fail by Building Half-Baked Products](https://weli.dev/blog/half-baked-product/) ⭐️ 9.2/10

An essay argues that startups often fail because they release half-baked products, misinterpreting MVP as a crude prototype rather than a learning tool. This critique challenges the common startup practice of rushing incomplete products to market, highlighting the need for a deeper understanding of MVP principles. The community discussion contrasts Eric Ries' definition of MVP—maximizing validated learning with minimal effort—with a 'crutch' approach that builds shoddy products.

hackernews · weli · Jul 3, 08:23 · [Discussion](https://news.ycombinator.com/item?id=48772388)

**Background**: MVP (Minimum Viable Product) is a key concept in Lean Startup methodology, intended to test hypotheses quickly. Many founders misuse it to justify releasing unfinished products, leading to failure.

**Discussion**: Commenters debate the definition of MVP and founder motivation. One user criticizes founders who chase wealth without domain expertise, while another notes the disconnect between different personas in a startup.

**Tags**: `#startup`, `#product development`, `#MVP`, `#failure`, `#founder motivation`

---

<a id="item-4"></a>
## [Let AI Judge When to Test and Which Model to Use](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 8.9/10

Simon Willison shared tips from the Claude Code team and Jesse Vincent on allowing AI models like Fable to use their own judgment for deciding when to write tests and which lower-power model to delegate tasks to, improving efficiency and saving tokens. This approach reduces token consumption and cost while maintaining quality, offering a practical optimization for developers using expensive top-tier models like Fable. It highlights a shift toward more autonomous AI agents that self-optimize resource usage. The technique involves adding a prompt like 'use your judgement to decide an appropriate lower power model and run that in a subagent' to store a memory file that guides the model to delegate coding tasks to cheaper models (e.g., Sonnet for substantive work, Haiku for trivial edits) while keeping judgment-heavy tasks on the main model.

rss · Simon Willison · Jul 3, 18:51

**Background**: Claude Fable and Opus are Anthropic's advanced AI models, with Fable being the most powerful and expensive, designed for complex reasoning and long-horizon tasks. Agentic AI systems can autonomously pursue goals and use tools, and this tip leverages that autonomy to optimize cost and performance by delegating simpler work to cheaper models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Claude Code`, `#testing`, `#agentic systems`

---

<a id="item-5"></a>
## [Skill engineering vs one-shot AI design](https://www.latent.space/p/skill-engineering-design) ⭐️ 8.9/10

Paul Bakaus argues for 'skill engineering'—breaking tasks into reusable skills—over one-shot AI design, promoting iterative human judgment in agent loops. This matters because it shifts the AI design paradigm from single-prompt solutions to continuous human oversight, impacting how AI agents are built and deployed in production. Bakaus created Impeccable, an open-source design skill system that lets agents adjust UI elements (e.g., 'bolder') incrementally, rather than redesigning entire pages at once.

rss · Latent Space · Jul 2, 14:36

**Background**: One-shot AI design refers to prompting a model to complete a complex task in a single request, which often leads to poor results. Skill engineering, by contrast, decomposes work into smaller, reusable skills that can be iteratively refined with human feedback. The term 'loopmaxxing' describes the practice of designing resilient feedback loops around AI agents to improve reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.latent.space/p/skill-engineering-design">Skill engineering and the case against one-shot AI design</a></li>
<li><a href="https://www.articsledge.com/post/skill-engineering">What Is Skill Engineering? The Complete 2026 Guide</a></li>
<li><a href="https://turnkeydatacenter.ai/blog/loopmaxxing-infinite-ai-agents-fixed-cost-infrastructure/">Loopmaxxing : Why Infinite AI Agents Demand... - turnkeydatacenter.ai</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#human-in-the-loop`, `#skill engineering`, `#AI design`, `#loopmaxxing`

---

<a id="item-6"></a>
## [Autoresearch: Feedback Loops for Self-Improving AI Agents](https://www.latent.space/p/autoresearch-introspection) ⭐️ 8.9/10

Introspection co-founder Roland Gavrilescu explains autoresearch, a framework where AI agents iteratively experiment and improve their own training pipelines, emphasizing that humans remain central to the software factory. This paradigm could accelerate AI development by automating research loops, but it also reframes the human role from direct coding to high-level oversight, which has implications for productivity and job design in AI labs. The autoresearch approach uses agent 'recipes' and self-improving loops, where the AI modifies its own training code based on experiment outcomes, yet humans are essential for setting goals, validating results, and maintaining the broader system context.

rss · Latent Space · Jul 1, 23:52

**Background**: Autoresearch refers to automated frameworks where AI agents act as intelligent orchestrators, conducting iterative experiments in R&D pipelines, often inspired by Andrej Karpathy's open-source project. Self-improving loops allow agents to learn from feedback and refine their skills without human engineers rewriting code. This concept is gaining traction as agents become more autonomous in production environments.

<details><summary>References</summary>
<ul>
<li><a href="https://ccapi.ai/blog/autoresearch-agents-single-gpu-nanochat-training">Autoresearch : Agents researching on single-GPU... | CCAPI Blog</a></li>
<li><a href="https://noqta.tn/en/blog/karpathy-autoresearch-autonomous-ai-experiments-loop-2026">The Karpathy Loop: AI Agents Running 700 Experiments Autonomously</a></li>
<li><a href="https://powerdrill.ai/blog/self-improving-data-agents">Self - Improving Data Agents : Unlocking Autonomous Learning and...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agents`, `#self-improving`, `#feedback loops`, `#software factory`

---

<a id="item-7"></a>
## [Developers Explore Beyond Prompt-Response for LLM Coding](https://news.ycombinator.com/item?id=48771515) ⭐️ 8.8/10

A Hacker News discussion highlights experiments with alternative LLM coding workflows, including heterogeneous LLM swarms and hermetic agents that break away from the standard prompt-response loop. These explorations could lead to more seamless, flow-state-friendly AI-assisted coding, potentially transforming how developers integrate LLMs into their workflow. Key ideas include heterogeneous swarms of multiple LLMs collaborating via directed acyclic graphs, and hermetic agents that isolate code generation from test writing to avoid bias.

hackernews · yehiaabdelm · Jul 3, 06:21

**Background**: Current LLM coding tools like Claude Code and Codex typically operate on a prompt-response loop: the user types a request, the model responds, then the user reviews and prompts again. This interrupts the developer's flow state. Heterogeneous swarms use multiple specialized LLMs arranged in a directed acyclic graph (DAG) to collaboratively solve tasks, optimizing model roles and weights. Hermetic agents run in isolated sandboxes where the code writer cannot see the tests and vice versa, enforcing a separation of concerns to improve software quality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.04510">[2502.04510] Heterogeneous Swarms: Jointly Optimizing Model Roles and Weights for Multi-LLM Systems</a></li>
<li><a href="https://hermeticagents.app/">Hermetic Agents — A Council of Seven Principle-Based AI Agents</a></li>
<li><a href="https://github.com/HermeticOrmus/Hermetic-Agents">GitHub - HermeticOrmus/ Hermetic - Agents</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiments, with one user building a homelab swarm of old GPUs to run heterogeneous LLMs, while another proposed hermetic agents to reduce confirmation bias. Others lamented the loss of flow state and discussed trade-offs between outsourcing understanding and maintaining code quality.

**Tags**: `#LLM`, `#coding`, `#AI agents`, `#software engineering`, `#programming`

---

<a id="item-8"></a>
## [PostgreSQL OOM Prevention with Strict Memory Overcommit](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.6/10

Ubicloud published a blog post detailing why they configure Linux's vm.overcommit_memory to strict mode (value 2) for their managed PostgreSQL clusters to prevent the OOM killer from terminating critical database processes. This configuration can significantly improve PostgreSQL stability under memory pressure, but it also introduces trade-offs that may affect system fork capability and overall memory management. The debate highlights the complexity of memory overcommit settings in production environments. The strict overcommit mode (mode 2) disallows memory overcommit by default, failing allocations early rather than relying on the OOM killer. However, as noted in community comments, this can prevent process forks if the overcommit ratio has been adjusted, and may cause instability in mixed-workload environments where other applications allocate large virtual memory.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: Linux provides three memory overcommit policies via vm.overcommit_memory: 0 (heuristic), 1 (always overcommit), and 2 (strict overcommit). The default heuristic mode allows the kernel to overcommit memory, which can lead to the OOM killer terminating processes when actual memory runs out. PostgreSQL is particularly vulnerable to OOM kills because it often uses large shared memory segments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdMemoryLimitVsOvercommit">Chris's Wiki :: blog/ linux /SystemdMemoryLimitVsOvercommit</a></li>
<li><a href="https://www.servermo.com/howto/stop-linux-oom-killer-ai-crash/">Stop AI Crashes: The Linux OOM-Killer Shield | ServerMO</a></li>

</ul>
</details>

**Discussion**: The community discussion shows mixed opinions. Users like baq criticize Linux defaults as 'insane' and point out multiple failure modes under memory pressure. Bender cautions about potential for preventing forks with mode 2 and recommends thorough testing. Ozgune from Ubicloud clarifies that while the technique works for their use case, the blog post's title was too strong and strict overcommit may have unanticipated side-effects in other scenarios.

**Tags**: `#PostgreSQL`, `#memory management`, `#Linux kernel`, `#OOM killer`, `#system administration`

---

<a id="item-9"></a>
## [Open Source AI Gap Map Launched by Current AI](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.6/10

Current AI, a nonprofit founded at the 2025 AI Action Summit, launched the Open Source AI Gap Map v0.1, indexing 421 open source AI products across models, tools, datasets, and hardware. The underlying data, including 1,184 YAML files, is released under an MIT license on GitHub. This gap map provides a comprehensive, structured overview of the open source AI ecosystem, helping researchers, developers, and policymakers identify strengths and missing pieces. It sets a baseline for tracking the evolution of open source AI, which is increasingly important as AI adoption accelerates. The map details 421 products: 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across 3 stack layers. An additional 24,400 artifacts are cataloged but unsorted.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global nonprofit partnership launched at the AI Action Summit in Paris in February 2025, with $400 million committed. The Open Source AI Gap Map aims to systematically catalog the fragmented open source AI landscape, making it easier to navigate and analyze.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Action_Summit_2025">AI Action Summit 2025</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open source`, `#gap map`, `#ecosystem`, `#non-profit`

---

<a id="item-10"></a>
## [Understand to Participate in AI-Assisted Coding](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.6/10

Geoffrey Litt introduced the concept of 'Understand to participate' at the AIE conference, arguing that developers must deeply understand code changes made by AI coding agents to remain effective collaborators and avoid cognitive debt. As AI coding agents become more sophisticated, developers risk accepting generated code without full comprehension, leading to cognitive debt that undermines long-term software maintainability and the developer's own creative participation. Litt emphasized that to participate fluently, developers need a rich set of mental concepts about the codebase, otherwise their ability to move the project forward is limited. Simon Willison recommends watching Litt's recorded talk from the AIE conference.

rss · Simon Willison · Jul 2, 17:07

**Background**: Cognitive debt refers to the lack of understanding that accumulates when developers use AI-generated code without fully grasping its logic or structure, making future changes harder. AI coding agents are tools that generate or modify code from natural language prompts, increasingly used in software development workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://mathiesen.dev/writing/cognitive-debt">Cognitive Debt | Jarle Mathiesen</a></li>
<li><a href="https://www.thoughtworks.com/en-th/insights/blog/generative-ai/cognitive-demands-ai-novelty">The cognitive demands of AI novelty | Thoughtworks Thailand</a></li>
<li><a href="https://www.artofsm.art/t/feeling-lost-in-your-codebase-5-tips-to-tackle-ai-induced-cognitive-debt/16929">Feeling lost in your codebase? 5 tips to tackle AI-induced cognitive debt</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#cognitive debt`, `#software engineering`, `#coding assistants`, `#collaboration`

---

<a id="item-11"></a>
## [Jamesob's guide to running SOTA LLMs locally](https://github.com/jamesob/local-llm) ⭐️ 8.3/10

Jamesob published a guide on building high-end local LLM setups, with configurations costing $40k-$55k using multiple high-end GPUs. This guide highlights the current extreme hardware requirements for running top-tier LLMs locally, which remains prohibitively expensive for most users, and sparks discussion on cost-effective alternatives like cloud services or unified memory architectures. The guide's top build starts with a $40k budget including 4 GPUs at $12k each, totaling closer to $50k-$55k, and relies on quantization techniques to fit models. Users note that even then, performance may not match cloud-based models like Claude Opus.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models (LLMs) locally requires significant computational resources, especially for state-of-the-art (SOTA) models. Typically, high-end GPUs with large amounts of VRAM are needed. Quantization is a technique that reduces model precision to fit into limited memory, but it can affect output quality. Cloud-based LLM services offer access to powerful models at a subscription cost, but sacrifice privacy and control.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Running_Open-Source_LLMs_Locally">Running Open-Source LLMs Locally</a></li>
<li><a href="https://fungies.io/local-llm-inference-tools-guide-2026-3/">How to Set Up and Use Local LLM Inference Tools in... - Fungies.io</a></li>

</ul>
</details>

**Discussion**: Community members express concerns about the high cost, noting that $40k-$55k could cover years of cloud subscriptions. Some suggest alternatives like unified memory Macs or 2x RTX 3090s for smaller models. Others warn that local setups often require quantization and may not match cloud performance.

**Tags**: `#AI`, `#LLM`, `#local inference`, `#hardware`

---

<a id="item-12"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.3/10

Wordgard, a new in-browser rich-text editor framework, has been released by Marijn Haverbeke, the creator of ProseMirror. It is licensed under MIT and available on his Forgejo server. Wordgard offers a fresh approach to building content editors, potentially addressing some limitations of ProseMirror while sharing its solid foundation. Developers gain a new option for customizable rich-text editing in web applications. Wordgard is not a free-form HTML editor but a framework that gives developers precise control over supported content types. There is no direct upgrade path from ProseMirror; switching requires significant rework.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: Rich-text editors in the browser have long been a challenge, with no standard built-in solution. ProseMirror is a widely used open-source framework for building such editors, powering tools like Tiptap. Wordgard is a new alternative from the same author, aiming to improve on ProseMirror's design.

<details><summary>References</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://code.haverbeke.berlin/wordgard/wordgard">wordgard / wordgard : The Wordgard rich text editor</a></li>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1</a></li>

</ul>
</details>

**Discussion**: Community comments show positive interest in Wordgard's technical merits, with users noting its design and comparisons to ProseMirror. Some developers expressed concerns about migration effort and the lack of a web standard for rich-text editing.

**Tags**: `#web development`, `#rich-text editor`, `#prosemirror`, `#open source`, `#devtools`

---

<a id="item-13"></a>
## [European Parliament Spy Probe Member Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.1/10

Citizen Lab's forensic analysis confirmed that Greek MEP Stelios Kouloglou, a member of the European Parliament's committee investigating spyware, had his iPhone infected with Pegasus spyware on at least three occasions in 2022-2023. This breach undermines the integrity of an EU investigation into spyware abuse and highlights that high-profile targets, including those probing surveillance, remain vulnerable to state-grade hacking. The infections occurred on or around October 21, 2022, and March 6-7, 2023, with high confidence from forensic artifacts, and likely involved a zero-click exploit on iOS. The compromised phone potentially exposed confidential medical and government documents.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a commercial spyware developed by Israel's NSO Group, capable of remotely infiltrating iOS and Android devices to extract data and activate sensors. Citizen Lab, based at the University of Toronto, is a leading research lab that investigates digital threats and has exposed numerous Pegasus infections worldwide.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Comments noted the potential lack of device separation in EU parliament, the broader Greek Pegasus scandal implicating the prime minister's office, and suggestions that using GrapheneOS or lockdown mode could have raised the attack cost. Some pointed out irony in an EU member being spied on by member states that also use Pegasus against journalists.

**Tags**: `#Pegasus`, `#spyware`, `#European Parliament`, `#Citizen Lab`, `#cybersecurity`

---

<a id="item-14"></a>
## [Smart Model Routing Emerges as Key AI Trend](https://blog.pragmaticengineer.com/the-pulse-a-new-trend-smart-model-routing/) ⭐️ 8.1/10

The article explores emerging smart model routing solutions that automatically select the best AI model for each task, highlighting a new trend in AI tooling. This matters because it can reduce AI inference costs by 50-80% while maintaining output quality, enabling more efficient and scalable deployments across applications. Smart routers analyze prompts for task type, required quality, and cost sensitivity, then route to the cheapest model that meets the quality bar, supporting providers like GPT-4o, Claude, and Gemini.

rss · Pragmatic Engineer · Jul 2, 18:46

**Background**: Traditionally, AI applications relied on a single model, leading to inefficiency. Smart model routing dynamically selects the optimal model per request, optimizing cost, speed, and quality. This concept resembles network routing but for AI inference, and can cut costs significantly while maintaining performance.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.chinallmapi.com/smart-model-routing-strategy/">Smart Model Routing : How to Choose the Right AI Model for Each...</a></li>
<li><a href="https://vincony.com/glossary/model-routing">Model Routing — AI Aggregator Concept Defined | Vincony | Vincony</a></li>

</ul>
</details>

**Tags**: `#AI`, `#model routing`, `#LLM`, `#inference`, `#practical AI`

---

<a id="item-15"></a>
## [LiteLLM v1.90.2 verifies Docker signatures](https://github.com/BerriAI/litellm/releases/tag/v1.90.2) ⭐️ 7.8/10

LiteLLM v1.90.2 introduces detailed steps for verifying Docker image signatures using cosign, with a recommended method using a pinned commit hash and a more convenient release-tag-based method. This enhances supply chain security for LiteLLM users by ensuring the integrity and authenticity of Docker images, which is critical for preventing tampering and building trust in AI tooling deployment. The same public key from commit 0112e53 is used for both methods; the pinned commit hash is cryptographically immutable, while the release tag method relies on tag protection rules.

github · yuneng-berri · Jul 3, 04:48

**Background**: Cosign is a tool from the Sigstore project designed for signing and verifying container images, supporting both key-based and keyless signing. Verifying signatures ensures that an image has not been altered since signing, which is crucial for secure software supply chains.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sigstore.dev/quickstart/quickstart-cosign/">Sigstore Quickstart with Cosign - Sigstore</a></li>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/ cosign : Code signing and transparency for...</a></li>

</ul>
</details>

**Tags**: `#LiteLLM`, `#Docker`, `#cosign`, `#supply chain security`, `#AI tooling`

---

<a id="item-16"></a>
## [Adobe Experiments with AI-Generated Personalized Websites](https://www.latent.space/p/the-website-of-the-future) ⭐️ 7.8/10

Adobe is experimenting with 'agentic sites' that use AI to generate web pages tailored to each visitor's intent in real time. This could fundamentally change web design and user experience by making websites adaptive rather than static, potentially increasing engagement and conversion rates. The concept, discussed by Adobe's Carlos Sanchez, involves generating pages around individual user intent using AI agents, rather than serving pre-built pages.

rss · Latent Space · Jul 2, 21:25

**Background**: Traditional websites serve the same content to all visitors, but 'agentic sites' use embedded AI agents to dynamically compose pages based on user behavior and context. Adobe is exploring this through its Experience Manager and Edge Delivery Services, aiming to automate site creation and migration for the agentic web.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=wIJKwPBbuPk">Building the Agentic Web | Adobe Developers Live 2025... - YouTube</a></li>
<li><a href="https://business.adobe.com/blog/modernizing-digital-experiences-for-the-agentic-web">Modernizing digital experiences with Adobe agentic AI</a></li>
<li><a href="https://www.businesswire.com/news/home/20250318537901/en/Adobe-Launches-Adobe-Experience-Platform-Agent-Orchestrator-for-Businesses-to-Activate-AI-Agents-in-Customer-Experiences-and-Marketing-Workflows">Adobe Launches Adobe Experience Platform Agent Orchestrator for...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agentic systems`, `#web development`, `#personalization`, `#Adobe`

---

<a id="item-17"></a>
## [AI Trains Turbines for Industrial Efficiency](https://www.technologyreview.com/2026/07/02/1138433/teaching-ai-to-run-with-the-turbines/) ⭐️ 7.7/10

A new application of AI is being deployed to control and optimize industrial turbines, enhancing operational continuity and safety beyond consumer-facing tools. This marks a shift of AI from chatbots to critical physical infrastructure, potentially reducing downtime and improving safety in energy and manufacturing sectors. The AI system integrates with operational technology (OT) to monitor and adjust turbine parameters in real time, leveraging industrial data streams for predictive maintenance.

rss · MIT Tech Review · Jul 2, 12:51

**Background**: Operational technology (OT) refers to hardware and software that monitors and controls industrial equipment, distinct from traditional IT. Turbines are complex machines critical for power generation, and AI's role is to manage their operation more efficiently and safely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Operational_technology">Operational technology</a></li>
<li><a href="https://www.marketresearchfuture.com/cat-intel/procurement-intelligence-industrial-turbines-market">Category Intelligence for Industrial Turbines Market - MRFR - MRFR</a></li>

</ul>
</details>

**Tags**: `#AI`, `#industrial AI`, `#energy`, `#operational technology`, `#applied AI`

---

<a id="item-18"></a>
## [Weekly Issue 402: My Days at Zhinian AI (Fiction)](http://www.ruanyifeng.com/blog/2026/07/weekly-issue-402.html) ⭐️ 7.5/10

Ruan Yifeng's 402nd weekly tech newsletter features a fictional story titled 'My Days at Zhinian AI' alongside curated tech articles. This newsletter provides a trusted weekly overview of important tech developments in China, and the fictional story offers a creative perspective on AI work culture. The issue is dated July 2026 and scores 7.5/10 for relevance and quality; the fictional element slightly reduces practical value.

rss · 阮一峰周刊 · Jul 2, 23:33

**Background**: Ruan Yifeng is a prominent Chinese blogger and author who publishes a widely-read weekly tech newsletter. 'Zhinian AI' appears to be a fictional AI company context for the story. The newsletter typically covers AI, programming, and industry trends.

**Tags**: `#tech newsletter`, `#AI`, `#weekly curation`, `#阮一峰`

---

<a id="item-19"></a>
## [Anthropic releases Claude Code v2.1.200 with critical fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) ⭐️ 7.3/10

The release changes AskUserQuestion dialogs to no longer auto-continue by default and sets the default permission mode to Manual across all interfaces. It also fixes over a dozen bugs affecting background sessions, MCP server configuration, and screen-reader accessibility. This update gives users more control over dialog and permission flow, reducing unexpected automation and improving security. The bug fixes enhance reliability for background agents and MCP integration, which are key features for power users and developers using Claude Code in CI/CD or long-running tasks. Notable fixes include crash prevention when MCP server arrays are misconfigured, resolution of background sessions stalling after sleep/wake, and improved screen-reader output with hidden decorative glyphs and nested table labeling. The install script now explains when installation is killed due to low memory.

github · ashwin-ant · Jul 3, 16:52

**Background**: Claude Code is an AI coding assistant developed by Anthropic, part of the Claude product family. It supports background agents for autonomous task execution and uses the Model Context Protocol (MCP) to integrate with external tools and data sources. Permission modes control how the tool handles user approval for actions like file edits or command execution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>
<li><a href="https://code.claude.com/docs/en/permission-modes">Choose a permission mode - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI tools`, `#release notes`, `#bug fixes`, `#Anthropic`

---

<a id="item-20"></a>
## [Code-to-image OCR trick slashes LLM costs 60%](https://github.com/teamchong/pxpipe) ⭐️ 7.3/10

A GitHub project called pxpipe converts code into images and uses OCR to process them, reportedly cutting Fable's LLM costs by 60% by exploiting a token accounting loophole. This technique exposes a potential pricing loophole in LLM services, where image tokens are cheaper or not charged as text, enabling significant cost savings. It could prompt providers to close the loophole or adjust pricing models. The method reduces prompt tokens but may increase completion tokens and latency, as noted in community tests. It relies on how providers like Gemini and Claude process PDFs by OCR'ing text without charging for those text tokens.

hackernews · dimitropoulos · Jul 3, 15:50 · [Discussion](https://news.ycombinator.com/item?id=48776464)

**Background**: LLMs typically charge per token, where tokens are chunks of text (e.g., a word or subword). Code as text can be tokenized into many tokens, but images are processed differently and may have separate, cheaper token pricing. Converting code to an image bypasses the text token counting, potentially reducing costs if the provider charges less for image tokens or does not count OCR'd text tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them">What are tokens and how to count them? | OpenAI Help Center</a></li>
<li><a href="https://ssimplifi.com/blog/llm-cost-reduction-techniques-ranked-by-roi">LLM cost reduction techniques ranked by ROI... | Prism by Ssimplifi</a></li>

</ul>
</details>

**Discussion**: Commenter aabhay noted that Gemini and likely Claude OCR PDFs and feed the text without charging for those tokens, implying this is a loophole. lpellis found a similar approach last year with OpenAI but it was ultimately more expensive. lstroud sarcastically remarked that this is rediscovering compressed binary formats.

**Tags**: `#AI`, `#LLM`, `#cost optimization`, `#OCR`, `#token accounting`

---

<a id="item-21"></a>
## [The Fall and Rise of Screwworm](https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm) ⭐️ 7.2/10

The article chronicles the historical eradication of screwworm via the sterile insect technique and its recent resurgence in the Americas, with cases reported in Texas in 2025/2026. This matters because screwworm infestations cause severe economic losses in livestock and wildlife, and the resurgence challenges decades of successful eradication efforts, highlighting the vulnerability of biological control programs. The sterile insect technique involves mass-rearing and sterilizing male flies using radiation, then releasing them to mate with wild females, leading to population collapse; the recent resurgence may be due to a breakdown in the barrier zone at the Darien Gap.

hackernews · crescit_eundo · Jul 3, 12:58 · [Discussion](https://news.ycombinator.com/item?id=48774492)

**Background**: Screwworm (Cochliomyia hominivorax) is a parasitic fly whose larvae feed on living tissue, causing myiasis in animals. The USDA and partners successfully eradicated it from North and Central America using the sterile insect technique. However, maintaining a barrier in Panama has been challenging, and recent cases in Texas indicate a breach.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Screwworm">Screwworm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sterile_insect_technique">Sterile insect technique</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article's depth, noting that early researchers overcame ridicule and lack of resources. Others discussed the ethics of historical experiments and the economics of maintaining the barrier versus eradicating screwworm continent-wide.

**Tags**: `#screwworm`, `#sterile insect technique`, `#eradication`, `#biology`, `#agriculture`

---

<a id="item-22"></a>
## [AI Engineer World's Fair: Loops Debate and State of AI](https://www.latent.space/p/aiewf-daily-dispatch-locomotives) ⭐️ 7.2/10

The AI Engineer World's Fair concluded with a debate about loops in agentic systems, the release of a state of AI engineering report, and closing keynotes on what to build next. This event highlights critical discussions shaping AI engineering, especially the debate over loops (iterative feedback mechanisms) in AI agents, which is central to building reliable autonomous systems. The debate centered on whether loops in agentic systems improve performance or introduce complexity and failure modes. The state of AI engineering report likely covers trends, challenges, and adoption patterns in AI development.

rss · Latent Space · Jul 3, 05:11

**Background**: The AI Engineer World's Fair is a conference focused on practical AI engineering, bringing together developers, researchers, and industry leaders to discuss tools, techniques, and trends. 'Loops' refer to iterative feedback mechanisms in AI agents, such as self-reflection or tool-use loops, which are debated for their effectiveness in real-world applications. The term 'state of AI engineering' typically refers to an industry report that surveys the current practices, bottlenecks, and future directions of building AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.movingavg.com/essays/vibes-at-the-ai-engineer-worlds-fair.html">Vibes at the AI Engineer World ' s Fair</a></li>

</ul>
</details>

**Tags**: `#AI Engineering`, `#Agentic Systems`, `#LLM`, `#Industry Report`, `#Event Summary`

---

<a id="item-23"></a>
## [Claude Code v2.1.199 Fixes Stacked Skills, SSL Errors, Subagent Failures, and More](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) ⭐️ 7.0/10

Anthropic released Claude Code v2.1.199, a bug-fix update addressing over 20 issues including stacked skill invocations, SSL certificate errors, streaming response handling, subagent failures, background agent daemon corruption, and more. This release significantly improves the reliability and user experience for Claude Code users, especially those leveraging advanced features like skills, subagents, and background agents. It reduces frustration and potential data loss from silent failures in production workflows. Notable technical details include stacked skills now loading up to 5 leading skills, SSL errors failing immediately with actionable guidance, partial streaming responses kept with an incomplete-response notice, and fixing background agent daemon corruption after an unclean shutdown. Multiple subagent error reporting fixes ensure errors like usage limits are properly surfaced.

github · ashwin-ant · Jul 2, 23:35

**Background**: Claude Code is Anthropic's command-line AI coding assistant. Skills are modular capabilities that extend its functionality through organized folders containing instructions and resources. Subagents are isolated Claude instances used for delegation, each with its own context and tools. Background agents allow tasks to run in parallel without blocking the main session. These features enable complex workflows but have had reliability issues that this release addresses.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/skills">Agent Skills - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#tooling`, `#claude-code`, `#bug-fixes`

---

<a id="item-24"></a>
## [Vercel AI SDK Patch Adds Streaming Transcription](https://github.com/vercel/ai/releases/tag/%40ai-sdk/xai%404.0.6) ⭐️ 7.0/10

Version 4.0.6 of @ai-sdk/xai adds experimental streaming transcription support for models such as OpenAI's gpt-realtime-whisper and xAI's WebSocket STT. This update enables developers to integrate real-time speech-to-text capabilities directly into their applications using the Vercel AI SDK, simplifying the development of live transcription features. The feature is experimental and updates several dependencies: @ai-sdk/provider to 4.0.2, @ai-sdk/provider-utils to 5.0.5, and @ai-sdk/openai-compatible to 3.0.5.

github · github-actions[bot] · Jul 2, 20:46

**Background**: The Vercel AI SDK is a popular toolkit for building AI-powered applications, offering unified access to various AI providers. @ai-sdk/xai is the provider package for xAI Grok models and now supports streaming transcription. Streaming transcription converts live audio into text incrementally, enabling low-latency voice applications.

<details><summary>References</summary>
<ul>
<li><a href="https://ai-sdk.dev/providers/ai-sdk-providers/xai">AI SDK Providers: xAI Grok</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-whisper">GPT - Realtime - Whisper Model | OpenAI API</a></li>
<li><a href="https://docs.x.ai/developers/quickstart">Tutorial on using Grok models via xAI API | xAI Docs</a></li>

</ul>
</details>

**Tags**: `#AI SDK`, `#streaming transcription`, `#xAI`, `#OpenAI Whisper`, `#release notes`

---

<a id="item-25"></a>
## [Device Revives Donor Eyeballs for Eye Transplants](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) ⭐️ 7.0/10

Researchers have developed a device that maintains donor eyeballs after death, preventing rapid degeneration and preserving the retina's ability to transmit electrical signals. The device, called eye-ECMO, was tested with fluorescent dye showing successful circulation through the retina. This breakthrough could make whole-eye transplantation a viable option for restoring vision in blind patients. It addresses a major obstacle—rapid post-mortem degeneration—and moves the field closer to successful human eye transplants. The eye-ECMO device works by providing extracorporeal membrane oxygenation to the donor eye, maintaining blood flow and oxygen supply. Tests showed dye circulating through the retina, indicating preserved vascular function, though vision restoration has not yet been achieved.

rss · MIT Tech Review · Jul 3, 17:34

**Background**: Whole-eye transplantation has historically been extremely difficult due to the complex surgery and the rapid degeneration of ocular tissue after death. Previous attempts, such as one a few years ago, resulted in a transplanted eye that could not see. The new device aims to keep donor eyes viable long enough for successful transplantation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/">A device that revives eyeballs from dead donors could make eye ...</a></li>
<li><a href="https://gables-gazette.com/university-of-miami-is-paving-the-way-for-human-eye-transplants/">University of Miami is paving the way for human eye transplants</a></li>

</ul>
</details>

**Tags**: `#medical technology`, `#eye transplant`, `#biomedical engineering`, `#organ preservation`

---