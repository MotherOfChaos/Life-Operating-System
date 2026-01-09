# Email Setup - OAuth Method (All 3 Accounts)

**Your Workspace blocks service accounts, so we'll use OAuth instead.**

This is actually simpler! Just means you authorize each email once.

---

## Accounts to Set Up:
1. sarah@teatrometamorfosis.com (Workspace)
2. info@teatrometamorfosis.com (Workspace)
3. sarahpoer@gmail.com (Personal)

---

## Step 1: Enable Gmail API

### For Workspace emails:
1. Go to: https://console.cloud.google.com
2. **Log in as sarah@teatrometamorfosis.com**
3. Create/select project: "Life-OS-Email-Automation"
4. Go to: **APIs & Services** → **Library**
5. Search "Gmail API" → Click **Enable**

### For Personal Gmail:
Same API works for both! No separate step needed.

---

## Step 2: Configure OAuth Consent Screen

1. Still in Cloud Console: **APIs & Services** → **OAuth consent screen**
2. User Type: **Internal** (if available) OR **External**
3. Click **Create**

**Fill in:**
- App name: "Life OS Email Checker"
- User support email: sarah@teatrometamorfosis.com
- Developer contact: sarah@teatrometamorfosis.com

4. Click **Save and Continue**

**Scopes:** Click **Add or Remove Scopes**
- Find and add: `https://www.googleapis.com/auth/gmail.readonly`
- Click **Update** → **Save and Continue**

**Test users** (if External):
- Add: sarah@teatrometamorfosis.com
- Add: sarahpoer@gmail.com
- Click **Save and Continue**

5. Click **Back to Dashboard**

---

## Step 3: Create OAuth Credentials

1. **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Application type: **Desktop app**
4. Name: "Life-OS-Email-Desktop"
5. Click **Create**

---

## Step 4: Download Credentials

1. You'll see a popup with Client ID and Secret
2. Click **Download JSON** (⬇️ button)
3. Save the file (it's named like `client_secret_XXX.json`)

---

## Step 5: Add to GitHub Secrets

1. Open the downloaded JSON in a text editor
2. Copy the ENTIRE contents
3. Go to: https://github.com/MotherOfChaos/Life-Operating-System/settings/secrets/actions
4. Click **New repository secret**
5. Name: `GMAIL_OAUTH_CREDENTIALS`
6. Value: Paste the entire JSON
7. Click **Add secret**

---

## Step 6: Add Email Accounts List

1. Still in GitHub Secrets
2. Click **New repository secret**
3. Name: `EMAIL_ACCOUNTS_TO_CHECK`
4. Value:
   ```
   sarah@teatrometamorfosis.com,info@teatrometamorfosis.com,sarahpoer@gmail.com
   ```
5. Click **Add secret**

---

## Step 7: First-Time Authorization (One-Time Only!)

**This happens automatically the first time the automation runs.**

For each email account, you'll need to:
1. The automation will show an authorization URL in the logs
2. Open that URL in your browser
3. **Choose which account** (sarah@teatro, info@teatro, or sarahpoer)
4. Click "Allow"
5. Done for that account!

**After this one-time setup:** Everything works automatically, no more manual steps!

---

## How It Works

**Workspace emails (sarah@ and info@):**
- Uses same OAuth credentials
- You authorize each one once
- Credentials stored securely

**Personal Gmail (sarahpoer@):**
- Uses same OAuth credentials  
- Authorize once
- Works the same way

**All stored in GitHub** - encrypted and secure!

---

## Next Steps

After you complete Steps 1-6, tell me and I'll:
1. ✅ Update the email checker script to use OAuth
2. ✅ Update the workflow to handle all 3 accounts
3. ✅ Test trigger it so you can do the one-time authorization
4. ✅ Then it works automatically forever!

---

## Estimated Time

- Steps 1-6: **15 minutes**
- First authorization (Step 7): **5 minutes** (done automatically when you test)
- **Total: 20 minutes**

---

## Important Notes

✅ OAuth = Industry standard, very secure
✅ Read-only access (can't send/delete emails)
✅ Can revoke access anytime at: https://myaccount.google.com/permissions
✅ Works for Workspace + Personal Gmail
✅ No service account needed!

---

Ready to start? Follow Steps 1-6, then ping me! 💚
