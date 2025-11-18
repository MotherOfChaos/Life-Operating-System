# 🌅 Morning Brief Automation - Setup Guide

**ADHD-friendly step-by-step instructions**

---

## What This Does

Every day at 11:30am (CET), this script automatically:
- ✅ Checks your Gmail and triages emails into 7 categories
- ✅ Pulls your TODO list and daily tracker from GitHub
- ✅ Creates a comprehensive morning brief
- ✅ Pushes it to GitHub so any Claude chat can read it
- ✅ Keeps last 7 days of briefs, deletes older ones

You can also run it manually anytime with: `./automation/morning-brief-now.sh`

---

## 📋 Prerequisites

You need:
1. **Python 3.8+** installed
2. **Git** installed
3. **A Google Account** with Gmail
4. **Your GitHub token** (you provided: `ghp_fPb...`)

---

## 🚀 Step-by-Step Setup

### STEP 1: Install Python Dependencies

Open terminal and run:

```bash
cd ~/Life-Operating-System/automation
pip3 install -r requirements.txt
```

If you get permission errors, try:
```bash
pip3 install --user -r requirements.txt
```

**✅ Verify it worked:** Run `python3 -c "import google.auth; print('OK')"` - should print "OK"

---

### STEP 2: Set Up Gmail API

This is the trickiest part but I'll guide you through it!

#### 2.1: Create Google Cloud Project

1. Go to: https://console.cloud.google.com/
2. Click **"Select a project"** → **"New Project"**
3. Name it: `Morning Brief Automation`
4. Click **"Create"**
5. Wait for it to create (you'll see a notification)

#### 2.2: Enable Gmail API

1. In the Cloud Console, click **"APIs & Services"** → **"Enable APIs and Services"**
2. Search for: `Gmail API`
3. Click on it, then click **"Enable"**
4. Do the same for: `Google Calendar API` (optional, for future calendar integration)

#### 2.3: Create OAuth Credentials

1. Go to: **"APIs & Services"** → **"Credentials"**
2. Click **"Create Credentials"** → **"OAuth client ID"**
3. If prompted to configure consent screen:
   - Click **"Configure Consent Screen"**
   - Choose **"External"** (unless you have Google Workspace)
   - Fill in:
     - App name: `Morning Brief`
     - User support email: your email
     - Developer contact: your email
   - Click **"Save and Continue"**
   - Click **"Add or Remove Scopes"**
   - Add: `gmail.readonly`
   - Click **"Save and Continue"**
   - Add yourself as a test user
   - Click **"Save and Continue"**

4. Back to **"Credentials"** → **"Create Credentials"** → **"OAuth client ID"**
   - Application type: **"Desktop app"**
   - Name: `Morning Brief Desktop`
   - Click **"Create"**

5. **IMPORTANT:** Download the credentials file
   - Click the download button (⬇️) next to your new OAuth client
   - This downloads a JSON file
   - **Rename it to:** `credentials.json`
   - **Move it to:** `~/Life-Operating-System/automation/credentials.json`

**✅ Verify:** Check that file exists: `ls ~/Life-Operating-System/automation/credentials.json`

---

### STEP 3: Configure the Script

#### 3.1: Create config.py

```bash
cd ~/Life-Operating-System/automation
cp config.template.py config.py
```

#### 3.2: Edit config.py

Open `config.py` in a text editor and fill in your credentials:

```bash
nano config.py
```

**Replace these values:**

```python
# GitHub Configuration
GITHUB_TOKEN = "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"  # Your token
GITHUB_REPO = "MotherOfChaos/Life-Operating-System"
GITHUB_BRANCH = "main"  # Change if needed

# Gmail Configuration - leave these as is, they're filled from credentials.json
# No changes needed here

# Google Calendar
CALENDAR_ENABLED = False  # Set to True later if you want calendar

# File paths in repository
TODO_FILE = "PERMANENT_TODO.md"
TRACKER_FILE = "SARAH_DAILY_TRACKER_CURRENT.md"
BRIEFS_FOLDER = "morning-briefs"

# Settings
TIMEZONE = "Europe/Berlin"
BRIEF_RETENTION_DAYS = 7
EMAIL_LOOKBACK_HOURS = 24
TOP_PRIORITIES_COUNT = 5
```

**Save and exit** (in nano: Ctrl+X, then Y, then Enter)

**🔒 SECURITY NOTE:** `config.py` is in `.gitignore` - your token won't be committed to GitHub!

---

### STEP 4: Test Gmail Authentication

Run this to authenticate with Gmail (one-time setup):

```bash
cd ~/Life-Operating-System/automation
python3 -c "from gmail_integration import GmailIntegration; g = GmailIntegration(); g.authenticate()"
```

**What happens:**
1. A browser window will open
2. Log in with your Gmail account
3. Grant permission to read your emails
4. You'll see "The authentication flow has completed"
5. Close the browser

**✅ Verify:** Check that `token.json` was created: `ls automation/token.json`

This creates `token.json` which stores your authentication. You won't need to log in again!

---

### STEP 5: Create morning-briefs Folder on GitHub

The script needs a folder to store briefs. Let's create it:

```bash
cd ~/Life-Operating-System
mkdir -p morning-briefs
echo "# Morning Briefs" > morning-briefs/README.md
echo "This folder contains automated morning briefs generated daily at 11:30am CET." >> morning-briefs/README.md
git add morning-briefs/
git commit -m "Add morning-briefs folder for automation"
git push
```

---

### STEP 6: Test the Script Manually

Before scheduling it, let's test it works:

```bash
cd ~/Life-Operating-System
./automation/morning-brief-now.sh
```

**You should see:**
```
🌅 Running morning brief now...

========================================================
🌅 MORNING BRIEF AUTOMATION STARTED
========================================================
📧 Checking Gmail...
✓ Emails categorized: 🔴 Urgent Action Required: 2 | 🟡 Needs Response: 5
📥 Pulling GitHub files...
✓ Pulled PERMANENT_TODO.md
✓ Pulled SARAH_DAILY_TRACKER_CURRENT.md
📝 Creating brief...
✓ Brief generated successfully
💾 Saving local backup...
✓ Backup saved: automation/backups/MORNING_BRIEF_2025-11-18.md
⬆️  Pushing to GitHub...
✓ Pushed to GitHub: morning-briefs/MORNING_BRIEF_2025-11-18.md
🗑️  Cleaning old briefs...
✓ No old briefs to delete
========================================================
✅ MORNING BRIEF COMPLETED SUCCESSFULLY
📍 Brief available on GitHub
========================================================

✅ Morning brief completed!
📍 Check GitHub for the latest brief
📋 Log file: automation/logs/morning_brief.log
```

**✅ Verify:** Check GitHub - you should see `morning-briefs/MORNING_BRIEF_[today's date].md`

**If it failed:** Check the log file:
```bash
cat automation/logs/morning_brief.log
```

---

### STEP 7: Set Up Automated Daily Run (Cron Job)

Now let's make it run automatically at 11:30am every day!

#### 7.1: Open crontab

```bash
crontab -e
```

If asked to choose an editor, pick `nano` (usually option 1)

#### 7.2: Add this line at the bottom

```bash
# Morning Brief Automation - runs daily at 11:30am CET
30 11 * * * cd ~/Life-Operating-System && ./automation/morning-brief-now.sh >> automation/logs/cron.log 2>&1
```

**Save and exit** (Ctrl+X, Y, Enter)

#### 7.3: Verify cron is set

```bash
crontab -l
```

You should see your cron job listed.

**✅ Done!** The script will now run every day at 11:30am (as long as your computer is on).

---

### STEP 8: Keep Your Computer Running (Optional)

**Problem:** Cron only runs when your computer is on.

**Solutions:**

#### Option A: Keep Your Computer On
- Disable sleep/hibernation in system settings
- Keep it plugged in
- **Best for:** If you have a dedicated computer or laptop you keep on

#### Option B: Use a Cloud Server (Recommended for reliability)

**Free/Cheap options:**

1. **Oracle Cloud (FREE tier)**
   - Always-on Linux VM
   - Completely free forever
   - Tutorial: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm

2. **Raspberry Pi**
   - One-time cost ~$50
   - Runs 24/7 with minimal power
   - Setup similar to above

3. **AWS EC2 (Free tier for 12 months)**
   - t2.micro instance
   - Free for first year

**For cloud setup:** You'll need to:
1. Install Python on the server
2. Copy the automation scripts
3. Set up the cron job
4. Keep credentials secure

**Want help with this?** Let me know and I can guide you through cloud setup!

---

## 🎯 Usage

### Daily Automatic Run
- ✅ Happens automatically at 11:30am CET
- ✅ No action needed from you
- ✅ Check GitHub for the brief: `morning-briefs/MORNING_BRIEF_[date].md`
- ✅ Check logs if you want: `automation/logs/morning_brief.log`

### Manual Run
Run anytime you want a fresh brief:

```bash
cd ~/Life-Operating-System
./automation/morning-brief-now.sh
```

Useful if:
- You wake up before 11:30am
- You want updated email info
- You want to test the system

### With Claude Chat

**Morning routine:**
1. Say to Claude: "Good morning! Pull my morning brief"
2. Claude pulls latest files from GitHub (including your brief)
3. Claude presents your overview
4. **Token efficient:** Uses ~3-5K tokens instead of 10-15K

**Update emails later:**
1. Say: "Check my email again" or "Refresh email"
2. Claude does fresh Gmail check
3. Get latest updates

---

## 🐛 Troubleshooting

### Gmail Authentication Issues

**Problem:** "Gmail authentication failed"

**Solutions:**
1. Make sure `credentials.json` is in the right place
2. Delete `token.json` and re-authenticate: `rm automation/token.json` then run the auth test again
3. Check that Gmail API is enabled in Google Cloud Console
4. Make sure you granted permission during OAuth

### GitHub Push Failed

**Problem:** "Failed to push to GitHub"

**Solutions:**
1. Check your GitHub token is correct in `config.py`
2. Verify the token has `repo` scope permissions
3. Make sure `morning-briefs/` folder exists on GitHub
4. Check your internet connection

### Script Won't Run

**Problem:** Permission denied

**Solution:**
```bash
chmod +x ~/Life-Operating-System/automation/morning-brief-now.sh
```

### Cron Job Not Running

**Check cron logs:**
```bash
cat automation/logs/cron.log
```

**Common issues:**
- Computer was asleep/off at 11:30am
- Path issues (make sure to use full paths in crontab)
- Python not in PATH for cron

### No Emails Showing Up

**Problem:** Email categories are empty

**Possible causes:**
1. No emails in last 24 hours (check `EMAIL_LOOKBACK_HOURS` in config)
2. Gmail API quota exceeded (unlikely with daily use)
3. Authentication expired (re-run auth test)

---

## 📁 File Structure

```
Life-Operating-System/
├── automation/
│   ├── config.py                    # Your credentials (NOT committed)
│   ├── config.template.py           # Template for config
│   ├── morning_brief.py             # Main script
│   ├── github_integration.py        # GitHub API module
│   ├── gmail_integration.py         # Gmail API module
│   ├── brief_generator.py           # Brief formatting module
│   ├── morning-brief-now.sh         # Manual run script
│   ├── requirements.txt             # Python dependencies
│   ├── credentials.json             # Gmail OAuth (NOT committed)
│   ├── token.json                   # Gmail token (NOT committed)
│   ├── logs/
│   │   ├── morning_brief.log        # Detailed logs
│   │   └── cron.log                 # Cron execution logs
│   └── backups/
│       └── MORNING_BRIEF_*.md       # Local backup copies
├── morning-briefs/
│   └── MORNING_BRIEF_*.md           # Pushed to GitHub
├── PERMANENT_TODO.md
└── SARAH_DAILY_TRACKER_CURRENT.md
```

---

## 🔐 Security Notes

**Protected files (in .gitignore):**
- `automation/config.py` - Contains your GitHub token
- `automation/token.json` - Gmail authentication
- `automation/credentials.json` - Gmail OAuth credentials
- `automation/*.log` - Log files

**✅ These will NEVER be committed to GitHub**

**⚠️ NEVER share:**
- Your GitHub token
- Your `credentials.json`
- Your `token.json`

If you accidentally expose your GitHub token:
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Delete the old token
3. Create a new one
4. Update `config.py`

---

## 🚀 Future Enhancements

Want to add these later?

1. **Google Calendar Integration**
   - Set `CALENDAR_ENABLED = True` in config
   - Follow similar OAuth setup for Calendar API
   - Brief will show today's events

2. **Email to Sarah on Failure**
   - Set `SEND_ERROR_ALERTS = True`
   - Add your email to `ALERT_EMAIL`
   - Requires SMTP setup (can add if you want)

3. **More Categories**
   - Edit `_determine_category()` in `gmail_integration.py`
   - Add your own keyword rules

4. **Slack/Discord Notifications**
   - Get brief posted to Slack/Discord
   - Requires webhook setup

**Want any of these?** Just ask!

---

## ✅ Quick Reference

**Test the system:**
```bash
./automation/morning-brief-now.sh
```

**Check logs:**
```bash
tail -f automation/logs/morning_brief.log
```

**Check if cron is running:**
```bash
crontab -l
```

**View latest brief locally:**
```bash
cat automation/backups/MORNING_BRIEF_$(date +%Y-%m-%d).md
```

**Re-authenticate Gmail:**
```bash
rm automation/token.json
python3 -c "from gmail_integration import GmailIntegration; g = GmailIntegration(); g.authenticate()"
```

---

## 🆘 Need Help?

If you get stuck:

1. **Check the logs first:** `cat automation/logs/morning_brief.log`
2. **Run manually to see errors:** `./automation/morning-brief-now.sh`
3. **Ask Claude for help** - I can debug with you!
4. **Send me the error message** from the log file

**I'm here to help!** This is designed to be ADHD-friendly, so don't hesitate to ask if something is confusing. 💚

---

**You've got this!** 🚀
