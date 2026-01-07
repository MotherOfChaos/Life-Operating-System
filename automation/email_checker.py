#!/usr/bin/env python3
"""
Email Checking Automation for M
Fetches emails from multiple accounts and categorizes them for easy reading

Accounts:
- sarah poer@gmail.com
- sarah@teatrometamorfosis.com
- info@teatrometamorfosis.com

Categories:
🔴 Urgent (require immediate action)
🟡 Needs Response (not urgent)
📅 Calendar/Events
💰 Financial/Payments
📰 Newsletters/Marketing
ℹ️ FYI (informational)
🗑️ Can Archive
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict
import pytz


class EmailChecker:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.anthropic.com/v1/messages"

    def fetch_emails_via_gmail_api(self, account: str, hours: int = 24) -> List[Dict]:
        """
        Fetch emails from Gmail API for the specified account
        This is a placeholder - actual implementation needs Gmail API credentials
        """
        # TODO: Implement actual Gmail API fetching
        # For now, return empty list
        print(f"📧 Would fetch emails from {account} (last {hours} hours)")
        return []

    def categorize_emails(self, emails: List[Dict]) -> Dict:
        """
        Use Claude to categorize emails into ADHD-friendly categories
        """
        if not emails:
            return {
                "urgent": [],
                "needs_response": [],
                "calendar": [],
                "financial": [],
                "newsletters": [],
                "fyi": [],
                "archive": []
            }

        # Prepare email summaries for Claude
        email_summaries = []
        for email in emails:
            email_summaries.append({
                "from": email.get("from", "Unknown"),
                "subject": email.get("subject", "No subject"),
                "snippet": email.get("snippet", "")[:200],
                "date": email.get("date", "Unknown")
            })

        prompt = f"""You are helping someone with ADHD organize their emails.

Categorize these emails into these categories:
🔴 urgent: Require immediate action (deadlines, urgent requests, problems)
🟡 needs_response: Needs a response but not urgent
📅 calendar: Events, meetings, invitations
💰 financial: Bills, payments, invoices, receipts
📰 newsletters: Newsletters, marketing, promotional
ℹ️ fyi: Informational, no action needed
🗑️ archive: Can be archived (confirmations, automated messages)

Emails to categorize:
{json.dumps(email_summaries, indent=2, ensure_ascii=False)}

Return ONLY a JSON object with this structure:
{{
  "urgent": [list of email indices],
  "needs_response": [list of email indices],
  "calendar": [list of email indices],
  "financial": [list of email indices],
  "newsletters": [list of email indices],
  "fyi": [list of email indices],
  "archive": [list of email indices]
}}
"""

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
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
                timeout=60
            )
            response.raise_for_status()

            result = response.json()
            content = result['content'][0]['text']

            # Extract JSON from response
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                categories = json.loads(json_match.group())

                # Map indices back to emails
                categorized = {}
                for category, indices in categories.items():
                    categorized[category] = [emails[i] for i in indices if i < len(emails)]

                return categorized
            else:
                print("⚠️ Could not parse categorization response")
                return self._default_categories(emails)

        except Exception as e:
            print(f"⚠️ Error categorizing emails: {str(e)}")
            return self._default_categories(emails)

    def _default_categories(self, emails: List[Dict]) -> Dict:
        """Fallback: put all emails in FYI category"""
        return {
            "urgent": [],
            "needs_response": [],
            "calendar": [],
            "financial": [],
            "newsletters": [],
            "fyi": emails,
            "archive": []
        }

    def check_all_accounts(self, accounts: List[str], hours: int = 24) -> Dict:
        """
        Check all email accounts and categorize emails
        """
        madrid_tz = pytz.timezone('Europe/Madrid')
        timestamp = datetime.now(madrid_tz).strftime("%Y-%m-%d %H:%M")

        results = {
            "timestamp": timestamp,
            "accounts": {}
        }

        for account in accounts:
            print(f"\n📧 Checking {account}...")
            emails = self.fetch_emails_via_gmail_api(account, hours)
            categorized = self.categorize_emails(emails)

            results["accounts"][account] = {
                "total": len(emails),
                "categories": categorized
            }

            # Print summary
            print(f"   Total: {len(emails)}")
            for category, items in categorized.items():
                if items:
                    print(f"   {category}: {len(items)}")

        return results

    def save_digest(self, results: Dict):
        """Save email digest to GitHub for M to read"""
        madrid_tz = pytz.timezone('Europe/Madrid')
        now = datetime.now(madrid_tz)
        filename = f"email-digest/{now.strftime('%Y-%m-%d-%H-%M')}.json"

        os.makedirs("email-digest", exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False, default=str)

        print(f"\n✅ Email digest saved to: {filename}")
        return filename


def main():
    """Main execution"""
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not set")
        return

    accounts = [
        "sarahpoer@gmail.com",
        "sarah@teatrometamorfosis.com",
        "info@teatrometamorfosis.com"
    ]

    checker = EmailChecker(api_key)
    results = checker.check_all_accounts(accounts, hours=24)
    checker.save_digest(results)

    print("\n✅ Email check complete!")


if __name__ == "__main__":
    main()
