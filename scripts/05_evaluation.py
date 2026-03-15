"""
05_evaluation.py

Purpose:
Evaluate and compare baseline and feature-engineered models.
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from pathlib import Path

def evaluate_file(file_path, model_name):
    df = pd.read_csv(file_path)

    y_true = df["actual"]
    y_pred = df["predicted"]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "Model": model_name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

def main():
    results = []

    results.append(
        evaluate_file(
            "outputs/predictions/baseline_model.csv",
            "Baseline_Model"
        )
    )

    results.append(
        evaluate_file(
            "outputs/predictions/feature_engineered_model.csv",
            "Feature_Engineered_Model"
        )
    )

    metrics_dir = Path("outputs/metrics")
    metrics_dir.mkdir(parents=True, exist_ok=True)

    metrics_df = pd.DataFrame(results)
    metrics_df.to_csv("outputs/metrics/evaluation_metrics.csv", index=False)
   
    print("Evaluation complete.")
    print(metrics_df)

if __name__ == "__main__":
    main()