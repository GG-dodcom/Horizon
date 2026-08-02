---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 68 items, 9 important content pieces were selected

---

1. [Stateless MCP 2.0 reignites interest, spawns mcp-explorer and datasette-mcp](#item-1) ⭐️ 9.5/10
2. [DeepSeek V4 Flash 0731: Low-Cost 304B Model with Agentic Gains](#item-2) ⭐️ 7.8/10
3. [Karpathy Proposes 'Pelican on a Bicycle' AI Benchmark](#item-3) ⭐️ 7.5/10
4. [AI Open Letters: Microsoft-led Open Weights Push vs Anthropic and Pacing Frontier](#item-4) ⭐️ 7.5/10
5. [Datasette-apps 0.2a0 lets AI agent test and edit apps](#item-5) ⭐️ 7.3/10
6. [Bor v0.8: Open-Source mTLS/gRPC Policy Management for Linux Desktops](#item-6) ⭐️ 7.2/10
7. [OpenAI's Astra Model Solves Ten Long-Standing Math Problems for Under $2,000 Each](#item-7) ⭐️ 7.2/10
8. [F*: A Proof-Oriented Programming Language for Formal Verification](#item-8) ⭐️ 7.1/10
9. [Mexico Becomes Top U.S. Supplier of AI Servers, Overtaking Autos](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Stateless MCP 2.0 reignites interest, spawns mcp-explorer and datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.5/10

Simon Willison describes the Stateless MCP spec update (MCP 2.0, the 2026-07-28 Model Context Protocol specification) that simplifies the protocol to a single HTTP request. He also introduces his two new tools: mcp-explorer and datasette-mcp. This matters because MCP had been eclipsed by Skills and agentic shell access, but the stateless redesign lowers implementation complexity, making MCP easier to audit, control, and run on smaller models. It could revive MCP adoption in the AI agent ecosystem. The stateless MCP uses headers like MCP-Protocol-Version and Mcp-Method instead of session initialization, removing the need for server-side sessions. Simon built three implementations in a week, including mcp-explorer (a CLI for interactively probing MCP servers) and datasette-mcp (a plugin exposing Datasette databases via MCP with read-only SQL access).

rss · Simon Willison · Jul 31, 23:13

**Background**: MCP (Model Context Protocol) is an open standard introduced by Anthropic in November 2024 for exposing tools to LLM agent frameworks. Legacy MCP requires a two-step initialization session, while stateless MCP uses a single request/response, making it a better fit for scalable web infrastructure and simpler to implement for both clients and servers.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/31/stateless-mcp/">Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>
<li><a href="https://github.com/datasette/datasette-mcp">GitHub - datasette/ datasette - mcp : Adds a /-/mcp MCP server to any...</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI`, `#Agentic Systems`, `#LLM`, `#Developer Tools`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731: Low-Cost 304B Model with Agentic Gains](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 7.8/10

DeepSeek released V4 Flash 0731, a 304B-parameter open-weight model with substantially enhanced agentic capabilities, priced at $0.14 per million input tokens and $0.27 per million output tokens. Artificial Analysis ranks it ahead of MiniMax M3 (428B) on the Intelligence Index, and Simon Willison highlighted it as possibly the best value-per-intelligence model available. This release could significantly lower the cost of agentic AI applications, making advanced reasoning accessible to more developers at roughly $0.028 per task. It intensifies price-performance competition in the LLM market, pressuring larger and pricier models like Grok 4.5 and Claude Opus 5 in value comparisons. The model is 167GB on Hugging Face with 304B total parameters. Simon Willison found that default reasoning level via OpenRouter produced a 'disappointing pelican', but raising reasoning_effort to high with the command `llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high` yielded much better results, showing reasoning effort materially affects output quality.

rss · Simon Willison · Jul 31, 23:59

**Background**: DeepSeek is a Chinese AI lab that releases open-weight models. The Artificial Analysis Intelligence Index is a composite benchmark that scores models across reasoning, coding, knowledge, instruction following, and multi-step tasks, used here to compare value. 'Agentic capabilities' refer to a model's ability to plan, act, and interact autonomously with tools, which is a key differentiator in current LLM market positioning.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index</a></li>
<li><a href="https://hackernoon.com/notes-on-agentic-reasoning-for-large-language-models">Notes on Agentic Reasoning for Large Language Models | HackerNoon</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#LLM`, `#AI models`, `#inference`, `#agentic AI`

---

<a id="item-3"></a>
## [Karpathy Proposes 'Pelican on a Bicycle' AI Benchmark](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.5/10

Andrej Karpathy tweeted about using a 'pelican on a bicycle' as a benchmark for AI's physical-world understanding, igniting discussion on Hacker News. The proposal shifts AI evaluation from text-only tasks to visual and physical plausibility, potentially reshaping how the community measures progress in multimodal and world models. It highlights whether generative models truly understand real-world constraints rather than just producing plausible pixels. The benchmark uses the prompt 'Generate an SVG of a pelican riding a bicycle,' originally created by Simon Willison in October 2024. It is an informal, qualitative test of whether a model can render an impossible scene in a visually and physically coherent way.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: The 'pelican on a bicycle' benchmark is an informal test that asks AI models to generate an SVG image of a pelican riding a bicycle, a physically impossible scene. It was created by developer Simon Willison in October 2024 as a way to probe models' visual and spatial reasoning, complementing traditional text-only benchmarks like MMLU and GSM8K. As interest grows in Physical AI — systems that understand and interact with the physical world — such qualitative challenges help reveal whether models grasp commonsense constraints beyond text statistics.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) - Grokipedia</a></li>
<li><a href="https://ai.miraheze.org/wiki/Pelican_Bicycle_Benchmark">Pelican Bicycle Benchmark - Learn AI</a></li>
<li><a href="https://www.ibm.com/think/topics/physical-ai">What is physical AI? - IBM</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some worry that janky AI-generated results are being hailed as solved, reflecting lowered quality expectations, while others argue imperfect outputs are precisely what make the benchmark useful for measuring physical-world understanding. A side discussion questions whether models like Anthropic's are merely overfitted to generating three.js code, not genuinely understanding scenes.

**Tags**: `#AI`, `#benchmarking`, `#image generation`, `#Karpathy`, `#LLM`

---

<a id="item-4"></a>
## [AI Open Letters: Microsoft-led Open Weights Push vs Anthropic and Pacing Frontier](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.5/10

Simon Willison summarized a wave of recent AI open letters. These include a Microsoft-led open-weights letter dated July 24 signed by 235 companies including NVIDIA and OpenAI, Anthropic's counter-position three days later, and a July 28 'Pacing the Frontier' letter signed by 1,324 employees of frontier AI companies. The letters expose a deep industry split over open-weight AI, with Microsoft and allies framing openness as a safety and competition win while Anthropic and many frontier researchers emphasize misuse risks and the dangers of competitive pressure. The policy outcome could shape how the US regulates model releases, distillation, and automated AI research. The Microsoft letter explicitly defends distillation as a legitimate model-development technique and warns against conflating it with misappropriation, while Anthropic declined to sign and CEO Dario Amodei instead called for a crackdown on industrial-scale distillation (though he said Anthropic has never advocated a ban). The Pacing the Frontier signatories include OpenAI chief scientist Jakub Pachocki, Ilya Sutskever, and Dario Amodei.

rss · Simon Willison · Aug 2, 04:16

**Background**: Open-weight models publicly release the trained parameters of an AI model, so anyone can download, run, study, or modify them, which sits between fully open source and closed API models (Stanford HAI). Supporters argue this enables external auditing, transparency, and competition, while critics worry about misuse for cyberattacks, biological attacks, or empowering authoritarian governments. Recent US government actions, including a directive to suspend access to a frontier model, have intensified the debate over open weights and safety.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/971690/dario-amodei-weighed-in-on-anthropics-open-weight-model-controversy">Dario Amodei weighed in on Anthropic’s open - weight model ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Weights`, `#Policy`, `#Open Source`, `#Simon Willison`

---

<a id="item-5"></a>
## [Datasette-apps 0.2a0 lets AI agent test and edit apps](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 7.3/10

Datasette-apps 0.2a0 adds app_debug() and app_list() tools so Datasette Agent can test and edit Datasette Apps. The app_debug() tool runs agent-provided JavaScript inside an invisible, sandboxed iframe for smoke testing. This bridge between AI agents and app testing enables Datasette Agent to autonomously verify and modify Datasette Apps. It will make AI-assisted development and maintenance of Datasette-hosted applications more practical. app_debug() displays the app in an iframe with opacity: 0 and pointer-events: none, then executes agent-provided JavaScript inside that sandboxed iframe. It relies on the context.browser_task() mechanism introduced in datasette-agent 0.4a0, while app_list() lists apps the user has permission to edit.

rss · Simon Willison · Aug 1, 21:23

**Background**: Datasette Apps let developers host web applications inside Datasette, an open-source tool for exploring and publishing data. Datasette Agent is an LLM-powered extensible AI assistant for Datasette, and smoke testing is a technique that verifies whether the core functionality of a new build works before deeper testing begins.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/1/datasette-apps/">Release: datasette - apps 0.2a0 | Simon Willison’s Weblog</a></li>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/ datasette - apps : Apps that live inside Datasette</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help ...</a></li>

</ul>
</details>

**Tags**: `#Datasette`, `#AI agents`, `#agentic tools`, `#software release`, `#testing`

---

<a id="item-6"></a>
## [Bor v0.8: Open-Source mTLS/gRPC Policy Management for Linux Desktops](https://getbor.dev/blog/2026-08-02-bor-v080-release/) ⭐️ 7.2/10

Bor v0.8 was released on August 2, 2026, adding new policy types for Thunderbird, Microsoft Edge for Business, and FirewallD zones. The open-source system centrally manages Linux desktops via a lightweight Go agent that streams policies over mTLS/gRPC in real time without polling. Linux desktop fleet management has few good open-source options, and this release expands policy coverage to common email, browser, and firewall tools. It offers a promising policy-as-code alternative for nonprofits, enterprises, and sysadmins who want to avoid proprietary management stacks like Microsoft Intune. Current policy targets include Firefox, Chrome, KDE, dconf, polkit, and package management, with v0.8 adding Thunderbird, Edge for Business, and FirewallD zones. Policies are pushed in real time over mTLS/gRPC, so there is no polling interval; the release notes also mention improvements and fixes but do not yet document drift-reversion behavior.

hackernews · eniac111 · Aug 2, 09:06 · [Discussion](https://news.ycombinator.com/item?id=49142569)

**Background**: dconf is the low-level configuration database used by GNOME and related desktop environments, storing settings as key-value pairs. Polkit is an authorization framework that lets privileged programs offer services to unprivileged clients, commonly used in graphical Linux desktops for fine-grained access control. FirewallD is a dynamically managed firewall that uses zones to define trust levels for network connections and interfaces. Bor ties these together as policy targets so administrators can enforce desktop configuration from a central server.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dconf">dconf - Wikipedia</a></li>
<li><a href="https://linuxconfig.org/introduction-to-polkit-navigating-authorization-frameworks-in-linux">Introduction to Polkit: Navigating Authorization Frameworks in Linux</a></li>
<li><a href="https://firewalld.org/">Home | firewalld</a></li>

</ul>
</details>

**Discussion**: Commenters are generally enthusiastic, saying the tool is close to what they need for managing fleets by hand, but they ask for specifics: Cinnamon support, custom script execution, integration with identity providers like Authentik, how user mapping works, and how configuration drift is handled given there is no polling. Others ask how it compares to existing solutions and why mTLS was chosen over SSH, and some suggest using Mermaid diagrams in the docs instead of ASCII charts.

**Tags**: `#Linux`, `#open-source`, `#device-management`, `#Go`, `#policy-as-code`

---

<a id="item-7"></a>
## [OpenAI's Astra Model Solves Ten Long-Standing Math Problems for Under $2,000 Each](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 7.2/10

OpenAI announced that an internal version of its next major model, Astra, solved ten mathematical problems that had seen no progress for at least a decade, costing less than $2,000 each at GPT-5.6 Sol token prices. The company released Lean 4 formalizations of all ten proofs in a public GitHub repository. This development highlights the growing capability of frontier AI models to produce verifiable mathematical research, potentially accelerating progress in mathematics and theoretical computer science. It also fuels an ongoing debate about how AI should be transparently evaluated, especially regarding unreported failed attempts. The ten-proofs repository allows anyone with the Lean compiler to verify each proof independently, without needing to trust OpenAI. However, Simon Willison and some observers note that OpenAI has not disclosed how many problems were attempted without success, and OpenAI's public marketing materials do not list an Astra model.

rss · Simon Willison · Aug 1, 20:34

**Background**: Lean 4 is an interactive theorem prover that lets mathematicians formalize proofs and verify them mechanically. The idea of 'big mathematics', as described by mathematician Terence Tao, envisions large-scale collaboration between humans and AI, where machines handle technical grunt work and humans focus on creative aspects. This announcement also comes shortly after Anthropic's Claude was used to discover cryptographic weaknesses, showing an arms race in AI-assisted research.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/ten-proofs">GitHub - openai/ten-proofs: Lean certificates accompanying proofs in mathematics and theoretical computer science · GitHub</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT-5.6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://runtimewire.com/article/openai-astra-ten-open-math-problems">OpenAI says unreleased Astra model solved 10 open... - RuntimeWire</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#mathematics`, `#OpenAI`, `#research`

---

<a id="item-8"></a>
## [F*: A Proof-Oriented Programming Language for Formal Verification](https://fstar-lang.org/) ⭐️ 7.1/10

The Hacker News community discussed F*, a proof-oriented programming language, after a link to its official site was posted. F* integrates dependent types, monadic effects, and refinement types to verify program correctness. F* is significant because it enables formal verification of security and functional correctness properties in real-world software, with industry adoption including use by Microsoft Research. It bridges the gap between formal methods research and practical programming, offering a general-purpose language for building verified systems. F* can be compiled to OCaml, F#, C, WebAssembly (via KaRaMeL), and assembly language (via Vale). Its type system supports dependent types, monadic effects, and refinement types, and the type-checker uses SMT solving combined with manual proofs to verify specifications.

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: F* (pronounced "F star") is a high-level, multi-paradigm language developed by Microsoft Research and Inria, inspired by ML, Caml, and OCaml. It aims to prove that programs meet their specifications, which is valuable for security-sensitive software such as cryptographic protocols and verified compilers. The language has been under active development since 2011 and is available on GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language)</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof - Oriented Programming Language</a></li>

</ul>
</details>

**Discussion**: Community comments included a critique that the F* website lacks code examples on the homepage, while another user praised the ability to incrementally migrate existing C codebases to F*. Several users also asked about industry usage and the language's suitability for functional programming newcomers.

**Tags**: `#proof-oriented language`, `#formal verification`, `#F*`, `#programming languages`, `#software engineering`

---

<a id="item-9"></a>
## [Mexico Becomes Top U.S. Supplier of AI Servers, Overtaking Autos](https://feeds.feedblitz.com/~/965674583/0/marginalrevolution~Mexico-Taiwan-fact-of-the-day.html) ⭐️ 7.0/10

Mexico now provides 40% of U.S. imports of computer servers widely used in AI data centers, and servers have overtaken autos as the country's top export to the U.S. Taiwanese manufacturers are rapidly expanding factories in Mexico to assemble these servers. This quietly makes Mexico a cornerstone of the AI supply chain, reshaping North American manufacturing and trade flows. It also highlights how Taiwanese companies are moving assembly closer to the U.S. market amid the AI infrastructure boom. The 40% figure refers to U.S. imports of servers 'this year,' according to the post, which offers no further breakdown by product category or manufacturer. Servers are now Mexico's top export to the U.S., overtaking automobiles, a notable shift in the bilateral trade relationship.

rss · Marginal Revolution · Aug 2, 04:35

**Background**: Servers are the high-performance computers that power data centers, and AI workloads require especially large numbers of them. Taiwan is a global hub for server design and manufacturing, so Taiwanese companies moving assembly to Mexico allows them to serve the U.S. market while keeping supply chains relatively close to North America.

**Discussion**: Comments are mixed: some say the trend should surprise no one given Mexico's long history in manufacturing, while others urge caution about overenthusiasm. One comment brings up the Trump administration, and another thread takes a dismissive tone toward another commenter. Overall, readers largely accept the data point but disagree on its political and economic significance.

**Tags**: `#AI infrastructure`, `#supply chain`, `#Mexico`, `#servers`, `#economics`

---