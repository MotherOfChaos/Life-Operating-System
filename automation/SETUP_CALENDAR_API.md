# Google Calendar API Setup

## What This Does

Lets M manage your Google Calendar (sarahpoer@gmail.com):
- ✅ List upcoming events
- ➕ Add new events
- ✏️ Modify existing events
- 🗑️ Delete events

## Step 1: Enable Calendar API

1. Go to: https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
2. Make sure you're logged in as sarahpoer@gmail.com
3. Click "Enable"

## Step 2: Use Same OAuth Credentials

Good news! You can use the SAME credentials from Gmail setup:

1. Go to: https://console.cloud.google.com/apis/credentials
2. Find your "Life-OS-Email-Checker" OAuth client
3. Click "Edit"
4. The credentials already work for Calendar API too!

**OR** create separate credentials:
- Follow same steps as Gmail
- Name it "Life-OS-Calendar-Manager"
- Add as separate secret: `GOOGLE_CALENDAR_CREDENTIALS`

## Step 3: First-Time Authorization

Same as Gmail - first run needs your permission:
1. Workflow shows URL in logs
2. Open URL, log in as sarahpoer@gmail.com
3. Click "Allow"
4. Done! Works automatically after that

## How M Uses It

**List events:**
"What's on my calendar today?"
"Show me next week's calendar"

**Add event:**
"Add meeting with Ruy tomorrow at 3pm"
"Schedule dentist appointment Friday 10am"

**Modify event:**
"Move my 2pm meeting to 4pm"
"Change dentist to next week"

**Delete event:**
"Cancel my 3pm meeting"
"Remove yoga class from calendar"

## M Triggers Calendar Action

1. You ask M about calendar
2. M triggers GitHub Action with parameters
3. Action performs calendar operation
4. M shows you the result

## Permissions Needed

- Read calendar events
- Create calendar events
- Modify calendar events  
- Delete calendar events

All on your primary calendar (sarahpoer@gmail.com).

## Privacy & Security

- Stored securely in GitHub Secrets
- Only access to YOUR calendar
- Can revoke anytime: https://myaccount.google.com/permissions
- No access to other Google services

## Testing

After setup:
- "What's on my calendar this week?"
- "Add test event tomorrow at noon"
- "Delete test event"

## Scopes Required

If creating separate credentials, add these scopes:
- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/calendar.events`
