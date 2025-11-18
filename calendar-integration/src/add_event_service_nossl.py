#!/usr/bin/env python3
"""
Add events to Google Calendar using Service Account (SSL verification disabled for testing)
"""

import os
import sys
from datetime import datetime, timedelta
import ssl
import httplib2

# Disable SSL verification (for testing only!)
httplib2.CA_CERTS = None

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError as e:
    print(f"ERROR: {e}")
    sys.exit(1)

SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.config/claude-calendar/service-account.json')
SCOPES = ['https://www.googleapis.com/auth/calendar']

CALENDAR_COLORS = {
    'lavender': '1', 'sage': '2', 'grape': '3', 'flamingo': '4',
    'banana': '5', 'tangerine': '6', 'peacock': '7', 'graphite': '8',
    'blueberry': '9', 'basil': '10', 'tomato': '11'
}

def get_calendar_service():
    """Get calendar service"""
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"❌ Service account file not found: {SERVICE_ACCOUNT_FILE}")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build with SSL verification disabled
    http = httplib2.Http(disable_ssl_certificate_validation=True)
    return build('calendar', 'v3', credentials=credentials, http=http)

def parse_date(date_str):
    """Parse date"""
    formats = ['%A, %B %d, %Y', '%B %d, %Y', '%Y-%m-%d', '%d/%m/%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    date_str_lower = date_str.lower()
    if date_str_lower == 'today':
        return datetime.now()
    elif date_str_lower == 'tomorrow':
        return datetime.now() + timedelta(days=1)

    raise ValueError(f"Could not parse date: {date_str}")

def parse_time(time_str):
    """Parse time"""
    time_str = time_str.lower().replace('.', ':')
    formats = ['%H:%M', '%I:%M%p', '%I%p', '%H']
    for fmt in formats:
        try:
            return datetime.strptime(time_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Could not parse time: {time_str}")

def add_event(title, date_str, start_time_str, end_time_str=None,
              color=None, notification_minutes=None, location=None):
    """Add event to calendar"""
    try:
        service = get_calendar_service()

        date_obj = parse_date(date_str)
        start_time = parse_time(start_time_str)

        start_datetime = date_obj.replace(
            hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0)

        if end_time_str:
            end_time = parse_time(end_time_str)
            end_datetime = date_obj.replace(
                hour=end_time.hour, minute=end_time.minute, second=0, microsecond=0)
        else:
            end_datetime = start_datetime + timedelta(hours=1)

        event = {
            'summary': title,
            'start': {'dateTime': start_datetime.isoformat(), 'timeZone': 'Europe/Madrid'},
            'end': {'dateTime': end_datetime.isoformat(), 'timeZone': 'Europe/Madrid'},
        }

        if location:
            event['location'] = location
        if color and color.lower() in CALENDAR_COLORS:
            event['colorId'] = CALENDAR_COLORS[color.lower()]
        if notification_minutes is not None:
            event['reminders'] = {
                'useDefault': False,
                'overrides': [{'method': 'email', 'minutes': notification_minutes}],
            }

        created_event = service.events().insert(calendarId='primary', body=event).execute()

        print("✅ EVENT CREATED SUCCESSFULLY!")
        print(f"\n📅 {created_event['summary']}")
        print(f"🕐 {start_datetime.strftime('%A, %B %d, %Y at %H:%M')}")
        print(f"   to {end_datetime.strftime('%H:%M')}")
        if location:
            print(f"📍 {location}")
        if color:
            print(f"🎨 Color: {color}")
        if notification_minutes:
            print(f"⏰ Email: {notification_minutes} min before")
        print(f"\n🔗 {created_event.get('htmlLink', 'N/A')}")

        return created_event

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Add event (no SSL verification)')
    parser.add_argument('title')
    parser.add_argument('date')
    parser.add_argument('start_time')
    parser.add_argument('end_time', nargs='?')
    parser.add_argument('--color', '-c', choices=list(CALENDAR_COLORS.keys()))
    parser.add_argument('--notification', '-n', type=int)
    parser.add_argument('--location', '-l')
    args = parser.parse_args()

    add_event(args.title, args.date, args.start_time, args.end_time,
              args.color, args.notification, args.location)
