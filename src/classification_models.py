import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    random_state=42
)
classification_data = pd.DataFrame(
    X,
    columns=["Feature_1", "Feature_2", "Feature_3", "Feature_4", "Feature_5"]
)

classification_data["Target"] = y
X = classification_data.drop("Target", axis=1)
y = classification_data["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
logistic_model = LogisticRegression()

logistic_model.fit(X_train, y_train)
tree_model = DecisionTreeClassifier()

tree_model.fit(X_train, y_train)
logistic_predictions = logistic_model.predict(X_test)

tree_predictions = tree_model.predict(X_test)
print("Logistic Regression Results")
print("Accuracy:", accuracy_score(y_test, logistic_predictions))
print("Precision:", precision_score(y_test, logistic_predictions))
print("Recall:", recall_score(y_test, logistic_predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, logistic_predictions))


print("\nDecision Tree Results")
print("Accuracy:", accuracy_score(y_test, tree_predictions))
print("Precision:", precision_score(y_test, tree_predictions))
print("Recall:", recall_score(y_test, tree_predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, tree_predictions))
print(classification_data.head())