# ADHD-Friendly Life OS Automation System

**Shared by Sarah (Mother of Chaos) - Built with Claude Code**

**For:** Xavier (and other ADHD friends who want to level up their life management!)

---

## 🎯 What This System Does

**Morning Brief Automation:**
- Runs automatically every morning at 8:30 AM (customizable)
- Checks your email accounts and triages them
- Pulls your TODO list priorities
- Generates AI news digest from sources you choose
- Checks your calendar (filters out noise)
- Gives you complete morning overview - ready to go!

**Token Efficient:**
- Pre-generates everything = saves ~13K tokens per day
- Batch tracking = saves ~22K tokens per session
- Total savings: ~35K tokens daily!

**ADHD-Friendly:**
- Scannable bullet points
- Clear priorities upfront
- Automation reduces decision fatigue
- Nothing gets forgotten
- Works across all devices

---

## 📦 What's Included

### Core Automation:
1. **Morning Brief Generator** - Daily overview at 8:30 AM
2. **Multi-Account Email Triage** - Categorizes all your emails automatically
3. **News Digest Generator** - AI-powered news summaries
4. **Calendar Integration** - Smart filtering (hide recurring noise)
5. **TODO Tracking System** - Track tasks, meds, wins
6. **Mobile/Web Solutions** - Access everything on phone/tablet

### Files in This Package:
```
XAVIER/
├── README.md (this file - start here!)
├── SETUP_GUIDE.md (step-by-step setup instructions)
├── automation/ (all the automation scripts)
├── templates/ (template files to customize)
├── examples/ (example configurations)
└── docs/ (detailed documentation)
```

---

## 🚀 Quick Start (30 Minutes Setup)

### Prerequisites:
- GitHub account
- Claude account (any tier)
- Gmail account(s) you want to automate
- (Optional) Anthropic API key for news digest

### Setup Steps:

**1. Fork or Copy This Repo** (5 min)
- Copy the `XAVIER/` folder to your own GitHub repo
- Or fork Sarah's repo and customize

**2. Set Up GitHub Actions** (10 min)
- Enable GitHub Actions in your repo
- Add secrets (email passwords, API keys)
- Configure schedule (default: 8:30 AM your timezone)

**3. Customize Your Files** (10 min)
- Edit `templates/config.template.py` with your info
- Add your email accounts
- Choose your news sources
- Set your timezone

**4. Test It** (5 min)
- Run workflow manually
- Check your morning brief appears
- Verify email triage works

**Done!** Tomorrow morning you'll have automated brief waiting!

---

## 💡 Key Features

### Morning Brief Includes:
- 🔴 Top 5 urgent TODO priorities
- 📧 Email triage (all accounts, categorized)
- 📰 News digest (AI-generated TLDR)
- 📅 Calendar (smart filtered - only real appointments)
- 💊 Medication reminders (customizable)
- 📊 Quick stats

### Email Triage Categories:
**Standard Mode (Personal Email):**
- 🔴 Urgent Action Required
- 🟡 Needs Response
- 🔵 FYI/Read Later
- 📅 Calendar/Events
- 💰 Financial/Invoices
- 📧 Newsletters/Promotions
- ✅ Can Archive

**Custom Mode (Work Email):**
- You can define your own categories!
- Example: Artist inquiries, Provider info, Contracts, etc.

### Calendar Smart Filtering:
Automatically hides:
- Recurring all-day events (like "Day X - notes")
- Long-term reminders (like "Baja medica")
- Only shows actual timed appointments

When you have no appointments → **"FREE DAY! 🎉"**

### News Digest:
- Choose your own news sources
- AI summarizes into ADHD-friendly bullet points
- Saves ~10K tokens vs. manual news reading

---

## 🎭 ADHD-Friendly Design Principles

**Why This Works for ADHD:**

1. **Automation = Less Decision Fatigue**
   - Everything happens automatically
   - No "should I check email?" decisions
   - Morning routine becomes effortless

2. **Scannable Format**
   - Bullet points, not paragraphs
   - Clear emoji indicators
   - Priorities upfront

3. **Nothing Gets Lost**
   - Track everything in working memory
   - Batch save at end of day
   - Files synced to GitHub
   - Access from any device

4. **Token Efficient**
   - Pre-generated briefs
   - Batch operations
   - Saves your Claude usage limits

5. **Works Everywhere**
   - Desktop, mobile, web
   - iOS shortcuts available
   - Browser bookmarklets
   - Simple copy/paste templates

---

## 🔧 Customization Options

### Change Schedule:
Default is 8:30 AM. Edit `.github/workflows/morning-brief.yml`:
```yaml
schedule:
  - cron: '30 7 * * *'  # 8:30 AM CET (7:30 UTC)
```

### Add More Email Accounts:
Edit `automation/config.py` - supports unlimited accounts!

### Customize Triage Categories:
Edit `automation/email_automation.py` - define your own categories

### Choose News Sources:
Edit `Global_Media_Database_v3.json` - add/remove sources

### Add Medication Reminders:
Edit `templates/DAILY_TRACKER_TEMPLATE.md`

---

## 📱 Mobile/Web Access

**Three Ways to Access Your Brief:**

### 1. "Fetch Brief Anywhere" (Fastest)
Simple template you paste in ANY Claude chat:
```
Hi! Fetch today's morning brief from GitHub:
Repository: [your-username]/[your-repo]
File: morning-briefs/MORNING_BRIEF_[today].md
[Instructions in SETUP_GUIDE.md]
```

### 2. iOS Shortcut (Best for iPhone)
- Voice activated: "Hey Siri, morning brief"
- One-tap widget
- Auto-runs at wake time
- [Instructions in docs/ios-shortcut-instructions.md]

### 3. Web Bookmarklet (Best for Browser)
- One-click loading
- Works in any browser
- [Instructions in docs/web-bookmarklet.html]

---

## 🤝 How Sarah Uses This

**Sarah's Morning Routine:**
1. 8:30 AM: Automation runs (while she sleeps)
2. Wake up: Opens Claude (any device)
3. Says "Good morning" or pastes fetch command
4. Gets complete overview in 5 seconds
5. Starts day with clarity!

**During Day:**
- Tracks tasks, meds, wins in working memory
- "Wrap up" command at end of day
- Everything saves to GitHub
- Next morning includes yesterday's updates

**Token Savings:**
- Old way: ~50K tokens per day
- New way: ~15K tokens per day
- Savings: ~35K tokens daily! 💰

---

## 🎁 What Makes This Special

**Built by ADHD person, for ADHD people:**
- Designed by Sarah (who has ADHD)
- Tested in real daily use
- Optimized for executive function challenges
- Reduces cognitive load at every step

**Claude-Native:**
- Uses Claude's strengths (summarization, categorization)
- Token-efficient by design
- Works with free or paid tiers
- No external apps needed (except GitHub)

**Open & Customizable:**
- All code included
- Fully documented
- Adapt to your needs
- Share with friends!

---

## 📚 Documentation

**Start Here:**
1. `SETUP_GUIDE.md` - Step-by-step setup instructions
2. `docs/HOW_IT_WORKS.md` - Technical overview
3. `docs/CUSTOMIZATION.md` - How to adapt to your needs
4. `docs/TROUBLESHOOTING.md` - Common issues & fixes

**Reference:**
- `automation/README.md` - Automation scripts overview
- `templates/README.md` - Template files guide
- `examples/` - Real-world examples

---

## 🆘 Support

**Questions? Issues?**
- Check `docs/TROUBLESHOOTING.md` first
- Ask Claude! (Seriously - Claude Code can help debug)
- Contact Sarah if you know her
- Open GitHub issue

---

## 🎉 Get Started!

**Ready to level up your ADHD life management?**

1. Read `SETUP_GUIDE.md`
2. Follow the steps
3. Customize to your needs
4. Enjoy automated mornings!

**Time investment:** ~30 minutes setup
**Daily benefit:** Save hours of decision fatigue
**ADHD impact:** Massive! 💚

---

## 📝 Credits

**Created by:** Sarah (Mother of Chaos) with Claude Code (Cody)
**Shared with love** for the ADHD community 💚
**Built:** November 2025
**Philosophy:** "Mens sana in corpore sano" 🌹

---

**Welcome to the Life OS, Xavier!** 🚀

Let automation handle the logistics while you focus on what matters.

**Go build something amazing!** ✨
