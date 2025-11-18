#!/usr/bin/env python3
"""
Google Calendar MCP Server for Sarah's Life OS
Enables adding/reading calendar events from any Claude chat
"""

import os
import json
import sys
from datetime import datetime, timedelta
from typing import Any, Sequence
import asyncio

# MCP SDK imports
try:
    from mcp.server import Server
    from mcp.types import Tool, TextContent
    import mcp.server.stdio
except ImportError:
    print("ERROR: MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Google Calendar API imports
try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("ERROR: Google Calendar API not installed. Run: pip install google-auth-oauthlib google-api-python-client", file=sys.stderr)
    sys.exit(1)

# Scopes for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Color mapping for calendar events
CALENDAR_COLORS = {
    'lavender': '1',
    'sage': '2',
    'grape': '3',
    'flamingo': '4',
    'banana': '5',
    'tangerine': '6',
    'peacock': '7',
    'graphite': '8',
    'blueberry': '9',
    'basil': '10',
    'tomato': '11'
}

app = Server("google-calendar")

def get_calendar_service():
    """Authenticate and return Google Calendar service"""
    creds = None
    token_path = os.path.expanduser('~/.config/claude-calendar/token.json')
    creds_path = os.path.expanduser('~/.config/claude-calendar/credentials.json')

    # Load existing credentials
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # Refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_path):
                raise FileNotFoundError(
                    f"Credentials file not found at {creds_path}\n"
                    "Please follow setup instructions to create it."
                )
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def parse_datetime(date_str: str, time_str: str = None) -> str:
    """Parse date and optional time into ISO format"""
    # Handle common date formats
    date_formats = [
        '%A, %B %d, %Y',  # Tuesday, November 18, 2025
        '%B %d, %Y',       # November 18, 2025
        '%Y-%m-%d',        # 2025-11-18
        '%d/%m/%Y',        # 18/11/2025
    ]

    parsed_date = None
    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue

    if not parsed_date:
        # Try parsing as "today", "tomorrow", etc.
        date_str_lower = date_str.lower()
        if date_str_lower == 'today':
            parsed_date = datetime.now()
        elif date_str_lower == 'tomorrow':
            parsed_date = datetime.now() + timedelta(days=1)
        else:
            raise ValueError(f"Could not parse date: {date_str}")

    # Add time if provided
    if time_str:
        # Handle formats like "11:00", "11.00", "11am", "2:30pm"
        time_str = time_str.lower().replace('.', ':')

        # Parse time
        for time_fmt in ['%H:%M', '%I:%M%p', '%I%p', '%H']:
            try:
                time_obj = datetime.strptime(time_str.strip(), time_fmt)
                parsed_date = parsed_date.replace(
                    hour=time_obj.hour,
                    minute=time_obj.minute,
                    second=0,
                    microsecond=0
                )
                break
            except ValueError:
                continue

    return parsed_date.isoformat()

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available calendar tools"""
    return [
        Tool(
            name="add_calendar_event",
            description="Add an event to Google Calendar with date, time, title, color, and notifications",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Event title/summary"
                    },
                    "date": {
                        "type": "string",
                        "description": "Event date (e.g., 'Tuesday, November 18, 2025' or 'today' or '2025-11-18')"
                    },
                    "start_time": {
                        "type": "string",
                        "description": "Start time (e.g., '11:00', '11.00', '2:30pm')"
                    },
                    "end_time": {
                        "type": "string",
                        "description": "End time (optional, defaults to start_time + 1 hour)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Event location (optional)"
                    },
                    "description": {
                        "type": "string",
                        "description": "Event description (optional)"
                    },
                    "color": {
                        "type": "string",
                        "description": "Event color: lavender, sage, grape, flamingo, banana, tangerine, peacock, graphite, blueberry, basil, or tomato"
                    },
                    "notification_minutes": {
                        "type": "integer",
                        "description": "Minutes before event to send email notification (optional)"
                    }
                },
                "required": ["title", "date", "start_time"]
            }
        ),
        Tool(
            name="list_upcoming_events",
            description="List upcoming calendar events",
            inputSchema={
                "type": "object",
                "properties": {
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of events to return (default: 10)"
                    },
                    "days_ahead": {
                        "type": "integer",
                        "description": "Number of days ahead to look (default: 7)"
                    }
                },
                "required": []
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    """Handle tool calls"""

    if name == "add_calendar_event":
        try:
            service = get_calendar_service()

            # Parse dates and times
            start_datetime = parse_datetime(arguments['date'], arguments['start_time'])

            # Handle end time
            if 'end_time' in arguments and arguments['end_time']:
                end_datetime = parse_datetime(arguments['date'], arguments['end_time'])
            else:
                # Default to 1 hour after start
                start_dt = datetime.fromisoformat(start_datetime)
                end_dt = start_dt + timedelta(hours=1)
                end_datetime = end_dt.isoformat()

            # Build event
            event = {
                'summary': arguments['title'],
                'start': {
                    'dateTime': start_datetime,
                    'timeZone': 'Europe/Madrid',  # Sarah's timezone
                },
                'end': {
                    'dateTime': end_datetime,
                    'timeZone': 'Europe/Madrid',
                },
            }

            # Add optional fields
            if 'location' in arguments:
                event['location'] = arguments['location']

            if 'description' in arguments:
                event['description'] = arguments['description']

            # Add color
            if 'color' in arguments:
                color_name = arguments['color'].lower()
                if color_name in CALENDAR_COLORS:
                    event['colorId'] = CALENDAR_COLORS[color_name]

            # Add notification
            if 'notification_minutes' in arguments:
                event['reminders'] = {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': arguments['notification_minutes']},
                    ],
                }

            # Create event
            created_event = service.events().insert(
                calendarId='primary',
                body=event
            ).execute()

            return [TextContent(
                type="text",
                text=f"✅ Event created successfully!\n\n"
                     f"Title: {created_event['summary']}\n"
                     f"Start: {created_event['start']['dateTime']}\n"
                     f"End: {created_event['end']['dateTime']}\n"
                     f"Link: {created_event.get('htmlLink', 'N/A')}"
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ Error creating event: {str(e)}"
            )]

    elif name == "list_upcoming_events":
        try:
            service = get_calendar_service()

            max_results = arguments.get('max_results', 10)
            days_ahead = arguments.get('days_ahead', 7)

            # Get events
            now = datetime.utcnow().isoformat() + 'Z'
            time_max = (datetime.utcnow() + timedelta(days=days_ahead)).isoformat() + 'Z'

            events_result = service.events().list(
                calendarId='primary',
                timeMin=now,
                timeMax=time_max,
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])

            if not events:
                return [TextContent(
                    type="text",
                    text="No upcoming events found."
                )]

            output = f"📅 Upcoming Events (next {days_ahead} days):\n\n"
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                output += f"• {event['summary']} - {start}\n"
                if 'location' in event:
                    output += f"  📍 {event['location']}\n"

            return [TextContent(
                type="text",
                text=output
            )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ Error listing events: {str(e)}"
            )]

    else:
        return [TextContent(
            type="text",
            text=f"Unknown tool: {name}"
        )]

async def main():
    """Run the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
