**LogView Project README**

📁 **Project Structure**
```
📂 LogView
  ├── AuthView.py
  ├── KernelView.py
  ├── MongodbView.py
  ├── NginxErrorView.py
  ├── NginxView.py
  └── SysLogView.py
```

**AuthView.py**
```python
🔐 **Authentication Log View**

- This module handles authentication logs.
- Captures 'sudo' command usage and failed SSH login attempts.
- Displays detailed information about user activities and failed login attempts.

**Usage:**
1. Run the file.
2. Set the log file path and view authentication logs.
3. Analyze 'sudo' command usage and SSH login attempts, and view activities of specific users.

```

**KernelView.py**
```python
🐧 **Kernel Log View**

- This module handles kernel logs.
- Captures EXT4 filesystem warnings, errors, and undervoltage warnings.
- Displays aggregated log events and their occurrences.

**Usage:**
1. Run the file.
2. Set the kernel log file path and view kernel events.
3. Identify warnings and errors in the logs, and view their frequency of occurrence.

```

**MongodbView.py**
```python
📦 **MongoDB Log View**

- This module handles MongoDB logs.
- Extracts JSON objects and displays log entries.
- Provides timestamp, level, category, context, message, and additional attributes.

**Usage:**
1. Run the file.
2. Set the MongoDB log file path and view logs.
3. Extract JSON objects and view detailed information about MongoDB operations.

```

**NginxErrorView.py**
```python
🚨 **Nginx Error Log View**

- This module handles Nginx error logs.
- Parses timestamp, level, client IP, server, request method, request URL, message, and referrer.
- Displays detailed error information and IP count summary.

**Usage:**
1. Run the file.
2. Set the Nginx error log file path and analyze errors.
3. View timestamps, client IPs, and details of corresponding errors.

```

**NginxView.py**
```python
🌐 **Nginx Access Log View**

- This module handles Nginx access logs.
- Parses IP address, timestamp, HTTP method, URL, status code, and user agent.
- Displays access details and IP count summary.

**Usage:**
1. Run the file.
2. Set the Nginx access log file path and view logs.
3. View details such as URLs, status codes, and user agents of user accesses.

```

**SysLogView.py**
```python
📝 **System Log View**

- This module handles system logs.
- Captures timestamp, process, PID, and message for regular system log entries.
- Displays system log messages.

**Usage:**
1. Run the file.
2. Set the system log file path and view logs.
3. View system events and process activities in log messages.

```

This project handles and analyzes various types of logs to understand system status and troubleshoot issues. Each module provides detailed information about specific types of logs to help diagnose and resolve problems.

[中文](./README_CN.md)
[한국어](./README_KR.md)
