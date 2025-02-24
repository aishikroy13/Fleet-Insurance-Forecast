import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

def generate_forecasts():
    # Load the trained model
    model = Prophet.load('../models/prophet_model.joblib')

    # Create future dataframe for 12 months ahead
    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)

    os.makedirs('../results', exist_ok=True)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('../results/forecasts.csv', index=False)

    # Plot forecast
    fig = model.plot(forecast)
    plt.savefig('../results/claims_forecast_plot.png')
    plt.close()

if __name__ == '__main__':
    generate_forecasts()

