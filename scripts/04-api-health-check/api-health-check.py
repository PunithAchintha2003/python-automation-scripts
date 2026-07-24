import requests
import time
import logging
from pathlib import Path
from datetime import datetime


# -----------------------------------
# Configuration
# -----------------------------------

API_URL = "https://www.google.com"


# -----------------------------------
# Output Directories
# -----------------------------------

LOG_DIR = Path("output/logs")
REPORT_DIR = Path("output/reports")

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# -----------------------------------
# Output File Paths
# -----------------------------------

LOG_FILE = LOG_DIR / "health_check.log"
REPORT_FILE = REPORT_DIR / "health_report.txt"


# -----------------------------------
# Logging Configuration
# -----------------------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------------
# Check API Health
# -----------------------------------

def check_api_health(url):
    """Send an HTTP GET request and check API health."""

    start_time = time.time()

    try:

        response = requests.get(
            url,
            timeout=10
        )

        end_time = time.time()

        response_time = (
            end_time - start_time
        )

        status_code = response.status_code

        if 200 <= status_code < 300:

            status = "Healthy"

            logging.info(
                f"API is healthy - URL: {url} - "
                f"Status Code: {status_code} - "
                f"Response Time: "
                f"{response_time:.2f} seconds"
            )

        else:

            status = "Unhealthy"

            logging.warning(
                f"API returned an error - URL: {url} - "
                f"Status Code: {status_code}"
            )

        return {
            "url": url,
            "status_code": status_code,
            "response_time": response_time,
            "status": status
        }

    except requests.exceptions.Timeout:

        logging.error(
            f"API request timed out - URL: {url}"
        )

        return {
            "url": url,
            "status_code": "N/A",
            "response_time": "N/A",
            "status": "Timeout"
        }

    except requests.exceptions.ConnectionError:

        logging.error(
            f"Connection failed - URL: {url}"
        )

        return {
            "url": url,
            "status_code": "N/A",
            "response_time": "N/A",
            "status": "Connection Failed"
        }

    except requests.exceptions.RequestException as error:

        logging.error(
            f"API request failed - URL: {url} - "
            f"Error: {error}"
        )

        return {
            "url": url,
            "status_code": "N/A",
            "response_time": "N/A",
            "status": "Request Failed"
        }


# -----------------------------------
# Generate Health Report
# -----------------------------------

def generate_report(result):
    """Generate a formatted API health report."""

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
========================================
          API HEALTH CHECK REPORT
========================================

Checked At:
{current_time}

----------------------------------------
API INFORMATION
----------------------------------------

URL:
{result["url"]}

Status Code:
{result["status_code"]}

Response Time:
{result["response_time"]} seconds

Health Status:
{result["status"]}

========================================
"""

    return report


# -----------------------------------
# Save Health Report
# -----------------------------------

def save_report(report):
    """Save health report to the output directory."""

    with REPORT_FILE.open("w") as file:
        file.write(report)


# -----------------------------------
# Main Program
# -----------------------------------

def main():

    logging.info(
        "API health check started."
    )

    print(
        "Starting API health check..."
    )

    result = check_api_health(
        API_URL
    )

    report = generate_report(
        result
    )

    print(report)

    save_report(
        report
    )

    logging.info(
        "Health report saved successfully."
    )

    print(
        f"Health report saved to: "
        f"{REPORT_FILE}"
    )


if __name__ == "__main__":
    main()