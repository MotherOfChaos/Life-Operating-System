#!/usr/bin/env python3
"""
News Digest Generator using NewsAPI + Claude
Fetches REAL articles, then Claude analyzes and formats them
"""

import os
import json
import requests
from datetime import datetime
import pytz
from newsapi_fetcher import NewsAPIFetcher


class NewsDigestWithAPI:
    def __init__(self, anthropic_key=None, newsapi_key=None):
        self.anthropic_key = anthropic_key or os.environ.get('ANTHROPIC_API_KEY')
        self.newsapi_key = newsapi_key or os.environ.get('NEWSAPI_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        
    def generate_digest(self):
        """Generate news digest from real NewsAPI articles"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        
        print(f"📰 Generating news digest for {today}...")
        
        # Step 1: Fetch real articles
        fetcher = NewsAPIFetcher(self.newsapi_key)
        articles = fetcher.fetch_sarah_news()
        
        if not articles:
            print("⚠️  No articles fetched - check NewsAPI key")
            return self._fallback_digest()
        
        # Step 2: Prepare articles for Claude
        articles_summary = []
        for article in articles[:50]:  # Limit to 50 most relevant
            articles_summary.append({
                'title': article.get('title'),
                'source': article.get('source', {}).get('name'),
                'description': article.get('description', '')[:200],
                'url': article.get('url'),
                'publishedAt': article.get('publishedAt')
            })
        
        # Step 3: Have Claude analyze and format
        prompt = f"""Today is {today}.

You have {len(articles_summary)} REAL news articles from today. Analyze them and create Sarah's ADHD-friendly news digest.

**ARTICLES:**
{json.dumps(articles_summary, indent=2, ensure_ascii=False)}

**CREATE DIGEST WITH:**

## 💬 TL;DR (Top 5-7 Stories)
- Pick the most important/interesting for Sarah

## 🇪🇸 Spain & Europe
## 🇮🇹 Italy  
## 🌍 World News
## 🧠 Psychology & Science
## 🎭 Arts & Culture
## 💻 Tech

**CRITICAL:**
- These are REAL articles from today
- Cite source names when mentioning stories
- Separate facts from analysis/opinion
- ADHD-friendly: scannable, clear sections
- Focus on Sarah's interests: Spain, Italy, psychology, theater, neuroscience

Generate the digest now."""

        headers = {
            "x-api-key": self.anthropic_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            
            if response.status_code != 200:
                print(f"⚠️  API Error: {response.status_code}")
                return self._fallback_digest()
            
            result = response.json()
            digest_content = ""
            for block in result.get("content", []):
                if block.get("type") == "text":
                    digest_content += block.get("text", "")
            
            if digest_content and len(digest_content) > 300:
                print("✅ Digest generated from real articles!")
                return f"# 📰 News Digest for Sarah - {today}\n\n{digest_content}"
            else:
                return self._fallback_digest()
                
        except Exception as e:
            print(f"⚠️  Error: {str(e)}")
            return self._fallback_digest()

    def _fallback_digest(self):
        """Fallback message"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        return f"""# 📰 News Digest for Sarah - {today}

## ⚠️ Automated Generation Unavailable

Could not generate automated news digest. Use the news-intelligence skill in Projects with M.

Say to M: "Generate news digest" for real-time news with web search."""

    def save_digest(self, digest_content, output_dir="news-digests"):
        """Save digest to file"""
        os.makedirs(output_dir, exist_ok=True)
        madrid_tz = pytz.timezone('Europe/Madrid')
        date_str = datetime.now(madrid_tz).strftime("%Y-%m-%d")
        filename = f"news-digest-{date_str}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(digest_content)
        
        print(f"✓ Saved to: {filepath}")


def main():
    generator = NewsDigestWithAPI()
    digest = generator.generate_digest()
    generator.save_digest(digest)
    print("✅ Complete!")


if __name__ == "__main__":
    main()
