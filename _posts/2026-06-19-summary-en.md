---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 95 items, 15 important content pieces were selected

---

1. [Beyond LoRA: Can alternative PEFT methods beat LoRA?](#item-1) ⭐️ 9.2/10
2. [Amateur may have cracked Linear A using AI](#item-2) ⭐️ 8.8/10
3. [Project Valhalla Arrives in JDK 28: Value Types & Heap Flattening](#item-3) ⭐️ 8.5/10
4. [MosaicLeaks: Privacy Risks in AI Research Agents](#item-4) ⭐️ 8.5/10
5. [Benchmarking Open Models for Agentic Capabilities](#item-5) ⭐️ 8.5/10
6. [GLM-5.2: Leading Open-Weight LLM with 1M Context](#item-6) ⭐️ 8.4/10
7. [Interview with Michael Morton on AI & E-Commerce](#item-7) ⭐️ 8.3/10
8. [Claude Code v2.1.183 Adds Safety Blocks for Destructive Commands](#item-8) ⭐️ 8.0/10
9. [Anjney Midha Interview: The Professor of Outputmaxxing](#item-9) ⭐️ 8.0/10
10. [ATProto Has No Instances, Explains Dan Abramov](#item-10) ⭐️ 7.9/10
11. [Datasette Apps: Host Sandboxed HTML+JS Apps Inside Datasette](#item-11) ⭐️ 7.8/10
12. [Norway bans AI for elementary students](#item-12) ⭐️ 7.6/10
13. [ALS patient becomes first long-term BCI power user](#item-13) ⭐️ 7.6/10
14. [Stratechery Roundup on Anthropic and AI E-commerce](#item-14) ⭐️ 7.5/10
15. [Vercel AI SDK Workflow Fixes Provider-Executed Tool Approval Bug](#item-15) ⭐️ 7.2/10

---

<a id="item-1"></a>
## [Beyond LoRA: Can alternative PEFT methods beat LoRA?](https://huggingface.co/blog/peft-beyond-lora) ⭐️ 9.2/10

The Hugging Face blog post 'Beyond LoRA: Can you beat the most popular fine-tuning technique?' investigates whether alternative parameter-efficient fine-tuning (PEFT) methods can outperform LoRA for large language models, providing technical comparisons and practical insights. This analysis is significant because LoRA is the dominant PEFT method, and finding superior alternatives could reduce computational costs and improve model performance for practitioners fine-tuning LLMs. It directly impacts the efficiency and accessibility of LLM adaptation. The blog likely compares LoRA with methods like MoRA (high-rank updates) and other LoRA variants, discussing trade-offs in parameter efficiency, training speed, and final model quality. Technical details may include rank selection, update constraints, and adapter architectures.

rss · Hugging Face Blog · Jun 18, 00:00

**Background**: Parameter-efficient fine-tuning (PEFT) allows adapting large pre-trained models by updating only a small fraction of parameters, reducing memory and compute. LoRA (Low-Rank Adaptation) is the most popular PEFT method, which inserts trainable low-rank matrices. Alternatives like MoRA aim to achieve higher-rank updates for better performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2405.12130">MoRA: High-Rank Updates for Fine - Tuning</a></li>

</ul>
</details>

**Tags**: `#LoRA`, `#fine-tuning`, `#PEFT`, `#LLM`, `#Hugging Face`

---

<a id="item-2"></a>
## [Amateur may have cracked Linear A using AI](https://aiclambake.com/clamtakes/linear-a/) ⭐️ 8.8/10

An amateur researcher, Tom Di Mino, used Anthropic's Claude Code to build Python scripts that systematically test hypotheses on the Linear A corpus, potentially achieving a breakthrough in deciphering the undeciphered Minoan script. If validated, this would be the first successful decipherment of Linear A after over a century of effort, demonstrating how AI-assisted tooling can accelerate progress in complex puzzles that have resisted traditional methods. Di Mino's approach translates over 300 words based on the 'Libation Formula' and uses Claude Code not as a black-box solver but to build hypothesis-testing tools. His work is under review by linguists at Rutgers and Cambridge.

hackernews · Kosturdistan · Jun 19, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48600107)

**Background**: Linear A is a script used by the Minoan civilization on Crete from 1800–1450 BC. Despite sharing many symbols with Linear B (which was deciphered in the 1950s as an early form of Greek), Linear A remains undeciphered because the underlying language is unknown. Claude Code is an AI coding agent by Anthropic that can read and edit codebases across multiple files, enabling non-engineers to build software tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A">Linear A - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: Community commenters express cautious optimism: one notes that Di Mino's work is being reviewed by experts at Rutgers and Cambridge, and that his translation of over 300 words is unprecedented. Another commenter praises the approach of using AI to build tools rather than as a black-box solver. There is also mention of other undeciphered scripts like the Indus Valley script.

**Tags**: `#AI`, `#Linear A`, `#decipherment`, `#ancient scripts`, `#LLM applications`

---

<a id="item-3"></a>
## [Project Valhalla Arrives in JDK 28: Value Types & Heap Flattening](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.5/10

After a decade of development, Project Valhalla's value types and heap flattening are arriving in JDK 28, fundamentally changing how Java handles objects by allowing dense storage without object headers or indirection pointers. This improves memory density and performance for Java applications, especially for data-intensive workloads, and brings Java closer to the performance of languages like C or Rust while maintaining its safety guarantees. Heap flattening only applies to value objects that fit within 64 bits, so larger value objects may not benefit from full flattening. The implementation requires value types to be immutable, non-null, and identity-free.

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: Project Valhalla is an OpenJDK project started in 2014 to introduce value types to Java, aiming to combine the abstraction of objects with the performance of primitives. Value types are user-defined types that behave like primitives, with no object identity or headers. Heap flattening is a key optimization that stores value type fields directly in arrays or objects, eliminating pointer indirection and reducing memory overhead. This is particularly beneficial for collections of small data objects, such as points or complex numbers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language)</a></li>
<li><a href="https://openjdk.org/projects/valhalla/">Project Valhalla</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS - Inside.java</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about readability and uniformity, with some arguing that value classes break the principle of least surprise because assignment behavior differs from reference classes. Others defended the design, noting that Java has evolved significantly and that value types offer substantial performance benefits.

**Tags**: `#Java`, `#JVM`, `#Project Valhalla`, `#Programming Languages`, `#Performance`

---

<a id="item-4"></a>
## [MosaicLeaks: Privacy Risks in AI Research Agents](https://huggingface.co/blog/ServiceNow/mosaicleaks) ⭐️ 8.5/10

ServiceNow's Hugging Face blog introduces MosaicLeaks, a benchmark designed to evaluate privacy vulnerabilities in AI research agents, revealing that many agents inadvertently leak sensitive information from user queries. As AI research agents become widely used for automated data gathering and analysis, this benchmark highlights critical privacy risks that could expose confidential data, impacting users and organizations that rely on these tools for sensitive tasks. The MosaicLeaks benchmark systematically tests research agents by crafting queries that include private information and monitoring how the agents handle it, revealing that many agents fail to redact or protect such data in their outputs and internal logs.

rss · Hugging Face Blog · Jun 18, 18:13

**Background**: AI research agents are systems that can perform multi-step web browsing, document analysis, and report generation autonomously. Privacy vulnerabilities in these agents can arise from prompt injection, data retention, and insufficient output sanitization, similar to other LLM-based applications.

**Tags**: `#AI`, `#LLM`, `#privacy`, `#agent security`

---

<a id="item-5"></a>
## [Benchmarking Open Models for Agentic Capabilities](https://huggingface.co/blog/is-it-agentic-enough) ⭐️ 8.5/10

Hugging Face released a guide on benchmarking open-source LLMs for agentic capabilities using custom tooling and evaluation frameworks. As agentic AI gains traction, a standardized benchmarking approach for open models helps developers select the right model for tool use, planning, and autonomous tasks. The guide covers practical steps to set up evaluations for tool use, multi-step reasoning, and agentic workflows, emphasizing customization for specific use cases.

rss · Hugging Face Blog · Jun 18, 00:00

**Background**: Agentic AI refers to language models that can independently plan, use tools, and execute multi-step tasks to achieve goals. Unlike standard chatbots, agentic systems require robust benchmarking for reliability. Open models lack standardized agentic benchmarks, making this guide valuable for the community.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Comparison_of_agentic_capabilities_in_major_LLM_vendors_2026">Comparison of agentic capabilities in major LLM vendors (2026)</a></li>
<li><a href="https://benchlm.ai/agentic">Agentic Benchmarks 2026: Tool Use, Browsing, Computer Use</a></li>
<li><a href="https://artificialanalysis.ai/models/capabilities/agentic">Agentic Index - Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Agentic AI`, `#LLM`, `#Benchmarking`, `#Open Models`

---

<a id="item-6"></a>
## [GLM-5.2: Leading Open-Weight LLM with 1M Context](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 8.4/10

Z.ai released GLM-5.2, a 753B parameter Mixture-of-Experts model with 1 million token context window, under MIT license on June 16, 2026. It has become the top-ranked open-weights model on the Artificial Analysis Intelligence Index with a score of 51, surpassing MiniMax-M3 and DeepSeek V4 Pro. This demonstrates that open-weights models continue to close the gap with proprietary models, offering cost-effective alternatives. GLM-5.2's strong performance in coding and reasoning tasks, combined with its MIT license, could accelerate AI adoption in research and production. GLM-5.2 uses 40 active parameters via MoE, requires 1.51TB of storage, and has a context window expanded from 200k to 1M tokens compared to its predecessor. It is text-only, with vision capabilities available separately in GLM-5V-Turbo (not open-weights).

rss · Simon Willison · Jun 17, 23:58

**Background**: Large Language Models (LLMs) are neural networks trained on vast text data to generate human-like text. Mixture of Experts (MoE) is an architecture that activates only a subset of parameters per input, enabling large model sizes with efficient computation. The context window determines how much text the model can consider at once; a 1M token window allows processing entire books or very long documents in one go.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.innovatrixinfotech.com/blog/context-windows-explained-1-million-tokens-architecture">1 Million Token Context Window: What It Means for Builders | Innovatrix Infotech</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open weights`, `#GLM`, `#AI research`, `#artificial intelligence`

---

<a id="item-7"></a>
## [Interview with Michael Morton on AI & E-Commerce](https://stratechery.com/2026/an-interview-with-michael-morton-about-e-commerce-in-the-age-of-ai/) ⭐️ 8.3/10

In an interview on Stratechery, Michael Morton discusses how AI is transforming e-commerce, covering topics such as unfalsifiable bear cases, distribution versus referral models, and the challenges of grocery delivery and autonomous vehicles. This interview provides strategic insights from an expert on how AI reshapes e-commerce distribution models and addresses long-standing industry challenges like grocery profitability. It offers valuable perspective for anyone involved in e-commerce strategy and AI adoption. The interview specifically examines unfalsifiable bear cases—pessimistic scenarios that cannot be disproven—and contrasts distribution models (where a company owns inventory) with referral models (where it connects customers to sellers). It also delves into the unique difficulties of grocery e-commerce and the potential of autonomous vehicles.

rss · Stratechery · Jun 18, 10:00

**Background**: An 'unfalsifiable bear case' refers to a pessimistic claim that cannot be proven false, a concept derived from Karl Popper's falsifiability principle. In e-commerce, distribution models involve direct ownership of inventory and logistics, while referral models generate leads or sales through third-party referrals without holding stock. Understanding these distinctions is crucial for evaluating business strategies in the AI era.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falsifiability">Falsifiability - Wikipedia</a></li>
<li><a href="https://awealthofcommonsense.com/2020/08/bull-case-bear-case/">Bull Case / Bear Case - A Wealth of Common Sense</a></li>
<li><a href="https://www.salesforce.com/sales/distribution-channels/">Distribution Channels: Types, Examples, and Benefits</a></li>

</ul>
</details>

**Tags**: `#AI`, `#e-commerce`, `#strategy`, `#interview`, `#Michael Morton`

---

<a id="item-8"></a>
## [Claude Code v2.1.183 Adds Safety Blocks for Destructive Commands](https://github.com/anthropics/claude-code/releases/tag/v2.1.183) ⭐️ 8.0/10

Claude Code v2.1.183 introduces safety blocks for destructive git commands like git reset --hard and git clean -fd, as well as terraform destroy/pulumi destroy/cdk destroy, unless the user explicitly requested them. It also adds model deprecation warnings on stderr, a new /config --help command, and several bug fixes. This update significantly improves safety for developers using Claude Code, preventing accidental loss of work and infrastructure destruction. It demonstrates Anthropic's commitment to responsible AI tooling and addresses common pain points in agentic coding workflows. Destructive git commands are blocked when the user did not ask to discard local work, and git commit --amend is blocked if the commit wasn't made by the agent this session. The model deprecation warning now also covers models set in agent frontmatter, not just those in print mode.

github · ashwin-ant · Jun 19, 01:20

**Background**: Claude Code is an AI-powered coding assistant from Anthropic that operates in the terminal, IDE, and browser, capable of reading codebases, editing files, and running commands. As an agentic coding system, it can perform destructive operations like git resets or infrastructure teardowns, making safety measures critical. The update also addresses various bugs in subagent spawning, terminal rendering, and MCP server authentication.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://developer.hashicorp.com/terraform/cli/commands/destroy">terraform destroy command reference | Terraform | HashiCorp ...</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI tools`, `#safety`, `#git`, `#Anthropic`

---

<a id="item-9"></a>
## [Anjney Midha Interview: The Professor of Outputmaxxing](https://www.latent.space/p/anj) ⭐️ 8.0/10

Anjney Midha, a venture capitalist at AMP, shares his journey from Singapore to leading investments in Anthropic, Mistral, Black Forest Labs, and Periodic Labs, along with AMP's secret master plan. This interview offers rare insider perspectives on key AI startup investments, revealing the strategies behind some of the most influential companies in the space. The interview covers Midha's humble beginnings in Singapore and his role in funding high-profile AI startups like Anthropic and Mistral, teasing an undisclosed 'secret master plan' from AMP.

rss · Latent Space · Jun 18, 17:30

**Background**: Anjney Midha is a venture capitalist at AMP, a firm that has invested in multiple prominent AI companies. Anthropic and Mistral are leading AI startups focused on developing advanced large language models. Black Forest Labs and Periodic Labs are also part of AMP's portfolio, though they are less well-known.

**Tags**: `#AI`, `#Venture Capital`, `#Anthropic`, `#Mistral`, `#Startups`

---

<a id="item-10"></a>
## [ATProto Has No Instances, Explains Dan Abramov](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.9/10

Dan Abramov published a blog post explaining that ATProto does not have 'instances' like Mastodon, instead separating roles into Personal Data Servers (PDS), Relays, and AppViews. This clarification is important for developers and users exploring decentralized social protocols, as it highlights a fundamental architectural difference between ATProto and ActivityPub-based systems like Mastodon. The blog uses an RSS analogy: PDS is like the feed source, Relay is like the feed reader's aggregation, and AppView is like the reader's display. This contrasts with Mastodon where a single 'instance' handles all these roles.

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: ATProto (Authenticated Transfer Protocol) is the decentralized protocol powering Bluesky. Unlike ActivityPub's federated model where each server (instance) hosts accounts and content, ATProto separates data storage (PDS), indexing (Relay), and application logic (AppView). This separation aims to improve scalability and user control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://github.com/bluesky-social/atproto/discussions/3036">Relay Operational Updates · bluesky-social/atproto · Discussion #3036</a></li>

</ul>
</details>

**Discussion**: Community comments were mixed: some appreciated the clarity but disagreed with the RSS analogy, noting that blogs are more self-sufficient than ATProto's components. Others praised the separation of concerns as a scalable design. There was also frustration that the article didn't address how ATProto solves problems like defederation.

**Tags**: `#ATProto`, `#Bluesky`, `#decentralized protocols`, `#federation`

---

<a id="item-11"></a>
## [Datasette Apps: Host Sandboxed HTML+JS Apps Inside Datasette](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.8/10

Simon Willison announced datasette-apps, a new plugin for the open-source Datasette tool that allows users to host and run custom HTML+JavaScript applications inside a sandboxed iframe, with the ability to execute read-only and optionally write SQL queries against the underlying data. This plugin extends Datasette from a data exploration tool into a full-fledged application platform, enabling developers to build interactive data-driven web apps directly within Datasette without compromising security. It also reuses the sandboxing pattern from Claude Artifacts, making it a practical model for safe third-party app hosting. Apps run in an iframe with sandbox="allow-scripts allow-forms" and an injected Content Security Policy that blocks outbound HTTP requests, preventing data exfiltration. The plugin also provides a plugin hook for other plugins to add their own Python apps.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, built on top of SQLite. It provides a JSON API and a web interface for querying databases. The datasette-apps plugin allows developers to embed custom HTML+JavaScript frontends that interact with that API, similar to how Claude Artifacts works but within the Datasette ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps: Host custom HTML applications inside Datasette</a></li>
<li><a href="https://github.com/datasette/datasette-apps">GitHub - datasette/datasette-apps: Apps that live inside Datasette · GitHub</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#plugin`, `#SQL`, `#web applications`, `#developer tools`

---

<a id="item-12"></a>
## [Norway bans AI for elementary students](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 7.6/10

Norway announced a near-total ban on AI use for elementary students aged 6-13, and limited supervised use for lower secondary students aged 14-16, as a general rule starting from 2026. The policy aims to protect foundational learning skills like reading, writing, and comprehension, which generative AI could undermine. It sets a significant precedent for AI regulation in education globally. The ban applies to students in 1st through 7th grade as a general rule, with teachers given discretion for exceptions. For older students, AI tools are allowed only under careful supervision.

hackernews · ilreb · Jun 19, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48600093)

**Background**: Norway's education system emphasizes foundational skills in early years. There is growing concern that AI tools like chatbots may hinder the development of critical thinking and core competencies. Similar debates are happening in other countries over AI in classrooms.

**Discussion**: The Hacker News comments generally support the ban, with users comparing it to withholding calculators until arithmetic is understood. Some highlight the risk of teachers themselves misusing AI to generate incorrect exercises. However, one user questions how AI is actually used by younger students in practice.

**Tags**: `#AI regulation`, `#education`, `#Norway`, `#LLM policy`, `#technology in schools`

---

<a id="item-13"></a>
## [ALS patient becomes first long-term BCI power user](https://www.technologyreview.com/2026/06/19/1139270/brain-computer-interface-trials-are-taking-off/) ⭐️ 7.6/10

Casey Harrell, an ALS patient, has become the first long-term 'power user' of a brain-computer interface, using the implant to communicate for nearly three years. This milestone demonstrates that BCIs can provide sustained functional benefits for severely paralyzed patients, paving the way for wider clinical adoption and improved quality of life. Harrell is paralyzed and unable to speak without the device; researchers consider him the first 'power user' due to his extensive daily usage over three years.

rss · MIT Tech Review · Jun 19, 09:00

**Background**: A brain-computer interface (BCI) is a system that decodes neural signals to control external devices, often used to restore communication or movement for people with paralysis. ALS (amyotrophic lateral sclerosis) progressively destroys motor neurons, leading to loss of voluntary muscle control. The trial highlights advances in BCI durability and usability.

**Tags**: `#brain-computer interface`, `#neuroscience`, `#ALS`, `#medical technology`, `#neural implants`

---

<a id="item-14"></a>
## [Stratechery Roundup on Anthropic and AI E-commerce](https://stratechery.com/2026/the-stuff-of-mythos/) ⭐️ 7.5/10

Ben Thompson's Stratechery published a weekly roundup on June 15, 2026, highlighting articles on AI company Anthropic, the impact of AI on e-commerce, and a perfect 10 analysis of the NBA Finals. The roundup offers a concentrated dose of analysis on critical AI developments, particularly Anthropic's focus on safety, and the evolving e-commerce landscape, making it valuable for tech professionals and investors. The roundup format means the content is a curated list rather than a single in-depth article; the NBA Finals commentary is noted as scoring a perfect 10, indicating a highly favorable review.

rss · Stratechery · Jun 19, 17:00

**Background**: Stratechery is a subscription-based analysis site by Ben Thompson, covering tech industry strategy. Anthropic is an AI research company focused on building safe and interpretable AI systems, including the Claude model. The roundup reflects Thompson's interest in high-impact AI applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#e-commerce`, `#Ben Thompson`, `#Stratechery`

---

<a id="item-15"></a>
## [Vercel AI SDK Workflow Fixes Provider-Executed Tool Approval Bug](https://github.com/vercel/ai/releases/tag/%40ai-sdk/workflow%401.0.0-beta.100) ⭐️ 7.2/10

Vercel released @ai-sdk/workflow@1.0.0-beta.100, which fixes a bug where provider-executed tool approvals were not forwarded to the provider on resume. This fix ensures that provider-executed tools (e.g., MCP via OpenAI Responses API) receive approval signals correctly, preventing silent failures. Developers relying on the AI SDK for agent workflows will experience more reliable tool execution. The bug occurred because WorkflowAgent stripped all tool-approval-request and tool-approval-response messages on resume, regardless of whether the tool was locally or provider-executed. Local approvals are still stripped, but provider-executed approvals are now preserved and forwarded.

github · github-actions[bot] · Jun 18, 21:56

**Background**: Vercel's AI SDK provides a unified API for building AI-powered applications, including tool calling capabilities. In agent workflows, tools can require user approval before execution, and this approval can be handled locally or by the provider (e.g., OpenAI). The Model Context Protocol (MCP) allows providers to execute tools remotely. This fix aligns the workflow behavior with the streamText discriminator core logic.

<details><summary>References</summary>
<ul>
<li><a href="https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling">AI SDK Core: Tool Calling</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/tools-connectors-mcp">MCP and Connectors | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#AI SDK`, `#workflow`, `#tool approval`, `#bug fix`, `#Vercel`

---