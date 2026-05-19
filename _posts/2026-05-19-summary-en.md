---
layout: default
title: "Horizon Summary: 2026-05-19 (EN)"
date: 2026-05-19
lang: en
---

> From 107 items, 24 important content pieces were selected

---

1. [Fine-Tuning NVIDIA Cosmos Predict 2.5 with LoRA/DoRA for Robot Video](#item-1) ⭐️ 9.3/10
2. [Forge Guardrails Boost Local LLM Reliability from 53% to 99%](#item-2) ⭐️ 9.0/10
3. [AI Warfare Is Here, and the West Is Unprepared: Ukrainian Founder](#item-3) ⭐️ 9.0/10
4. [CISA Admin Leaked AWS GovCloud Keys on GitHub](#item-4) ⭐️ 8.9/10
5. [OlmoEarth v1.1: More Efficient Open Earth AI Models](#item-5) ⭐️ 8.9/10
6. [Simon Willison's 5-Minute LLM Summary at PyCon US 2026](#item-6) ⭐️ 8.8/10
7. [Google Launches Gemini 3.5 Flash with Significant Price Hike](#item-7) ⭐️ 8.5/10
8. [Virtual Museum Showcases Nearly Every OS](#item-8) ⭐️ 8.5/10
9. [Gemini Omni Video Model Faces Spatial Reasoning Criticism](#item-9) ⭐️ 8.5/10
10. [Hugging Face and IBM Launch Open Agent Leaderboard](#item-10) ⭐️ 8.5/10
11. [Musk v. Altman Trial Roundtable Analysis](#item-11) ⭐️ 8.3/10
12. [PaddleOCR 3.5: OCR with Transformers Backend](#item-12) ⭐️ 8.0/10
13. [Nate Silver Laments Disney's Shutdown of FiveThirtyEight](#item-13) ⭐️ 7.9/10
14. [PSOS paper (1979): Provably secure OS foundations](#item-14) ⭐️ 7.8/10
15. [Hugging Face launches Ettin Reranker family for improved search retrieval.](#item-15) ⭐️ 7.8/10
16. [Google's AI-powered search box sparks traffic and trust debate](#item-16) ⭐️ 7.7/10
17. [NASA's Voyager Code Maintainers Are Dwindling](#item-17) ⭐️ 7.7/10
18. [Claude Code v2.1.145 Adds JSON Session Listing and Fixes](#item-18) ⭐️ 7.5/10
19. [MIT Insider Panel Decodes Key Tech Signals](#item-19) ⭐️ 7.5/10
20. [Claude Code v2.1.144 Adds Background Session Resume and Fixes](#item-20) ⭐️ 7.4/10
21. [Andrej Karpathy Joins Anthropic's Pre-Training Team](#item-21) ⭐️ 7.1/10
22. [OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool](#item-22) ⭐️ 7.0/10
23. [Mistral AI Acquires Emmi to Build Industrial AI Stack](#item-23) ⭐️ 7.0/10
24. [Interactive 3D Gaussian Splatting Demo of a Strawberry](#item-24) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Fine-Tuning NVIDIA Cosmos Predict 2.5 with LoRA/DoRA for Robot Video](https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation) ⭐️ 9.3/10

A tutorial published on Hugging Face demonstrates how to fine-tune NVIDIA's Cosmos Predict 2.5, a world foundation model, using Low-Rank Adaptation (LoRA) and its variant DoRA for generating robot videos. This tutorial lowers the barrier for adapting large-scale video generation models to specific robotics tasks, enabling efficient fine-tuning with limited computational resources. It accelerates progress in robot simulation and autonomous systems research by allowing practitioners to generate physics-aware, domain-specific videos. LoRA reduces trainable parameters by injecting low-rank matrices into the model's layers, while DoRA further improves performance by decomposing weights into magnitude and direction components. The tutorial likely covers dataset preparation, training configuration, and inference steps tailored for robot video generation.

rss · Hugging Face Blog · May 18, 16:00

**Background**: Cosmos Predict 2.5 is a world foundation model from NVIDIA that generates consistent, physics-aware videos from input frames. LoRA is a parameter-efficient fine-tuning method introduced by Microsoft in 2021, and DoRA is an enhancement developed by NVIDIA that better preserves pre-trained knowledge while maintaining efficiency. These techniques are widely used to adapt large models without full retraining.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-dora-a-high-performing-alternative-to-lora-for-fine-tuning/">Introducing DoRA, a High-Performing Alternative to LoRA for ...</a></li>
<li><a href="https://arxiv.org/abs/2402.09353">[2402.09353] DoRA: Weight-Decomposed Low-Rank Adaptation</a></li>
<li><a href="https://research.nvidia.com/labs/cosmos-lab/cosmos-predict2/">Cosmos - Predict 2 — Cosmos Lab</a></li>

</ul>
</details>

**Tags**: `#NVIDIA Cosmos`, `#Fine-tuning`, `#LoRA`, `#Robot Video Generation`, `#AI`

---

<a id="item-2"></a>
## [Forge Guardrails Boost Local LLM Reliability from 53% to 99%](https://github.com/antoinezambelli/forge) ⭐️ 9.0/10

Forge is an open-source guardrail layer that dramatically improves multi-step agentic task success rates for local LLMs, achieving 99%+ accuracy with an 8B model. This demonstrates that with proper guardrails, smaller local models can rival frontier APIs like Claude Sonnet, significantly reducing costs and enabling reliable self-hosted agentic systems. Forge includes five toggleable guardrail layers: retry nudges, step enforcement, error recovery, rescue parsing, and context compaction, with retry nudges and error recovery contributing the most to performance gains.

hackernews · zambelli · May 19, 12:23 · [Discussion](https://news.ycombinator.com/item?id=48192383)

**Background**: Agentic tasks involve AI systems making decisions, calling tools, and coordinating steps autonomously. Small models often fail on multi-step tasks due to compounding errors. LLM guardrails are safety mechanisms that steer model behavior. Forge adds structured reliability layers to address this.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/LLM_Guardrails">LLM Guardrails</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-workflows">What are agentic workflows? - IBM</a></li>

</ul>
</details>

**Discussion**: Commenters generally praised Forge, noting similar findings that structural guardrails unlock small model performance. One commenter shared their own approach with parse rescue and state machine enforcement, seeing completion rates jump from ~20% to 100% on some tasks. Others highlighted the value of appropriately scaled tech.

**Tags**: `#AI`, `#LLM`, `#guardrails`, `#agentic`, `#open-source`

---

<a id="item-3"></a>
## [AI Warfare Is Here, and the West Is Unprepared: Ukrainian Founder](https://www.latent.space/p/the-fourth-law) ⭐️ 9.0/10

Yaroslav Azhnyuk, a Ukrainian drone entrepreneur and founder of The Fourth Law, explains on Noah Smith's podcast how AI-guided drones are already transforming combat, arguing that Western militaries lag behind in adopting these technologies. The discussion highlights a critical gap in Western defense strategy, as AI-powered autonomous systems enable low-cost, asymmetric warfare that can overcome traditional military advantages, posing urgent implications for national security and defense investment. Azhnyuk transitioned from building pet cameras to developing AI-guided weapons, and the episode covers how computer vision and drone swarms can achieve coordinated attacks with minimal human oversight.

rss · Latent Space · May 18, 13:45

**Background**: Recent demonstrations show AI-guided drone swarms autonomously engaging targets, such as a swarm bypassing Russia's S-400 air defenses. Computer vision enables drones to detect objects, avoid obstacles, and execute missions without constant human control. However, Western militaries have been slower to integrate these capabilities compared to actors like Ukraine and Israel.

<details><summary>References</summary>
<ul>
<li><a href="https://auterion.com/auterion-launches-nemyx-enabling-fully-coordinated-drone-swarms/">Auterion Launches Nemyx, Enabling Fully Coordinated Drone Swarms</a></li>
<li><a href="https://recapio.com/digest/how-ai-drone-swarms-remotely-outmaneuvered-russias-s-400-in-sochi-by-battle-teller">How AI Drone Swarms Remotely Outmaneuvered... | Recapio</a></li>
<li><a href="https://www.meegle.com/en_us/topics/computer-vision/computer-vision-for-autonomous-drones">Computer Vision For Autonomous Drones</a></li>

</ul>
</details>

**Tags**: `#AI`, `#drones`, `#warfare`, `#defense technology`, `#Noah Smith`

---

<a id="item-4"></a>
## [CISA Admin Leaked AWS GovCloud Keys on GitHub](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 8.9/10

A CISA contractor inadvertently posted AWS GovCloud keys and other credentials on a public GitHub repository, exposing highly sensitive government cloud infrastructure. This incident underscores critical failures in secrets management and security practices within a top US cybersecurity agency, potentially allowing adversaries access to classified government systems. The leaked data included plaintext usernames and passwords for dozens of internal CISA systems, and the contractor reportedly ignored notifications about the exposure before it was escalated.

hackernews · LelouBil · May 19, 07:45 · [Discussion](https://news.ycombinator.com/item?id=48190454)

**Background**: AWS GovCloud is a US-only region designed to host sensitive government workloads with FedRAMP compliance. GitHub secret scanning tools can detect exposed credentials, but they rely on proper configuration and responsive action. Secrets management tools like AWS Secrets Manager exist to prevent such leaks.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cloud-security/github-secret-scanning/">GitHub Secret Scanning : Importance & Best Practices</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock at the lack of response and the inclusion of plaintext passwords, with some suspecting foreign intelligence agencies might view this as a honeypot. Others noted the broader problem of LLMs inadvertently scraping secrets from repos and the need for organizational audits.

**Tags**: `#security`, `#aws`, `#cloud`, `#cisa`, `#secrets-management`

---

<a id="item-5"></a>
## [OlmoEarth v1.1: More Efficient Open Earth AI Models](https://huggingface.co/blog/allenai/olmoearth-v1-1) ⭐️ 8.9/10

Allen AI released OlmoEarth v1.1, a more efficient family of open-source Earth observation foundation models, building on the original v1 release. The new version improves computational efficiency while maintaining performance on remote sensing tasks. OlmoEarth v1.1 makes advanced Earth AI more accessible to non-profits and researchers, accelerating work on climate monitoring, agriculture, and disaster response. Its efficiency gains reduce compute costs, lowering the barrier to using satellite data analysis at scale. The model family includes variants such as Base (~90M parameters) and Large (308M parameters), using a ViT architecture trained on 10TB of Sentinel-1, Sentinel-2, and Landsat satellite data. v1.1 improvements likely include optimized training or inference methods for greater throughput.

rss · Hugging Face Blog · May 19, 18:38

**Background**: OlmoEarth is a family of open-source foundation models developed by the Allen Institute for AI (Ai2) specifically for Earth observation tasks. Unlike general-purpose language models, these models learn patterns in satellite imagery to track environmental changes. The original OlmoEarth v1 was released in November 2025 and trained 10 terabytes of public satellite data.

<details><summary>References</summary>
<ul>
<li><a href="https://allenai.org/blog/olmoearth-models">OlmoEarth: A new state-of-the-art Earth observation foundation model family | Ai2</a></li>
<li><a href="https://arxiv.org/abs/2511.13655">[2511.13655] OlmoEarth: Stable Latent Image Modeling for Multimodal Earth Observation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Efficiency`, `#OlmoEarth`, `#Open-Source`

---

<a id="item-6"></a>
## [Simon Willison's 5-Minute LLM Summary at PyCon US 2026](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) ⭐️ 8.8/10

Simon Willison presented a lightning talk at PyCon US 2026 that summarized the last six months of LLM developments, highlighting a critical inflection point in November 2025 and the rapid succession of 'best' models from Anthropic, OpenAI, and Google. This talk provides a concise, expert-curated overview of the rapidly evolving LLM landscape, helping developers and researchers quickly grasp key milestones and model competition dynamics over a six-month period. Willison used his 'Generate an SVG of a pelican riding a bicycle' test to illustrate model differences, and noted that the 'best' model changed hands five times between the three major providers starting from September 2025.

rss · Simon Willison · May 19, 01:09

**Background**: Simon Willison is a well-known Python developer and creator of the annotated presentation tool, which enriches slides with explanatory text. His lightning talk at PyCon US 2026 uses this tool to break down LLM developments in a format accessible to a technical audience. The 'pelican riding a bicycle' test is a creative benchmark to compare image generation capabilities of different LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://tools.simonwillison.net/annotated-presentations">Annotated Presentation Creator - tools.simonwillison.net</a></li>
<li><a href="https://github.com/simonw/tools">GitHub - simonw/tools: Assorted useful tools, almost entirely ...</a></li>
<li><a href="https://the-decoder.com/get-more-out-of-your-presentations-with-ai-powered-annotated-slides/">Get more out of your presentations with AI-powered annotated ...</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#AI`, `#PyCon`, `#Simon Willison`, `#lightning talk`

---

<a id="item-7"></a>
## [Google Launches Gemini 3.5 Flash with Significant Price Hike](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) ⭐️ 8.5/10

Google has released Gemini 3.5 Flash as a generally available model, skipping the preview phase, with prices per million tokens at $1.50 input and $9.00 output — a 3x increase over earlier Gemini Flash models. This pricing shift makes Gemini 3.5 Flash comparable to Gemini 2.5 Pro in cost, potentially altering developer decisions on model selection and raising questions about the value proposition of smaller Flash models. Despite the price increase, Gemini 3.5 Flash offers improved agentic and coding performance, as demonstrated by benchmarks like Terminal-Bench 2.1 (76.2%) and MCP Atlas (83.6%).

hackernews · spectraldrift · May 19, 17:43 · [Discussion](https://news.ycombinator.com/item?id=48196570)

**Background**: Gemini Flash models are designed as faster, more affordable variants of Google's flagship Gemini models. Previous versions, such as Gemini 2.5 Flash and Gemini 3.0 Flash Preview, were priced lower, making this sudden increase notable.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5: frontier intelligence with action</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/pricing">Gemini Developer API pricing | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with users like GodelNumbering pointing out the unprecedented 3x price increase and comparing costs to larger models. Others, like SimonW and hmate9, report high token consumption and quota exhaustion, raising usability concerns.

**Tags**: `#AI`, `#LLM`, `#Gemini`, `#Google`, `#Pricing`

---

<a id="item-8"></a>
## [Virtual Museum Showcases Nearly Every OS](https://virtualosmuseum.org/) ⭐️ 8.5/10

A virtual museum, virtualosmuseum.org, has been launched, featuring interactive emulations of nearly every operating system ever created, from early mainframe OSes to modern versions. This project serves as an invaluable educational and nostalgic resource for developers, historians, and enthusiasts, preserving computing history in an accessible, interactive format. The museum includes over 1,700 emulated systems, covering major platforms like Windows, macOS, Linux, as well as obscure ones like Apollo Domain/OS and Pick OS.

hackernews · andreww591 · May 19, 15:53 · [Discussion](https://news.ycombinator.com/item?id=48195009)

**Background**: Operating system emulation allows modern browsers to run historical software through techniques like JavaScript-based interpreters or WebAssembly. This project builds on similar efforts but at an unprecedented scale, aiming to be the most comprehensive online OS collection.

**Discussion**: Commenters praised the immense curation effort, with one noting the fiddly work involved even for a smaller project of 13 OSes. Some pointed out missing systems like TempleOS and Pick OS, while others debated the choice of specific versions, such as Domain/OS SR10.4 not representing the most interesting iteration.

**Tags**: `#operating systems`, `#virtual museum`, `#computing history`, `#emulation`, `#retro computing`

---

<a id="item-9"></a>
## [Gemini Omni Video Model Faces Spatial Reasoning Criticism](https://deepmind.google/models/gemini-omni/) ⭐️ 8.5/10

Google launched Gemini Omni, a unified multimodal video generation model capable of text-to-video, remixing, and editing. Community discussions highlight that despite impressive visual quality, the model still struggles with spatial understanding and object coherence. This criticism underscores a fundamental limitation in current AI video generation: the lack of deep spatial reasoning. Addressing this is crucial for applications like simulations, advertising, and content creation where physical plausibility is essential. Google's Gemini Omni offers text-to-video, video remixing, and editing with text prompts, but testers report issues like objects disappearing or morphing when out of frame. The model's difficulty with rigid-body physics suggests a training methodology that prioritizes visual fidelity over structural understanding.

hackernews · meetpateltech · May 19, 17:46 · [Discussion](https://news.ycombinator.com/item?id=48196609)

**Background**: Gemini Omni is Google's latest unified multimodal video model that generates and edits videos from text prompts. Spatial reasoning in video generation is a known challenge, as models often fail to maintain consistent geometry and physics across frames. Recent research (e.g., 'Thinking with Video') explores using video generation as a reasoning paradigm, but practical models still struggle with these tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://gemini-omni.ai/">Gemini Omni Video Generator | AI Video Generator & Editor</a></li>
<li><a href="https://arxiv.org/html/2511.04570v1">Thinking with Video : Video Generation as a Promising Multimodal...</a></li>

</ul>
</details>

**Discussion**: Community comments are critically skeptical. Users point out that requests involving physical interactions (e.g., a Jenga tower falling) produce unrealistic results with bricks disappearing or morphing. Comparisons with Seedance 2 suggest Gemini Omni does not outperform existing alternatives, and a poorly phrased prompt raises concerns about model safety or misuse.

**Tags**: `#AI video generation`, `#spatial reasoning`, `#Google DeepMind`, `#video generation limitations`, `#model critique`

---

<a id="item-10"></a>
## [Hugging Face and IBM Launch Open Agent Leaderboard](https://huggingface.co/blog/ibm-research/open-agent-leaderboard) ⭐️ 8.5/10

Hugging Face and IBM Research have launched the Open Agent Leaderboard, a new open-source benchmark for evaluating AI agents across diverse tasks including planning, decision-making, and tool use. The leaderboard currently features five models, including DeepSeek V3.2 and Kimi K2.5, across six benchmarks. This leaderboard addresses a critical gap in AI evaluation, as most existing benchmarks were not designed for general-purpose agents. It provides a standardized, transparent way to compare agent capabilities, which is essential for advancing research and practical deployment of AI agents. The leaderboard is an evolving project that welcomes community feedback and contributions. Since launch, it has added two open-weight models, DeepSeek V3.2 and Kimi K2.5, bringing the total to five models across five agents and six benchmarks. Users can filter and compare accuracy vs. cost via an interactive web app.

rss · Hugging Face Blog · May 18, 14:12

**Background**: AI agents are systems that combine large language models with tools and planning capabilities to perform complex tasks autonomously. Leaderboards like this one are crucial for benchmarking progress; the Open Agent Leaderboard specifically addresses the lack of standardized evaluation for general-purpose agents that can handle diverse real-world scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-research/open-agent-leaderboard">The Open Agent Leaderboard</a></li>
<li><a href="https://www.evidentlyai.com/blog/ai-agent-benchmarks">10 AI agent benchmarks</a></li>
<li><a href="https://huggingface.co/spaces/omlab/open-agent-leaderboard">Open Agent Leaderboard - a Hugging Face Space by omlab</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#benchmarking`, `#open source`, `#performance evaluation`, `#Hugging Face`

---

<a id="item-11"></a>
## [Musk v. Altman Trial Roundtable Analysis](https://www.technologyreview.com/2026/05/19/1137454/roundtables-inside-the-musk-v-altman-trial/) ⭐️ 8.3/10

MIT Technology Review published a roundtable discussion with reporter Michelle Kim analyzing the Musk v. Altman trial, where Elon Musk lost his suit against OpenAI alleging deception over its non-profit status. This trial has significant implications for AI governance, particularly regarding the conversion of non-profit AI research organizations to for-profit entities, and sets a precedent for legal accountability in the AI industry. The roundtable features AI reporter and attorney Michelle Kim, who covered the trial for MIT Technology Review, discussing the case with the editor. Elon Musk alleged CEO Sam Altman and President Greg Brockman deceived him about OpenAI's non-profit status.

rss · MIT Tech Review · May 19, 20:15

**Background**: Elon Musk co-founded OpenAI in 2015 as a non-profit AI research organization, but left in 2018. He later sued OpenAI, claiming the company abandoned its non-profit mission by transitioning to a for-profit structure. The trial focused on whether Musk was misled about this transition, and the court ultimately ruled in favor of OpenAI.

**Tags**: `#AI`, `#OpenAI`, `#Elon Musk`, `#legal`, `#governance`

---

<a id="item-12"></a>
## [PaddleOCR 3.5: OCR with Transformers Backend](https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers) ⭐️ 8.0/10

PaddleOCR 3.5 introduces a Transformers backend, enabling seamless integration of OCR and document parsing tasks with modern transformer models. This update bridges the gap between traditional OCR toolkits and the transformer ecosystem, making it easier for developers to combine OCR with large language models for document understanding. The release supports over 100 languages and includes advanced models like PaddleOCR-VL-1.5, which achieves 94.5% accuracy on OmniDocBench v1.5.

rss · Hugging Face Blog · May 18, 15:12

**Background**: PaddleOCR is an open-source OCR toolkit developed by PaddlePaddle. It provides text detection and recognition for multilingual documents and images. The Transformers backend allows users to leverage pre-trained transformer models for improved accuracy and flexibility.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/PaddleOCR">PaddleOCR</a></li>
<li><a href="https://github.com/PADDLEPADDLE/PADDLEOCR">GitHub - PaddlePaddle/PaddleOCR: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. · GitHub</a></li>
<li><a href="https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5">PaddlePaddle/PaddleOCR-VL-1.5 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#PaddleOCR`, `#Transformers`, `#Document Parsing`, `#AI Tooling`

---

<a id="item-13"></a>
## [Nate Silver Laments Disney's Shutdown of FiveThirtyEight](https://www.natesilver.net/p/disney-erased-fivethirtyeight) ⭐️ 7.9/10

Nate Silver published a newsletter reflecting on Disney's shutdown of FiveThirtyEight in March 2025, expressing regrets about the acquisition and criticizing leadership changes at ABC News that led to the site's demise. This event underscores the fragility of data journalism under corporate ownership, where leadership transitions can override editorial success. It also highlights the tension between independent statistical analysis and corporate media goals. Silver left FiveThirtyEight in 2023, taking his forecasting model to his new site Silver Bulletin. Disney hired G. Elliott Morris to develop a new model, then in 2025 the site was shut down and its domain redirected to ABC News.

hackernews · 7777777phil · May 19, 18:56 · [Discussion](https://news.ycombinator.com/item?id=48197703)

**Background**: FiveThirtyEight was founded by Nate Silver in 2008, gaining fame for accurate election forecasts using statistical models. Disney's ESPN acquired the site in 2014, integrating it into ABC News later. In 2023, Silver left amid corporate restructuring, and the site was rebranded as 538 before being shuttered in 2025.

**Discussion**: Commenters expressed frustration with Silver's narrative, with some criticizing him for selling out to a conglomerate and then acting surprised. Others cited the 2016 election forecast as a turning point that disillusioned them with FiveThirtyEight.

**Tags**: `#media`, `#acquisitions`, `#data journalism`, `#corporate strategy`

---

<a id="item-14"></a>
## [PSOS paper (1979): Provably secure OS foundations](http://www.csl.sri.com/users/neumann/psos.pdf) ⭐️ 7.8/10

The Hacker News community revisits the 1979 PSOS paper, discussing its capability-based architecture and its connection to the modern formally verified microkernel seL4. This discussion highlights the enduring relevance of capability-based security and formal verification, showing how ideas from the 1970s are finally being realized in production systems like seL4. PSOS used the SRI Hierarchical Development Methodology (HDM) for formal specification, while seL4 provides a machine-checked proof of its C implementation down to abstract specification using Isabelle/HOL. The concept of tag memory with unforgeable access tokens is a core difference from typical software ACLs.

hackernews · rurban · May 18, 09:40 · [Discussion](https://news.ycombinator.com/item?id=48177300)

**Background**: Formal verification of operating systems aims to mathematically prove security properties like confidentiality and integrity. Capability-based security replaces ambient authority (global user permissions) with unforgeable tokens passed between components. PSOS was a pioneering design from 1975-1979, while seL4 achieved the first practical formal verification of a general-purpose OS kernel in 2009.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infosecinstitute.com/resources/operating-system-security/provably-secure-operating-systems/">Provably Secure Operating Systems | Infosec</a></li>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments express surprise at seeing PSOS again, with firsthand accounts from former KSOS developers. The discussion emphasizes that capability systems are the only suitable architecture for the internet age, and that seL4 is the modern inheritor of PSOS ideas. Some users draw analogies between capability systems and local variable scoping in programming languages.

**Tags**: `#operating system security`, `#formal verification`, `#capability-based security`, `#seL4`, `#PSOS`

---

<a id="item-15"></a>
## [Hugging Face launches Ettin Reranker family for improved search retrieval.](https://huggingface.co/blog/ettin-reranker) ⭐️ 7.8/10

Hugging Face released six new reranking models called the Ettin Reranker family, finetuned from Ettin encoders on the MS MARCO dataset and licensed under Apache 2.0. Rerankers are critical for enhancing retrieval accuracy in retrieval-augmented generation (RAG) systems, and this open-source release makes state-of-the-art reranking more accessible to the AI community. The models range from 32M to 68M parameters and were evaluated on the full MTEB (v2) English Retrieval benchmark using six different embedding models in a two-stage reranking flow.

rss · Hugging Face Blog · May 19, 00:00

**Background**: Rerankers are cross-encoder models that reorder a set of initially retrieved documents based on semantic relevance to a query. They are typically used as a second stage after fast initial retrieval to improve accuracy in search and RAG pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ettin-reranker">Introducing the Ettin Reranker Family</a></li>
<li><a href="https://huggingface.co/tomaarsen/ms-marco-ettin-32m-reranker">tomaarsen/ms-marco-ettin-32m-reranker · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#reranker`, `#Hugging Face`, `#retrieval`

---

<a id="item-16"></a>
## [Google's AI-powered search box sparks traffic and trust debate](https://blog.google/products-and-platforms/products/search/search-io-2026/) ⭐️ 7.7/10

At Google I/O 2026, Google announced that its search box will now use Gemini AI to generate direct answers, replacing the traditional list of links. This change aims to provide instant information but raises concerns about reduced traffic to websites. This shift could drastically reduce organic traffic to publishers, a phenomenon known as 'Google Zero,' and may undermine user trust in search results as AI-generated answers may lack accuracy. It reflects the broader industry trend of LLMs replacing traditional search, affecting how information is accessed and monetized. The integration uses Google's Gemini model (likely Gemini 3.5 or later) to synthesize answers from multiple sources, but critics warn it may combine information from different eras, leading to errors. The update is part of a broader move toward 'answer engines' that prioritize direct responses over link lists.

hackernews · berkeleyjunk · May 19, 18:34 · [Discussion](https://news.ycombinator.com/item?id=48197370)

**Background**: Traditional search engines like Google return a list of links to websites. Large language models (LLMs) such as Google's Gemini can generate direct answers by synthesizing information from multiple sources. Google has been incorporating AI into search for a while, but the new search box represents a fundamental shift, as it prioritizes AI-generated answers over links. This has led to concerns about reduced traffic to content creators, a scenario known as 'Google Zero'.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://hbr.org/2026/03/llms-are-overtaking-search-heres-how-to-adjust-your-online-presence">LLMs Are Overtaking Search. Here’s How to Adjust Your Online Presence.</a></li>
<li><a href="https://searchengineland.com/decoding-llms-generative-ai-search-results-448630">Decoding LLMs: How to be visible in generative AI search results</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about the reliability of AI-generated answers, noting that the model may treat random comments as representative ('people think...' but from only one source). Others highlighted the 'Google Zero' phenomenon and their own decreased reliance on Google Search. The overall sentiment is skeptical, with users demanding primary sources and questioning the value of synthesized answers.

**Tags**: `#AI`, `#Search`, `#LLM`, `#Google`, `#Gemini`

---

<a id="item-17"></a>
## [NASA's Voyager Code Maintainers Are Dwindling](https://www.solidot.org/story?sid=84328) ⭐️ 7.7/10

NASA's Voyager probes, launched 48 years ago, still run on assembly code from the 1970s, and the team of aging engineers who maintain it is shrinking, with most original documentation lost. This highlights the critical risk of institutional knowledge loss in long-running space missions, as the unique expertise required to maintain Voyager's legacy software is disappearing with the aging workforce. The probes have three computer systems (CCS, ACS, FDS) with only 64-70 KB of total memory, run on a specialized assembly language for a custom processor, and ground systems use Fortran. Larry Zottarelli, the last original-team engineer, retired in 2016 at age 80.

rss · Solidot · May 18, 12:59

**Background**: The Voyager 1 and Voyager 2 spacecraft were launched by NASA in 1977 to explore the outer planets and are now in interstellar space. Their onboard computers were designed with 1970s technology, using very limited memory and custom assembly code. As the original engineers age or pass away, maintaining this legacy software becomes increasingly difficult, especially since much of the documentation was on paper and lost during office moves.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/">Where Are Voyager 1 and 2 Now? - NASA Science</a></li>

</ul>
</details>

**Tags**: `#NASA`, `#Voyager`, `#Legacy Code`, `#Software Maintenance`, `#Engineering`

---

<a id="item-18"></a>
## [Claude Code v2.1.145 Adds JSON Session Listing and Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) ⭐️ 7.5/10

Anthropic released claude-code v2.1.145, adding a `claude agents --json` command to list live sessions as JSON, improving telemetry with new OpenTelemetry span attributes, and fixing numerous bugs including a permission bypass and MCP prompt errors. These updates enhance claude-code's usability for power users and developers who integrate it into scripting workflows and status monitors, while security and stability fixes make the tool more reliable for production use. The JSON session listing supports tools like tmux-resurrect, status bars, and session pickers; telemetry now includes `agent_id` and `parent_agent_id` for better tracing; a critical fix prevents auto-approval of non-allowlisted environment variables in Bash commands.

github · ashwin-ant · May 19, 21:31

**Background**: Claude Code is Anthropic's command-line AI agent tool for coding tasks. It leverages Claude's abilities to assist with code generation, debugging, and repository management. The release also addresses integration with tmux (terminal multiplexer), OpenTelemetry for observability, and the Model Context Protocol (MCP) for connecting AI to external tools.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tmux-plugins/tmux-resurrect">GitHub - tmux-plugins/tmux-resurrect: Persists tmux ...</a></li>
<li><a href="https://opentelemetry.io/docs/concepts/signals/traces/">Traces | OpenTelemetry</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI agents`, `#CLI tool`, `#Anthropic`

---

<a id="item-19"></a>
## [MIT Insider Panel Decodes Key Tech Signals](https://www.technologyreview.com/2026/05/18/1137430/the-signals-that-matter-mit-insiders-panel/) ⭐️ 7.5/10

An MIT-hosted panel, 'The Signals That Matter,' discussed critical emerging technology signals with a focus on AI trends and their practical implications for industry and research. This panel provides curated insights from top MIT researchers, helping professionals identify which early signals truly indicate transformative shifts rather than noise, influencing strategic decisions in tech adoption and investment. The panel likely covered signals across AI safety, generative models, and hardware bottlenecks, emphasizing interdisciplinary approaches to detect meaningful patterns in a rapidly evolving landscape.

rss · MIT Tech Review · May 18, 16:57

**Background**: In technology forecasting, 'signals' refer to early indicators that a new technology or trend may become significant. MIT has a long history of leading such foresight discussions through its Media Lab, CSAIL, and Technology Review, making this panel a credible source for identifying which signals merit attention.

**Tags**: `#AI`, `#technology trends`, `#MIT`, `#signals`, `#tech industry`

---

<a id="item-20"></a>
## [Claude Code v2.1.144 Adds Background Session Resume and Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) ⭐️ 7.4/10

Anthropic released Claude Code v2.1.144, introducing /resume support for background sessions, renaming 'extra usage' to 'usage credits', and fixing over 20 bugs including startup hangs, terminal corruption, and MCP tool issues. This update significantly improves reliability and user experience for Claude Code users, especially those using background sessions and encountering network or terminal issues. The fixes for startup hangs and terminal corruption make the tool more robust for daily development workflows. Key technical improvements include a 15-second timeout for side-channel API calls to prevent 75-second startup hangs, self-healing terminal display after missed resize events, and proper fallback for Bedrock and Vertex users selecting Opus model. The /model command now changes the model for the current session only, with a new 'd' shortcut to set a default.

github · ashwin-ant · May 19, 00:48

**Background**: Claude Code is a terminal-based AI coding assistant from Anthropic that integrates with various APIs and tools. A side-channel API call refers to a background or auxiliary request made in addition to the primary API communication. A captive portal is a web page that intercepts network traffic and requires user action (e.g., login or acceptance of terms) before granting internet access; it commonly appears on public Wi-Fi and can cause connectivity issues for CLI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/66848604/best-practice-for-securing-a-client-side-call-to-an-api-endpoint">Best practice for securing a client side call to an API endpoint</a></li>
<li><a href="https://en.wikipedia.org/wiki/Captive_portal">Captive portal</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#release notes`, `#CLI tool`, `#bug fixes`

---

<a id="item-21"></a>
## [Andrej Karpathy Joins Anthropic's Pre-Training Team](https://twitter.com/karpathy/status/2056753169888334312) ⭐️ 7.1/10

Andrej Karpathy announced via Twitter that he has joined Anthropic, specifically their pre-training team, which is responsible for the massive training runs that give Claude its core knowledge and capabilities. This move signals a major talent acquisition for Anthropic, as Karpathy is a highly influential figure in AI education and research. His involvement could accelerate advances in pre-training techniques, benefiting the entire AI ecosystem. Karpathy will start immediately on the pre-training team, which handles the massive computation and data processing required for training Claude. He had previously hinted at such a move in a recent interview, expressing interest in joining a frontier lab.

hackernews · dmarcos · May 19, 15:07 · [Discussion](https://news.ycombinator.com/item?id=48194352)

**Background**: Pre-training is a machine learning technique where a model is first trained on a large, unlabeled dataset to learn general patterns, then fine-tuned on specific tasks. This approach underpins models like GPT and Claude, enabling them to acquire broad language understanding before specialization. Karpathy is well-known for his educational contributions, including the concepts of 'Software 2.0' and 'Vibe Coding'.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre - trained transformer - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed hope that Karpathy will continue his teaching efforts despite potential NDA constraints. One noted he had foreshadowed this move in a prior interview. The general sentiment is positive, with appreciation for his educational contributions and concern about possible restrictions.

**Tags**: `#AI`, `#Anthropic`, `#Karpathy`, `#machine learning`, `#industry news`

---

<a id="item-22"></a>
## [OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool](https://openai.com/index/advancing-content-provenance/) ⭐️ 7.0/10

OpenAI announced it is integrating Google DeepMind's SynthID watermarking technology into its AI image generation models, along with a new content provenance verification tool, to help users identify AI-generated images. This move represents a major step toward industry-wide content provenance standards, as major AI companies align on watermarking to combat misinformation. However, the effectiveness hinges on widespread adoption and resistance to tampering. SynthID embeds imperceptible digital watermarks into images, audio, and text, which can be detected by a verification tool. OpenAI's implementation currently covers images from DALL-E and other generative models, but the watermark can be removed by cropping, compression, or malicious actors who opt not to use SynthID.

hackernews · OpenAI Blog · May 19, 19:34 · [Discussion](https://news.ycombinator.com/item?id=48198291)

**Background**: SynthID is a watermarking tool developed by Google DeepMind for AI-generated content, designed to embed imperceptible identifiers. It works across multiple modalities including images, audio, and text. Content provenance refers to the ability to trace the origin and history of digital media, which is increasingly important as generative AI becomes widespread.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/SynthID">SynthID</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some users doubt the watermark's robustness, noting it can be easily removed through cropping or compression, while others argue no reproducible watermark removal repo exists. There is also criticism that this is 'performative nonsense' and concerns that malicious actors will simply avoid using SynthID.

**Tags**: `#AI`, `#OpenAI`, `#SynthID`, `#watermark`, `#content provenance`

---

<a id="item-23"></a>
## [Mistral AI Acquires Emmi to Build Industrial AI Stack](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai) ⭐️ 7.0/10

Mistral AI has acquired Austrian startup Emmi AI to create what it calls the leading AI stack for industrial engineering and manufacturing. This acquisition signals a strategic push by Mistral AI into vertical industrial AI, leveraging ASML's investment to differentiate from general-purpose AI models. Emmi AI has developed Noether, an open-source deep learning framework for engineering simulations, and Mistral AI plans to integrate it into a comprehensive industrial AI stack.

hackernews · doener · May 19, 19:14 · [Discussion](https://news.ycombinator.com/item?id=48197995)

**Background**: Mistral AI is a French AI startup that has received significant investment from ASML, a leading semiconductor equipment manufacturer. Industrial AI refers to AI models tailored for physics-based simulations, manufacturing, and automation, an area where general-purpose LLMs often fall short. The acquisition aims to combine Mistral's platform with Emmi's domain expertise to serve industrial enterprises.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai">Mistral AI Acquires Emmi AI to Create the Leading AI Stack ...</a></li>
<li><a href="https://techstartups.com/2026/05/19/mistral-ai-acquires-emmi-ai-to-expand-industrial-ai-push-across-europe/">Mistral AI acquires Emmi AI to expand industrial AI push ...</a></li>
<li><a href="https://seekingalpha.com/news/4594732-mistral-ai-acquires-industrial-engineering-ai-startup-emmi">Mistral AI acquires industrial engineering AI startup Emmi</a></li>

</ul>
</details>

**Discussion**: Community comments highlight ASML's investment as a key factor making Mistral's industrial ambitions credible. Some express skepticism due to lack of concrete product details, while others see vertical differentiation as a smart move.

**Tags**: `#AI`, `#Mistral AI`, `#acquisition`, `#industrial engineering`, `#LLM`

---

<a id="item-24"></a>
## [Interactive 3D Gaussian Splatting Demo of a Strawberry](https://superspl.at/scene/84df8849) ⭐️ 7.0/10

A user uploaded a 3D Gaussian splatting reconstruction of a strawberry from multiple photographs, viewable interactively in the browser via WebGL on SuperSplat. This demo showcases the accessibility of 3D Gaussian splatting, a cutting-edge research technique for photorealistic novel view synthesis, now usable by anyone with a browser. The reconstruction was created from multiple photographs of a strawberry setup, using Gaussian splatting to represent the scene as anisotropic ellipsoids, rendered in real-time on the web with SuperSplat.

hackernews · danybittel · May 19, 10:38 · [Discussion](https://news.ycombinator.com/item?id=48191602)

**Background**: Gaussian splatting is a volume rendering technique that represents 3D scenes using collections of anisotropic 3D Gaussian primitives. It was popularized in 2023 by a research group from Inria, enabling high-quality, real-time radiance field rendering from multiple images. SuperSplat is an open platform for editing, sharing, and browsing 3D Gaussian splat scenes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting</a></li>
<li><a href="https://github.com/graphdeco-inria/gaussian-splatting">GitHub - graphdeco-inria/gaussian-splatting: Original ... What Is Gaussian Splatting? Complete Beginner Guide for ... Splats Change Everything: Why a once-obscure technology is ... SuperSplat - The Home for 3D Gaussian Splatting Beyond polygons: How Gaussian Splatting transforms 3D rendering A Comprehensive Overview of Gaussian Splatting</a></li>

</ul>
</details>

**Discussion**: Commenters shared additional interesting scenes and noted technical aspects: one pointed out that WebGL support is required, while another praised the graceful degradation of Gaussian splats, which become blurry rather than blocky when zooming in.

**Tags**: `#gaussian splatting`, `#3d reconstruction`, `#computer graphics`, `#webgl`, `#show hn`

---