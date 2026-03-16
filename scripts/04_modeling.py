"""
04_modeling.py

Purpose:
Train and compare a baseline model and a feature-engineered model
for ERCOT load forecasting using a chronological train-test split.
Also generates coefficient magnitude and predicted vs actual plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
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

    # Keep only numeric columns for modeling
    numeric_df = df.select_dtypes(include=["number"]).copy()

    if target_column not in numeric_df.columns:
        print(f"Error: target column '{target_column}' is not numeric or missing after filtering.")
        return

    # -----------------------------
    # Feature Definitions
    # -----------------------------
    # Baseline model: calendar/time-based features only
    baseline_features = [
        col for col in ["year", "month", "day", "hour", "weekday"]
        if col in numeric_df.columns
    ]

    # Feature-engineered model: baseline + lag/rolling features
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
        print("Expected features: year, month, day, hour, weekday")
        return

    if len(engineered_features) == len(baseline_features):
        print("Warning: engineered features were not found.")
        print("The feature-engineered model may be identical to the baseline model.")

    model_definitions = {
        "Baseline_Model": baseline_features,
        "Feature_Engineered_Model": engineered_features
    }

    # Chronological split for time series
    split_index = int(len(numeric_df) * 0.8)

    # Create output directories
    predictions_dir = Path("outputs/predictions")
    figures_dir = Path("outputs/figures")

    predictions_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    # -----------------------------
    # Model Training Loop
    # -----------------------------
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

        # -----------------------------
        # Save Predictions
        # -----------------------------
        output = pd.DataFrame({
            "Model": model_name,
            "actual": y_test.values,
            "predicted": predictions
        })

        output_file = predictions_dir / f"{model_name.lower()}.csv"
        output.to_csv(output_file, index=False)

        # -----------------------------
        # Coefficient Magnitude Plot
        # -----------------------------
        coefficients = pd.Series(model.coef_, index=feature_list)
        coefficients = coefficients.abs().sort_values(ascending=False)

        plt.figure(figsize=(10, 5))
        coefficients.plot(kind="bar")
        plt.title(f"{model_name} Coefficient Magnitude")
        plt.xlabel("Feature")
        plt.ylabel("Absolute Coefficient Value")
        plt.xticks(rotation=45)
        plt.tight_layout()

        coefficient_plot_file = figures_dir / f"{model_name.lower()}_feature_importance.png"
        plt.savefig(coefficient_plot_file)
        plt.close()

        # -----------------------------
        # Predicted vs Actual Plot
        # -----------------------------
        plt.figure(figsize=(6, 6))
        plt.scatter(y_test, predictions, alpha=0.6)
        plt.xlabel("Actual Load")
        plt.ylabel("Predicted Load")
        plt.title(f"{model_name} Predicted vs Actual")

        # Reference line
        plt.plot(
            [y_test.min(), y_test.max()],
            [y_test.min(), y_test.max()],
            "r--"
        )

        plt.tight_layout()

        scatter_plot_file = figures_dir / f"{model_name.lower()}_predicted_vs_actual.png"
        plt.savefig(scatter_plot_file)
        plt.close()

        print(f"{model_name} complete.")
        print(f"Features used: {feature_list}")
        print(f"Predictions saved to {output_file}")
        print(f"Coefficient magnitude plot saved to {coefficient_plot_file}")
        print(f"Predicted vs actual plot saved to {scatter_plot_file}\n")


if __name__ == "__main__":
    main()