import pandas as pd
from ydata_profiling import ProfileReport

# Load sample CSV data
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Basic inspection
print(df.head()) ## first 5 rows of the dataset, quick peek

# Full data profiling
## helps to catch collinearity, missing values, distributions, etc.
profile = ProfileReport(df, title="Data Profile Report", explorative=True)
profile.to_file("data_profile_report.html")