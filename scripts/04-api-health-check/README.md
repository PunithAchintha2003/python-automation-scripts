# API Health Check

A Python-based API monitoring tool that checks whether an API or website is available and responding correctly.

This project is part of my Python Automation Toolkit, developed as part of my journey toward AI Infrastructure and MLOps engineering.

---

## Features

- Send HTTP GET requests
- Check HTTP status codes
- Measure API response time
- Detect healthy APIs
- Detect unhealthy APIs
- Detect connection failures
- Detect request timeouts
- Generate health reports
- Save health reports to a file
- Log successful API checks
- Log API failures and errors

---

## Technologies Used

- Python 3
- requests
- time
- logging
- datetime

---

## Project Structure

```text
04-api-health-check/

├── api-health-check.py
├── health_report.txt
├── health_check.log
└── README.md