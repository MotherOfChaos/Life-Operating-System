# 📱 HOW ANY CLAUDE CAN ADD CALENDAR EVENTS FOR SARAH

**For: Pilot, M, or ANY Claude assistant**

When Sarah says something like:
- "Add to my calendar..."
- "Put on my calendar..."
- "Schedule..."

Use this API to add events to her Google Calendar!

---

## 🔗 SARAH'S CALENDAR API URL:

```
https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec
```

---

## 📋 HOW TO USE IT:

### Example Request:

Sarah says: "Add dentist appointment tomorrow at 2pm for 1 hour, flamingo color, remind me 30 minutes before"

**You (Claude) do:**

```bash
curl -X POST 'https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Dentist appointment",
    "date": "2025-11-19",
    "start_time": "14:00",
    "end_time": "15:00",
    "color": "flamingo",
    "notification": 30
  }'
```

---

## 📝 PARAMETERS:

- **title** (required): Event title
- **date** (required): YYYY-MM-DD format
- **start_time** (required): HH:MM format (24-hour)
- **end_time** (required): HH:MM format (24-hour)
- **color** (optional): lavender, sage, grape, flamingo, banana, tangerine, peacock, graphite, blueberry, basil, tomato
- **notification** (optional): Minutes before event to send email reminder

---

## 🎨 NATURAL LANGUAGE PARSING:

Parse Sarah's natural language into the structured format:

**Examples:**

"Tomorrow 2pm dentist" →
- date: tomorrow's date in YYYY-MM-DD
- start_time: "14:00"
- end_time: "15:00" (default 1 hour)
- title: "Dentist"

"Friday Nov 22 at 10:30am team meeting for 90 minutes" →
- date: "2025-11-22"
- start_time: "10:30"
- end_time: "12:00"
- title: "Team meeting"

"Yoga class next Monday 6pm, sage color, remind me 1 hour before" →
- date: next Monday's date
- start_time: "18:00"
- end_time: "19:00"
- title: "Yoga class"
- color: "sage"
- notification: 60

---

## ✅ SUCCESS RESPONSE:

```json
{
  "success": true,
  "message": "Event created!",
  "title": "Dentist appointment",
  "start": "2025-11-19T14:00:00.000Z",
  "eventId": "..."
}
```

Tell Sarah: "✅ Added to your calendar: [title] on [date] at [time]"

---

## ❌ ERROR RESPONSE:

```json
{
  "success": false,
  "error": "..."
}
```

Tell Sarah what went wrong and offer to try again.

---

## 💚 SARAH'S TIMEZONE:

**Europe/Madrid (CET/CEST)**

When parsing "tomorrow" or relative dates, use her timezone!

---

## 🎉 THIS WORKS FROM:

✅ Claude.ai web
✅ Claude mobile app
✅ Claude Code
✅ Literally ANY Claude chat, ANYWHERE!

---

**Sarah can now use voice on her phone to add calendar events! This is the execute-while-sleeping model in action!** 💚✨
