# iOS Shortcut Setup Instructions

**Purpose:** One-tap automation to load M's context on iPhone/iPad
**Time to setup:** 5-10 minutes (one-time only)
**Friction reduction:** 8 steps → 2 taps

---

## OPTION A: Import via iCloud Link (EASIEST)

I'll create an importable Shortcut file that you can install with one tap.

**Once I provide the link:**
1. Open the link on your iPhone
2. Tap "Add Shortcut"
3. Review the actions (make sure PAT is correct)
4. Tap "Add Untrusted Shortcut" (if prompted)
5. Done!

---

## OPTION B: Build Manually (15 minutes)

If you prefer to build it yourself or the import doesn't work:

### Step 1: Open Shortcuts App

1. Open the **Shortcuts** app on iPhone
2. Tap **+** (top right) to create new shortcut
3. Tap "Add Action"

### Step 2: Add GitHub API Fetches

**For each of the 3 files, add these actions:**

#### File 1: SARAH_LIFE_OS_CURRENT.json

1. Search for "**Get Contents of URL**"
2. Set URL to:
   ```
   https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/SARAH_LIFE_OS_CURRENT.json
   ```
3. Tap "Show More" → Add Headers:
   - `Authorization`: `token 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`
   - `Accept`: `application/vnd.github.v3.raw`
4. Method: **GET**
5. Search for "**Set Variable**"
6. Name it: `File1Content`

#### File 2: SARAH_DAILY_TRACKER_CURRENT.md

Repeat the above with:
- URL: `https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/SARAH_DAILY_TRACKER_CURRENT.md`
- Variable name: `File2Content`
- Same headers

#### File 3: TRANSFER_README_CURRENT.md

Repeat the above with:
- URL: `https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/TRANSFER_README_CURRENT.md`
- Variable name: `File3Content`
- Same headers

### Step 3: Format the Message

1. Search for "**Text**" action
2. Build this message (you can copy/paste and use the variable buttons):

```
Hi M! 💚 Here's my latest Life OS context:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 SARAH_LIFE_OS_CURRENT.json
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Insert Variable: File1Content]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 SARAH_DAILY_TRACKER_CURRENT.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Insert Variable: File2Content]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 TRANSFER_README_CURRENT.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Insert Variable: File3Content]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Authenticate as M and continue where we left off.
Mens sana in corpore sano, my friend. 🌹
```

3. Search for "**Set Variable**"
4. Name it: `CompleteMessage`

### Step 4: Copy to Clipboard

1. Search for "**Copy to Clipboard**"
2. Select the `CompleteMessage` variable

### Step 5: Open Claude App

1. Search for "**Open App**"
2. Select **Claude**

### Step 6: Show Notification (Optional)

1. Search for "**Show Notification**"
2. Set text to: "Context copied! Paste into Claude and send 💚"

### Step 7: Name and Save

1. Tap the shortcut name at top (probably "Shortcut")
2. Rename to: **"M Context"** or **"Good Morning M"**
3. Tap "Done"

---

## USAGE OPTIONS

### Option 1: Home Screen Widget

1. Long-press on iPhone home screen
2. Tap **+** (top left) to add widget
3. Search for "**Shortcuts**"
4. Select widget size
5. Tap "**Add Widget**"
6. Long-press the widget → **Edit Widget**
7. Select your "M Context" shortcut
8. Now you have a one-tap button on home screen! 🎯

### Option 2: Siri Voice Command

1. Open Shortcuts app
2. Tap your "M Context" shortcut
3. Tap the ⓘ (info) button
4. Toggle ON: "**Add to Siri**"
5. Record phrase: "**Good morning M**" or "**Load M context**"
6. Now you can say "Hey Siri, good morning M" and it runs! 🎙️

### Option 3: Manual Tap

1. Open Shortcuts app
2. Tap "M Context"
3. Done!

### Option 4: Automation (ADVANCED)

Make it run automatically at specific times or conditions:

1. Open Shortcuts app → **Automation** tab
2. Tap **+** (top right)
3. Choose trigger:
   - **Time of Day** (e.g., 8:00 AM every morning)
   - **When Alarm Stopped** (right when you wake up)
   - **When I Leave** a location (e.g., when leaving home)
4. Select your "M Context" shortcut
5. Toggle OFF "Ask Before Running" (for full automation)
6. Done!

**Example:** Auto-run every morning at 8am when your alarm goes off 🌅

---

## HOW TO USE

### Every time you want to start a new Claude chat with M:

**Method 1: Widget**
1. Tap the home screen widget → **[1 second]**
2. Claude opens with notification
3. Long-press in chat → Tap "Paste" → **[1 tap]**
4. Tap "Send" → **[1 tap]**
5. **Total: 3 taps, ~5 seconds** ✅

**Method 2: Siri**
1. Say "Hey Siri, good morning M" → **[voice command]**
2. Claude opens with notification
3. Long-press in chat → Tap "Paste" → **[1 tap]**
4. Tap "Send" → **[1 tap]**
5. **Total: 2 taps + voice, ~5 seconds** ✅

**Method 3: Automation (Best!)**
1. Wake up, alarm stops → **[automatic trigger]**
2. Get notification: "Context copied!"
3. Open Claude → **[tap app]**
4. Paste → Send → **[2 taps]**
5. **Total: 3 taps, ~5 seconds, zero thinking** ✅✅✅

---

## TROUBLESHOOTING

### "Untrusted Shortcut" warning
- This is normal for shortcuts with web requests
- Tap "Allow" in Settings → Shortcuts → "Allow Running Scripts"

### GitHub API returns 401 Unauthorized
- Check that PAT is correct (no spaces, full token)
- Verify PAT hasn't expired
- Regenerate PAT if needed from GitHub settings

### GitHub API returns 404 Not Found
- Check file names are exact (case-sensitive)
- Verify repository name is correct
- Make sure PAT has access to private repos

### Claude app doesn't open
- Make sure Claude app is installed
- Try manually opening Claude first
- Update to latest Claude app version

### Paste doesn't work in Claude
- Sometimes clipboard content is too large
- Try breaking into smaller messages
- Alternative: Upload as text file instead

### Files are empty or corrupted
- Check the "Accept" header is set correctly
- Verify you're using `application/vnd.github.v3.raw`
- Test URLs in browser to confirm they work

---

## SECURITY NOTE

Your GitHub Personal Access Token (PAT) is stored in the Shortcut.

**This is safe because:**
- Shortcuts are stored locally on your iPhone
- Only you have access
- PAT only has read access to one private repo
- You can revoke it anytime from GitHub settings

**To be extra cautious:**
- Don't share this Shortcut with anyone
- Don't post screenshots that show the PAT
- Regenerate the PAT periodically (every 3-6 months)

---

## UPDATING THE SHORTCUT

If your PAT changes or file names change:

1. Open Shortcuts app
2. Long-press your "M Context" shortcut
3. Tap "**Edit**"
4. Update the Authorization header with new PAT
5. Update file URLs if needed
6. Tap "Done"

---

## ALTERNATIVE: SIMPLIFIED VERSION

If the full version is too complex, here's a minimal version:

**Just paste this pre-formatted message into Claude:**

```
Hi M! Please fetch my latest context from GitHub:

Repo: MotherOfChaos/Life-Operating-System
Files: SARAH_LIFE_OS_CURRENT.json, SARAH_DAILY_TRACKER_CURRENT.md, TRANSFER_README_CURRENT.md
PAT: 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

Use GitHub API to pull these files, then authenticate as M and continue where we left off. 💚
```

Save this in iOS Notes as "M Context" for quick access.

**Pros:** Super simple, no setup
**Cons:** Relies on Claude's ability to fetch (not guaranteed on mobile)

---

## NEXT LEVEL: COMBINE WITH VOICE MODE

Once context is loaded, you can use Claude's voice mode!

1. Run shortcut → Paste context → Send
2. Wait for M to authenticate
3. Tap the microphone icon
4. Now you can talk to M hands-free! 🎙️💚

**Perfect for:**
- Morning routines while getting ready
- Bedtime check-ins while in bed
- Commute conversations while driving

---

**Questions? Issues? Let me know and I'll help troubleshoot!** 🔧

- Cody
