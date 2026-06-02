---
layout: default
title: "Horizon Summary: 2026-06-02 (EN)"
date: 2026-06-02
lang: en
---

> From 112 items, 21 important content pieces were selected

---

1. [JetBrains Releases Mellum2: 12B MoE Model](#item-1) ⭐️ 9.5/10
2. [NVIDIA Launches Cosmos 3: First Open Omni-Model for Physical AI](#item-2) ⭐️ 9.4/10
3. [China Approves First Invasive Brain-Computer Chip Implant](#item-3) ⭐️ 9.1/10
4. [Why systemd Timers Are Superior to Cron](#item-4) ⭐️ 8.9/10
5. [Why Janet? A Deep Dive into the Janet Programming Language](#item-5) ⭐️ 8.8/10
6. [GitHub Unveils Strategy for Agentic AI Coding Tools](#item-6) ⭐️ 8.8/10
7. [Author Leaves Gmail Over AI Suggestions, Switches to Fastmail](#item-7) ⭐️ 8.5/10
8. [Anthropic Expands Claude Mythos to Critical Infrastructure](#item-8) ⭐️ 8.5/10
9. [Big Tech's ad attribution system undermines privacy](#item-9) ⭐️ 8.2/10
10. [Holo3.1: Fast Local Computer Use AI Agent](#item-10) ⭐️ 8.2/10
11. [Agent Logic Key to Enterprise AI Scalability Beyond LLMs](#item-11) ⭐️ 8.0/10
12. [Why Video Agent Models Are Next: Inside xAI's Grok Imagine](#item-12) ⭐️ 8.0/10
13. [Claude Code v2.1.160 Improves Safety and Fixes WSL Clipboard](#item-13) ⭐️ 7.9/10
14. [Google Issues Equity to Berkshire, Signaling Capital Commoditization](#item-14) ⭐️ 7.8/10
15. [Claude Code v2.1.161: OTEL, Parallel Tools, Clipboard Fixes](#item-15) ⭐️ 7.7/10
16. [YouTubers Beat Hollywood at Box Office](#item-16) ⭐️ 7.7/10
17. [Trump signs downsized AI order focusing on cybersecurity](#item-17) ⭐️ 7.5/10
18. [OpenAI's AI Policy Advocacy: Transparency and Independence](#item-18) ⭐️ 7.5/10
19. [Walking tour of Seattle's surveillance infrastructure](#item-19) ⭐️ 7.4/10
20. [KDE Plasma to Drop X11 Support After Next Release](#item-20) ⭐️ 7.2/10
21. [Age verification threatens free internet, says Mullvad](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [JetBrains Releases Mellum2: 12B MoE Model](https://huggingface.co/blog/JetBrains/mellum2-launch) ⭐️ 9.5/10

JetBrains has released Mellum2, a 12 billion parameter Mixture-of-Experts (MoE) language model, as announced on the Hugging Face blog. Mellum2 demonstrates JetBrains' entry into the large language model space with a computationally efficient MoE architecture, potentially offering strong performance for developer tools and AI-assisted coding. The model uses a sparse Mixture-of-Experts design, activating only a subset of parameters per token, which reduces inference cost compared to a dense model of equivalent total parameters.

rss · Hugging Face Blog · Jun 1, 15:45

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that splits computation into multiple expert subnetworks, with a router selecting which experts to use for each input. This allows models to have a large number of parameters while keeping computational cost manageable, as only a fraction of parameters are used per inference. Notable examples include Mixtral 8x7B and other recent MoE models.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA ...</a></li>
<li><a href="https://arxiv.org/abs/2401.04088">[2401.04088] Mixtral of Experts - arXiv.org Understanding Mixture of Experts (MoE): The Architecture ... Mixture of Experts (MoE) Models: Architecture and ... Mixture of Experts (MoE) Architecture: A Complete Analysis Mixture of Experts (MoE) Architecture: A Deep Dive and ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Mixture-of-Experts`, `#JetBrains`, `#Hugging Face`

---

<a id="item-2"></a>
## [NVIDIA Launches Cosmos 3: First Open Omni-Model for Physical AI](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) ⭐️ 9.4/10

NVIDIA announced Cosmos 3, the first open omni-modal world model that can process and generate language, videos, and action sequences for physical AI and advanced robotics. This breakthrough bridges AI reasoning with physical action, enabling robots and embodied AI systems to understand and interact with the real world more naturally. Being open-source, it democratizes access to cutting-edge physical AI capabilities, accelerating research and development in robotics and autonomous systems. Cosmos 3 includes a 'Nano' variant with 16 billion trainable parameters, supporting BF16 weights and integration with vLLM-Omni, PyTorch, and Hugging Face Diffusers. It can reason about motion, causality, and spatial relationships, and predict future video and action sequences.

rss · Hugging Face Blog · Jun 1, 04:44

**Background**: Physical AI refers to systems that perceive, reason, and act in the real world, understanding physical constraints like gravity and friction. Previous models typically handled only one modality (text or vision); Cosmos 3 unifies multiple modalities into a single omni-model, advancing embodied AI research by enabling more coherent understanding and generation across language, video, and action.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai">Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical ...</a></li>
<li><a href="https://huggingface.co/nvidia/Cosmos3-Nano">nvidia / Cosmos 3 -Nano · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Cosmos 3`, `#Physical AI`, `#Open Model`, `#AI Reasoning`

---

<a id="item-3"></a>
## [China Approves First Invasive Brain-Computer Chip Implant](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/) ⭐️ 9.1/10

In March 2026, China's National Medical Products Administration (NMPA) approved the NEO brain-computer interface, developed by Neuracle Technology and Tsinghua University, for commercial use. Patient Dong Hui, paralyzed from a spinal cord injury, demonstrated the ability to write using the implant. This is the world's first regulatory approval for an invasive BCI device, marking a major milestone for neurotechnology and offering new hope for paralysis patients. China's rapid approval and integration into healthcare policy could accelerate global BCI adoption and regulation. The NEO device features eight sensors placed on the dura mater (the outermost protective layer of the brain), reducing tissue damage compared to Neuralink's N1 which penetrates the brain cortex. The implantation surgery took about 1.5 hours, and the patient began rehabilitation within a week.

rss · MIT Tech Review · Jun 1, 09:09

**Background**: A brain-computer interface (BCI) enables direct communication between the brain and an external device, often used to restore function in paralyzed individuals. Invasive BCIs require surgery to implant electrodes, while non-invasive ones use external sensors. The meninges are the three protective membranes covering the brain: dura mater, arachnoid mater, and pia mater. Placing sensors on the dura mater is considered less invasive than penetrating the cortex, as done by Neuralink.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41587-026-03101-8">China approves brain chip to overcome paralysis - Nature</a></li>
<li><a href="https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/">China has approved the world’s first invasive brain-computer ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dura_mater">Dura mater - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#neural implants`, `#China`, `#regulatory approval`, `#neurotechnology`

---

<a id="item-4"></a>
## [Why systemd Timers Are Superior to Cron](https://blog.tjll.net/you-dont-love-systemd-timers-enough/) ⭐️ 8.9/10

A blog post by Tylerjl argues that systemd timers are superior to cron for modern Linux systems, citing better flexibility, integration with journalctl, and resilience to system startup times. This discussion matters for system administrators and developers managing scheduled tasks on Linux, as systemd timers offer advantages such as handling missed runs due to system downtime and simpler logging via journalctl. Key technical details include that systemd timers support OnBootSec, OnCalendar, and monotonic timers, and they integrate tightly with systemd's service and logging infrastructure.

hackernews · yacin · Jun 2, 09:34 · [Discussion](https://news.ycombinator.com/item?id=48367904)

**Background**: systemd is a system and service manager for Linux that provides an init system and various daemons. systemd timers are unit files (with .timer suffix) that control when associated services run, offering features like monotonic timers and integration with journalctl. Cron is a time-based job scheduler found in Unix-like systems, using crontab files to define schedules. systemd timers are increasingly replacing cron in many Linux distributions due to their richer feature set.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Systemd/Timers">systemd/Timers - ArchWiki</a></li>
<li><a href="https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html">systemd.timer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Systemd-timesync">Systemd-timesync</a></li>

</ul>
</details>

**Discussion**: Community comments include skepticism about the PATH argument, but many users share positive experiences with systemd timers, such as handling missed runs after system downtime. The author actively engages in the discussion.

**Tags**: `#systemd`, `#timers`, `#cron`, `#linux`, `#sysadmin`

---

<a id="item-5"></a>
## [Why Janet? A Deep Dive into the Janet Programming Language](https://ianthehenry.com/posts/why-janet/) ⭐️ 8.8/10

The article 'Why Janet?' (2023) comprehensively examines the design, benefits, and trade-offs of the Janet programming language, highlighting its strengths for system scripting, embedding, and native binary compilation. This analysis matters because Janet offers a modern Lisp alternative with a tiny footprint, easy embedding, and native executable generation, potentially filling niches dominated by Lua while providing richer built-in functionality. Janet's core language has only eight instructions (do, def, var, set, if, while, break, fn), but supports powerful macros and a PEG engine for text parsing. The entire language is under 1MB and can be embedded via a single C source file and header.

hackernews · yacin · Jun 2, 09:34 · [Discussion](https://news.ycombinator.com/item?id=48367907)

**Background**: Janet is a functional and imperative programming language inspired by Clojure and implemented in C. It is designed for system scripting, automation, and embedding into C/C++ applications. Similar to Lua, but with a richer core library and modern features like PEG, Janet compiles to bytecode and can create standalone executables.

<details><summary>References</summary>
<ul>
<li><a href="https://janet-lang.org/">Janet Programming Language</a></li>
<li><a href="https://ianthehenry.com/posts/why-janet/">Why Janet? - ianthehenry.com luajit2 vs janet - compare differences and reviews? | LibHunt Videos Reagan Izabelle Miriam Laylah Maggie Janet Addison Performance? · janet-lang janet · Discussion #1239 · GitHub the Fennel programming language Janet: a lightweight, expressive and modern Lisp | Hacker News My Janet Story - Junglecoder</a></li>
<li><a href="https://github.com/janet-lang/janet">GitHub - janet-lang/janet: A dynamic language and bytecode vm Janet for Mortals Why Janet? - ianthehenry.com Janet Programming I Love Janet (the Language) | Caleb's Notes Learn Janet in Y Minutes</a></li>

</ul>
</details>

**Discussion**: Commenters appreciate Janet's portability and binary creation, but note limitations like lack of package versioning and sparse library ecosystem. Some point out inaccuracies in the article (e.g., SETQ vs def behavior) and compare Janet favorably to alternatives like Fennel and Lua.

**Tags**: `#janet`, `#programming languages`, `#lisp`, `#scripting`

---

<a id="item-6"></a>
## [GitHub Unveils Strategy for Agentic AI Coding Tools](https://www.latent.space/p/github) ⭐️ 8.8/10

GitHub has outlined a plan to address the growing strain on its platform caused by the rise of agentic AI coding tools, which automate more complex software development tasks beyond simple code generation. This matters because agentic coding tools are fundamentally changing how developers work, and GitHub's response will shape the future of collaborative software development on the world's largest code hosting platform. The plan likely involves integrating and managing AI agents within GitHub's existing workflows, such as Copilot, Actions, and pull requests, to ensure reliability and maintain developer trust. Further details about the exact technical changes have not been publicly disclosed yet.

rss · Latent Space · Jun 2, 16:48

**Background**: Agentic coding refers to the use of AI agents—autonomous programs that can plan, debug, and execute tasks—to assist in software development, going beyond LLM-based code completion. Tools like Cursor, Claude Code, and Devin represent this new wave, which puts additional load on platforms like GitHub by generating more complex code changes and demanding deeper integration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://www.datacamp.com/blog/best-agentic-ide">The 13 Best Agentic IDEs in 2026 - DataCamp</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GitHub`, `#Copilot`, `#agentic coding`, `#developer tools`

---

<a id="item-7"></a>
## [Author Leaves Gmail Over AI Suggestions, Switches to Fastmail](https://moddedbear.com/gmail-thinks-im-stupid-so-i-left) ⭐️ 8.5/10

The author of the blog post 'Gmail thinks I'm stupid, so I left' details their decision to abandon Gmail due to intrusive AI-powered suggestions and migrate to Fastmail, a subscription-based email service. This reflects growing user frustration with AI-driven features that can feel patronizing or unnecessary, and highlights a shift toward privacy-focused, ad-free alternatives like Fastmail. Fastmail offers features similar to Gmail, including app passwords, hide-my-email, and iOS integration, but without AI suggestions; the author notes that Fastmail operations are instant compared to Gmail's loading delays.

hackernews · speckx · Jun 2, 19:27 · [Discussion](https://news.ycombinator.com/item?id=48375016)

**Background**: Gmail's Smart Compose, introduced in 2018, uses AI to suggest complete sentences as users type, aiming to speed up email writing. However, many users find these suggestions intrusive or irrelevant. Fastmail is a subscription-based email hosting service founded in 1999, known for its ad-free experience and focus on privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fastmail">Fastmail - Wikipedia</a></li>
<li><a href="https://support.google.com/mail/answer/9116836?hl=en&co=GENIE.Platform=Desktop">Use Smart Compose in Gmail - Computer - Gmail Help</a></li>
<li><a href="https://blog.google/products-and-platforms/products/gmail/subject-write-emails-faster-smart-compose-gmail/">SUBJECT: Write emails faster with Smart Compose in Gmail</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree with the author's frustration, with some praising Fastmail's performance and simplicity. One user criticizes Gmail's AI suggestions for being overly verbose, while another wonders why native speakers rely on LLMs for email writing. There is also irritation at Google's pushy AI advertising on other platforms like Chrome.

**Tags**: `#AI`, `#Gmail`, `#email`, `#user experience`, `#Fastmail`

---

<a id="item-8"></a>
## [Anthropic Expands Claude Mythos to Critical Infrastructure](https://www.anthropic.com/news/expanding-project-glasswing) ⭐️ 8.5/10

Anthropic has expanded Project Glasswing, granting approximately 150 new organizations access to Claude Mythos Preview, extending coverage to critical infrastructure in 15 countries. This move aims to proactively secure foundational software systems against vulnerabilities, potentially reducing cyber risks for billions of users, but it also raises concerns about AI access and surveillance. Claude Mythos is Anthropic's most powerful model, gated due to safety concerns; initial partners include maintainers of core internet infrastructure, and the model detects software flaws but has been reported to generate many false positives.

hackernews · surprisetalk · Jun 2, 13:15 · [Discussion](https://news.ycombinator.com/item?id=48369863)

**Background**: Project Glasswing, launched in April 2026, is Anthropic's cybersecurity initiative to use AI to secure critical software. Claude Mythos is a large language model specifically designed for vulnerability discovery, described as a 'step change' in capability. Anthropic has restricted public access to Mythos, offering it only through gated previews to mitigate risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/04/08/what-is-claude-mythos-and-why-anthropic-wont-let-anyone-use-it/">What Is Claude Mythos—And Why Anthropic Won’t ... - Forbes</a></li>

</ul>
</details>

**Discussion**: Some users report that Mythos generates excessive false positives, calling the security scanning framework more valuable than the model itself. Others suspect Anthropic is using security concerns to mask compute limitations and maintain a lead over competitors. Additionally, there are fears about Anthropic's stance on mass surveillance and the ethical implications of granting AI access to critical infrastructure source code.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#critical infrastructure`

---

<a id="item-9"></a>
## [Big Tech's ad attribution system undermines privacy](https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/) ⭐️ 8.2/10

A blog post argues that a proposed ad attribution system from Google, Meta, Apple, and Mozilla creates a two-track system that exempts their own tracking from privacy regulations while burdening competitors. This matters because it reveals how big tech companies may co-opt privacy rhetoric to entrench their market power, potentially undermining existing privacy laws like GDPR and CCPA. The author claims the proposal includes no permission or consent section, and users must manually find and disable the built-in tracking feature, while third-party ad features face strict regulation.

hackernews · speckx · Jun 2, 19:39 · [Discussion](https://news.ycombinator.com/item?id=48375175)

**Background**: Ad attribution is the process of assigning credit to ads for conversions. Privacy regulations increasingly restrict third-party tracking, prompting browsers to implement new attribution APIs. Critics argue that browser vendors design these APIs to favor their own advertising ecosystems.

<details><summary>References</summary>
<ul>
<li><a href="https://volument.com/blog/advertising-attribution-explained/">Advertising Attribution Explained: Models, Privacy , and... - Volument</a></li>
<li><a href="https://www.cometly.com/post/ad-attribution-after-privacy-updates">Ad Attribution After Privacy Updates: Complete Guide</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed. Some users see the proposal as a cartel that consolidates big tech control, while others view the agreement between competitors as a positive sign for privacy. A few commentators suspect the author is an advertiser defending profit over privacy.

**Tags**: `#privacy`, `#advertising`, `#web browsers`, `#big tech`, `#ad attribution`

---

<a id="item-10"></a>
## [Holo3.1: Fast Local Computer Use AI Agent](https://huggingface.co/blog/Hcompany/holo31) ⭐️ 8.2/10

Holo3.1 is a newly released AI agent system that runs locally on a user's device, designed to automate computer use tasks like clicking, typing, and navigating applications. This matters because it enables fast, private, and cost-effective automation of computer tasks without relying on cloud servers, making AI agents accessible even on consumer hardware. The system is presented on the Hugging Face blog, suggesting it is open-source or at least documented for the community. As a local inference solution, it likely supports various hardware configurations and emphasizes low latency.

rss · Hugging Face Blog · Jun 2, 14:13

**Background**: AI agents that can use computers like humans are a growing trend, with examples like OpenAI's Computer-Using Agent and Microsoft's computer use feature. Running such agents locally means inference happens on the user's device, improving privacy and reducing costs, but typically requires powerful hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent - OpenAI</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use">Automate web and desktop apps with computer use</a></li>
<li><a href="https://localai.io/">LocalAI</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#local inference`, `#computer use`, `#Hugging Face`, `#LLM`

---

<a id="item-11"></a>
## [Agent Logic Key to Enterprise AI Scalability Beyond LLMs](https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption) ⭐️ 8.0/10

IBM Research argues that scalable enterprise AI adoption requires moving beyond standalone LLMs to agent logic that coordinates complex workflows, decision-making, and error handling. Many enterprise AI projects stall due to operational challenges, and agent logic offers a structured way to integrate AI into business processes reliably and at scale. The blog likely emphasizes that agent logic enables deterministic behavior, error recovery, and multi-step reasoning, which are critical for production AI systems.

rss · Hugging Face Blog · Jun 1, 13:51

**Background**: LLMs excel at generating text but lack built-in mechanisms for structured task execution. Intelligent agents use logic to perceive, reason, and act, making them suitable for enterprise workflows. IBM has been a proponent of agent-based AI, and this blog aligns with industry trends toward agentic systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_agent">Intelligent agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/insights/why-most-enterprise-ai-projects-stall-before-scale">Why most enterprise AI projects stall before they scale | IBM</a></li>
<li><a href="https://openai.com/business/guides-and-resources/how-enterprises-are-scaling-ai/">How enterprises are scaling AI | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agents`, `#enterprise AI`, `#scalability`, `#LLMs`

---

<a id="item-12"></a>
## [Why Video Agent Models Are Next: Inside xAI's Grok Imagine](https://www.latent.space/p/video-agents) ⭐️ 8.0/10

Ethan He from xAI discusses building Grok Imagine in three months, comparing video generation versus world models, and argues that video agent models represent the next frontier in AI. Video agent models combine video generation with agentic reasoning, potentially enabling more interactive and world-aware AI systems that could transform content creation, robotics, and simulation. Grok Imagine supports text-to-image, image-to-video generation, and includes an Imagine Agent Mode for iterative refinement, with native audio generation for videos.

rss · Latent Space · Jun 1, 15:41

**Background**: Video agent models differ from static video generators by incorporating planning and interactive reasoning. World models simulate environments and predict outcomes, while traditional video generation focuses on producing clips. xAI's Grok Imagine is built on these concepts, aiming to create more coherent and controllable video content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://x.ai/news/grok-imagine-api">Grok Imagine API | xAI</a></li>
<li><a href="https://arxiv.org/abs/2403.10517">[2403.10517] VideoAgent: Long-form Video Understanding with ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#video agents`, `#xAI`, `#Grok Imagine`, `#world models`

---

<a id="item-13"></a>
## [Claude Code v2.1.160 Improves Safety and Fixes WSL Clipboard](https://github.com/anthropics/claude-code/releases/tag/v2.1.160) ⭐️ 7.9/10

Anthropic released Claude Code v2.1.160, adding safety prompts before editing shell startup files and build-tool configs, and fixing WSL clipboard using PowerShell interop instead of OSC 52. These updates make Claude Code safer for users by preventing unintended command execution from config edits, and improve the experience for Windows/WSL users with a more reliable clipboard fix. The release adds prompt confirmation before writing to `.zshenv`, `.bash_login`, and `~/.config/git/` files, and in `acceptEdits` mode for configs like `.npmrc` and `.yarnrc`. It also fixes session restoration, background agent issues, and IME composition in CJK.

github · ashwin-ant · Jun 2, 02:10

**Background**: Claude Code is Anthropic's AI-powered coding assistant that runs in the terminal. WSL (Windows Subsystem for Linux) allows running Linux tools on Windows; clipboard interoperability between Linux and Windows can be challenging. OSC 52 is a terminal escape sequence for clipboard access, but some terminals like MobaXterm do not support it; PowerShell interop provides an alternative.

<details><summary>References</summary>
<ul>
<li><a href="https://marceloborges.dev/posts/3/">Supercharging My Clipboard with OSC 52 Escape Sequence</a></li>
<li><a href="https://www.windowscentral.com/software-apps/like-me-you-might-not-have-known-this-handy-windows-11-clipboard-terminal-trick-for-powershell-and-wsl">Like me, you might not have known this handy Windows 11 clipboard terminal trick for PowerShell and WSL</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#AI tooling`, `#developer tools`, `#changelog`, `#Anthropic`

---

<a id="item-14"></a>
## [Google Issues Equity to Berkshire, Signaling Capital Commoditization](https://stratechery.com/2026/the-google-capital-company/) ⭐️ 7.8/10

Google issued equity to Berkshire Hathaway in a deal that signals a future where capital is viewed as a commodity, according to Ben Thompson's analysis on Stratechery. This transaction suggests that even major tech companies now treat capital as a fungible resource, potentially reshaping how tech firms finance operations and growth. It underscores a shift where access to capital is less of a competitive advantage. The equity issuance to Berkshire Hathaway indicates a strategic relationship between a leading tech firm and a diversified conglomerate, possibly to secure long-term investment without diluting control immediately.

rss · Stratechery · Jun 2, 10:00

**Background**: Capital has traditionally been a scarce resource for startups, but for established tech giants like Google, access to capital markets is abundant. The deal with Berkshire Hathaway, known for its massive capital reserves, highlights that even for such firms, securing patient capital from a trusted partner can be valuable. This event may indicate a broader trend where capital becomes a commodity, reducing its strategic importance.

**Tags**: `#Google`, `#Berkshire Hathaway`, `#capital markets`, `#business strategy`, `#tech industry`

---

<a id="item-15"></a>
## [Claude Code v2.1.161: OTEL, Parallel Tools, Clipboard Fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) ⭐️ 7.7/10

Anthropic released version 2.1.161 of claude-code on GitHub, featuring improvements to OpenTelemetry resource attributes, parallel tool call independence, and enhanced Linux clipboard handling with wl-copy/xclip/xsel support. This release enhances observability for developers by making OTEL resource attributes available as metric labels, and improves tool call reliability by isolating failures in parallel Bash commands. Notably, failed Bash commands no longer cancel other parallel tool calls, and clipboard operations on Linux now copy to both clipboard and PRIMARY selection for middle-click paste.

github · ashwin-ant · Jun 2, 21:58

**Background**: Claude Code is Anthropic's command-line tool for interacting with Claude, an AI assistant, enabling developers to execute tasks directly from the terminal. OpenTelemetry (OTEL) is an observability framework for generating and collecting telemetry data, and resource attributes help identify the source of metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://opentelemetry.io/docs/concepts/resources/">Resources | OpenTelemetry</a></li>
<li><a href="https://github.com/bugaevc/wl-clipboard">GitHub - bugaevc/wl-clipboard: Command-line copy/paste ...</a></li>

</ul>
</details>

**Tags**: `#claude-code`, `#release notes`, `#AI tooling`, `#developer tools`, `#Anthropic`

---

<a id="item-16"></a>
## [YouTubers Beat Hollywood at Box Office](https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/) ⭐️ 7.7/10

Ben Thompson argues that YouTubers' box office success proves the YouTube algorithm sets a higher bar for content quality than traditional Hollywood gatekeepers. This shift signals a fundamental change in content creation and distribution, where platform-driven metrics may replace legacy gatekeepers, empowering individual creators over established studios. Thompson specifically highlights that the YouTube algorithm's reliance on audience retention and engagement creates a more rigorous selection process than Hollywood's network-based pitching system.

rss · Stratechery · Jun 1, 10:00

**Background**: YouTube's algorithm recommends videos based on watch time and user satisfaction, rewarding creators who produce highly engaging content. In contrast, Hollywood traditionally relies on a gatekeeping system where producers, studios, and distributors greenlight projects. The article argues that the algorithm's objective feedback loop is a tougher test than subjective industry decisions.

**Tags**: `#YouTube`, `#Hollywood`, `#gatekeeping`, `#media disruption`, `#platform economics`

---

<a id="item-17"></a>
## [Trump signs downsized AI order focusing on cybersecurity](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389) ⭐️ 7.5/10

President Trump signed a scaled-back executive order on AI that emphasizes cybersecurity measures and voluntary government review of new models. The order lacks substance and could pave the way for regulatory capture, potentially stifling AI innovation and competition. The order requires AI companies to voluntarily submit powerful new models for government review 30 days before release and directs the Justice Department to prosecute hacking using AI.

hackernews · _alternator_ · Jun 2, 16:40 · [Discussion](https://news.ycombinator.com/item?id=48372628)

**Background**: The Trump administration had previously made several reversals on AI policy before settling on this scaled-down order. The order focuses on cybersecurity and voluntary benchmarking, avoiding broader regulatory frameworks.

**Discussion**: Community comments on Hacker News widely criticize the order as vague and insubstantial, with many expressing concern that it may ultimately lead to bans on open-source models or create barriers for smaller competitors.

**Tags**: `#AI policy`, `#executive order`, `#cybersecurity`, `#regulation`, `#HN discussion`

---

<a id="item-18"></a>
## [OpenAI's AI Policy Advocacy: Transparency and Independence](https://openai.com/index/our-views-on-ai-policy-and-political-advocacy) ⭐️ 7.5/10

OpenAI released a statement outlining its approach to AI policy and political advocacy, emphasizing transparency, support for thoughtful regulation, and AI safety, and clarifying that no external political group speaks on the company's behalf. This statement provides clarity on OpenAI's political neutrality and its commitment to responsible AI development, which could influence how other AI companies approach policy advocacy and public trust. OpenAI reaffirms its support for thoughtful regulation and AI safety, and asserts that no outside political group speaks on its behalf, emphasizing the company's independence in advocacy efforts.

rss · OpenAI Blog · Jun 1, 17:00

**Background**: AI policy refers to the set of regulations and guidelines governing the development and deployment of artificial intelligence. OpenAI is a leading AI research organization that has been actively involved in discussions around AI safety and regulation. This statement is part of ongoing efforts to communicate its stance transparently to the public and policymakers.

**Tags**: `#AI policy`, `#OpenAI`, `#regulation`, `#AI safety`, `#political advocacy`

---

<a id="item-19"></a>
## [Walking tour of Seattle's surveillance infrastructure](https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/) ⭐️ 7.4/10

A detailed walking tour documents the pervasive surveillance cameras, license plate readers, and other monitoring technologies in Seattle, offering critical commentary on their social implications. This analysis highlights the extent of urban surveillance and raises important questions about privacy, civil liberties, and the trade-offs between security and freedom. The tour covers various types of cameras and Automated License Plate Readers (ALPRs), with commentary on how these technologies encode social norms and enforce what is considered 'normal' behavior.

hackernews · eustoria · Jun 2, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48369980)

**Background**: Automated License Plate Readers (ALPRs) are cameras that capture license plate numbers and are often used by law enforcement. City-wide surveillance networks are increasingly common for traffic management and crime prevention. This article critiques these systems from a social control perspective, arguing that they can reinforce biases and chill free expression.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number- plate recognition - Wikipedia</a></li>
<li><a href="https://sls.eff.org/technologies/automated-license-plate-readers-alprs">Automated License Plate Readers</a></li>
<li><a href="https://www.senergy.io/industries/municipal-security/">Municipal & Police City-Wide Security Camera Video Surveillance</a></li>

</ul>
</details>

**Discussion**: Comments on Hacker News are mixed. Some readers argue that surveillance is necessary for safety, citing cases where video evidence is needed for prosecution. Others criticize the article's academic language as inaccessible and express concerns about the erosion of privacy and freedom.

**Tags**: `#surveillance`, `#privacy`, `#security`, `#urban technology`, `#Seattle`

---

<a id="item-20"></a>
## [KDE Plasma to Drop X11 Support After Next Release](https://blog.davidedmundson.co.uk/blog/596/) ⭐️ 7.2/10

KDE Plasma's upcoming release will be the last to support the X11 display server, marking a full transition to Wayland. This change streamlines development by focusing on a single code path. This decision signals the end of an era for the legacy X11 system and accelerates Wayland adoption, promising better performance and security for Linux desktop users. However, it may impact users relying on X11-specific features like some accessibility tools. The transition allows KDE to innovate faster with Wayland, but known issues remain, such as lack of window position saving and per-application keyboard layouts. The KDE team acknowledges that some X11 features are not yet replicated in Wayland.

hackernews · jandeboevrie · Jun 2, 14:16 · [Discussion](https://news.ycombinator.com/item?id=48370588)

**Background**: X11 (X Window System) is a legacy display server protocol that has been the standard on Unix-like systems for decades. Wayland is its modern replacement, designed to be simpler, faster, and more secure by removing unnecessary legacy features. Many Linux distributions have already moved to Wayland as default, but KDE Plasma has been gradually transitioning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xming">Xming - Wikipedia</a></li>
<li><a href="https://www.wikiwand.com/en/Wayland_(protocol)">Wayland ( protocol ) - Wikiwand</a></li>

</ul>
</details>

**Discussion**: Comments express mixed feelings: some praise KDE's progress on Wayland, citing improved smoothness and responsiveness. Others raise concerns about regressions in accessibility software (e.g., Talon voice input) and missing features like window position saving and per-app keyboard layouts. The discussion highlights a tension between security-driven design choices in Wayland and the needs of power users.

**Tags**: `#KDE`, `#Plasma`, `#Wayland`, `#X11`, `#Linux desktop`

---

<a id="item-21"></a>
## [Age verification threatens free internet, says Mullvad](https://mullvad.net/en/blog/age-verification-for-social-media-the-beginning-of-the-end-for-a-free-internet) ⭐️ 7.0/10

Mullvad published a blog post arguing that mandatory age verification for social media sets a dangerous precedent that could erode internet freedom and privacy for all users. If implemented broadly, age verification could normalize surveillance and censorship, affecting not just children but every internet user's right to anonymous and private communication. Mullvad's argument focuses on the slippery slope: age verification often requires sharing government IDs or biometric data, creating a centralized database that could be abused or breached.

hackernews · StrLght · Jun 1, 23:22 · [Discussion](https://news.ycombinator.com/item?id=48363882)

**Background**: Age verification systems are being proposed by governments worldwide to restrict minors' access to social media, but many privacy advocates warn they threaten anonymity and free expression. Companies like Mullvad, a Swedish VPN provider known for strong privacy protections, argue that such measures could be the start of broader internet surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mullvad_VPN">Mullvad VPN</a></li>
<li><a href="https://www.newamerica.org/insights/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look ...</a></li>

</ul>
</details>

**Discussion**: Comments show divided opinions: some agree age verification is a slippery slope toward ending the free internet, while others argue it's a necessary measure to protect children from harmful content. A few commenters note that the internet's original peer-to-peer nature has already been compromised by centralized platforms and surveillance advertising.

**Tags**: `#privacy`, `#age verification`, `#internet freedom`, `#social media`, `#surveillance`

---