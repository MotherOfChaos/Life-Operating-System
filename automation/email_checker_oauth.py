#!/usr/bin/env python3
"""
Email Checker with OAuth - All 3 Accounts
"""
import os
import json
import requests
from datetime import datetime
import pytz

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

class EmailCheckerOAuth:
    def __init__(self, anthropic_key=None):
        self.anthropic_key = anthropic_key or os.environ.get('ANTHROPIC_API_KEY')
        self.accounts = {
            'sarah@teatrometamorfosis.com': 'GMAIL_TOKEN_SARAH_TEATRO',
            'info@teatrometamorfosis.com': 'GMAIL_TOKEN_INFO_TEATRO',
            'sarahpoer@gmail.com': 'GMAIL_TOKEN_SARAH_PERSONAL'
        }

    def get_credentials(self, token_env_var):
        """Load credentials from GitHub secret"""
        token_json = os.environ.get(token_env_var)
        if not token_json:
            print(f"  WARNING: {token_env_var} not found in environment")
            return None

        try:
            token_data = json.loads(token_json)
            creds = Credentials.from_authorized_user_info(token_data)
            if creds.expired and creds.refresh_token:
                print(f"  Refreshing expired token for {token_env_var}")
                creds.refresh(Request())
            return creds
        except Exception as e:
            print(f"  ERROR loading {token_env_var}: {e}")
            import traceback
            traceback.print_exc()
            return None

    def fetch_emails_from_account(self, email_address, token_env_var):
        """Fetch emails from one account"""
        print(f"\nChecking {email_address}...")

        if not GOOGLE_AVAILABLE:
            print("  ERROR: Google API libraries not available")
            return []

        creds = self.get_credentials(token_env_var)
        if not creds:
            print(f"  ERROR: Could not load credentials for {email_address}")
            return []

        try:
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me', maxResults=20).execute()
            messages = results.get('messages', [])

            emails = []
            for msg in messages:
                message = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                headers = message['payload']['headers']

                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')

                emails.append({
                    'account': email_address,
                    'subject': subject,
                    'from': sender,
                    'snippet': message.get('snippet', '')[:200]
                })

            print(f"  ✓ Found {len(emails)} emails")
            return emails

        except Exception as e:
            print(f"  ERROR fetching emails: {e}")
            import traceback
            traceback.print_exc()
            return []

    def check_all_accounts(self):
        """Check all accounts and save results"""
        print("\n" + "="*60)
        print("EMAIL CHECKER - STARTING")
        print("="*60)

        all_emails = []

        for email, token_var in self.accounts.items():
            emails = self.fetch_emails_from_account(email, token_var)
            all_emails.extend(emails)

        madrid_tz = pytz.timezone('Europe/Madrid')
        timestamp = datetime.now(madrid_tz).strftime("%Y-%m-%d-%H-%M")

        result = {
            'timestamp': timestamp,
            'total_emails': len(all_emails),
            'accounts': list(self.accounts.keys()),
            'emails': all_emails
        }

        print("\n" + "="*60)
        print(f"Saving results: {len(all_emails)} total emails")
        print("="*60)

        os.makedirs('email-digest', exist_ok=True)
        output_file = f'email-digest/email-digest-{timestamp}.json'

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"\n✓ SUCCESS: Saved {output_file}")
        print(f"✓ Total emails collected: {len(all_emails)}")
        print("="*60)

def main():
    print("\n" + "="*60)
    print("EMAIL CHECKER - ENVIRONMENT CHECK")
    print("="*60)

    # Check if environment variables are set
    token_vars = ['GMAIL_TOKEN_SARAH_TEATRO', 'GMAIL_TOKEN_INFO_TEATRO', 'GMAIL_TOKEN_SARAH_PERSONAL']
    for var in token_vars:
        if os.environ.get(var):
            print(f"✓ {var} is set ({len(os.environ.get(var))} chars)")
        else:
            print(f"✗ {var} is NOT set")

    anthropic_key = os.environ.get('ANTHROPIC_API_KEY')
    if anthropic_key:
        print(f"✓ ANTHROPIC_API_KEY is set")
    else:
        print(f"✗ ANTHROPIC_API_KEY is NOT set")

    print("="*60 + "\n")

    checker = EmailCheckerOAuth()
    checker.check_all_accounts()

if __name__ == "__main__":
    main()
