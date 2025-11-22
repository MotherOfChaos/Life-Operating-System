#!/usr/bin/env python3
"""
Multi-Account Email Automation with IMAP
Supports multiple Gmail accounts (including Google Workspace)
Can triage emails differently per account
Token-efficient: runs once, saves results
"""

import os
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass
from imap_tools import MailBox, AND, OR
import json


@dataclass
class EmailAccount:
    """Configuration for a single email account"""
    name: str  # Friendly name (e.g., "Personal", "Work")
    email: str  # Email address
    password: str  # App-specific password
    imap_server: str  # Usually "imap.gmail.com"
    triage_mode: str  # "standard" or "artist_database"
    lookback_hours: int = 24  # How far back to check


@dataclass
class EmailMessage:
    """Simplified email message"""
    from_email: str
    from_name: str
    subject: str
    snippet: str
    received: datetime
    category: str = ""
    importance: str = ""


class MultiAccountEmailChecker:
    """Check multiple email accounts and triage messages"""

    # Standard triage categories
    STANDARD_CATEGORIES = {
        "urgent": "🔴 Urgent Action Required",
        "response": "🟡 Needs Response",
        "fyi": "🔵 FYI/Read Later",
        "calendar": "📅 Calendar/Events",
        "financial": "💰 Financial/Invoices",
        "newsletter": "📧 Newsletters/Promotions",
        "archive": "✅ Can Archive"
    }

    # Work/artist triage categories (different from personal)
    WORK_CATEGORIES = {
        "urgent": "🔴 Urgent Work Action",
        "artist_inquiry": "🎭 Artist Inquiry",
        "provider_info": "🏢 Provider/Venue Info",
        "contract": "📄 Contract/Legal",
        "financial": "💰 Financial",
        "calendar": "📅 Events/Meetings",
        "archive": "✅ Can Archive"
    }

    def __init__(self, accounts: List[EmailAccount]):
        self.accounts = accounts
        self.results = {}

    def check_all_accounts(self) -> Dict:
        """Check all configured email accounts"""
        print("\n" + "=" * 60)
        print("📧 MULTI-ACCOUNT EMAIL CHECK")
        print("=" * 60)

        for account in self.accounts:
            print(f"\n📥 Checking {account.name} ({account.email})...")
            try:
                emails = self._check_account(account)
                self.results[account.name] = {
                    "account": account.email,
                    "mode": account.triage_mode,
                    "emails": emails,
                    "checked_at": datetime.now().isoformat()
                }
                print(f"   ✓ Found {len(emails)} emails")
            except Exception as e:
                print(f"   ⚠️  Error: {str(e)}")
                self.results[account.name] = {
                    "account": account.email,
                    "error": str(e),
                    "checked_at": datetime.now().isoformat()
                }

        return self.results

    def _check_account(self, account: EmailAccount) -> List[EmailMessage]:
        """Check a single email account via IMAP"""
        emails = []

        # Calculate lookback date
        since_date = datetime.now() - timedelta(hours=account.lookback_hours)

        # Connect to IMAP server
        with MailBox(account.imap_server).login(account.email, account.password) as mailbox:
            # Fetch unread emails from lookback period
            for msg in mailbox.fetch(
                AND(date_gte=since_date.date()),
                mark_seen=False  # Don't mark as read
            ):
                email_msg = EmailMessage(
                    from_email=msg.from_ or "",
                    from_name=self._extract_name(msg.from_ or ""),
                    subject=msg.subject or "(no subject)",
                    snippet=self._get_snippet(msg),
                    received=msg.date or datetime.now()
                )

                # Categorize based on account's triage mode
                if account.triage_mode == "artist_database":
                    email_msg = self._categorize_work_email(email_msg, msg)
                else:
                    email_msg = self._categorize_standard_email(email_msg, msg)

                emails.append(email_msg)

        # Sort by importance and date
        emails.sort(key=lambda x: (
            0 if x.category == "urgent" else 1,
            -x.received.timestamp()
        ))

        return emails

    def _extract_name(self, from_field: str) -> str:
        """Extract name from email From field"""
        if '<' in from_field:
            return from_field.split('<')[0].strip().strip('"')
        return from_field

    def _get_snippet(self, msg) -> str:
        """Get email preview snippet"""
        try:
            # Try to get plain text first
            text = msg.text or msg.html or ""
            # Take first 100 chars, strip whitespace
            snippet = ' '.join(text.split())[:100]
            return snippet if snippet else "(no preview)"
        except:
            return "(no preview)"

    def _categorize_standard_email(self, email: EmailMessage, raw_msg) -> EmailMessage:
        """Categorize personal email into standard categories"""
        subject_lower = email.subject.lower()
        from_lower = email.from_email.lower()
        snippet_lower = email.snippet.lower()

        # Check for urgent keywords
        urgent_keywords = ['urgent', 'asap', 'immediately', 'action required', 'deadline']
        if any(kw in subject_lower or kw in snippet_lower for kw in urgent_keywords):
            email.category = "urgent"
            email.importance = "high"
            return email

        # Check for calendar/event
        calendar_keywords = ['invitation', 'meeting', 'event', 'rsvp', 'calendar', 'invite']
        if any(kw in subject_lower for kw in calendar_keywords):
            email.category = "calendar"
            return email

        # Check for financial
        financial_keywords = ['invoice', 'payment', 'bill', 'transaction', 'receipt', 'bank']
        if any(kw in subject_lower or kw in from_lower for kw in financial_keywords):
            email.category = "financial"
            return email

        # Check for newsletters/promotions
        if 'unsubscribe' in snippet_lower or 'noreply' in from_lower:
            email.category = "newsletter"
            return email

        # Check if it needs a response (questions, requests)
        response_keywords = ['question', '?', 'let me know', 'please confirm', 'can you']
        if any(kw in snippet_lower for kw in response_keywords):
            email.category = "response"
            return email

        # Default to FYI
        email.category = "fyi"
        return email

    def _categorize_work_email(self, email: EmailMessage, raw_msg) -> EmailMessage:
        """Categorize work email (with artist/provider detection)"""
        subject_lower = email.subject.lower()
        from_lower = email.from_email.lower()
        snippet_lower = email.snippet.lower()

        # Check for urgent
        urgent_keywords = ['urgent', 'asap', 'deadline', 'today']
        if any(kw in subject_lower or kw in snippet_lower for kw in urgent_keywords):
            email.category = "urgent"
            email.importance = "high"
            return email

        # Check for artist inquiries
        artist_keywords = ['artist', 'performer', 'show', 'performance', 'booking', 'availability']
        if any(kw in subject_lower or kw in snippet_lower for kw in artist_keywords):
            email.category = "artist_inquiry"
            email.importance = "high"
            # Mark for artist database extraction
            email.extract_to_database = True
            return email

        # Check for provider/venue info
        provider_keywords = ['venue', 'theater', 'theatre', 'space', 'equipment', 'rental']
        if any(kw in subject_lower or kw in snippet_lower for kw in provider_keywords):
            email.category = "provider_info"
            email.extract_to_database = True
            return email

        # Check for contracts
        contract_keywords = ['contract', 'agreement', 'legal', 'terms']
        if any(kw in subject_lower for kw in contract_keywords):
            email.category = "contract"
            email.importance = "high"
            return email

        # Check for financial
        financial_keywords = ['invoice', 'payment', 'budget']
        if any(kw in subject_lower for kw in financial_keywords):
            email.category = "financial"
            return email

        # Check for calendar
        calendar_keywords = ['meeting', 'event', 'calendar']
        if any(kw in subject_lower for kw in calendar_keywords):
            email.category = "calendar"
            return email

        # Default to archive
        email.category = "archive"
        return email

    def generate_triage_report(self) -> str:
        """Generate formatted triage report for morning brief"""
        report = ""

        for account_name, data in self.results.items():
            if "error" in data:
                report += f"## ⚠️ {account_name}\n\n"
                report += f"Error checking account: {data['error']}\n\n"
                continue

            emails = data.get("emails", [])
            mode = data.get("mode", "standard")

            report += f"## 📧 {account_name} ({data['account']})\n\n"

            if not emails:
                report += "_No new emails in the last 24 hours_\n\n"
                continue

            # Get appropriate categories for this account
            categories = self.WORK_CATEGORIES if mode == "artist_database" else self.STANDARD_CATEGORIES

            # Group emails by category
            categorized = {}
            for email in emails:
                cat = email.category
                if cat not in categorized:
                    categorized[cat] = []
                categorized[cat].append(email)

            # Show urgent first
            if "urgent" in categorized:
                report += f"### {categories['urgent']}\n\n"
                for email in categorized["urgent"]:
                    report += f"- **{email.from_name}**: {email.subject}\n"
                    report += f"  _{email.snippet}_\n"
                    report += f"  _{email.received.strftime('%I:%M %p')}_\n\n"

            # Show other important categories
            priority_order = ["artist_inquiry", "provider_info", "contract", "response", "calendar", "financial"]
            for cat in priority_order:
                if cat in categorized and cat != "urgent":
                    count = len(categorized[cat])
                    report += f"### {categories.get(cat, cat)}: {count} email(s)\n\n"
                    # Show top 3
                    for email in categorized[cat][:3]:
                        report += f"- {email.from_name}: {email.subject}\n"
                    if count > 3:
                        report += f"- _...and {count - 3} more_\n"
                    report += "\n"

            # Summary stats
            report += f"**Total new emails:** {len(emails)}\n\n"

        report += "---\n\n"
        return report

    def save_results(self, filepath: str = "email_triage_results.json"):
        """Save results as JSON for artist database extraction later"""
        # Convert EmailMessage objects to dicts
        json_results = {}
        for account_name, data in self.results.items():
            if "emails" in data:
                data["emails"] = [
                    {
                        "from_email": e.from_email,
                        "from_name": e.from_name,
                        "subject": e.subject,
                        "snippet": e.snippet,
                        "received": e.received.isoformat(),
                        "category": e.category,
                        "importance": e.importance,
                        "extract_to_database": getattr(e, 'extract_to_database', False)
                    }
                    for e in data["emails"]
                ]
            json_results[account_name] = data

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Results saved to {filepath}")


def load_accounts_from_env() -> List[EmailAccount]:
    """Load email accounts from environment variables (GitHub Actions secrets)"""
    accounts = []

    # Account 1 (Personal - from env or config)
    if os.getenv('EMAIL_1_ADDRESS'):
        accounts.append(EmailAccount(
            name=os.getenv('EMAIL_1_NAME', 'Personal'),
            email=os.getenv('EMAIL_1_ADDRESS'),
            password=os.getenv('EMAIL_1_PASSWORD'),
            imap_server=os.getenv('EMAIL_1_IMAP', 'imap.gmail.com'),
            triage_mode=os.getenv('EMAIL_1_MODE', 'standard'),
            lookback_hours=int(os.getenv('EMAIL_1_LOOKBACK', '24'))
        ))

    # Account 2 (Work - from env or config)
    if os.getenv('EMAIL_2_ADDRESS'):
        accounts.append(EmailAccount(
            name=os.getenv('EMAIL_2_NAME', 'Work'),
            email=os.getenv('EMAIL_2_ADDRESS'),
            password=os.getenv('EMAIL_2_PASSWORD'),
            imap_server=os.getenv('EMAIL_2_IMAP', 'imap.gmail.com'),
            triage_mode=os.getenv('EMAIL_2_MODE', 'artist_database'),
            lookback_hours=int(os.getenv('EMAIL_2_LOOKBACK', '24'))
        ))

    # Account 3 (optional - from env or config)
    if os.getenv('EMAIL_3_ADDRESS'):
        accounts.append(EmailAccount(
            name=os.getenv('EMAIL_3_NAME', 'Other'),
            email=os.getenv('EMAIL_3_ADDRESS'),
            password=os.getenv('EMAIL_3_PASSWORD'),
            imap_server=os.getenv('EMAIL_3_IMAP', 'imap.gmail.com'),
            triage_mode=os.getenv('EMAIL_3_MODE', 'standard'),
            lookback_hours=int(os.getenv('EMAIL_3_LOOKBACK', '24'))
        ))

    # If no env vars, try loading from config.py
    if not accounts:
        try:
            import config
            if hasattr(config, 'EMAIL_ACCOUNTS'):
                for acc_config in config.EMAIL_ACCOUNTS:
                    accounts.append(EmailAccount(**acc_config))
        except ImportError:
            pass

    return accounts


def main():
    """Standalone test mode"""
    print("🔍 EMAIL AUTOMATION - TEST MODE")

    accounts = load_accounts_from_env()

    if not accounts:
        print("⚠️  No email accounts configured!")
        print("Set environment variables or add EMAIL_ACCOUNTS to config.py")
        sys.exit(1)

    print(f"Found {len(accounts)} account(s) to check")

    checker = MultiAccountEmailChecker(accounts)
    checker.check_all_accounts()

    print("\n" + "=" * 60)
    print("📊 TRIAGE REPORT")
    print("=" * 60)

    report = checker.generate_triage_report()
    print(report)

    # Save results (JSON)
    checker.save_results()

    # Save readable report (Markdown)
    from datetime import datetime
    report_file = f"email_check_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Email Check - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(report)
    print(f"\n💾 Readable report saved: {report_file}")


if __name__ == "__main__":
    main()
