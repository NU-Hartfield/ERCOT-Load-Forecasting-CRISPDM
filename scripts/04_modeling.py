"""
04_modeling.py

Purpose:
Train and compare a baseline model and a feature-engineered model
for ERCOT load forecasting using a chronological train-test split.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from pathlib import Path
def main():
    file_path = "data/processed/ercot_processed.csv"
    df = pd.read_csv(file_path)

    target_column = "Load"

    if target_column not in df.columns:
        print(f"Error: target column '{target_column}' not found.")
        print("Available columns:")
        print(df.columns.tolist())
        return

    numeric_df = df.select_dtypes(include=["number"]).copy()

    if target_column not in numeric_df.columns:
        print(f"Error: target column '{target_column}' is not numeric or missing after filtering.")
        return

    baseline_features = [
        col for col in ["year", "month", "day", "hour", "weekday"]
        if col in numeric_df.columns
    ]

    engineered_features = baseline_features + [
        col for col in [
            "load_lag_1",
            "load_lag_24",
            "load_rolling_mean_24",
            "load_rolling_std_24"
        ]
        if col in numeric_df.columns
    ]

    if not baseline_features:
        print("Error: baseline time-based features not found.")
        return

    model_definitions = {
        "Baseline_Model": baseline_features,
        "Feature_Engineered_Model": engineered_features
    }

    split_index = int(len(numeric_df) * 0.8)

    for model_name, feature_list in model_definitions.items():
        X = numeric_df[feature_list]
        y = numeric_df[target_column]

        X_train = X.iloc[:split_index]
        X_test = X.iloc[split_index:]
        y_train = y.iloc[:split_index]
        y_test = y.iloc[split_index:]

        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        output = pd.DataFrame({
            "Model": model_name,
            "actual": y_test.values,
            "predicted": predictions
        })

        predictions_dir = Path("outputs/predictions")
        predictions_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = predictions_dir / f"{model_name.lower()}.csv"
        output.to_csv(output_file, index=False)

        print(f"{model_name} complete.")
        print(f"Features used: {feature_list}")
        print(f"Predictions saved to {output_file}\n")

if __name__ == "__main__":
    main()