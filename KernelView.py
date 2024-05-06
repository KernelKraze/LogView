import glob
import os
import re
import gzip
from collections import defaultdict, Counter
from rich.console import Console
from rich.table import Table

# Initialize the console object for rich output
console = Console()

# Define the path to the log directory and the correct log file name
#log_directory = "/var/log"
log_directory = "example_log"
log_file_name = "kern.log"  # Ensure the correct file name is used

# Find all log files including rotated and compressed ones
log_files = sorted(glob.glob(os.path.join(log_directory, log_file_name + '*')), reverse=True)

# Regex to capture EXT4 filesystem warnings, errors, and undervoltage warnings
log_regex = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2})\s+\S+\s+kernel:\s+.*?'
    r'((EXT4-fs (warning|error) \(device \S+\):\s+(?P<ext4_message>.*))|'
    r'(hwmon \S+: (?P<hw_message>Undervoltage detected|Voltage normalised)))'
)

# Dictionary to store log events
log_events = defaultdict(Counter)

# Function to process each log file, handling gzip if necessary
def process_log_file(file_path):
    open_func = gzip.open if file_path.endswith('.gz') else open
    try:
        with open_func(file_path, 'rt', encoding='utf-8', errors='replace') as file:
            for line in file:
                match = log_regex.search(line)
                if match:
                    timestamp = match.group('timestamp')
                    message = match.group('ext4_message') if match.group('ext4_message') else match.group('hw_message')
                    log_events[message][timestamp] += 1
    except Exception as e:
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

# Process each log file and display processing status
for log_file in log_files:
    console.print(f"Processing file: {log_file}", style="bold green")
    process_log_file(log_file)

# Create a table to display the aggregated log events
log_table = Table(show_header=True, header_style="bold magenta")
log_table.add_column("Event Message", style="yellow", no_wrap=True)
log_table.add_column("Occurrences", style="green")
log_table.add_column("Last Occurrence", style="red")

# Populate the table with data
for message, timestamps in log_events.items():
    total_occurrences = sum(timestamps.values())
    latest_timestamp = max(timestamps, key=timestamps.get)  # Get the latest timestamp
    log_table.add_row(message, str(total_occurrences), latest_timestamp)

# Display the table
console.print(log_table)

