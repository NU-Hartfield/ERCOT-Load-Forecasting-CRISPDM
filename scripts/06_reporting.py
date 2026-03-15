"""
06_reporting.py

Purpose:
Generate a simple summary report of project outputs.
"""

import os

def main():
    print("CRISP-DM Stage: Reporting")
    print("\nProject output folders:")

    output_dirs = [
        "outputs/figures",
        "outputs/metrics",
        "outputs/predictions"
    ]

    for folder in output_dirs:
        print(f"\nContents of {folder}:")
        if os.path.exists(folder):
            files = os.listdir(folder)
            if files:
                for file in files:
                    print(f" - {file}")
            else:
                print(" - No files yet")
        else:
            print(" - Folder not found")

if __name__ == "__main__":
    main()