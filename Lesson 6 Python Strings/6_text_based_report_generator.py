
# Task 1: Header Formatter
def format_header(header):
    return f"{header.upper():=^50}"

# Task 2: Data Alignment
def align_data(data):
    columns = data.split(',')
    formatted_data = ', '.join(column.strip() for column in columns)
    return formatted_data

# Task 3: Report Summary
def report_summary(data):
    num_entries = len(data)
    print(f"Total data entries: {num_entries}")

if __name__ == '__main__':
    format_header('header')
    align_data('data')
    report_summary('header')
