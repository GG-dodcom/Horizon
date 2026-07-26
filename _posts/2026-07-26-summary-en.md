---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
---

> From 46 items, 7 important content pieces were selected

---

1. [Inside the Relay Market for Discounted LLM Tokens via Fraud](#item-1) ⭐️ 8.5/10
2. [Handing off details to AI can be disempowering](#item-2) ⭐️ 8.4/10
3. [GrapheneOS auto-reboot protects locked devices from data extraction](#item-3) ⭐️ 8.4/10
4. [AI Superpowers: Focus & Followthrough](#item-4) ⭐️ 8.2/10
5. [Ruff v0.16.0 Expands Default Rules to 413](#item-5) ⭐️ 7.6/10
6. [EU Proposal to Kill Cookie Banners with Browser Privacy Settings](#item-6) ⭐️ 7.1/10
7. [Decker revives HyperCard for modern interactive documents](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Inside the Relay Market for Discounted LLM Tokens via Fraud](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.5/10

An investigation by Matt Lenhard reveals a thriving relay market in China where resellers use open-source proxy software like one-api and new-api to pool API keys and resell LLM tokens at a discount through fraud, including abusing free trials, unprotected support bots, stolen credit cards, and chargeback attacks. This market undermines LLM vendors' revenue models and poses security risks for developers exposing LLM applications publicly, highlighting the urgent need for better API usage caps and fraud detection. The ecosystem also enables data collection for model distillation, impacting intellectual property. The proxy software one-api and new-api are legitimate open-source projects for managing and distributing LLM API keys, but they are exploited by resellers to load-balance requests across pooled credentials. Buyers include those seeking cheap tokens, circumventing geo-restrictions, or harvesting data for model distillation.

rss · Simon Willison · Jul 26, 19:30

**Background**: LLM API tokens are typically sold by vendors like OpenAI at fixed prices, but a secondary relay market has emerged where resellers aggregate credentials from various sources—such as free trials, compromised accounts, or stolen credit cards—and offer them at a discount. Open-source proxy tools like one-api and new-api, designed for legitimate key management, are repurposed to build these relay services. The practice is concentrated in China, with forum discussions on V2EX serving as a key source for the investigation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/songquanpeng/one-api">GitHub - songquanpeng/one-api: LLM API 管理 & 分发系统，支持 Open...</a></li>

</ul>
</details>

**Discussion**: Community comments draw parallels to advertising fraud markets, noting that similar resale ecosystems have existed for other internet products. Commenters highlight the abuse of free cloud credits (e.g., AWS) as a major enabler, and compare the dynamic to ticket touting. Some question the sustainability of subscription models for AI tokens, arguing that arbitrage opportunities are inherent when prices are not market-clearing.

**Tags**: `#LLM`, `#fraud`, `#API security`, `#token reselling`, `#China`

---

<a id="item-2"></a>
## [Handing off details to AI can be disempowering](https://davidnicholaswilliams.com/its-not-empowering-to-hand-off-the-details/) ⭐️ 8.4/10

The article argues that relying on AI to handle details reduces true understanding and agency, as empowerment comes from grappling with specifics rather than delegating them. This perspective challenges the prevalent narrative that AI coding tools and agentic systems automatically empower developers, urging a more nuanced view of human-AI collaboration. It resonates with concerns about skill degradation and loss of deep technical expertise. The article is written by David Nicholas Williams and has a score of 8.4/10 for high relevance to AI coding tools and developer empowerment. It is tagged with AI, LLM, software engineering, developer tools, and agentic systems.

hackernews · davnicwil · Jul 26, 17:58 · [Discussion](https://news.ycombinator.com/item?id=49060592)

**Background**: Agentic systems are autonomous AI systems that can reason, plan, and execute complex workflows with minimal human intervention. The article challenges the assumption that delegating details to such systems is inherently empowering, suggesting instead that genuine understanding comes from engaging with specifics.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/agentic_ai">Agentic AI</a></li>
<li><a href="https://medium.com/mongodb/here-are-7-design-patterns-for-agentic-systems-you-need-to-know-d74a4b5835a5?trk=article-ssr-frontend-pulse_little-text-block">7 Design Patterns for Agentic Systems You NEED to Know | MongoDB</a></li>

</ul>
</details>

**Discussion**: Commenters express mixed views: some agree that over-reliance on AI leads to fatigue and loss of control, while others argue that verification does not require full understanding and that delegating can be empowering if one focuses on high-level design. A commenter notes that experienced developers develop judgment on what details to scrutinize, and another shares a positive experience using AI for a Sega Genesis homebrew game, focusing on creative aspects.

**Tags**: `#AI`, `#LLM`, `#software engineering`, `#developer tools`, `#agentic systems`

---

<a id="item-3"></a>
## [GrapheneOS auto-reboot protects locked devices from data extraction](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 8.4/10

A Hacker News thread highlights GrapheneOS's 18-hour auto-reboot feature, which returns a locked device to the Before First Unlock (BFU) state, preventing forensic data extraction even without a duress password. This feature significantly enhances mobile device security for journalists, activists, and privacy-conscious users by ensuring that encryption keys are not accessible when the device is unattended, thwarting forensic tools used by law enforcement and attackers. The auto-reboot triggers after 18 hours of inactivity, resetting the device to BFU mode where full disk encryption keys are not loaded into memory, making data extraction nearly impossible. This is an upstream Android feature enhanced by GrapheneOS.

hackernews · Cider9986 · Jul 26, 05:57 · [Discussion](https://news.ycombinator.com/item?id=49055169)

**Background**: Mobile devices have two main lock states: Before First Unlock (BFU) and After First Unlock (AFU). In BFU mode, the device is powered on but the user has not yet entered the passcode, so the file-based encryption keys are absent, limiting data access. Once unlocked (AFU), encryption keys are in memory, making extraction easier. GrapheneOS's auto-reboot forces a return to BFU after a period of inactivity, minimizing the window of vulnerability.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.dsu.edu/digforce/2023/08/23/bfu-and-afu-lock-states/">BFU and AFU Lock States – Blog | DigForCE Lab - DSU</a></li>
<li><a href="https://discuss.grapheneos.org/d/23736-automatic-18-hour-reboots">Automatic 18 hour reboots - GrapheneOS Discussion Forum</a></li>
<li><a href="https://teeltechcanada.com/understanding-mobile-device-lock-states-in-forensic-extractions/">Understanding Mobile Device Lock States in Forensic ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the feature's strong protection, with rzk noting it works even without a duress password. Prmoustache called for a complete backup solution to enable pre-border wiping, while muyuu analyzed pattern lock entropy. Himata4113 pointed out similar protections on Apple devices, and usern20260720 expressed appreciation for a phone not conspiring against its user.

**Tags**: `#GrapheneOS`, `#mobile security`, `#data extraction`, `#BFU mode`, `#privacy`

---

<a id="item-4"></a>
## [AI Superpowers: Focus & Followthrough](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and) ⭐️ 8.2/10

The article posits that AI, particularly coding agents, can enhance developers' focus and followthrough, reducing cognitive load and enabling them to tackle more projects efficiently. This shift could dramatically improve software development productivity, reduce burnout, and allow developers to allocate more time to creative problem-solving rather than repetitive tasks. The article identifies focus and followthrough as new superpowers amplified by AI, with developers using agents to explore what-if projects and fix configuration issues without getting bogged down.

hackernews · mooreds · Jul 26, 13:13 · [Discussion](https://news.ycombinator.com/item?id=49057877)

**Background**: AI coding assistants like GitHub Copilot and Cursor have become common in software development, automating boilerplate code and debugging. However, this article emphasizes the human-centric skills of maintaining focus and following through on projects, which AI can augment to improve overall workflow.

**Discussion**: Commenters express mixed sentiments: some worry about fragmented, incompatible solutions proliferating, while others report reduced burnout and increased feature velocity when using AI agents. One user notes that AI helps with the 99% but not the last 1% of a project.

**Tags**: `#AI`, `#LLM`, `#programming`, `#productivity`, `#software engineering`

---

<a id="item-5"></a>
## [Ruff v0.16.0 Expands Default Rules to 413](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.6/10

Ruff v0.16.0 increases the number of default rules from 59 to 413, causing CI failures for many projects that rely on unpinned Ruff versions. This change forces Python developers to update their configurations and fix thousands of newly flagged issues, while also demonstrating the growing capability of AI coding agents to automate such fixes. The update was shipped on July 23, 2026, and the `uvx ruff@latest check . --fix --unsafe-fixes` command can automatically fix most issues; for example, it resolved 1,538 out of 1,618 errors in the sqlite-utils project.

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is an extremely fast Python linter and code formatter written in Rust, developed by Astral (now part of OpenAI). It serves as a drop-in replacement for tools like Flake8, isort, and pydocstyle. The previous default rule set was frozen since version 0.1.0, while the total number of available rules grew from 708 to 968.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code ...</a></li>
<li><a href="https://pypi.org/project/ruff/">ruff · PyPI</a></li>

</ul>
</details>

**Tags**: `#Ruff`, `#Python`, `#linting`, `#developer tools`, `#Astral`

---

<a id="item-6"></a>
## [EU Proposal to Kill Cookie Banners with Browser Privacy Settings](https://killthecookiebanner.eu/) ⭐️ 7.1/10

The European Commission has proposed a browser-level privacy preference solution that would allow users to set their privacy preferences once and never see cookie banners again, but the tracking industry is pushing back against the proposal. If adopted, this could eliminate the annoying and often misleading cookie banners that plague the web, giving users real control over their privacy while setting a potential global standard for consent management. The proposal builds on existing technologies like Global Privacy Control (GPC), which already has legal force under some privacy laws; however, the tracking industry and major ad companies are lobbying against it to preserve their ability to track users.

hackernews · rapnie · Jul 26, 11:53 · [Discussion](https://news.ycombinator.com/item?id=49057175)

**Background**: Cookie banners are required under EU law (ePrivacy Directive and GDPR) to obtain user consent for non-essential cookies. However, many banners are designed to nudge users into accepting tracking, leading to widespread criticism. The Global Privacy Control (GPC) is a browser signal that tells websites the user does not want their data sold or shared, and it is recognized by some state laws like the California Consumer Privacy Act (CCPA).

<details><summary>References</summary>
<ul>
<li><a href="https://killthecookiebanner.eu/">Kill the Cookie Banner !</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Privacy_Control">Global Privacy Control</a></li>
<li><a href="https://privacybadger.org/">Privacy Badger | Electronic Frontier Foundation</a></li>

</ul>
</details>

**Discussion**: Commenters on the news largely support the proposal, with some arguing that the EU should go further by declaring that ticking a checkbox cannot constitute informed consent. Others point out that California has already enacted similar browser-level controls, and some simply suggest that the easiest solution is to stop tracking users altogether.

**Tags**: `#privacy`, `#cookie banners`, `#EU regulation`, `#browser standards`, `#web technology`

---

<a id="item-7"></a>
## [Decker revives HyperCard for modern interactive documents](https://beyondloom.com/decker/) ⭐️ 7.0/10

Decker, a multimedia platform inspired by HyperCard, has been released as a modern tool for creating interactive documents with sound, images, hypertext, and scripting. Decker brings back the accessible, intuitive programming environment of HyperCard, which empowered non-programmers to build applications, potentially reigniting a grassroots software creation movement. Decker features a classic MacOS aesthetic but runs on modern systems, and uses its own scripting language (Lil) for interactivity. It aims to be a spiritual successor to HyperCard with a focus on simplicity and retro charm.

hackernews · tosh · Jul 26, 18:23 · [Discussion](https://news.ycombinator.com/item?id=49060856)

**Background**: HyperCard, released by Apple in 1987, was a revolutionary hypermedia system that combined a database with a graphical interface, allowing non-programmers to create 'stacks' of cards with buttons, text, and media. It predated the World Wide Web and inspired a generation of developers and hobbyists. Decker, created by John Earnest, seeks to recreate that experience with modern compatibility and a 1-bit retro aesthetic.

<details><summary>References</summary>
<ul>
<li><a href="https://beyondloom.com/decker/">Decker</a></li>
<li><a href="https://en.wikipedia.org/wiki/HyperCard">HyperCard - Wikipedia</a></li>
<li><a href="https://hackaday.com/2023/09/22/decker-is-the-cozy-retro-creative-engine-you-didnt-know-you-needed/">Decker Is The Cozy Retro Creative Engine You Didn’t Know You Needed | Hackaday</a></li>

</ul>
</details>

**Discussion**: Community comments express strong nostalgia for HyperCard, with users recalling how it made programming accessible. Some compare Decker favorably to modern tools like Delphi and Lazarus, while others question whether such a platform can find a place in today's web-centric world. Overall sentiment is positive, with hope that Decker can revive the ease and fun of HyperCard.

**Tags**: `#hypercard`, `#retrocomputing`, `#programming-tools`, `#decker`

---