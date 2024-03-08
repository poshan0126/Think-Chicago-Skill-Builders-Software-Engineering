grades = [88, 76, 92, 85, 69]

def calculate_average():
    return sum(grades) / len(grades)

def main():
    print(f"The average grade is: {calculate_average()}")

if __name__ == '__main__':
    main()
