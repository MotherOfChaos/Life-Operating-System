#!/usr/bin/env python3
"""
Simple CLI tool to add events to Google Calendar
Can be used directly or via Claude MCP
"""

import argparse
import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calendar_mcp_server import (
    get_calendar_service,
    parse_datetime,
    CALENDAR_COLORS
)

def add_event(
    title: str,
    date: str,
    start_time: str,
    end_time: str = None,
    location: str = None,
    description: str = None,
    color: str = None,
    notification_minutes: int = None
):
    """Add an event to Google Calendar"""

    try:
        service = get_calendar_service()

        # Parse dates and times
        start_datetime = parse_datetime(date, start_time)

        # Handle end time
        if end_time:
            end_datetime = parse_datetime(date, end_time)
        else:
            # Default to 1 hour after start
            start_dt = datetime.fromisoformat(start_datetime)
            end_dt = start_dt + timedelta(hours=1)
            end_datetime = end_dt.isoformat()

        # Build event
        event = {
            'summary': title,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'Europe/Madrid',
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'Europe/Madrid',
            },
        }

        # Add optional fields
        if location:
            event['location'] = location

        if description:
            event['description'] = description

        # Add color
        if color:
            color_name = color.lower()
            if color_name in CALENDAR_COLORS:
                event['colorId'] = CALENDAR_COLORS[color_name]
            else:
                print(f"Warning: Unknown color '{color}'. Available: {', '.join(CALENDAR_COLORS.keys())}")

        # Add notification
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
        print(f"\nTitle: {created_event['summary']}")
        print(f"Start: {created_event['start']['dateTime']}")
        print(f"End: {created_event['end']['dateTime']}")
        if 'location' in created_event:
            print(f"Location: {created_event['location']}")
        print(f"\nLink: {created_event.get('htmlLink', 'N/A')}")

        return created_event

    except Exception as e:
        print(f"❌ Error creating event: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Add an event to Google Calendar",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple event
  %(prog)s "Team Meeting" "today" "14:00" "15:00"

  # Event with location and color
  %(prog)s "PACO AIR CON @ABarraca" "Tuesday, November 18, 2025" "11:00" "12:00" \\
    --color tangerine --notification 20

  # All-day event
  %(prog)s "Birthday Party" "2025-12-25" --all-day

Available colors: """ + ", ".join(CALENDAR_COLORS.keys())
    )

    parser.add_argument('title', help='Event title')
    parser.add_argument('date', help='Event date (e.g., "today", "tomorrow", "2025-11-18", "November 18, 2025")')
    parser.add_argument('start_time', nargs='?', help='Start time (e.g., "11:00", "2:30pm")')
    parser.add_argument('end_time', nargs='?', help='End time (optional)')
    parser.add_argument('--location', '-l', help='Event location')
    parser.add_argument('--description', '-d', help='Event description')
    parser.add_argument('--color', '-c', choices=list(CALENDAR_COLORS.keys()), help='Event color')
    parser.add_argument('--notification', '-n', type=int, metavar='MINUTES',
                        help='Send email notification N minutes before event')
    parser.add_argument('--all-day', action='store_true', help='Create all-day event')

    args = parser.parse_args()

    # Validate
    if not args.all_day and not args.start_time:
        parser.error("start_time is required unless --all-day is specified")

    add_event(
        title=args.title,
        date=args.date,
        start_time=args.start_time,
        end_time=args.end_time,
        location=args.location,
        description=args.description,
        color=args.color,
        notification_minutes=args.notification
    )

if __name__ == '__main__':
    main()
