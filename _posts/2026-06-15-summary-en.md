---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 94 items, 19 important content pieces were selected

---

1. [Fake LinkedIn Job Interview Hides npm Backdoor in Repo](#item-1) ⭐️ 9.3/10
2. [Iroh 1.0 Released: Peer-to-Peer Library for Apps](#item-2) ⭐️ 8.7/10
3. [Rust vs C/C++ Memory Safety CVE Patterns](#item-3) ⭐️ 8.7/10
4. [Essay Argues AI Won't Replace Software Engineers](#item-4) ⭐️ 8.6/10
5. [Developers Replace Claude/GPT with Local Qwen 3.6 for Daily Coding](#item-5) ⭐️ 8.4/10
6. [Building a Self-Hosted AI Coding Platform](#item-6) ⭐️ 8.4/10
7. [TimescaleDB Hypercore Compression Achieves Up to 98% Ratio](#item-7) ⭐️ 8.4/10
8. [Anthropic's Safety Superpower as a Business Asset](#item-8) ⭐️ 8.2/10
9. [Claude Code v2.1.178 Adds Tool Parameter Matching & Nested Skills](#item-9) ⭐️ 8.1/10
10. [Typst 0.15.0 Adds Multiple Bibliographies and Better HTML/MathML Support](#item-10) ⭐️ 7.8/10
11. [Love for Computers vs. Tech Industry Critique Sparks Gatekeeping Debate](#item-11) ⭐️ 7.5/10
12. [Guide to Making Glass-to-Metal Seals for Homemade Vacuum Tubes](#item-12) ⭐️ 7.5/10
13. [Datasette Agent 0.3a0 Adds Write SQL with User Approval](#item-13) ⭐️ 7.3/10
14. [Pyodide 314.0 lets Python packages publish WASM wheels to PyPI](#item-14) ⭐️ 7.3/10
15. [LiteLLM v1.88.2 Adds Cosign Docker Image Verification](#item-15) ⭐️ 7.2/10
16. [Hetzner Announces Major Price Hikes Across Server Products](#item-16) ⭐️ 7.0/10
17. [Deep Dive into Commander Keen's Game Engine History](#item-17) ⭐️ 7.0/10
18. [Copper transport drug restores memory in Alzheimer's mice](#item-18) ⭐️ 7.0/10
19. [Personality clashes behind Anthropic model shutdown](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Fake LinkedIn Job Interview Hides npm Backdoor in Repo](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.3/10

A security researcher reports a backdoor hidden in a GitHub repository sent by a fake recruiter during a job interview, which uses npm's prepare script to execute arbitrary code upon installation of dependencies. This attack exploits the trust inherent in job interviews and the common practice of installing dependencies, making it a dangerous supply chain threat that could compromise developer machines and corporate networks. The backdoor payload runs via npm's 'prepare' hook, which automatically executes after 'npm install', and is hidden among commented-out tests in the repository. The attacker asked the victim to investigate 'deprecated Node modules' to lower suspicion.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm's 'prepare' script runs automatically during 'npm install' for local packages, commonly used for build steps. Attackers can exploit this to execute arbitrary code, a technique known as a supply chain attack via dependency confusion. Fake job interviews have become a vector for such attacks as many developers are eager to prove their skills.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">How npm handles the "scripts" field</a></li>
<li><a href="https://www.emmanuelgautier.com/blog/install-production-only-dependencies-with-dev-dependency-hooks-node">Installing Production-Only Dependencies with Dev Dependency Hooks ...</a></li>

</ul>
</details>

**Discussion**: Comments express concern about the frequency of such attacks, noting that many developers would blindly run npm install during a standardized interview task. The lack of a central reporting mechanism for cybercrime is criticized, as is the slow response from GitHub and LinkedIn.

**Tags**: `#security`, `#npm`, `#backdoor`, `#job scam`, `#supply chain attack`

---

<a id="item-2"></a>
## [Iroh 1.0 Released: Peer-to-Peer Library for Apps](https://www.iroh.computer/blog/v1) ⭐️ 8.7/10

Iroh 1.0, the first major release of the peer-to-peer connectivity library, is now available, featuring custom transport support and end-to-end encryption over QUIC. This release simplifies building decentralized applications by providing a library that handles NAT traversal, encryption, and relay, allowing developers to focus on their app logic rather than networking complexity. Iroh currently supports IPv4, IPv6, and relay transports out of the box, and allows developers to implement custom transports such as WebRTC, BLE, or LoRa. Connections are established directly between peers, bypassing traditional firewalls and NATs.

hackernews · chadfowler · Jun 15, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48542480)

**Background**: Iroh is a Rust library that provides peer-to-peer connectivity for applications. It uses QUIC for encrypted connections and includes relay servers for cases where direct connections are not possible. The project is inspired by Tailscale but operates at the application layer, meaning developers can embed it into their apps without requiring users to have additional accounts or infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/">iroh</a></li>
<li><a href="https://news.ycombinator.com/item?id=44379173">Iroh: A library to establish direct connection between peers | Hacker News</a></li>
<li><a href="https://blog.lambdaclass.com/the-wisdom-of-iroh/">The Wisdom of Iroh - LambdaClass Blog</a></li>

</ul>
</details>

**Discussion**: Commenters compare Iroh to 'Tailscale at the application layer' and appreciate the custom transport extensibility. Some question the need for such a library given existing protocols like IP and DNS, while others highlight the value of embedded P2P networking for decentralized apps.

**Tags**: `#P2P`, `#networking`, `#devtools`, `#iroh`, `#peer-to-peer`

---

<a id="item-3"></a>
## [Rust vs C/C++ Memory Safety CVE Patterns](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.7/10

A detailed analysis reveals how memory safety CVEs in Rust differ fundamentally from those in C/C++, highlighting that Rust's borrow checker eliminates many classic vulnerability classes but introduces new panic-based risks. This distinction matters because raw CVE counts are misleading; understanding Rust's unique vulnerability patterns is crucial for accurately assessing security and allocating defensive resources. The analysis notes that Rust CVEs often involve panics (e.g., from unwrap on None) or logic errors in unsafe blocks, whereas C/C++ CVEs typically stem from buffer overflows, use-after-free, or null pointer dereferences.

hackernews · nicoburns · Jun 15, 16:11 · [Discussion](https://news.ycombinator.com/item?id=48543392)

**Background**: Memory safety vulnerabilities are bugs that allow attackers to corrupt memory, leading to crashes or arbitrary code execution. C and C++ lack built-in memory safety, relying on manual management, while Rust enforces ownership and borrowing at compile time via its borrow checker, preventing many memory errors but not logical panics.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.logrocket.com/introducing-rust-borrow-checker/">Understanding the Rust borrow checker - LogRocket Blog</a></li>
<li><a href="https://www.linkedin.com/posts/alexispaques_the-numbers-are-there-rust-has-1000x-less-activity-7395443398020669440-OnoQ">The numbers are there! Rust has 1000x less memory vulnerabilities...</a></li>

</ul>
</details>

**Discussion**: Commenters debate the usefulness of comparing CVE counts, with some arguing the metric is meaningless without context. Others point out that Rust's Option<T> explicitly handles null-like cases, unlike C's NULL pointer, making direct comparisons difficult.

**Tags**: `#Rust`, `#C++`, `#memory safety`, `#CVEs`, `#security`

---

<a id="item-4"></a>
## [Essay Argues AI Won't Replace Software Engineers](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.6/10

Arvind Narayanan and Sayash Kapoor published an essay arguing that AI has not and will not cause mass layoffs of software engineers, citing New York's WARN Act data from 2025 where no company checked the AI disclosure box. This challenges the prevailing narrative that AI will soon replace software engineers, providing data-driven evidence that the profession's core value lies in deep human understanding of codebases and business needs, not just code generation. The essay identifies three real bottlenecks in software engineering: deciding what to build, verifying and being accountable for deliverables, and the deep human understanding required for both—none of which are easily automated by current AI.

rss · Simon Willison · Jun 14, 23:54

**Background**: The WARN Act requires U.S. employers with 100+ employees to provide 60 days' notice before mass layoffs. In March 2025, New York added an optional AI disclosure checkbox to these filings to track AI-related job losses. Over 160 companies filed in the first year, but none indicated AI as a cause.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WARN_Act">WARN Act</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#job market`, `#LLM`, `#economics`

---

<a id="item-5"></a>
## [Developers Replace Claude/GPT with Local Qwen 3.6 for Daily Coding](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.4/10

Hacker News users report successfully replacing cloud-based coding assistants like Claude and GPT with local models, primarily Qwen 3.6 (35B variant), achieving token rates of up to 150 tokens per second on dual RTX 3090 setups. This shift demonstrates that open-source local models can match or approach the performance of subscription-based services for daily coding, offering developers greater privacy, lower ongoing costs, and offline capability. Many users leverage Qwen 3.6-35B-A3B (a Mixture of Experts model with 3B active parameters) via llama.cpp or the Pi coding harness, running offline on machines with 128GB RAM or dual RTX 3090s. Performance degrades noticeably for contexts beyond 150k tokens.

hackernews · cloudking · Jun 15, 14:46

**Background**: Large language models (LLMs) like GPT-4 and Claude are typically accessed via cloud APIs, raising privacy and cost concerns for heavy users. Local LLMs run on the user's own hardware, eliminating data transmission and subscription fees. Qwen 3.6, developed by Alibaba's Qwen team, is a state-of-the-art open-source model series optimized for coding tasks, with variants like 35B-A3B balancing speed and quality.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen/Qwen3.6-35B-A3B · Hugging Face</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.6">Qwen3.6-Plus: Towards Real World Agents</a></li>

</ul>
</details>

**Discussion**: Community members generally agree that Qwen 3.6 is a viable replacement for many coding tasks, though some note it is 'not as smart' as Claude or Codex. There is enthusiasm about speed (150 tok/s on dual 3090s) and the ability to run fully offline, but concerns remain about long-context degradation.

**Tags**: `#local-LLM`, `#Qwen`, `#coding-assistant`, `#AI-tooling`, `#hacker-news`

---

<a id="item-6"></a>
## [Building a Self-Hosted AI Coding Platform](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 8.4/10

The article details a guide for setting up a personal AI coding assistant platform using opencode, Forgejo, and self-hosted servers. This matters as it demonstrates how to create a private, autonomous coding agent with minimal reliance on external services, appealing to homelab enthusiasts and those prioritizing data privacy. Opencode is an open-source AI coding agent supporting over 75 LLM providers and runs as a terminal app, desktop app, or IDE extension. Forgejo is a lightweight, self-hosted Git service that can be integrated with opencode for issue-driven code generation.

hackernews · rsgm · Jun 15, 15:09 · [Discussion](https://news.ycombinator.com/item?id=48542433)

**Background**: Agentic coding involves autonomous AI agents that plan, write, test, and modify code with minimal human intervention, operating at the project level. Opencode is one such agent designed for the terminal. Forgejo is a self-hosted software forge, similar to a private GitHub instance, that is simple to install and maintain.

<details><summary>References</summary>
<ul>
<li><a href="https://opencode.ai/docs/">Intro | AI coding agent built for the terminal - opencode.ai</a></li>
<li><a href="https://dev.to/nuculabs_dev/self-hosting-forgejo-44kh">Self Hosting Forgejo - DEV Community</a></li>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude</a></li>

</ul>
</details>

**Discussion**: Community members shared similar setups, with one integrating opencode into Forgejo action runners for issue-based PR generation. Some noted resource concerns for running opencode on low-spec VMs and preferred running coding agents on their main development devices for faster testing.

**Tags**: `#AI dev platform`, `#opencode`, `#homelab`, `#Forgejo`, `#agentic coding`

---

<a id="item-7"></a>
## [TimescaleDB Hypercore Compression Achieves Up to 98% Ratio](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.4/10

TimescaleDB has introduced hypercore, a new compression technique for time-series data in PostgreSQL, achieving up to 98% compression ratio while maintaining query performance. This advancement significantly reduces storage costs for time-series workloads without sacrificing query speed, making PostgreSQL more competitive against specialized time-series databases. Hypercore uses columnar storage combined with type-specific compression algorithms, and allows configuration via segmentby and orderby options on hypertables.

hackernews · lkanwoqwp · Jun 15, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48544451)

**Background**: TimescaleDB is a PostgreSQL extension for time-series data, and compression is critical for managing large volumes of historical data. Traditional row-based compression can be inefficient for analytical queries, while columnar compression reduces I/O and improves scan performance.

<details><summary>References</summary>
<ul>
<li><a href="https://roszigit.com/en/blog/timescaledb-compression-hypercore/">TimescaleDB Compression: Hypercore and Columnar Storage with ...</a></li>
<li><a href="https://github.com/timescale/docs/blob/latest/use-timescale/hypercore/compression-methods.md">docs/use-timescale/hypercore/compression-methods.md ... - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters discussed trade-offs between compression and query performance, with references to other projects like deltax and gorilla compression. Some expressed skepticism about 'up to' claims in marketing, while others noted the practical benefits for IoT data with swinging-door algorithms.

**Tags**: `#time-series`, `#PostgreSQL`, `#compression`, `#databases`, `#engineering`

---

<a id="item-8"></a>
## [Anthropic's Safety Superpower as a Business Asset](https://stratechery.com/2026/anthropics-safety-superpower/) ⭐️ 8.2/10

Ben Thompson's Stratechery analysis argues that Anthropic's strong safety reputation enables the company to aggressively pursue business interests and challenge U.S. government policies. This insight reframes AI safety from a constraint into a competitive advantage, showing how a company can use ethical positioning to gain market and political leverage. The analysis highlights that Anthropic's safety-first approach, while genuine, also serves as a strategic tool to advocate for regulation that may benefit the company and to differentiate from competitors like OpenAI.

rss · Stratechery · Jun 15, 10:00

**Background**: Anthropic is an AI company co-founded by former OpenAI employees, focused on building safe and beneficial AI systems. It has publicly emphasized its commitment to safety, which has influenced its product development and public messaging. This safety reputation has become a distinguishing feature in the competitive AI landscape.

**Tags**: `#Anthropic`, `#AI safety`, `#business strategy`, `#LLM`, `#regulation`

---

<a id="item-9"></a>
## [Claude Code v2.1.178 Adds Tool Parameter Matching & Nested Skills](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) ⭐️ 8.1/10

Claude Code v2.1.178 introduces tool parameter matching via Tool(param:value) syntax with wildcard support, loads skills from nested .claude/skills directories with name clash resolution, and improves subagent evaluation in auto mode. These updates enhance control over AI tool usage and skill organization, enabling more precise permission rules and better management of complex codebases. The subagent evaluation improvement increases safety by preventing unauthorized actions before subagent launch. The new permission syntax uses a colon to separate tool name and parameter, e.g., Agent(model:opus) to block specific subagent models. Nested skills with conflicting names are displayed as <dir>:<name> to keep both accessible. Auto mode now evaluates subagent spawns via a classifier before proceeding.

github · ashwin-ant · Jun 15, 21:35

**Background**: Claude Code is an AI-powered coding assistant by Anthropic that can execute commands, edit files, and run subagents for complex tasks. It uses skills — reusable markdown instructions in .claude/skills — and a permission system to control which tools and parameters AI actions can use. Subagents are specialized agents spawned for specific subtasks, and the auto mode decides when to automatically delegate to them.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/permissions">Configure permissions - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI-tooling`, `#agentic-systems`, `#developer-tools`

---

<a id="item-10"></a>
## [Typst 0.15.0 Adds Multiple Bibliographies and Better HTML/MathML Support](https://typst.app/docs/changelog/0.15.0/) ⭐️ 7.8/10

Typst 0.15.0 was released, introducing support for multiple bibliographies in a single document, improved HTML export with automatic MathML conversion for equations, and several bug fixes for footnotes. This release significantly enhances Typst's suitability for academic writing, allowing authors to manage separate reference lists (e.g., primary and secondary sources) and improving web accessibility of mathematical content through MathML. The multiple bibliographies feature enables separate reference lists per section or chapter, while the HTML export now produces MathML for mathematical equations, making them render natively in browsers without JavaScript.

hackernews · schu · Jun 15, 17:24 · [Discussion](https://news.ycombinator.com/item?id=48544396)

**Background**: Typst is an open-source typesetting system designed as a modern alternative to LaTeX, using a simpler syntax and faster compilation. MathML is an XML-based standard for representing mathematical notation on the web, integrated into HTML5 and supported by all major browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MathML">MathML</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/MathML">MathML - MDN Web Docs</a></li>

</ul>
</details>

**Discussion**: The community reacted positively, praising multiple bibliographies and improved HTML/MathML support. Users also noted that footnote issues, previously a pain point, have been addressed, with one user expressing optimism about Typst catching up to LuaTeX in typographic quality.

**Tags**: `#typst`, `#typesetting`, `#opensource`, `#programming`

---

<a id="item-11"></a>
## [Love for Computers vs. Tech Industry Critique Sparks Gatekeeping Debate](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 7.5/10

A blog post titled 'I Love the Computer' expresses nostalgic affection for computing while criticizing modern tech industry trends and AI hype, sparking a debate in the comments about gatekeeping and genuine passion. The discussion highlights a tension within the tech community between those who value deep, manual engagement with computers and those who embrace modern tools like AI, reflecting broader cultural divides in software development. The author's sentiment is criticized by commenter tptacek as 'gatekeepy,' implying that the author's nostalgia implies authority over how others use computers. Other commenters share personal stories of loving computers but disliking the industry, or finding AI useful despite reservations.

hackernews · speckx · Jun 15, 20:14 · [Discussion](https://news.ycombinator.com/item?id=48546441)

**Background**: The blog post is a personal reflection, not a technical analysis, but touches on recurring themes in hacker culture: the intrinsic joy of tinkering with computers versus the commercialization and hype of the tech industry. AI, particularly large language models (LLMs), is a current flashpoint, with some viewing it as a tool and others as overhyped.

**Discussion**: Commenters largely agree with the author's love for computers, but debate the gatekeeping accusation: tptacek argues the post subtly claims authority, while others defend it as personal expression. Some express frustration with the industry but still find joy in low-level computing, and a few defend LLMs as genuinely useful tools.

**Tags**: `#technology-critique`, `#software-culture`, `#hacker-culture`, `#programming`, `#AI-cynicism`

---

<a id="item-12"></a>
## [Guide to Making Glass-to-Metal Seals for Homemade Vacuum Tubes](https://maurycyz.com/projects/glass/1/) ⭐️ 7.5/10

Maurycy Z's detailed guide describes techniques for creating glass-to-metal seals suitable for homemade vacuum tubes, covering material selection and step-by-step processes. This enables hobbyists to build custom vacuum tubes, reviving a lost art and fostering experimentation in electronics craftsmanship. It bridges historical manufacturing knowledge with modern DIY accessibility. The guide emphasizes matching coefficients of thermal expansion (CTE) between glass and metal, often using Kovar alloy, and covers both matched and graded seals. Proper surface preparation and controlled heating are critical for a hermetic seal.

hackernews · zdw · Jun 14, 15:52 · [Discussion](https://news.ycombinator.com/item?id=48528587)

**Background**: Glass-to-metal seals are used to create vacuum-tight electrical feedthroughs in vacuum tubes. The key challenge is matching the thermal expansion of glass and metal to prevent cracking upon cooling. Kovar, an iron-nickel-cobalt alloy, has a CTE similar to borosilicate glass, making it a common choice. Graded seals use multiple intermediate glasses to bridge CTE mismatches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Glass-to-metal_seal">Glass-to-metal seal - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kovar">Kovar - Wikipedia</a></li>
<li><a href="https://www.glass-to-metal.com/industry-news-blog/enhancing-durability-with-glass-to-metal-sealing-techniques/">Enhancing Durability with Glass-to-Metal Sealing Techniques</a></li>

</ul>
</details>

**Discussion**: Commenters discussed alternative seal materials like gallium/galinstan (noting its low vapor pressure but adhesion issues), questioned whether historical commercial techniques are lost, and proposed simpler methods using metal endplates with o-rings or premade neon tube electrodes. Some pointed to existing resources like Nixie tube building tutorials.

**Tags**: `#hardware`, `#diy`, `#vacuum tubes`, `#glassblowing`, `#craftsmanship`

---

<a id="item-13"></a>
## [Datasette Agent 0.3a0 Adds Write SQL with User Approval](https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything) ⭐️ 7.3/10

Simon Willison released datasette-agent 0.3a0, introducing a new 'execute_write_sql' tool that requests user approval before executing write operations on the database. The release also enhances the terminal chat mode to support approvals and adds --unsafe mode for auto-approval. This update significantly improves the safety of AI-powered database interactions by requiring explicit user consent for write operations, reducing the risk of accidental data modifications. It enables users to confidently delegate complex SQL tasks to an LLM agent while maintaining control over changes. The execute_write_sql tool checks user permissions and presents a confirmation dialog showing the exact SQL statements and parameters. The datasette agent chat CLI now supports approval prompts, and the --unsafe flag enables automatic approval of all write operations.

rss · Simon Willison · Jun 15, 17:19

**Background**: Datasette Agent is an AI assistant built on top of Datasette, a tool for exploring and publishing data. It uses large language models (LLMs) to interpret natural language queries and generate SQL, which is then executed against SQLite databases. Prior versions lacked write capabilities, limiting the agent to read-only operations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette/ datasette - agent : An LLM-powered agent for...</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#AI agent`, `#SQL`, `#tool use`, `#release`

---

<a id="item-14"></a>
## [Pyodide 314.0 lets Python packages publish WASM wheels to PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 7.3/10

Pyodide 314.0 was released, allowing Python package maintainers to publish WebAssembly (WASM) wheels directly to PyPI, removing the need for Pyodide maintainers to manually build and host over 300 packages. This simplifies distribution of Python packages for browser and Node.js runtimes, reducing maintenance burden on Pyodide and enabling faster adoption of Python in web environments. The feature is based on PEP 783, which defines the PyEmscripten platform tag. Package maintainers can build wheels with cibuildwheel and publish them just like native wheels. A demonstration package, luau-wasm, was published as a proof of concept.

rss · Simon Willison · Jun 13, 23:55

**Background**: Pyodide is a port of CPython to WebAssembly/Emscripten, enabling Python to run in browsers and Node.js without a server. Previously, all Pyodide-compatible packages had to be hosted by the Pyodide project, creating a bottleneck. PEP 783 standardizes the platform tag for Emscripten-based wheels, making it possible for any maintainer to publish WASM wheels to PyPI.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.0</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps .python.org</a></li>
<li><a href="https://news.ycombinator.com/item?id=48462759">Pyodide 314.0: Python packages can now publish WebAssembly wheels to PyPI | Hacker News</a></li>

</ul>
</details>

**Tags**: `#pyodide`, `#wasm`, `#pypi`, `#python`, `#webassembly`

---

<a id="item-15"></a>
## [LiteLLM v1.88.2 Adds Cosign Docker Image Verification](https://github.com/BerriAI/litellm/releases/tag/v1.88.2) ⭐️ 7.2/10

BerriAI released LiteLLM v1.88.2, which includes detailed instructions for verifying Docker image signatures using the cosign tool. This release enhances security for LiteLLM users by enabling them to verify the integrity and authenticity of Docker images, protecting against supply chain attacks. Users can verify signatures using either a pinned commit hash (recommended for immutability) or a release tag, both referencing the same public key hosted on GitHub.

github · github-actions[bot] · Jun 14, 02:51

**Background**: Cosign is a tool from the Sigstore project for signing and verifying container images. Signing Docker images helps ensure that the image has not been tampered with and comes from a trusted source. LiteLLM v1.88.2 now provides clear steps to perform this verification.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/ cosign : Code signing and transparency for...</a></li>
<li><a href="https://medium.com/@Shoaib14/cosign-github-and-why-do-you-need-it-499a0f5ff265">Signing Container Images with Cosign . | by Shoaib Murtaza | Medium</a></li>
<li><a href="https://dev.to/n3wt0n/sign-your-container-images-with-cosign-github-actions-and-github-container-registry-3mni">Sign Your Container Images with Cosign , GitHub... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#litellm`, `#docker`, `#cosign`, `#security`, `#release`

---

<a id="item-16"></a>
## [Hetzner Announces Major Price Hikes Across Server Products](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 7.0/10

Hetzner has announced significant price increases across its server products, including cloud servers, dedicated servers, and storage, with some products seeing up to 3x the previous price. The changes, effective from a specified date, also include a standardization of product lines. This price adjustment reflects the broader impact of AI-driven hardware scarcity on cloud and hosting costs. Customers who relied on Hetzner's historically low prices may need to reassess their infrastructure budgets, potentially shifting demand to larger providers. The price increases range from 25% to 200% depending on the product category, with dedicated servers and cloud instances among the most affected. Existing customers are not grandfathered in; the new prices apply to both new and existing contracts.

hackernews · tuhtah · Jun 15, 13:19 · [Discussion](https://news.ycombinator.com/item?id=48540844)

**Background**: Hetzner is a German data center operator and hosting provider known for affordable dedicated servers and cloud services. The AI boom has caused global scarcity of GPUs, RAM, and SSDs, driving up hardware costs. Smaller providers like Hetzner often have less leverage in the supply chain compared to hyperscalers such as AWS, GCP, and Azure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hetzner">Hetzner</a></li>
<li><a href="https://www.educative.io/newsletter/system-design/how-ai-hardware-is-redefining-system-design">From chips to chains: How AI hardware is redefining System Design</a></li>
<li><a href="https://blog.lqd3-solutions.ai/2026/01/08/overcoming-ai-hardware-scarcity-strategic-investment-2025/">Overcoming AI Hardware Scarcity : Strategic Investment and...</a></li>

</ul>
</details>

**Discussion**: Comments on the news express frustration at the magnitude of increases, with one user calling a 3x jump 'wild'. Some argue that Hetzner's previous low prices were unsustainable, while others question when the upsides of the AI boom will materialize for the average consumer.

**Tags**: `#Hetzner`, `#cloud pricing`, `#AI hardware costs`, `#infrastructure`, `#hosting`

---

<a id="item-17"></a>
## [Deep Dive into Commander Keen's Game Engine History](https://forgottenbytes.net/commander_keen.html) ⭐️ 7.0/10

A detailed analysis of Commander Keen's game engine has been published, explaining the breakthrough adaptive tile refresh technique that enabled smooth scrolling on PC hardware. This analysis highlights a pivotal moment in early game programming, showcasing how clever software techniques overcame hardware limitations to influence future game engines. John Carmack's adaptive tile refresh technique uses the EGA card's offset capability to slide the screen through a buffer, redrawing only changed tiles, achieving smooth scrolling without hardware sprite support.

hackernews · mfiguiere · Jun 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=48544781)

**Background**: In the early 1990s, PC hardware lacked dedicated sprite hardware, making smooth side-scrolling difficult. John Carmack's innovative technique, first used in Commander Keen, allowed PC games to match the fluidity of console titles like those on the SNES. This breakthrough was instrumental in the success of id Software and the rise of shareware games.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adaptive_tile_refresh">Adaptive tile refresh - Wikipedia</a></li>
<li><a href="http://www.vogonswiki.com/index.php/Commander_Keen_4">Commander Keen 4 - Vogons Wiki</a></li>

</ul>
</details>

**Discussion**: Commenters praised the analysis and recommended the book 'Masters of Doom' for deeper history on id Software. They also discussed why PC hardware struggled with sprite rendering compared to consoles like the SNES, and some suggested contacting Fabien Sanglard for further insights.

**Tags**: `#game development`, `#engine programming`, `#id Software`, `#Commander Keen`, `#retro gaming`

---

<a id="item-18"></a>
## [Copper transport drug restores memory in Alzheimer's mice](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins) ⭐️ 7.0/10

Monash University researchers have shown that a copper-delivering drug reduces toxic amyloid-beta proteins and improves spatial memory in Alzheimer's mouse models. This finding challenges the prevailing view that copper is harmful in Alzheimer's, and the drug's prior safety data could enable rapid transition to human trials. The drug was tested in mice, not humans, but it has already undergone safety evaluations for other diseases, potentially accelerating clinical development.

hackernews · bookofjoe · Jun 15, 14:48 · [Discussion](https://news.ycombinator.com/item?id=48542132)

**Background**: Alzheimer's disease is characterized by the accumulation of amyloid-beta plaques in the brain, which are thought to trigger neurodegeneration. Most current therapies aim to remove these plaques, but with limited success. Copper imbalance has been implicated in Alzheimer's, but targeting copper delivery represents a new approach.

<details><summary>References</summary>
<ul>
<li><a href="https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins">Copper drug restores memory and clears toxic Alzheimer’s ...</a></li>
<li><a href="https://medicalxpress.com/news/2026-06-copper-drug-memory-toxic-alzheimer.html">Copper drug restores memory and clears toxic Alzheimer's ...</a></li>
<li><a href="https://scienceblog.com/a-copper-drug-cleared-toxic-proteins-and-restored-memory-in-alzheimers-mice/">A Copper Drug Cleared Toxic Proteins and Restored Memory in ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some dismissed the amyloid hypothesis based on past failures, while others noted that the copper mechanism is distinct and could still be promising. A user with personal experience highlighted the disease's complexity and the need for subtyping.

**Tags**: `#Alzheimer's`, `#amyloid-beta`, `#copper`, `#neuroscience`, `#drug development`

---

<a id="item-19"></a>
## [Personality clashes behind Anthropic model shutdown](https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything) ⭐️ 7.0/10

An Axios report reveals that personality clashes between Anthropic and the US Commerce Department contributed to the suspension of Anthropic's advanced AI models, Mythos and Fable, due to export control concerns. This incident highlights the growing tension between AI companies and regulators over export controls, and shows that human factors can significantly impact AI governance and access to cutting-edge models. Anthropic's Frontier Red Team, led by Logan Graham, is meeting with the Commerce Department to discuss the issue. The administration insists that Anthropic fix the jailbreak problem, though perfect resistance may be impossible according to Anthropic.

rss · Simon Willison · Jun 15, 14:57

**Background**: Anthropic's Claude Mythos is a powerful AI model designed for cybersecurity and research, but has been restricted due to safety concerns. Claude Fable 5 is a public version with guardrails. The US government invoked export controls to suspend access after a jailbreak was discovered.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://fortune.com/2025/09/04/anthropic-red-team-pushes-ai-models-into-the-danger-zone-and-burnishes-companys-reputation-for-safety/">Anthropic’s ‘ Red Team ’ pushes its AI models into the danger... | Fortune</a></li>

</ul>
</details>

**Tags**: `#anthropic`, `#export control`, `#US government`, `#AI safety`, `#political gossip`

---