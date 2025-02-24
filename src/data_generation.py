import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_vehicle_data():
    vehicles = pd.DataFrame({
        'vehicle_id': range(1, 101),
        'vehicle_type': np.random.choice(['car', 'van', 'truck'], 100),
        'vehicle_age': np.random.randint(1, 10, 100),
        'mileage': np.random.randint(10000, 100000, 100)
    })
    return vehicles

def generate_driver_data():
    drivers = pd.DataFrame({
        'driver_id': range(1, 101),
        'age': np.random.randint(25, 65, 100),
        'experience': np.random.randint(1, 40, 100),
        'accidents': np.random.randint(0, 3, 100)
    })
    return drivers

def generate_telematics_data():
    dates = pd.date_range(start='2021-01-01', end='2022-12-31', freq='M')
    telematics = []
    for vehicle_id in range(1, 101):
        for date in dates:
            telematics.append({
                'vehicle_id': vehicle_id,
                'date': date,
                'avg_speed': np.random.uniform(30, 70),
                'harsh_braking': np.random.randint(0, 5),
                'acceleration': np.random.uniform(0, 1)
            })
    return pd.DataFrame(telematics)

def generate_claims_data():
    dates = pd.date_range(start='2021-01-01', end='2022-12-31', freq='M')
    claims = []
    for vehicle_id in range(1, 101):
        for date in dates:
            claim_flag = np.random.choice([0, 1], p=[0.95, 0.05])
            claims.append({
                'vehicle_id': vehicle_id,
                'date': date,
                'claim_made': claim_flag,
                'claim_cost': np.random.randint(1000, 5000) if claim_flag == 1 else 0
            })
    return pd.DataFrame(claims)

def generate_weather_data():
    dates = pd.date_range(start='2021-01-01', end='2022-12-31', freq='M')
    weather = pd.DataFrame({
        'date': dates,
        'temperature': np.random.uniform(0, 30, len(dates)),
        'precipitation': np.random.uniform(0, 10, len(dates))
    })
    return weather

def save_datasets():
    vehicles = generate_vehicle_data()
    drivers = generate_driver_data()
    telematics = generate_telematics_data()
    claims = generate_claims_data()
    weather = generate_weather_data()

    os.makedirs('../data', exist_ok=True)
    vehicles.to_csv('../data/vehicles.csv', index=False)
    drivers.to_csv('../data/drivers.csv', index=False)
    telematics.to_csv('../data/telematics.csv', index=False)
    claims.to_csv('../data/claims.csv', index=False)
    weather.to_csv('../data/weather.csv', index=False)

if __name__ == '__main__':
    save_datasets()
