import pandas as pd
import os

def load_data():
    vehicles = pd.read_csv('../data/vehicles.csv')
    drivers = pd.read_csv('../data/drivers.csv')
    telematics = pd.read_csv('../data/telematics.csv')
    claims = pd.read_csv('../data/claims.csv')
    weather = pd.read_csv('../data/weather.csv')
    return vehicles, drivers, telematics, claims, weather

def preprocess_data():
    vehicles, drivers, telematics, claims, weather = load_data()

    # Convert date columns
    telematics['date'] = pd.to_datetime(telematics['date'])
    claims['date'] = pd.to_datetime(claims['date'])
    weather['date'] = pd.to_datetime(weather['date'])

    # Merge datasets
    merged = pd.merge(telematics, claims, on=['vehicle_id', 'date'], how='left')
    merged = pd.merge(merged, weather, on='date', how='left')
    merged = pd.merge(merged, vehicles, on='vehicle_id', how='left')
    # Assuming driver_id exists in vehicles for merging drivers
    if 'driver_id' in vehicles.columns:
        merged = pd.merge(merged, drivers, on='driver_id', how='left')
    else:
        # If not, join drivers based on vehicle_id for this example
        merged = pd.merge(merged, drivers, left_on='vehicle_id', right_on='driver_id', how='left')

    merged.fillna(0, inplace=True)

    os.makedirs('../data', exist_ok=True)
    merged.to_csv('../data/merged_data.csv', index=False)
    return merged

if __name__ == '__main__':
    preprocess_data()
