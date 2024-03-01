attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio system" if attendees > 50 else "projector"
food_preference = input("Do you want vegetarian food? (yes/no): ")
caterers = "Veggie Delight Caterers" if food_preference == "yes" else "Gourmet Meals Caterers"

print(f"Venue: {venue}, Facilities: {facilities}, Caterers: {caterers}")