year = int(input("Enter a year: "))

# Leap Year Checker
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("It's a leap year." if is_leap_year else "It's not a leap year.")

# Century Verification
if year % 100 == 0:
    print("It's a century year.")

# Time Traveler
if year > 2024:
    print("It's a future year.")
elif year < 2024:
    print("It's a past year.")
else:
    print("It's the current year.")