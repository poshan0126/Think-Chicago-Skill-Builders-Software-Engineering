
# Text-Based Report Generator

# Task 1: Header Formatter
def format_header(header):
    return header.upper().center(50, "=")

# Task 2: Data Alignment
def align_data(data_rows):
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data_rows)]
    for row in data_rows:
        print(" ".join(str(item).ljust(width) for item, width in zip(row, column_widths)))

# Task 3: Report Summary
def report_summary(data_rows):
    total_entries = len(data_rows)
    numeric_column = [float(row[-1]) for row in data_rows if row[-1].replace('.', '', 1).isdigit()]
    average_value = sum(numeric_column) / len(numeric_column) if numeric_column else 0
    print(f"Total Entries: {total_entries}, Average Value: {average_value:.2f}")

# Calls with dummy values
header = format_header("Sales Report")
print(header)
data_rows = [["Item", "Quantity", "Price"], ["Apples", "24", "1.00"], ["Bananas", "18", "0.80"]]
align_data(data_rows)
report_summary(data_rows[1:])  # Excluding header for calculation
