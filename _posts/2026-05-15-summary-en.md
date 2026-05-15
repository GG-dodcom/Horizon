---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 121 items, 30 important content pieces were selected

---

1. [OxCaml Stack Annotations Cut GC Latency in Space Software](#item-1) ⭐️ 9.7/10
2. [Ben Thompson on Compute Shortage and Aggregation Theory](#item-2) ⭐️ 9.6/10
3. [Pixel 10 0-click exploit chain via AI message decoding](#item-3) ⭐️ 9.0/10
4. [Unlocking Async in Continuous Batching for LLM Inference](#item-4) ⭐️ 9.0/10
5. [Did Capacity Shortages Make Anthropic Seem Hostile to Devs?](#item-5) ⭐️ 9.0/10
6. [Chinese short dramas embrace AI as content creation engines](#item-6) ⭐️ 8.9/10
7. [AI and data sovereignty: Control over proprietary data](#item-7) ⭐️ 8.8/10
8. [Sea Limited CPO Discusses Codex for Agentic Development](#item-8) ⭐️ 8.5/10
9. [IBM Granite Embedding Multilingual R2: Open, 32K Context, Top Retrieval](#item-9) ⭐️ 8.5/10
10. [Abridge: AI Turns Doctor Visits into Healthcare OS](#item-10) ⭐️ 8.5/10
11. [Claude Code v2.1.141 Released with New Hooks and Fixes](#item-11) ⭐️ 8.3/10
12. [Meta gets $3.3B tax break for $10B Louisiana data center](#item-12) ⭐️ 8.2/10
13. [Image-blaster: Generate 3D Worlds from a Single Image](#item-13) ⭐️ 8.2/10
14. [Sigmoid Curves Won't Save AI: Limits Ahead](#item-14) ⭐️ 8.1/10
15. [Claude Code v2.1.143 Adds Plugin Dependency Enforcement and Context Cost Estimates](#item-15) ⭐️ 8.0/10
16. [Radicle: Decentralized peer-to-peer code forge built on Git](#item-16) ⭐️ 8.0/10
17. [Stratechery Weekly Roundup: Computing, Musk, US-China](#item-17) ⭐️ 8.0/10
18. [Companies Under 'AI Psychosis' Warns Mitchell Hashimoto](#item-18) ⭐️ 7.7/10
19. [Jason Scott's Blog Celebrated for Digital Preservation](#item-19) ⭐️ 7.6/10
20. [OpenAI Improves ChatGPT Context Awareness in Sensitive Talks](#item-20) ⭐️ 7.6/10
21. [New Book Explores Steve Jobs' Underrated NeXT Era](#item-21) ⭐️ 7.5/10
22. [Codex and Claude: AI Coding Agents and Programmatic Metering](#item-22) ⭐️ 7.5/10
23. [Zulip Forms Independent Nonprofit Foundation](#item-23) ⭐️ 7.2/10
24. [Waymo recalls 3,800 robotaxis over standing water glitch](#item-24) ⭐️ 7.2/10
25. [Hands-on with Linux Terminal on Android (2026 Edition)](#item-25) ⭐️ 7.2/10
26. [6-8 Hours Sleep Linked to Lower Risk of Early Death and Disease](#item-26) ⭐️ 7.2/10
27. [Coding Agents Lower Technology Lock-in](#item-27) ⭐️ 7.1/10
28. [Project Gutenberg Continuously Improves Its Digital Library](#item-28) ⭐️ 7.0/10
29. [DOJ Orders Apple and Google to Unmask 100K+ App Users](#item-29) ⭐️ 7.0/10
30. [The emotional toll of nonconsensual deepfake porn](#item-30) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OxCaml Stack Annotations Cut GC Latency in Space Software](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 9.7/10

A team used OxCaml, an OCaml variant, with stack annotations to eliminate garbage collection pressure in satellite communication software, reducing p99.9 latency from 29 ns to 9 ns per packet on the hot path. This demonstrates that garbage-collected languages can be tuned for hard real-time systems like satellites, merging safety and performance. It could influence language design and adoption in embedded and aerospace domains. Over 25 million packets, the annotation approach reduced minor GC collections from 394 to zero, with comparable throughput. The technique involves typing annotations that push data to the stack, reducing heap allocations.

hackernews · yminsky · May 15, 10:55 · [Discussion](https://news.ycombinator.com/item?id=48147058)

**Background**: Garbage collection (GC) automatically reclaims memory but can cause unpredictable pauses, problematic for real-time systems. Stack annotations in languages like OCaml allow developers to specify that certain values live on the stack, avoiding heap allocation and GC scanning. OxCaml is an OCaml derivative focused on performance and determinism.

<details><summary>References</summary>
<ul>
<li><a href="https://ocaml.org/manual/5.2/api/Stack.html">OCaml library : Stack</a></li>
<li><a href="https://www.linkedin.com/advice/0/how-can-you-minimize-memory-usage-garbage-collected-n5fic">How to Minimize Memory Usage in Garbage - Collected Languages</a></li>

</ul>
</details>

**Discussion**: Commenters noted previous OCaml satellite use (GHGSat-D in 2016) and discussed the difficulty of bending GC languages to behave like non-GC ones. Some questioned the security trade-offs of reinventing encryption protocols per CCSDS standards vs using TLS.

**Tags**: `#OCaml`, `#space software`, `#garbage collection`, `#low-latency systems`, `#programming languages`

---

<a id="item-2"></a>
## [Ben Thompson on Compute Shortage and Aggregation Theory](https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/) ⭐️ 9.6/10

Ben Thompson, in an interview at the MoffettNathanson conference, discussed how the compute shortage affects Aggregation Theory and the future of consumer AI. This analysis is crucial for understanding how resource constraints like compute shortages may reshape the strategic dynamics of large tech platforms and startups. The interview covers implications for Aggregation Theory—a framework explaining the dominance of internet giants—in an era of limited compute resources. Thompson likely addresses how consumer AI products must adapt to hardware bottlenecks.

rss · Stratechery · May 14, 10:00

**Background**: Aggregation Theory, coined by Ben Thompson, describes how digital platforms like Google and Facebook aggregate supply and demand to dominate markets. The current compute shortage, driven by high demand for AI chips, creates a bottleneck for AI development, potentially altering the dynamics of aggregation.

<details><summary>References</summary>
<ul>
<li><a href="https://stratechery.com/aggregation-theory/">Aggregation Theory – Stratechery by Ben Thompson</a></li>
<li><a href="https://medium.com/@hagaetc/an-introduction-to-aggregation-theory-7cea63cc0e20">An introduction to Aggregation Theory | by Fredrik Haga | Medium</a></li>
<li><a href="https://www.youtube.com/watch?v=ZesA-Iqju4U">The wild power of aggregation theory - YouTube</a></li>

</ul>
</details>

**Tags**: `#AI`, `#compute shortage`, `#Aggregation Theory`, `#consumer AI`, `#tech strategy`

---

<a id="item-3"></a>
## [Pixel 10 0-click exploit chain via AI message decoding](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a 0-click exploit chain targeting the Pixel 10, which leverages vulnerabilities in AI-powered message decoding to achieve remote code execution without user interaction. This exploit highlights how AI features in modern smartphones can inadvertently expand the attack surface, making devices vulnerable to 0-click attacks, and underscores the importance of timely vendor patching. The exploit chain includes a bug in the Android kernel driver (VPU) that was patched within 90 days—notably fast for Android. The attack works by decoding message media before the user opens it, enabling 0-click code execution.

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: A 0-click exploit requires no user interaction, such as clicking a link or opening a file. AI-powered features on phones, like automatic message analysis, can decode media before the user views it, increasing the attack surface if the decoding process has vulnerabilities. Project Zero is Google's security team that finds and discloses zero-day vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exploit_(computer_security)">Exploit (computer security) - Wikipedia</a></li>
<li><a href="https://www.kaspersky.com/resource-center/definitions/what-is-zero-click-malware">Zero-Click Exploits</a></li>
<li><a href="https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities">AI-powered scanner vulnerabilities | Web Security Academy</a></li>

</ul>
</details>

**Discussion**: Commenter krupan questioned why lessons from past 0-click attacks haven't been learned, as AI features increase attack surface. greesil noted the fast patching by Google but expressed concern about other Android vendors. revolvingthrow wondered if the perceived increase in exploit publications is due to AI hype or actual rise in attacks.

**Tags**: `#Android`, `#0-click exploit`, `#AI security`, `#Project Zero`, `#Pixel 10`

---

<a id="item-4"></a>
## [Unlocking Async in Continuous Batching for LLM Inference](https://huggingface.co/blog/continuous_async) ⭐️ 9.0/10

A new HuggingFace blog post introduces techniques to add asynchronicity to continuous batching, enabling overlapping of computation and data transfer for more efficient LLM inference. This advance directly addresses a key bottleneck in LLM serving, potentially improving throughput and reducing latency for production inference systems like vLLM and TGI. Asynchronous continuous batching allows preemption and resumption of requests, better GPU utilization, and seamless integration with async Python frameworks like asyncio.

rss · Hugging Face Blog · May 14, 00:00

**Background**: Continuous batching dynamically schedules requests into batches for LLM inference, avoiding waiting for all requests to finish. Adding asynchronicity overlaps KV cache management and compute, further reducing idle time and improving efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/continuous_batching">Continuous batching from first principles</a></li>
<li><a href="https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html">Inside vLLM: Anatomy of a High-Throughput LLM Inference System | vLLM Blog</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#batching`, `#HuggingFace`, `#asynchronous`

---

<a id="item-5"></a>
## [Did Capacity Shortages Make Anthropic Seem Hostile to Devs?](https://blog.pragmaticengineer.com/the-pulse-did-capacity-shortages-turn-anthropic-hostile-to-devs/) ⭐️ 9.0/10

Anthropic has been upsetting developers with a perceived dumber Claude model and by removing Claude Code access from some paid accounts, which may be due to capacity shortages rather than hostility. This matters because it highlights how AI infrastructure constraints can negatively impact developer experience and trust, potentially driving users to competitors. The capacity issues may be concealed by Anthropic's recent compute deal with SpaceX, announced on May 6, 2026, which substantially increases near-term capacity.

rss · Pragmatic Engineer · May 14, 16:10

**Background**: Anthropic is the company behind the Claude series of large language models, including Claude Code, an AI-assisted software development tool. Capacity shortages refer to insufficient computational resources to serve all users reliably, which can lead to throttling or access removal. The SpaceX compute deal is a partnership to provide additional computing power for Anthropic's AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/higher-limits-spacex">Higher usage limits for Claude and a compute deal with SpaceX</a></li>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/05/06/anthropic-just-signed-a-compute-deal-with-elon-musks-spacex/">Anthropic Just Signed A Compute Deal With Elon Musk's SpaceX</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI capacity`, `#developer experience`, `#LLM`

---

<a id="item-6"></a>
## [Chinese short dramas embrace AI as content creation engines](https://www.technologyreview.com/2026/05/15/1137326/chinese-short-dramas-ai/) ⭐️ 8.9/10

An MIT Technology Review article explores how Chinese short drama producers are using generative AI, including text-to-video tools and LLMs, to rapidly create content, as illustrated by a supernatural scene generated via AI. This marks a shift in media production where AI enables low-cost, high-volume content creation, potentially disrupting traditional filmmaking and reshaping the global short-video ecosystem. The article highlights that Chinese short dramas, typically vertical micro-dramas of 1-3 minutes per episode, are now being produced with AI tools like Hailuo AI and Genra, which turn text prompts into video scenes, including complex effects like flame vines and levitation.

rss · MIT Tech Review · May 15, 09:00

**Background**: Chinese short dramas are a rapidly growing format on platforms like Douyin (TikTok), known for their high emotional impact and quick production cycles. AI content generation tools, such as text-to-video and LLM-based scriptwriting, allow creators to bypass traditional filming costs and iterate rapidly. Companies like Hailuo AI and Genra offer specialized platforms for generating such micro-dramas, while LLMs assist with plot and dialogue generation.

<details><summary>References</summary>
<ul>
<li><a href="https://genra.ai/blog/ai-short-drama-generation-guide">Create Viral Short Dramas with Genra AI Video Generator</a></li>
<li><a href="https://hailuoai.video/tools/ai-short-drama-generator">AI Short Drama Generator - Create Micro-Drama Videos with Hailuo AI</a></li>
<li><a href="https://www.secondtalent.com/resources/chinese-ai-video-generation-tools/">7 Best Chinese AI Video Generation Tools [2026] | Second Talent</a></li>

</ul>
</details>

**Tags**: `#AI content generation`, `#Chinese short dramas`, `#media`, `#LLM`

---

<a id="item-7"></a>
## [AI and data sovereignty: Control over proprietary data](https://www.technologyreview.com/2026/05/14/1137168/establishing-ai-and-data-sovereignty-in-the-age-of-autonomous-systems/) ⭐️ 8.8/10

This article by MIT Technology Review highlights the urgent need for enterprises to establish data sovereignty and regain control over their proprietary data when using third-party AI models, moving from a 'capability now, control later' approach to a more governed one. As autonomous systems proliferate, reliance on third-party AI models risks losing control over sensitive data, making data sovereignty a critical enterprise priority for compliance, security, and competitive advantage. The article cites EDB internal data showing that 70% of companies prioritize AI and data sovereignty, and suggests distributed infrastructure and federated AI as solutions to break dependence on centralized providers.

rss · MIT Tech Review · May 14, 13:00

**Background**: Data sovereignty means data stored and processed in the country where it was generated, ensuring compliance with local laws. Many enterprises have been feeding proprietary data into third-party AI models without clear governance, leading to potential regulatory and security risks. The article argues that establishing genuine control over models and data estates is now an urgent priority.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/14/1137168/establishing-ai-and-data-sovereignty-in-the-age-of-autonomous-systems/">Establishing AI and data sovereignty in the age of autonomous systems | MIT Technology Review</a></li>
<li><a href="https://blog.equinix.com/blog/2025/05/14/data-sovereignty-and-ai-why-you-need-distributed-infrastructure/">Data Sovereignty and AI: Why You Need Distributed Infrastructure - Interconnections - The Equinix Blog</a></li>
<li><a href="https://www.ibm.com/think/topics/data-sovereignty">What is data sovereignty? | IBM</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#data sovereignty`, `#enterprise AI`, `#autonomous systems`

---

<a id="item-8"></a>
## [Sea Limited CPO Discusses Codex for Agentic Development](https://openai.com/index/sea-david-chen) ⭐️ 8.5/10

Sea Limited's Chief Product Officer (CPO) explained how the company is deploying OpenAI's Codex across engineering teams to accelerate AI-native software development in Asia. This highlights a major Asian tech firm's practical adoption of agentic AI systems, potentially setting a precedent for how large-scale software engineering can be transformed by autonomous coding agents. Sea Limited uses Codex to enable AI agents that autonomously plan, write, test, and modify code with minimal human intervention, aligning with the broader trend of agentic software development.

rss · OpenAI Blog · May 14, 20:30

**Background**: Agentic software development involves autonomous AI agents performing coding tasks traditionally done by humans. AI-native development integrates AI throughout the software development lifecycle. Sea Limited, the parent company of Shopee and Garena, is a leading internet company in Southeast Asia and Taiwan, making its adoption noteworthy.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases</a></li>
<li><a href="https://developers.openai.com/codex/guides/build-ai-native-engineering-team">Building an AI-Native Engineering Team – Codex | OpenAI ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Codex`, `#agentic systems`, `#software engineering`, `#LLM`

---

<a id="item-9"></a>
## [IBM Granite Embedding Multilingual R2: Open, 32K Context, Top Retrieval](https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2) ⭐️ 8.5/10

IBM released Granite Embedding Multilingual R2, an open-source multilingual embedding model under Apache 2.0 license, featuring a 32K context length and achieving state-of-the-art retrieval quality among models under 100M parameters. This model sets a new benchmark for efficient, open-source multilingual embeddings, enabling high-quality retrieval in retrieval-augmented generation (RAG) systems across many languages without requiring large parameter counts. The model has a 149M parameter dense biencoder architecture, optimized for multilingual retrieval, and is part of IBM's Granite Embedding collection that includes a reranker model.

rss · Hugging Face Blog · May 14, 18:55

**Background**: Embedding models convert text into dense vector representations that capture semantic meaning, enabling efficient similarity search. They are critical for RAG systems, which retrieve relevant information from large corpora to augment LLM responses. The Granite Embedding models are built on permissively licensed public datasets and set high standards on benchmarks like BEIR.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/granite/docs/models/embedding">Granite Embedding - IBM Granite</a></li>
<li><a href="https://github.com/ibm-granite/granite-embedding-models/">GitHub - ibm-granite/granite-embedding-models · GitHub</a></li>

</ul>
</details>

**Tags**: `#multilingual embeddings`, `#retrieval`, `#open source`, `#LLM`, `#IBM Granite`

---

<a id="item-10"></a>
## [Abridge: AI Turns Doctor Visits into Healthcare OS](https://www.latent.space/p/abridge) ⭐️ 8.5/10

Abridge has processed over 100 million patient-clinician conversations using its AI platform, saving clinicians 10-20 hours per week and reducing prior authorization from hours to minutes. This demonstrates how AI-native systems can dramatically reduce administrative burden in healthcare, addressing clinician burnout and improving access to care by streamlining critical workflows like prior authorization. Abridge generates context-aware, clinically useful, and billable AI notes from patient-clinician conversations, with real-world deployments showing the ability to handle prior authorization requests in minutes instead of hours.

rss · Latent Space · May 14, 22:05

**Background**: Prior authorization (PA) is a process health insurers use to approve treatments or medications before they are provided, which can cause delays and administrative burden. Abridge is a generative AI platform that listens to medical conversations and automatically produces structured clinical documentation to reduce clinician workload.

<details><summary>References</summary>
<ul>
<li><a href="https://www.verywellhealth.com/prior-authorization-1738770">What Is Prior Authorization and How Does It Work?</a></li>
<li><a href="https://www.abridge.com/">Generative AI for Clinical Conversations | Abridge</a></li>

</ul>
</details>

**Tags**: `#AI`, `#healthcare`, `#LLM`, `#prior authorization`, `#clinical AI`

---

<a id="item-11"></a>
## [Claude Code v2.1.141 Released with New Hooks and Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) ⭐️ 8.3/10

Anthropic released Claude Code v2.1.141, adding terminal sequence support for hooks, HTTPS plugin cloning, workspace ID environment variable, session directory scoping, improved feedback, rewind summarization, and auto-mode permission clarification, along with numerous bug fixes. This update enhances developer productivity by enabling hooks to emit terminal notifications without a controlling terminal, simplifies plugin setup in SSH-restricted environments, and introduces context compression via rewind summarization to manage large sessions, making Claude Code more versatile and robust for AI-assisted coding workflows. The new `terminalSequence` field in hook JSON output allows hooks to trigger desktop notifications, window title changes, and bells. The `ANTHROPIC_WORKSPACE_ID` environment variable enables workload identity federation for scoped token minting. The rewind 'Summarize up to here' option compresses earlier context while preserving recent turns, and the auto-mode permission dialog now explains when a `permissions.ask` rule caused the prompt.

github · ashwin-ant · May 13, 23:19

**Background**: Claude Code is Anthropic's AI coding assistant that runs in the terminal, helping developers with code generation, debugging, and refactoring. Hooks are custom scripts that respond to events like before or after tool execution. The rewind feature allows users to roll back to a previous session state, and the new summarization option compresses context to optimize token usage. Workload identity federation is a modern authentication method that uses federated trust instead of shared secrets, enabling secure cloud access for workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/58858">[DOCS] Hooks reference missing `terminalSequence` JSON output ...</a></li>
<li><a href="https://nicolasuter.medium.com/why-you-should-use-entra-workload-identity-federation-dfe8b6b626a1">Why you should use Entra Workload Identity Federation | Medium</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#release-notes`, `#ai-tooling`, `#developer-tools`, `#anthropic`

---

<a id="item-12"></a>
## [Meta gets $3.3B tax break for $10B Louisiana data center](https://fortune.com/2026/05/14/meta-data-center-tax-break-hyperion-louisiana/) ⭐️ 8.2/10

Meta will receive $3.3 billion in tax breaks from Louisiana for its planned $10 billion data center, Hyperion, which is intended to train and develop AI models. This massive incentive package raises concerns about transparency in local government negotiations and the real economic benefits for residents, especially as data centers create few permanent jobs. It also sets a precedent for how states compete for AI infrastructure investment. The $3.3 billion figure comes from exempting Meta from state and local sales and use taxes on equipment, including GPUs, for 20 years. Sherwood News estimated that with a combined tax rate of 9.56% and roughly $35 billion spent on GPUs, the break totals $3.3 billion.

hackernews · logickkk1 · May 15, 19:32 · [Discussion](https://news.ycombinator.com/item?id=48152825)

**Background**: Data centers like Hyperion are critical infrastructure for AI and cloud computing, but they consume enormous amounts of electricity and water. Local governments often offer tax incentives to attract such investments, hoping for job creation and economic growth, though the benefits are sometimes disputed. Critics argue that these deals are often negotiated in secret without adequate public input.

**Discussion**: Commenters on the news expressed strong skepticism, with one noting the deal was struck through nondisclosure agreements and closed-door politics. Others questioned the local benefits, comparing data centers unfavorably to prisons in job creation. Several pointed out similar deals with Amazon and raised environmental and tax equity concerns.

**Tags**: `#AI infrastructure`, `#data centers`, `#tax incentives`, `#Meta`, `#tech policy`

---

<a id="item-13"></a>
## [Image-blaster: Generate 3D Worlds from a Single Image](https://github.com/neilsonnn/image-blaster) ⭐️ 8.2/10

A new open-source GitHub repository called Image-blaster uses a single input image to generate 3D environments, meshes, and sound effects via pipelines including World Labs' AI. This tool dramatically lowers the barrier for 3D content creation, enabling anyone with a single photo to produce interactive 3D scenes, which could transform game development, VR/AR, and digital art. Image-blaster relies on World Labs' Marble platform for spatial generation, but community testing reveals hallucinated regions that may make outputs unusable. The repository also integrates other AI pipelines for mesh and SFX generation.

hackernews · MattRogish · May 15, 15:42 · [Discussion](https://news.ycombinator.com/item?id=48150069)

**Background**: Traditional 3D scene generation from images required multiple photos or depth data. Recent AI models like World Labs' Marble and TRELLIS can infer 3D structure from a single image using generative techniques. Image-blaster packages such models into an accessible pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://www.worldlabs.ai/">World Labs</a></li>
<li><a href="https://techcrunch.com/2024/12/02/world-labs-ai-can-generate-interactive-3d-scenes-from-a-single-photo/">World Labs' AI can generate interactive 3D scenes from a ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the technology, comparing it to Microsoft's old PhotoSynth and noting improved quality. However, some reported that World Labs outputs often hallucinate nonsensical parts, and others suggested alternatives like Meshy.ai or GPT Image 2 for better results.

**Tags**: `#AI`, `#3D modeling`, `#generative AI`, `#computer vision`, `#open source`

---

<a id="item-14"></a>
## [Sigmoid Curves Won't Save AI: Limits Ahead](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 8.1/10

The article argues that AI scaling, following an S-curve like previous technologies, may hit fundamental limits, and proposes Lindy's Law as a more robust predictor for technological progress. This challenges the dominant belief that AI performance will continue to improve exponentially with scale, potentially affecting investment decisions and research directions in AI. The author uses the history of aircraft speed to illustrate how each technology (propellers, turbojets, ramjets) followed an S-curve before hitting limits, suggesting AI may follow a similar pattern.

hackernews · Tomte · May 15, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48147021)

**Background**: S-curves describe technology adoption where slow initial growth accelerates then plateaus. Lindy's Law states that the future life expectancy of non-perishable things (like ideas) is proportional to their current age. AI scaling laws have shown performance improvements with increased model size, data, and compute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lindy_effect">Lindy effect - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technology_adoption_life_cycle">Technology adoption life cycle - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments highlight that the author has predicted AGI within 1-2 years, creating a potential bias. Some argue Lindy's Law cannot be applied to trends as static objects, while others praise Lindy's Law as a useful heuristic.

**Tags**: `#AI`, `#technology trends`, `#scaling laws`, `#Lindy's Law`, `#forecasting`

---

<a id="item-15"></a>
## [Claude Code v2.1.143 Adds Plugin Dependency Enforcement and Context Cost Estimates](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) ⭐️ 8.0/10

Anthropic released Claude Code v2.1.143, introducing plugin dependency enforcement, projected context cost estimates in the plugin marketplace, a new worktree isolation setting, and numerous fixes for credentials, paste, and PowerShell improvements. These improvements enhance developer productivity by preventing broken plugin chains, providing cost transparency for token usage, and offering more flexible worktree isolation—critical for large-scale AI-assisted development workflows. Notable changes include the new worktree.bgIsolation 'none' setting for repos where worktrees are impractical, automatic dependency resolution for plugins, and PowerShell tool enabled by default on Windows for Bedrock/Vertex/Foundry users with opt-out environment variables.

github · ashwin-ant · May 15, 22:28

**Background**: Claude Code is a CLI-based AI coding assistant from Anthropic that operates within a developer's terminal. It uses git worktrees to isolate parallel AI sessions, preventing file conflicts. Plugins extend its functionality, and dependency enforcement ensures plugin compatibility. Token cost estimates help developers manage API usage expenses.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@richardhightower/git-worktree-isolation-in-claude-code-parallel-development-without-the-chaos-262e12b85cc5">Git Worktree Isolation in Claude Code : Parallel... | Medium</a></li>
<li><a href="https://code.claude.com/docs/en/plugin-dependencies">Constrain plugin dependency versions - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI tooling`, `#dev tools`, `#release notes`

---

<a id="item-16"></a>
## [Radicle: Decentralized peer-to-peer code forge built on Git](https://radicle.dev/) ⭐️ 8.0/10

Radicle is a sovereign, peer-to-peer code forge built on Git that enables decentralized code collaboration without relying on a central server. It supports private repositories and local-first data ownership. This approach challenges centralized platforms like GitHub by giving developers full control over their data and workflow, enhancing resilience and avoiding vendor lock-in. It is significant for open source infrastructure and decentralized development. Radicle uses a peer-to-peer networking layer called Radicle Link to extend Git, and repositories are replicated across peers. Private repos are supported by not publishing updates to the network, though history remains accessible.

hackernews · KolmogorovComp · May 15, 12:07 · [Discussion](https://news.ycombinator.com/item?id=48147603)

**Background**: Traditional code forges like GitHub centralize code hosting and collaboration on servers controlled by a single entity. Radicle's local-first approach stores data primarily on users' devices and syncs changes peer-to-peer, aligning with the principles of decentralized and sovereign software development.

<details><summary>References</summary>
<ul>
<li><a href="https://radicle.dev/">The Radicle forge is an open source, peer-to-peer code collaboration...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Local-first_software">Local-first software</a></li>

</ul>
</details>

**Discussion**: Community members praised Radicle's local-first design and private repo capabilities, but expressed concerns about its license (not AGPL) potentially allowing SaaS companies to leverage the code. There were also questions about support for the jj version control system.

**Tags**: `#decentralized`, `#git`, `#code hosting`, `#open source`, `#developer tools`

---

<a id="item-17"></a>
## [Stratechery Weekly Roundup: Computing, Musk, US-China](https://stratechery.com/2026/shifting-alliances-in-a-changing-world/) ⭐️ 8.0/10

A roundup of the best Stratechery articles from the week of May 11, 2026, covering a new kind of computing, Elon Musk's activities, and US-China relations from a 360-degree perspective. This collection provides deep strategic analysis on key tech and geopolitical trends, helping business leaders and technologists understand shifting alliances and emerging computing paradigms. The articles include insights on a new kind of computing beyond traditional architectures, Elon Musk's influence on multiple industries, and the multifaceted nature of US-China relations. Each piece reflects Stratechery's signature depth and strategic framing.

rss · Stratechery · May 15, 17:00

**Background**: Stratechery is a subscription-based analysis platform by Ben Thompson that focuses on technology, business, and strategy. Its articles are known for rigorous reasoning and long-term perspectives. The topics covered here are central to current tech and geopolitical discourse, with computing evolving beyond Moore's Law, Elon Musk pushing boundaries in electric vehicles, space, and AI, and US-China relations impacting global supply chains.

**Tags**: `#technology`, `#geopolitics`, `#computing`, `#Elon Musk`, `#strategy`

---

<a id="item-18"></a>
## [Companies Under 'AI Psychosis' Warns Mitchell Hashimoto](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 7.7/10

Mitchell Hashimoto tweeted that entire companies are under 'AI psychosis,' meaning they irrationally over-rely on AI and outsource decision-making to it. The Hacker News community expanded on this, discussing the risks of purely AI-written systems and the potential rise of 'AI rescue consulting.' This highlights a dangerous trend where companies may deploy unstable systems that become incomprehensible to humans, leading to escalating defects and costs. It also points to a potential new consulting niche—rescuing companies from their own AI overreliance. One HN commenter predicted that purely AI-written systems will scale to a complexity no human can understand, and eventually AI changes will cause more defects than they close. Another observed that proponents argue shipping bugs is acceptable because AI agents fix them quickly, creating an unsustainable cycle.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: AI overreliance occurs when users accept incorrect or incomplete AI outputs because system design makes errors hard to spot. Agentic AI systems are autonomous, goal-oriented systems that reason, plan, and execute multi-step workflows with minimal human intervention. When companies blindly trust such systems for critical decisions, they risk creating brittle, unmanageable codebases and operational failures.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/overreliance-on-ai/overreliance-on-ai">Overreliance on AI : Risk Identification and Mitigation... | Microsoft Learn</a></li>
<li><a href="https://www.moveworks.com/us/en/resources/blog/the-rise-of-agentic-systems-how-they-work">Agentic Systems : The Rise of Agentic AI-powered Automation</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with the warning, with some proposing 'AI rescue consulting' as a lucrative field. Others emphasized that the core problem is outsourcing thinking, not using AI as a tool. A few noted that slow-moving companies may gain a competitive advantage by avoiding this overreliance.

**Tags**: `#AI`, `#AI overreliance`, `#agentic systems`, `#software engineering`, `#HN discussion`

---

<a id="item-19"></a>
## [Jason Scott's Blog Celebrated for Digital Preservation](https://ascii.textfiles.com/) ⭐️ 7.6/10

Jason Scott's blog ASCII by Textfiles.com, a hub for digital preservation and software history, continues to gain attention and appreciation from the tech community, as evidenced by recent Hacker News discussion and community comments. This blog represents a vital resource for preserving digital heritage, inspiring others to contribute to archiving efforts, and fostering a community dedicated to keeping information free and accessible. Jason Scott has digitized over 1,300 tapes of magnetic media and a collection of 13,000 manuals, now publicly available on the Internet Archive, showcasing his prolific output and dedication.

hackernews · bookofjoe · May 15, 14:02 · [Discussion](https://news.ycombinator.com/item?id=48148726)

**Background**: Jason Scott is a digital archivist and activist known for founding the Internet Archive's software collection and the Archive Team. His blog 'ASCII by Jason Scott' documents his ongoing projects and thoughts on digital preservation, software history, and online culture.

**Discussion**: Commenters express deep gratitude for Jason Scott's work, highlighting his prolific digitization of rare media and manuals, and praise his character as a 'delightful person' and 'one of the good guys.' Some also provide updated links to his blog and note his live streaming on Twitch.

**Tags**: `#digital preservation`, `#archiving`, `#software history`, `#Jason Scott`, `#internet archive`

---

<a id="item-20"></a>
## [OpenAI Improves ChatGPT Context Awareness in Sensitive Talks](https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations) ⭐️ 7.6/10

OpenAI has announced new safety updates for ChatGPT that improve its ability to recognize context in sensitive conversations, helping to detect risk over time and respond more safely. This update addresses a critical challenge in AI safety: enabling large language models to understand nuanced context in sensitive interactions, which is essential for reducing harmful outputs and building trust in AI assistants. The updates focus on improving the model's ability to track conversation history and subtle cues, allowing it to better judge when a topic becomes sensitive and adjust its responses accordingly.

rss · OpenAI Blog · May 14, 00:00

**Background**: ChatGPT is a large language model developed by OpenAI that generates human-like text. Context awareness refers to the model's ability to understand and remember the flow of a conversation, which is particularly challenging in sensitive topics involving health, finance, or personal safety.

**Tags**: `#ChatGPT`, `#AI safety`, `#LLM`, `#context awareness`, `#sensitive conversations`

---

<a id="item-21"></a>
## [New Book Explores Steve Jobs' Underrated NeXT Era](https://spectrum.ieee.org/steve-jobs-next-computer) ⭐️ 7.5/10

A new book about Steve Jobs' tenure at NeXT has prompted thoughtful discussion on his underrated contributions, the role of NeXT in modern Apple, and the origins of object-oriented programming and app stores. This book sheds light on a pivotal but often overlooked period in Jobs' career, showing how NeXT's technologies—like object-oriented programming and the first app store—shaped modern Apple and software engineering. The book discusses how NeXT's use of object-oriented programming in 1988 led to the first app store, and how modern Apple is largely built on NeXT's foundation, including macOS and iOS.

hackernews · rbanffy · May 15, 10:34 · [Discussion](https://news.ycombinator.com/item?id=48146908)

**Background**: NeXT was a computer company founded by Steve Jobs after leaving Apple in 1985. It developed the NeXT Computer (nicknamed 'the cube') and the NeXTSTEP operating system, which pioneered object-oriented programming in mainstream computing. When Apple acquired NeXT in 1997, its technology became the backbone for macOS, iOS, and the App Store concept.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeXT">NeXT - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/NeXT_Computer">NeXT Computer - Wikipedia</a></li>
<li><a href="https://simson.net/ref/NeXT/aboutnext.htm">A Short History of NeXT</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that Jobs' NeXT era is underrated, with some noting that modern Apple is essentially NeXT. However, one commenter questioned the claim that NeXT had the first app store, and another expressed concern about Apple's software direction since Jobs.

**Tags**: `#Steve Jobs`, `#NeXT`, `#App Store history`, `#object-oriented programming`, `#tech history`

---

<a id="item-22"></a>
## [Codex and Claude: AI Coding Agents and Programmatic Metering](https://www.latent.space/p/ainews-codex-rises-claude-meters) ⭐️ 7.5/10

OpenAI's Codex is gaining traction as a leading AI coding agent, while Anthropic introduces programmatic usage metering for Claude, shifting API access to credit-based pricing starting June 15, 2025. This highlights the growing competition in AI-powered coding tools and a trend toward metered pricing, which directly affects developers and enterprises relying on these agents for automated software development. Anthropic's metering offers Pro users $20 in monthly credits, Max 5x users $100, and Max 20x users $200, while Codex is integrated into ChatGPT and supports parallel agentic workflows through worktrees and cloud environments.

rss · Latent Space · May 14, 03:53

**Background**: AI coding agents like OpenAI's Codex and Anthropic's Claude Code are tools that assist developers by generating and editing code based on natural language prompts. They operate via APIs or dedicated interfaces, and as usage scales, providers are moving to consumption-based pricing models. The programmatic metering for Claude means that automated API calls will be deducted from a credit pool, separate from interactive chat usage.

<details><summary>References</summary>
<ul>
<li><a href="https://max.nardit.com/articles/anthropic-meter-on-agent">Anthropic's June 15 metering change for Agent SDK and claude -p</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex ( AI agent ) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Coding Agents`, `#Codex`, `#Claude`, `#News`

---

<a id="item-23"></a>
## [Zulip Forms Independent Nonprofit Foundation](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 7.2/10

Zulip announced the formation of the Zulip Foundation, an independent nonprofit organization to ensure the long-term sustainability of the open-source team chat platform. Founder Tim Abbott is stepping back from full-time leadership to join Anthropic, along with three senior team members. This move secures Zulip's future as a community-governed open-source project, free from corporate control, which is crucial for its users who rely on it for serious discussions. The transition of key talent to Anthropic highlights the growing intersection between open-source collaboration tools and AI safety research. The Zulip Foundation will be independent and nonprofit, with an advisory board that includes volunteer members. The founder and three senior team members are donating the company to the foundation and moving to Anthropic, which focuses on AI safety.

hackernews · boramalper · May 15, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48152168)

**Background**: Zulip is an open-source team chat platform known for its threaded conversations that combine the speed of chat with the structure of email. It has been adopted by communities like Creative Commons and Lean. Anthropic is an AI safety company that develops the Claude large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://zulip.com/">Zulip — organized team chat</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://creativecommons.org/2025/09/18/new-community-chat-platform-moving-from-slack-to-zulip/">New Community Chat Platform: Moving from Slack to Zulip</a></li>

</ul>
</details>

**Discussion**: Community reactions are generally positive, with users praising Zulip's interface and expressing confidence in the foundation's long-term benefit. One user noted the Friday afternoon announcement timing might be to minimize attention, but others, including an advisory board member, affirmed the changes are good for stability.

**Tags**: `#Zulip`, `#open source`, `#foundation`, `#team chat`, `#governance`

---

<a id="item-24"></a>
## [Waymo recalls 3,800 robotaxis over standing water glitch](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html) ⭐️ 7.2/10

Waymo issued a recall for 3,800 robotaxis after a software glitch caused some vehicles to drive into standing water instead of avoiding it. This incident highlights a challenging edge case in autonomous driving: distinguishing between wet pavement and deep water. It underscores the ongoing debate between relying on sensor hardware versus inference-based software solutions. The glitch allowed vehicles to drive into standing water, potentially causing damage or stranding. Waymo updated the software to fix the issue, but no accidents were reported.

hackernews · drob518 · May 15, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48151767)

**Background**: Autonomous vehicles rely on sensors like cameras, LiDAR, and radar, combined with AI algorithms, to perceive the environment. Detecting standing water is difficult because it can appear similar to wet asphalt. Some researchers advocate for dedicated water sensors, while others prefer inference from vehicle behavior (e.g., slowing down, steering corrections) and vision processing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quora.com/How-do-self-driving-cars-handle-water-on-the-road">How do self-driving cars handle water on the road? - Quora</a></li>
<li><a href="https://arxiv.org/html/2411.10535v1">Advancing Autonomous Driving Perception: Analysis of Sensor ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters debated the sensor vs. inference approach. One commenter noted that a water sensor could make vehicles overly cautious about shallow puddles. Another pointed out the advantage of using Google's map data for inference. A humorous comment speculated about Waymo submarines.

**Tags**: `#autonomous vehicles`, `#Waymo`, `#robotaxi`, `#self-driving`, `#AI safety`

---

<a id="item-25"></a>
## [Hands-on with Linux Terminal on Android (2026 Edition)](https://sspai.com/prime/story/linux-vm-on-android) ⭐️ 7.2/10

An in-depth article explores Google's experimental Linux virtual machine feature on Pixel phones, introduced in 2025 and continuously updated through 2026, providing a native Linux terminal environment on Android. This feature brings a full Linux terminal to Android devices, enabling developers to code, run scripts, and use command-line tools directly on their phones, potentially transforming mobile devices into portable development workstations. The initial release in Android 15 only supports terminal access without graphical applications; GUI support is expected in Android 16. The feature is based on the Android Virtualization Framework (AVF) and currently limited to Google Pixel devices.

rss · 少数派 · May 14, 07:45

**Background**: Google's Linux-on-Android effort builds on the ChromeOS Crostini project, which runs Linux applications in a virtual machine on Chromebooks. The Android Virtualization Framework (AVF) provides the underlying secure execution environment. This experimental feature marks a step toward unifying mobile and desktop development ecosystems.

<details><summary>References</summary>
<ul>
<li><a href="https://habr.com/ru/news/889330/">В Android 15 для устройств Google Pixel добавлен Linux -терминал</a></li>
<li><a href="https://source.android.com/docs/core/virtualization">Android Virtualization Framework (AVF) overview | Android Open Source Project</a></li>
<li><a href="https://www.chromium.org/chromium-os/developer-library/guides/containers/containers-and-vms/">Running Custom Containers Under ChromeOS</a></li>

</ul>
</details>

**Tags**: `#Linux on Android`, `#Android development`, `#Linux VM`, `#ChromeOS`, `#mobile development`

---

<a id="item-26"></a>
## [6-8 Hours Sleep Linked to Lower Risk of Early Death and Disease](https://www.solidot.org/story?sid=84307) ⭐️ 7.2/10

A large-scale analysis of 500,000 adults found that sleeping 6 to 8 hours per day is associated with lower risks of premature death and diseases, with both shorter and longer sleep accelerating biological aging. The study examined 23 biological aging clocks across 17 organs, revealing a U-shaped relationship between sleep duration and aging. This study provides the most comprehensive overview to date of the relationship between sleep and human aging, supporting the hypothesis that adjusting sleep duration could be a viable way to reduce age-related disease risk. It offers actionable guidance for public health recommendations on optimal sleep duration. The optimal sleep duration varied by organ: for example, heart protein-based clocks indicated 6 hours as best, while brain protein clocks favored 8 hours. Gender differences were also observed in some cases. The study does not prove that meeting the 6-8 hour requirement directly improves health, but it shows a strong association.

rss · Solidot · May 15, 09:52

**Background**: Biological aging clocks are analytical tools that estimate biological age based on molecular markers such as proteins, metabolites, or medical imaging features, rather than chronological age. They measure how different organs have aged, revealing that aging rates vary across tissues. This study used 23 such clocks to assess the impact of sleep duration on aging across 17 organs.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9245174/">Aging clocks & mortality timers, methylation, glycomic, telomeric and more. A window to measuring biological age - PMC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epigenetic_clock">Epigenetic clock - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#sleep health`, `#unionization`, `#LLM agents`, `#science`

---

<a id="item-27"></a>
## [Coding Agents Lower Technology Lock-in](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 7.1/10

A medium-sized technology company used coding agents to migrate its legacy iPhone and Android apps to React Native, citing reduced lock-in concerns. The decision reflects a belief that future reversions could be equally feasible with agent assistance. This anecdote demonstrates how AI-powered coding agents are breaking long-standing technology lock-in by lowering the cost of cross-platform migrations. It may encourage more companies to adopt flexible architectures without fear of being permanently tied to one stack. The company used coding agents to rewrite two separate native mobile applications into a single React Native codebase. The agent-driven process presumably reduced effort and risk, making the migration economically viable despite the loss of platform-specific optimizations.

rss · Simon Willison · May 14, 22:53

**Background**: Coding agents are AI-powered assistants that can generate, refactor, and port code between languages or frameworks. React Native is a cross-platform framework that allows building mobile apps using JavaScript and React. Historically, technology choices like programming languages or platforms created lock-in because rewriting code was expensive and error-prone. Coding agents dramatically reduce that cost, making migrations and reversions more feasible.

<details><summary>References</summary>
<ul>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>
<li><a href="https://www.codegpt.co/">CodeGPT - AI Coding Assistant with Your Own API Key</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#React Native`, `#programming languages`, `#lock-in`, `#mobile development`

---

<a id="item-28"></a>
## [Project Gutenberg Continuously Improves Its Digital Library](https://www.gutenberg.org/) ⭐️ 7.0/10

Project Gutenberg's programmers have been making significant improvements to the website over the past few months, with more updates planned. This ongoing improvement enhances access to public domain literature for millions of readers worldwide, strengthening one of the oldest and most valuable digital libraries. The site now offers better usability and a richer browsing experience, though some users in Italy reported temporary access issues due to a legal seizure notice.

hackernews · JSeiko · May 15, 16:15 · [Discussion](https://news.ycombinator.com/item?id=48150431)

**Background**: Project Gutenberg, founded in 1971 by Michael S. Hart, is the oldest digital library, focusing on public domain works. It started with the digitization of the US Declaration of Independence and now offers over 70,000 free eBooks.

**Discussion**: Community comments highlight appreciation for recent site improvements, historical significance (founded in 1971), and personal stories of using Project Gutenberg. However, there is also a report of access issues in Italy due to a legal seizure, raising concerns about censorship.

**Tags**: `#project gutenberg`, `#digital library`, `#public domain`, `#ebooks`

---

<a id="item-29"></a>
## [DOJ Orders Apple and Google to Unmask 100K+ App Users](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 7.0/10

The U.S. Department of Justice has issued subpoenas demanding that Apple and Google reveal the identities of over 100,000 users who downloaded a car-tinkering app used to bypass emissions controls. This move signals a potential precedent for government data requests from centralized app stores, raising serious privacy concerns and highlighting the risks of relying on major platforms for software distribution. The app, described as a 'car-tinkering' tool, allows users to modify vehicle ECUs to disable emissions controls; the DOJ seeks user data to identify potential witnesses in an emissions crackdown.

hackernews · tencentshill · May 15, 17:28 · [Discussion](https://news.ycombinator.com/item?id=48151383)

**Background**: Emissions defeat devices are hardware or software that bypass a vehicle's emission control systems. ECU tuning refers to modifying a car's engine control unit to alter performance; while often used for performance gains, it can also disable emissions controls and is illegal in many jurisdictions. The DOJ's request targets users of such an app, which functions as a defeat device.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Defeat_device">Defeat device - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ECU_tuning">ECU tuning</a></li>

</ul>
</details>

**Discussion**: The discussion includes concerns about government overreach and the centralization of app distribution. Some commenters argue that users who deliberately defeat emissions controls are not worth sympathizing with, while others worry about potential misuse of data for non-environmental purposes.

**Tags**: `#privacy`, `#government overreach`, `#app stores`, `#emissions`, `#tech policy`

---

<a id="item-30"></a>
## [The emotional toll of nonconsensual deepfake porn](https://www.technologyreview.com/2026/05/14/1137161/ai-porn-nonconsensual-deepfakes-takedown-piracy-copyright/) ⭐️ 7.0/10

Jennifer, a nonprofit researcher, discovered that nonconsensual deepfake porn using her likeness still circulates online, and found the copyright takedown process inadequate for removal. This story highlights the severe emotional distress and legal obstacles faced by victims of nonconsensual deepfakes, exposing gaps in current copyright and takedown systems. Jennifer ran her professional headshot through facial recognition software to find old porn videos, and the search returned the deepfake content. The article underscores that copyright frameworks are ill-equipped to handle unauthorized pornographic use of one's likeness.

rss · MIT Tech Review · May 14, 09:00

**Background**: Deepfakes are realistic fake videos or images created using Generative Adversarial Networks (GANs), which can swap faces onto existing content. Nonconsensual deepfake pornography has become a growing crisis, with victims often struggling to remove content due to legal loopholes and platform policies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cvisionlab.com/cases/deepfake-gan/">Deepfake (Generative adversarial network) | CVisionLab</a></li>
<li><a href="https://rsilpak.org/2024/deepfakes-a-crisis-of-human-rights/">Deepfakes : A Crisis of Human Rights</a></li>

</ul>
</details>

**Tags**: `#deepfakes`, `#AI ethics`, `#nonconsensual porn`, `#copyright`, `#tech policy`

---