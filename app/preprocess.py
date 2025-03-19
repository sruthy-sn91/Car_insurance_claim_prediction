import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load saved encoders and scaler
encoder = pickle.load(open("models/encoder.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

def preprocess_input(data):
    df = pd.DataFrame([data])  # Convert input dictionary to DataFrame

    # Convert numerical values (use .iloc[0] to avoid FutureWarning)
    df['CREDIT_SCORE'] = float(df['CREDIT_SCORE'].iloc[0])
    df['ANNUAL_MILEAGE'] = float(df['ANNUAL_MILEAGE'].iloc[0])

    # Fix categorical value processing
    df['GENDER'] = df['GENDER'].str.lower().map({'male': 1, 'female': 0})
    df['VEHICLE_YEAR'] = df['VEHICLE_YEAR'].map({'after 2015': 1, 'before 2015': 0})
    df['VEHICLE_OWNERSHIP'] = df['VEHICLE_OWNERSHIP'].astype(int)
    df['MARRIED'] = df['MARRIED'].astype(int)

    # Encode categorical variables
    categorical_features = ['AGE', 'INCOME', 'EDUCATION', 'DRIVING_EXPERIENCE']
    encoded_cats = encoder.transform(df[categorical_features]).toarray()

    # Scale numerical features
    numerical_features = ['CREDIT_SCORE', 'ANNUAL_MILEAGE']
    scaled_numericals = scaler.transform(df[numerical_features])

    # Prepare final input data for the model
    processed_df = pd.concat([pd.DataFrame(scaled_numericals), pd.DataFrame(encoded_cats)], axis=1)
    
    return processed_df
