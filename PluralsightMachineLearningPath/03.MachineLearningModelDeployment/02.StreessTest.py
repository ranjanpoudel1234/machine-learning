import os  # standard library utilities for file checks
import time  # timing utilities for performance measurement
import joblib  # model persistence for scikit-learn pipelines
import psutil  # system/process utilities for CPU affinity
import pandas as pd  # data loading and DataFrame operations
import numpy as np  # numerical utilities and NaN handling

from sklearn.model_selection import train_test_split  # split data into train/test sets

# 1. Reload data
df = pd.read_csv(  # load the Adult dataset from the UCI repository
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",  # remote CSV URL
    header=None,  # file has no header row
    names=[  # assign column names to the dataset
        "age", "workclass", "fnlwgt", "education", "education-num",  # demographic + education fields
        "marital-status", "occupation", "relationship", "race", "sex",  # categorical attributes
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"  # financial + target
    ]  # end of column names list
)  # finish reading CSV into a DataFrame

# Clean and preprocess just like before
df.replace(" ?", np.nan, inplace=True)  # treat missing value marker as NaN
df.dropna(inplace=True)  # remove rows with any missing values

X = df.drop("income", axis=1)  # feature matrix without the target column
y = df["income"].apply(lambda x: x.strip() == ">50K")  # boolean target from income label

X_train, X_test, y_train, y_test = train_test_split(  # split data for training and testing
    X, y, stratify=y, test_size=0.2, random_state=42  # preserve class balance and set split size/seed
)  # end train/test split

# 2. Load previously saved model
model_file = "MLPClassifier.joblib"  # or use "LogisticRegression.joblib"
if not os.path.exists(model_file):  # guard against missing model file
    print(f"Error: {model_file} not found. Run training script first.")  # user-facing error message
    exit(1)  # terminate with a non-zero exit code

pipeline = joblib.load(model_file)  # load the saved preprocessing+model pipeline

# 3. Define test sample (single row, same structure)
sample = X_test.iloc[[0]]  # preserves DataFrame shape

# 4. Print available CPUs
cpu_list = psutil.cpu_count(logical=True)  # get number of logical CPU cores
print(f"\nAvailable logical CPUs: {cpu_list}")  # display CPU count
print("Pinning to a single core for stress test...\n")  # describe the test setup

# 5. Pin to a single CPU core
p = psutil.Process()  # get handle to current process
original_affinity = p.cpu_affinity()  # store the existing CPU affinity
p.cpu_affinity([0])  # Pin to CPU core 0

# 6. Warmup + timing
print("Running 1000 inferences on single CPU core...\n")  # announce the benchmark run
start_time = time.perf_counter()  # capture high-resolution start time
for _ in range(1000):  # run a fixed number of inferences
    _ = pipeline.predict(sample)  # perform prediction and discard output
elapsed = time.perf_counter() - start_time  # compute total elapsed seconds
latency_ms = (elapsed / 1000) * 1000  # compute average latency per inference in ms

# 7. Restore original CPU affinity
p.cpu_affinity(original_affinity)  # restore the process to its original CPU set

# 8. Output results
print("===== Latency Results =====")  # header for results
print(f"Model: {model_file}")  # show the model file used
print(f"Total time for 1000 inferences (1 core): {elapsed:.3f} seconds")  # total runtime
print(f"Avg latency per inference: {latency_ms:.3f} ms")  # average latency
print("===========================\n")  # footer for results

