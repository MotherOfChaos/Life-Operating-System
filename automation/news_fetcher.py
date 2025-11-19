"""
News Fetcher for Morning Brief
Fetches news from NewsAPI and formats it for ADHD-friendly digest
"""

import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class NewsFetcher:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('NEWS_API_KEY')
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def fetch_news_digest(self) -> str:
        """
        Fetch news and create ADHD-friendly digest
        Returns formatted markdown string
        """
        if not self.api_key:
            return self._no_api_key_fallback()

        # Fetch news by category
        spain_news = self._fetch_news(country='es', page_size=5)
        italy_news = self._fetch_news(country='it', page_size=3)
        europe_news = self._fetch_news(category='general', page_size=5)
        science_news = self._fetch_news(category='science', page_size=3)
        tech_news = self._fetch_news(category='technology', page_size=2)

        # Generate formatted digest
        digest = self._format_digest(
            spain_news,
            italy_news,
            europe_news,
            science_news,
            tech_news
        )

        return digest

    def _fetch_news(
        self,
        country: Optional[str] = None,
        category: Optional[str] = None,
        page_size: int = 5
    ) -> List[Dict]:
        """Fetch news from NewsAPI"""
        try:
            params = {
                'apiKey': self.api_key,
                'pageSize': page_size,
                'language': 'en' if not country else None
            }

            if country:
                params['country'] = country
            if category:
                params['category'] = category

            response = requests.get(self.base_url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return data.get('articles', [])
            else:
                print(f"⚠️  NewsAPI error: {response.status_code}")
                return []

        except Exception as e:
            print(f"⚠️  Error fetching news: {str(e)}")
            return []

    def _format_digest(
        self,
        spain_news: List[Dict],
        italy_news: List[Dict],
        europe_news: List[Dict],
        science_news: List[Dict],
        tech_news: List[Dict]
    ) -> str:
        """Format news into ADHD-friendly digest"""

        digest = "## 📰 NEWS DIGEST - TLDR\n\n"

        # Spain headlines
        if spain_news:
            digest += "**🇪🇸 Spain:**\n"
            for article in spain_news[:3]:
                title = article.get('title', 'No title')
                digest += f"- {self._clean_title(title)}\n"
            digest += "\n"

        # Italy headlines
        if italy_news:
            digest += "**🇮🇹 Italy:**\n"
            for article in italy_news[:2]:
                title = article.get('title', 'No title')
                digest += f"- {self._clean_title(title)}\n"
            digest += "\n"

        # Europe headlines
        if europe_news:
            digest += "**🇪🇺 Europe:**\n"
            for article in europe_news[:3]:
                title = article.get('title', 'No title')
                digest += f"- {self._clean_title(title)}\n"
            digest += "\n"

        # Science headlines
        if science_news:
            digest += "**🔬 Science:**\n"
            for article in science_news[:2]:
                title = article.get('title', 'No title')
                digest += f"- {self._clean_title(title)}\n"
            digest += "\n"

        # Tech headlines
        if tech_news:
            digest += "**💻 Tech:**\n"
            for article in tech_news[:2]:
                title = article.get('title', 'No title')
                digest += f"- {self._clean_title(title)}\n"
            digest += "\n"

        digest += "_📎 Full digest: Check news-digest branch for detailed coverage_\n\n"

        return digest

    def _clean_title(self, title: str) -> str:
        """Clean up news title"""
        # Remove source attribution from title (e.g., "- BBC News")
        if ' - ' in title:
            title = title.split(' - ')[0]

        # Truncate if too long
        if len(title) > 100:
            title = title[:97] + "..."

        return title.strip()

    def _no_api_key_fallback(self) -> str:
        """Fallback message when no API key"""
        return """## 📰 NEWS DIGEST

_📎 News API key not configured. Check news manually or say "fetch today's news" to Claude._

"""
