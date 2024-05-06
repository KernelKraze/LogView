import glob
import os
import json
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

log_directory = "/var/log/mongodb"
log_file_name = "mongod.log"

log_files = sorted(glob.glob(os.path.join(log_directory, log_file_name + '*')), reverse=True)

log_data = defaultdict(list)

def extract_json_objects(line):
    objects = []
    depth = 0
    obj_start = None
    for i, char in enumerate(line):
        if char == '{':
            if depth == 0:
                obj_start = i
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0 and obj_start is not None:
                try:
                    obj = json.loads(line[obj_start:i+1])
                    objects.append(obj)
                    obj_start = None
                except json.JSONDecodeError:
                    console.print("Failed to decode JSON", style="bold red")
    return objects

def process_log_file(file_path):
    try:
        with open(file_path, 'rt', encoding='utf-8', errors='ignore') as file:
            for line in file:
                json_objects = extract_json_objects(line)
                for obj in json_objects:
                    if 'c' in obj:
                        log_data[obj['c']].append(obj)
                    else:
                        console.print("Missing 'c' key in log entry.", style="bold yellow")
    except Exception as e:
        console.print(f"Error reading {file_path}: {str(e)}", style="bold red")

for log_file in log_files:
    console.print(f"Processing file: {log_file}", style="bold green")
    process_log_file(log_file)

log_table = Table(show_header=True, header_style="bold magenta")
log_table.add_column("Timestamp", style="dim")
log_table.add_column("Level", style="green")
log_table.add_column("Category", style="blue")
log_table.add_column("Context", style="cyan")
log_table.add_column("Message", style="yellow")
log_table.add_column("Details", style="red")

for category, entries in log_data.items():
    for entry in entries:
        details = entry.get('attr', "N/A")
        log_table.add_row(
            entry['t']['$date'] if 't' in entry and '$date' in entry['t'] else "N/A",
            entry.get('s', "N/A"),
            category,
            entry.get('ctx', "N/A"),
            entry.get('msg', "N/A"),
            Text(str(details))
        )

console.print(log_table)

