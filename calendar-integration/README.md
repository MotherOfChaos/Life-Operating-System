# 🗓️ Google Calendar Integration for Sarah's Life OS

**"Add this appointment to my Google Calendar" - FROM ANY CLAUDE CHAT**

Built while you sleep. Execute-while-sleeping model in action! 💚

---

## ⚡ What You Asked For

> "I want to be able to say 'add this appointment (including data) to my Google calendar', from any Claude chat, and that it works."

**Status: ✅ BUILT AND READY TO TEST**

---

## 🎯 Quick Start (3 Steps)

### 1️⃣ Install Dependencies
```bash
cd ~/Life-Operating-System/calendar-integration
pip3 install -r requirements.txt
```

### 2️⃣ Set Up Google Calendar Access
- Follow the detailed steps in `SETUP_INSTRUCTIONS.md`
- One-time setup to get Google OAuth credentials
- Takes about 5-10 minutes

### 3️⃣ Choose Your Integration

**Option A - MCP Server (RECOMMENDED)**
- Works in ANY Claude chat (desktop app)
- Just say "add to calendar..." naturally
- See `SETUP_INSTRUCTIONS.md` section "Path A"

**Option B - CLI Tool**
- Direct command-line access
- `./src/add_event.py "Meeting" "today" "14:00" "15:00"`
- See `SETUP_INSTRUCTIONS.md` section "Path B"

---

## 🧪 Test It Right Now

Once you've done the setup:

```bash
./tests/test_paco_event.sh
```

This adds YOUR test event:
- PACO AIR CON @ABarraca
- Tuesday, November 18, 2025, 11:00-12:00
- Tangerine color 🍊
- Email notification 20 minutes before

---

## 💬 How to Use (After Setup)

### In any Claude chat:
```
"Add to my calendar:
Thursday 2pm dentist appointment
Color it flamingo
Remind me 1 hour before"
```

### Command line:
```bash
cd src/
./add_event.py "Yoga Class" "tomorrow" "18:00" "19:00" --color sage
```

---

## 📂 What's Inside

```
calendar-integration/
├── README.md                      ← You are here
├── SETUP_INSTRUCTIONS.md          ← Full detailed setup guide
├── requirements.txt               ← Python packages needed
├── src/
│   ├── calendar_mcp_server.py    ← MCP server (for Claude chats)
│   └── add_event.py              ← CLI tool (direct use)
├── config/
│   └── mcp_config_template.json  ← Example MCP configuration
└── tests/
    └── test_paco_event.sh        ← Test with your PACO event
```

---

## 🎨 Features

✅ **Natural language dates:** "today", "tomorrow", "next Friday"
✅ **Flexible time formats:** "11:00", "11.00", "2:30pm"
✅ **11 calendar colors:** tangerine, flamingo, peacock, etc.
✅ **Email notifications:** X minutes before event
✅ **Location support:** Add meeting places
✅ **ADHD-friendly:** No app switching, just tell Claude

---

## 🔐 Security

- Runs locally on your machine
- Uses Google OAuth (industry standard)
- Only YOU can authorize access
- Tokens stored securely at `~/.config/claude-calendar/`
- Can revoke access anytime at https://myaccount.google.com/permissions

---

## 💚 The Execute-While-Sleeping Model

You said: "I'll be sleeping so need you to go on on your own"

I built:
- ✅ Full MCP server for "any Claude chat" integration
- ✅ Standalone CLI tool for direct use
- ✅ Test script with your exact event
- ✅ Comprehensive setup instructions
- ✅ ADHD-friendly natural language parsing
- ✅ All 11 Google Calendar colors supported
- ✅ Email notifications
- ✅ Location, description, custom times

All ready for you when you wake up! 🌙✨

---

## 📋 Next Steps When You Wake

1. Read `SETUP_INSTRUCTIONS.md` (comprehensive guide)
2. Do the one-time Google OAuth setup (5-10 minutes)
3. Run `./tests/test_paco_event.sh` to test
4. Start using "add to calendar" in any Claude chat! 🎉

---

## ❓ Questions or Issues?

Check `SETUP_INSTRUCTIONS.md` for:
- Detailed setup steps
- Troubleshooting section
- Usage examples
- Security notes

Or ask M (or any Claude) - the MCP integration means we can all help! 💚

---

**Built with:** Python, Google Calendar API, MCP SDK
**Built for:** ADHD-friendly calendar management
**Built by:** M, while Sarah sleeps 🌙

Mens sana in corpore sano, my friend. 💚
