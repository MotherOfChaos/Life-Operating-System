"""
Gmail Integration Module
Handles Gmail API authentication and email retrieval/categorization
"""

import os
import base64
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from email.utils import parsedate_to_datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    GMAIL_AVAILABLE = True
except ImportError:
    GMAIL_AVAILABLE = False

import config


# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailIntegration:
    def __init__(self):
        self.service = None
        self.available = GMAIL_AVAILABLE

        if not GMAIL_AVAILABLE:
            print("⚠️  Gmail libraries not installed. Run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")

    def authenticate(self) -> bool:
        """
        Authenticate with Gmail API using OAuth2
        Returns True if successful
        """
        if not self.available:
            return False

        try:
            creds = None
            token_path = 'automation/token.json'
            credentials_path = 'automation/credentials.json'

            # Check if we have valid credentials
            if os.path.exists(token_path):
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)

            # If no valid credentials, let user log in
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    if not os.path.exists(credentials_path):
                        print("⚠️  credentials.json not found!")
                        print("📝  Please download it from Google Cloud Console")
                        print("    Go to: https://console.cloud.google.com/apis/credentials")
                        return False

                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save credentials for next run
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())

            # Build the service
            self.service = build('gmail', 'v1', credentials=creds)
            return True

        except Exception as e:
            print(f"⚠️  Gmail authentication failed: {str(e)}")
            return False

    def get_recent_emails(self, hours: int = 24) -> List[Dict]:
        """
        Get emails from the last N hours
        Returns list of email dictionaries
        """
        if not self.service:
            return []

        try:
            # Calculate timestamp for query
            after_date = datetime.now() - timedelta(hours=hours)
            query = f'after:{int(after_date.timestamp())}'

            # Get message list
            results = self.service.users().messages().list(
                userId='me',
                q=query,
                maxResults=100
            ).execute()

            messages = results.get('messages', [])
            emails = []

            for msg in messages:
                # Get full message details
                message = self.service.users().messages().get(
                    userId='me',
                    id=msg['id'],
                    format='full'
                ).execute()

                email_data = self._parse_message(message)
                if email_data:
                    emails.append(email_data)

            return emails

        except Exception as e:
            print(f"⚠️  Error fetching emails: {str(e)}")
            return []

    def _parse_message(self, message: Dict) -> Optional[Dict]:
        """Parse Gmail API message into simplified format"""
        try:
            headers = message['payload']['headers']
            subject = self._get_header(headers, 'Subject')
            sender = self._get_header(headers, 'From')
            date_str = self._get_header(headers, 'Date')

            # Parse date
            try:
                date = parsedate_to_datetime(date_str)
            except:
                date = datetime.now()

            # Get snippet
            snippet = message.get('snippet', '')[:200]

            return {
                'id': message['id'],
                'subject': subject,
                'from': sender,
                'date': date,
                'snippet': snippet,
                'labels': message.get('labelIds', [])
            }

        except Exception as e:
            print(f"⚠️  Error parsing message: {str(e)}")
            return None

    def _get_header(self, headers: List[Dict], name: str) -> str:
        """Extract header value by name"""
        for header in headers:
            if header['name'].lower() == name.lower():
                return header['value']
        return ''

    def categorize_emails(self, emails: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Categorize emails into the 7 categories Sarah specified
        Returns dictionary with category names as keys
        """
        categories = {
            '🔴 Urgent Action Required': [],
            '🟡 Needs Response': [],
            '🔵 FYI/Read Later': [],
            '📅 Calendar/Events': [],
            '💰 Financial/Invoices': [],
            '📧 Newsletters/Promotions': [],
            '✅ Can Archive': []
        }

        for email in emails:
            category = self._determine_category(email)
            categories[category].append(email)

        return categories

    def _determine_category(self, email: Dict) -> str:
        """
        Determine which category an email belongs to
        Uses simple keyword matching - can be enhanced with ML
        """
        subject_lower = email['subject'].lower()
        sender_lower = email['from'].lower()
        snippet_lower = email['snippet'].lower()

        # Check for urgent keywords
        urgent_keywords = [
            'urgent', 'asap', 'immediate', 'emergency',
            'action required', 'respond today', 'deadline today'
        ]
        if any(kw in subject_lower or kw in snippet_lower for kw in urgent_keywords):
            return '🔴 Urgent Action Required'

        # Check for calendar/events
        calendar_keywords = [
            'invitation', 'event', 'meeting', 'calendar',
            'invite', 'rsvp', 'schedule', 'appointment'
        ]
        if any(kw in subject_lower or kw in snippet_lower for kw in calendar_keywords):
            return '📅 Calendar/Events'

        # Check for financial
        financial_keywords = [
            'invoice', 'payment', 'bill', 'receipt',
            'transaction', 'bank', 'card', 'paypal', 'stripe'
        ]
        if any(kw in subject_lower or kw in snippet_lower for kw in financial_keywords):
            return '💰 Financial/Invoices'

        # Check for newsletters/promotions
        newsletter_keywords = [
            'unsubscribe', 'newsletter', 'promotion', 'sale',
            'offer', 'discount', 'marketing', 'deals'
        ]
        if any(kw in subject_lower or kw in snippet_lower for kw in newsletter_keywords):
            return '📧 Newsletters/Promotions'

        # Check for automated/no-reply (can archive)
        if 'no-reply' in sender_lower or 'noreply' in sender_lower:
            # But not if it's financial or urgent
            if '💰' not in self._determine_category(email):
                return '✅ Can Archive'

        # Check if it needs a response (questions, requests)
        response_keywords = [
            '?', 'please', 'could you', 'can you',
            'let me know', 'get back', 'thoughts on'
        ]
        if any(kw in subject_lower or kw in snippet_lower for kw in response_keywords):
            return '🟡 Needs Response'

        # Default: FYI/Read Later
        return '🔵 FYI/Read Later'

    def test_connection(self) -> bool:
        """Test if Gmail connection works"""
        try:
            if not self.service:
                return False
            # Try to get profile
            self.service.users().getProfile(userId='me').execute()
            return True
        except:
            return False
