
# The Event Planner

from datetime import datetime

# Task 1: Start
date_input = input("Enter the event date and time (YYYY-MM-DD HH:MM): ")

# Task 2: Reminder Setup
def setup_event(date_str):
    try:
        event_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM format.")
    else:
        print(f"Event set for {event_date}. Reminder is active.")

# Task 3: User Guidance
    finally:
        print("Thank you for using the Event Planner.")

setup_event(date_input)
