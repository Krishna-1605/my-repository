
import calendar
from datetime import datetime

# Store events
events = {}

# --------- Input Event ---------
date = input("Enter event date (YYYY-MM-DD): ")
title = input("Enter event title: ")
time = input("Enter event time (HH:MM): ")
priority = input("Enter priority (high/medium/low): ").lower()

# --------- Date Validation ---------
try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("❌ Invalid date")
    exit()

# --------- Store Event ---------
event = {"title": title, "time": time, "priority": priority}
events[date] = [event]

# --------- Display Calendar ---------
year, month, _ = map(int, date.split("-"))

print(f"\n========== {calendar.month_name[month]} {year} ==========")
print(calendar.month(year, month))
print("==================================")

# --------- Display Organized Event ---------
print(f"\n📅 Events for {date}:")
print("---------------------------------")

if priority == "high":
    alert = "🔴 [HIGH]"
elif priority == "medium":
    alert = "🟠 [MEDIUM]"
else:
    alert = "🟢 [LOW]"

print(f"{alert} {time} - {title}")
print("---------------------------------")
# --------- WEEK SUMMARY INPUT ---------
total_events = int(input("\nEnter total events this week: "))
high_priority = int(input("Enter high priority events count: "))
upcoming_today = int(input("Enter today's upcoming events: "))

# --------- WEEK SUMMARY OUTPUT ---------
print("\n📊 This Week Summary:")
print(f"- Total Events: {total_events}")
print(f"- High Priority: {high_priority}")
print(f"- Upcoming Today: {upcoming_today}")
print("==================================")
