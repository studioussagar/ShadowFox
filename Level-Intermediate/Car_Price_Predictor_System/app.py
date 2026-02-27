from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join("model", "car_price_model.pkl")
model = joblib.load(model_path)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ----- Numerical Inputs -----
        present_price_rupees = float(request.form['present_price'])
        kms_driven = float(request.form['kms_driven'])
        car_age = int(request.form['car_age'])
        owner = int(request.form['owner'])

        # Convert rupees to lakhs (MODEL EXPECTS LAKHS)
        present_price = present_price_rupees / 100000

        # ----- Categorical Inputs -----
        fuel_type = request.form['fuel_type']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']

        # Encoding (must match training)
        fuel_diesel = 1 if fuel_type == "Diesel" else 0
        fuel_petrol = 1 if fuel_type == "Petrol" else 0

        seller_individual = 1 if seller_type == "Individual" else 0
        transmission_manual = 1 if transmission == "Manual" else 0

        features = np.array([[present_price,
                              kms_driven,
                              owner,
                              car_age,
                              fuel_diesel,
                              fuel_petrol,
                              seller_individual,
                              transmission_manual]])

        prediction_lakhs = model.predict(features)[0]
        prediction_rupees = prediction_lakhs * 100000

        prediction_rupees = round(prediction_rupees, 2)

        return render_template("index.html",
                               prediction_text=f"Estimated Resale Price: ₹ {prediction_rupees:,.0f}",form_data=request.form)

    except Exception:
        return render_template("index.html",
                               prediction_text="Invalid input. Please check all fields.",form_data=request.form)


if __name__ == "__main__":
    app.run(debug=True)