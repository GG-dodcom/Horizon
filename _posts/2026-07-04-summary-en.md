---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 79 items, 14 important content pieces were selected

---

1. [Researcher reveals YouTube private video leak vulnerability](#item-1) ⭐️ 9.2/10
2. [Comprehensive guide to htop/top fields on Linux](#item-2) ⭐️ 9.1/10
3. [Vercel's Andrew Qu on agents as a new software paradigm](#item-3) ⭐️ 8.7/10
4. [LiteLLM v1.90.1 Adds Docker Image Signature Verification](#item-4) ⭐️ 8.4/10
5. [Indoor CO2 Levels May Impair Cognitive Function](#item-5) ⭐️ 8.2/10
6. [Claude Code v2.1.199 fixes SSL errors, streaming, and daemon crashes](#item-6) ⭐️ 8.0/10
7. [Course Sales Plunge 50%+ Attributed to AI](#item-7) ⭐️ 8.0/10
8. [LiteLLM v1.92.0 Adds Cosign Docker Image Verification](#item-8) ⭐️ 7.9/10
9. [Open Source AI Gap Map Released](#item-9) ⭐️ 7.7/10
10. [Potential session/cache leakage bug in Claude Code sparks debate](#item-10) ⭐️ 7.6/10
11. [LiteLLM v1.90.3 adds cosign Docker image verification](#item-11) ⭐️ 7.4/10
12. [Let AI Models Use Their Own Judgement](#item-12) ⭐️ 7.2/10
13. [AI Engineer World's Fair: Loops Debate and State of AI](#item-13) ⭐️ 7.2/10
14. [Simon Willison's June 2026 Newsletter Covers AI, Tokenmaxxing, Datasette](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Researcher reveals YouTube private video leak vulnerability](https://javoriuski.com/post/youtube) ⭐️ 9.2/10

A security researcher discovered a vulnerability that allows attackers to leak YouTube creators' private videos by crafting a malicious link. The researcher reported the issue to Google, which has since fixed it. This vulnerability undermines the privacy guarantees of YouTube's 'private' video setting, potentially exposing sensitive content. It also raises concerns about YouTube's handling of bug reports and the prevalence of prompt injection issues. The attack works by replacing a video ID parameter with a video title, which then appears in a server request visible to the attacker. Additionally, the researcher showed a prompt injection attack via YouTube Studio's AI comment suggestions.

hackernews · javxfps · Jul 4, 16:45 · [Discussion](https://news.ycombinator.com/item?id=48786781)

**Background**: YouTube offers three privacy settings for videos: public, unlisted (accessible by anyone with the link), and private (only visible to the creator and selected users). The vulnerability discovered exploits how YouTube's systems handle video titles when constructing URLs, allowing an attacker to trick a creator into revealing the title of a private video. Additionally, prompt injection refers to manipulating AI-generated suggestions to produce unintended behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.threatshub.org/blog/how-i-found-a-bug-in-youtube-that-let-me-watch-private-videos-i-wasnt-allowed-to-says-compsci-student/">How I found a bug in YouTube that let me watch private videos I wasn't ...</a></li>
<li><a href="https://grokipedia.com/page/YouTube_video_ID">YouTube video ID — Grokipedia</a></li>

</ul>
</details>

**Discussion**: Comments include a former Google employee explaining the internal handling of such bugs, praise for the article's clarity and lack of sensationalism, criticism of YouTube for not treating prompt injection as a bug, and a user reporting that the attack did not work in their test.

**Tags**: `#security`, `#vulnerability`, `#YouTube`, `#privacy`, `#bug bounty`

---

<a id="item-2"></a>
## [Comprehensive guide to htop/top fields on Linux](https://peteris.rocks/blog/htop/) ⭐️ 9.1/10

This article provides an exhaustive explanation of every field and feature visible in the htop and top process monitoring tools on Linux, including CPU, memory, and process states. For Linux system administrators and developers, understanding htop/top output is essential for diagnosing performance issues, memory leaks, and CPU bottlenecks. This guide fills a gap by explaining even obscure fields like VIRT, RES, SHR, and process states, making system monitoring more accessible. The article covers over 30 fields including process state letters (R, S, D, Z, T), memory columns (VIRT, RES, SHR, %MEM), CPU metrics, and the 'nice' value. It also includes practical tips such as disabling user threads and enabling tree view to reduce clutter.

hackernews · theanonymousone · Jul 4, 12:00 · [Discussion](https://news.ycombinator.com/item?id=48784777)

**Background**: htop and top are command-line process monitoring tools in Linux that display real-time information about system processes, including CPU usage, memory consumption, and process states. They are essential for troubleshooting performance issues. The process state 'R' means running or runnable, 'S' means interruptible sleep, 'D' means uninterruptible sleep (disk I/O), 'Z' means zombie, and 'T' means stopped. Memory columns like VIRT represent total virtual memory allocated, RES is actual physical memory used, and SHR is shared memory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/process-states">Linux Process States | Baeldung on Linux</a></li>
<li><a href="https://serverfault.com/questions/138427/what-does-virtual-memory-size-in-top-mean">linux - What does Virtual memory size in top mean? - Server Fault</a></li>
<li><a href="https://www.geeksforgeeks.org/linux-unix/priority-of-process-in-linux-nice-value/">Priority of process in Linux | nice value - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Comments recommend alternatives like btop for a modern interface and suggest practical htop settings: disabling user threads and enabling tree view. Another user cautions that virtual memory (VIRT) is unreliable and recommends using resident size (RES) as a more accurate memory metric.

**Tags**: `#Linux`, `#htop`, `#top`, `#process monitoring`, `#system administration`

---

<a id="item-3"></a>
## [Vercel's Andrew Qu on agents as a new software paradigm](https://www.latent.space/p/vercel-agents-new-software) ⭐️ 8.7/10

Andrew Qu, Vercel's Chief of Software, explains how the company's open-source agent framework 'eve' was built, introducing concepts like skills, sandboxes, and agent-readable websites that redefine software development for AI agents. This matters because it signals a shift from traditional human-oriented software to agent-native systems, where agents are first-class citizens with their own tools and environments, potentially accelerating the adoption of autonomous AI agents in production. In eve, each agent is represented as a folder containing files, with tools as files, and skills as Markdown documents. Sandboxes provide secure, isolated execution environments for agent tasks, while agent-readable websites follow specifications like llms.txt to make content machine-accessible.

rss · Latent Space · Jul 3, 00:08

**Background**: Traditional AI agents often lack standardization and secure execution. Vercel's eve framework aims to provide a reliable, scalable platform similar to Next.js for frontend development. Skills allow agents to discover reusable contexts, sandboxes ensure safety, and agent-readable websites optimize content for LLMs, representing a new paradigm where software is designed for both humans and agents.

<details><summary>References</summary>
<ul>
<li><a href="https://otf-kit.dev/blog/eve-framework">Vercel launches eve , an open-source framework simplifying AI agent ...</a></li>
<li><a href="https://vercel.com/kb/guide/agent-readability-spec">Agent Readability: A Specification for AI-Optimized Websites | Vercel Knowledge Base</a></li>
<li><a href="https://www.firecrawl.dev/blog/ai-agent-sandbox">AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Agents`, `#Vercel`, `#Software Development`

---

<a id="item-4"></a>
## [LiteLLM v1.90.1 Adds Docker Image Signature Verification](https://github.com/BerriAI/litellm/releases/tag/v1.90.1) ⭐️ 8.4/10

LiteLLM released version 1.90.1, which includes detailed instructions for verifying Docker image signatures using cosign with either a pinned commit hash or a release tag. This release strengthens supply chain security for AI/LLM tooling by enabling users to cryptographically verify the authenticity and integrity of LiteLLM Docker images, reducing the risk of using tampered or malicious images. The verification command uses cosign with a public key stored on GitHub; the pinned commit hash method is recommended because it is cryptographically immutable, while the release tag method is more convenient but relies on repository tag protection.

github · yuneng-berri · Jul 3, 04:47

**Background**: Cosign is a tool for signing and verifying container images as part of the Sigstore project, which aims to improve software supply chain security. Signing Docker images allows users to confirm the image was produced by the claimed publisher and has not been altered. LiteLLM is an open-source library that provides a unified interface for calling various large language model APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/">How to Sign a Container with Cosign — Chainguard Academy</a></li>
<li><a href="https://www.docker.com/blog/software-supply-chain-security-best-practices/">5 Software Supply Chain Security Best Practices | Docker</a></li>

</ul>
</details>

**Tags**: `#litellm`, `#docker`, `#cosign`, `#supply chain security`, `#AI tooling`

---

<a id="item-5"></a>
## [Indoor CO2 Levels May Impair Cognitive Function](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/) ⭐️ 8.2/10

Mike Bowler's blog post highlights how elevated indoor CO2 levels can impair decision-making, sparking a discussion that includes real-world evidence from a teacher and scientific skepticism about replication issues. This matters because millions of people work and learn in poorly ventilated spaces, and simply raising awareness via CO2 monitors could improve cognitive performance and health, especially in schools and offices. A high school teacher reported CO2 levels reaching 2000 ppm in classrooms within minutes, while some commenters noted that cognitive impact studies have replication issues and that submarines operate at high ppm without recorded effects.

hackernews · gslin · Jul 4, 06:32 · [Discussion](https://news.ycombinator.com/item?id=48783117)

**Background**: Humans exhale carbon dioxide, which can accumulate indoors without adequate ventilation. While early studies like the 2012 Satish study suggested cognitive decline at levels as low as 1000 ppm, the findings have been debated due to replication failures and methodological concerns.

**Discussion**: Community sentiment is mixed: some advocate for OEMs to integrate CO2 sensors into devices to raise awareness, while others question the scientific basis, citing replication issues and pointing to submarine environments where high CO2 is tolerated without cognitive impact.

**Tags**: `#CO2 monitoring`, `#cognitive science`, `#ventilation`, `#health hazards`, `#indoor air quality`

---

<a id="item-6"></a>
## [Claude Code v2.1.199 fixes SSL errors, streaming, and daemon crashes](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) ⭐️ 8.0/10

Anthropic released Claude Code v2.1.199, a bug fix update that addresses over 20 issues including SSL certificate errors, mid-stream API failures, subagent reliability, and a Linux daemon crash that killed agents every 50 seconds. This release significantly improves the reliability of Claude Code for developers, especially in enterprise environments with TLS-inspecting proxies and memory-constrained machines, and fixes critical issues that could cause silent data loss or daemon instability. Notable fixes include immediate failure with guidance for SSL errors instead of burning retries, preserving partial streaming output on server errors, and preventing background daemon from self-destructing after unclean shutdown. The update also raises the default retry count for transient rate-limit errors via the CLAUDE_CODE_RETRY_WATCHDOG environment variable.

github · ashwin-ant · Jul 2, 23:35

**Background**: Claude Code is Anthropic's AI-powered coding assistant that runs in the terminal and leverages large language models to help developers write, debug, and refactor code. TLS-inspecting proxies are corporate network tools that intercept encrypted HTTPS traffic for security monitoring, which can interfere with Node.js applications that require valid SSL certificates. The NODE_EXTRA_CA_CERTS environment variable is a Node.js mechanism to specify additional Certificate Authority certificates when behind such proxies or using self-signed certs.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview">TLS inspection overview | Secure Web Proxy - Google Cloud</a></li>
<li><a href="https://stackoverflow.com/questions/44459971/nodejs-environment-variable-node-extra-ca-certs">node.js - nodejs environment variable " NODE _ EXTRA _ CA _ CERTS "</a></li>
<li><a href="https://michaeldishmon-com.vercel.app/writing/background-agents-run-in-background">Background agents with run_in_ background : when it pays off</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#Anthropic`, `#bug fix`, `#developer tools`, `#AI tooling`

---

<a id="item-7"></a>
## [Course Sales Plunge 50%+ Attributed to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau reports that his course sales have dropped by over 50%, with his latest launch on track to sell only a third of previous launches. He attributes the decline to AI's dual impact: reducing developer job security and replacing paid courses with LLM-based personalized tutoring. This signals a significant shift in developer education, as AI tools like LLMs are disrupting traditional course markets and influencing career investment decisions. It highlights broader economic anxiety among developers and the need for course creators to adapt to AI-driven changes. Comeau's latest course 'Whimsical Animations' is on track for a third of typical sales, and his two existing courses also show significant year-over-year declines. He notes that other course creators are seeing similar trends, with revenue down 50%+ and reduced engagement.

rss · Simon Willison · Jul 3, 21:25

**Background**: Josh W. Comeau is a well-known front-end developer educator, popular for his interactive courses on React and CSS. The rise of large language models (LLMs) like GPT-4 has enabled personalized tutoring, potentially reducing demand for structured paid courses. Additionally, AI-driven uncertainty about future developer job prospects makes people hesitant to invest time and money in learning new skills.

**Tags**: `#AI impact`, `#developer education`, `#course sales decline`, `#LLM tutoring`, `#job market uncertainty`

---

<a id="item-8"></a>
## [LiteLLM v1.92.0 Adds Cosign Docker Image Verification](https://github.com/BerriAI/litellm/releases/tag/v1.92.0-dev.2) ⭐️ 7.9/10

LiteLLM v1.92.0-dev.2 provides instructions for verifying Docker image signatures using cosign, with both pinned commit hash and release tag methods. This enhances supply chain security for LiteLLM users, allowing them to ensure the integrity and authenticity of Docker images before deployment. The signing key is introduced in commit 0112e53, and the recommended method uses the pinned commit hash for immutability. The release tag method relies on tag protection rules.

github · github-actions[bot] · Jul 3, 20:08

**Background**: Cosign is a tool for signing and verifying container images as part of the Sigstore project. By signing Docker images, developers can cryptographically guarantee that the image has not been tampered with since it was built. This is crucial for production deployments to prevent supply chain attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/">How to Sign a Container with Cosign — Chainguard Academy</a></li>

</ul>
</details>

**Tags**: `#LiteLLM`, `#Docker`, `#cosign`, `#security`, `#dev tools`

---

<a id="item-9"></a>
## [Open Source AI Gap Map Released](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 7.7/10

Current AI launched version 0.1 of the Open Source AI Gap Map, an index of 421 open source AI products including software tools, models, datasets, and hardware projects. The underlying data is released under an MIT license on GitHub. This map provides a comprehensive overview of the open source AI ecosystem, helping identify gaps and areas for investment. It serves as a valuable resource for developers, researchers, and organizations to understand and contribute to open source AI. The map details 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three layers. The data includes 1,184 YAML files and a CSV of 16,185 tracked GitHub repositories.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a non-profit global partnership founded at the AI Action Summit in Paris in February 2025, with $400 million committed. The Gap Map aims to systematically map the open source AI stack to identify high-leverage points for building new capabilities and tools.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#LLM`, `#Resource`, `#Ecosystem`

---

<a id="item-10"></a>
## [Potential session/cache leakage bug in Claude Code sparks debate](https://github.com/anthropics/claude-code/issues/74066) ⭐️ 7.6/10

A detailed bug report on GitHub claims that Claude Code may leak session or cache data between different workspace instances or consumer accounts, causing the AI to reference unrelated user contexts. If confirmed, this would be a significant security and privacy issue for users of Claude Code, potentially exposing sensitive data across accounts. The discussion highlights the challenges of debugging AI behavior, where hallucinations can mimic genuine leaks. The bug reporter observed the AI asking about building a Minecraft temple when the user was working in an enterprise workspace, suggesting cross-session leakage. However, the Claude Code team responded on Hacker News stating they are confident it is a hallucination but are investigating anyway.

hackernews · chatmasta · Jul 4, 14:03 · [Discussion](https://news.ycombinator.com/item?id=48785485)

**Background**: Claude Code is an AI-powered coding assistant developed by Anthropic, integrated into the Claude model family. Session/cache leakage refers to a scenario where the AI inadvertently accesses data from another user's session, potentially due to misconfiguration in the infrastructure. Such bugs are notoriously difficult to distinguish from LLM hallucination, where the model generates plausible but false information.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/74066">[Bug] Potential session / cache leakage between workspace instances...</a></li>

</ul>
</details>

**Discussion**: The Hacker News commenters are largely skeptical, with many noting similar experiences that turned out to be hallucinations. A commenter from the Claude Code team acknowledged the report and said they are looking into it, while others suggested large context windows might make hallucinations more likely.

**Tags**: `#Claude Code`, `#LLM hallucination`, `#session leakage`, `#AI infrastructure`

---

<a id="item-11"></a>
## [LiteLLM v1.90.3 adds cosign Docker image verification](https://github.com/BerriAI/litellm/releases/tag/v1.90.3) ⭐️ 7.4/10

BerriAI/litellm released v1.90.3 with detailed instructions to verify Docker image signatures using cosign. The release also includes a backport of several fixes. This enhances supply chain security for LiteLLM users, helping prevent tampered images from being deployed. It sets a good security practice example for the LLM tool ecosystem. Users can verify the Docker image using either a pinned commit hash (recommended) or a release tag, both pointing to the same signing key. The cosign verification command is provided with expected output.

github · yuneng-berri · Jul 3, 21:06

**Background**: Cosign is a CNCF open-source tool from the Sigstore project for signing and verifying OCI container images. Supply chain security ensures that software artifacts have not been tampered with from build to deployment. LiteLLM is a popular proxy for managing multiple LLM providers.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sigstore.dev/quickstart/quickstart-cosign/">Sigstore Quickstart with Cosign - Sigstore</a></li>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/ cosign : Code signing and transparency for...</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-25-sigstore-supply-chain-security/view">How to Implement Supply Chain Security with Sigstore</a></li>

</ul>
</details>

**Tags**: `#litellm`, `#Docker`, `#cosign`, `#security`, `#supply-chain-security`

---

<a id="item-12"></a>
## [Let AI Models Use Their Own Judgement](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 7.2/10

A tip from the Claude Code team suggests letting AI models like Fable use their own judgement for tasks such as testing and model selection instead of hardcoding rules. The author also shared a practical prompt that delegates coding tasks to lower-power models to save on expensive Fable tokens. This approach improves efficiency and cost-effectiveness by leveraging the model's own reasoning to optimize task routing and resource usage. It is especially relevant for developers using expensive top-tier models like Fable, helping them balance performance with token budgets. The author used the prompt 'For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent' in Claude Code, which created a memory file to delegate coding tasks to Sonnet or Haiku while keeping judgment-heavy work on the main model. The technique reportedly reduced Fable token consumption significantly.

rss · Simon Willison · Jul 3, 18:51

**Background**: Claude Code is an AI coding agent by Anthropic that reads codebases, edits files, and runs commands in a terminal or IDE. Anthropic's Claude model family includes tiers like Haiku, Sonnet, Opus, and the more powerful Mythos-class Fable, which offers large context windows and advanced agentic capabilities but also higher cost. The tip reflects a growing trend in AI engineering to use models metacognitively—letting them decide how to allocate resources.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Claude Code`, `#Fable`, `#AI engineering`

---

<a id="item-13"></a>
## [AI Engineer World's Fair: Loops Debate and State of AI](https://www.latent.space/p/aiewf-daily-dispatch-locomotives) ⭐️ 7.2/10

The AI Engineer World's Fair ended with a debate on loops, a report on the state of AI engineering, and closing keynotes focused on what to build next. This dispatch captures key debates shaping AI engineering, particularly around multi-agent loops, and offers insights for practitioners on where to focus their efforts. The loops debate likely refers to multi-agent debate loop architectures where multiple AI agents deliberate iteratively to refine outputs, as seen in protocols like Muthu's "Basic Debate Loop". The state-of-AI engineering report and keynotes provide actionable guidance for builders.

rss · Latent Space · Jul 3, 05:11

**Background**: The "loops debate" in AI engineering centers on whether iterative multi-agent deliberation loops improve output quality over single-pass generation. Techniques like multi-agent debate (MAD) use multiple models debating in rounds to reach more nuanced answers, with each agent critiquing others' responses. This approach is increasingly explored in applied AI tooling workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://notes.muthu.co/2025/12/improving-decisions-through-multi-agent-debate-and-deliberation/">Improving Decisions Through Multi-Agent Debate and Deliberation</a></li>
<li><a href="https://polymind.cloud/blog/how-we-built-6-model-ai-debate-engine">How we built a 6-model AI debate engine | Polymind</a></li>

</ul>
</details>

**Tags**: `#AI engineering`, `#loops debate`, `#state of AI`, `#conference summary`, `#applied AI tooling`

---

<a id="item-14"></a>
## [Simon Willison's June 2026 Newsletter Covers AI, Tokenmaxxing, Datasette](https://simonwillison.net/2026/Jul/3/june-newsletter/#atom-everything) ⭐️ 7.0/10

Simon Willison published his June 2026 sponsors-only newsletter, covering topics like Claude Fable 5, GPT-5.6, US export restrictions, GLM-5.2 as the best open weights model, tokenmaxxing trends, and updates to Datasette Apps. This newsletter provides a curated update on cutting-edge AI developments and developer tools, highlighting significant shifts like the backlash against tokenmaxxing and the rise of open-weight models such as GLM-5.2. The newsletter is exclusively available to GitHub sponsors at $10 per month, with a preview of the previous month's edition linked. Topics also include US export restrictions on AI models and miscellaneous WASM projects.

rss · Simon Willison · Jul 3, 14:50

**Background**: Tokenmaxxing refers to the practice of maximizing AI token usage to an extreme, often driving up enterprise costs. GLM-5.2 is an open-source flagship model with 1M-token context and effort level control, positioned between Claude Opus 4.7 and 4.8. Datasette Apps is a new feature that allows hosting custom HTML+JavaScript apps in a sandboxed environment within Datasette, enabling rapid prototyping of persistent applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.2 - openlm.ai</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette ... - Datasette Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLMs`, `#newsletter`, `#dev tools`, `#Simon Willison`

---