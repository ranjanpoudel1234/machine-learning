import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import os

# Step 1: Load the Titanic dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'titanic.csv')
df = pd.read_csv(csv_file)

# Step 2: Preview the raw data
print("Initial dataset shape:", df.shape)
print(df.head())

# Step 3: Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 4: Fill missing 'Age' values with the median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Step 5: Drop rows with missing 'Embarked' values
df.dropna(subset=['Embarked'], inplace=True)

# Step 6: Drop any duplicate rows
df.drop_duplicates(inplace=True)

# Step 7: Normalize the 'Fare' column to a [0, 1] scale
# Example: If fare prices range from $0 to $500:

# A $0 fare → 0.0
# A $250 fare → 0.5
# A $500 fare → 1.0
# This normalization helps machine learning models that are sensitive to feature scales (like neural networks or distance-based algorithms).
# good when you need bounded values
scaler = MinMaxScaler()
df['Fare_Normalized'] = scaler.fit_transform(df[['Fare']])

# Step 8: Standardize the 'Age' column to mean=0, std=1
# fit_transform(): Calculates the mean and std from Age, then applies the transformation
# Example: If ages have mean=30 and std=10:

# Age 30 → 0.0 (exactly at the mean)
# Age 40 → 1.0 (one std above mean)
# Age 20 → -1.0 (one std below mean)
# Age 50 → 2.0 (two std above mean)
# good for algorithms assuming normally distributed data (like linear regression, logistic regression, supported vector machines)
standardizer = StandardScaler()
df['Age_Standardized'] = standardizer.fit_transform(df[['Age']])

# Step 9: Print cleaned dataset summary
print("\nPost-cleaning dataset shape:", df.shape)
print(df[['Age', 'Fare', 'Fare_Normalized', 'Age_Standardized']].head())

# Step 10: Optionally save the cleaned dataset
df.to_csv(os.path.join(script_dir, "titanic_cleaned.csv"), index=False)