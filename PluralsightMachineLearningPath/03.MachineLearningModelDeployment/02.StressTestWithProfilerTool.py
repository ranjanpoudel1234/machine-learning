import cProfile  # built-in profiler for CPU time measurement
import pstats  # profiler stats formatting utilities
import io  # in-memory text buffer for stats output
import joblib  # load persisted scikit-learn models
import pandas as pd  # data loading and DataFrame operations

# Reload test data (same as before)
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
X = X.reset_index(drop=True)  # reset index for stable slicing
X = X.iloc[:2000]  # Limit for consistent runtime

# Load MLP model pipeline
mlp_model = joblib.load("MLPClassifier.joblib")  # load the saved MLP pipeline

# Set up profiler
profiler = cProfile.Profile()  # create a profiler instance
profiler.enable()  # start collecting profile data

# Run prediction
_ = mlp_model.predict(X)  # execute inference to profile CPU hotspots

# Stop profiler
profiler.disable()  # stop profiling

# Output stats
s = io.StringIO()  # buffer for formatted stats output
stats = pstats.Stats(profiler, stream=s).sort_stats("cumtime")  # Cumulative time
stats.print_stats(15)  # Top 15 functions
print("\n=== CPU Hotspot Report ===\n")  # header for profiler report
print(s.getvalue())  # display the captured stats

