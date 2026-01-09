#!/usr/bin/env python3
"""
News Digest Generator - Using Extended Thinking with Web Search
"""

import os
import json
import requests
from datetime import datetime
import pytz


class NewsDigestGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        
        self.api_url = "https://api.anthropic.com/v1/messages"
        
        # Load media database
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Global_Media_Database_v3.json')
        with open(db_path, 'r', encoding='utf-8') as f:
            self.media_db = json.load(f)
        
        # Load skill instructions
        skill_path = os.path.join(os.path.dirname(__file__), 'news-intelligence-SKILL.md')
        with open(skill_path, 'r', encoding='utf-8') as f:
            self.skill_instructions = f.read()

    def generate_digest(self):
        """Generate news digest using extended thinking with web search"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        
        print(f"📰 Generating news digest for {today}...")
        print("   Using 154 verified sources with web search...")
        
        prompt = f"""Today is {today}.

Generate Sarah's daily news digest using these 154 verified sources:

{json.dumps(self.media_db, ensure_ascii=False, indent=2)[:5000]}... (full database loaded)

Follow these instructions:
{self.skill_instructions[:3000]}...

Search today's news from these priority sources:
- 🇪🇸 Spain: El País, El Diario, Público (search in Spanish!)
- 🇮🇹 Italy: ANSA, La Repubblica, Corriere della Sera
- 🌍 Global: Reuters, AP, AFP, BBC
- 🎭 Culture: The Guardian, arts sections
- 🧠 Science: Nature, major journals

Generate ADHD-friendly digest with:
1. TL;DR section (5-7 top stories)
2. Sections: Spain, Italy, Europe, World, Arts/Culture, Science/Tech
3. Separate FACTS from OPINIONS
4. Cross-reference multiple sources
5. Note political lean of sources

Format as markdown with clear sections."""

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 8000,
            "thinking": {
                "type": "enabled",
                "budget_tokens": 5000
            },
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=120
            )
            
            if response.status_code != 200:
                print(f"⚠️ API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return self._fallback_digest()
            
            result = response.json()
            
            # Extract content from response
            digest_content = ""
            for block in result.get("content", []):
                if block.get("type") == "text":
                    digest_content += block.get("text", "")
            
            if not digest_content or len(digest_content) < 500:
                print("⚠️ No sufficient content generated")
                return self._fallback_digest()
            
            print("✅ News digest generated successfully!")
            return digest_content
            
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
            return self._fallback_digest()

    def _fallback_digest(self):
        """Fallback when generation fails"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        return f"""# 📰 News Digest for Sarah - {today}

## ⚠️ Automated Generation Unavailable

The automated news digest could not be generated. Please use the news-intelligence skill directly in Projects with M.

**Sources available:** 154 verified international sources in Global_Media_Database_v3.json

---

*To get today's news, say to M: "Generate news digest" and M will use web search with the verified sources.*
"""

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
        return filepath


def main():
    """Main execution"""
    try:
        generator = NewsDigestGenerator()
        digest = generator.generate_digest()
        generator.save_digest(digest)
        print("✅ Complete!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
