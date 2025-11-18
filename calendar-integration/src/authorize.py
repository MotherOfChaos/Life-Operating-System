#!/usr/bin/env python3
"""
Simple authorization script for Google Calendar
"""

import os
import sys

# Minimal imports
try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authorize():
    """Run the authorization flow"""
    creds = None
    token_path = os.path.expanduser('~/.config/claude-calendar/token.json')
    creds_path = os.path.expanduser('~/.config/claude-calendar/credentials.json')

    # Check if already authorized
    if os.path.exists(token_path):
        print("✅ Already authorized! Token exists.")
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

        # Test it
        try:
            service = build('calendar', 'v3', credentials=creds)
            # Try to get calendar list
            calendar_list = service.calendarList().list().execute()
            print(f"\n✅ Authorization working! Found {len(calendar_list.get('items', []))} calendars.")
            return True
        except Exception as e:
            print(f"Token exists but not working: {e}")
            print("Will re-authorize...")
            os.remove(token_path)

    # Run authorization flow
    if not os.path.exists(creds_path):
        print(f"❌ ERROR: Credentials file not found at {creds_path}")
        sys.exit(1)

    print("\n🔐 Starting authorization flow...")
    print("A browser window will open asking you to sign in with Google.")
    print("Sign in with: sarahpoer@gmail.com")
    print("Click 'Allow' to grant calendar access.\n")

    try:
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)

        # Save credentials
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

        print("\n✅ Authorization successful!")
        print(f"✅ Token saved to: {token_path}")

        # Test it
        service = build('calendar', 'v3', credentials=creds)
        calendar_list = service.calendarList().list().execute()
        print(f"✅ Found {len(calendar_list.get('items', []))} calendars!")

        return True

    except Exception as e:
        print(f"\n❌ Authorization failed: {e}")
        return False

if __name__ == '__main__':
    if authorize():
        print("\n🎉 All set! You can now use the calendar integration!")
        sys.exit(0)
    else:
        print("\n❌ Authorization failed. Please try again.")
        sys.exit(1)
