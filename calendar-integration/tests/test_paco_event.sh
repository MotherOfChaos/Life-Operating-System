#!/bin/bash
# Test script for Sarah's PACO AIR CON event
# Event details from her request:
# Tuesday, November 18, 2025 // 11:00 to 12:00
# Title: PACO AIR CON @ABarraca
# Color: tangerine
# Notification: 20 mins before as email

echo "🧪 Testing calendar integration with PACO AIR CON event..."
echo ""
echo "Event Details:"
echo "  Title: PACO AIR CON @ABarraca"
echo "  Date: Tuesday, November 18, 2025"
echo "  Time: 11:00 - 12:00"
echo "  Color: Tangerine 🍊"
echo "  Notification: Email 20 minutes before"
echo ""
echo "Running command..."
echo ""

cd "$(dirname "$0")/../src"

python3 add_event.py \
  "PACO AIR CON @ABarraca" \
  "Tuesday, November 18, 2025" \
  "11:00" \
  "12:00" \
  --color tangerine \
  --notification 20

echo ""
echo "✨ Test complete! Check your Google Calendar."
