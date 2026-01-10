#!/usr/bin/env python3
"""
Email Checker Diagnostic - Tests OAuth token loading and Gmail API access
"""
import os
import json
from datetime import datetime
import pytz

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

def test_token_loading():
    """Test if tokens can be loaded from environment variables"""
    print("\n" + "="*60)
    print("DIAGNOSTIC TEST - TOKEN LOADING")
    print("="*60)

    token_vars = {
        'GMAIL_TOKEN_SARAH_TEATRO': 'sarah@teatrometamorfosis.com',
        'GMAIL_TOKEN_INFO_TEATRO': 'info@teatrometamorfosis.com',
        'GMAIL_TOKEN_SARAH_PERSONAL': 'sarahpoer@gmail.com'
    }

    results = {}

    for token_var, email in token_vars.items():
        print(f"\n--- Testing {email} ---")

        token_json = os.environ.get(token_var)
        if not token_json:
            print(f"✗ {token_var} NOT FOUND in environment")
            results[email] = "NOT_FOUND"
            continue

        print(f"✓ {token_var} found ({len(token_json)} chars)")

        try:
            token_data = json.loads(token_json)
            print(f"✓ JSON parses successfully")
            print(f"  - Has refresh_token: {'refresh_token' in token_data}")
            print(f"  - Has token: {'token' in token_data}")
            print(f"  - Scopes: {token_data.get('scopes', [])}")

            if 'expiry' in token_data:
                print(f"  - Expiry: {token_data['expiry']}")

            creds = Credentials.from_authorized_user_info(token_data)
            print(f"✓ Credentials object created")

            # Check if expired
            if creds.expired:
                print(f"⚠ Token is EXPIRED")
                if creds.refresh_token:
                    print(f"  Attempting to refresh...")
                    try:
                        creds.refresh(Request())
                        print(f"✓ Token refreshed successfully!")
                        results[email] = "REFRESHED"
                    except Exception as e:
                        print(f"✗ Refresh failed: {e}")
                        results[email] = "REFRESH_FAILED"
                else:
                    print(f"✗ No refresh token available")
                    results[email] = "NO_REFRESH_TOKEN"
            else:
                print(f"✓ Token is still valid")
                results[email] = "VALID"

            # Try to access Gmail API
            print(f"  Testing Gmail API access...")
            try:
                service = build('gmail', 'v1', credentials=creds)
                profile = service.users().getProfile(userId='me').execute()
                print(f"✓ Gmail API access successful!")
                print(f"  - Email: {profile.get('emailAddress')}")
                print(f"  - Total messages: {profile.get('messagesTotal')}")
                print(f"  - Total threads: {profile.get('threadsTotal')}")

                # Try to list messages
                messages_result = service.users().messages().list(userId='me', maxResults=5).execute()
                message_count = len(messages_result.get('messages', []))
                print(f"✓ Can list messages: found {message_count} recent messages")
                results[email] = "SUCCESS"

            except Exception as e:
                print(f"✗ Gmail API error: {e}")
                results[email] = "API_ERROR"

        except json.JSONDecodeError as e:
            print(f"✗ JSON parse error: {e}")
            results[email] = "JSON_ERROR"
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            results[email] = "ERROR"

    print("\n" + "="*60)
    print("DIAGNOSTIC SUMMARY")
    print("="*60)
    for email, status in results.items():
        print(f"{email}: {status}")
    print("="*60)

    return results

if __name__ == "__main__":
    if not GOOGLE_AVAILABLE:
        print("ERROR: Google API libraries not available!")
        print("Run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    else:
        test_token_loading()
