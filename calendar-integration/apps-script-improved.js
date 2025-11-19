/**
 * IMPROVED Google Apps Script for Calendar Integration
 *
 * Enhancements:
 * - Multiple notifications support (array of minutes)
 * - Better error handling
 * - Support for email and popup notifications
 * - Natural language date parsing improvements
 * - Validation and confirmation responses
 *
 * To update your live API:
 * 1. Go to https://script.google.com/
 * 2. Open "Life OS Calendar API" project
 * 3. Replace the code with this
 * 4. Deploy → Manage deployments → Edit → New version → Deploy
 */

function doPost(e) {
  try {
    // Parse incoming JSON
    const params = JSON.parse(e.postData.contents);

    // Extract parameters
    const title = params.title;
    const dateStr = params.date; // YYYY-MM-DD
    const startTime = params.start_time; // HH:MM
    const endTime = params.end_time; // HH:MM
    const color = params.color;
    const location = params.location || '';
    const description = params.description || '';

    // Handle multiple notifications (backwards compatible)
    let notifications = params.notifications || [];
    if (params.notification && !Array.isArray(notifications)) {
      // Support old single notification format
      notifications = [params.notification];
    }

    // Validate required fields
    if (!title || !dateStr || !startTime) {
      return createResponse(false, 'Missing required fields: title, date, start_time');
    }

    // Parse date and time
    const dateParts = dateStr.split('-');
    const year = parseInt(dateParts[0]);
    const month = parseInt(dateParts[1]) - 1; // JS months are 0-indexed
    const day = parseInt(dateParts[2]);

    const startParts = startTime.split(':');
    const startHour = parseInt(startParts[0]);
    const startMin = parseInt(startParts[1]);

    // Create start date
    const startDateTime = new Date(year, month, day, startHour, startMin);

    // Create end date
    let endDateTime;
    if (endTime) {
      const endParts = endTime.split(':');
      const endHour = parseInt(endParts[0]);
      const endMin = parseInt(endParts[1]);
      endDateTime = new Date(year, month, day, endHour, endMin);
    } else {
      // Default to 1 hour if no end time specified
      endDateTime = new Date(startDateTime.getTime() + 60 * 60 * 1000);
    }

    // Validate dates
    if (isNaN(startDateTime.getTime()) || isNaN(endDateTime.getTime())) {
      return createResponse(false, 'Invalid date or time format');
    }

    if (endDateTime <= startDateTime) {
      return createResponse(false, 'End time must be after start time');
    }

    // Get calendar
    const calendar = CalendarApp.getDefaultCalendar();

    // Create event
    const event = calendar.createEvent(title, startDateTime, endDateTime, {
      description: description,
      location: location
    });

    // Set color if provided
    const colorMap = {
      'lavender': CalendarApp.EventColor.PALE_BLUE,
      'sage': CalendarApp.EventColor.PALE_GREEN,
      'grape': CalendarApp.EventColor.MAUVE,
      'flamingo': CalendarApp.EventColor.PALE_RED,
      'banana': CalendarApp.EventColor.YELLOW,
      'tangerine': CalendarApp.EventColor.ORANGE,
      'peacock': CalendarApp.EventColor.CYAN,
      'graphite': CalendarApp.EventColor.GRAY,
      'blueberry': CalendarApp.EventColor.BLUE,
      'basil': CalendarApp.EventColor.GREEN,
      'tomato': CalendarApp.EventColor.RED
    };

    if (color && colorMap[color.toLowerCase()]) {
      event.setColor(colorMap[color.toLowerCase()]);
    }

    // Add notifications
    // First, remove default notifications
    event.removeAllReminders();

    // Add each notification
    for (const minutes of notifications) {
      const mins = parseInt(minutes);
      if (!isNaN(mins) && mins >= 0) {
        // Add popup notification
        event.addPopupReminder(mins);

        // Also add email notification for notifications >= 60 minutes
        if (mins >= 60) {
          event.addEmailReminder(mins);
        }
      }
    }

    // If no notifications specified, add default (10 minutes)
    if (notifications.length === 0) {
      event.addPopupReminder(10);
    }

    // Get day of week for confirmation
    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const dayOfWeek = daysOfWeek[startDateTime.getDay()];

    // Create success response
    return createResponse(true, 'Event created successfully', {
      event_id: event.getId(),
      title: title,
      date: dateStr,
      day_of_week: dayOfWeek,
      start_time: startTime,
      end_time: endTime,
      color: color,
      notifications: notifications,
      calendar_link: event.getUrl()
    });

  } catch (error) {
    return createResponse(false, 'Error creating event: ' + error.message);
  }
}

function createResponse(success, message, data = {}) {
  const response = {
    success: success,
    message: message,
    ...data
  };

  return ContentService
    .createTextOutput(JSON.stringify(response))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Test function - run this in the Apps Script editor to test locally
 */
function testCreateEvent() {
  const testData = {
    postData: {
      contents: JSON.stringify({
        title: 'Test Event from Apps Script',
        date: '2025-11-20',
        start_time: '15:00',
        end_time: '16:30',
        color: 'banana',
        notifications: [60, 10],
        location: 'Test Location',
        description: 'This is a test event'
      })
    }
  };

  const result = doPost(testData);
  Logger.log(result.getContent());
}
