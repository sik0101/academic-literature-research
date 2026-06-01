---
type: documentation
description: "Examples directory - sample outputs demonstrating each analysis type"
---

# Examples Directory

This directory contains example outputs demonstrating each analysis type. These examples show how to use the templates and what quality output should look like.

## Example Files

### 1. `single_paper_analysis.md`
**Type**: Single Paper Analysis Example  
**Paper**: "Attention Is All You Need" (Vaswani et al., 2017)  
**Frontmatter**:
```yaml
example_type: single-paper-analysis
paper: "Attention Is All You Need"
authors: "Vaswani et al."
year: 2017
```

**Demonstrates**:
- How to structure a deep analysis of a single paper
- Application of the 7-point framework
- Proper citation and verification formatting
- Comprehensive coverage of research motivation, problem formulation, solution approach, innovations, experimental results, limitations, and implications

**Key Sections**:
- Paper metadata and identifiers
- Executive summary
- 7-point framework analysis
- Research implications and future directions

---

### 2. `quick_brief.md`
**Type**: Quick Brief Example  
**Paper**: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (Devlin et al., 2018)  
**Frontmatter**:
```yaml
example_type: quick-brief
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors: "Devlin et al."
year: 2018
```

**Demonstrates**:
- How to create a concise paper overview
- One-sentence summary format
- Quick takeaways for practitioners and researchers
- Efficient presentation of key results and limitations
- Rating system for paper quality assessment

**Key Sections**:
- One-sentence summary
- Core contribution
- Key results
- Strengths and limitations
- Quick reference ratings

---

### 3. `multi_paper_synthesis.md`
**Type**: Multi-Paper Synthesis Example  
**Topic**: "Transformer Variants and Efficiency Improvements"  
**Papers**: 3 papers (Longformer, Linformer, BigBird)  
**Year Range**: 2019-2021  
**Frontmatter**:
```yaml
example_type: multi-paper-synthesis
topic: "Transformer Variants and Efficiency Improvements"
papers_count: 3
year_range: "2019-2021"
```

**Demonstrates**:
- How to compare and synthesize multiple papers
- Identification of common themes across papers
- Reconciliation of contradictions
- Comparative analysis tables
- Cross-paper synthesis methodology

**Key Sections**:
- Executive summary
- Individual paper summaries
- Comparative analysis
- Thematic synthesis
- Contradictions and reconciliation
- Research gaps and future directions

---

### 4. `survey_report.md`
**Type**: Literature Survey Example  
**Topic**: "Vision Transformers and Visual Recognition"  
**Papers**: 3 key papers (representative sample)  
**Time Period**: 2020-2021  
**Frontmatter**:
```yaml
example_type: literature-survey
topic: "Vision Transformers and Visual Recognition"
papers_count: 3
year_range: "2020-2021"
```

**Demonstrates**:
- How to structure a comprehensive literature survey
- Application of 7-point framework to multiple papers
- Research landscape overview
- Identification of major research gaps
- Recommendations for future research directions
- Proper APA 7.0 citation formatting

**Key Sections**:
- Executive summary
- Introduction and scope
- Key papers analysis (7-point framework)
- Cross-paper synthesis
- Research landscape overview
- Research gaps and future directions
- Conclusion and references

---

## Frontmatter Standard

All examples include YAML frontmatter with the following fields:

```yaml
---
example_type: [single-paper-analysis | quick-brief | multi-paper-synthesis | literature-survey]
paper: "[Paper title]" (for single-paper and quick-brief)
topic: "[Topic]" (for multi-paper and survey)
authors: "[Author names]" (for single-paper and quick-brief)
year: [Year] (for single-paper and quick-brief)
papers_count: [Number] (for multi-paper and survey)
year_range: "[Start-End]" (for survey)
---
```

---

## How to Use These Examples

### 1. As Learning Resources
- Study the structure and organization
- Understand how to apply the 7-point framework
- Learn proper citation and verification formatting
- See how to synthesize findings across papers

### 2. As Templates for Your Own Work
- Copy the structure for your analysis
- Replace content with your own papers and findings
- Maintain the same level of detail and rigor
- Follow the same citation standards

### 3. As Quality Benchmarks
- Compare your output to these examples
- Ensure similar depth of analysis
- Verify proper use of evidence hierarchy
- Check for actionable insights

---

## Quality Standards Demonstrated

All examples follow these quality standards:

1. ✅ **Every claim has a citation** — All assertions are grounded in source papers
2. ✅ **Evidence hierarchy respected** — Peer-reviewed sources prioritized
3. ✅ **Contradictions disclosed** — Disagreements between sources are noted
4. ✅ **Limitations explicitly stated** — Each analysis includes limitations section
5. ✅ **AI disclosure included** — Statement about AI-assisted analysis
6. ✅ **Reproducibility documented** — Methodology and sources are clear
7. ✅ **Actionable insights provided** — Implications are specific and useful

---

## Mapping to Templates

| Example | Template | Relationship |
|---------|----------|--------------|
| `single_paper_analysis.md` | `../templates/paper_analysis_template.md` | Filled-in example |
| `quick_brief.md` | `../templates/quick_brief_template.md` | Filled-in example |
| `multi_paper_synthesis.md` | `../templates/multi_paper_synthesis_template.md` | Filled-in example |
| `survey_report.md` | `../templates/survey_report_template.md` | Filled-in example |

---

## Related Files

- `../templates/` — Template files for each analysis type
- `../SKILL.md` — Main skill documentation
- `../references/` — Reference materials for analysis

---

**Last Updated**: 2026-05-29  
**Version**: 1.0
