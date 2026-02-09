# Q1_Calendar_Generation.py
# Program to generate calendar for a given month and year

import calendar

# -------- USER INPUT --------
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print(f"\nCalendar for {month}/{year}\n")
print(calendar.month(year, month))



