# 📅 CALENDAR QUICK REFERENCE

**For Sarah - Keep this handy on your phone!**

---

## ⚡ 2-MINUTE SETUP (DO THIS ONCE):

### On Phone:
1. Open Claude app → Menu → Settings → Custom Instructions
2. Paste this in "Response style":

```
When I ask to add a calendar event, POST to:
https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec

JSON: {title, date:"YYYY-MM-DD", start_time:"HH:MM", end_time:"HH:MM", color, notifications:[mins]}
Confirm details first. Timezone: Europe/Madrid.
```

3. Save
4. Done! Now works in ANY chat with voice! ✅

---

## 💬 HOW TO USE:

### Just say naturally:

```
Add to my calendar: Dentist June 6 at 3pm for 1 hour
```

```
Create calendar event: Meeting tomorrow 10am to 11:30am, banana color
```

```
Put on my calendar: Yoga Friday 6pm for 90 minutes, remind me 30 and 10 minutes before
```

**That's it!** Claude handles the rest.

---

## 🎨 COLORS:

banana | lavender | sage | grape | flamingo | tangerine | blueberry | tomato

---

## ⏰ NOTIFICATIONS:

- `10` = 10 min before
- `30` = 30 min before
- `60` = 1 hour before (email + popup)
- `1440` = 1 day before (email + popup)

Multiple: "remind me 1 hour before and 15 minutes before"
= notifications: [60, 15]

---

## ✅ CHECKLIST AFTER SETUP:

- [ ] Custom Instructions added to Claude app
- [ ] Tested: "Add test event to my calendar tomorrow at 2pm"
- [ ] Event appeared in Google Calendar
- [ ] Deleted test event

**If all checked: YOU'RE SET! 🎉**

---

## 🆘 TROUBLESHOOTING:

**"I don't see Custom Instructions in settings"**
→ Update Claude app to latest version

**"Event didn't create"**
→ Check Google Calendar API is still deployed
→ Make sure you said "add to my calendar" clearly

**"Wrong date/time"**
→ Use specific dates: "June 6" not "next Friday"
→ Confirm the date before Claude creates it

**"Can't remember the command"**
→ Just say: "Add [event] to my calendar on [date] at [time]"

---

## 📱 PHONE TEXT SHORTCUT (OPTIONAL):

**iOS:** Settings → General → Keyboard → Text Replacement

Shortcut: `calapi`
Phrase: `https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec`

Type "calapi" → URL appears ✨

---

## 💚 REMEMBER:

- Works from PHONE ✅
- Works with VOICE ✅
- Works in ANY chat ✅
- Takes 2 MINUTES to set up ✅

**You've got this!**

---

**Need help? Check:**
- `GOOD_MORNING_SARAH.md` for full guide
- `calendar-integration/CLAUDE_AI_CUSTOM_INSTRUCTIONS.md` for detailed setup
- `NIGHT_SHIFT_RESEARCH.md` for all the technical details

**Quick win:** Just add Custom Instructions and start using it! 🚀
