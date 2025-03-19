import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE

import os
os.makedirs("models", exist_ok=True)  # Ensure models directory exists

# Load dataset
df = pd.read_csv('data/Car_Insurance_Claim.csv')

# Handling missing values
imputer = SimpleImputer(strategy='median')
df[['CREDIT_SCORE', 'ANNUAL_MILEAGE']] = imputer.fit_transform(df[['CREDIT_SCORE', 'ANNUAL_MILEAGE']])

# Handling skewness
df['CREDIT_SCORE'] = np.log1p(df['CREDIT_SCORE'])
df['ANNUAL_MILEAGE'] = np.log1p(df['ANNUAL_MILEAGE'])

# Handling outliers
from scipy import stats
z_scores = np.abs(stats.zscore(df[['CREDIT_SCORE', 'ANNUAL_MILEAGE']]))
df = df[(z_scores < 3).all(axis=1)]

# Convert appropriate columns to numerical types after imputation
df['AGE'] = df['AGE'].astype(str)  # Keep as categorical for encoding
df['CREDIT_SCORE'] = df['CREDIT_SCORE'].astype(float)
df['ANNUAL_MILEAGE'] = df['ANNUAL_MILEAGE'].astype(float)
df['VEHICLE_OWNERSHIP'] = df['VEHICLE_OWNERSHIP'].astype(int)
df['MARRIED'] = df['MARRIED'].astype(int)
df['OUTCOME'] = df['OUTCOME'].astype(int)

# Encoding categorical variables including AGE
categorical_features = ['AGE', 'INCOME', 'EDUCATION', 'DRIVING_EXPERIENCE']
encoder = OneHotEncoder(drop='first', handle_unknown='ignore')
encoded_cats = encoder.fit_transform(df[categorical_features]).toarray()
# Save encoder for preprocessing input data in API
pickle.dump(encoder, open("models/encoder.pkl", "wb"))

# Scaling numerical features
scaler = StandardScaler()
numerical_features = ['CREDIT_SCORE', 'ANNUAL_MILEAGE']
scaled_numericals = scaler.fit_transform(df[numerical_features])

# Save scaler for later use
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

# Prepare final dataset
X = pd.concat([pd.DataFrame(scaled_numericals), pd.DataFrame(encoded_cats)], axis=1)
y = df['OUTCOME']


# Handle class imbalance using SMOTE
smote = SMOTE(sampling_strategy=0.5, random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_resampled, y_resampled)

# Save model
pickle.dump(model, open("models/model.pkl", "wb"))

