#!/usr/bin/env python3
"""Generate a fresh OAuth authorization URL"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds_path = os.path.expanduser('~/.config/claude-calendar/credentials.json')

flow = InstalledAppFlow.from_client_secrets_file(
    creds_path,
    SCOPES,
    redirect_uri='urn:ietf:wg:oauth:2.0:oob'
)

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print("\n" + "="*70)
print("🔐 FRESH AUTHORIZATION URL")
print("="*70)
print(f"\n{auth_url}\n")
print("="*70)
