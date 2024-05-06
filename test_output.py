import pexpect
import sys
def run_script(script_name):
    """Function to run a Python script using pexpect to emulate a terminal and capture colored output."""
    print(f"Starting: {script_name}")
    child = pexpect.spawn(f'python3 {script_name}')
    child.logfile = sys.stdout.buffer  # Redirect output to stdout to capture color
    child.expect(pexpect.EOF)
    child.close()

# List of scripts to execute
scripts = [
    'AuthView.py',
    'KernelView.py',
    'MongodbView.py',
    'NginxErrorView.py',
    'NginxView.py',
    'SysLogView.py'
]

# Execute each script in the list
for script in scripts:
    run_script(script)

print("All scripts have been executed.")

