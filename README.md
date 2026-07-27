# Supervised Learning Algorithms Implementation

## Project Overview

This project focuses on the implementation and evaluation of supervised machine learning algorithms using Python and Scikit-learn. The objective of this project was to understand the working principles of different supervised learning models, train them on suitable datasets, and evaluate their performance using appropriate evaluation metrics.

Three machine learning algorithms were implemented:

- Linear Regression for predicting continuous numerical values.
- Logistic Regression for binary classification problems.
- Decision Tree Classifier for classification-based predictions.

Synthetic datasets were generated using Scikit-learn for both regression and classification tasks. The models were trained, tested, and evaluated to compare their performance and understand their practical applications.


## Algorithms Implemented

### Linear Regression

Linear Regression is a supervised learning algorithm used for predicting continuous values by finding the relationship between input features and the target variable.

The model was evaluated using:
- Mean Squared Error (MSE)
- R-squared (R²) Score


### Logistic Regression

Logistic Regression is a classification algorithm used to predict the probability of a class label. It was implemented for binary classification using the generated classification dataset.

The model was evaluated using:
- Accuracy
- Precision
- Recall
- Confusion Matrix


### Decision Tree Classifier

Decision Tree is a supervised learning algorithm that makes predictions by learning decision rules from the training data. It was implemented and evaluated on the same classification dataset used for Logistic Regression.

The model was evaluated using:
- Accuracy
- Precision
- Recall
- Confusion Matrix


## Dataset Description

Two synthetic datasets were created using Scikit-learn:

### Regression Dataset

The regression dataset was generated using the `make_regression` function. It contains 500 samples with 5 input features and a continuous target variable. This dataset was used for training and evaluating the Linear Regression model.

### Classification Dataset

The classification dataset was generated using the `make_classification` function. It contains 500 samples with 5 input features and two target classes (0 and 1). This dataset was used for implementing Logistic Regression and Decision Tree models.




## Installation and Setup

### Prerequisites

Make sure Python is installed on your system.

Required Python libraries:
- Pandas
- NumPy
- Scikit-learn


### Installing Dependencies

Clone the repository and navigate to the project directory.

Install the required libraries using:
pip install -r requirements.txt


## Running the Project

To run the Linear Regression model:
python src/linear_regression.py

To run the Logistic Regression and Decision Tree models:
python src/classification_models.py


## Results Summary

### Linear Regression

The Linear Regression model achieved the following results:

- Mean Squared Error (MSE): 239.23
- R-squared Score: 0.980

The high R-squared score indicates that the model was able to explain approximately 98% of the variation in the target variable.


### Logistic Regression

The Logistic Regression model achieved:

- Accuracy: 0.90
- Precision: 0.9348
- Recall: 0.86

The model showed good classification performance with higher precision compared to the Decision Tree classifier.


### Decision Tree Classifier

The Decision Tree model achieved:

- Accuracy: 0.86
- Precision: 0.86
- Recall: 0.86


## Key Findings

- Linear Regression performed effectively for predicting continuous values.
- Logistic Regression provided better classification performance compared to the Decision Tree model on the generated dataset.
- Different machine learning algorithms perform differently depending on the type of problem, dataset characteristics, and evaluation criteria.


## Conclusion

This project provided practical experience in implementing supervised learning algorithms, preparing datasets, training machine learning models, and evaluating their performance.

The implementation helped in understanding the differences between regression and classification algorithms and their real-world applications.




