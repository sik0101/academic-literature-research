# Academic Literature Research Skill

A specialized Claude Code skill for deep academic literature research and paper analysis in academic and technology domains.

## Overview

**Academic Literature Research** is a comprehensive skill designed to help researchers systematically analyze papers and conduct literature reviews. It provides structured frameworks for understanding research papers, identifying innovations, and extracting actionable insights for follow-up research.

### Key Features

- **Deep Paper Analysis**: Systematic analysis of research papers using a comprehensive framework
- **Multi-Paper Synthesis**: Comparative analysis and synthesis of multiple papers
- **Literature Surveys**: Comprehensive literature review in specific research areas
- **Quick Briefs**: Fast paper overviews for quick understanding
- **Structured Reports**: APA 7.0 formatted reports with actionable insights
- **Innovation Assessment**: Systematic evaluation of research contributions
- **Research Implications**: Extraction of theoretical, practical, and methodological implications

## When to Use This Skill

Use this skill when you need to:

- **Understand a specific paper deeply** — Get comprehensive analysis of research motivation, methodology, contributions, and implications
- **Survey literature in a research area** — Understand the state-of-the-art and research landscape
- **Compare multiple papers** — Analyze similarities, differences, and complementary contributions
- **Extract research insights** — Identify actionable insights and future research directions
- **Assess research innovations** — Evaluate novelty and significance of research contributions

### Trigger Keywords

**English**: literature review, read paper, paper analysis, research survey, literature survey, deep read, paper deep-dive, technical research, research landscape, state of the art

**中文**: 文献调研, 论文阅读, 论文分析, 研究综述, 技术调研, 深度阅读, 文献综述, 研究现状, 技术现状

## Operational Modes

### 1. Single Paper Analysis (Default)
Deep analysis of a single paper with comprehensive coverage of all aspects.

**Output**: 2,000-4,000 words structured report

**Use when**: You want to thoroughly understand a specific paper

### 2. Multi-Paper Synthesis
Comparative analysis of multiple papers with synthesis of key findings.

**Output**: 3,000-6,000 words synthesis report + individual analyses

**Use when**: You want to compare approaches or understand different perspectives

### 3. Literature Survey
Comprehensive literature review in a specific research area.

**Output**: 4,000-8,000 words survey report + key papers analysis

**Use when**: You want to understand the research landscape and trends

### 4. Quick Brief
Fast overview of a paper with key insights.

**Output**: 800-1,500 words brief summary

**Use when**: You need a quick understanding without deep analysis

## Paper Analysis Framework

Every paper analysis includes systematic examination of:

1. **Research Motivation & Background**
   - Why this problem matters
   - Current limitations of existing approaches
   - Research gap and significance

2. **Problem Formulation**
   - Clear problem statement
   - Input, output, and task objectives
   - Scope boundaries

3. **Solution Approach**
   - Core idea and overall framework
   - Technical modules and their roles
   - Innovation points

4. **Experimental Validation**
   - Datasets and baselines
   - Results analysis and improvements
   - Ablation studies and complexity analysis

5. **Strengths Analysis**
   - Theoretical soundness
   - Experimental rigor
   - Practical applicability

6. **Limitations & Constraints**
   - Method limitations
   - Experimental limitations
   - Generalization challenges

7. **Research Implications & Insights**
   - Implications for the field
   - Potential improvements
   - Transferability to other problems
   - Connection to your research

## Report Structure

All reports follow a consistent structure:

```
# [Paper Title]

## Executive Summary

## 1. Research Motivation & Background
### 1.1 Research Field
### 1.2 Research Problem
### 1.3 Problem Significance

## 2. Related Work & Current Limitations
### 2.1 Existing Approaches Classification
### 2.2 Limitations of Existing Methods

## 3. Core Contribution
### 3.1 Core Idea
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
### 5.1 Theoretical Strengths
### 5.2 Experimental Strengths
### 5.3 Practical Strengths

## 6. Limitations & Constraints
### 6.1 Method Limitations
### 6.2 Experimental Limitations
### 6.3 Theoretical Limitations
### 6.4 Generalization Challenges

## 7. Research Implications & Insights
### 7.1 Implications for the Field
### 7.2 Potential Improvements
### 7.3 Transferability to Other Problems
### 7.4 Connection to Your Research

## 8. Summary & Recommendations

## References
```

## Quick Start

### Single Paper Analysis

```
Deep reading of this paper: [Title or link]
```

The skill will:
1. Clarify your research context and objectives
2. Retrieve and verify the paper
3. Conduct systematic analysis
4. Generate comprehensive report with insights

### Literature Survey

```
Research the latest literature on [research direction]
```

The skill will:
1. Confirm the research scope
2. Search for relevant papers
3. Analyze key papers
4. Synthesize findings and identify research gaps

### Quick Brief

```
Quickly summarize the core content of this paper
```

The skill will:
1. Provide quick overview
2. Highlight key contributions
3. Summarize main findings
4. Suggest follow-up directions

## Key Features

### Comprehensive Analysis Framework
- Systematic examination of all important aspects
- Consistent structure across all papers
- Actionable insights for follow-up research

### Innovation Assessment
- Systematic evaluation of research contributions
- Comparison with existing methods
- Assessment of novelty and significance

### Research Implications Extraction
- Theoretical implications
- Practical applications
- Methodological insights
- Future research directions

### Quality Standards
- Every claim is supported by evidence
- Limitations are honestly discussed
- Insights are specific and actionable
- Reports are balanced and comprehensive

## File Structure

```
academic-literature-research/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── references/
│   ├── paper_analysis_framework.md   # Detailed analysis methodology
│   ├── innovation_assessment_guide.md # How to evaluate innovation
│   └── research_implications_guide.md # How to extract insights
├── templates/
│   ├── paper_analysis_template.md    # Single paper analysis template
│   ├── multi_paper_synthesis_template.md
│   ├── survey_report_template.md
│   └── quick_brief_template.md
└── examples/
    ├── single_paper_analysis.md      # Example analysis
    ├── multi_paper_synthesis.md
    ├── survey_report.md
    └── quick_brief.md
```

## Installation

### Option 1: Claude Code Plugin Marketplace
```bash
/plugin marketplace add sik0101/academic-literature-research
/plugin install academic-literature-research
```

### Option 2: Manual Installation
1. Clone the repository:
```bash
git clone https://github.com/sik0101/academic-literature-research.git
```

2. Copy to Claude Code skills directory:
```bash
cp -r academic-literature-research ~/.claude/skills/
```

3. Restart Claude Code

## Usage Examples

### Example 1: Deep Paper Analysis

**Input**:
```
Deep reading of the paper: "Attention Is All You Need" (Vaswani et al., 2017)
```

**Output**: Comprehensive analysis including:
- Research motivation (why Transformers were needed)
- Problem formulation (sequence-to-sequence modeling)
- Core contribution (self-attention mechanism)
- Experimental validation (BLEU scores on translation tasks)
- Strengths (parallelizability, long-range dependencies)
- Limitations (computational complexity, interpretability)
- Implications (paradigm shift in NLP, applications to other domains)

### Example 2: Literature Survey

**Input**:
```
Survey the latest literature on the application of graph neural networks in recommendation systems
```

**Output**: Survey report including:
- Research landscape overview
- Key papers analysis
- Comparison of different approaches
- Research gaps and trends
- Recommendations for follow-up research

### Example 3: Quick Brief

**Input**:
```
Quickly summarize the core content of the BERT paper
```

**Output**: Brief summary including:
- Core contribution
- Key findings
- Main advantages
- Potential applications

## Quality Standards

This skill maintains high quality standards:

1. **Evidence-Based**: Every claim is supported by the paper's content
2. **Comprehensive**: All important aspects are covered
3. **Balanced**: Both strengths and limitations are discussed
4. **Actionable**: Insights are specific and useful for follow-up research
5. **Transparent**: Limitations and uncertainties are acknowledged
6. **Reproducible**: Analysis methodology is documented

## Integration with Other Skills

This skill complements the academic research suite:

- **deep-research**: For comprehensive literature review and synthesis
- **academic-paper**: For writing papers based on research findings
- **academic-paper-reviewer**: For peer review of papers
- **academic-pipeline**: For full research-to-publication pipeline

## Recommended Workflow

1. **Start with this skill** to understand specific papers or research areas
2. **Use deep-research** for comprehensive literature review and synthesis
3. **Use academic-paper** to write your own paper based on research findings
4. **Use academic-paper-reviewer** for peer review and feedback
5. **Use academic-pipeline** for full pipeline orchestration

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This skill is licensed under CC-BY-NC 4.0. See LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the maintainer

## Version History

### v1.0.0 (2026-05-29)
- Initial release
- Single paper analysis mode
- Multi-paper synthesis mode
- Literature survey mode
- Quick brief mode
- Comprehensive analysis framework
- Innovation assessment guide
- Research implications extraction

## Citation

If you use this skill in your research, please cite:

```bibtex
@software{academic_literature_research_2026,
  title={Academic Literature Research Skill},
  author={[Your Name]},
  year={2026},
  url={https://github.com/[username]/academic-literature-research}
}
```

## Acknowledgments

This skill is built on top of the deep-research skill from the academic-research-skills suite. It extends and specializes the deep-research functionality for academic literature analysis.

---

**Last Updated**: 2026-05-29  
**Version**: 1.0.0  
**Status**: Active
