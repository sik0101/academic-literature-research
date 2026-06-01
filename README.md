# Academic Literature Research Skill

A self-sufficient Claude Code skill for deep academic literature research and paper analysis. No external skills required.

## Overview

**Academic Literature Research** helps researchers systematically analyze papers and conduct literature reviews. It uses WebSearch, WebFetch, and the Semantic Scholar API directly — no dependency on `web-access` or `deep-research` skills.

### Key Features

- **Deep Paper Analysis**: 7-point structured framework covering motivation, problem, solution, innovation, results, limitations, and implications
- **Multi-Paper Synthesis**: Comparative analysis of 2–5 papers
- **Literature Surveys**: Comprehensive review of a research area (5–10 papers)
- **Quick Briefs**: Fast paper overviews
- **Self-Sufficient Search**: Discovers papers via Semantic Scholar API + WebSearch fallback
- **Content Retrieval**: Fetches paper content from arXiv and DOI pages via WebFetch
- **APA 7.0 Citations**: All reports include properly formatted references

## When to Use

Use this skill when you need to:

- **Understand a specific paper deeply** — comprehensive analysis of motivation, methodology, contributions, and implications
- **Survey a research area** — understand the state-of-the-art and research landscape
- **Compare multiple papers** — analyze similarities, differences, and complementary contributions
- **Extract research insights** — identify actionable insights and future research directions

### Trigger Keywords

**English**: literature review, read paper, paper analysis, research survey, literature survey, deep read, analyze paper, survey literature

**中文**: 文献调研, 论文阅读, 论文分析, 研究综述, 深度阅读, 分析论文, 调研文献

## Operational Modes

| Mode | Output | Use When |
|------|--------|----------|
| `single-paper` | 2,000–4,000 words | Thoroughly understand one specific paper |
| `multi-paper` | 3,000–6,000 words | Compare approaches across 2–5 papers |
| `survey` | 4,000–8,000 words | Understand a research area's landscape |
| `quick-brief` | 800–1,500 words | Quick overview without deep analysis |

## Paper Analysis Framework (7-Point)

Every paper analysis covers:

1. **Research Motivation** — why the problem matters, research gaps
2. **Problem Formulation** — precise problem statement, challenges, metrics
3. **Solution Approach** — core idea, architecture, key algorithms
4. **Innovation Points** — what is novel and why it matters
5. **Experimental Results** — datasets, baselines, quantitative findings
6. **Limitations** — method, experimental, and theoretical constraints
7. **Research Implications** — field significance, potential improvements, future directions

## Quick Start

```
# Single paper
Deep read this paper: Attention Is All You Need

# Literature survey
Survey literature on transformer architectures

# With mode and time period pre-specified
使用 survey 模式调研：近年（2022–2026）多模态大模型研究方向
```

The skill detects pre-specified parameters (mode, topic, time period, language) and skips redundant questions.

## File Structure

```
academic-literature-research/
├── SKILL.md                              # Main skill definition (v2.0.0)
├── README.md                             # This file
├── references/
│   ├── paper_analysis_framework.md       # 7-point analysis methodology
│   ├── innovation_assessment_guide.md    # How to evaluate innovation
│   ├── research_implications_guide.md    # How to extract insights
│   ├── semantic_scholar_api_guide.md     # Semantic Scholar API reference
│   ├── apa7_style_guide.md               # APA 7th edition quick reference
│   └── source_quality_hierarchy.md       # Evidence pyramid + grading rubric
├── templates/
│   ├── paper_analysis_template.md        # Single paper template
│   ├── multi_paper_synthesis_template.md # Multi-paper template
│   ├── survey_report_template.md         # Survey template
│   └── quick_brief_template.md           # Quick brief template
└── examples/
    ├── single_paper_analysis.md
    ├── multi_paper_synthesis.md
    ├── survey_report.md
    └── quick_brief.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/sik0101/academic-literature-research.git

# Copy to Claude Code skills directory
# macOS/Linux
cp -r academic-literature-research ~/.claude/skills/

# Windows
xcopy academic-literature-research %USERPROFILE%\.claude\skills\ /E /I
```

Restart Claude Code after installation.

## Integration with Other Skills

This skill is **self-sufficient** — it does not require `deep-research` or `web-access` to function.

It complements the academic writing suite:

| Skill | Use After This Skill |
|-------|---------------------|
| `academic-paper` | Write your own paper based on survey findings |
| `academic-paper-reviewer` | Peer review of a draft paper |

## Quality Standards

1. Every claim is supported by the source paper
2. Limitations are explicitly discussed for every paper
3. All reports include APA 7.0 formatted references
4. AI disclosure statement included in every output
5. Content level (`full_text` / `abstract_only`) is transparently marked

## Version History

### v2.0.0 (2026-06-01)
- Self-sufficient architecture: WebSearch + WebFetch + Semantic Scholar API (no external skill dependencies)
- Research Architect Agent for paper discovery in survey/multi-paper modes
- Content Retrieval Agent with 5-tier fallback for fetching paper content
- Phase 1 fast-path: detects pre-specified parameters, skips redundant questions
- Time period filter applied to search queries and screening
- 7-point framework adapted for `abstract_only` content level
- Output language matches user's request language
- Fixed Edit tool append technique for large file writing

### v1.0.0 (2026-05-29)
- Initial release with single paper, multi-paper, survey, and quick-brief modes
- Semantic Scholar API integration for paper verification

## License

CC-BY-NC 4.0. See LICENSE file for details.

---

**Last Updated**: 2026-06-01  
**Version**: 2.0.0  
**Status**: Active
