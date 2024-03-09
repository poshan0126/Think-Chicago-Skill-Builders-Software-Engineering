
# The Grade Analyzer

grades = [88, 92, 78, 90, 82, 85, 91, 60, 77, 72]

# Task 1: Calculate the Average Grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Task 2: Find Highest and Lowest Grade
def find_extremes(grades):
    return max(grades), min(grades)

# Task 3: Categorize Grades
def categorize_grades(grades):
    grade_categories = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}
    for grade in grades:
        if grade >= 90:
            grade_categories['A'].append(grade)
        elif grade >= 80:
            grade_categories['B'].append(grade)
        elif grade >= 70:
            grade_categories['C'].append(grade)
        elif grade >= 60:
            grade_categories['D'].append(grade)
        else:
            grade_categories['F'].append(grade)
    return grade_categories

# Displaying Results
average = calculate_average(grades)
high, low = find_extremes(grades)
categories = categorize_grades(grades)

print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {high}, Lowest Grade: {low}")
print("Grade Categories:")
for category, grades in categories.items():
    print(f"{category}: {grades}")
