# 🎯 SIMPLE ALTERNATIVE: Service Account Method

Sarah, instead of the OAuth nightmare, we can use a **Service Account**!

## What's the difference?

**OAuth (what we tried):** Needs browser, clicking allow, test users, publishing... UGH!

**Service Account:** Download 1 JSON file, done! ✅

## Quick Steps:

1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts?project=precise-braid-478615-e0

2. Click: **"+ CREATE SERVICE ACCOUNT"** / **"+ CREAR CUENTA DE SERVICIO"**

3. Fill in:
   - Name: **calendar-service**
   - Click **CREATE**
   - Skip the optional parts, click **DONE**

4. Click on the service account you just created

5. Go to **KEYS** tab / **CLAVES**

6. Click **ADD KEY** → **Create new key** → **JSON**

7. Download the JSON file

8. Paste the contents here

9. Then share your calendar with the service account email

## This should take 2 minutes and JUST WORK!

Want to try this instead?
