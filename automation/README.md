# 🌅 Morning Brief Automation

**Automated daily morning briefs for ADHD-friendly life management**

---

## What This Does

Runs automatically every day at 11:30am CET to:
- ✅ Check Gmail and triage emails into 7 categories
- ✅ Pull TODO list and daily tracker from GitHub
- ✅ Generate comprehensive morning brief
- ✅ Push to GitHub for access by any Claude chat
- ✅ Clean up briefs older than 7 days

---

## Quick Start

1. **First time setup:** Follow `SETUP_GUIDE.md` (step-by-step instructions)
2. **Run manually anytime:** `./automation/morning-brief-now.sh`
3. **Check logs:** `cat automation/logs/morning_brief.log`

---

## Files

- `morning_brief.py` - Main orchestration script
- `github_integration.py` - GitHub API module
- `gmail_integration.py` - Gmail API module
- `brief_generator.py` - Brief formatting module
- `config.template.py` - Configuration template
- `config.py` - Your actual config (create from template, NOT committed)
- `morning-brief-now.sh` - Manual run script
- `SETUP_GUIDE.md` - Complete setup instructions
- `requirements.txt` - Python dependencies

---

## Email Categories

Emails are automatically sorted into:

1. 🔴 **Urgent Action Required** - needs response today
2. 🟡 **Needs Response** - not urgent but requires reply
3. 🔵 **FYI/Read Later** - informational only
4. 📅 **Calendar/Events** - invitations, scheduling
5. 💰 **Financial/Invoices** - money-related
6. 📧 **Newsletters/Promotions** - marketing, subscriptions
7. ✅ **Can Archive** - already handled or irrelevant

---

## Morning Brief Format

Each brief includes:
- 🔴 Top 5 urgent priorities from TODO
- 📧 Urgent emails requiring action
- 🟡 Emails needing response (not urgent)
- 📅 Today's calendar (if configured)
- 💊 Medication reminder
- 📊 Quick stats (email counts, task counts)

---

## Usage with Claude

**Morning routine:**
```
You: "Good morning! Pull my morning brief"
Claude: [pulls latest from GitHub, presents overview]
```

**Token efficient:** ~3-5K tokens vs 10-15K for live email check

**Update later:**
```
You: "Check my email again"
Claude: [does fresh Gmail check, ~5-10K tokens]
```

---

## Requirements

- Python 3.8+
- Gmail account with API access
- GitHub personal access token
- Dependencies: `pip3 install -r requirements.txt`

---

## Security

These files are in `.gitignore` and NEVER committed:
- `config.py` - Contains your tokens
- `credentials.json` - Gmail OAuth credentials
- `token.json` - Gmail authentication token
- `*.log` - Log files

**Keep your tokens safe!**

---

## Logs

- `logs/morning_brief.log` - Detailed execution logs
- `logs/cron.log` - Cron job execution logs
- `backups/` - Local backup copies of briefs

---

## Need Help?

See `SETUP_GUIDE.md` for:
- Complete setup instructions
- Troubleshooting guide
- Gmail API setup walkthrough
- Cron job configuration
- Cloud hosting options

---

**Built with 💚 for Sarah's ADHD-friendly Life Operating System**
