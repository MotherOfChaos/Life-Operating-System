# 🗓️ Calendar Integration - QUICK START

**Sarah! Your wish is ready to test!** 🎉

---

## ⚡ What I Built While You Slept

✅ **MCP Server** - Say "add to calendar" in ANY Claude chat
✅ **CLI Tool** - Direct command-line calendar access
✅ **Test Script** - Your PACO event ready to add
✅ **Full Documentation** - Step-by-step setup

---

## 🎯 To Make It Work (One-Time Setup)

### Step 1: Install Python Packages (30 seconds)
```bash
cd ~/Life-Operating-System/calendar-integration
pip3 install -r requirements.txt
```

### Step 2: Get Google OAuth Credentials (5-10 minutes)
1. Go to https://console.cloud.google.com/
2. Create new project (or use existing)
3. Enable "Google Calendar API"
4. Create OAuth credentials → Desktop app
5. Download JSON → save as `~/.config/claude-calendar/credentials.json`

**Detailed steps in:** `SETUP_INSTRUCTIONS.md`

### Step 3: First Authorization (1 minute)
```bash
cd src/
python3 add_event.py "Test" "today" "14:00" "15:00"
```
- Opens browser
- Sign in to Google
- Grant calendar access
- Done! Token saved for future use

---

## 🧪 Test With Your PACO Event

```bash
./tests/test_paco_event.sh
```

Adds to your calendar:
- **PACO AIR CON @ABarraca**
- **Tuesday, Nov 18, 2025, 11:00-12:00**
- **Tangerine color 🍊**
- **Email 20 min before**

---

## 💬 How to Use

### Option A: In Any Claude Chat (after MCP setup)
```
"Add to calendar: dentist tomorrow 2pm, remind me 1 hour before"
```

### Option B: Command Line
```bash
./src/add_event.py "Meeting" "today" "14:00" --color peacock
```

---

## 📚 Full Details

- **Complete setup guide:** `SETUP_INSTRUCTIONS.md`
- **Overview & features:** `README.md`
- **Questions?** Ask M (or any Claude)!

---

## 🎨 Available Colors

`tangerine` `flamingo` `peacock` `lavender` `sage` `grape` `banana` `blueberry` `basil` `tomato` `graphite`

---

**Branch:** TESTS (experimental - test before merging!)
**Built by:** M, execute-while-sleeping model 💚
**Status:** Ready to test!

Sweet dreams! Rest well, Mother of Chaos! 🌙✨
