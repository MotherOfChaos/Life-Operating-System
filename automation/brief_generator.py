"""
Morning Brief Generator
Creates ADHD-friendly morning briefs combining emails, todos, and tracker data
"""

from datetime import datetime
from typing import Dict, List, Optional
import re
import os

try:
    import config
except ImportError:
    # If config doesn't exist (like in GitHub Actions), use defaults
    class config:
        TIMEZONE = "Europe/Berlin"
        TOP_PRIORITIES_COUNT = 5


class BriefGenerator:
    def __init__(self):
        self.timezone = config.TIMEZONE
        self.top_priorities_count = config.TOP_PRIORITIES_COUNT

    def generate_brief(
        self,
        todo_content: Optional[str],
        tracker_content: Optional[str],
        email_categories: Dict[str, List[Dict]],
        calendar_events: Optional[List[Dict]] = None
    ) -> str:
        """
        Generate the complete morning brief
        Returns formatted markdown string
        """
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        timestamp = now.strftime("%I:%M %p %Z")

        # Build the brief
        brief = f"# 🌅 MORNING BRIEF - {date_str}\n\n"
        brief += f"**Generated:** {timestamp}\n\n"
        brief += "---\n\n"

        # Section 1: Top 5 Urgent Priorities
        brief += self._generate_priorities_section(todo_content)

        # Section 2: Urgent Emails
        brief += self._generate_urgent_emails_section(
            email_categories.get('🔴 Urgent Action Required', [])
        )

        # Section 3: Emails Needing Response
        brief += self._generate_response_emails_section(
            email_categories.get('🟡 Needs Response', [])
        )

        # Section 4: Calendar
        brief += self._generate_calendar_section(calendar_events)

        # Section 5: Medication Reminder
        brief += self._generate_medication_section()

        # Section 6: Quick Stats
        brief += self._generate_stats_section(email_categories, todo_content)

        # Footer
        brief += "---\n\n"
        brief += "**Token-efficient format. Scannable for ADHD. Ready to go.** 💚\n"

        return brief

    def _generate_priorities_section(self, todo_content: Optional[str]) -> str:
        """Extract top priorities from TODO file"""
        section = "## 🔴 TOP 5 URGENT PRIORITIES TODAY\n\n"

        if not todo_content:
            section += "⚠️ *Could not load PERMANENT_TODO.md - check manually*\n\n"
            section += "---\n\n"
            return section

        # Extract uncompleted tasks from ACTIVE TASKS section
        tasks = self._extract_active_tasks(todo_content)

        if not tasks:
            section += "✨ *No urgent tasks found - check PERMANENT_TODO.md*\n\n"
        else:
            # Show up to top N priorities
            for i, task in enumerate(tasks[:self.top_priorities_count], 1):
                section += f"{i}. {task}\n"

        section += "\n---\n\n"
        return section

    def _extract_active_tasks(self, todo_content: str) -> List[str]:
        """Extract active (uncompleted) tasks from TODO content"""
        tasks = []

        # Find the ACTIVE TASKS section (stops at next ## heading, not ###)
        active_section_match = re.search(
            r'## 🎯 ACTIVE TASKS.*?(?=\n##\s|\Z)',
            todo_content,
            re.DOTALL
        )

        if not active_section_match:
            # Try alternative pattern without emoji
            active_section_match = re.search(
                r'## ACTIVE TASKS.*?(?=\n##\s|\Z)',
                todo_content,
                re.DOTALL
            )

        if active_section_match:
            active_section = active_section_match.group(0)

            # Find uncompleted tasks (- [ ])
            uncompleted_tasks = re.findall(
                r'- \[ \] (.+)',
                active_section
            )

            tasks.extend(uncompleted_tasks)

        # Also check for urgent items added at bottom
        urgent_match = re.search(
            r'### Urgent.*?:.*?(?=###|##|\Z)',
            todo_content,
            re.DOTALL | re.IGNORECASE
        )

        if urgent_match:
            urgent_section = urgent_match.group(0)
            urgent_tasks = re.findall(
                r'- \[ \] (.+)',
                urgent_section
            )
            # Add urgent tasks to the beginning
            tasks = urgent_tasks + tasks

        return tasks

    def _generate_urgent_emails_section(self, urgent_emails: List[Dict]) -> str:
        """Generate urgent emails section"""
        section = "## 📧 URGENT EMAILS REQUIRING ACTION\n\n"

        if not urgent_emails:
            section += "✅ *No urgent emails - you're good!*\n\n"
        else:
            for email in urgent_emails:
                sender = self._clean_sender(email['from'])
                subject = email['subject']
                snippet = email['snippet'][:100] + "..." if len(email['snippet']) > 100 else email['snippet']
                time = email['date'].strftime("%I:%M %p")

                section += f"**From:** {sender}  \n"
                section += f"**Subject:** {subject}  \n"
                section += f"**Preview:** {snippet}  \n"
                section += f"**Received:** {time}\n\n"

        section += "---\n\n"
        return section

    def _generate_response_emails_section(self, response_emails: List[Dict]) -> str:
        """Generate emails needing response section"""
        section = "## 🟡 EMAILS NEEDING RESPONSE (Not Urgent)\n\n"

        count = len(response_emails)
        section += f"**Total:** {count} emails\n\n"

        if count == 0:
            section += "✅ *Inbox zero on responses!*\n\n"
        else:
            # Show top 3-5
            for email in response_emails[:5]:
                sender = self._clean_sender(email['from'])
                subject = email['subject']
                section += f"- **{sender}:** {subject}\n"

            if count > 5:
                section += f"\n*...and {count - 5} more*\n"

        section += "\n---\n\n"
        return section

    def _generate_calendar_section(self, calendar_events: Optional[List[Dict]]) -> str:
        """Generate calendar section with filtering"""
        section = "## 📅 TODAY'S CALENDAR\n\n"

        if calendar_events is None:
            section += "*Calendar integration not configured - check manually with Claude*\n\n"
        elif not calendar_events:
            section += "✨ *No scheduled events today*\n\n"
        else:
            # Filter calendar events
            filtered_events = self._filter_calendar_events(calendar_events)

            if not filtered_events:
                section += "✨ *No scheduled events today (after filtering)*\n\n"
            else:
                for event in filtered_events:
                    time = event.get('time', 'TBD')
                    title = event.get('title', 'Untitled Event')
                    section += f"- **{time}:** {title}\n"
                section += "\n"

        section += "---\n\n"
        return section

    def _filter_calendar_events(self, events: List[Dict]) -> List[Dict]:
        """
        Filter calendar events based on Sarah's preferences:
        - Exclude events with "notes" in title
        - Exclude all-day events
        - Exclude "Baja medica" events
        - Only show time-specific appointments
        """
        filtered = []

        for event in events:
            title = event.get('title', '').lower()
            is_all_day = event.get('all_day', False)
            time = event.get('time', '')

            # Skip if it contains "notes" (case insensitive)
            if 'notes' in title:
                continue

            # Skip if it contains "baja medica" (case insensitive)
            if 'baja medica' in title or 'baja médica' in title:
                continue

            # Skip if it's an all-day event
            if is_all_day:
                continue

            # Skip if there's no specific time
            if not time or time == 'TBD' or time.lower() == 'all day':
                continue

            # This event passed all filters
            filtered.append(event)

        return filtered

    def _generate_medication_section(self) -> str:
        """Generate medication reminder"""
        section = "## 💊 MEDICATION REMINDER\n\n"
        section += "- **Concerta 36mg** (take on waking)\n\n"
        section += "---\n\n"
        return section

    def _generate_stats_section(
        self,
        email_categories: Dict[str, List[Dict]],
        todo_content: Optional[str]
    ) -> str:
        """Generate quick stats section"""
        section = "## 📊 QUICK STATS\n\n"

        # Count urgent emails
        urgent_count = len(email_categories.get('🔴 Urgent Action Required', []))
        response_count = len(email_categories.get('🟡 Needs Response', []))

        # Count pending tasks
        task_count = 0
        if todo_content:
            tasks = self._extract_active_tasks(todo_content)
            task_count = len(tasks)

        section += f"- **Urgent emails:** {urgent_count}\n"
        section += f"- **Response needed:** {response_count}\n"
        section += f"- **Pending priority tasks:** {task_count}\n"
        section += f"- **Last generated:** {datetime.now().strftime('%I:%M %p')}\n\n"

        return section

    def _clean_sender(self, sender: str) -> str:
        """Clean sender email to show just name or email"""
        # Extract name if in format "Name <email@example.com>"
        match = re.match(r'(.*?)\s*<.*?>', sender)
        if match:
            name = match.group(1).strip()
            if name:
                return name

        # Otherwise return the email
        return sender

    def generate_email_summary(self, email_categories: Dict[str, List[Dict]]) -> str:
        """Generate a simple email summary for logging"""
        summary = []
        for category, emails in email_categories.items():
            count = len(emails)
            if count > 0:
                summary.append(f"{category}: {count}")

        return " | ".join(summary) if summary else "No emails"
