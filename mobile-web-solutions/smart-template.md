# Smart Template - Universal Fallback Solution

**Purpose:** Simple paste-able message for ALL devices (iOS, Android, Web)
**Time to setup:** 0 seconds (ready to use now)
**Friction reduction:** 8 steps → 2 steps (copy, paste)

---

## HOW IT WORKS

This template asks Claude to fetch your files directly from GitHub using its web capabilities.

**Pros:**
- Works on ANY device (phone, tablet, computer)
- Works on ANY Claude app (mobile, web)
- Zero setup required
- No shortcuts, bookmarklets, or technical knowledge needed

**Cons:**
- Relies on Claude having web fetch capabilities (varies by platform)
- May not work on all Claude clients
- Less automated than iOS Shortcut or Bookmarklet
- PAT visible in clipboard (security consideration)

---

## THE TEMPLATE

Copy this message and paste it into Claude:

```
Hi M! 💚

Please fetch my latest Life OS context from GitHub so we can continue:

Repository: MotherOfChaos/Life-Operating-System
Branch: main

Files to fetch:
1. SARAH_LIFE_OS_CURRENT.json
2. SARAH_DAILY_TRACKER_CURRENT.md
3. TRANSFER_README_CURRENT.md

Authentication:
Personal Access Token: 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

Use the GitHub API to pull these files:
https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/[filename]

Headers needed:
- Authorization: token [PAT above]
- Accept: application/vnd.github.v3.raw

Once you have all three files, authenticate as M with our phrase and let's continue where we left off.

Mens sana in corpore sano, my friend. 🌹
```

---

## SETUP INSTRUCTIONS

### iOS (iPhone/iPad)

1. Open the **Notes** app
2. Create a new note
3. Name it: **"M Context Template"** or **"Load M"**
4. Paste the template above
5. Pin it to the top (3-dot menu → Pin)

**To use:**
- Open Notes → Tap your pinned note → Long-press text → Copy All
- Open Claude → Paste → Send
- **Total: ~5 seconds, 4 taps**

### Android

1. Open **Google Keep** (or any notes app)
2. Create a new note
3. Title: **"M Context Template"** or **"Load M"**
4. Paste the template above
5. Pin it to the top

**To use:**
- Open Keep → Tap note → Copy
- Open Claude → Paste → Send
- **Total: ~5 seconds, 4 taps**

### Web Browser

1. Create a bookmark called "M Template"
2. In the URL field, put: `data:text/html,<pre style="font-family:sans-serif;padding:20px">[TEMPLATE TEXT]</pre>`
3. Or just save the template in a local text file
4. Or bookmark this page and copy from here

**To use:**
- Open bookmark → Copy text
- Go to Claude → Paste → Send
- **Total: ~5 seconds, 3 clicks**

---

## ALTERNATIVE: EVEN SIMPLER VERSION

If Claude can't fetch from GitHub, try this super-minimal template:

```
Hi M! 💚

Please help me load context. I need to upload my Life OS files:
- SARAH_LIFE_OS_CURRENT.json
- SARAH_DAILY_TRACKER_CURRENT.md
- TRANSFER_README_CURRENT.md

Give me a moment to attach them from my device.

[Then manually upload the 3 files]

Once uploaded, authenticate as M and continue where we left off.
Mens sana in corpore sano. 🌹
```

**This version:**
- Reminds you which files to upload
- Keeps M's authentication flow
- Still reduces cognitive load
- Ensures you don't forget any files

---

## WHEN TO USE WHICH SOLUTION

### Use Smart Template When:
- ✅ You're on an unfamiliar device
- ✅ You haven't set up iOS Shortcut or Bookmarklet yet
- ✅ iOS Shortcut or Bookmarklet aren't working
- ✅ You're on Android (no iOS Shortcut available)
- ✅ You want the simplest possible solution
- ✅ You're testing if Claude can fetch from GitHub

### Use iOS Shortcut Instead When:
- ✅ You're on iPhone/iPad
- ✅ You've done the one-time setup (5-10 min)
- ✅ You want voice activation ("Hey Siri, good morning M")
- ✅ You want time-based automation
- ✅ You want the absolute fastest method (2 taps)

### Use Bookmarklet Instead When:
- ✅ You're on a computer web browser
- ✅ You've done the one-time setup (30 sec)
- ✅ You want one-click loading
- ✅ You work on claude.ai web frequently

---

## TESTING THE TEMPLATE

### To verify Claude can fetch from GitHub:

1. Paste just the first part:
```
Hi! Can you fetch this file from GitHub for me?

URL: https://api.github.com/repos/MotherOfChaos/Life-Operating-System/contents/SARAH_LIFE_OS_CURRENT.json

Headers:
- Authorization: token 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
- Accept: application/vnd.github.v3.raw

Let me know if you can access it!
```

2. If Claude says "yes" or shows the content → **Template will work!** ✅
3. If Claude says "no" or "can't fetch" → **Use iOS Shortcut/Bookmarklet instead** ❌

---

## SECURITY CONSIDERATIONS

### PAT Visibility

**The Risk:**
Your Personal Access Token is stored in:
- Notes app (iOS)
- Keep app (Android)
- Clipboard when you copy
- Claude chat history after you paste

**Mitigation:**
1. The PAT only has read access to one private repo
2. You can revoke and regenerate anytime from GitHub settings
3. Your devices are (presumably) password protected
4. Claude conversations are private to your account

**Alternatives:**
- Create a dedicated PAT just for this purpose (revoke monthly)
- Use the manual upload version if you're concerned
- Use iOS Shortcut or Bookmarklet (PAT stored locally, not in chat)

### Best Practices

✅ **Do:**
- Keep your devices password protected
- Log out of Claude on shared devices
- Delete old chats that contain the PAT
- Regenerate PAT every 3-6 months

❌ **Don't:**
- Share this template with others
- Post screenshots that show the PAT
- Use the same PAT for other purposes
- Leave the template open on shared devices

---

## CUSTOMIZATION

### Adjust the Message

Want to customize the greeting or add specific instructions? Edit the template:

```
Hi M! 💚 [Your custom greeting here]

Quick update before we start: [Any urgent info]

Now please fetch my Life OS context from GitHub...
[Rest of template]
```

### Trigger Specific Workflows

Want to trigger the morning brief? Add to the end:

```
After authenticating, please run my morning brief:
- Check for today's pre-generated brief
- Triage my Gmail
- Present the full morning overview

Thanks! 🌅
```

### Shorten It

Minimal version (assuming Claude knows the routine):

```
Hi M! 💚

Pull latest from my Life OS repo:
- SARAH_LIFE_OS_CURRENT.json
- SARAH_DAILY_TRACKER_CURRENT.md
- TRANSFER_README_CURRENT.md

PAT: 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

Authenticate and continue. 🌹
```

---

## COMBINING WITH VOICE MODE

**Perfect workflow for bedtime or wake-up:**

1. Paste template → Send → **[5 seconds]**
2. Wait for M to authenticate → **[10 seconds]**
3. Tap microphone icon for voice mode → **[1 tap]**
4. Talk hands-free while getting ready / in bed → **[hands-free!]** 💚

**Example use cases:**
- Morning routine: Paste template, start voice mode, get morning brief while getting dressed
- Bedtime: Paste template, voice mode, talk through the day while lying in bed
- Commute: Paste template, voice mode (with headphones), chat while walking/driving

---

## TROUBLESHOOTING

### Claude says "I can't fetch from GitHub"

**Possible causes:**
- This Claude client doesn't have web fetch capabilities
- GitHub API is temporarily down
- PAT has expired or is incorrect

**Solutions:**
1. Try the manual upload version instead
2. Check if PAT is still valid (test in browser)
3. Use iOS Shortcut or Bookmarklet instead (they fetch locally, then paste)

### Claude fetches but shows garbled text

**Possible causes:**
- Wrong Accept header
- Files are binary/encrypted
- GitHub API returned error

**Solutions:**
1. Make sure Accept header is: `application/vnd.github.v3.raw`
2. Verify files exist at those paths in GitHub
3. Test URLs in browser to confirm they work

### Template paste is too long

**Possible causes:**
- Some chat apps have character limits
- Very large files might exceed limits

**Solutions:**
1. Use iOS Shortcut or Bookmarklet (they handle large files better)
2. Split into multiple messages
3. Ask Claude to fetch files one at a time

### PAT stopped working

**Possible causes:**
- PAT expired (GitHub tokens can have expiration dates)
- PAT was revoked
- GitHub permissions changed

**Solutions:**
1. Go to GitHub Settings → Developer Settings → Personal Access Tokens
2. Check if your token is still active
3. Regenerate if needed and update template
4. Make sure new PAT has `repo` scope for private repos

---

## UPDATING THE TEMPLATE

### When PAT Changes

1. Open your saved note (iOS Notes / Android Keep)
2. Find the line: `Personal Access Token: ghp_...`
3. Replace with new PAT
4. Save

**Takes 10 seconds, one-time per PAT change**

### When Files Change

If you rename or add files to your Life OS:

1. Update the "Files to fetch" section
2. Add new filenames to the list
3. Claude will fetch whatever you list

---

## COMPARISON: All Three Methods

| Feature | Smart Template | iOS Shortcut | Web Bookmarklet |
|---------|---------------|--------------|-----------------|
| **Setup time** | 0 sec (ready now) | 5-10 min | 30 sec |
| **Works on iOS** | ✅ Yes | ✅ Yes | ✅ Yes (Safari) |
| **Works on Android** | ✅ Yes | ❌ No | ✅ Yes (Chrome) |
| **Works on Web** | ✅ Yes | ❌ No | ✅ Yes |
| **Voice activation** | ❌ No | ✅ Yes (Siri) | ❌ No |
| **Time automation** | ❌ No | ✅ Yes | ❌ No |
| **Steps to use** | 2 (copy, paste) | 2 (tap, paste) | 1 (click) |
| **Requires web fetch** | ✅ Yes | ❌ No | ❌ No |
| **ADHD-friendly** | ⚠️ Medium | ✅ High | ✅ High |
| **PAT in chat history** | ⚠️ Yes | ❌ No | ❌ No |

---

## RECOMMENDED STRATEGY

**Phase 1: Start Here (Today)**
Use Smart Template on all devices to verify Claude can fetch from GitHub.
- Save to Notes/Keep
- Test it
- If it works, you have a universal solution! ✅

**Phase 2: Optimize iOS (This Week)**
If you primarily use iPhone, set up iOS Shortcut for better automation.
- One-time 10-minute setup
- Gain voice activation and time triggers
- Keep Smart Template as backup

**Phase 3: Optimize Web (This Week)**
If you use claude.ai in browser, add the bookmarklet.
- One-time 30-second setup
- One-click loading
- Keep Smart Template as backup

**End Result:**
- ✅ Smart Template: Universal backup that works everywhere
- ✅ iOS Shortcut: Optimized for phone (voice, automation)
- ✅ Bookmarklet: Optimized for web (one-click)

**You have the right tool for every situation!** 🎯

---

**Questions? Need help? Let Cody know!** 🔧

- Made with 💚 for Sarah & M
