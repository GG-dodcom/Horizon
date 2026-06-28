---
layout: default
title: "Horizon Summary: 2026-06-28 (EN)"
date: 2026-06-28
lang: en
---

> From 65 items, 7 important content pieces were selected

---

1. [Patient Uses Claude Code for MRI Second Opinion](#item-1) ⭐️ 8.7/10
2. [GLM 5.2 Outperforms Claude in Security Benchmarks](#item-2) ⭐️ 8.3/10
3. [OpenAI Codex Issue #2847: Need for Sensitive File Exclusion](#item-3) ⭐️ 8.3/10
4. [Brown professor denounces mass AI fraud on exam](#item-4) ⭐️ 7.8/10
5. [AI Forces Mathematicians to Rethink Their Work's Meaning](#item-5) ⭐️ 7.2/10
6. [LiteLLM v1.91.0-rc.1 adds Docker image signing](#item-6) ⭐️ 7.1/10
7. [Why Polish Diacritics Vanish in Software](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Patient Uses Claude Code for MRI Second Opinion](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.7/10

A software developer used Claude Code, an AI coding agent, to analyze their shoulder MRI and obtain a second opinion, documenting the experience in a detailed blog post. This case highlights the growing intersection of large language models and personal healthcare, raising critical questions about AI reliability, trust, and the role of expert radiologists. Claude Code is primarily designed for software development tasks, not medical imaging; radiologists in the community noted that a proper evaluation requires the full 3D MRI dataset, not just snapshots.

hackernews · engmarketer · Jun 28, 16:35 · [Discussion](https://news.ycombinator.com/item?id=48708941)

**Background**: Claude Code is an AI coding agent developed by Anthropic, trained using constitutional AI to align with ethical guidelines. While FDA-cleared AI solutions for radiology second opinions exist (e.g., Braid Health), they typically combine AI with human radiologists; standalone use of general-purpose AI for medical diagnosis is not standard practice.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://braid.health/www/page/same-day-radiology-second-opinion">Braid Health | AI Radiology Second Opinions & Ask AI</a></li>

</ul>
</details>

**Discussion**: Radiologists emphasized the need for complete imaging data and cautioned against over-reliance on AI. Some commenters appreciated the empowerment of questioning medical decisions, while others shared personal stories of misdiagnosis, highlighting systemic issues in healthcare.

**Tags**: `#AI`, `#healthcare`, `#radiology`, `#LLM`, `#personal experience`

---

<a id="item-2"></a>
## [GLM 5.2 Outperforms Claude in Security Benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.3/10

Semgrep's benchmarks show that the GLM 5.2 model outperforms Claude in cybersecurity vulnerability detection, finding bugs at a lower cost per vulnerability. This demonstrates that open-source LLMs can surpass proprietary models in specialized security tasks, potentially reducing costs for security teams and challenging the dominance of closed models. GLM 5.2 is reportedly a 753B-parameter model (though some sources list 376.7B), and in Semgrep's tests, it achieved a higher bug-finding rate than Claude at roughly $0.17 per vulnerability.

hackernews · jms703 · Jun 28, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48709670)

**Background**: Semgrep is an open-source static code analysis tool used for finding security vulnerabilities and enforcing coding standards. The benchmarks tested LLMs' ability to identify real-world cybersecurity bugs. GLM 5.2 is a recent open-source LLM from zai-org, optimized for coding and long-horizon tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://ollama.com/library/glm-5.2">GLM - 5 . 2 is Z.ai’s flagship model for the era of long-horizon tasks.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semgrep">Semgrep - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that GLM 5.2 is a solid workhorse for daily programming and security tasks, though some note that comparing a model to Claude Code (an agent harness) may be misleading. Others report that the benchmark numbers seem low compared to their own experiences.

**Tags**: `#AI`, `#LLM`, `#benchmarks`, `#GLM`, `#Claude`

---

<a id="item-3"></a>
## [OpenAI Codex Issue #2847: Need for Sensitive File Exclusion](https://github.com/openai/codex/issues/2847) ⭐️ 8.3/10

A GitHub issue (openai/codex#2847) discusses the need for a feature to exclude sensitive files from OpenAI Codex, with community members proposing workarounds such as using chmod to restrict file access or running Codex in a container. This issue highlights a critical security gap in AI coding agents, where sensitive data can be inadvertently exposed via tool outputs or model behavior. Proper file exclusion is essential for enterprise adoption and safe usage of AI-assisted development. Community comments argue that an opt-in approach (like sandboxing) is more reliable than an opt-out blocklist, and that the feature alone cannot guarantee security due to the unpredictable nature of LLMs. Some users have already built internal sandboxing solutions.

hackernews · pikseladam · Jun 28, 12:27 · [Discussion](https://news.ycombinator.com/item?id=48706714)

**Background**: Chmod is a Unix command that changes file permissions to control read, write, and execute access. Containerization, in computing, isolates applications in user-space environments called containers, limiting their access to host resources. These are system-level security measures that can prevent AI agents from accessing sensitive files.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chmod">Chmod</a></li>
<li><a href="https://en.wikipedia.org/wiki/Containerization_(computing)">Containerization (computing) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is divided: some believe an opt-out blocklist is insufficient and even dangerous, providing false security; others argue that system-level tools like chmod and containers already solve the problem, and any enforcement at the agent level is futile. Several users share their own sandboxing implementations.

**Tags**: `#AI`, `#security`, `#codex`, `#LLM`, `#privacy`

---

<a id="item-4"></a>
## [Brown professor denounces mass AI fraud on exam](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 7.8/10

A Brown University economics professor, a game theory expert, discovered that the majority of students in his class used AI to cheat on a take-home, closed-book exam, marking what he calls the worst academic integrity breach in his 34-year career. This incident highlights the growing challenge AI poses to traditional take-home exams and may accelerate the shift toward in-person, handwritten testing. It also underscores the game-theoretic dilemma where students rationally choose to use AI when others likely do. The exam was a take-home, closed-book type, which the professor believed would allow harder questions. Despite his expertise in game theory, he did not anticipate the scale of cheating; many students submitted answers clearly generated by large language models.

hackernews · geox · Jun 28, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48708991)

**Background**: Large language models (LLMs) like GPT-4 can generate human-like text, making it difficult to detect AI-generated answers on written exams. Game theory, a field the professor specializes in, predicts that when all students have access to AI, using it becomes the dominant strategy, even if individual integrity is high.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s40979-024-00154-7">Integrity games: an online teaching tool on academic ...</a></li>

</ul>
</details>

**Discussion**: Commenters widely agreed that AI makes take-home exams untenable, with one pointing out the game-theoretic inevitability of students using AI. Others expressed disappointment in the lack of integrity at an elite institution, while some criticized the take-home closed-book format as inherently contradictory.

**Tags**: `#AI`, `#education`, `#academic integrity`, `#LLMs`, `#game theory`

---

<a id="item-5"></a>
## [AI Forces Mathematicians to Rethink Their Work's Meaning](https://www.solidot.org/story?sid=84695) ⭐️ 7.2/10

Terence Tao and others are envisioning a future where humans and AI collaborate on complex mathematical problems, with AI handling technical tasks while humans focus on creativity. This shift could transform mathematical practice, enabling larger-scale collaboration and potentially accelerating discovery, while forcing mathematicians to reassess the value of human intuition and creativity. AI has evolved from 'stochastic parrots' that merely repeat patterns to advanced reasoning machines in just a few years. Tao has already begun implementing this collaborative vision in his own work.

rss · Solidot · Jun 27, 16:02

**Background**: The term 'stochastic parrot' was introduced in a 2021 paper to critique large language models for mimicking language without understanding. Tao's concept of 'big mathematics' envisions decentralized human-AI collaboration on massive problems, building on earlier computational proofs like the four-color theorem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_parrot">Stochastic parrot</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Terence Tao`, `#LLM`, `#scientific impact`

---

<a id="item-6"></a>
## [LiteLLM v1.91.0-rc.1 adds Docker image signing](https://github.com/BerriAI/litellm/releases/tag/v1.91.0-rc.1) ⭐️ 7.1/10

BerriAI released LiteLLM v1.91.0-rc.1, introducing cosign-based Docker image signature verification for enhanced supply chain security, along with multiple bug fixes and features such as MCP OAuth token foundation and improved Prometheus metrics. This release strengthens security for users deploying LiteLLM via Docker by allowing cryptographic verification of image authenticity, which is critical for preventing supply chain attacks. The additional monitoring and guardrail improvements also benefit reliability and observability in production AI gateways. The recommended verification method uses a pinned commit hash (0112e53) to ensure immutable key binding, while a tag-based option is also available for convenience. The release includes over 15 changes covering guardrails, MCP, web search, cost tracking, and proxy performance.

github · github-actions[bot] · Jun 28, 03:46

**Background**: LiteLLM is an open-source AI Gateway that provides a unified API interface to over 100 large language models, simplifying model access, cost tracking, and fallback management. Cosign, part of the Sigstore project, is a tool for signing and verifying container images and binaries, helping to ensure software supply chain integrity.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://docs.docker.com/dhi/core-concepts/signatures/">Code signing | Docker Docs</a></li>
<li><a href="https://www.litellm.ai/">LiteLLM</a></li>

</ul>
</details>

**Tags**: `#LiteLLM`, `#Docker`, `#cosign`, `#security`, `#release-notes`

---

<a id="item-7"></a>
## [Why Polish Diacritics Vanish in Software](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/) ⭐️ 7.0/10

This article explores the historical and technical reasons why Polish diacritic letters (like ś, ć, ń) are frequently lost or mangled in software, tracing the issue from 1960s ASCII limitations to modern browser keyboard shortcuts and Unicode normalization differences. This matters because millions of Polish speakers face daily input problems, and the issue exemplifies broader challenges in internationalization and input method compatibility that affect many languages with diacritics. Among Polish letters, 'ł' does not decompose under Unicode NFD normalization, while 8 others break into base letter plus combining mark. Browser shortcuts (e.g., Ctrl+Alt+S for 'ś') often intercept the intended AltGr combinations, and no simple browser API exists to detect such conflicts.

hackernews · colinprince · Jun 28, 12:44 · [Discussion](https://news.ycombinator.com/item?id=48706814)

**Background**: The Polish alphabet uses Latin script with additional diacritic letters (ą, ć, ę, ł, ń, ó, ś, ź, ż). Early computing systems often limited character sets to ASCII, which lacked these letters. Unicode introduced normalization forms (NFC, NFD) to handle equivalent sequences, but software handling varies. Modern browsers and applications sometimes steal keyboard combinations intended for inputting these diacritics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unicode_normalization">Unicode normalization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polish_alphabet">Polish alphabet - Wikipedia</a></li>
<li><a href="https://accentcodes.com/languages/polish-alt-codes.html">Polish ALT Codes — ą ć ę ł ń ś ź ż (Unicode Alt+X Method)</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted additional aspects: one noted that Polish's Latin script facilitated Western alignment; another pointed out that browsers lack a simple way to check key combinations, leading to developer workarounds. A user reported that Microsoft Copilot intercepts 'Ć' input on Windows, and another shared a fun fact that 'ł' remains intact during Unicode normalization, causing issues with SQLite's remove_diacritics tokenizer.

**Tags**: `#Polish diacritics`, `#Unicode`, `#software localization`, `#keyboard shortcuts`, `#historical computing`

---