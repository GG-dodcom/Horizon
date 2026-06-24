---
layout: default
title: "Horizon Summary: 2026-06-24 (EN)"
date: 2026-06-24
lang: en
---

> From 118 items, 25 important content pieces were selected

---

1. [Krea 2: Open-weights 12B Image Model Released](#item-1) ⭐️ 9.9/10
2. [NSA lost access to Anthropic's Mythos](#item-2) ⭐️ 9.7/10
3. [Carmack Regrets Pushing id Software Team Too Hard](#item-3) ⭐️ 9.6/10
4. [Hugging Face's weekly AI-assisted release process](#item-4) ⭐️ 9.5/10
5. [Databricks Leaders: Why Frontier Ecosystem Must Be Open](#item-5) ⭐️ 9.4/10
6. [Porting Moebius 0.2B Image Inpainting Model to Browser with WebGPU](#item-6) ⭐️ 9.2/10
7. [CUGA: Open-source harness for building agentic apps with 24 examples](#item-7) ⭐️ 9.2/10
8. [OpenAI Unveils First Custom AI Chip Jalapeño](#item-8) ⭐️ 9.0/10
9. [Nub: Bun-like all-in-one toolkit for Node.js](#item-9) ⭐️ 8.8/10
10. [Debate grows on removing GitHub dependency for Rust crates.io publishing](#item-10) ⭐️ 8.8/10
11. [NVIDIA NeMo AutoModel Accelerates Transformer Fine-Tuning](#item-11) ⭐️ 8.7/10
12. [NVIDIA 45°C Liquid Cooling Slashes Data Center Water Use](#item-12) ⭐️ 8.5/10
13. [DeepMind's Gemini 3.5 Flash Gains Computer Use Abilities](#item-13) ⭐️ 8.5/10
14. [Memory Chip Makers' Regret and Microsoft's China AI Incentive](#item-14) ⭐️ 8.5/10
15. [Ben Thompson's Vibe Coding Takeaways](#item-15) ⭐️ 8.4/10
16. [Hugging Face Launches FFASR Leaderboard for Real-World ASR](#item-16) ⭐️ 8.0/10
17. [Experimenting with Cross-Origin Storage API for Transformers.js](#item-17) ⭐️ 8.0/10
18. [Claude Slack Integration Gets Multiplayer, Proactive, Persistent Agents](#item-18) ⭐️ 8.0/10
19. [LLMs Confuse System Tags with User Input, Enabling Jailbreaks](#item-19) ⭐️ 7.8/10
20. [Bunny DNS Becomes Free for Up to 500 Domains](#item-20) ⭐️ 7.7/10
21. [Web data infrastructure layer emerges for AI models](#item-21) ⭐️ 7.6/10
22. [Claude Code v2.1.187: Sandbox Credentials, Model Restrictions, Mouse Support](#item-22) ⭐️ 7.5/10
23. [PR spam mirrors early 2000s email spam](#item-23) ⭐️ 7.5/10
24. [Coinbase's lack of automated zone failover](#item-24) ⭐️ 7.5/10
25. [RubyLLM: Unified Ruby framework for AI providers](#item-25) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [Krea 2: Open-weights 12B Image Model Released](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 9.9/10

Krea AI has released the weights and a comprehensive technical report for Krea 2, a state-of-the-art 12-billion-parameter open-weights image generation model, along with a faster Turbo variant. This release provides the AI community with a high-quality, locally hostable image model that outperforms other open models and rivals proprietary ones, promoting transparency and further research. Krea 2 uses a diffusion transformer architecture with timestep and guidance distillation for the Turbo variant, and the technical report details data curation, captioning, post-training, and RL pipelines.

hackernews · mattnewton · Jun 23, 15:31 · [Discussion](https://news.ycombinator.com/item?id=48646659)

**Background**: Open-weights models allow anyone to download, inspect, and fine-tune the model weights. Krea 2 is trained from scratch and focuses on creative stylistic exploration, offering both text and image-based control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.krea.ai/blog/krea-2-technical-report">Krea 2 Technical Report</a></li>
<li><a href="https://github.com/krea-ai/krea-2">GitHub - krea-ai/krea-2: Official inference code for Krea 2</a></li>
<li><a href="https://www.krea.ai/krea-2">Krea 2: AI Image Foundation Model & Style Control</a></li>

</ul>
</details>

**Discussion**: Community members praised the detailed write-up and noted that Krea 2 Turbo achieved the highest score among locally hostable models in benchmarks, though it failed certain adversarial tests. The authors engaged actively, answering questions about infrastructure and training.

**Tags**: `#AI`, `#image generation`, `#open weights`, `#technical report`, `#machine learning`

---

<a id="item-2"></a>
## [NSA lost access to Anthropic's Mythos](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html) ⭐️ 9.7/10

The NSA lost access to Anthropic's advanced AI cybersecurity tool, Mythos, due to a dispute over safety terms. The contract has not been finalized, and some Pentagon officials want the NSA to work with other models. This incident highlights the tension between AI safety and national security, as Mythos is a powerful tool capable of breaking into classified systems in hours. It raises questions about who controls cutting-edge AI and how such power should be governed. Mythos is an unreleased AI model from Anthropic designed for high-stakes cybersecurity, capable of quickly penetrating classified systems. The dispute arose when Anthropic refused to license Mythos under terms it deemed unsafe, leading to a broader clash with the US government.

hackernews · thm · Jun 24, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48658300)

**Background**: Anthropic, an AI safety company, developed Mythos as a powerful cybersecurity tool but deemed it too dangerous for public release. The company has been in an escalating dispute with the US government, with President Trump ordering federal agencies to stop using Anthropic's AI in February 2026. The NSA had been using Mythos under a special arrangement, which has now been revoked amid the dispute.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/apr/22/what-is-anthropic-mythos-ai-threat-global-cybersecurity">What is Mythos AI and why could it be a threat to global cybersecurity ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute</a></li>
<li><a href="https://apnews.com/article/anthropic-pentagon-ai-hegseth-dario-amodei-b72d1894bc842d9acf026df3867bee8a">Trump orders all US agencies to stop using Anthropic's AI ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some criticized the NSA and hoped the agency would not regain access, while others questioned the tool's capabilities, noting that Mythos can break into classified systems in hours. A few speculated that the government could still obtain the weights if desired.

**Tags**: `#AI`, `#cybersecurity`, `#NSA`, `#Anthropic`, `#LLM`

---

<a id="item-3"></a>
## [Carmack Regrets Pushing id Software Team Too Hard](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 9.6/10

John Carmack, co-founder of id Software, admitted in a tweet that he pushed his team too hard during the early days and failed to adjust management style as the company matured. He specifically noted that running people at startup intensity constantly wears them out and harms company longevity. This candid self-criticism from a legendary game developer offers valuable lessons for software engineering and startup culture, highlighting the trade-off between intense productivity and sustainable team health. It resonates with ongoing debates about work intensity, burnout, and company longevity in the tech industry. Carmack's reflection is framed by the success of Quake, which he considers worth the cost even if it 'gutted' id Software. Community comments point to Sandy Petersen's account of the intense environment, and note a perceived decline in id Software's innovation after Quake 3 Arena.

hackernews · shadowtree · Jun 24, 15:56 · [Discussion](https://news.ycombinator.com/item?id=48661825)

**Background**: John Carmack is a renowned programmer and co-founder of id Software, known for pioneering first-person shooters like Wolfenstein 3D, Doom, and Quake. The company was famous for its intense, startup-like culture, which drove groundbreaking technical achievements but also led to burnout and turnover. This tweet reflects Carmack's retrospective view on the sustainability of such a culture.

**Discussion**: Comments generally agree with Carmack's assessment, with users like ChrisMarshallNY calling it 'wisdom many companies might consider.' Some debate whether Quake was worth the cost, with rustyhancock and FartyMcFarter defending its impact on gaming. Others, like tejohnso, note a perceived decline in id Software's innovation after Quake 3 Arena, suggesting the intense culture had long-term effects.

**Tags**: `#software engineering`, `#management`, `#game development`, `#startup culture`, `#id Software`

---

<a id="item-4"></a>
## [Hugging Face's weekly AI-assisted release process](https://huggingface.co/blog/huggingface-hub-release-ci) ⭐️ 9.5/10

Hugging Face shared their weekly release process for the huggingface_hub library, which uses AI tools and human review to automate and ensure quality. This demonstrates a practical CI/CD pipeline that leverages AI to accelerate development while maintaining human oversight, setting an example for open-source projects. The process likely involves automated testing, AI-generated changelogs or code reviews, and a human-in-the-loop to approve final releases every week.

rss · Hugging Face Blog · Jun 23, 00:00

**Background**: The huggingface_hub library is the official Python client for the Hugging Face Hub, a platform for sharing and managing machine learning models, datasets, and other artifacts. It enables developers to interact with the Hub programmatically. The blog describes their automated release pipeline that runs weekly.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huggingface/huggingface_hub">GitHub - huggingface/huggingface_hub: The official Python client for the Hugging Face Hub. · GitHub</a></li>
<li><a href="https://huggingface.co/docs/huggingface_hub/en/index">🤗 Hub client library · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#huggingface`, `#CI/CD`, `#AI-assisted development`, `#open source`, `#release process`

---

<a id="item-5"></a>
## [Databricks Leaders: Why Frontier Ecosystem Must Be Open](https://www.latent.space/p/databricks) ⭐️ 9.4/10

In a rare double-interview, Databricks technical leaders Matei Zaharia and Reynold Xin discuss why open ecosystems are essential for building enterprise agent clouds. As agentic AI becomes central to enterprise workflows, Databricks' advocacy for open ecosystems challenges the trend of closed, proprietary agent platforms and could shape how companies build and deploy AI agents. The interview covers Databricks' multi-provider catalog of frontier models accessible through a single unified API, highlighting the company's stance against vendor lock-in and its broad partner ecosystem.

rss · Latent Space · Jun 24, 18:53

**Background**: Enterprise agent clouds are platforms that allow developers to build, deploy, and govern AI agents at scale. Databricks, known for its unified data and AI platform, has been expanding into agentic workflows with products like Agent Bricks, announced at Data + AI Summit 2026. The company emphasizes openness to allow customers to choose from multiple frontier models and avoid dependency on a single AI provider.

<details><summary>References</summary>
<ul>
<li><a href="https://www.databricks.com/blog/agent-bricks-dais-2026">Agent Bricks: Data + AI Summit 2026 | Databricks Blog</a></li>
<li><a href="https://anudeepsri.medium.com/a-technical-deep-dive-into-databricks-ai-ecosystem-26f032111ad4">A Technical Deep Dive into Databricks AI Ecosystem | by Anudeep | Medium</a></li>
<li><a href="https://www.atscale.com/blog/databricks-summit-2026-takeaways/">Databricks Data & AI Summit 2026 Takeaways | AtScale</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Agent Clouds`, `#Databricks`, `#Infrastructure`

---

<a id="item-6"></a>
## [Porting Moebius 0.2B Image Inpainting Model to Browser with WebGPU](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 9.2/10

Simon Willison successfully ported the Moebius 0.2B image inpainting model from PyTorch/CUDA to run entirely in the browser using WebGPU, and he released a working demo at simonw.github.io/moebius-web/. This demonstrates that even moderately sized models (0.2B parameters) can be run efficiently client-side, reducing reliance on server GPUs and enabling private, low-latency AI applications in the browser. The port used ONNX Runtime Web with the WebGPU backend, not the higher-level Transformers.js library. Simon also used Claude Code as an AI coding agent to assist in the porting process, documenting the approach in a research note.

rss · Simon Willison · Jun 22, 23:43

**Background**: Image inpainting is a technique where missing or selected regions of an image are filled in by a model that predicts plausible content. The Moebius model is a lightweight 0.2B parameter framework that claims performance comparable to 10B parameter models. WebGPU is a modern web API that allows access to GPU acceleration from the browser, enabling machine learning inference without server-side infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/22/porting-moebius/">Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code</a></li>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page</a></li>
<li><a href="https://news.ycombinator.com/item?id=48630171">Moebius: 0.2B image inpainting model with 10B-level performance | Hacker News</a></li>

</ul>
</details>

**Discussion**: On Hacker News, the discussion noted that the original model weights are in fp32, and commenters wondered if lower precision (fp16) could be used. Overall, the port was well-received as a practical demonstration of browser-based AI inference.

**Tags**: `#AI`, `#image inpainting`, `#WebGPU`, `#browser inference`, `#machine learning`

---

<a id="item-7"></a>
## [CUGA: Open-source harness for building agentic apps with 24 examples](https://huggingface.co/blog/ibm-research/cuga-apps) ⭐️ 9.2/10

IBM Research released CUGA, an open-source agent harness, along with two dozen working examples on GitHub that demonstrate building LLM-based agents. The framework handles orchestration, planning, tool execution, state management, and guardrails, so developers only need to define tools and prompts. This significantly lowers the barrier for developers to create production-ready AI agents by providing a configurable, enterprise-grade framework. It could accelerate the adoption of agentic systems in real-world applications across industries. CUGA includes a supervisor, agents, and a policy layer, and has been validated on public benchmarks and real-world deployments. The two dozen examples range from simple chatbots to multi-agent workflows, all built on a lightweight harness.

rss · Hugging Face Blog · Jun 23, 12:51

**Background**: CUGA stands for Configurable Generalist Agent, an open-source project by IBM Research. It handles the complex infrastructure for AI agents—planning, execution loops, tool calls, state management—allowing developers to focus on defining tools and prompts. The harness is configurable and designed for enterprise use.

<details><summary>References</summary>
<ul>
<li><a href="https://cuga.dev/">CUGA — Configurable Generalist Agent · Agent Harness for the enterprise</a></li>
<li><a href="https://huggingface.co/blog/ibm-research/cuga-apps">Build real agentic apps using CUGA: two dozen working examples on a lightweight harness</a></li>
<li><a href="https://github.com/cuga-project/cuga-apps">GitHub - cuga-project/cuga-apps: A showcase of conversational ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#CUGA`, `#LLM applications`, `#agentic systems`, `#Hugging Face`

---

<a id="item-8"></a>
## [OpenAI Unveils First Custom AI Chip Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI and Broadcom announced Jalapeño, a custom AI inference chip designed for large language model workloads, with manufacturing by TSMC and production achieved in nine months. Jalapeño could reduce inference costs by approximately 50% compared to typical AI GPUs, potentially lowering the cost of serving ChatGPT and other AI services, and signals OpenAI's move to vertically integrate hardware to optimize performance and scale. The chip was designed from the ground up by OpenAI and brought to production with Broadcom, using OpenAI's own models to accelerate parts of the design process; Broadcom CEO Hock Tan reported cost savings of roughly 50% compared with standard AI GPUs.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors designed to run trained machine learning models efficiently, as opposed to training chips. Large language models like GPT-4 require massive computational resources for inference, driving demand for custom silicon that can deliver higher throughput and lower latency at lower cost.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI unveils first chip as part of Broadcom deal in effort to 'build the full stack'</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>

</ul>
</details>

**Discussion**: Some commenters were skeptical about OpenAI's claim that its models accelerated chip design, calling it potentially vague marketing, while others confirmed TSMC as the manufacturer and speculated on chip architecture, including burning weights into silicon for extreme efficiency, and compared Jalapeño to Taalas' approach of etching models directly into hardware.

**Tags**: `#AI`, `#hardware`, `#inference`, `#chips`, `#OpenAI`

---

<a id="item-9"></a>
## [Nub: Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 8.8/10

Colin McDonnell, creator of Zod and former Bun engineer, has released Nub, a Node.js toolkit that augments stock Node with Bun-like features. It uses a --require preload hook to inject an oxc-powered transpiler and polyfills for APIs like Worker and Temporal. Nub provides Bun's developer experience without requiring a separate runtime, allowing Node.js users to leverage fast transpilation and modern APIs. It could streamline Node.js tooling and reduce fragmentation by offering an additive, backward-compatible approach. Nub uses Node's --require flag for preloading rather than the newer --import, which surprised some commenters regarding ESM support. The transpiler is powered by oxc, a high-performance Rust-based JavaScript tooling collection, packaged as a Node-API add-on for speed.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Node.js is a JavaScript runtime built on Chrome's V8 engine, commonly used for server-side development. Bun is a newer runtime aiming for speed and built-in tooling like transpilation and package management. Nub bridges the gap by adding similar features to Node.js via preload hooks, which allow injecting code before the main application runs. Oxc is a collection of high-performance JavaScript tools written in Rust, and Temporal is a modern JavaScript API for date/time handling that replaces the legacy Date object.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal">Temporal - JavaScript | MDN</a></li>

</ul>
</details>

**Discussion**: Commenters were generally positive, praising the idea and the author's credibility as Zod's creator. Some noted surprise at the use of --require instead of --import for ESM support, while others reported successful migrations with zero issues.

**Tags**: `#Node.js`, `#developer tools`, `#Bun`, `#transpiler`, `#module resolution`

---

<a id="item-10"></a>
## [Debate grows on removing GitHub dependency for Rust crates.io publishing](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 8.8/10

Community members and Rust project participants are discussing the desire and ongoing work to decouple publishing Rust crates on crates.io from GitHub, with a recently merged RFC and implementation starting. This matters because tying crates.io publishing to GitHub creates a single point of failure and raises concerns about centralization in the Rust ecosystem; decoupling would improve resilience and align with open-source decentralization goals. An RFC (Pull Request #3963) was recently merged to unblock this effort, but implementation is still in early stages and faces challenges due to limited volunteer and funding resources.

hackernews · speckx · Jun 24, 19:40 · [Discussion](https://news.ycombinator.com/item?id=48664733)

**Background**: Crates.io is the official Rust package registry, similar to npm for JavaScript or PyPI for Python. Currently, publishing a crate often requires a GitHub account and repository, as the system is tightly integrated with GitHub for authentication and CI. This has been a long-standing issue tracked in the crates.io repository (issue #326).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crates.io">Crates.io</a></li>
<li><a href="https://crates.io/">crates.io: Rust Package Registry</a></li>

</ul>
</details>

**Discussion**: Community sentiment is broadly supportive of decoupling, but many acknowledge the difficulty of the task, comparing it to 'rebuilding the track while the train is driving.' Volunteers and maintainers note that boring or uninteresting tasks depend on funding, and contributions are welcome. Some also argue that publishing should not depend on any single internet property, including crates.io itself.

**Tags**: `#rust`, `#crates.io`, `#github`, `#dependency`, `#open-source`

---

<a id="item-11"></a>
## [NVIDIA NeMo AutoModel Accelerates Transformer Fine-Tuning](https://huggingface.co/blog/nvidia/accelerating-fine-tuning-nvidia-nemo-automodel) ⭐️ 8.7/10

NVIDIA introduced NeMo AutoModel, an open-source PyTorch DTensor-native library that automates model selection and optimization to accelerate fine-tuning of transformer models. This simplifies and speeds up fine-tuning for AI practitioners, reducing the need for manual hyperparameter tuning and model selection, thereby lowering the barrier to deploying customized LLMs, VLMs, and diffusion models. NeMo AutoModel is designed for distributed training with SPMD parallelism, supporting LLMs, VLMs, diffusion models, and retrieval models. It can be installed via PyPI, Docker, or from source, and includes a lightweight CLI for login-node installs.

rss · Hugging Face Blog · Jun 24, 16:00

**Background**: Fine-tuning large transformer models traditionally requires significant manual effort to select the right architecture and optimize hyperparameters. NeMo AutoModel automates these steps using techniques like Bayesian optimization, making the process more efficient. NVIDIA NeMo is a framework for building and deploying generative AI models, and AutoModel extends its capabilities for automated fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/nemo/automodel/latest/index.html">NeMo AutoModel Documentation — NeMo-AutoModel</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Automodel">GitHub - NVIDIA-NeMo/Automodel: Pytorch Distributed native ...</a></li>
<li><a href="https://docs.nvidia.com/nemo/automodel/latest/guides/installation.html">Install NeMo AutoModel - NVIDIA Documentation Hub</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#fine-tuning`, `#NVIDIA`, `#NeMo`, `#Hugging Face`

---

<a id="item-12"></a>
## [NVIDIA 45°C Liquid Cooling Slashes Data Center Water Use](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.5/10

NVIDIA has introduced a 45°C liquid cooling design for its Rubin-generation AI data centers, nearly eliminating water consumption by using higher-temperature coolant to avoid evaporative cooling. This innovation could significantly reduce the environmental impact of AI infrastructure, saving hyperscale facilities over $4 million annually in water costs and enabling more sustainable data center growth. The design is part of NVIDIA's Vera Rubin platform, which is the world's first 100% liquid-cooled AI server architecture running at 45°C with zero fans, and mass production is scheduled to begin in autumn 2026.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers use evaporative cooling, which consumes large amounts of water. Liquid cooling circulates coolant to absorb heat, but typically requires lower temperatures. NVIDIA's 45°C approach allows heat rejection without water evaporation, enabling near-zero water consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://techstory.in/the-45c-breakthrough-nvidias-liquid-cooling-architecture-solves-data-center-water-crisis/">NVIDIA Liquid Cooling Design Cuts Water to Near Zero - TechStory</a></li>
<li><a href="https://icharles.com/articles/nvidia-rubin-45c-liquid-cooling-zero-water">NVIDIA Rubin: 45°C Cooling, Near-Zero Water - iCharles</a></li>

</ul>
</details>

**Discussion**: Some commenters questioned what the actual innovation is, noting that higher-temperature liquid cooling has been used before. Others discussed the potential for district heating, noting that 45°C is usable for community heating loops, providing additional value.

**Tags**: `#data center cooling`, `#liquid cooling`, `#water conservation`, `#AI infrastructure`, `#NVIDIA`

---

<a id="item-13"></a>
## [DeepMind's Gemini 3.5 Flash Gains Computer Use Abilities](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) ⭐️ 8.5/10

DeepMind announced computer use capabilities in Gemini 3.5 Flash, allowing the model to interact with graphical user interfaces (GUIs) like a human—clicking, typing, and navigating. This enables Gemini to automate complex desktop tasks end-to-end, competing directly with Anthropic's similar computer use feature in Claude, and opens new possibilities for AI-driven workflow automation. The blog post shares benchmark scores where Gemini 3.5 Flash performs well on computer use tasks but some community members noted it lags behind Anthropic's Opus 4.8 and GPT 5.5 on certain graphs. The feature is likely still experimental.

rss · DeepMind Blog · Jun 24, 16:30

**Background**: Computer use refers to an AI capability that allows language models to control computer interfaces—clicking buttons, typing text, navigating menus. Anthropic pioneered this with Claude, and now DeepMind follows. It enables AI agents to perform tasks that require interacting with software applications.

<details><summary>References</summary>
<ul>
<li><a href="https://promptwatch.com/glossary/computer-use">Computer Use - AI SEO & GEO Glossary | Promptwatch</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2024/12/anthropic-computer-use/">Anthropic Computer Use : AI Assistant Taking Over Your Computer</a></li>
<li><a href="https://theoutpost.ai/news-story/anthropic-unveils-groundbreaking-computer-use-ai-for-autonomous-task-performance-7482/">Anthropic Unveils Groundbreaking ' Computer Use ' AI for Autonomous...</a></li>

</ul>
</details>

**Discussion**: The community expressed mixed reactions. Some users reported frustration with Gemini's error-prone performance and overly cautious guardrails, while others doubted the screenshot-based approach compared to direct API integration or accessibility trees. A skeptical comment highlighted that benchmark graphs seemed misleadingly favorable to Gemini.

**Tags**: `#AI`, `#LLM`, `#Gemini`, `#computer use`, `#DeepMind`

---

<a id="item-14"></a>
## [Memory Chip Makers' Regret and Microsoft's China AI Incentive](https://stratechery.com/2026/memory-chips-and-china-microsoft-and-chinese-models/) ⭐️ 8.5/10

The three major memory chip manufacturers (Samsung, SK Hynix, Micron) may regret enabling Chinese competitors, while Microsoft has strong incentives to adopt Chinese AI models. This analysis highlights strategic missteps in the memory chip industry and Microsoft's potential pivot towards Chinese AI, which could reshape global tech supply chains and raise geopolitical concerns. The 'big three' memory makers have historically dominated the market, but Chinese firms like YMTC gained technology through partnerships. Microsoft's incentives likely include lower costs from Chinese models and access to the Chinese market.

rss · Stratechery · Jun 23, 10:00

**Background**: Memory chips are essential components in electronics, and the industry is a strategic sector. Chinese companies have been rapidly advancing with government support. Microsoft, as a leading AI platform, may choose Chinese AI models to reduce costs or comply with local regulations.

**Tags**: `#Memory Chips`, `#China`, `#Microsoft`, `#AI Models`, `#Geopolitics`

---

<a id="item-15"></a>
## [Ben Thompson's Vibe Coding Takeaways](https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/) ⭐️ 8.4/10

Ben Thompson shares ten key takeaways from his personal experience of vibe coding an app he intends to use regularly. This provides practical insights from a respected tech analyst on a rapidly emerging AI-assisted development practice, offering valuable lessons for both novice and experienced developers. The post is based on Thompson's own hands-on experience building a real app, not theoretical advice, and it highlights both successes and challenges encountered during the process.

rss · Stratechery · Jun 24, 10:00

**Background**: Vibe coding is a software development practice where a developer describes a project or task in a natural language prompt to an AI large language model, which generates source code automatically. The term was coined in February 2025 by Andrej Karpathy, a co-founder of OpenAI and former AI leader at Tesla. It has gained popularity for enabling amateur programmers to produce software without extensive training, but critics warn of reduced accountability, maintainability, and increased security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://grokipedia.com/page/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**Tags**: `#vibe coding`, `#AI-assisted development`, `#software engineering`, `#app development`, `#personal experience`

---

<a id="item-16"></a>
## [Hugging Face Launches FFASR Leaderboard for Real-World ASR](https://huggingface.co/blog/ffasr-leaderboard) ⭐️ 8.0/10

Hugging Face, in partnership with Treble Technologies, has launched the Far Field ASR (FFASR) Leaderboard, the first open, community-driven benchmark designed to evaluate automatic speech recognition models under realistic, far-field conditions. Traditional ASR benchmarks often use clean audio, failing to reflect real-world challenges like background noise and reverberation. The FFASR Leaderboard addresses this gap, enabling more accurate comparisons of model robustness and driving improvements for practical applications. The leaderboard evaluates models across nine distinct acoustic conditions, with four of them — including varying degrees of reverberation and noise — determining the primary ranking score. The dataset incorporates diverse RT60 profiles to test model robustness.

rss · Hugging Face Blog · Jun 24, 00:00

**Background**: Automatic speech recognition (ASR) converts spoken language into text. In real-world settings, microphones often pick up sound from a distance (far-field), introducing reverberation and noise. Traditional benchmarks like LibriSpeech use clean, close-talk audio, which does not reflect these challenges. The FFASR Leaderboard uses a dataset specifically designed to include far-field conditions, providing a more realistic test.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huggingface/blog/blob/main/ffasr-leaderboard.md">blog/ ffasr -leaderboard.md at main · huggingface/blog · GitHub</a></li>
<li><a href="https://www.mlhive.com/2026/06/how-ffasr-leaderboard-redefines-speech-recognition-testing">How the New FFASR Leaderboard Redefines Speech... — ML Hive</a></li>
<li><a href="https://icymi.in/article/treble-technologies-and-hugging-face-address-benchmark-of-automatic-speech-recognition-models">Treble Technologies and Hugging Face Address Benchmark of...</a></li>

</ul>
</details>

**Tags**: `#Automatic Speech Recognition`, `#Benchmarking`, `#Hugging Face`, `#AI Tooling`, `#Real-world ASR`

---

<a id="item-17"></a>
## [Experimenting with Cross-Origin Storage API for Transformers.js](https://huggingface.co/blog/cross-origin-storage) ⭐️ 8.0/10

Hugging Face blog explores the proposed Cross-Origin Storage API for Transformers.js, enabling browsers to share AI model files across origins, reducing redundant downloads and supporting offline client-side AI inference. This could significantly improve load times and bandwidth efficiency for web-based AI applications, making client-side inference more practical for large models and opening up new possibilities for offline AI experiences in the browser. The API is a proposal under the WICG and provides a secure mechanism for storing and retrieving large files across origins, applicable to AI models, WebAssembly modules, and JavaScript libraries.

rss · Hugging Face Blog · Jun 23, 00:00

**Background**: Transformers.js allows running pretrained models directly in the browser via JavaScript, similar to Hugging Face's Python transformers library. However, downloading large model files for each origin leads to redundant data transfer. The Cross-Origin Storage API addresses this by enabling shared storage across different web origins, reducing bandwidth usage and enabling offline capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://wicg.github.io/cross-origin-storage/">Explainer for the Cross-Origin Storage (COS) API | cross ...</a></li>
<li><a href="https://explore.n1n.ai/blog/cross-origin-storage-api-transformers-js-2026-06-24">Exploring the Cross-Origin Storage API for Transformers.js</a></li>
<li><a href="https://www.welcome.ai/content/cross-origin-storage-api-enhances-resource-management-for-web-applications">Cross-Origin Storage API Enhances Resource Management for Web ...</a></li>

</ul>
</details>

**Tags**: `#Transformers.js`, `#Cross-Origin Storage`, `#Browser-based AI`, `#Web Machine Learning`, `#Hugging Face`

---

<a id="item-18"></a>
## [Claude Slack Integration Gets Multiplayer, Proactive, Persistent Agents](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 8.0/10

Anthropic has upgraded Claude's Slack integration to support multiplayer, proactive, and persistent agent behaviors, enabling teams to collaborate with AI directly in Slack. This advancement transforms team productivity by allowing multiple users to simultaneously interact with a persistent Claude agent that proactively engages in tasks, streamlining workflows and reducing context switching. The upgrade introduces multiplayer capabilities for concurrent user interactions, proactive behaviors where the agent initiates conversations, and persistent memory across sessions. This builds on Claude's existing Slack integration, providing a more autonomous and collaborative AI assistant.

rss · Latent Space · Jun 24, 07:14

**Background**: Claude is a family of large language models developed by Anthropic, known for its constitutional AI training approach. The Slack integration allows teams to leverage Claude for tasks like answering questions, generating content, and automating workflows directly within the communication platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://www.linkedin.com/posts/craighosang_introducing-multiplayer-ai-agents-activity-7184633394926931968-_MyD">Craig Hosang on LinkedIn: Introducing Multiplayer AI Agents</a></li>
<li><a href="https://argybargy.dev/">Argybargy — a peer-to-peer bridge for AI agents</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#Slack`, `#AI agents`, `#productivity`, `#Anthropic`

---

<a id="item-19"></a>
## [LLMs Confuse System Tags with User Input, Enabling Jailbreaks](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 7.8/10

A new paper by Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell reveals that LLMs cannot reliably distinguish between privileged role tags (e.g., <system>) and untrusted user input, leading to effective jailbreak attacks via 'role confusion'. This research highlights a fundamental flaw in LLM security, showing that current prompt injection defenses are likely to be a 'perpetual whack-a-mole game' until models achieve genuine role perception. It impacts the safety and reliability of AI systems deployed in untrusted environments. The paper found that simply 'destyling' user text—rewriting it to look less like a model's internal role format—reduced attack success rates from 61% to 10%. Models appear to prioritize the style of the text over its actual role tags, enabling jailbreaks like tricking the model into overriding its training with a green-shirt policy.

rss · Simon Willison · Jun 22, 23:59

**Background**: Prompt injection is a type of attack where malicious user input tricks an LLM into ignoring its system instructions. In many LLM architectures, system prompts, user inputs, and assistant responses are wrapped in role tags like <system>, <user>, and <assistant> to help the model distinguish them. However, LLMs lack a true understanding of these roles; they rely on patterns in the text. This paper formalizes 'role confusion' as the root cause of prompt injection and demonstrates attacks that exploit stylistic mimicry.

<details><summary>References</summary>
<ul>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>
<li><a href="https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/">Prompt Injection as Role Confusion - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#prompt injection`, `#jailbreak`, `#security`

---

<a id="item-20"></a>
## [Bunny DNS Becomes Free for Up to 500 Domains](https://bunny.net/blog/were-making-bunny-dns-free/) ⭐️ 7.7/10

Bunny DNS has eliminated all DNS query fees and now offers free DNS hosting for up to 500 domains per account, with no query limits or hidden charges. This positions Bunny DNS as a strong European alternative to Cloudflare and other DNS providers, potentially attracting users seeking EU-based services amid geopolitical tensions. The free tier includes smart records, health monitoring, and scriptable DNS records, with no critical features gated behind enterprise plans.

hackernews · dabinat · Jun 24, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48657030)

**Background**: DNS (Domain Name System) translates human-readable domain names into IP addresses, essential for internet browsing. Bunny DNS is a scriptable DNS platform from Bunny.net, a private EU-based company with minimal venture capital funding, focusing on organic growth.

<details><summary>References</summary>
<ul>
<li><a href="https://bunny.net/dns/">Bunny DNS | The #1 Scriptable DNS Platform | bunny .net</a></li>
<li><a href="https://euroalternative.eu/bunny-dns">Bunny DNS : European Alternative to Amazon Route 53 and...</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcomed the free offering as a step toward EU-based alternatives to Cloudflare, though some expressed concerns about potential unexpected costs from LLM crawlers and lack of billing caps on non-CDN products.

**Tags**: `#DNS`, `#CDN`, `#Cloudflare Alternative`, `#EU Tech`, `#Free Service`

---

<a id="item-21"></a>
## [Web data infrastructure layer emerges for AI models](https://www.technologyreview.com/2026/06/24/1139202/the-emergence-of-the-web-data-infrastructure-layer-for-ai/) ⭐️ 7.6/10

A new web data infrastructure layer is emerging to make web data accessible and usable for AI models, addressing the challenge that the web was not designed for machine consumption. This development is significant because enterprises need scalable data to capitalize on AI, and currently much web data is unstructured or blocked, limiting AI model utility. The web data infrastructure layer includes processes, standards, and validation layers that transform raw web data into AI-ready formats, as highlighted in recent guides.

rss · MIT Tech Review · Jun 24, 11:59

**Background**: The web was originally designed for human readers, not for automated data extraction. AI models require clean, structured data at scale, which often involves scraping, cleaning, and organizing web data. A dedicated infrastructure layer can automate and standardize these steps.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/24/1139202/the-emergence-of-the-web-data-infrastructure-layer-for-ai/">The emergence of the web data infrastructure layer for AI</a></li>
<li><a href="https://www.promptcloud.com/blog/ai-ready-web-data-infrastructure-2025/">AI-Ready Web Data Infrastructure Guide for 2025</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#web data`, `#data engineering`, `#enterprise AI`

---

<a id="item-22"></a>
## [Claude Code v2.1.187: Sandbox Credentials, Model Restrictions, Mouse Support](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) ⭐️ 7.5/10

Anthropic released v2.1.187 of its Claude Code CLI, adding a sandbox.credentials setting to block credential leaks, org-configured model restrictions, and mouse click support for select menus in fullscreen mode. This release enhances security by preventing sandboxed commands from accessing sensitive credentials, and gives organizations more control over model usage. The mouse support and numerous bug fixes improve developer experience with Claude Code. Notable fixes include resolving `--resume` failures, fixing structured output loops in `StructuredOutput`, and aborting MCP tool calls that hang for 5 minutes (configurable via `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`). Also fixed Korean/CJK text mojibake in terminals and improved agent stop notifications.

github · ashwin-ant · Jun 23, 21:03

**Background**: Claude Code is Anthropic's CLI tool for interacting with their LLM in a terminal environment. The Model Context Protocol (MCP) is an open standard by Anthropic that standardizes how AI systems connect to external tools and data sources. Sandbox credentials refer to the environment variables and credential files that sandboxed commands might inadvertently expose.

<details><summary>References</summary>
<ul>
<li><a href="https://vibecodedthis.com/blog/claude-code-2-1-187-sandbox-credentials-org-model-june-2026/">Claude Code 2.1.187: Credential Sandboxing, Org... | VibecodedThis</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI-tooling`, `#dev-tools`, `#release-notes`

---

<a id="item-23"></a>
## [PR spam mirrors early 2000s email spam](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 7.5/10

A Hacker News discussion compares modern pull request spam to early 2000s email spam, highlighting differences and potential solutions like GitHub's configurable PR limits and maintainer verification. This discussion offers practical insights for open-source maintainers struggling with spam, potentially shaping community norms and tooling to protect project quality and reduce maintainer burden. GitHub recently added configurable pull request limits for maintainers, and some projects require new contributors to meet a maintainer non-textually before first PR merge. The discussion also explores differences from email spam, such as lack of server-level reputation for PRs.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: Pull request spam refers to low-quality or automated PRs submitted to open-source projects, often for promotion or link building. Like early email spam, it wastes maintainer time and clogs project queues. The comparison highlights evolving challenges in online community management.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/rest/pulls">REST API endpoints for pull requests - GitHub Docs</a></li>
<li><a href="https://github.com/orgs/community/discussions/43993">I'm the maintainer of a large open source project - how can I get...</a></li>

</ul>
</details>

**Discussion**: Commenters noted key differences from email spam: PR spam lacks server-level reputation, making it harder to block. Some suggested solutions include GitHub's new PR limits, non-textual contributor validation, or a token-based donation system for open-source projects.

**Tags**: `#open source`, `#spam`, `#pull requests`, `#GitHub`, `#maintainer tools`

---

<a id="item-24"></a>
## [Coinbase's lack of automated zone failover](https://blog.pragmaticengineer.com/coinbase-fail/) ⭐️ 7.5/10

An analysis from the Pragmatic Engineer newsletter reveals that Coinbase's global trading service lacks automated zone failover, a critical reliability mechanism. This reliability gap could lead to prolonged outages during a zone failure, affecting millions of traders and undermining trust in the platform. Zone failover automatically redirects traffic to a backup data center when a primary zone fails; Coinbase's absence of this automation means manual intervention is required, increasing downtime risk.

rss · Pragmatic Engineer · Jun 23, 16:30

**Background**: Zone failover is a disaster recovery technique that replicates services and data across geographically separate data centers (zones). When one zone experiences an outage, traffic is automatically rerouted to a healthy zone, ensuring high availability. Major cloud providers and financial platforms typically implement automated failover to meet strict uptime SLAs.

<details><summary>References</summary>
<ul>
<li><a href="https://pantheon.io/features/disaster-recovery">Multizone Failover | Pantheon.io</a></li>

</ul>
</details>

**Tags**: `#reliability`, `#coinbase`, `#failover`, `#infrastructure`, `#engineering-culture`

---

<a id="item-25"></a>
## [RubyLLM: Unified Ruby framework for AI providers](https://rubyllm.com/) ⭐️ 7.3/10

RubyLLM is a Ruby gem that provides a single, beautiful API for interacting with major AI providers like OpenAI, Anthropic, and local models via Ollama, aiming to simplify multi-provider AI development. It addresses the fragmentation of AI provider SDKs in the Ruby ecosystem, allowing developers to switch providers without changing code and reducing vendor lock-in. Its high usability, akin to Vercel's AI framework, makes it a valuable tool for Ruby developers building AI applications. RubyLLM has minimal dependencies (Faraday, Zeitwerk, Marcel) and supports multiple providers. However, known issues include caching failures for some providers (e.g., xAI) and initial lack of native support for responses API, though this may have been addressed. It also poses challenges for observability and tracing.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: The Ruby ecosystem has lacked a unified AI framework compared to JavaScript alternatives like Vercel AI SDK. RubyLLM fills this gap by abstracting provider-specific APIs into a consistent interface. It is designed for building chatbots, AI agents, RAG applications, and more.

<details><summary>References</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI ...</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ruby_llm: One delightful Ruby framework for ...</a></li>

</ul>
</details>

**Discussion**: Community feedback is mostly positive, praising RubyLLM's usability and simplicity. Some users built complementary tools like Raix on top of it. Criticisms include caching issues, incomplete API coverage (e.g., responses API), and difficulty with observability. There is debate on whether a unified framework is beneficial for single-provider use.

**Tags**: `#Ruby`, `#LLM`, `#AI framework`, `#AI providers`, `#developer tools`

---