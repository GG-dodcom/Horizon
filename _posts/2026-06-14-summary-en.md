---
layout: default
title: "Horizon Summary: 2026-06-14 (EN)"
date: 2026-06-14
lang: en
---

> From 34 items, 13 important content pieces were selected

---

1. [US Government Orders Anthropic to Suspend Fable 5 and Mythos 5 Access](#item-1) ⭐️ 9.6/10
2. [How to Build a Billion-Dollar Startup: Paul Graham's Guide](#item-2) ⭐️ 9.5/10
3. [Rio's homegrown LLM found to be a weighted merge of existing models](#item-3) ⭐️ 9.4/10
4. [Mapping SQLite Result Columns to Source table.column](#item-4) ⭐️ 9.0/10
5. [Local ML Indexes 669 GB of GoPro Videos on M1 Max](#item-5) ⭐️ 8.9/10
6. [Formal methods and the future of programming](#item-6) ⭐️ 8.8/10
7. [2014 Talk Predicted JavaScript's Replacement by WebAssembly](#item-7) ⭐️ 8.8/10
8. [AI usage not as widespread as assumed](#item-8) ⭐️ 8.2/10
9. [OpenAI WebRTC Audio Playground Updated with GPT-Realtime-2 and Document Context](#item-9) ⭐️ 8.1/10
10. [Pyodide 314.0 enables direct WASM wheel publishing to PyPI](#item-10) ⭐️ 8.0/10
11. [Kage: Turn any website into a single binary for offline viewing](#item-11) ⭐️ 7.5/10
12. [Orbital Data Centers: Harder Than Silicon Valley Thinks](#item-12) ⭐️ 7.5/10
13. [Zeroserve claims Caddy compatibility with major speed gains](#item-13) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [US Government Orders Anthropic to Suspend Fable 5 and Mythos 5 Access](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything) ⭐️ 9.6/10

The US government issued an export control directive to suspend all access to Anthropic's Fable 5 and Mythos 5 models by any foreign national, citing national security concerns over a potential jailbreak method. Anthropic abruptly disabled access for all customers on June 12, 2026. This marks an unprecedented government intervention in AI model access, raising major questions about national security, export controls, and the balance between AI advancement and safety. It sets a precedent for how the US government may regulate frontier AI models in the future. The directive was received at 5:21pm ET on June 12, 2026, with access cut off by 6:59pm PT. Anthropic disputes the severity, noting the alleged jailbreak technique is also available in other models like GPT-5.5 and is used by defenders.

rss · Simon Willison · Jun 13, 01:01

**Background**: Fable 5 is a 'Mythos-class' model from Anthropic made safe for general use, while Mythos 5 is designed for vulnerability discovery. The US government used export control authorities typically applied to dual-use technologies, treating these AI models as national security concerns. Anthropic had previously released Fable 5 for general use, claiming it had sufficient safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/fable-mythos-access">Statement on the US government directive to suspend access to Fable 5 and Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.nytimes.com/2026/06/12/technology/anthropic-mythos-fable5-blocked.html">U.S. Bars Foreigners From Using Anthropic ’s Most Advanced...</a></li>
<li><a href="https://www.bbc.com/news/articles/c932g3v3e13o">Anthropic 's Claude Fable 5 and Mythos 5 AI suspended over security...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#regulation`, `#Anthropic`, `#government directive`

---

<a id="item-2"></a>
## [How to Build a Billion-Dollar Startup: Paul Graham's Guide](https://paulgraham.com/earn.html) ⭐️ 9.5/10

Paul Graham's essay outlines a framework for creating a billion-dollar company by focusing on making something people want and capturing a large market. This insight is significant for entrepreneurs seeking scale, as it distills the key principles behind unicorn startups and challenges common misconceptions about wealth creation. Graham emphasizes that billion-dollar outcomes typically come from addressing a large unmet need rather than incremental improvements, and warns that founders often underestimate the difficulty of scaling.

hackernews · kingstoned · Jun 14, 11:50 · [Discussion](https://news.ycombinator.com/item?id=48526360)

**Background**: The essay is part of Paul Graham's collection of startup advice. He is a venture capitalist and co-founder of Y Combinator. The concept of a "unicorn" – a startup valued at over $1 billion – is central to venture capital.

**Discussion**: The comments show a mix of support and criticism. Some readers appreciate the practical advice, while others argue that billion-dollar startups often involve exploitation or negative externalities. A few engage in speculative math about growth rates.

**Tags**: `#startups`, `#entrepreneurship`, `#wealth`, `#business strategy`, `#technology`

---

<a id="item-3"></a>
## [Rio's homegrown LLM found to be a weighted merge of existing models](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 9.4/10

An investigation revealed that Rio-3.5-Open-397B, presented as a homegrown fine-tune by the municipality of Rio de Janeiro, is actually a weighted merge of approximately 60% Nex-N2 Pro and 40% Qwen3.5-397B-A17B, with no additional training. This discovery raises serious concerns about transparency and attribution in AI development, as it undermines trust in claimed homegrown models and highlights the need for proper disclosure of model origins. Every weight tensor in Rio matches a 0.6/0.4 blend of Nex and Qwen to thousands of standard deviations, across all 60 layers; the authors did not disclose the merge or the use of Nex-N2 Pro.

hackernews · unrvl22 · Jun 14, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48528371)

**Background**: Model merging is a technique that combines parameters from two or more models via weighted averaging or other methods, enabling performance improvements without training on new data. It is commonly used in the LLM community but requires proper attribution when derived works are released.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2411.09263v4">Rethinking Weight-Averaged Model-merging - arXiv.org</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/blog/mlabonne/merge-models">Merge Large Language Models with mergekit</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some defend the approach as legitimate model merging with possible on-policy distillation that wasn't uploaded, while others criticize the lack of attribution and transparency, comparing it to profiting from others' work.

**Tags**: `#LLM`, `#model merging`, `#open-source`, `#AI ethics`, `#investigation`

---

<a id="item-4"></a>
## [Mapping SQLite Result Columns to Source table.column](https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything) ⭐️ 9.0/10

Simon Willison used Claude Code to explore three programmatic methods for determining the source table and column of each result column in arbitrary SQL queries, aiming to enhance Datasette with column provenance information. This research enables richer user interfaces in Datasette, such as showing column origins, and demonstrates practical techniques for accessing SQLite's internal column metadata from Python, which is not natively exposed. The three approaches involve using the apsw library, ctypes to call the sqlite3_column_table_name() C function, and intelligent parsing of EXPLAIN output. All require SQLite to be compiled with SQLITE_ENABLE_COLUMN_METADATA.

rss · Simon Willison · Jun 13, 23:05

**Background**: Column provenance refers to identifying which table and column each result column in a SQL query originates from, which is crucial for data lineage and UI enhancements. Datasette is an open-source tool for exploring and publishing databases. SQLite internally computes this information but its Python sqlite3 module does not expose it, motivating these workarounds.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/">Research: Mapping SQLite result columns back to their source ...</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#SQL`, `#Datasette`, `#column provenance`, `#Claude Code`

---

<a id="item-5"></a>
## [Local ML Indexes 669 GB of GoPro Videos on M1 Max](https://news.ycombinator.com/item?id=48528029) ⭐️ 8.9/10

The author indexed 2,207 GoPro videos (669 GB, 15+ hours) on an M1 Max Mac using open-source ML models to detect and compile interesting moments into a DaVinci Resolve timeline. This demonstrates that powerful local AI video analysis is now feasible on consumer hardware, enabling privacy-preserving and free alternatives to cloud-based services for personal media management. The pipeline processes videos at 1 fps, analyzing 57,537 frames over 67 hours of compute time; it uses open-source models for scene detection and embedding, requiring no internet access.

hackernews · iliashad · Jun 14, 15:13

**Background**: GoPro users often accumulate large video libraries that are tedious to manually review. Local ML models can automatically identify relevant scenes (e.g., cycling highlights) by analyzing frame embeddings. The M1 Max's unified memory and GPU accelerate these workloads without cloud dependency. DaVinci Resolve is a professional video editor; a script can import selected clips directly into its timeline.

**Discussion**: Commenters noted that DaVinci Resolve 21 already has built-in AI IntelliSearch for similar indexing, and another user shared a parallel project (Framedex). There was curiosity about compute time versus paid cloud alternatives, and some lighthearted jokes about applicability to other video collections.

**Tags**: `#AI`, `#video processing`, `#GoPro`, `#local ML`, `#personal project`

---

<a id="item-6"></a>
## [Formal methods and the future of programming](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.8/10

A blog post by Jane Street explores the evolving role of formal methods in programming, highlighting how they can complement AI-generated code by shifting human effort toward verification and using expressive types in languages like Scala 3. As AI generates increasing amounts of code, formal methods become crucial for ensuring correctness and safety, potentially redefining the programmer's role from writing code to verifying it. The post references proof automation tools like SAT solvers and the Boyer-Moore prover, and community comments note that expressive types in Scala 3 can help prevent issues like 'noun accretion' in AI-generated code.

hackernews · eatonphil · Jun 14, 12:35 · [Discussion](https://news.ycombinator.com/item?id=48526633)

**Background**: Formal methods use mathematical models to specify and verify software systems, offering stronger guarantees than testing alone. Expressive type systems in languages like Scala 3 allow compile-time proofs of program invariants. With the rise of AI code generation, there is growing interest in shifting human expertise toward verification tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_methods">Formal methods - Wikipedia</a></li>
<li><a href="https://www.flyriver.com/g/expressive-type-system">Expressive Type Systems: A Deep Dive - flyriver.com</a></li>

</ul>
</details>

**Discussion**: Commenters shared diverse experiences: Animats recalled earlier proof automation work with SAT solvers and the Boyer-Moore prover; winwang praised Scala 3's expressive types for controlling AI agent quality; jdw64 noted that AI-generated code makes verification critical for non-native English speakers; brap questioned whether formal specs merely duplicate tests, risking the same bugs.

**Tags**: `#formal methods`, `#programming`, `#verification`, `#AI`, `#Scala`

---

<a id="item-7"></a>
## [2014 Talk Predicted JavaScript's Replacement by WebAssembly](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.8/10

The talk 'The Birth and Death of JavaScript' from 2014 predicted that JavaScript would become a compilation target and eventually be replaced, which accurately foreshadowed the development of WebAssembly (announced in 2015 and released in 2017). This prediction highlighted the evolution of the web platform toward supporting high-performance languages beyond JavaScript, and its accuracy validates the vision of WebAssembly as a portable compilation target that now powers many web and non-web applications. The talk's creator, Gary Bernhardt, is also known for the famous 'Wat' talk, and the prediction included the idea that JavaScript would become a mere compilation target, with WebAssembly later fulfilling that role but still requiring JavaScript glue code for DOM access.

hackernews · subset · Jun 14, 12:38 · [Discussion](https://news.ycombinator.com/item?id=48526661)

**Background**: JavaScript was originally designed as a scripting language for web browsers but evolved into a general-purpose language. In 2013, asm.js was introduced as a subset of JavaScript for high-performance applications. The talk predicted that JavaScript would be reduced to a compilation target, which eventually led to the development of WebAssembly, a low-level binary format that runs at near-native speed. WebAssembly is now a W3C standard supported by all major browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**Discussion**: The Hacker News community largely agrees that the talk's predictions were accurate, with one comment noting that WebAssembly hasn't advanced as fast as hoped and still requires JavaScript for DOM access, while another joked about the talk's incidental prediction of a global disaster between 2020-2025 being wrong about the type but 'very JavaScript.'

**Tags**: `#JavaScript`, `#WebAssembly`, `#Programming Languages`, `#Tech Talk`, `#Historical`

---

<a id="item-8"></a>
## [AI usage not as widespread as assumed](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) ⭐️ 8.2/10

An article argues that despite the hype around AI, many people use AI tools less than once per week, and job seekers face a dilemma in interviews when asked about AI usage. This challenges the assumption that AI adoption is universal, highlighting that actual usage lags behind perception, which affects product design, hiring practices, and investment decisions. The article cites a study showing over 50% of people use AI less than once per week, and notes that job seekers must hedge between AI-enthusiastic and AI-hesitant employers.

hackernews · yegg · Jun 14, 14:44 · [Discussion](https://news.ycombinator.com/item?id=48527700)

**Background**: Since the launch of ChatGPT in late 2022, AI tools have seen massive media attention and corporate investment. However, adoption in everyday work and personal life may be uneven, with many users trying AI occasionally but not integrating it deeply.

**Discussion**: Commenters note that AI integration is more about embedding features into existing software than standalone chat interfaces. Some remain skeptical, with one stating they still haven't tried AI for anything.

**Tags**: `#AI`, `#LLMs`, `#adoption`, `#usage statistics`, `#perspective`

---

<a id="item-9"></a>
## [OpenAI WebRTC Audio Playground Updated with GPT-Realtime-2 and Document Context](https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything) ⭐️ 8.1/10

Simon Willison updated his browser-based OpenAI WebRTC audio playground to support the newly released GPT-Realtime-2 model and optional document context, allowing users to paste text for voice conversations about that content. This update makes advanced realtime voice AI accessible in a simple browser tool, bridging the gap until OpenAI's own apps adopt GPT-Realtime-2, and demonstrates the practical use of document context for interactive audio discussions. Users can select between old and new models, choose a voice like Coral, and paste any text as document context before starting a session; the model then discusses that content via audio.

rss · Simon Willison · Jun 12, 23:53

**Background**: OpenAI's Realtime API enables low-latency speech-to-speech interactions using models like GPT-Realtime-2, which is described as having GPT-5-class reasoning. WebRTC is a standard for real-time communication in browsers. Simon Willison's playground is a lightweight, open-source browser tool that demonstrates these capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/realtime-webrtc">Realtime API with WebRTC | OpenAI API</a></li>
<li><a href="https://awesomeagents.ai/news/openai-realtime-api-ga-three-models/">OpenAI's Realtime API Goes GA with Three New... | Awesome Agents</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#WebRTC`, `#audio`, `#tooling`, `#GPT-Realtime-2`

---

<a id="item-10"></a>
## [Pyodide 314.0 enables direct WASM wheel publishing to PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 8.0/10

Pyodide 314.0, released on June 13, 2026, allows Python package maintainers to build and publish WebAssembly (WASM) wheels directly to PyPI using the new PyEmscripten platform tag defined in PEP 783. This eliminates the previous bottleneck where Pyodide maintainers had to manually build and host over 300 packages, significantly reducing maintainer burden and enabling the community to distribute packages independently. The platform tag follows the format pyemscripten_YYYY_M_wasm32, and support was added to PyPI's Warehouse repository in April 2026. Tools like cibuildwheel can now produce these wheels, with a working demonstration package 'luau-wasm' published as an example.

rss · Simon Willison · Jun 13, 23:55

**Background**: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly, allowing Python code to run in web browsers. Previously, distributing Python packages with C or Rust extensions compiled to WASM required manual intervention by Pyodide maintainers. PEP 783 standardized the platform tag for Emscripten wheels, making it possible to publish them on PyPI like native wheels.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>
<li><a href="https://pyodide.org/en/314.0.0/development/abi.html">The PyEmscripten Platform — Version 314.0.0 - pyodide.org</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps.python.org</a></li>

</ul>
</details>

**Tags**: `#Pyodide`, `#WASM`, `#PyPI`, `#Python packaging`, `#dev tools`

---

<a id="item-11"></a>
## [Kage: Turn any website into a single binary for offline viewing](https://github.com/tamnd/kage) ⭐️ 7.5/10

Kage is a new open-source tool that clones any website into a single self-contained binary for offline viewing, using headless Chrome to capture the DOM as rendered and stripping all JavaScript. It supports output as folders, ZIM archives, or standalone binaries. This tool addresses the growing need for lightweight, offline-accessible web archives without JavaScript dependency, making it valuable for developers, researchers, and users in low-connectivity environments. It reflects a broader trend against web bloat and for preserving web content in a portable format. Kage uses headless Chrome to render pages, then snapshots the DOM and removes all JavaScript, resulting in a static snapshot. It can output a single binary that includes a built-in HTTP server, which is necessary because browser security restrictions prevent loading local assets directly from file:// URLs.

hackernews · tamnd · Jun 14, 17:25 · [Discussion](https://news.ycombinator.com/item?id=48529990)

**Background**: Traditional website archiving tools like HTTrack download the raw HTML and resources but often fail with JavaScript-heavy sites. Newer tools like SingleFile pack everything into a single HTML file using base64 encoding. Kage takes a different approach by rendering the page first, capturing the post-JavaScript DOM, making it more accurate for dynamic content, while also offering a single-binary distribution that is easier to share.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tamnd/kage">GitHub - tamnd/ kage : Shadow any website for offline viewing, with the...</a></li>
<li><a href="https://news.lavx.hu/article/kage-when-developers-start-questioning-javascript-s-grip-on-the-web">kage : When Developers Start Questioning JavaScript's Grip on the Web</a></li>
<li><a href="https://www.getsinglefile.com/">SingleFile - Effortlessly Save and Preserve Web Pages</a></li>

</ul>
</details>

**Discussion**: Community members praised Kage's concept but noted that SingleFile and HTTrack already offer similar functionality. One user requested a version that doesn't require a separate server process, while another pointed out that the demo GIF was made using the author's other tool, ascii-gif. The discussion also highlighted use cases like offline access to company wikis in areas without cellular coverage.

**Tags**: `#devtools`, `#offline`, `#web archiving`, `#static site`

---

<a id="item-12"></a>
## [Orbital Data Centers: Harder Than Silicon Valley Thinks](https://www.solidot.org/story?sid=84571) ⭐️ 7.5/10

An article critically examines the physical and economic challenges of orbital data centers, concluding that free cooling is a misconception and costs are an order of magnitude higher than terrestrial data centers. This analysis is significant because major companies like SpaceX, Google, and Starcloud are actively pursuing space-based AI computing, but the findings suggest it may not be economically viable, impacting investment decisions and research priorities. In space, only radiative cooling works, requiring large and expensive radiators to prevent chip overheating; solar power requires complex pointing systems, and cosmic rays degrade components. The cost of launching and operating an AI GPU in orbit for a year is at least an order of magnitude higher than on Earth.

rss · Solidot · Jun 13, 15:22

**Background**: Orbital data centers are proposed satellite constellations equipped with AI GPUs, using optical interconnects and microwave links. Proponents claim advantages like abundant solar energy and free cooling, but in a vacuum, heat cannot be dissipated by conduction or convection—only by radiation, which is much less efficient. This misconception about cooling is central to the article's criticism.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Radiant_heating_and_cooling">Radiant heating and cooling - Wikipedia</a></li>
<li><a href="https://futureofenergy.co.ke/energy/the-hidden-advantage-radiative-cooling-in-space/">The Hidden Advantage Radiative Cooling in Space - Africa Digest...</a></li>

</ul>
</details>

**Tags**: `#orbital data centers`, `#AI infrastructure`, `#satellite computing`, `#cooling physics`, `#economics`

---

<a id="item-13"></a>
## [Zeroserve claims Caddy compatibility with major speed gains](https://su3.io/posts/zeroserve-caddy-compat) ⭐️ 7.3/10

Zeroserve, an eBPF-powered web server, has achieved compatibility with Caddy's configuration format, claiming 3x throughput and 70% lower latency compared to standard Caddy. This performance boost could challenge dominant web servers like NGINX, but the lack of ACME and plugin support may limit practical adoption. The compatibility does not include ACME automatic certificate management or Caddy's plugin ecosystem, which are critical for production use. The performance claims are based on benchmarks using io_uring for asynchronous I/O.

hackernews · losfair · Jun 14, 13:43 · [Discussion](https://news.ycombinator.com/item?id=48527145)

**Background**: Zeroserve is a zero-config, high-performance HTTPS server that uses eBPF and io_uring to achieve low overhead. io_uring is a Linux kernel interface for asynchronous I/O that reduces system call overhead. Caddy is a popular web server known for its automatic HTTPS via ACME and plugin architecture. This news describes efforts to make zeroserve accept Caddy configuration files, but with significant omissions.

<details><summary>References</summary>
<ul>
<li><a href="https://su3.io/posts/introducing-zeroserve">zeroserve : a zero -config web server you can script with eBPF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members criticized the lack of ACME and plugin support, calling it a dealbreaker. One user also questioned the security of io_uring for web servers, citing concerns about cybersecurity.

**Tags**: `#web server`, `#performance`, `#Caddy`, `#zeroserve`, `#io_uring`

---