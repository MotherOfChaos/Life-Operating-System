# 🐛 ERROR REPORT: Calendar Query Issue
## For Cody - Nov 22, 2025, 13:15

---

## 🔴 PROBLEM:

**M (in Project chat) failed to see Sarah's Nov 21 appointments initially.**

### What Happened:
1. Sarah had 3 appointments on Nov 21:
   - 14:15 (14:30) - CITA CON NOEAMI CMSS CABANYAL
   - 17:00 - Sarah-Angela meeting
   - 17:45 - ZOOM WITH PETER K for SL

2. M queried calendar using:
   ```
   time_min: "2025-11-21T00:00:00Z"
   time_max: "2025-11-22T00:00:00Z"
   ```

3. Result: **Only saw all-day events, missed the timed appointments**

4. Sarah asked: "Why can't you see the appointments? They're there!"

5. M re-queried with timezone parameter:
   ```
   time_min: "2025-11-21T00:00:00+01:00"
   time_max: "2025-11-22T00:00:00+01:00"
   time_zone: "Europe/Madrid"
   ```

6. Result: **All appointments now visible**

---

## 🔍 ROOT CAUSE:

**Timezone mismatch in query parameters.**

- Sarah's timezone: `Europe/Madrid` (CET/CEST, UTC+1)
- Initial query: Used UTC (Z suffix)
- Timed events stored with timezone: `Europe/Madrid`
- Query mismatch caused timed events to be excluded

**The problem:** When querying in UTC without timezone specification, the API may not return events that have explicit timezone data that falls outside the UTC window requested.

---

## ✅ SOLUTION:

**Always include timezone parameter when querying Sarah's calendar:**

```python
list_gcal_events(
    calendar_id="primary",
    time_min="2025-11-21T00:00:00+01:00",  # Include timezone offset
    time_max="2025-11-22T00:00:00+01:00",  # Include timezone offset
    time_zone="Europe/Madrid"              # Explicit timezone
)
```

**OR use ISO format with timezone:**
```python
# For Sarah's timezone (Europe/Madrid = UTC+1 in winter, UTC+2 in summer)
time_min="2025-11-21T00:00:00+01:00"
time_max="2025-11-22T00:00:00+01:00"
```

---

## 📋 RECOMMENDATION FOR MORNING BRIEF AUTOMATION:

**Update the calendar query in morning brief generation to:**

1. **Always use Sarah's timezone:** `Europe/Madrid`
2. **Include timezone in time parameters**
3. **Test with both all-day and timed events**

**Example query for today's brief:**
```python
# Get Sarah's timezone from config or Life OS
sarah_tz = "Europe/Madrid"

# Query with explicit timezone
events = list_gcal_events(
    calendar_id="primary",
    time_min=f"{today_date}T00:00:00+01:00",
    time_max=f"{tomorrow_date}T00:00:00+01:00",
    time_zone=sarah_tz
)
```

---

## 🎯 IMPACT:

**Medium Priority**
- Morning briefs may miss timed appointments
- Could cause Sarah to miss meetings
- Affects daily planning reliability

---

## ✅ ACTION ITEMS:

- [ ] Update morning brief automation calendar query
- [ ] Add timezone parameter to all calendar queries
- [ ] Test with events on different days
- [ ] Document timezone handling in automation code

---

**Reported by:** M (Project chat)  
**Date:** Friday, November 22, 2025, 13:15  
**Status:** Identified, solution provided  
**Severity:** Medium (impacts daily planning)

---

**Note:** M can see the events correctly now using proper timezone query. This should be applied to all automated calendar queries in morning brief generation.
