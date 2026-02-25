# app.py

from flask import Flask, render_template, request, jsonify
from core.ultimate import ultimate_predictor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    text = data.get("text", "")

    result = ultimate_predictor(text, k=3)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)