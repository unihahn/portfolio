## Titanic Survival Prediction Model

This project implements a machine learning model to predict passenger survival on the Titanic, using the dataset from the Kaggle Titanic - Machine Learning from Disaster competition ([https://www.kaggle.com/competitions/titanic](https://www.kaggle.com/competitions/titanic)).

### Project Overview

This project aims to predict passenger survival on the Titanic using the provided dataset. The analysis includes data loading, exploration, and the development of a predictive model using a Random Forest classifier.

### Data Acquisition and Exploration

The training and test datasets were downloaded from the Kaggle competition. Pandas was used to load and explore the data.  Initial exploration included examining the data's structure, displaying the first few rows, and calculating survival rates for men and women.

### Model Development

A Random Forest Classifier was used to predict survival. The following features were selected for the model:

*   Pclass (Passenger Class)
*   Sex
*   SibSp (Number of siblings/spouses aboard)
*   Parch (Number of parents/children aboard)

One-hot encoding was applied to the categorical features ('Sex') using `pd.get_dummies()`.  The model was trained on the training data and used to predict survival on the test data.

### Model Training and Evaluation

A Random Forest Classifier with 100 estimators and a maximum depth of 5 was trained on the training data. The `random_state` was set for reproducibility.  The model's performance was evaluated implicitly through the Kaggle competition score upon submission. 

### Project Deliverables

*   `tragic-titanic.ipynb`: Contains the code for data loading, exploration, feature engineering, model training, and prediction.
*   `submission.csv`: The CSV file containing the predictions for the test dataset, ready for submission to Kaggle.

### How to Run the Code

1.  Download the `train.csv` and `test.csv` datasets from the Kaggle Titanic competition ([https://www.kaggle.com/competitions/titanic](https://www.kaggle.com/competitions/titanic)). Place the CSV files within a folder called `input/titanic` in the same directory as the notebook.
2.  Open the Jupyter Notebook `titanic_model.ipynb`.
3.  Run the cells in the notebook.  The `submission.csv` file will be created in the same directory as the notebook.

