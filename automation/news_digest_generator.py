#!/usr/bin/env python3
"""
News Digest Generator - Simple Test Version
Confirms API connection and workflow execution
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

    def generate_digest(self):
        """Generate a simple test news digest"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")

        prompt = f"""Today is {today}.

Generate an ADHD-friendly news digest for Sarah with this structure:

# 📰 News Digest for Sarah - {today}

## 💬 TL;DR (Top Stories)
- [5-7 bullet points with today's major news highlights]

## 🇪🇸 Spain & Europe
[Key stories from Spain, Italy, EU]

## 🧠 Psychology & Science  
[Mental health, neuroscience, research]

## 🎭 Arts & Culture
[Theater, cultural news]

## 👥 Social Issues
[Gender equality, human rights]

## ⚖️ Politics & Governance
[Political developments, investigations]

Use placeholder headlines that show Sarah's preferred style: clear, factual, diverse perspectives."""

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            print(f"📰 Generating news digest for {today}...")
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )

            if response.status_code != 200:
                print(f"⚠️ API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return self._fallback_digest()

            result = response.json()
            digest_content = ""
            for block in result.get("content", []):
                if block.get("type") == "text":
                    digest_content += block.get("text", "")

            if not digest_content:
                print("⚠️ No content in API response")
                return self._fallback_digest()

            print("✅ News digest generated successfully!")
            return digest_content

        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
            return self._fallback_digest()

    def _fallback_digest(self):
        """Fallback message"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        return f"""# 📰 News Digest for Sarah - {today}

## ⚠️ Automated Generation Unavailable

The automated news digest could not be generated. Please:
1. Check news manually, or
2. Ask Claude in chat: "Generate today's news digest"
3. Check workflow logs for details

---

**Note**: This is a test version. Web search integration coming soon.
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

        print(f"✓ Digest saved: {filepath}")
        return filepath


def main():
    """Main execution"""
    try:
        generator = NewsDigestGenerator()
        digest = generator.generate_digest()
        generator.save_digest(digest)
        print("✅ News digest complete!")
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")


if __name__ == "__main__":
    main()
