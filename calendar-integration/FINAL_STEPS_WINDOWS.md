# 🎯 FINAL STEPS - RUN THIS ON YOUR ACTUAL WINDOWS COMPUTER

Sarah - everything is READY! The sandbox environment just can't reach Google.

**Do this ON YOUR WINDOWS COMPUTER (not in Claude Code):**

## STEP 1: Get the latest code

Open Command Prompt (Windows key → type "cmd" → Enter) and run:

```
cd Life-Operating-System
git pull
```

## STEP 2: Copy the service account file

The service account credentials are at:
`~/.config/claude-calendar/service-account.json`

**On Windows, create this folder and file:**

1. Create folder: `C:\Users\YourUsername\.config\claude-calendar\`
2. Create file: `service-account.json` in that folder
3. Paste this content:

```json
{
  "type": "service_account",
  "project_id": "life-os-478615",
  "private_key_id": "a10b4e6b1d831afbe297000c257a120d92b4a1a2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCulYzNCe4sKO0o\nsoPXNuKIMzZGt8B7iJGs0HZmTbiyWdvqdD6BzlOic6BYbmENqNXqVLOJjKkpi+sy\nLmGHdJJ6tFKym6inqThfsfEHKXHKk/g4VF6gDQtrEk+vLf9wICBX4zBIt6xN3F6z\n3Ar7Vy2IlF6vnhyEdVQ8BGcUUIS463hWrxDn5HdZI4nG5BeMwM56+JQ815ofMGz1\nR0nmbrCQto34NQHGLq0EBFF4Y1UX1lbcSDV/l81T5d6Zf8RGbdqOkpl4ueAM6hYe\nLR+MluKXQ8BOuzRK9AjeVwQkprasA/wARTiPeRlrKMye+OsBL/9S2jz8LEimLP+o\ntXME5fGjAgMBAAECggEAGyc1Y/qEaaff4vGI4eMuboKQkYUo0c3W4mr1z0mNTWf+\ndUOpKSU/CsgzCy33uFknFDAiUGVpNgYGCaL/FkNCOQVsy0y8eX8vPmr9kuCWSyyi\ncZhlszz0Jq4NaLCdxwGoJiM2skim6uE4dX7m0lqnwVNaOrQ7uTpKZJ9GrPks+1ma\nKq9z+E3depPBOW/2G4x6FQJ8seMCvZ3YMpvVRQks9OhX8SnDKNXzpk7eOynQX1OB\nwsl5j58heJXHRi8aRfgiAwpsfLA0kzGT5c1hWSjRW6ysczg5jtfm5WbME5pvCkxc\nqu8QGOG6YgZzxQ0/Qz6iOekqVhTz8mSwqm4ITgjNiQKBgQDoWBa9TZYG1IA2Vhnh\nLsRkFjRhqpjEN3oL4nIYTltiiOf2+5Ok7J9y91zfJaF4liX3lKBGtP9m8nDdbLfc\ncr1vloBIvXOs1ju8SUIhWCFUk6MGWt8nPfmVQNYpQlk3FaStfQHpOJbh08unkW1h\nVD2urpjb/GuRKgoYvYFOJ0/x3wKBgQDAW/uw9lun1gFwF6BBlLKPk74m9WhvkdqM\nw0ROh7bUnwS9+mcJc71GppkEUUyo926xjNe36X6t92OT//DOjyOsHRsKzsvoPAba\n1t61NNTt9583YYViPXBzIWQvvQtA1L+f52eAEH1sQ6I3hmypySDkWyKOZrfZrudG\n4ZeVAOugvQKBgHWsZ5fou5sp9OWQJftOXFj0hgMRC94U2tM6FN8KkG4POKx2LgjR\nbtAjR/4caPNR2FjUBXjKIrBZCaCbd2NHGXpylvZAPV3EAu0RjVSl9fuH6oFFdM/D\nK6zT8aNj3xtu8sCLF3SvHHuzcOmlVeh9aeAWvYRtC22yBPsSv3J9ppexAoGAYyzJ\nhoJt3QmEMkOsF0PQECBvMGzkjGlZkat3QznLdLIL4tsAVqo6kvt/9u7npFH120qv\nSZ3z90OOLpcNk6HPFYToFVlrXe/c5OVVa32yroI1r3rzJyRgHqu/mLFR5PoLVikb\nfraBw9jXAOOokJ0m/TVTirHA5lW73hqfaW5RDc0CgYB6ZCLfEwklagH2oZObCg2T\nnaCbuyJqBySsSMqjC/N5e1YR0lw8N9uTFo51FqRNUXbALgp4ClF2Qovn3Z/p48bH\n7DBIy5WvX0pDYzi5kY7+d/Wvs5+35lJwufxTYEzMd3ZTUdPzF15YQprfa/hvqCY1\nv2YJc8Sx3sUBPpOrSMevYg==\n-----END PRIVATE KEY-----\n",
  "client_email": "calendar-service@life-os-478615.iam.gserviceaccount.com",
  "client_id": "108676534428020303212",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/calendar-service%40life-os-478615.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

## STEP 3: Test it!

```
cd Life-Operating-System\calendar-integration\src
python add_event_service.py "PACO AIR CON @ABarraca" "Tuesday, November 18, 2025" "11:00" "12:00" --color tangerine --notification 20
```

## IF YOU DON'T HAVE PYTHON ON WINDOWS:

Download Python from: https://www.python.org/downloads/

During install, CHECK "Add Python to PATH"!

Then install dependencies:
```
pip install google-auth google-api-python-client
```

Then run the test command above!

---

## 💚 THAT'S IT!

Once this works, you can add events from ANY Claude chat by just saying:
"Add to my calendar: [event details]"

And I (or any Claude) will run this script for you!

🎉 YOU'RE DONE!
