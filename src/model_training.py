import pandas as pd
from prophet import Prophet
import os

def train_model():
    data = pd.read_csv('../data/engineered_data.csv')

    # Aggregate claims by date (ensure 'date' column is datetime)
    claims_by_month = data.groupby('date')['claim_made'].sum().reset_index()
    claims_by_month['date'] = pd.to_datetime(claims_by_month['date'])
    claims_by_month.columns = ['ds', 'y']

    # Split data: use all but last 6 months for training
    train = claims_by_month.iloc[:-6]
    test = claims_by_month.iloc[-6:]

    model = Prophet()
    model.fit(train)

    os.makedirs('../models', exist_ok=True)
    model.save('../models/prophet_model.joblib')
    return model, test

if __name__ == '__main__':
    train_model()
