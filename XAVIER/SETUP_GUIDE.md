# Setup Guide - ADHD-Friendly Life OS Automation

**Time needed:** 30-45 minutes (one-time setup)
**Difficulty:** Beginner-friendly (step-by-step instructions)

---

## 📋 What You'll Need

Before starting, gather these:

- ✅ GitHub account
- ✅ Claude account (any tier works)
- ✅ Gmail account(s) you want to automate
- ✅ (Optional) Anthropic API key for news digest
- ✅ 30-45 minutes of focused time

---

## 🎯 Setup Overview

1. **GitHub Setup** (10 min) - Create repo, enable Actions
2. **Email Setup** (15 min) - App-specific passwords
3. **Configuration** (10 min) - Customize your settings
4. **Test & Deploy** (5 min) - Make sure it works!

---

## STEP 1: GitHub Repository Setup

### 1.1 Create Your Repository

**Option A: Fork Sarah's Repo** (Easiest)
1. Go to Sarah's GitHub repo (if she shared the link)
2. Click "Fork" button
3. Name it: `Life-Operating-System` or your own name
4. Click "Create fork"

**Option B: Create New Repo**
1. Go to https://github.com/new
2. Name: `Life-Operating-System` (or whatever you like)
3. **Important:** Make it **Private** (contains your personal data!)
4. Initialize with README
5. Click "Create repository"

### 1.2 Copy XAVIER Folder to Your Repo

**If you forked:**
- The XAVIER folder is already there!
- Copy contents from `XAVIER/` to your repo root

**If you created new:**
- Download XAVIER folder from Sarah
- Upload to your repo
- Or copy files one by one

### 1.3 Enable GitHub Actions

1. In your repo, go to **Settings** tab
2. Click **Actions** in left sidebar
3. Under "Actions permissions", select:
   - ✅ "Allow all actions and reusable workflows"
4. Click **Save**

### 1.4 Create GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. **Note:** "Life OS Automation"
4. **Expiration:** 90 days or no expiration
5. **Scopes:** Check these boxes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. Click **"Generate token"**
7. **COPY THE TOKEN** (you'll only see it once!)
8. Save it somewhere safe temporarily

---

## STEP 2: Email Setup (Gmail)

For EACH Gmail account you want to automate:

### 2.1 Enable IMAP

1. Open Gmail
2. Click gear icon → **"See all settings"**
3. Click **"Forwarding and POP/IMAP"** tab
4. Under "IMAP access", select **"Enable IMAP"**
5. Click **"Save Changes"**

### 2.2 Enable 2-Factor Authentication

**If you already have 2FA:** Skip to 2.3

**If you don't:**
1. Go to https://myaccount.google.com/security
2. Find "2-Step Verification"
3. Click **"Get Started"**
4. Follow the setup wizard (SMS or authenticator app)

### 2.3 Generate App-Specific Password

1. Go to https://myaccount.google.com/apppasswords
2. **Select app:** Mail
3. **Select device:** Other (Custom name)
4. **Name it:** "Life OS Automation"
5. Click **"Generate"**
6. **COPY THE 16-CHARACTER PASSWORD**
   - It looks like: `abcd efgh ijkl mnop`
   - **Remove the spaces:** `abcdefghijklmnop`
7. Save it temporarily

**Repeat 2.1-2.3 for each Gmail account!**

---

## STEP 3: GitHub Secrets Setup

Now add your passwords/tokens to GitHub Secrets (encrypted storage):

### 3.1 Navigate to Secrets

1. Go to your GitHub repo
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **"New repository secret"** (green button)

### 3.2 Add Required Secrets

**For each secret:**
- Click "New repository secret"
- Enter Name and Value
- Click "Add secret"

**Add these secrets:**

| Secret Name | Value | Where to get it |
|-------------|-------|-----------------|
| `GH_PAT` | Your GitHub token | Step 1.4 |
| `ANTHROPIC_API_KEY` | Your Anthropic API key | https://console.anthropic.com/settings/keys |
| `EMAIL_1_NAME` | Friendly name | e.g., "Personal" |
| `EMAIL_1_ADDRESS` | Gmail address | e.g., "you@gmail.com" |
| `EMAIL_1_PASSWORD` | App-specific password | Step 2.3 (no spaces!) |
| `EMAIL_1_MODE` | Triage mode | "standard" |

**For second email account (if you have one):**

| Secret Name | Value |
|-------------|-------|
| `EMAIL_2_NAME` | "Work" (or whatever) |
| `EMAIL_2_ADDRESS` | work@gmail.com |
| `EMAIL_2_PASSWORD` | App password (no spaces!) |
| `EMAIL_2_MODE` | "standard" |

**For third account (optional):**

| Secret Name | Value |
|-------------|-------|
| `EMAIL_3_NAME` | Name |
| `EMAIL_3_ADDRESS` | Email |
| `EMAIL_3_PASSWORD` | Password |
| `EMAIL_3_MODE` | "standard" |

**Note:** Passwords must have **NO SPACES**! Remove all spaces from the 16-character app password.

---

## STEP 4: File Setup

### 4.1 Copy Workflow Files

From `XAVIER/templates/`:

1. Copy `morning-brief.yml.template`
2. Create `.github/workflows/` folder in your repo
3. Rename to `morning-brief.yml` and save there
4. Same for `email-check.yml.template`

### 4.2 Create Your Core Files

**Create these files in your repo root:**

**`PERMANENT_TODO.md`** - Your task list
```markdown
# My TODO List

## 🔴 Urgent (Do Today)
- [ ] Example urgent task

## 🟡 This Week
- [ ] Example task for this week

## 🔵 This Month
- [ ] Example task for this month

## ✅ Completed
- [x] Setup Life OS automation!
```

**`DAILY_TRACKER_CURRENT.md`** - Track your day
```markdown
# Daily Tracker

## Today (Nov 21, 2025)

### Medications Taken:
- [Time and medication]

### Tasks Completed:
- [Tasks you completed]

### Wins:
- [Achievements today]

### Patterns/Notes:
- [Anything you noticed]
```

**`LIFE_OS_CURRENT.json`** - Your core context (optional)
```json
{
  "name": "Your Name",
  "timezone": "Your/Timezone",
  "adhd": true,
  "medications": ["Your meds"],
  "current_projects": ["Your projects"]
}
```

### 4.3 Customize Config

1. Open `XAVIER/templates/config.template.py`
2. Fill in your details:
   - GitHub repo name
   - Email accounts
   - Timezone
   - Medications
3. Save as `automation/config.py` in your repo
4. **Important:** Add to `.gitignore`:

```
# .gitignore file
automation/config.py
automation/token.json
automation/credentials.json
automation/*.log
```

### 4.4 Customize News Sources (Optional)

1. Open `XAVIER/templates/Global_Media_Database_v3.json`
2. Add/remove news sources you care about
3. Save as `Global_Media_Database_v3.json` in repo root

---

## STEP 5: Test the System

### 5.1 Manual Test Run

1. Go to your repo on GitHub
2. Click **"Actions"** tab
3. Click **"Morning Brief Automation"** workflow
4. Click **"Run workflow"** dropdown (right side)
5. Click **"Run workflow"** button (green)
6. Wait 2-3 minutes
7. Check for ✅ green checkmark

### 5.2 Check the Output

1. Go back to your repo **"Code"** tab
2. Look for new folders:
   - `morning-briefs/`
   - `news-digests/`
3. Open today's morning brief
4. Verify it includes:
   - ✅ Your TODO priorities
   - ✅ Email triage
   - ✅ News digest
   - ✅ Calendar

### 5.3 Test Email Check

1. Go to **Actions** tab
2. Click **"Email Check (On-Demand)"**
3. Run it manually
4. Check `automation/email_triage_results.json` appears

---

## STEP 6: Schedule Automation

The morning brief is already scheduled for 8:30 AM your timezone!

**To change the time:**

1. Edit `.github/workflows/morning-brief.yml`
2. Find the `cron` line:
```yaml
schedule:
  - cron: '30 7 * * *'  # 8:30 AM CET
```
3. Change to your preferred time:
   - Cron uses UTC time
   - Example: 9:00 AM EST = `'0 14 * * *'`
   - Use https://crontab.guru to convert times

---

## STEP 7: Access Your Brief

### Option A: "Fetch Brief Anywhere" (Easiest)

**Save this template in your phone's Notes/Keep:**

```
Hi! Please fetch my morning brief from GitHub:

Repository: [your-username]/[your-repo-name]
File: morning-briefs/MORNING_BRIEF_[today in YYYY-MM-DD].md

Use GitHub API:
URL: https://api.github.com/repos/[your-username]/[your-repo]/contents/morning-briefs/MORNING_BRIEF_[today].md
Auth: token [your-github-token]
Accept: application/vnd.github.v3.raw

Show me today's brief!
```

**To use:**
1. Open any Claude chat
2. Copy/paste this template
3. Get your brief in 5 seconds!

### Option B: iOS Shortcut (Best for iPhone)

See `XAVIER/docs/ios-shortcut-instructions.md`

### Option C: Web Bookmarklet (Best for Browser)

See `XAVIER/docs/web-bookmarklet.html`

---

## ✅ You're Done!

**What happens now:**

### Every Morning at 8:30 AM:
1. ✅ GitHub Actions runs automatically
2. ✅ Checks all your email accounts
3. ✅ Triages emails into categories
4. ✅ Fetches your TODO priorities
5. ✅ Generates AI news digest
6. ✅ Checks your calendar
7. ✅ Creates complete morning brief
8. ✅ Pushes to GitHub

### When You Wake Up:
1. Open Claude (any device)
2. Paste "Fetch Brief" template
3. Get complete overview in 5 seconds
4. Start your day with clarity!

---

## 🎨 Customization Ideas

### Add More Email Accounts:
Just add `EMAIL_3`, `EMAIL_4`, etc. to GitHub secrets

### Change Triage Categories:
Edit `automation/email_automation.py`

### Add Custom Tracking:
Edit `DAILY_TRACKER_CURRENT.md` template

### Choose Different News Sources:
Edit `Global_Media_Database_v3.json`

### Set Different Schedule:
Edit the cron schedule in workflow file

---

## 🐛 Troubleshooting

### Workflow Fails:
- Check GitHub Actions logs
- Verify all secrets are set correctly
- Check app-specific passwords have no spaces

### No Emails in Brief:
- Verify IMAP is enabled
- Check app-specific password is correct
- Make sure you have new emails in last 24 hours

### News Digest Empty:
- Verify ANTHROPIC_API_KEY is set
- Check you have credits in Anthropic account

### Calendar Not Working:
- Calendar integration is optional
- Requires additional Google Calendar API setup
- See `docs/calendar-setup.md` (if included)

---

## 📚 Next Steps

**After setup:**
1. Read `docs/HOW_IT_WORKS.md` to understand the system
2. Customize to your needs
3. Set up mobile access (iOS Shortcut or Bookmarklet)
4. Enjoy automated mornings!

**Need help?**
- Check `docs/TROUBLESHOOTING.md`
- Ask Claude! (Claude Code can help debug)
- Adjust and experiment - it's yours now!

---

## 💚 Welcome to the ADHD-Friendly Life!

You've just set up automation that will:
- Save you hours of decision fatigue
- Never forget important emails
- Give you clarity every morning
- Work silently in the background

**Now go live your life while the robots handle the logistics!** ✨

---

**Questions? Stuck?** Ask Claude to help debug - seriously! 🤖

**Enjoying the system?** Share with other ADHD friends! 💚
