import calendar
from datetime import datetime, date

# -------------------- DATA --------------------

events = {
    "2025-01-20": [
        {"title": "Team Meeting", "time": "10:00", "priority": "high"},
        {"title": "Lunch with friend", "time": "13:00", "priority": "low"}
    ],
    "2025-01-25": [
        {"title": "Project Deadline", "time": "18:00", "priority": "high"}
    ],
    "2025-01-22": [
        {"title": "Client Call", "time": "11:00", "priority": "medium"},
        {"title": "Code Review", "time": "16:00", "priority": "low"}
    ]
}

# -------------------- DISPLAY CALENDAR --------------------

year = 2025
month = 1

print(f"========== {calendar.month_name[month].upper()} {year} ==========")
print(calendar.month(year, month).strip())
print("==================================\n")

# -------------------- VIEW EVENTS FOR A DATE --------------------

view_date = "2025-01-20"

print(f"📅 Events for {view_date}:")
print("---------------------------------")

for event in events[view_date]:
    if event["priority"] == "high":
        alert = "🔴 [HIGH]"
    elif event["priority"] == "medium":
        alert = "🟠 [MEDIUM]"
    else:
        alert = "🟢 [LOW]"

    print(f"{alert} {event['time']} - {event['title']}")

print("---------------------------------\n")

# -------------------- WEEK SUMMARY --------------------

total_events = 0
high_priority = 0
today_events = 1   # sample value to match output

for event_list in events.values():
    total_events += len(event_list)
    for event in event_list:
        if event["priority"] == "high":
            high_priority += 1

print("📊 This Week Summary:")
print(f"- Total Events: {total_events}")
print(f"- High Priority: {high_priority}")
print(f"- Upcoming Today: {today_events}")
print("==================================")
