---
description: Complete morning brief with email triage (auto-runs when Sarah says good morning)
---

# Morning Brief Automation

**AUTOMATIC WORKFLOW - Run this when Sarah says "Good morning", "Hi" (at start of day), or manually with /morning**

## Step 1: Fetch Today's Morning Brief from GitHub

**CRITICAL FOR ADHD:** This must work from phone/web/desktop with ZERO manual steps from Sarah!

**Determine today's date in Sarah's timezone:**
- Sarah is in Europe/Madrid (CET/CEST)
- Format: YYYY-MM-DD (e.g., 2025-11-30)

**Fetch the morning brief via GitHub API:**

```
URL: https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/morning-briefs/MORNING_BRIEF_[today's date].md

Headers:
  Authorization: token [GH_PAT from CLAUDE_PROJECTS_INSTRUCTIONS.md]
  Accept: application/vnd.github.v3.raw
```

**If fetch succeeds:**
- Parse the morning brief content
- Extract TOP 5 priorities
- Note the news digest section
- Continue to Step 2 (email triage)

**If fetch fails (404 - file doesn't exist):**
- The automation hasn't run yet (before 08:30 CET)
- Tell Sarah: "⏰ Morning brief not ready yet - automation runs at 08:30 CET. I can check your email now if you'd like?"
- Offer to do email triage anyway

**If fetch fails (auth error):**
- Tell Sarah: "⚠️ GitHub token issue - please ask Cody to check the setup"
- Do NOT expose token details

## Step 2: Check and Triage Gmail

After fetching the morning brief, check Sarah's Gmail and categorize emails into these 7 categories:

**Email Categories:**
1. 🔴 **Urgent Action Required** - needs response TODAY (keywords: urgent, asap, deadline today, action required)
2. 🟡 **Needs Response** - not urgent but requires reply (keywords: questions, requests, "let me know")
3. 🔵 **FYI/Read Later** - informational only, no action needed
4. 📅 **Calendar/Events** - invitations, meetings, scheduling (keywords: invitation, event, meeting, RSVP)
5. 💰 **Financial/Invoices** - money-related (keywords: invoice, payment, bill, transaction)
6. 📧 **Newsletters/Promotions** - marketing, subscriptions (keywords: unsubscribe, newsletter, promotion)
7. ✅ **Can Archive** - already handled or irrelevant (especially no-reply emails)

## Step 2b: Check Google Calendar (Optional)

If Sarah has granted calendar access, check today's Google Calendar events and apply these filters:

**Calendar Filtering Rules:**
- **EXCLUDE** any event with "notes" in the title (case insensitive)
- **EXCLUDE** any all-day events
- **EXCLUDE** "Baja medica" or "Baja médica" events
- **ONLY SHOW** time-specific appointments with actual times

Return calendar events in this format:
```python
[
    {'time': '10:00 AM', 'title': 'Event Name', 'all_day': False},
    {'time': '2:30 PM', 'title': 'Another Event', 'all_day': False}
]
```

## Step 3: Present Complete Morning Brief

Combine the brief from the script with your email triage and present in this format:

```
# 🌅 GOOD MORNING SARAH! - [Day, Month Date, Year]

**Your Morning Brief is Ready** ☕

---

## 🔴 TOP 5 URGENT PRIORITIES TODAY

[List from the script output - top 5 TODO items]

---

## 📧 URGENT EMAILS REQUIRING ACTION

[List emails from 🔴 category with:
- From
- Subject
- Brief snippet (1 line)
- Received time]

---

## 🟡 EMAILS NEEDING RESPONSE (Not Urgent)

**Count:** [X emails]

[List top 3-5 with sender/subject]

---

## 📅 TODAY'S CALENDAR

[If calendar checked, show filtered events with time and title]
[Example: "- **10:00 AM:** Doctor appointment"]
[Or: "✨ *No scheduled events today*"]

---

## 📧 OTHER EMAIL CATEGORIES

**Calendar/Events:** [count] emails
**Financial/Invoices:** [count] emails
**Newsletters/Promotions:** [count] emails
**FYI/Read Later:** [count] emails
**Can Archive:** [count] emails

---

## 💊 MEDICATION REMINDER

- **Concerta 36mg** (take on waking)

---

## 📊 QUICK STATS

- Urgent emails: [count]
- Response needed: [count]
- Pending priority tasks: [count from TODO]
- Total emails checked: [count]

---

**Token-efficient format. Scannable for ADHD. Ready to go.** 💚
```

## Step 4: Save Updated Brief to GitHub

After presenting, save the complete brief (with email info added) back to GitHub:

```python
# Update the morning-briefs/MORNING_BRIEF_[today].md file with complete info
```

## Important Notes

- **Token efficient:** Brief template from GitHub (~2K) + email check (~5K) = ~7K total vs ~15K fresh
- **ADHD-friendly:** All info in one place, pre-categorized, scannable
- **Auto-saves:** Everything saved to GitHub for other Claude instances to reference
- **No OAuth needed:** You check Gmail directly in the session

## If Script Fails

If the morning brief script fails:
- Still check Gmail and present email triage
- Note that TODO/tracker info wasn't available
- Present what you can with: "⚠️ Could not pull from GitHub - check manually"

## Timezone

Sarah is in **Europe/Berlin** (CET/CEST)
