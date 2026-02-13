# 1. Import Libraries
import os
import pandas as pd
from ydata_profiling import ProfileReport

# 2. Load Dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'heart_cleveland_upload.csv')
df = pd.read_csv(csv_file)

# 3. Preview Data
print("=== HEAD ===")
print(df.head())
print("\n=== INFO ===")
print(df.info())
print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

# 4. Check for Missing Values and Duplicates
print("\n=== NULL VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATES ===")
print(df.duplicated().sum())

# 5. Handle Duplicates and Missing Values
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

# 6. Data Type Conversion for Label Column (if needed)
# Change 'target' to 'condition' based on actual dataset
if df['condition'].dtype != 'int64':
    df['condition'] = df['condition'].astype(int)

# 7. Generate Data Profile Report
profile = ProfileReport(df, title="Heart Disease Data Profile", explorative=True)
profile.to_file("heart_data_profile.html")

# 8. Export Cleaned Dataset
csv_output = os.path.join(script_dir, "validated_heart_data.csv")
json_output = os.path.join(script_dir, "validated_heart_data.json")

df.to_csv(csv_output, index=False)
df.to_json(json_output, orient="records", lines=True)

print("✅ Data validation complete. Files exported.")