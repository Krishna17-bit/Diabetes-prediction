**Diabetes Prediction Using Machine Learning and Web Application**

**Project Overview**

This project focuses on predicting whether a patient has diabetes or not based on medical input data. The project includes:

*   A Jupyter Notebook for data analysis and model training.
    
*   A Python-based web application that allows users to input medical data and receive a diabetes prediction.
    

**Repository Contents**

*   **diabetes-prediction.ipynb** - Jupyter Notebook for analyzing data, training the machine learning model, and evaluating the results.
    
*   **app.py** - The web application script, built using Flask, which takes input data from users and returns a prediction.
    

**Installation and Setup**

To set up the project locally, follow the steps below:

**1\. Clone the Repository**
Run the following commands in your terminal:

git clone https://github.com/Krishna17-bit/Diabetes-prediction  

**2\. Install Required Packages**Use pip to install the necessary dependencies:

pip install -r requirements.txt 

**3\. Running the Data Analysis**Open the diabetes-prediction.ipynb notebook in Jupyter Notebook and run all cells to:

*   Load and preprocess the diabetes dataset.
    
*   Train a machine learning model (e.g., Logistic Regression, Decision Tree, or any other).
    
*   Evaluate the model's accuracy.
    

**4\. Launching the Web Application**Run the app.py file to start the web application:
python app.py   `

Open your browser and go to http://127.0.0.1:5000 to access the application. Users can input medical data such as glucose levels, blood pressure, BMI, etc., and get a prediction on whether they might have diabetes.

**Usage**

*   **Data Analysis**: Use the Jupyter Notebook to understand the data, build, and evaluate the model.
    
*   **Web Application**: Use the web app to input data and get real-time predictions.
