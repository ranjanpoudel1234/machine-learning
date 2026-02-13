from memory_profiler import memory_usage  # measure memory usage of a function call
import joblib  # load persisted scikit-learn models
import pandas as pd  # data loading and DataFrame operations

def main():  # entry point needed for multiprocessing on Windows
    # Reload the test dataset (same as Segment 1)
    df = pd.read_csv(  # load the Adult dataset from the UCI repository
        "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",  # remote CSV URL
        header=None,  # file has no header row
        names=[  # assign column names to the dataset
            "age", "workclass", "fnlwgt", "education", "education-num",  # demographic + education fields
            "marital-status", "occupation", "relationship", "race", "sex",  # categorical attributes
            "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"  # financial + target
        ]  # end of column names list
    )  # finish reading CSV into a DataFrame

    df.replace(" ?", pd.NA, inplace=True)  # treat missing value marker as NA
    df.dropna(inplace=True)  # remove rows with any missing values

    X = df.drop("income", axis=1)  # feature matrix without the target column
    X = X.reset_index(drop=True)  # Required for row slicing
    X = X.iloc[:2000]  # Use a subset for quicker profiling

    # Load all models
    models = {  # map labels to loaded model pipelines
        "LogReg": joblib.load("LogisticRegression.joblib"),  # load logistic regression pipeline
        "RandForest": joblib.load("RandomForest.joblib"),  # load random forest pipeline
        "MLP": joblib.load("MLPClassifier.joblib")  # load MLP pipeline
    }  # end model dictionary

    # Define prediction wrapper
    def profile_predict(model, X):  # wrapper used by memory_profiler
        return model.predict(X)  # run inference for memory measurement

    # Measure peak memory for each model
    mem_results = {}  # store peak memory per model
    for name, model in models.items():  # iterate through model labels and pipelines
        mem_usage = memory_usage((profile_predict, (model, X)), max_usage=True)  # capture peak MB
        mem_results[name] = round(mem_usage, 2)  # round for cleaner display

    # Display results
    print("\nPeak Memory Usage During Inference (MB):\n")  # header for output
    for name, mem in mem_results.items():  # print each model's peak memory
        print(f"{name:<10} {mem} MB")  # formatted row with label and memory


if __name__ == "__main__":  # ensure safe multiprocessing on Windows
    main()  # run the profiling workflow

