import os

# Ensure the directory for logs exists
log_directory = "example_log"
os.makedirs(log_directory, exist_ok=True)

# Define log content based on each script's requirements
logs = {
    "auth.log": [
        "2023-05-01T12:34:56.789+00:00 localhost sudo: johndoe : TTY=pts/0 ; PWD=/home/johndoe ; USER=root ; COMMAND=/usr/bin/ls",
        "2023-05-01T12:35:00.123+00:00 localhost sshd[1234]: Failed password for invalid user hacker from 192.168.1.10 port 22 ssh2"
    ],
    "kern.log": [
        "2023-05-01T12:30:00.456+00:00 localhost kernel: EXT4-fs warning (device sda1): ext4_resize_begin: No space left on device",
        "2023-05-01T12:32:00.789+00:00 localhost kernel: hwmon1: Undervoltage detected"
    ],
    "mongod.log": [
        '{ "t": { "$date": "2023-05-01T12:40:00.123+00:00" }, "s": "W", "c": "STORAGE", "ctx": "initandlisten", "msg": "Initialized MongoDB", "attr": {"volume": "db1"}}'
    ],
    "nginx/error.log": [
        '2023/05/01 12:45:00 [error] 1234#1: *5678 open() "/usr/share/nginx/html/index.html" failed (2: No such file or directory), client: 192.168.1.20, server: localhost, request: "GET /index.html HTTP/1.1", host: "localhost", referrer: "http://localhost/"'
    ],
    "nginx/access.log": [
        '192.168.1.30 - - [01/May/2023:12:50:00 +0000] "GET /api/data HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"'
    ],
    "syslog": [
        "2023-05-01T12:55:00.456+00:00 localhost crond[123]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)"
    ]
}

# Write each log content to the corresponding file
for filename, entries in logs.items():
    full_path = os.path.join(log_directory, filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as file:
        file.write("\n".join(entries) + "\n")

print("Log files have been generated successfully.")

