---
type: documentation
description: "Templates directory - standardized formats for academic literature analysis"
---

# Templates Directory

This directory contains standardized templates for academic literature analysis outputs. All templates follow a consistent format with YAML frontmatter and structured markdown sections.

## Template Files

### 1. `paper_analysis_template.md`
**Type**: Single Paper Analysis  
**Use Case**: Deep analysis of a single paper using the 7-point framework  
**Output Length**: 2,000-4,000 words  
**Frontmatter**:
```yaml
template_type: single-paper-analysis
version: "1.0"
description: "Deep analysis of a single paper using 7-point framework"
```

**Key Sections**:
- Paper Identifiers & Links
- Executive Summary
- 7-Point Framework Analysis:
  1. Research Motivation & Background
  2. Problem Formulation
  3. Solution Approach
  4. Innovation Points
  5. Experimental Results
  6. Limitations
  7. Research Implications

---

### 2. `multi_paper_synthesis_template.md`
**Type**: Multi-Paper Synthesis  
**Use Case**: Comparative analysis and synthesis of 2-5 papers  
**Output Length**: 3,000-6,000 words  
**Frontmatter**:
```yaml
template_type: multi-paper-synthesis
version: "1.0"
description: "Comparative analysis and synthesis of 2-5 papers"
```

**Key Sections**:
- Executive Summary
- Individual Paper Summaries
- Comparative Analysis (Research Questions, Methodology, Findings, Frameworks)
- Thematic Synthesis
- Contradictions & Reconciliation
- Research Gaps & Future Directions
- Implications & Applications
- Conclusion

---

### 3. `survey_report_template.md`
**Type**: Literature Survey  
**Use Case**: Comprehensive review of a research area (5-10 papers)  
**Output Length**: 4,000-8,000 words  
**Frontmatter**:
```yaml
template_type: literature-survey
version: "1.0"
description: "Comprehensive literature survey of a research area (5-10 papers)"
```

**Key Sections**:
- Executive Summary
- Introduction & Scope
- Key Papers Analysis (7-point framework for each paper)
- Cross-Paper Synthesis & Thematic Analysis
- Research Landscape Overview
- Research Gaps & Future Directions
- Conclusion
- References
- AI Disclosure Statement

---

### 4. `quick_brief_template.md`
**Type**: Quick Brief  
**Use Case**: Fast overview of a paper  
**Output Length**: 800-1,500 words  
**Frontmatter**:
```yaml
template_type: quick-brief
version: "1.0"
description: "Quick paper overview (800-1,500 words)"
```

**Key Sections**:
- One-Sentence Summary
- Core Contribution
- Key Results
- Strengths
- Limitations
- Who Should Read This
- Quick Takeaways
- Related Work
- Bottom Line
- Quick Reference (Rating Table)

---

## Frontmatter Standard

All templates include YAML frontmatter with the following fields:

```yaml
---
template_type: [single-paper-analysis | multi-paper-synthesis | literature-survey | quick-brief]
version: "1.0"
description: "Brief description of the template"
---
```

**Fields**:
- `template_type`: Identifies the analysis type
- `version`: Template version (currently 1.0)
- `description`: One-line description of the template's purpose

---

## Usage Guidelines

### When to Use Each Template

| Situation | Template | Output |
|-----------|----------|--------|
| Analyzing one specific paper | `paper_analysis_template.md` | 2,000-4,000 words |
| Comparing 2-5 papers | `multi_paper_synthesis_template.md` | 3,000-6,000 words |
| Reviewing a research area | `survey_report_template.md` | 4,000-8,000 words |
| Quick paper overview | `quick_brief_template.md` | 800-1,500 words |

### Template Customization

Templates are designed to be flexible:
- Replace `[Placeholder]` text with actual content
- Add or remove subsections as needed
- Maintain the overall structure and frontmatter
- Keep the 7-point framework for single-paper and survey modes

### Quality Standards

All outputs using these templates must meet:
1. ✅ Every claim has a citation
2. ✅ Evidence hierarchy respected (peer-reviewed > preprint > report)
3. ✅ Contradictions disclosed with evidence quality comparison
4. ✅ Limitations explicitly stated
5. ✅ AI disclosure statement included
6. ✅ Reproducibility documented
7. ✅ Actionable insights provided

---

## Related Files

- `../examples/` — Example outputs using these templates
- `../SKILL.md` — Main skill documentation
- `../references/` — Reference materials for analysis

---

**Last Updated**: 2026-05-29  
**Version**: 1.0
