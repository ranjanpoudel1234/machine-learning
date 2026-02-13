import joblib ## for rehydrating trained pipeline
import pandas as pd ## fetch same dataset we trained on to get column names and dtypes for ONNX conversion
from skl2onnx import convert_sklearn ## handle actual export
from skl2onnx.common.data_types import StringTensorType, FloatTensorType

# Load training data to get column names and dtypes
## Even though model has already been built and saved, we need to load the same data to get the column names
#  and dtypes for ONNX conversion. This is because ONNX needs to know the input schema (column names and types) to properly convert the model.
df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
    header=None,
    names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
    ]
)
df.dropna(inplace=True) ## drop missing rows
X = df.drop("income", axis=1) ## isolate feature metrix X by removing income label column.
# We only need the feature matrix to get the column names and dtypes for ONNX conversion. 
# The target variable (income) is not needed for this step.

# Construct initial_types using column names and types
# ONNX expects you to define shape and type of every input feature, so we build initialType list, one entry per column
initial_types = []

for col in X.columns:
    if X[col].dtype == object:
        initial_types.append((col, StringTensorType([None, 1]))) ## These types are required because the converter needs to know
        ## what type of ONNX compatible operations to generate for each part of the pipeline
        ## especially for things like one-hot encoding
        # Similar to how we handle columns during training in previous module
    else:
        initial_types.append((col, FloatTensorType([None, 1])))

# Load fitted pipeline | Use file names of models trained in Module 1
pipe = joblib.load("LogisticRegression.joblib")

# Convert pipeline to ONNX using column-aware initial_types. It also applies preprocessing steps like one-hot encoding and scaling as part of the conversion, 
# so we don't have to worry about those separately.
# ONNX single conversion function can handle entire pipeline, so we just pass in the whole thing and it will convert all steps at once.
onnx_model = convert_sklearn(pipe, initial_types=initial_types)

# Save to file
## This will create a file called logreg.onnx in the current directory,
#  which contains the ONNX representation of our trained pipeline.
## It contains everything, no additional logic needed at the inference time
with open("logreg.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("ONNX model exported successfully to logreg.onnx")

