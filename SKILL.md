---
name: academic-literature-research
description: "Deep academic literature research and paper analysis skill. Specialized for systematic literature review, paper deep-reading, and technical research in academic and technology domains. Triggers on: literature review, read paper, paper analysis, research survey, literature survey, 文献调研, 论文阅读, 论文分析, 研究综述, 技术调研. Provides comprehensive paper analysis including: research motivation, problem formulation, solution approach, innovation points, experimental validation, limitations, and research implications. Generates structured reports with APA 7.0 citations and actionable insights for follow-up research."
metadata:
  version: "1.0.0"
  last_updated: "2026-05-29"
  status: active
  data_access_level: raw
  task_type: open-ended
  related_skills:
    - deep-research
    - academic-paper
    - academic-pipeline
---

# Academic Literature Research — Deep Paper Analysis & Literature Review

Specialized skill for rigorous academic literature research and paper analysis in academic and technology domains.

**Core Purpose**: Transform raw papers and research topics into structured, actionable literature analysis with deep insights for follow-up research.

## Quick Start

**Single paper deep-read:**
```
深度阅读这篇论文：[论文标题或链接]
```

**Literature survey:**
```
调研关于[研究方向]的最新文献
```

**Technical research:**
```
我需要了解[技术领域]的研究现状和发展方向
```

---

## Trigger Conditions

### Trigger Keywords

**English**: literature review, read paper, paper analysis, research survey, literature survey, deep read, paper deep-dive, technical research, research landscape, state of the art, SOTA, systematic literature review

**中文**: 文献调研, 论文阅读, 论文分析, 研究综述, 技术调研, 深度阅读, 文献综述, 研究现状, 技术现状, 发展方向

### Intent Signals

Activate this skill when the user's **intent** matches any of the following patterns:

1. User wants to understand a specific paper in depth
2. User wants to survey literature in a research area
3. User wants to understand the state-of-the-art in a technical domain
4. User wants to analyze research trends and gaps
5. User wants structured insights from multiple papers for follow-up research

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Writing a paper (not researching) | `academic-paper` |
| Reviewing a paper (structured review) | `academic-paper-reviewer` |
| Full research-to-paper pipeline | `academic-pipeline` |
| General web research (not academic) | `deep-research` |

---

## Operational Modes

| Mode | Focus | Output | Word Count |
|------|-------|--------|------------|
| `single-paper` (default) | Deep analysis of one paper | Comprehensive paper analysis report | 2,000-4,000 |
| `multi-paper` | Comparative analysis of multiple papers | Synthesis report + individual analyses | 3,000-6,000 |
| `survey` | Literature landscape in a research area | Survey report + key papers analysis | 4,000-8,000 |
| `quick-brief` | Quick overview of a paper | Brief summary + key insights | 800-1,500 |

---

## Orchestration Workflow (4 Phases)

```
User: "深度阅读这篇论文" / "调研[研究方向]"
     |
=== Phase 1: CLARIFICATION (Interactive) ===
     |
     |-> Confirm research scope and objectives
     |   - Which paper(s) to analyze?
     |   - What is the research context?
     |   - What specific aspects to focus on?
     |
     +-> User confirmation before Phase 2
     |
=== Phase 2: INVESTIGATION ===
     |
     |-> [literature_analyst_agent] -> Paper Collection & Metadata
     |   - Retrieve paper information
     |   - Verify source quality
     |   - Collect related papers (if multi-paper mode)
     |
     +-> [source_verification_agent] -> Source Grading
         - Evidence hierarchy assessment
         - Publication venue verification
         - Author credibility check
     |
=== Phase 3: ANALYSIS ===
     |
     |-> [paper_analyzer_agent] -> Structured Paper Analysis
     |   - Research motivation & background
     |   - Problem formulation
     |   - Solution approach & methodology
     |   - Innovation points identification
     |   - Experimental validation analysis
     |   - Limitations & constraints
     |   - Research implications & insights
     |
     +-> [synthesis_agent] -> Cross-Paper Synthesis (if multi-paper)
         - Thematic synthesis
         - Contradiction identification
         - Research gap analysis
     |
=== Phase 4: COMPOSITION ===
     |
     +-> [report_compiler_agent] -> Final Analysis Report
         - Executive Summary
         - Paper Analysis (per template)
         - Comparative Analysis (if multi-paper)
         - Research Implications
         - Recommendations for Follow-up Research
         - References (APA 7.0)
```

---

## Paper Analysis Framework

Every paper analysis includes systematic examination of:

### 1. Research Motivation & Background
- **Why this problem?** — Practical and academic significance
- **Current limitations** — What existing methods cannot do
- **Research gap** — What is missing in the field

### 2. Problem Formulation
- **Clear problem statement** — Input, output, task objective
- **Scope boundaries** — In-scope vs. out-of-scope
- **Evaluation criteria** — How success is measured

### 3. Solution Approach
- **Core idea** (one-sentence summary)
- **Overall framework** — Data flow and architecture
- **Technical modules** — Each component's role and implementation
- **Innovation points** — What is novel compared to existing work

### 4. Experimental Validation
- **Datasets** — Scale, characteristics, representativeness
- **Baselines** — Comparison methods and their categories
- **Results analysis** — Performance improvements and their significance
- **Ablation studies** — Component contribution analysis
- **Complexity analysis** — Parameters, time/space complexity, inference speed

### 5. Strengths Analysis
- **Theoretical soundness** — Mathematical rigor and clarity
- **Experimental rigor** — Comprehensive evaluation and fair comparison
- **Practical applicability** — Ease of implementation and deployment
- **Generalization capability** — Cross-domain and cross-dataset performance

### 6. Limitations & Constraints
- **Method limitations** — Complexity, dependencies, scalability issues
- **Experimental limitations** — Dataset bias, incomplete baselines
- **Theoretical gaps** — Missing proofs or analysis
- **Generalization challenges** — Domain-specific constraints

### 7. Research Implications & Insights
- **Implications for the field** — How this work advances the research area
- **Potential improvements** — Future research directions
- **Transferability** — Which modules/ideas can be applied to other problems
- **Connection to your research** — Relevance and applicability

---

## Report Structure

```
# [Paper Title]

## Executive Summary
- One-paragraph overview of the paper's contribution

## 1. Research Motivation & Background
### 1.1 Research Field
### 1.2 Research Problem
### 1.3 Problem Significance

## 2. Related Work & Current Limitations
### 2.1 Existing Approaches Classification
### 2.2 Limitations of Existing Methods

## 3. Core Contribution
### 3.1 Core Idea (One-Sentence Summary)
### 3.2 Overall Framework
### 3.3 Technical Modules
### 3.4 Innovation Points

## 4. Experimental Analysis
### 4.1 Datasets
### 4.2 Baselines
### 4.3 Results Analysis
### 4.4 Ablation Studies
### 4.5 Complexity Analysis

## 5. Strengths Analysis
### 5.1 Theoretical Level
### 5.2 Experimental Level
### 5.3 Engineering Level

## 6. Limitations & Constraints
### 6.1 Method Level
### 6.2 Experimental Level
### 6.3 Theoretical Level
### 6.4 Generalization Challenges

## 7. Research Implications & Insights
### 7.1 Implications for the Field
### 7.2 Potential Improvements
### 7.3 Transferability to Other Problems
### 7.4 Connection to Your Research

## 8. Summary & Recommendations
- Concise summary of the paper
- Recommendations for follow-up research

## References
- APA 7.0 formatted citations
```

---

## Quality Standards

1. ⚠️ **IRON RULE**: **Every claim must have a citation** — no unsupported assertions
2. **Evidence hierarchy** — Peer-reviewed papers > preprints > technical reports
3. **Contradiction disclosure** — If sources disagree, report both sides with evidence quality comparison
4. **Limitation transparency** — Every analysis must include explicit limitations section
5. **AI disclosure** — All reports include a statement that AI-assisted research tools were used
6. **Reproducibility** — Analysis methodology and data sources must be documented
7. **Actionability** — Insights must be specific and actionable for follow-up research

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes:

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

## Integration with Other Skills

This skill complements the academic research suite:

```
academic-literature-research (single-paper/survey)
  → deep-research (full mode)
    → academic-paper (plan/full)
      → academic-paper-reviewer (full/guided)
        → academic-paper (revision)
          → final output
```

**Handoff to deep-research**: After analyzing key papers, use deep-research for comprehensive literature review and synthesis.

**Handoff to academic-paper**: After understanding the research landscape, use academic-paper to write your own paper.

---

## Output Language

Follows the user's language. Academic terminology kept in English. Analysis uses natural, clear language suitable for researchers.

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 1.0.0 |
| Last Updated | 2026-05-29 |
| Based On | deep-research v2.9.4 |
| Related Skills | deep-research, academic-paper, academic-pipeline |

---

## Reference Files

| Reference | Purpose |
|-----------|---------|
| `references/paper_analysis_framework.md` | Detailed paper analysis methodology |
| `references/apa7_style_guide.md` | APA 7th edition quick reference |
| `references/source_quality_hierarchy.md` | Evidence pyramid and grading rubric |
| `references/innovation_assessment_guide.md` | How to identify and evaluate innovation |
| `references/research_implications_guide.md` | How to extract actionable insights |

---

## Templates

| Template | Purpose |
|----------|---------|
| `templates/paper_analysis_template.md` | Single paper analysis template |
| `templates/multi_paper_synthesis_template.md` | Multi-paper synthesis template |
| `templates/survey_report_template.md` | Literature survey report template |
| `templates/quick_brief_template.md` | Quick paper brief template |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/single_paper_analysis.md` | Complete single paper analysis walkthrough |
| `examples/multi_paper_synthesis.md` | Comparative analysis of multiple papers |
| `examples/survey_report.md` | Literature survey in a research area |
| `examples/quick_brief.md` | Quick paper overview |
