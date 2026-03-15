# Project Overview

Electricity demand forecasting is a critical component of power system planning and grid reliability. Accurate load predictions allow system operators to anticipate demand, schedule generation resources efficiently, and maintain grid stability.

This project applies the **CRISP-DM (Cross Industry Standard Process for Data Mining)** methodology to analyze historical electricity demand data from the **Electric Reliability Council of Texas (ERCOT)**. The objective is to develop machine learning models that estimate electricity load using historical patterns and engineered features.

The repository demonstrates a **complete end-to-end data science workflow**, including:

- exploratory data analysis
    
- data cleaning and preprocessing
    
- feature engineering
    
- predictive modeling
    
- model evaluation
    
- reporting and visualization
    

By organizing the workflow around CRISP-DM phases, the project provides a **structured and reproducible machine learning pipeline**.

---

# Project Workflow

The analysis follows the CRISP-DM lifecycle.

Business Understanding  
        │  
        ▼  
Data Understanding  
        │  
        ▼  
Data Preparation  
        │  
        ▼  
Baseline Model ───► Feature Engineered Model  
        │                     │  
        └──────────► Evaluation  
                         │  
                         ▼  
                     Reporting

Each stage of the pipeline is implemented as a Python script located in the `scripts/` directory.

---

# Dataset Information

The dataset contains historical electricity demand observations for the ERCOT power grid.

ERCOT manages the flow of electricity to more than **26 million Texas customers**, making it one of the largest competitive electricity markets in the United States.

The dataset includes:

- timestamp (`TIME`)
    
- regional electricity load values
    
- total ERCOT system load (`Load`)
    

The project derives additional predictors from the raw data.

### Calendar Features

- year
    
- month
    
- day
    
- hour
    
- weekday
    

### Engineered Load Features

- load lag variables
    
- rolling statistical summaries
    

Raw dataset location:

data/raw/ercot_load.csv

Processed dataset location:

data/processed/ercot_processed.csv

Separating raw and processed data ensures transparency and reproducibility in the data preparation stage.

---

# CRISP-DM Workflow

## 1. Business Understanding

The goal of the project is to forecast electricity demand using historical ERCOT load data.

Accurate demand forecasts support:

- grid reliability planning
    
- electricity market operations
    
- generation scheduling
    
- energy demand research
    

---

## 2. Data Understanding

Exploratory analysis examines dataset structure and identifies patterns and potential data quality issues.

Key tasks include:

- inspecting dataset dimensions
    
- analyzing variable types
    
- identifying missing values
    
- generating summary statistics
    
- visualizing load patterns
    

Exploratory analysis is conducted in:

notebooks/01_data_understanding.ipynb

---

## 3. Data Preparation

The data preparation stage transforms raw ERCOT data into a format suitable for modeling.

Processing steps include:

- removing duplicate observations
    
- converting timestamps to datetime
    
- converting load values to numeric format
    
- sorting data chronologically
    
- generating calendar features
    
- creating lag features
    
- computing rolling statistics
    

### Time-Based Features

year  
month  
day  
hour  
weekday

### Lag Features

load_lag_1  
load_lag_24

### Rolling Features

load_rolling_mean_24  
load_rolling_std_24

These engineered variables capture **short-term load persistence and recent demand trends**.

---

## 4. Modeling

The modeling stage compares two forecasting models.

### Baseline Model

The baseline model uses only calendar-based predictors:

year  
month  
day  
hour  
weekday

This model captures general temporal demand patterns.

---

### Feature-Engineered Model

The feature-engineered model extends the baseline model with lag and rolling load features:

load_lag_1  
load_lag_24  
load_rolling_mean_24  
load_rolling_std_24

These features incorporate historical load behavior and improve predictive performance.

Both models are implemented using **Linear Regression from Scikit-Learn**.

---

## 5. Evaluation

Model performance is evaluated using standard regression metrics:

| Metric | Description                  |
| ------ | ---------------------------- |
| MAE    | Mean Absolute Error          |
| RMSE   | Root Mean Squared Error      |
| R²     | Coefficient of Determination |

Evaluation results are saved in:

outputs/metrics/evaluation_metrics.csv

This file compares the predictive accuracy of the baseline and feature-engineered models.

---

## 6. Reporting and Visualization

The reporting stage summarizes model outputs and generates visualizations.

Generated outputs include:

### Predictions

outputs/predictions/baseline_model.csv  
outputs/predictions/feature_engineered_model.csv

### Metrics

outputs/metrics/evaluation_metrics.csv

### Visualizations

outputs/figures/load_trend.png  
outputs/figures/model_scatter.png

These artifacts demonstrate the complete machine learning workflow.

---

# Repository Structure

ercot-load-forecasting-crispdm  
│  
├── data  
│   ├── raw  
│   │   └── ercot_load.csv  
│   └── processed  
│       └── ercot_processed.csv  
│  
├── notebooks  
│   └── 01_data_understanding.ipynb  
│  
├── scripts  
│   ├── 01_business_understanding.py  
│   ├── 02_data_understanding.py  
│   ├── 03_data_preparation.py  
│   ├── 04_modeling.py  
│   ├── 05_evaluation.py  
│   └── 06_reporting.py  
│  
├── outputs  
│   ├── figures  
│   │   ├── load_trend.png  
│   │   └── model_scatter.png  
│   ├── metrics  
│   │   └── evaluation_metrics.csv  
│   └── predictions  
│       ├── baseline_model.csv  
│       └── feature_engineered_model.csv  
│  
├── requirements.txt  
├── run_pipeline.py  
└── README.md

This structure separates **data, code, and outputs**, improving reproducibility and project clarity.

---

# How to Run the Project

Follow these steps to reproduce the analysis.

---

## 1. Clone the Repository

git clone  https://github.com/NU-Hartfield/ERCOT-Load-Forecasting-CRISPDM.git
cd ercot-load-forecasting-crispdm

---

## 2. Create a Virtual Environment

python -m venv venv

Activate the environment.

### Windows

venv\Scripts\activate

### Mac / Linux

source venv/bin/activate

---

## 3. Install Dependencies

pip install -r requirements.txt

---

## 4. Run the CRISP-DM Pipeline

python scripts/01_business_understanding.py  
python scripts/02_data_understanding.py  
python scripts/03_data_preparation.py  
python scripts/04_modeling.py  
python scripts/05_evaluation.py  
python scripts/06_reporting.py

Alternatively run the entire pipeline:

python run_pipeline.py

---

## 5. Explore the Notebook 

Launch Jupyter Notebook:

jupyter notebook

Open:

notebooks/01_data_understanding.ipynb

---

# Example Output

### Load Trend Visualization

The exploratory analysis generates visualizations illustrating load patterns over time.

---

# Dependencies

Required Python libraries include:

pandas  
numpy  
matplotlib  
seaborn  
scikit-learn  
jupyter  
statsmodels

All dependencies are listed in:

requirements.txt

---

# Results and Insights

The project produces reproducible outputs demonstrating the complete CRISP-DM machine learning workflow.

Key outputs include:

- processed dataset used for modeling
    
- predictions from baseline and feature-engineered models
    
- evaluation metrics comparing model accuracy
    
- visualizations illustrating electricity demand patterns
    

The comparison between baseline and feature-engineered models demonstrates how **incorporating historical load dynamics improves forecasting accuracy**.