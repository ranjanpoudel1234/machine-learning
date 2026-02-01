# Import pandas library
import pandas as pd
import os

# Step 1: Load the CSV file into a DataFrame
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'HRIS.csv')
dataFrame = pd.read_csv(csv_file)

# Step 2: Display the first few rows of the DataFrame
print(dataFrame.head())

# Step 3: Display basic information about the DataFrame
print(dataFrame.info())

# Step 4: Display summary statistics
print(dataFrame.describe())