import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 1: Load the Titanic dataset
df = pd.read_csv("titanic.csv")

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
scaler = MinMaxScaler()
df['Fare_Normalized'] = scaler.fit_transform(df[['Fare']])

# Step 8: Standardize the 'Age' column to mean=0, std=1
standardizer = StandardScaler()
df['Age_Standardized'] = standardizer.fit_transform(df[['Age']])

# Step 9: Print cleaned dataset summary
print("\nPost-cleaning dataset shape:", df.shape)
print(df[['Age', 'Fare', 'Fare_Normalized', 'Age_Standardized']].head())

# Step 10: Optionally save the cleaned dataset
df.to_csv("./Module1_Clip3/titanic_cleaned.csv", index=False)