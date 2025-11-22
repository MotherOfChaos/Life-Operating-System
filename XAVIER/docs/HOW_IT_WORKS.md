# How It Works - Technical Overview

**For:** People who want to understand what's happening under the hood

---

## 🏗️ System Architecture

```
GitHub Actions (Cloud)          Your Devices
       |                              |
       |                              |
   [Schedule]                    [You wake up]
   8:30 AM Daily                      |
       |                              |
       v                              |
[Morning Brief Script]                |
       |                              |
       ├─> Check Emails (IMAP)        |
       ├─> Fetch TODO from GitHub     |
       ├─> Generate News (AI)         |
       ├─> Check Calendar             |
       |                              |
       v                              |
[Create Brief Markdown File]          |
       |                              |
       v                              |
[Push to GitHub Repo]                 |
       |                              |
       └──────────────────────────────┤
                                      |
                                 [Claude Chat]
                                      |
                                 [Read Brief]
                                      |
                                [You see it!]
```

---

## 🔄 The Daily Flow

### 1. Automated Generation (8:30 AM)

**What happens (on GitHub's servers):**

```python
# 1. Email Checking
for each_email_account:
    - Connect via IMAP
    - Fetch last 24 hours of emails
    - Categorize using keywords
    - Save to categories

# 2. TODO Fetching
- Pull PERMANENT_TODO.md from GitHub
- Extract top 5 urgent priorities
- Format for display

# 3. News Digest
- Read Global_Media_Database_v3.json
- Fetch articles from sources
- Use Claude API to summarize
- Create ADHD-friendly bullets

# 4. Calendar Check (if enabled)
- Connect to Google Calendar API
- Fetch today's events
- Filter out all-day/recurring noise
- Keep only real appointments

# 5. Combine Everything
- Build markdown file
- Save as morning-briefs/MORNING_BRIEF_[date].md
- Push to GitHub repo
```

**Result:** A static file sitting in your repo, ready to read!

### 2. You Access It (Anytime After 8:30 AM)

**Option A: "Fetch Brief" Template**
```
You → Paste template → Claude
Claude → Fetch file from GitHub → Read it → Show you
```

**Option B: iOS Shortcut**
```
You → Tap widget → Shortcut downloads file → Copies to clipboard
You → Paste in Claude → Claude shows it
```

**Option C: Web Bookmarklet**
```
You → Click bookmark → JavaScript fetches file → Injects into Claude
You → Click send → Claude shows it
```

---

## 🔐 Security Model

### What's Private:
- ✅ Your GitHub repo (private)
- ✅ GitHub Secrets (encrypted)
- ✅ Your email passwords (app-specific, revocable)
- ✅ Your personal files (never leave your repo)

### What Runs Where:
- **GitHub Actions:** Runs on GitHub's secure servers
- **Your Claude Chats:** Runs on Anthropic's servers
- **Your Files:** Stored in your private GitHub repo

### Data Flow:
```
Your Gmail → GitHub Actions (checks) → Your GitHub Repo → Claude (reads)
```

**Nothing is stored outside your control!**

---

## 💾 File Structure

```
your-repo/
├── .github/
│   └── workflows/
│       ├── morning-brief.yml      # Runs daily at 8:30 AM
│       └── email-check.yml        # On-demand email check
│
├── automation/
│   ├── email_automation.py        # Multi-account IMAP email checker
│   ├── brief_generator.py         # Creates morning brief
│   ├── news_digest_generator.py   # AI-powered news summarizer
│   ├── github_integration.py      # GitHub API helper
│   ├── config.py                  # Your settings (gitignored!)
│   └── requirements.txt           # Python dependencies
│
├── morning-briefs/
│   ├── MORNING_BRIEF_2025-11-21.md
│   ├── MORNING_BRIEF_2025-11-22.md
│   └── ... (keeps last 7 days)
│
├── news-digests/
│   ├── NEWS_DIGEST_2025-11-21.md
│   └── ... (keeps last 7 days)
│
├── PERMANENT_TODO.md              # Your task list
├── DAILY_TRACKER_CURRENT.md       # Daily tracking
└── Global_Media_Database_v3.json  # News sources
```

---

## ⚙️ Key Components

### 1. Email Automation (`email_automation.py`)

**Technology:** IMAP (Internet Message Access Protocol)

**How it works:**
```python
for account in email_accounts:
    # Connect via IMAP (standard email protocol)
    mailbox = MailBox(account.imap_server)
    mailbox.login(account.email, account.app_password)

    # Fetch recent emails
    emails = mailbox.fetch(since_date=yesterday)

    # Categorize using keyword matching
    for email in emails:
        if 'urgent' in subject or 'asap' in subject:
            category = 'urgent'
        elif '?' in body:
            category = 'needs_response'
        # ... etc

    # Save results
    results[account.name] = categorized_emails
```

**Why app-specific passwords?**
- More secure than real password
- Can be revoked if compromised
- Allows IMAP access even with 2FA

### 2. News Digest (`news_digest_generator.py`)

**Technology:** Anthropic Claude API

**How it works:**
```python
# 1. Fetch articles from sources
sources = load_json('Global_Media_Database_v3.json')
articles = []
for source in sources:
    articles += fetch_recent_articles(source.url)

# 2. Send to Claude for summarization
prompt = f"""
Summarize these {len(articles)} news articles
into ADHD-friendly bullet points.
Focus on: [your interests]
Format: Scannable, actionable, concise
"""

summary = claude_api.create_message(
    model="claude-3-5-sonnet",
    prompt=prompt + articles
)

# 3. Save formatted summary
save_markdown(summary, 'news-digests/[date].md')
```

**Token efficiency:**
- Summarizes 50+ articles → 10 bullet points
- You read 2 minutes instead of 2 hours!

### 3. Brief Generator (`brief_generator.py`)

**Combines everything:**
```python
def create_morning_brief():
    # Pull from GitHub
    todo = fetch_file('PERMANENT_TODO.md')
    tracker = fetch_file('DAILY_TRACKER_CURRENT.md')

    # Get email results
    emails = load_json('email_triage_results.json')

    # Get news
    news = fetch_file('news-digests/[today].md')

    # Format into sections
    brief = format_markdown(
        top_priorities=extract_top_5(todo),
        urgent_emails=filter_urgent(emails),
        news_summary=news,
        calendar=get_calendar_events(),
        meds=get_medication_reminders()
    )

    # Save
    save_file('morning-briefs/MORNING_BRIEF_[date].md', brief)
```

### 4. GitHub Actions Workflow

**Cron Schedule:**
```yaml
on:
  schedule:
    - cron: '30 7 * * *'  # 8:30 AM CET (7:30 UTC)
  workflow_dispatch:       # Manual trigger
```

**What runs:**
```yaml
steps:
  - Checkout repo
  - Install Python
  - Install dependencies
  - Run news_digest_generator.py
  - Run morning_brief_with_email.py
  - Commit results
  - Push to repo
```

**Why GitHub Actions?**
- Free (2000 minutes/month)
- Reliable scheduling
- Secure (encrypted secrets)
- No server needed!

---

## 🎯 Design Decisions

### Why Static Files?

**Instead of real-time API calls:**

✅ **Token Efficient:**
- Generate once at 8:30 AM
- Read many times throughout day
- Save ~13K tokens per read

✅ **Reliable:**
- File exists even if APIs are down
- Works offline (once fetched)
- No rate limits

✅ **Fast:**
- Reading file = instant
- API calls = slow

### Why IMAP Instead of Gmail API?

✅ **Simpler Setup:**
- No OAuth dance
- No API credentials
- Just app-specific password

✅ **Works Everywhere:**
- GitHub Actions
- Local scripts
- Any Python environment

✅ **Universal:**
- Works with Gmail
- Works with Google Workspace
- Works with any IMAP server

### Why Batch Operations?

**Track in memory → Push once at wrap up:**

✅ **Token Savings:**
- One GitHub push vs. many = 22K tokens saved/day

✅ **Cleaner Commits:**
- One comprehensive commit
- vs. 20 tiny commits

✅ **Better History:**
- Clear what happened each day
- Easy to review changes

---

## 📊 Token Economics

### Traditional Approach:
```
Morning:
- Fetch TODO from GitHub: 3K tokens
- Check email manually: 10K tokens
- Generate news summary: 8K tokens
- Format and present: 2K tokens
Total: ~23K tokens

Throughout day:
- Track medication: GitHub push (2K tokens)
- Update task: GitHub push (2K tokens)
- Add note: GitHub push (2K tokens)
- ... (10 updates = 20K tokens)

Daily total: ~43K tokens
```

### Our Approach:
```
Morning (automated):
- Read pre-generated brief: 2K tokens
Total: ~2K tokens

Throughout day (in memory):
- Track medication: 0 tokens (memory)
- Update task: 0 tokens (memory)
- Add note: 0 tokens (memory)
- Wrap up: GitHub push (2K tokens)

Daily total: ~4K tokens
```

**Savings: ~39K tokens per day** (90% reduction!) 💰

---

## 🔧 Customization Points

### Easy Customizations:
- Schedule time (cron expression)
- Email accounts (add unlimited)
- News sources (edit JSON)
- Triage categories (keyword lists)
- Brief sections (template)

### Medium Customizations:
- Calendar integration (Google API)
- Additional data sources (APIs)
- Custom tracking fields (code edit)
- Different AI models (API calls)

### Advanced Customizations:
- Custom categorization AI (ML)
- Voice interface (iOS Shortcuts)
- Mobile app integration (APIs)
- Team sharing (multi-user)

---

## 🐛 Common Issues & Solutions

### "Workflow Failed"
**Cause:** Missing secrets or permissions
**Fix:** Check GitHub Actions logs, verify all secrets set

### "No Emails Showing"
**Cause:** IMAP not enabled or wrong password
**Fix:** Enable IMAP, regenerate app-specific password

### "News Digest Empty"
**Cause:** No Anthropic API key or no credits
**Fix:** Add ANTHROPIC_API_KEY, check account credits

### "Brief Not Generating"
**Cause:** Workflow not running or errors in script
**Fix:** Check Actions logs, test manually

---

## 📚 Technologies Used

- **Python 3.10+** - Automation scripts
- **GitHub Actions** - Scheduling and execution
- **IMAP** - Email checking
- **Anthropic Claude API** - AI summarization
- **GitHub API** - File storage and retrieval
- **Markdown** - Human-readable format
- **JSON** - Data exchange
- **YAML** - Workflow configuration

**All free/open-source except Claude API!**

---

## 🚀 Future Possibilities

**Could be added:**
- Weather integration
- Habit tracking graphs
- Pomodoro timer integration
- Spotify/music suggestions
- Voice summaries (text-to-speech)
- Team collaboration features
- Mobile app wrapper
- Smart home integration

**The foundation is here - build what you need!**

---

## 💡 Philosophy

**Why this approach works:**

1. **Automation Reduces Decisions** - ADHD-friendly
2. **Static Files Are Fast** - Better UX
3. **Batch Operations Save Tokens** - Cost-effective
4. **Open Source Is Flexible** - Customizable
5. **Privacy First** - Your data stays yours

**Built for humans with ADHD, by humans with ADHD.** 💚

---

**Questions about how something works? Ask Claude!** 🤖
