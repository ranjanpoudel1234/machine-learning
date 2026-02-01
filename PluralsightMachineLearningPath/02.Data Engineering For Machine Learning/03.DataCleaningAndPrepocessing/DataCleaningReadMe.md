# Module 1, Clip 3: Data Cleansing

This module demonstrates essential data cleansing and preprocessing techniques for machine learning datasets.

## Files

- `cleansing.py`: Main data cleansing script
- `titanic.csv`: Original Titanic dataset (downloaded from GitHub)
- `titanic_cleaned.csv`: Processed and cleaned dataset

## What You'll Learn

- Identifying and handling missing values
- Removing duplicate records
- Data normalization and standardization
- Feature scaling techniques
- Data quality improvement strategies

## Key Concepts

### Missing Value Handling
- **Median Imputation**: Filling missing age values with median
- **Row Removal**: Dropping rows with missing critical data (Embarked)
- **Strategic Decisions**: Choosing appropriate imputation strategies

### Data Quality Improvements
- **Duplicate Removal**: Eliminating duplicate records
- **Data Normalization**: MinMax scaling to [0,1] range
- **Standardization**: Z-score normalization (mean=0, std=1)

### Feature Engineering
- Creating normalized versions of existing features
- Maintaining original data while adding processed versions
- Understanding when to use different scaling methods

## Usage

```bash
python cleansing.py
```

## Data Processing Pipeline

1. **Load Data**: Import Titanic dataset from GitHub
2. **Inspect Data**: Check for missing values and duplicates
3. **Handle Missing Values**: 
   - Fill Age with median
   - Drop rows missing Embarked
4. **Remove Duplicates**: Clean duplicate records
5. **Feature Scaling**:
   - Normalize Fare to [0,1] range
   - Standardize Age to mean=0, std=1
6. **Export Results**: Save cleaned dataset

## Scaling Techniques Demonstrated

### MinMax Scaling
```python
scaler = MinMaxScaler()
df['Fare_Normalized'] = scaler.fit_transform(df[['Fare']])
```

### Standard Scaling
```python
standardizer = StandardScaler()
df['Age_Standardized'] = standardizer.fit_transform(df[['Age']])
```

## Dependencies

- `pandas`: Data manipulation
- `scikit-learn`: Preprocessing tools (MinMaxScaler, StandardScaler)

## Learning Outcomes

After completing this module, you'll understand:
- How to identify data quality issues
- Different strategies for handling missing values
- When to use normalization vs standardization
- Best practices for data preprocessing
- How to maintain data integrity during cleaning