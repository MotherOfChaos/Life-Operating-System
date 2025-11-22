"""
Configuration Template for Life OS Automation
Copy this to automation/config.py and fill in your details
NEVER commit config.py to GitHub! (add to .gitignore)
"""

# ============================================================================
# GITHUB CONFIGURATION
# ============================================================================

GITHUB_TOKEN = "your_github_personal_access_token_here"
GITHUB_REPO = "your-username/your-repo-name"
GITHUB_BRANCH = "main"

# ============================================================================
# ANTHROPIC API CONFIGURATION (for news digest)
# ============================================================================

ANTHROPIC_API_KEY = "your_anthropic_api_key_here"
# Get one at: https://console.anthropic.com/settings/keys

# ============================================================================
# EMAIL ACCOUNTS (IMAP with App-Specific Passwords)
# ============================================================================

# Get app-specific passwords from: https://myaccount.google.com/apppasswords
# For each Gmail account:
#   1. Enable 2-factor authentication
#   2. Generate an app-specific password
#   3. Add it here (16 chars, no spaces)

EMAIL_ACCOUNTS = [
    # Example Personal Account
    {
        "name": "Personal",  # Friendly name for reports
        "email": "your.email@gmail.com",  # Your Gmail address
        "password": "your_app_specific_password",  # App-specific password (16 chars)
        "imap_server": "imap.gmail.com",  # Gmail IMAP server
        "triage_mode": "standard",  # "standard" or "custom"
        "lookback_hours": 24  # How far back to check
    },

    # Example Work Account (Google Workspace)
    {
        "name": "Work",
        "email": "your.work@company.com",
        "password": "your_work_app_password",
        "imap_server": "imap.gmail.com",
        "triage_mode": "standard",
        "lookback_hours": 24
    },

    # Add more accounts as needed...
]

# ============================================================================
# FILE PATHS IN REPOSITORY
# ============================================================================

TODO_FILE = "PERMANENT_TODO.md"
TRACKER_FILE = "DAILY_TRACKER_CURRENT.md"
BRIEFS_FOLDER = "morning-briefs"
NEWS_DIGESTS_FOLDER = "news-digests"

# ============================================================================
# SETTINGS
# ============================================================================

TIMEZONE = "Europe/Madrid"  # Your timezone (e.g., "America/New_York", "Asia/Tokyo")
BRIEF_RETENTION_DAYS = 7  # Keep briefs for 7 days
EMAIL_LOOKBACK_HOURS = 24  # Check emails from last 24 hours
TOP_PRIORITIES_COUNT = 5  # Number of top priorities to show

# ============================================================================
# MEDICATION REMINDERS (customize for yourself)
# ============================================================================

MEDICATIONS = [
    "Your medication here (e.g., Concerta 36mg)",
    # Add more as needed
]

# ============================================================================
# CALENDAR CONFIGURATION (optional)
# ============================================================================

CALENDAR_ENABLED = False  # Set to True after setting up Calendar API

# ============================================================================
# EMAIL ALERT SETTINGS (optional)
# ============================================================================

SEND_ERROR_ALERTS = False
ALERT_EMAIL = "your_email@example.com"

# ============================================================================
# NOTES FOR SETUP
# ============================================================================

"""
After filling this out:
1. Copy to automation/config.py
2. Add config.py to .gitignore
3. Test with: python automation/email_automation.py
4. Add secrets to GitHub Actions (see SETUP_GUIDE.md)
"""
