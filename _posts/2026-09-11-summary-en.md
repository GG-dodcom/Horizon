---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 108 items, 14 important content pieces were selected

---

1. [Terry Tao Warns of a Severe Misalignment of AI in Mathematics](#item-1) ⭐️ 8.8/10
2. [Benchmarks challenge RTK's claimed token savings for AI coding](#item-2) ⭐️ 8.3/10
3. [Measuring the sloppiness of code: metrics to guide AI coding agents](#item-3) ⭐️ 8.2/10
4. [Shopify moves back to native Swift and Kotlin, citing AI agents](#item-4) ⭐️ 8.2/10
5. [OpenRouter auto-routing can make one model behave differently](#item-5) ⭐️ 8.0/10
6. [Rebuilding AUTOMATIC1111 WebUI with Gradio Workflow](#item-6) ⭐️ 8.0/10
7. [Stratechery: Apple's Belief in App Primacy Is Its AI Blindspot](#item-7) ⭐️ 8.0/10
8. [trynix.dev boots any Nix package in a browser VM](#item-8) ⭐️ 7.9/10
9. [OpenAI claims AI agents found Navier-Stokes counterexample, sparking credit dispute](#item-9) ⭐️ 7.7/10
10. [Dev finds 60% of $220 Google Ads app installs were bots](#item-10) ⭐️ 7.4/10
11. [Calif Research Claims AI-Built Zero-Click WeChat Call Worm](#item-11) ⭐️ 7.4/10
12. [Rune, a hackable Go-based terminal editor, goes open source](#item-12) ⭐️ 7.2/10
13. [OpenAI scales Habitat storage to 1B ChatGPT users at 22M req/s](#item-13) ⭐️ 7.0/10
14. [Ruan Yifeng's Weekly #412: Ban Issues, Accept Only Pull Requests](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Terry Tao Warns of a Severe Misalignment of AI in Mathematics](https://mathandai.org/) ⭐️ 8.8/10

On September 11, 2026, Fields Medalist Terry Tao published a blog post titled "A severe misalignment of AI in mathematics," arguing that AI-generated proofs threaten mathematics' epistemic foundations. Around the same time, The Economist reported that top mathematicians are outraged by OpenAI's methods, and the topic drew 549 points and 612 comments on Hacker News. The debate goes beyond tooling: if machines can produce proofs of open problems faster than humans can verify them, the long-standing yardstick used to measure mathematical contribution — solving famous open problems — loses its meaning, and credit, careers, and funding may be reallocated on a new and contested basis. It also raises broader questions about how every knowledge-producing field will handle machine-generated results it cannot fully comprehend. Commenters noted that this is not a wholly new problem: Shinichi Mochizuki's 2012 abc conjecture proof was similarly vast and opaque, producing years of skepticism, conferences, and failed verification attempts rather than a clean resolution. The discussion also stressed that the capability itself is already out in the open, so the real problem is not stopping the models but rebuilding systems for assigning credit and validating understanding.

hackernews · meredydd · Sep 11, 17:45 · [Discussion](https://news.ycombinator.com/item?id=49662371)

**Background**: Mathematics has traditionally relied on peer review and human-readable proofs: a result counts as established only when other mathematicians can follow the argument and verify it. Terry Tao is one of the most prominent living mathematicians and has written extensively about how AI and proof assistants such as Lean are changing mathematical practice. Recent advances in large language models have let systems tackle competition problems and assist with formalization, which is why claims of AI solving major open problems now carry real weight.

**Discussion**: Sentiment was divided but substantive. Several mathematicians and engineers pushed back on the pessimism: tmhn2 compared the situation to Mochizuki's abc conjecture, noting that opaque proofs still generated conferences, papers, and partial understanding, while gwd likened the panic to 1990s fears that computers would ruin chess — a game that is now more popular and better played than ever. jeremysalwen argued that AI has not destroyed mathematicians' ability to understand and share ideas, only the yardstick of solving open problems, and david-gpu drew an analogy to Baudelaire's 19th-century dismissal of photography as the mechanical refuge of failed painters.

**Tags**: `#AI`, `#mathematics`, `#LLM`, `#AI alignment`, `#epistemics`

---

<a id="item-2"></a>
## [Benchmarks challenge RTK's claimed token savings for AI coding](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/) ⭐️ 8.3/10

Quesma published a benchmark-based blog post arguing that RTK's reported token savings do not translate into real AI-coding cost reductions, despite RTK's advertised 60–90% reductions. The post sparked a Hacker News debate about how `rtk gain` accounts for saved tokens. Many developers are adopting CLI proxies and context-compression tricks to control the rising cost of coding agents, so a credible benchmark that contradicts a popular tool's savings claims can change tooling and procurement decisions. It also underscores the need for independent, end-to-end cost benchmarks rather than self-reported token counts. RTK is a single Rust binary that sits between the shell and the LLM, compressing command output before it enters the context window. A key criticism is that `rtk gain` can count a command that prints 100k tokens but is piped to `tail -5` as 100k tokens saved even though the model only sees five lines, and its default persistence of savings stats can break sandboxing and trigger auto-mode denials.

hackernews · michalwarda · Sep 11, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49656471)

**Background**: RTK (Rust Token Killer) is an open-source CLI proxy that intercepts common developer commands and compresses their output before sending it to an AI coding agent, with claims of cutting up to 90% of token noise. AI coding agents spend a large share of their API budget on tool outputs, so reducing tokens can lower costs if the compression preserves enough information for the model. However, self-reported savings can be misleading when they measure pre-compression output rather than the actual tokens billed by the model.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/rtk-ai/rtk">GitHub - rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies · GitHub</a></li>
<li><a href="https://www.rtk-ai.app/">RTK — Rust Token Killer</a></li>
<li><a href="https://dev.to/arshtechpro/how-rtk-reduces-llm-token-usage-for-ai-coding-agents-2kfd">RTK: Cut Your AI Coding Bill by 80% With One CLI Tool - DEV Community</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely skeptical: aeneas_ory called these token-saving hacks 'snakeoil' and reported better results from indexing a codebase with a local embedding model, while monneyboi uses treesitter to build file and directory outlines. oefrha said the flaw is obvious from `rtk gain` output because commands piped to `tail -5` are counted as full savings, and ProjectBarks argued these tools are mostly vaporware and called for independent benchmarks. gillesjacobs summarized cost-per-attempt comparisons with and without RTK, though the quoted figures were incomplete.

**Tags**: `#AI coding agents`, `#LLM cost optimization`, `#benchmarking`, `#developer tooling`, `#token usage`

---

<a id="item-3"></a>
## [Measuring the sloppiness of code: metrics to guide AI coding agents](https://earendil.com/posts/measuring-code-sloppiness/) ⭐️ 8.2/10

An article on earendil.com titled "If coding is solved, what now?: Measuring the sloppiness of code" proposes quantitative metrics for evaluating code sloppiness — such as verbosity, duplication, erosion and complexity — specifically as feedback signals for AI agents that generate code at scale. It argues that while LLMs produce formally correct code, they introduce unprecedented levels of verbosity and duplication that agents themselves cannot manage, and concludes that human intuition and taste remain implicitly or explicitly baked into any such evaluation. As AI coding agents move from autocomplete to autonomously planning and refactoring across multi-file codebases, teams need objective ways to measure whether generated code is merely correct or actually maintainable. This work sits at the intersection of two hot areas — agentic AI systems and software engineering quality — and could inform how agent feedback loops, code review tooling and cost models (token spend vs. human maintenance) are designed going forward. The author explicitly notes that metrics for code sloppiness are hard to define objectively because human intuition and taste are unavoidably part of the evaluation, and flags promising unexplored directions such as coupledness of functions, code churn and cohesion. The discussion also touches on a practical caveat: with unlimited token spend on frontier models, coding may look "solved," but per-token enterprise pricing can quickly make human developers the more cost-effective option.

hackernews · doppp · Sep 11, 13:42 · [Discussion](https://news.ycombinator.com/item?id=49658311)

**Background**: LLM-based coding agents are tools that can autonomously write, modify, debug and refactor code across multiple files, going well beyond simple autocompletion. Traditional software engineering already has the concept of "code smells" — design weaknesses that are not bugs but signal technical debt and future maintenance risk — yet these are usually judged by human reviewers rather than measured numerically. This article asks what happens when the primary producer of code is an agent rather than a person, and tries to turn fuzzy notions of "slop" into something an agent could optimize against.

<details><summary>References</summary>
<ul>
<li><a href="https://earendil.com/posts/measuring-code-sloppiness/">If coding is solved, what now?: Measuring the sloppiness of ...</a></li>
<li><a href="https://news.lavx.hu/article/if-coding-is-solved-what-now-measuring-the-sloppiness-of-code">If coding is solved, what now?: Measuring the sloppiness of code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code_smell">Code smell - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly welcomed the quantitative approach to agent feedback, with dherman arguing that the sloppiness problems that really matter are global properties rather than local ones, since both agents and humans have finite attention and can fix local messiness on a by-need basis. conqrr pushed back on the framing that coding is "solved," noting that coding is also the process of distributing a shared mental model across a team, and asking who holds that model if humans are kept out of the loop. toddwprice added a cost angle: frontier-model token spend may make coding look solved until enterprise per-token pricing forces teams back to "sane" cost levels where human developers can be more cost-effective.

**Tags**: `#code quality`, `#AI agents`, `#software engineering`, `#metrics`, `#technical debt`

---

<a id="item-4"></a>
## [Shopify moves back to native Swift and Kotlin, citing AI agents](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.2/10

Shopify announced it is moving its mobile apps from React Native back to separate native Swift (iOS) and Kotlin (Android) codebases, saying that AI agents can now handle enough implementation, translation, testing, and review work that maintaining two codebases is no longer the deciding cost factor it was in 2020. As part of the shift, the company's react-native-skia and flash-list libraries are being handed to new maintainers, while restyle will be archived at the end of 2026 because it "has a smaller user base than our other libraries." This is a concrete, real-world signal that coding agents are reshaping the fundamental build-versus-buy and platform-choice economics of software engineering, not just speeding up individual tasks. If a company as large as Shopify reverses a well-known 2020 cross-platform decision on these grounds, other engineering organizations are likely to revisit their own framework choices, with knock-on effects for the React Native ecosystem and the libraries it depends on. Shopify was a significant React Native contributor, maintaining three notable libraries: react-native-skia, flash-list, and restyle; the first two are being re-homed and restyle will be archived at the end of 2026. Shopify's post explicitly credits React Native as a great platform across the six years it was used, so the reversal is framed as an economics calculation rather than a rejection of the technology or a claim that native is now cheaper in raw engineering terms.

rss · Simon Willison · Sep 10, 21:11

**Background**: React Native is Meta's open-source framework that lets developers write UI and logic once in JavaScript/React and run it on both iOS and Android, which avoids duplicating features across two platforms. The alternative, native development, means writing separate codebases in Swift (Apple's language for iOS) and Kotlin (the dominant language for Android), which delivers the best platform fidelity but requires building and maintaining everything twice. Cross-platform frameworks were widely adopted through the 2010s and 2020s precisely to cut that duplication cost. AI coding agents built on large language models can now generate implementations, port code between languages, write tests, and review pull requests, which is the specific change Shopify says shifts the tradeoff.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://kotlinlang.org/docs/multiplatform/native-and-cross-platform.html">Cross-platform and native app development: How do you choose?</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_software_development">AI-assisted software development - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software engineering`, `#mobile development`, `#React Native`, `#developer tooling`

---

<a id="item-5"></a>
## [OpenRouter auto-routing can make one model behave differently](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 8.0/10

Simon Willison highlighted Mohamed Moustafa's blog post "So you want to use OpenRouter?", which warns that OpenRouter's automatic provider routing can silently send requests for the same model ID to different backend providers — each running different serving software, optimizations and settings — so the identical endpoint can produce behaviorally different results. The post points to OpenRouter's provider.only option as the fix, with the /endpoints method listing which providers are available for a given model ID. Developers who build on OpenRouter for its automatic fallbacks and cost optimization may unknowingly get non-reproducible outputs, which is a serious problem for evaluations, agent pipelines, structured-output parsing and any application where consistent behavior matters. It also highlights a broader tension in the multi-provider LLM gateway model: a unified API hides real infrastructure differences that can leak into product behavior. The inconsistencies cited include different serving software and optimization settings across providers, some providers lacking vision capability even for vision-capable models, and differing handling of the reasoning effort parameter. To pin behavior, you can restrict routing with provider.only and enumerate the providers backing a model through the /endpoints method before choosing one.

rss · Simon Willison · Sep 11, 22:49

**Background**: OpenRouter is a gateway that exposes many LLMs behind a single OpenAI-compatible API, advertising automatic fallbacks and routing to the most cost-effective backend for each request. Under the hood it aggregates third-party inference providers, each of which may run its own copy of a model with distinct quantization, serving frameworks (such as vLLM or TensorRT-LLM-style stacks) and feature support. The reasoning effort parameter is a common knob in modern reasoning models that trades latency and cost for how much internal "thinking" the model does before answering, so inconsistent handling of it changes both output quality and price.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/docs/guides/routing/provider-selection">Provider Routing - Smart Multi-Provider Request ... - OpenRouter</a></li>
<li><a href="https://or.vh.brainex.co/blog/insights/model-routing/">How OpenRouter Model Routing Works: Providers , Fallbacks & Auto ...</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/reasoning-effort">Reasoning effort - LLM Parameter Guide - Vellum</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#OpenRouter`, `#AI infrastructure`, `#API routing`, `#LLM inference`

---

<a id="item-6"></a>
## [Rebuilding AUTOMATIC1111 WebUI with Gradio Workflow](https://huggingface.co/blog/gradio-workflow-1111) ⭐️ 8.0/10

Hugging Face published a technical walkthrough that reimplements the AUTOMATIC1111 (A1111) Stable Diffusion WebUI using Gradio Workflow, demonstrating how to decompose a monolithic generative-AI interface into modular, connected pipelines. The post is a hands-on, code-oriented guide rather than a new product or model release. A1111 is one of the most widely used open-source image-generation front ends, so showing how its functionality maps onto a workflow framework gives developers a reusable pattern for building and refactoring generative-AI UIs. It also signals Gradio's push beyond single-function demos toward multi-step, composable AI applications. In Gradio's workflow model, every workflow app is still a Gradio app that exposes its connected pipelines through the standard Gradio REST API, with each disconnected pipeline containing one or more output nodes getting its own endpoint. That means the modular design in the walkthrough should remain programmatically callable, though a reimplementation is unlikely to cover A1111's large third-party extension ecosystem out of the box.

rss · Hugging Face Blog · Sep 10, 00:00

**Background**: AUTOMATIC1111 Stable Diffusion Web UI, often called SD WebUI or simply A1111, is an open-source program released in August 2022 by an anonymous GitHub developer known as AUTOMATIC1111; it generates images from text prompts using Stable Diffusion as its base model, plus a wide set of extensions and customization features. Gradio is a Python library for building machine-learning web UIs, and its Workflow capability lets developers chain several models or processing steps into connected pipelines instead of one monolithic function. Related tooling such as gradio-app/daggr—inspired by orchestrators like Airflow and Prefect but aimed at interactive AI/ML prototyping—reflects the same trend toward visually inspectable, step-by-step pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AUTOMATIC1111_Stable_Diffusion_Web_UI">AUTOMATIC1111 Stable Diffusion Web UI</a></li>
<li><a href="https://gradio.app/guides/workflows">Workflows</a></li>
<li><a href="https://github.com/gradio-app/daggr">GitHub - gradio-app/daggr: Chain apps and models to build robust AI workflows 🤗</a></li>

</ul>
</details>

**Tags**: `#Gradio`, `#Stable Diffusion`, `#AI tooling`, `#developer tools`, `#generative AI`

---

<a id="item-7"></a>
## [Stratechery: Apple's Belief in App Primacy Is Its AI Blindspot](https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/) ⭐️ 8.0/10

Ben Thompson published a Stratechery analysis of Apple's September 2026 product event, covering the "iPhone Duo," the company's positioning of the iPhone as an "intelligent personal hub," and the new Apple Watch "Audio Intelligence" features. His core argument is that Apple's hardware-software integration remains unmatched, but that its belief in the primacy of apps is its biggest AI blindspot. The critique targets the fault line between Apple's app-centric worldview and agentic AI, which pursues goals across services rather than waiting for a user to open and operate a single app. If Apple keeps treating apps as the atomic unit of computing, it risks ceding the assistant layer — and the user relationship that comes with it — to rivals, even while its devices remain the best hardware for AI. The Stratechery piece is largely paywalled, so only its teaser line — that Apple's app-centric worldview is its AI blindspot — is publicly available, and the full argument cannot be summarized here. It lands alongside concrete announcements: Apple markets the iPhone 18 Pro and Pro Max as an "intelligent personal hub," and Audio Intelligence on Apple Watch Series 12 and Apple Watch Ultra 4 uses the watch's microphones with on-device and cloud-based models to detect sounds, identify music, and surface missed conversational moments.

rss · Stratechery · Sep 10, 10:00

**Background**: Apple's historical advantage is vertical integration: by controlling its own silicon, operating system, and hardware together, it delivers performance and privacy that more fragmented competitors struggle to match. Its business model, however, was built around apps as discrete destinations — the App Store, and Apple Intelligence features such as writing tools and notification summaries, all live inside individual apps. Agentic AI inverts that model: a language model runs in a loop, choosing actions and calling tools across services to accomplish a goal without step-by-step human approval, which makes the app boundary look more like a constraint than a feature. Apple executives, including CEO John Ternus, frame the iPhone as the ideal "intelligent personal hub" with broad personal context, which is precisely the claim Thompson is testing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.computerworld.com/article/4220404/the-iphone-is-now-apples-intelligent-personal-hub.html">The iPhone is now Apple’s ‘intelligent personal hub’</a></li>
<li><a href="https://techcrunch.com/2026/09/09/apple-ceo-john-ternus-says-the-best-ai-device-is-still-the-iphone/">Apple CEO John Ternus says the best AI device is still the ...</a></li>
<li><a href="https://remolda.com/en/glossary/agentic-ai">Agentic AI — definition | Remolda</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI Strategy`, `#Product Management`, `#Hardware-Software Integration`, `#Agentic AI`

---

<a id="item-8"></a>
## [trynix.dev boots any Nix package in a browser VM](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 7.9/10

Farid Zakaria launched trynix.dev, which Simon Willison describes as a "magnum opus" of Nix work: it runs an x86_64 Linux virtual machine entirely inside the browser via qemu-wasm (QEMU compiled to WebAssembly), and that VM can be booted with any Nix package built over the past 13 years. Packages are URL-addressable — visiting https://trynix.dev/?pkg=python3%403.6.2 and clicking "Load" yields an interactive shell running Python 3.6.2 from 2017. Zakaria has also published trynix-preview, a GitHub Action that comments a trynix.dev boot link on a pull request so reviewers can boot the PR's build with no servers involved. It collapses the usual gap between "this build worked in 2017" and "let me actually run it": reproducibility, legacy-environment testing, and PR review become a browser tab instead of a container or cloud VM. Because it is URL-addressable and needs no server, it could reshape how open-source projects let contributors and reviewers validate changes, and it is a striking demonstration of how far WebAssembly-based virtualization has come. The Nix package manager's content-addressed store is what makes this feasible: each package version has a stable, hash-derived path, so a URL can point unambiguously at Python 3.6.2 or any other historical build. qemu-wasm itself is explicitly described by its author as experimental software, so performance and compatibility caveats apply, and booting a full VM in the browser implies a non-trivial download and startup cost before the shell appears.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a package manager and build system that derives every package from a pure function of its dependencies, storing results in uniquely named directories under /nix/store. That design eliminates dependency conflicts and makes builds reproducible and bit-for-bit verifiable, which is why historical versions remain installable years later. WebAssembly is a low-level, assembly-like bytecode format that runs at near-native speed inside browsers (and other hosts), letting large C/C++ codebases like QEMU be compiled to run on the web. qemu-wasm applies that idea to QEMU, the widely used open-source machine emulator and virtualizer, so a full x86_64 Linux guest can execute in a browser tab.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager) - Wikipedia</a></li>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly - MDN</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#DevTools`, `#Reproducibility`, `#Virtualization`

---

<a id="item-9"></a>
## [OpenAI claims AI agents found Navier-Stokes counterexample, sparking credit dispute](https://www.solidot.org/story?sid=85339) ⭐️ 7.7/10

OpenAI announced this week that roughly 10,000 AI agents running for 88 hours found, on September 5, a special case in which the Navier-Stokes equations break down, and it claims this is the first time AI has solved a major mathematical problem. The claim quickly became contentious: NYU mathematician Tristan Buckmaster and Anthropic researcher Levent Alpöge, who had made significant progress on the problem over the past month using OpenAI and Anthropic tools, allege that OpenAI used their unpublished results without credit and scraped their data for training. If confirmed, this would be the first time an AI system resolved a major open mathematics problem — and one of the Clay Mathematics Institute's Millennium Prize Problems — which would be a landmark for AI-assisted mathematical research. The accompanying dispute also pushes questions about training-data provenance, researcher credit, and the ethics of using unpublished work to the center of the AI research community. OpenAI says it spent millions of dollars of compute on the push and denies relying on Buckmaster and Alpöge's latest results, while Buckmaster has publicly disputed that account and the NYU team accuses OpenAI of scraping its data; the result itself has not yet been verified through peer review. The same news roundup also covers a separate report that LG smart TVs continue to record and upload user data even when offline or in standby, which LG denies, saying it only processes voice data after the remote's voice button is pressed or a 'Hi LG' wake word is detected, and that its Automatic Content Recognition (ACR) feature is opt-in.

rss · Solidot · Sep 10, 15:51

**Background**: The Navier-Stokes equations, proposed roughly 200 years ago by French physicist Claude-Louis Navier and Irish physicist George Stokes, describe the motion of fluids such as liquids and air and are still widely used today. In 2000 the Clay Mathematics Institute named the question of whether smooth solutions always exist — the existence and smoothness problem — as one of its seven Millennium Prize Problems, each carrying a $1 million prize. An 'AI agent' (agentic AI) refers to an AI program that can pursue goals, use software or other tools, and take actions with some degree of autonomy, as opposed to a narrow, single-task chatbot.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Navier-Stokes`, `#agentic systems`, `#research ethics`, `#privacy`

---

<a id="item-10"></a>
## [Dev finds 60% of $220 Google Ads app installs were bots](https://dayzlegame.com/blog/google-ads-bot-farm/) ⭐️ 7.4/10

A developer published a blog post documenting an investigation into a $220 Google app-install ad campaign, concluding that roughly 60% of the resulting installs came from bots rather than real users. The post, discussed widely on Hacker News, is notable for pairing a small, concrete spend figure with data-driven evidence of fraud rather than general speculation. Ad fraud directly burns the budgets of indie developers and early-stage startups who rely on paid installs to bootstrap growth, and this case shows even a modest $220 campaign can be majority fake. It adds pressure on Google and other ad platforms to explain how much invalid traffic escapes their filters, and it reinforces skepticism toward CPI-based user acquisition as a growth strategy. The analysis is largely anecdotal rather than statistically rigorous, but the Hacker News thread supplied concrete mitigations: one commenter recommends pulling the offending IPs from the dashboard and blocking entire network or data-center ranges via Google Ads > Admin > Account Settings > IP Exclusions, noting their own list now exceeds 4000 blocked networks in the US alone. Another commenter recounted the ironic case of a developer whose AdMob account was banned for invalid traffic shortly after buying Google Ads to promote the very same app.

hackernews · nickabe · Sep 11, 18:24 · [Discussion](https://news.ycombinator.com/item?id=49662990)

**Background**: Mobile ad fraud commonly takes the form of click injection, where a malicious app detects a fresh installation and fires a fake click to steal attribution credit, or device/bot farms, where dozens or hundreds of real phones on real networks generate fake installs and engagement that basic filters miss because the traffic looks legitimate. Advertisers in cost-per-install (CPI) campaigns are the primary victims, since they pay per attributed install regardless of whether the user is a real person. Anti-fraud practice typically relies on IP exclusion lists, traffic-source auditing, and third-party invalid-traffic detection tools.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.g2.com/click-injection">What Is Click Injection? How It Works and How to Stop It - G2</a></li>
<li><a href="https://www.trafficguard.ai/blog/cell-phone-bot-farm">What is a bot farm? The advertiser's guide to bot fraud (2026)</a></li>
<li><a href="https://adex.com/blog/device-farm-fraud-real-phones-fake-installs/">Device Farm Fraud: Real Phones, Fake Installs - adex.com</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly sympathetic and skeptical of the platforms: one called Google and Meta ads "a con," and another argued Google is very capable of detecting ad fraud but turns a blind eye when it suits them. Others pushed back with practical advice, sharing an IP-exclusion workflow with 4000+ blocked networks, and one reader said the post actually made them install and play the app, praising its clean interface as an accidental marketing win.

**Tags**: `#ad-fraud`, `#google-ads`, `#mobile-marketing`, `#bot-detection`, `#startup-growth`

---

<a id="item-11"></a>
## [Calif Research Claims AI-Built Zero-Click WeChat Call Worm](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 7.4/10

Calif Research released a demo of WeWorm, which it describes as the first zero-click worm to spread through WeChat calls across both iOS and Android, claiming its team used AI to find the underlying bug and write the first remote code execution (RCE) exploit in about two days, then build the full worm in one more week. Simon Willison quoted the announcement directly, framing it as a notable capability signal for AI-assisted security research. If the claim holds up, it suggests LLM-assisted tooling can compress what used to be months of work by a larger team into roughly a week, lowering the barrier to building cross-platform zero-click malware. That has direct implications for the security of WeChat's very large user base and for how quickly defenders will need to patch such flaws once AI-assisted discovery becomes routine. The announcement stresses that the victim never needs to answer the call or touch the phone at all, and that even if they do answer they hear nothing while the exploit still succeeds. It is presented as a demo with no CVE identifier, no patch status, and no independent verification, and the citing post adds no technical analysis or caveats of its own.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit is an attack that compromises a device without any action from the user, which makes it far stealthier than the usual phishing-style attack that requires a click or a download. Remote code execution (RCE) is the class of vulnerability that lets an attacker run arbitrary code on a remote machine, and a worm is malware that self-propagates across devices or networks without human help — combining the three produces a self-spreading, no-interaction compromise, historically a multi-month effort for a well-resourced team. WeChat calls are a communications channel used by hundreds of millions of people, so a flaw reachable simply by calling a target is unusually severe; AI-assisted vulnerability research and exploit development is the emerging practice of using large language models to speed up that work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.f5.com/glossary/zero-click-attack">Zero - click attack | F5</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/remote-code-execution/">What is Remote Code Execution (RCE)? | CrowdStrike</a></li>
<li><a href="https://www.nozominetworks.com/blog/p2pinfect-worm-evolves-to-target-a-new-platform">P2PInfect Worm Evolves, Targeting a New Platform</a></li>

</ul>
</details>

**Tags**: `#ai-security-research`, `#zero-click-exploit`, `#llm-assisted-development`, `#wechat`, `#vulnerability-research`

---

<a id="item-12"></a>
## [Rune, a hackable Go-based terminal editor, goes open source](https://rune.build/blog/rune-is-now-open-source) ⭐️ 7.2/10

Rune, a keyboard-driven terminal-based development environment written in Go, is now open source, according to an announcement on its blog. Alongside the release, the project detailed a plan to give participating contributors a contractual right to share in the revenue Rune generates. A new hackable, Go-based terminal editor gives programmers an alternative to the established incumbents like Vim, Emacs, and Neovim, while its source availability lets users inspect and modify the tool. The revenue-sharing proposal also makes it a test case for how open-source projects try to fund and incentivize contributions beyond reputation. Rune is positioned as a fast, keyboard-driven IDE that runs inside the terminal, combining a command prompt, a console, splittable terminal tiles, and language tooling under one set of key bindings. It syncs work across multiple machines through a coordination server with its own encryption approach, which some users say raises a trust question they would rather solve with a tool like Tailscale or plain SSH.

hackernews · ernestrc · Sep 11, 15:31 · [Discussion](https://news.ycombinator.com/item?id=49660149)

**Background**: Terminal editors are text editors that run inside a command-line shell rather than a graphical window, and long-time examples such as Vim and Emacs are prized for speed and extensibility but have steep learning curves. Rune is written in Go, a language known for easy cross-compilation and simple deployment, and it targets users who want a modern, hackable alternative. The project's networking feature and its contributor revenue-sharing model are the two aspects drawing the most scrutiny from early adopters.

<details><summary>References</summary>
<ul>
<li><a href="https://rune.build/blog/rune-is-now-open-source">Rune is now open source. Rune Blog</a></li>
<li><a href="https://rune.build/">Rune — The development environment for pros</a></li>
<li><a href="https://docs.rune.build/">Rune: The development environment for pros</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly excited about a hackable Go-based editor, with one Vim user praising the onboarding, though another noted a conflict with fish shell's own Vim bindings. A recurring criticism targets the multi-machine networking: users would prefer not to trust Rune's coordination server and ask whether it can run over Tailscale or SSH instead. The sharpest pushback was against the revenue-sharing plan, with one commenter arguing that paying contributors directly invites low-quality PR spam like that seen with Hacktoberfest and AI-generated pull requests.

**Tags**: `#Open Source`, `#Developer Tools`, `#Code Editor`, `#Go`, `#Terminal`

---

<a id="item-13"></a>
## [OpenAI scales Habitat storage to 1B ChatGPT users at 22M req/s](https://openai.com/index/scaling-storage-one-billion-users-part-one) ⭐️ 7.0/10

OpenAI published an engineering post describing how its internal Habitat storage system grew from a simple Python client-side library connected to a single database into a globally distributed storage platform. The post says Habitat now handles roughly 22 million requests per second while supporting products used by more than 1 billion people per week across almost 40 geographic regions. Rare first-hand detail about how OpenAI runs storage at consumer-internet scale gives infrastructure engineers a reference point for designing systems that must survive billions of users and tens of millions of requests per second. It also signals that storage, not just GPUs or models, has become a first-class scaling bottleneck for large AI products. The headline figure in the article is 22 million requests per second, while a passage in the same post is summarized elsewhere as citing more than 70 million requests per second, so the exact figure appears to vary by scope (per-region versus fleet-wide). Third-party write-ups of the post also report a migration away from Python toward Rust for performance reasons, a notable detail given Habitat's origins as a Python library.

rss · OpenAI Blog · Sep 11, 10:00

**Background**: Habitat is OpenAI's internal storage layer, the software that actually holds and serves the data behind ChatGPT and other products. Distributed storage platforms spread data across many machines and geographic regions so that no single database becomes a bottleneck, trading simplicity for throughput, fault tolerance and locality. "Requests per second" is the standard measure of how much traffic such a system absorbs, and Python is popular for building systems quickly but is usually too slow for the hottest paths at this scale, which is why rewrites into lower-level languages like Rust are common.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/scaling-storage-one-billion-users-part-one/">Rapidly scaling online storage to serve over 1 billion... | OpenAI</a></li>
<li><a href="https://krivoshein.site/openai-habitat-70-млн-запросов-с-и-rust-вместо-python/">OpenAI Habitat : 70 млн запросов/с и Rust вместо Python</a></li>
<li><a href="https://www.systemdesignhandbook.com/blog/distributed-file-storage/">Distributed File Storage: Architecture, Examples & Benefits</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#distributed-storage`, `#infrastructure`, `#scaling`, `#systems-engineering`

---

<a id="item-14"></a>
## [Ruan Yifeng's Weekly #412: Ban Issues, Accept Only Pull Requests](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-412.html) ⭐️ 7.0/10

Issue 412 of Ruan Yifeng's weekly tech newsletter (科技爱好者周刊) was published, themed around the proposition that a project should ban its issue tracker and accept contributions only in the form of pull requests. As usual, the issue is a curated roundup released on a Friday, covering links and commentary on technology topics of the week. The theme touches a live debate in open-source governance: whether public issue trackers help or hurt maintainers by generating noise, duplicate reports and entitlement-driven demands. If more projects adopt a PR-only or issues-disabled policy, it would change how newcomers, bug reporters and non-coding users interact with open-source projects. The newsletter is a curated link digest rather than original research, so the issue's theme represents an editorial stance argued through selected examples and commentary rather than a formal study. The excerpt available here is only the newsletter's opening intro line, so the concrete arguments, cited projects and counterexamples in the full issue cannot be verified from this material.

rss · 阮一峰周刊 · Sep 11, 00:11

**Background**: Ruan Yifeng is a well-known Chinese software developer and technical blogger, and his 科技爱好者周刊 (Technology Enthusiast Weekly) has been published on Fridays for many years, making it one of the most widely read Chinese-language tech newsletters. The debate it addresses concerns two core GitHub features: the issue tracker, where anyone can file bug reports and feature requests, and the pull request (PR), where a contributor submits a concrete code change for review. Because filing an issue is cheap and open to anyone while writing a PR requires actual code, some maintainers argue that issue sections attract low-quality reports and demands, whereas requiring PRs filters for people willing to do the work — at the cost of excluding users who cannot code.

**Tags**: `#tech-newsletter`, `#open-source`, `#developer-culture`, `#software-engineering`, `#github-workflow`

---