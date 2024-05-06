import glob
import os
import re
import gzip
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialize the rich console for enhanced output
console = Console()

# Define the directory where log files are stored and the base name of the log files
#log_directory = "/var/log"
log_directory = "example_log"
log_file_name = "syslog"

# Find all syslog files, including rotated and possibly compressed files
log_files = sorted(glob.glob(os.path.join(log_directory, log_file_name + '*')), reverse=True)

# Regular expression to capture general syslog entries
syslog_regex = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2})\s+\S+\s+'
    r'(?P<process>\S+)\[(?P<pid>\d+)\]:\s+(?P<message>.+)'
)

# Dictionary to store syslog messages
syslog_messages = defaultdict(list)

# Function to process each log file, handling gzipped files if necessary
def process_log_file(file_path):
    open_func = gzip.open if file_path.endswith('.gz') else open  # Determine how to open the file based on its extension
    try:
        with open_func(file_path, 'rt', encoding='utf-8', errors='replace') as file:
            for line in file:
                match = syslog_regex.search(line)
                if match:
                    # Extract and store the necessary details from each log entry
                    details = match.groupdict()
                    syslog_messages[details['timestamp']].append(details)
    except Exception as e:
        # Print any errors encountered during file reading
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

# Process each syslog file and display the processing status
for log_file in log_files:
    console.print(f"Processing file: {log_file}", style="bold green")
    process_log_file(log_file)

# Table to display syslog messages
syslog_table = Table(show_header=True, header_style="bold magenta")
syslog_table.add_column("Timestamp", style="dim")
syslog_table.add_column("Process", style="green")
syslog_table.add_column("PID", style="cyan")
syslog_table.add_column("Message", style="yellow")

# Populate the table with the collected data
for timestamp, entries in syslog_messages.items():
    for entry in entries:
        syslog_table.add_row(
            Text(entry.get("timestamp", "N/A")),
            Text(entry.get("process", "N/A")),
            Text(entry.get("pid", "N/A")),
            Text(entry.get("message", "N/A"))
        )

# Display the table
console.print(syslog_table)

