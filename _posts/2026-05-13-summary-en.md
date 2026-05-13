---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 112 items, 30 important content pieces were selected

---

1. [CERT releases six CVEs for critical dnsmasq vulnerabilities](#item-1) ⭐️ 9.0/10
2. [OrcaSlicer fork restores BambuNetwork support](#item-2) ⭐️ 8.0/10
3. [Elevator: Deterministic Binary Translation Without Heuristics](#item-3) ⭐️ 8.0/10
4. [Googlebook: Android Laptop with Gemini AI Sparks Debate](#item-4) ⭐️ 8.0/10
5. [Needle: 26M Parameter Tool-Calling Model from Gemini Distillation](#item-5) ⭐️ 8.0/10
6. [Linux kernel optimization copied into QUIC leads to performance bug](#item-6) ⭐️ 8.0/10
7. [Rendering Realistic Skies with Ray Marching](#item-7) ⭐️ 8.0/10
8. [Quack: DuckDB's New Client-Server Protocol](#item-8) ⭐️ 8.0/10
9. [Massive Security Audit of European Government Domains](#item-9) ⭐️ 8.0/10
10. [Obsidian Launches Automated Plugin Review System](#item-10) ⭐️ 8.0/10
11. [Jason Koebler coins 'Zombie Internet' as AI pollutes web](#item-11) ⭐️ 8.0/10
12. [Shopify's River Agent Teaches via Public Transparency](#item-12) ⭐️ 8.0/10
13. [World Models Top MIT's 10 Things That Matter in AI](#item-13) ⭐️ 8.0/10
14. [Nobel economist highlights three AI trends to watch](#item-14) ⭐️ 8.0/10
15. [OpenAI Deployment Company and Apple-Intel Strategy Analysis](#item-15) ⭐️ 8.0/10
16. [Claude Code v2.1.139 introduces agent view and /goal command](#item-16) ⭐️ 7.0/10
17. [Developer Migrates Infrastructure to European Cloud Providers](#item-17) ⭐️ 7.0/10
18. [Scrcpy v4.0 Adds Flexible Virtual Display](#item-18) ⭐️ 7.0/10
19. [AI Mouse Pointer: DeepMind's Voice-Driven Redesign](#item-19) ⭐️ 7.0/10
20. [User-Controlled CSP Allow-listing via Sandbox Iframe](#item-20) ⭐️ 7.0/10
21. [Mitchell Hashimoto on TDM Risk Aversion](#item-21) ⭐️ 7.0/10
22. [LLM 0.32a2 adds support for OpenAI /v1/responses endpoint](#item-22) ⭐️ 7.0/10
23. [GitLab's Workforce Reduction and Strategic Shift](#item-23) ⭐️ 7.0/10
24. [AI Coding Agents Must Cut Maintenance Costs, Warns James Shore](#item-24) ⭐️ 7.0/10
25. [Parameter Golf: Lessons from AI-Assisted Model Design](#item-25) ⭐️ 7.0/10
26. [AWS Building Blocks for Foundation Model Training and Inference](#item-26) ⭐️ 7.0/10
27. [Varda and United Therapeutics to make drugs in orbit commercially](#item-27) ⭐️ 7.0/10
28. [TechPays acquired by Levels.fyi to boost European pay transparency](#item-28) ⭐️ 7.0/10
29. [Thinking Machines Launches TML-Interaction-Small, New Realtime Voice AI](#item-29) ⭐️ 7.0/10
30. [AI Agent Methodology DRIL Automates Economic Dataset Construction](#item-30) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CERT releases six CVEs for critical dnsmasq vulnerabilities](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT has disclosed six new CVEs affecting dnsmasq, a widely-used DNS/DHCP server, including vulnerabilities that allow remote code execution and denial of service via malformed DNS queries or DHCP requests. These vulnerabilities are critical because dnsmasq is embedded in millions of devices—routers, IoT gadgets, and Android—many of which rarely receive security updates, leaving a vast attack surface exposed. The vulnerabilities include a heap out-of-bounds write from a remote attacker, an infinite loop causing denial of service, and a buffer overflow from malicious DHCP requests.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: Dnsmasq is a lightweight network service that provides DNS caching, DHCP, and router advertisement for small networks. It is included in many Linux distributions, home routers, and Android. Memory safety vulnerabilities like those announced arise from languages like C that lack automatic memory protection, and adopting memory-safe languages such as Rust is increasingly recommended to mitigate such risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/06/24/new-guidance-released-reducing-memory-related-vulnerabilities">New Guidance Released for Reducing Memory-Related Vulnerabilities</a></li>

</ul>
</details>

**Discussion**: Community comments emphasize the urgency of moving to memory-safe languages, with one user calling this a breaking point. Others sarcastically note that dnsmasq is used in devices that almost never get updates, highlighting the real-world impact and the difficulty of patching.

**Tags**: `#security`, `#dnsmasq`, `#CVE`, `#memory-safety`, `#vulnerabilities`

---

<a id="item-2"></a>
## [OrcaSlicer fork restores BambuNetwork support](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

A GitHub repository (FULU-Foundation/OrcaSlicer-bambulab) has been created to restore full BambuNetwork support for Bambu Lab printers, enabling cloud-based printing without restrictions after a controversial firmware update. This fork addresses community outrage over Bambu Lab's firmware update that removed local LAN printing capabilities by requiring cloud authentication, upholding user rights and open-source principles in the 3D printing community. The fork is based on OrcaSlicer and restores internet-based printing via BambuNetwork, bypassing the new cloud authentication requirement that previously locked out third-party slicers.

hackernews · Murfalo · May 12, 21:55 · [Discussion](https://news.ycombinator.com/item?id=48115127)

**Background**: Bambu Lab released a firmware update that added cloud authentication for local printing, effectively requiring users to use their proprietary software. This sparked backlash from the 3D printing community, leading to reverse-engineering efforts. OrcaSlicer is an open-source slicer commonly used with Bambu printers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dafik/OrcaSlicer-bambulab">GitHub - dafik/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>
<li><a href="https://github.com/unS0uL/OrcaSlicer-bambulab">GitHub - unS0uL/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments express anger over the firmware change, with some accusing Bambu of theft by removing functionality. Others provide technical analysis of how the new system works, and some note that Bambu initially required cloud auth for LAN mode before backtracking after backlash.

**Tags**: `#3D-printing`, `#open-source`, `#firmware`, `#controversy`, `#reverse-engineering`

---

<a id="item-3"></a>
## [Elevator: Deterministic Binary Translation Without Heuristics](https://arxiv.org/abs/2605.08419) ⭐️ 8.0/10

Researchers introduced Elevator, the first fully-static, deterministic binary translator that converts entire x86-64 executables to AArch64 without heuristics or runtime fallbacks. This deterministic approach eliminates the non-determinism and security risks of heuristics-based translation, making it suitable for certification in regulated industries like aviation and medical devices. However, the trade-offs in binary size and feature support (single-thread only, no exception handling) limit its immediate practical impact. Elevator achieves ~4.75x runtime speedup over QEMU user-mode JIT but incurs a 50x increase in binary size and a 7x increase in executed instruction count. It only supports single-threaded binaries and lacks exception handling and stack unwinding.

hackernews · matt_d · May 13, 04:25 · [Discussion](https://news.ycombinator.com/item?id=48117810)

**Background**: Binary translation converts executable code from one instruction set architecture (ISA) to another. Fully-static translation processes the entire binary ahead of time without execution, but must heuristically decide which bytes are code versus data, which can introduce errors. Elevator avoids heuristics by considering all possible interpretations of every byte, producing separate translations for each feasible one, and then composing them into a deterministic output.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">Deterministic Fully-Static Whole-Binary Translation without ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_translation">Binary translation - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48117810">Deterministic Fully-Static Whole-Binary Translation Without ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted the 50x size increase as a reasonable trade-off for determinism, especially for certification use cases. Some debated the performance comparison, with one commenter sharing past experience with a custom JIT engine. There was also speculation about using heuristics later to reduce size at the cost of guarantees, and discussion of remaining challenges like relative offsets.

**Tags**: `#binary translation`, `#deterministic`, `#static analysis`, `#systems`, `#emulation`

---

<a id="item-4"></a>
## [Googlebook: Android Laptop with Gemini AI Sparks Debate](https://googlebook.google/) ⭐️ 8.0/10

Google announced Googlebook, a new category of laptops running Android and deeply integrated with the Gemini AI assistant, aiming to redefine app-based computing with a focus on AI-driven interactions. This launch represents Google's latest push to merge mobile and desktop computing through AI, potentially challenging traditional laptop paradigms and expanding the role of AI assistants in daily productivity. Googlebook is built on Android 17 with a desktop mode and Gemini integration, allowing users to interact with data through natural language rather than traditional apps. However, it retains the app-based ecosystem, which has drawn criticism about its target audience and UX coherence.

hackernews · tambourine_man · May 12, 17:37 · [Discussion](https://news.ycombinator.com/item?id=48111545)

**Background**: Chromebooks have long offered a laptop experience based on Chrome OS, while Android has primarily been a mobile OS. Googlebook attempts to blend these by bringing Android to a laptop form factor with a desktop interface and AI-powered features. Gemini is Google's generative AI assistant, capable of processing text, images, audio, and video, and is integrated across Google services.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini.google">Gemini.google</a></li>
<li><a href="https://gemini.google/about/">Learn about Gemini, the everyday AI assistant from Google</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some see Googlebook as a visionary move toward an AI-first, app-less future, praising the potential of Gemini integration. Others criticize the UX, particularly the top panel design, and question the target audience, arguing that Android's app-centric model limits laptop usefulness for traditional computing tasks.

**Tags**: `#Googlebook`, `#Android`, `#AI`, `#laptops`, `#UX`

---

<a id="item-5"></a>
## [Needle: 26M Parameter Tool-Calling Model from Gemini Distillation](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus open-sourced Needle, a 26M parameter model for single-shot tool calling, distilled from Gemini using an attention-only architecture without MLPs. It achieves 6000 tokens/s prefill and 1200 tokens/s decode on consumer devices. This shows that tiny, specialized models can rival larger ones for tool calling, enabling on-device agentic AI on phones, watches, and other edge devices. It also challenges the necessity of MLPs in transformer architectures for retrieval-and-assembly tasks. The model was pretrained on 200B tokens using 16 TPU v6e for 27 hours, then post-trained on 2B tokens of synthesized function-calling data via Gemini for 45 minutes. It outperforms several larger models like FunctionGemma-270M and Qwen-0.6B on single-shot function calling, but lacks conversational breadth.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Traditional transformer models combine attention layers with feedforward networks (MLPs) to learn and store knowledge. Needle removes MLPs entirely, based on the insight that tool calling is a retrieval-and-assembly task where the input provides all needed information, so attention alone suffices. TPU v6e, also known as Trillium, are Google's latest AI accelerators optimized for both training and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://docs.cloud.google.com/tpu/docs/v6e">TPU v6e | Google Cloud Documentation</a></li>

</ul>
</details>

**Discussion**: Community comments raised questions about the model's discriminative power for complex tool use cases, and some noted potential for CLI natural language parsing. Concerns were also voiced about Google's anti-distillation defenses that might degrade student model performance. A user suggested providing a live demo, and another reported independent confirmation of the MLP removal finding.

**Tags**: `#tool calling`, `#model distillation`, `#small language models`, `#on-device AI`, `#function calling`

---

<a id="item-6"></a>
## [Linux kernel optimization copied into QUIC leads to performance bug](https://blog.cloudflare.com/quic-death-spiral-fix/) ⭐️ 8.0/10

Cloudflare engineers discovered that a QUIC performance bug originated from copying a Linux kernel TCP optimization (TCP Small Queues) into their QUIC implementation without incorporating a subsequent kernel fix that relaxed the throttling. This incident highlights the risks of porting kernel code to userspace network stacks, especially for protocols like QUIC that rely on precise pacing and congestion control, and underscores the need to track upstream fixes when forking kernel code. The bug caused a 'death spiral' in QUIC connections where pacing backoff reduced throughput, and the problem only manifested under specific network conditions such as high bandwidth-delay product paths.

hackernews · sbulaev · May 12, 23:46 · [Discussion](https://news.ycombinator.com/item?id=48116064)

**Background**: TCP Small Queues (TSQ) is a Linux kernel mechanism that limits per-socket queued data to reduce bufferbloat and improve latency. Cloudflare's QUIC implementation copied the initial TSQ algorithm but missed a later kernel commit (75eefc6) that relaxed the throttling for certain cases. QUIC pacing is crucial for congestion control algorithms like BBR.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/506237/">tcp: TCP Small Queues - LWN.net</a></li>
<li><a href="https://lwn.net/Articles/469652/">bql: Byte Queue Limits [LWN.net]</a></li>

</ul>
</details>

**Discussion**: Community comments noted the challenge of maintaining in-house implementations forking kernel code, with one user suggesting a more accurate title would be 'How we copied code from Linux kernel without fully understanding it and missed its follow-up fixes.' Another user questioned the use of CUBIC in datacenters and suggested BBR might be more suitable.

**Tags**: `#QUIC`, `#Linux kernel`, `#networking`, `#Cloudflare`, `#bug analysis`

---

<a id="item-7"></a>
## [Rendering Realistic Skies with Ray Marching](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

Maxime Heckel published a detailed technical blog post explaining how to render realistic skies, sunsets, and planets in web browsers using ray marching and atmospheric scattering models. This work demonstrates the growing capability of web-based graphics, enabling complex visual effects that were previously limited to native applications, and inspires further experimentation in real-time rendering. The blog includes interactive demos and covers techniques such as Rayleigh and Mie scattering, Mie phase functions, and ozone absorption to simulate realistic sky colors and twilight.

hackernews · ibobev · May 12, 13:26 · [Discussion](https://news.ycombinator.com/item?id=48107997)

**Background**: Ray marching is a rendering technique that iteratively steps along rays through a scene, sampling at each step, often used for volumetric effects. Atmospheric scattering refers to the physical processes where light is scattered by particles in the atmosphere, causing phenomena like blue skies and red sunsets. Rayleigh scattering by small molecules gives the sky its blue color, while Mie scattering by larger particles adds haze and affects sunset hues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ray_marching">Ray marching</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atmospheric_scattering">Atmospheric scattering</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article's depth and visuals (e.g., baliex called it inspirational), while others pointed out inaccuracies in the sunset model (e.g., gmiller123456 noted the sky should not go black immediately after sunset). References were made to Sebastian Lague's video on atmospheres and the seminal 1993 paper by Nishita et al.

**Tags**: `#computer graphics`, `#rendering`, `#web development`, `#atmospheric scattering`, `#shaders`

---

<a id="item-8"></a>
## [Quack: DuckDB's New Client-Server Protocol](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

On May 12, 2026, DuckDB announced Quack, an HTTP-based client-server protocol that enables remote access and concurrent writes to DuckDB, marking its first official server mode. Quack solves DuckDB's biggest historical limitation—single-user embedded usage—by enabling horizontal scaling and network-based querying, opening up new use cases in distributed analytics and microservices. According to benchmarks, Quack is 32x faster than PostgreSQL for bulk analytics, and it supports multiple concurrent writers on the server side, a feature previously unavailable in DuckDB.

hackernews · aduffy · May 12, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48111765)

**Background**: DuckDB is an in-process SQL OLAP database designed for analytical workloads, traditionally embedded within applications and limited to single-user access. Quack extends DuckDB with a client-server protocol, allowing it to operate as a standalone server accessible over a network, similar to traditional databases like PostgreSQL but optimized for analytics.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/duckdb/duckdb-quack">GitHub - duckdb/duckdb-quack · GitHub</a></li>
<li><a href="https://motherduck.com/blog/first-variant/duckdb-client-server/">If It Quacks Like a Duck: DuckDB Gets a Client-Server Protocol</a></li>
<li><a href="https://byteiota.com/quack-protocol-duckdb-client-server-32x-faster/">Quack Protocol: DuckDB Client-Server 32x Faster | byteiota</a></li>

</ul>
</details>

**Discussion**: The community reaction is generally positive, with users expressing excitement about solving remote access and horizontal scaling problems. Some users noted technical concerns about the definition of concurrent writers, while others appreciated the practical use cases like querying live data without server interruption.

**Tags**: `#duckdb`, `#database`, `#client-server`, `#remote protocol`, `#scalability`

---

<a id="item-9"></a>
## [Massive Security Audit of European Government Domains](https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/) ⭐️ 8.0/10

SecurityBaseline.eu launched on May 13, 2026, revealing that out of 67,000 European government domains, 3,000 sites use illegal tracking cookies, over 1,000 expose database interfaces like phpMyAdmin, and 99% have poorly encrypted email. This audit highlights critical cybersecurity weaknesses in European government digital infrastructure, threatening citizen privacy and national security. It pressures governments to improve baseline security measures and may drive new regulations. The project reports detail that many exposed database interfaces are accessible without authentication, and poor email encryption includes missing or misconfigured DANE or MTA-STS. The data is available via an interactive map at SecurityBaseline.eu.

hackernews · aequitas · May 13, 07:11 · [Discussion](https://news.ycombinator.com/item?id=48118763)

**Background**: SecurityBaseline.eu is a spin-off from the Dutch 'Basisbeveiliging' program, which has monitored baseline security for over a decade. The audit checks for common issues like illegal tracking cookies (violating ePrivacy Directive), publicly accessible database management tools, and email encryption standards (such as DANE and MTA-STS). These are fundamental security hygiene measures that many organizations overlook.

<details><summary>References</summary>
<ul>
<li><a href="https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/">European governments: 3.000 tracking sites, 1.000 phpMyAdmins, and 99% poorly encrypted email. Introducing SecurityBaseline.eu - Internet Cleanup Foundation</a></li>

</ul>
</details>

**Discussion**: Community comments express concern about legal barriers to pentesting in Germany, with some noting that scanning could be considered illegal under hacking laws. Others question data accuracy, pointing out that some flagged sites are non-governmental or decommissioned, and debate whether DNSSEC coloring is excessive. A positive comment highlights the correlation between e-government maturity and security incidents.

**Tags**: `#security`, `#privacy`, `#government`, `#europe`, `#cybersecurity`

---

<a id="item-10"></a>
## [Obsidian Launches Automated Plugin Review System](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian has announced a new automated plugin review system to replace manual reviews, aiming to speed up submissions and reduce developer frustration. This addresses a major scaling bottleneck in Obsidian's plugin ecosystem, which had become nearly impossible to submit new plugins manually. It demonstrates the company's commitment to supporting its developer community as the platform grows. The system relies on automated checks, but some commenters worry about security as plugins still have full disk and network access. The CEO mentioned the team has been working on this for nearly a year and consists of only seven people.

hackernews · xz18r · May 12, 15:45 · [Discussion](https://news.ycombinator.com/item?id=48109970)

**Background**: Obsidian is a popular note-taking app that supports plugins to extend functionality. Previously, all plugins were manually reviewed, leading to long wait times and developer frustration, especially as AI-assisted plugin creation increased submission volume.

**Discussion**: The community response is mixed: many congratulate the team for solving the bottleneck, but there are concerns about automated security checks and the lack of a permission system. Some users worry about future security incidents.

**Tags**: `#Obsidian`, `#plugins`, `#developer tools`, `#community`, `#automation`

---

<a id="item-11"></a>
## [Jason Koebler coins 'Zombie Internet' as AI pollutes web](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler published an angry op-ed on 404 Media coining the term 'Zombie Internet' to describe how AI-generated content is overwhelming the web and exhausting human readers. This piece highlights a growing crisis in online content quality, where AI-generated slop is not only proliferating but also distorting human writing styles. Koebler distinguishes the Zombie Internet from the Dead Internet theory, emphasizing that it involves a complex mix of humans and bots interacting, including people using AI to talk to others, and AI-generated summaries of books being sold as the real thing.

rss · Simon Willison · May 11, 19:21

**Background**: The Dead Internet theory is a conspiracy theory that suggests since around 2016, most internet content and interactions are automated, controlled by algorithms and bots. In contrast, the Zombie Internet describes a state where AI-generated content is pervasive, but real human activity still occurs, creating an exhausting hybrid environment. The term was popularized by Jason Koebler in a 2025 article on 404 Media.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>
<li><a href="https://www.fastcompany.com/91489308/zombie-internet-devastating-consequences-advertising-social-media-human-web-dead-internet-moltbook-ai-tbpn">The ‘ zombie internet ’ has arrived—and it has... - Fast Company</a></li>

</ul>
</details>

**Tags**: `#AI`, `#content quality`, `#internet culture`, `#journalism`

---

<a id="item-12"></a>
## [Shopify's River Agent Teaches via Public Transparency](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything) ⭐️ 8.0/10

Shopify's internal AI coding agent, River, operates entirely in public Slack channels, allowing any employee to observe and participate in interactions, creating an environment of 'osmosis learning' without formal curricula. This transparent approach transforms AI agent usage into a collaborative learning tool, potentially influencing how companies deploy AI agents by prioritizing knowledge sharing and collective improvement. River does not respond to direct messages; it requires users to create public channels. In CEO Tobias Lütke's own channel, over 100 people follow along, adding context, reviews, and learning from the interactions.

rss · Simon Willison · May 11, 15:46

**Background**: River is Shopify's internal AI coding agent designed to assist developers with tasks like code generation and debugging. By making all interactions public, the company turns into a 'Lehrwerkstatt' (teaching workshop), where learning happens organically by observing real work. This contrasts with typical private AI agent interactions and echoes Midjourney's early public Discord approach.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zenml.io/llmops-database/building-a-public-ai-agent-workspace-for-organizational-learning">Shopify: Building a Public AI Agent Workspace for ...</a></li>
<li><a href="https://shopify.dev/docs/apps/build/ai-toolkit">Shopify AI Toolkit</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#software development`, `#internal tools`, `#collaboration`, `#transparency`

---

<a id="item-13"></a>
## [World Models Top MIT's 10 Things That Matter in AI](https://www.technologyreview.com/2026/05/12/1137134/world-models-10-things-that-matter-in-ai-right-now/) ⭐️ 8.0/10

On May 12, 2026, MIT Technology Review published a list of '10 Things That Matter in AI Right Now,' featuring world models as a key emerging area. The publication also announced a subscriber-only roundtable discussion titled 'Can AI Learn to Understand the World?' hosted by executive editor Niall Firth. World models represent a paradigm shift toward AI that can simulate and understand physical dynamics, which is crucial for robotics, autonomous driving, and interactive video generation. MIT Technology Review's endorsement signals that world models are becoming a central focus for the AI industry, driving investment and research. World models differ from large language models by building internal representations that predict how an environment changes in response to actions, simulating physics, object interactions, and causality. The upcoming roundtable will explore how AI may evolve to achieve a deeper understanding of the world.

rss · MIT Tech Review · May 12, 16:22

**Background**: A world model in AI is a neural network that learns an internal representation of an environment and predicts its dynamics over time. These systems enable agents to plan and reason without constant real-world interaction, drawing on ideas dating back to the 1990s. Modern world models are used to train robots and autonomous vehicles by generating synthetic data and simulating physics. They contrast with traditional AI models that focus on classification or generation, offering a path toward more grounded and causal understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://www.forbes.com/sites/nishatalagala/2026/04/19/ai-world-models-what-are-they-and-why-should-you-care/">AI World Models: What Are They And Why Should You Care - Forbes</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Is a World Model? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#AI`, `#world models`, `#MIT Technology Review`, `#emerging technology`

---

<a id="item-14"></a>
## [Nobel economist highlights three AI trends to watch](https://www.technologyreview.com/2026/05/11/1137090/three-things-in-ai-to-watch-according-to-a-nobel-winning-economist/) ⭐️ 8.0/10

Daron Acemoglu, a 2024 Nobel Prize-winning economist, published a paper critical of Big Tech's AI claims and outlined three key areas in AI that he believes deserve close monitoring. Acemoglu's perspective carries significant weight as a Nobel laureate, offering a counterpoint to the often-optimistic AI narratives from Big Tech, and his analysis could influence policy debates and public understanding of AI's economic and societal impacts. The article from MIT Technology Review's newsletter 'The Algorithm' highlights that Acemoglu's critical analysis of Big Tech's claims earned him few fans in Silicon Valley. The specific three things to watch are detailed within the full article, but the summary indicates they stem from his research on the potential overestimation of AI's benefits.

rss · MIT Tech Review · May 11, 17:35

**Background**: Daron Acemoglu is a renowned economist who shared the 2024 Nobel Prize in Economics for his work on institutions and economic growth. His recent research has focused on the economic impact of artificial intelligence, often challenging the prevailing optimistic views among tech companies and investors.

**Tags**: `#AI`, `#Economics`, `#Nobel laureate`, `#Trends`, `#Policy`

---

<a id="item-15"></a>
## [OpenAI Deployment Company and Apple-Intel Strategy Analysis](https://stratechery.com/2026/the-deployment-company-back-to-the-70s-apple-and-intel/) ⭐️ 8.0/10

Ben Thompson's analysis highlights OpenAI's formation of a new deployment-focused company and Apple's economic motivations to partner with Intel. These moves signal a strategic shift: AI deployment requires top-down enterprise integration, and Apple's chip strategy may pivot from exclusive in-house designs to leveraging Intel for cost efficiencies. OpenAI's deployment company has reportedly secured $4 billion in backing from TPG, Goldman Sachs, and McKinsey. The Apple-Intel partnership rationale is not fully detailed in the analysis but suggests economic pressures.

rss · Stratechery · May 13, 10:00

**Background**: OpenAI is known for developing advanced AI models like GPT-4. The new deployment company aims to help enterprises integrate AI into critical operations. Apple has historically used custom silicon (Apple Silicon) and recently moved away from Intel processors for Macs; a potential partnership would mark a reversal.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-launches-the-deployment-company/">OpenAI launches the OpenAI Deployment Company to help ...</a></li>
<li><a href="https://techjournal.org/openai-launches-4-billion-deployment-company">OpenAI Launches $4B Deployment Company: What It Means for ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#Apple`, `#Intel`, `#strategy`

---

<a id="item-16"></a>
## [Claude Code v2.1.139 introduces agent view and /goal command](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) ⭐️ 7.0/10

Anthropic released Claude Code v2.1.139, adding an agent view that lists all sessions and a /goal command that allows Claude to work across turns until a condition is met. These features significantly improve developer productivity by enabling better session management and autonomous task completion, making Claude Code more powerful for complex, multi-step coding workflows. The agent view shows running, blocked, and completed sessions; the /goal command works in interactive, -p, and Remote Control modes with a live overlay panel showing elapsed time, turns, and tokens.

github · ashwin-ant · May 11, 18:43

**Background**: Claude Code is Anthropic's terminal-based AI coding assistant that understands codebases, edits files, and runs commands through natural language. The agent view provides a centralized dashboard for managing multiple sessions, while the /goal command allows Claude to autonomously work towards a defined objective without constant user prompting.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/releases">Releases · anthropics/ claude - code · GitHub</a></li>
<li><a href="https://gist.github.com/yurukusa/afd1b170cbe76101c15942c7a0471310">Claude Code v2.1.139's / goal command and issue #58373...</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI coding assistant`, `#release notes`, `#developer tools`, `#Anthropic`

---

<a id="item-17"></a>
## [Developer Migrates Infrastructure to European Cloud Providers](https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/) ⭐️ 7.0/10

A developer details their experience migrating their digital infrastructure from US-based providers to European alternatives, citing regulatory and privacy concerns under GDPR. This migration reflects a growing trend of digital sovereignty in Europe, offering practical insights for others considering similar moves to reduce reliance on US cloud services. The author moved from Cloudflare to Bunny CDN and built a Terraform setup for cross-provider high availability within Europe.

hackernews · monokai_nl · May 13, 11:42 · [Discussion](https://news.ycombinator.com/item?id=48120629)

**Background**: Digital sovereignty refers to a country's or individual's control over their own data and technology infrastructure. In Europe, this is driven by GDPR compliance and concerns over US surveillance laws, leading many to seek European cloud providers like Scaleway or Hetzner.

**Discussion**: Commenters share similar experiences: one notes that EU government officials increasingly ask about European hosting, another successfully migrated product hosting and built a Terraform setup, while others praise Scaleway as a reliable provider. Some irony was noted about rate limiting via Cloudflare despite moving to European stack.

**Tags**: `#cloud`, `#infrastructure`, `#GDPR`, `#Europe`, `#DevOps`

---

<a id="item-18"></a>
## [Scrcpy v4.0 Adds Flexible Virtual Display](https://github.com/Genymobile/scrcpy/releases/tag/v4.0) ⭐️ 7.0/10

Scrcpy v4.0 has been released, introducing a flexible virtual display that can be resized dynamically along with the client window using the --flex-display (or -x) flag. This enhancement makes Scrcpy even more versatile for users who need to mirror Android devices onto larger screens, enabling seamless resizing without compromising display quality. It significantly improves user experience for developers, testers, and anyone using virtual displays for productivity. The flexible display feature is activated by passing -x or --flex-display when starting a new virtual display with --new-display. This works alongside other options like codec selection and resolution limits.

hackernews · xnx · May 12, 20:50 · [Discussion](https://news.ycombinator.com/item?id=48114356)

**Background**: Scrcpy is a free and open-source tool that displays and controls Android devices connected via USB or wirelessly, with high performance and low latency. Version 3.0 introduced virtual displays, allowing a separate display from the device screen. Version 4.0 builds on that by making the virtual display size automatically adapt to the client window, providing a more integrated experience.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Genymobile/scrcpy">GitHub - Genymobile/scrcpy: Display and control your Android device · GitHub</a></li>
<li><a href="https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md">scrcpy/doc/virtual_display.md at master · Genymobile/scrcpy</a></li>
<li><a href="https://itsfoss.community/t/scrcpy-3-0-comes-with-virtual-displays/12873">Scrcpy 3.0 comes with virtual displays! - Discussion - It's FOSS Community</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive, with users praising the seamless ease of use. However, a Samsung user reports a gesture navigation bug that persists even in v4.0, requiring a phone restart. Others share creative use cases like using a phone as a WiFi bridge.

**Tags**: `#android`, `#screen-mirroring`, `#open-source`, `#tooling`

---

<a id="item-19"></a>
## [AI Mouse Pointer: DeepMind's Voice-Driven Redesign](https://deepmind.google/blog/ai-pointer/) ⭐️ 7.0/10

DeepMind has proposed an AI-powered mouse pointer that uses voice commands and contextual understanding to streamline user interactions, allowing actions like moving objects or adding text via spoken prompts. This concept could fundamentally change human-computer interaction by reducing reliance on menus and keyboard shortcuts, but raises significant usability and privacy concerns that may limit adoption. The pointer integrates with an LLM to interpret context and voice input, but critics note that many actions could be performed faster with existing menus or keyboard shortcuts, and the constant server communication raises privacy risks.

hackernews · devhouse · May 12, 17:40 · [Discussion](https://news.ycombinator.com/item?id=48111581)

**Background**: The mouse pointer is a fundamental element of graphical user interfaces, typically controlled by physical movement. DeepMind's proposal adds an AI layer that enables context-aware interactions, potentially reducing the need for manual navigation. Voice control in computing has a long history but remains niche due to accuracy and social awkwardness.

**Discussion**: Commenters are skeptical, with many pointing out that voice control is impractical in shared spaces and that the demos show no time savings over traditional methods. Privacy concerns about constant server communication are also raised. A few commenters see potential in a continuous 'point and talk' interaction with LLMs.

**Tags**: `#AI`, `#human-computer interaction`, `#DeepMind`, `#user interface`, `#voice control`

---

<a id="item-20"></a>
## [User-Controlled CSP Allow-listing via Sandbox Iframe](https://simonwillison.net/2026/May/13/csp-allow/#atom-everything) ⭐️ 7.0/10

Simon Willison created a tool that loads an app in a CSP-protected sandbox iframe, intercepts fetch errors caused by CSP violations, and prompts the user to add the blocked origin to an allow-list, then refreshes the page. This experiment introduces a novel, user-driven approach to managing Content Security Policy, potentially making it easier to handle dynamic third-party resource needs without relaxing overall security. The tool uses a custom fetch() inside the sandbox to catch CSP errors and communicate them to the parent window, which then displays a modal asking for user consent; it was built using GPT-5.5 xhigh in the Codex desktop app.

rss · Simon Willison · May 13, 04:50

**Background**: Content Security Policy (CSP) is a browser security mechanism that restricts which resources a page can load, typically via an HTTP header. The sandbox attribute on iframes further restricts the embedded content, giving it a unique origin and limiting its capabilities. Normally, CSP allow-lists are static and set by the server; this experiment dynamically adjusts the allow-list based on user interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox">Content-Security-Policy: sandbox directive - HTTP | MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP">Content Security Policy (CSP) - HTTP | MDN - MDN Web Docs Usage example</a></li>

</ul>
</details>

**Tags**: `#CSP`, `#security`, `#web`, `#sandbox`, `#iframe`

---

<a id="item-21"></a>
## [Mitchell Hashimoto on TDM Risk Aversion](https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything) ⭐️ 7.0/10

Mitchell Hashimoto, co-founder of HashiCorp, posted a critical observation on Lobste.rs that 90% of technical decision makers are primarily motivated by avoiding blame, leading them to follow analyst trends like 'AI strategy' rather than genuine innovation. This insight highlights a pervasive but under-discussed driver of enterprise technology adoption, explaining why buzzword-driven purchases often win over technically superior solutions, and may help developers and vendors better understand decision-maker psychology. The quote came from a Lobste.rs discussion about the Redis homepage design. Hashimoto distinguishes between passionate contributors and risk-averse managers who rely on analyst endorsements (e.g., Gartner, McKinsey) to justify purchases.

rss · Simon Willison · May 12, 22:21

**Background**: Mitchell Hashimoto is well-known as the co-founder of HashiCorp and creator of popular DevOps tools like Vagrant, Terraform, and Consul. Technical decision makers (TDMs) are individuals in organizations responsible for choosing which technologies to adopt. Hashimoto's critique reflects a common pattern where risk-averse behavior leads to herd mentality in tech procurement, prioritizing safe choices aligned with market trends over innovative but unproven alternatives.

**Tags**: `#technology decision making`, `#marketing`, `#tech industry`, `#risk aversion`

---

<a id="item-22"></a>
## [LLM 0.32a2 adds support for OpenAI /v1/responses endpoint](https://simonwillison.net/2026/May/12/llm/#atom-everything) ⭐️ 7.0/10

The alpha release of LLM 0.32a2 now uses OpenAI's /v1/responses endpoint for most reasoning-capable models instead of /v1/chat/completions, enabling interleaved reasoning across tool calls and displaying summarized reasoning tokens to users. This update allows users to see the reasoning process behind model outputs, enhancing transparency and debugging capabilities for developers working with OpenAI's advanced reasoning models like GPT-5 class models. The reasoning tokens are displayed in a different color to standard error, and users can hide them with the -R or --hide-reasoning flags. The change is part of pull request #1435 in the open-source LLM project.

rss · Simon Willison · May 12, 17:45

**Background**: LLM is a command-line tool and Python library by Simon Willison for interacting with large language models. The /v1/responses endpoint is OpenAI's new API for advanced agentic workflows and chain-of-thought reasoning. Reasoning tokens are internal tokens used by models to plan and generate intermediate outputs before providing a final answer.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.openai.com/docs/api-reference/responses">platform. openai .com/docs/api-reference/ responses</a></li>
<li><a href="https://openrouter.ai/docs/guides/best-practices/reasoning-tokens">Reasoning Tokens | Enhanced AI... | OpenRouter | Documentation</a></li>

</ul>
</details>

**Tags**: `#llm`, `#openai`, `#reasoning`, `#tool release`, `#ai`

---

<a id="item-23"></a>
## [GitLab's Workforce Reduction and Strategic Shift](https://simonwillison.net/2026/May/11/gitlab-act-2/#atom-everything) ⭐️ 7.0/10

GitLab announced a 7% workforce reduction, plans to reduce its country footprint by 30%, flatten management layers, and retire its CREDIT values framework in favor of new values like 'Speed with Quality' and 'Customer Outcomes' for the agentic era. This restructuring reflects a broader trend of tech companies aggressively reorganizing for AI-driven efficiency, and may serve as a blueprint for how remote-first firms adapt to the agentic era. The changes will impact hundreds of employees and reshape GitLab's operational model. GitLab will cut 7% of its workforce, reduce countries with small teams by 30%, remove up to three layers of management in some functions, and reorganize R&D into about 60 smaller, autonomous teams. The CREDIT values framework is replaced by 'Speed with Quality', 'Ownership Mindset', and 'Customer Outcomes', though diversity is retained under 'Interpersonal excellence'.

rss · Simon Willison · May 11, 23:58

**Background**: GitLab is known for its all-remote workforce and transparent handbook, operating in nearly 60 countries. The 'agentic era' refers to the rising use of AI agents that can autonomously perform tasks, increasing software demand. This restructuring aims to position GitLab for that new era by automating internal processes and empowering smaller teams.

<details><summary>References</summary>
<ul>
<li><a href="https://about.gitlab.com/blog/gitlab-act-2/">GitLab Act 2</a></li>
<li><a href="https://www.thehrdigest.com/agentic-ai-ambitions-strike-again-as-gitlab-announces-layoffs-for-2026/">Agentic AI Ambitions Strike Again as GitLab Announces Layoffs ...</a></li>

</ul>
</details>

**Tags**: `#GitLab`, `#business strategy`, `#remote work`, `#workforce reduction`

---

<a id="item-24"></a>
## [AI Coding Agents Must Cut Maintenance Costs, Warns James Shore](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 7.0/10

James Shore argues that AI coding agents must reduce maintenance costs by the same factor they increase coding productivity, otherwise long-term costs will spiral. He uses a simple mathematical model to show that doubling productivity without halving maintenance costs quadruples overall maintenance expenses. This highlights a critical, often overlooked trade-off in adopting AI for software development: productivity gains can be negated by accumulating technical debt. It matters for engineering leaders and developers who need to evaluate AI tools not just on speed but on long-term cost impact. Shore's argument relies on the formula: total maintenance cost scales with (productivity multiplier) × (maintenance cost multiplier). If productivity doubles (multiplier 2) but maintenance stays same (multiplier 1), total cost doubles. If maintenance also halves (0.5), total cost stays the same.

rss · Simon Willison · May 11, 19:48

**Background**: Software maintenance costs are a major part of total cost of ownership, often exceeding initial development. AI coding agents boost productivity by generating code faster, but if that code is harder to maintain, technical debt increases. Shore's insight is that AI tools must not only generate code but also help manage and reduce maintenance burden to be sustainable.

**Tags**: `#AI coding`, `#software maintenance`, `#productivity`, `#technical debt`

---

<a id="item-25"></a>
## [Parameter Golf: Lessons from AI-Assisted Model Design](https://openai.com/index/what-parameter-golf-taught-us) ⭐️ 7.0/10

OpenAI published insights from the Parameter Golf competition, where over 1,000 participants submitted more than 2,000 models trained under strict constraints: a 16MB size limit and a 10-minute training budget on 8×H100 GPUs. This competition demonstrates how AI-assisted research and coding agents can accelerate model design under extreme resource constraints, potentially influencing future efficient model development and quantization techniques. Models were evaluated by compression on the FineWeb validation set using bits per byte, and the challenge also served as a recruiting pipeline for OpenAI.

rss · OpenAI Blog · May 12, 00:00

**Background**: Quantization is a technique that reduces the precision of model weights and activations to lower bit-widths (e.g., from 32-bit float to 8-bit integer), making models smaller and faster with minimal accuracy loss. Parameter Golf imposed a 16MB total size limit, forcing participants to apply aggressive quantization and other compression methods. The competition also explored AI-assisted research, where coding agents and human-AI collaboration helped design novel architectures under tight budgets.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/parameter-golf/">OpenAI Model Craft: Parameter Golf</a></li>
<li><a href="https://github.com/openai/parameter-golf/">GitHub - openai/parameter-golf: Train the smallest LM you can ...</a></li>
<li><a href="https://aihola.com/article/openai-parameter-golf-competition">OpenAI Parameter Golf: 16MB Model Competition and Hiring Pip</a></li>

</ul>
</details>

**Tags**: `#AI research`, `#machine learning`, `#coding agents`, `#quantization`

---

<a id="item-26"></a>
## [AWS Building Blocks for Foundation Model Training and Inference](https://huggingface.co/blog/amazon/foundation-model-building-blocks) ⭐️ 7.0/10

Hugging Face published a blog post detailing the key AWS components, including Trainium and Inferentia accelerators and the Neuron SDK, for building and scaling foundation model training and inference workloads. This guidance helps practitioners efficiently deploy large models on AWS custom hardware, potentially reducing costs and improving performance for generative AI workloads. The post covers the entire workflow from training using AWS Trainium to inference using AWS Inferentia, leveraging the AWS Neuron SDK for optimization.

rss · Hugging Face Blog · May 11, 23:18

**Background**: Foundation models are large AI models like GPT-4 and Llama that require significant compute resources. AWS has developed custom AI accelerators: Trainium for training and Inferentia for inference, along with the Neuron SDK to optimize model performance on these chips.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/neuron/">SDK for Gen AI and Deep Learning - AWS Neuron - AWS</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#foundation models`, `#training`, `#inference`, `#machine learning`

---

<a id="item-27"></a>
## [Varda and United Therapeutics to make drugs in orbit commercially](https://www.technologyreview.com/2026/05/13/1137153/varda-united-therapeutics-drug-manufacturing-in-space/) ⭐️ 7.0/10

Varda Space Industries has signed its first major agreement with pharmaceutical company United Therapeutics to develop and manufacture drugs in microgravity. This marks a key step toward commercial in-orbit drug manufacturing. This partnership demonstrates that in-space drug manufacturing is moving from experimental to commercial, potentially enabling the production of novel drugs that are difficult to make on Earth. It could open a new industry for space-based pharmaceutical production and attract more investment. Varda's approach involves crystallizing small molecules in microgravity using its spacecraft, then returning them to Earth via an atmospheric reentry vehicle. The company was founded in 2021 and is backed by Khosla Ventures and Founders Fund.

rss · MIT Tech Review · May 13, 10:00

**Background**: Pharmaceutical research in microgravity has been conducted for decades on the Space Shuttle and International Space Station, but often with limited access and high costs. Varda aims to provide a practical, repeatable commercial service for drug manufacturers to exploit the unique crystallization conditions in space.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Varda_Space_Industries">Varda Space Industries</a></li>
<li><a href="https://arstechnica.com/space/2026/05/varda-signs-deal-with-major-us-pharma-firm-to-develop-drugs-in-space/">Could this be the moment that drug manufacturing takes off in ...</a></li>
<li><a href="https://spacenews.com/varda-to-collaborate-with-united-therapeutics-on-microgravity-drug-research/">Varda to collaborate with United Therapeutics on microgravity ...</a></li>

</ul>
</details>

**Tags**: `#space manufacturing`, `#pharmaceuticals`, `#biotechnology`, `#commercial space`

---

<a id="item-28"></a>
## [TechPays acquired by Levels.fyi to boost European pay transparency](https://blog.pragmaticengineer.com/techpays-has-been-acquired-levels-fyi/) ⭐️ 7.0/10

Levels.fyi has acquired TechPays, the leading European tech salary transparency site, as announced on July 31, 2025. The acquisition will combine salary data from both platforms to enhance pay transparency. This acquisition significantly strengthens pay transparency for European tech workers, who have historically had less access to salary data than their US counterparts. Combining datasets from Levels.fyi and TechPays will provide a more comprehensive view of compensation across the region. TechPays was co-founded by Gergely Orosz (author of The Pragmatic Engineer blog) and Zsombor Szász. The site focused on European tech salaries, particularly in hubs like London and Berlin, and will now be integrated into Levels.fyi.

rss · Pragmatic Engineer · May 12, 16:06

**Background**: Levels.fyi is a crowdsourced platform that provides salary and compensation data for tech companies, primarily in the United States. TechPays was created to address the lack of pay transparency in Europe, where salary information is often opaque. The acquisition is expected to accelerate Levels.fyi's expansion into European markets.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.pragmaticengineer.com/techpays-has-been-acquired-levels-fyi/">TechPays has been acquired by Levels.fyi - The Pragmatic Engineer</a></li>
<li><a href="https://www.levels.fyi/blog/levelsfyi-acquires-techpays.html">Levels.fyi acquires TechPays</a></li>

</ul>
</details>

**Tags**: `#acquisition`, `#tech salaries`, `#pay transparency`, `#Levels.fyi`, `#TechPays`

---

<a id="item-29"></a>
## [Thinking Machines Launches TML-Interaction-Small, New Realtime Voice AI](https://www.latent.space/p/ainews-thinking-machines-native-interaction) ⭐️ 7.0/10

Thinking Machines released TML-Interaction-Small, a 276-billion parameter Mixture-of-Experts model with 12 billion active parameters, achieving state-of-the-art realtime voice interaction and eliminating the need for traditional Voice Activity Detection (VAD). This model represents a shift from turn-based voice AI to native full-duplex interaction, making voice conversations more natural and seamless. It also challenges existing approaches by integrating interactivity directly into the model architecture, potentially setting a new standard for realtime voice AI. The model uses a Mixture-of-Experts architecture with 276B total parameters but only 12B active per inference, balancing performance and efficiency. It is paired with a slower asynchronous background model for complex reasoning, web search, and tool calls, allowing the foreground model to maintain fluent conversation.

rss · Latent Space · May 12, 04:33

**Background**: Traditional voice AI systems rely on Voice Activity Detection (VAD) to determine when a user starts or stops speaking, which introduces latency and unnatural pauses. Mixture-of-Experts (MoE) models activate only a subset of parameters for each input, enabling larger models to run efficiently. Thinking Machines' new interaction model makes interactivity native, meaning the model itself handles turn-taking without separate VAD components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.creativeainews.com/articles/thinking-machines-tml-interaction-full-duplex-voice-ai/">Thinking Machines TML - Interaction : Full-Duplex Voice AI</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/2374/thinking-machines-interaction-models-mira-murati">Thinking Machines Interaction Models : Mira Murati's full-duplex...</a></li>
<li><a href="https://picovoice.ai/blog/complete-guide-voice-activity-detection-vad/">Voice Activity Detection Guide 2026: Complete Technical Overview</a></li>

</ul>
</details>

**Tags**: `#AI`, `#voice interaction`, `#realtime systems`, `#machine learning models`

---

<a id="item-30"></a>
## [AI Agent Methodology DRIL Automates Economic Dataset Construction](https://feeds.feedblitz.com/~/955775837/0/marginalrevolution~Using-agents-to-build-economic-datasets.html) ⭐️ 7.0/10

Researchers propose Deep Research on a Loop (DRIL), a methodology using AI agents to automate the construction of economic datasets from publicly available sources, outlined in NBER working paper W35188. DRIL significantly reduces the cost and time of constructing primary-source datasets in empirical economics, potentially accelerating research and enabling larger-scale studies. DRIL applies a fixed research instrument across a mapped unit space (e.g., countries by years) and uses a two-stage architecture that separates design from implementation.

rss · Marginal Revolution · May 12, 04:26

**Background**: Constructing datasets from primary sources is one of the most costly tasks in empirical economics, often requiring extensive manual effort. AI agents, which can autonomously perform tasks like web scraping and data extraction, offer a potential solution. DRIL systematizes this process by defining a repeatable methodology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nber.org/papers/w35188">Deep Research on a Loop: Using AI Agents to Construct ...</a></li>
<li><a href="https://letsdatascience.com/news/researchers-propose-dril-method-to-automate-dataset-construc-73e5ebc1">Researchers Propose DRIL Method to Automate Dataset ...</a></li>

</ul>
</details>

**Discussion**: Community comments raise concerns about data reliability and the quality of AI-generated datasets, with some questioning whether the output can be trusted without human validation.

**Tags**: `#AI agents`, `#economic datasets`, `#methodology`, `#Deep Research`, `#empirical economics`

---