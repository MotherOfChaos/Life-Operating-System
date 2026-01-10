#!/usr/bin/env python3
"""
Local OAuth Setup - Run this ONCE on your computer
This will authorize each email account and create token files
"""

import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def setup_account(email_address, credentials_file):
    """Set up OAuth for one account"""
    print(f"\n{'='*60}")
    print(f"Setting up: {email_address}")
    print(f"{'='*60}")
    
    token_file = f'token_{email_address.replace("@", "_").replace(".", "_")}.json'
    
    # Check if already authorized
    if os.path.exists(token_file):
        print(f"Already authorized! Token file exists: {token_file}")
        response = input("Re-authorize? (y/n): ")
        if response.lower() != 'y':
            return True
    
    try:
        # Start OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_file, SCOPES)
        
        print(f"\nA browser window will open...")
        print(f"1. Log in as: {email_address}")
        print(f"2. Click 'Allow' to grant access")
        print(f"3. The window will close automatically\n")
        
        input("Press Enter when ready...")
        
        creds = flow.run_local_server(port=0)
        
        # Save token
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
        
        print(f"\nSUCCESS! Token saved: {token_file}")
        return True
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        return False

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║      Gmail OAuth Setup - One-Time Authorization           ║
╚═══════════════════════════════════════════════════════════╝

This will authorize 3 email accounts:
  1. sarah@teatrometamorfosis.com
  2. info@teatrometamorfosis.com  
  3. sarahpoer@gmail.com

You'll need:
  ✓ The credentials.json file you downloaded
  ✓ Access to each email account
  ✓ A web browser
""")
    
    # Find credentials file
    credentials_file = 'credentials.json'
    if not os.path.exists(credentials_file):
        print("ERROR: credentials.json not found!")
        print("\nPlease:")
        print("1. Place the downloaded JSON file in this folder")
        print("2. Rename it to: credentials.json")
        print("3. Run this script again")
        return
    
    accounts = [
        'sarah@teatrometamorfosis.com',
        'info@teatrometamorfosis.com',
        'sarahpoer@gmail.com'
    ]
    
    success_count = 0
    
    for email in accounts:
        if setup_account(email, credentials_file):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"SETUP COMPLETE: {success_count}/{len(accounts)} accounts authorized")
    print(f"{'='*60}\n")
    
    if success_count == len(accounts):
        print("ALL DONE! Token files created:")
        for email in accounts:
            token_file = f'token_{email.replace("@", "_").replace(".", "_")}.json'
            if os.path.exists(token_file):
                print(f"  ✓ {token_file}")
        
        print("\nNEXT STEPS:")
        print("1. These token files need to be added to GitHub Secrets")
        print("2. Tell Cody you're done and he'll help with that")
    else:
        print("SOME ACCOUNTS FAILED - try running this script again")

if __name__ == "__main__":
    main()
