@echo off
echo 🎯 Testing Calendar Integration with PACO Event!
echo.
echo Make sure you're in the calendar-integration\src folder!
echo.
python add_event_service.py "PACO AIR CON @ABarraca" "Tuesday, November 18, 2025" "11:00" "12:00" --color tangerine --notification 20
echo.
pause
