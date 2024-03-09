
# The Fitness Tracker

activities = []

# Task 1: Log Activities
def log_activity(name, duration):
    activities.append({'activity': name, 'duration': duration})
    print(f"Activity '{name}' logged for {duration} minutes.")

# Task 2: Estimate Calories Burned
def estimate_calories():
    calories_burned = sum(activity['duration'] * 5 for activity in activities)  # Assuming 5 calories per minute as a simple estimate
    return calories_burned

# Task 3: Summary Report
def summary_report():
    total_duration = sum(activity['duration'] for activity in activities)
    print(f"Total Activities Logged: {len(activities)}")
    print(f"Total Duration: {total_duration} minutes")
    print(f"Estimated Calories Burned: {estimate_calories()}")

# Sample Function Calls
log_activity("Running", 30)
log_activity("Cycling", 45)
summary_report()
