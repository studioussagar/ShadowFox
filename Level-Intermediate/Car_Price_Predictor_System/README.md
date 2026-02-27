# 🚗 Car Resale Price Predictor

A production-ready Machine Learning web application that predicts the resale price of a car based on user-provided specifications.

The system uses a Random Forest Regression model trained on historical car sales data and provides real-time price predictions through a Flask-based web interface.

---

## 📌 Project Overview

This project implements a supervised regression model to estimate the selling price of used cars using key vehicle attributes such as:

- Original showroom price
- Years of usage
- Kilometers driven
- Fuel type
- Seller type (Dealer/Individual)
- Transmission type
- Number of previous owners

The application converts user inputs into the appropriate feature format, performs prediction using a trained ML model, and displays the estimated resale value in Indian Rupees.

---

## 🎯 Objectives

- Build a robust regression model for car resale price prediction
- Perform feature engineering and categorical encoding
- Evaluate model performance using R², MAE, and MSE
- Deploy the trained model using Flask
- Create a user-friendly production-ready web interface

---

## 🧠 Machine Learning Model

- Algorithm: Random Forest Regressor
- Test R² Score: ~0.96
- Evaluation Metrics:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

Feature importance analysis revealed:

- **Present_Price** is the most influential feature (~88%)
- Car age and kilometers driven significantly affect depreciation
- Fuel type, seller type, and ownership have minor impact in this dataset

---

## 🏗 Project Structure


car-price-prediction/
│
├── app.py
├── model/
│ └── car_price_model.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd car-price-prediction
2️⃣ Create virtual environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
python app.py

Open in browser:

http://127.0.0.1:5000
🚀 Production Deployment

For production deployment (Render, Railway, etc.), use:

gunicorn app:app
🔍 How It Works

User inputs car details in Rupees.

Backend converts price to Lakhs (model training format).

Features are encoded to match training data.

Random Forest model predicts resale price.

Output is converted back to Rupees and displayed.

💡 Business Insights

Resale price is strongly dependent on original showroom price.

Depreciation is significantly influenced by vehicle age.

Mileage moderately affects resale value.

Fuel type and ownership history have relatively smaller impact in this dataset.

📚 Technologies Used

Python

Flask

Scikit-learn

NumPy

HTML/CSS

Joblib

📈 Future Improvements

Add API endpoint for external integration

Implement cross-validation

Add model comparison (Linear Regression vs Gradient Boosting)

Improve UI responsiveness

Deploy to cloud platform

👨‍💻 Sagar Samadder

Developed as a Machine Learning deployment project demonstrating end-to-end ML pipeline implementation.