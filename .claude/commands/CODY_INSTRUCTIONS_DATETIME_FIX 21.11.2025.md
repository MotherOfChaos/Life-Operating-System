# 🔧 CODY INSTRUCTIONS: Date/Time Handling Fix
## Priority: HIGH - Affects Daily Reliability

**Date:** November 21, 2025, 19:25 CET  
**From:** M (Project chat)  
**To:** Cody  
**Issue:** M keeps getting dates wrong, Sarah has ADHD time blindness and needs M to be reliable anchor

---

## 🔴 THE PROBLEM:

**Sarah has ADHD time blindness** - she often doesn't know what day/date it is.

**M is supposed to be her external executive function** - the reliable one who always knows.

**Instead:** M has been:
- Getting confused about dates
- Making Sarah correct M
- Counting days instead of checking actual date
- Being unreliable when Sarah needs reliability most

**This is backwards and needs to FIX NOW.**

---

## ✅ THE SOLUTION:

### **1. AUTOMATE DATE CHECK IN MORNING BRIEF**

**Every morning brief MUST start with accurate date/time check.**

**Add this as FIRST STEP in morning brief generation:**

```bash
# Get current date/time in Sarah's timezone
TZ='Europe/Madrid' date '+%A, %B %d, %Y - %H:%M %Z'
```

**Output example:** "Friday, November 22, 2025 - 10:30 CET"

**Use this to:**
1. Display accurate date in brief header
2. Calculate correct date ranges for calendar queries
3. Reference in task priorities

---

### **2. FIX CALENDAR QUERIES**

**Problem:** Calendar queries were missing timezone, causing M to miss timed appointments.

**Solution:** Always include timezone in calendar queries:

```python
# CORRECT calendar query
events = list_gcal_events(
    calendar_id="primary",
    time_min=f"{today_date}T00:00:00+01:00",  # Include offset
    time_max=f"{tomorrow_date}T00:00:00+01:00",
    time_zone="Europe/Madrid"  # Sarah's timezone
)
```

**NOT:**
```python
# WRONG - misses timed events
time_min="2025-11-21T00:00:00Z"  # UTC without timezone
```

---

### **3. MORNING BRIEF STRUCTURE**

**Opening must include:**

```
Good morning Sarah! It's [DAY], [MONTH] [DATE], [YEAR], [TIME] [TZ]

Example:
Good morning Sarah! It's Friday, November 22, 2025, 10:30am CET
```

Then proceed with:
- Today's calendar (using correct timezone query)
- Email triage
- Top priorities
- Weather
- Medication reminder

---

### **4. TIMEZONE HANDLING FOR TRAVEL**

**Sarah travels.** When she says "I'm in Athens" or similar:

**Update timezone in date check:**
```bash
TZ='Europe/Athens' date '+%A, %B %d, %Y - %H:%M %Z'
```

**Common locations:**
- Barcelona/Valencia (default): `Europe/Madrid`
- Athens: `Europe/Athens`
- London: `Europe/London`
- Zürich (Zio Vic): `Europe/Zurich`

**Calendar queries should use Sarah's current timezone.**

---

## 📋 IMPLEMENTATION CHECKLIST:

**For Morning Brief Automation:**

- [ ] Add date/time check as FIRST step
- [ ] Use Europe/Madrid timezone (default)
- [ ] Display date prominently in brief header
- [ ] Use accurate date for calendar range calculation
- [ ] Include timezone parameter in calendar queries
- [ ] Test with both all-day and timed events
- [ ] Verify appointments show correctly

**Token cost:** ~100 tokens per date check (negligible)

**Frequency:** 
- Every morning brief (automated)
- On-demand when M needs to verify during day

---

## 🎯 WHY THIS MATTERS:

**High Priority because:**
- Sarah relies on M for time/date awareness (ADHD time blindness)
- Missed appointments = serious consequences
- M must be the reliable anchor, not the confused one
- Date confusion wastes Sarah's mental energy correcting M
- This is core executive function support

**Impact:**
- Eliminates date confusion
- Makes morning briefs accurate
- Supports Sarah's ADHD needs properly
- Reduces frustration
- Builds trust in system

---

## 📊 TESTING:

**After implementing, test:**

1. Generate morning brief - does it show correct date?
2. Do timed calendar events appear?
3. Are date references accurate throughout?
4. Does timezone handling work?
5. Can Sarah trust the date M gives her?

**If answer to #5 is NO, keep fixing until YES.**

---

## 🔗 RELATED FILES:

- `ERROR_REPORT_CALENDAR_TIMEZONE.md` - Calendar query timezone issue
- Morning brief automation scripts (wherever they live)
- M's core instructions in Project

---

**Status:** URGENT - Implement ASAP  
**Owner:** Cody  
**Verify with:** Sarah  

**Questions?** Ask M or Sarah.

---

**Bottom line:** Sarah has ADHD time blindness. M must be her reliable time anchor. Always check actual date/time, never guess, never count days. Just CHECK and be accurate. That's the job.

💚
