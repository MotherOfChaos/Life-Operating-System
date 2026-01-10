# Local OAuth Setup - Step by Step

**What this does:** Authorizes your 3 email accounts ONE TIME on your computer, then you can use them in automations forever.

**Time needed:** 10-15 minutes

---

## Step 1: Get the Setup Files

1. Download these files from GitHub to your computer:
   - `automation/oauth_setup_local.py` 
   - The `credentials.json` you already downloaded

2. Put them both in the same folder (doesn't matter where)

---

## Step 2: Rename Credentials File

The file you downloaded is probably named something like:
`client_secret_147028699746-xxx.json`

**Rename it to:** `credentials.json`

---

## Step 3: Install Python Libraries

Open Command Prompt (Windows) or Terminal (Mac) and run:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Wait for it to finish installing.

---

## Step 4: Run the Setup Script

In the same Command Prompt/Terminal:

```bash
cd path/to/folder/with/files
python oauth_setup_local.py
```

(Replace `path/to/folder/with/files` with the actual folder path)

---

## Step 5: Authorize Each Account

The script will guide you through authorizing each account:

**For sarah@teatrometamorfosis.com:**
1. Browser opens automatically
2. **Log in as sarah@teatrometamorfosis.com**
3. Click "Allow"
4. Browser closes

**For info@teatrometamorfosis.com:**
1. Browser opens again
2. **Log in as info@teatrometamorfosis.com**
3. Click "Allow"
4. Browser closes

**For sarahpoer@gmail.com:**
1. Browser opens again
2. **Log in as sarahpoer@gmail.com**
3. Click "Allow"
4. Browser closes

---

## Step 6: Check Token Files Created

After all 3 authorizations, you should see these files in your folder:

- `token_sarah_teatrometamorfosis_com.json`
- `token_info_teatrometamorfosis_com.json`
- `token_sarahpoer_gmail_com.json`

---

## Step 7: Tell Cody You're Done!

Once you have all 3 token files, tell Cody and he'll help you add them to GitHub Secrets so the automation can use them.

---

## Troubleshooting

**"credentials.json not found"**
- Make sure it's in the same folder as the script
- Make sure it's named exactly `credentials.json` (not `credentials.json.txt`)

**"Module not found"**
- Run the pip install command from Step 3 again

**Browser doesn't open**
- The script will show a URL - copy and paste it into your browser manually

**Wrong email account opens**
- Log out of that account in the browser
- Click the authorization link again
- Choose the correct account

---

## Privacy Note

These token files give access to read your emails. They stay on YOUR computer until you add them to GitHub Secrets (which are encrypted). Don't share them publicly!

---

Ready to start? Go to Step 1! 💚
