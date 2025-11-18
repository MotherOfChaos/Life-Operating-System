# 🌅 Morning Briefs

This folder contains automated morning briefs generated daily at 11:30am CET.

## What's Here

Each morning, the automation script creates a file named:
```
MORNING_BRIEF_YYYY-MM-DD.md
```

For example: `MORNING_BRIEF_2025-11-18.md`

## Brief Contents

Each brief includes:
- 🔴 Top 5 urgent priorities from TODO list
- 📧 Urgent emails requiring action today
- 🟡 Emails needing response (not urgent)
- 📅 Today's calendar events
- 💊 Medication reminders
- 📊 Quick stats (email counts, task counts)

## Automatic Cleanup

Briefs older than 7 days are automatically deleted to keep this folder tidy.

## Access from Claude

Any Claude chat instance can pull the latest morning brief by reading files from GitHub.

**Usage:**
```
You: "Good morning! Show me my morning brief"
Claude: [pulls latest brief and presents overview]
```

Token-efficient way to start your day! 💚

---

**Automation:** See `/automation/` folder for the scripts that generate these briefs.
