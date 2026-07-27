import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X, y = make_regression(
    n_samples=500,
    n_features=5,
    noise=15,
    random_state=42
)

regression_data = pd.DataFrame(
    X,
    columns=["Feature_1", "Feature_2", "Feature_3", "Feature_4", "Feature_5"]
)

regression_data["Target"] = y
X = regression_data.drop("Target", axis=1)
y = regression_data["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

print(regression_data.head())