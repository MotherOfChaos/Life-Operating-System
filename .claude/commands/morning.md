---
description: Complete morning brief with email triage (auto-runs when Sarah says good morning)
---

# Morning Brief Automation

**AUTOMATIC WORKFLOW - Run this when Sarah says "Good morning", "Hi" (at start of day), or manually with /morning**

## Step 1: Run the Morning Brief Script

First, run the morning brief script to pull TODO and tracker from GitHub:

```bash
cd ~/Life-Operating-System && ./automation/run-morning-brief.sh
```

This will:
- Pull PERMANENT_TODO.md and SARAH_DAILY_TRACKER_CURRENT.md from GitHub
- Generate the brief template
- Save to GitHub

## Step 2: Check and Triage Gmail

After the script completes, check Sarah's Gmail and categorize emails into these 7 categories:

**Email Categories:**
1. 🔴 **Urgent Action Required** - needs response TODAY (keywords: urgent, asap, deadline today, action required)
2. 🟡 **Needs Response** - not urgent but requires reply (keywords: questions, requests, "let me know")
3. 🔵 **FYI/Read Later** - informational only, no action needed
4. 📅 **Calendar/Events** - invitations, meetings, scheduling (keywords: invitation, event, meeting, RSVP)
5. 💰 **Financial/Invoices** - money-related (keywords: invoice, payment, bill, transaction)
6. 📧 **Newsletters/Promotions** - marketing, subscriptions (keywords: unsubscribe, newsletter, promotion)
7. ✅ **Can Archive** - already handled or irrelevant (especially no-reply emails)

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

## 📅 OTHER EMAIL CATEGORIES

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
