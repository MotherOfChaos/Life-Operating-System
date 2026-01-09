# Google Workspace Email Setup - All 3 Accounts

**Accounts to enable:**
- sarah@teatrometamorfosis.com (you already have this working!)
- info@teatrometamorfosis.com
- sarahpoer@gmail.com (personal Gmail)

---

## Step 1: Enable Gmail API in Google Workspace

1. Go to **Google Workspace Admin Console**: https://admin.google.com
2. Log in with your Workspace admin account (sarah@teatrometamorfosis.com)
3. Navigate to: **Apps** → **Google Workspace** → **Gmail**
4. Make sure Gmail is **enabled** for your organization
5. Go to: **Security** → **API Controls** → **Manage Domain-wide Delegation** (we'll use this later)

---

## Step 2: Enable Gmail API in Google Cloud Console

1. Go to: https://console.cloud.google.com
2. **Make sure you're logged in as sarah@teatrometamorfosis.com** (check top-right corner)
3. Select or create a project (e.g., "Life-OS-Automations")
4. Go to: **APIs & Services** → **Library**
5. Search for "Gmail API"
6. Click **Enable**

---

## Step 3: Create Service Account (Recommended for Multiple Accounts)

Since you need to access multiple accounts, a **service account** is better than OAuth:

1. In Google Cloud Console: **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **Service Account**
3. Name: "life-os-email-checker"
4. Description: "Automated email checking for Life OS"
5. Click **Create and Continue**
6. Grant role: **Service Account User**
7. Click **Done**

---

## Step 4: Download Service Account Key

1. Click on the service account you just created
2. Go to **Keys** tab
3. Click **Add Key** → **Create new key**
4. Choose **JSON** format
5. Click **Create**
6. A JSON file downloads - **SAVE THIS SECURELY**

---

## Step 5: Enable Domain-Wide Delegation

This allows the service account to impersonate users and read their emails:

1. Copy the **Client ID** from your service account (long number)
2. Go back to **Google Workspace Admin Console**: https://admin.google.com
3. Navigate to: **Security** → **Access and data control** → **API Controls**
4. Click **Manage Domain Wide Delegation**
5. Click **Add new**
6. Paste the **Client ID**
7. Add these **OAuth Scopes**:
   ```
   https://www.googleapis.com/auth/gmail.readonly
   ```
8. Click **Authorize**

---

## Step 6: Add Service Account JSON to GitHub Secrets

1. Open the JSON file you downloaded in Step 4
2. Copy the ENTIRE contents
3. Go to: https://github.com/MotherOfChaos/Life-Operating-System/settings/secrets/actions
4. Click **New repository secret**
5. Name: `GMAIL_SERVICE_ACCOUNT`
6. Value: Paste the entire JSON
7. Click **Add secret**

---

## Step 7: Add Email Accounts List to Secrets

1. Go to: https://github.com/MotherOfChaos/Life-Operating-System/settings/secrets/actions
2. Click **New repository secret**
3. Name: `EMAIL_ACCOUNTS`
4. Value: 
   ```
   sarah@teatrometamorfosis.com,info@teatrometamorfosis.com,sarahpoer@gmail.com
   ```
5. Click **Add secret**

**Note:** For sarahpoer@gmail.com (personal Gmail, not Workspace), you might need separate OAuth setup. Let's test the Workspace emails first.

---

## Step 8: Update Email Checker Script

The script needs to be updated to use service account authentication. I'll do this for you - just confirm you've completed steps 1-7.

---

## Step 9: Test It

Once everything is set up:

1. Say to M: "check my emails"
2. M triggers the GitHub Action
3. Action uses service account to access all 3 Workspace emails
4. Results saved and presented to you

**First run might take 2-3 minutes**

---

## Troubleshooting

**"Delegation not enabled"**
- Make sure you completed Step 5 with the correct Client ID
- Wait 5-10 minutes for changes to propagate

**"Access denied"**
- Check the OAuth scope is exactly: `https://www.googleapis.com/auth/gmail.readonly`
- Make sure Gmail API is enabled in Cloud Console

**"Invalid service account"**
- Re-download the JSON and re-add to GitHub secrets
- Make sure you copied the ENTIRE JSON file contents

**Personal Gmail not working**
- sarahpoer@gmail.com needs separate OAuth (not service account)
- We can add this after Workspace emails work

---

## Important Notes

✅ **Service account** = automated access, no manual login needed
✅ **Domain-wide delegation** = can access all Workspace users' emails
✅ **Read-only** = cannot send or delete emails
✅ **Secure** = JSON key stored encrypted in GitHub

⚠️ **For sarahpoer@gmail.com**: If it doesn't work with this setup, we'll add separate OAuth credentials (takes 5 more minutes)

---

## Next Step

After you complete Steps 1-7, tell me and I'll:
1. Update the email checker script to use service account
2. Update the workflow
3. Test it for you

**Estimated time:** 15-20 minutes for all steps

Ready to start? 💚
