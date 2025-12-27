# 🔧 NEWS AUTOMATION FIX - FOR CODE

**Date:** December 27, 2025  
**Reporter:** Sync (via Sarah)  
**Priority:** Medium

---

## 🎯 TL;DR - WHAT NEEDS TO HAPPEN

**Problem:** News digest automation STOPPED working after Dec 3, 2025.

**Goal:** News digest auto-generates daily at **08:00 AM CET** and saves to GitHub so ANY Claude instance can fetch it when Sarah says "News Digest"

**Current Status:**
- ✅ Morning brief automation working (runs 08:30 AM daily)
- ❌ News digest NOT generating (stopped Dec 3)
- ❌ No workflow file for news automation exists

---

## 📋 DETAILED REQUIREMENTS

### 1. AUTOMATION SCHEDULE
- **Time:** 08:00 AM CET daily (07:00 UTC winter, 06:00 UTC summer)
- **Trigger:** Cron schedule + manual workflow_dispatch for testing

### 2. OUTPUT LOCATION
- **Folder:** `news-digests/`
- **Filename format:** `news-digest-YYYY-MM-DD.md`
- **Example:** `news-digest-2025-12-27.md`

### 3. CONTENT STRUCTURE (ADHD-FRIENDLY!)

```markdown
# 📰 News Digest - [Date]

## 🎯 TL;DR (Top 3-5 headlines)
- [Most important story 1]
- [Most important story 2]
- [Most important story 3]
---

## 🇪🇸 SPAIN & BARCELONA
[Brief summaries]

## 🇮🇹 ITALY
[Brief summaries]

## 🇪🇺 EUROPE
[Brief summaries]

## 🌍 WORLD NEWS
[Brief summaries]

## 🎭 ARTS & CULTURE
[Brief summaries]

## 🔬 SCIENCE
[Brief summaries]

## 💻 TECH
[Brief summaries]

## 📊 SOURCES USED
- [List of sources]
```

### 4. HOW CLAUDE FETCHES IT

When Sarah says "News Digest", ANY Claude instance should:

```bash
# Fetch today's digest from GitHub
curl -H "Authorization: token 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" \
  -H "Accept: application/vnd.github.v3.raw" \
  "https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/news-digests/news-digest-$(date +%Y-%m-%d).md"
```

Then read and present to Sarah. **Token cost: ~2-5K instead of 20-30K!**

---

## 🐛 WHAT'S BROKEN

### Current State:
- **Last working digest:** December 3, 2025
- **Gap:** 24 days (Dec 4 - Dec 27)
- **Morning brief says:** "_News digest generation pending_"

### What Exists:
- ✅ `automation/news-intelligence-SKILL.md` (the skill instructions)
- ✅ `automation/news_digest_generator.py` (Python script - MAY exist)
- ✅ `automation/news_fetcher.py` (Python script - MAY exist)
- ✅ `.github/workflows/morning-brief.yml` (morning brief workflow)
- ❌ `.github/workflows/news-digest.yml` (MISSING!)

### What's Missing:
1. **GitHub Actions workflow** for news digest automation
2. **Python script** that actually generates the digest (or it's broken)
3. **API key/secrets** properly configured (if needed)

---

## 🔨 WHAT CODE NEEDS TO DO

### Task 1: Create News Digest Workflow
**File:** `.github/workflows/news-digest.yml`

**Schedule:** 08:00 AM CET (cron: `0 6 * * *` for summer, `0 7 * * *` for winter)

**Job Steps:**
1. Checkout repo
2. Set up Python
3. Install dependencies
4. Run news generation script
5. Commit and push to `news-digests/news-digest-[date].md`

### Task 2: Fix/Create Python Script
**File:** `automation/generate_news_digest.py` (or similar)

**What it does:**
1. Use news-intelligence-SKILL.md as reference
2. Search web for news from key sources:
   - El País (Spain)
   - ANSA (Italy)
   - Reuters (Global)
   - AFP (Europe)
3. Create ADHD-friendly digest with TL;DR at top
4. Save to `news-digests/news-digest-[today].md`

### Task 3: Test It Works
1. Run workflow manually (workflow_dispatch)
2. Verify file created in `news-digests/`
3. Verify Sarah can fetch it via GitHub API
4. Verify cron schedule triggers correctly

---

## 📚 REFERENCE FILES

**In GitHub repo:**
- `/automation/news-intelligence-SKILL.md` - Full skill instructions
- `/automation/news_digest_generator.py` - Python script (check if exists/working)
- `/.github/workflows/morning-brief.yml` - Working example of automation

**Local skill (same as GitHub):**
- `/mnt/skills/user/news-intelligence/SKILL.md`

---

## ✅ SUCCESS CRITERIA

When complete:
- [ ] News digest auto-generates daily at 08:00 AM CET
- [ ] Files appear in `news-digests/` folder with correct date
- [ ] TL;DR section at top (ADHD-friendly!)
- [ ] Sarah can say "News Digest" and M/Pilot fetches from GitHub
- [ ] Token cost: 2-5K (vs 20-30K manual generation)
- [ ] No gaps in daily coverage

---

## 💬 NOTES FOR CODE

- **API Access:** Use `secrets.GH_PAT` in workflow (same as morning-brief)
- **Python deps:** Probably needs `requests`, `anthropic` API library
- **Error handling:** If generation fails, don't break - log error and retry next day
- **Keep it simple:** Don't over-engineer - just get it working daily
- **ADHD format:** TL;DR MUST be at top - this is critical for Sarah's workflow

---

## 🔗 RELATED

**GitHub PAT (for API access):**
```
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
```

**Repository:**
```
MotherOfChaos/Life-Operating-System
```

**Questions?** Ask Sync or check existing morning-brief automation for reference.

---

**Created by:** Sync  
**For:** Code (Claude Code)  
**Urgency:** Medium - Nice to have but not blocking Sarah's work
