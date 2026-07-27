# Supervised Learning Algorithms Report

## Introduction

This report explains the implementation and evaluation of three supervised learning algorithms: Linear Regression, Logistic Regression, and Decision Tree. The main purpose of this project was to understand how different machine learning algorithms work and how their performance can be measured on different types of datasets.

For this project, synthetic datasets were created for both regression and classification tasks. Linear Regression was used to predict continuous values, while Logistic Regression and Decision Tree models were used for classification.

The models were trained and tested using Python libraries such as Scikit-learn and Pandas. Their performance was evaluated using suitable evaluation metrics like Mean Squared Error (MSE), R-squared score, accuracy, precision, recall, and confusion matrix.

## Dataset Description

Two synthetic datasets were generated using Scikit-learn for this project.

### Regression Dataset

The regression dataset was created using the `make_regression` function. It contains 500 samples with 5 input features and a continuous target variable. This dataset was used to train and evaluate the Linear Regression model.

### Classification Dataset

The classification dataset was created using the `make_classification` function. It contains 500 samples with 5 input features and a binary target variable with two classes (0 and 1). This dataset was used for implementing Logistic Regression and Decision Tree classification models.

## Key Assumptions of Algorithms

### Linear Regression

Linear Regression works based on the assumption that there is a linear relationship between the input features and the target variable. It also assumes that the observations are independent, the errors have constant variance, and the features do not have strong multicollinearity.

### Logistic Regression

Logistic Regression assumes that the observations are independent and that there is a linear relationship between the input features and the log-odds of the output classes. It also works best when there is low multicollinearity between features.

### Decision Tree

Decision Trees do not require assumptions about linear relationships in the data. However, they assume that the available features are useful for making decisions. They can also overfit the training data if the tree grows too complex.

## Algorithm Implementation

### 1. Linear Regression

Linear Regression was implemented to predict a continuous target value from the regression dataset. The dataset was divided into training and testing sets using an 80:20 split. The model was trained on the training data and evaluated using Mean Squared Error (MSE) and R-squared score.

### 2. Logistic Regression

Logistic Regression was implemented as a classification model to predict the class labels of the classification dataset. The model was trained using the training data and evaluated using accuracy, precision, recall, and confusion matrix.

### 3. Decision Tree Classifier

A Decision Tree classifier was implemented for the classification task. The model learns decision rules from the training data and predicts the target classes. Its performance was evaluated using accuracy, precision, recall, and confusion matrix.

## Model Results and Performance

### Linear Regression Results

The Linear Regression model was evaluated using Mean Squared Error (MSE) and R-squared score.

- Mean Squared Error (MSE): 239.23
- R-squared Score: 0.980

The R-squared value shows that the model was able to explain approximately 98% of the variation in the target variable, indicating good prediction performance.

### Classification Model Results

#### Logistic Regression

The Logistic Regression model achieved the following results:

- Accuracy: 0.90
- Precision: 0.9348
- Recall: 0.86

Confusion Matrix:

```text
[[47  3]
 [ 7 43]]
```


#### Decision Tree Classifier

The Decision Tree model achieved the following results:

- Accuracy: 0.86
- Precision: 0.86
- Recall: 0.86

Confusion Matrix:

```text
[[43  7]
 [ 7 43]]
```
## Algorithm Comparison

The three algorithms used in this project have different strengths and are suitable for different types of problems.

| Algorithm | Type | Main Purpose | Evaluation Metrics |
|-----------|------|--------------|-------------------|
| Linear Regression | Regression | Predict continuous values | MSE, R-squared Score |
| Logistic Regression | Classification | Predict class labels | Accuracy, Precision, Recall, Confusion Matrix |
| Decision Tree | Classification | Make predictions using decision rules | Accuracy, Precision, Recall, Confusion Matrix |

Based on the results, Linear Regression performed well on the regression dataset with an R-squared score of 0.980. Among the classification models, Logistic Regression achieved better performance compared to the Decision Tree classifier, with higher accuracy and precision.

However, the choice of algorithm depends on the problem requirements, dataset characteristics, and the type of output that needs to be predicted.

## Common Use Cases

### Linear Regression
Linear Regression is commonly used when the goal is to predict a continuous value. Some real-world applications include:
- House price prediction
- Sales forecasting
- Salary prediction
- Weather and temperature prediction

### Logistic Regression
Logistic Regression is used for classification problems where the output belongs to different categories. Common applications include:
- Spam email detection
- Disease prediction
- Customer churn prediction
- Fraud detection

### Decision Tree
Decision Trees are useful for making decisions based on different conditions and rules. Common applications include:
- Loan approval systems
- Medical diagnosis
- Customer segmentation
- Credit risk analysis


## Conclusion

In this project, three supervised learning algorithms were implemented and evaluated. Linear Regression successfully predicted continuous values, while Logistic Regression and Decision Tree models were used for classification tasks.

The results showed that Logistic Regression performed better than the Decision Tree classifier on the generated classification dataset. Linear Regression also provided strong performance with a high R-squared score.

This project helped in understanding the working principles, implementation process, and evaluation methods of different supervised learning algorithms.