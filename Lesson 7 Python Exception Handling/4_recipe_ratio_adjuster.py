
# The Recipe Ratio Adjuster

# Task 1: Start
original_servings = float(input("Original number of servings: "))
desired_servings = float(input("Desired number of servings: "))

# Task 2: Quantity Calculation
def adjust_recipe(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        print(f"Adjustment factor: {adjustment_factor}")
        # Adjust recipe quantities here if needed
    except ZeroDivisionError:
        print("Original servings cannot be zero.")
    finally:
        print("Enjoy your cooking!")

# Task 3: Serving Success
adjust_recipe(original_servings, desired_servings)
