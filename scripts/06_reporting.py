"""
06_reporting.py

Purpose:
Generate a simple summary report of project outputs.
"""

import os
from pathlib import Path


def main():

    print("CRISP-DM Stage: Reporting")
    print("\nProject output folders:")

    output_dirs = [
        "outputs/figures",
        "outputs/metrics",
        "outputs/predictions"
    ]

    # Ensure output directories exist
    for folder in output_dirs:
        Path(folder).mkdir(parents=True, exist_ok=True)

    # Display contents
    for folder in output_dirs:
        print(f"\nContents of {folder}:")
        files = os.listdir(folder)

        if files:
            for file in files:
                print(f" - {file}")
        else:
            print(" - No files yet")


if __name__ == "__main__":
    main()