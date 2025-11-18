# 🌅 Morning Brief - SUPER SIMPLE Setup

**3 steps. That's it. I did the rest for you.**

---

## What This Does

When you say **"Good morning"** to Claude:
1. Claude runs a quick script to pull your TODO and tracker from GitHub
2. Claude checks your Gmail directly (no OAuth needed!)
3. Claude generates your morning brief right there
4. Claude saves it to GitHub for later

**No scheduling. No cloud server. No complex auth. It runs when YOU run it.**

---

## ✅ Setup (3 Steps)

### Step 1: Install Dependencies

Open terminal and run:

```bash
cd ~/Life-Operating-System/automation
pip3 install requests pytz
```

**That's it for this step!**

---

### Step 2: Test It Works

```bash
cd ~/Life-Operating-System/automation
./run-morning-brief.sh
```

**What you should see:**
```
🌅 Good morning! Running your brief...

============================================================
🌅 GENERATING MORNING BRIEF
============================================================

📥 Pulling from GitHub...
   ✓ PERMANENT_TODO.md
   ✓ SARAH_DAILY_TRACKER_CURRENT.md

📝 Creating brief template...
   ✓ Brief generated

💾 Saving brief...
   ✓ Local backup: automation/backups/MORNING_BRIEF_2025-11-18.md
   ✓ Pushed to GitHub

============================================================
✅ BRIEF READY!
============================================================
```

**If it works:** You're done! Go to Step 3.

**If it says "Failed to fetch" or "GitHub push failed":**
- Your GitHub token might need updating
- Tell Claude and I'll fix it

---

### Step 3: Use It Every Morning

Two ways:

**Option A: Ask Claude to run it**
```
You: "Good morning! Run my morning brief"
Claude: [runs the script, checks your email, presents everything]
```

**Option B: Run it yourself first, then talk to Claude**
```bash
cd ~/Life-Operating-System/automation
./run-morning-brief.sh
```

Then say to Claude: "Read my morning brief and check my email"

---

## 🎯 Daily Workflow

### Your Morning (Wake up anytime!)

1. Open Claude chat
2. Say: **"Good morning!"**
3. Claude will:
   - Run the morning brief script
   - Pull your TODO and tracker from GitHub
   - Check your Gmail directly
   - Categorize emails into 7 categories
   - Present everything in ADHD-friendly format

**That's it!**

---

## 📧 About Email

**No Gmail OAuth needed!**

When you say "Good morning" or "check my email", Claude can access your Gmail directly in the chat session (like we've done before). The script just handles the GitHub part and creates the brief template.

This avoids all the OAuth complexity that got frustrating before!

---

## 🔐 Security

**Your GitHub token is in `config.py`** - already set up for you!

This file is in `.gitignore` so it won't be committed publicly.

If you ever need to change it:
```bash
nano ~/Life-Operating-System/automation/config.py
```

Change the `GITHUB_TOKEN` line, save, and you're done.

---

## 🐛 Troubleshooting

### "Import error: No module named requests"

Run:
```bash
pip3 install requests pytz
```

### "Failed to fetch PERMANENT_TODO.md"

Your GitHub token might be wrong or expired. Tell Claude and I'll help you fix it.

### "GitHub push failed"

Token issue or network issue. The brief still saves locally in `automation/backups/` so you won't lose it!

---

## 💡 Files You Care About

**Script that runs:** `automation/simple_morning_brief.py`

**Your config:** `automation/config.py` (GitHub token is here)

**Briefs are saved to:**
- GitHub: `morning-briefs/MORNING_BRIEF_[date].md`
- Local backup: `automation/backups/MORNING_BRIEF_[date].md`

**To run manually:**
```bash
./automation/run-morning-brief.sh
```

---

## ✨ That's Everything!

No cron jobs. No OAuth. No cloud servers. No scheduling.

Just: **Wake up → Say "Good morning" to Claude → Get your brief**

**Token efficient:** Brief template from GitHub (~2K tokens) + Claude checks email (~5K) = ~7K total

vs checking everything fresh every time (~15K tokens)

---

**Questions?** Just ask Claude! I can help debug anything. 💚
