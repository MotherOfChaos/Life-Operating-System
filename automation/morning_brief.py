#!/usr/bin/env python3
"""
Morning Brief Automation Script
Runs daily at 11:30am to generate comprehensive morning brief

Author: Created for Sarah's ADHD-friendly Life Operating System
"""

import sys
import os
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import config
    from github_integration import GitHubIntegration
    from gmail_integration import GmailIntegration
    from brief_generator import BriefGenerator
except ImportError as e:
    print(f"⚠️  Import error: {e}")
    print("Make sure config.py exists and all modules are in place")
    sys.exit(1)


class MorningBriefRunner:
    def __init__(self):
        self.log_file = "automation/logs/morning_brief.log"
        self.backup_dir = "automation/backups"
        self.github = GitHubIntegration()
        self.gmail = GmailIntegration()
        self.generator = BriefGenerator()

    def log(self, message: str, print_also: bool = True):
        """Log message to file and optionally print"""
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        log_message = f"[{timestamp}] {message}"

        if print_also:
            print(log_message)

        # Ensure log directory exists
        Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)

        # Append to log file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + "\n")

    def run(self):
        """Main execution flow"""
        self.log("=" * 60)
        self.log("🌅 MORNING BRIEF AUTOMATION STARTED")
        self.log("=" * 60)

        # Step 1: Check Gmail
        self.log("📧 Checking Gmail...")
        email_categories = self._fetch_and_categorize_emails()

        # Step 2: Pull GitHub files
        self.log("📥 Pulling GitHub files...")
        todo_content = self._fetch_github_file(config.TODO_FILE)
        tracker_content = self._fetch_github_file(config.TRACKER_FILE)

        # Step 3: Generate brief
        self.log("📝 Creating brief...")
        brief_content = self._generate_brief(
            todo_content,
            tracker_content,
            email_categories
        )

        # Step 4: Save backup locally
        self.log("💾 Saving local backup...")
        backup_path = self._save_backup(brief_content)

        # Step 5: Push to GitHub
        self.log("⬆️  Pushing to GitHub...")
        push_success = self._push_to_github(brief_content)

        # Step 6: Clean old briefs
        if push_success:
            self.log("🗑️  Cleaning old briefs...")
            self._clean_old_briefs()

        # Final status
        self.log("=" * 60)
        if push_success:
            self.log("✅ MORNING BRIEF COMPLETED SUCCESSFULLY")
            self.log(f"📍 Brief available on GitHub")
        else:
            self.log("⚠️  BRIEF GENERATED BUT GITHUB PUSH FAILED")
            self.log(f"📍 Backup saved locally: {backup_path}")

        self.log("=" * 60)

        return push_success

    def _fetch_and_categorize_emails(self) -> dict:
        """Fetch and categorize emails from Gmail"""
        try:
            # Authenticate with Gmail
            if not self.gmail.authenticate():
                self.log("⚠️  Gmail authentication failed - skipping email section")
                return self._empty_email_categories()

            # Fetch recent emails
            emails = self.gmail.get_recent_emails(config.EMAIL_LOOKBACK_HOURS)

            if not emails:
                self.log("📭 No new emails found")
                return self._empty_email_categories()

            # Categorize
            categories = self.gmail.categorize_emails(emails)
            summary = self.generator.generate_email_summary(categories)
            self.log(f"✓ Emails categorized: {summary}")

            return categories

        except Exception as e:
            self.log(f"⚠️  Error with Gmail: {str(e)}")
            return self._empty_email_categories()

    def _empty_email_categories(self) -> dict:
        """Return empty email categories structure"""
        return {
            '🔴 Urgent Action Required': [],
            '🟡 Needs Response': [],
            '🔵 FYI/Read Later': [],
            '📅 Calendar/Events': [],
            '💰 Financial/Invoices': [],
            '📧 Newsletters/Promotions': [],
            '✅ Can Archive': []
        }

    def _fetch_github_file(self, file_path: str) -> str:
        """Fetch a file from GitHub"""
        try:
            content = self.github.get_file_content(file_path)
            if content:
                self.log(f"✓ Pulled {file_path}")
                return content
            else:
                self.log(f"⚠️  Failed to pull {file_path}")
                return None
        except Exception as e:
            self.log(f"⚠️  Error fetching {file_path}: {str(e)}")
            return None

    def _generate_brief(
        self,
        todo_content: str,
        tracker_content: str,
        email_categories: dict
    ) -> str:
        """Generate the morning brief"""
        try:
            brief = self.generator.generate_brief(
                todo_content,
                tracker_content,
                email_categories,
                calendar_events=None  # TODO: Add calendar integration
            )
            self.log("✓ Brief generated successfully")
            return brief
        except Exception as e:
            self.log(f"⚠️  Error generating brief: {str(e)}")
            raise

    def _save_backup(self, content: str) -> str:
        """Save brief to local backup"""
        try:
            # Ensure backup directory exists
            Path(self.backup_dir).mkdir(parents=True, exist_ok=True)

            # Generate filename
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"MORNING_BRIEF_{date_str}.md"
            filepath = os.path.join(self.backup_dir, filename)

            # Save file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            self.log(f"✓ Backup saved: {filepath}")
            return filepath

        except Exception as e:
            self.log(f"⚠️  Error saving backup: {str(e)}")
            return None

    def _push_to_github(self, content: str) -> bool:
        """Push brief to GitHub"""
        try:
            # Generate filename
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"MORNING_BRIEF_{date_str}.md"

            # Create briefs folder if it doesn't exist
            briefs_folder = config.BRIEFS_FOLDER
            file_path = f"{briefs_folder}/{filename}"

            # Push to GitHub
            commit_message = f"Morning brief - {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"

            success = self.github.push_file(file_path, content, commit_message)

            if success:
                self.log(f"✓ Pushed to GitHub: {file_path}")
            else:
                self.log(f"⚠️  Failed to push to GitHub")

            return success

        except Exception as e:
            self.log(f"⚠️  Error pushing to GitHub: {str(e)}")
            return False

    def _clean_old_briefs(self):
        """Delete briefs older than retention period"""
        try:
            deleted = self.github.delete_old_briefs(
                config.BRIEFS_FOLDER,
                config.BRIEF_RETENTION_DAYS
            )

            if deleted > 0:
                self.log(f"✓ Deleted {deleted} old brief(s)")
            else:
                self.log("✓ No old briefs to delete")

        except Exception as e:
            self.log(f"⚠️  Error cleaning old briefs: {str(e)}")


def main():
    """Main entry point"""
    try:
        runner = MorningBriefRunner()
        success = runner.run()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"⚠️  FATAL ERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
