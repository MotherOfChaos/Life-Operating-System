#!/usr/bin/env python3
"""
Automated News Digest Generator
Uses Anthropic API + Claude to generate news digest with your perfected system

Preserves:
- Global_Media_Database_v3.json sources
- v4 format (TL;DR + detailed sections)
- Spanish sources in Spanish
- Cross-referenced political leans
- Fact vs opinion separation
- Your curated interests
"""

import os
import json
import requests
from datetime import datetime
from typing import Optional
import pytz


class NewsDigestGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")

        self.api_url = "https://api.anthropic.com/v1/messages"

        # Load media database (from root directory)
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Global_Media_Database_v3.json')
        with open(db_path, 'r', encoding='utf-8') as f:
            self.media_db = json.load(f)

        # Load news intelligence skill
        skill_path = os.path.join(os.path.dirname(__file__), 'news-intelligence-SKILL.md')
        with open(skill_path, 'r', encoding='utf-8') as f:
            self.skill_instructions = f.read()

    def generate_digest(self) -> tuple[str, str]:
        """
        Generate news digest using Claude API with web search
        Returns: (detailed_digest, tldr_summary)
        """
        print("📰 Calling Claude API to generate news digest...")
        print("   Using your perfected system with WebSearch...")

        # Use Madrid timezone for accurate date
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")

        prompt = f"""Today is {today}.

Using the news-intelligence skill and Global Media Database provided below, generate today's news digest following the EXACT v4 format.

CRITICAL REQUIREMENTS:
1. Search Spanish sources IN SPANISH (site:publico.es, site:eldiario.es, site:infolibre.es)
2. Use WebSearch tool to search for today's news
3. Follow the v4 format exactly (TL;DR + detailed sections)
4. Cross-reference sources with different political leans
5. Separate facts from opinions clearly
6. Focus on Sarah's interests: Spain, Italy, Europe, psychology, theater, corruption, gender violence

GLOBAL MEDIA DATABASE:
```json
{json.dumps(self.media_db, ensure_ascii=False, indent=2)}
```

NEWS INTELLIGENCE SKILL INSTRUCTIONS:
{self.skill_instructions}

Generate the complete news digest for today following the v4 format from the skill.
"""

        # Call Claude API with web search capability
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            
            "content-type": "application/json"
        }

        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 16000,
            "tools": [{"type": "web_search"}],
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=180  # 3 minutes for news generation
            )

            if response.status_code != 200:
                print(f"⚠️  API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return self._fallback_digest()

            result = response.json()

            # Extract the digest from response
            digest_content = ""
            for block in result.get("content", []):
                if block.get("type") == "text":
                    digest_content += block.get("text", "")

            if not digest_content:
                print("⚠️  No content in API response")
                return self._fallback_digest()

            print("   ✓ News digest generated successfully")

            # Extract TLDR from the digest
            tldr = self._extract_tldr(digest_content)

            return digest_content, tldr

        except Exception as e:
            print(f"⚠️  Error generating news: {str(e)}")
            return self._fallback_digest()

    def _extract_tldr(self, digest: str) -> str:
        """Extract TL;DR section from detailed digest"""
        # Look for TL;DR section
        if "## 💬 TL;DR" in digest:
            start = digest.find("## 💬 TL;DR")
            # Find next ## header or ---
            end = digest.find("\n##", start + 10)
            if end == -1:
                end = digest.find("\n---", start + 10)
            if end == -1:
                end = len(digest)

            tldr_section = digest[start:end].strip()
            return tldr_section
        else:
            # Create a simple TLDR from first few headlines
            return "## 📰 NEWS DIGEST\n\n_Check detailed digest for full coverage_\n"

    def _fallback_digest(self) -> tuple[str, str]:
        """Fallback when API fails"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        today = datetime.now(madrid_tz).strftime("%B %d, %Y")
        fallback = f"""# 📰 News Digest for Sarah - {today}

## ⚠️  Automated Generation Unavailable

The automated news digest could not be generated. Please:
1. Check news manually, or
2. Ask Claude in chat: "Generate today's news digest"
3. Check if Anthropic API key is configured

---

**Sources:** Global Media Database (154 sources available)
"""
        tldr = "## 📰 NEWS DIGEST\n\n_Automated generation failed - check manually_\n"
        return fallback, tldr

    def save_digest(self, detailed_digest: str, output_dir: str = "news-digests"):
        """Save the detailed digest to file"""
        os.makedirs(output_dir, exist_ok=True)

        # Use Madrid timezone for filename
        madrid_tz = pytz.timezone('Europe/Madrid')
        date_str = datetime.now(madrid_tz).strftime("%Y-%m-%d")
        filename = f"news-digest-{date_str}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(detailed_digest)

        print(f"   ✓ Detailed digest saved: {filepath}")
        return filepath


def main():
    """Generate news digest for GitHub Actions"""
    try:
        generator = NewsDigestGenerator()
        detailed_digest, tldr = generator.generate_digest()

        # Save detailed version
        generator.save_digest(detailed_digest)

        # Save TLDR for morning brief to use
        with open('automation/.news_tldr_cache.md', 'w', encoding='utf-8') as f:
            f.write(tldr)

        print("✅ News digest generation complete")

    except Exception as e:
        print(f"⚠️  Fatal error: {str(e)}")
        # Create fallback
        fallback_tldr = "## 📰 NEWS DIGEST\n\n_Generation failed - check manually_\n"
        with open('automation/.news_tldr_cache.md', 'w', encoding='utf-8') as f:
            f.write(fallback_tldr)


if __name__ == "__main__":
    main()
