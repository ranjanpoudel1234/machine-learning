# Types of Machine Learning Models

## Logistic Regression

Logistic regression is a type of regression analysis used for predicting the outcome of a categorical dependent variable based on one or more predictor variables. It is commonly used for binary classification problems. It does not do well with images or complex non-linear relationships. Example, predicting house price based on number of bedrooms, location etc

## Decision Trees

Decision trees are a type of supervised learning algorithm used for both classification and regression tasks. They work by splitting the data into subsets based on the value of input features, creating a tree-like model of decisions. Decision trees are easy to interpret and visualize but can be prone to overfitting.  

Eg, Diagnosing patient disease based on symptoms. Do not do well with images.

## Random Forest

Random forests are an ensemble learning method that combines multiple decision trees to improve predictive performance and reduce overfitting. Each tree is trained on a random subset of the data, and the final prediction is made by aggregating the predictions of all trees. Random forests are robust and can handle large datasets with high dimensionality.


Eg, Diagnosing patient disease based on symptoms.

Do not do well with images.

## Gradient Boosting

Gradient boosting is an ensemble learning technique that builds models sequentially, with each new model attempting to correct the errors of the previous ones. It is highly effective for both classification and regression tasks and can handle complex non-linear relationships. However, it can be prone to overfitting if not properly tuned.

 Example of gradient boosting algorithms include XGBoost, LightGBM, and CatBoost.  
 
 Eg, Diagnosing patient disease based on symptoms. Do not do well with images.

## Support Vector Machines

Support Vector Machines (SVMs) are a type of supervised learning algorithm used for classification and regression tasks. They work by finding the hyperplane that best separates the data into different classes. SVMs are effective in high-dimensional spaces and are particularly useful for text classification and image recognition tasks. However, they can be less effective on very large datasets and may require careful tuning of parameters.

Often used for text classification like filtering spams or not. This is a black box model - not human readable

## Small Neural Nets (MLP)

Small neural networks are a type of artificial neural network with a relatively small number of layers and neurons. They are suitable for simple tasks and small datasets. Small neural networks are easier to train and interpret compared to deep neural networks but may not perform well on complex tasks such as image recognition or natural language processing.

They can be used with tabulated data, text and images! but not exceptionally well suited to any of the three.

Good for handwriting and speech recognition.

## Large Neural Nets(Transformers/CNNs)

- Broadly used for image and video recognition, natural language processing, and other complex tasks.
- Great for image classification, autonomous vehicles, and natural language processing.
- Transformers are a type of large neural network architecture that have revolutionized natural language processing and are increasingly being applied to other domains such as computer vision.
- Convolutional Neural Networks (CNNs) are a type of large neural network architecture that are particularly effective for image and video recognition tasks.
- These can be expensive models though. So, unless you need large computation, its best to chose simpler models with less cost!

### All the packages used

- pip install pstat joblib memory-profiler numpy scikit-learn

### Github Repo:

https://github.com/XFactor-Consultants/pluralsight-machine-Learning-model-development

### Stress Testing a Model

- Stress testing a model involves evaluating its performance under extreme or unusual conditions to identify potential weaknesses and ensure it can handle real-world scenarios effectively. This can include testing the model with outliers, noisy data, or edge cases to assess its robustness and reliability. Stress testing helps in understanding the limitations of the model and improving its generalization capabilities.
- Stress test is important because a model barely has entire CPU to itself. There are single threads, and there are multiple models running on the same machine. So, you want to make sure that your model can handle the load and not crash or slow down the system.
![alt text](image.png)

In all of these stress test, we found logistic regression to be the best model. Hence, we will chose it for production


### Deployment of the Model

ONXX: Open Neural Network Exchange (ONNX) is an open format for representing machine learning models. It allows models to be transferred between different frameworks and tools, enabling interoperability and flexibility in deploying machine learning models across various platforms. ONNX supports a wide range of model types, including deep learning, traditional machine learning, and even custom models, making it a versatile choice for model deployment.
    - It is a cross platform format, so you can use it in any language or framework that supports it.
    - It saves the model in a graph format

Pickle: Pickle is a Python module used for serializing and deserializing Python objects. It allows you to save a machine learning model to a file and load it back later for use in predictions. However, using Pickle for model deployment can be risky as it may not be secure and can lead to compatibility issues across different Python versions or environments. It is generally recommended to use more robust and secure formats like ONNX for model deployment.
    - It only works in python
    - Its sensitive to environment changes. If you change the version of python, or the version of the libraries, it may not work anymore.