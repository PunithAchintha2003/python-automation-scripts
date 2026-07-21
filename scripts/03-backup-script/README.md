# Backup Script

A Python-based automated backup tool that copies files and folders into timestamped backup directories.

This project is part of my Python Automation Toolkit, developed as part of my journey toward AI Infrastructure and MLOps engineering.

---

## Features

- Copy files
- Copy folders
- Create backup directories automatically
- Add timestamps to backup directories
- Preserve file metadata using `shutil.copy2()`
- Log backup activities
- Log successful file and folder copies
- Handle backup errors
- Create multiple timestamped backups

---

## Technologies Used

- Python 3
- shutil
- pathlib
- datetime
- logging

---

## Project Structure

```text
03-backup-script/

├── backup-script.py
├── backups/
└── README.md