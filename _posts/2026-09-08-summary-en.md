---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 109 items, 11 important content pieces were selected

---

1. [Interactive LLM Attention Visualization Tool Makes Mechanisms Intuitive](#item-1) ⭐️ 8.5/10
2. [Qwen3.8 27B Quantization Benchmark: 4-Bit Holds Up, 1-Bit Collapses](#item-2) ⭐️ 8.2/10
3. [AlphaGenome Atlas Maps Molecular Effects of 9 Billion Human DNA Variants](#item-3) ⭐️ 8.2/10
4. [Frontier AEO Tracker Reveals Source Choices of AI Assistants](#item-4) ⭐️ 8.0/10
5. [Ben Thompson Argues Purpose and Action Must Precede Writing Things Down](#item-5) ⭐️ 7.9/10
6. [OpenAI Claims AI-Generated Solution to Navier–Stokes Millennium Problem](#item-6) ⭐️ 7.8/10
7. [Inception Launches Mercury 2.5 Diffusion LLM with 40% Intelligence Gain](#item-7) ⭐️ 7.8/10
8. [Safety Refusals Should Target Harmful Subsets, Not Whole Topics](#item-8) ⭐️ 7.5/10
9. [Mathematician Buckmaster Alleges OpenAI Pressure Over Navier-Stokes Result](#item-9) ⭐️ 7.4/10
10. [New Skill 'I-Have-ADHD' Fights Claude Code's Lede-Burying Verbosity](#item-10) ⭐️ 7.0/10
11. [OpenAI Introduces ChatGPT Images 2.5 with Sunburst and Flare API Models](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Interactive LLM Attention Visualization Tool Makes Mechanisms Intuitive](https://ishamf.dev/p/llm-attention-visualizer/) ⭐️ 8.5/10

An interactive web tool called "LLM Attention Visualizer" was published at ishamf.dev as a 'Show HN' post on Hacker News. The tool aims to make attention in large language models easier to grasp by showing how information is combined across different layers and phrases. Attention mechanisms are central to modern LLMs, but their internal weighting schemes are abstract and hard to teach intuitively. This visualization provides a practical teaching aid that could improve AI education and help practitioners reason about model behavior. The tool displays attention patterns across transformer layers and phrase pairings, making cross-phrase information mixing visible in an accessible format. As a commenter noted, a potential design caveat is that later-layer attention may appear diluted when summed with contributions from many earlier layers.

hackernews · ifz · Sep 8, 16:59 · [Discussion](https://news.ycombinator.com/item?id=49613068)

**Background**: The attention mechanism in large language models determines which parts of a prompt are most relevant when generating each token, rather than treating every word equally. Transformers, the architecture behind many LLMs, are composed of many layers in which each token is contextualized within others via self-attention. Visualizing this process helps demystify why models arrive at specific predictions and is especially useful for students and developers new to the field.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>
<li><a href="https://medium.com/@QuarkAndCode/attention-mechanism-in-llms-explained-in-simple-terms-f9cd7d5278c2">Attention Mechanism in LLMs Explained in Simple Terms | Medium</a></li>
<li><a href="https://www.youtube.com/watch?v=XN7sevVxyUM">Lecture 13: Introduction to the Attention Mechanism in Large ...</a></li>

</ul>
</details>

**Discussion**: Commenters were overwhelmingly positive: a teacher said it arrived just in time for a Friday class, and an experienced reader called it the clearest example of attention they had seen. A deeper technical question asked whether attention from later layers gets drowned out by many earlier-layer contributions in the sum, and others expressed brief enthusiasm. Overall, the discussion praised the tool's teaching value while raising a valid conceptual limitation.

**Tags**: `#LLM`, `#Attention Mechanism`, `#Visualization`, `#AI Education`, `#Developer Tools`

---

<a id="item-2"></a>
## [Qwen3.8 27B Quantization Benchmark: 4-Bit Holds Up, 1-Bit Collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 8.2/10

A benchmark of Qwen3.8 27B across different quantization levels reports that 4-bit quantization preserves quality well, while 1-bit quantization causes the model's performance to collapse. The results offer practical guidance for choosing quantization settings when deploying the model locally. Quantization is essential for running large language models on consumer hardware, where memory constraints force trade-offs among quality, context length, and speed. Showing that 4-bit remains solid while 1-bit fails helps developers choose practical deployment defaults and highlights the limits of extreme low-bit quantization. In the benchmark, quality differences remain small down to 4-bit, 2-bit scores somewhat lower, and 1-bit collapses dramatically. Because this is a model-specific result, users should verify the quality knee on their own workloads; commenters also noted that no Q3-level result was included, which matters for sub-16GB GPUs.

hackernews · stared · Sep 8, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49611128)

**Background**: Quantization compresses an LLM by converting its weights and activations from high-precision representations, such as 16-bit floats, into lower-precision values such as 4-bit or 1-bit integers, reducing memory usage and speeding up inference at the cost of some accuracy. Qwen is a family of open-weight large language models developed by Alibaba Cloud; a 27B model is large enough that quantization is often needed to fit it into local GPUs and keep inference practical.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/quantization-for-large-language-models">Quantization for Large Language Models (LLMs): Reduce... | DataCamp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**Discussion**: Commenters generally valued the benchmark, but spider-mario criticized the use of Wilson confidence intervals, noting they do not measure run-to-run variation. Sharmajai hypothesized that Qwen3.8 27B compensates for quantization noise by simply thinking longer, while others asked for KV-cache quantization benchmarks, pointed out the missing Q3 setting for sub-16GB GPUs, and asked how to evaluate AI-assisted articles.

**Tags**: `#LLM quantization`, `#benchmarking`, `#inference`, `#local LLM`, `#Qwen`

---

<a id="item-3"></a>
## [AlphaGenome Atlas Maps Molecular Effects of 9 Billion Human DNA Variants](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) ⭐️ 8.2/10

DeepMind has launched AlphaGenome Atlas, a predictive catalogue that maps the molecular effects and AVI scores of all 9 billion possible single-nucleotide variants in the human genome. It is built on AlphaGenome, a unified DNA sequence model described in Nature that processes 1 Mb of DNA sequence in a single input. This is an exhaustive genome-wide map of predicted variant effects, covering not only protein-coding regions but also the roughly 98% of the genome that is non-coding. It could accelerate interpretation of disease-associated variants, support clinical genomics and drug discovery, and set a new benchmark for AI-driven biological research. The catalogue assigns an AVI (AlphaGenome variant impact) score to every single-letter DNA change in the human genome. AlphaGenome is presented as a DNA sequence model that can score variant effects across multiple modalities at once, overcoming the previous trade-off between input sequence length and prediction resolution, and DeepMind provides tools for making genome tracks and variant effect predictions from sequence.

rss · DeepMind Blog · Sep 8, 14:00

**Background**: The human genome contains roughly 3 billion DNA base pairs, but only about 2% of them form protein-coding genes; the rest is non-coding and plays a major role in regulating gene activity. A single-nucleotide variant is a change of one DNA letter at a specific position, and variant effect predictors are computational tools that estimate how such changes affect molecular function or disease risk. Earlier approaches often specialized in coding or non-coding regions—for example, a protein language model was used to predict 450 million missense variants—whereas AlphaGenome scales this idea to regulatory and non-coding DNA across the entire genome.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-10014-0">Advancing regulatory variant effect prediction with AlphaGenome | Nature</a></li>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas: Molecular predictions for 9 Billion human DNA variants — Google DeepMind</a></li>
<li><a href="https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/">AlphaGenome: AI for better understanding the genome — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#DeepMind`, `#genomics`, `#AI for science`, `#variant effect prediction`, `#human genome`

---

<a id="item-4"></a>
## [Frontier AEO Tracker Reveals Source Choices of AI Assistants](https://www.latent.space/p/aeo) ⭐️ 8.0/10

Latent Space launched an answer-engine optimization (AEO) tracker, starting with a report on Project Astra, to monitor which sources frontier AI assistants like Astra choose. The project also offers actionable guidance for founders and developer experience leaders. As AI assistants increasingly replace traditional search, being cited by these engines is becoming critical for businesses and content creators. This tracker provides a data-driven view into AEO trends, helping teams adapt their content and developer experience strategies accordingly. The first report centers on Project Astra, Google DeepMind's research prototype for a universal AI assistant, which is currently available as Gemini Live on Android and iOS. The topic was selected because it is one of the most frequently asked questions from founders and DX leaders in the Latent Space community.

rss · Latent Space · Sep 7, 21:32

**Background**: Answer engine optimization (AEO) is the process of optimizing content and brands to appear in AI-generated answers from engines like ChatGPT, Gemini, and AI Overviews. Frontier AI models are the most advanced AI systems at any given time, pushing the limits of reasoning and task complexity. As more users turn to AI assistants for answers, the sources these models choose to cite can directly impact a company's visibility and web traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://www.seo.com/ai/answer-engine-optimization/">Answer Engine Optimization (AEO): What It Is & How to Start</a></li>
<li><a href="https://deepmind.google/models/project-astra/">Project Astra — Google DeepMind</a></li>
<li><a href="https://www.brinqa.com/glossary/frontier-ai-models">Frontier AI Models : Definition & Security Impact</a></li>

</ul>
</details>

**Tags**: `#Answer Engine Optimization`, `#AI assistants`, `#LLM applications`, `#Frontier models`, `#Developer experience`

---

<a id="item-5"></a>
## [Ben Thompson Argues Purpose and Action Must Precede Writing Things Down](https://stratechery.com/2026/write-things-down/) ⭐️ 7.9/10

Stratechery's Ben Thompson has published 'Write Things Down,' arguing that writing is powerful for both humans and AI. He stresses, however, that deciding what to write, understanding why, and actually doing the work must come before the act of writing. The argument is significant for knowledge workers who are increasingly feeding their notes and documents to AI assistants, since the value of that material depends on why and how it was created. It also pushes back against the popular idea that merely capturing more text automatically improves human memory or AI performance. The article does not introduce a new technical tool or dataset; it is a conceptual argument about process. Thompson places execution and intentionality ahead of documentation, implying that writing is a means rather than a self-justifying end.

rss · Stratechery · Sep 8, 10:00

**Background**: Writing serves as an external memory for humans and as retrievable context or source material for AI systems. However, the usefulness of written artifacts depends on whether the writer had a clear purpose and followed through with action. This premise underlies the article's emphasis on deciding what to write, why to write it, and doing the actual work first.

**Tags**: `#writing`, `#AI`, `#knowledge management`, `#productivity`

---

<a id="item-6"></a>
## [OpenAI Claims AI-Generated Solution to Navier–Stokes Millennium Problem](https://openai.com/index/navier-stokes-solution/) ⭐️ 7.8/10

In a blog post, OpenAI announced that an unreleased internal model produced a proof that solutions of the three-dimensional Navier–Stokes equations can develop a singularity in finite time. The company says the result, formalized in the Lean proof assistant, establishes statements C and D of Fefferman's official formulation of the Navier–Stokes existence and smoothness Millennium Prize Problem. A verified solution to the Navier–Stokes problem would be a landmark in mathematics, and an AI-produced proof would show that large language models can contribute to frontier mathematical research. However, the claim is unverified, has been accused of leaning on other researchers' unpublished work, and has triggered debate about hype and how AI-assisted discoveries should be credited. According to the blog post, the proof shows that a smooth, finite-energy three-dimensional incompressible flow subject to a smooth external force can develop a singularity in finite time, providing a counterexample to global smoothness. The announcement included a formalization in the Lean proof assistant and noted a priority dispute with two mathematicians, one affiliated with Anthropic, who had derived closely related results on the Euler equations; the proof had not been independently verified by the Clay Mathematics Institute when it was announced.

hackernews · OpenAI Blog · Sep 8, 17:13 · [Discussion](https://news.ycombinator.com/item?id=49613262)

**Background**: The Navier–Stokes equations describe the motion of viscous fluids, such as air and water, and are widely used in engineering and physics, but whether smooth three-dimensional solutions can persist forever or blow up in finite time remains unproven. This question is the Navier–Stokes existence and smoothness problem, one of the seven Millennium Prize Problems that the Clay Mathematics Institute selected in 2000, each carrying a $1 million prize for a correct solution. As of 2026, the Poincaré conjecture is the only Millennium problem to have been officially solved; OpenAI has said it would decline the prize if its current claim were verified.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters are largely wary: some argue the work may be based on another researcher's results and prompts, linking to a personal statement and a priority dispute, while others share Terence Tao's warning that AI-powered research can 'flatten' problems before human investigators finish their work, discouraging open sharing. A few note the capability claim is itself striking—one commenter points out OpenAI says a model trained for less than two weeks is more than twice as capable in mathematics as Astra, which had been made public only a week earlier—but many remain skeptical of the hype and of the surrounding research culture.

**Tags**: `#OpenAI`, `#Navier-Stokes`, `#mathematics`, `#AI research`, `#research ethics`

---

<a id="item-7"></a>
## [Inception Launches Mercury 2.5 Diffusion LLM with 40% Intelligence Gain](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) ⭐️ 7.8/10

Inception Labs has launched Mercury 2.5, a general-purpose diffusion LLM that runs at about 1,100 tokens per second and delivers a roughly 40% intelligence increase over Mercury 2. The model is available through Inception's API and on OpenRouter. This release signals that diffusion-based LLMs are maturing into fast, low-cost general-purpose models rather than niche speech-only systems. Developers of latency-sensitive agents, including multi-model pipelines that need a fast judge model, are likely beneficiaries. Inception says Mercury 2.5 is the most capable diffusion LLM on the market; one community commenter compared it to cost-optimized frontier models such as GPT-5.6 Luna (Low), Gemini 3.5 Flash-Lite, and Claude Haiku 4.5. The model is not open-weights, and API users can opt out of training on their submissions by turning off the 'Improve the model for everyone' setting.

hackernews · Topfi · Sep 8, 20:14 · [Discussion](https://news.ycombinator.com/item?id=49616354)

**Background**: Mercury 2.5 is built by Inception Labs, a Palo Alto company founded in 2024 by Stanford, UCLA, and Cornell researchers behind the first diffusion LLM; its team also draws from Google DeepMind, Meta AI, Microsoft AI, and OpenAI. Unlike conventional autoregressive LLMs that predict tokens one by one, diffusion LLMs generate text through iterative denoising, allowing much faster parallel decoding. Inception is already deploying these models at Fortune 500 companies. OpenRouter, where Mercury 2.5 is listed, is a unified API gateway that routes requests across hundreds of models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inceptionlabs.ai/blog/introducing-mercury-2-5">Introducing Mercury 2.5 – Inception</a></li>
<li><a href="https://www.businesswire.com/news/home/20260908593295/en/Inception-Launches-Mercury-2.5-the-Next-Tier-of-Intelligence-for-Diffusion-LLMs">Inception Launches Mercury 2.5, the Next Tier of Intelligence ...</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Discussion**: Overall sentiment on Hacker News is positive but measured: commenters call Inception one of the most interesting neolabs and say Mercury 2.5 Preview is usable as a general-purpose chatbot, though not frontier-level. The main disappointment is that the model is not open-weights. Some developers see the 1,100 tokens per second speed as a major benefit for reducing judge latency in multi-model systems like llm-consortium.

**Tags**: `#LLM`, `#Model Release`, `#Inference Speed`, `#OpenRouter`, `#AI Tools`

---

<a id="item-8"></a>
## [Safety Refusals Should Target Harmful Subsets, Not Whole Topics](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) ⭐️ 7.5/10

A Hugging Face blog post by MultiverseComputingCAI argues that safety refusal mechanisms should operate at a finer granularity: models should refuse only the genuinely harmful subset of a topic rather than refusing the entire topic. The post contends that subset-level refusal preserves model usefulness while keeping safety guardrails intact. This discussion is directly relevant to LLM safety alignment and content moderation, as it addresses the trade-off between safety and helpfulness. If implemented well, fine-grained refusal could reduce over-refusal and keep models usable in legitimate contexts. The argument depends on a model's ability to reliably isolate harmful sub-concepts within a broader topic. Research on open-weight models suggests refusal behavior is often carried by a low-dimensional, linearly accessible feature, which may make fine-grained refusals technically feasible.

rss · Hugging Face Blog · Sep 8, 14:23

**Background**: LLM alignment is the process of training or fine-tuning models so that their outputs are safe, accurate, and consistent with human values. Modern chat models are typically trained to refuse requests considered harmful or inappropriate, often by learning examples such as 'User: inappropriate request; AI: elaborate apology.' However, refusal can be applied coarsely, causing models to avoid entire topics rather than only the dangerous parts. This blog post focuses on that granularity problem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/llm-alignment">What Is LLM Alignment? | IBM</a></li>
<li><a href="https://zentara.co/blog/llm-refusal-behavior/">LLM Refusal Behavior on Open-Weight Model</a></li>
<li><a href="https://www.lesswrong.com/posts/Dan6iKFruioYmZafw/thoughts-on-refusing-harmful-requests-to-large-language">Thoughts on refusing harmful requests to large language models</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#LLM alignment`, `#refusal behavior`, `#content moderation`, `#Hugging Face`

---

<a id="item-9"></a>
## [Mathematician Buckmaster Alleges OpenAI Pressure Over Navier-Stokes Result](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 7.4/10

Tristan Buckmaster published an online statement accusing OpenAI of pressuring him and Anthropic researcher Levent Alpöge over their finite-time blow-up work related to Navier-Stokes, and alleging ambiguity about whether OpenAI used their insights to train models. The statement also describes offers and warnings that he claims were aimed at influencing how the results were presented. This raises serious questions about research ethics, data privacy, and the increasing influence of AI companies over academic work. It could undermine trust in how OpenAI and similar companies handle user data and interact with independent researchers, especially on high-stakes problems like the Navier-Stokes Millennium Prize challenge. Buckmaster and Alpöge reportedly made progress on finite-time blow-up for incompressible porous media, Boussinesq, and 3D incompressible Euler equations, but not a full proof of the original Navier-Stokes Millennium problem. OpenAI acknowledged it 'cannot rule out that de-identified data derived from their usage of our products helped improve our models,' adding to the ambiguity.

hackernews · procedurecall · Sep 8, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49605915)

**Background**: The Navier-Stokes equations describe the motion of fluids, and whether smooth solutions always exist is one of the Millennium Prize Problems offering a $1 million reward. A 'finite-time blow-up' means a solution develops singularities in finite time. OpenAI had previously used a language model to discover a blow-up solution for a simplified Navier-Stokes-like problem, but Buckmaster's statement raises concerns that his and Alpöge's independent insights may have been used without consent. Earlier work by Buckmaster and Vicol used convex integration to show nonuniqueness of finite-energy weak solutions for the original equations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf">Finite time blowup for navier – stokes</a></li>

</ul>
</details>

**Discussion**: Commenters are largely angry at OpenAI, accusing it of using researchers' work without consent and of making threats to suppress independent results. Some express skepticism about whether the ambiguous evidence is sufficient to condemn OpenAI, but many see it as a pattern of problematic behavior by large AI companies regarding user data and academic integrity.

**Tags**: `#Navier-Stokes`, `#research ethics`, `#OpenAI`, `#AI data privacy`, `#mathematics`

---

<a id="item-10"></a>
## [New Skill 'I-Have-ADHD' Fights Claude Code's Lede-Burying Verbosity](https://github.com/ayghri/i-have-adhd) ⭐️ 7.0/10

A new open-source skill called 'i-have-adhd' was released on GitHub to make coding agents like Claude Code give concise answers instead of burying the key point. The project sparked a Hacker News discussion in which developers debated Claude's verbose writing style. Many developers rely on Claude Code as an agentic coding tool, and verbose output slows code review and obscures important changes. This skill highlights a broader ecosystem trend of using prompt-level hacks to counteract model behaviors that providers have not fixed by default. The installation method shown in the Hacker News thread is to paste a prompt into Claude Code that points to the repository's AGENTS.md file, where the skill/plugin instructions live. Commenters noted the effect often fades after a few turns unless reinforced, and suggested a hook could force it on every response.

hackernews · domhudson · Sep 8, 14:13 · [Discussion](https://news.ycombinator.com/item?id=49610631)

**Background**: Claude Code is Anthropic's agentic coding tool that runs in the terminal: it reads codebases, edits files, executes commands, and integrates with development tools. 'Skills' are add-on instructions that customize how such agents behave. The discussion centers on 'Claudisms' — recurring verbal and structural tics in Claude output, such as 'not-this-but-that' phrasing, unnecessary participial clauses, and burying the lede.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/wespomeroyny/claudisms/blob/main/claudisms.md">claudisms/claudisms.md at main · wespomeroyny/claudisms</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly validated the pain point: one said Claude is 'a terrible writer,' and another flagged its habit of reporting what it did not do. Others were skeptical about durability, saying the skill only lasts a few turns before Claude reverts to verbosity. One user also cautioned against installing skills through copy-pasted prompts.

**Tags**: `#AI`, `#LLM`, `#Claude Code`, `#coding agents`, `#developer tools`

---

<a id="item-11"></a>
## [OpenAI Introduces ChatGPT Images 2.5 with Sunburst and Flare API Models](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.0/10

OpenAI announced ChatGPT Images 2.5, which improves multi-turn instruction following, responds faster, and better preserves subjects in reference photos. The company also introduced two new API model IDs: gpt-image-2.5-sunburst for precision editing and gpt-image-2.5-flare for fast everyday generation. This release matters because OpenAI says its image generation models have already been used to create more than 3 billion images, and the new model choices give developers clearer trade-offs between speed and editing precision. It will be especially relevant for builders integrating text-to-image or image-editing features into their products. The Sunburst model offers extra precision for detailed creative work with longer generation times, while Flare is positioned as the default option for fast, high-quality everyday generation. According to OpenAI's API documentation, image output for gpt-image-2.5-sunburst costs $30 per million tokens, and Simon Willison demonstrated the new reference-image capability by upgrading his openai_image.py CLI to add a raccoon scientist to an existing chart.

rss · Simon Willison · Sep 8, 22:46

**Background**: ChatGPT Images is OpenAI's image generation offering, available both through ChatGPT and through the GPT-Image models in the OpenAI API. These models can generate images from natural-language prompts and edit or transform existing images while trying to preserve key subjects from reference photos. Instruction-following refers to how well a model obeys multi-turn prompts, while subject preservation describes its ability to keep the identity or style of an input image intact.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-5/">Introducing ChatGPT Images 2.5 | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst">GPT-Image-2.5 Sunburst Model | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#image generation`, `#API`, `#AI models`, `#Simon Willison`

---