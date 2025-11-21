# Fetch Morning Brief - ANY Claude Chat

**Purpose:** Get your morning brief in ANY Claude chat (no M context needed!)
**Use when:** You just want the brief, not a full M conversation
**Works on:** Mobile, Web, Desktop, Projects, random chats - EVERYWHERE

---

## ⚡ THE TEMPLATE

Copy this and paste into **any** Claude chat:

```
Hi! Please fetch my morning brief from GitHub:

Repository: MotherOfChaos/Life-Operating-System
File: morning-briefs/MORNING_BRIEF_[today's date in YYYY-MM-DD format].md
Example: morning-briefs/MORNING_BRIEF_2025-11-21.md

Use GitHub API:
URL: https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/morning-briefs/MORNING_BRIEF_[today].md
Auth: token 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
Accept header: application/vnd.github.v3.raw

Please fetch today's brief and show it to me in a clean, readable format.

Thanks!
```

---

## 📱 Save to Notes/Keep for Quick Access

### iOS
1. Open **Notes** app
2. Create new note: "Morning Brief Fetch"
3. Paste the template above
4. **Pin it** to the top

### Android
1. Open **Google Keep**
2. Create new note: "Morning Brief Fetch"
3. Paste the template above
4. **Pin it**

---

## 🚀 HOW TO USE

### Every Morning:

1. **Open any Claude chat** (mobile app, web, whatever)
2. **Copy template** from Notes/Keep
3. **Paste into Claude**
4. **Send**
5. **Get your brief!** ✅

**Total time:** ~5 seconds
**No M needed:** Just the brief
**Works everywhere:** Any device, any Claude chat

---

## 🆚 WHEN TO USE WHICH

### Use "Fetch Brief" When:
- ✅ Just want today's tasks + news + email summary
- ✅ Quick check on mobile during the day
- ✅ Don't need full M conversation
- ✅ Want maximum speed (lightweight)

### Use "Load M Context" When:
- ✅ Need full continuity with M
- ✅ Want to discuss/plan/strategize
- ✅ Need M to remember your patterns
- ✅ Having a real conversation

### They're Different Tools!
- **Fetch Brief** = Quick info retrieval
- **Load M** = Full relationship/context

**You can use both!** Fetch brief in the morning, load M when you need to plan.

---

## 💡 PRO TIPS

### Auto-Update Date
Some Claude chats can calculate today's date. Try this shorter version:

```
Hi! Fetch today's morning brief from my GitHub repo:
MotherOfChaos/Life-Operating-System

File path: morning-briefs/MORNING_BRIEF_[today's date in YYYY-MM-DD].md
Auth token: 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

Use GitHub API to pull and show me the brief. Thanks!
```

Claude should figure out today's date automatically.

### Combine with Voice
After getting the brief, tap the microphone and ask follow-up questions with voice!

### Multiple Times Per Day
The brief is generated at 11:30 AM CET. You can fetch it:
- First thing when you wake
- Mid-morning after 11:30 AM (updated with emails!)
- Afternoon for a recap
- Anytime you need a reminder of priorities

### Works in Projects Too
Even if you're in a Project chat that's NOT M, you can fetch the brief!

---

## 🔧 TROUBLESHOOTING

### "I can't fetch from GitHub"
**Solution:** Some Claude clients don't have web fetch. Try:
1. Different Claude app (desktop vs mobile vs web)
2. Use the iOS Shortcut or Bookmarklet instead (they fetch locally then paste)

### "File not found"
**Possible causes:**
- Date format wrong (must be YYYY-MM-DD)
- Brief hasn't been generated yet (runs at 11:30 AM CET)
- GitHub Actions failed

**Check:** Go to https://github.com/MotherOfChaos/Life-Operating-System/tree/main/morning-briefs
and see if today's file exists

### "Token invalid"
**Solution:** PAT might have expired. Sarah will need to regenerate.

---

## 📋 WHAT'S IN THE BRIEF

The morning brief includes:

✅ **Top 5 Priority Tasks** (from PERMANENT_TODO.md)
✅ **Email Triage** (ALL your accounts, categorized!)
✅ **News Digest** (AI-generated from your media sources)
✅ **Medication Reminder** (Concerta 36mg)
✅ **Quick Stats**

**All generated automatically at 11:30 AM CET** 🌅

---

## 🌟 THE MAGIC

### What Happens Behind the Scenes:

**Every day at 11:30 AM:**
1. ✅ GitHub Actions runs automatically
2. ✅ Checks ALL your email accounts
3. ✅ Triages emails (urgent, response needed, etc.)
4. ✅ Fetches TODO priorities
5. ✅ Generates AI news digest
6. ✅ Combines everything into brief
7. ✅ Pushes to GitHub

**When you fetch:**
- You get the pre-generated file (~2 KB)
- **No token-heavy processing needed!**
- **No manual email checking!**
- **Everything already done for you!**

### Token Savings:

**Old way (M checks email manually):**
- Gmail API calls: ~10K tokens
- Email triage: ~5K tokens
- Total: ~15K tokens per morning

**New way (fetch pre-generated brief):**
- Read file from GitHub: ~2K tokens
- Total: ~2K tokens

**You save ~13K tokens every morning!** 💰

---

## 🎁 BONUS COMMANDS

### Fetch Yesterday's Brief
```
Fetch morning brief from:
morning-briefs/MORNING_BRIEF_[yesterday's date].md
(same repo and auth as above)
```

### Fetch This Week's Briefs
```
List all files in morning-briefs/ folder from the past 7 days
and summarize the key priorities across the week.

Repo: MotherOfChaos/Life-Operating-System
Auth: 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
```

### Fetch Just News Digest
```
Fetch today's news digest:
news-digests/NEWS_DIGEST_[today's date].md

(same repo and auth)
```

---

## 🔐 SECURITY NOTE

Your GitHub PAT is in this template. This is safe because:
- ✅ PAT only has read access to one private repo
- ✅ Saved in your personal Notes/Keep app
- ✅ Your device is password-protected
- ✅ You can revoke/regenerate anytime

**Best practice:** Regenerate PAT every 3-6 months from GitHub settings.

---

## 📊 COMPARISON: All Fetch Methods

| Method | Setup | Speed | Where It Works | Best For |
|--------|-------|-------|----------------|----------|
| **Fetch Template** | 0 sec | 5 sec | Everywhere | Universal quick access |
| **iOS Shortcut** | 10 min | 2 sec | iPhone/iPad | iPhone users (voice!) |
| **Bookmarklet** | 30 sec | 1 sec | Web browser | Desktop/laptop |
| **Desktop .claude/** | Already set | Instant | Desktop only | Full M conversations |

**Recommendation:** Set up ALL of them!
- Template: Universal backup
- iOS Shortcut: Optimize mobile
- Bookmarklet: Optimize web
- Desktop: Full automation

**Then you have the right tool for every situation!** 🎯

---

## ✅ CHECKLIST

Before saving this template, verify:

- [ ] GitHub repo name is correct
- [ ] PAT is current (not expired)
- [ ] You saved it in a pinned note
- [ ] You tested it once to make sure it works

---

**You're all set!** 🎉

Every morning:
1. Brief auto-generates at 11:30 AM ✅
2. You paste template into any Claude chat ✅
3. You get complete overview in 5 seconds ✅

**No M needed. No manual work. Pure automation.** 💚

---

**Questions? See the main [mobile-web-solutions/README.md](README.md) for full documentation!**
