---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 110 items, 29 important content pieces were selected

---

1. [Deterministic static binary translation without heuristics](#item-1) ⭐️ 9.6/10
2. [GitHub repo restores BambuNetwork support for third-party slicers](#item-2) ⭐️ 9.2/10
3. [DuckDB Launches Quack: Client-Server Protocol for Scalable Analytics](#item-3) ⭐️ 9.1/10
4. [AI Coding Agents Must Slash Maintenance Costs, Says James Shore](#item-4) ⭐️ 9.1/10
5. [Needle: 26M Parameter Tool Calling Model Distilled from Gemini](#item-5) ⭐️ 9.0/10
6. [AWS Building Blocks for Foundation Model Training and Inference](#item-6) ⭐️ 8.9/10
7. [Musk should focus SpaceXAI on serving others: Stratechery analysis](#item-7) ⭐️ 8.9/10
8. [Linux idle optimization triggers QUIC death spiral](#item-8) ⭐️ 8.7/10
9. [Google DeepMind's AI-powered Magic Pointer for Chrome](#item-9) ⭐️ 8.6/10
10. [OpenAI Forms $4B Deployment Company, Apple Intel Ties](#item-10) ⭐️ 8.5/10
11. [Nobel-winning economist flags three AI trends to watch](#item-11) ⭐️ 8.4/10
12. [Why Senior Developers Struggle to Communicate Expertise](#item-12) ⭐️ 8.2/10
13. [Six CVEs Released for Critical dnsmasq Vulnerabilities](#item-13) ⭐️ 8.2/10
14. [Using LLM in script shebang lines](#item-14) ⭐️ 8.2/10
15. [AI Agents Build Economic Datasets with DRIL](#item-15) ⭐️ 8.1/10
16. [Claude Code v2.1.139 adds agent view and /goal command](#item-16) ⭐️ 8.0/10
17. [LLM 0.32a2 Adds OpenAI /v1/responses Support](#item-17) ⭐️ 8.0/10
18. [Parameter Golf reveals insights for AI-assisted research](#item-18) ⭐️ 7.8/10
19. [Developer leaves GitHub for self-hosted Forgejo over AI scraping and centralization concerns](#item-19) ⭐️ 7.7/10
20. [Zombie Internet: AI Content Pollutes Online](#item-20) ⭐️ 7.7/10
21. [Obsidian Unveils New Community Site and Plugin Review System](#item-21) ⭐️ 7.4/10
22. [Data Centers Boost AI and Cloud Computing, Says Economist](#item-22) ⭐️ 7.4/10
23. [Claude Code v2.1.140: Bug Fixes and Minor Improvements](#item-23) ⭐️ 7.3/10
24. [AutoScout24 boosts engineering with AI workflows](#item-24) ⭐️ 7.3/10
25. [As researchers age, disruptive work declines](#item-25) ⭐️ 7.2/10
26. [Mitchell Hashimoto: TDM Motivated by Fear of Being Fired](#item-26) ⭐️ 7.2/10
27. [AI's Transitional Employment Problems: Non-Obvious Hurdles](#item-27) ⭐️ 7.1/10
28. [Rendering the Sky, Sunsets, and Planets with WebGL and Ray Marching](#item-28) ⭐️ 7.0/10
29. [Google Separates Android from I/O Keynote to Spotlight AI](#item-29) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Deterministic static binary translation without heuristics](https://arxiv.org/abs/2605.08419) ⭐️ 9.6/10

A new paper presents Elevator, the first binary translator that performs fully-static whole-binary translation from x86-64 to AArch64 without using heuristics or runtime fallbacks, achieving performance comparable to QEMU's JIT emulation. This work is significant because it enables deterministic translation that produces certifiable binaries, which is critical for regulated industries like aviation and medical devices where JIT-based emulation is unacceptable due to nondeterminism. The translated code can be up to 50 times larger in the .text section, but the performance is on par with or better than QEMU's user-mode JIT. Elevator handles indirect jumps by considering all possible interpretations of every byte, avoiding heuristics.

hackernews · matt_d · May 13, 04:25 · [Discussion](https://news.ycombinator.com/item?id=48117810)

**Background**: Binary translation converts executable code from one instruction set architecture (ISA) to another. Static binary translation attempts to translate the entire binary before execution, but traditional static translators struggle with uncertain code-data boundaries and indirect jumps, often relying on heuristics or dynamic fallbacks. Elevator overcomes this by deterministically encoding all possible interpretations, producing a correct-by-construction binary.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">Deterministic Fully-Static Whole-Binary Translation without ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_binary_translation">Static binary translation</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that the 50x code size increase is a reasonable trade-off for deterministic translation, and the certification angle is particularly valuable for regulated industries. Some commenters also note that handling indirect jumps is a key challenge, and Elevator's approach is elegant but costly in size.

**Tags**: `#binary translation`, `#static analysis`, `#compiler`, `#emulation`, `#deterministic`

---

<a id="item-2"></a>
## [GitHub repo restores BambuNetwork support for third-party slicers](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 9.2/10

A GitHub repository called OrcaSlicer-bambulab has been created to restore full BambuNetwork support for Bambu Lab printers, allowing third-party slicers like OrcaSlicer to control printers over the network. This comes in response to Bambu Lab's firmware update that introduced an authorization control system blocking such support. This development matters because it directly challenges Bambu Lab's restrictive firmware update that limits user control over their own printers. It represents a community-driven effort to preserve open-source principles and user autonomy in the 3D printing ecosystem. The repository is a clone of the prior state of OrcaSlicer that included BambuNetwork support before Bambu Lab's changes. It enables internet-based printing beyond LAN mode, bypassing the new cloud authentication requirements.

hackernews · Murfalo · May 12, 21:55 · [Discussion](https://news.ycombinator.com/item?id=48115127)

**Background**: Bambu Lab is a 3D printer manufacturer that recently released a firmware update introducing an 'Authorization Control System,' which prevents third-party software from directly controlling printers. This move sparked backlash from the 3D printing community, who argued it reduces user control and violates the principle of owning hardware. The community values open-source tools like OrcaSlicer that offer flexibility beyond manufacturer-provided software.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.bambulab.com/firmware-update-introducing-new-authorization-control-system-2/">Firmware Update Introducing New Authorization Control System</a></li>
<li><a href="https://3dprintingindustry.com/news/bambu-lab-responds-to-backlash-over-new-firmware-update-235771/">Bambu Lab Responds to Backlash Over New Firmware Update - 3D Printing Industry</a></li>
<li><a href="https://cybermediacreations.com/restore-full-bambunetwork-support-for-bambu-lab-printers/">Restore full BambuNetwork support for... - Cyber Media Creations</a></li>

</ul>
</details>

**Discussion**: Community comments show strong opposition to Bambu Lab's firmware changes, with users comparing the restriction to theft and pointing out that the company initially required cloud auth even for LAN mode before backtracking. Some users also reference other vendors like Ubiquiti as examples of more user-friendly authentication approaches.

**Tags**: `#3D printing`, `#firmware`, `#DRM`, `#open source`, `#Bambu Lab`

---

<a id="item-3"></a>
## [DuckDB Launches Quack: Client-Server Protocol for Scalable Analytics](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 9.1/10

DuckDB Labs announced Quack, an HTTP-based client-server protocol that decouples compute from storage, enabling multiple concurrent writers and 32x faster bulk analytics compared to PostgreSQL. This protocol solves DuckDB's historical limitation of single-writer concurrency, making it viable for multi-user, real-time data applications and horizontal scaling in production environments. The Quack extension allows DuckDB to act as both server and client over a network, with support for multiple concurrent writers on the server side, addressing a key scalability bottleneck.

hackernews · aduffy · May 12, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48111765)

**Background**: DuckDB is an embedded, in-process SQL database optimized for analytical workloads, traditionally used single-process and single-threaded. The Quack protocol extends it with a client-server architecture, decoupling storage and compute for concurrent access and scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/duckdb/duckdb-quack">GitHub - duckdb/duckdb-quack · GitHub</a></li>
<li><a href="https://motherduck.com/blog/first-variant/duckdb-client-server/">If It Quacks Like a Duck: DuckDB Gets a Client-Server Protocol</a></li>
<li><a href="https://byteiota.com/quack-protocol-duckdb-client-server-32x-faster/">Quack Protocol: DuckDB Client-Server 32x Faster | byteiota</a></li>

</ul>
</details>

**Discussion**: Comments are overwhelmingly positive, with users like steve_adams_86 and rglover praising the solution for concurrent access and horizontal scaling. Some users, like simlevesque, expressed confusion about DuckDB's evolving identity, while feverzsj asked for clarification on 'concurrent writers', suspecting it might be serialized writes on the server side.

**Tags**: `#DuckDB`, `#database`, `#protocol`, `#scalability`, `#open source`

---

<a id="item-4"></a>
## [AI Coding Agents Must Slash Maintenance Costs, Says James Shore](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 9.1/10

James Shore argues that AI coding agents must reduce maintenance costs proportionally to their productivity gains. Otherwise, they create unsustainable debt, turning a temporary speed boost into permanent indenture. This insight challenges the common assumption that faster code generation automatically leads to overall efficiency. It highlights a critical risk for software teams adopting AI agents: maintenance costs can explode if productivity gains are not matched by cost reductions. Shore uses a simple multiplication example: if you double your output and hold maintenance costs steady, you effectively double total maintenance costs. The required reduction is exactly the inverse of the productivity multiplier (e.g., 2x productivity requires 1/2 maintenance costs).

rss · Simon Willison · May 11, 19:48

**Background**: In software engineering, maintenance costs (fixing bugs, updating dependencies, refactoring) often dominate the total cost of ownership. AI coding agents can dramatically accelerate code writing, but if they produce code that is harder or more expensive to maintain, the long-term burden can outweigh short-term gains. Shore's argument is a call for AI tools to focus on maintainability, not just speed.

**Tags**: `#AI coding agents`, `#maintenance costs`, `#software engineering`, `#productivity`, `#LLM`

---

<a id="item-5"></a>
## [Needle: 26M Parameter Tool Calling Model Distilled from Gemini](https://github.com/cactus-compute/needle) ⭐️ 9.0/10

Cactus Compute has open-sourced Needle, a 26 million parameter model distilled from Gemini for single-shot tool calling, achieving 6000 tokens/second prefill and 1200 tokens/second decode on consumer devices. This demonstrates that tiny models can handle tool calling efficiently, potentially enabling agentic AI on resource-constrained devices like phones, watches, and glasses, and challenging the assumption that large models are necessary for such tasks. The model uses a 'Simple Attention Network' architecture with no feedforward layers, relying solely on cross-attention and gating, and was pretrained on 200B tokens and post-trained on 2B tokens of synthesized function-calling data from Gemini.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Tool calling allows LLMs to invoke external functions or APIs by generating structured JSON outputs. Traditional models use large transformers with feedforward layers to memorize facts, but Needle's approach argues that for retrieval-and-assembly tasks like tool use, cross-attention alone is sufficient, as the required knowledge is provided in the input context.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@yasir_siddique/tool-calling-for-llms-a-detailed-tutorial-a2b4d78633e2">Tool Calling for LLMs: A Detailed Tutorial - Medium</a></li>
<li><a href="https://martinuke0.github.io/posts/2026-01-07-the-anatomy-of-tool-calling-in-llms-a-deep-dive/">The Anatomy of Tool Calling in LLMs: A Deep Dive</a></li>

</ul>
</details>

**Discussion**: Community members expressed curiosity about the model's discriminatory power for complex tool use, concerns about potential countermeasures from Google against distillation, and suggestions to host a live demo for easier testing. Some also noted independent research confirming the possibility of removing MLP layers for external-knowledge tasks.

**Tags**: `#AI`, `#LLM`, `#tool calling`, `#model distillation`, `#open-source`

---

<a id="item-6"></a>
## [AWS Building Blocks for Foundation Model Training and Inference](https://huggingface.co/blog/amazon/foundation-model-building-blocks) ⭐️ 8.9/10

A new Hugging Face blog post details AWS building blocks and best practices for training and deploying foundation models at scale, covering services like SageMaker, EKS, and EC2. This guide helps AI practitioners effectively leverage AWS services for foundation model workflows, potentially reducing costs and improving scalability, while strengthening the integration between Hugging Face and AWS. The blog likely discusses AWS Trainium and Inferentia chips for cost-efficient training and inference, as well as using SageMaker for managed training and EKS for orchestration.

rss · Hugging Face Blog · May 11, 23:18

**Background**: Foundation models are large AI models trained on vast datasets that can be adapted for many tasks. AWS offers custom silicon, Trainium for training and Inferentia for inference, as well as services like SageMaker and EKS to manage ML workflows. Hugging Face is a popular platform for sharing and deploying these models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://huggingface.co/docs/hub/models-the-hub">The Model Hub · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#foundation models`, `#training`, `#inference`, `#Hugging Face`

---

<a id="item-7"></a>
## [Musk should focus SpaceXAI on serving others: Stratechery analysis](https://stratechery.com/2026/spacex-and-anthropic-xais-two-companies-elon-musk-and-spacexais-future/) ⭐️ 8.9/10

Ben Thompson's analysis argues that the Anthropic-xAI deal, while shocking, has strategic logic, and recommends Elon Musk focus SpaceXAI on serving other companies rather than competing directly. This analysis provides a clear strategic direction for Musk's AI efforts, potentially reshaping the competitive landscape by positioning SpaceXAI as an infrastructure provider for enterprises. The article notes that the Anthropic-xAI deal may seem shocking but is strategically unsurprising, and Thompson specifically advises Musk to double down on a business-to-business model for SpaceXAI.

rss · Stratechery · May 12, 10:00

**Background**: xAI is Elon Musk's AI company, while Anthropic is a rival AI startup backed by Amazon and Google. SpaceXAI is a potential AI division within SpaceX. The recent deal between Anthropic and xAI has raised questions about Musk's overall AI strategy.

**Tags**: `#AI`, `#Elon Musk`, `#xAI`, `#Anthropic`, `#Strategy`

---

<a id="item-8"></a>
## [Linux idle optimization triggers QUIC death spiral](https://blog.cloudflare.com/quic-death-spiral-fix/) ⭐️ 8.7/10

Cloudflare engineers discovered that a Linux kernel CPU idle state optimization caused a QUIC connection death spiral, and they fixed it by adding a non-trivial test to their quiche implementation. This incident shows how kernel-level power-saving optimizations can inadvertently break userspace protocols like QUIC, emphasizing the need for cross-layer testing. It impacts all organizations deploying QUIC on Linux servers. The bug involved interactions between CPU C-state transitions, packet pacing, and CUBIC congestion control, causing repeated backoff and throughput starvation. Cloudflare's fix required careful analysis and a custom test to reproduce the rare condition.

hackernews · sbulaev · May 12, 23:46 · [Discussion](https://news.ycombinator.com/item?id=48116064)

**Background**: QUIC is a transport layer protocol that uses UDP, designed for low-latency web communication and forms the basis of HTTP/3. Linux kernel idle states (C-states) manage power consumption by putting idle CPUs into low-power modes, but transitions can introduce latency. Cloudflare uses a custom QUIC implementation called quiche.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/QUIC">QUIC - Wikipedia</a></li>
<li><a href="https://www.kernel.org/doc/html/latest/admin-guide/pm/cpuidle.html">CPU Idle Time Management — The Linux Kernel documentation</a></li>

</ul>
</details>

**Discussion**: Commenters praised the engineering effort behind the test, with one noting it's a great example for teams reluctant to write complex tests. Another questioned why Cloudflare still uses CUBIC instead of BBR, and a user asked about the undefined term 'CCA', which stands for 'Congestion Control Algorithm'.

**Tags**: `#Linux kernel`, `#QUIC`, `#networking`, `#debugging`, `#Cloudflare`

---

<a id="item-9"></a>
## [Google DeepMind's AI-powered Magic Pointer for Chrome](https://deepmind.google/blog/ai-pointer/) ⭐️ 8.6/10

Google DeepMind has unveiled a prototype AI-enhanced mouse pointer called Magic Pointer, which integrates Gemini AI and voice commands for contextual interaction within the Chrome browser. This innovation could lower the barrier to human-AI interaction by making assistance more intuitive and context-aware, potentially reshaping how users interact with web content and applications in the AI era. Magic Pointer is a Chrome extension that uses Gemini to understand page context and user intent, activated by a specific mouse gesture; voice input is supported but text input remains an option, and it is expected to ship as part of Googlebook this fall.

hackernews · devhouse · May 12, 17:40 · [Discussion](https://news.ycombinator.com/item?id=48111581)

**Background**: Traditional mouse pointers merely indicate position, but DeepMind's Magic Pointer transforms the cursor into an active AI agent that can recognize UI elements and offer contextual actions. This builds on recent trends of integrating AI into operating systems and browsers, such as Microsoft's Copilot and Apple's Intelligence features.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/ai-pointer/">Shaping the future of AI interaction by reimagining the mouse ...</a></li>
<li><a href="https://winbuzzer.com/2026/05/13/google-deepmind-details-a-gemini-powered-mouse-poi-xcxwbn/">Google DeepMind Unveils Gemini-Enabled Mouse Pointer for Chrome</a></li>
<li><a href="https://www.explainx.ai/blog/google-deepmind-magic-pointer-ai-cursor">Google DeepMind's Magic Pointer: The AI Cursor That ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some express skepticism about voice commands due to privacy and social awkwardness, while others find the concept promising for continuous LLM interaction. A few have started building similar open-source projects, and there is criticism that the system is slower than typing.

**Tags**: `#AI`, `#human-computer interaction`, `#voice control`, `#mouse pointer`, `#DeepMind`

---

<a id="item-10"></a>
## [OpenAI Forms $4B Deployment Company, Apple Intel Ties](https://stratechery.com/2026/the-deployment-company-back-to-the-70s-apple-and-intel/) ⭐️ 8.5/10

OpenAI launched the OpenAI Deployment Company (DeployCo) with $4 billion in backing from TPG, Goldman Sachs, and McKinsey, and is acquiring London-based AI consulting firm Tomoro. Meanwhile, Apple has economic reasons to partner with Intel, as analyzed in the Stratechery article. This signals that AI's impact will be driven by top-down organizational implementation, moving beyond model development to real-world deployment. For Apple, partnering with Intel could reshape its chip supply chain and competitive dynamics in the industry. The deployment company is backed by $4 billion from major investors and includes the acquisition of Tomoro. This reinforces the thesis that enterprises need specialized support to integrate frontier AI into production for measurable business impact.

rss · Stratechery · May 13, 10:00

**Background**: Top-down AI implementation means that organizations deploy AI through central planning and executive directives, as opposed to bottom-up grassroots adoption. OpenAI's new company aims to help enterprises adopt AI at scale, addressing the complexity of moving from research prototypes to production systems. This approach is similar to how enterprise software companies provide consulting and implementation services.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-launches-the-deployment-company/">OpenAI launches the OpenAI Deployment Company to help ...</a></li>
<li><a href="https://www.crn.com/news/ai/2026/openai-launches-services-business-on-heels-of-similar-anthropic-announcement">OpenAI Debuts $4B AI Services Company As Rival Anthropic ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#Deployment`, `#Apple`, `#Intel`

---

<a id="item-11"></a>
## [Nobel-winning economist flags three AI trends to watch](https://www.technologyreview.com/2026/05/11/1137090/three-things-in-ai-to-watch-according-to-a-nobel-winning-economist/) ⭐️ 8.4/10

Daron Acemoglu, a Nobel Prize-winning economist, has outlined three key developments in AI that he believes deserve close attention, offering a critical perspective on the influence of Big Tech companies. As a Nobel laureate in economics, Acemoglu's views carry significant weight in shaping public and policy discourse on AI, especially his skepticism toward Big Tech's unchecked power and its implications for society and labor markets. The article previews Acemoglu's analysis from a paper published before his Nobel win in 2024, which reportedly drew criticism from Silicon Valley for its skeptical stance on Big Tech's role in AI development.

rss · MIT Tech Review · May 11, 17:35

**Background**: Daron Acemoglu is a prominent economist known for his work on institutions, technological change, and economic growth. His recent research has focused on the economic impacts of AI, often warning about the risks of automation and inequality. The MIT Technology Review article captures his perspective on AI trends that merit scrutiny, particularly regarding corporate concentration and labor displacement.

**Tags**: `#AI`, `#economics`, `#Daron Acemoglu`, `#technology trends`, `#MIT Technology Review`

---

<a id="item-12"></a>
## [Why Senior Developers Struggle to Communicate Expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise) ⭐️ 8.2/10

This article explores the reasons senior developers often fail to articulate their expertise, attributing it to the nature of tacit knowledge and internal world models that are difficult to verbalize. Understanding this communication gap is crucial for improving knowledge transfer in software teams, where senior experience is vital but often underutilized. The article suggests that senior developers' expertise is deeply tied to their internal 'world model,' making it inseparable from their intuition.

hackernews · nilirl · May 12, 15:08 · [Discussion](https://news.ycombinator.com/item?id=48109460)

**Background**: Tacit knowledge is knowledge that is difficult to transfer through writing or verbalizing. Senior developers often accumulate such knowledge through years of experience, yet struggle to explain their decision-making because much of it is intuitive.

**Discussion**: Community comments highlight varied perspectives: some agree that tacit knowledge is hard to communicate, others criticize blanket statements about senior developers, and there is discussion about the 'avoider' vs 'experimenter' dichotomy.

**Tags**: `#senior developers`, `#communication`, `#expertise`, `#software engineering`, `#professional development`

---

<a id="item-13"></a>
## [Six CVEs Released for Critical dnsmasq Vulnerabilities](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 8.2/10

CERT has released six Common Vulnerabilities and Exposures (CVEs) for serious security vulnerabilities in dnsmasq, a lightweight DNS and DHCP server. The vulnerabilities affect versions prior to the upcoming patch, allowing remote attacks. dnsmasq is embedded in millions of home routers and IoT devices, making these vulnerabilities critical for widespread network infrastructure. The discovery has reignited calls for rewriting such software in memory-safe languages to prevent future exploits. The vulnerabilities include a remote heap out-of-bounds write, an infinite loop causing denial of service, and a DHCP buffer overflow. These issues can be triggered by malicious DNS queries or DHCP requests.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: dnsmasq is a widely-deployed open-source software providing DNS caching, DHCP server, and network boot services for small networks. It is known for low resource usage and is included in many Linux distributions, Android, and consumer routers. Memory safety bugs like buffer overflows are common in C/C++ code, prompting interest in memory-safe alternatives such as Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://thekelleys.org.uk/dnsmasq/doc.html">Dnsmasq - network services for small networks.</a></li>
<li><a href="https://www.memorysafety.org/docs/memory-safety/">What is memory safety and why does it matter? - Prossimo</a></li>

</ul>
</details>

**Discussion**: Community members expressed urgency, with one user calling this a breaking point for rewriting code in memory-safe languages like Rust or Go. Another sarcastically noted the widespread use of dnsmasq in devices that rarely receive updates.

**Tags**: `#security`, `#DNS`, `#CVE`, `#memory safety`, `#dnsmasq`

---

<a id="item-14"></a>
## [Using LLM in script shebang lines](https://simonwillison.net/2026/May/11/llm-shebang/#atom-everything) ⭐️ 8.2/10

Simon Willison demonstrates how to use the LLM command-line tool in a script's shebang line to generate text directly from text files, leveraging fragments, tool calls, and YAML templates. This approach enables plain text files to become executable AI-powered scripts, blurring the line between documentation and automation, and opens up new possibilities for lightweight prompt-driven workflows. The shebang can use `-f` for fragments, `-T` for tool calls (e.g., `llm_time`), and `-t` for YAML templates defining custom Python functions and models like `gpt-5.4-mini`.

rss · Simon Willison · May 11, 18:48

**Background**: LLM is an open-source command-line tool by Simon Willison that allows users to interact with various large language models via APIs or locally. Fragments enable adding content from files or URLs into prompts, while tool calling lets LLMs execute predefined functions. The shebang line (`#!`) tells Unix systems to run the script with a specific interpreter, and this technique repurposes it for AI text generation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the command-line · GitHub</a></li>
<li><a href="https://llm.datasette.io/en/stable/fragments.html">Fragments - LLM</a></li>
<li><a href="https://news.ycombinator.com/item?id=40782755">Language models on the command line | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News comment by Kim_Bruning that inspired this was a playful suggestion to put a shebang on English text files. The community reaction appears positive, focusing on the practical utility and novelty of treating text files as executable prompts.

**Tags**: `#LLM`, `#shebang`, `#scripting`, `#AI tools`, `#command-line`

---

<a id="item-15"></a>
## [AI Agents Build Economic Datasets with DRIL](https://feeds.feedblitz.com/~/955775837/0/marginalrevolution~Using-agents-to-build-economic-datasets.html) ⭐️ 8.1/10

Researchers propose Deep Research on a Loop (DRIL), a methodology that uses AI agents to automatically construct economic datasets from publicly available sources, significantly reducing the cost and effort of data collection. This approach could democratize empirical economics by making dataset construction accessible to smaller research teams and enabling large-scale cross-country or historical analyses that were previously impractical. DRIL employs a two-stage architecture: a fixed research instrument is applied across a mapped unit space (e.g., countries by years), and the stages separate the tasks of information retrieval and data structuring.

rss · Marginal Revolution · May 12, 04:26

**Background**: Constructing datasets from primary sources is one of the most costly and time-consuming tasks in empirical economics, often requiring manual extraction and validation. AI agents, powered by large language models, can automate parts of this workflow by navigating websites, extracting tables, and cleaning data.

<details><summary>References</summary>
<ul>
<li><a href="https://marginalrevolution.com/marginalrevolution/2026/05/using-agents-to-build-economic-datasets.html">Using agents to build economic datasets - Marginal REVOLUTION</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about data reliability and quality, questioning whether AI-generated datasets can be trusted without extensive validation. However, some acknowledged the potential and noted that with proper checks, the methodology could be valuable.

**Tags**: `#AI agents`, `#economic datasets`, `#DRIL`, `#empirical economics`, `#research methodology`

---

<a id="item-16"></a>
## [Claude Code v2.1.139 adds agent view and /goal command](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) ⭐️ 8.0/10

Claude Code v2.1.139 introduces an agent view that lists all sessions, a /goal command for sustained multi-turn tasks, and several UX improvements like adjustable scroll speed and enhanced hook configuration. These features significantly enhance developer productivity by enabling simultaneous management of multiple coding sessions and hands-free task completion, making Claude Code a more powerful agentic coding tool. The agent view is a research preview accessible via the 'claude agents' command. The /goal command works in interactive, -p, and Remote Control modes, displaying live metrics. Hooks now support an exec form with direct command execution and a 'continueOnBlock' option for PostToolUse.

github · ashwin-ant · May 11, 18:43

**Background**: Claude Code is an agentic coding tool from Anthropic that operates in the terminal, understands codebases, and assists with tasks through natural language. Agent view provides a centralized dashboard to monitor and manage multiple Claude Code sessions. Hooks are deterministic shell commands attached to events, enabling custom workflows and safety checks.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/agent-view">Manage multiple agents with agent view - Claude Code Docs</a></li>
<li><a href="https://github.com/anthropics/claude-code/releases">Releases · anthropics/ claude - code · GitHub</a></li>
<li><a href="https://c-ai.chat/claude-code/claude-code-hooks/">Claude Code Hooks — PreToolUse, PostToolUse, St… - c-ai.chat</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Claude Code`, `#agent`, `#dev tools`

---

<a id="item-17"></a>
## [LLM 0.32a2 Adds OpenAI /v1/responses Support](https://simonwillison.net/2026/May/12/llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32a2 alpha now uses OpenAI's /v1/responses endpoint for GPT-5 class models, enabling display of reasoning tokens in the CLI with color-coded output. This update improves transparency for users running reasoning-heavy models, making it easier to understand and debug model behavior. It also ensures LLM stays compatible with OpenAI's latest API evolution. Reasoning tokens are displayed in a different color from standard error, and can be hidden using the -R or --hide-reasoning flags. This change applies to most reasoning-capable OpenAI models.

rss · Simon Willison · May 12, 17:45

**Background**: LLM is a command-line tool for running large language models. OpenAI recently introduced the /v1/responses endpoint to support stateful reasoning interactions, replacing /v1/chat/completions for GPT-5 class models. Reasoning tokens are internal tokens used by models to plan and reason before producing final output.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/migrate-to-responses">Migrate to the Responses API | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/reasoning">Reasoning models | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#llm`, `#OpenAI`, `#GPT-5`, `#tooling`, `#reasoning`

---

<a id="item-18"></a>
## [Parameter Golf reveals insights for AI-assisted research](https://openai.com/index/what-parameter-golf-taught-us) ⭐️ 7.8/10

OpenAI's Parameter Golf competition, which attracted over 1,000 participants and 2,000 submissions, explored AI-assisted ML research, coding agents, quantization, and novel model design under strict constraints of a 16MB weight and code limit and a 10-minute training budget on 8×H100 GPUs. This competition demonstrates that combining human creativity with AI-assisted tools can push the boundaries of model compression and efficient design, which is critical for deploying LLMs on resource-constrained devices. The insights gained could accelerate the development of more efficient AI models and coding agents. Participants were required to train a language model that fits within a 16MB total size (weights and training code combined) using at most 10 minutes on 8×H100 GPUs. The competition highlighted techniques such as quantization, pruning, and novel architectures to achieve high performance under extreme constraints.

rss · OpenAI Blog · May 12, 00:00

**Background**: Model compression techniques like quantization reduce the precision of model weights from 32-bit floats to lower-bit formats (e.g., 8-bit integers), significantly cutting memory usage while preserving accuracy. AI-assisted research involves using AI tools (e.g., coding agents) to help design and optimize machine learning models. Parameter Golf is a challenge that tests both human ingenuity and the effectiveness of AI assistance in creating extremely efficient models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/parameter-golf/">OpenAI Model Craft: Parameter Golf | OpenAI</a></li>
<li><a href="https://the-decoder.com/openai-turns-model-compression-into-a-talent-hunt-with-its-16-mb-parameter-golf-challenge/">OpenAI turns model compression into a talent hunt with its 16 MB "Parameter Golf" challenge</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/what-is-quantization/">What is quantization in machine learning ? | Cloudflare</a></li>

</ul>
</details>

**Tags**: `#AI-assisted research`, `#parameter golf`, `#machine learning`, `#quantization`, `#coding agents`

---

<a id="item-19"></a>
## [Developer leaves GitHub for self-hosted Forgejo over AI scraping and centralization concerns](https://jorijn.com/en/blog/leaving-github-for-forgejo/) ⭐️ 7.7/10

A developer announced they are moving their Git repositories from GitHub to a self-hosted Forgejo instance, citing concerns about AI scraping of code and a desire for decentralization. This migration reflects a growing trend of developers leaving centralized platforms like GitHub due to privacy and control issues, potentially accelerating the adoption of self-hosted forges like Forgejo. Forgejo is a lightweight, self-hosted software forge for Git, offering features like bug tracking, code review, and continuous integration, and was created in 2022 as a community-owned fork of Gitea.

hackernews · jorijn · May 13, 12:54 · [Discussion](https://news.ycombinator.com/item?id=48121266)

**Background**: GitHub, owned by Microsoft, is a centralized platform for version control and collaboration using Git. Many developers are becoming concerned about how their code is used, particularly for training AI models, leading to a push towards self-hosted alternatives that give users full control over their data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://forgejo.org/">Forgejo – Beyond coding. We forge.</a></li>
<li><a href="https://codeberg.org/forgejo/forgejo">forgejo/forgejo: Beyond coding. We forge. - Codeberg.org</a></li>

</ul>
</details>

**Discussion**: The Hacker News comments express support for self-hosting and share similar concerns about AI scraping; some suggest tools like GitSocial for cross-forge collaboration, while others note that Git was always meant to be decentralized and that GitHub's convenience created centralization. A few commenters recommend Fossil as an alternative that packages all repository state in a single file.

**Tags**: `#self-hosting`, `#git`, `#forgejo`, `#decentralization`, `#open-source`

---

<a id="item-20"></a>
## [Zombie Internet: AI Content Pollutes Online](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 7.7/10

Jason Koebler's article on 404 Media introduces the 'Zombie Internet' concept, describing how AI-generated content blends with human output, exhausting readers. This highlights a growing problem where AI writing degrades online discourse and mental wellbeing, potentially eroding trust in digital content. The 'Zombie Internet' differs from the 'Dead Internet' theory by including human-AI interactions, such as people using AI agents to talk to others, and commercial spam.

rss · Simon Willison · May 11, 19:21

**Background**: The Dead Internet theory suggests most online content is bot-generated. Koebler's Zombie Internet is a more insidious variant where humans and AI coexist, creating a confusing mix. AI agents are software that can autonomously pursue goals using AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory - Wikipedia</a></li>
<li><a href="https://tech.yahoo.com/social-media/articles/zombie-internet-arrived-devastating-consequences-100000186.html">The ‘ zombie internet ’ has arrived—and it has devastating...</a></li>

</ul>
</details>

**Tags**: `#AI writing`, `#Zombie Internet`, `#online content quality`, `#AI impact`, `#Jason Koebler`

---

<a id="item-21"></a>
## [Obsidian Unveils New Community Site and Plugin Review System](https://obsidian.md/blog/future-of-plugins/) ⭐️ 7.4/10

Obsidian has launched a new community website and automated plugin review system to replace the previous manual review bottleneck that made submitting new plugins nearly impossible. This change significantly reduces friction for plugin developers, alleviates burnout for the small Obsidian team, and helps maintain the app's vibrant ecosystem that depends on community contributions. The new system includes automated security checks and community-based review, though some experts question whether automated checks alone can reliably catch malicious plugins. CEO Kepano noted this is a first version with many improvements planned.

hackernews · xz18r · May 12, 15:45 · [Discussion](https://news.ycombinator.com/item?id=48109970)

**Background**: Obsidian is a note-taking application that stores notes as plain Markdown files, offering extensive customization through plugins written in web technologies. The plugin ecosystem grew rapidly, especially with AI-assisted development, leading to a backlog of submissions and developer frustration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Obsidian_(software)">Obsidian (software) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Developer reactions were largely positive, with many acknowledging the severe submission bottleneck that existed previously. Some commenters expressed skepticism about automated security checks, advocating instead for a proper sandbox with an explicit permission API to eliminate the need for reviews.

**Tags**: `#Obsidian`, `#Plugin Ecosystem`, `#Dev Tools`, `#Community Management`, `#Software Engineering`

---

<a id="item-22"></a>
## [Data Centers Boost AI and Cloud Computing, Says Economist](https://feeds.feedblitz.com/~/955834529/0/marginalrevolution~Data-centers-are-good.html) ⭐️ 7.4/10

Tyler Cowen argues in a blog post that despite local concerns over environmental and economic impacts, data centers provide net benefits by enabling AI and cloud computing. This perspective matters as communities and policymakers weigh the costs and benefits of data center expansion, which is accelerating due to AI demand. The post highlights a local policy tradeoff: data centers create jobs and tax revenue but also strain water and power resources.

rss · Marginal Revolution · May 13, 05:13

**Background**: Data centers are large facilities that house computer servers and networking equipment, forming the backbone of cloud computing and AI services. Their rapid expansion has sparked debates over energy consumption, water usage, and local economic benefits.

**Discussion**: Commenters discuss specific tradeoffs, with some noting that data center construction costs and messaging could be improved to gain public support.

**Tags**: `#data centers`, `#AI infrastructure`, `#economics`, `#cloud computing`, `#tech policy`

---

<a id="item-23"></a>
## [Claude Code v2.1.140: Bug Fixes and Minor Improvements](https://github.com/anthropics/claude-code/releases/tag/v2.1.140) ⭐️ 7.3/10

Anthropic released version 2.1.140 of Claude Code, a patch update focusing on bug fixes and minor improvements, including better subagent type matching and fixes for several hanging, hook, and startup issues. This update improves reliability and user experience for developers using Claude Code as an AI coding agent, fixing subtle bugs that could cause hangs or misconfigurations, which is critical for agentic workflows in production. Notable fixes include: `/goal` no longer hangs when hooks are disabled; symlinked settings files no longer trigger spurious config change hooks; background service startup gives more time on enterprise endpoint security systems; and Windows event-loop stalls caused by missing executables are resolved.

github · ashwin-ant · May 12, 21:09

**Background**: Claude Code is an agentic coding tool from Anthropic that lives in the terminal, helping developers understand codebases, edit files, run commands, and automate workflows. It can spawn subagents for focused tasks, and permission rules can match subagent types case- and separator-insensitively. The tool also supports hooks for reacting to config changes and other events.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">Claude Code is an agentic coding tool that lives in your ...</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/58540">[DOCS] [Permissions] Agent(subagent) matching docs omit case ...</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#agentic systems`, `#bug-fixes`, `#AI-tools`, `#Anthropic`

---

<a id="item-24"></a>
## [AutoScout24 boosts engineering with AI workflows](https://openai.com/index/autoscout24) ⭐️ 7.3/10

AutoScout24 Group has adopted OpenAI's Codex and ChatGPT to accelerate development cycles, improve code quality, and scale AI adoption across its engineering teams. This case study demonstrates how a large automotive marketplace can leverage AI coding agents to boost developer productivity and code quality, offering a replicable model for other enterprises exploring AI-assisted engineering. AutoScout24 uses Codex for automated code generation and debugging, while ChatGPT assists in documentation and code review. The integration has led to faster iteration and fewer defects in production.

rss · OpenAI Blog · May 12, 00:00

**Background**: OpenAI Codex is an AI system that translates natural language into code, powering tools like GitHub Copilot. ChatGPT, also from OpenAI, helps with conversational tasks including code explanation and brainstorming. AutoScout24 is a leading online car marketplace in Europe, with a large engineering organization.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>

</ul>
</details>

**Tags**: `#AI workflows`, `#Codex`, `#ChatGPT`, `#software engineering`, `#AutoScout24`

---

<a id="item-25"></a>
## [As researchers age, disruptive work declines](https://nautil.us/is-this-why-science-advances-one-funeral-at-a-time-1280650) ⭐️ 7.2/10

A Nautilus article explores the observation that older researchers tend to produce less disruptive work, citing factors such as staying in one field too long and settling into conventional thinking. This pattern has implications for how scientific innovation is fostered and funded, as it suggests that encouraging researchers to switch fields or maintain novelty could increase breakthrough discoveries. The article references examples like Yuval Ne'eman, who discovered SU(3) after switching from a military career, and Douglas Adams's rules about technology adoption ages.

hackernews · Brajeshwar · May 12, 17:16 · [Discussion](https://news.ycombinator.com/item?id=48111243)

**Background**: The phenomenon 'science advances one funeral at a time' refers to Max Planck's observation that new scientific truths are often accepted not by convincing opponents but by waiting for them to die off. This article suggests a similar dynamic related to researcher age and disruptive work.

**Discussion**: Commenters debated whether the cause is age itself or time spent in a field, with some suggesting that switching fields or maintaining novelty can sustain creativity. Others highlighted confounding factors like family obligations and biological changes.

**Tags**: `#science`, `#research`, `#innovation`, `#academia`, `#aging`

---

<a id="item-26"></a>
## [Mitchell Hashimoto: TDM Motivated by Fear of Being Fired](https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything) ⭐️ 7.2/10

Mitchell Hashimoto argued that most Technical Decision Makers (TDMs) are primarily motivated by not getting fired, and thus follow secular trends and analyst recommendations rather than pursuing genuine innovation. This insight challenges the common perception that technical leaders are driven by passion and deep expertise, highlighting how career risk aversion can shape technology adoption and industry direction. Hashimoto's comment was made in a Lobsters discussion about the Redis homepage design, and he specifically mentions Gartner and McKinsey as influencers of TDM behavior.

rss · Simon Willison · May 12, 22:21

**Background**: A Technical Decision Maker (TDM) is a role in organizations responsible for making technical choices, often balancing business needs with technology options. Hashimoto's argument suggests that many TDMs prioritize job security over genuine technological innovation, leading to herd behavior in the market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.acronymfinder.com/Technical-Decision-Maker-(various-companies)-(TDM).html">TDM - Technical Decision Maker (various companies ...</a></li>
<li><a href="https://marketingwithjay.uk/bdm-vs-tdm-understanding-the-dual-perspectives-in-it-decisions/">BDM vs TDM: Understanding the Dual Perspectives in IT ...</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#product management`, `#marketing`, `#AI strategy`, `#industry analysis`

---

<a id="item-27"></a>
## [AI's Transitional Employment Problems: Non-Obvious Hurdles](https://feeds.feedblitz.com/~/955838699/0/marginalrevolution~Some-nonobvious-reasons-why-AI-will-create-some-transitional-problems-in-employment.html) ⭐️ 7.1/10

Tyler Cowen argues that while mass unemployment from AI is unlikely, three non-obvious transitional problems will arise: new jobs emerging in highly regulated sectors, potential skill mismatches, and short-term adjustment costs. This analysis shifts the debate from apocalyptic job loss to real but manageable transitional frictions, highlighting regulatory and structural barriers that could slow adaptation to AI-driven changes. Cowen specifically points out that new AI-related jobs may concentrate in heavily regulated sectors like healthcare and law, where occupational licensing and compliance requirements create entry barriers.

rss · Marginal Revolution · May 13, 07:36

**Background**: AI automation is expected to displace some jobs but also create new ones. However, the transition may not be smooth if new jobs require licenses or certifications that take time to obtain. Tyler Cowen, an economist, often writes about technology and economics.

**Discussion**: Comments on the post express skepticism about AI's freedom in regulated sectors and note a conundrum in technology's effect on employment, suggesting that many readers agree with Cowen's nuanced view.

**Tags**: `#AI`, `#employment`, `#transitional problems`, `#economics`, `#Tyler Cowen`

---

<a id="item-28"></a>
## [Rendering the Sky, Sunsets, and Planets with WebGL and Ray Marching](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 7.0/10

Maxime Heckel published a detailed blog post demonstrating how to render realistic skies, sunsets, and planets in the browser using WebGL and ray marching techniques, complete with interactive demos. This work showcases the power of modern web graphics to simulate complex atmospheric scattering effects, making advanced rendering techniques accessible to web developers and inspiring further experimentation in browser-based 3D graphics. The blog uses ray marching with signed distance functions (SDFs) for planet geometry and models atmospheric scattering using Rayleigh and Mie scattering approximations. Interactive demos allow readers to tweak parameters like sun position and atmospheric density in real time.

hackernews · ibobev · May 12, 13:26 · [Discussion](https://news.ycombinator.com/item?id=48107997)

**Background**: Ray marching is a rendering technique where rays are iteratively stepped through a scene to compute intersections with implicit surfaces or volumetric effects. It is well-suited for rendering procedural geometry and participating media like atmosphere. Atmospheric scattering refers to the physical phenomenon where sunlight is scattered by particles in the atmosphere, producing blue skies and red sunsets. WebGL enables hardware-accelerated graphics in the browser without plugins.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ray_marching">Ray marching</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.15010">Physically Based Real‐Time Rendering of Atmospheres using Mie ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the blog's quality and interactivity, with one noting the inspiration from Sebastian Lague's atmosphere video. Another pointed out a realistic limitation: the sky should not go completely black immediately after sunset, as twilight persists until the sun is 18 degrees below the horizon. Overall, the community found the post inspirational and technically impressive.

**Tags**: `#graphics`, `#rendering`, `#WebGL`, `#atmosphere simulation`, `#planet rendering`

---

<a id="item-29"></a>
## [Google Separates Android from I/O Keynote to Spotlight AI](https://sspai.com/post/109699) ⭐️ 7.0/10

In 2025, Google for the first time removed the Android segment from its I/O keynote, hosting a separate event earlier to emphasize its AI-first strategy. This strategic shift signals that AI has become Google's central focus, even above its flagship mobile OS. It could reshape how developers and users perceive Google's priorities in the coming years. The separate Android event was held before Google I/O 2025, while the I/O keynote continued to highlight AI advancements such as Gemini. This move decouples Android updates from the main developer conference.

rss · 少数派 · May 13, 00:10

**Background**: Google I/O is the company's annual developer conference, traditionally where major Android versions and hardware are announced. In recent years, Google has increasingly pushed an 'AI-first' strategy, making AI a priority across products. By separating Android, Google can dedicate more I/O stage time to AI breakthroughs.

<details><summary>References</summary>
<ul>
<li><a href="https://io.google/">Google I/O 2026</a></li>
<li><a href="https://online.hbs.edu/blog/post/ai-first">How to Create an AI-First Company</a></li>

</ul>
</details>

**Tags**: `#Google`, `#Android`, `#AI`, `#I/O`, `#tech strategy`

---