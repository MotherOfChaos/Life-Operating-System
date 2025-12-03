# MCP Setup Guide - Gmail & Calendar Access

**For M (Claude Projects):** This guide enables automatic Gmail and Calendar access for Sarah's morning brief.

---

## What is MCP?

MCP (Model Context Protocol) gives Claude access to external services like Gmail and Google Calendar. Once set up, M can automatically check emails and calendar when Sarah says "Good morning" - with ZERO manual steps from Sarah!

---

## Setup Status

**Current:** M can fetch morning brief from GitHub ✅
**Needed:** M needs Gmail and Calendar access to complete automation

---

## How to Set Up (Sarah - Do This Once)

### Option 1: Claude Desktop App (Recommended)

**Step 1: Check if MCP is available**
1. Open Claude Desktop app
2. Look for MCP or "Integrations" in settings
3. If you see it, continue. If not, update Claude Desktop to latest version.

**Step 2: Add Gmail MCP**
1. In Claude Desktop settings → MCP/Integrations
2. Add "Gmail" integration
3. Click "Connect" and sign in with Google
4. Grant permissions (read emails only)
5. Done!

**Step 3: Add Google Calendar MCP**
1. In same MCP/Integrations settings
2. Add "Google Calendar" integration
3. Click "Connect" and sign in with same Google account
4. Grant permissions (read calendar only)
5. Done!

**Step 4: Test**
1. In Claude Desktop, ask: "Can you check my Gmail?"
2. If M can see emails → SUCCESS!
3. Ask: "Can you check my calendar for today?"
4. If M can see events → SUCCESS!

**Step 5: Sync to Claude Projects (for phone/web)**
- The MCP settings should automatically sync to your Claude account
- Test by saying "/morning" on phone
- If Gmail/Calendar don't work on phone, you may need to reconnect MCP in web interface

---

### Option 2: Manual Email/Calendar Input (Works NOW - No Setup)

If MCP setup is too complicated or doesn't work:

**Every morning when you say "Good morning":**
1. M shows your TOP 5 priorities ✅ (automatic)
2. M shows news digest ✅ (automatic)
3. M asks: "Do you have any urgent emails?"
4. You reply: "Yes, 2 urgent - one from Andreu about aircon, one from Ruy about meeting"
5. M asks: "Any calendar events today?"
6. You reply: "Meeting at 3pm with Fergie"
7. M presents complete overview

**This takes 30 seconds and works TODAY with zero setup!**

---

## For M: How to Use MCP Tools

Once MCP is set up, you'll have access to these tools:

### Gmail Tool
```
- List recent emails
- Filter by unread, sender, date
- Get email content
- Mark as read (optional)
```

### Calendar Tool
```
- List today's events
- Get event details
- Filter out recurring/"notes"/all-day events
```

### In /morning Command

When Sarah says "Good morning", you should:
1. Fetch morning brief from GitHub (Step 1)
2. Generate news digest with web search (Step 1b)
3. **Check Gmail** using MCP tool (Step 2)
   - Categorize into 7 categories as instructed
4. **Check Calendar** using MCP tool (Step 2b)
   - Filter out "notes", all-day, "Baja medica" events
5. Present everything in one complete overview

---

## Troubleshooting

**MCP not available in Claude Desktop:**
- Update to latest version
- Check https://docs.anthropic.com for MCP availability

**Permissions errors:**
- Re-authenticate Google account
- Check that Gmail/Calendar APIs are enabled

**Works on Desktop but not Phone:**
- MCP might only work on Desktop currently
- Use Option 2 (manual input) on phone for now

---

## Summary

**BEST:** Set up MCP → Full automation everywhere
**GOOD:** Use manual input → Works TODAY, takes 30 seconds
**Either way:** Morning brief automation is working! ✅

