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

# Define the directory where Nginx error log files are stored and the log file name pattern
#error_log_directory = "/var/log/nginx"
error_log_directory = "example_log/nginx"
error_log_file_pattern = "error.log*"

# Find all Nginx error log files, including rotated and compressed files
error_log_files = sorted(glob.glob(os.path.join(error_log_directory, error_log_file_pattern)), reverse=True)
# Regex to parse the Nginx error log entries
error_log_regex = re.compile(
    r'(?P<timestamp>\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] \d+#\d+: '
    r'\*?\d+ (?P<message>.+?)?,? client: (?P<client_ip>\S+), server: (?P<server>\S+), '
    r'request: "(?P<request_method>\S+) (?P<request_url>\S+) HTTP/\d.\d", host: "(?P<host>\S+)"(?:, referrer: "(?P<referrer>\S+)")?', re.DOTALL
)

# Dictionary to store parsed error log data
error_log_data = defaultdict(list)

# Function to process each error log file, handling gzipped files if necessary
def process_error_log_file(file_path):
    open_func = gzip.open if file_path.endswith('.gz') else open  # Open function based on file extension
    try:
        with open_func(file_path, 'rt', encoding='utf-8', errors='replace') as file:
            for line in file:
                match = error_log_regex.search(line)
                if match:
                    details = match.groupdict()
                    # Default empty string if message or referrer are None
                    details['message'] = details['message'] if details['message'] else ''
                    details['referrer'] = details['referrer'] if details.get('referrer') else ''
                    error_log_data[details['client_ip']].append(details)
    except Exception as e:
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

# Process each Nginx error log file and display the processing status
for error_log_file in error_log_files:
    console.print(f"Processing file: {error_log_file}", style="bold green")
    process_error_log_file(error_log_file)

# Display a summary table of error logs
error_table = Table(show_header=True, header_style="bold magenta")
error_table.add_column("Timestamp", style="dim")
error_table.add_column("Level", style="green")
error_table.add_column("Client IP", style="blue")
error_table.add_column("Server", style="cyan")
error_table.add_column("Request Method", style="yellow")
error_table.add_column("Request URL", style="magenta")
error_table.add_column("Message", style="green")
error_table.add_column("Referrer", style="red")

# Add entries to the table
for client_ip, entries in error_log_data.items():
    for entry in entries:
        error_table.add_row(
            Text(entry['timestamp']), Text(entry['level']), Text(entry['client_ip']),
            Text(entry['server']), Text(entry['request_method']), Text(entry['request_url']),
            Text(entry['message']), Text(entry['referrer'])
        )

console.print(error_table)

# Additional summary table for IP counts
summary_table = Table(show_header=True, header_style="bold blue")
summary_table.add_column("Client IP", style="dim")
summary_table.add_column("Total Errors", style="green")

# Summarize error counts per IP
ip_error_counts = {ip: len(entries) for ip, entries in error_log_data.items()}
for ip, count in sorted(ip_error_counts.items(), key=lambda item: item[1], reverse=True):
    summary_table.add_row(Text(ip), Text(str(count)))

console.print(summary_table)

