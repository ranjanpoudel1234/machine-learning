# -----------------------------------------------------------------------------
# Step 1: Import Libraries
# -----------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport
from datetime import datetime
import os

# -----------------------------------------------------------------------------
# Step 2: Load Data
# -----------------------------------------------------------------------------
def load_data():
    # Load Titanic dataset
    df = sns.load_dataset("titanic")
    return df

# -----------------------------------------------------------------------------
# Step 3: Clean Data
# -----------------------------------------------------------------------------
def clean_data(df):
    df = df.dropna(subset=["embarked"]).copy()
    df.loc[:, "age"] = df["age"].fillna(df["age"].median())
    df.loc[:, "embark_town"] = df["embark_town"].fillna("Unknown")
    return df


# -----------------------------------------------------------------------------
# Step 4: Feature Engineering
# -----------------------------------------------------------------------------
def engineer_features(df):
    # Create new feature: age group
    df["age_group"] = pd.cut(df["age"], bins=[0, 12, 18, 35, 60, 120], 
                             labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])
    # Encode 'sex' as binary
    df["sex_encoded"] = df["sex"].map({"male": 0, "female": 1})
    return df

# -----------------------------------------------------------------------------
# Step 5: Validate Data
# -----------------------------------------------------------------------------
def validate_data(df):
    # Create a profiling report for manual review
    profile = ProfileReport(df, title="Titanic Data Report", explorative=True)
    profile.to_file("titanic_data_profile.html")

# -----------------------------------------------------------------------------
# Step 6: Export Cleaned Data
# -----------------------------------------------------------------------------
def export_data(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("output", exist_ok=True)
    df.to_csv(f"output/titanic_cleaned_{timestamp}.csv", index=False)

# -----------------------------------------------------------------------------
# Step 7: Main Function
# -----------------------------------------------------------------------------
def main():
    df = load_data()
    df = clean_data(df)
    df = engineer_features(df)
    validate_data(df)
    export_data(df)

if __name__ == "__main__":
    main()