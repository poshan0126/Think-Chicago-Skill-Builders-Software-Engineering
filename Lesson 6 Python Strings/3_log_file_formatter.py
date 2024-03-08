
# Task 1: Timestamp Extraction
def extract_timestamps(log_entries):
    for entry in log_entries:
        timestamp = entry.split(']')[0][1:]
        print(timestamp)

# Task 2: Error Identification
def identify_errors(log_entries):
    for entry in log_entries:
        if "ERROR:" in entry:
            timestamp = entry.split(']')[0][1:]
            print(f"{timestamp}: {entry}")

# Task 3: Log Summary
def log_summary(log_entries):
    total_entries = len(log_entries)
    error_messages = [entry for entry in log_entries if "ERROR:" in entry]
    unique_timestamps = set(entry.split(']')[0][1:] for entry in log_entries)
    print(f"Total Entries: {total_entries}, Errors: {len(error_messages)}, Unique Timestamps: {len(unique_timestamps)}")
    

if __name__ == '__main__':
    extract_timestamps("test")
    identify_errors("test")
    log_summary("test")