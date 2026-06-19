---
name: academic-literature-research
description: "Deep academic literature research and paper analysis skill. Specialized for systematic literature review, paper deep-reading, and technical research in academic and technology domains. Triggers on: literature review, read paper, paper analysis, research survey, literature survey, 文献调研, 论文阅读, 论文分析, 研究综述, 技术调研. Provides comprehensive paper analysis including: research motivation, problem formulation, solution approach, innovation points, experimental validation, limitations, and research implications. Generates structured reports with APA 7.0 citations and actionable insights for follow-up research."
metadata:
  version: "3.1.0"
  last_updated: "2026-06-14"
  status: active
  data_access_level: raw
  task_type: open-ended
---

# Academic Literature Research — Deep Paper Analysis & Literature Review

Specialized skill for rigorous academic literature research and paper analysis in academic and technology domains.

**Core Purpose**: Transform raw papers and research topics into structured, actionable literature analysis with deep insights for follow-up research.

---

## Quick Start

### Minimal Command

```
Deep read this paper: Attention Is All You Need
```

or

```
Survey literature on transformer architectures
```

### Execution

1. **Clarification** — Understand user intent and research scope
2. **Discovery** — Research Architect Agent finds papers via Semantic Scholar API + WebSearch (survey/multi-paper modes)
3. **Retrieval** — Content Retrieval Agent fetches paper content via WebFetch
4. **Analysis** — Apply 7-point framework (or 10-point for survey mode) to each paper's content
5. **Composition** — Generate final report with APA 7.0 citations and insights
6. **File Output** — Save analysis as markdown file to disk (NOT command line output)

### Output

All analysis results are saved as markdown files:
- ✅ Single paper analysis → `[Paper_Title]_analysis.md`
- ✅ Multi-paper synthesis → `[Topic]_synthesis.md`
- ✅ Literature survey → `[Topic]_survey.md`
- ✅ Quick brief → `[Paper_Title]_brief.md`

Files are saved to your current directory with a confirmation message showing the file path.

---

## Trigger Conditions

### Trigger Keywords

**English**: literature review, read paper, paper analysis, research survey, literature survey, deep read, analyze paper, survey literature

**中文**: 文献调研, 论文阅读, 论文分析, 研究综述, 深度阅读, 分析论文, 调研文献

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Writing a paper (not researching) | `academic-paper` |
| Reviewing a paper (structured peer review) | `academic-paper-reviewer` |

---

## Mode Selection Guide

| Your Situation | Recommended Mode | Output |
|---|---|---|
| Deep analysis of one specific paper | `single-paper` | 2,000-4,000 words |
| Compare and synthesize multiple papers | `multi-paper` | 3,000-6,000 words |
| Comprehensive review of a research area | `survey` | 4,000-8,000 words |
| Fast overview of a paper | `quick-brief` | 800-1,500 words |

---

## Dependencies

### Built-in Tools (No Installation Required)

| Tool | Purpose | How Used |
|---|---|---|
| **WebSearch** | Discover papers by topic when API is insufficient | Phase 2 — Research Architect Agent |
| **WebFetch** | Retrieve paper content from arXiv, Semantic Scholar, DOI pages | Phase 2 — Content Retrieval Agent |
| **Semantic Scholar API** | Paper metadata, citation counts, link generation | Phase 2 — primary search source |

### Not Required

- ❌ web-access skill (WebSearch/WebFetch are used directly)
- ❌ External API keys (Semantic Scholar is free; WebSearch/WebFetch are built-in)
- ❌ Additional installations

---

## Agent Architecture

This skill uses four specialized agents that activate based on mode. Each agent has a defined role, tools, and handoff contract.

| Agent | Role | Tools | Active In |
|---|---|---|---|
| **Research Architect** | Discover papers via multi-source search | WebSearch, Semantic Scholar API | survey, multi-paper |
| **Content Retrieval** | Fetch actual paper content from URLs | WebFetch | all modes |
| **Analysis** | Apply 7-point (or 10-point for survey) framework to each paper | (reasoning only) | all modes |
| **Synthesis** | Cross-paper comparison and report generation | Write, Edit | multi-paper, survey |

### Research Architect Agent

**Trigger**: survey mode or multi-paper mode when user provides a topic rather than specific papers.

**Responsibilities**:
1. Decompose the research topic into 3–5 targeted search queries
2. Query Semantic Scholar API for each query (primary source)
3. Fall back to WebSearch for queries returning < 3 results
4. Screen candidates for relevance using title + abstract
5. Rank and select final paper set (5–10 for survey, 2–5 for multi-paper)

**Query generation strategy**:
- Core query: `[topic] [key method]`
- Problem query: `[problem being solved] [domain]`
- Method query: `[technique] [application area]`
- Recency query: `[topic] 2024 2025`
- Survey query: `survey [topic]` or `review [topic]`

**Screening criteria** (apply in order):
1. Title relevance — must match research topic
2. Abstract relevance — abstract must address the core problem
3. Quality — peer-reviewed > arXiv preprint > technical report
4. Recency — weight 2022–2026 unless historical context is needed
5. Citations — prefer > 10 citations for survey mode

### Content Retrieval Agent

**Trigger**: all modes, after paper list is confirmed.

**Responsibilities**:
1. For each paper, fetch content from the best available URL
2. Extract: abstract, introduction key paragraphs, method description, results summary, conclusion
3. If full text is inaccessible (paywall), use Semantic Scholar abstract + metadata

**Retrieval priority per paper**:
1. arXiv abstract page: `https://arxiv.org/abs/{arxiv_id}` — fetch HTML, extract sections
2. Semantic Scholar page: `https://www.semanticscholar.org/paper/{id}` — fetch HTML
3. DOI page: `https://doi.org/{doi}` — fetch HTML (may be paywalled; use abstract if blocked)
4. WebSearch fallback: `"{title}" abstract site:arxiv.org` — find accessible version

**Handoff to Analysis Agent**: structured dict per paper with keys `title`, `authors`, `year`, `venue`, `abstract`, `content_sections`, `links`, `citation_count`, `verified`.

---

## Operational Modes

| Mode | Focus | Agents Active | Output |
|---|---|---|---|
| `single-paper` (default) | Deep analysis of one paper | Content Retrieval + Analysis | Comprehensive analysis report |
| `multi-paper` | Comparative analysis of 2-5 papers | Research Architect (if topic given) + Content Retrieval + Analysis + Synthesis | Synthesis report + individual analyses |
| `survey` | Literature landscape in a research area | Research Architect + Content Retrieval + Analysis + Synthesis | Survey report + key papers analysis |
| `quick-brief` | Quick overview of a paper | Content Retrieval + Analysis (abbreviated) | Brief summary + key insights |

---

## Phase-by-Phase Workflow

### Phase 1: CLARIFICATION (Interactive)

Determine the user's research intent and scope.

#### Fast Path — Pre-Specified Parameters

**Before asking any questions, check what the user already provided:**

| Parameter | Already provided? | Action |
|-----------|------------------|--------|
| Mode | e.g., "survey模式", "single paper", "quick brief" | Skip Step 1 |
| Topic | e.g., "MLLM/LVLM", "transformer architectures" | Skip topic question in Step 2 |
| Time period | e.g., "2022–2026", "last 5 years" | Skip time period question in Step 2 |
| Paper count | e.g., "8 papers", "top 10" | Skip paper count question in Step 2 |
| Language | e.g., request written in Chinese | Output report in same language |

If the user has already specified mode + topic + time period, skip directly to Step 3 (Confirm Scope) with those values pre-filled. Only ask for genuinely missing parameters.

**Example**: User says "survey模式调研：近年（2022–2026）多模态大模型研究方向"
→ mode=survey ✓, topic=MLLM/LVLM ✓, time=2022–2026 ✓, language=Chinese ✓
→ Skip Steps 1 and 2. Go directly to Step 3 with paper count defaulting to 8.

#### Step 1 — Detect Mode

Only ask if mode was NOT specified by the user:

> Which of these best describes what you need?
>
> 1. **Single Paper Analysis** — Deep analysis of one specific paper
> 2. **Multi-Paper Synthesis** — Compare and synthesize multiple papers
> 3. **Literature Survey** — Comprehensive review of a research area
> 4. **Quick Brief** — Fast overview of a paper

Wait for user selection.

#### Step 2 — Collect Inputs

Only ask for parameters NOT already provided by the user.

**For Single Paper / Quick Brief:**
- What is the paper title, DOI, arXiv ID, or URL? *(if not provided)*
- What is your research context? *(optional)*
- Any specific aspects to focus on? *(optional)*

**For Multi-Paper Synthesis:**
- How many papers? (2-5 recommended) *(if not provided)*
- Provide titles, DOIs, or URLs for each paper *(if not provided)*
- What is the comparison focus? *(if not provided)*

**For Literature Survey:**
- What is the research area or topic? *(if not provided)*
- Any specific sub-areas or keywords? *(optional)*
- Time period? (default: last 5 years) *(if not provided)*
- How many key papers to analyze? (default: 8) *(if not provided)*

#### Step 3 — Confirm Scope

Summarize back to user with all parameters (pre-specified + collected):

> **Confirmed Scope:**
> - Mode: [selected mode]
> - Topic: [research topic]
> - Time Period: [years]
> - Papers: [count]
> - Output Language: [language of user's request]
> - Output File: `[Topic]_survey.md`
>
> Ready to proceed? (yes/no)

Wait for confirmation before Phase 2.

---

### Phase 2: INVESTIGATION

Discover papers, retrieve their content, and verify source quality. Uses Research Architect Agent (discovery) and Content Retrieval Agent (fetching).

#### Step 1 — Paper Discovery

**For single-paper / quick-brief** (user provides a specific paper):
- Skip discovery. Go directly to Step 2 with the user-provided title/DOI/URL.

**For survey / multi-paper** (user provides a topic):

Activate **Research Architect Agent**. Execute the following search pipeline:

**1a. Generate search queries**

From the user's topic and time period, produce 3–5 queries covering different angles. **Always incorporate the user's time period into at least one query.**

```
Topic: "multimodal large language models (MLLM/LVLM)"
Time period: 2022–2026

Queries:
1. "multimodal large language model"
2. "vision language model LVLM benchmark"
3. "MLLM visual reasoning instruction tuning"
4. "multimodal large language model 2024 2025"
5. "survey multimodal large language model"
```

**1b. Search Semantic Scholar API (primary)**

**CRITICAL — Call queries ONE AT A TIME (sequentially), never in parallel.**  
Semantic Scholar's public API enforces a per-second rate limit. Calling 3+ URLs simultaneously triggers HTTP 429 for all of them. Send one WebFetch request, wait for the result, then send the next.

For each query, use **WebFetch** to call the Semantic Scholar API:

```
Tool: WebFetch
URL: https://api.semanticscholar.org/graph/v1/paper/search?query={URL-encoded query}&limit=10&fields=title,authors,year,venue,externalIds,citationCount,abstract
Prompt: "Extract all papers from this JSON response. For each paper return: title, authors (list of names), year, venue, arXiv ID (from externalIds.ArXiv), DOI (from externalIds.DOI), Semantic Scholar paperId, citationCount, and abstract. Format as a numbered list."
```

Example URL for query "multimodal large language model 2024":
```
https://api.semanticscholar.org/graph/v1/paper/search?query=multimodal+large+language+model+2024&limit=10&fields=title,authors,year,venue,externalIds,citationCount,abstract
```

**429 Rate-Limit Handling:**  
If any query returns HTTP 429, **stop all remaining API calls immediately** and switch the entire discovery phase to the arXiv Direct Fallback described in Step 1c. Do NOT retry the API — the rate limit window is 1 minute and retrying wastes time. Log which queries succeeded before the 429 and carry their results forward.

Collect all results across all queries. Deduplicate by title similarity (threshold: 0.85 — same paper if titles are >85% similar).

**1c. arXiv Direct Fallback (primary fallback — use when API returns 429, or < 3 results for a query)**

This fallback activates in two situations:
- The Semantic Scholar API returned HTTP 429 (rate limit), OR
- A specific query returned fewer than 3 papers with non-empty abstracts

**Why arXiv direct fetch instead of WebSearch:**  
WebSearch with academic queries (e.g., `site:arxiv.org multimodal large language model`) frequently returns zero results in this environment. The reliable alternative is to fetch arXiv abstract pages directly using known or inferred arXiv IDs.

**arXiv Direct Fetch strategy:**

*Step 1 — Use domain knowledge to infer arXiv IDs for well-known papers in the topic area.*

For common research areas, landmark papers have well-known arXiv IDs. For example:
- MLLM/LLaVA family: 2304.08485, 2310.03744 (LLaVA-1.5), 2312.14238 (InternVL)
- Instruction tuning: 2305.06500 (InstructBLIP), 2309.05519 (NExT-GPT)
- Benchmarks: 2307.06281 (MMBench), 2409.12191 (Qwen2-VL)

For each inferred arXiv ID, fetch the abstract page:
```
Tool: WebFetch
URL: https://arxiv.org/abs/{arxiv_id}
Prompt: "Extract the paper title, authors, year, venue (if mentioned), and abstract."
```

*Step 2 — Extract "Related Work" or "References" sections from retrieved papers to discover more papers.*

Once 2–3 seed papers are retrieved, their reference lists often contain the next tier of important papers. Fetch the HTML version of each seed paper and extract cited paper titles:
```
Tool: WebFetch
URL: https://arxiv.org/html/{arxiv_id}
Prompt: "List all paper titles and arXiv IDs mentioned in the references or related work section."
```

*Step 3 — Follow up on discovered paper titles by fetching their arXiv pages.*

From discovered titles, infer or search for their arXiv IDs. For any paper where the arXiv ID is unknown, use:
```
Tool: WebFetch
URL: https://arxiv.org/search/?query={URL-encoded title}&searchtype=all&start=0
Prompt: "Find the arXiv ID and year for the paper titled '{title}'. Extract the first matching result's arXiv ID."
```

**Minimum viable fallback:** If no API results and arXiv fallback also fails to find enough papers, proceed with whatever papers were successfully retrieved, noting the constraint. Do not invent papers.

**Legacy WebSearch patterns (secondary — try only if arXiv fallback is also unsuccessful):**
- `site:arxiv.org "{core topic}" {year}` — may return results for specific topics
- `"{paper title}" filetype:pdf` — sometimes finds preprint PDFs

**1d. Screen and rank candidates**

Apply screening criteria in order:
1. Title must contain topic keywords or close synonyms
2. Abstract must address the core research problem (not just mention it tangentially)
3. **Time period filter**: exclude papers published outside the user's specified range (e.g., exclude year < 2022 or year > 2026). Apply this strictly.
4. Venue quality: top-tier conference/journal > workshop > arXiv > other
5. Citation count: ≥ 10 for survey mode (waive for papers < 1 year old, i.e., published in 2025–2026)

**Paper Type Classification** (survey mode — classify each paper before selection):

| Type | Definition | Target Ratio | Hard Limit |
|------|-----------|-------------|-----------|
| Method Paper | Proposes a new model, algorithm, or architecture | ≥ 60% | required |
| Benchmark Paper | Establishes evaluation tasks, metrics, or competition | ≥ 20% combined (see note) | soft |
| Dataset Paper | Introduces a new training or evaluation dataset | ≥ 20% combined (see note) | soft |
| Analysis Paper | Empirical analysis, ablation study, or theoretical work | ≥ 10% | soft |
| Survey Paper | Reviews existing work in a subfield | ≤ 10% | required |

**Note — Benchmark/Dataset ratio is a soft target, not a hard requirement:**  
In fast-moving fields where research is method-centric (MLLM, LLM, Agent), Benchmark and Dataset papers represent a structurally smaller share of the literature. In these fields it is acceptable for Benchmark+Dataset to be 10–15% instead of 20%+, provided that:
1. At least 1 Benchmark or Dataset paper is included if one exists in the field
2. The deficit is explicitly noted in the Executive Summary
3. Method Papers make up the difference (capped at 80%)

Do NOT include low-quality papers solely to hit a ratio target. Quality over quota.

Survey papers may only be used for background context; they must not become core analysis subjects. Avoid selecting multiple surveys covering the same sub-topic.

**Prioritization within each type:**
- Pioneering papers that introduced a research paradigm
- Highly-cited papers (≥ 100 citations)
- Technical turning-point papers that shifted the dominant approach
- Current SOTA papers
- Most recent representative papers (2025–2026)

**Time Coverage Requirement** (fast-evolving fields: LLM, Agent, MLLM, recommender systems, spatiotemporal prediction, AI4Science):
- Papers from 2025–2026 must account for ≥ 30% of the final selection
- Must include: latest top-conference papers, latest high-impact arXiv preprints, latest benchmark work
- Final selection must span: classic foundational work + current mainstream work + latest cutting-edge work
- Avoid surveys dominated only by 2018–2024 historical review

Select final paper set:
- Survey mode: 5–10 papers covering different paper types, sub-topics, and time periods within the user's range
- Multi-paper mode: 2–5 papers matching user's comparison focus

#### Step 2 — Content Retrieval

Activate **Content Retrieval Agent** for each paper in the final set.

**Retrieval sequence** (try in order, stop at first success):

**Success** = WebFetch returns content containing the paper's abstract text (at least 50 words). If WebFetch returns an error, a login page, a 404, or content that does not contain the abstract, treat as failure and try the next option.

```
1. arXiv abstract page (most reliable for arXiv papers)
   URL: https://arxiv.org/abs/{arxiv_id}
   Tool: WebFetch
   Prompt: "Extract the paper title, authors, abstract, and any available sections
            (introduction, method/approach, experiments/results, conclusion).
            Return each section with its heading."
   Success check: response contains abstract text ≥ 50 words

2. arXiv HTML full text (when abstract page succeeds, try for full text)
   URL: https://arxiv.org/html/{arxiv_id}
   Tool: WebFetch
   Prompt: "Extract the introduction (first 3 paragraphs), method/approach section
            (key technical description), results section (main quantitative findings),
            and conclusion. Return each with its section heading."
   Success check: response contains method or results content

3. Semantic Scholar API — abstract endpoint (for non-arXiv papers)
   URL: https://api.semanticscholar.org/graph/v1/paper/{s2_paperId}?fields=title,abstract,tldr,year,venue,authors,citationCount
   Tool: WebFetch
   Prompt: "Extract the title, abstract, tldr (if present), year, venue, authors,
            and citationCount from this JSON response."
   Success check: response contains abstract text ≥ 50 words

4. DOI page
   URL: https://doi.org/{doi}
   Tool: WebFetch
   Prompt: "Extract the paper abstract and any available sections."
   Success check: response contains abstract text ≥ 50 words (often paywalled — may fail)

5. WebSearch fallback
   Query: '"{paper title}" abstract arxiv'
   Tool: WebSearch
   → Find an accessible URL from results, then WebFetch that URL
   Prompt: "Extract the paper abstract and key sections."
```

**Content extraction targets** (from fetched HTML):
- `abstract` — full abstract text
- `introduction` — first 2–3 paragraphs (research motivation, gap statement)
- `method` — core technical approach description
- `results` — key quantitative findings and comparisons
- `conclusion` — summary and future work

**Minimum viable content**: If only the abstract is retrievable, proceed with abstract-only analysis. Mark the paper as `content_level: abstract_only` in the output. Do not skip the paper.

**Handoff to Phase 3**: For each paper, produce:
```
{
  title: str,
  authors: [str],
  year: int,
  venue: str,
  abstract: str,
  content_sections: {intro, method, results, conclusion},  # may be empty
  content_level: "full_text" | "abstract_only" | "metadata_only",
  links: {arxiv, doi, semantic_scholar},
  citation_count: int,
  verified: bool,
  verification_method: "s2_api" | "doi" | "web_search" | "none"
}
```

#### Step 3 — Source Quality Assessment

For each retrieved paper, assess quality using available data:

```
Quality Score:
  HIGH   — Peer-reviewed top-tier venue (NeurIPS, ICML, Nature, Science, etc.) + citations > 100
  MEDIUM — Peer-reviewed reputable venue + citations 10–100
  LOW    — arXiv preprint, workshop, or citations < 10
  UNVERIFIED — Could not verify via any source
```

Quality score is included in the final report and used to weight claims in synthesis.

#### Fallback: Manual Input Mode

When all retrieval methods fail for a paper, ask the user:

```
Could not retrieve content for: [paper title]

Please provide any of the following so I can proceed:
- Paper abstract (paste text)
- arXiv ID (e.g., 2106.14881)
- DOI (e.g., 10.1145/3495530.3495531)
- Direct URL to the paper

Or type "skip" to exclude this paper from the analysis.
```

---

### Phase 3: ANALYSIS

Conduct structured analysis of each paper using the appropriate framework.

#### Analysis Frameworks

**Single Paper, Quick Brief, Multi-Paper modes** use the **7-point framework** below.  
**Survey mode** uses the extended **10-point framework** defined in the Survey Mode section.

For single/quick-brief/multi-paper modes, analyze using these 7 dimensions:

##### 1. Research Motivation (为什么提出)

**What to extract:**
- Historical context and background
- Why this research matters
- The main research question being addressed
- Research gaps and white spaces

**Output format:**
```
**Background**: [Historical context]
**Core Research Question**: [Main research question]
**Research Gaps**: 
- [Gap 1]
- [Gap 2]
- [Gap 3]
```

##### 2. Problem Formulation (解决什么问题)

**What to extract:**
- Precise problem statement
- Specific challenges being addressed
- Evaluation criteria and metrics
- Constraints and assumptions

**Output format:**
```
**Problem Statement**: [Problem statement]
**Specific Challenges**:
- [Challenge 1]
- [Challenge 2]
- [Challenge 3]
**Evaluation Metrics**:
- [Metric 1]
- [Metric 2]
- [Metric 3]
```

##### 3. Solution Approach (如何解决)

**What to extract:**
- Core idea or main approach
- Technical components and modules
- Architecture or system design
- Key algorithms or methods

**Output format:**
```
**Core Idea**: [Main idea]
**Technical Components**:
1. **Component 1**
   - [Description]
   - [Key details]
2. **Component 2**
   - [Description]
   - [Key details]
**Architecture**:
[ASCII diagram or flowchart]
```

##### 4. Innovation Points (创新在哪)

**What to extract:**
- What is novel compared to existing work
- Why each innovation matters
- Comparison with related approaches
- Significance of the contribution

**Output format:**
```
1. **Innovation 1**
   - [Description of what is novel]
   - [Why it matters]
2. **Innovation 2**
   - [Description of what is novel]
   - [Why it matters]
3. **Innovation 3**
   - [Description of what is novel]
   - [Why it matters]
```

##### 5. Experimental Results (效果是否有效)

**What to extract:**
- Datasets and benchmarks used
- Baseline methods and comparisons
- Quantitative results and metrics
- Ablation studies and analysis
- Statistical significance

**Output format:**
```
**Datasets/Benchmarks**:
- [Dataset 1]: [Description]
- [Dataset 2]: [Description]

**Results Comparison**:
| Model | Metric 1 | Metric 2 | Metric 3 |
|-------|----------|----------|----------|
| [Baseline 1] | [Value] | [Value] | [Value] |
| [This Paper] | [Value] | [Value] | [Value] |

**Key Findings**:
- [Finding 1]
- [Finding 2]
```

##### 6. Limitations (限制是什么)

**What to extract:**
- Method-level limitations (complexity, scalability)
- Experimental limitations (dataset bias, incomplete baselines)
- Theoretical gaps (missing proofs, assumptions)
- Generalization challenges (domain-specific constraints)

**Output format:**
```
**Method Level**:
- [Limitation 1]
- [Limitation 2]
**Experimental Level**:
- [Limitation 1]
- [Limitation 2]
**Theoretical Level**:
- [Limitation 1]
- [Limitation 2]
**Generalization Challenges**:
- [Challenge 1]
- [Challenge 2]
```

##### 7. Research Implications (研究启发)

**What to extract:**
- Implications for the research field
- Potential improvements and extensions
- Transferability to other problems
- Connection to your own research

**Output format:**
```
**Implications for the Field**:
- [Implication 1]
- [Implication 2]
**Potential Improvements**:
- [Improvement 1]
- [Improvement 2]
**Transferability to Other Problems**:
- [Application 1]
- [Application 2]
**Connection to Your Research**:
- [How this relates to your work]
```

#### Implementation for Different Modes

**Content-level adaptation** — adjust depth based on what was retrieved:

| content_level | Available sections | Sections to mark as limited |
|---|---|---|
| `full_text` | All | None |
| `abstract_only` | Abstract only | §3 Solution Approach, §5 Experimental Results — write "Limited: based on abstract only" |
| `metadata_only` | Title, venue, year, citations | §1–§7 all limited — write brief note, do not fabricate |

**Single Paper Mode:**
1. Apply 7-point framework to the single paper
2. Generate detailed analysis document
3. Include paper identifiers and links
4. Add verification status from Semantic Scholar

**Multi-Paper Mode:**
1. Apply 7-point framework to each paper
2. Conduct cross-paper synthesis:
   - Identify common themes
   - Compare methodological approaches
   - Detect contradictions and reconcile
   - Analyze research gaps
3. Create thematic analysis sections

**Survey Mode:**

Survey mode is **research-question-centric**, not paper-centric. Research problems are the backbone; papers are evidence. Do not organize the output as "Paper A, Paper B, Paper C" — organize it around what the field is trying to solve.

**Step A: Identify Core Research Problems**

Before any per-paper analysis, identify 3–6 core problems the field is working on. Examples:
- Spatiotemporal forecasting: modeling spatial dependencies / temporal dependencies / dynamic graph structure / cross-city generalization
- MLLM: visual alignment / visual instruction tuning / visual reasoning / Agent capability
- Recommender systems: cold start / long-term interest modeling / generalization

**Step B: Build Research Landscape**

For each core research problem, identify the technical routes used to address it. For each route, document:
- **Research Question**: what specific problem this route addresses
- **Motivation**: why this route matters and why other routes were insufficient
- **Main Approaches**: categories of methods within this route (e.g., GNN-based, Transformer-based, hybrid)
- **Representative Papers**: at minimum Title, Authors, Year, Venue, Link for each — at least 2–3 papers per route
- **Strengths**: what problems this route successfully addresses
- **Limitations**: unsolved problems that remain within this route
- **Relationship to Other Directions**: complementary routes, competing routes, hierarchical relationships

**Step C: Apply 10-Point Framework to Representative Papers**

For the most important/representative papers (typically 5–8), apply the full 10-point framework. Other papers may appear in the Research Landscape with briefer mentions.

10-point analysis framework:

1. **Research Problem** — what specific problem does this paper address (1–2 sentences)
2. **Core Idea** — the central conceptual insight (not just "we propose X", but WHY X was the right approach to the problem)
3. **Method Overview** — technical description of key components and architecture
4. **Innovation** — what is genuinely novel compared to prior work; compare explicitly with direct predecessors
5. **Why It Works** — design rationale analysis (REQUIRED; do not merely describe modules):
   - Why is this design better than the previous approach?
   - What key bottleneck or contradiction does it resolve?
   - What insight makes the performance improvement possible?
6. **Experimental Evidence** — critical evaluation of support for claims:
   - Datasets and baselines used
   - Key quantitative results
   - Are experiments adequate? (sufficient ablation, fair baselines, reproducibility)
7. **Strengths** — what this paper contributes well
8. **Limitations** — method-level, experimental, and generalization limitations
9. **Position in the Field** — lineage mapping:
   - Which technical route this paper belongs to
   - Which prior works it builds on (name specific papers)
   - Which subsequent works it influenced (name specific papers if known)
   - Classification: Pioneering Work / Refinement Work / Turning-Point Work / Extension Work
10. **Research Insights** — what this paper reveals for future research

Content-level adaptation for 10-point framework:
- `full_text`: complete all 10 points
- `abstract_only`: mark §3, §5, §6 as limited; complete §1, §2, §4, §7, §8, §9, §10 from abstract
- `metadata_only`: note briefly; do not fabricate

**Step D: Cross-Paper Insights**

Extract field-level patterns from the paper set. Do NOT repeat per-paper summaries.

**Common Patterns**: what mainstream methods in this field share (data representations, training strategies, evaluation protocols)

**Bottlenecks**: shared unsolved problems that constrain the entire field

**Open Questions**: research problems the field has not yet seriously addressed

**Research Evolution Analysis**: for each major paradigm shift (2–4 total), analyze:
- **Previous Paradigm**: what the old dominant approach was
- **New Paradigm**: what replaced or is replacing it
- **Why the Shift Happened**: analyze at least one cause: performance bottleneck, scalability issue, data scale change, compute improvement, hardware environment change, benchmark change, application requirement change
- **Evidence**: cite 2–3 representative papers that document or exemplify the shift
- **Remaining Issues**: what the new paradigm still fails to resolve

Example format:
```
Previous Paradigm: CNN with locality inductive bias
New Paradigm: Vision Transformer with global self-attention

Why the shift happened:
- CNN receptive field limited long-range dependency modeling
- Self-attention enables full-sequence global context at acceptable cost
- Large-scale pretraining data (ImageNet-21K) became available
Evidence: Dosovitskiy et al. (ViT, ICLR 2021), Liu et al. (Swin, ICCV 2021)
Remaining issues: High compute cost, requires large pretraining data
```

**Step E: Critical Analysis**

Critically evaluate the field. Do not default to treating all papers as valid.

**Contradictions**: cite papers with conflicting conclusions and analyze why they disagree

**Benchmark Bias**: which datasets or evaluation setups systematically favor certain methods

**Evaluation Issues**: gaps between reported benchmark performance and real-world capability

**Scalability Issues**: which claimed advantages disappear at larger scale or different data distributions

**Hype vs Evidence**: for 2–3 prominent directions, assess:
- **Popularity**: how much attention this direction receives
- **Evidence Strength**: Strong (extensive ablation, multiple venues, reproduced) / Moderate / Weak (single paper, no ablation, unreproduced)
- **Research Maturity**: Emerging / Growing / Mature / Saturated
- **Risk Assessment**: flag any: data contamination, benchmark gaming, engineering over-tuning, reproducibility concerns

**Step F: Emerging Directions (2025–2026)**

Identify 3–5 research directions gaining significant traction in 2025–2026. For each:
- **Research Trend**: name and one-line description
- **Why It Emerged**: what limitation or new opportunity triggered this direction
- **Representative Papers**: must provide Title, Authors, Year, Venue/arXiv, Link — use actual papers, do not invent
- **Relationship to Existing Work**: builds on / challenges / orthogonal to which established routes
- **Potential Impact**: what changes this direction could bring
- **Maturity Assessment**: Emerging / Growing / Mature

**Step G: Evidence-Based Future Directions**

Derive future directions from evidence; do not invent generic suggestions. Each direction must trace to a specific bottleneck, open question, critical finding, or emerging trend.

Required format for each future direction:
```
Current Bottleneck: [specific observed limitation]
↓
Why Existing Methods Fail: [reason existing approaches cannot solve it]
↓
Possible Future Direction: [specific research approach]
```

**Prohibited** unless backed by specific evidence: "improve performance", "improve efficiency", "improve generalization", "scale to larger models"

---

### Phase 4: COMPOSITION

Generate final analysis report using the appropriate template.

#### Template Selection

```
1. Single paper: templates/paper_analysis_template.md
2. Multi-paper: templates/multi_paper_synthesis_template.md
3. Survey: templates/survey_report_template.md
4. Quick brief: templates/quick_brief_template.md
```

#### Survey Report Template Structure

For survey mode, use the following structure:

```
1. Header
   - Survey title
   - Scope, papers analyzed, time period, date

2. Executive Summary
   - 2-3 paragraphs: research landscape overview, key findings, major gaps

3. Research Landscape
   - 3.1 Core Research Problems (the 3-6 key problems the field addresses)
   - 3.2 Technical Routes (one subsection per route):
     - Route N: [Route Name]
       - Research Question
       - Motivation
       - Main Approaches
       - Representative Papers (Title, Authors, Year, Venue, Link)
       - Strengths
       - Limitations
       - Relationship to Other Directions

4. Representative Papers (10-point framework for each core paper)
   - PAPER 1: [Title]
     - Paper Identifiers & Links
     - 1. Research Problem
     - 2. Core Idea
     - 3. Method Overview
     - 4. Innovation
     - 5. Why It Works
     - 6. Experimental Evidence
     - 7. Strengths
     - 8. Limitations
     - 9. Position in the Field
     - 10. Research Insights
   - PAPER 2 … PAPER N: [Same 10-point structure]

5. Cross-Paper Insights
   - 5.1 Common Patterns
   - 5.2 Bottlenecks
   - 5.3 Open Questions
   - 5.4 Research Evolution Analysis
     - Evolution N: [Previous Paradigm → New Paradigm]
       - Previous Paradigm
       - New Paradigm
       - Why the Shift Happened
       - Evidence
       - Remaining Issues

6. Critical Analysis
   - 6.1 Contradictions
   - 6.2 Benchmark Bias
   - 6.3 Evaluation Issues
   - 6.4 Scalability Issues
   - 6.5 Hype vs Evidence
     - Direction: [Name]
       - Popularity / Evidence Strength / Research Maturity / Risk Assessment

7. Emerging Directions (2025–2026)
   - Direction N: [Trend Name]
     - Why It Emerged
     - Representative Papers (with links)
     - Relationship to Existing Work
     - Potential Impact
     - Maturity Assessment

8. Future Directions (Evidence-Based)
   - Direction N: [Name]
     - Current Bottleneck → Why Existing Methods Fail → Possible Future Direction

9. References (APA 7.0)

10. AI Disclosure Statement
```

#### Implementation Steps

**Step 1: Load Appropriate Template**

Use the **Read tool** to load the template file before generating content:

```
Tool: Read
file_path: [skill_base_dir]/templates/survey_report_template.md   (for survey)
file_path: [skill_base_dir]/templates/paper_analysis_template.md  (for single-paper)
file_path: [skill_base_dir]/templates/multi_paper_synthesis_template.md (for multi-paper)
file_path: [skill_base_dir]/templates/quick_brief_template.md     (for quick-brief)
```

The skill base directory is the directory containing this SKILL.md file. Read the template to understand the exact section structure before generating any content.

**Step 2: Determine Output Language**

Generate the entire report in the **same language as the user's request**:
- User wrote in Chinese → report in Chinese (section headings, analysis text, synthesis, conclusions)
- User wrote in English → report in English
- Mixed → use the dominant language of the user's request

APA 7.0 citations remain in their original language (paper titles as published).

**Step 3: Determine Output Directory**

Save the output file to the **user's current working directory** (the directory the user is working in, NOT the skill directory). If unclear, ask the user:
> Where should I save the output file? (default: current directory)

**Step 4: Populate Template Sections**

Fill in all template sections with analysis content:
- Header: Use confirmed scope parameters (topic, time period, paper count, date)
- Executive Summary: Synthesize key findings (2-3 paragraphs)
- Introduction: Explain research area and methodology (include search queries used)
- Key Papers Analysis: Use 7-point framework output from Phase 3 — expand the full structure for EVERY paper (do not write "repeat structure above")
- Cross-Paper Synthesis: Integrate findings across papers
- Research Gaps: Identify and prioritize gaps
- Conclusion: Synthesize implications and future directions

**Step 5: Format Citations**

Format all citations in APA 7.0 style:
- Author(s), Year. Title. Journal/Conference, Volume(Issue), pages. DOI/URL

**Step 6: Add Paper Identifiers and Links**

For each paper, include:
- DOI links: `https://doi.org/10.xxxxx`
- arXiv links: `https://arxiv.org/abs/xxxx.xxxxx`
- Semantic Scholar links: `https://api.semanticscholar.org/graph/v1/paper/{paperId}`
- Verification status: Citation count, verification method

**Step 7: Add AI Disclosure Statement**

Include at the end of the document:

```
This literature analysis was generated with AI-assisted research tools. 
All claims are grounded in the source papers and related work. 
The analysis framework, paper selection, and synthesis were conducted 
using automated literature research capabilities (WebSearch, WebFetch, 
Semantic Scholar API), with human oversight of the final output.
```

**Step 8: Generate and Save Output File**

**Output filename** (use underscores, no spaces, ASCII-safe):

| Mode | Filename Format | Example |
|------|-----------------|---------|
| Single paper | `[Paper_Title]_analysis.md` | `Attention_Is_All_You_Need_analysis.md` |
| Multi-paper | `[Topic]_synthesis.md` | `Transformer_Efficiency_synthesis.md` |
| Survey | `[Topic]_survey.md` | `MLLM_LVLM_survey.md` |
| Quick brief | `[Paper_Title]_brief.md` | `BERT_brief.md` |

**File writing procedure** — survey reports are always > 150 lines; use chunked writing:

```
STEP A: Plan the full content in memory first. Do NOT write partial content.
        Estimate total lines. For a survey of 8 papers: ~500–700 lines.

STEP B: Write the first chunk (header + executive summary + intro, ≤ 50 lines)
        Tool: Write
        file_path: [output_dir]/[filename].md
        content: [first 50 lines]

STEP C: For each subsequent chunk (50 lines max per Edit call):
        Tool: Edit
        file_path: [output_dir]/[filename].md
        old_string: [EXACT last 3 lines of the current file content]
        new_string: [those same 3 lines] + "\n" + [next 50 lines of new content]

        CRITICAL: old_string must match the file EXACTLY (character for character).
        Use the last 3 lines of the previously written content as the anchor.
        Never use a line that contains special regex characters as the anchor
        if it might not match exactly — use a plain text line instead.

STEP D: After all chunks are written, verify the file exists and has content.
```

**Example anchor technique for Edit appends:**

If the file currently ends with:
```
...
## 3. Cross-Paper Synthesis

### 3.1 Research Themes
```

Then the Edit call is:
```
old_string: "## 3. Cross-Paper Synthesis\n\n### 3.1 Research Themes"
new_string: "## 3. Cross-Paper Synthesis\n\n### 3.1 Research Themes\n\n[next 50 lines of content]"
```

---

## File Output & Workflow

### Output File Generation

All analysis results are saved as markdown files. The system does NOT output results directly to the command line.

**Workflow**:
1. User provides paper(s) or research topic
2. System completes analysis through all 4 phases
3. System generates markdown file using the appropriate template (loaded via Read tool)
4. File is saved to the user's current working directory
5. User receives confirmation with file location and summary

### File Naming Convention

| Mode | Format | Example |
|------|--------|---------|
| Single paper | `[Paper_Title]_analysis.md` | `Attention_Is_All_You_Need_analysis.md` |
| Multi-paper | `[Topic]_synthesis.md` | `Transformer_Efficiency_synthesis.md` |
| Survey | `[Topic]_survey.md` | `MLLM_LVLM_survey.md` |
| Quick brief | `[Paper_Title]_brief.md` | `BERT_brief.md` |

Use underscores instead of spaces. Keep filenames ASCII-safe (no Chinese characters in filename).

### Output Confirmation

After file generation, provide:

```
✅ Analysis Complete

📄 File: MLLM_LVLM_survey.md
📊 Papers analyzed: 8
📋 Sections: Executive Summary, Research Landscape (Technical Routes), 8× Paper Analysis (10-point),
             Cross-Paper Insights (Evolution Analysis), Critical Analysis, Emerging Directions,
             Future Directions (Evidence-Based), References
🔗 Saved to: [full path]
```

### Tool Usage Standards

**Write Tool**: Creates the file. Use for the first chunk (≤ 50 lines).

**Edit Tool**: Appends content. Use for all subsequent chunks (≤ 50 lines each).
- `old_string` must be the exact last 3 lines of the current file
- `new_string` = those same 3 lines + new content
- Never use a line with special characters as the anchor if it might not match exactly

**File size estimates**:

| Type | Papers | Est. Lines | Write calls | Edit calls |
|------|--------|-----------|-------------|------------|
| Quick Brief | 1 | ~60 | 1 | 0 |
| Single Paper | 1 | ~150 | 1 | 2 |
| Multi-Paper | 3 | ~270 | 1 | 5 |
| Survey | 8 | ~800 | 1 | 15 |
| Large Survey | 10 | ~1000 | 1 | 19 |

---

## Quality Standards

These standards apply to all outputs:

1. ⚠️ **IRON RULE**: **Every claim must have a citation** — no unsupported assertions
2. **Evidence hierarchy** — Peer-reviewed papers > preprints > technical reports
3. **Contradiction disclosure** — If sources disagree, report both sides with evidence quality comparison
4. **Limitation transparency** — Every analysis must include explicit limitations section
5. **AI disclosure** — All reports include a statement that AI-assisted research tools were used
6. **Reproducibility** — Analysis methodology and data sources must be documented
7. **Actionability** — Insights must be specific and actionable for follow-up research

---

## Anti-Patterns (What NOT to Do)

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **Vague paper summary** | Copying abstract without deep analysis | Provide structured analysis per framework |
| 2 | **Missing innovation analysis** | Not clearly identifying what is novel | Explicitly compare with existing methods |
| 3 | **Incomplete limitation discussion** | Only mentioning minor limitations | Analyze method, experimental, and theoretical limitations |
| 4 | **No actionable insights** | Generic observations without specificity | Provide concrete implications for follow-up research |
| 5 | **Unsupported claims** | Making assertions without evidence | Every claim must reference the paper or related work |
| 6 | **Shallow experimental analysis** | Only reporting numbers without interpretation | Analyze why results improved and what they mean |
| 7 | **Missing context** | Not explaining why the problem matters | Always include research motivation and significance |
| 8 | **Paper-centric organization** | Organizing survey as "Paper A, Paper B, Paper C" | Organize around core research questions; papers serve as evidence |
| 9 | **Missing Research Landscape** | No technical route overview before per-paper analysis | Build Research Landscape first: core problems → technical routes → representative papers |
| 10 | **Module description instead of design rationale** | §5 "Why It Works" just lists modules | Analyze WHY the design resolves a specific bottleneck; explain the key insight enabling the improvement |
| 11 | **Missing evolution analysis** | States "GNN → Transformer" without explaining why | For each paradigm shift, analyze cause: performance bottleneck, scale change, compute shift, etc. |
| 12 | **Uncritical acceptance of all papers** | Treats all reported results as valid | Apply Critical Analysis: flag contradictions, benchmark bias, hype vs evidence |
| 13 | **Time-blind survey** | Survey dominated by 2018–2022 papers for a fast-moving field | For fast-evolving fields, ≥ 30% from 2025–2026; include latest top-conference + arXiv work |
| 14 | **Survey-heavy paper selection** | > 10% surveys as core analysis objects | Surveys ≤ 10%; prioritize Method Papers ≥ 60%; surveys for background only |
| 15 | **Generic future directions** | "Improve performance", "improve efficiency" | Derive each direction from: Bottleneck → Why Methods Fail → Specific Future Direction |

---

## Troubleshooting Guide

### Issue: "No papers found for query"

**Symptoms:**
```
No papers found for query: [topic]
```

**Causes:**
- Search keywords not specific enough
- Paper too new (< 1 week) or too old
- Paper not in Semantic Scholar database

**Solutions:**
1. Try more specific keywords
   - ❌ Bad: "machine learning"
   - ✅ Good: "transformer attention mechanism 2024"

2. Try using DOI or arXiv ID directly
   - DOI: `10.1145/3495530.3495531`
   - arXiv: `2106.14881`

3. Use manual input mode
   - Provide paper title, authors, year, etc.
   - System will verify and analyze

### Issue: "Paper verification failed"

**Symptoms:**
```
Paper verification failed
Citation count: N/A
```

**Causes:**
- Semantic Scholar API cannot find paper
- Paper title spelling error
- Paper too new or too old

**Solutions:**
1. Check paper title spelling
   - Use official title
   - Avoid abbreviations or simplifications

2. Provide DOI or arXiv ID
   - System uses these identifiers for verification
   - Higher success rate

3. Use manual input mode
   - Skip verification step
   - Proceed directly to analysis

### Issue: "API rate limit exceeded"

**Symptoms:**
```
Error 429: Too Many Requests
```

**Root cause:** Semantic Scholar's public API has a strict per-second rate limit. Sending multiple queries concurrently (as parallel tool calls) almost always triggers 429 for all of them simultaneously.

**Immediate action — switch to arXiv Direct Fallback:**

1. **Stop all pending API queries** — do not retry the same URLs
2. **Switch to Step 1c arXiv Direct Fallback** immediately:
   - Use domain knowledge to list landmark arXiv IDs for the topic
   - Fetch each via `https://arxiv.org/abs/{arxiv_id}` **one at a time**
   - Extract references from HTML pages to discover additional papers
3. **Carry forward any results** already received before the 429 hit

**Prevention (apply before starting any survey):**
- Always call Semantic Scholar API queries **sequentially** (one at a time), never in parallel
- The extra latency per query (~2–5s) is acceptable; a full 429 failure wastes far more time

**Optional — Get a Semantic Scholar API key** (increases rate limit 10×):
- Visit: https://www.semanticscholar.org/product/api
- Register and obtain an API key
- Pass as HTTP header: `x-api-key: {key}` — note this requires WebFetch to support custom headers (environment-dependent)

### Issue: "Manual input mode"

When Semantic Scholar API is slow or cannot find paper:

```markdown
Please provide the following information:

**Paper 1**:
- Title: Attention Is All You Need
- Authors: Ashish Vaswani, Noam Shazeer, et al.
- Year: 2017
- Venue: NeurIPS 2017
- DOI: 10.5555/3295222.3295349
- arXiv: 1706.03762
- Abstract: [Paper abstract]

**Paper 2**:
- ...
```

System will use this information for analysis and attempt verification via Semantic Scholar API.

---

## Reference Materials

Use these guides to support analysis:

| Reference | Purpose |
|-----------|---------|
| `references/paper_analysis_framework.md` | Detailed methodology for 7-point framework |
| `references/innovation_assessment_guide.md` | How to evaluate innovation |
| `references/research_implications_guide.md` | How to extract insights |
| `references/semantic_scholar_api_guide.md` | Semantic Scholar API integration |
| `references/apa7_style_guide.md` | APA 7th edition quick reference |
| `references/source_quality_hierarchy.md` | Evidence pyramid + grading rubric |

---

## Templates

Use appropriate template for each mode:

| Template | Purpose |
|----------|---------|
| `templates/paper_analysis_template.md` | Single paper analysis |
| `templates/multi_paper_synthesis_template.md` | Multi-paper comparison |
| `templates/survey_report_template.md` | Literature survey |
| `templates/quick_brief_template.md` | Quick overview |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/single_paper_analysis.md` | Deep analysis of one paper |
| `examples/multi_paper_synthesis.md` | Comparative analysis of multiple papers |
| `examples/survey_report.md` | Comprehensive literature survey |
| `examples/quick_brief.md` | Quick paper overview |

---

## Integration with Other Skills

This skill is **self-sufficient** for literature research — it does not require `deep-research` or `web-access` to function. WebSearch and WebFetch are used directly in Phase 2.

It complements the academic writing suite:

```
academic-literature-research  →  academic-paper         (research findings → write paper)
academic-literature-research  →  academic-paper-reviewer (analyze papers → peer review)
```

**Recommended workflow:**
1. Use this skill to survey a research area or deep-read specific papers
2. Use `academic-paper` to write your own paper based on the findings
3. Use `academic-paper-reviewer` for structured peer review of a draft

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 3.1.0 |
| Last Updated | 2026-06-14 |
| Status | Active — self-sufficient (WebSearch + WebFetch + Semantic Scholar API) |
| Web-Access Integration | ✅ Built-in (WebSearch + WebFetch used directly) |
| Template Support | ✅ Enabled |

---

## Version History

See `references/changelog.md` for full version history.

---

**Ready to begin? Provide a paper title, DOI, URL, or research topic to start.**
