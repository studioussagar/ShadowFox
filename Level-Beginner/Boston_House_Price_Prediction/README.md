# 🏠 Boston House Price Prediction

This project builds a complete Machine Learning pipeline to predict
housing prices using the Boston Housing dataset.

The goal was not only to train a model, but to understand the
**end-to-end workflow** followed in real ML systems --- from data
inspection to model comparison and finally saving the best model for
reuse.

------------------------------------------------------------------------

## 🚀 What I Focused On

Instead of jumping directly to complex algorithms, I followed a
step-by-step approach:

-   Understand the dataset\
-   Clean missing values\
-   Build a simple baseline\
-   Improve it\
-   Compare multiple models\
-   Save the best performer

This mirrors how real-world ML development usually happens.

------------------------------------------------------------------------

## 🧠 Problem Type

This is a **supervised regression** problem.

Given features such as crime rate, number of rooms, tax rate, etc., the
model predicts the **median house value (MEDV)**.

------------------------------------------------------------------------

## 🏗 Workflow Followed

1.  Load and inspect data\
2.  Handle missing values using mean imputation\
3.  Split features and target\
4.  Create training and testing datasets\
5.  Train baseline **Linear Regression**\
6.  Improve with **feature scaling**\
7.  Train **Random Forest** as a more powerful model\
8.  Evaluate using **MSE** and **R² score**\
9.  Compare results\
10. Save the best model

------------------------------------------------------------------------

## 📊 Model Comparison

Linear Regression provides a strong and interpretable starting point.

Random Forest typically performs better because it can capture complex
and non-linear relationships between housing features.

The final decision is made based on evaluation metrics rather than
individual predictions.

------------------------------------------------------------------------

## 📂 Project Structure

    Boston-House-Price/
    │
    ├── data/                  # dataset  
    ├── notebooks/             # experimentation & learning  
    ├── src/                   # reusable training script  
    ├── models/                # saved model files  
    ├── requirements.txt  
    └── README.md  

------------------------------------------------------------------------

## ▶️ How to Run

From the project root:

``` bash
python src/train.py
```

This will: - preprocess data\
- train models\
- print evaluation metrics\
- save the best model

------------------------------------------------------------------------

## 💾 Saved Models

    models/
       ├── boston_model_best.pkl
       └── boston_model_scaler.pkl

These allow predictions later **without retraining**.

------------------------------------------------------------------------

## 🧰 Tools & Libraries

-   Python\
-   pandas\
-   numpy\
-   scikit-learn\
-   matplotlib\
-   seaborn\
-   joblib

------------------------------------------------------------------------

## 🎯 Key Learning Outcomes

Through this project, I learned:

-   how regression models are built and evaluated\
-   why baseline models are important\
-   how feature scaling affects learning\
-   how ensemble methods improve accuracy\
-   how to transition from notebooks → reusable scripts\
-   how trained models are persisted for deployment

------------------------------------------------------------------------

## 🔮 Possible Extensions

There are many directions to extend this work:

-   hyperparameter tuning\
-   cross validation\
-   feature importance analysis\
-   building an API for live predictions\
-   experiment tracking

------------------------------------------------------------------------

## 👨‍💻 About This Project

This is part of my journey from beginner toward building
production-ready AI/ML systems.\
The emphasis is on **clarity, reproducibility, and understanding**, not
just accuracy.
