# What's Included in This Package

**Complete ADHD-Friendly Life OS Automation System**

---

## 📂 Folder Structure

```
XAVIER/
├── README.md                    ← START HERE!
├── SETUP_GUIDE.md              ← Step-by-step setup (30 min)
├── WHATS_INCLUDED.md           ← This file
│
├── automation/                  ← All automation scripts
│   ├── email_automation.py
│   ├── brief_generator.py
│   ├── news_digest_generator.py
│   ├── news_fetcher.py
│   ├── github_integration.py
│   ├── github_actions_morning_brief_with_email.py
│   ├── artist_database_extractor.py
│   ├── check-emails-now.sh
│   ├── run-morning-brief.sh
│   └── requirements.txt
│
├── templates/                   ← Customize these for yourself
│   ├── config.template.py
│   ├── morning-brief.yml.template
│   ├── email-check.yml.template
│   └── Global_Media_Database_v3.json
│
├── docs/                        ← Documentation
│   ├── HOW_IT_WORKS.md
│   └── FETCH_BRIEF_ANYWHERE.md
│
└── examples/                    ← (Future: example configs)
```

---

## 🎁 Core Features Included

### 1. Morning Brief Automation
- **What:** Complete daily overview generated at 8:30 AM
- **Includes:** TODO priorities, email triage, news digest, calendar
- **File:** `automation/brief_generator.py`
- **Setup:** See SETUP_GUIDE.md

### 2. Multi-Account Email Automation
- **What:** Check unlimited Gmail accounts, categorize emails
- **Categories:** Urgent, Needs Response, FYI, Calendar, Financial, Newsletters
- **File:** `automation/email_automation.py`
- **Setup:** Requires app-specific passwords (see SETUP_GUIDE.md)

### 3. AI News Digest
- **What:** Summarize news from your chosen sources
- **Powered by:** Anthropic Claude API
- **File:** `automation/news_digest_generator.py`
- **Setup:** Requires Anthropic API key

### 4. Calendar Integration
- **What:** Smart filtering - hide recurring noise, show real appointments
- **Filters:** All-day events, "notes" events, "baja medica", etc.
- **File:** Part of `brief_generator.py`
- **Setup:** Google Calendar API (optional)

### 5. GitHub Actions Workflows
- **What:** Runs automation in the cloud (free!)
- **Schedules:** Daily at 8:30 AM + on-demand email check
- **Files:** `templates/morning-brief.yml.template`, `email-check.yml.template`
- **Setup:** Copy to `.github/workflows/` folder

### 6. Mobile/Web Access
- **What:** Access your brief from any device
- **Methods:** "Fetch Brief" template, iOS Shortcut, Web Bookmarklet
- **Files:** `docs/FETCH_BRIEF_ANYWHERE.md`
- **Setup:** See docs

---

## 📄 Template Files (Customize These!)

### `config.template.py`
**What:** Your personal configuration
**Contains:**
- GitHub repo info
- Email account details
- Timezone settings
- Medication reminders
- Preferences

**How to use:** Copy to `automation/config.py` and fill in your details

### `morning-brief.yml.template`
**What:** GitHub Actions workflow for morning automation
**Runs:** Daily at 8:30 AM (customizable)
**How to use:** Copy to `.github/workflows/morning-brief.yml`

### `email-check.yml.template`
**What:** On-demand email checking
**Runs:** Whenever you want (manual trigger)
**How to use:** Copy to `.github/workflows/email-check.yml`

### `Global_Media_Database_v3.json`
**What:** News sources for AI digest
**Contains:** 151+ news sources (customize!)
**How to use:** Edit to add/remove sources you care about

---

## 🛠️ Automation Scripts

### Core Scripts:

**`email_automation.py`** (Multi-account email checker)
- Connects via IMAP
- Supports unlimited accounts
- Different triage modes per account
- Saves results to JSON

**`brief_generator.py`** (Morning brief creator)
- Pulls TODO from GitHub
- Formats email triage
- Includes news digest
- Smart calendar filtering
- Medication reminders

**`news_digest_generator.py`** (AI news summarizer)
- Fetches from media database
- Uses Claude API to summarize
- ADHD-friendly bullet points
- Token-efficient

**`github_integration.py`** (GitHub helper)
- Fetch files from repo
- Push updates
- Clean API wrapper

**`github_actions_morning_brief_with_email.py`** (Complete workflow)
- Orchestrates everything
- Runs in GitHub Actions
- Combines all components

### Helper Scripts:

**`check-emails-now.sh`** (Manual email check)
- Run anytime to check emails
- Local execution
- Quick results

**`run-morning-brief.sh`** (Manual brief generation)
- Generate brief on-demand
- Test locally
- Debug issues

**`artist_database_extractor.py`** (Bonus feature!)
- Extract artist/provider info from work emails
- AI-powered
- Builds databases automatically

---

## 📚 Documentation

### `README.md` (Start Here!)
- Overview of system
- Quick start guide
- Key features
- ADHD-friendly design

### `SETUP_GUIDE.md` (Step-by-Step Setup)
- 30-minute setup walkthrough
- GitHub configuration
- Email setup (app-specific passwords)
- Testing and deployment

### `docs/HOW_IT_WORKS.md` (Technical Deep Dive)
- System architecture
- Data flow diagrams
- Security model
- Token economics
- Customization points

### `docs/FETCH_BRIEF_ANYWHERE.md` (Mobile Access)
- "Fetch Brief" template
- Works in any Claude chat
- Mobile-friendly
- Quick access guide

---

## 🎨 Customization Examples

### Change Schedule:
Edit cron expression in workflow file
```yaml
- cron: '0 9 * * *'  # 9:00 AM UTC
```

### Add Email Account:
Add to `config.py`:
```python
{
    "name": "Another Account",
    "email": "another@gmail.com",
    "password": "app_password",
    "triage_mode": "standard"
}
```

### Change Triage Categories:
Edit keyword lists in `email_automation.py`:
```python
urgent_keywords = ['urgent', 'asap', 'my_custom_urgent_word']
```

### Add News Source:
Edit `Global_Media_Database_v3.json`:
```json
{
    "name": "My Favorite Site",
    "url": "https://example.com/rss",
    "category": "Tech"
}
```

---

## 🔐 What's NOT Included (For Privacy)

**Personal data removed:**
- ❌ Real email addresses
- ❌ Real passwords/tokens
- ❌ Personal TODO lists
- ❌ Personal tracking data
- ❌ Private calendar events

**You'll add your own:**
- Your GitHub token
- Your email accounts
- Your Anthropic API key
- Your preferences
- Your content

---

## 💾 File Sizes

**Small footprint:**
- Total code: ~50KB
- Templates: ~10KB
- Documentation: ~100KB
- **Total package: ~160KB**

**Your data over time:**
- Morning briefs: ~5KB/day × 7 days = 35KB
- News digests: ~3KB/day × 7 days = 21KB
- Email results: ~5KB/day = 5KB
- **Total active data: ~60KB** (stays small!)

---

## 🚀 What Happens After Setup

### Daily (Automatic):
- 8:30 AM: Brief generates
- Files pushed to your repo
- Ready when you wake up

### When You Access:
- Open Claude (any device)
- Paste "Fetch Brief" template
- Get complete overview
- Start your day!

### Throughout Day:
- Check email anytime (on-demand workflow)
- Track tasks/meds (in Claude chat)
- "Wrap up" at end of day
- Everything saved to GitHub

---

## 📈 Benefits You'll See

**Time Savings:**
- No more 14-step manual process
- 5-second brief access
- ~7 minutes saved daily

**Token Savings:**
- 90% reduction in daily usage
- ~35K tokens saved per day
- More conversations possible!

**Mental Savings:**
- No decision fatigue
- No forgotten emails
- Clear priorities
- Reduced anxiety

**ADHD-Specific:**
- Scannable format
- Automation reduces executive function load
- Nothing gets lost
- Works when you're overwhelmed

---

## ✅ Ready to Start?

1. Read `README.md` for overview
2. Follow `SETUP_GUIDE.md` step-by-step
3. Customize templates for yourself
4. Test and deploy
5. Enjoy automated mornings!

**30 minutes of setup = lifetime of clarity** ✨

---

**Welcome to the ADHD-friendly future!** 💚

*Built by Sarah, shared with love for Xavier and the ADHD community* 🌹
