#!/usr/bin/env python3
"""
Artist & Provider Database Extractor
Processes work emails to build/update artist and provider databases
Uses Anthropic API to extract structured information from emails
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

try:
    import anthropic
except ImportError:
    print("⚠️  Anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


class ArtistDatabaseExtractor:
    """Extract artist and provider info from work emails"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.artists_db_file = "artists_database.json"
        self.providers_db_file = "providers_database.json"

    def process_email_triage_results(self, results_file: str = "email_triage_results.json"):
        """Process email triage results and extract artist/provider info"""

        print("\n" + "=" * 60)
        print("🎭 ARTIST & PROVIDER DATABASE EXTRACTION")
        print("=" * 60)

        # Load email triage results
        if not os.path.exists(results_file):
            print(f"⚠️  No email triage results found: {results_file}")
            return

        with open(results_file, 'r', encoding='utf-8') as f:
            results = json.load(f)

        # Find emails marked for database extraction
        emails_to_process = []
        for account_name, data in results.items():
            if "emails" in data and data.get("mode") == "artist_database":
                for email in data["emails"]:
                    if email.get("extract_to_database", False):
                        emails_to_process.append({
                            **email,
                            "account": account_name
                        })

        if not emails_to_process:
            print("✅ No emails marked for extraction")
            return

        print(f"\n📧 Found {len(emails_to_process)} email(s) to process")

        # Load existing databases
        artists_db = self._load_database(self.artists_db_file)
        providers_db = self._load_database(self.providers_db_file)

        # Process each email
        for i, email in enumerate(emails_to_process, 1):
            print(f"\n📨 Processing {i}/{len(emails_to_process)}: {email['subject']}")

            try:
                extraction = self._extract_info_with_ai(email)

                if extraction.get("type") == "artist":
                    self._add_to_artist_db(artists_db, extraction, email)
                    print(f"   ✓ Added to artist database")
                elif extraction.get("type") == "provider":
                    self._add_to_provider_db(providers_db, extraction, email)
                    print(f"   ✓ Added to provider database")
                else:
                    print(f"   ⚠️  Could not categorize")

            except Exception as e:
                print(f"   ⚠️  Error: {str(e)}")

        # Save updated databases
        self._save_database(self.artists_db_file, artists_db)
        self._save_database(self.providers_db_file, providers_db)

        print("\n" + "=" * 60)
        print("✅ EXTRACTION COMPLETE")
        print(f"🎭 Artists: {len(artists_db.get('artists', []))} total")
        print(f"🏢 Providers: {len(providers_db.get('providers', []))} total")
        print("=" * 60)

    def _extract_info_with_ai(self, email: Dict) -> Dict:
        """Use Claude to extract structured info from email"""

        prompt = f"""
Extract structured information from this work email.

FROM: {email['from_name']} <{email['from_email']}>
SUBJECT: {email['subject']}
CONTENT: {email['snippet']}
CATEGORY: {email['category']}

Please analyze this email and extract:

1. Is this about an ARTIST/PERFORMER or a PROVIDER/VENUE?
2. Extract relevant structured data:

For ARTIST:
- Name
- Type (musician, actor, performer, etc.)
- Contact email
- Contact person (if different from artist)
- Specialty/genre
- Availability mentioned
- Rate/fee mentioned
- Any other relevant notes

For PROVIDER/VENUE:
- Company/venue name
- Type (venue, equipment, catering, etc.)
- Contact email
- Contact person
- Services offered
- Rates mentioned
- Location
- Any other relevant notes

Respond in JSON format:
{{
  "type": "artist" or "provider",
  "data": {{ extracted fields }}
}}

If you can't determine the type or extract meaningful info, respond:
{{
  "type": "unknown",
  "reason": "explanation"
}}
"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse JSON response
        response_text = response.content[0].text.strip()

        # Extract JSON from markdown code blocks if present
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()

        return json.loads(response_text)

    def _add_to_artist_db(self, db: Dict, extraction: Dict, email: Dict):
        """Add artist to database"""
        if "artists" not in db:
            db["artists"] = []

        artist_data = extraction.get("data", {})
        artist_data["source_email"] = email["from_email"]
        artist_data["date_added"] = datetime.now().isoformat()
        artist_data["original_subject"] = email["subject"]

        # Check for duplicates (by email)
        existing = next(
            (a for a in db["artists"] if a.get("source_email") == artist_data["source_email"]),
            None
        )

        if existing:
            # Update existing entry
            existing.update(artist_data)
            existing["last_updated"] = datetime.now().isoformat()
        else:
            # Add new entry
            db["artists"].append(artist_data)

    def _add_to_provider_db(self, db: Dict, extraction: Dict, email: Dict):
        """Add provider to database"""
        if "providers" not in db:
            db["providers"] = []

        provider_data = extraction.get("data", {})
        provider_data["source_email"] = email["from_email"]
        provider_data["date_added"] = datetime.now().isoformat()
        provider_data["original_subject"] = email["subject"]

        # Check for duplicates (by email)
        existing = next(
            (p for p in db["providers"] if p.get("source_email") == provider_data["source_email"]),
            None
        )

        if existing:
            # Update existing entry
            existing.update(provider_data)
            existing["last_updated"] = datetime.now().isoformat()
        else:
            # Add new entry
            db["providers"].append(provider_data)

    def _load_database(self, filename: str) -> Dict:
        """Load existing database or create new"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_database(self, filename: str, data: Dict):
        """Save database to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Saved: {filename}")


def main():
    """Standalone mode - process email triage results"""
    print("🎭 ARTIST & PROVIDER DATABASE EXTRACTOR")

    # Load API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not set!")
        print("Set it as environment variable or in config.py")
        sys.exit(1)

    # Create extractor
    extractor = ArtistDatabaseExtractor(api_key)

    # Process email triage results
    extractor.process_email_triage_results()


if __name__ == "__main__":
    main()
