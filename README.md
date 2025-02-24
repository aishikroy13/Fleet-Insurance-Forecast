# Fleet Insurance Forecast Model for FP&A Analyst Role at Flock

This GitHub repository contains a forecast model that predicts the number of insurance claims for commercial fleets over the coming months. The model is built using simulated data that mimics real-world fleet insurance scenarios, including vehicle telematics, driver information, claims history, and external factors like weather. The project reflects Flock's data-driven approach to fleet insurance and demonstrates key skills required for the FP&A Analyst role, such as financial modeling, data analysis, and forecasting.

## Key Features
- **Data Simulation:** Synthetic datasets for vehicles, drivers, telematics, claims, and weather.
- **Data Cleaning and Merging:** Combines multiple data sources into a single, clean dataset.
- **Feature Engineering:** Creates relevant features to improve forecast accuracy.
- **Forecasting Model:** Uses the Prophet model to predict future claims.
- **Financial Analysis:** Estimates the financial impact of predicted claims.
- **Visualizations:** Provides clear insights through plots and dashboards.

## Repository Structure

fleet-insurance-forecast/
│
├── data/                           # Simulated datasets
│   ├── vehicles.csv
│   ├── drivers.csv
│   ├── telematics.csv
│   ├── claims.csv
│   └── weather.csv
│
├── notebooks/                      # Jupyter notebooks for each step
│   ├── 01_data_generation.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_forecasting.ipynb
│   └── 06_financial_analysis.ipynb
│
├── src/                            # Python scripts for key functions
│   ├── data_generation.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── forecasting.py
│
├── models/                         # Saved model files (if applicable)
│
├── results/                        # Output files (forecasts, visualizations)
│   ├── forecasts.csv
│   └── claims_forecast_plot.png
│
├── README.md                       # Project overview and instructions
└── requirements.txt                # Python dependencies



   
