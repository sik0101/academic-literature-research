# Semantic Scholar API 使用指南

**版本**: 1.0  
**创建日期**: 2026-05-29  
**基于**: academic-research-skills 最佳实践

---

## 概述

Semantic Scholar API 是一个免费的学术论文搜索和验证 API，由 Allen Institute for AI 提供。

**主要特点**:
- ✅ 免费使用，无需认证
- ✅ 包含 200M+ 论文
- ✅ 支持标题搜索、DOI 查询、ID 查询
- ✅ 返回论文元数据（作者、年份、引用数等）
- ✅ 支持 arXiv、DOI、Semantic Scholar ID

---

## API 端点

### 1. 论文搜索 (按标题)

```
GET https://api.semanticscholar.org/graph/v1/paper/search
```

**参数**:
```
query: 论文标题 (必需)
limit: 返回结果数量 (默认 10)
fields: 返回字段 (逗号分隔)
```

**示例**:
```
GET https://api.semanticscholar.org/graph/v1/paper/search?query=Attention%20Is%20All%20You%20Need&limit=5&fields=title,authors,year,externalIds,citationCount
```

### 2. DOI 查询

```
GET https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}
```

### 3. ID 查询

```
GET https://api.semanticscholar.org/graph/v1/paper/{paperId}
```

---

## 论文匹配算法

### Levenshtein 相似度

用于匹配搜索结果中最相关的论文。

```python
from difflib import SequenceMatcher

def calculate_similarity(title1, title2):
    """计算两个标题的相似度"""
    return SequenceMatcher(None, 
                          title1.lower().strip(), 
                          title2.lower().strip()).ratio()
```

### 匹配规则

- **相似度阈值**: >= 0.70 (70%)
- **优先级**: 
  1. 相似度最高的结果
  2. 如果多个结果相似度相同，选择年份匹配的
  3. 如果仍有多个，选择引用数最多的

---

## 速率限制

| 认证方式 | 速率限制 | 建议用途 |
|---------|---------|---------|
| 无认证 | 1 req/sec | 小规模查询 (< 100 论文) |
| 有 API key | 10 req/sec | 大规模查询 (> 100 论文) |

### 获取 API Key

1. 访问: https://www.semanticscholar.org/product/api
2. 注册账户
3. 获取 API key
4. 设置环境变量: `export S2_API_KEY=your_api_key`

---

## 错误处理

### 常见错误

| 错误码 | 说明 | 处理方式 |
|--------|------|---------|
| 200 | 成功 | 继续处理结果 |
| 400 | 请求参数错误 | 检查查询参数 |
| 429 | 速率限制 | 等待 2 秒后重试 |
| 500 | 服务器错误 | 跳过此论文，继续下一个 |
| 503 | 服务不可用 | 使用降级方案 (DOI 或 web-access) |

### 降级策略

```
Tier 0 失败 (Semantic Scholar API 标题搜索)
  ↓
Tier 1 (DOI 直接解析)
  ↓
Tier 2 (WebSearch: site:arxiv.org "{title}")
  ↓
Tier 3 (WebFetch: 直接抓取 arXiv/DOI 页面)
  ↓
使用现有信息，标记为 "未验证"
```

---

## 最佳实践

### 1. 批量查询优化

```python
# 实现速率限制
for paper in papers:
    result = api.search_paper(paper['title'])
    # API 会自动处理速率限制
```

### 2. 缓存结果

```python
# 缓存已验证的论文，避免重复查询
cache = {}

def verify_paper_cached(title):
    if title in cache:
        return cache[title]
    
    result = api.verify_paper(title)
    cache[title] = result
    return result
```

### 3. 错误恢复

```python
# 实现重试机制
def verify_paper_with_retry(title, max_retries=3):
    for attempt in range(max_retries):
        try:
            return api.verify_paper(title)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # 指数退避
            else:
                return {'verified': False}
```

---

## 常见问题

### Q1: 为什么有些论文找不到？

**A**: Semantic Scholar 可能没有索引该论文。常见原因：
- 论文太新 (< 1 周)
- 论文是非英文的
- 论文是灰色文献 (技术报告、工作论文)
- 论文标题有特殊字符

**解决方案**: 使用 DOI 或 arXiv ID 直接查询

### Q2: 如何获得更快的速度？

**A**: 
1. 获取 API key (速度提升 10 倍)
2. 使用缓存避免重复查询
3. 批量查询而不是逐个查询

### Q3: 如何处理 API 不可用的情况？

**A**: 使用三层降级策略：
1. Semantic Scholar API (主要)
2. DOI 解析 (备用)
3. Web-Access (可选)

---

## 参考资源

- **官方文档**: https://api.semanticscholar.org/
- **API Key 申请**: https://www.semanticscholar.org/product/api

---

**文档版本**: 1.0  
**最后更新**: 2026-05-29  
**状态**: 完成
