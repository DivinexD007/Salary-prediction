# Import pandas for data loading and manipulation
import pandas as pd

# Import matplotlib for potential data visualization (not used further here)
import matplotlib.pyplot as plt

# Load the employee dataset from an Excel file
# This dataset contains employee details such as years at company,
# job performance rating, and annual salary
data = pd.read_excel("/Volumes/Personal/Python/Salary Prediction/Employees.xlsx")

# Display the first two rows of the dataset to verify successful loading
print(data.head(2))


# Select independent variables (features) used for prediction
# Years: Number of years the employee has been with the company
# Job Rate: Performance rating of the employee
X = data[["Years", "Job Rate"]]

# Select the dependent variable (target)
# Annual Salary is the value we want the model to predict
y = data["Annual Salary"]

# Import utility to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing subsets
# 80% of data is used for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Print the number of samples in the training target set
print(len(y_train))

# Print the number of samples in the test feature set
print(len(X_test))


# Import the Linear Regression model from scikit-learn
from sklearn.linear_model import LinearRegression

# Initialize the Linear Regression model
lr = LinearRegression()

# Train the model using the training data
lr.fit(X_train, y_train)

# Generate salary predictions using the test feature set
predslr = lr.predict(X_test)

# Import Mean Absolute Error to evaluate model performance
from sklearn.metrics import mean_absolute_error

# Calculate the mean absolute error between predictions and actual salaries
# This metric represents the average absolute difference between predicted
# and actual salary values
mean_absolute_error(predslr, y_test)

# Import joblib to save the trained model to disk
import joblib

# Save the trained Linear Regression model as a pickle file
# This model file can later be loaded and used for predictions in the Streamlit app
joblib.dump(lr, "linearmodel.pkl")