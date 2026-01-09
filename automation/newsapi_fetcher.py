#!/usr/bin/env python3
"""
NewsAPI Integration - Fetch REAL news articles from verified sources
Free tier: 100 requests/day, good for daily automation
"""

import os
import json
import requests
from datetime import datetime, timedelta
import pytz


class NewsAPIFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('NEWSAPI_KEY')
        if not self.api_key:
            print("⚠️  NEWSAPI_KEY not set - get free key at https://newsapi.org/")
            self.api_key = None
        
        self.base_url = "https://newsapi.org/v2"
        
        # Load our verified sources database
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Global_Media_Database_v3.json')
        with open(db_path, 'r', encoding='utf-8') as f:
            self.media_db = json.load(f)

    def fetch_news(self, sources_list, query=None, days_back=1):
        """
        Fetch news from specified sources
        sources_list: list of source IDs (e.g., ['bbc-news', 'reuters'])
        """
        if not self.api_key:
            return []
        
        # Calculate date range
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz)
        from_date = (today - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        # Build sources string
        sources_str = ','.join(sources_list)
        
        params = {
            'apiKey': self.api_key,
            'sources': sources_str,
            'from': from_date,
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': 20
        }
        
        if query:
            params['q'] = query
        
        try:
            response = requests.get(
                f"{self.base_url}/everything",
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('articles', [])
            else:
                print(f"⚠️  NewsAPI error: {response.status_code}")
                print(f"Response: {response.text}")
                return []
                
        except Exception as e:
            print(f"⚠️  Error fetching news: {str(e)}")
            return []

    def fetch_by_topic(self, topic, language='en', days_back=1):
        """Fetch news by topic/keyword"""
        if not self.api_key:
            return []
        
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz)
        from_date = (today - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        params = {
            'apiKey': self.api_key,
            'q': topic,
            'from': from_date,
            'language': language,
            'sortBy': 'publishedAt',
            'pageSize': 10
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/everything",
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('articles', [])
            else:
                return []
                
        except Exception as e:
            print(f"⚠️  Error: {str(e)}")
            return []

    def fetch_sarah_news(self):
        """Fetch news for Sarah's interests"""
        all_articles = []
        
        print("📰 Fetching news from priority sources...")
        
        # English sources (NewsAPI format)
        english_sources = [
            'bbc-news',
            'reuters', 
            'associated-press',
            'the-guardian-uk',
            'ansa'  # Italian news agency
        ]
        
        articles = self.fetch_news(english_sources)
        print(f"   ✓ Got {len(articles)} articles from major sources")
        all_articles.extend(articles)
        
        # Topic searches for Sarah's interests
        topics = {
            'psychology': 'en',
            'neuroscience': 'en',
            'theater': 'en',
            'Barcelona': 'en',
            'Spain politics': 'en',
            'Italy': 'en'
        }
        
        for topic, lang in topics.items():
            articles = self.fetch_by_topic(topic, language=lang, days_back=1)
            print(f"   ✓ Got {len(articles)} articles for '{topic}'")
            all_articles.extend(articles)
        
        # Remove duplicates
        seen_urls = set()
        unique_articles = []
        for article in all_articles:
            url = article.get('url')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_articles.append(article)
        
        print(f"\n✅ Total unique articles: {len(unique_articles)}")
        return unique_articles

    def save_articles(self, articles, output_file="automation/.newsapi_cache.json"):
        """Save fetched articles for Claude to process"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved articles to {output_file}")


def main():
    """Test the NewsAPI fetcher"""
    fetcher = NewsAPIFetcher()
    
    if not fetcher.api_key:
        print("\n❌ No API key found!")
        print("To use NewsAPI:")
        print("1. Get free key at https://newsapi.org/register")
        print("2. Add to GitHub secrets as NEWSAPI_KEY")
        return
    
    articles = fetcher.fetch_sarah_news()
    fetcher.save_articles(articles)
    
    # Show sample
    if articles:
        print("\n📄 Sample article:")
        article = articles[0]
        print(f"   Title: {article.get('title')}")
        print(f"   Source: {article.get('source', {}).get('name')}")
        print(f"   Published: {article.get('publishedAt')}")


if __name__ == "__main__":
    main()
