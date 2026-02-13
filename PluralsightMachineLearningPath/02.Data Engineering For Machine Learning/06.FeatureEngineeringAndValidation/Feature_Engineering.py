# demo_heart_feature_engineering.py

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport

# -----------------------------------------------------------------------------
# STEP 1: Load the Dataset
# -----------------------------------------------------------------------------


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "heart.csv")

df = pd.read_csv(csv_file)
print("Dataset shape:", df.shape)
print(df.head())

# -----------------------------------------------------------------------------
# STEP 2: Check and Handle Missing Values (if any)
# -----------------------------------------------------------------------------

print("\nMissing values:\n", df.isnull().sum())

# -----------------------------------------------------------------------------
# STEP 3: Encode a Binary Categorical Feature
# -----------------------------------------------------------------------------

df['Sex'] = df['Sex'].map({0: 'Female', 1: 'Male'})  # Temporarily make it categorical. This is on purpose wrong to demonstrate, should use M and F value
df['Sex_encoded'] = df['Sex'].map({'Female': 0, 'Male': 1})  # Re-encode manually

print("\nEncoded 'Sex' column preview:\n", df[['Sex', 'Sex_encoded']].head())

# -----------------------------------------------------------------------------
# STEP 4: Feature Creation - BMI-like Feature
# -----------------------------------------------------------------------------

df['chol_age_ratio'] = df['Cholesterol'] / (df['Age'] + 1)  # avoid division by zero

print("\nNew feature 'chol_age_ratio' preview:\n", df[['Cholesterol', 'Age', 'chol_age_ratio']].head())

# -----------------------------------------------------------------------------
# STEP 5: Normalize Numerical Features. Really useful for algorithms sensitive to feature scales like Logistic Regression, SVM, and KNN.
# -----------------------------------------------------------------------------

scaler = StandardScaler()
df[['RestingBP_scaled', 'chol_age_ratio_scaled']] = scaler.fit_transform(df[['RestingBP', 'chol_age_ratio']])

print("\nScaled features preview:\n", df[['RestingBP', 'RestingBP_scaled', 'chol_age_ratio_scaled']].head())

# -----------------------------------------------------------------------------
# STEP 6: Validate with Profiling
# -----------------------------------------------------------------------------


profile = ProfileReport(df, title="Heart Disease Feature Engineering Report", explorative=True)
profile.to_file("heart_feature_engineering_report.html")

print("\n✅ Profiling report saved: 'heart_feature_engineering_report.html'")
