import pandas as pd

def engineer_features():
    data = pd.read_csv('../data/merged_data.csv')

    # Create lagged claims
    data['lagged_claims'] = data.groupby('vehicle_id')['claim_made'].shift(1)

    # Create rolling averages for telematics metrics
    data['avg_speed_rolling'] = data.groupby('vehicle_id')['avg_speed'].rolling(3).mean().reset_index(0, drop=True)
    data['harsh_braking_rolling'] = data.groupby('vehicle_id')['harsh_braking'].rolling(3).mean().reset_index(0, drop=True)

    # Calculate driver risk score (example formula)
    if 'age' in data.columns and 'accidents' in data.columns and 'experience' in data.columns:
        data['driver_risk_score'] = (data['age'] / 100) + (data['accidents'] * 0.2) - (data['experience'] / 50)
    else:
        data['driver_risk_score'] = 0

    data.fillna(0, inplace=True)
    data.to_csv('../data/engineered_data.csv', index=False)
    return data

if __name__ == '__main__':
    engineer_features()
