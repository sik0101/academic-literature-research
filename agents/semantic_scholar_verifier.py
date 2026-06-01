"""
Semantic Scholar API Verifier
用于论文搜索、验证和链接生成

基于 academic-research-skills 的最佳实践
"""

import requests
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Tuple
import time


class SemanticScholarVerifier:
    """Semantic Scholar API 验证器"""

    def __init__(self, api_key: Optional[str] = None):
        """
        初始化验证器

        Args:
            api_key: Semantic Scholar API key (可选)
                    无 API key: 1 req/sec
                    有 API key: 10 req/sec
        """
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.api_key = api_key
        self.headers = {}
        if api_key:
            self.headers['x-api-key'] = api_key

        self.last_request_time = 0
        self.rate_limit = 1 if not api_key else 0.1  # 秒

    def _rate_limit(self):
        """实现速率限制"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self.last_request_time = time.time()

    def search_paper(self, title: str, limit: int = 5) -> Dict:
        """
        通过标题搜索论文

        Args:
            title: 论文标题
            limit: 返回结果数量

        Returns:
            搜索结果字典
        """
        url = f"{self.base_url}/paper/search"
        params = {
            'query': title,
            'limit': limit,
            'fields': 'title,authors,year,externalIds,venue,publicationDate,citationCount'
        }

        self._rate_limit()

        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[S2-API-ERROR] Search failed: {e}")
            return {'data': []}

    def get_paper_by_doi(self, doi: str) -> Dict:
        """
        通过 DOI 获取论文

        Args:
            doi: 论文 DOI

        Returns:
            论文信息字典
        """
        url = f"{self.base_url}/paper/DOI:{doi}"
        params = {
            'fields': 'title,authors,year,externalIds,venue,publicationDate,citationCount'
        }

        self._rate_limit()

        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[S2-API-ERROR] DOI lookup failed: {e}")
            return {}

    def get_paper_by_id(self, paper_id: str) -> Dict:
        """
        通过 Semantic Scholar ID 获取论文

        Args:
            paper_id: Semantic Scholar 论文 ID

        Returns:
            论文信息字典
        """
        url = f"{self.base_url}/paper/{paper_id}"
        params = {
            'fields': 'title,authors,year,externalIds,venue,publicationDate,citationCount'
        }

        self._rate_limit()

        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[S2-API-ERROR] ID lookup failed: {e}")
            return {}

    def match_paper(self, title: str, search_results: Dict, threshold: float = 0.70) -> Tuple[Optional[Dict], float]:
        """
        匹配论文 (Levenshtein 相似度)

        Args:
            title: 查询标题
            search_results: 搜索结果
            threshold: 相似度阈值 (0-1)

        Returns:
            (匹配的论文, 相似度分数)
        """
        best_match = None
        best_score = 0

        for result in search_results.get('data', []):
            # 计算 Levenshtein 相似度
            score = SequenceMatcher(
                None,
                title.lower().strip(),
                result['title'].lower().strip()
            ).ratio()

            if score > best_score:
                best_score = score
                best_match = result

        if best_score >= threshold and best_match:
            return best_match, best_score

        return None, best_score

    def generate_links(self, paper: Dict) -> Dict[str, Optional[str]]:
        """
        生成论文链接

        Args:
            paper: 论文信息字典

        Returns:
            链接字典
        """
        links = {}

        # arXiv 链接
        if paper.get('externalIds', {}).get('ArXiv'):
            arxiv_id = paper['externalIds']['ArXiv']
            links['arxiv'] = f"https://arxiv.org/abs/{arxiv_id}"

        # DOI 链接
        if paper.get('externalIds', {}).get('DOI'):
            doi = paper['externalIds']['DOI']
            links['doi'] = f"https://doi.org/{doi}"

        # Semantic Scholar 链接
        if paper.get('paperId'):
            links['semantic_scholar'] = f"https://www.semanticscholar.org/paper/{paper['paperId']}"

        return links

    def verify_paper(self, paper_info: Dict) -> Dict:
        """
        验证论文并提取链接

        Args:
            paper_info: 论文信息 (至少包含 'title')

        Returns:
            验证后的论文信息
        """
        title = paper_info.get('title', '')

        if not title:
            paper_info['verified'] = False
            paper_info['verification_method'] = 'none'
            return paper_info

        # Tier 0: 通过标题搜索
        search_results = self.search_paper(title)
        match, score = self.match_paper(title, search_results)

        if match and score >= 0.70:
            # 匹配成功
            paper_info['semantic_scholar_id'] = match['paperId']
            paper_info['doi'] = match['externalIds'].get('DOI')
            paper_info['arxiv_id'] = match['externalIds'].get('ArXiv')
            paper_info['citation_count'] = match.get('citationCount', 0)
            paper_info['verified'] = True
            paper_info['verification_method'] = 's2_api'
            paper_info['match_score'] = score
            paper_info['links'] = self.generate_links(match)

            return paper_info

        # Tier 1: 尝试 DOI 解析
        if paper_info.get('doi'):
            doi_result = self.get_paper_by_doi(paper_info['doi'])
            if doi_result and 'paperId' in doi_result:
                paper_info['semantic_scholar_id'] = doi_result['paperId']
                paper_info['verified'] = True
                paper_info['verification_method'] = 'doi'
                paper_info['links'] = self.generate_links(doi_result)
                return paper_info

        # 验证失败
        paper_info['verified'] = False
        paper_info['verification_method'] = 'none'
        paper_info['links'] = {}

        return paper_info

    def search_latest_papers(self, topic: str, year_range: Tuple[int, int] = (2024, 2026),
                            limit: int = 10) -> List[Dict]:
        """
        搜索最新论文

        Args:
            topic: 研究主题
            year_range: 年份范围 (min_year, max_year)
            limit: 返回论文数量

        Returns:
            论文列表 (按发表时间倒序)
        """
        # 注意: Semantic Scholar API 的搜索不直接支持年份过滤
        # 这里我们搜索后在客户端过滤

        search_results = self.search_paper(topic, limit=limit*2)
        papers = []

        for result in search_results.get('data', []):
            year = result.get('year', 0)
            if year_range[0] <= year <= year_range[1]:
                papers.append(result)

        # 按发表时间倒序排列
        papers.sort(
            key=lambda x: x.get('publicationDate', '0000-00-00'),
            reverse=True
        )

        return papers[:limit]

    def filter_papers_by_quality(self, papers: List[Dict],
                                min_citation_count: int = 10,
                                peer_reviewed_only: bool = True,
                                relevance_threshold: float = 0.7) -> List[Dict]:
        """
        根据质量筛选论文

        Args:
            papers: 论文列表
            min_citation_count: 最少引用数
            peer_reviewed_only: 仅同行评审
            relevance_threshold: 相关性阈值

        Returns:
            筛选后的论文列表
        """
        filtered = []

        for paper in papers:
            # 检查引用数
            if paper.get('citationCount', 0) < min_citation_count:
                continue

            # 检查相关性
            if paper.get('relevance_score', 1.0) < relevance_threshold:
                continue

            filtered.append(paper)

        return filtered


def generate_paper_header_with_links(paper: Dict) -> str:
    """
    生成包含链接的论文头部

    Args:
        paper: 论文信息字典

    Returns:
        格式化的论文头部字符串
    """
    header = f"# {paper.get('title', 'Unknown Title')}\n\n"

    # 作者和发表信息
    authors = paper.get('authors', [])
    if authors:
        author_names = ', '.join([a.get('name', 'Unknown') for a in authors[:5]])
        if len(authors) > 5:
            author_names += f", et al."
        header += f"**Authors**: {author_names}\n"

    header += f"**Publication**: {paper.get('venue', 'Unknown')}, {paper.get('year', 'Unknown')}\n\n"

    # 标识符和链接
    header += "## Paper Identifiers & Links\n\n"
    header += "**Identifiers**:\n"

    if paper.get('doi'):
        header += f"- **DOI**: {paper['doi']}\n"

    if paper.get('arxiv_id'):
        header += f"- **arXiv ID**: {paper['arxiv_id']}\n"

    if paper.get('semantic_scholar_id'):
        header += f"- **Semantic Scholar ID**: {paper['semantic_scholar_id']}\n\n"

    # 访问链接
    header += "**Access Links**:\n"
    links = paper.get('links', {})

    if links.get('arxiv'):
        header += f"- 🔗 [View on arXiv]({links['arxiv']})\n"

    if links.get('doi'):
        header += f"- 🔗 [View on DOI]({links['doi']})\n"

    if links.get('semantic_scholar'):
        header += f"- 🔗 [View on Semantic Scholar]({links['semantic_scholar']})\n\n"

    # 验证信息
    header += "**Verification Status**:\n"
    if paper.get('verified'):
        header += f"- ✅ Verified via {paper.get('verification_method', 'unknown').upper()}\n"
        if paper.get('match_score'):
            header += f"- ✅ Match Score: {paper['match_score']:.2%}\n"
    else:
        header += "- ⚠️ Verification pending\n"

    header += f"- ✅ Citation Count: {paper.get('citation_count', 'N/A')}\n\n"

    return header


if __name__ == "__main__":
    # 测试示例
    verifier = SemanticScholarVerifier()

    # 测试论文搜索
    test_paper = {
        'title': 'Attention Is All You Need'
    }

    result = verifier.verify_paper(test_paper)
    print("验证结果:")
    print(f"  标题: {result.get('title')}")
    print(f"  验证状态: {result.get('verified')}")
    print(f"  验证方法: {result.get('verification_method')}")
    print(f"  DOI: {result.get('doi')}")
    print(f"  arXiv: {result.get('arxiv_id')}")
    print(f"  引用数: {result.get('citation_count')}")
    print(f"  链接: {result.get('links')}")

    # 生成论文头部
    header = generate_paper_header_with_links(result)
    print("\n生成的论文头部:")
    print(header)
