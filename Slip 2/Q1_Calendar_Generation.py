# Program to generate calendar for a given month and year
# This file prints the calendar. Sample output is stored in a variable (so it won't display in Jupyter).

import calendar

def main():
    try:
        year = int(input("Enter year: ").strip())
        month = int(input("Enter month (1-12): ").strip())
        if month < 1 or month > 12:
            print("Month must be between 1 and 12.")
            return
    except ValueError:
        print("Please enter valid integers for year and month.")
        return

    print(f"\nCalendar for {month} / {year}")
    print(calendar.month(year, month))


if __name__ == "__main__":
    main()

# Sample Input:
# Enter year: 2025
# Enter month (1-12): 11