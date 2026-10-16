# Gold Price Prediction Using Python and Machine Learning

## 1. Project Overview

This project focuses on analyzing historical financial market data and predicting gold prices using Machine Learning techniques. Python is used for data processing, analysis, visualization, and model development.

The project includes a Streamlit application (`app.py`) to provide an interactive interface for the prediction workflow.

## 2. Business Problem

Gold prices are influenced by several financial and market-related factors. Understanding historical price patterns can help users explore how gold prices have changed over time.

This project demonstrates how historical data and Machine Learning can be used to build a gold price prediction system.

## 3. Project Objectives

- Analyze historical financial market data.
- Explore patterns and relationships in the dataset.
- Prepare data for Machine Learning.
- Build a Linear Regression model for prediction.
- Evaluate model performance using Mean Squared Error (MSE).
- Develop an interactive application using Streamlit.

## 4. Dataset

**Dataset File:** `FINAL_USO.csv`

The dataset contains historical financial market data used in the project.

Pandas is used to load and process the dataset. The relevant features are selected based on the implementation in the Python code.

## 5. Tools and Technologies

- **Python** — Programming and analysis
- **Pandas** — Data loading and manipulation
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Scikit-learn** — Machine Learning
- **Linear Regression** — Prediction algorithm
- **Streamlit** — Interactive application

## 6. Project Workflow

1. Load the historical dataset.
2. Explore the data and understand its structure.
3. Prepare the required data for modelling.
4. Analyze patterns and visualize relevant information.
5. Train the Linear Regression model.
6. Generate predictions using the model.
7. Evaluate prediction errors using Mean Squared Error.
8. Use the Streamlit application to interact with the project.

## 7. Model Evaluation

Mean Squared Error (MSE) is used to measure the average squared difference between actual and predicted values.

The evaluation result depends on the selected features, data preparation, and model configuration. No specific accuracy or performance score is claimed here because it must be taken from the actual model output.

## 8. Key Learnings

- Data loading and manipulation with Pandas.
- Numerical data handling with NumPy.
- Data visualization using Matplotlib.
- Applying Linear Regression to a prediction problem.
- Evaluating predictions using MSE.
- Organizing a Python project with requirements and documentation.
- Developing an interactive interface with Streamlit.

## 9. Project Structure

```text
Gold-Price-Prediction/
│
├── FINAL_USO.csv
├── app.py
├── requirements.txt
└── README.md
```

## 10. How to Run the Project

Clone the repository:

```bash
git clone https://github.com/harmeet-data-analytics/Gold-Price-Prediction.git
```

Move into the project folder:

```bash
cd Gold-Price-Prediction
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 11. Future Improvements

- Experiment with additional Machine Learning algorithms.
- Compare model performance using appropriate evaluation metrics.
- Improve feature selection and model evaluation.
- Enhance the interactive dashboard and visualizations.

## 12. Author

**Harmeet Kaur**

B.Tech Electronics and Communication Engineering Student

GitHub: [harmeet-data-analytics](https://github.com/harmeet-data-analytics)
