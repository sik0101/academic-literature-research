# Literature Survey Skill V5 改进需求文档

## 目标

当前 Skill 已具备：

- 文献检索
- 论文筛选
- 单篇论文分析
- 多篇论文汇总

但整体输出仍偏向：

- 论文摘要集合
- 信息堆砌
- Survey 总结 Survey

缺少：

- 研究问题驱动分析
- 技术路线分析
- 领域演化逻辑
- 批判性分析
- 最新研究趋势

最终目标：

让用户不仅知道：

"有哪些论文"

更知道：

"这些论文之间是什么关系"

以及：

"为什么这个领域会发展成现在这样"

和：

"未来可能会发展到哪里"

------

# 一、论文筛选策略

新增论文分类：

- Method Paper
- Benchmark Paper
- Dataset Paper
- Analysis Paper
- Survey Paper

推荐比例：

- Method Paper ≥ 60%
- Benchmark / Dataset ≥ 20%
- Analysis ≥ 10%
- Survey ≤ 10%

Survey 仅用于：

- 构建背景
- 验证研究方向

不得成为核心分析对象。

优先保留：

- 开创性论文
- 高引用论文
- 技术路线转折点论文
- 当前 SOTA 论文
- 最新代表性论文

避免：

多个内容重复的 Survey 同时进入核心分析。

------

# 二、时间覆盖要求（新增）

避免调研被历史经典论文主导。

对于快速发展领域：

- LLM
- Agent
- MLLM
- 推荐系统
- 时空预测
- AI4Science

要求：

近两年（2025-2026）论文占比 ≥ 30%

必须覆盖：

- 最新顶会论文
- 最新高影响力 Arxiv 论文
- 最新 Benchmark 工作

输出必须同时体现：

- 经典工作
- 当前主流工作
- 最新研究工作

避免只停留在：

2018-2024 的历史回顾。

------

# 三、从“论文中心”改为“研究问题中心”

不要按：

论文A
论文B
论文C

组织调研。

而应首先识别：

领域正在解决哪些核心问题。

例如：

交通预测：

- 如何建模空间依赖
- 如何建模长期时间依赖
- 如何建模动态图结构
- 如何实现跨城市泛化

MLLM：

- 如何实现视觉对齐
- 如何进行视觉指令学习
- 如何提升视觉推理能力
- 如何实现Agent能力

推荐系统：

- 如何解决冷启动
- 如何建模长期兴趣
- 如何提升泛化能力

围绕问题组织综述。

论文作为支撑证据。

------

# 四、Research Landscape（核心模块）

首先生成：

Research Landscape

目标：

构建整个领域的研究版图。

回答：

- 领域主要研究问题是什么？
- 存在哪些技术路线？
- 不同路线解决什么问题？
- 路线之间是什么关系？

------

每条路线输出：

## Research Question

解决什么问题

------

## Motivation

为什么重要

------

## Main Approaches

主要方法类别

------

## Representative Papers

至少列出：

- Title
- Authors
- Year
- Venue
- Link

------

## Strengths

解决了什么问题

------

## Limitations

尚未解决什么问题

------

## Relationship to Other Directions

与其他路线的联系与区别

------

# 五、Representative Papers（保留并升级原七步分析）

对于核心论文进行深入分析。

保留原有优势。

------

## 1. Research Problem

解决什么问题

------

## 2. Core Idea

核心思想

------

## 3. Method Overview

方法概述

------

## 4. Innovation

创新点

------

## 5. Why It Works（新增）

为什么这样设计？

为什么相比前代方法有效？

解决了什么关键矛盾？

避免仅描述模块。

------

## 6. Experimental Evidence

实验是否真正支持结论

------

## 7. Strengths

优点

------

## 8. Limitations

缺点

------

## 9. Position in the Field（新增）

属于哪条技术路线

继承了哪些工作

影响了哪些后续工作

是：

- 开创工作
- 完善工作
- 转折工作
- 扩展工作

中的哪一种

------

## 10. Research Insights

带来的研究启发

------

# 六、Cross-Paper Insights

从论文集合中提炼规律。

而不是重复论文摘要。

------

## Common Patterns

主流方法的共性

------

## Bottlenecks

当前领域共同面临的问题

------

## Open Questions

尚未解决的问题

------

## Research Evolution Analysis（新增重点模块）

回答：

为什么领域从A发展到B？

而不仅仅是：

从A发展到B。

------

每个演化趋势必须包含：

### Previous Paradigm

旧范式

------

### New Paradigm

新范式

------

### Why the Shift Happened

必须分析转变原因：

例如：

- 性能瓶颈
- 可扩展性问题
- 数据规模变化
- 算力提升
- 硬件环境变化
- Benchmark变化
- 应用需求变化

至少分析一种。

------

### Evidence

引用代表论文支撑。

------

### Remaining Issues

转变后仍未解决的问题。

------

示例：

Graph Neural Network
↓

Transformer

原因：

- GNN感受野有限
- 长距离依赖建模困难
- Transformer支持全局建模
- GPU算力提升降低Attention成本

而不是仅写：

GNN → Transformer

------

# 七、Critical Analysis

必须具备批判性分析能力。

不要默认所有论文都有效。

------

## Contradictions

不同论文是否存在冲突结论

------

## Benchmark Bias

数据集偏差

------

## Evaluation Issues

评测是否充分

------

## Scalability Issues

是否真正具备扩展性

------

## Hype vs Evidence（新增）

防止：

热点方向 = 最优方向

------

分析：

### Popularity

热度如何

------

### Evidence Strength

证据是否充分

------

### Research Maturity

属于：

- Emerging
- Growing
- Mature
- Saturated

------

### Risk Assessment

是否存在：

- 数据污染
- Benchmark刷榜
- 工程堆料
- 难以复现

等问题

------

# 八、Emerging Directions（2025-2026新增模块）

目标：

识别最新研究趋势。

回答：

现在大家正在研究什么？

------

对于每个方向：

## Research Trend

趋势名称

------

## Why It Emerged

为什么最近开始受到关注

------

## Representative Papers

必须给出：

- Title
- Authors
- Year
- Venue/Arxiv
- Link

------

## Relationship to Existing Work

与已有路线关系

------

## Potential Impact

可能带来的影响

------

## Maturity Assessment

成熟度：

- Emerging
- Growing
- Mature

------

# 九、Future Directions

Future Directions 必须基于证据推导。

来源：

- Bottlenecks
- Open Questions
- Critical Analysis
- Emerging Directions

------

格式：

Current Bottleneck

↓

Why Existing Methods Fail

↓

Possible Future Direction

------

禁止：

空泛建议：

- 提高性能
- 提高效率
- 提高泛化能力

除非有明确证据支撑。

------

# 十、论文引用要求

所有关键结论必须绑定论文。

禁止：

只出现概念。

例如：

错误：

Transformer路线

正确：

Transformer路线

代表论文：

- PDFormer (NeurIPS 2023)
- STAEformer (CIKM 2023)
- TimeXer (ICLR 2025)

并附：

- 作者
- 年份
- Venue
- Link

保证用户可继续追踪文献。

------

# 十一、最终输出结构

1. Executive Summary
2. Research Landscape
   - 核心问题
   - 技术路线
   - 代表论文
3. Representative Papers
   - 深度论文分析
4. Cross-Paper Insights
   - Common Patterns
   - Bottlenecks
   - Open Questions
   - Research Evolution Analysis
5. Critical Analysis
   - Contradictions
   - Benchmark Bias
   - Scalability
   - Hype vs Evidence
6. Emerging Directions (2025-2026)
7. Future Directions
8. References

------

# 最终要求

输出必须做到：

Level 1：
论文讲了什么

Level 2：
为什么这么设计

Level 3：
为什么有效

Level 4：
解决了什么核心矛盾

Level 5：
与其他路线有什么关系

Level 6：
为什么仍然不够

Level 7：
未来为什么会向某个方向发展

最终让用户理解：

“这个领域为什么会发展成这样，以及未来可能发展到哪里。”

而不仅仅是：

“有哪些论文。”