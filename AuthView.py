import glob
import os
import re
import gzip
from collections import defaultdict
from rich.console import Console
from rich.table import Table

# Initialize the console for enhanced output using the rich library
console = Console()

# Define the directory where log files are stored and the base name of the log files
log_directory = "/var/log"
log_file_name = "auth.log"

# Find all log files, including rotated and compressed files, in the specified directory
log_files = sorted(glob.glob(os.path.join(log_directory, log_file_name + '*')), reverse=True)

# Regular expression to capture details from 'sudo' command usage
sudo_regex = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[\+\-]\d{2}:\d{2})\s+\S+\s+sudo:\s+'
    r'(?P<user>\S+) : TTY=(?P<tty>\S+) ; PWD=(?P<pwd>\S+) ; USER=(?P<runas>\S+) ; COMMAND=(?P<command>.+)$'
)

# Regular expression to capture failed SSH login attempts
failed_login_regex = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[\+\-]\d{2}:\d{2})\s+\S+\s+'
    r'sshd\[\d+\]: Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+) port \d+ ssh2'
)

# Data structure to store command usage details and failed login attempts
command_usage = defaultdict(list)
failed_logins = defaultdict(lambda: {'count': 0, 'users': set(), 'timestamps': []})

# Function to process each log file, handling gzip files if necessary
def process_log_file(file_path):
    # Determine the appropriate function to open the file based on its extension
    open_func = gzip.open if file_path.endswith('.gz') else open
    try:
        # Open the file and read each line
        with open_func(file_path, 'rt', encoding='utf-8', errors='replace') as file:
            for line in file:
                # Search for 'sudo' command usage and store relevant details
                sudo_match = sudo_regex.search(line)
                if sudo_match:
                    details = {
                        "timestamp": sudo_match.group("timestamp"),
                        "tty": sudo_match.group("tty"),
                        "pwd": sudo_match.group("pwd"),
                        "runas": sudo_match.group("runas"),
                        "command": sudo_match.group("command")
                    }
                    command_usage[sudo_match.group("user")].append(details)

                # Search for failed login attempts and store relevant details
                failed_match = failed_login_regex.search(line)
                if failed_match:
                    ip = failed_match.group("ip")
                    user = failed_match.group("user")
                    timestamp = failed_match.group("timestamp")
                    failed_logins[ip]['count'] += 1
                    failed_logins[ip]['users'].add(user)
                    failed_logins[ip]['timestamps'].append(timestamp)
    except Exception as e:
        # Print any errors encountered during file reading
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

# Process each log file and display the processing status
for log_file in log_files:
    console.print(f"Processing file: {log_file}", style="bold green")
    process_log_file(log_file)

# Tables to display command usage and failed login details
command_table = Table(show_header=True, header_style="bold magenta")
command_table.add_column("User", style="dim")
command_table.add_column("Timestamp", style="green")
command_table.add_column("TTY", style="cyan")
command_table.add_column("PWD", style="blue")
command_table.add_column("Run as", style="magenta")
command_table.add_column("Command", style="yellow")

failed_login_table = Table(show_header=True, header_style="bold blue")
failed_login_table.add_column("IP Address", style="dim")
failed_login_table.add_column("Failed Attempts", style="red")
failed_login_table.add_column("Attempted Users", style="magenta")
failed_login_table.add_column("Timestamps", style="cyan")  # Added column for timestamps

# Populate the tables with the collected data
for user, activities in command_usage.items():
    for activity in activities:
        command_table.add_row(
            user,
            activity["timestamp"],
            activity["tty"],
            activity["pwd"],
            activity["runas"],
            activity["command"]
        )

for ip, details in failed_logins.items():
    # Join multiple timestamps into a single string for display
    timestamps = ", ".join(details['timestamps'])
    users_string = ", ".join(details['users'])
    failed_login_table.add_row(ip, str(details['count']), users_string, timestamps)

# Display the tables
console.print(command_table)
console.print(failed_login_table)

