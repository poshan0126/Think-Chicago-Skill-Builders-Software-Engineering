activities = []

def log_activity(activity, duration):
    activities.append((activity, duration))
    print(f"Logged {activity} for {duration} minutes.")

def main():
    log_activity('Running', 30)
    print(f"Today's activities: {activities}")

if __name__ == '__main__':
    main()
