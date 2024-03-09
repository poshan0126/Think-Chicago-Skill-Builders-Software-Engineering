
# The Time Zone Traveler

from datetime import datetime
import pytz

# Task 1: Start
current_time = input("Enter the current time (YYYY-MM-DD HH:MM): ")
target_time_zone = input("Enter the target time zone: ")

# Task 2: Time Conversion
def convert_time(current_time_str, target_time_zone):
    try:
        current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
        current_time_utc = current_time.replace(tzinfo=pytz.UTC)
        target_zone = pytz.timezone(target_time_zone)
        target_time = current_time_utc.astimezone(target_zone)
    except ValueError:
        print("Invalid time or time zone format.")
    except pytz.exceptions.UnknownTimeZoneError:
        print("Unknown time zone. Please enter a valid time zone.")
    else:
        print(f"The time in {target_time_zone} is {target_time.strftime('%Y-%m-%d %H:%M')}.")

# Task 3: Traveler's Aid
    finally:
        print("Safe travels!")

convert_time(current_time, target_time_zone)
