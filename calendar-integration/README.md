# 🗓️ Calendar Integration - Technical Details

**For Sarah: You don't need to read this! Use `CALENDAR_SIMPLE_GUIDE.md` in the main folder instead!**

This folder contains the technical implementation details.

---

## What's Here:

### Google Apps Script (ACTIVE - WORKS!)

**Live API:** https://script.google.com/macros/s/AKfycbwsQmuvufHqGncpuln6JE9dINsEKe2ROwDfcuXpBakqtwQ98GokTpeiAQCoAVVs05U3/exec

**Project:** Life OS Calendar API (in your Google Apps Script account)

**How it works:**
- Receives POST requests with event data
- Creates events in your Google Calendar
- Works from ANY Claude chat when you include the URL

---

### Python Scripts (FOR REFERENCE ONLY)

These were built but don't work from Claude Code due to SSL restrictions:

- `src/add_event_service.py` - Service account method
- `src/calendar_mcp_server.py` - MCP server
- Various test scripts

**We use Google Apps Script instead because it actually works!**

---

## Current Status (Nov 18, 2025):

✅ **Works:** Google Apps Script API from Claude.ai when URL is included
❌ **Doesn't work:** Python scripts from Claude Code (SSL restrictions)
⚠️ **Needs fixing:** Multiple notifications, Claude.ai memory integration

---

## For Developers:

If you need to modify the API:
1. Go to https://script.google.com/
2. Open "Life OS Calendar API" project
3. Edit the code
4. Deploy → Manage deployments → Edit → New version → Deploy

---

**Sarah: Go back to the main folder and use CALENDAR_SIMPLE_GUIDE.md!** 💚
