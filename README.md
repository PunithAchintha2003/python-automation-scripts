# 🐍 Python Automation Toolkit

> A collection of practical Python automation and system administration tools designed to build real-world scripting, monitoring, logging, file automation, and API integration skills.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Overview

This repository contains a collection of practical Python automation projects focused on **system monitoring, log analysis, file and folder backups, and API health monitoring**.

The goal of this repository is to develop strong foundations in:

* 🐍 Python scripting
* ⚙️ System automation
* 🖥️ System monitoring
* 📊 Log analysis
* 💾 Backup automation
* 🌐 API monitoring
* 📝 Application logging
* 🛡️ Error handling
* 📁 File system operations
* 🔧 DevOps and infrastructure automation concepts

These projects are designed as hands-on learning exercises while building a foundation for **AI Infrastructure Engineering, MLOps, DevOps, and Cloud Engineering**.

---

## 🗂️ Project Structure

```text
python-automation-scripts/
│
├── scripts/
│   │
│   ├── 01-system-monitor/
│   │   ├── system-monitor.py
│   │   ├── system_report.txt
│   │   ├── system_monitor.log
│   │   └── README.md
│   │
│   ├── 02-log-analyzer/
│   │   ├── log-analyzer.py
│   │   ├── sample.log
│   │   ├── report.txt
│   │   └── README.md
│   │
│   ├── 03-backup-script/
│   │   ├── backup-script.py
│   │   ├── backups/
│   │   └── README.md
│   │
│   └── 04-api-health-check/
│       ├── api-health-check.py
│       ├── health_report.txt
│       ├── health_check.log
│       └── README.md
│
└── README.md
```

---

# 🚀 Projects

## 1️⃣ System Monitor

📂 `01-system-monitor/`

A Python-based system monitoring tool that collects information about system resource usage and generates an automated report.

### ✨ Features

* 🖥️ CPU usage monitoring
* 🧠 Memory usage monitoring
* 💽 Disk usage monitoring
* 📊 Automated system report generation
* 📄 Save reports to a text file
* 📝 Application logging
* ⚠️ Error handling

### 🛠️ Technologies

* Python
* `psutil`
* `datetime`
* `logging`

### 🎯 Key Concepts

* System monitoring
* Resource utilization
* File handling
* Python logging
* Exception handling

---

## 2️⃣ Log Analyzer

📂 `02-log-analyzer/`

A Python-based log analysis tool that reads log files and generates a summary of different log levels.

### ✨ Features

* 📖 Read log files
* ℹ️ Count `INFO` messages
* ⚠️ Count `WARNING` messages
* ❌ Count `ERROR` messages
* 📊 Generate summary reports
* 📄 Save analysis results to a file

### 🛠️ Technologies

* Python
* `pathlib`
* `collections.Counter`

### 🎯 Key Concepts

* File processing
* Text parsing
* Log analysis
* Data aggregation
* Python standard library

---

## 3️⃣ Backup Script

📂 `03-backup-script/`

A Python automation script that creates timestamped backups of files and directories.

### ✨ Features

* 📁 Copy files
* 📂 Copy directories
* 💾 Create backup directories
* 🕒 Generate timestamped backup folders
* 📝 Log backup operations
* ⚠️ Handle backup errors
* 🔄 Support multiple backup versions

### 🛠️ Technologies

* Python
* `shutil`
* `os`
* `pathlib`
* `datetime`
* `logging`

### 🎯 Key Concepts

* File system automation
* Backup workflows
* Directory management
* Timestamp generation
* Logging and error handling

---

## 4️⃣ API Health Check

📂 `04-api-health-check/`

A Python-based monitoring tool that checks the availability and health of APIs or web services.

### ✨ Features

* 🌐 Send HTTP GET requests
* 🔢 Check HTTP status codes
* ⏱️ Measure response time
* 💚 Detect healthy services
* 🔴 Detect unhealthy services
* ⏳ Handle request timeouts
* 🔌 Handle connection failures
* 📄 Generate health reports
* 📝 Log API failures

### 🛠️ Technologies

* Python
* `requests`
* `time`
* `datetime`
* `logging`

### 🎯 Key Concepts

* REST API communication
* HTTP status codes
* Service health monitoring
* Network error handling
* Response time monitoring
* Application logging

---

# 🧰 Technologies & Tools

### Programming Language

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square\&logo=python\&logoColor=white)

### Python Libraries

* `psutil`
* `requests`
* `pathlib`
* `shutil`
* `os`
* `datetime`
* `logging`
* `collections`

### Development Tools

* 💻 macOS
* 🐍 Python 3.12+
* 🔀 Git
* 🐙 GitHub
* 📝 VS Code
* 🛠️ pyenv
* 📦 Python Virtual Environments

---

# ⚙️ Getting Started

## 📋 Prerequisites

Make sure you have the following installed:

* Python 3.12+
* Git
* pip

Check your Python version:

```bash
python --version
```

Or:

```bash
python3 --version
```

---

## 📥 Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd python-automation-scripts
```

---

# 🐍 Python Environment Setup

This repository uses Python virtual environments to isolate project dependencies.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on macOS/Linux:

```bash
source .venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

# 📦 Install Dependencies

Some projects use third-party Python libraries.

Install `psutil` for the System Monitor:

```bash
pip install psutil
```

Install `requests` for the API Health Check:

```bash
pip install requests
```

Or install both:

```bash
pip install psutil requests
```

---

# ▶️ Running the Projects

## 🖥️ System Monitor

```bash
cd 01-system-monitor
python system-monitor.py
```

---

## 📊 Log Analyzer

```bash
cd 02-log-analyzer
python log-analyzer.py
```

---

## 💾 Backup Script

```bash
cd 03-backup-script
python backup-script.py
```

---

## 🌐 API Health Check

```bash
cd 04-api-health-check
python api-health-check.py
```

---

# 📈 Learning Progress

| Project             | Focus Area                  | Status      |
| ------------------- | --------------------------- | ----------- |
| 🖥️ System Monitor  | System Monitoring & Logging | ✅ Completed |
| 📊 Log Analyzer     | Log Processing & Analysis   | ✅ Completed |
| 💾 Backup Script    | File & Directory Automation | ✅ Completed |
| 🌐 API Health Check | API & Service Monitoring    | ✅ Completed |

---

# 🎓 Skills Demonstrated

By completing these projects, this repository demonstrates practical experience with:

### 🐍 Python

* Functions
* Dictionaries
* Lists
* Exception handling
* File handling
* Modules and packages
* Standard library usage

### ⚙️ Automation

* System resource monitoring
* File and directory automation
* Automated backups
* API health monitoring

### 📝 Logging & Monitoring

* Application logging
* Error logging
* System monitoring
* Service health checks
* Response time monitoring

### 📁 File Systems

* Reading and writing files
* Directory management
* File copying
* Folder copying
* Path manipulation

### 🌐 APIs

* HTTP GET requests
* HTTP status codes
* API availability checks
* Timeout handling
* Connection error handling

---

# 🔮 Future Roadmap

The repository will continue to evolve with more advanced automation and infrastructure projects.

### 🔹 Python Automation

* [ ] Add command-line interfaces using `argparse`
* [ ] Add configuration files
* [ ] Add environment variable support
* [ ] Improve error handling
* [ ] Add unit tests with `pytest`
* [ ] Add type hints
* [ ] Add code formatting with `Black`
* [ ] Add linting with `Ruff`

### 🔹 DevOps & Infrastructure

* [ ] Dockerize automation tools
* [ ] Add Docker Compose projects
* [ ] Add CI/CD with GitHub Actions
* [ ] Add automated testing pipelines
* [ ] Add Linux system administration scripts
* [ ] Add process monitoring
* [ ] Add network monitoring

### 🔹 Cloud & MLOps

* [ ] AWS automation scripts
* [ ] Azure automation scripts
* [ ] Cloud infrastructure monitoring
* [ ] Infrastructure as Code with Terraform
* [ ] Kubernetes automation
* [ ] MLOps pipeline automation

---

# 🗺️ Learning Roadmap

```text
Python Fundamentals
        │
        ▼
Python Automation
        │
        ▼
Linux & System Administration
        │
        ▼
Git & GitHub
        │
        ▼
Docker & Containers
        │
        ▼
CI/CD & GitHub Actions
        │
        ▼
Cloud Engineering
        │
        ▼
Infrastructure as Code
        │
        ▼
Kubernetes
        │
        ▼
MLOps & AI Infrastructure
```

---

# 🤝 Contributing

This repository is primarily a personal learning and portfolio project.

However, suggestions and improvements are welcome.

If you have an idea:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Punith Achintha**

🎓 BSc (Hons) Software Engineering

💡 Interested in:

* 🤖 AI Infrastructure
* 🔄 MLOps
* ☁️ Cloud Engineering
* ⚙️ DevOps
* 🐍 Python Automation
* 🐧 Linux

---

🚀 This repository is part of my journey toward becoming an **AI Infrastructure / MLOps Engineer**.
