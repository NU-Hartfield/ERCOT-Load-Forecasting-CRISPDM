"""
01_business_understanding.py

Purpose:
Define the forecasting objective, business relevance, and success metrics
for the ERCOT electricity load forecasting project.

This script represents the CRISP-DM Business Understanding phase and
generates a summary file documenting the project objectives.
"""

from pathlib import Path

def main():

    project_info = {
        "project": "ERCOT Electricity Load Forecasting",
        "framework": "CRISP-DM",
        "objective": "Forecast ERCOT electricity demand using historical load data and machine learning.",
        "business_relevance": (
            "Accurate electricity load forecasting supports grid reliability, "
            "generation scheduling, and operational planning for power systems."
        ),
        "success_metrics": [
            "MAE (Mean Absolute Error)",
            "RMSE (Root Mean Squared Error)",
            "R² (Coefficient of Determination)"
        ]
    }

    print("\nCRISP-DM Stage: Business Understanding\n")

    print("Project:", project_info["project"])
    print("Framework:", project_info["framework"])
    print("Objective:", project_info["objective"])
    print("Business Relevance:", project_info["business_relevance"])
    print("Success Metrics:", ", ".join(project_info["success_metrics"]))

    # Save documentation output
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "business_understanding.txt"

    with open(output_file, "w") as f:
        f.write("CRISP-DM Stage: Business Understanding\n\n")
        f.write(f"Project: {project_info['project']}\n")
        f.write(f"Framework: {project_info['framework']}\n\n")
        f.write("Objective:\n")
        f.write(project_info["objective"] + "\n\n")
        f.write("Business Relevance:\n")
        f.write(project_info["business_relevance"] + "\n\n")
        f.write("Success Metrics:\n")
        for metric in project_info["success_metrics"]:
            f.write(f"- {metric}\n")

    print("\nBusiness understanding summary saved to:")
    print(output_file)


if __name__ == "__main__":
    main()