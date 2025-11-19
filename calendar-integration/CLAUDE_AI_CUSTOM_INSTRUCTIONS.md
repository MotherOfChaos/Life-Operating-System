# 📱 Claude.ai Custom Instructions for Calendar Integration

**Purpose:** Make calendar creation work from ANY Claude chat (including phone with voice!)

---

## 🎯 WHERE TO ADD THIS:

### On Claude.ai Web:
1. Go to: https://claude.ai/
2. Click your profile icon (bottom left)
3. Click: **"Settings"**
4. Click: **"Custom Instructions"**
5. Paste the instruction below in **"How would you like Claude to respond?"**

### On Claude Mobile App:
1. Open Claude app
2. Tap menu (☰) → Settings
3. Tap: **"Custom Instructions"**
4. Paste in the "Response style" section

---

## 📝 CUSTOM INSTRUCTION (COPY THIS):

```
CALENDAR EVENT CREATION:

When I ask you to add/create a calendar event, use this API:

Endpoint: https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec

Method: POST
Format: JSON

Required fields:
- title: event name
- date: YYYY-MM-DD format only
- start_time: HH:MM (24-hour)
- end_time: HH:MM (24-hour)

Optional fields:
- color: lavender|sage|grape|flamingo|banana|tangerine|peacock|graphite|blueberry|basil|tomato
- notifications: array of minutes [60, 30, 10]
- location: text
- description: text

Important date handling:
1. Always convert relative dates ("tomorrow", "next Friday") to YYYY-MM-DD
2. Calculate day of week and confirm with me before creating
3. Use Europe/Madrid timezone
4. If unsure about date, ask me to confirm

Example request:
{
  "title": "Dentist appointment",
  "date": "2025-06-06",
  "start_time": "15:00",
  "end_time": "16:30",
  "color": "banana",
  "notifications": [60, 15]
}

Always confirm the event details with me before making the API call, showing:
- Event name
- Full date (YYYY-MM-DD) and day of week
- Time range
- Notifications

After creating, tell me if it succeeded and show the confirmation details.
```

---

## 💬 HOW TO USE (NATURAL LANGUAGE!):

Once you add the custom instruction, just say:

### Simple Events:

```
Add to my calendar: Dentist June 6 at 3pm for 90 minutes
```

```
Create calendar event: Team meeting tomorrow 10am to 11:30am
```

### With All Options:

```
Add to my calendar: Doctor appointment next Friday at 4pm for 1 hour, banana color, remind me 1 hour before and 15 minutes before
```

```
Put on my calendar: Yoga class December 1 at 6pm lasting 90 minutes, sage color, send notifications at 30 minutes and 10 minutes before
```

### Voice Commands (Phone):

Just tap the voice button and say naturally:

- "Add dentist appointment to my calendar June sixth at three PM for one hour"
- "Create a calendar event for team meeting tomorrow at ten AM lasting ninety minutes"

**Claude will:**
1. Parse your natural language
2. Convert to correct format
3. Confirm the details with you
4. Create the event
5. Tell you it succeeded

---

## 🎨 COLOR OPTIONS:

- **lavender** (pale blue)
- **sage** (pale green)
- **grape** (purple/mauve)
- **flamingo** (pale red/pink)
- **banana** (yellow) ← recommended for appointments
- **tangerine** (orange)
- **peacock** (cyan/turquoise)
- **graphite** (gray)
- **blueberry** (blue)
- **basil** (green)
- **tomato** (red)

---

## ⏰ NOTIFICATION EXAMPLES:

- `[60]` = 1 hour before (popup + email)
- `[30]` = 30 minutes before (popup only)
- `[60, 30, 10]` = three reminders (1 hour with email, 30 min popup, 10 min popup)
- `[1440]` = 1 day before (popup + email)

**Tip:** Notifications >= 60 minutes get both popup AND email!

---

## ✅ TESTING:

After adding the custom instruction, test with:

```
Add to my calendar: Test event tomorrow at 2pm for 30 minutes, banana color, remind me 15 minutes before
```

Claude should:
1. Show you the parsed details
2. Ask you to confirm
3. Make the API call
4. Tell you it succeeded

Then check your Google Calendar to verify!

---

## 🔧 TROUBLESHOOTING:

### "I don't have access to calendar integration"

Claude.ai's **native** calendar integration is read-only. We're using our **custom API** instead - no need for native integration!

### "The API returned an error"

Common issues:
- Date not in YYYY-MM-DD format
- Time not in HH:MM 24-hour format
- Missing required fields

Ask Claude to show you the exact JSON it's sending.

### "Wrong day of week"

Tell Claude: "That's [correct day], not [wrong day]" and it will recalculate.

### Custom instruction too long?

Use this shorter version:

```
For calendar events, POST to: https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec
JSON: {title, date:"YYYY-MM-DD", start_time:"HH:MM", end_time:"HH:MM", color, notifications:[mins]}
Confirm details before creating. Timezone: Europe/Madrid
```

---

## 💚 BENEFITS:

With this custom instruction:
- ✅ Works in ANY Claude chat
- ✅ Works from phone with voice
- ✅ Works from web
- ✅ Natural language support
- ✅ Multiple notifications
- ✅ Color coding
- ✅ ADHD-friendly (no complex commands!)

---

## 📱 MOBILE TIP:

Save a shorter version in your phone's text replacement:

**Shortcut:** `calapi`
**Phrase:** `https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec`

Then if you ever need to include the URL manually, just type "calapi" and it expands!

---

**That's it! Now ANY Claude chat can create calendar events!** 🎉
