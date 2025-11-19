#!/usr/bin/env python3
"""
SIMPLIFIED Morning Brief - No Gmail OAuth needed!
Claude will check email directly when you say "Good morning"
This script just pulls from GitHub and generates a brief template
"""

import sys
import os
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import config
    from github_integration import GitHubIntegration
    from brief_generator import BriefGenerator
except ImportError as e:
    print(f"⚠️  Import error: {e}")
    print("Run: pip3 install requests pytz")
    sys.exit(1)


class SimpleMorningBrief:
    def __init__(self):
        self.github = GitHubIntegration()
        self.generator = BriefGenerator()

    def run(self):
        """Run the morning brief - simplified version"""
        print("=" * 60)
        print("🌅 GENERATING MORNING BRIEF")
        print("=" * 60)

        # Step 1: Pull GitHub files
        print("\n📥 Pulling from GitHub...")
        todo_content = self._fetch_github_file(config.TODO_FILE)
        tracker_content = self._fetch_github_file(config.TRACKER_FILE)

        # Step 2: Generate brief (without email - Claude will add that)
        print("\n📝 Creating brief template...")
        brief_content = self._generate_brief(todo_content, tracker_content)

        # Step 3: Save locally and to GitHub
        print("\n💾 Saving brief...")
        self._save_local(brief_content)
        self._push_to_github(brief_content)

        print("\n" + "=" * 60)
        print("✅ BRIEF READY!")
        print("📍 Saved to: morning-briefs/MORNING_BRIEF_[today].md")
        print("=" * 60)

        # Return the brief content for Claude to use
        return brief_content

    def _fetch_github_file(self, file_path: str):
        """Fetch a file from GitHub"""
        try:
            content = self.github.get_file_content(file_path)
            if content:
                print(f"   ✓ {file_path}")
                return content
            else:
                print(f"   ⚠️  Failed to fetch {file_path}")
                return None
        except Exception as e:
            print(f"   ⚠️  Error: {str(e)}")
            return None

    def _generate_brief(self, todo_content, tracker_content):
        """Generate brief template"""
        # Empty email categories - Claude will fill this in
        empty_emails = {
            '🔴 Urgent Action Required': [],
            '🟡 Needs Response': [],
            '🔵 FYI/Read Later': [],
            '📅 Calendar/Events': [],
            '💰 Financial/Invoices': [],
            '📧 Newsletters/Promotions': [],
            '✅ Can Archive': []
        }

        brief = self.generator.generate_brief(
            todo_content,
            tracker_content,
            empty_emails,
            calendar_events=None
        )

        print("   ✓ Brief generated")
        return brief

    def _save_local(self, content):
        """Save local backup"""
        Path("backups").mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        filepath = f"backups/MORNING_BRIEF_{date_str}.md"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"   ✓ Local backup: {filepath}")

    def _push_to_github(self, content):
        """Push to GitHub"""
        try:
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"MORNING_BRIEF_{date_str}.md"
            file_path = f"{config.BRIEFS_FOLDER}/{filename}"

            commit_message = f"Morning brief - {datetime.now().strftime('%B %d, %Y')}"

            success = self.github.push_file(file_path, content, commit_message)

            if success:
                print(f"   ✓ Pushed to GitHub")
            else:
                print(f"   ⚠️  GitHub push failed (check token)")

        except Exception as e:
            print(f"   ⚠️  Error: {str(e)}")


def main():
    """Main entry point"""
    try:
        brief = SimpleMorningBrief()
        content = brief.run()

        # Print the brief so Claude can see it
        print("\n" + "=" * 60)
        print("BRIEF CONTENT:")
        print("=" * 60)
        print(content)

    except Exception as e:
        print(f"\n⚠️  Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
