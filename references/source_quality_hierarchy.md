# Source Quality Hierarchy & Evidence Grading Rubric

A comprehensive guide for assessing the credibility and quality of academic sources.

---

## Evidence Hierarchy Pyramid

```
                    ┌─────────────────────────┐
                    │  Systematic Reviews &   │
                    │  Meta-Analyses          │
                    │  (Highest Quality)      │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │  Randomized Controlled  │
                    │  Trials (RCTs)          │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │  Cohort Studies &       │
                    │  Case-Control Studies   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │  Case Reports &         │
                    │  Case Series            │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │  Expert Opinion &       │
                    │  Editorials             │
                    │  (Lowest Quality)       │
                    └─────────────────────────┘
```

---

## Quality Tiers

### Tier 1: Highest Quality (PRIMARY SOURCES)

**Characteristics:**
- Peer-reviewed publication
- Rigorous methodology
- Large sample size or comprehensive scope
- Published in top-tier venue
- High citation count
- Recent publication (within 5 years for fast-moving fields)

**Examples:**
- Systematic reviews and meta-analyses
- Randomized controlled trials (RCTs)
- Large cohort studies
- Papers in top journals (Nature, Science, JAMA, Lancet, etc.)
- Papers in top-tier conferences (NeurIPS, ICML, ICCV, ACL, etc.)

**Quality Score:** ⭐⭐⭐⭐⭐ (5/5)

**Use in Analysis:** 
- Primary evidence for major claims
- Can be cited directly without additional verification
- Highest weight in synthesis

---

### Tier 2: High Quality (PEER-REVIEWED RESEARCH)

**Characteristics:**
- Peer-reviewed publication
- Solid methodology
- Moderate sample size
- Published in reputable venue
- Moderate citation count
- Published within 10 years

**Examples:**
- Papers in well-established journals
- Papers in established conferences
- Rigorous empirical studies
- Well-designed experiments

**Quality Score:** ⭐⭐⭐⭐ (4/5)

**Use in Analysis:**
- Strong supporting evidence
- Can be cited with minor caveats
- Medium-high weight in synthesis

---

### Tier 3: Medium Quality (MIXED PEER-REVIEW)

**Characteristics:**
- Peer-reviewed or editorially reviewed
- Reasonable methodology
- Limited sample size or scope
- Published in moderate-tier venue
- Low-to-moderate citation count
- May be older (10-20 years)

**Examples:**
- Papers in specialized journals
- Papers in regional conferences
- Smaller empirical studies
- Technical reports from established organizations
- Preprints from established researchers

**Quality Score:** ⭐⭐⭐ (3/5)

**Use in Analysis:**
- Supporting evidence with caveats
- Should be cited with methodology notes
- Medium weight in synthesis
- Verify against higher-tier sources

---

### Tier 4: Lower Quality (LIMITED PEER-REVIEW)

**Characteristics:**
- Limited or no peer review
- Questionable methodology
- Small sample size
- Published in low-tier venue or self-published
- Very few citations
- Older publication (20+ years)

**Examples:**
- Blog posts and opinion pieces
- Preprints from unknown authors
- Self-published reports
- Outdated papers
- Papers from predatory journals

**Quality Score:** ⭐⭐ (2/5)

**Use in Analysis:**
- Use with extreme caution
- Must be verified against higher-tier sources
- Low weight in synthesis
- Flag as "limited evidence" in report

---

### Tier 5: Lowest Quality (NOT RECOMMENDED)

**Characteristics:**
- No peer review
- Unreliable methodology
- Unverifiable claims
- Published in predatory venue or not published
- No citations
- Highly outdated

**Examples:**
- Misinformation and disinformation
- Predatory journal articles
- Unverified social media claims
- Conspiracy theories
- Retracted papers

**Quality Score:** ⭐ (1/5)

**Use in Analysis:**
- DO NOT USE as evidence
- Only mention to explicitly refute
- Flag as "not credible" in report

---

## Publication Venue Assessment

### Journal Ranking

**Top-Tier Journals:**
- Impact Factor > 10
- Acceptance rate < 10%
- Examples: Nature, Science, JAMA, Lancet, Cell

**High-Quality Journals:**
- Impact Factor 5-10
- Acceptance rate 10-20%
- Examples: Nature Communications, PLOS ONE, Journal of Machine Learning Research

**Reputable Journals:**
- Impact Factor 2-5
- Acceptance rate 20-40%
- Examples: IEEE Transactions, ACM Transactions, domain-specific journals

**Moderate Journals:**
- Impact Factor 1-2
- Acceptance rate 40-60%
- Examples: Specialized journals, regional publications

**Low-Quality Journals:**
- Impact Factor < 1
- Acceptance rate > 60%
- Examples: Predatory journals, vanity presses

### Conference Ranking

**Top-Tier Conferences:**
- Acceptance rate < 20%
- High citation count
- Examples: NeurIPS, ICML, ICCV, ACL, EMNLP, ICLR

**High-Quality Conferences:**
- Acceptance rate 20-30%
- Moderate citation count
- Examples: CVPR, AAAI, IJCAI, SIGMOD

**Reputable Conferences:**
- Acceptance rate 30-50%
- Examples: Domain-specific conferences, regional conferences

**Lower-Quality Conferences:**
- Acceptance rate > 50%
- Examples: Predatory conferences, workshops

---

## Author Credibility Assessment

### H-Index Interpretation

| H-Index | Career Stage | Interpretation |
|---------|--------------|-----------------|
| 0-5 | Early career | Emerging researcher |
| 5-10 | Mid-career | Established researcher |
| 10-20 | Senior | Highly cited researcher |
| 20-50 | Very senior | Leading researcher in field |
| 50+ | Exceptional | Seminal contributor to field |

### Author Affiliation

**High-Credibility Affiliations:**
- Top research universities
- National laboratories
- Established research institutes
- Major tech companies (research divisions)

**Medium-Credibility Affiliations:**
- Regional universities
- Smaller research institutions
- Startup research labs

**Lower-Credibility Affiliations:**
- Unknown institutions
- Diploma mills
- Predatory organizations

### Track Record

**High Credibility:**
- Consistent publication record
- Multiple papers in top venues
- Recognized expertise in field
- Positive peer feedback

**Medium Credibility:**
- Some publication record
- Mix of venue quality
- Developing expertise

**Lower Credibility:**
- Inconsistent publication
- Primarily in low-tier venues
- Limited peer recognition

---

## Citation Count Interpretation

### Citation Metrics

| Citations | Interpretation | Quality Signal |
|-----------|-----------------|-----------------|
| 0-10 | Very recent or niche | May be too new to assess |
| 10-50 | Recent or specialized | Moderate impact |
| 50-100 | Established | Good impact |
| 100-500 | Influential | High impact |
| 500+ | Seminal | Very high impact |

**Important Notes:**
- Citation count depends on field (CS papers cite more than humanities)
- Self-citations should be excluded
- Citation count alone is not sufficient quality indicator
- Recent papers may have low citations but high quality

---

## Peer-Review Status Assessment

### Publication Types

**Peer-Reviewed:**
- Journal articles (most rigorous)
- Conference papers (varies by venue)
- Book chapters (varies by publisher)

**Editorially Reviewed:**
- Magazine articles
- Newspaper articles
- Some online publications

**Not Reviewed:**
- Blog posts
- Social media
- Self-published books
- Preprints (unless explicitly peer-reviewed)

### Preprint Assessment

**High-Quality Preprints:**
- From established researchers
- Later published in peer-reviewed venue
- High citation count
- Clear methodology

**Medium-Quality Preprints:**
- From known institutions
- Reasonable methodology
- Moderate citations

**Lower-Quality Preprints:**
- From unknown sources
- Unclear methodology
- No citations
- Never published in peer-reviewed venue

---

## Red Flags for Low-Quality Sources

| Red Flag | Concern | Action |
|----------|---------|--------|
| Predatory journal | Lack of peer review | Reject |
| Retracted paper | Fraudulent or erroneous | Reject |
| No author information | Unverifiable source | Reject |
| Sensationalized claims | Exaggeration or misinformation | Verify independently |
| No methodology section | Lack of rigor | Downgrade quality |
| Excessive self-citations | Bias or manipulation | Downgrade quality |
| Outdated data | Relevance concerns | Use with caution |
| Conflicts of interest | Potential bias | Flag and note |
| No citations to prior work | Lack of context | Downgrade quality |
| Extraordinary claims | Requires extraordinary evidence | Require multiple sources |

---

## Quality Assessment Checklist

When evaluating a source, check:

- [ ] **Peer Review**: Is it peer-reviewed?
- [ ] **Venue**: What is the publication venue's reputation?
- [ ] **Authors**: Are the authors credible and established?
- [ ] **Methodology**: Is the methodology sound and clearly described?
- [ ] **Sample Size**: Is the sample size adequate?
- [ ] **Citations**: How many citations does it have?
- [ ] **Recency**: Is it recent enough for the field?
- [ ] **Conflicts of Interest**: Are there potential conflicts?
- [ ] **Reproducibility**: Can the work be reproduced?
- [ ] **Limitations**: Are limitations honestly discussed?

---

## Using the Hierarchy in Analysis

### For Single Claims

**Tier 1 Source:** Use directly as primary evidence
```
"Research shows X (Smith et al., 2024, Nature)"
```

**Tier 2 Source:** Use as supporting evidence
```
"Research suggests X (Jones et al., 2023, Journal of Research)"
```

**Tier 3 Source:** Use with caveats
```
"Preliminary evidence indicates X (Brown et al., 2022, Technical Report)"
```

**Tier 4 Source:** Use only with strong caveats
```
"Some sources suggest X, though evidence is limited (Lee et al., 2020)"
```

### For Contradictory Claims

When sources disagree:

1. **Identify the evidence quality** of each source
2. **Compare methodologies** — which is more rigorous?
3. **Check publication dates** — is one more recent?
4. **Report both sides** with quality comparison
5. **Recommend further research** if unclear

**Example:**
```
"While Smith et al. (2024, Nature) found X, Jones et al. (2023, preprint) 
reported Y. The Smith study used a larger sample (n=10,000) and was 
peer-reviewed, suggesting higher confidence in X, though the Jones 
findings warrant further investigation."
```

---

## Tools for Source Assessment

### Citation Databases
- **Google Scholar** — Free citation lookup
- **Semantic Scholar** — AI-powered paper search
- **Web of Science** — Citation tracking
- **Scopus** — Comprehensive indexing

### Journal Ranking
- **Journal Citation Reports (JCR)** — Impact factor
- **Scimago Journal Rank (SJR)** — Alternative ranking
- **h-index** — Author impact metric

### Predatory Journal Detection
- **Beall's List** — Predatory journal database
- **DOAJ** — Directory of Open Access Journals
- **Think Check Submit** — Journal evaluation checklist

### Retraction Tracking
- **Retraction Watch** — Retracted paper database
- **PubMed** — Retraction notices

---

## Best Practices

1. **Prioritize Tier 1 sources** for major claims
2. **Use multiple sources** to triangulate findings
3. **Check for conflicts of interest** in funding and affiliations
4. **Verify extraordinary claims** with multiple high-quality sources
5. **Update regularly** — older sources may be superseded
6. **Disclose source quality** in your analysis
7. **Be transparent** about limitations of evidence
8. **Avoid cherry-picking** — represent the full evidence landscape

---

**Last Updated**: 2026-05-29  
**Reference**: Based on GRADE (Grading of Recommendations Assessment, Development and Evaluation) methodology and academic research standards.
