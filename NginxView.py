import glob
import os
import re
import gzip
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialize the console for output
console = Console()

# Define the directory where Nginx log files are stored and the log file name pattern
log_directory = "/var/log/nginx"
log_file_pattern = "access.log*"

# Find all Nginx access log files, including rotated and compressed files
log_files = sorted(glob.glob(os.path.join(log_directory, log_file_pattern)), reverse=True)

# Regex to parse the Nginx access log entries
log_regex = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) \S+ '
    r'"\S+" "(?P<agent>.+)"'
)

# Dictionary to store parsed log data
log_data = defaultdict(list)

# Function to process each log file, handling gzipped files if necessary
def process_log_file(file_path):
    open_func = gzip.open if file_path.endswith('.gz') else open  # Open function based on file extension
    try:
        with open_func(file_path, 'rt', encoding='utf-8', errors='replace') as file:
            for line in file:
                match = log_regex.search(line)
                if match:
                    details = match.groupdict()
                    log_data[details['ip']].append(details)
    except Exception as e:
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

# Process each Nginx log file and display the processing status
for log_file in log_files:
    console.print(f"Processing file: {log_file}", style="bold green")
    process_log_file(log_file)

# Display a summary table of IP addresses along with their access details
ip_table = Table(show_header=True, header_style="bold magenta")
ip_table.add_column("IP Address", style="dim")
ip_table.add_column("Count", style="green")
ip_table.add_column("Timestamp", style="blue")
ip_table.add_column("Method", style="cyan")
ip_table.add_column("URL", style="yellow")
ip_table.add_column("Status Code", style="magenta")
ip_table.add_column("User Agent", style="green")

# Calculate counts for each IP address
for ip, entries in log_data.items():
    ip_table.add_row(Text(ip), Text(str(len(entries))), "", "", "", "", "")  # Add IP address and count first
    for entry in entries:
        ip_table.add_row(
            "", "", Text(entry['timestamp']), Text(entry['method']), Text(entry['url']),
            Text(entry['status']), Text(entry['agent'])
        )

console.print(ip_table)

# Additional summary table for overall IP counts
summary_table = Table(show_header=True, header_style="bold blue")
summary_table.add_column("IP Address", style="dim")
summary_table.add_column("Total Accesses", style="green")

# Summarize access counts
ip_counts = {ip: len(entries) for ip, entries in log_data.items()}
for ip, count in sorted(ip_counts.items(), key=lambda item: item[1], reverse=True):
    summary_table.add_row(Text(ip), Text(str(count)))

console.print(summary_table)

