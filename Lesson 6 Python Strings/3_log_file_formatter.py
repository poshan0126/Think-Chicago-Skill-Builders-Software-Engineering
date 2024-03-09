
# Log File Formatter

# Task 1: Timestamp Extraction
def extract_timestamps(log_entries):
    for entry in log_entries:
        timestamp = entry.split("]")[0][1:]
        print(timestamp)

# Task 2: Error Identification
def identify_errors(log_entries):
    for entry in log_entries:
        if "ERROR:" in entry:
            timestamp = entry.split("]")[0][1:]
            print(f"Error at {timestamp}: {entry}")

# Task 3: Log Summary
def log_summary(log_entries):
    total_entries = len(log_entries)
    error_messages = sum("ERROR:" in entry for entry in log_entries)
    unique_timestamps = len(set(entry.split("]")[0][1:] for entry in log_entries))
    print(f"Total Entries: {total_entries}, Errors: {error_messages}, Unique Timestamps: {unique_timestamps}")

# Calls with dummy values
log_entries = [
    "[2021-03-15 10:00:00] INFO: System boot",
    "[2021-03-15 10:01:00] ERROR: Failed to load module"
]
extract_timestamps(log_entries)
identify_errors(log_entries)
log_summary(log_entries)
