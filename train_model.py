
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("/Volumes/Personal/Python/Salary Prediction/Employees.xlsx")
print(data.head(2))


X = data[["Years", "Job Rate"]]
y = data["Annual Salary"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

print(len(y_train))
print(len(X_test))

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)

predslr = lr.predict(X_test)

from sklearn.metrics import mean_absolute_error

mean_absolute_error(predslr, y_test)

import joblib
joblib.dump(lr, "linearmodel.pkl")


