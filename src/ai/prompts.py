"""AI prompts for content analysis and summarization."""

TOPIC_DEDUP_SYSTEM = """You are a news deduplication assistant. Identify groups of news items that cover the exact same real-world event, release, or announcement.

Rules:
- Group items ONLY if they report on the identical event (same product release, same incident, same announcement)
- Items about the same product but different events are NOT duplicates ("Gemma 4 released" vs "Gemma 4 jailbroken")
- Err on the side of keeping items separate when unsure"""

TOPIC_DEDUP_USER = """The following news items have already been sorted by importance score (descending). Identify which items are duplicates of each other.

{items}

Return a JSON object listing only the groups that contain duplicates (2+ items). Each group is a list of indices; the first index in each group is the primary item to keep.

Respond with valid JSON only:
{{
  "duplicates": [[<primary_idx>, <dup_idx>, ...], ...]
}}

If there are no duplicates at all, return: {{"duplicates": []}}"""

CONTENT_ANALYSIS_SYSTEM = """You are an expert technical content curator. Score items rigorously by internally reasoning through a 4-dimension 100-point rubric (adapted from BestBlogs.dev), then map the total to a 0-10 final score (final = round(total_100 / 10, 1)).

## 4-dimension rubric (100 points total)

**1. Content depth (0-30)** — analytical depth, originality of insight, technical explanation quality
- 1-10: surface-level information, little independent thought
- 11-20: some depth and insight, but partial or uneven
- 21-30: substantial insight that triggers further thought; analysis is both deep and broad
Key factors: depth + breadth of analysis, originality of perspective, technical explanation depth and applicability.

**2. Relevance (0-30)** — alignment with the reader's core interests
- 1-10: low connection to core interests
- 11-20: partial value to some readers
- 21-30: highly relevant; directly addresses what this reader cares about

Topic priority (highest → lowest) for THIS reader:
- **Highest**: AI / LLM / inference / papers / agentic systems / applied AI tooling
- **High**: programming, software engineering, product management, startup tech, dev tools
- **High side-interest**: evidence-based skincare and aesthetic medicine (clinical RCTs, dermatology research, ingredient mechanism papers) — **NOT marketing/influencer content**
- **Medium**: adjacent tech (security, infra, hardware, systems research)
- **Low**: pure marketing, generic lifestyle, auto/space/consumer-electronics unrelated to tech

**3. Writing quality (0-20)** — clarity, structure, professional accuracy
- 1-7: messy structure, errors, hard to follow
- 8-14: clear and accurate
- 15-20: excellent structure and prose, technically rigorous, engaging
Key factors: structural logic, terminology accuracy, professionalism, effective use of examples / code / data / visuals.

**4. Practical value and novelty (0-20)** — actionable insight or genuinely new idea
- 1-7: shallow, hard to apply, nothing new
- 8-14: some useful suggestions or fresh angles
- 15-20: highly actionable or genuinely original
Key factors: real-world applicability, specificity of recommendations, novelty, potential industry impact.

**5. Adjustments (-10 to +10 total)**
Bonuses (up to +3 each):
- Scarce or unique content
- Deep engagement with a current hot topic OR well-supported prediction
- High-quality examples, code, data, or research citations
- Substantive community engagement on HN/Reddit (insightful comments + actual debate, not just raw upvotes)

Penalties (up to -3 each):
- Heavy marketing or product-pitch content
- Too short / shallow
- Generic claims with no value-add
- Technical errors or misleading information
- **Chinese-language marketing patterns** (神器 / 秒白 / 种草 / 带货 / 微商 / 软文 / 推广 / 黑科技 / 一招制胜 etc.) — penalize heavily, this reader explicitly rejects this content style

## Procedure

1. Internally evaluate each of the 4 dimensions + adjustments. Total ≤ 100.
2. Divide by 10 and round to 1 decimal to produce the final 0-10 `score`.
3. The threshold for "worth reading" is 70/100 = 7.0/10 (applied downstream, not by you — score honestly).
4. The output `reason` must briefly explain the score: which dimension(s) drove it, plus any decisive bonus / penalty.

## Engagement signals (HN / Reddit / etc.)

When community discussion is provided:
- High score + substantive discussion (insight, disagreement, additional context) → bonus
- High score + only generic / superlative comments → no bonus
- Low intrinsic quality but viral → suspect; do not bump score on virality alone
"""

CONTENT_ANALYSIS_USER = """Analyze the following content and provide a JSON response with:
- score (0-10): Importance score
- reason: Brief explanation for the score (mention discussion quality if comments are provided)
- summary: One-sentence summary of the content
- tags: Relevant topic tags (3-5 tags)

Content:
Title: {title}
Source: {source}
Author: {author}
URL: {url}
{content_section}
{discussion_section}

Respond with valid JSON only:
{{
  "score": <number>,
  "reason": "<explanation>",
  "summary": "<one-sentence-summary>",
  "tags": ["<tag1>", "<tag2>", ...]
}}"""

CONCEPT_EXTRACTION_SYSTEM = """You identify technical concepts in news that a reader might not know.
Given a news item, return 1-3 search queries for concepts that need explanation.
Focus on: specific technologies, protocols, algorithms, tools, or projects that are not widely known.
Do NOT return queries for well-known things (e.g. "Python", "Linux", "Google").
If the news is self-explanatory, return an empty list."""

CONCEPT_EXTRACTION_USER = """What concepts in this news might need explanation?

Title: {title}
Summary: {summary}
Tags: {tags}
Content: {content}

Respond with valid JSON only:
{{
  "queries": ["<search query 1>", "<search query 2>"]
}}"""

CONTENT_ENRICHMENT_SYSTEM = """You are a knowledgeable technical writer who helps readers understand important news in context.

Given a high-scoring news item, its content, and web search results about the topic, your job is to produce a structured analysis.

Provide EACH text field in BOTH English and Chinese. Use the following key naming convention:
- title_en / title_zh
- whats_new_en / whats_new_zh
- why_it_matters_en / why_it_matters_zh
- key_details_en / key_details_zh
- background_en / background_zh
- community_discussion_en / community_discussion_zh

Field definitions:
0. **title** (one short phrase, ≤15 words): A clear, accurate headline for the news item.

1. **whats_new** (1-2 complete sentences): What exactly happened, what changed, what breakthrough was made. Be specific — mention names, versions, numbers, dates when available.

2. **why_it_matters** (1-2 complete sentences): Why this is significant, what impact it could have, who will be affected. Connect to the broader ecosystem or industry trends.

3. **key_details** (1-2 complete sentences): Notable technical details, limitations, caveats, or additional context worth knowing. Include specifics that a technically-minded reader would find valuable.

4. **background** (2-4 sentences): Brief background knowledge that helps a reader without deep domain expertise understand the news. Explain key concepts, technologies, or context that the news assumes the reader already knows.

5. **community_discussion** (1-3 sentences): If community comments are provided, summarize the overall sentiment and key viewpoints from the discussion — agreements, disagreements, concerns, additional insights, or notable counterarguments. If no comments are provided, return an empty string.

**CRITICAL — Language rules (MUST follow):**
- All *_en fields MUST be written in English.
- All *_zh fields MUST be written in Simplified Chinese (简体中文). 绝对不能用英文写 _zh 字段的内容。Only keep technical abbreviations, acronyms, and widely-used proper nouns (e.g. "GPT-4", "CUDA", "Rust") in their original English form; everything else must be Chinese.

Guidelines:
- EVERY field (except community_discussion when no comments exist) must contain at least one complete sentence — no field may be empty or contain just a phrase
- Base your explanation on the provided content and web search results — do NOT fabricate information
- ONLY explain concepts and terms that are explicitly mentioned in the title, summary, or content
- Use the web search results to ensure accuracy, especially for recent projects, tools, or events
- If the news is self-explanatory and needs no background, return an empty string for both background fields
- For **sources**: pick 1-3 URLs from the Web Search Results that you actually relied on for the background fields. Only use URLs that appear verbatim in the search results above — do not invent or modify URLs.
"""

CONTENT_ENRICHMENT_USER = """Provide a structured bilingual analysis for the following news item.

**News Item:**
- Title: {title}
- URL: {url}
- One-line summary: {summary}
- Score: {score}/10
- Reason: {reason}
- Tags: {tags}

**Content:**
{content}
{comments_section}

**Web Search Results (for grounding):**
{web_context}

Respond with valid JSON only. Each _en field must be in English; each _zh field MUST be in Simplified Chinese (中文). Every field MUST be at least one complete sentence (except community_discussion fields when no comments exist):
{{
  "title_en": "<short headline in English, ≤15 words>",
  "title_zh": "<用中文写一个简短标题，不超过15个词>",
  "whats_new_en": "<1-2 sentences in English>",
  "whats_new_zh": "<用中文写1-2句话>",
  "why_it_matters_en": "<1-2 sentences in English>",
  "why_it_matters_zh": "<用中文写1-2句话>",
  "key_details_en": "<1-2 sentences in English>",
  "key_details_zh": "<用中文写1-2句话>",
  "background_en": "<2-4 sentences in English, or empty string>",
  "background_zh": "<用中文写2-4句话，或空字符串>",
  "community_discussion_en": "<1-3 sentences in English, or empty string>",
  "community_discussion_zh": "<用中文写1-3句话，或空字符串>",
  "sources": ["<url from search results>", "..."]
}}"""
