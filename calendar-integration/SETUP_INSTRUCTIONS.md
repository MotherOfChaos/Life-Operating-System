# 🗓️ Google Calendar Integration - Setup Instructions

**Your wish: "Add this appointment to my Google Calendar" from ANY Claude chat**

I've built two ways to make this happen:
1. **MCP Server** - Works in any Claude chat (desktop app)
2. **CLI Tool** - Direct command-line access

---

## 🎯 Quick Start (Choose Your Path)

### Path A: MCP Server (Recommended - works in ANY Claude chat)
### Path B: CLI Tool (Direct command-line use)

---

## 📋 Prerequisites (Do Once)

### 1. Install Python Dependencies

```bash
cd ~/Life-Operating-System/calendar-integration
pip3 install -r requirements.txt
```

### 2. Get Google Calendar API Credentials

This is the ONE-TIME setup that lets the system access your calendar:

#### Step 2a: Create Google Cloud Project
1. Go to https://console.cloud.google.com/
2. Create a new project (or use existing)
3. Enable Google Calendar API:
   - Search for "Google Calendar API"
   - Click "Enable"

#### Step 2b: Create OAuth Credentials
1. Go to "Credentials" in left sidebar
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   - User Type: External (or Internal if you have workspace)
   - App name: "Sarah's Life OS Calendar"
   - User support email: your email
   - Add your email as test user
4. Create OAuth client ID:
   - Application type: **Desktop app**
   - Name: "Life OS Calendar Integration"
5. Download the JSON file
6. Save it as: `~/.config/claude-calendar/credentials.json`

```bash
mkdir -p ~/.config/claude-calendar
# Move your downloaded file here:
mv ~/Downloads/client_secret_*.json ~/.config/claude-calendar/credentials.json
```

### 3. First-Time Authorization

Run this once to authorize:

```bash
cd ~/Life-Operating-System/calendar-integration/src
python3 add_event.py "Test Event" "today" "14:00" "15:00"
```

This will:
- Open your browser
- Ask you to sign in to Google
- Ask permission to access your calendar
- Save authorization token for future use

**IMPORTANT:** The token is saved at `~/.config/claude-calendar/token.json`. Keep it secure!

---

## 🚀 Path A: MCP Server Setup (For "Any Claude Chat")

### 1. Configure Claude Desktop App

Edit your Claude Desktop MCP config:

**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add this section:

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "python3",
      "args": [
        "/home/user/Life-Operating-System/calendar-integration/src/calendar_mcp_server.py"
      ]
    }
  }
}
```

**Note:** Adjust the path if your Life-Operating-System is in a different location.

### 2. Restart Claude Desktop App

Completely quit and restart Claude.

### 3. Test It!

In ANY Claude chat, say:

```
Add this event to my calendar:
Tuesday, November 19, 2025
2:00pm to 3:00pm
Coffee with Mom
Color: lavender
Notify me 30 minutes before
```

Claude will now have access to the `add_calendar_event` tool! 🎉

---

## 🚀 Path B: CLI Tool (Direct Use)

### Usage Examples

```bash
# Navigate to the tool
cd ~/Life-Operating-System/calendar-integration/src

# Simple event
./add_event.py "Team Meeting" "today" "14:00" "15:00"

# Event with all options
./add_event.py "PACO AIR CON @ABarraca" "Tuesday, November 18, 2025" "11:00" "12:00" \
  --color tangerine \
  --notification 20

# Using natural language dates
./add_event.py "Dentist Appointment" "tomorrow" "10:00" "11:00" \
  --location "Clinic" \
  --color flamingo \
  --notification 60

# Event with description
./add_event.py "Project Review" "2025-11-20" "15:30" "16:30" \
  --description "Quarterly review with team" \
  --color peacock
```

### Make it Global (Optional)

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
alias add-event='python3 ~/Life-Operating-System/calendar-integration/src/add_event.py'
```

Then use it anywhere:
```bash
add-event "Yoga Class" "today" "18:00" "19:00" --color sage
```

---

## 🎨 Available Colors

- `lavender` - Purple
- `sage` - Light green
- `grape` - Dark purple
- `flamingo` - Pink
- `banana` - Yellow
- `tangerine` - Orange 🍊
- `peacock` - Teal/Blue
- `graphite` - Dark gray
- `blueberry` - Blue
- `basil` - Green
- `tomato` - Red

---

## 🧪 Test Event (From Your Request)

I've created a test script with your exact event:

```bash
cd ~/Life-Operating-System/calendar-integration/tests
./test_paco_event.sh
```

This will add:
- **Title:** PACO AIR CON @ABarraca
- **Date:** Tuesday, November 18, 2025
- **Time:** 11:00 - 12:00
- **Color:** Tangerine 🍊
- **Notification:** Email 20 minutes before

---

## 📱 ADHD-Friendly Quick Commands

Once set up, you can say to Claude (in ANY chat if using MCP):

### Natural Language Style:
```
"Add appointment: Thursday 2pm dentist, color it flamingo, remind me 1 hour before"

"Put on my calendar: tomorrow 10am coffee with Dad at ABarraca"

"Calendar: Friday Nov 22, 11:00-12:30, Team Meeting, peacock color, email me 15 min before"
```

### Structured Style:
```
Add to calendar:
- Wednesday, Nov 20
- 3:00pm to 4:30pm
- Rehearsal @Teatro Metamorfosis
- Color: grape
- Notify: 30 minutes before
```

---

## 🔧 Troubleshooting

### "Credentials not found"
- Make sure `~/.config/claude-calendar/credentials.json` exists
- Check the file has your OAuth client credentials from Google Cloud

### "Token expired"
- Delete `~/.config/claude-calendar/token.json`
- Run the CLI tool again to re-authorize

### MCP server not showing in Claude
- Check your Claude config file path is correct
- Verify the Python script path in the config
- Restart Claude Desktop completely
- Check Claude's MCP status (should show "google-calendar" connected)

### "Permission denied"
- Make the scripts executable:
  ```bash
  chmod +x ~/Life-Operating-System/calendar-integration/src/*.py
  chmod +x ~/Life-Operating-System/calendar-integration/tests/*.sh
  ```

---

## 💚 What This Gives You

✅ **From any Claude chat:** "Add this to my calendar" → Done!
✅ **Natural language:** Claude understands your casual descriptions
✅ **All the details:** Time, location, color, notifications
✅ **ADHD-friendly:** No context switching, no app hopping
✅ **Syncs everywhere:** Google Calendar = phone, computer, everywhere

---

## 🔐 Security Notes

- OAuth tokens are stored locally at `~/.config/claude-calendar/`
- Only YOU can authorize the app
- Only YOUR calendar is accessed
- Tokens can be revoked at https://myaccount.google.com/permissions
- The MCP server runs locally on your machine

---

## 📚 Files Created

```
calendar-integration/
├── src/
│   ├── calendar_mcp_server.py    # MCP server for Claude
│   └── add_event.py               # CLI tool
├── config/
│   └── mcp_config_template.json   # Example config
├── tests/
│   └── test_paco_event.sh         # Test with your event
├── requirements.txt               # Python dependencies
└── SETUP_INSTRUCTIONS.md          # This file
```

---

## 🌙 Execute-While-Sleeping Model

Built this while you sleep, ready when you wake! 💚

Next steps when you're back:
1. Follow Prerequisites (one-time setup)
2. Choose MCP Server OR CLI Tool
3. Test with the PACO event
4. Start using "add to calendar" in any chat!

Sweet dreams, Mother of Chaos! 🗓️✨

---

**Questions?** Check the troubleshooting section or ask M in any chat!
