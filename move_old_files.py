import os
import shutil
from datetime import datetime, timedelta

# Paths for Desktop and Downloads folders (modify as needed)
desktop_path = os.path.expanduser("~/Desktop")
downloads_path = os.path.expanduser("~/Downloads")
archive_folder_path = os.path.expanduser("~/Archive")

# Create the archive folder if it doesn't exist
if not os.path.exists(archive_folder_path):
    os.makedirs(archive_folder_path)

# Function to move old files to the archive folder
def move_old_files(folder_path):
    # Define how many days old a file needs to be to get moved (e.g., 30 days)
    days_old = 30

    # Current time for comparison
    now = datetime.now()

    # Iterate over files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the last modified time of the file
        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        # Calculate the age of the file
        if now - file_time > timedelta(days=days_old):
            # Move file to archive
            shutil.move(file_path, os.path.join(archive_folder_path, filename))

# Move old files from Desktop and Downloads
move_old_files(desktop_path)
move_old_files(downloads_path)
