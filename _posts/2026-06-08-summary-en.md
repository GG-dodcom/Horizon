---
layout: default
title: "Horizon Summary: 2026-06-08 (EN)"
date: 2026-06-08
lang: en
---

> From 83 items, 15 important content pieces were selected

---

1. [Apple Unveils Core AI Framework to Replace Core ML](#item-1) ⭐️ 9.7/10
2. [xAI's GPU leasing makes it a datacenter REIT, not a lab](#item-2) ⭐️ 9.2/10
3. [Xiaomi MiMo-v2.5-Pro-UltraSpeed: 1T model at 1000 tokens/s](#item-3) ⭐️ 9.0/10
4. [AI development slowing, faces $3 trillion revenue gap](#item-4) ⭐️ 9.0/10
5. [Signal: UK Surveillance Proposals Threaten Privacy, Not Safety](#item-5) ⭐️ 8.9/10
6. [Apple unveils AI architecture integrating Google Gemini](#item-6) ⭐️ 8.6/10
7. [Google-SpaceX Deal and Broadcom Outlook Bolster Nvidia's Dominance](#item-7) ⭐️ 8.5/10
8. [Open Source Community Backs OpenEnv for Agentic RL](#item-8) ⭐️ 8.4/10
9. [Users share custom tools built since AI's rise](#item-9) ⭐️ 7.8/10
10. [Study: 2017 BAHA Order Halved H-1B Approvals, Hurt Productivity](#item-10) ⭐️ 7.8/10
11. [Apple Unveils Siri AI, Sparks DMA Debate](#item-11) ⭐️ 7.5/10
12. [Performative-UI: Satirical React Library of Design Tropes](#item-12) ⭐️ 7.3/10
13. [Massachusetts bans sale of precise location data in new privacy bill](#item-13) ⭐️ 7.3/10
14. [Claude Code v2.1.169: Safe Mode, /cd Command, and Bug Fixes](#item-14) ⭐️ 7.1/10
15. [Investigation finds systematic antibody data manipulation at Thermo Fisher](#item-15) ⭐️ 7.1/10

---

<a id="item-1"></a>
## [Apple Unveils Core AI Framework to Replace Core ML](https://developer.apple.com/documentation/coreai/) ⭐️ 9.7/10

Apple announced Core AI at WWDC 2026 as a replacement for Core ML, enabling conversion of PyTorch models to run on CPU, GPU, and Apple Neural Engine. This marks a significant shift toward on-device AI, reducing reliance on cloud-based AI services and enabling faster, private inference. It could reshape the AI industry as companies rush to adapt to local AI. Core AI supports model conversion from PyTorch and optimizes for Apple's hardware. It is available in iOS 27 and later, with related tools like Core AI Optimization and Generative AI Skills.

hackernews · hmokiguess · Jun 8, 18:47 · [Discussion](https://news.ycombinator.com/item?id=48449665)

**Background**: Core ML had been Apple's on-device machine learning framework since 2017, used for tasks like image classification and natural language processing. Core AI is its successor, announced at WWDC 2026, offering improved support for large language models and generative AI on device. On-device AI involves converting models (e.g., from PyTorch) to formats compatible with local runtimes, providing privacy, low latency, and offline capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/core-ai/">Core AI - Apple Developer</a></li>
<li><a href="https://udit.co/blog/apple-core-ai-replaces-core-ml-wwdc-ios-27">Apple replacing Core ML with Core AI at WWDC 2026 changes e</a></li>
<li><a href="https://learn.deeplearning.ai/courses/introduction-to-on-device-ai/lesson/1/introduction">Introduction to on - device AI - DeepLearning. AI</a></li>

</ul>
</details>

**Discussion**: Commenters are excited about the shift to on-device AI, with one arguing that AI companies have no moat and are rushing to IPO before on-device models dominate. Another developer notes that Core AI seems to replace the previous Core ML API and points to WWDC videos for more details. There is general agreement that this move could disrupt cloud AI providers.

**Tags**: `#Apple`, `#AI framework`, `#on-device AI`, `#CoreML`, `#PyTorch`

---

<a id="item-2"></a>
## [xAI's GPU leasing makes it a datacenter REIT, not a lab](https://martinalderson.com/posts/xais-new-rental-business/) ⭐️ 9.2/10

xAI is primarily renting out its massive GPU cluster, named Colossus, to Google and Anthropic, generating an estimated $26 billion in annual revenue, which suggests its core business is infrastructure leasing rather than frontier AI research. This shift highlights a new business model where AI labs become infrastructure providers, potentially distorting market incentives and raising conflicts of interest, especially given Google's stake in SpaceX and the circular deals between these companies. The Colossus cluster operates on on-site gas turbines with a fuel cost of only about $90 million per year, and Google owns 5–6% of SpaceX, creating a circular valuation dynamic where GPU leasing profits boost SpaceX's IPO valuation.

hackernews · martinald · Jun 8, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48446428)

**Background**: GPU clusters are high-performance computing systems with multiple GPUs, essential for training large AI models. A REIT (Real Estate Investment Trust) is a company that owns and operates income-generating real estate, and datacenter REITs specialize in leasing data center space. xAI, founded by Elon Musk, originally focused on developing frontier AI models but now appears to generate most of its revenue from leasing GPU compute capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPU_cluster">GPU cluster</a></li>
<li><a href="https://money.usnews.com/investing/articles/best-data-center-stocks">7 Best Data Center Stocks, ETFs and REITs to Buy | Investing - U.S. News - Money</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the circular deals and valuations, with some noting that the new revenue data should update prior beliefs about xAI's technology quality. Others pointed out the low fuel costs and questioned whether the deals provide enough margin to cover depreciation. There was also a mention that the analysis may have been inspired by a previous HN comment.

**Tags**: `#AI infrastructure`, `#GPU leasing`, `#xAI`, `#business model`, `#data center economics`

---

<a id="item-3"></a>
## [Xiaomi MiMo-v2.5-Pro-UltraSpeed: 1T model at 1000 tokens/s](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) ⭐️ 9.0/10

Xiaomi released MiMo-v2.5-Pro-UltraSpeed, a 1 trillion parameter model achieving 1000 tokens per second inference speed at a shockingly low cost. This breakthrough could significantly reduce AI deployment costs and latency, making large-scale AI applications more practical and accessible, especially for real-time use cases. The model achieves this speed using unknown optimization techniques; the 'UltraSpeed' variant is priced 3x the regular MiMo v2.5 Pro, which is already as cheap as DeepSeek.

hackernews · gainsurier · Jun 8, 15:27 · [Discussion](https://news.ycombinator.com/item?id=48446639)

**Background**: MiMo (Xiaomi MiMo) is a reasoning-focused language model developed by Xiaomi, led by former DeepSeek researcher Luo Fuli. It is used in Xiaomi's 'Human x Car x Home' ecosystem. The model was trained using multi-token prediction techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed both excitement and unease about ultra-fast AI, questioning productivity gains and noting price advantages of Chinese providers. Some highlighted that MiMo v2.5 Pro is the strongest open-weights agentic coding model they've tested, but underappreciated.

**Tags**: `#AI`, `#LLM`, `#Inference`, `#Speed`, `#Xiaomi`

---

<a id="item-4"></a>
## [AI development slowing, faces $3 trillion revenue gap](https://www.wheresyoured.at/ai-is-slowing-down/) ⭐️ 9.0/10

An article argues that AI development is decelerating and that the industry must generate over $3 trillion in revenue by 2030 to sustain itself, questioning its economic viability. This analysis highlights a critical financial risk for the AI industry, suggesting that current investment levels may not be justified by future returns, which could impact funding, jobs, and innovation. The $3 trillion figure is based on the cumulative investment in AI infrastructure and the expected need for revenue to cover costs by 2030. The article claims that model improvements have stagnated, with little progress from last year to this year.

hackernews · crescit_eundo · Jun 8, 15:46 · [Discussion](https://news.ycombinator.com/item?id=48446893)

**Background**: The AI industry has seen massive investment in compute resources and data centers, driven by the promise of transformative AI. However, generating sufficient revenue from AI products and services remains a challenge, leading to concerns about a bubble or shakeout.

**Discussion**: Comments are mixed; some agree that models have not improved much recently, while others criticize the article's tone and logic as overly pessimistic. A few attempt to verify the $3 trillion claim with economic data, noting it is an order of magnitude higher than expected.

**Tags**: `#AI`, `#LLMs`, `#economics`, `#slowdown`, `#sustainability`

---

<a id="item-5"></a>
## [Signal: UK Surveillance Proposals Threaten Privacy, Not Safety](https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf) ⭐️ 8.9/10

Signal published a PDF statement titled 'Surveillance Is Not Safety' arguing that the UK's latest surveillance proposals, including client-side scanning under the Online Safety Act, threaten privacy and are ineffective for safety. This matters because the UK's proposals could set a precedent for weakening encryption globally, affecting the privacy of millions of users on platforms like Signal that rely on strong encryption. The proposal involves client-side scanning, which would scan messages on users' devices before encryption, effectively bypassing end-to-end encryption. Signal argues this creates a backdoor that could be exploited by malicious actors.

hackernews · g0xA52A2A · Jun 8, 19:42 · [Discussion](https://news.ycombinator.com/item?id=48450646)

**Background**: Client-side scanning is a technique where software on a user's device analyzes content (e.g., images or text) before it is encrypted and sent. The UK's Online Safety Act, updated in 2026, mandates such scanning to detect child sexual abuse material (CSAM), but critics argue it undermines encryption and privacy. Encryption backdoors are intentional vulnerabilities that allow third parties to access encrypted data, which security experts widely oppose as they weaken overall security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sectigo.com/root-causes/root-causes-606-what-is-the-uk-online-safety-act">Root Causes 606: What Is the UK Online Safety Act? | Sectigo® Official</a></li>
<li><a href="https://www.theregister.com/2022/10/13/clientside_scanning_csam_anderson?ref=privacy.thenexus.today">Client - side scanning to detect child abuse material harmful</a></li>
<li><a href="https://behindthescreen.uk/britain-admits-defeat-in-controversial-online-safety-bill/">Britain Admits Defeat in Controversial Online Safety Bill</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns that client-side scanning could lead to a slippery slope, starting with CSAM detection and expanding to general surveillance. Some noted that remote attestation and digital identity verification could further erode privacy. Others praised Signal for taking a strong stance quickly.

**Tags**: `#surveillance`, `#privacy`, `#UK`, `#Signal`, `#cybersecurity`

---

<a id="item-6"></a>
## [Apple unveils AI architecture integrating Google Gemini](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) ⭐️ 8.6/10

On June 8, 2026, Apple announced a new AI architecture that integrates Google Gemini models into Apple Intelligence, focusing on on-device processing and privacy via Private Cloud Compute. This move enables Apple to leverage Google's advanced multimodal models while maintaining its privacy-first approach, potentially enhancing Siri and other AI features without compromising user data, and signals a strategic partnership shift in the AI ecosystem. Apple's architecture routes requests between on-device models and Google's Gemini models through a Private Cloud Compute layer, ensuring user data is used only for the immediate request and is not accessible to Apple or Google; outside experts can verify these privacy guarantees.

hackernews · unclefuzzy · Jun 8, 19:14 · [Discussion](https://news.ycombinator.com/item?id=48450142)

**Background**: Apple Intelligence is Apple's suite of AI features powered by its own foundation models and a Private Cloud Compute system that processes requests without storing data. Google Gemini is a family of multimodal large language models capable of handling text, images, audio, and video. Apple's integration likely uses Gemini Pro or Ultra for complex tasks while keeping simple tasks on-device.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini</a></li>
<li><a href="https://grokipedia.com/page/google_gemini">Google Gemini</a></li>

</ul>
</details>

**Discussion**: Community commenters expressed skepticism about the privacy guarantees, with some arguing absolute data isolation is technically impossible. Others questioned which Gemini models are used and how Apple will differentiate from Android. The lack of EU launch drew criticism as a red flag.

**Tags**: `#AI`, `#Apple`, `#Google Gemini`, `#privacy`, `#architecture`

---

<a id="item-7"></a>
## [Google-SpaceX Deal and Broadcom Outlook Bolster Nvidia's Dominance](https://stratechery.com/2026/google-buys-compute-from-spacex-broadcoms-outlook-apples-ai-politics/) ⭐️ 8.5/10

Google has reportedly purchased compute capacity from SpaceX, while Broadcom's earnings outlook suggests strong demand for AI chips, both reinforcing Nvidia's market leadership. This indicates that cloud and satellite compute providers are increasingly reliant on Nvidia's hardware, and Apple's upcoming AI strategy at WWDC could further shape the competitive landscape. The SpaceX deal may involve using Starlink satellites for edge computing or data transport, while Broadcom's custom AI chips are seen as complementary to Nvidia's GPUs.

rss · Stratechery · Jun 8, 10:00

**Background**: Nvidia dominates the AI chip market with its GPUs used for training large language models. SpaceX's Starlink provides low-latency satellite internet, which could be used for distributed computing. Broadcom is a key supplier of networking and custom AI chips.

**Tags**: `#AI`, `#Nvidia`, `#Apple`, `#Broadcom`, `#SpaceX`

---

<a id="item-8"></a>
## [Open Source Community Backs OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl) ⭐️ 8.4/10

Hugging Face and Meta-PyTorch have announced OpenEnv, a community-driven open-source hub and framework providing standardized execution environments for agentic reinforcement learning (RL) training, featuring a Gymnasium-style API and a collection of ready-to-use environments. OpenEnv lowers the barrier for researchers and developers to build and benchmark agentic RL systems by providing reusable, standardized environments, potentially accelerating progress in autonomous AI agents and multi-step reasoning. OpenEnv is still in early stages but offers a unique opportunity for the community to co-create and collaborate; it supports modular Docker-based RL setups with memory-efficient LoRA fine-tuning, achieving up to 6× faster training.

rss · Hugging Face Blog · Jun 8, 00:00

**Background**: Agentic reinforcement learning (RL) focuses on training AI agents that can autonomously plan and execute complex, long-horizon tasks by interacting with dynamic environments and learning from trial-and-error feedback. Unlike traditional RL, agentic RL often involves partially observable states, external tool use, and evolving goals. Standardized environments, akin to Gymnasium for classic RL, have been lacking for agentic AI, making it difficult to compare approaches. OpenEnv aims to fill this gap by providing a common playground and benchmark suite for the community.

<details><summary>References</summary>
<ul>
<li><a href="https://howaiworks.ai/blog/openenv-agentic-execution-environments">OpenEnv: Standard Agent Training Environments | AI Blog | HowAIWorks.ai</a></li>
<li><a href="https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/">The Building Blocks of Agentic AI: From Kernels to Clusters</a></li>
<li><a href="https://inclusionai.github.io/AReaL/tutorial/agentic_rl.html">Agentic Reinforcement Learning — AReaL Documentation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#RL`, `#agentic systems`, `#open source`, `#Hugging Face`

---

<a id="item-9"></a>
## [Users share custom tools built since AI's rise](https://news.ycombinator.com/item?id=48449187) ⭐️ 7.8/10

A Hacker News thread asks users to share tools they have built for themselves since the advent of AI, and the community responds with a diverse range of projects, from AI-augmented web archiving to physical crafts like ceramic molds. This showcases how individuals are leveraging AI not only for digital tools but also for personal, non-digital projects, reflecting a broad impact of AI on creativity and problem-solving across domains. Notable tools include a self-hosted web archiving tool with AI processing pipelines, a database fork (disc.sh) using Svelte, and a VW diagnostic tool built with Claude. Several users emphasize building physical tools over digital ones.

hackernews · aryamaan · Jun 8, 18:22

**Background**: The 'Ask HN' thread on Hacker News is a community-driven space where users ask questions and share insights. Since the rise of large language models and generative AI, many developers have created custom tools to automate tasks or explore new creative avenues. This thread highlights both digital and physical creations, showing that AI's influence extends beyond software.

**Discussion**: Commenters enthusiastically shared personal projects, ranging from AI-augmented archiving pipelines to physical crafts like ceramic molds and jewelry design. Some expressed satisfaction in making physical rather than digital tools, indicating a mix of practical and creative motivations.

**Tags**: `#AI`, `#tools`, `#hackernews`, `#community`, `#programming`

---

<a id="item-10"></a>
## [Study: 2017 BAHA Order Halved H-1B Approvals, Hurt Productivity](https://feeds.feedblitz.com/~/957843797/0/marginalrevolution~How-HighSkill-Immigration-Restrictions-Eroded-Regional-Productivity-Evidence-from-the-BAHA-Executive-Order.html) ⭐️ 7.8/10

A new study using a difference-in-differences framework finds that the 2017 'Buy American, Hire American' executive order, by doubling H-1B denial rates from 7% to 17% (and tripling STEM-specific rejections to 31%), significantly reduced regional productivity in the United States. This provides causal evidence that restricting high-skill immigration can harm economic productivity, challenging the premise that such restrictions protect domestic workers. It has direct implications for tech industry talent policy and overall economic growth. The study analyzes a quasi-experimental policy shock using administrative data on H-1B petitions and regional productivity measures. The analysis controls for various confounding factors, lending credibility to the causal interpretation.

rss · Marginal Revolution · Jun 7, 16:34

**Background**: The 'Buy American, Hire American' executive order, signed by President Trump in April 2017, directed federal agencies to propose reforms to protect US workers, particularly by tightening H-1B visa adjudication. The difference-in-differences method compares changes over time between regions more and less exposed to H-1B dependent firms, mimicking a randomized experiment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jdsupra.com/legalnews/president-biden-revokes-buy-american-2468016/">President Biden Revokes ‘Buy American and Hire American’ Executive ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference-in-differences_method">Difference-in-differences method</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism, with some noting the H-1B cap of 85,000 per year and questioning whether denial rate changes could have large effects, while others supported the paper's findings as consistent with economic theory.

**Tags**: `#economics`, `#immigration`, `#productivity`, `#H1-B`, `#policy`

---

<a id="item-11"></a>
## [Apple Unveils Siri AI, Sparks DMA Debate](https://www.apple.com/apple-intelligence/) ⭐️ 7.5/10

Apple has announced a major AI upgrade to Siri, leveraging large language models to enable more contextual and conversational interactions, but the rollout may be affected by the EU's Digital Markets Act. This move positions Apple to catch up in the AI assistant race, but the DMA restrictions could limit features in the EU, affecting a significant portion of users and raising questions about fairness and interoperability. The new Siri is powered by Apple's on-device and cloud-based LLMs, offering enhanced understanding of personal context and app control. However, the DMA requires Apple to allow third-party AI assistants equal access to system features, which may delay or alter the EU release.

hackernews · 0xedb · Jun 8, 18:17 · [Discussion](https://news.ycombinator.com/item?id=48449084)

**Background**: The Digital Markets Act (DMA) is an EU regulation that designates large tech platforms like Apple as 'gatekeepers' and imposes rules to ensure fair competition, including interoperability and non-discrimination. Large language models (LLMs) are AI systems trained on vast text data to generate human-like text, enabling advanced conversational agents like the new Siri.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets_Act">Digital Markets Act</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed reactions: some appreciated the context-menu integration but felt the improvements were overdue, while others were concerned about DMA restrictions leaving EU users without new features. There was also debate over whether Apple's approach to permissions and privacy adequately addresses third-party AI integration.

**Tags**: `#AI`, `#Siri`, `#Apple`, `#Digital Markets Act`, `#LLM`

---

<a id="item-12"></a>
## [Performative-UI: Satirical React Library of Design Tropes](https://vorpus.github.io/performativeUI/) ⭐️ 7.3/10

A developer released Performative-UI, a satirical React component library that parodies overused UI design tropes like animated loaders, popover prompts, and ASCII art animations. The library sparks reflection on UX culture, highlighting how once-advanced techniques become clichés and how performative design often prioritizes engagement over usability. Published on GitHub Pages as a live demo, the library includes components such as an obnoxious popover, ASCII art animation, and other visual gimmicks. The code is well-made, despite being satirical.

hackernews · lizhang · Jun 8, 14:05 · [Discussion](https://news.ycombinator.com/item?id=48445554)

**Background**: React component libraries are common in front-end development, but this one deliberately implements patterns that many designers now consider overused or annoying. The project comments on trends like 'performative UI' where flashy elements are added not for utility but to signal sophistication.

**Discussion**: Community comments show amusement and agreement that such performative elements are often demanded by clients, even though they detract from simplicity. Some expressed a desire to actually use some components sarcastically, while others joked about missing modern features like IntersectionObserver.

**Tags**: `#react`, `#ui-design`, `#satire`, `#frontend`, `#ux`

---

<a id="item-13"></a>
## [Massachusetts bans sale of precise location data in new privacy bill](https://techcrunch.com/2026/06/08/massachusetts-votes-to-pass-new-privacy-rights-bill-that-bans-sale-of-precise-location-data/) ⭐️ 7.3/10

Massachusetts has passed a privacy rights bill that bans the sale of precise location data, applying to both residents and visitors. The bill is anticipated to have a broad effect on startups that collect, share, and sell location data in the state. This legislation represents a significant step in protecting consumer location privacy, potentially influencing other states to adopt similar measures. It addresses growing concerns about data brokers selling location information that can be used for surveillance, stalking, or targeted misinformation. The ban specifically covers 'precise location data,' which typically refers to GPS coordinates or similar high-accuracy location information. However, community commentators have noted that the term 'sale' could be a loophole, as data could still be exchanged or transferred without a direct monetary transaction.

hackernews · 01-_- · Jun 8, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48448012)

**Background**: Precise location data can reveal sensitive information about individuals, such as visits to medical clinics, political meetings, or places of worship. Data brokers often collect this information from mobile apps and vehicle telematics, then sell it to advertisers, insurers, or even government agencies. Previous incidents, such as General Motors being fined $12.75 million for reselling OnStar location data, have highlighted the need for stronger privacy protections.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/08/massachusetts-votes-to-pass-new-privacy-rights-bill-that-bans-sale-of-precise-location-data/">Massachusetts votes to pass new privacy rights bill that bans sale of...</a></li>
<li><a href="https://www.aclum.org/en/press-releases/cellphone-location-data-used-target-abortion-misinformation-visitors">Cellphone location data used to target... | ACLU Massachusetts</a></li>

</ul>
</details>

**Discussion**: Commenters expressed cautious support, noting that while the bill is progress, the word 'sale' might become a loophole for data exchange. Several raised concerns about vehicle data not being covered, and one argued that the real harm is data collection itself, not just its sale.

**Tags**: `#privacy`, `#location-data`, `#massachusetts`, `#legislation`, `#data-rights`

---

<a id="item-14"></a>
## [Claude Code v2.1.169: Safe Mode, /cd Command, and Bug Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.169) ⭐️ 7.1/10

Anthropic released Claude Code v2.1.169, introducing a --safe-mode flag to disable all customizations for troubleshooting, a /cd command to change directories mid-session without cache loss, and numerous bug fixes. These enhancements improve developer productivity by providing safer troubleshooting paths and more flexible session management, while the extensive bug fixes address performance and stability issues across platforms. The safe-mode flag also supports environment variable CLAUDE_CODE_SAFE_MODE. The /cd command preserves the prompt cache. Additionally, a disableBundledSkills setting and environment variable allow hiding bundled skills and built-in slash commands.

github · ashwin-ant · Jun 8, 21:57

**Background**: Claude Code is Anthropic's AI-powered coding assistant that integrates with the developer's terminal. It supports customizations via CLAUDE.md files, plugins, skills, hooks, and MCP (Model Context Protocol) servers. Skills are reusable instructions that extend Claude's capabilities, and MCP servers allow it to connect to external tools and data sources.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/mcp-connector">MCP connector - Claude API Docs</a></li>
<li><a href="https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9">Complete Guide to CLAUDE . md and AGENTS. md 2026</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#release-notes`, `#AI-tools`, `#developer-tools`

---

<a id="item-15"></a>
## [Investigation finds systematic antibody data manipulation at Thermo Fisher](https://reeserichardson.blog/2026/05/28/how-much-of-thermo-fishers-antibody-data-has-been-manipulated/) ⭐️ 7.1/10

An investigation by fraud-busting scientist Sholto David has revealed systematic manipulation of antibody validation data by Thermo Fisher, a major supplier of antibodies for biomedical research. This undermines research reproducibility, wastes researchers' time and money, and is especially concerning given Thermo Fisher's dominant market position. The discovery highlights ongoing issues with data integrity in the biotech industry. The manipulated data involve antibody specificity and performance claims, which are critical for experiments. Other researchers had previously noted suspicious antibody results from Thermo Fisher but lacked a platform to raise alarms.

hackernews · mhrmsn · Jun 8, 06:56 · [Discussion](https://news.ycombinator.com/item?id=48442075)

**Background**: Antibody validation is the process of confirming that an antibody specifically recognizes its intended target without cross-reactivity. Poor validation contributes to the reproducibility crisis in biomedical research, where many published results cannot be replicated. Vendors like Thermo Fisher play a key role by providing validated reagents, but fraudulent data erodes trust in these products.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bio-rad-antibodies.com/blog/importance-of-antibody-validation.html">The Importance of Antibody Validation | Bio-Rad</a></li>
<li><a href="https://blog.addgene.org/antibodies-101-validation">Antibodies 101: Validation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong agreement that the fraud is obvious and systematic, with some noting they had personally avoided Thermo Fisher antibodies for years. Sholto David was praised for his persistence and prior success uncovering cancer research fraud at Dana-Farber Cancer Institute.

**Tags**: `#scientific fraud`, `#antibody data`, `#Thermo Fisher`, `#data manipulation`, `#biotech`

---