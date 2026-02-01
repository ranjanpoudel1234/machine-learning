# Data Engineering for Machine Learning

## Introduction

1. Data Collection: Gather from API, logs, databases etc
2. Cleaning: Remove duplicate, inconsistent, or irrelevant data points.
3. Preprocessing:is to transform raw data into an understandable format for the model. Example, handling missing values, normalization, encoding categorical variables.
4. Validation: Ensure data quality and integrity by checking for errors, data types and ranges
5. **80 Percent of ML work is Data Engineering as that is the foundation of the how model will perform**

## Pandas

Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like DataFrames and Series that make it easy to handle and analyze structured data. Helps in data cleaning, transformation, and exploration.

## Numpy

NumPy is a fundamental library for numerical computing in Python. It provides support for arrays, matrices, and a wide range of mathematical functions to operate on these data structures efficiently. In machine learnings, NumPy is used for numerical operations, linear algebra, and handling large datasets to capture numerical features

## Ydata-profiling

Ydata-profiling is a Python library that generates detailed reports from a pandas DataFrame. It provides insights into the data, including distributions, correlations, missing values, and summary statistics. This helps in understanding the dataset and identifying potential issues before building machine learning models.

## Importance of Data Cleaning And Preprocessing

![alt text](whyDataCleanAndPreprocessMatters.png)

1. Missing values: Handle missing data by imputation or removal to prevent bias.
2. Duplicates: Remove duplicate records to avoid skewed analysis.
3. Normalization: Scale features to a common range for better model performance.

Domain knowledge and understanding of the data is crucial for effective cleaning and preprocessing. For example, if weather value is missing, instead of using global average, it might be better to use mean of that region. If there are outliers, for example, spike in sensor reading, that spike might be important outlier to consider.

Categorical groupings: For example, in a dataset with job titles, grouping similar titles (e.g., "Software Engineer" and "Developer") can help reduce dimensionality and improve model performance.