---
name: academic-literature-research
description: "Deep academic literature research and paper analysis skill. Specialized for systematic literature review, paper deep-reading, and technical research in academic and technology domains. Triggers on: literature review, read paper, paper analysis, research survey, literature survey, 文献调研, 论文阅读, 论文分析, 研究综述, 技术调研. Provides comprehensive paper analysis including: research motivation, problem formulation, solution approach, innovation points, experimental validation, limitations, and research implications. Generates structured reports with APA 7.0 citations and actionable insights for follow-up research."
metadata:
  version: "2.0.0"
  last_updated: "2026-06-01"
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
4. **Analysis** — Apply 7-point framework to each paper's content
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
| **Analysis** | Apply 7-point framework to each paper | (reasoning only) | all modes |
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

Collect all results across all queries. Deduplicate by title similarity (threshold: 0.85 — same paper if titles are >85% similar).

**1c. WebSearch fallback (when API returns < 3 results for a query)**

"< 3 results" means fewer than 3 papers with non-empty abstracts after deduplication. Use WebSearch with these patterns:
- `site:arxiv.org {query}` — finds arXiv preprints
- `{query} paper {year1} OR {year2} site:semanticscholar.org` — finds indexed papers
- `"{core topic}" survey OR review` — finds survey papers

From WebSearch results, extract paper titles and URLs. For each title found, verify via Semantic Scholar API (WebFetch as above) to get full metadata.

**1d. Screen and rank candidates**

Apply screening criteria in order:
1. Title must contain topic keywords or close synonyms
2. Abstract must address the core research problem (not just mention it tangentially)
3. **Time period filter**: exclude papers published outside the user's specified range (e.g., exclude year < 2022 or year > 2026). Apply this strictly.
4. Venue quality: top-tier conference/journal > workshop > arXiv > other
5. Citation count: ≥ 10 for survey mode (waive for papers < 1 year old, i.e., published in 2025–2026)

Select final paper set:
- Survey mode: 5–10 papers covering different sub-topics and time periods within the user's range
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

Conduct structured analysis of each paper using the 7-point framework.

#### 7-Point Deep Analysis Framework

For each paper, analyze using these 7 dimensions:

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
1. Apply 7-point framework to each paper with these survey-specific adjustments:
   - **Omit** the "Connection to Your Research" sub-section from §7 (Research Implications) — replace with "Significance for the Research Field" instead
   - For `abstract_only` papers: mark §3 and §5 as limited; still complete §1, §2, §4, §6, §7 from abstract
2. Conduct comprehensive cross-paper synthesis:
   - Synthesize findings across all papers
   - Identify research trends and patterns
   - Map research landscape
   - Highlight emerging directions
3. Create thematic analysis sections
4. Analyze methodological approaches
5. Identify major research gaps
6. Recommend future research directions

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
   - 2-3 paragraph overview of findings

3. Introduction & Scope
   - Research area definition
   - Survey rationale
   - Survey methodology

4. Key Papers Analysis (7-point framework for each paper)
   - PAPER 1: [Title]
     - Paper Identifiers & Links
     - 1. Research Motivation
     - 2. Problem Formulation
     - 3. Solution Approach
     - 4. Innovation Points
     - 5. Experimental Results
     - 6. Limitations
     - 7. Research Implications
   - PAPER 2: [Title]
     - [Same 7-point structure]
   - PAPER 3: [Title]
     - [Same 7-point structure]

5. Cross-Paper Synthesis & Thematic Analysis
   - Research themes
   - Methodological synthesis
   - Theoretical frameworks

6. Research Landscape Overview
   - Publication trends
   - Research paradigms

7. Research Gaps & Future Directions
   - Major gaps identified
   - Recommended future research directions

8. Conclusion
   - Summary of key findings
   - Implications for practice
   - Implications for future research

9. References
   - APA 7.0 formatted citations

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
📋 Sections: Executive Summary, 8× Paper Analysis (7-point), Cross-Paper Synthesis,
             Research Landscape, Gaps & Future Directions, Conclusion, References
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
| Survey | 8 | ~500 | 1 | 9 |
| Large Survey | 10 | ~650 | 1 | 12 |

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

**Causes:**
- Too many requests in short time
- Semantic Scholar API rate limit

**Solutions:**
1. Wait 2-5 seconds and retry

2. Get Semantic Scholar API key
   - Visit: https://www.semanticscholar.org/product/api
   - Register account and get API key
   - Rate limit increases 10x

3. Use caching
   - Avoid duplicate queries
   - System auto-caches results

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
| `examples/literature_survey.md` | Comprehensive literature survey |
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
| Skill Version | 2.0.0 |
| Last Updated | 2026-06-01 |
| Status | Active — self-sufficient (WebSearch + WebFetch + Semantic Scholar API) |
| Web-Access Integration | ✅ Built-in (WebSearch + WebFetch used directly) |
| Template Support | ✅ Enabled |

---

## Version History

See `references/changelog.md` for full version history.

---

**Ready to begin? Provide a paper title, DOI, URL, or research topic to start.**
