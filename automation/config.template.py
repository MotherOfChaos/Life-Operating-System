"""
Configuration Template for Morning Brief Automation
Copy this file to config.py and fill in your credentials
NEVER commit config.py to GitHub!
"""

# GitHub Configuration
GITHUB_TOKEN = "your_github_token_here"
GITHUB_REPO = "MotherOfChaos/Life-Operating-System"
GITHUB_BRANCH = "main"  # or your preferred branch

# Gmail Configuration (will be set up during OAuth)
# You'll get these from Google Cloud Console
GMAIL_CLIENT_ID = "your_client_id_here.apps.googleusercontent.com"
GMAIL_CLIENT_SECRET = "your_client_secret_here"

# Google Calendar (optional)
CALENDAR_ENABLED = False  # Set to True after setting up Calendar API

# File paths in repository
TODO_FILE = "PERMANENT_TODO.md"
TRACKER_FILE = "SARAH_DAILY_TRACKER_CURRENT.md"
BRIEFS_FOLDER = "morning-briefs"

# Settings
TIMEZONE = "Europe/Berlin"  # CET/CEST
BRIEF_RETENTION_DAYS = 7  # Keep briefs for 7 days
EMAIL_LOOKBACK_HOURS = 24  # Check emails from last 24 hours

# Top priorities to show
TOP_PRIORITIES_COUNT = 5

# Email alert settings (optional)
SEND_ERROR_ALERTS = False
ALERT_EMAIL = "your_email@example.com"
