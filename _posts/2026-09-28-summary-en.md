---
layout: default
title: "Horizon Summary: 2026-09-28 (EN)"
date: 2026-09-28
lang: en
---

> From 63 items, 6 important content pieces were selected

---

1. [Simon Willison's 2026 LLM Retrospective Tracks the Coding-Agent Inflection Point](#item-1) ⭐️ 8.6/10
2. [Essay Warns LLM-Driven Dev Normalizes Inexplicable Failures](#item-2) ⭐️ 8.4/10
3. [Fireworks AI releases Ember-1, a Kimi K3-based efficient reasoning model](#item-3) ⭐️ 8.0/10
4. [Neovim Accused of Deleting Vim's Persistent Undo Files](#item-4) ⭐️ 7.7/10
5. [mitxela Renders Fluid Animations on Repurposed Flip-Dot Displays](#item-5) ⭐️ 7.4/10
6. [Don't couple your Go code to GitHub, blog argues](#item-6) ⭐️ 7.1/10

---

<a id="item-1"></a>
## [Simon Willison's 2026 LLM Retrospective Tracks the Coding-Agent Inflection Point](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) ⭐️ 8.6/10

Simon Willison published annotated slides and notes from his closing keynote at the WeAreDevelopers World Congress North America in San Jose on 25th September 2026, offering a chronological tour of everything notable that happened in LLMs during 2026 so far. He dates the real start of 2026 to November 2025, when Claude Opus 4.5 and GPT-5.1 shipped and, paired with their coding-agent harnesses (Claude Code and Codex), went from 'often make mistakes' to 'reliable enough to use on a day-to-day basis'. A year-scale synthesis from a widely trusted practitioner helps developers separate durable shifts from hype, and his central claim — that AI coding agents crossed a reliability threshold — has direct implications for how software is built, reviewed and maintained. It also reframes model releases as threshold-crossing events rather than simple benchmark increments, which matters for anyone deciding when to adopt agentic tooling. The supplied text is truncated and only covers the opening slides, so the bulk of the chronological review is not visible; the closing keynote frames this as a work in progress since 'the year isn't over yet'. A telling caveat is his deliberately silly 'SVG of a pelican riding a bicycle' test, where neither Claude Opus 4.5 nor GPT-5.1 could draw a correct bicycle — evidence that gains in coding-agent reliability do not translate into general visual or spatial competence.

rss · Simon Willison · Sep 27, 23:54

**Background**: Simon Willison is a veteran developer and prolific blogger whose commentary on large language models is widely read across the software industry. A coding agent is an LLM paired with a harness — tooling that lets it read files, run commands and edit code — and Claude Code and Codex are two well-known examples of such harnesses. LLM releases are usually incremental, but occasionally a modest improvement crosses a threshold where a previously unusable capability suddenly becomes dependable, which is exactly the pattern Willison identifies for late 2025 and 2026.

**Tags**: `#LLM`, `#AI trends`, `#Simon Willison`, `#2026 retrospective`, `#developer conference`

---

<a id="item-2"></a>
## [Essay Warns LLM-Driven Dev Normalizes Inexplicable Failures](https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html) ⭐️ 8.4/10

A blog post on ihatethefuture.com titled "The Normalization of Inexplicable Failures" argues that agentic and LLM-assisted software development is making software failures that nobody can explain — or is accountable for — seem acceptable, as long as things "work most of the time." The essay reached 236 points and 97 comments on Hacker News, where engineers debated reproducibility, determinism, and correctness versus shipping speed. If the implicit standard for software shifts from "correct and explainable" to "works most of the time," the erosion of accountability spreads from end-user apps into shared libraries, infrastructure, and compilers, slowing down the entire ecosystem. This matters to anyone who maintains dependencies, debugs production incidents, or is accountable for systems where a broken contract must have a defined owner and a discoverable cause. The piece is opinion and analysis rather than research with hard data, and it frames the problem in terms of broken contracts, ownership, and the difference between "it works" and "it works for reasons we understand." Commenters added that LLM outputs are inherently non-deterministic (sampling-based), that "confidence scores" are an anthropomorphic metaphor rather than a real measure of correctness, and that heisenbug-like intermittent failures are exactly what becomes harder to root-cause under agent-generated code.

hackernews · pxx · Sep 27, 15:26 · [Discussion](https://news.ycombinator.com/item?id=49867486)

**Background**: Agentic development refers to software engineering where AI agents don't just autocomplete code but reason, plan, and execute multi-step tasks across the development lifecycle. Design by Contract is a long-standing software engineering principle in which module interfaces are governed by precise specifications of preconditions, postconditions, and invariants — so a failure means some contract was violated by someone. Large language models complicate this because their output is probabilistic: the same prompt can yield different code each run, which is why concepts like heisenbugs (bugs that change behavior or vanish when you try to observe them) and determinism have become central to the debate.

<details><summary>References</summary>
<ul>
<li><a href="https://www.agentic-dev.org/en/handbook/introduction/what-is-agentic-development">What is Agentic Development? — Handbook</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heisenbug">Heisenbug - Wikipedia</a></li>
<li><a href="https://proglang.informatik.uni-freiburg.de/teaching/swt/2014/swt-07-design-by-contract.en.pdf">Software Engineering - Lecture 07: Design by Contract</a></li>

</ul>
</details>

**Discussion**: Sentiment was largely sympathetic to the essay's diagnosis, though several commenters pushed back on the implied pessimism about agents. One self-described Nix/Elixir practitioner said he values reproducibility, determinism, and nine-nines reliability yet still uses agent-assisted development productively — provided every check in the book is in place, and noting agents have both introduced bugs he wouldn't have written and fixed bugs of his own. Another commenter argued that "good enough" tolerance may be fine for a consumer app but becomes catastrophic if normalized in libraries, infrastructure, and compilers, while a third dismissed "confidence scores" as a fundamentally anthropocentric notion that algorithms do not possess.

**Tags**: `#AI agents`, `#software reliability`, `#LLM-assisted development`, `#software engineering`, `#determinism`

---

<a id="item-3"></a>
## [Fireworks AI releases Ember-1, a Kimi K3-based efficient reasoning model](https://fireworks.ai/blog/ember-1) ⭐️ 8.0/10

Fireworks Research, the research arm of inference platform Fireworks AI, announced Ember-1, a specialized reasoning model built on top of Kimi K3 that produces shorter reasoning traces while using roughly 40% fewer tokens at comparable quality. The model is available through the Fireworks API and Playground as well as via OpenRouter. The release shows an infrastructure provider moving beyond simply hosting other companies' open models into doing its own model research, which could shift how users think about vendor neutrality and lock-in. Token-efficiency gains like this directly cut inference cost for long-reasoning workloads, intensifying price/performance competition among open-model providers. Ember-1 is described as a specialized model derived from Kimi K3 rather than a from-scratch pretraining run, and its main claimed benefit is shorter reasoning traces at comparable evaluation quality. Because the headline claim is a ~40% token reduction, the practical savings depend heavily on the specific workload and how much of the output is reasoning tokens.

hackernews · gmays · Sep 27, 17:31 · [Discussion](https://news.ycombinator.com/item?id=49868830)

**Background**: Fireworks AI is an inference platform known for fast, scalable deployment of open-source models, so customers do not have to manage GPU infrastructure themselves. Kimi K3 is a large reasoning model from Moonshot AI whose strong benchmark results have made it a common base or comparison point for other vendors. Reasoning models spend many extra tokens 'thinking' before answering, so token efficiency has become a key lever for reducing serving costs.

<details><summary>References</summary>
<ul>
<li><a href="https://fireworks.ai/blog/ember-1">Introducing Ember-1</a></li>
<li><a href="https://fireworks.ai/models/fireworks/ember-1">Ember-1 API & Playground | Fireworks AI</a></li>
<li><a href="https://openrouter.ai/fireworks/ember-1">Ember-1 - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread was broadly positive about open-model progress, with one commenter calling this a 'golden age of model training' after fine-tuning a Qwen 3 0.6B model for English-to-Bash translation in about two days. The main friction was trust: a commenter said they were uneasy that Fireworks, which they had relied on to host open models like DeepSeek, now ships its own competing model, while another argued Kimi K3 needs a price cut since competitor Sol offers better quality at lower cost (2/10 vs 3/15 pricing). One commenter compared open models overtaking proprietary ones to how Linux and Wikipedia overtook their incumbents, and a self-identified Fireworks employee joined to ask what follow-up research or educational material users would find useful.

**Tags**: `#AI`, `#LLM`, `#open-models`, `#model-training`, `#inference`

---

<a id="item-4"></a>
## [Neovim Accused of Deleting Vim's Persistent Undo Files](https://unsung.aresluna.org/they-had-no-concept-of-a-duty-of-care-to-their-users/) ⭐️ 7.7/10

A critical blog post argues that Neovim deleted persistent undo (undofile) data created by Vim, treating the incident as a failure of the project's "duty of care" toward user data. The piece sparked a large Hacker News thread in which Neovim maintainer justinmk posted a concrete counter-demonstration showing that Vim itself resets undofiles when an external tool edits a file. The dispute matters to anyone who switches between Vim and Neovim, because silently losing undo history can cost real work and is hard to notice until you press "u". More broadly, it turns a small format-compatibility decision into a test case for how open-source projects weigh backwards compatibility and user-data safety against internal refactoring. The undo file formats of Vim and Neovim diverged as of Neovim 0.4.4, following a commit in March 2021, so undo files are no longer interchangeable between the two editors. Neovim's documentation also notes that an undo file is ignored if its owner differs from the owner of the edited file, and justinmk's counter-example shows Vim resets its own undofile when git or nano rewrites the file while Vim is closed.

hackernews · jandeboevrie · Sep 27, 14:45 · [Discussion](https://news.ycombinator.com/item?id=49867067)

**Background**: Persistent undo, introduced in Vim 7.3, saves the undo tree to a file on disk so you can undo changes even after closing and reopening a file. Neovim began as a fork of Vim in 2014 with the goal of modernizing the codebase, and over time the two projects' internal file formats, including undofiles, drifted apart. Because these files live in a shared undo directory, a tool that rewrites or deletes unrecognized undo files can destroy history that another editor created.

<details><summary>References</summary>
<ul>
<li><a href="https://vi.stackexchange.com/questions/46731/can-neovim-understand-vim-undo-files">Can Neovim understand Vim undo files? - Vi and Vim Stack Exchange</a></li>
<li><a href="https://neovim.io/doc/user/undo/">Undo - Neovim docs</a></li>
<li><a href="https://stackoverflow.com/questions/5700389/using-vims-persistent-undo">Using Vim 's persistent undo ? - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Sentiment in the thread was largely sympathetic to the criticism but not unanimous: one commenter listed the alleged facts (breaking undo history, deleting another program's data, knowing it in advance) while annotating that one point was not really accurate, and a long-time Vim user said they felt "terribly vindicated" for ignoring Neovim. A Neovim user reported a possible unnoticed undo loss after an upgrade and worried about format instability, while justinmk's reproduction of Vim's own undofile reset was offered as a rebuttal, and one commenter simply warned to "be careful with any vim fork."

**Tags**: `#neovim`, `#vim`, `#open-source-governance`, `#data-loss`, `#software-engineering`

---

<a id="item-5"></a>
## [mitxela Renders Fluid Animations on Repurposed Flip-Dot Displays](https://mitxela.com/projects/flipflip) ⭐️ 7.4/10

mitxela has published a project writeup titled "Flip Fluid on Flip Dots" in which he repurposes flip-dot displays — the electromechanical dot-matrix panels once common on buses and station signs — to render fluid-like animations, documenting the delicate hardware work needed to drive their tiny magnets and coils. It demonstrates genuinely novel creative reuse of a nearly obsolete electromechanical display technology, and the detailed writeup gives embedded-systems and creative-hardware developers reusable knowledge about reverse-engineering salvage hardware and designing custom driver electronics for it. The article notes that flip dots are extremely delicate: their magnet wire is hair-thin and their plastic bodies melt easily, so even the best desoldering equipment makes extraction slow work, and reversing the current direction in each coil usually requires capacitor-based driver tricks that an alternative negative supply rail could avoid.

hackernews · blutack · Sep 26, 07:50 · [Discussion](https://news.ycombinator.com/item?id=49854219)

**Background**: A flip-disc (flip-dot) display is an electromechanical dot-matrix technology used for large outdoor signs, bus and train destination boards and highway variable-message signs, and famously for the Family Feud game board. Each pixel is a small disc with a magnet that flips between its black and fluorescent-yellow faces when a current pulse through a surrounding coil generates a magnetic field; because the state is bistable, the display needs no power to hold an image. "FLIP" in this project refers to Fluid Implicit Particle simulation, the popular liquid-simulation technique also used by the FLIP Fluids addon for Blender, whose characteristic swirls mitxela is reproducing mechanically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flip-dot_display">Flip-dot display</a></li>
<li><a href="https://flipfluids.com/">FLIP Fluids Addon for Blender – FLIP Fluids Addon For Blender</a></li>
<li><a href="https://github.com/rlguy/Blender-FLIP-Fluids">GitHub - rlguy/Blender-FLIP-Fluids: The FLIP Fluids addon is a tool that helps you set up, run, and render high quality liquid fluid effects all within Blender, the free and open source 3D creation suite. · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by mitxela's precision work while adding practical tips: one suggested using a hot-air gun on the back of the board so the dots simply drop out instead of desoldering pins one by one, and another proposed replacing the usual capacitor-based drive with a negative supply rail so a coil's current direction can be flipped using only two transistors. Others shared related finds, including a flip-dot panel from Breakfast Studio (noted for its colour and quiet operation), a link to the Eurovision entry the article omitted, and one reader's own flip-dot unit salvaged from an old bus.

**Tags**: `#hardware`, `#embedded-systems`, `#flip-dot-display`, `#reverse-engineering`, `#creative-electronics`

---

<a id="item-6"></a>
## [Don't couple your Go code to GitHub, blog argues](https://iain.rocks/blog/dont-couple-your-go-code-to-github) ⭐️ 7.1/10

A blog post on iain.rocks argues that Go teams should namespace their internal libraries and packages with custom (vanity) domains instead of github.com paths, so that the code is not tied to a single git host. The post sparked a Hacker News thread with 59 comments debating whether the go.mod 'replace' directive is a viable escape hatch and raising worries about domain ownership and package hijacking. A module path is baked into every import statement and every go.mod requirement, so migrating git hosts normally forces changes across all dependent repositories. Vanity import paths make the module's identity independent of the hosting provider, which reduces migration cost and limits single-vendor dependency in the software supply chain — a concern for any team maintaining internal Go libraries over the long term. Vanity import paths work by serving a go-import meta tag from the custom domain, which tells the go command where the repository actually lives; commenters point out this simply shifts the single point of failure to the domain, since a registry like VeriSign can unilaterally delete a domain name. Others note that a go.mod 'replace' directive can redirect a module to a fork or another host, but it cannot make old releases buildable without editing every dependency that transitively pulls in the moved module.

hackernews · birdculture · Sep 27, 16:50 · [Discussion](https://news.ycombinator.com/item?id=49868404)

**Background**: In Go, a module path such as github.com/example/A serves double duty: it is the module's canonical identity and the URL that the go command uses to locate the source, either through a module proxy or by hitting the repository directly. A vanity import path instead uses a domain you control, for example example.com/pkg, and that domain serves a small HTML page containing a go-import meta tag that points to wherever the repository is hosted. This lets a team move from GitHub to GitLab or a self-hosted server without changing a single import statement, and tools such as go-vanity or vanity-imports exist to generate those pages.

<details><summary>References</summary>
<ul>
<li><a href="https://pkg.go.dev/go.mlcdf.fr/vanity-imports">vanity-imports command - go.mlcdf.fr/vanity-imports - Go Packages</a></li>
<li><a href="https://go.dev/doc/modules/managing-source">Managing module source - The Go Programming Language</a></li>
<li><a href="https://github.com/ananthb/go-vanity">GitHub - ananthb/go-vanity: Vanity import paths for Go ...</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly sympathetic to the principle — one commenter says it applies to other language stacks too, since even GitHub links in code comments rot after a migration — but the thread pushes back on practicality. A detailed comment walks through a module graph (A depends on B depends on C) to show that 'replace' directives do not let you build old releases without editing every dependency, another warns that the vanity domain itself is a fragile single point of failure given domain-deletion risk, and a third raises package-hijacking concerns about copycat packages surfacing in search results and being pulled in by Go tooling. At least one commenter dismisses the whole idea as premature optimization because 'replace' already handles the common cases.

**Tags**: `#golang`, `#dependency-management`, `#software-engineering`, `#dev-tools`, `#supply-chain-security`

---