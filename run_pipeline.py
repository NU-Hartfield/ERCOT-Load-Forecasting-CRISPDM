"""
run_pipeline.py

Purpose:
Run the full CRISP-DM pipeline in sequence.
"""

import subprocess

scripts = [
    "scripts/01_business_understanding.py",
    "scripts/02_data_understanding.py",
    "scripts/03_data_preparation.py",
    "scripts/04_modeling.py",
    "scripts/05_evaluation.py",
    "scripts/06_reporting.py"
]

print("\nRunning ERCOT Load Forecasting Pipeline\n")

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("\nPipeline completed successfully.")