
# The Journey Planner

# Task 1: Calculate Travel Time
def calculate_travel_time(distance, speed):
    return distance / speed

# Task 2: Suggest Stops
def suggest_stops(distance):
    if distance > 500:
        return "Consider stopping for the night."
    elif distance > 200:
        return "Take breaks and stretch your legs."
    else:
        return "You can drive without stopping."

# Task 3: User Input for Journey Details
def plan_journey():
    start = input("Enter your starting point: ")
    destination = input("Enter your destination: ")
    distance = float(input("Enter the distance in miles: "))
    speed = float(input("Enter your average speed in mph: "))

    travel_time = calculate_travel_time(distance, speed)
    stops = suggest_stops(distance)

    print(f"Estimated travel time from {start} to {destination} is {travel_time:.2f} hours.")
    print(stops)

plan_journey()
