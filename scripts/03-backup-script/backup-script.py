import shutil
import logging
from pathlib import Path
from datetime import datetime


# -----------------------------------
# Configuration
# -----------------------------------

SOURCE_DIR = Path("source_data")
BACKUP_DIR = Path("backups")


# -----------------------------------
# Logging Configuration
# -----------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------------
# Create Sample Source Directory
# -----------------------------------

def create_sample_source():
    """Create a sample source directory for testing."""

    if not SOURCE_DIR.exists():
        SOURCE_DIR.mkdir()

        sample_file = SOURCE_DIR / "example.txt"

        sample_file.write_text(
            "This is a sample file for the backup script.\n"
        )

        logging.info("Sample source directory created.")


# -----------------------------------
# Create Backup Directory
# -----------------------------------

def create_backup_directory():
    """Create a timestamped backup directory."""

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_path = BACKUP_DIR / f"backup_{timestamp}"

    backup_path.mkdir(parents=True, exist_ok=True)

    logging.info(f"Backup directory created: {backup_path}")

    return backup_path


# -----------------------------------
# Copy Files and Folders
# -----------------------------------

def create_backup(source, destination):
    """Copy source files and folders to the backup directory."""

    try:

        if not source.exists():
            logging.error(f"Source directory does not exist: {source}")
            return False

        for item in source.iterdir():

            destination_path = destination / item.name

            if item.is_dir():

                shutil.copytree(
                    item,
                    destination_path,
                    dirs_exist_ok=True
                )

                logging.info(
                    f"Folder copied successfully: {item.name}"
                )

            elif item.is_file():

                shutil.copy2(
                    item,
                    destination_path
                )

                logging.info(
                    f"File copied successfully: {item.name}"
                )

        return True

    except Exception as error:

        logging.error(
            f"Backup failed: {error}"
        )

        return False


# -----------------------------------
# Main Program
# -----------------------------------

def main():

    logging.info("Backup process started.")

    try:

        # Create sample source directory
        create_sample_source()

        # Create main backups directory
        BACKUP_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        # Create timestamped backup directory
        backup_path = create_backup_directory()

        # Create backup
        success = create_backup(
            SOURCE_DIR,
            backup_path
        )

        if success:

            logging.info(
                "Backup completed successfully."
            )

            print()
            print("=" * 50)
            print("       BACKUP COMPLETED SUCCESSFULLY")
            print("=" * 50)
            print()
            print(f"Source: {SOURCE_DIR}")
            print(f"Backup: {backup_path}")
            print()

        else:

            logging.error(
                "Backup process failed."
            )

            print(
                "Backup failed. Check the logs for details."
            )

    except Exception as error:

        logging.error(
            f"Unexpected error: {error}"
        )

        print(
            f"An unexpected error occurred: {error}"
        )


if __name__ == "__main__":
    main()