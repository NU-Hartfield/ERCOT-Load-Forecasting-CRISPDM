"""
03_data_preparation.py

Purpose:
Clean the ERCOT dataset, create time-based and lag-based features,
and save a processed version for modeling.
"""

import pandas as pd

def main():
    input_path = "data/raw/ercot_load.csv"
    output_path = "data/processed/ercot_processed.csv"

    df = pd.read_csv(input_path)

    print("Original shape:", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert TIME column to datetime safely
    if "TIME" in df.columns:
        df["TIME"] = pd.to_datetime(df["TIME"], errors="coerce", format="mixed")

    # Convert all non-time columns to numeric
    for col in df.columns:
        if col != "TIME":
            df[col] = df[col].astype(str).str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Rename ERCOT to Load if needed
    if "ERCOT" in df.columns and "Load" not in df.columns:
        df = df.rename(columns={"ERCOT": "Load"})

    # Drop rows with invalid timestamps
    if "TIME" in df.columns:
        df = df.dropna(subset=["TIME"])

    # Sort chronologically
    if "TIME" in df.columns:
        df = df.sort_values("TIME").reset_index(drop=True)

    # Create time-based features
    if "TIME" in df.columns:
        df["year"] = df["TIME"].dt.year
        df["month"] = df["TIME"].dt.month
        df["day"] = df["TIME"].dt.day
        df["hour"] = df["TIME"].dt.hour
        df["weekday"] = df["TIME"].dt.weekday

    # Create lag and rolling features if Load exists
    if "Load" in df.columns:
        df["load_lag_1"] = df["Load"].shift(1)
        df["load_lag_24"] = df["Load"].shift(24)
        df["load_rolling_mean_24"] = df["Load"].rolling(window=24).mean()
        df["load_rolling_std_24"] = df["Load"].rolling(window=24).std()

    # Drop rows with missing values created by lag/rolling features
    df = df.dropna()

    # Save processed dataset
    df.to_csv(output_path, index=False)

    print("Processed shape:", df.shape)
    print(f"Processed dataset saved to: {output_path}")
    print("Columns in processed dataset:")
    print(df.columns.tolist())

if __name__ == "__main__":
    main()