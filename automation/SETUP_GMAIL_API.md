# Gmail API Setup for Email Automation

## What This Does

Automatically checks your 3 email accounts and categorizes emails so M can present them to you:
- sarahpoer@gmail.com
- sarah@teatrometamorfosis.com  
- info@teatrometamorfosis.com

Categories: 🔴 Urgent, 🟡 Needs Response, 📅 Calendar, 💰 Financial, 📰 Newsletters, ℹ️ FYI, 🗑️ Archive

## Step 1: Enable Gmail API

1. Go to: https://console.cloud.google.com/apis/library/gmail.googleapis.com
2. Make sure you're logged in as sarahpoer@gmail.com
3. Click "Enable"

## Step 2: Create OAuth Credentials

1. Go to: https://console.cloud.google.com/apis/credentials
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted to configure OAuth consent screen:
   - User Type: External
   - App name: "Life OS Email Checker"
   - User support email: sarahpoer@gmail.com
   - Developer contact: sarahpoer@gmail.com
   - Scopes: Add `gmail.readonly`
   - Test users: Add sarahpoer@gmail.com
4. Application type: **"Desktop app"** (important!)
5. Name: "Life-OS-Email-Checker"
6. Click "Create"

## Step 3: Download Credentials

1. Click the download button (⬇️) next to your new credential
2. This downloads a JSON file like `client_secret_XXX.json`
3. Open it in a text editor
4. Copy the ENTIRE contents

## Step 4: Add to GitHub Secrets

1. Go to: https://github.com/MotherOfChaos/Life-Operating-System/settings/secrets/actions
2. Click "New repository secret"
3. Name: `GMAIL_CREDENTIALS`
4. Value: [paste the entire JSON]
5. Click "Add secret"

## Step 5: First-Time Authorization

The first time the automation runs, it needs your permission:

1. The workflow will pause and show a URL in the logs
2. Open that URL in your browser
3. Log in as sarahpoer@gmail.com
4. Click "Allow" to grant access
5. The automation will then work automatically going forward!

**Note:** This one-time setup applies to sarahpoer@gmail.com. For the Teatro Metamorfosis emails, you'll need to set up forwarding or use IMAP (simpler approach - we can do this after if needed).

## How M Uses It

When you say to M: "check my emails"

1. M triggers the GitHub Action
2. Action fetches emails from your accounts
3. Claude categorizes them
4. Saves to `email-digest/YYYY-MM-DD-HH-MM.json`
5. M fetches and presents to you

**Works from phone, web, desktop - anywhere M exists!**

## Privacy & Security

- Credentials stored securely in GitHub Secrets (encrypted)
- Only read-only access (can't send/delete emails)
- Only runs when you explicitly ask M
- You can revoke access anytime at: https://myaccount.google.com/permissions

## Testing

After setup, test it:
1. In Projects, say to M: "check my emails"
2. M will trigger the workflow
3. Wait ~2 minutes
4. M will present categorized emails

## Troubleshooting

**"Invalid credentials"**: Re-download and re-add the JSON to secrets
**"Access denied"**: Make sure you added yourself as a test user in OAuth consent screen
**"Redirect URI mismatch"**: Make sure you selected "Desktop app" not "Web application"
