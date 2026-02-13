# Module 2, Clip 3: Feature Engineering

This module demonstrates advanced feature engineering techniques for machine learning datasets, including encoding, feature creation, and normalization.

## Files

- `Feature_Engineering.py`: Main feature engineering script
- `heart.csv`: Heart disease dataset for analysis
- `heart_feature_engineering_report.html`: Generated feature engineering report

## What You'll Learn

- Categorical feature encoding techniques
- Feature creation and engineering strategies
- Data normalization and scaling methods
- Feature validation and profiling
- Advanced preprocessing for ML models

## Key Concepts

### Categorical Encoding
- **Binary Encoding**: Converting categorical variables to numeric
- **Manual Encoding**: Custom mapping for binary categories
- **Encoding Strategy**: Choosing appropriate encoding methods

### Feature Creation
- **Derived Features**: Creating new features from existing ones
- **Ratio Features**: Building meaningful ratios and relationships
- **Domain Knowledge**: Incorporating medical domain expertise

### Data Scaling
- **Standardization**: Z-score normalization for ML algorithms
- **Feature Scaling**: Preparing features for machine learning models
- **Scale Preservation**: Maintaining interpretability while scaling

## Usage

```bash
python Feature_Engineering.py
```

## Feature Engineering Pipeline

1. **Data Loading**: Import heart disease dataset
2. **Missing Value Analysis**: Check for data quality issues
3. **Categorical Encoding**: Convert Sex to binary numeric format
4. **Feature Creation**: Build cholesterol-age ratio feature
5. **Data Scaling**: Standardize features for ML algorithms
6. **Validation**: Generate comprehensive feature report

## Feature Engineering Techniques

### Binary Categorical Encoding
```python
# Convert categorical to numeric
df['Sex_encoded'] = df['Sex'].map({'Female': 0, 'Male': 1})
```

### Feature Creation
```python
# Create ratio feature
df['chol_age_ratio'] = df['Cholesterol'] / (df['Age'] + 1)
```

### Feature Scaling
```python
# Standardize features
scaler = StandardScaler()
df[['RestingBP_scaled', 'chol_age_ratio_scaled']] = scaler.fit_transform(df[['RestingBP', 'chol_age_ratio']])
```

## Dataset Information

The heart disease dataset contains:
- **Demographic Features**: Age, Sex
- **Medical Features**: RestingBP, Cholesterol, etc.
- **Target Variable**: Heart disease presence/absence

## Feature Engineering Benefits

- **Improved Model Performance**: Better feature representation
- **Domain Knowledge Integration**: Medical expertise in features
- **Scalability**: Features ready for ML algorithms
- **Interpretability**: Meaningful feature relationships

## Dependencies

- `pandas`: Data manipulation
- `numpy`: Numerical operations
- `scikit-learn`: Preprocessing tools
- `ydata_profiling`: Feature validation

## Learning Outcomes

After completing this module, you'll understand:
- How to encode categorical variables
- Feature creation strategies
- Data scaling and normalization
- Feature validation techniques
- Best practices for ML feature engineering
- Domain-specific feature engineering approaches
