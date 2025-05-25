import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",  
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Iterate and create files/directories
for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent
    filename = file_path.name

    if file_dir != Path("."):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {filename}")

    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")
