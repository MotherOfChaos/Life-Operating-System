#!/usr/bin/env python3
"""Quick test - disable SSL verification"""

import os
import sys
import ssl
from datetime import datetime, timedelta

# Disable SSL verification globally
ssl._create_default_https_context = ssl._create_unverified_context

from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.config/claude-calendar/service-account.json')
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Parse inputs
title = "PACO AIR CON @ABarraca"
date_str = "Tuesday, November 18, 2025"
start_time = "11:00"
end_time = "12:00"
color_id = '6'  # tangerine
notification = 20

# Get credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build service
service = build('calendar', 'v3', credentials=credentials)

# Parse date/time
date_obj = datetime.strptime(date_str, '%A, %B %d, %Y')
start_obj = datetime.strptime(start_time, '%H:%M')
end_obj = datetime.strptime(end_time, '%H:%M')

start_datetime = date_obj.replace(hour=start_obj.hour, minute=start_obj.minute)
end_datetime = date_obj.replace(hour=end_obj.hour, minute=end_obj.minute)

# Create event
event = {
    'summary': title,
    'start': {'dateTime': start_datetime.isoformat(), 'timeZone': 'Europe/Madrid'},
    'end': {'dateTime': end_datetime.isoformat(), 'timeZone': 'Europe/Madrid'},
    'colorId': color_id,
    'reminders': {
        'useDefault': False,
        'overrides': [{'method': 'email', 'minutes': notification}],
    },
}

print("🔄 Creating event...")
created_event = service.events().insert(calendarId='primary', body=event).execute()

print("\n✅ EVENT CREATED!")
print(f"📅 {created_event['summary']}")
print(f"🕐 {start_datetime.strftime('%A, %B %d, %Y at %H:%M')}")
print(f"🎨 Color: tangerine")
print(f"⏰ Email 20 min before")
print(f"\n🔗 {created_event.get('htmlLink')}")
print("\n🎉 CHECK YOUR GOOGLE CALENDAR!")
