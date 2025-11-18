#!/usr/bin/env python3
"""
Add events to Google Calendar using Service Account
MUCH SIMPLER than OAuth!
"""

import os
import sys
from datetime import datetime, timedelta

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError as e:
    print(f"ERROR: {e}")
    print("Run: pip3 install google-auth google-api-python-client")
    sys.exit(1)

# Service account file
SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.config/claude-calendar/service-account.json')

# Scopes
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Color mapping
CALENDAR_COLORS = {
    'lavender': '1', 'sage': '2', 'grape': '3', 'flamingo': '4',
    'banana': '5', 'tangerine': '6', 'peacock': '7', 'graphite': '8',
    'blueberry': '9', 'basil': '10', 'tomato': '11'
}

def get_calendar_service():
    """Get calendar service using service account"""
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"❌ Service account file not found: {SERVICE_ACCOUNT_FILE}")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    return build('calendar', 'v3', credentials=credentials)

def parse_date(date_str):
    """Parse various date formats"""
    formats = [
        '%A, %B %d, %Y',  # Tuesday, November 18, 2025
        '%B %d, %Y',      # November 18, 2025
        '%Y-%m-%d',       # 2025-11-18
        '%d/%m/%Y',       # 18/11/2025
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    # Try special cases
    date_str_lower = date_str.lower()
    if date_str_lower == 'today':
        return datetime.now()
    elif date_str_lower == 'tomorrow':
        return datetime.now() + timedelta(days=1)

    raise ValueError(f"Could not parse date: {date_str}")

def parse_time(time_str):
    """Parse various time formats"""
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
    """Add an event to Google Calendar"""

    try:
        service = get_calendar_service()

        # Parse date and times
        date_obj = parse_date(date_str)
        start_time = parse_time(start_time_str)

        # Combine date and time
        start_datetime = date_obj.replace(
            hour=start_time.hour,
            minute=start_time.minute,
            second=0,
            microsecond=0
        )

        # Handle end time
        if end_time_str:
            end_time = parse_time(end_time_str)
            end_datetime = date_obj.replace(
                hour=end_time.hour,
                minute=end_time.minute,
                second=0,
                microsecond=0
            )
        else:
            end_datetime = start_datetime + timedelta(hours=1)

        # Build event
        event = {
            'summary': title,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': 'Europe/Madrid',
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': 'Europe/Madrid',
            },
        }

        if location:
            event['location'] = location

        if color and color.lower() in CALENDAR_COLORS:
            event['colorId'] = CALENDAR_COLORS[color.lower()]

        if notification_minutes is not None:
            event['reminders'] = {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': notification_minutes},
                ],
            }

        # Create event
        created_event = service.events().insert(
            calendarId='primary',
            body=event
        ).execute()

        print("✅ Event created successfully!")
        print(f"\n📅 {created_event['summary']}")
        print(f"🕐 {start_datetime.strftime('%A, %B %d, %Y at %H:%M')}")
        print(f"   to {end_datetime.strftime('%H:%M')}")
        if location:
            print(f"📍 {location}")
        if color:
            print(f"🎨 Color: {color}")
        if notification_minutes:
            print(f"⏰ Email reminder: {notification_minutes} minutes before")
        print(f"\n🔗 {created_event.get('htmlLink', 'N/A')}")

        return created_event

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Add event to Google Calendar (Service Account)')
    parser.add_argument('title', help='Event title')
    parser.add_argument('date', help='Date (e.g., "today", "2025-11-18", "November 18, 2025")')
    parser.add_argument('start_time', help='Start time (e.g., "11:00", "2:30pm")')
    parser.add_argument('end_time', nargs='?', help='End time (optional)')
    parser.add_argument('--color', '-c', choices=list(CALENDAR_COLORS.keys()), help='Event color')
    parser.add_argument('--notification', '-n', type=int, metavar='MINUTES', help='Email notification')
    parser.add_argument('--location', '-l', help='Event location')

    args = parser.parse_args()

    add_event(
        title=args.title,
        date_str=args.date,
        start_time_str=args.start_time,
        end_time_str=args.end_time,
        color=args.color,
        notification_minutes=args.notification,
        location=args.location
    )
