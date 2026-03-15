"""
02_data_understanding.py

Purpose:
Explore the ERCOT load dataset, generate descriptive statistics,
identify data quality issues, and produce exploratory visualizations.

CRISP-DM Stage: Data Understanding
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def main():

    raw_path = Path("data/raw/ercot_load.csv")
    figures_path = Path("outputs/figures")
    figures_path.mkdir(parents=True, exist_ok=True)

    print("\nCRISP-DM Stage: Data Understanding\n")

    # Load dataset
    df = pd.read_csv(raw_path)

    print("Dataset Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    # Convert timestamp
    if "TIME" in df.columns:
        df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce", format="mixed")

    # Basic dataset preview
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nData Types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Convert numeric columns
    for col in df.columns:
        if col != "TIME":
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "", regex=False)
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Descriptive statistics
    print("\nDescriptive Statistics:")
    print(df.describe())

    # Identify Load column
    if "Load" not in df.columns:
        if "ERCOT" in df.columns:
            df = df.rename(columns={"ERCOT": "Load"})

    # ---- Visualization 1: Load Trend ----
    if "TIME" in df.columns and "Load" in df.columns:

        plt.figure(figsize=(12,5))
        plt.plot(df["TIME"], df["Load"], linewidth=1)
        plt.title("ERCOT Electricity Load Over Time")
        plt.xlabel("Time")
        plt.ylabel("Load (MW)")
        plt.tight_layout()

        trend_path = figures_path / "load_trend.png"
        plt.savefig(trend_path)
        plt.close()

        print("\nSaved:", trend_path)

    # ---- Visualization 2: Load Distribution ----
    if "Load" in df.columns:

        plt.figure(figsize=(8,5))
        sns.histplot(df["Load"], bins=50, kde=True)
        plt.title("Distribution of ERCOT Load")
        plt.xlabel("Load (MW)")
        plt.tight_layout()

        dist_path = figures_path / "load_distribution.png"
        plt.savefig(dist_path)
        plt.close()

        print("Saved:", dist_path)

    # ---- Visualization 3: Correlation Heatmap ----
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] > 1:

        plt.figure(figsize=(10,6))
        sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)
        plt.title("Feature Correlation Matrix")
        plt.tight_layout()

        corr_path = figures_path / "correlation_matrix.png"
        plt.savefig(corr_path)
        plt.close()

        print("Saved:", corr_path)

    print("\nData understanding stage completed.")


if __name__ == "__main__":
    main()