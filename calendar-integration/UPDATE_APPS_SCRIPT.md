# 📝 How to Update Your Google Apps Script (5 Minutes!)

**Goal:** Add multiple notifications support to your calendar API

---

## ✨ What This Update Does:

- ✅ Multiple notifications (e.g., 1 hour + 10 minutes)
- ✅ Both popup AND email notifications
- ✅ Better error messages
- ✅ Returns confirmation with day of week
- ✅ Backwards compatible (old format still works)

---

## 🔧 UPDATE STEPS (SIMPLE!):

### 1. Open Your Script

Go to: https://script.google.com/

Click on: **"Life OS Calendar API"**

### 2. Replace the Code

1. Select ALL the code (Ctrl+A or Cmd+A)
2. Delete it
3. Open the file: `calendar-integration/apps-script-improved.js` (in this repo)
4. Copy ALL the code from that file
5. Paste into the Apps Script editor

### 3. Deploy New Version

1. Click: **"Deploy"** button (top right)
2. Click: **"Manage deployments"**
3. Click the pencil icon ✏️ next to your deployment
4. Click: **"New version"** (under Version dropdown)
5. Click: **"Deploy"**

**Your URL stays the same!** No need to update anything else!

---

## 🧪 TEST IT:

### In the Apps Script Editor:

1. At the top, change dropdown from `doPost` to `testCreateEvent`
2. Click **"Run"**
3. Check your calendar - you should see "Test Event from Apps Script"
4. Delete the test event

### From Claude.ai (Your Phone):

Say:
```
Add to my calendar: Test with multiple notifications, on 2025-11-25, from 14:00 to 15:00, color banana, notifications [60, 30, 10]

My calendar API: https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec
```

**What to expect:**
- Event created ✅
- Popup reminder 10 minutes before ✅
- Popup reminder 30 minutes before ✅
- Popup + Email reminder 1 hour before ✅

---

## 📋 NEW FORMAT:

### What Changed:

**Old format (still works):**
```json
{
  "title": "Doctor",
  "date": "2025-11-20",
  "start_time": "15:00",
  "end_time": "16:00",
  "color": "banana",
  "notification": 60
}
```

**New format (supports multiple):**
```json
{
  "title": "Doctor",
  "date": "2025-11-20",
  "start_time": "15:00",
  "end_time": "16:00",
  "color": "banana",
  "notifications": [60, 30, 10]
}
```

### Notification Logic:

- **< 60 minutes:** Popup only
- **≥ 60 minutes:** Popup + Email
- **No notifications specified:** Default 10-minute popup

---

## 🎯 WHAT YOU CAN NOW SAY:

**Natural language examples:**

```
Add to my calendar: Dentist appointment June 6 at 3pm for 90 minutes, banana color, remind me 1 hour before and 15 minutes before

My calendar API: [URL]
```

```
Create calendar event: Team meeting tomorrow 10am to 11:30am, blueberry color, notifications at 30 and 10 minutes

My calendar API: [URL]
```

---

## ⚠️ NOTES:

- Date format must be YYYY-MM-DD (e.g., 2025-06-06)
- Time format must be 24-hour HH:MM (e.g., 15:00 not 3pm)
- Notifications in minutes (e.g., 60 = 1 hour, 10 = 10 minutes)
- Default notification is 10 minutes if none specified

---

## 🆘 IF SOMETHING GOES WRONG:

**The script editor shows errors?**
- Make sure you copied ALL the code
- Click the "Test" button to see detailed error

**Deployment failed?**
- Try: Deploy → New deployment → Web app
- Set: Execute as "Me"
- Set: Who has access "Anyone"

**Old code backup:**
- Apps Script keeps version history
- Deploy → Manage deployments → Click version number to rollback

---

**That's it! 5 minutes and you have multiple notifications!** 💚

Need help? Just ask! I can walk you through any step.
