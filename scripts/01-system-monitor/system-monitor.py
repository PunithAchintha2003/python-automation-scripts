import psutil
import logging
from datetime import datetime


# -----------------------------
# Logging Configuration
# -----------------------------

logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------
# Get System Information
# -----------------------------

def get_system_info():
    """Collect system resource information."""

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory.percent,
        "memory_total": memory.total,
        "memory_available": memory.available,
        "disk_usage": disk.percent,
        "disk_total": disk.total,
        "disk_free": disk.free
    }


# -----------------------------
# Generate System Report
# -----------------------------

def generate_report(system_info):
    """Generate a formatted system report."""

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
========================================
        SYSTEM MONITOR REPORT
========================================

Generated At:
{current_time}

----------------------------------------
CPU INFORMATION
----------------------------------------

CPU Usage: {system_info["cpu_usage"]}%

----------------------------------------
MEMORY INFORMATION
----------------------------------------

Memory Usage: {system_info["memory_usage"]}%
Total Memory: {system_info["memory_total"] / (1024 ** 3):.2f} GB
Available Memory: {system_info["memory_available"] / (1024 ** 3):.2f} GB

----------------------------------------
DISK INFORMATION
----------------------------------------

Disk Usage: {system_info["disk_usage"]}%
Total Disk Space: {system_info["disk_total"] / (1024 ** 3):.2f} GB
Free Disk Space: {system_info["disk_free"] / (1024 ** 3):.2f} GB

========================================
"""

    return report


# -----------------------------
# Save Report to File
# -----------------------------

def save_report(report):
    """Save system report to a text file."""

    with open("system_report.txt", "w") as file:
        file.write(report)


# -----------------------------
# Main Program
# -----------------------------

def main():

    logging.info("System monitoring started.")

    try:
        system_info = get_system_info()

        report = generate_report(system_info)

        print(report)

        save_report(report)

        logging.info("System report generated successfully.")
        logging.info("System report saved to system_report.txt")

    except Exception as error:
        logging.error(f"System monitoring failed: {error}")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()