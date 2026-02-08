# ==============================
# Boston House Price Training
# ==============================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("../Dataset/HousingData.csv")



# ==============================
# Data Cleaning
# ==============================
df = df.fillna(df.mean(numeric_only=True))


# ==============================
# Feature / Target Split
# ==============================
X = df.drop("MEDV", axis=1)
y = df["MEDV"]


# ==============================
# Train/Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# Baseline Model – Linear Regression
# ==============================
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)


# ==============================
# Improvement – Scaling + Linear
# ==============================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr_scaled = LinearRegression()
lr_scaled.fit(X_train_scaled, y_train)

lr_scaled_pred = lr_scaled.predict(X_test_scaled)
lr_scaled_r2 = r2_score(y_test, lr_scaled_pred)


# ==============================
# Advanced Model – Random Forest
# ==============================
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_mse = mean_squared_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)


# ==============================
# Final Comparison
# ==============================
print("====== Model Performance ======")
print(f"Linear R2: {lr_r2}")
print(f"Scaled Linear R2: {lr_scaled_r2}")
print(f"Random Forest R2: {rf_r2}")


# ==============================
# Save Best Model
# ==============================
joblib.dump(rf, "boston_model_best.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Training complete. Best model saved.")
