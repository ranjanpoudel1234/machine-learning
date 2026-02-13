# =============================================================================
# IMPORTS: Libraries needed for data processing, modeling, and benchmarking
# =============================================================================

import pandas as pd          # Data manipulation and analysis
import joblib                # Saving/loading trained models to/from disk
import os                    # File system operations (getting file sizes)
import time                  # High-precision timing for performance benchmarking
import numpy as np           # Numerical operations and handling NaN values

# Scikit-learn imports for machine learning pipeline
from sklearn.compose import ColumnTransformer         # Apply different preprocessing to different columns
from sklearn.pipeline import make_pipeline            # Chain preprocessing and model into a single object
from sklearn.preprocessing import OneHotEncoder, StandardScaler  # Data transformation techniques.OneHotEncoder - Convert categorical text to binary columns
                                                                 # StandardScaler - Normalize numeric features (mean=0, std=1)
from sklearn.linear_model import LogisticRegression   # Linear model for binary classification
from sklearn.ensemble import RandomForestClassifier   # Ensemble of decision trees
from sklearn.neural_network import MLPClassifier      # Multi-layer Perceptron (neural network)
from sklearn.model_selection import train_test_split  # Split data into training and testing sets
from sklearn.metrics import accuracy_score            # Calculate model accuracy
from sklearn.exceptions import ConvergenceWarning     # Handle convergence warnings

# =============================================================================
# DATA LOADING: Load UCI Adult Income dataset from remote source
# =============================================================================
# Dataset: Predicts whether income exceeds $50K/year based on census data
# Size: ~30K rows (using full dataset)
# Note: For large datasets, download locally to avoid network latency
# Rule of thumb: Use 20x the number of model parameters for tabulated data
# This varies by model type, complexity, and number of features

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
    header=None,  # CSV has no header row, so we define column names manually
    names=[        # Explicitly name each column for clarity
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
    ]
)

# =============================================================================
# DATA CLEANING: Handle missing values
# =============================================================================
# The dataset uses " ?" (space + question mark) to represent missing values
df.replace(" ?", np.nan, inplace=True)  # Convert " ?" strings to proper NaN values
df.dropna(inplace=True)                 # Remove all rows with any missing values
                                         # Note: This is simple but may lose data; 
                                         # consider imputation for production

# =============================================================================
# FEATURE AND TARGET SEPARATION
# =============================================================================
# X = Features (input variables used to make predictions)
# y = Target (output variable we want to predict)

X = df.drop("income", axis=1)  # All columns EXCEPT income = our features

# Convert income from string (" <=50K" or " >50K") to boolean (True/False)
# strip() removes leading/trailing whitespace
# This creates a BINARY CLASSIFICATION problem:
#   True (1) = income > $50K
#   False (0) = income <= $50K
# Note: The comment mentions "one hot" but this is actually BINARIZATION
# One-hot encoding is different (used later for categorical features)
y = df["income"].apply(lambda x: x.strip() == ">50K")

# =============================================================================
# IDENTIFY COLUMN TYPES: Separate categorical from numerical features
# =============================================================================
# Different feature types require different preprocessing strategies

# Categorical columns: stored as "object" dtype in pandas (strings)
# Examples: "workclass", "education", "occupation", "sex"
cat_cols = X.select_dtypes(include="object").columns.tolist()

# Numerical columns: int64, float64, etc.
# Examples: "age", "education-num", "hours-per-week"
## WATCH THE EXCLUDE = OBJECT HERE. THAT IS THE DIFFERENCE WITH CATEGORICAL COLUMNS VS NUMERICAL
num_cols = X.select_dtypes(exclude="object").columns.tolist()

# =============================================================================
# TRAIN/TEST SPLIT: Divide data into training and testing sets
# =============================================================================
# 80% training, 20% testing (test_size=0.2)
# stratify=y ensures both sets have the same proportion of True/False labels
# random_state=42 makes the split reproducible (same split every time)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# =============================================================================
# PREPROCESSING PIPELINE: Transform features for machine learning
# =============================================================================
# ColumnTransformer applies different transformations to different columns
# NOTE: This is data preprocessing, NOT a Transformer ML model (like BERT/GPT)

preprocessor = ColumnTransformer([
    # ONE-HOT ENCODING for categorical features: Binarizing
    # Converts categories into binary columns (e.g., "Male"/"Female" → [1,0] or [0,1])
    # handle_unknown="ignore" prevents errors if test data has new categories
    ("onehot", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    
    # STANDARD SCALING for numerical features: Normalizing
    # Centers data to mean=0 and scales to std=1
    # Formula: (x - mean) / std_dev
    # This prevents features with large values from dominating the model
    ("scale", StandardScaler(), num_cols)
])

# =============================================================================
# MODEL DEFINITIONS: Three different algorithms to compare
# =============================================================================
# Goal: Compare trade-offs between speed, model size, and accuracy
# These hyperparameters favor speed and reliability over maximum accuracy
# Feel free to experiment with different settings!

models = {
    # LOGISTIC REGRESSION: Fast, interpretable, linear model
    # max_iter=2000: Maximum training iterations
    # solver="lbfgs": Optimization algorithm (good for small-medium datasets)
    # n_jobs=-1: Use all CPU cores for parallel processing
    "LogisticRegression": LogisticRegression(max_iter=2000, solver="lbfgs", n_jobs=-1),
    
    # RANDOM FOREST: Ensemble of 200 decision trees
    # n_estimators=200: Number of trees in the forest
    # More trees = better accuracy but slower inference and larger model
    # n_jobs=-1: Train trees in parallel using all CPU cores
    "RandomForest": RandomForestClassifier(n_estimators=200, n_jobs=-1),
    
    # NEURAL NETWORK (Multi-Layer Perceptron): Non-linear, powerful but complex
    # hidden_layer_sizes=(128, 64): 2 hidden layers with 128 and 64 neurons
    # max_iter=400: Maximum training epochs
    "MLPClassifier": MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=400)
}

# Dictionary to store benchmark results for each model
results = {}

# =============================================================================
# TRAINING AND BENCHMARKING LOOP: Train each model and measure performance
# =============================================================================
for name, model in models.items():
    # Create a PIPELINE: chains preprocessing + model into a single object
    # Benefits: 
    # 1. Prevents data leakage (test data never sees training statistics)
    # 2. Simpler deployment (one object instead of two)
    # 3. Automatic transformation during prediction
    pipeline = make_pipeline(preprocessor, model)

    # BENCHMARK 1: TRAINING TIME
    # time.perf_counter() provides high-precision timing
    # Helps to gain insight into compute cost during retraining
    start_time = time.perf_counter()
    pipeline.fit(X_train, y_train)  # Train the model on training data
    fit_time = time.perf_counter() - start_time  # Calculate elapsed time in seconds

    # BENCHMARK 2: MODEL SIZE ON DISK
    # Saved models need to be loaded into memory during deployment
    # Larger models = more memory consumption and slower loading times
    # Simulates storing model in registry or moving into deployment
    filename = f"{name}.joblib"            # Create filename: LogisticRegression.joblib, etc.
    joblib.dump(pipeline, filename)        # Serialize and save entire pipeline to disk
    model_size_kb = os.path.getsize(filename) / 1024  # Get file size and convert bytes to KB

    # BENCHMARK 3: INFERENCE LATENCY (PREDICTION SPEED)
    # Latency = time to make a single prediction (critical for real-time systems)
    # Measure by running 1000 predictions and averaging. Predicting single row a thousand times
    # Simulates API request receiving individual requests in real time
    start_time = time.perf_counter()
    for _ in range(1000):
        # predict() expects 2D input (array of samples), so use double brackets
        # X_test.iloc[[0]] returns a DataFrame with 1 row (2D)
        # X_test.iloc[0] would return a Series (1D) and cause an error
        pipeline.predict(X_test.iloc[[0]]) ## Just one row!!!!!!
    # Calculate average time per prediction in milliseconds:
    # (total_time / 1000 predictions) * 1000 to convert seconds to milliseconds
    latency_ms = (time.perf_counter() - start_time) / 1000 * 1000


    # BENCHMARK 4: ACCURACY ON TEST SET
    # Measure how well the model generalizes to unseen data
    y_pred = pipeline.predict(X_test)  # Make predictions on entire test set
    acc = accuracy_score(y_test, y_pred)  # Compare predictions to true labels
    # Accuracy = (correct predictions) / (total predictions)

    # Store all benchmarks for this model
    results[name] = {
        "Train Time (s)": round(fit_time, 3),        # Rounded to 3 decimal places
        "Latency (ms)": round(latency_ms, 3),        # Rounded to 3 decimal places
        "Model Size (KB)": round(model_size_kb, 1),  # Rounded to 1 decimal place
        "Accuracy": round(acc * 100, 2)              # Convert to percentage, 2 decimals
    }

# =============================================================================
# DISPLAY RESULTS: Pretty-print benchmark comparison table
# =============================================================================
print("\nModel Benchmark Results:\n")

# Print header row with column alignment:
# {:<18} = left-aligned, width 18 characters
# {:>15} = right-aligned, width 15 characters
print("{:<18} {:>15} {:>15} {:>18} {:>12}".format(
    "Model", "Train Time (s)", "Latency (ms)", "Model Size (KB)", "Accuracy (%)"
))
print("-" * 80)  # Separator line

# Print each model's results in aligned columns
for model_name, stats in results.items():
    print("{:<18} {:>15} {:>15} {:>18} {:>12}".format(
        model_name,
        stats["Train Time (s)"],
        stats["Latency (ms)"],
        stats["Model Size (KB)"],
        stats["Accuracy"]
    ))

# =============================================================================
# KEY TAKEAWAYS FOR DEPLOYMENT:
# - Logistic Regression: Fastest inference, smallest size, good baseline, accuracy is usable
# - Random Forest: Good accuracy, larger model size. Slowest
# - MLP (Neural Net): Potentially highest accuracy, moderate speed, moderate size, most complex. Retraining cost and delay add up nightly
# MLP trails on accuracy because we are using one-hot structured data which is better for logistic and random forest
# # Choose based on your constraints: speed vs. accuracy vs. resource limits
# Model Benchmark Results:

# Model               Train Time (s)    Latency (ms)    Model Size (KB) Accuracy (%)
# --------------------------------------------------------------------------------
# LogisticRegression           0.231           5.157                7.1        84.75
# RandomForest                 6.998          51.237           134858.9         85.2
# MLPClassifier               84.237           4.479              698.3        82.15

# =============================================================================


