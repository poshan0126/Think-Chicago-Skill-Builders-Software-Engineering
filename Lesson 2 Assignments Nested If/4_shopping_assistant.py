weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
accessory = "sunscreen" if clothing == "sunglasses" else "boots" if clothing == "umbrella" else "hat"

print(f"Recommended clothing: {clothing}, Accessory: {accessory}")