from pathlib import Path
from collections import Counter


# -----------------------------
# Configuration
# -----------------------------

LOG_FILE = Path("sample.log")
REPORT_FILE = Path("report.txt")


# -----------------------------
# Read Log File
# -----------------------------

def read_log_file(log_file):
    """Read the log file and return all log lines."""

    try:
        with log_file.open("r") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        return []


# -----------------------------
# Analyze Log Entries
# -----------------------------

def analyze_logs(log_lines):
    """Count INFO, WARNING, and ERROR messages."""

    log_levels = []

    for line in log_lines:

        if "INFO" in line:
            log_levels.append("INFO")

        elif "WARNING" in line:
            log_levels.append("WARNING")

        elif "ERROR" in line:
            log_levels.append("ERROR")

    return Counter(log_levels)


# -----------------------------
# Generate Summary Report
# -----------------------------

def generate_report(log_file, counts):
    """Generate a formatted log analysis report."""

    total_entries = sum(counts.values())

    report = f"""
========================================
          LOG ANALYSIS REPORT
========================================

Log File:
{log_file}

----------------------------------------
SUMMARY
----------------------------------------

Total Log Entries: {total_entries}

INFO Messages:
{counts["INFO"]}

WARNING Messages:
{counts["WARNING"]}

ERROR Messages:
{counts["ERROR"]}

========================================
"""

    return report


# -----------------------------
# Save Report
# -----------------------------

def save_report(report, report_file):
    """Save the analysis report to a text file."""

    with report_file.open("w") as file:
        file.write(report)


# -----------------------------
# Main Program
# -----------------------------

def main():

    print("Starting log analysis...")

    log_lines = read_log_file(LOG_FILE)

    if not log_lines:
        print("No log entries found.")
        return

    counts = analyze_logs(log_lines)

    report = generate_report(LOG_FILE, counts)

    print(report)

    save_report(report, REPORT_FILE)

    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()