#!/usr/bin/env python3
"""
Manual authorization for Google Calendar (no browser needed)
"""

import os
import sys
import json

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError as e:
    print(f"ERROR: {e}")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/calendar']

def manual_authorize():
    """Manual authorization flow"""
    token_path = os.path.expanduser('~/.config/claude-calendar/token.json')
    creds_path = os.path.expanduser('~/.config/claude-calendar/credentials.json')

    # Check if already authorized
    if os.path.exists(token_path):
        print("✅ Already authorized!")
        return True

    if not os.path.exists(creds_path):
        print(f"❌ Credentials file not found: {creds_path}")
        sys.exit(1)

    # Create flow
    flow = InstalledAppFlow.from_client_secrets_file(
        creds_path,
        SCOPES,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )

    # Get authorization URL
    auth_url, _ = flow.authorization_url(prompt='consent')

    print("\n" + "="*70)
    print("🔐 GOOGLE CALENDAR AUTHORIZATION")
    print("="*70)
    print("\n1. Copy this URL:")
    print(f"\n{auth_url}\n")
    print("2. Open it in your browser")
    print("3. Sign in with: sarahpoer@gmail.com")
    print("4. Click 'Allow'")
    print("5. Copy the authorization code")
    print("6. Paste it below\n")
    print("="*70 + "\n")

    # Get code from user
    code = input("Enter authorization code: ").strip()

    try:
        # Exchange code for credentials
        flow.fetch_token(code=code)
        creds = flow.credentials

        # Save token
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

        print("\n✅ Authorization successful!")
        print(f"✅ Token saved: {token_path}")

        # Test it
        service = build('calendar', 'v3', credentials=creds)
        calendar_list = service.calendarList().list().execute()
        calendars = calendar_list.get('items', [])

        print(f"\n✅ Found {len(calendars)} calendars:")
        for cal in calendars[:5]:  # Show first 5
            print(f"   📅 {cal.get('summary', 'Unnamed')}")

        print("\n🎉 All set! Calendar integration ready!")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == '__main__':
    if manual_authorize():
        sys.exit(0)
    else:
        sys.exit(1)
