---
layout: default
title: "Horizon Summary: 2026-05-20 (EN)"
date: 2026-05-20
lang: en
---

> From 112 items, 20 important content pieces were selected

---

1. [SpaceX S-1 Reveals $1.25B/Month Compute Deal with Anthropic](#item-1) ⭐️ 9.8/10
2. [OpenAI's o3 model disproves 60-year-old geometry conjecture](#item-2) ⭐️ 9.5/10
3. [Qwen3.7-Max Open-Source LLM Achieves SOTA Non-Hallucination](#item-3) ⭐️ 9.3/10
4. [Railway Builds Agent-Native Cloud with Own-Metal Data Centers](#item-4) ⭐️ 9.3/10
5. [Google I/O 2026: Gemini 3.5 Flash, Omni, Spark Agents, Antigravity 2.0](#item-5) ⭐️ 9.3/10
6. [Google Quietly Fights AI Overview Manipulation via SEO](#item-6) ⭐️ 8.8/10
7. [Google's AI Search Threatens Web Traffic Model](#item-7) ⭐️ 8.7/10
8. [OlmoEarth v1.1: More Efficient Earth Observation Models](#item-8) ⭐️ 8.7/10
9. [SBCL as the Ultimate Assembly Code Breadboard](#item-9) ⭐️ 8.6/10
10. [Mozilla Deprecates Asm.js, WebAssembly Takes Over](#item-10) ⭐️ 8.5/10
11. [Railway's GCP Account Suspension Causes Two-Day Outage](#item-11) ⭐️ 8.5/10
12. [Hugging Face Launches Ettin Reranker Family for RAG](#item-12) ⭐️ 8.5/10
13. [PyCon US 2026: LLM Progress in 5 Minutes](#item-13) ⭐️ 8.4/10
14. [Claude Code v2.1.144 Adds Background Session Resume and Bug Fixes](#item-14) ⭐️ 8.1/10
15. [GitHub confirms 3,800 repos breached via malicious VSCode extension](#item-15) ⭐️ 8.0/10
16. [Disembodied human brains used for drug testing](#item-16) ⭐️ 7.7/10
17. [Ramp accelerates code review using OpenAI Codex](#item-17) ⭐️ 7.7/10
18. [Anthropic's claude-code v2.1.145 released with scripting and telemetry improvements](#item-18) ⭐️ 7.5/10
19. [Fedora Removes Deepin Desktop; Mozilla to Drop asm.js](#item-19) ⭐️ 7.4/10
20. [Google Cloud Blunder Deletes Australian Fund's Infra](#item-20) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [SpaceX S-1 Reveals $1.25B/Month Compute Deal with Anthropic](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 9.8/10

SpaceX's S-1 filing reveals a cloud services agreement with Anthropic where Anthropic will pay $1.25 billion per month for compute capacity on the COLOSSUS and COLOSSUS II supercomputers through May 2029. This deal highlights the immense capital flowing into AI compute infrastructure and the strategic value of large-scale GPU clusters. It also shows competitors (Anthropic and xAI) partnering for compute, reflecting the scarcity of high-end AI training resources. The agreement includes a ramp-up period with reduced fees in May and June 2026, and can be terminated by either party with 90 days' notice. The COLOSSUS clusters were originally built by xAI for training its Grok models, with COLOSSUS II being used for Grok 5.

rss · Simon Willison · May 20, 22:26

**Background**: COLOSSUS is a massive AI supercomputer built by Elon Musk's xAI in Memphis, Tennessee, starting in 2024. It originally contained 100,000 Nvidia GPUs and was later expanded to 200,000 GPUs, making it one of the most powerful AI training systems. SpaceX later took over operation of the clusters and began offering compute services to external customers like Anthropic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/musks-spacex-has-rented-out-access-to-its-supercomputers-220-000-nvidia-gpus-and-300-megawatts-of-ai-compute-power-to-rival-anthropic-musk-says-no-one-set-off-my-evil-detector-antrhropic-also-interested-in-orbital-data-centers">Musk's SpaceX has rented out access to its supercomputer's 220,000 Nvidia GPUs and 300 megawatts of AI compute power to rival Anthropic — Musk says “No one set off my evil detector,” Anthropic also interested in orbital data centers | Tom's Hardware</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**Discussion**: Community comments express surprise at SpaceX's relatively low revenue compared to its valuation, and skepticism about the feasibility of orbital data centers. Some highlight the impressive scale of the deal but question whether SpaceX can make data centers in space profitable, while others note Starlink's strong cash flow supporting AI bets.

**Tags**: `#AI Infrastructure`, `#SpaceX`, `#Anthropic`, `#Compute Cloud`, `#SEC Filing`

---

<a id="item-2"></a>
## [OpenAI's o3 model disproves 60-year-old geometry conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 9.5/10

OpenAI's o3 reasoning model has disproved a long-standing conjecture in discrete geometry, originally posed by Paul Erdős, by finding a counterexample after 60 years of unsolved status. This landmark achievement demonstrates that AI models can contribute to pure mathematical research, potentially accelerating discoveries and challenging the notion that LLMs merely interpolate training data. The disproof was achieved by constructing a counterexample using a combination of pattern recognition and computation, formally verified in the Lean proof assistant.

hackernews · OpenAI Blog · May 20, 19:05 · [Discussion](https://news.ycombinator.com/item?id=48212493)

**Background**: Discrete geometry studies combinatorial properties of finite geometric objects like points, lines, and circles. The disproved conjecture, part of the unit distance problem, asked whether a specific configuration of points always satisfies a certain property. AI models like o3 use chain-of-thought reasoning and can explore vast search spaces, making them suitable for finding counterexamples to long-standing conjectures.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in... | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_geometry">Discrete geometry</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of fascination and measured skepticism. Some see the result as proof that LLMs can genuinely discover new mathematics, while others argue that finding a counterexample is less insightful than proving the original conjecture true. Several commenters note that this milestone was expected, given AI's growing role in coding and combinatorial search.

**Tags**: `#AI`, `#mathematics`, `#LLM reasoning`, `#discrete geometry`, `#OpenAI`

---

<a id="item-3"></a>
## [Qwen3.7-Max Open-Source LLM Achieves SOTA Non-Hallucination](https://qwen.ai/blog?id=qwen3.7) ⭐️ 9.3/10

Qwen3.7-Max, a new open-source large language model, claims state-of-the-art non-hallucination rates, surpassing proprietary models like Claude Code. The model is designed for agentic tasks and is freely available. This release narrows the gap between open-source and proprietary LLMs, offering a viable alternative for developers concerned about cost and limits. Its low hallucination rate is crucial for reliable AI agents in production. The model achieves top scores in the AA-omniscience benchmark, beating Opus 4.7, Gemini 3.1 Pro, and GPT-5.5. It can be deployed locally via llama.cpp or OpenCode for free.

hackernews · kevinsimper · May 20, 10:35 · [Discussion](https://news.ycombinator.com/item?id=48205626)

**Background**: Large language models (LLMs) often generate plausible but incorrect information, known as hallucinations. Open-source models like Qwen aim to match proprietary ones while allowing local deployment for privacy and cost savings. Agentic LLMs can autonomously perform tasks by interacting with tools and environments.

<details><summary>References</summary>
<ul>
<li><a href="https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/">AI Hallucination Rates & Benchmarks in 2026</a></li>
<li><a href="https://www.datacamp.com/blog/llm-agents">LLM Agents Explained: Architecture, Frameworks, and Use Cases</a></li>

</ul>
</details>

**Discussion**: Commenters praised the low hallucination rate and noted that Qwen3.6 already served as a free alternative to Claude Code for simple tasks. Some wished for US-based hosting for production use, while others questioned the benchmark results without comparing to Opus 4.7 or GPT-5.5.

**Tags**: `#Qwen`, `#LLM`, `#AI`, `#Open Source`, `#Agent`

---

<a id="item-4"></a>
## [Railway Builds Agent-Native Cloud with Own-Metal Data Centers](https://www.latent.space/p/railway) ⭐️ 9.3/10

Railway has announced an agent-native cloud platform featuring own-metal data centers, with 3 million users and 100,000 weekly signups, signaling a major shift in AI agent deployment. This platform is designed specifically for AI agents, not humans, potentially transforming how developers build and scale autonomous agent systems, and could reduce reliance on traditional cloud providers. Railway operates its own metal data centers rather than using third-party cloud providers, and reports spending over $200,000 on coding agents, highlighting the demand for agent-native infrastructure.

rss · Latent Space · May 20, 22:42

**Background**: An agent-native cloud is a cloud platform architected for AI agents as primary users, rather than humans. Traditional clouds assume human interactions, but agents require different APIs, billing, and scaling patterns. Railway's use of its own metal (bare metal) servers gives direct hardware control, potentially offering better performance and cost efficiency for agent workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://agentuity.com/blog/agent-native">An Agent - Native Cloud Does Not Mean a Faster Horse — Agentuity</a></li>

</ul>
</details>

**Tags**: `#agent-native`, `#cloud infrastructure`, `#AI`, `#developer tools`, `#scaling`

---

<a id="item-5"></a>
## [Google I/O 2026: Gemini 3.5 Flash, Omni, Spark Agents, Antigravity 2.0](https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash) ⭐️ 9.3/10

At Google I/O 2026, Google DeepMind announced Gemini 3.5 Flash, a faster and cheaper multimodal LLM; Gemini Omni, a conversational video creation model; Spark, a background AI agent that automates tasks across Google apps; and Antigravity 2.0. These announcements signal Google's aggressive push into agentic AI and multimodal video, making advanced AI more accessible and practical for enterprise and consumer use. Gemini 3.5 Flash is optimized for sub-agent deployment and multi-step workflows, offering higher speed and lower cost; Omni provides text-to-video and in-chat editing of 10-second clips; Spark runs as an always-on background agent connecting to Gmail, Docs, and other apps.

rss · Latent Space · May 20, 03:34

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind. Flash models are designed for speed and cost efficiency, while Omni marks Google's entry into AI video generation. Background agents like Spark run continuously to automate tasks without user initiation, representing the next evolution of AI assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_2.5_Flash_Image">Gemini 2.5 Flash Image</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://gemini.google/overview/video-generation/">Gemini Omni – Create & edit videos as easy as having a ...</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gemini-spark-google-24-7-agent">What Is Gemini Spark ? Google's 24/7 Agent That Learns... | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Gemini`, `#Agentic Systems`, `#LLM`

---

<a id="item-6"></a>
## [Google Quietly Fights AI Overview Manipulation via SEO](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results) ⭐️ 8.8/10

Google is quietly implementing countermeasures to prevent SEO poisoners from manipulating its AI-generated search overviews, as reported by BBC Future. This matters because AI overviews, used by millions, are increasingly targeted by threat actors to spread misinformation and scams, undermining trust in AI search. The manipulation techniques include SEO poisoning attacks that have increased 60% in six months, with over 15,000 sites compromised in major campaigns targeting enterprise users.

hackernews · tigerlily · May 20, 10:57 · [Discussion](https://news.ycombinator.com/item?id=48205782)

**Background**: AI Overviews is an AI feature integrated into Google Search that produces AI-generated summaries of search results. SEO poisoning is an evolution of traditional SEO attacks that trick AI models into surfacing malicious content, often by compromising legitimate sites and injecting AI-generated nonsense.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://www.vectra.ai/topics/seo-poisoning">SEO Poisoning Attacks: Detection & Defense</a></li>
<li><a href="https://www.zerofox.com/blog/seo-poisoning-llms/">SEO Poisoning: How Threat Actors Are Tricking AI Models like ChatGPT, Gemini, and CoPilot</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed skepticism about Google's incentives, with one commenter noting that 'truth was never the product' and another doubting Google's ability to fight spam given its historical struggles. Some found the specific example of a fictional hot dog contest less concerning than manipulation of health or financial information.

**Tags**: `#AI`, `#Google`, `#SEO`, `#misinformation`, `#search`

---

<a id="item-7"></a>
## [Google's AI Search Threatens Web Traffic Model](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.7/10

Google is integrating generative AI into its search engine, producing AI-generated summaries (AI Overviews) that reduce the need for users to click through to websites, fundamentally altering the symbiotic traffic relationship between Google and content creators. This shift could devastate the web ecosystem that relies on Google for traffic, threatening the economic viability of content creation and consolidating Google's power as a gatekeeper of information. Google's AI Overviews produce a snapshot of key information with links, but early implementations have been criticized for inaccuracies and reducing website traffic; the feature is an evolution of the Search Generative Experience (SGE) launched in May 2023.

hackernews · cdrnsf · May 20, 21:33 · [Discussion](https://news.ycombinator.com/item?id=48214449)

**Background**: Historically, websites allowed Google to crawl their content in exchange for referral traffic via search results. Google's AI-generated answers bypass this traffic loop, as users get answers directly on the search results page, reducing incentives for websites to remain open to crawling. This threatens the open web's content creation model, which many rely on for revenue.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://www.semrush.com/blog/google-sge/">Google SGE: Google Search Generative Experience Explained</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/generative-ai-search/">How Google is improving Search with Generative AI</a></li>

</ul>
</details>

**Discussion**: Commenters express concern that AI search will concentrate profits among large corporations while preventing individual creators from monetizing their work. Some debate whether Google's move is worse than competitors like Perplexity doing the same, while others call for decentralized traffic alternatives reminiscent of StumbleUpon. A website owner reports seeing increased views but worries about inaccurate AI summaries harming their site.

**Tags**: `#Google`, `#AI Search`, `#Web Ecosystem`, `#Tech Monopoly`, `#Content Creation`

---

<a id="item-8"></a>
## [OlmoEarth v1.1: More Efficient Earth Observation Models](https://huggingface.co/blog/allenai/olmoearth-v1-1) ⭐️ 8.7/10

OlmoEarth v1.1 is a new family of remote sensing models that reduces compute costs by up to 3x while maintaining performance comparable to OlmoEarth v1. This efficiency makes large-scale satellite mapping faster and cheaper to run, enabling more partners to use the OlmoEarth platform and advancing geospatial analytics. OlmoEarth v1.1 models are encoder-decoder vision transformers trained via masked image modeling, offering up to 3x cost reduction without sacrificing performance.

rss · Hugging Face Blog · May 19, 18:38

**Background**: Earth observation models analyze satellite imagery for tasks like land use classification and change detection. Vision transformers (ViTs) are a neural network architecture that processes images as sequences of patches, and masked image modeling is a pretraining method where parts of an image are hidden and the model learns to reconstruct them.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/allenai/olmoearth-v1-1">OlmoEarth v1.1: A more efficient family of Earth observation models</a></li>
<li><a href="https://allenai.org/blog/olmoearth-v1-1">OlmoEarth v1.1: A more efficient family of models | Ai2</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Earth Observation`, `#Model Efficiency`, `#Remote Sensing`, `#Hugging Face`

---

<a id="item-9"></a>
## [SBCL as the Ultimate Assembly Code Breadboard](https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/) ⭐️ 8.6/10

This 2014 article demonstrates using SBCL's macro system to generate and optimize x86_64 assembly code for a virtual machine, effectively turning Lisp into a macro-assembler. It highlights the metaprogramming power of Common Lisp, allowing developers to write high-level code that produces low-level assembly, improving performance and flexibility for system-level programming. The author used eight x86_64 registers as VM stack slots and meticulously calculated instruction padding and alignment, showing how Lisp macros simplify tedious assembly tasks.

hackernews · yacin · May 20, 15:39 · [Discussion](https://news.ycombinator.com/item?id=48209558)

**Background**: SBCL (Steel Bank Common Lisp) is a high-performance Common Lisp compiler. Its macro system allows code transformations at compile time, enabling domain-specific languages and code generation. This article explores using those macros to write an assembler for a custom VM, leveraging Lisp's uniform syntax for metaprogramming.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sbcl/sbcl/blob/master/src/compiler/x86-64/macros.lisp">sbcl / macros .lisp at master · sbcl / sbcl · GitHub</a></li>
<li><a href="https://rosettacode.org/wiki/Metaprogramming">Metaprogramming - Rosetta Code</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters have appreciated the article's depth across multiple repostings. Some find it challenging but admire the technique, with one commenter noting related work on sb-simd for SIMD programming.

**Tags**: `#SBCL`, `#Common Lisp`, `#assembly`, `#metaprogramming`, `#low-level programming`

---

<a id="item-10"></a>
## [Mozilla Deprecates Asm.js, WebAssembly Takes Over](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.5/10

Mozilla officially deprecated asm.js in a SpiderMonkey blog post on May 20, 2026, marking the end of a pioneering technology that enabled near-native performance in the browser via a JavaScript subset. This deprecation signals the full industry transition to WebAssembly, which offers more efficient binary format and broader support, impacting developers who previously relied on asm.js for high-performance web applications. Asm.js is a strict subset of JavaScript designed for ahead-of-time compilation, but WebAssembly surpasses it in load time, bundle size, and parsing efficiency; future SpiderMonkey versions will not prioritize asm.js optimization.

hackernews · eqrion · May 20, 12:01 · [Discussion](https://news.ycombinator.com/item?id=48206340)

**Background**: Asm.js, introduced by Mozilla in 2013, is a low-level subset of JavaScript that allows C/C++ code to run in browsers with near-native speed by enabling ahead-of-time compilation. It was a response to Google's NaCl and PNaCl technologies. WebAssembly (Wasm), a binary instruction format standardized by the W3C, was launched in 2017 and has since become the preferred method for running high-performance code on the web, offering smaller file sizes and faster parsing than asm.js.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">asm . js - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Games/Tools/asm.js">asm . js - Game development | MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly | MDN</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of nostalgia and recognition of progress: users recall asm.js's role in pioneering projects like Figma and Unreal Engine, while also acknowledging WebAssembly's superiority. Several comments reference Gary Bernhardt's 2014 talk 'The Birth and Death of JavaScript,' noting how prescient it was about the evolution of web assembly.

**Tags**: `#asm.js`, `#WebAssembly`, `#SpiderMonkey`, `#web performance`, `#web standards`

---

<a id="item-11"></a>
## [Railway's GCP Account Suspension Causes Two-Day Outage](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) ⭐️ 8.5/10

Railway published a postmortem detailing a two-day outage caused by an unexpected suspension of its Google Cloud (GCP) account, highlighting the risks of single-cloud dependency. This incident underscores the fragility of relying on a single cloud provider, especially with GCP's aggressive account suspension policies. It serves as a cautionary tale for any business running critical infrastructure on GCP. The outage lasted approximately 48 hours, and Railway is now planning to remove Google Cloud from its data plane's hot path, keeping it only for secondary failover purposes.

hackernews · 0xedb · May 20, 08:37 · [Discussion](https://news.ycombinator.com/item?id=48204770)

**Background**: Railway is a cloud deployment platform (PaaS) that allows developers to deploy applications by connecting a GitHub repository. Single-cloud dependency occurs when an organization relies solely on one cloud provider for all computing needs, which introduces risks such as outages, vendor lock-in, and limited redundancy.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.railway.com/platform">Platform | Railway Docs</a></li>
<li><a href="https://www.pulsant.com/knowledge-hub/blog/single-cloud-dependency-is-a-disaster-waiting-to-happen">Single-Cloud Dependency Is a Disaster Waiting to Happen</a></li>

</ul>
</details>

**Discussion**: Commenters criticized GCP's account suspension practices, with some stating that Google can no longer be trusted as a B2B provider. Others noted that the root cause of the flagging remains unexplained, leaving unanswered questions.

**Tags**: `#incident report`, `#GCP`, `#cloud reliability`, `#infrastructure`, `#outage`

---

<a id="item-12"></a>
## [Hugging Face Launches Ettin Reranker Family for RAG](https://huggingface.co/blog/ettin-reranker) ⭐️ 8.5/10

Hugging Face announced the Ettin Reranker Family, a new set of reranking models designed to improve search and retrieval in AI applications, particularly for retrieval-augmented generation (RAG). Rerankers are critical for enhancing the accuracy of RAG systems by refining initial retrieval results, and the Ettin family from a reputable source like Hugging Face could set new performance baselines or offer compelling trade-offs between latency and accuracy. The Ettin Reranker Family likely includes multiple model sizes and variants optimized for different deployment scenarios, though specific technical details are not provided in the summary. The models are hosted on Hugging Face Hub.

rss · Hugging Face Blog · May 19, 00:00

**Background**: Rerankers are cross-encoder models that take a query and a set of candidate documents and output relevance scores. They are used as a second-stage retriever in RAG pipelines to improve the quality of retrieved information, which in turn enhances the factuality and relevance of LLM-generated responses. The BAAI bge-reranker series is a well-known baseline in this space. The Ettin family aims to offer a new option for developers building production RAG systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.mongodb.com/resources/basics/artificial-intelligence/reranking-models">What are Rerankers? | MongoDB</a></li>
<li><a href="https://huggingface.co/BAAI/bge-reranker-base">BAAI/bge-reranker-base · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#rerankers`, `#retrieval-augmented generation`, `#Hugging Face`

---

<a id="item-13"></a>
## [PyCon US 2026: LLM Progress in 5 Minutes](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) ⭐️ 8.4/10

Simon Willison presented annotated slides from his PyCon US 2026 lightning talk, summarizing key LLM developments over the past six months since the November 2025 inflection point. This talk captures the rapid competition among major AI labs, with the 'best' model changing hands five times, highlighting the accelerating pace of LLM innovation, especially in coding capabilities. Willison used his 'pelican riding a bicycle' SVG test to illustrate model differences, and noted that the top model shifted from Claude Sonnet 4.5 to GPT-5.1, Gemini 3, GPT-5.1 Codex Max, and back to Claude Opus in November 2025 alone.

rss · Simon Willison · May 19, 01:09

**Background**: Simon Willison is a well-known Python developer and technology commentator who frequently summarizes AI developments. A lightning talk is a short presentation, typically five minutes, at conferences like PyCon. The annotated presentation tool he built allows adding notes alongside slide images, making slides self-explanatory.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/may/15/annotated-presentations/">Tool : Annotated Presentation Creator | Simon Willison ’s Weblog</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI`, `#PyCon`, `#summary`, `#Simon Willison`

---

<a id="item-14"></a>
## [Claude Code v2.1.144 Adds Background Session Resume and Bug Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) ⭐️ 8.1/10

Anthropic released Claude Code v2.1.144, adding `/resume` support for background sessions and renaming 'extra usage' to 'usage credits'. The release also fixes startup hangs, terminal corruption, and dozens of other bugs. This update significantly improves the reliability and usability of Claude Code for developers, especially those using background sessions or encountering network issues. The extensive bug fixes reduce friction in AI-assisted coding workflows, making Claude Code a more robust tool. Notable fixes include a 15-second timeout for side-channel API calls when `api.anthropic.com` is unreachable, fixing startup hangs up to 75 seconds. Terminal corruption from missed resize events now self-heals, and MCP servers with paginated responses no longer silently drop tools.

github · ashwin-ant · May 19, 00:48

**Background**: Claude Code is Anthropic's command-line tool for AI-assisted coding, using large language models to help developers. Background sessions allow long-running tasks to continue in the background, and the new `/resume` command lets users reattach to them. A captive portal is a web page that intercepts network access until authentication, often causing issues for tools that need to reach external APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://gist.github.com/awreccan/8ad089aec0d279bc2c4df94c1bbc5f44">Claude Code /foreground skill — detach a background session and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Captive_portal">Captive portal</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI tooling`, `#dev tools`, `#release notes`, `#LLM`

---

<a id="item-15"></a>
## [GitHub confirms 3,800 repos breached via malicious VSCode extension](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 8.0/10

GitHub confirmed that a malicious Visual Studio Code extension breached approximately 3,800 internal repositories, and stolen source code was listed for sale online. The attack is attributed to the threat actor TeamPCP, which has previously targeted PyPI and NPM packages. This incident underscores the severe supply chain risk posed by malicious IDE extensions, which run with the same privileges as developers and can silently access source code and credentials. It affects millions of developers who rely on extension ecosystems, highlighting an urgent need for better security controls. The breach was achieved through a poisoned VSCode extension that infiltrated GitHub's internal development environment, leading to the exfiltration of source code from 3,800 repositories. TeamPCP is known for supply chain campaigns like 'Mini Shai-Hulud,' which previously caught two OpenAI employees.

hackernews · Timofeibu · May 20, 13:43 · [Discussion](https://news.ycombinator.com/item?id=48207660)

**Background**: Visual Studio Code extensions are plugins that add functionality to the editor, but they run with full user privileges and often have access to source code, credentials, and build scripts. Supply chain attacks on extension ecosystems are a growing threat, as malicious extensions can be disguised as legitimate ones and spread through official marketplaces.

<details><summary>References</summary>
<ul>
<li><a href="https://securityaffairs.com/192440/cyber-crime/a-malicious-vs-code-extension-just-breached-github-s-internal-repositories.html">A Malicious VS Code Extension Just Breached GitHub 's ...</a></li>
<li><a href="https://cybernews.com/security/github-vscode-extension-breach-sourcecode/">GitHub hacked after poisoned VS Code extension infects ...</a></li>
<li><a href="https://phoenix.security/vs-code-extension-malware-github-breach-teampcp-2026/">VS Code Extension Malware: How TeamPCP Breached GitHub</a></li>

</ul>
</details>

**Discussion**: Community members expressed concern over the security of VSCode extensions, with one commenter noting extensions have been a terrifying attack vector for years. Another suggested sandboxing extensions via WebAssembly, while others sarcastically remarked that Microsoft's three entities (GitHub, VSCode, npm) should collaborate on a solution.

**Tags**: `#security`, `#github`, `#vscode`, `#supply chain attack`, `#infosec`

---

<a id="item-16"></a>
## [Disembodied human brains used for drug testing](https://www.science.org/content/article/not-alive-not-dead-disembodied-human-brains-used-drug-testing) ⭐️ 7.7/10

An article in Science.org reports that scientists are using reanimated, disembodied human brains—likely ex vivo brain slices or organoids—for drug testing, raising profound ethical questions about consciousness and experimentation. This research pushes the boundaries of what is considered acceptable in human experimentation, potentially challenging existing ethical frameworks for neuroscience and drug development. It also forces society to confront the possibility of consciousness in lab-grown brain tissue. The article describes using heavy sedation to prevent electrical activity in the reanimated brains, which some critics argue tacitly acknowledges the risk of returning consciousness. The technique involves reanimating brain tissue from deceased donors or using surgically removed tissue for drug screening.

hackernews · Timofeibu · May 20, 19:38 · [Discussion](https://news.ycombinator.com/item?id=48212992)

**Background**: Ex vivo brain slices and brain organoids are laboratory models that mimic parts of the human brain. Brain slices are thin sections of brain tissue kept alive in culture, while organoids are 3D structures grown from stem cells. Both are valuable tools for studying disease and testing drugs, but ethical debates intensify as they become more realistic and potentially conscious.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebral_organoid">Cerebral organoid - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9923402/">Development and validation of an advanced ex vivo brain slice ...</a></li>

</ul>
</details>

**Discussion**: Community comments express shock and revulsion, comparing the research to dystopian science fiction. Commenters question the legality of the experiments, the adequacy of ethics review, and whether the brains could be conscious and suffer. Some draw parallels to philosophical thought experiments like the 'brain in a vat.'

**Tags**: `#neuroscience`, `#ethics`, `#drug testing`, `#bioethics`, `#human experimentation`

---

<a id="item-17"></a>
## [Ramp accelerates code review using OpenAI Codex](https://openai.com/index/ramp) ⭐️ 7.7/10

Ramp engineers are using OpenAI's Codex, powered by GPT-5.5, to automate code review, reducing feedback time from hours to minutes. This demonstrates a practical application of large language models in software engineering, potentially increasing developer productivity and code quality across the industry. Codex is a suite of AI-driven coding agents that run locally, and GPT-5.5 is OpenAI's latest frontier model with improved reasoning and reduced hallucinations.

rss · OpenAI Blog · May 20, 00:00

**Background**: Code review is a critical but time-consuming part of software development. AI-assisted code review tools leverage large language models to automatically analyze code changes, detect bugs, and suggest improvements. OpenAI Codex is a lightweight coding agent that can integrate into developer workflows, and GPT-5.5 is designed for complex agentic tasks including coding.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-instant/">GPT - 5 . 5 Instant: smarter, clearer, and more personalized | OpenAI</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://grokipedia.com/page/automated_code_review">Automated code review</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Code Review`, `#Codex`, `#GPT`, `#Software Engineering`

---

<a id="item-18"></a>
## [Anthropic's claude-code v2.1.145 released with scripting and telemetry improvements](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) ⭐️ 7.5/10

Anthropic released claude-code v2.1.145, adding a 'claude agents --json' command to list live sessions as JSON for scripting, improving OTEL telemetry with agent_id attributes, and fixing multiple bugs including a security bypass for permission prompts and cross-project resume on Windows. This release strengthens Claude Code as a developer tool by enabling seamless integration with tmux workflows and status bars, enhancing observability of agentic systems, and fixing critical security and usability issues. It reflects Anthropic's focus on stable, production-ready AI coding assistants. The 'claude agents --json' feature enables external scripts to interact with Claude sessions, such as tmux-resurrect for environment persistence. OTEL spans now include 'agent_id' and 'parent_agent_id' for better trace parenting, and several fixes address permission-prompt bypasses, MCP prompt validation errors, and console-specific issues like frozen spinner after terminal resize.

github · ashwin-ant · May 19, 21:31

**Background**: Claude Code is a command-line AI coding assistant by Anthropic that helps developers with tasks like code generation, debugging, and version control. OpenTelemetry (OTEL) is an open-source observability framework for collecting traces, metrics, and logs. tmux-resurrect is a popular plugin that saves and restores tmux sessions, and MCP/LSP are protocols for AI model context and language server integration, respectively.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tmux-plugins/tmux-resurrect">GitHub - tmux-plugins/tmux-resurrect: Persists tmux ...</a></li>
<li><a href="https://opentelemetry.io/docs/">Documentation | OpenTelemetry</a></li>
<li><a href="https://github.com/sminnee/lsp-mcp">GitHub - sminnee/ lsp - mcp : MCP server for LSP - providing IDE...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#claude-code`, `#agents`, `#developer tools`

---

<a id="item-19"></a>
## [Fedora Removes Deepin Desktop; Mozilla to Drop asm.js](https://www.solidot.org/story?sid=84353) ⭐️ 7.4/10

Fedora has removed the Deepin Desktop Environment (DDE) packages due to unresolved security concerns and lack of maintainer responsiveness. Separately, Mozilla announced plans to remove asm.js support from Firefox, starting with disabling optimizations in version 148 and full removal in a future release. Both decisions reflect the open-source community's emphasis on security and code maintenance—Deepin's opaque package insertion and asm.js's superseding by WebAssembly highlight the need for transparent governance and technology modernization. Developers and users relying on these technologies must prepare for transitions. The deepin-feature-enable package, added silently in 2021, re-enabled disabled dbus and polkit functions after user agreement, bypassing openSUSE's security policies. For asm.js, Mozilla will keep sites functional via WebAssembly, which offers faster execution and smaller binaries, and recommends recompilation.

rss · Solidot · May 20, 10:43

**Background**: Deepin Desktop is a Qt-based desktop environment developed by Deepin Technology (a subsidiary of UnionTech, China) and is popular among Chinese users. asm.js is a strict subset of JavaScript introduced in Firefox 22 (2013) to enable near-native performance for C/C++ code on the web, but it was superseded by the standard WebAssembly in 2019. WebAssembly is now the standard for high-performance web applications and is supported by all major browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepin_Desktop_Environment">Deepin Desktop Environment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>

</ul>
</details>

**Tags**: `#security`, `#Linux`, `#Firefox`, `#WebAssembly`, `#open source`

---

<a id="item-20"></a>
## [Google Cloud Blunder Deletes Australian Fund's Infra](https://blog.pragmaticengineer.com/google-cloud-deletes-australian-trading-funds-infra/) ⭐️ 7.3/10

Google Cloud experienced a rare blunder that resulted in the full deletion of infrastructure for a $124 billion Australian fund, though third-party backups prevented total data loss. Google Cloud CEO Thomas Kurian publicly took responsibility for the incident. This incident highlights the critical importance of multi-region replication and third-party backups for cloud reliability, even from a major provider like Google Cloud. It serves as a stark reminder that cloud providers are not immune to catastrophic failures, and customers must have robust backup strategies. The deletion occurred despite Google Cloud's regional replication features, which did not stop the data loss. The fund had third-party backups, which saved them from complete loss; without those, all data would have been gone.

rss · Pragmatic Engineer · May 20, 08:31

**Background**: Google Cloud offers regional replication options such as dual-region buckets and turbo replication to protect data against regional failures. However, this incident shows that even these built-in mechanisms can fail under certain circumstances. Third-party backups provide an additional layer of protection independent of the cloud provider's infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/googlecloud/comments/kkiere/best_practices_for_gcp_multiregion_data/">Best practices for GCP multi-region data replication? - Reddit</a></li>

</ul>
</details>

**Tags**: `#Google Cloud`, `#infrastructure`, `#cloud reliability`, `#data loss`, `#backup`

---