---
layout: default
title: "Horizon Summary: 2026-09-19 (EN)"
date: 2026-09-19
lang: en
---

> From 92 items, 6 important content pieces were selected

---

1. [Terry Tao: Math Is More Than Proof, and AI Is Testing That](#item-1) ⭐️ 8.4/10
2. [Brood War Bench: A StarCraft Benchmark for Testing AI Agents](#item-2) ⭐️ 7.8/10
3. [Substack Essay Argues Against AI Writing for Others](#item-3) ⭐️ 7.7/10
4. [Ruan Yifeng Weekly Issue 413: Goodbye, React Native](#item-4) ⭐️ 7.2/10
5. [Blog Shows How to Make AI-Generated Event Posters Look Decent](#item-5) ⭐️ 7.0/10
6. [PlanetScale launches Tin, a cloud-only full-text search engine for Postgres](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Terry Tao: Math Is More Than Proof, and AI Is Testing That](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/) ⭐️ 8.4/10

Terry Tao published a blog essay arguing that mathematics is far more than the production of proofs, and that its intuitive, collaborative, and conceptual dimensions deserve far wider recognition than they currently receive. The post triggered a large Hacker News discussion (299 points, 231 comments) that quickly shifted toward how AI is destabilizing the professional role of mathematicians. The piece matters because it reframes a cultural question — what mathematicians should be celebrated for — at exactly the moment AI tools are automating the task-based part of mathematical work that careers, tenure, and prestige were built on. If proof-writing is no longer the scarce human contribution, then the discipline's reward structures, training, and self-image all need to change, and that affects everyone whose knowledge work is being similarly unbundled. The essay is reflective rather than technical — it offers a framing rather than concrete proposals for reform, and it does not present new mathematical results. The discussion surrounding it adds substance: one commenter who identifies as a professional mathematician says weeks of serious AI use helped produce a proof they had been thinking about for years and are now writing up, while others argue the advantage held by elite, Fields Medal-caliber mathematicians has narrowed considerably.

hackernews · num42 · Sep 19, 06:28 · [Discussion](https://news.ycombinator.com/item?id=49763928)

**Background**: Terry Tao is a Fields Medal-winning mathematician at UCLA and one of the most widely read academic bloggers in the field, so his essays carry unusual weight in framing debates about the discipline. The comment thread reaches back to the 1900 International Congress of Mathematicians in Paris, where the Poincaré–Hilbert debate helped establish proof, rather than intuition, as the field's dominant standard. Commenters also note that the Fields Medal has an age limit (awarded up to age 40), which they say structurally rewards raw brainpower over accumulated understanding — making AI's arrival feel like a direct challenge to the community's guiding award. This discussion unfolds against rapid progress in AI systems that can now carry out substantial parts of mathematical research work.

**Discussion**: Sentiment is divided but broadly resigned to disruption: several commenters draw an explicit analogy to software engineering, arguing that AI can already automate mathematical tasks even if it cannot yet do a whole job — and that for many mathematicians those tasks were the job, so tenure and career models are failing. A professional mathematician counters with an optimistic firsthand account of AI-accelerated proof discovery, and another argues the real crisis is narrower than it looks: it is the shrinking edge of elite prize-winners, which means there has never been a better time to be a mathematician. Others lament that the intuitive, communicative side of mathematics that Tao defends has long been squeezed out of school and university teaching.

**Tags**: `#mathematics`, `#AI`, `#philosophy-of-math`, `#academic-research`, `#Terry-Tao`

---

<a id="item-2"></a>
## [Brood War Bench: A StarCraft Benchmark for Testing AI Agents](https://bw.swerdlow.dev/report) ⭐️ 7.8/10

A new report site, Brood War Bench (bw.swerdlow.dev/report), presents a benchmark that evaluates AI systems on StarCraft: Brood War, and it was surfaced and heavily discussed on Hacker News. The project joins a small but growing family of game-based evaluations that put LLM-driven or scripted agents into a full real-time strategy environment rather than a static question-answering task. Real-time strategy games stress exactly the capabilities that current LLM benchmarks struggle to measure: long-horizon planning, partial observability, resource management, and acting under time pressure, so a Brood War benchmark could reveal agent weaknesses that coding or reasoning leaderboards miss. It also reflects a broader industry shift toward evaluating agents by what they can accomplish in a live environment rather than by single-turn answers. Brood War is an unusually demanding test bed because matches run for thousands of game ticks with fog of war, and agent performance depends heavily on interface and action-rate (APM) affordances rather than raw model quality alone. Note that the report page itself was not included in the excerpt, so the benchmark's exact task design, model lineup, and scoring methodology could not be independently verified here.

hackernews · benswerd · Sep 19, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49766966)

**Background**: StarCraft: Brood War is a 1998 real-time strategy game by Blizzard in which players build bases, manage resources, and command armies under fog of war. Its open BWAPI interface made it a popular platform for programmatic bots, including a 2010 Brood War AI tournament run by the Expressive Intelligence Studio at UC Santa Cruz. DeepMind later trained AlphaStar on StarCraft II, a milestone that established RTS games as a hard test of AI planning. Benchmarks such as LiveBench serve a similar purpose for language models by providing contamination-resistant, regularly refreshed tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/SKTBrain/awesome-starcraftAI">Awesome StarCraft AI</a></li>
<li><a href="https://starcraft.ai/">StarCraft.AI</a></li>
<li><a href="https://livebench.ai/">LiveBench</a></li>

</ul>
</details>

**Discussion**: Commenters were largely enthusiastic: one reader nostalgically recalled the LAN-café era of Brood War and the friendships it produced, while another offered a widely appreciated analogy mapping agent architectures onto the three factions — Protoss as expensive frontier coding agents you micromanage, Terran as versatile teams of specialized agents you delegate to, and Zerg as swarms of cheap custom agents optimized for speed and cost. Others added historical and technical context, noting the 2010 BWAPI tournament at UC Santa Cruz, pointing out that a bot is currently dominating the ladder, and citing GoBench, which evaluates LLMs on 9x9 Go using KataGo as Elo anchors.

**Tags**: `#AI benchmark`, `#StarCraft`, `#LLM evaluation`, `#agentic AI`, `#game AI`

---

<a id="item-3"></a>
## [Substack Essay Argues Against AI Writing for Others](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai) ⭐️ 7.7/10

Erich Grunewald published a Substack essay arguing that people should almost never use AI to write text for others, citing cognitive-science reasoning such as Eric Schwitzgebel's claim that reading a generated text is cognitively different from actively producing prose. The piece sparked a Hacker News discussion with 111 comments debating when LLM-assisted writing genuinely helps. As LLMs become embedded in everyday writing workflows, the essay pushes back on the assumption that faster text generation is always better, warning that it can weaken writers' engagement with word choice and meaning. The debate matters to writers, students, professionals, and tool builders trying to define healthy human-AI collaboration. The essay's core heuristic, echoed in the HN thread, is to use AI for texts you want for yourself—summaries, reports, meeting-to-email drafts—rather than texts you produce for others to consume. Commenters also suggest lighter uses: asking for multiple phrasings to clarify your own intent or requesting critique instead of a full rewrite, though these remain opinion-based practices rather than controlled findings.

hackernews · erwald · Sep 19, 16:35 · [Discussion](https://news.ycombinator.com/item?id=49767937)

**Background**: Substack is a subscription-based publishing platform launched in 2017 that lets writers send newsletters, podcasts, and video directly to subscribers. The essay's argument draws on cognitive science: cognitive offloading describes delegating mental tasks to external tools, and recent research such as MIT Media Lab's 'Your Brain on ChatGPT' has examined whether LLM-assisted essay writing can create 'cognitive debt' by reducing active engagement. Eric Schwitzgebel's point is that passively reading a finished text does not exercise the same productive effort as composing prose word by word.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Substack">Substack - Wikipedia</a></li>
<li><a href="https://www.media.mit.edu/publications/your-brain-on-chatgpt/">Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task — MIT Media Lab</a></li>
<li><a href="https://arxiv.org/abs/2506.08872">[2506.08872] Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task</a></li>

</ul>
</details>

**Discussion**: HN commenters largely agreed that AI is more defensible for private sensemaking than for writing on someone else's behalf: jameshart framed it as using AI to write what you wish someone else had written for you, while foobarbecue argued LLM prose buries the author's meaning and is mainly useful for filling space. Others offered practical middle grounds, such as wdutch asking for multiple versions to clarify one's own preference and rectang recommending AI critique rather than full rewrites, reflecting a nuanced rather than blanket rejection. patrickmay also quoted the essay's Schwitzgebel passage about the gap between nodding along while reading and productively generating text.

**Tags**: `#AI writing`, `#LLM`, `#human-AI collaboration`, `#cognition`, `#writing craft`

---

<a id="item-4"></a>
## [Ruan Yifeng Weekly Issue 413: Goodbye, React Native](http://www.ruanyifeng.com/blog/2026/09/weekly-issue-413.html) ⭐️ 7.2/10

Ruan Yifeng published issue 413 of his tech weekly on his blog, this time themed "Goodbye, React Native," rounding up noteworthy technology and programming items from the week. The same post also carries a notice that the newsletter will take a break during the upcoming Mid-Autumn Festival and National Day holidays starting next Friday. Ruan Yifeng's weekly is one of the longest-running, highest-signal curation sources in the Chinese developer community, so the framing of a React Native "farewell" spotlights an ongoing debate among front-end and mobile engineers about whether the framework still deserves a place in new projects. For teams currently weighing React Native against Flutter or fully native development, the issue's angle is a useful signal of where community sentiment is heading. The available excerpt is thin — it contains only the standard introductory sentence and the holiday notice, so the specific arguments behind the React Native theme cannot be verified from the text provided. The newsletter is published on Fridays and is a curated link roundup rather than original technical analysis.

rss · 阮一峰周刊 · Sep 18, 00:03

**Background**: Ruan Yifeng is a well-known Chinese technology blogger, widely recognized as the author of the book introducing the ES6 JavaScript standard. His 科技爱好者周刊 (Technology Enthusiast Weekly) has run for hundreds of issues, collecting tools, articles, and open-source projects of interest to programmers. React Native is Meta's open-source framework, released in 2015, that lets developers build iOS and Android apps using JavaScript and React; in recent years its adoption has been debated amid competition from Flutter, native development, and newer cross-platform approaches.

**Tags**: `#科技周刊`, `#React Native`, `#前端开发`, `#移动开发`, `#编程`

---

<a id="item-5"></a>
## [Blog Shows How to Make AI-Generated Event Posters Look Decent](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) ⭐️ 7.0/10

A blog post published on john.hartnup.uk (dated 2026-06-07) walks through practical techniques for producing AI-generated event posters that don't look obviously machine-made, and it triggered a large Hacker News discussion with roughly 729 comments. The post compares weaker default outputs with better-directed examples, including a prompt asking for a poster "in the style of a 90s drum n bass gig flyer, with early 3D/fractal computer imagery." As AI image generators become standard tools for small events, clubs, and community organizers, the question of whether their default aesthetic is acceptable output or a visible mark of low effort directly affects designers, clients, and the perceived value of creative work. The discussion matters because it frames AI not just as a replacement for top-tier artists but as a competitor to cheap freelance designers, reshaping the bottom end of the design market. Commenters note that even the improved examples still show tell-tale rendering errors — for instance, a wireframe sphere that is stylistically appropriate for early CGI aesthetics but is geometrically incorrect, which breaks the illusion the style depends on. Another recurring point is that models converge on top-of-mind clichés, so a "Japanese minimal poster" prompt defaults to sakura blossoms and a stylized Japanese flag rather than a less obvious concept.

hackernews · ereiamjh · Sep 19, 09:20 · [Discussion](https://news.ycombinator.com/item?id=49764791)

**Background**: AI image generation tools such as diffusion-based models (Midjourney, DALL·E, Stable Diffusion and their successors) turn a text prompt into an image, and their outputs are strongly shaped by the prompt and by any style reference given. Because these models are trained on large scraped datasets, their "default" look tends to reflect the most common associations in that data, which is why unguided prompts often produce generic or stereotyped imagery. The blog post is essentially a craft guide to steering those models away from that default toward a specific visual intent.

**Discussion**: Sentiment is split: one commenter (ajjenkins) argues from experience that the average budget Fiverr designer is significantly worse than AI, so the bar being compared against is unrealistic. Others (vova_hn2, JSR_FDED) counter that the failure is conceptual and social — models fall back on banal associations like sakura for "Japan," and the recognizably default style signals low effort that pretends to be high effort. mrob adds a technical critique that detail-heavy examples fail on incorrect rendering, and jstummbillig half-defends AI by noting that average human design taste is itself poor.

**Tags**: `#AI image generation`, `#creative AI`, `#design`, `#applied AI`, `#Hacker News`

---

<a id="item-6"></a>
## [PlanetScale launches Tin, a cloud-only full-text search engine for Postgres](https://planetscale.com/blog/introducing-tin) ⭐️ 7.0/10

PlanetScale introduced Tin (short for "Text INdex"), a new full-text search capability for its hosted Postgres offering. Enabling the tin extension adds a search-optimized inverted index type, BM25 relevance ranking, and a dedicated query language called TINQL. It lands in the middle of a wave of managed database vendors racing to bolt first-class search onto Postgres, following ParadeDB's pg_search, Timescale's pg_textsearch, and Databricks/Neon's Lakebase Search. For teams already on PlanetScale it could remove the need to run a separate Elasticsearch-style service, but it also deepens platform lock-in and raises questions about whether comparable performance will ever be available in self-hosted Postgres. The most-discussed caveat is that Tin is not shipped as a general-purpose extension: it runs only on PlanetScale's cloud service, and the open-source local counterpart, `lead`, is mainly intended for testing query syntax and does not share the same performance characteristics. Tin uses BM25 ranking, the same scoring model popularized by Lucene and Elasticsearch, rather than Postgres' built-in ts_rank.

hackernews · ksec · Sep 19, 13:52 · [Discussion](https://news.ycombinator.com/item?id=49766611)

**Background**: PostgreSQL has shipped built-in full-text search for years through the tsvector and tsquery types, the ts_rank ranking functions, and GIN/GiST indexes, but its relevance scoring is generally considered weaker than the BM25-based systems used by dedicated search engines. BM25 is a probabilistic ranking function that weighs term frequency, document length, and how rare a term is across the corpus. PlanetScale is a managed relational database platform best known for Vitess/MySQL at scale, and it now also hosts Postgres. Vendors like ParadeDB and Timescale have been building Postgres extensions that bring inverted indexes and BM25 ranking into the database itself.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/docs/postgres/search">TIN : PlanetScale Postgres Search - PlanetScale</a></li>
<li><a href="https://news.ycombinator.com/item?id=49766611">Tin : full - text search for Postgres | Hacker News</a></li>
<li><a href="https://www.postgresql.org/docs/current/textsearch.html">PostgreSQL: Documentation: 18: Chapter 12. Full Text Search</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were broadly skeptical, with several asking why they would adopt a third-party, cloud-only, somewhat "vibecoded" solution when core Postgres already offers a sophisticated built-in FTS stack with tsvector/tsquery. Others framed the announcement as part of an industry trend driven by AI-assisted coding productivity, citing ParadeDB, Timescale, and Databricks, while noting that a local `lead` build exists but lacks the same performance. There was also interest in SQLite's FTS and Lucene-style query support, and in whether Tin might one day be open-sourced so performance could be tested independently.

**Tags**: `#Postgres`, `#Full-Text Search`, `#Databases`, `#Dev Tools`, `#PlanetScale`

---