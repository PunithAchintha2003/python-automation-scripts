# 🐍 Python Automation Scripts

> A production-oriented collection of Python automation utilities for system monitoring, log analysis, automated backups, and API health monitoring, containerized with Docker and orchestrated using Docker Compose.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Orchestration-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Published-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
- [Run Individual Scripts](#run-individual-scripts)
- [Docker](#docker)
- [Docker Compose](#docker-compose)
- [Docker Hub](#docker-hub)
- [Project Status](#project-status)
- [Key Skills Demonstrated](#key-skills-demonstrated)
- [Engineering Focus](#engineering-focus)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Overview

This project demonstrates practical Python automation and infrastructure scripting through four independent utilities:

- **System Monitor** — Monitors CPU, memory, and disk utilization.
- **Log Analyzer** — Processes application logs and generates summary reports.
- **Backup Script** — Creates timestamped backups of files and directories.
- **API Health Check** — Monitors service availability, HTTP status codes, and response times.

The tools can be executed locally or deployed as independent Docker containers using Docker Compose, with persistent output managed through Docker volumes.

---

## Architecture

```text
                    Python Automation Scripts
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       System Monitor    Log Analyzer    Backup Script
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                     API Health Check
                              │
                              ▼
                    Docker Containerization
                              │
                              ▼
                    Docker Compose Services
                              │
                              ▼
                     Persistent Volumes
```

---

## Tech Stack

### Programming
- Python 3.12+

### Python Libraries
- `psutil`
- `requests`
- `pathlib`
- `shutil`
- `datetime`
- `logging`
- `collections`

### DevOps & Infrastructure
- Docker
- Docker Compose
- Docker Volumes
- Docker Hub

### Development Tools
- Git
- GitHub
- pyenv
- Python Virtual Environment

---

## Features

- CPU, memory, and disk resource monitoring.
- Automated log analysis and reporting.
- Timestamped file and directory backups.
- API availability and health monitoring.
- HTTP response-time measurement.
- Structured application and operational logging.
- Exception and error handling.
- Automated file system operations.
- Docker containerization.
- Multi-container Docker Compose orchestration.
- Persistent Docker volume management.
- Docker Hub image publishing.

---

## Project Structure

```text
python-automation-scripts/
│
├── data/
│   ├── sample.log
│   └── source_data/
│
├── output/
│   ├── backups/
│   ├── logs/
│   └── reports/
│
├── scripts/
│   ├── 01-system-monitor/
│   │   └── system-monitor.py
│   │
│   ├── 02-log-analyzer/
│   │   └── log-analyzer.py
│   │
│   ├── 03-backup-script/
│   │   └── backup-script.py
│   │
│   └── 04-api-health-check/
│       └── api-health-check.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Local Setup

### Prerequisites
- Python 3.12+
- pip
- Git

### Clone the Repository
```bash
git clone <your-repository-url>
cd python-automation-scripts
```

### Create Virtual Environment
```bash
python -m venv .venv
```

### Activate the Environment

#### macOS/Linux
```bash
source .venv/bin/activate
```

#### Windows
```bash
.venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Run Individual Scripts

### System Monitor
```bash
python scripts/01-system-monitor/system-monitor.py
```

### Log Analyzer
```bash
python scripts/02-log-analyzer/log-analyzer.py
```

### Backup Script
```bash
python scripts/03-backup-script/backup-script.py
```

### API Health Check
```bash
python scripts/04-api-health-check/api-health-check.py
```

---

## Docker

### Build the Image
```bash
docker build -t python-automation-scripts .
```

### Run the Container
```bash
docker run --rm python-automation-scripts
```

---

## Docker Compose

The project includes four independent services:

| Service | Responsibility |
|---|---|
| `system-monitor` | System resource monitoring |
| `log-analyzer` | Log processing and reporting |
| `backup-script` | Automated file and directory backups |
| `api-health-check` | API availability and response monitoring |

### Build All Services
```bash
docker compose build
```

### Start Services
```bash
docker compose up
```

### Run in Detached Mode
```bash
docker compose up -d
```

### Check Service Status
```bash
docker compose ps
```

### View Service Logs
```bash
docker compose logs
```

### Stop Services
```bash
docker compose down
```

The services use Docker volumes to persist generated reports, logs, and backup data outside the container lifecycle.

---

## Docker Hub

The Docker image is published to Docker Hub:

**achintha2003/python-automation-scripts**

### Pull the Image
```bash
docker pull achintha2003/python-automation-scripts:latest
```

### Run the Published Image
```bash
docker run --rm achintha2003/python-automation-scripts:latest
```

---

## Project Status

| Component | Status |
|---|---|
| System Monitoring | ✅ Completed |
| Log Analysis | ✅ Completed |
| Automated Backups | ✅ Completed |
| API Health Monitoring | ✅ Completed |
| Python Automation | ✅ Completed |
| Docker Containerization | ✅ Completed |
| Docker Compose Orchestration | ✅ Completed |
| Persistent Docker Volumes | ✅ Completed |
| Docker Hub Publishing | ✅ Completed |

---

## Key Skills Demonstrated

This project demonstrates practical experience in:

- Python automation and scripting.
- Linux-oriented system operations.
- System resource monitoring.
- Application and operational logging.
- Log processing and analysis.
- File system automation.
- Automated backup workflows.
- HTTP API monitoring.
- Network error handling.
- Exception handling.
- Docker image creation and containerization.
- Multi-service Docker Compose orchestration.
- Persistent container data management.
- Docker Hub image publishing.

---

## Engineering Focus

This project provides practical foundations relevant to:

**DevOps Engineering • MLOps Engineering • Cloud Engineering • AI Infrastructure Engineering • Platform Engineering**

---

## Troubleshooting

### Module not found error
Make sure the virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Docker build fails
Check that Docker is running and that your `Dockerfile` exists in the project root:
```bash
docker build -t python-automation-scripts .
```

### Docker Compose services exit immediately
Inspect logs for the failed service:
```bash
docker compose logs
```

### Permission issues on Linux/macOS
If needed, make the script executable or run with proper permissions:
```bash
chmod +x scripts/01-system-monitor/system-monitor.py
```

---

## Contributing

Contributions are welcome. If you want to improve the scripts, Docker setup, or documentation:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Author

**Punith Achintha**

BSc (Hons) Software Engineering

Focus Areas:
- AI Infrastructure
- MLOps
- Cloud Engineering
- DevOps
- Python Automation

---

## License

This project is licensed under the MIT License.