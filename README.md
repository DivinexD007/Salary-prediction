# Salary-prediction
An end-to-end machine learning project for predicting employee salaries, covering data preprocessing, model training, evaluation, and deployment via a Streamlit web application.




Overview
This project implements an end-to-end machine learning application to predict employee salaries based on years at the company and job performance rating. The goal of this project is to demonstrate the complete machine learning workflow, including data handling, model training, evaluation, and deployment through an interactive web interface.

The application is built using Python and deployed with Streamlit to enable real-time salary predictions.

⸻

Tech Stack
Python
NumPy
Pandas
Scikit-learn
Streamlit
Joblib

⸻

Project Structure

salary-prediction-ml/
├── app.py               Streamlit web application
├── train_model.py       Model training and evaluation
├── Employees.xlsx       Dataset used for training
├── linearmodel.pkl      Trained machine learning model
├── README.md
└── .gitignore

⸻

Machine Learning Workflow
	1.	Load and inspect the employee salary dataset
	2.	Select relevant features such as years at company and job rating
	3.	Train a Linear Regression model
	4.	Evaluate the model’s performance
	5.	Save the trained model using Joblib
	6.	Load the model into the Streamlit application for inference

⸻

How to Run the Project

Step 1: Clone the repository

git clone https://github.com/DivinexD007/Salary-prediction.git
cd salary-prediction-ml

Step 2: Install dependencies

pip install -r requirements.txt

Step 3: Run the Streamlit application

streamlit run app.py

⸻

Sample Input

Years at company: 5
Job rating: 4.0

⸻

Output

The application displays the predicted salary formatted for readability.

⸻

Future Improvements

Add more predictive features such as education, department, and total experience
Introduce preprocessing pipelines for better data handling
Add model explainability and feature importance
Improve evaluation metrics and validation
Deploy the application using Streamlit Cloud or Docker

⸻

Author

Tejas