Salary Prediction System – End-to-End Machine Learning Application

Overview
This project implements an end-to-end machine learning application to predict employee salaries based on years at the company and job performance rating. The objective is to demonstrate the complete machine learning lifecycle, including data preprocessing, model training, evaluation, visualization, and deployment through an interactive Streamlit web application.

The application is built using Python and scikit-learn, with Streamlit used to provide a real-time inference interface.

⸻

Tech Stack
Python
NumPy
Pandas
Scikit-learn
Streamlit
Joblib
Matplotlib

⸻

Project Structure

salary-prediction-ml/
├── app.py               Streamlit web application for inference
├── train_model.py       Model training, evaluation, and visualization
├── Employees.xlsx       Dataset used for training and testing
├── linearmodel.pkl      Trained machine learning model
├── README.md
└── .gitignore

⸻

Machine Learning Workflow
	1.	Load and inspect the employee salary dataset
	2.	Select relevant features (years at company, job performance rating)
	3.	Split the data into training and test sets
	4.	Train a Linear Regression model
	5.	Evaluate the model using standard regression metrics
	6.	Visualize model performance using an actual vs predicted salary plot
	7.	Save the trained model using Joblib
	8.	Deploy the model in a Streamlit application for real-time predictions

⸻

Model Performance

The Linear Regression model was evaluated on a held-out test dataset using standard regression metrics.
	•	Mean Absolute Error (MAE): indicates the average absolute difference between predicted and actual salaries
	•	Root Mean Squared Error (RMSE): penalizes larger prediction errors
	•	R² Score: measures the proportion of variance explained by the model

A scatter plot comparing actual salaries versus predicted salaries is used to visually assess model performance and prediction accuracy.

These metrics are computed offline during training and remain constant unless the model is retrained.

⸻

Visualization

The training script generates an Actual vs Predicted Salary scatter plot to assess how closely predictions align with real salary values. This visualization helps identify underfitting, overfitting, and systematic prediction errors.

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

The application displays the predicted salary value formatted for readability. Model performance metrics are displayed for reference, based on offline evaluation.

⸻

Future Improvements

Add additional predictive features such as education level, department, and total experience
Introduce preprocessing pipelines for improved data handling and scalability
Add model explainability and feature importance analysis
Enhance evaluation using cross-validation
Deploy the application using Streamlit Cloud or Docker

⸻

Author

Tejas
