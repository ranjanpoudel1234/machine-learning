import time
import joblib

models = {
    "Logistic Regression": "LogisticRegression.joblib",
    "Random Forest": "RandomForest.joblib",
    "MLP Classifier": "MLPClassifier.joblib"
}

## Logistic Regression took much longer even though its small
## because logistic regression was not cached on the disk as others were in this instance
## call accross networks can make this worse
print("\n=== Cold-Start Deserialization Times ===\n")
for name, path in models.items():
    start = time.perf_counter()
    _ = joblib.load(path)
    duration = time.perf_counter() - start
    print(f"{name:<20}: {duration:.4f} seconds")