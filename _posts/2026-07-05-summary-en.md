---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 56 items, 7 important content pieces were selected

---

1. [Better Models: Worse Tools](#item-1) ⭐️ 9.0/10
2. [Claude Fable AI Reviews sqlite-utils 4.0rc2, Finds Critical Bugs](#item-2) ⭐️ 8.4/10
3. [Vercel AI SDK Fixes Silent Drop of Disabled Thinking Parameter](#item-3) ⭐️ 7.9/10
4. [AI tutor improves student performance by 0.71-1.30 SD](#item-4) ⭐️ 7.7/10
5. [Digital game ownership debate: It's about control, not format](#item-5) ⭐️ 7.7/10
6. [Free Online Textbook: Build a C-Style Compiler Step by Step](#item-6) ⭐️ 7.5/10
7. [Organic Maps Fork CoMaps Sparks Governance Debate](#item-7) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [Better Models: Worse Tools](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 9.0/10

Armin Ronacher discovered that newer Anthropic Claude models (Opus 4.8, Sonnet 5) generate malformed tool calls with extra invented fields when using Pi's edit tool, unlike older models. This matters because it reveals a counterintuitive regression where state-of-the-art improvements in tool-specific training degrade performance on generic tool-calling, potentially forcing third-party coding harnesses to adapt to model-specific quirks and fragmenting the ecosystem. The problem affects nested edits[] arrays where newer models invent extra keys, while older models adhere to the schema; Armin theorizes that reinforcement learning for Claude's built-in edit tool causes this, harming custom tools like Pi's.

rss · Simon Willison · Jul 4, 22:53

**Background**: Tool-calling in LLMs allows models to generate structured JSON arguments matching a predefined schema. While reinforcement learning can improve performance on specific tools, it may cause overfitting to those schemas, leading to hallucinations when calling similar but distinct tools. This highlights a trade-off between specialization and generalization in model training.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.00737v1">To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling</a></li>
<li><a href="https://llm-stats.com/leaderboards/best-ai-for-tool-calling">Best AI for Tool Calling 2026 - Top Function Calling Models</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#tool-calling`, `#model regression`, `#Claude`

---

<a id="item-2"></a>
## [Claude Fable AI Reviews sqlite-utils 4.0rc2, Finds Critical Bugs](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything) ⭐️ 8.4/10

Simon Willison used Anthropic's Claude Fable AI model to review the sqlite-utils 4.0rc2 codebase, costing about $149.25, and discovered several critical bugs including a data loss bug in delete_where() that left connections in an uncommitted transaction state. This demonstrates that advanced AI models can effectively perform deep code reviews for major releases, catching subtle bugs that could have caused data loss or breaking changes, at a relatively low cost compared to human review. The review involved 37 prompts, 34 commits, and +1,321 -190 code changes across 30 files, with 5 'release blocker' bugs identified, including a data loss bug where delete_where() never committed and poisoned the connection for subsequent operations.

rss · Simon Willison · Jul 5, 01:00

**Background**: sqlite-utils is a Python library and CLI tool for building SQLite databases, created by Simon Willison. Claude Fable is Anthropic's latest AI model with state-of-the-art performance. The review was done during the final phase before shipping sqlite-utils 4.0 stable.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/3.14/python-api.html">sqlite _ utils Python library — sqlite - utils 3.14 documentation</a></li>
<li><a href="https://pypi.org/project/sqlite-utils/">CLI tool and Python library for manipulating SQLite databases</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#software engineering`, `#sqlite-utils`, `#code review`

---

<a id="item-3"></a>
## [Vercel AI SDK Fixes Silent Drop of Disabled Thinking Parameter](https://github.com/vercel/ai/releases/tag/%40ai-sdk/anthropic%404.0.8) ⭐️ 7.9/10

@ai-sdk/anthropic 4.0.8 fixes a bug where setting `thinking: { type: 'disabled' }` was silently stripped from the outgoing request, and now properly forwards it to the Anthropic API. This fix is important because models like Claude Sonnet 5 enable extended thinking by default, which can consume token budget unnecessarily; ensuring the disabled flag is respected gives users full control over API usage and costs. The patch in commit 0aa0ff3 ensures that both `providerOptions.anthropic.thinking = { type: 'disabled' }` and top-level `reasoning: 'none'` are now sent to the Anthropic Messages API instead of being ignored.

github · github-actions[bot] · Jul 4, 06:11

**Background**: The Anthropic Claude API supports an extended thinking mode that allows models to reason for longer, but some tasks (e.g., tool use) require disabling it. Certain models, such as Claude Sonnet 5, enable thinking by default, so explicitly setting `disabled` is necessary to avoid consuming the `max_tokens` budget. Prior to this fix, the SDK silently dropped the disable directive, leaving thinking active.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/model-config">Model configuration - Claude Code Docs</a></li>
<li><a href="https://github.com/n8n-io/n8n/issues/15715">Anthropic Models with "Enable Thinking" Fail in AI Agent When Using Tools Due to Message Formatting · Issue #15715 · n8n-io/n8n</a></li>

</ul>
</details>

**Tags**: `#AI SDK`, `#Vercel`, `#Anthropic`, `#bug fix`

---

<a id="item-4"></a>
## [AI tutor improves student performance by 0.71-1.30 SD](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf) ⭐️ 7.7/10

A paper presented at the Intextbooks Workshop 2026 reports that an AI tutor using LLMs improved student performance by 0.71 to 1.30 standard deviations in a Dartmouth College course, based on observational data from 145 students. This study suggests potential for AI-driven personalized tutoring at scale, but its non-randomized design and small effective sample size (only 16 fully engaged students) undermine causal claims, highlighting the need for rigorous evaluation in educational AI research. The claimed effect size of 0.71–1.30 SD is derived from a statistical model controlling for prior grades, not from a randomized controlled trial. Only 11% of the treatment group (16 students) reached the defined 'full engagement' level.

hackernews · jonahbard · Jul 5, 18:47 · [Discussion](https://news.ycombinator.com/item?id=48796817)

**Background**: Effect size, measured in standard deviations (SD), is commonly used in education research to quantify the magnitude of an intervention's impact. An effect size of 0.4 is considered average for educational interventions. Standard deviation measures how spread out data are from the mean; a larger SD indicates more variability. This study's reported effect sizes are unusually large, which often raises suspicion about study design flaws such as selection bias or small sample sizes.

<details><summary>References</summary>
<ul>
<li><a href="https://ies.ed.gov/rel-west/2025/01/main-resource-file-1">EVIDENCE USE IN EDUCATION NOVEMBER 2021 Effect Size Basics:</a></li>
<li><a href="https://en.wikipedia.org/wiki/Standard_deviation">Standard deviation - Wikipedia</a></li>
<li><a href="https://www.ascd.org/el/articles/interpreting-education-research-and-effect-sizes">Interpreting Education Research and Effect Sizes</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News express skepticism, pointing out that the study is not randomized, the headline result relies on a statistical model rather than direct comparison, and the Hawthorne effect (novelty-induced productivity gain) may inflate results. One commenter notes that only 16 students achieved full engagement, calling the sample size insufficient. Another suggests combining LLMs with physical note-taking for better scalability.

**Tags**: `#AI tutor`, `#LLM`, `#education`, `#effect size`, `#Dartmouth`

---

<a id="item-5"></a>
## [Digital game ownership debate: It's about control, not format](https://popcar.bearblog.dev/its-about-ownership/) ⭐️ 7.7/10

An article argues that the core issue in the physical vs. digital game debate is consumer ownership, specifically the ability to transfer, lend, and retain access to purchased software indefinitely. This highlights a growing concern among gamers and consumer advocates that digital game purchases often lack the ownership rights associated with physical copies, potentially impacting long-term access and resale value. The article suggests regulatory changes could mandate that digital purchases include transferability and offline access, similar to physical goods, and notes that some platforms like Steam allow DRM-free usage.

hackernews · popcar2 · Jul 5, 14:56 · [Discussion](https://news.ycombinator.com/item?id=48794750)

**Background**: Digital rights management (DRM) technologies often restrict how consumers use purchased digital content, such as requiring online activation or preventing resale. The debate over ownership has intensified as digital game sales have surpassed physical, with many consumers realizing they may not truly own the games they buy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Always-on_DRM">Always-on DRM - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that digital ownership is limited, citing experiences of games becoming unplayable after servers shut down or subscriptions end. Some argue that cracks and piracy provide actual ownership, while others call for regulation to enforce transferability and long-term access.

**Tags**: `#ownership`, `#digital rights`, `#gaming`, `#DRM`, `#consumer protection`

---

<a id="item-6"></a>
## [Free Online Textbook: Build a C-Style Compiler Step by Step](https://dthain.github.io/books/compiler/) ⭐️ 7.5/10

Douglas Thain's 'Introduction to Compilers and Language Design' is a free online textbook that guides readers through building a C-style compiler from scratch, with the project available on GitHub. This resource makes compiler construction accessible to self-learners and students, filling a gap for practical, hands-on materials in a traditionally challenging area of computer science. The textbook is based on Professor Thain's course at the University of Notre Dame, and the sample project closely mirrors the actual course project, leading students to a working compiler.

hackernews · AlexeyBrin · Jul 5, 11:54 · [Discussion](https://news.ycombinator.com/item?id=48793454)

**Background**: Compilers translate high-level programming languages into machine code. Learning how to build one helps programmers understand language design, optimization, and system internals. Many compiler textbooks focus on theory; this one emphasizes hands-on building of a C-like language.

**Discussion**: Former student shuyang praised the course as excellent. User userbinator suggested alternative tiny compilers C4 and C4x86 for further study. Others noted the book focuses more on compilers than language design, with commenter conartist6 pointing out that major language design topics are missing.

**Tags**: `#compilers`, `#language design`, `#programming`, `#education`

---

<a id="item-7"></a>
## [Organic Maps Fork CoMaps Sparks Governance Debate](https://organicmaps.app/) ⭐️ 7.3/10

The Organic Maps project, a popular open-source offline navigation app, has seen a community fork called CoMaps emerge due to concerns over governance and licensing. CoMaps aims to provide a more transparent and community-driven alternative, with features like CarPlay Dashboard support being developed. This fork highlights critical issues in open-source governance, transparency, and licensing that can affect user trust and project sustainability. It affects users who prioritize privacy and FOSS principles, and may influence how similar projects manage community relations. Organic Maps has been accused of quietly adding ads, turning previously open-source code proprietary, and misappropriating donations, according to community comments. CoMaps, forked about a year ago, is now gaining features and community support, and has been audited for no data collection.

hackernews · tosh · Jul 5, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48794446)

**Background**: Organic Maps is an offline navigation app that uses map data from OpenStreetMap, designed to work without internet and with strong privacy protections (no ads, no tracking). The project was created by the same developers behind MapsWithMe/Maps.Me. However, concerns arose about the inclusion of non-open-source components and governance issues, leading to a community fork named CoMaps, which emphasizes full openness and community accountability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Organic_Maps">Organic Maps - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoMaps">CoMaps</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed sentiments: some praised Organic Maps for its usability but noted the fork; others strongly criticized Organic Maps for alleged unethical behavior like adding ads and making code proprietary, recommending CoMaps instead. There were also calls for more testers and developers for iOS features, and a desire for a web client to reduce reliance on apps.

**Tags**: `#open-source`, `#navigation`, `#software-engineering`, `#governance`, `#FOSS`

---